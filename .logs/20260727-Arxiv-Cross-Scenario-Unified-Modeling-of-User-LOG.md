# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260727-ADBD50D5`
- Deployment item ID: `BLAD-2200-20260727-ADBD50D5-P05`
- Public-safe date: 2026-07-27
- Paper: *Cross-Scenario Unified Modeling of User Interests at Billion Scale*
- Identifier: `arXiv:2510.14788`; DOI: `10.48550/arXiv.2510.14788`
- URL: https://arxiv.org/abs/2510.14788

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 66,290 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Cross-Scenario-Unified-Modeling-of-User` slug; the 24-hour marker cutoff was 2026-07-26.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 27,024,111 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 21; sampled text inspection: true.
- Full-paper HTML: 278,361 bytes, 75,280 body characters, 126 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260727-Arxiv-Cross-Scenario-Unified-Modeling-of-User-LOG.md`
- `.reports/BL-Arxiv-Cross-Scenario-Unified-Modeling-of-User-20260727/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260727-Cross-Scenario Unified/README.md`
- `.lake-data/DEP-E/DEP-E-20260727-Cross-Scenario Unified/cross_scenario_unified_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260722-Pixie System Recommending/pixie_system_recommending_manuscript.md` - Pixie System Recommending Review - DEP-E; overlap: billion, users.
2. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - OViP Preference - DEP-E; overlap: preference, online.
3. `.lake-data/DEP-E/DEP-E-20260724-A Large Scale Study of/a_large_scale_study_of_manuscript.md` - A Large Scale Study of - DEP-E; overlap: techniques, scale.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
