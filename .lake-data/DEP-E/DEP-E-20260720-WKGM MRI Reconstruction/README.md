# DEP-E-20260720-WKGM MRI Reconstruction

#mri #parallel-imaging #k-space #diffusion #score-model #inverse-problems #low-rank #medical-imaging #research

Public-safe DEP-E research deposit for a uniformly selected arXiv paper review. The entry preserves a source-grounded manuscript on weighted k-space score modeling, predictor-corrector reconstruction, acquired-sample data consistency, and optional SAKE low-rank projection. The source unit was repaired and verified before review. All paper files, endpoint responses, extracted text, caches, integrity records, and page renderings remain local and were withheld.

## Contents

- `README.md` - DEP inventory, summary, relevance, source policy, and attribution.
- `wkgm_mri_reconstruction_manuscript.md` - Schema-complete manuscript review, evidence ledger, critique, implementation translations, exercises, and replication guidance.

No `.source/` directory is present. Source-document redistribution was not authorized, and the Black Lake repository rules require arXiv automation source documents to remain local.

## Summary of Items

### `wkgm_mri_reconstruction_manuscript.md`

The manuscript reviews *WKGM: Weight-K-space Generative Model for Parallel Imaging Reconstruction* (`arXiv:2205.03883v4`, DOI `10.1002/nbm.5005`). It traces the radial k-space weighting transform, six-channel complex representation, variance-exploding score model, predictor-corrector sampler, data-consistency update, and SVD-WKGM's SAKE/Hankel projection.

The strongest displayed high-acceleration point is 31.69 dB PSNR and 0.841 SSIM for SVD-WKGM on T2 Transverse Brain under 2D Poisson sampling at `R=10`, compared with 29.75/0.823 for SAKE and 25.00/0.737 for the no-weight ablation. The manuscript also preserves counterevidence: supervised k-space deep learning is better on both displayed Cartesian `R=3` knee slices, while SVD-WKGM is better on the displayed Poisson `R=6` slices.

The review treats these as source-reported point results rather than clinical proof. Training data are described as 500 two-dimensional images from one healthy volunteer, augmented to 4,000 single-coil images. External comparisons often use one image or selected slices, and the paper reports no seeds, uncertainty, reader study, pathology preservation, runtime, memory, energy, or end-to-end compute accounting.

## Insights and Relevance

WKGM is relevant to Black Lake because it composes three distinct constraints: a learned score prior proposes plausible weighted k-space, data consistency anchors acquired samples, and SAKE optionally projects multi-coil neighborhoods toward structured low rank. That composition is a reusable pattern for inverse systems, but it also creates an attribution problem: headline gains cannot be assigned cleanly to weighting, channel augmentation, diffusion prior, consistency, or low-rank projection without matched-compute factorial ablations.

Exactly three related DEP entries sharpen the review. Hypercomplex MRI provides a direct representation-efficiency and clinical-evaluation neighbor. Residual Gaussian CBCT provides a sparse medical inverse-reconstruction analogy centered on high-frequency detail preservation. Acoustic Phase Retrieval provides a structured Fourier/Hankel inverse-problem comparison that makes conditioning and measurement identifiability explicit. Together they motivate an auditable reconstruction stack with separate representation, constraint, uncertainty, and resource ledgers.

Practical follow-up should begin with a pinned offline reproduction harness, synthetic or appropriately licensed k-space, subject-level splits, multiple seeds, matched compute, explicit latency/memory/SVD accounting, acquired-sample residual gates, localized disagreement maps, and human review. Aggregate PSNR/SSIM improvements are not sufficient for diagnostic or autonomous clinical use.

## Attribution Block

- Source URL: https://arxiv.org/abs/2205.03883
  - Applies to: `wkgm_mri_reconstruction_manuscript.md`.
  - Notes: Canonical arXiv metadata, authors, dates, version, and abstract; metadata only, not full-paper evidence.
- Source URL: https://arxiv.org/pdf/2205.03883
  - Applies to: `wkgm_mri_reconstruction_manuscript.md`.
  - Notes: Full paper used for method, equations, algorithms, tables, figures, experiments, and critique; source file withheld locally.
- Source URL: https://doi.org/10.1002/nbm.5005
  - Applies to: `wkgm_mri_reconstruction_manuscript.md`.
  - Notes: Official journal publication metadata and publisher DOI.
- Source URL: https://github.com/yqx7150/WKGM
  - Applies to: `wkgm_mri_reconstruction_manuscript.md`.
  - Notes: Official implementation repository; README and key files inspected, not executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md
  - Applies to: `wkgm_mri_reconstruction_manuscript.md`.
  - Notes: Related DEP evidence for accelerated MRI representation, resource measurement, and reliability boundaries.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Residual%20Gaussian/residual_gaussian_cbct_manuscript.md
  - Applies to: `wkgm_mri_reconstruction_manuscript.md`.
  - Notes: Related DEP evidence for sparse medical inverse reconstruction and high-frequency detail preservation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Acoustic%20Phase%20Retrieval/acoustic_phase_retrieval_manuscript.md
  - Applies to: `wkgm_mri_reconstruction_manuscript.md`.
  - Notes: Related DEP evidence for Fourier/Hankel inverse reconstruction, conditioning, and observability.
