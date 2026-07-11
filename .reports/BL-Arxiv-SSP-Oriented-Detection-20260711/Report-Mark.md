# Report-Mark: SSP Oriented Detection

## Source Metadata

- `Paper`: Semantic-decoupled Spatial Partition Guided Point-supervised Oriented Object Detection.
- `Authors`: Xinyuan Liu, Hang Xu, Zirui Chen, Yike Ma, Chenggang Yan, Feng Dai.
- `Stable identifiers`: arXiv:2506.10601v2; DOI 10.48550/arXiv.2506.10601; publisher DOI 10.1016/j.patcog.2026.114079.
- `Publication`: Pattern Recognition, Volume 180, Part B, Article 114079 (2026).
- `Primary URLs`: https://arxiv.org/abs/2506.10601; https://arxiv.org/html/2506.10601; https://doi.org/10.1016/j.patcog.2026.114079.
- `Official implementation`: https://github.com/AntXinyuan/SSP, inspected at main commit `1e42389c4770e835a55afb733f6d9079b3f9567a`.
- `Source access date`: 2026-07-11.
- `Source-file policy`: No original PDF, source package, dataset, model, checkpoint, or repository file was deposited.

## Concise Research Notes

SSP is a two-stage point-supervised oriented-object detection framework. A lightweight label marker first converts point annotations to pseudo rotated boxes; a conventional detector then trains on those boxes. SSP improves the label-marker stage through two explicit algorithms:

1. Pixel Spatial Partition-based Sample Assignment combines a fixed positive radius, nearest-neighbor scale bounds, Voronoi-like partitions, and region growing. It increases positive/negative coverage while preserving ignored regions where evidence remains ambiguous.
2. Semantic Spatial Partition-based Box Extraction separates semantic maps by class, partitions compatible point sets, performs constrained region growing, and converts masks to rotated boxes with a PCA-MinMax rule.

The DOTA-v1.0 table reports 48.41 mAP for SSP(FCOSR) versus 41.68 for PointOBB-v2. Stronger detector variants report 50.00 and 50.81. The cost table reports 1.91 hours and 5.34 GB on two RTX 3090 GPUs for SSP’s strongest listed result. These are author-reported, not reproduced.

The most informative ablations move detector mAP from 12.88 to 48.41 as radius negatives, grown positives, and partition-boundary negatives are added. Decoupled semantic maps report 48.41 versus 30.81 for merged maps, while partition-based box extraction reports 48.41 versus 42.80 for oriented search. Performance declines with point offset, and bridges remain a severe failure class.

Evidence quality is mixed-high for describing the method and reported tables, but medium-low for generalization. The paper relies on limited same-class overlap and visible foreground/background contrast; uses dataset-specific compatibility pairs; and contains prose/table discrepancies for DOTA-v1.0, DOTA-v1.5, DOTA-v2.0, and 30% point-offset results. Table values were retained and discrepancies flagged.

## Evidence and Attribution

| Evidence | Inspected basis | Use | Limitation |
|---|---|---|---|
| Primary metadata | arXiv abstract page and publisher DOI record | Identity, dates, authors, venue, identifiers. | Metadata does not validate results. |
| Primary full text | arXiv HTML and extracted TeX-source text | Method, datasets, tables, ablations, limitations, conclusion. | PDF text backend unavailable; experiments not reproduced. |
| Official repository | Repository metadata and README at pinned commit | License, release status, commands, configs, pseudo labels, checkpoints, metrics. | Not cloned or executed; external datasets/assets not verified. |
| Local archive unit | Nearby README and PDF presence | Random selection identity. | Location withheld and file not redistributed. |
| Extraction cache | Public-safe summary | Cache hit/miss, extractor, output status. | Private manifest paths excluded. |
| Related DEP manuscripts | Three repository-relative Black Lake entries | Conceptual synthesis. | Context only; not validation evidence for SSP. |

## Related DEP Entries

1. `.lake-data/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md`
   - `Relevance`: CAR reconstructs a full clothed avatar from one RGB image by surrounding sparse evidence with body, pose, normal, SDF, and hyper-network priors. SSP similarly recovers missing box extent/orientation from one point by combining geometric and semantic constraints.
   - `Source basis`: The related manuscript’s executive summary, method, evidence ledger, and limitations were inspected.
