# DEP-E-20260818-ST-NeRF Video

#st-nerf #free-viewpoint-video #neural-rendering #dynamic-scenes

This public-safe DEP preserves a source-grounded review of arXiv:2104.14786v1, “Editable Free-Viewpoint Video using a Layered Neural Representation.” The paper presents layered spatio-temporal neural radiance fields for editable dynamic-scene viewing from synchronized multi-view RGB video. The verified PDF, full-paper HTML, metadata HTML, extraction cache, repair receipts, and any source package remain local and are not included here.

## Contents

- `README.md` — public-safe inventory, summary, relevance, and attribution.
- `st_nerf_video_manuscript.md` — schema-complete manuscript research document.

No `.source/` directory is included because local source retention and public-safe redistribution rules require the original source files to remain withheld.

## Summary of Items

The manuscript records the paper’s source metadata, ST-NeRF representation, scene parsing and tracking pipeline, layered renderer, editing operations, training strategy, reported evaluation, limitations, implementation boundary, and exactly three related Black Lake entries. It distinguishes author-reported metrics from reviewer interpretation and preserves the Table 1 metric-direction inconsistency for follow-up.

## Insights and Relevance

The paper is a useful bridge between multi-view capture, dynamic neural scene representation, controllable video editing, and geometry-aware evaluation. Its per-entity layer abstraction suggests an auditable control surface for scene composition, while its reliance on segmentation, bounding boxes, calibration, and dense capture makes the failure boundary explicit. The related DEP entries connect this older ST-NeRF design to current work on dynamic neural appearance, geometry-consistent video generation, and spatiotemporal world models.

## Attribution Block

- Source URL: https://arxiv.org/abs/2104.14786
  - Applies to: source identity, authors, abstract, version, and public metadata.
  - Notes: Public arXiv metadata; original files withheld locally.
- Source URL: https://arxiv.org/html/2104.14786
  - Applies to: full-paper method, results, limitations, and references.
  - Notes: Public full-paper HTML; not redistributed.
- Source URL: https://arxiv.org/pdf/2104.14786
  - Applies to: PDF integrity and visual Table 1 inspection.
  - Notes: Public PDF; not uploaded.
- Source URL: https://doi.org/10.1145/3450626.3459756
  - Applies to: ACM publication metadata.
  - Notes: Publisher DOI locator.
- Source URL: https://jiakai-zhang.github.io/st-nerf/
  - Applies to: project context and official code locator.
  - Notes: Author project page.
- Source URL: https://github.com/DarlingHang/st-nerf
  - Applies to: official implementation README, configuration, and demo boundary.
  - Notes: Repository inspected but not executed; no code or dataset redistributed.
- Repository-relative source: `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic/controllable_dynamic_manuscript.md`
  - Applies to: related-DEP synthesis.
  - Notes: Existing Black Lake manuscript; no source file collected here.
- Repository-relative source: `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
  - Applies to: related-DEP synthesis.
  - Notes: Existing Black Lake manuscript; no source file collected here.
- Repository-relative source: `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md`
  - Applies to: related-DEP synthesis.
  - Notes: Existing Black Lake manuscript; no source file collected here.
