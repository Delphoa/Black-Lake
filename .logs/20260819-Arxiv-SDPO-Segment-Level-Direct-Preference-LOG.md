# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P251`
- Public-safe date: 2026-08-19
- Paper: *SDPO: Segment-Level Direct Preference Optimization for Social Agents*
- Identifier: `arXiv:2501.01821`; DOI: `10.48550/arXiv.2501.01821`
- URL: https://arxiv.org/abs/2501.01821

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 61,772 on draw 17.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: optimization.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `SDPO-Segment-Level-Direct-Preference` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 15; source-gate exclusions: 0; reselections: 16.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 793,197 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 15; sampled text inspection: true.
- Full-paper HTML: 212,495 bytes, 54,224 body characters, 79 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-SDPO-Segment-Level-Direct-Preference-LOG.md`
- `.reports/BL-Arxiv-SDPO-Segment-Level-Direct-Preference-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-SDPO Segment-Level Direct/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-SDPO Segment-Level Direct/sdpo_segment_level_direct_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-A Survey of Direct/a_survey_of_direct_manuscript.md` - A Survey of Direct - DEP-E; overlap: preference, direct, optimization.
2. `.lake-data/DEP-E/DEP-E-20260819-CRPO Confidence-Reward/crpo_confidence_reward_manuscript.md` - CRPO Confidence-Reward - DEP-E; overlap: preference, optimization, direct.
3. `.lake-data/DEP-E/DEP-E-20260819-Reverse Preference/reverse_preference_manuscript.md` - Reverse Preference - DEP-E; overlap: preference, optimization, direct.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
