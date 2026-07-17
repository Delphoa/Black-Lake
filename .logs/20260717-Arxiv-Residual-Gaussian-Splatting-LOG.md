# Arxiv DEP Log - Residual Gaussian Splatting

- Deposit date: 2026-07-17
- Actor: Codex scheduled research workflow
- Selected paper: *Residual Gaussian Splatting for Ultra Sparse-View CBCT Reconstruction*
- Authors: Jian Lin; Jiancheng Fang; Shaoyu Wang; Changan Lai; Yikun Zhang; Yang Chen; Qiegen Liu
- Stable identifiers: arXiv:2604.27552v1; arXiv DOI 10.48550/arXiv.2604.27552
- Selection method: `rg --files -g "*.pdf"` enumerated 75,777 PDFs. Their parent directories were normalized into 75,776 paper units, sorted, and sampled uniformly with PowerShell `Get-Random`. The accepted zero-based index was 48,493.
- Candidate and exclusion counts: 75,776 paper units; 0 duplicate exclusions; 0 other exclusions; 0 reselections. The first draw was accepted.
- Dedup validation: no match for the arXiv ID, arXiv DOI, normalized title, or slug family was found in Black-Lake `.logs`, `.reports`, `.lake-data`, the automation memory, relevant Black-Lake-Data DEP entries, or same-paper markers from the preceding 24 hours. Metadata-only author inventory rows were not treated as research deposits.

## Source Integrity

- Initial classification: `partial`. A valid full PDF existed, but full-paper HTML and companion provenance records were absent, so review paused.
- Repair: preserved the existing PDF; fetched official arXiv full-paper HTML, metadata HTML, and e-print payload through bounded direct-HTTPS requests. The archive README, attribution record, machine-readable summary, and verification report were updated locally.
- Final classification: `complete`. The PDF is 17,698,694 bytes, begins with `%PDF-`, and contains a trailing `%%EOF`. Official full-paper HTML is 324,487 bytes with 61,612 body characters, a document marker, 55 heading/section markers, and seven paper-structure term classes. The e-print is a valid 26,997,742-byte gzip/tar source package. Partial files: 0.
- Visual review: the 10-page PDF was text-extracted and selected pages containing the method diagrams, experimental setup, quantitative tables, ablations, and real-specimen evaluation were rendered and inspected. The renders were legible despite non-fatal font-substitution warnings.
- Source locality: PDF, full-paper HTML, metadata HTML, source archive, integrity records, and temporary renders remain local. No source file was copied, staged, attached, committed, or uploaded.

## Research Outcome

- Problem: projection-driven 3D Gaussian splatting tends to fit low-frequency CBCT structure before fine anatomy, producing over-smoothed reconstructions under ultra sparse views.
- Method: Residual Gaussian Splatting uses a single-level 2D wavelet decomposition to initialize a low-frequency base Gaussian set and a high-frequency-saliency detail set. It avoids directly fitting signed wavelet coefficients by learning a non-negative residual in the raw projection domain.
- Optimization: a 5,000-iteration low-frequency warm-up freezes the detail branch, followed by joint refinement to 25,000 iterations with projection fidelity and low-frequency consistency losses.
- Evidence: on six AAPM volumes, the source reports average 20-view performance of 34.68 dB PSNR and 0.909 SSIM, compared with 34.15/0.897 for the next-best aggregate baseline. The 40-view wavelet ablation improves from 35.86/0.936 to 37.22/0.951; the curriculum ablation improves from 34.65/0.922 to 37.62/0.953.
- Evidence limits: the clinical experiments use simulated projections from CT volumes; the real beetle experiment is qualitative; no repeated seeds, uncertainty intervals, runtime, memory, or independent reproduction are reported. The declared code repository currently contains only `README.md`, so the implementation claim is not presently actionable.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md` - medical reconstruction from undersampled measurements, PSNR/SSIM evaluation, and representation design under limited acquisition.
2. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - complementary image/Fourier operators and an explicit division between spatial detail and global spectral mixing.
3. `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` - sparse-observation 3D reconstruction using explicit geometric priors, coarse-to-fine decomposition, and detail refinement.

## Output Paths

- `.logs/20260717-Arxiv-Residual-Gaussian-Splatting-LOG.md`
- `.reports/BL-Arxiv-Residual-Gaussian-Splatting-20260717/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/README.md`
- `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Do the reported gains persist across repeated seeds, additional anatomies, calibrated dose/noise regimes, and truly acquired clinical sparse-view CBCT rather than simulated projections?
2. How much of the improvement comes from spectral initialization, the extra 30,000 detail primitives, the two-phase schedule, and the low-frequency consistency loss when compute and parameter budgets are matched?
3. Can the authors publish the implementation, environment, projection geometry, splits, and table-generation scripts needed to reproduce every baseline and ablation?

## Challenges

1. The selected archive unit failed the mandatory full-paper HTML gate and required a bounded local repair before review could begin.
2. Several quantitative claims are visually supported by source tables but lack repeated-run uncertainty, compute-cost reporting, and independent clinical validation.
3. The paper states that code is public, but the inspected official repository currently exposes only a README and no executable implementation.

## Outcome

All required public artifacts were generated from a verified complete local source bundle. Public records use date-only markers, public URLs, and repository-relative paths, and they explicitly state that source files were withheld locally.
