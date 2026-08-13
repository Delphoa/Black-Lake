# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260805-6C10E207`
- Deployment item ID: `BLAD-2200-20260805-6C10E207-P05`
- Public-safe date: 2026-08-05
- Paper: *Back to the Future! Studying Data Cleanness in Defects4J and its Impact on Fault Localization*
- Identifier: `arXiv:2310.19139`; DOI: `10.48550/arXiv.2310.19139`
- URL: https://arxiv.org/abs/2310.19139

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 47,266 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Back-to-the-Future-Studying-Data-Cleanness` slug; the 24-hour marker cutoff was 2026-08-04.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 789,603 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 20; sampled text inspection: true.
- Full-paper HTML: 241,075 bytes, 83,611 body characters, 33 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260805-Arxiv-Back-to-the-Future-Studying-Data-Cleanness-LOG.md`
- `.reports/BL-Arxiv-Back-to-the-Future-Studying-Data-Cleanness-20260805/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260805-Back to the Future/README.md`
- `.lake-data/DEP-E/DEP-E-20260805-Back to the Future/back_to_the_future_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` - Document Fraud LLM - DEP-E; overlap: studying, impact, localization, future, its.
2. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - iKalibr Calibration - DEP-E; overlap: fault, back, impact, future, its.
3. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md` - Smart Coverage Goals - DEP-E; overlap: defects4j, fault, future, its.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
