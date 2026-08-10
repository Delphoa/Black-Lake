# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260810-B3B6846E`
- Deployment item ID: `BLAD-2200-20260810-B3B6846E-P09`
- Public-safe date: 2026-08-10
- Paper: *Solver-Informed RL: Grounding Large Language Models for Authentic Optimization Modeling*
- Identifier: `arXiv:2505.11792`; DOI: `10.48550/arXiv.2505.11792`
- URL: https://arxiv.org/abs/2505.11792

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 25,702 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Solver-Informed-RL-Grounding-Large-Language` slug; the 24-hour marker cutoff was 2026-08-09.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,110,357 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 37; sampled text inspection: true.
- Full-paper HTML: 415,626 bytes, 94,654 body characters, 97 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260810-Arxiv-Solver-Informed-RL-Grounding-Large-Language-LOG.md`
- `.reports/BL-Arxiv-Solver-Informed-RL-Grounding-Large-Language-20260810/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260810-Solver-Informed RL/README.md`
- `.lake-data/DEP-E/DEP-E-20260810-Solver-Informed RL/solver_informed_rl_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260728-Multi-step Problem/multi_step_problem_manuscript.md` - Multi-step Problem - DEP-E; overlap: verifier feedback, process supervision, reasoning correctness.
2. `.lake-data/DEP-E/DEP-E-20260730-Epsilon Prox Affine/epsilon_prox_affine_manuscript.md` - Epsilon Prox Affine - DEP-E; overlap: optimization modeling, solver execution, disciplined programs.
3. `.lake-data/DEP-E/DEP-E-20260723-COEVO Co-Evolutionary Fra/coevo_co_evolutionary_fra_manuscript.md` - COEVO Co-Evolutionary Fra - DEP-E; overlap: LLM-generated formal artifacts, correctness feedback, optimization objectives.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
