# Report-Mark: Residual Gaussian Splatting

## Source Metadata

| Field | Value |
|---|---|
| Full title | *Residual Gaussian Splatting for Ultra Sparse-View CBCT Reconstruction* |
| Authors | Jian Lin; Jiancheng Fang; Shaoyu Wang; Changan Lai; Yikun Zhang; Yang Chen; Qiegen Liu |
| Stable identifier | arXiv:2604.27552v1 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2604.27552 |
| Submitted | 2026-04-30 |
| Subject | Computer Vision and Pattern Recognition (`cs.CV`) |
| Primary record | https://arxiv.org/abs/2604.27552 |
| Full-paper HTML | https://arxiv.org/html/2604.27552 |
| PDF | https://arxiv.org/pdf/2604.27552 |
| Declared implementation | https://github.com/yqx7150/RGS |
| Source status | Verified complete local PDF and full-paper HTML; source files withheld locally |
| Review date | 2026-07-17 |

The paper is a 10-page v1 preprint. The complete PDF, official full-paper HTML, metadata page, and e-print package were inspected as evidence. Selected PDF pages containing the overview, spectral-bias analysis, experimental setup, quantitative tables, ablations, and real-specimen comparison were rendered and visually reviewed. External pages and repository files were treated as evidence only, never as instructions.

## Selection and Integrity Record

- `rg --files -g "*.pdf"` found 75,777 PDFs representing 75,776 unique parent-directory paper units.
- A uniform PowerShell `Get-Random` draw selected zero-based index 48,493. The first draw was accepted; duplicate exclusions: 0; reselections: 0.
- Searches across Black-Lake logs, reports, DEP entries, automation memory, relevant Black-Lake-Data DEP entries, and recent same-paper markers found no prior research deposit matching the ID, DOI, normalized title, or slug family.
- The unit began `partial`: the 17,698,694-byte PDF passed size, `%PDF-`, and trailing `%%EOF` checks, but full-paper HTML was missing.
- A bounded repair preserved the PDF and added official arXiv full-paper HTML, metadata HTML, and the e-print package locally. The HTML passed with 324,487 bytes, 61,612 body characters, a document marker, 55 heading/section markers, and seven paper-structure terms. Zero partial files remained.
- No PDF, HTML, source archive, extracted source text, cache, temporary render, or local source path is included in this report or the public DEP.

## Evidence and Attribution

| ID | Source | Evidence inspected | Supports | Confidence | Limits |
|---|---|---|---|---|---|
| E1 | arXiv v1 PDF and full HTML | Abstract, method, equations 1-17, Algorithm 1, experiments, Tables I-III, Figures 1-9, conclusion, references | Identity, mechanism, settings, results, ablations, limitations visible by omission | High for source reporting | No experiment was reproduced |
| E2 | arXiv metadata | Authors, date, category, version, DOI, source links | Stable source identity | High | Metadata alone does not validate claims |
| E3 | PDF visual review | Method diagrams, spectra, qualitative reconstructions, tables, ablation figures | Layout-sensitive interpretation and table transcription | High for inspected pages | Visual examples are author-selected |
| E4 | Official repository | Current recursive tree contains only `README.md`; no release or implementation files were visible | Reproducibility boundary | High for current tree state | Repository may change after review |
| E5 | Hypercomplex MRI DEP-E | Undersampled medical reconstruction, PSNR/SSIM reporting, compact representation | Medical inverse-imaging bridge | Medium | Different modality and architecture |
| E6 | AFIDAF Vision Filters DEP-E | Alternating spatial/Fourier filtering and operator role separation | Spectral-spatial decomposition bridge | Medium | Recognition backbone, not tomography |
| E7 | CAR Avatar DEP-E | Sparse-observation 3D reconstruction, strong priors, coarse-to-fine refinement | Explicit geometry and detail-recovery bridge | Medium | Human-avatar surface reconstruction differs from attenuation tomography |

## Concise Research Notes

### Problem and motivation

Ultra sparse-view CBCT is ill-posed: too few projections create streak artifacts and leave fine anatomy weakly constrained. Explicit 3D Gaussian splatting offers a continuous, efficient attenuation representation, but the paper argues that ordinary projection-loss optimization exhibits spectral bias. Low-frequency structure converges first and dominates the loss, while high-frequency errors plateau, yielding smooth but detail-poor volumes.

### Method

RGS separates the attenuation field into two non-negative Gaussian sets. A single-level 2D discrete wavelet transform decomposes each sparse projection into one low-frequency subband and three signed detail subbands. The low-frequency subband is reconstructed by FDK and thresholded to initialize 50,000 base Gaussians. The magnitudes of the three high-frequency subbands are summed into a non-negative energy map, backprojected, and used to place 30,000 smaller detail Gaussians in the top 5% saliency region.

