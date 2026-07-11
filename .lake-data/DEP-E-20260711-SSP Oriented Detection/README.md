# DEP-E-20260711-SSP Oriented Detection

#computer-vision #remote-sensing #oriented-detection #weak-supervision #point-supervision #spatial-partition #pseudo-labels #research-review

Public-safe source-first research deposit for arXiv:2506.10601, *Semantic-decoupled Spatial Partition Guided Point-supervised Oriented Object Detection*. The deposit records a cache-accelerated primary-source review, implementation context, evidence tensions, and three related Black Lake concept bridges. No original source file is redistributed.

## Contents

- `README.md` - DEP inventory, summaries, relevance, and source attribution.
- `ssp_oriented_detection_manuscript.md` - Schema-complete manuscript review with source metadata, evidence ledger, methods, results, limitations, implementations, related research, replication checklist, and attribution.

## Summary of Items

- `README.md` makes the deposit independently discoverable and states the source-file policy.
- `ssp_oriented_detection_manuscript.md` reviews SSP’s partition-guided point-supervision pipeline, preserves author-reported results with discrepancy notes, evaluates the official code evidence, and translates the work into bounded audit and benchmark concepts.

## Insights and Relevance

SSP illustrates a recurring Black Lake design pattern: weak evidence becomes more useful when a system introduces explicit, auditable structure. The paper combines point centers, nearest-neighbor scale, partition boundaries, semantic compatibility, region growing, and principal-axis geometry rather than relying on a single opaque inference step. Its strongest reported contribution is a 6.73-point DOTA-v1.0 mAP gain over PointOBB-v2 at roughly two hours and below 6 GB in the reported setup. Its strongest warning is equally valuable: hard priors break on overlap, low contrast, noise, low resolution, and bridge-like structures, while prose/table discrepancies require careful evidence handling.

## Attribution Block

- Source URL: https://arxiv.org/abs/2506.10601
  - Applies to: `ssp_oriented_detection_manuscript.md`
  - Notes: Primary paper metadata, abstract, versions, identifiers, and source links.
- Source URL: https://arxiv.org/html/2506.10601
  - Applies to: `ssp_oriented_detection_manuscript.md`
  - Notes: Primary full-text evidence for methods, experiments, and limitations.
- Source URL: https://arxiv.org/e-print/2506.10601
  - Applies to: `ssp_oriented_detection_manuscript.md`
  - Notes: Public TeX source used by the private extraction cache; not redistributed.
- Source URL: https://doi.org/10.1016/j.patcog.2026.114079
  - Applies to: `ssp_oriented_detection_manuscript.md`
  - Notes: Pattern Recognition publication metadata.
- Source URL: https://github.com/AntXinyuan/SSP
  - Applies to: `ssp_oriented_detection_manuscript.md`
  - Notes: Official Apache-2.0 implementation inspected at a pinned main-branch commit; no code copied.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260709-Clothed%20Avatar%20CAR/clothed_avatar_car_manuscript.md
  - Applies to: `ssp_oriented_detection_manuscript.md`
  - Notes: Related DEP bridge for sparse visual evidence and explicit geometric priors.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: `ssp_oriented_detection_manuscript.md`
  - Notes: Related DEP bridge for geometry-aware representation consistency.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - Applies to: `ssp_oriented_detection_manuscript.md`
  - Notes: Related DEP bridge for boundary-constrained spatial search.
