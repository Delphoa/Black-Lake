# Arxiv DEP Log: De-homogenized 3D Topologies

- Public date: 2026-08-01
- Paper: De-homogenization of optimal multi-scale 3D topologies
- Identifier: arXiv:1910.13002v1; DOI: https://doi.org/10.48550/arXiv.1910.13002; journal DOI: https://doi.org/10.1016/j.cma.2020.112979
- Selection method: `rg --files -g "*.pdf"` produced 75,960 PDFs in 75,957 unique PDF-parent units. A sorted unit list was frozen after identifier reconciliation, and PowerShell `Get-Random` uniformly selected zero-based index 10 from 133 eligible units.
- Counts: 75,957 candidates; 75,639 prior-ID exclusions; 185 identifier-incomplete units; 133 eligible units; 0 duplicate exclusions after the draw; 0 source-gate exclusions; 0 reselections.
- Dedup: exact arXiv ID, DOI, normalized title, and `dehomogenization-3d-topologies` slug were scanned in Black-Lake logs, reports, DEP entries, publication index, automation memory, and the metadata-only Black-Lake-Data inventory. No owning Arxiv DEP artifact or same-paper marker within 24 hours was found. Any inventory-only match would not have counted as an owning deposit; the selected paper had no match.
- Source integrity: complete before review. The retained PDF passed the size, `%PDF-`, and trailing `%%EOF` checks and parsed as a 22-page paper. The retained full-paper HTML passed the size, body-character, document-marker, heading, and paper-structure checks. No repair was required.
- Review basis: the complete local PDF and full-paper HTML were cross-checked against the public arXiv record, the peer-reviewed ScienceDirect record, and the DTU Orbit record. No author-designated implementation repository was established in the bounded public search.
- Related DEP entries: WKGM MRI Reconstruction; CAP Rank Sparsity; Flag Hardy Operators.
- Outputs: `.logs/20260801-Arxiv-Dehomogenized-3D-Topologies-LOG.md`; `.reports/BL-Arxiv-Dehomogenized-3D-Topologies-20260801/Report-Mark.md`; `.lake-data/DEP-E/DEP-E-20260801-Dehomogenized 3D Topology/README.md`; `.lake-data/DEP-E/DEP-E-20260801-Dehomogenized 3D Topology/dehomogenized_3d_topology_manuscript.md`; `.lake-data/DEP-E/.index/pubs-index.md`.

## Next-Review Questions

1. Can the coarse-to-fine mapping preserve compliance and volume constraints across multiple loading cases and singularity-rich domains?
2. What error and runtime frontier results when cell spacing, minimum feature size, mesh resolution, and post-processing are varied under matched budgets?
3. Can an openly released implementation reproduce the reported 3D examples and expose manufacturing, connectivity, and boundary-condition failure cases?

## Challenges

1. The reported 5–10% performance gap and three-orders-of-magnitude cost claim are source-reported comparisons, not an independent reproduction.
2. Minimum-feature-size enforcement can add material and violate the nominal volume constraint, with sensitivity varying by geometry and cell spacing.
3. The method is explicitly limited by orientation-field singularities and by the single-loading-case rank-3 parameterization used in the paper.

## Public Source Policy

Public sources: https://arxiv.org/abs/1910.13002; https://ar5iv.labs.arxiv.org/html/1910.13002; https://doi.org/10.1016/j.cma.2020.112979; https://www.sciencedirect.com/science/article/pii/S0045782520301626; https://orbit.dtu.dk/en/publications/de-homogenization-of-optimal-multi-scale-3d-topologies/

No PDF, HTML, TeX/source package, cache, extracted text, or other source file was staged, uploaded, or attached. Source files were withheld in the local archive.
