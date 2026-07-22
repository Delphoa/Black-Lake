# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260722-A5461BD0`
- Deployment item ID: `BLAD-2200-20260722-A5461BD0-P06`
- Public-safe date: 2026-07-22
- Paper: *Pixie: A System for Recommending 3+ Billion Items to 200+ Million Users in Real-Time*
- Identifier: `arXiv:1711.07601`; DOI: `10.48550/arXiv.1711.07601`
- URL: https://arxiv.org/abs/1711.07601

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 43,021 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Pixie-System-Recommending` slug; the 24-hour marker cutoff was 2026-07-21.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded archive repair.
- PDF: 694,703 bytes with a valid `%PDF-` header and trailing `%%EOF`.
- Full-paper HTML: 325,535 bytes, 61,053 body characters, 2 document markers, 34 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260722-Arxiv-Pixie-System-Recommending-LOG.md`
- `.reports/BL-Arxiv-Pixie-System-Recommending-20260722/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260722-Pixie System Recommending/README.md`
- `.lake-data/DEP-E/DEP-E-20260722-Pixie System Recommending/pixie_system_recommending_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260719-MIRA One Touch/mira_one_touch_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
