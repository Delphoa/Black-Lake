# Arxiv DEP Job Log: Noisy Poisson Inference

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2301.00139v1, *On High dimensional Poisson models with measurement error: hypothesis testing for nonlinear nonconvex optimization*
- Selection result: accepted on the first uniform draw
- Source-integrity result: initial `partial`, repaired to verified `complete`
- Source-file policy: PDF, full-paper HTML, metadata HTML, TeX/source, cache, and extracted text remain local; none are deposited
- Extraction cache: initial miss; final `cached`

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"`
- PDF count: 75,777
- Unique parent-paper units: 75,776
- Sampling method: PowerShell `Get-Random` over the complete sorted unique parent-unit list
- Zero-based selected index: 45,743
- Exclusions: 0
- Reselections: 0

## Dedup Validation

No matching arXiv ID, DOI, normalized title, slug, Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, automation-memory entry, companion-repository DEP, or same-paper marker from the preceding 24 hours was found. A companion metadata inventory row names the author and paper, but it is not a research deposit and did not disqualify the first draw.

## Source Integrity and Cache

- Existing PDF: 1,385,919 bytes, `%PDF-` header and trailing `%%EOF` present
- Initial full-paper HTML: missing
- Public repair attempts: the official arXiv full-paper endpoint was unavailable; ar5iv requests redirected to the arXiv abstract record and were classified as metadata-only
- Verified repair: a local full-text HTML rendering was derived page-by-page from the verified 78-page PDF, with explicit provenance and no claim that it is an official arXiv rendering
- Verified HTML: 182,059 bytes, 170,802 body characters, 79 headings, all eight checked structure terms, and a document marker
- Metadata HTML: 42,317 bytes; abstract/metadata only
- Source archive: 5,848,348 bytes, 105 entries
- Remaining partial files: 0
- Cache: 2.322-second missing-only backfill via `pypdf`, `html-regex`, and `tarfile`
- Cache outputs: PDF text 175,819 bytes; HTML text 170,805 bytes; source text 348,082 bytes

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` - supplies a finite-sample uncertainty and distribution-envelope contrast for asymptotic test calibration.
2. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - connects measurement noise, inverse recovery, conditioning certificates, and perturbation-aware validation.
3. `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md` - connects mixed nonconvex optimization, coordinate-style algorithms, convergence boundaries, and scenario-dependent evidence.

## Output Paths

- Job log: `.logs/20260716-Arxiv-Noisy-Poisson-Inference-LOG.md`
- Phase log: `.logs/20260716-Arxiv-Noisy-Poisson-Inference-PHASE-LOG.md`
- Report-Mark: `.reports/BL-Arxiv-Noisy-Poisson-Inference-20260716/Report-Mark.md`
- DEP README: `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/README.md`
- DEP manuscript: `.lake-data/DEP-E/DEP-E-20260716-Noisy Poisson Inference/noisy_poisson_inference_manuscript.md`
- Publication index: `.lake-data/DEP-E/.index/pubs-index.md`
- Dedup pointer: `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. How robust are the Wald and score tests when the measurement-error covariance is estimated poorly, covariates are non-Gaussian, or count outcomes are overdispersed?
2. Do the reported selection and inference properties survive honest sample splitting, dependent multiple testing, and external clinical validation on a larger neuroimaging cohort?
3. Can the official implementation be reconciled with the paper's ADNI experiment and released with the exact data schema, tuning path, environment, and simulation seeds?

## Challenges

1. Official full-paper HTML was unavailable, and ar5iv returned the abstract record, so the archive required a provenance-labeled local rendering from the verified PDF before review.
2. The guarantees depend on dense high-dimensional regularity conditions, known or accurately estimated measurement-error covariance, and convergence to an appropriate local minimum.
3. The paper-linked code repository appears to contain county COVID/weather analysis rather than the reported ADNI workflow and lacks a README, license, or pinned environment.

## Known Shortfalls

- No proof was independently rederived and no simulation or ADNI analysis was rerun.
- The local HTML is a text rendering of the verified PDF, not an official publisher or arXiv HTML edition.
- The ADNI findings are observational, use a modest complete-case sample, and do not establish causality, diagnosis, or clinical utility.
- The published multiplicity treatment assumes independent p-values; dependence sensitivity was not reported.

## Submission Record

- Primary artifact commit: https://github.com/Delphoa/Black-Lake/commit/c64863af639d21e309c873b06a60ad006d48f6ce
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784203880533799
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source files
- Submission status: direct default-branch push succeeded; Slack notice delivered