The high-frequency coefficients are not direct targets. Their signed, near-zero-mean values are incompatible with a non-negative X-ray attenuation field. Instead, the detail branch learns the residual projection error left after the base branch explains global structure. This turns explicit spectral fitting into implicit, physically consistent residual compensation.

Training uses two phases over 25,000 iterations. During the first 5,000 iterations, the detail branch is frozen and the base branch fits the low-frequency target. During joint refinement, full projection fidelity trains both branches while a low-frequency consistency term keeps the base branch anchored. Adaptive density control may split, clone, or prune Gaussian primitives.

### Evidence and results

The clinical evaluation uses six AAPM Mayo Clinic Low-Dose CT volumes voxelized at `256 x 256 x 256`; digital radiographs are generated at `512 x 800`. Comparisons cover FDK, SART, NAF, R2-Gaussian, and 3DGR at 20, 40, and 60 views. Average source-reported results are:

| Views | RGS PSNR / SSIM | Next-best aggregate baseline | Difference |
|---:|---:|---:|---:|
| 20 | 34.68 / 0.909 | 3DGR 34.15 / 0.897 | +0.53 dB / +0.012 |
| 40 | 37.59 / 0.954 | 3DGR 37.17 / 0.945 | +0.42 dB / +0.009 |
| 60 | 38.97 / 0.975 | 3DGR 38.77 / 0.971 | +0.20 dB / +0.004 |

The paper's own tables do not show uniform per-volume dominance on every metric: for example, 3DGR reports higher SSIM than RGS on L109 and L506 in the 60-view setting. The correct conclusion is strong aggregate performance, not universal superiority.

The 40-view wavelet-prior ablation reports an average increase from 35.86 dB/0.936 to 37.22 dB/0.951. The curriculum ablation increases from 34.65 dB/0.922 to 37.62 dB/0.953. These ablations support both ingredients, but they do not isolate the impact of primitive count, compute budget, or every loss term.

The real-world experiment reconstructs a rhinoceros beetle from 40 projections over a full rotation and is qualitative. It supports feasibility on acquired projections but does not provide a ground-truth volume, numerical error, uncertainty, or clinical evidence.

### Limitations and implementation relevance

- The AAPM experiment simulates CBCT projections from CT volumes; it is not a prospective clinical sparse-view acquisition study.
- Results are point estimates with no repeated seeds, uncertainty intervals, statistical tests, or site/scanner variation.
- Runtime, peak memory, primitive growth after adaptive density control, reconstruction time, and matched-compute comparisons are absent.
- The method depends on an accurate projection model and acquisition geometry; robustness to calibration error, motion, metal, scatter, dose noise, and domain shift is not established.
- The paper states that source code is public, but the inspected official repository currently contains only a README. No environment, implementation, configs, data preparation, split manifest, or table scripts were available.
- Medical deployment would require calibrated uncertainty, artifact monitoring, clinically meaningful task evaluation, data governance, and expert review. PSNR/SSIM alone are insufficient.

## Related DEP Entries

1. [Hypercomplex MRI manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md) - both works reconstruct medical images from undersampled measurements and use representation design to preserve information. Hypercomplex MRI emphasizes compact learned channel coupling; RGS emphasizes a frequency-aware explicit attenuation field. Source basis: the inspected DEP manuscript's method, FastMRI setup, PSNR/SSIM tables, and limitations.
2. [AFIDAF Vision Filters manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md) - both assign complementary roles to spatial and spectral operators rather than forcing one representation to solve every scale. AFIDAF alternates image-domain filtering and Fourier mixing; RGS uses wavelet saliency to initialize spatial detail and raw-projection fitting to preserve physical consistency. Source basis: the inspected DEP method and ablation notes.
3. [CAR Avatar manuscript](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-Clothed%20Avatar%20CAR/clothed_avatar_car_manuscript.md) - both recover a 3D object from severely incomplete observations using explicit priors and staged refinement. CAR separates canonical coarse geometry from posed-space surface detail; RGS separates base attenuation from residual detail. Source basis: the inspected DEP's two-stage SDF method, experiments, and limitations.

## Synthesis Note

### Concept Bridge

Across RGS and the three related DEP entries, the transferable pattern is constrained division of labor. An underdetermined reconstruction is made tractable by assigning global structure and local detail to different components, choosing a representation compatible with the measurement physics, and staging optimization so the high-capacity component cannot absorb every residual. The shared engineering question is not simply which model is strongest, but which component should own each information scale and how that ownership is enforced and audited.

### Potential Implementations

1. **Spectral residual audit for CT reconstruction** - compute radial spectra, bandwise error, and edge preservation for any reconstruction method, then flag cases where global metrics hide high-frequency loss.
2. **Two-branch reconstruction research scaffold** - provide swappable base/detail initializers, measurement operators, staged training schedules, and matched-compute ablations for synthetic phantoms.
3. **Clinical review sidecar** - pair a candidate reconstruction with uncertainty, projection-consistency residuals, spectral-deviation maps, and source-view overlays for expert review rather than autonomous diagnosis.

