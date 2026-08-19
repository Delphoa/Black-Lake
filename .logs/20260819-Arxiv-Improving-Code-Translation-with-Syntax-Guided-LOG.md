# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P63`
- Public-safe date: 2026-08-19
- Paper: *Improving Code Translation with Syntax-Guided and Semantic-aware Preference Optimization*
- Identifier: `arXiv:2605.13229`; DOI: `10.48550/arXiv.2605.13229`
- URL: https://arxiv.org/abs/2605.13229

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 4,385 on draw 32.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: optimization.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Improving-Code-Translation-with-Syntax-Guided` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 30; source-gate exclusions: 0; reselections: 31.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,317,799 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 223,513 bytes, 50,224 body characters, 70 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Improving-Code-Translation-with-Syntax-Guided-LOG.md`
- `.reports/BL-Arxiv-Improving-Code-Translation-with-Syntax-Guided-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Improving Code/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Improving Code/improving_code_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-CRPO Confidence-Reward/crpo_confidence_reward_manuscript.md` - CRPO Confidence-Reward - DEP-E; overlap: preference, optimization, translation.
2. `.lake-data/DEP-E/DEP-E-20260818-Debate Reflect and/debate_reflect_and_manuscript.md` - Debate Reflect and - DEP-E; overlap: preference, optimization, translation.
3. `.lake-data/DEP-E/DEP-E-20260819-A Survey of Direct/a_survey_of_direct_manuscript.md` - A Survey of Direct - DEP-E; overlap: preference, optimization, translation.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
