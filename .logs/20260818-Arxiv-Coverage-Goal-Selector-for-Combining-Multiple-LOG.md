# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-BBEE0F31`
- Deployment item ID: `BLAD-2200-20260818-BBEE0F31-P25`
- Public-safe date: 2026-08-18
- Paper: *Coverage Goal Selector for Combining Multiple Criteria in Search-Based Unit Test Generation*
- Identifier: `arXiv:2309.07518`; DOI: `10.48550/arXiv.2309.07518`
- URL: https://arxiv.org/abs/2309.07518

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 22,916 on draw 3.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: search.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Coverage-Goal-Selector-for-Combining-Multiple` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 2; source-gate exclusions: 0; reselections: 2.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 4,477,540 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 28; sampled text inspection: true.
- Full-paper HTML: 946,621 bytes, 134,540 body characters, 63 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Coverage-Goal-Selector-for-Combining-Multiple-LOG.md`
- `.reports/BL-Arxiv-Coverage-Goal-Selector-for-Combining-Multiple-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Coverage Goal Selector/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Coverage Goal Selector/coverage_goal_selector_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md` - Smart Coverage Goals - DEP-E; overlap: search-based, generation, coverage, selector, combining.
2. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` - HERMES World Model - DEP-E; overlap: generation, goal, multiple, unit, coverage.
3. `.lake-data/DEP-E/DEP-E-20260719-DiscourseFlip RAG Risk/discourseflip_rag_risk_manuscript.md` - DiscourseFlip Risk Review; overlap: generation, goal, multiple, unit, coverage.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
