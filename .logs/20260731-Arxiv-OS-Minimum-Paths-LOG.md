# Arxiv DEP Job Log: OS Minimum Paths

## Public-Safe Run Summary

- Selected paper: *Paths and Intersections: Minimum Realization of Okamura-Seymour Instances* by Yu Chen, Pavlo Pylyavskyy, and Zihan Tan.
- Stable identifiers: arXiv:2607.02883v1; DOI: [10.48550/arXiv.2607.02883](https://doi.org/10.48550/arXiv.2607.02883).
- Selection method: enumerated 75,960 PDFs with `rg --files -g "*.pdf"`, collapsed them to 75,957 unique parent-directory paper units, then used a uniform PowerShell `Get-Random` zero-based draw. Draw index 349 was accepted.
- Dedup and reselection: zero matching arXiv-ID, DOI, normalized-title, or slug records were found in the dedup pointer, Black Lake artifacts, automation memory, or the available Black-Lake-Data checkout. No same-paper marker was found within 24 hours. Exclusions: 0; reselections: 0.
- Source integrity: the selected unit began partial (valid PDF but no full-paper HTML). One bounded brokered repair preserved the PDF and added validated full-paper HTML plus metadata. The final state is complete; source-package availability is recorded as unavailable.
- Cache: miss to `cached` in missing-only mode. PDF text used the `pypdf` fallback because `pdftotext` was unavailable; HTML text used `html-regex`; source text is absent because no source package was available.

## Public Outputs

- `.logs/20260731-Arxiv-OS-Minimum-Paths-LOG.md`
- `.logs/20260731-Arxiv-OS-Minimum-Paths-PHASE-LOG.md`
- `.reports/BL-Arxiv-OS-Minimum-Paths-20260731/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260731-OS Minimum Paths/README.md`
- `.lake-data/DEP-E/DEP-E-20260731-OS Minimum Paths/os_minimum_paths_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. What explicit polynomial bound follows from the construction, and which parts dominate as the terminal count grows?
2. Can a reference implementation enumerate non-isomorphic arrangements of the fixed medial template without duplicate work?
3. How robust are the repelling-pair and cut-count computations under noisy or approximately metric distance data?

## Challenges

1. The source is theorem-driven, so no independently reproducible benchmark or implementation was available to test runtime claims.
2. The source package was unavailable; the review relied on the validated PDF and full-paper HTML, with source text absent from the cache.
3. The proof chain invokes earlier path-structure and uncrossing results that were inspected as citations but not independently formalized here.

## Source-Handling Confirmation

Original PDFs, full-paper HTML, metadata HTML, source-package records, extracted text, cache files, repair receipts, and private verification records remain local. No source file, cache output, or `.source/` directory was staged, committed, uploaded, or attached.
