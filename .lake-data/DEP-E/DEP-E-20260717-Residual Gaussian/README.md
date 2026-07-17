# DEP-E-20260717-Residual Gaussian

#cbct #computed-tomography #sparse-view #3d-gaussian-splatting #wavelets #spectral-bias #medical-imaging #inverse-problems #research-review #arxiv

Public-safe DEP-E research artifact reviewing Residual Gaussian Splatting for ultra sparse-view cone-beam CT reconstruction. The complete source bundle was verified and inspected locally. Only derived Markdown and public source URLs are deposited; no source document is redistributed.

## Contents

- `README.md` - inventory, context, relevance, and source attribution for this DEP-E entry.
- `residual_gaussian_cbct_manuscript.md` - schema-complete manuscript review covering source evidence, method, experiments, limitations, implementation paths, related research, and local-source integrity validation.

No `.source/` directory is present. The source PDF, full-paper HTML, metadata HTML, e-print archive, extracted text, integrity records, and temporary page renders were withheld locally.

## Summary of Items

- `README.md` establishes the public deposition boundary and maps every public source URL to the generated manuscript.
- `residual_gaussian_cbct_manuscript.md` reviews arXiv:2604.27552v1 source-first. It explains the dual Gaussian representation, wavelet-derived initialization, residual projection fitting, curriculum optimization, AAPM comparisons, ablations, real-specimen evidence, reproducibility gaps, and exactly three related Black Lake DEP bridges.

## Insights and Relevance

The paper's most transferable insight is to use spectral analysis for capacity placement without forcing a non-negative physical model to reproduce signed wavelet coefficients. A low-frequency Gaussian branch anchors global attenuation; a detail branch learns only the residual left in the raw projection domain; and a warm-up schedule prevents the base branch from consuming the detail signal. Source-reported AAPM results and ablations support this mechanism, but the evidence is bounded by simulated clinical projections, a qualitative real-specimen experiment, missing uncertainty and resource measurements, and an official repository that currently contains only a README. The related Hypercomplex MRI, AFIDAF, and CAR Avatar deposits place RGS within a broader design pattern: decompose underdetermined reconstruction into compatible representations, enforce a division of labor, and audit local detail rather than trusting one aggregate score.

## Attribution Block

- Source URL: https://arxiv.org/abs/2604.27552
  - Applies to: `residual_gaussian_cbct_manuscript.md`
  - Notes: Canonical metadata, authors, version, abstract, DOI, and source links.
- Source URL: https://arxiv.org/html/2604.27552
  - Applies to: `residual_gaussian_cbct_manuscript.md`
  - Notes: Official full-paper HTML used for method, experiment, result, and limitation review.
- Source URL: https://arxiv.org/pdf/2604.27552
  - Applies to: `residual_gaussian_cbct_manuscript.md`
  - Notes: Complete paper and layout-sensitive figure/table evidence; file retained locally only.
- Source URL: https://doi.org/10.48550/arXiv.2604.27552
  - Applies to: `residual_gaussian_cbct_manuscript.md`
  - Notes: Persistent arXiv DOI.
- Source URL: https://github.com/yqx7150/RGS
  - Applies to: `residual_gaussian_cbct_manuscript.md`
  - Notes: Paper-declared official repository; current tree inspection informed the reproducibility boundary.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md
  - Applies to: `residual_gaussian_cbct_manuscript.md`
  - Notes: Related DEP basis for undersampled medical reconstruction and representation design.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md
  - Applies to: `residual_gaussian_cbct_manuscript.md`
  - Notes: Related DEP basis for complementary spatial and spectral operators.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-Clothed%20Avatar%20CAR/clothed_avatar_car_manuscript.md
  - Applies to: `residual_gaussian_cbct_manuscript.md`
  - Notes: Related DEP basis for sparse-observation 3D reconstruction and staged detail refinement.
- Source-file policy: all original and derived source documents remain local and were not copied, staged, committed, attached, or uploaded.
