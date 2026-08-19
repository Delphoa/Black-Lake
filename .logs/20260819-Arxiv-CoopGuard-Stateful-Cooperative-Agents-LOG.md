# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P209`
- Public-safe date: 2026-08-19
- Paper: *CoopGuard: Stateful Cooperative Agents Safeguarding LLMs Against Evolving Multi-Round Attacks*
- Identifier: `arXiv:2604.04060`; DOI: `10.48550/arXiv.2604.04060`
- URL: https://arxiv.org/abs/2604.04060

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 55,239 on draw 8.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: stateful.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `CoopGuard-Stateful-Cooperative-Agents` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 6; source-gate exclusions: 0; reselections: 7.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 889,417 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 278,691 bytes, 53,381 body characters, 78 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-CoopGuard-Stateful-Cooperative-Agents-LOG.md`
- `.reports/BL-Arxiv-CoopGuard-Stateful-Cooperative-Agents-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-CoopGuard Stateful/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-CoopGuard Stateful/coopguard_stateful_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Cooperative Training of/cooperative_training_of_manuscript.md` - Cooperative Training of - DEP-E; overlap: cooperative, stateful.
2. `.lake-data/DEP-E/DEP-E-20260803-Empirical Study on/empirical_study_on_manuscript.md` - Empirical Study on - DEP-E; overlap: cooperative.
3. `.lake-data/DEP-E/DEP-E-20260805-UAV-Assisted Cooperative/uav_assisted_cooperative_manuscript.md` - UAV-Assisted Cooperative - DEP-E; overlap: cooperative.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
