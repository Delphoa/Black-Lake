# 2026-07-12 - Arxiv Global NS Existence Job Log

## Public-Safe Run Summary

- `Selected paper`: Global Existence of Strong and Weak Solutions to 2D Compressible Navier-Stokes System in Bounded Domains with Large Data and Vacuum.
- `Stable identifiers`: arXiv:2102.09229v2; arXiv DOI 10.48550/arXiv.2102.09229; publisher DOI 10.1007/s00205-022-01790-4.
- `Selection method`: Enumerated PDFs with `rg --files -g "*.pdf"`, treated each unique PDF parent directory as one paper unit, and used PowerShell `Get-Random` for one uniform zero-based index.
- `Candidate count`: 75,761 PDF-backed paper units.
- `Selected index`: 17,885.
- `Duplicate exclusions`: 0.
- `Same-paper 24-hour exclusions`: 0.
- `Reselections`: 0.
- `Source-file deposition`: No source files collected for repository deposition; no `.source/` directory created.

## Dedup and Eligibility

The arXiv ID, publisher DOI, normalized title, and slug were checked against `.staging/arxiv-dep-dedup-index.json`, Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and Black-Lake-Data repository search. No earlier Arxiv DEP artifact or same-paper marker was found. The first random draw was accepted.

## Cache and Source Review

Extractor preflight found `pypdf` available while `pdftotext`, PyMuPDF, PyPDF2, and pdfminer were unavailable. Initial cache lookup was a miss. Local `missing-only` extraction created a partial cache in 0.944 seconds: `pypdf` produced 72,259 bytes of PDF text; local HTML and source-package inputs were absent. No network backfill was needed for paper-body synthesis. The public arXiv metadata page and Springer version-of-record page were inspected for title, authors, dates, abstract, venue, DOI, and publication status.

The review inspected the complete extracted paper, including definitions, Theorems 1.1 and 1.2, the effective-viscous-flux construction, pull-back Green's function, commutator estimates, density upper bound, higher-order estimates, approximation/compactness arguments, stated open regime, and bibliography. The proof was not formally verified or independently reproduced.

## Output Paths

- `.logs/20260712-Arxiv-Global-NS-Existence-LOG.md`
- `.logs/20260712-Arxiv-Global-NS-Existence-PHASE-LOG.md`
- `.reports/BL-Arxiv-Global-NS-Existence-20260712/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/README.md`
- `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-Fermat Difference/fermat-difference-manuscript.md` - a theorem-centered global-solution classification artifact with explicit parameter regimes, proof dependencies, and formal-verification limits.
2. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` - a PDE-shaped implementation artifact that makes equation choice and domain fit explicit design constraints.
3. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` - a dynamical-systems artifact centered on forward invariance, boundary constraints, approximation, and the gap between mathematical conditions and computational evidence.

## Next-Review Questions

1. Can the boundary commutator argument be extended beyond simply connected planar domains or beyond the stated Navier-slip condition without losing the density upper bound?
2. Is the technical threshold `beta > 4/3` sharp, or can a new estimate close the source-identified open regime `1 < beta <= 4/3`?
3. Can the strong- and weak-solution approximation steps be formalized into a machine-checkable dependency map that exposes every compactness and uniqueness assumption?

## Challenges

1. PDF extraction was usable but introduced encoding corruption in mathematical symbols, so claims had to be cross-checked against theorem numbering and surrounding prose.
2. The paper is a proof artifact rather than an experimental study; this run could review the argument structure but could not independently verify every estimate or compactness step.
3. Existing Black Lake entries have only cross-domain overlap, requiring careful separation of conceptual bridges from mathematical validation.

## Outcome

The source-first review, schema-complete DEP manuscript, Report-Mark synthesis, public-safe logs, and dedup pointer were prepared as one atomic Black Lake artifact set. Repository submission and Slack notification are recorded in the completion report after validation.
