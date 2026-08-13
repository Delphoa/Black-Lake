# Black Lake Arxiv DEP — Rauzy Neighbors

Public-safe run date: 2026-08-05

- Black Lake Arxiv DEP selected and reviewed one arXiv archive paper: Neighbors of self-affine tiles and Rauzy Fractals, arXiv:2511.16442v1.
- Random selection: rg --files -g "*.pdf" enumerated 75,960 PDFs, collapsed to 75,957 unique parent-directory paper units, then PowerShell Get-Random selected zero-based index 68,395. A failed path helper was discarded before acceptance; no manual substitution was used.
- Eligibility and deduplication: scanned Black-Lake .logs, .reports, .lake-data, .staging, automation memory, and Black-Lake-Data context for arXiv ID, DOI, normalized title, slug, automation markers, and recent markers. Exclusions: 0. Reselections: 0. Public 24-hour cutoff: 2026-08-04.
- Source gate: the unit was initially partial because full-paper HTML was absent. One bounded broker-mediated repair preserved the valid PDF and produced verified full-paper HTML, metadata, provenance, and verification companions. PDF and HTML gates passed; the optional source package was unavailable.
- Related DEP entries selected: DEP-E-20260717-Moran Spectra; DEP-E-20260716-Flag Hardy Operators; DEP-E-20260716-Acoustic Phase Retrieval.
- Outputs: .reports/BL-Arxiv-Neighbours-Rauzy-20260805/Report-Mark.md; .lake-data/DEP-E/DEP-E-20260805-Rauzy Neighbors/README.md; .lake-data/DEP-E/DEP-E-20260805-Rauzy Neighbors/rauzy_neighbors_manuscript.md.
- Validation: manuscript schema and title contract, exact-three synthesis blocks, source-reference coverage, DEP inventory, publication-index ownership, public-safety sanitization, staged no-source allowlist, and Git whitespace checks are required before submission. PDF, HTML, metadata, source archive, cache, and local paths are withheld; no source files were uploaded.

## Questions for the Next Reviewer

1. Can the C-corona and reduction loop be independently implemented on the two worked substitutions while preserving the paper's graph conventions?
2. Which broader graph-directed iterated-function-system classes retain the finite contact-degree bound required by the termination proof?
3. How should graph fixed-point evidence be combined with Fourier or spectral diagnostics when a tiling claim is only partially observable?

## Challenges for the Next Review Pass

1. Re-derive the contact-degree connectivity lemma and identify every imported theorem needed for the finite bound.
2. Reproduce the two example graph constructions from the stated substitutions using a small auditable implementation.
3. Separate the paper's proof guarantees from the practical cost of enumerating ambient graphs and reducing coronas.
