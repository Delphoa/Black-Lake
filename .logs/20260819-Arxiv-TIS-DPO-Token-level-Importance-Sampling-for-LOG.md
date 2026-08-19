# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P123`
- Public-safe date: 2026-08-19
- Paper: *TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights*
- Identifier: `arXiv:2410.04350`; DOI: `10.48550/arXiv.2410.04350`
- URL: https://arxiv.org/abs/2410.04350

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 67,722 on draw 41.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: optimization.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `TIS-DPO-Token-level-Importance-Sampling-for` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 3; focus exclusions: 36; source-gate exclusions: 1; reselections: 40.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,010,274 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 30; sampled text inspection: true.
- Full-paper HTML: 629,123 bytes, 112,240 body characters, 126 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-TIS-DPO-Token-level-Importance-Sampling-for-LOG.md`
- `.reports/BL-Arxiv-TIS-DPO-Token-level-Importance-Sampling-for-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-TIS-DPO Token-level/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-TIS-DPO Token-level/tis_dpo_token_level_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-A Survey of Direct/a_survey_of_direct_manuscript.md` - A Survey of Direct - DEP-E; overlap: preference, direct, optimization, importance.
2. `.lake-data/DEP-E/DEP-E-20260819-Earlier Tokens Contribute/earlier_tokens_contribute_manuscript.md` - Earlier Tokens Contribute - DEP-E; overlap: preference, direct, optimization, importance.
3. `.lake-data/DEP-E/DEP-E-20260819-SDPO Segment-Level Direct/sdpo_segment_level_direct_manuscript.md` - SDPO Segment-Level Direct - DEP-E; overlap: preference, direct, optimization, importance.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
