# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P374`
- Public-safe date: 2026-08-19
- Paper: *An efficient multi-core implementation of a novel HSS-structured multifrontal solver using randomized sampling*
- Identifier: `arXiv:1502.07405`; DOI: `10.48550/arXiv.1502.07405`
- URL: https://arxiv.org/abs/1502.07405

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 10,076 on draw 12.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: solver.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `An-efficient-multi-core-implementation-of-a` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 4; focus exclusions: 7; source-gate exclusions: 0; reselections: 11.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 602,141 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 26; sampled text inspection: true.
- Full-paper HTML: 553,354 bytes, 100,016 body characters, 75 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-An-efficient-multi-core-implementation-of-a-LOG.md`
- `.reports/BL-Arxiv-An-efficient-multi-core-implementation-of-a-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-An efficient multi-core/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-An efficient multi-core/an_efficient_multi_core_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-DPM-Solver A Fast ODE/dpm_solver_a_fast_ode_manuscript.md` - DPM-Solver A Fast ODE - DEP-E; overlap: solver, sampling.
2. `.lake-data/DEP-E/DEP-E-20260819-Differentiable Solver/differentiable_solver_manuscript.md` - Differentiable Solver - DEP-E; overlap: solver, sampling.
3. `.lake-data/DEP-E/DEP-E-20260804-RPDG Incremental Grad/rpdg_incremental_gradient_manuscript.md` - RPDG Incremental Gradient - DEP-E; overlap: randomized, solver, sampling.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
