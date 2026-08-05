# Arxiv DEP Log: Graph Filter Banks

- Run date: 2026-08-05.
- Status: complete.
- Selected paper: *Scalable $M$-Channel Critically Sampled Filter Banks for Graph Signals*.
- Authors: Shuni Li; Yan Jin; David I. Shuman.
- Identifier: arXiv:1608.03171v5.
- Public-safe source state: complete after one bounded brokered repair; source files remain local and were not uploaded.

## Selection and Deduplication

- Candidate enumeration used `rg --files -g "*.pdf"` against the local arXiv archive.
- Candidate count: 75,960 PDFs.
- Paper-unit count: 75,957 unique PDF parent directories.
- Selection method: uniform PowerShell `Get-Random` over the sorted unique paper-unit list, using zero-based index 23,807.
- Initial source classification: partial because the valid PDF existed without metadata HTML or full-paper HTML.
- Repair: one bounded brokered single-paper repair preserved the valid PDF and added metadata HTML plus verified full-paper HTML; the optional TeX/source package was unavailable through the permitted redirect policy.
- Dedup scan: no exact arXiv-ID, DOI, normalized-title, slug, prior Arxiv DEP artifact, or same-paper-within-24-hours marker was found in the checked Black-Lake artifacts, automation memory, or related Black-Lake-Data inventory.
- Exclusion counts: duplicate exclusions 0; other exclusions 0; source-gate exclusions 0 after repair; same-paper 24-hour exclusions 0; reselections 0.
- Acceptance: first random draw accepted after repair validation.

## Source Integrity Gate

- PDF: 20,196,142 bytes; `%PDF-` header present; trailing `%%EOF` present.
- Full-paper HTML: 1,689,113 bytes; 154,784 body characters after script/style removal; 89 heading markers; three document markers; eight paper-structure terms.
- Metadata HTML: present and non-empty.
- Partial or temporary files: none remained in the selected unit.
- Local archive records updated by the repair workflow: README, provenance record, machine-readable summary, verification report, and immutable acquisition receipt.
- Source package: unavailable; no source package was copied, staged, committed, uploaded, or attached.

## Public Outputs

- `.logs/20260805-Arxiv-Graph-Filter-Banks-LOG.md`
- `.reports/BL-Arxiv-Graph-Filter-Banks-20260805/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260805-Graph Filter Banks/README.md`
- `.lake-data/DEP-E/DEP-E-20260805-Graph Filter Banks/graph_filter_banks_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Can the fast transform retain its reconstruction and compression behavior on changing, directed, weighted, or temporally evolving graphs without rebuilding the full sampling plan for every signal?
2. What matched-compute uncertainty and failure distributions appear when polynomial order, conjugate-gradient tolerance, band count, and sampling allocation are jointly swept?
3. Can a public implementation reproduce the reported large-graph timing and temperature-signal results while accounting for preprocessing, memory, synthesis, and rerun costs?

## Challenges

1. The exact construction is conceptually clean but depends on eigendecomposition, while the fast construction introduces approximation and interpolation error that must be monitored together.
2. Signal-adapted sampling improves source-reported reconstruction error, but it requires a signal-specific sampling decision and can complicate caching, fairness, and reproducibility.
3. The paper reports strong source-scale results, yet code availability, repeated-seed uncertainty, and deployment behavior on changing graph streams remain unresolved.

## Attribution Block

- Source URL: https://arxiv.org/abs/1608.03171
  - Applies to: selection metadata, source identity, abstract, and public provenance.
- Source URL: https://arxiv.org/pdf/1608.03171
  - Applies to: full-paper review and reported method/results.
- Source URL: https://ar5iv.labs.arxiv.org/html/1608.03171
  - Applies to: full-paper HTML structure and cross-checking.
- Source URL: https://doi.org/10.48550/arXiv.1608.03171
  - Applies to: persistent arXiv identifier.
- Source URL: https://doi.org/10.1109/TSP.2019.2923142
  - Applies to: journal-publication metadata.
- Source files: withheld locally; no original PDF, HTML, metadata page, source package, cache, extracted text, or verification record is redistributed.
  - Applies to: all generated public artifacts.
