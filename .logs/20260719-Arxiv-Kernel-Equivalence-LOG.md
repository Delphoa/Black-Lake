# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P04`
- Public-safe run date: 2026-07-19
- Outcome: reviewed, validated, and prepared for submission
- Selected paper: *Kernel Tests of Equivalence*
- Stable identifier: `arXiv:2603.10886v2`
- Canonical URL: https://arxiv.org/abs/2603.10886

## Random Selection

- Method: `rg --files -g "*.pdf"`, unique PDF-parent units, uniform PowerShell `Get-Random` index.
- PDF candidates: 75,778; candidate paper units: 75,776.
- Selected one-based index: 28,880.
- Random selection succeeded on the first draw and used no machine, user, path, timezone, or timestamp-derived seed.

## Deduplication and Reselection

- Scanned Black Lake public artifact/index surfaces, this automation memory, current Black-Lake-Data relevant records, and the current-job selected set.
- Keys: arXiv ID, DOI, normalized title, `Kernel-Equivalence` slug, artifact markers, and markers on or after the public-safe cutoff date 2026-07-18.
- Prior used-paper match: none; current-job match: none.
- Duplicate exclusions: 0; reselections: 0.

## Source Integrity

- Initial classification: partial; valid PDF present, full-paper HTML absent.
- Repair: one bounded attempt retrieved official full-paper HTML, metadata HTML, and source package while preserving the PDF.
- PDF: 776,081 bytes; `%PDF-` and trailing `%%EOF` passed.
- Full-paper HTML: 981,932 bytes; 172,614 body characters; document marker; 102 heading markers; eight structure terms; no rejected payload pattern.
- Unexpected partials: 0; cache status: `cached`; PDF, HTML, and source extraction succeeded.
- Final state: complete. All original and extracted source files remain local.

## Public Outputs

- `.logs/20260719-Arxiv-Kernel-Equivalence-LOG.md`
- `.reports/BL-Arxiv-Kernel-Equivalence-20260719/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260719-Kernel Equivalence/README.md`
- `.lake-data/DEP-E/DEP-E-20260719-Kernel Equivalence/kernel_equivalence_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` - finite-sample confidence coverage, calibration assumptions, and decision thresholds.
2. `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md` - asymptotic hypothesis tests, finite-sample Type-I error, and measurement-model misspecification.
3. `.lake-data/DEP-E/DEP-E-20260718-Transport Convexity/transport_convexity_manuscript.md` - distribution geometry, transform-dependent comparison, and the need to tie a distance to a generative assumption.

## Submission Gate

- Allowlist: generated Markdown plus required publication-index Markdown and dedup JSON.
- `.source/`: not created. Source-document upload: none.
- Public sanitization withholds local paths, user/machine context, timezone labels, and exact execution timestamps.
