# DEP-E-20260718-Pixel Point Transfer

#3d-vision #point-clouds #contrastive-learning #knowledge-transfer #rgbd #representation-learning #pretraining #arxiv-review

Public-safe deposition context: This DEP-E entry preserves a source-first review of arXiv:2104.04687v3, *Learning from 2D: Contrastive Pixel-to-Point Knowledge Transfer for 3D Pretraining*. It records a uniform random draw, stable-key deduplication, mandatory source repair, complete-paper verification, evidence review, and related-DEP synthesis using date-only provenance. Original PDF, HTML, metadata, TeX/source, extracted text, caches, and local verification records were withheld.

## Contents

- `README.md` - DEP inventory, public-safe context, synthesis summary, and source attribution.
- `pixel_point_transfer_manuscript.md` - Schema-complete manuscript review with source metadata, evidence ledger, method/results analysis, constraints, implementation paths, MVP design, related reading, and appendix.

No `.source/` directory is present. Original source documents were not authorized for public deposition.

## Summary of Items

### `README.md`

Defines the deposit boundary and source-withholding policy. It links the reviewed paper and exactly three related Black Lake entries without exposing private filesystem, machine, timezone, or precise execution details.

### `pixel_point_transfer_manuscript.md`

Reviews PPKT, which uses calibrated RGB-D back-projection, a learned upsampling feature projection layer, and point-pixel NCE to transfer a frozen 2D teacher's local representations into a sparse 3D student. The manuscript preserves the reported S3DIS, SUN RGB-D, and ScanNet results; distinguishes table values from conflicting narrative arithmetic; examines teacher, objective, capacity, and label-fraction ablations; and states the non-reproduction boundary.

## Insights and Relevance

PPKT's durable design lesson is that cross-modal transfer needs an explicit correspondence unit and adapter. Physical pixel-point alignment makes local contrastive supervision possible, while the upsampling projection decides which high-level 2D information reaches each point. HERMES extends the spatial bridge from cameras through BEV into point-cloud generation; CorrKD shows how same-sample and relational contrastive distillation preserve privileged modality structure; VideoWeave similarly adapts geometry features into another latent space and distills them into a student. Together they motivate a reusable evaluation pattern: audit correspondence, pin the adapter, isolate the transfer objective, and test the student under the constraint where transfer is expected to matter. The source evidence supports indoor RGB-D research, not unrestricted 3D deployment; code release, multi-seed intervals, cross-domain tests, calibration perturbations, and corrected result arithmetic remain important follow-up work.

## Attribution Block

- Source URL: https://arxiv.org/abs/2104.04687v3
  - Applies to: paper identity, authors, revision, subject, and abstract metadata.
- Source URL: https://arxiv.org/pdf/2104.04687
  - Applies to: complete paper, tables, figures, and empirical review; source file withheld locally.
- Source URL: https://ar5iv.labs.arxiv.org/html/2104.04687
  - Applies to: verified full-paper HTML used after the official arXiv HTML response failed validation; source file withheld locally.
- Source URL: https://arxiv.org/e-print/2104.04687
  - Applies to: TeX/source, supplement, tables, and pseudocode inspection; source package withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2104.04687
  - Applies to: arXiv-issued DOI identity.
- Source URL: https://liu115.github.io/
  - Applies to: author-maintained preprint classification and public code-link check.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: repository filing, attribution, and source-withholding policy.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP-E placement and publication-index maintenance rules.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related-repository authority and dedup context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md
  - Applies to: camera/BEV/point-cloud representation synthesis; primary basis https://arxiv.org/abs/2501.14729.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-CorrKD%20Missing%20Modal/corrkd_missing_modal_manuscript.md
  - Applies to: contrastive teacher/student and relational-distillation synthesis; primary basis https://arxiv.org/abs/2404.16456v2.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md
  - Applies to: feature-adapter and distilled geometry-prior synthesis; primary basis https://arxiv.org/abs/2606.14162.
