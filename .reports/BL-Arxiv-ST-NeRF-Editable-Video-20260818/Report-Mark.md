# Report-Mark: ST-NeRF Editable Video

## Source Metadata

- Title: “Editable Free-Viewpoint Video using a Layered Neural Representation.”
- Authors: Jiakai Zhang, Xinhang Liu, Xinyi Ye, Fuqiang Zhao, Yanshun Zhang, Minye Wu, Yingliang Zhang, Lan Xu, and Jingyi Yu.
- Identifiers: arXiv:2104.14786v1; DOI: 10.1145/3450626.3459756.
- Public primary sources: [arXiv metadata](https://arxiv.org/abs/2104.14786), [full-paper HTML](https://arxiv.org/html/2104.14786), [PDF](https://arxiv.org/pdf/2104.14786), and [ACM DOI](https://doi.org/10.1145/3450626.3459756).
- Implementation context: [author project page](https://jiakai-zhang.github.io/st-nerf/) and [official ST-NeRF repository](https://github.com/DarlingHang/st-nerf).
- Source integrity: initial local unit was partial because full-paper HTML was missing; one bounded repair produced a verified complete PDF/HTML unit. The source package was unavailable.
- Source locality: original PDF, HTML, metadata, extracted text, cache, and repair records were withheld locally. No source files were uploaded, staged, committed, or attached.

## Concise Research Notes

ST-NeRF represents the environment and each tracked dynamic entity as a separate continuous function of space and time. A scene-parsing stage uses multi-view stereo, multi-view tracking, trajectory correction, mask refinement, and 3D bounding boxes. The renderer segments rays through layer boxes, samples each segment, evaluates the corresponding ST-NeRF, and performs object-aware volume rendering. This design makes position, scale, duplication, hiding, transparency, and retiming controllable at inference.

The reported data consists of eight indoor scenes with two or three performers, 16 synchronized RGB cameras, 1920x1080 capture, and 25 fps. The paper reports 12–36 hours of lower-resolution training on one RTX 3090, extra days for high-resolution refinement, and about two minutes to render a 1920x1080 image with three layers. It claims strong baseline comparisons and component ablations, but the rendered Table 1 visibly prints an internal metric inconsistency: `Ours` is bolded at SSIM 0.9203 and MAE 0.1178 even though NeRF-T has SSIM 0.9243 and all listed baselines have lower MAE. The artifact preserves the printed evidence and does not repair it.

## Evidence and Attribution

| Evidence | Basis | Use in this report |
|---|---|---|
| E1 | arXiv metadata, full HTML, PDF, and ACM DOI | Identity, authors, version, venue, and primary source context |
| E2 | Method sections and figures in the full paper | Scene parsing, ST-NeRF, renderer, training, and editing mechanism |
| E3 | Results, ablations, limitation section, and rendered Table 1 | Reported metrics, operating boundary, and evidence tension |
| E4 | Author project page and official repository README/config/demo | Code/data availability and reproduction boundary |
| E5 | Existing Black Lake DEP manuscripts | Conceptual bridge and related-entry selection |
| E6 | Public-safe workflow records | Random selection, source repair, cache status, and dedup validation |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic/controllable_dynamic_manuscript.md` — direct overlap in dynamic neural 3D portrait representation and controllable appearance editing; its source URL is https://arxiv.org/abs/2309.11009.
2. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` — overlap in geometry-consistent video synthesis and metrics beyond frame appearance; its source URL is https://arxiv.org/abs/2606.14162.
3. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` — overlap in multi-view spatial state, temporal modeling, and 3D-world evaluation; its source URL is https://arxiv.org/abs/2501.14729.

## Synthesis Note

### Concept Bridge

ST-NeRF makes dynamic-scene control explicit by separating a scene into neural layers anchored by tracked boxes and timestamps. Controllable Dynamic extends the same broad idea toward appearance control in neural 3D portraits. VideoWeave moves the geometry signal into latent video training so that spatial consistency is retained without an explicit inference-time geometry pipeline. HERMES uses a compressed multi-view BEV state and language-conditioned world queries to forecast future 3D structure. The bridge is a design question: which spatial state should be explicit and editable, which should be latent and distilled, and which should be exposed as an auditable evaluation interface?

### Potential Implementations

1. **Layered Scene Evidence Gate** — Build a local evaluator that ingests authorized multi-view frames, calibration, layer masks, and timestamps; checks layer identity, depth order, temporal continuity, and metric direction; and emits a nonbinding report. ST-NeRF supplies the layer contract, VideoWeave supplies spatial-consistency metrics, and HERMES supplies horizon-aware state checks.
2. **Offline Editable-Video Workbench** — Wrap a pinned ST-NeRF checkpoint with a manifest-driven edit graph for translation, duplication, hiding, transparency, and retiming. Every output carries an edit manifest, source version, confidence status, and human-review gate. This is a research tool for licensed or synthetic media, not a production capture service.
3. **Geometry-Aware Video Release Gate** — Apply a cross-model gate to edited or generated clips. Compare identity, occlusion, depth ordering, camera-motion consistency, and temporal drift against synthetic references or authorized held-out views. Release only a bounded preview when the evidence bundle passes; otherwise abstain and preserve the failure slice.

### Deeper Relationship Observations

1. **Control location is the central tradeoff.** ST-NeRF exposes object layers at inference, VideoWeave hides geometry in a training-time latent, and HERMES exposes a compact BEV/query interface for future state. Explicit control improves editability but increases perception and runtime dependencies; latent control reduces inference overhead but shifts risk to validation.
2. **Geometry is useful only when its failure boundary is visible.** ST-NeRF’s boxes and masks can create ghosting when tracking fails; VideoWeave’s geometric prior can fail under out-of-distribution motion; HERMES’s Chamfer distance can underweight rare-object errors. Each design needs identity- and coverage-aware diagnostics, not just average visual or geometric scores.
3. **The layer/state abstraction is an evaluation primitive.** Whether implemented as neural layers, geometry latents, or BEV queries, a reusable spatial state enables counterfactual edits, horizon tests, and failure localization. This is a reviewer inference across the three existing DEP artifacts, not a validated cross-paper result.

### Conceptual Similarities

1. **Spatiotemporal consistency:** all four works treat time and spatial structure as more than independent frame appearance.
2. **Structured intermediate state:** ST-NeRF layers, VideoWeave geometry latents, HERMES BEV/world queries, and Controllable Dynamic’s neural 3D controls all create a representation between raw pixels and final output.
3. **Evaluation beyond aesthetics:** each direction motivates geometry, identity, controllability, or downstream consistency checks that complement surface-level visual quality.

### MVP Implementations

#### MVP 1: Synthetic Layer Composer

Purpose: validate deterministic layer ordering and edit manifests without restricted media. It uses synthetic rectangles and timestamps, not personal or source video.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Layer:
    name: str
    depth: float
    visible: bool = True

def compose_layers(layers):
    """Return a deterministic back-to-front render plan."""
    return [layer.name for layer in sorted(layers, key=lambda item: item.depth)
            if layer.visible]

plan = compose_layers([Layer("background", 10), Layer("actor", 4)])
assert plan == ["actor", "background"]
```

#### MVP 2: Direction-Aware Metric Gate

Purpose: catch the class of Table 1 inconsistency seen in the source before a report declares a winner.

```python
def metric_winner(rows, metric, direction):
    values = {row["name"]: row[metric] for row in rows}
    best = max(values.values()) if direction == "higher" else min(values.values())
    return [name for name, value in values.items() if value == best]

rows = [{"name": "baseline", "ssim": 0.9243},
        {"name": "ours", "ssim": 0.9203}]
assert metric_winner(rows, "ssim", "higher") == ["baseline"]
```

#### MVP 3: Temporal Edit Manifest

Purpose: keep retiming or duplication changes auditable and bounded before rendering.

```python
def validate_edit(edit, frame_count):
    if not 0 <= edit["source_frame"] < frame_count:
        raise ValueError("source frame outside manifest")
    if edit["operation"] not in {"move", "duplicate", "retime", "hide"}:
        raise ValueError("unsupported edit")
    return {"layer": edit["layer"], "operation": edit["operation"],
            "source_frame": edit["source_frame"]}

assert validate_edit({"layer": "actor", "operation": "retime", "source_frame": 3}, 10)
```

### Developer Challenges

1. **Data and environment reproducibility:** align the official repository’s older PyTorch/CUDA assumptions, checkpoint paths, dataset access, camera calibration, and expected outputs without silently changing the recipe.
2. **Metric and evidence integrity:** reproduce all table columns with explicit metric directions, resolve the printed SSIM/MAE conflict, and retain raw predictions, seeds, and failure slices.
3. **Robust layer contracts:** handle occlusion, similar appearance, camera dropout, lighting change, non-human objects, non-rigid motion, and uncertain tracking without emitting plausible but incorrect edits.

### Author Challenges

1. **Generalization beyond performers:** replace or extend human-specific parsing so arbitrary objects and mixed scenes can become stable, editable layers.
2. **Sparse-view and lighting robustness:** reduce the 16-camera dependence while preventing ghosting, missing-region artifacts, and view-dependent errors under illumination change.
3. **Transparent artifact release:** publish exact data terms, raw evaluation outputs, metric scripts, checkpoints, and environment manifests so later reviewers can audit and reproduce the comparative claims.

## Validation Notes

- Required source gate: passed after one bounded repair. The PDF passed size, `%PDF-`, and trailing `%%EOF`; full-paper HTML passed size, body-text, document-marker, heading, and structure-term checks.
- Cache: initial miss to `cached` in missing-only mode; `pypdf` and `html-regex` succeeded; `pdftotext` unavailable; source package unavailable.
- Random selection: 75,967 PDFs; 75,964 unique parent units; zero-based index 34,230; first draw accepted; duplicate exclusions 0; reselections 0.
- Dedup: no match in the local pointer index, logs, reports, lake-data, automation memory, relevant Black-Lake-Data searches, or preceding 24-hour marker window.
- Schema: manuscript front matter and H1 are identical and under 40 characters; all required full-manuscript headings are present; exactly three exercise paths are present.
- Report contracts: exactly three potential implementations, deeper relationship observations, conceptual similarities, MVP implementations, developer challenges, and author challenges are present. Each MVP includes one safe Python mock-up.
- Public-safe check: no local absolute paths, drive paths, usernames, machine names, exact local execution timestamps, local timezone labels, PDFs, HTML, source archives, caches, extracted source text, or `.source/` folder are intended for submission.
- Related-entry count: exactly three existing Black Lake DEP entries were selected for conceptual overlap.
- Source upload status: no original source file was uploaded, staged, committed, or attached.

## Attribution Block

- Source URL: https://arxiv.org/abs/2104.14786
  - Applies to: source identity, authors, abstract, version, and metadata.
  - Notes: Public arXiv metadata; original source files withheld locally.
- Source URL: https://arxiv.org/html/2104.14786
  - Applies to: method, evaluation, limitations, and references.
  - Notes: Public full-paper HTML; not redistributed.
- Source URL: https://arxiv.org/pdf/2104.14786
  - Applies to: PDF integrity and visual Table 1 inspection.
  - Notes: Public PDF; not uploaded.
- Source URL: https://doi.org/10.1145/3450626.3459756
  - Applies to: ACM publication metadata.
  - Notes: Publisher DOI locator.
- Source URL: https://jiakai-zhang.github.io/st-nerf/
  - Applies to: project context and code locator.
  - Notes: Author project page.
- Source URL: https://github.com/DarlingHang/st-nerf
  - Applies to: official code README, configs, demos, and reproduction boundary.
  - Notes: Inspected but not executed; source files and data were not redistributed.
- Repository-relative source: `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic/controllable_dynamic_manuscript.md`
  - Applies to: related DEP synthesis.
  - Notes: Existing public-safe artifact.
- Repository-relative source: `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
  - Applies to: related DEP synthesis.
  - Notes: Existing public-safe artifact.
- Repository-relative source: `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md`
  - Applies to: related DEP synthesis.
  - Notes: Existing public-safe artifact.
