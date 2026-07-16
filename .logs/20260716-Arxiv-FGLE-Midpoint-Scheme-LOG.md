# Arxiv DEP Job Log: FGLE Midpoint Scheme

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:1601.02301v1, *An implicit midpoint difference scheme for the fractional Ginzburg-Landau equation*
- Selection: first uniform draw; zero exclusions and reselections
- Source integrity: initial `partial`, repaired to verified `complete`
- Cache: initial miss; final `cached`
- Source policy: paper files, metadata, cache, and extracted text remain local; none are deposited

## Random Selection

- Enumeration: `rg --files -g "*.pdf"`
- PDFs / parent units: 75,777 / 75,776
- Sampling: PowerShell `Get-Random` over sorted unique paper units
- Zero-based index: 47,945
- Exclusions / reselections: 0 / 0

## Dedup Validation

No prior matching versioned/base arXiv ID, journal DOI, arXiv DOI, normalized title, slug, job log, report, DEP-E manuscript, dedup pointer, automation-memory entry, companion-repository entry, or 24-hour same-paper marker was found. The first draw was eligible.

## Source Integrity and Cache

- PDF: 1,743,106 bytes; `%PDF-` header and trailing `%%EOF` valid
- Repair: official arXiv HTML was unavailable after bounded retries; approved ar5iv full-paper HTML and official metadata HTML were fetched
- Full HTML: 2,651,436 bytes; 123,389 body characters; two document markers; 51 headings; six paper-structure terms
- Metadata: 42,428 bytes; metadata only; partial files: 0; source package: not collected
- Cache: miss to `cached` in about 6.3 seconds using `pypdf` / `html-regex`
- PDF / HTML / source text: 53,161 / 123,257 / 0 bytes

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md` - shares nonlinear-PDE a priori estimates, theorem assumptions, existence/uniqueness distinctions, and proof-verification boundaries.
2. `.lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md` - connects nonlocal operator norm estimates, discrete representation, imported lemmas, and finite-grid evidence limits.
3. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - supplies independent-solver, mesh-error, mismatch, calibration, timing, and uncertainty requirements for synthetic PDE studies.

## Output Paths

- `.logs/20260716-Arxiv-FGLE-Midpoint-Scheme-LOG.md`
- `.logs/20260716-Arxiv-FGLE-Midpoint-Scheme-PHASE-LOG.md`
- `.reports/BL-Arxiv-FGLE-Midpoint-Scheme-20260716/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260716-FGLE Midpoint Scheme/README.md`
- `.lake-data/DEP-E/DEP-E-20260716-FGLE Midpoint Scheme/fgle_midpoint_scheme_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Does the proposed nonlinear inner iteration converge throughout the theorem's parameter regime, and how do iteration error and failure affect the reported second-order accuracy?
2. How large are the finite-domain truncation and exterior-boundary errors relative to `O(tau^2+h^2)` across fractional orders and final times?
3. Can manufactured fractional solutions and an independent spectral or finite-element solver reproduce the convergence orders at competitive runtime and memory?

## Challenges

1. The convergence theorem avoids a mesh-ratio restriction, but the uniqueness theorem assumes `tau <= C h`, so “unconditional” must be interpreted property by property.
2. Fractional-order tables use a finer run of the same scheme as reference and do not independently validate the nonlocal discretization.
3. No code, iteration-convergence analysis, timing, complexity, memory, domain-sensitivity, or comparator supports the practical efficiency claim.

## Known Shortfalls

- No proof was formally checked and no numerical result was reproduced.
- No official code was identified; solver residuals, iteration counts, hardware, runtime, memory, and scaling remain unknown.
- Physical validation, independent fractional truth, domain-truncation error, and sensitivity to non-smooth data remain open.
- The public deposit contains review text and derived status JSON only; source documents and cache outputs are withheld.

## Submission Record

- Primary artifact commit: https://github.com/Delphoa/Black-Lake/commit/0a939dfc7ad7c19d8ed0f1609c29a52648ab42c8
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784218921216309
- Source-upload gate: passed with exactly seven Markdown/JSON artifacts and zero source-document artifacts
- Submission status: direct default-branch push succeeded; Slack notice delivered
