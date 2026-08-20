from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


MODULE_PATH = Path(__file__).with_name("dep_series.py")
SPEC = importlib.util.spec_from_file_location("dep_series", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class DepSeriesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self._git("init", "--quiet")
        self._git("config", "user.email", "dep-series-tests@example.invalid")
        self._git("config", "user.name", "DEP Series Tests")
        self._git("commit", "--quiet", "--allow-empty", "-m", "fixture base")
        self.lock = self.root / "deployment-lock.json"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _git(self, *args: str) -> str:
        completed = subprocess.run(
            ["git", *args],
            cwd=self.repo,
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()

    @property
    def head(self) -> str:
        return self._git("rev-parse", "HEAD")

    @staticmethod
    def _dep_name(index: int, dep_class: str = "DEP-A") -> str:
        return f"{dep_class}-20260820-Fixture {index:04d}"

    @staticmethod
    def _current_path(dep_class: str, dep_name: str, series_number: int) -> str:
        return f".lake-data/{dep_class}/Series {series_number:03d}/{dep_name}"

    def _write_map(self, count: int, dep_class: str = "DEP-A") -> Path:
        class_root = self.repo / ".lake-data" / dep_class
        entries = []
        for ordinal in range(1, count + 1):
            dep_name = self._dep_name(ordinal, dep_class)
            series_number = ((ordinal - 1) // 1000) + 1
            current_path = self._current_path(dep_class, dep_name, series_number)
            entries.append(
                {
                    "ordinal": ordinal,
                    "dep_name": dep_name,
                    "object_identity": f"{dep_class}/{dep_name}",
                    "series_number": series_number,
                    "current_path": current_path,
                    "prior_paths": [],
                }
            )
            object_root = self.repo / Path(*current_path.split("/"))
            object_root.mkdir(parents=True, exist_ok=True)
            (object_root / "README.md").write_text(
                f"# {dep_name}\n", encoding="utf-8"
            )

        active_series = max(1, ((count - 1) // 1000) + 1) if count else 1
        series = []
        for series_number in range(1, active_series + 1 if count else 1):
            start = (series_number - 1) * 1000 + 1
            series_count = max(0, min(1000, count - start + 1))
            series.append(
                {
                    "series_number": series_number,
                    "series_name": f"Series {series_number:03d}",
                    "capacity_start": start,
                    "capacity_end": series_number * 1000,
                    "entry_count": series_count,
                    "sealed": series_number < active_series,
                }
            )

        value = {
            "schema_version": 1,
            "record_kind": "dep_series_map",
            "dep_class": dep_class,
            "container_path": f".lake-data/{dep_class}",
            "series_capacity": 1000,
            "series_name_format": "Series %03d",
            "canonical_path_template": "{container_path}/{series_name}/{dep_name}",
            "assignment_policy": "append_only_ordinal_v1",
            "initialization": {
                "source_commit": self.head,
                "ordering": "unicode_casefold_then_exact_dep_name",
            },
            "entry_count": count,
            "next_ordinal": count + 1,
            "active_series_number": active_series,
            "series": series,
            "entries": entries,
        }
        map_path = class_root / ".index" / "series-map.json"
        write_json(map_path, value)
        return map_path

    def _write_lock(self, *, scope: str = "deployment") -> None:
        write_json(
            self.lock,
            {
                "schema_version": 2,
                "record_kind": "family_scoped_mutation_lock",
                "scope": scope,
                "automation_id": "test-automation",
                "run_key": "test-run",
                "acquired_at": "2026-08-20T00:00:00+00:00",
                "process_id": 1234,
            },
        )

    def _run_cli(self, *args: str) -> tuple[subprocess.CompletedProcess[str], dict]:
        completed = subprocess.run(
            [sys.executable, str(MODULE_PATH), *args],
            cwd=self.repo,
            capture_output=True,
            text=True,
        )
        self.assertTrue(completed.stdout.strip(), completed.stderr)
        return completed, json.loads(completed.stdout)

    def _append_args(self, dep_name: str, *, object_identity: str | None = None) -> list[str]:
        return [
            "append-entry",
            "--repo",
            str(self.repo),
            "--class",
            "DEP-A",
            "--dep-name",
            dep_name,
            "--object-identity",
            object_identity or f"fixture:{dep_name}",
            "--expected-head",
            self.head,
            "--deployment-lock-token",
            str(self.lock),
            "--automation-id",
            "test-automation",
            "--run-key",
            "test-run",
        ]

    def test_series_number_boundaries(self) -> None:
        expected = {
            999: 1,
            1000: 1,
            1001: 2,
            1999: 2,
            2000: 2,
            2001: 3,
        }
        for ordinal, series_number in expected.items():
            with self.subTest(ordinal=ordinal):
                self.assertEqual(series_number, MODULE.series_number_for_ordinal(ordinal))

    def test_validate_and_resolve_by_identity_current_path_and_prior_path(self) -> None:
        map_path = self._write_map(1)
        value = json.loads(map_path.read_text(encoding="utf-8"))
        value["entries"][0]["prior_paths"] = [
            ".lake-data/DEP-A/DEP-A-20260820-Fixture 0001"
        ]
        write_json(map_path, value)

        completed, result = self._run_cli(
            "validate", "--repo", str(self.repo), "--class", "DEP-A"
        )
        self.assertEqual(0, completed.returncode)
        self.assertTrue(result["passed"])
        self.assertEqual(1, result["entry_count"])

        selectors = [
            ("--object-identity", "DEP-A/DEP-A-20260820-Fixture 0001", "object_identity"),
            (
                "--path",
                ".lake-data/DEP-A/Series 001/DEP-A-20260820-Fixture 0001",
                "current_path",
            ),
            (
                "--path",
                ".lake-data/DEP-A/DEP-A-20260820-Fixture 0001",
                "prior_path",
            ),
        ]
        for option, value, matched_by in selectors:
            with self.subTest(selector=option):
                completed, result = self._run_cli(
                    "resolve",
                    "--repo",
                    str(self.repo),
                    "--class",
                    "DEP-A",
                    option,
                    value,
                )
                self.assertEqual(0, completed.returncode)
                self.assertEqual(matched_by, result["matched_by"])
                self.assertEqual(1, result["entry"]["ordinal"])

    def test_resolve_rejects_bare_dep_name_selector(self) -> None:
        self._write_map(1)

        completed, result = self._run_cli(
            "resolve",
            "--repo",
            str(self.repo),
            "--class",
            "DEP-A",
            "--dep-name",
            self._dep_name(1),
        )

        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_invalid_arguments", result["error_code"])
        self.assertFalse(result["retryable"])

    def test_plan_allocation_reports_existing_or_next_without_mutation(self) -> None:
        map_path = self._write_map(1)
        before = file_sha256(map_path)

        completed, existing = self._run_cli(
            "plan-allocation",
            "--repo",
            str(self.repo),
            "--class",
            "DEP-A",
            "--dep-name",
            self._dep_name(1),
            "--object-identity",
            f"DEP-A/{self._dep_name(1)}",
            "--expected-head",
            self.head,
        )
        self.assertEqual(0, completed.returncode)
        self.assertFalse(existing["allocation_required"])
        self.assertEqual(1, existing["entry"]["ordinal"])

        completed, planned = self._run_cli(
            "plan-allocation",
            "--repo",
            str(self.repo),
            "--class",
            "DEP-A",
            "--dep-name",
            "DEP-A-20260820-New Object",
            "--object-identity",
            "fixture:new-object",
            "--expected-head",
            self.head,
        )
        self.assertEqual(0, completed.returncode)
        self.assertTrue(planned["allocation_required"])
        self.assertEqual(2, planned["entry"]["ordinal"])
        self.assertEqual("fixture:new-object", planned["entry"]["object_identity"])
        self.assertEqual(before, file_sha256(map_path))

    def test_plan_allocation_rejects_basename_only_lookup(self) -> None:
        map_path = self._write_map(1)
        before = file_sha256(map_path)

        completed, result = self._run_cli(
            "plan-allocation",
            "--repo",
            str(self.repo),
            "--class",
            "DEP-A",
            "--dep-name",
            self._dep_name(1),
            "--expected-head",
            self.head,
        )

        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_invalid_arguments", result["error_code"])
        self.assertEqual(before, file_sha256(map_path))

    def test_append_entry_activates_series_two_and_seals_series_one(self) -> None:
        map_path = self._write_map(1000)
        os.chmod(map_path, 0o640)
        original_mode = map_path.stat().st_mode & 0o777
        dep_name = "DEP-A-20260820-First In Series Two"
        object_root = self.repo / ".lake-data" / "DEP-A" / "Series 002" / dep_name
        object_root.mkdir(parents=True)
        (object_root / "README.md").write_text("# First in Series Two\n", encoding="utf-8")
        self._write_lock()

        completed, result = self._run_cli(*self._append_args(dep_name))

        self.assertEqual(0, completed.returncode)
        self.assertTrue(result["passed"])
        self.assertTrue(result["created_new_series"])
        self.assertEqual(1, result["sealed_series_number"])
        value = json.loads(map_path.read_text(encoding="utf-8"))
        self.assertEqual(1002, value["next_ordinal"])
        self.assertEqual(2, value["active_series_number"])
        self.assertTrue(value["series"][0]["sealed"])
        self.assertFalse(value["series"][1]["sealed"])
        self.assertEqual(1, value["series"][1]["entry_count"])
        self.assertEqual(original_mode, map_path.stat().st_mode & 0o777)
        self.assertTrue(object_root.is_dir())
        self.assertEqual([], [path for path in object_root.parent.iterdir() if path.name == ".gitkeep"])

    def test_append_entry_activates_series_three_at_ordinal_2001(self) -> None:
        map_path = self._write_map(2000)
        dep_name = "DEP-A-20260820-First In Series Three"
        object_root = self.repo / ".lake-data" / "DEP-A" / "Series 003" / dep_name
        object_root.mkdir(parents=True)
        (object_root / "README.md").write_text("# First in Series Three\n", encoding="utf-8")
        self._write_lock()

        completed, result = self._run_cli(*self._append_args(dep_name))

        self.assertEqual(0, completed.returncode)
        self.assertTrue(result["created_new_series"])
        self.assertEqual(2, result["sealed_series_number"])
        value = json.loads(map_path.read_text(encoding="utf-8"))
        self.assertEqual(3, value["active_series_number"])
        self.assertTrue(value["series"][1]["sealed"])
        self.assertFalse(value["series"][2]["sealed"])

    def test_append_requires_materialized_nonempty_object_and_never_creates_empty_series(self) -> None:
        map_path = self._write_map(1000)
        before = file_sha256(map_path)
        self._write_lock()
        dep_name = "DEP-A-20260820-Missing Object"

        completed, result = self._run_cli(*self._append_args(dep_name))

        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_candidate_missing", result["error_code"])
        self.assertEqual(before, file_sha256(map_path))
        self.assertFalse((self.repo / ".lake-data" / "DEP-A" / "Series 002").exists())

    def test_append_rejects_manual_filing_in_full_series(self) -> None:
        map_path = self._write_map(1000)
        before = file_sha256(map_path)
        dep_name = "DEP-A-20260820-Wrong Full Series"
        wrong_root = self.repo / ".lake-data" / "DEP-A" / "Series 001" / dep_name
        wrong_root.mkdir(parents=True)
        (wrong_root / "README.md").write_text("# Wrong Series\n", encoding="utf-8")
        self._write_lock()

        completed, result = self._run_cli(*self._append_args(dep_name))

        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_candidate_missing", result["error_code"])
        self.assertEqual(before, file_sha256(map_path))
        self.assertFalse((self.repo / ".lake-data" / "DEP-A" / "Series 002").exists())

    def test_duplicate_dep_name_and_identity_fail_without_mutation(self) -> None:
        map_path = self._write_map(1)
        self._write_lock()
        before = file_sha256(map_path)

        duplicate_name = self._dep_name(1)
        completed, result = self._run_cli(*self._append_args(duplicate_name))
        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_duplicate_name", result["error_code"])
        self.assertEqual(before, file_sha256(map_path))

        new_name = "DEP-A-20260820-New Name Same Identity"
        new_root = self.repo / ".lake-data" / "DEP-A" / "Series 001" / new_name
        new_root.mkdir(parents=True)
        (new_root / "README.md").write_text("# duplicate identity\n", encoding="utf-8")
        completed, result = self._run_cli(
            *self._append_args(new_name),
            "--object-identity",
            f"DEP-A/{self._dep_name(1)}",
        )
        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_duplicate_identity", result["error_code"])
        self.assertEqual(before, file_sha256(map_path))

    def test_validate_rejects_duplicate_current_and_prior_path_aliases(self) -> None:
        map_path = self._write_map(2)
        value = json.loads(map_path.read_text(encoding="utf-8"))
        value["entries"][1]["prior_paths"] = [value["entries"][0]["current_path"]]
        write_json(map_path, value)

        completed, result = self._run_cli(
            "validate", "--repo", str(self.repo), "--class", "DEP-A"
        )

        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_path_collision", result["error_code"])

    def test_stale_head_and_bad_lock_fail_before_map_mutation(self) -> None:
        map_path = self._write_map(1)
        dep_name = "DEP-A-20260820-New Object"
        object_root = self.repo / ".lake-data" / "DEP-A" / "Series 001" / dep_name
        object_root.mkdir(parents=True)
        (object_root / "README.md").write_text("# New\n", encoding="utf-8")
        self._write_lock()
        before = file_sha256(map_path)

        stale_args = self._append_args(dep_name)
        stale_args[stale_args.index("--expected-head") + 1] = "0" * 40
        completed, result = self._run_cli(*stale_args)
        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_stale_head", result["error_code"])
        self.assertEqual(before, file_sha256(map_path))

        self._write_lock(scope="ledger")
        completed, result = self._run_cli(*self._append_args(dep_name))
        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_invalid_deployment_lock", result["error_code"])
        self.assertEqual(before, file_sha256(map_path))

    def test_concurrent_lock_drift_fails_before_map_mutation(self) -> None:
        map_path = self._write_map(1)
        dep_name = "DEP-A-20260820-Concurrent Object"
        object_root = self.repo / ".lake-data" / "DEP-A" / "Series 001" / dep_name
        object_root.mkdir(parents=True)
        (object_root / "README.md").write_text("# Concurrent\n", encoding="utf-8")
        self._write_lock()
        before = file_sha256(map_path)

        with mock.patch.object(
            MODULE,
            "verify_deployment_lock",
            side_effect=[({}, "a" * 64), ({}, "b" * 64)],
        ):
            with self.assertRaises(MODULE.DepSeriesError) as raised:
                MODULE.append_entry_command(
                    self.repo,
                    "DEP-A",
                    dep_name,
                    self.head,
                    self.lock,
                    "test-automation",
                    "test-run",
                    object_identity=f"fixture:{dep_name}",
                    prior_paths=(),
                )

        self.assertEqual("dep_series_concurrent_mutation", raised.exception.code)
        self.assertEqual(before, file_sha256(map_path))

    def test_map_tree_drift_and_empty_series_fail_closed(self) -> None:
        self._write_map(1)
        extra = self.repo / ".lake-data" / "DEP-A" / "Series 001" / "DEP-A-20260820-Unmapped"
        extra.mkdir(parents=True)
        (extra / "README.md").write_text("# unmapped\n", encoding="utf-8")

        completed, result = self._run_cli(
            "validate", "--repo", str(self.repo), "--class", "DEP-A"
        )
        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_map_tree_drift", result["error_code"])

        extra.parent.joinpath("DEP-A-20260820-Unmapped", "README.md").unlink()
        extra.rmdir()
        (self.repo / ".lake-data" / "DEP-A" / "Series 002").mkdir()
        completed, result = self._run_cli(
            "validate", "--repo", str(self.repo), "--class", "DEP-A"
        )
        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_empty_series", result["error_code"])

    def test_invalid_class_and_unsafe_path_return_structured_json_errors(self) -> None:
        self._write_map(1)

        completed, result = self._run_cli(
            "validate", "--repo", str(self.repo), "--class", "DEP-Z"
        )
        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_invalid_arguments", result["error_code"])
        self.assertFalse(result["retryable"])

        completed, result = self._run_cli(
            "resolve",
            "--repo",
            str(self.repo),
            "--class",
            "DEP-A",
            "--path",
            "../../outside",
        )
        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_invalid_path", result["error_code"])
        self.assertFalse(result["retryable"])

    def test_direct_under_class_and_root_flat_paths_are_rejected(self) -> None:
        self._write_map(1)
        direct = self.repo / ".lake-data" / "DEP-A" / "DEP-A-20260820-Direct"
        direct.mkdir(parents=True)
        (direct / "README.md").write_text("# direct\n", encoding="utf-8")
        completed, result = self._run_cli(
            "validate", "--repo", str(self.repo), "--class", "DEP-A"
        )
        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_invalid_layout", result["error_code"])

        direct.joinpath("README.md").unlink()
        direct.rmdir()
        root_flat = self.repo / ".lake-data" / "DEP-A-20260820-Root Flat"
        root_flat.mkdir(parents=True)
        (root_flat / "README.md").write_text("# root flat\n", encoding="utf-8")
        completed, result = self._run_cli(
            "validate", "--repo", str(self.repo), "--class", "DEP-A"
        )
        self.assertEqual(2, completed.returncode)
        self.assertEqual("dep_series_invalid_layout", result["error_code"])


if __name__ == "__main__":
    unittest.main()
