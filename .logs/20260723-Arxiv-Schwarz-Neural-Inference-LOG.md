# Arxiv DEP Job Log: Schwarz Neural Inference

## Job Summary

This source-first review deposited a public-safe analysis of *Operator Learning with Domain Decomposition for Geometry Generalization in PDE Solving* (arXiv:2504.00510v2; ICLR 2026). The work trains a neural operator on local polygonal PDE problems and applies Schwarz Neural Inference (SNI) to iteratively assemble solutions on unseen global geometries. Source documents, extraction caches, provenance records, and inspection renders were retained locally and were not copied into this repository.

## Random Selection

- Method: enumerate PDFs with `rg --files -g "*.pdf"`, collapse paths to unique parent paper units, then draw a uniform random integer with PowerShell `Get-Random`.
- PDF count observed: 75,780.
- Candidate paper-unit count: 75,777.
- Zero-based random index: 57,700.
- Selection outcome: first draw accepted.
- Duplicate exclusions: 0.
- Reselections: 0.

## Deduplication Validation

The public dedup index, Black Lake logs, reports, DEP-E deposits, automation memory, active recent remote branches, and relevant Black-Lake-Data content were checked for arXiv ID `2504.00510`, arXiv DOI `10.48550/arXiv.2504.00510`, normalized title, and slug. The only companion-repository hit was a metadata-only author-inventory row, not a prior research deposit. No Arxiv DEP package or same-paper marker within 24 hours was found.

## Source Integrity and Cache

- Initial archive state: partial; the existing PDF was valid, but full-paper HTML was absent.
- Repair: the valid PDF was preserved. Official arXiv metadata, official full-paper HTML, and the TeX/source package were collected in one bounded repair pass. The local README, attribution record, machine-readable summary, preflight manifest, and verification report were refreshed.
- Final source state: complete and independently verified before synthesis.
- PDF validation: 3,294,807 bytes, `%PDF-` header present, trailing `%%EOF` present.
- Full-paper HTML validation: 497,212 bytes, 95,618 body characters after script/style removal, document marker present, 79 heading markers, and eight paper-structure terms detected.
- Source package: valid archive with 78 entries, including `main.tex`.
- Partial artifacts in the selected unit: none.
- Extractor preflight: `pypdf`, HTML, and source-package fallbacks available; `pdftotext` unavailable.
- Cache trajectory: miss -> backfilled -> cached.
- Extraction mode: `missing-only`; extraction completed from the verified local unit without network access.
- Extracted text: PDF 82,660 bytes, HTML 95,313 bytes, source package 209,706 bytes.
- Source policy: all PDF, HTML, metadata, TeX/source, extracted text, cache, integrity records, and inspection renders were withheld locally; no source files were uploaded.

## Evidence Reviewed

The review inspected the 28-page ICLR 2026 paper, full-paper HTML, TeX/source representation, theorem and proof, Algorithm 1, Tables 1-10, selected figures, appendices, the official arXiv record, the official ICLR 2026 poster record, and the official `questionstorer/sni` repository at its observed default-branch head. No training, inference, FEM generation, or metric recomputation was performed.

## Output Paths

- `.logs/20260723-Arxiv-Schwarz-Neural-Inference-LOG.md`
- `.logs/20260723-Arxiv-Schwarz-Neural-Inference-PHASE-LOG.md`
- `.reports/BL-Arxiv-Schwarz-Neural-Inference-20260723/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260723-Schwarz Neural Inference/README.md`
- `.lake-data/DEP-E/DEP-E-20260723-Schwarz Neural Inference/schwarz_neural_inference_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` - connects PDE structure, learned representations, compact parameterizations, and the need to test whether the chosen physical prior fits the data domain.
2. `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md` - provides a direct bridge to PDE assumption tracking, boundary geometry, theorem dependency, and the paper's out-of-scope Navier-Stokes direction.
3. `.lake-data/DEP-E/DEP-E-20260716-FGLE Midpoint Scheme/fgle_midpoint_scheme_manuscript.md` - supplies a numerical-analysis counterpart for separating convergence statements, nonlinear-solver behavior, independent reference error, runtime, and implementation evidence.

## Exactly Three Next-Review Questions

1. Does SNI retain its error advantage on a preregistered distribution of unseen geometries, mesh resolutions, PDE coefficients, and boundary-condition topologies rather than three hand-constructed domains?
2. Can the convergence theorem be repaired with assumptions that actually make the learned iteration contractive, and do those assumptions hold for the released GNOT and Geo-FNO implementations?
3. At what mesh scale, parallel configuration, and initialization quality does SNI become competitive with optimized FEM or classical domain-decomposition solvers at matched error?

## Exactly Three Challenges

1. The selected archive unit initially lacked full-paper HTML and had to pass a bounded repair-and-verification gate before any synthesis.
2. The theorem proof's final Cauchy step does not follow from the displayed fixed error bound, so convergence is preserved as an author claim with a reviewer-identified proof gap.
3. The official code is available but its observed default branch postdates the paper, has no tagged paper release in inspected evidence, and was not executed; paper-to-code reproducibility remains unverified.

## Submission Record

- Status: deposited on the default branch.
- Primary commit: [7b795c0](https://github.com/Delphoa/Black-Lake/commit/7b795c0ccb8278b800b74b423c000f414b5c4e9c).
- Slack notification: delivered to `#black-lake-artifacts`.
- Public-source policy: source files withheld locally; no source files uploaded.
