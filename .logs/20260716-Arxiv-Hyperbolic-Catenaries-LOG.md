# Arxiv DEP Job Log: Hyperbolic Catenaries

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: *Catenaries and minimal surfaces of revolution in hyperbolic space*
- Authors: Luiz C. B. da Silva; Rafael López
- arXiv: https://arxiv.org/abs/2211.15297
- Journal DOI: https://doi.org/10.1017/prm.2024.56
- Source state: initially `partial`; repaired and verified `complete` before review
- Source policy: PDF, full-paper HTML, metadata HTML, TeX/source, extracted text, and caches were retained locally; no source file was copied into the repository or attached to Slack
- Submission status: generated and pending validated repository submission

## Random Selection

- Enumeration command: `rg --files -g "*.pdf"`
- Paper unit: each unique PDF parent directory
- PDF candidates enumerated: 75,777
- Eligible paper-unit candidates: 75,776
- Random method: uniform PowerShell `Get-Random` index over the complete paper-unit array
- Selected zero-based index: 43,368
- Exclusions before acceptance: 0
- Duplicate reselections: 0
- Same-paper markers within the preceding 24 hours: 0

## Dedup Validation

The selected arXiv ID, journal DOI, arXiv DOI, normalized title, and slug were checked against `.staging/arxiv-dep-dedup-index.json`, Black Lake `.logs`, `.reports`, and `.lake-data`, automation memory, relevant Black-Lake-Data results, and active-worktree artifacts. Black-Lake-Data contained only an author-inventory row, not a prior DEP or Arxiv DEP artifact. No exclusion marker was found, so the first draw was accepted.

## Source Integrity and Cache

- Existing PDF: 277,685 bytes; `%PDF-` header; trailing `%%EOF`; preserved without redownload
- Full-paper HTML: 2,239,423 bytes; 221,596 body characters; document marker; 44 heading/section markers; four paper-structure terms
- Metadata HTML: 41,096 bytes; metadata only and never counted as the paper
- TeX/source: 33,851-byte validated archive retained locally
- Partial files after repair: 0
- Initial cache: miss
- Extraction mode: `missing-only`
- Final cache: `cached`
- Extractors: `pypdf`, `html-regex`, and `tarfile`; `pypdf` was the fallback because `pdftotext` was unavailable
- Text outputs: 43,846 bytes PDF text; 193,203 bytes HTML text; 78,385 bytes source text

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Flag Hardy Operators/flag_hardy_operators_manuscript.md` - connects symmetry-adapted analysis on a non-Euclidean homogeneous space with the need to preserve the geometry dictated by the ambient group.
2. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - connects continuous curves on a Lie group, coordinate gauges, and invariant geometric constraints to practical estimation.
3. `.lake-data/DEP-A/DEP-A-20260714-CoreMem Geometry/2606.18406-whitepaper-review.md` - supplies a useful negative comparison: it audits when “Riemannian” language is not backed by a genuine manifold metric, unlike the selected paper's explicit hyperbolic and Lorentzian construction.

## Output Paths

- `.logs/20260716-Arxiv-Hyperbolic-Catenaries-LOG.md`
- `.logs/20260716-Arxiv-Hyperbolic-Catenaries-PHASE-LOG.md`
- `.reports/BL-Arxiv-Hyperbolic-Catenaries-20260716/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260716-Hyperbolic Catenaries/README.md`
- `.lake-data/DEP-E/DEP-E-20260716-Hyperbolic Catenaries/hyperbolic_catenaries_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Can the hyperbolic and parabolic extrinsic catenaries be characterized intrinsically, without choosing the hyperboloid embedding?
2. What first integrals, boundary-value existence results, and stability properties hold beyond the elliptic family?
3. Can the numerical generating curves in the journal version be reproduced from published initial conditions and independently verified to have zero mean curvature?

## Challenges

1. The sampled archive unit lacked full-paper HTML, so review had to stop for bounded repair and complete-source verification.
2. The arXiv v2 and journal version differ materially in exposition, figures, theorem wording, and one corrected curvature scaling, requiring version-aware synthesis.
3. No official numerical code or initial-condition manifest was identified, and both inspected versions retain a likely `cosh(u/u)` typographical defect in the main equivalence calculation.

## Known Shortfalls

- The differential-geometric proofs were reconstructed and cross-checked but not formally verified.
- The journal figure-generating ODEs were not independently solved.
- No code, numerical parameters, stability computation, boundary-value theorem, or global minimizer analysis was reproduced.
- The review treats the journal theorem as the authoritative formulation while preserving differences from arXiv v2.

## Submission Record

- Primary artifact commit: https://github.com/Delphoa/Black-Lake/commit/8f2019d8805d3ddc4dcd939ebb5dec954cb6dc99
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784183767449989
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source files
- Submission status: direct default-branch push succeeded; Slack notice delivered
