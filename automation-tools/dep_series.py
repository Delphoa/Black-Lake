from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


ALLOWED_DEP_CLASSES = ("DEP-A", "DEP-E", "DEP-R")
SERIES_CAPACITY = 1000
SERIES_NAME_FORMAT = "Series %03d"
ASSIGNMENT_POLICY = "append_only_ordinal_v1"
INITIAL_ORDERING = "unicode_casefold_then_exact_dep_name"
MAP_RELATIVE_TEMPLATE = ".lake-data/{dep_class}/.index/series-map.json"
DEP_NAME_RE = re.compile(r"^DEP-[AER]-\d{8}-.+$")
SERIES_NAME_RE = re.compile(r"^Series ([0-9]{3,})$")
SHA_RE = re.compile(r"^[0-9a-fA-F]{40}(?:[0-9a-fA-F]{24})?$")
WINDOWS_FORBIDDEN_COMPONENT_CHARS = set('<>:"/\\|?*')


class DepSeriesError(RuntimeError):
    def __init__(self, code: str, message: str, *, retryable: bool = False) -> None:
        super().__init__(message)
        self.code = code
        self.retryable = retryable


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        print(
            canonical_json(
                {
                    "passed": False,
                    "error_code": "dep_series_invalid_arguments",
                    "message": message,
                    "retryable": False,
                }
            ),
            end="",
        )
        raise SystemExit(2)


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_dep_class(dep_class: str) -> str:
    if dep_class not in ALLOWED_DEP_CLASSES:
        raise DepSeriesError(
            "dep_series_invalid_class",
            f"unsupported DEP class {dep_class!r}; expected one of {', '.join(ALLOWED_DEP_CLASSES)}",
        )
    return dep_class


def validate_dep_name(dep_name: str, dep_class: str) -> str:
    if not isinstance(dep_name, str) or not dep_name:
        raise DepSeriesError("dep_series_invalid_path", "DEP name must be a non-empty string")
    if dep_name in {".", ".."} or dep_name.endswith((" ", ".")):
        raise DepSeriesError("dep_series_invalid_path", f"unsafe DEP name: {dep_name!r}")
    if any(ord(character) < 32 for character in dep_name):
        raise DepSeriesError("dep_series_invalid_path", "DEP name contains a control character")
    if WINDOWS_FORBIDDEN_COMPONENT_CHARS.intersection(dep_name):
        raise DepSeriesError("dep_series_invalid_path", f"unsafe DEP name: {dep_name!r}")
    if not DEP_NAME_RE.fullmatch(dep_name) or not dep_name.startswith(dep_class + "-"):
        raise DepSeriesError(
            "dep_series_invalid_path",
            f"DEP name {dep_name!r} does not belong to {dep_class}",
        )
    return dep_name


