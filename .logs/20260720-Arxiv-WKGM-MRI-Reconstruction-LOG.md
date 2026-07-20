# 2026-07-20 - Arxiv DEP: WKGM MRI Reconstruction

- Actor/tool: Codex scheduled research workflow.
- Related DEP path: `.lake-data/DEP-E/DEP-E-20260720-WKGM MRI Reconstruction/`.
- Action: Uniformly selected, source-repaired, verified, reviewed, and synthesized *WKGM: Weight-K-space Generative Model for Parallel Imaging Reconstruction*.
- Inputs: Verified complete arXiv PDF, provenance-labeled PDF-derived full-text HTML, metadata, official journal record, official implementation repository, and exactly three related Black Lake DEP entries. Original source documents and derivatives were withheld locally.
- Outputs: `.reports/BL-Arxiv-WKGM-MRI-Reconstruction-20260720/Report-Mark.md`, `.lake-data/DEP-E/DEP-E-20260720-WKGM MRI Reconstruction/README.md`, `.lake-data/DEP-E/DEP-E-20260720-WKGM MRI Reconstruction/wkgm_mri_reconstruction_manuscript.md`, `.lake-data/DEP-E/.index/pubs-index.md`, and `.staging/arxiv-dep-dedup-index.json`.
- Outcome: Public-safe artifact set deposited directly to the default branch.
- Commit or PR: [Primary commit `b025afc`](https://github.com/Delphoa/Black-Lake/commit/b025afcbde123682df8d1acc58b8862a1cbc90b0).
- Slack notification: [Delivered to `#black-lake-artifacts`](https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784548280995699).
- Blockers: None.

## Random Selection and Deduplication

- Candidate enumeration: `rg --files -g "*.pdf"` over the local archive.
- Candidate unit: Unique PDF parent directory.
- PDF candidates: 75,778.
- Candidate paper units: 75,776.
- Random method: PowerShell `Get-Random` selected one uniform zero-based index over all candidate units, followed by identity and dedup validation.
- Selected zero-based index: 53,793.
- Selected paper: *WKGM: Weight-K-space Generative Model for Parallel Imaging Reconstruction*.
- Selected arXiv ID: `2205.03883v4` (base ID `2205.03883`).
- DOI: `10.1002/nbm.5005`; arXiv DOI `10.48550/arXiv.2205.03883`.
- Exclusions: 0.
- Duplicate rejections and reselections: 0.
- Dedup scan locations: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging/arxiv-dep-dedup-index.json`; automation memory; substantive Black-Lake-Data entries; and active-worktree same-paper markers within 24 hours.
- Dedup result: No arXiv ID, DOI, normalized-title, slug, artifact, memory, companion-repository, or recent-worktree match.

## Source Integrity Gate

- Initial classification: `partial`; the PDF was present and valid, but only a brief README was available and full-paper HTML was absent.
- Existing PDF: 1,884,860 bytes; `%PDF-` header present; trailing `%%EOF` present; 11 pages.
- Repair strategy: One bounded recent-paper archive pass with a 100 MB target ceiling, 20 MB partial ceiling, one attempt per artifact, no credentials, and no automatic restart.
- Endpoint findings: The official arXiv HTML route and the approved ar5iv fallback both returned abstract-only content byte-identical to the metadata page and were rejected.
- Final HTML repair: A provenance-labeled full-text HTML rendering was derived page-by-page from the verified PDF. It is 62,379 bytes with 59,163 body characters, 23 heading/section markers, five paper-structure terms, a document marker, the paper title, and a hash distinct from metadata.
- Source-package finding: The e-print endpoint returned a PDF rather than a TeX/source archive. The response was classified as invalid source-package evidence and preserved locally for inspection.
- Partial files: 0.
- Local records refreshed: README, attribution/provenance record, preflight manifest, machine-readable summary, and verification report.
- Final classification: `complete`; review began only after the PDF and full-text HTML gate passed.

## Extraction Cache

- Preflight: `pypdf` available; preferred `pdftotext`, PyMuPDF, PyPDF2, and pdfminer backends unavailable.
- Initial cache lookup: Miss.
- Mode: `missing-only`; network disabled because source repair had already completed the local unit.
- PDF extraction: `pypdf`, status `ok`, 62,576 text bytes; fallback reason `pdftotext unavailable`.
- HTML extraction: `html-regex`, status `ok`, 59,793 text bytes.
- Source extraction: Not available because no valid TeX/source archive was obtained.
- Extraction command elapsed: 2.458 seconds.
- Final cache status: `cached`.

## Evidence and Related DEP Validation

- Paper evidence: Full 11-page PDF, PDF-derived full-text HTML, equations 1-19, Algorithms 1-2, Tables I-VIII, Figures 1-13, experimental settings, conclusion, and references were inspected. Evidence-bearing pages 4 and 7-11 were rendered for visual review.
- Publisher context: Wiley identifies the journal version as *NMR in Biomedicine* 36(11), e5005, first published 2023-08-07, DOI `10.1002/nbm.5005`.
- Official implementation: `yqx7150/WKGM` exposes training and demonstration scripts plus configuration files. The README states non-commercial use; no root `LICENSE` or `requirements.txt` was found, and the code was not executed.
- Core reported result: On T2 Transverse Brain with 2D Poisson sampling at `R=10`, SVD-WKGM reports 31.69 dB PSNR and 0.841 SSIM versus 29.75/0.823 for SAKE and 25.00/0.737 for the no-weight ablation.
- Counterevidence: On knee Cartesian `R=3`, supervised k-space deep learning reports higher PSNR/SSIM than SVD-WKGM for both displayed slices; the advantage reverses on the displayed 2D Poisson `R=6` cases.
- Principal evidence gap: Point estimates come from narrow slice/image settings without repeated seeds, confidence intervals, pathology-preservation analysis, external clinical readers, runtime, peak memory, or end-to-end compute accounting.
- Related DEP 1: `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md` - direct accelerated-MRI reconstruction neighbor connecting complex k-space representation to matched resource and clinical-evaluation gates.
- Related DEP 2: `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md` - medical inverse-reconstruction neighbor focused on high-frequency detail preservation under sparse measurements.
- Related DEP 3: `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - structured inverse-problem neighbor connecting Fourier/Hankel representations, measurement constraints, and conditioning.

## Submission Gate

- Public-output allowlist: Exactly the generated `.logs`, `.reports`, DEP-E Markdown/README, DEP-E publication index, and dedup JSON paths for this run.
- Source-upload denylist: PDFs, HTML, metadata pages, source archives, cache records, extracted source text, temporary renderings, local archive paths, and `.source/` directories.
- Public safety: No local absolute path, username, home directory, drive path, machine name, exact execution timestamp, or local timezone label is permitted.
- Source policy: Source files and derivatives remain local and withheld. No `.source/` directory was created.
- Repository submission: Direct default-branch push succeeded in primary commit [`b025afc`](https://github.com/Delphoa/Black-Lake/commit/b025afcbde123682df8d1acc58b8862a1cbc90b0) after rebasing onto concurrent DEP updates.
- Staged allowlist result: Exactly seven public Markdown/JSON paths; zero forbidden source-document, cache, extracted-text, archive, temporary-render, or `.source/` paths.
- Slack notification: [Delivered to `#black-lake-artifacts`](https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784548280995699).

## Next-Review Questions

1. Do WKGM and SVD-WKGM retain their reported gains across complete multi-subject cohorts, repeated seeds, scanner vendors, anatomies, coils, masks, acceleration factors, and pathology-bearing cases?
2. What are the end-to-end latency, peak memory, energy, and singular-value-decomposition costs of 1,000 predictor-corrector steps with data consistency and optional SAKE updates?
3. Can a pinned, licensed environment reproduce Tables I-VIII and separate the gains from weighting, six-channel augmentation, score modeling, data consistency, and low-rank projection at matched compute?

## Challenges

1. The strongest comparisons are point estimates over incompletely specified slice-level test sets, so statistical and clinical generalization cannot be inferred.
2. SVD-WKGM combines the learned prior with SAKE, making attribution and compute fairness difficult without matched ablations and resource accounting.
3. The official repository improves inspectability but lacks a root license file, dependency lock, dataset manifest, and verified table-reproduction workflow.