2. `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
   - `Relevance`: VideoWeave injects geometry-aware latent structure to improve consistency without depending only on appearance. SSP decouples semantic maps and adds spatial geometry so pseudo boxes remain instance-consistent.
   - `Source basis`: The related manuscript’s executive summary, evidence ledger, geometry-latent mechanism, and reproducibility boundary were inspected.
3. `.lake-data/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md`
   - `Relevance`: RRT-CBF constrains spatial search with explicit safe boundaries. SSP constrains region growth with partition boundaries, converting unconstrained expansion into auditable, locally valid regions.
   - `Source basis`: The related manuscript’s executive summary, mobile-robot method, evidence ledger, and boundary-condition analysis were inspected.

## Synthesis Note

### Concept Bridge

Across all four works, explicit structure is used to narrow an underdetermined search space. CAR narrows 3D reconstruction with human-body and surface priors. VideoWeave narrows video generation with geometry-aware latent coupling. RRT-CBF narrows motion exploration with barrier constraints. SSP narrows pseudo-label generation with point-distance bounds, partitions, semantic confidence, and principal-axis geometry. The reusable pattern is not “add more priors” in the abstract; it is to make each prior observable, testable, and defeasible when the environment violates it.

### Potential Implementations

1. `Partition Evidence Viewer`: A local analysis tool that overlays points, radius bounds, partitions, grown masks, semantic scores, and final rotated boxes, with per-stage failure labels.
2. `Sparse Supervision Stress Bench`: A deterministic benchmark that sweeps point offset, overlap, contrast, object size, noise, and resolution, then reports pseudo-label and detector metrics by stratum.
3. `Structural Prior Registry`: A Markdown/JSON ledger that records every hand-authored or learned prior, its expected domain, failure tests, code/config version, and fallback behavior.

### Deeper Relationship Observations

1. The methods separate proposal from correction: SSP proposes regions from points and corrects them with semantic learning; CAR predicts coarse shape then refines it; RRT proposes motion then constrains/tracks it. This separation improves auditability but creates stage-coupling risks.
2. Geometry helps only when its assumptions match the scene. SSP partitions fail on bridges and heavy overlap; CAR priors can hallucinate occluded geometry; RRT-CBF depends on faithful obstacle models; VideoWeave’s geometry latents can inherit reconstruction bias. Explicit priors move uncertainty rather than eliminate it.
3. Intermediate artifacts become evidence surfaces. SSP masks and partitions, CAR normals/SDFs, VideoWeave geometry latents, and RRT barrier margins can all support targeted diagnostics that final-output metrics alone cannot provide.

### Conceptual Similarities

1. Each work injects domain structure to compensate for missing or ambiguous observations.
2. Each work benefits from a multi-stage or multi-representation decomposition instead of a single end-to-end prediction surface.
3. Each work needs failure reporting tied to violated assumptions, not only aggregate accuracy or visual quality.

### MVP Implementations with Code Mock-ups

1. `Geometry-stage invariant checker`

```python
def check_geometry(point, region, box):
    return {
        "point_in_region": region.contains(point),
        "point_in_box": box.contains(point),
        "region_nonempty": region.area > 0,
        "box_finite": all(map(math.isfinite, box.parameters)),
    }
```

This uses synthetic geometry only and stops on invalid or non-finite values.

2. `Prior-failure stratifier`

```python
def stratum(overlap, contrast, offset):
    return {
        "high_overlap": overlap >= 0.25,
        "low_contrast": contrast < 0.10,
        "large_offset": offset >= 0.20,
    }
```

The output labels evaluation strata; it does not infer sensitive object identity or location.

3. `Claim-to-run ledger row`

```python
def ledger_row(claim_id, config_sha, metric, value):
    if not claim_id or not config_sha:
        raise ValueError("provenance required")
    return {"claim": claim_id, "config": config_sha,
            "metric": metric, "value": float(value)}
```

Production hardening would validate schemas, authenticate restricted manifests, and never store raw imagery in public exports.

### Developer Challenges

1. Reconstructing a compatible MMRotate/PyTorch environment while pinning every table result to the correct config, pseudo-label archive, and checkpoint.
2. Implementing coordinate transforms, rotated-box conventions, and region-growth boundaries without silent orientation or scale errors.
3. Building stage-aware evaluation that detects data leakage and reports both pseudo-label quality and downstream detector performance across failure strata.

### Author Challenges

1. Reconcile all prose/table discrepancies and release a machine-readable result manifest linked to exact configs and logs.
2. Demonstrate generalization without hand-authored compatibility pairs, especially under dense same-class overlap and unseen nested categories.
3. Establish credible bridge and low-contrast performance through targeted benchmarks, repeated seeds, uncertainty estimates, and failure-case disclosure.

## Validation Notes

- The paper was selected by one uniform random index over 75,438 PDF-parent paper units: zero-based index 29,914.
- Dedup scans checked arXiv ID, DOI, normalized title, and slug across the dedup index, `.logs`, `.reports`, `.lake-data`, automation memory, and Black-Lake-Data. Prior matches: 0. Same-paper markers within 24 hours: 0. Reselections: 0.
- Extraction preflight found no PDF backend. Local missing-only extraction produced metadata only; approved network fallback backfilled HTML and TeX-source text. Final cache status: `cached`; PDF text remained unavailable.
- Exactly three related DEP entries are listed and used.
- Synthesis Note counts: 3 potential implementations, 3 deeper relationship observations, 3 conceptual similarities, 3 MVP code mock-ups, 3 developer challenges, and 3 author challenges.
- The schema-complete manuscript is `.lake-data/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md`.
- Public-safe validation excludes local absolute paths, usernames, machine names, workspace roots, local timezone labels, and exact local execution timestamps.
- Source files collected for deposition: none. No `.source/` directory was created.

## Attribution Block

- Source URL: https://arxiv.org/abs/2506.10601
  - Applies to: paper identity, metadata, abstract, version, and source links.
  - Notes: Primary arXiv record.
- Source URL: https://arxiv.org/html/2506.10601
  - Applies to: method, experiment, limitation, and conclusion notes.
  - Notes: Primary full-text evidence.
- Source URL: https://arxiv.org/e-print/2506.10601
  - Applies to: extraction-backed paper review.
  - Notes: Public source package inspected through a private cache; not redistributed.
- Source URL: https://doi.org/10.1016/j.patcog.2026.114079
  - Applies to: publication and DOI metadata.
  - Notes: Pattern Recognition article identifier.
- Source URL: https://github.com/AntXinyuan/SSP
  - Applies to: code availability, commands, configs, license, and repository result context.
  - Notes: Official implementation inspected at the pinned commit; not executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260709-Clothed%20Avatar%20CAR/clothed_avatar_car_manuscript.md
  - Applies to: CAR Avatar related-entry bridge.
  - Notes: Processed DEP artifact, contextual evidence only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: VideoWeave related-entry bridge.
  - Notes: Processed DEP artifact, contextual evidence only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - Applies to: RRT-CBF related-entry bridge.
  - Notes: Processed DEP artifact, contextual evidence only.
