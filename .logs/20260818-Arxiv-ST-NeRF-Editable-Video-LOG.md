# Arxiv DEP Job Log

## Public-Safe Run Summary

- Selected paper: Jiakai Zhang, Xinhang Liu, Xinyi Ye, Fuqiang Zhao, Yanshun Zhang, Minye Wu, Yingliang Zhang, Lan Xu, and Jingyi Yu, “Editable Free-Viewpoint Video using a Layered Neural Representation.”
- Identifier: arXiv:2104.14786v1; publisher DOI: 10.1145/3450626.3459756.
- Selection date: 2026-08-18. Exact local execution time is intentionally withheld.
- Selection method: `rg --files -g "*.pdf"` enumerated 75,967 PDFs; unique parent-directory units were collapsed to 75,964; PowerShell `Get-Random` selected zero-based index 34,230. The first draw was accepted after validation.
- Candidate and exclusion counts: 75,964 candidate units; duplicate exclusions 0; source-gate exclusions 0 after bounded repair; reselections 0; same-paper recent-marker exclusions 0.
- Initial source state: partial unit with a valid PDF and missing full-paper HTML.
- Repair: one bounded single-paper archive repair fetched and verified the official full-paper HTML. The valid PDF was preserved. The source package was unavailable.
- Final source state: complete. PDF header/EOF and full-paper HTML size, body, document-marker, heading, and paper-structure tests passed.
- Cache status: initial cache miss; missing-only extraction completed as `cached`. HTML used `html-regex`; PDF used `pypdf` because `pdftotext` was unavailable; source text was unavailable because no source package was present.
- Public source policy: PDF, full-paper HTML, metadata HTML, extracted text, cache, repair receipts, and local provenance remain local. No source files were uploaded, staged, committed, or attached.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic/controllable_dynamic_manuscript.md` — neural 3D portrait appearance control and dynamic radiance-field transfer.
2. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` — geometry-consistent video generation and spatial-consistency evaluation.
3. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` — multi-view spatial state, temporal prediction, and 3D world-model evaluation.

## Output Paths

- `.logs/20260818-Arxiv-ST-NeRF-Editable-Video-LOG.md`
- `.logs/20260818-Arxiv-ST-NeRF-Editable-Video-PHASE-LOG.md`
- `.reports/BL-Arxiv-ST-NeRF-Editable-Video-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-ST-NeRF Video/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-ST-NeRF Video/st_nerf_video_manuscript.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Can the official ST-NeRF repository reproduce the paper’s edited free-viewpoint results with the released walking or taekwondo artifacts under a pinned environment?
2. Does the Table 1 inconsistency for SSIM and MAE persist in the camera-view evaluation when the raw predictions and metric script are inspected?
3. How does layer decomposition behave under non-human objects, severe occlusion, lighting change, camera sparsity, and non-rigid motion?

## Challenges

1. The paper’s scene-parsing pipeline depends on human tracking, color separation, bounding boxes, and multi-view calibration, which can fail before neural rendering begins.
2. The reported training and rendering costs are substantial, while the public code and dataset boundary still require environment, data-access, and license verification.
3. The printed comparison table and its prose disagree on which metrics are best, so downstream evaluations must preserve raw tables and recompute metric directionality.

## Attribution Block

- Source URL: https://arxiv.org/abs/2104.14786
  - Applies to: selection identity, authors, abstract, version, and public metadata.
  - Notes: Public arXiv metadata page; source files were withheld locally.
- Source URL: https://arxiv.org/html/2104.14786
  - Applies to: full-paper method, experiments, limitations, and references.
  - Notes: Public full-paper HTML; source files were withheld locally.
- Source URL: https://arxiv.org/pdf/2104.14786
  - Applies to: PDF integrity and visual Table 1 inspection.
  - Notes: Public PDF; not uploaded to Black Lake.
- Source URL: https://doi.org/10.1145/3450626.3459756
  - Applies to: ACM Transactions on Graphics publication metadata.
  - Notes: Publisher DOI locator.
- Source URL: https://jiakai-zhang.github.io/st-nerf/
  - Applies to: project-page context and official code locator.
  - Notes: Author project page.
- Source URL: https://github.com/DarlingHang/st-nerf
  - Applies to: official code README, configuration, and demo inspection.
  - Notes: Public repository; code and datasets were not executed or redistributed.
