# Arxiv DEP Job Log — SLFE Redundancy Reduction

## Run Summary

- Selected work: *Start Late or Finish Early: A Distributed Graph Processing System with Redundancy Reduction* (arXiv:1805.12305; DOI: [10.48550/arXiv.1805.12305](https://doi.org/10.48550/arXiv.1805.12305)).
- Deposit class: DEP-E research.
- Source-integrity result: complete after a bounded local repair. The preserved PDF passed header and EOF checks; the repaired full-paper HTML passed size, body-text, document-marker, heading, and paper-structure checks.
- Source policy: PDF, metadata HTML, full-paper HTML, cache material, extraction text, and repair receipts remain in the local source archive. No source file was uploaded or deposited.

## Random Selection and Deduplication

- Candidate enumeration: `rg --files -g "*.pdf"` returned 75,959 PDFs.
- Selection method: a uniformly random PowerShell `Get-Random` index selected candidate 6,515 (one-based); its parent directory was treated as the paper evidence unit and nearby metadata files were inspected.
- Accepted identity: arXiv:1805.12305; normalized title: `Start Late or Finish Early A Distributed Graph Processing System with Redundancy Reduction`; slug: `SLFE-Redundancy-Reduction`.
- Exclusions before acceptance: 0. Reselections: 0.
- Dedup validation: no match for arXiv ID, DOI, normalized title, or slug was found in the public dedup pointer, Black-Lake logs/reports/DEP artifacts, automation memory, or current remote Black-Lake records. The related Black-Lake-Data search found only a metadata-inventory row, not a prior research DEP, so it was not a duplicate.

## Public Outputs

- `.logs/20260730-Arxiv-SLFE-Redundancy-Reduction-LOG.md`
- `.logs/20260730-Arxiv-SLFE-Redundancy-Reduction-PHASE-LOG.md`
- `.reports/BL-Arxiv-SLFE-Redundancy-Reduction-20260730/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260730-SLFE Redundancy Review/README.md`
- `.lake-data/DEP-E/DEP-E-20260730-SLFE Redundancy Review/slfe_redundancy_manuscript.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Does RRG remain correct and cost-effective on dynamic graphs whose topology changes between jobs?
2. How does the method behave on tail-latency, energy, and failure-recovery measures absent from the reported benchmark tables?
3. Can the published API and evaluation be independently reproduced on current graph-processing runtimes and heterogeneous clusters?

## Challenges

1. The selected local unit initially lacked full-paper HTML and required bounded repair before review could begin.
2. The source-package endpoint was unavailable under the collector's redirect policy, so the review relies on the verified PDF and full-paper HTML rather than TeX sources.
3. No author-linked implementation was identified in the inspected canonical record, and no benchmark was independently rerun.
