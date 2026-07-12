# DEP-E-20260712-Global NS Existence

#arxiv #mathematics #partial-differential-equations #navier-stokes #compressible-flow #global-existence #weak-solutions #strong-solutions #boundary-analysis #black-lake-arxiv-dep

This DEP-E contains a public-safe, source-grounded review of arXiv:2102.09229v2 and its 2022 version of record. It preserves the strong- and weak-solution statements, the boundary-specific effective-viscous-flux and commutator mechanism, the viscosity-exponent limitation, extraction provenance, dedup validation, and implementation/formalization implications. Original source files remain outside the deposit; only public URLs and generated analysis are included.

## Contents

- `README.md` - DEP inventory, context, summaries, relevance, and source attribution.
- `global_ns_existence_manuscript.md` - Schema-complete manuscript review with source metadata, evidence ledger, proof-mechanism synthesis, limitations, implementation paths, and verification appendix.

## Summary of Items

### `README.md`

Defines the deposit boundary and gives a complete two-file inventory. It records that no `.source/` directory exists because no original PDF, TeX package, or publisher file was collected for repository deposition.

### `global_ns_existence_manuscript.md`

Reviews the global-existence result for a two-dimensional compressible Navier-Stokes system with constant shear viscosity, density-dependent bulk viscosity, Navier-slip boundaries, large initial data, and possible vacuum. It distinguishes author theorem claims from reviewer synthesis, maps the conformal/Green-function/commutator proof architecture, records the open `1 < beta <= 4/3` regime, and connects the work to exactly three existing Black Lake deposits.

## Insights and Relevance

The paper is a useful Black Lake example of geometry functioning as proof infrastructure. A conformal map is not merely a coordinate convenience: angle preservation carries slip-boundary orthogonality into a representation where a dangerous singular term becomes a cancellable velocity difference. The deposit also reinforces a broader repository pattern: guarantees should remain attached to their parameter regimes, domain assumptions, evidence type, and verification status. Fermat Difference supplies theorem-regime review discipline, Physical Data AI supplies PDE/domain-fit translation, and RRT-CBF Motion supplies an invariance-and-boundary telemetry analogy. None is treated as proof evidence for this paper.

## Attribution Block

- Source URL: https://arxiv.org/abs/2102.09229
  - Applies to: `global_ns_existence_manuscript.md` and `README.md`.
  - Notes: Primary arXiv metadata, abstract, version history, and source links.
- Source URL: https://arxiv.org/pdf/2102.09229
  - Applies to: `global_ns_existence_manuscript.md`.
  - Notes: Primary paper inspected through a private extraction cache; not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2102.09229
  - Applies to: `global_ns_existence_manuscript.md`.
  - Notes: Persistent arXiv DOI.
- Source URL: https://link.springer.com/article/10.1007/s00205-022-01790-4
  - Applies to: `global_ns_existence_manuscript.md` and `README.md`.
  - Notes: Version-of-record metadata, publication history, abstract, and bibliography.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md` and deposit structure.
  - Notes: Live Black Lake deposition standard.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: provenance and related-repository context in `global_ns_existence_manuscript.md`.
  - Notes: Live related repository standard.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260709-Fermat%20Difference/fermat-difference-manuscript.md
  - Applies to: related-entry synthesis in `global_ns_existence_manuscript.md`.
  - Notes: Theorem-regime and proof-review context only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md
  - Applies to: related-entry synthesis in `global_ns_existence_manuscript.md`.
  - Notes: PDE/domain-fit implementation context only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - Applies to: related-entry synthesis in `global_ns_existence_manuscript.md`.
  - Notes: Invariance and boundary-constraint context only.