def validate_object_identity(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise DepSeriesError(
            "dep_series_invalid_identity", "object identity must be a non-empty string"
        )
    if any(ord(character) < 32 for character in value):
        raise DepSeriesError(
            "dep_series_invalid_identity", "object identity contains a control character"
        )
    if len(value) > 2048:
        raise DepSeriesError(
            "dep_series_invalid_identity", "object identity exceeds 2,048 characters"
        )
    return value


def validate_repo_relative_path(value: str) -> str:
    if not isinstance(value, str) or not value:
        raise DepSeriesError("dep_series_invalid_path", "repository path must be non-empty")
    if "\\" in value or value.startswith("/") or re.match(r"^[A-Za-z]:", value):
        raise DepSeriesError(
            "dep_series_invalid_path",
            f"repository path must be a forward-slash relative path: {value!r}",
        )
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise DepSeriesError("dep_series_invalid_path", f"unsafe repository path: {value!r}")
    if not path.parts or path.parts[0] != ".lake-data":
        raise DepSeriesError(
            "dep_series_invalid_path", f"DEP repository path must begin with .lake-data/: {value!r}"
        )
    return path.as_posix()


def normalized_key(value: str) -> str:
    return value.replace("\\", "/").casefold()


def series_number_for_ordinal(ordinal: int, capacity: int = SERIES_CAPACITY) -> int:
    if isinstance(ordinal, bool) or not isinstance(ordinal, int) or ordinal < 1:
        raise DepSeriesError(
            "dep_series_invalid_ordinal", "ordinal must be a positive integer"
        )
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity < 1:
        raise DepSeriesError(
            "dep_series_invalid_capacity", "series capacity must be a positive integer"
        )
    return ((ordinal - 1) // capacity) + 1


def series_name(series_number: int) -> str:
    if isinstance(series_number, bool) or not isinstance(series_number, int) or series_number < 1:
        raise DepSeriesError(
            "dep_series_invalid_series", "series number must be a positive integer"
        )
    return SERIES_NAME_FORMAT % series_number


def current_path_for(dep_class: str, dep_name: str, series_number: int) -> str:
    validate_dep_class(dep_class)
    validate_dep_name(dep_name, dep_class)
    return f".lake-data/{dep_class}/{series_name(series_number)}/{dep_name}"


def repository_root(repo: Path) -> Path:
    try:
        resolved = repo.resolve(strict=True)
    except OSError as exc:
        raise DepSeriesError(
            "dep_series_invalid_repository", f"repository root does not exist: {repo}"
        ) from exc
    if not resolved.is_dir():
        raise DepSeriesError(
            "dep_series_invalid_repository", f"repository root is not a directory: {resolved}"
        )
    try:
        completed = subprocess.run(
            ["git", "-C", str(resolved), "rev-parse", "--show-toplevel"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise DepSeriesError(
            "dep_series_invalid_repository", f"path is not a readable Git repository: {resolved}"
        ) from exc
    observed = Path(completed.stdout.strip()).resolve()
    if os.path.normcase(str(observed)) != os.path.normcase(str(resolved)):
        raise DepSeriesError(
            "dep_series_invalid_repository",
            f"--repo must name the Git worktree root exactly; observed root is {observed}",
        )
    return resolved


def observed_head(repo: Path) -> str:
    try:
        completed = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise DepSeriesError(
            "dep_series_invalid_repository", f"cannot read repository HEAD: {repo}"
        ) from exc
    head = completed.stdout.strip()
    if not SHA_RE.fullmatch(head):
        raise DepSeriesError(
            "dep_series_invalid_repository", f"Git returned an invalid HEAD identity: {head!r}"
        )
    return head


def assert_expected_head(repo: Path, expected_head: str) -> str:
    if not SHA_RE.fullmatch(expected_head or ""):
        raise DepSeriesError(
            "dep_series_stale_head", "expected repository head must be a 40- or 64-digit SHA"
        )
    head = observed_head(repo)
    if head.casefold() != expected_head.casefold():
        raise DepSeriesError(
            "dep_series_stale_head",
            f"repository HEAD differs from the caller's expected head: expected {expected_head}, observed {head}",
        )
    return head


def canonical_map_path(repo: Path, dep_class: str) -> Path:
    validate_dep_class(dep_class)
    return repo / Path(*MAP_RELATIVE_TEMPLATE.format(dep_class=dep_class).split("/"))


def load_json_object(path: Path, *, code: str = "dep_series_invalid_map") -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError as exc:
        raise DepSeriesError(code, f"required JSON file is missing: {path}") from exc
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise DepSeriesError(code, f"cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise DepSeriesError(code, f"JSON root must be an object: {path}")
    return value


def require_int(value: Any, field: str, *, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise DepSeriesError(
            "dep_series_invalid_map", f"{field} must be an integer greater than or equal to {minimum}"
        )
    return value


def validate_map_structure(value: dict[str, Any], dep_class: str) -> dict[str, Any]:
    validate_dep_class(dep_class)
    expected_scalars = {
        "schema_version": 1,
        "record_kind": "dep_series_map",
        "dep_class": dep_class,
        "container_path": f".lake-data/{dep_class}",
        "series_capacity": SERIES_CAPACITY,
        "series_name_format": SERIES_NAME_FORMAT,
        "canonical_path_template": "{container_path}/{series_name}/{dep_name}",
        "assignment_policy": ASSIGNMENT_POLICY,
    }
    for field, expected in expected_scalars.items():
        if value.get(field) != expected:
            raise DepSeriesError(
                "dep_series_invalid_map",
                f"map field {field!r} must equal {expected!r}, observed {value.get(field)!r}",
            )

    initialization = value.get("initialization")
    if not isinstance(initialization, dict):
        raise DepSeriesError("dep_series_invalid_map", "initialization must be an object")
    if not SHA_RE.fullmatch(str(initialization.get("source_commit") or "")):
        raise DepSeriesError(
            "dep_series_invalid_map", "initialization.source_commit must be a Git SHA"
        )
    if initialization.get("ordering") != INITIAL_ORDERING:
        raise DepSeriesError(
            "dep_series_invalid_map",
            f"initialization.ordering must equal {INITIAL_ORDERING!r}",
        )

    entries = value.get("entries")
    if not isinstance(entries, list):
        raise DepSeriesError("dep_series_invalid_map", "entries must be an array")
    entry_count = require_int(value.get("entry_count"), "entry_count")
    if entry_count != len(entries):
        raise DepSeriesError(
            "dep_series_invalid_map",
            f"entry_count={entry_count} but entries contains {len(entries)} records",
        )
    if require_int(value.get("next_ordinal"), "next_ordinal", minimum=1) != entry_count + 1:
        raise DepSeriesError(
            "dep_series_invalid_map", "next_ordinal must equal entry_count + 1"
        )
    active_series = require_int(
        value.get("active_series_number"), "active_series_number", minimum=1
    )
    expected_active = series_number_for_ordinal(entry_count) if entry_count else 1
    if active_series != expected_active:
        raise DepSeriesError(
            "dep_series_invalid_map",
            f"active_series_number must be {expected_active} for {entry_count} entries",
        )

    names: dict[str, int] = {}
    identities: dict[str, int] = {}
    paths: dict[str, tuple[int, str]] = {}
    for expected_ordinal, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            raise DepSeriesError(
                "dep_series_invalid_map", f"entry {expected_ordinal} must be an object"
            )
        ordinal = require_int(entry.get("ordinal"), "entry.ordinal", minimum=1)
        if ordinal != expected_ordinal:
            raise DepSeriesError(
                "dep_series_invalid_map",
                f"entries must be contiguous and ordinal-sorted; expected {expected_ordinal}, observed {ordinal}",
            )
        dep_name = validate_dep_name(entry.get("dep_name"), dep_class)
        name_key = normalized_key(dep_name)
        if name_key in names:
            raise DepSeriesError(
                "dep_series_duplicate_name",
                f"DEP name collides with ordinal {names[name_key]}: {dep_name}",
            )
        names[name_key] = ordinal

        identity = validate_object_identity(entry.get("object_identity"))
        identity_key = normalized_key(identity)
        if identity_key in identities:
            raise DepSeriesError(
                "dep_series_duplicate_identity",
                f"object identity collides with ordinal {identities[identity_key]}: {identity}",
            )
        identities[identity_key] = ordinal

        expected_series = series_number_for_ordinal(ordinal)
        if require_int(entry.get("series_number"), "entry.series_number", minimum=1) != expected_series:
            raise DepSeriesError(
                "dep_series_invalid_map",
                f"ordinal {ordinal} must belong to {series_name(expected_series)}",
            )
        expected_path = current_path_for(dep_class, dep_name, expected_series)
        current_path = validate_repo_relative_path(entry.get("current_path"))
        if current_path != expected_path:
            raise DepSeriesError(
                "dep_series_invalid_map",
                f"entry {ordinal} current_path must equal {expected_path!r}",
            )
        prior_paths = entry.get("prior_paths")
        if not isinstance(prior_paths, list):
            raise DepSeriesError(
                "dep_series_invalid_map", f"entry {ordinal} prior_paths must be an array"
            )
        entry_paths = [(current_path, "current_path")]
        entry_paths.extend(
            (validate_repo_relative_path(prior_path), "prior_path")
            for prior_path in prior_paths
        )
        for path_value, path_kind in entry_paths:
            path_key = normalized_key(path_value)
            if path_key in paths:
                prior_ordinal, prior_kind = paths[path_key]
                raise DepSeriesError(
                    "dep_series_path_collision",
                    f"{path_kind} for ordinal {ordinal} collides with {prior_kind} for ordinal {prior_ordinal}: {path_value}",
                )
            paths[path_key] = (ordinal, path_kind)

    series_records = value.get("series")
    if not isinstance(series_records, list):
        raise DepSeriesError("dep_series_invalid_map", "series must be an array")
    expected_series_count = active_series if entry_count else 0
    if len(series_records) != expected_series_count:
        raise DepSeriesError(
            "dep_series_invalid_map",
            f"series must contain {expected_series_count} records, observed {len(series_records)}",
        )
    for expected_number, record in enumerate(series_records, start=1):
        if not isinstance(record, dict):
            raise DepSeriesError(
                "dep_series_invalid_map", f"series record {expected_number} must be an object"
            )
        start = (expected_number - 1) * SERIES_CAPACITY + 1
        expected_count = max(0, min(SERIES_CAPACITY, entry_count - start + 1))
        expected_record = {
            "series_number": expected_number,
            "series_name": series_name(expected_number),
            "capacity_start": start,
            "capacity_end": expected_number * SERIES_CAPACITY,
            "entry_count": expected_count,
            "sealed": expected_number < active_series,
        }
        for field, expected in expected_record.items():
            if record.get(field) != expected:
                raise DepSeriesError(
                    "dep_series_invalid_map",
                    f"series {expected_number} field {field!r} must equal {expected!r}",
                )
    return value


def path_on_disk(repo: Path, relative_path: str) -> Path:
    validated = validate_repo_relative_path(relative_path)
    return repo / Path(*PurePosixPath(validated).parts)


def validate_object_directory(path: Path) -> bool:
    if not path.is_dir() or path.is_symlink():
        return False
    contains_file = False
    for item in path.rglob("*"):
        if item.is_symlink():
            raise DepSeriesError(
                "dep_series_invalid_layout", f"symlinks are forbidden inside DEP objects: {item}"
            )
        if item.is_file():
            contains_file = True
    return contains_file


def validate_map_tree(
    repo: Path,
    dep_class: str,
    value: dict[str, Any],
    *,
    pending_path: str | None = None,
) -> None:
    class_root = repo / ".lake-data" / dep_class
    lake_root = repo / ".lake-data"
    if not class_root.is_dir():
        raise DepSeriesError(
            "dep_series_invalid_layout", f"class container is missing: .lake-data/{dep_class}"
        )

    if lake_root.is_dir():
        root_flat = sorted(
            item.name for item in lake_root.iterdir() if item.name.startswith(dep_class + "-")
        )
        if root_flat:
            raise DepSeriesError(
                "dep_series_invalid_layout",
                f"root-flat {dep_class} objects are forbidden: {root_flat[0]}",
            )

    actual_paths: set[str] = set()
    actual_series: set[str] = set()
    for child in class_root.iterdir():
        if child.name in {".index", "README.md"}:
            continue
        if child.name.startswith(dep_class + "-"):
            raise DepSeriesError(
                "dep_series_invalid_layout",
                f"direct-under-class DEP objects are forbidden: {child.name}",
            )
        match = SERIES_NAME_RE.fullmatch(child.name)
        if not child.is_dir() or child.is_symlink() or match is None:
            raise DepSeriesError(
                "dep_series_invalid_layout",
                f"unexpected class-container entry: .lake-data/{dep_class}/{child.name}",
            )
        number = int(match.group(1))
        if child.name != series_name(number):
            raise DepSeriesError(
                "dep_series_invalid_layout", f"non-canonical Series name: {child.name}"
            )
        children = list(child.iterdir())
        if not children:
            raise DepSeriesError(
                "dep_series_empty_series", f"empty Series directories are forbidden: {child.name}"
            )
        actual_series.add(child.name)
        for object_root in children:
            if (
                not object_root.is_dir()
                or object_root.is_symlink()
                or not object_root.name.startswith(dep_class + "-")
            ):
                raise DepSeriesError(
                    "dep_series_invalid_layout",
                    f"Series directories may contain only {dep_class} object directories: {object_root}",
                )
            validate_dep_name(object_root.name, dep_class)
            if not validate_object_directory(object_root):
                raise DepSeriesError(
                    "dep_series_invalid_layout", f"DEP object directory contains no files: {object_root}"
                )
            actual_paths.add(
                f".lake-data/{dep_class}/{child.name}/{object_root.name}"
            )

    expected_paths = {entry["current_path"] for entry in value["entries"]}
    if pending_path is not None:
        pending_path = validate_repo_relative_path(pending_path)
        expected_paths.add(pending_path)
    if actual_paths != expected_paths:
        missing = sorted(expected_paths - actual_paths)
        extra = sorted(actual_paths - expected_paths)
        raise DepSeriesError(
            "dep_series_map_tree_drift",
            f"map/tree bijection failed; missing={missing[:3]}, extra={extra[:3]}",
        )

    expected_series = {
        PurePosixPath(path).parts[2]
        for path in expected_paths
    }
    if actual_series != expected_series:
        raise DepSeriesError(
            "dep_series_map_tree_drift",
            f"Series directory set differs from mapped paths; expected={sorted(expected_series)}, observed={sorted(actual_series)}",
        )

    for entry in value["entries"]:
        for prior_path in entry["prior_paths"]:
            if path_on_disk(repo, prior_path).exists():
                raise DepSeriesError(
                    "dep_series_invalid_layout",
                    f"prior-path alias still exists in the current tree: {prior_path}",
                )


def load_validated_map(
    repo: Path,
    dep_class: str,
    *,
    pending_path: str | None = None,
) -> tuple[Path, dict[str, Any]]:
    map_path = canonical_map_path(repo, dep_class)
    value = load_json_object(map_path)
    validate_map_structure(value, dep_class)
    validate_map_tree(repo, dep_class, value, pending_path=pending_path)
    return map_path, value


def map_summary(repo: Path, dep_class: str, map_path: Path, value: dict[str, Any]) -> dict[str, Any]:
    return {
        "record_kind": "dep_series_validation_result",
        "dep_class": dep_class,
        "repository_head": observed_head(repo),
        "map_path": map_path.relative_to(repo).as_posix(),
        "map_sha256": sha256_file(map_path),
        "entry_count": value["entry_count"],
        "next_ordinal": value["next_ordinal"],
        "active_series_number": value["active_series_number"],
        "series_count": len(value["series"]),
        "map_tree_bijection": True,
    }


def find_entry(
    entries: Iterable[dict[str, Any]],
    *,
    object_identity: str | None = None,
    path: str | None = None,
) -> tuple[dict[str, Any], str]:
    supplied = sum(selector is not None for selector in (object_identity, path))
    if supplied != 1:
        raise DepSeriesError(
            "dep_series_invalid_arguments",
            "resolve requires exactly one of object_identity or path",
        )
    if object_identity is not None:
        key = normalized_key(validate_object_identity(object_identity))
        matches = [entry for entry in entries if normalized_key(entry["object_identity"]) == key]
        matched_by = "object_identity"
    elif path is not None:
        validated_path = validate_repo_relative_path(path)
        key = normalized_key(validated_path)
        matches = [entry for entry in entries if normalized_key(entry["current_path"]) == key]
        matched_by = "current_path"
        if not matches:
            matches = [
                entry
                for entry in entries
                if any(normalized_key(alias) == key for alias in entry["prior_paths"])
            ]
            matched_by = "prior_path"
    if not matches:
        raise DepSeriesError("dep_series_not_found", "no mapped DEP object matches the selector")
    if len(matches) != 1:
        raise DepSeriesError(
            "dep_series_ambiguous_selector", "selector maps to more than one DEP object"
        )
    return copy.deepcopy(matches[0]), matched_by


def validate_command(repo_arg: Path, dep_class: str) -> dict[str, Any]:
    repo = repository_root(repo_arg)
    map_path, value = load_validated_map(repo, dep_class)
    return map_summary(repo, dep_class, map_path, value)


def resolve_command(
    repo_arg: Path,
    dep_class: str,
    *,
    object_identity: str | None,
    path: str | None,
) -> dict[str, Any]:
    repo = repository_root(repo_arg)
    map_path, value = load_validated_map(repo, dep_class)
    entry, matched_by = find_entry(
        value["entries"],
        object_identity=object_identity,
        path=path,
    )
    return {
        "record_kind": "dep_series_resolution_result",
        "dep_class": dep_class,
        "repository_head": observed_head(repo),
        "map_path": map_path.relative_to(repo).as_posix(),
        "map_sha256": sha256_file(map_path),
        "matched_by": matched_by,
        "entry": entry,
    }


def proposed_entry(
    value: dict[str, Any],
    dep_class: str,
    dep_name: str,
    *,
    object_identity: str | None = None,
    prior_paths: Iterable[str] = (),
) -> tuple[dict[str, Any], bool, int | None]:
    validate_dep_name(dep_name, dep_class)
    if object_identity is None:
        raise DepSeriesError(
            "dep_series_identity_required",
            "allocation requires an explicit stable object identity; DEP names are not identity selectors",
        )
    identity = validate_object_identity(object_identity)
    name_key = normalized_key(dep_name)
    identity_key = normalized_key(identity)
    existing_name = [
        entry for entry in value["entries"] if normalized_key(entry["dep_name"]) == name_key
    ]
    if existing_name:
        if normalized_key(existing_name[0]["object_identity"]) != identity_key:
            raise DepSeriesError(
                "dep_series_duplicate_name",
                f"DEP name is already assigned to another identity: {dep_name}",
            )
        return copy.deepcopy(existing_name[0]), False, None
    if any(normalized_key(entry["object_identity"]) == identity_key for entry in value["entries"]):
        raise DepSeriesError(
            "dep_series_duplicate_identity", f"object identity is already mapped: {identity}"
        )

    ordinal = value["next_ordinal"]
    target_series = series_number_for_ordinal(ordinal)
    current_path = current_path_for(dep_class, dep_name, target_series)
    aliases = [validate_repo_relative_path(alias) for alias in prior_paths]
    occupied_paths = {
        normalized_key(path_value)
        for entry in value["entries"]
        for path_value in [entry["current_path"], *entry["prior_paths"]]
    }
    for path_value in [current_path, *aliases]:
        if normalized_key(path_value) in occupied_paths:
            raise DepSeriesError(
                "dep_series_path_collision", f"new entry path is already mapped: {path_value}"
            )
        occupied_paths.add(normalized_key(path_value))
    entry = {
        "ordinal": ordinal,
        "dep_name": dep_name,
        "object_identity": identity,
        "series_number": target_series,
        "current_path": current_path,
        "prior_paths": aliases,
    }
    creates_new_series = target_series > value["active_series_number"] or value["entry_count"] == 0
    sealed_series = target_series - 1 if creates_new_series and target_series > 1 else None
    return entry, creates_new_series, sealed_series


def plan_allocation_command(
    repo_arg: Path,
    dep_class: str,
    dep_name: str,
    expected_head: str,
    *,
    object_identity: str | None,
    prior_paths: Iterable[str],
) -> dict[str, Any]:
    repo = repository_root(repo_arg)
    head = assert_expected_head(repo, expected_head)
    map_path, value = load_validated_map(repo, dep_class)
    entry, creates_new_series, sealed_series = proposed_entry(
        value,
        dep_class,
        dep_name,
        object_identity=object_identity,
        prior_paths=prior_paths,
    )
    allocation_required = entry["ordinal"] == value["next_ordinal"]
    return {
        "record_kind": "dep_series_allocation_plan",
        "dep_class": dep_class,
        "repository_head": head,
        "map_path": map_path.relative_to(repo).as_posix(),
        "map_sha256": sha256_file(map_path),
        "allocation_required": allocation_required,
        "created_new_series": creates_new_series if allocation_required else False,
        "sealed_series_number": sealed_series if allocation_required else None,
        "entry": entry,
        "shared_state_mutated": False,
    }


def verify_deployment_lock(
    lock_path: Path,
    *,
    automation_id: str,
    run_key: str,
) -> tuple[dict[str, Any], str]:
    value = load_json_object(lock_path, code="dep_series_invalid_deployment_lock")
    expected = {
        "record_kind": "family_scoped_mutation_lock",
        "scope": "deployment",
        "automation_id": automation_id,
        "run_key": run_key,
    }
    for field, expected_value in expected.items():
        if value.get(field) != expected_value:
            raise DepSeriesError(
                "dep_series_invalid_deployment_lock",
                f"deployment lock field {field!r} must equal {expected_value!r}",
            )
    return value, sha256_file(lock_path)


def appended_map(value: dict[str, Any], entry: dict[str, Any]) -> dict[str, Any]:
    updated = copy.deepcopy(value)
    target_series = entry["series_number"]
    prior_active = updated["active_series_number"]
    if target_series > prior_active or updated["entry_count"] == 0:
        if updated["series"]:
            updated["series"][-1]["sealed"] = True
        start = (target_series - 1) * SERIES_CAPACITY + 1
        updated["series"].append(
            {
                "series_number": target_series,
                "series_name": series_name(target_series),
                "capacity_start": start,
                "capacity_end": target_series * SERIES_CAPACITY,
                "entry_count": 1,
                "sealed": False,
            }
        )
        updated["active_series_number"] = target_series
    else:
        updated["series"][target_series - 1]["entry_count"] += 1
    updated["entries"].append(copy.deepcopy(entry))
    updated["entry_count"] += 1
    updated["next_ordinal"] += 1
    return updated


def atomic_write_json(path: Path, value: dict[str, Any]) -> str:
    payload = canonical_json(value).encode("utf-8")
    existing_mode = stat.S_IMODE(path.stat().st_mode)
    descriptor, temporary_name = tempfile.mkstemp(prefix=path.name + ".tmp.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, existing_mode)
        os.replace(temporary, path)
    except BaseException:
        try:
            temporary.unlink()
        except OSError:
            pass
        raise
    return sha256_bytes(payload)


def append_entry_command(
    repo_arg: Path,
    dep_class: str,
    dep_name: str,
    expected_head: str,
    lock_path: Path,
    automation_id: str,
    run_key: str,
    *,
    object_identity: str | None,
    prior_paths: Iterable[str],
) -> dict[str, Any]:
    repo = repository_root(repo_arg)
    head = assert_expected_head(repo, expected_head)
    _, lock_sha = verify_deployment_lock(
        lock_path, automation_id=automation_id, run_key=run_key
    )
    map_path = canonical_map_path(repo, dep_class)
    value = load_json_object(map_path)
    validate_map_structure(value, dep_class)
    map_sha_before = sha256_file(map_path)
    entry, creates_new_series, sealed_series = proposed_entry(
        value,
        dep_class,
        dep_name,
        object_identity=object_identity,
        prior_paths=prior_paths,
    )
    if entry["ordinal"] != value["next_ordinal"]:
        raise DepSeriesError(
            "dep_series_duplicate_name",
            "append-entry accepts new objects only; use resolve for an existing assignment",
        )
    candidate_root = path_on_disk(repo, entry["current_path"])
    if not validate_object_directory(candidate_root):
        raise DepSeriesError(
            "dep_series_candidate_missing",
            f"candidate DEP directory must already exist and contain a file: {entry['current_path']}",
        )
    validate_map_tree(repo, dep_class, value, pending_path=entry["current_path"])

    updated = appended_map(value, entry)
    validate_map_structure(updated, dep_class)
    validate_map_tree(repo, dep_class, updated)

    if assert_expected_head(repo, expected_head) != head:
        raise DepSeriesError(
            "dep_series_stale_head", "repository HEAD changed during append-entry"
        )
    _, final_lock_sha = verify_deployment_lock(
        lock_path, automation_id=automation_id, run_key=run_key
    )
    if final_lock_sha != lock_sha:
        raise DepSeriesError(
            "dep_series_concurrent_mutation", "deployment lock changed during append-entry"
        )
    if sha256_file(map_path) != map_sha_before:
        raise DepSeriesError(
            "dep_series_concurrent_mutation", "series map changed during append-entry"
        )

    map_sha_after = atomic_write_json(map_path, updated)
    return {
        "record_kind": "dep_series_append_result",
        "dep_class": dep_class,
        "repository_head": head,
        "map_path": map_path.relative_to(repo).as_posix(),
        "map_sha256_before": map_sha_before,
        "map_sha256_after": map_sha_after,
        "deployment_lock_sha256": lock_sha,
        "created_new_series": creates_new_series,
        "sealed_series_number": sealed_series,
        "entry": entry,
        "map_tree_bijection": True,
    }


def add_repo_and_class(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--class", dest="dep_class", choices=ALLOWED_DEP_CLASSES, required=True)


def add_allocation_arguments(parser: argparse.ArgumentParser) -> None:
    add_repo_and_class(parser)
    parser.add_argument("--dep-name", required=True)
    parser.add_argument("--object-identity", required=True)
    parser.add_argument("--prior-path", action="append", default=[])
    parser.add_argument("--expected-head", required=True)


def build_parser() -> argparse.ArgumentParser:
    parser = JsonArgumentParser(
        description="Resolve, validate, and append authoritative Black Lake DEP Series assignments."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate")
    add_repo_and_class(validate_parser)

    resolve_parser = subparsers.add_parser("resolve")
    add_repo_and_class(resolve_parser)
    selectors = resolve_parser.add_mutually_exclusive_group(required=True)
    selectors.add_argument("--object-identity")
    selectors.add_argument("--path")

    plan_parser = subparsers.add_parser("plan-allocation")
    add_allocation_arguments(plan_parser)

    append_parser = subparsers.add_parser("append-entry")
    add_allocation_arguments(append_parser)
    append_parser.add_argument("--deployment-lock-token", type=Path, required=True)
    append_parser.add_argument("--automation-id", required=True)
    append_parser.add_argument("--run-key", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            result = validate_command(args.repo, args.dep_class)
        elif args.command == "resolve":
            result = resolve_command(
                args.repo,
                args.dep_class,
                object_identity=args.object_identity,
                path=args.path,
            )
        elif args.command == "plan-allocation":
            result = plan_allocation_command(
                args.repo,
                args.dep_class,
                args.dep_name,
                args.expected_head,
                object_identity=args.object_identity,
                prior_paths=args.prior_path,
            )
        else:
            result = append_entry_command(
                args.repo,
                args.dep_class,
                args.dep_name,
                args.expected_head,
                args.deployment_lock_token,
                args.automation_id,
                args.run_key,
                object_identity=args.object_identity,
                prior_paths=args.prior_path,
            )
    except DepSeriesError as exc:
        print(
            canonical_json(
                {
                    "passed": False,
                    "error_code": exc.code,
                    "message": str(exc),
                    "retryable": exc.retryable,
                }
            ),
            end="",
        )
        return 2
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(
            canonical_json(
                {
                    "passed": False,
                    "error_code": "dep_series_io_error",
                    "message": str(exc),
                    "retryable": False,
                }
            ),
            end="",
        )
        return 2
    print(canonical_json({"passed": True, **result}), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