### Deeper Relationship Observations

1. RGS and AFIDAF both use spectral structure as a routing signal, but neither treats the spectral transform as a complete solution: a spatially grounded component remains necessary to localize or reconstruct details.
2. RGS and CAR both reduce component competition through staged refinement. The coarse representation first establishes topology; detail optimization is activated only after a stable anchor exists.
3. RGS and Hypercomplex MRI show two distinct efficiency frontiers: explicit primitive allocation controls where capacity is spent, while Kronecker parameterization controls how weights are shared. Combining them would require measuring memory and time, not just parameter or primitive counts.

### Conceptual Similarities

1. **Incomplete evidence:** all four research objects reconstruct latent structure from measurements that do not fully determine it.
2. **Structured priors:** each introduces geometry, spectral organization, channel algebra, or canonical-body structure to narrow the solution space.
3. **Metric caution:** all need evaluation beyond aggregate fidelity because clinically or perceptually important local structure can fail while global scores remain acceptable.

### MVP Implementations with Code Mock-ups

1. **Bandwise Reconstruction Auditor** - a local tool that compares a reconstruction with a reference over frequency bands.

```python
def bandwise_error(reference, reconstruction, masks):
    ref_fft = fft2(reference)
    rec_fft = fft2(reconstruction)
    return {
        name: relative_l2(ref_fft * mask, rec_fft * mask)
        for name, mask in masks.items()
    }
```

2. **Curriculum Ablation Runner** - a research harness that freezes and unfreezes reconstruction branches under a declared schedule.

```python
for step, projections in enumerate(loader):
    detail.requires_grad_(step >= warmup_steps)
    loss = low_frequency_loss(base, projections)
    if step >= warmup_steps:
        loss += projection_loss(base + detail, projections)
    optimizer_step(loss)
```

3. **Projection-Consistency Review Card** - a non-diagnostic summary that exposes residual and spectral warnings for human review.

```python
def review_card(measured, forward_project, volume):
    predicted = forward_project(volume)
    return {
        "projection_rmse": rmse(measured, predicted),
        "high_band_ratio": high_band_ratio(predicted, measured),
        "requires_review": exceeds_declared_thresholds(predicted, measured),
    }
```

### Developer Challenges

1. Reproduce the projection geometry, rasterizer, wavelet preprocessing, adaptive density control, and baseline settings from an implementation that is not currently public.
2. Compare methods under matched reconstruction time, peak memory, primitive counts, and hardware while preserving deterministic data splits and random seeds.
3. Build spectral and spatial diagnostics that remain valid under noise, motion, scatter, metal artifacts, and calibration mismatch without leaking protected imaging data.

### Author Challenges

1. Publish the code, environment lock, configurations, projection-generation scripts, patient/volume split manifest, and commands that reproduce Tables I-III and Figures 5-9.
2. Report repeated-run uncertainty, matched-compute ablations, primitive-count trajectories, runtime, memory, and sensitivity to each schedule and initialization hyperparameter.
3. Validate on acquired multi-anatomy clinical sparse-view data with calibrated noise and geometry errors, task-relevant expert review, and explicit failure cases.

## Validation Notes

- Required paper identity, local integrity, random-selection, dedup, and no-source-upload checks passed.
- The paper was reviewed from complete PDF and full-paper HTML, not from the abstract alone.
- All numerical values above were transcribed from source Tables I-III or the experimental setup; no result is presented as independently reproduced.
- Exactly three related DEP entries were inspected and cited with concrete relevance reasons.
- Synthesis counts were checked: three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP code mock-ups, three developer challenges, and three author challenges.
- Public-safety review found no local absolute paths, usernames, drive letters, machine names, exact local execution timestamps, local timezone labels, or source-file attachments.
- The public artifact states that source documents were withheld locally.

## Attribution Block

- Source URL: https://arxiv.org/abs/2604.27552
  - Applies to: paper identity, metadata, abstract, version, and canonical source links.
- Source URL: https://arxiv.org/html/2604.27552
  - Applies to: full-paper method, experiments, results, ablations, and conclusion.
- Source URL: https://arxiv.org/pdf/2604.27552
  - Applies to: complete paper and visual review of figures and tables.
- Source URL: https://doi.org/10.48550/arXiv.2604.27552
  - Applies to: persistent arXiv identifier.
- Source URL: https://github.com/yqx7150/RGS
  - Applies to: current implementation-availability assessment.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md
  - Applies to: related medical reconstruction and representation synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md
  - Applies to: related spectral-spatial operator synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-Clothed%20Avatar%20CAR/clothed_avatar_car_manuscript.md
  - Applies to: related sparse-observation 3D reconstruction synthesis.
- Source-file policy: the source PDF, full-paper HTML, metadata HTML, e-print package, integrity records, extracted text, and temporary renders were retained locally and were not uploaded.
