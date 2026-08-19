# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P142`
- Public-safe date: 2026-08-19
- Paper: *Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models*
- Identifier: `arXiv:2508.11953`; DOI: `10.48550/arXiv.2508.11953`
- URL: https://arxiv.org/abs/2508.11953

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 65,327 on draw 4.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: optimization.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Data-Mixing-Optimization-for-Supervised-Fine` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 3; source-gate exclusions: 0; reselections: 3.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,120,544 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 19; sampled text inspection: true.
- Full-paper HTML: 429,729 bytes, 83,106 body characters, 112 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Data-Mixing-Optimization-for-Supervised-Fine-LOG.md`
- `.reports/BL-Arxiv-Data-Mixing-Optimization-for-Supervised-Fine-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Data Mixing Optimization/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Data Mixing Optimization/data_mixing_optimization_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-DRIFT Decoupled Rollouts/drift_decoupled_rollouts_manuscript.md` - DRIFT Decoupled Rollouts - DEP-E; overlap: fine-tuning, optimization, language.
2. `.lake-data/DEP-E/DEP-E-20260819-Towards Fast LLM/towards_fast_llm_manuscript.md` - Towards Fast LLM - DEP-E; overlap: fine-tuning, optimization, language.
3. `.lake-data/DEP-E/DEP-E-20260819-FlowPRO Reward-Free/flowpro_reward_free_manuscript.md` - FlowPRO Reward-Free - DEP-E; overlap: fine-tuning, optimization.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
