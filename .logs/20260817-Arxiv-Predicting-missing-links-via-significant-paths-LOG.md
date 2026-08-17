# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260817-2C1A830E`
- Deployment item ID: `BLAD-2200-20260817-2C1A830E-P09`
- Public-safe date: 2026-08-17
- Paper: *Predicting missing links via significant paths*
- Identifier: `arXiv:1402.6225`; DOI: `10.1209/0295-5075/106/18008`
- URL: https://arxiv.org/abs/1402.6225

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 6,846 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Predicting-missing-links-via-significant-paths` slug; the 24-hour marker cutoff was 2026-08-16.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 483,597 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 6; sampled text inspection: true.
- Full-paper HTML: 145,286 bytes, 32,796 body characters, 30 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260817-Arxiv-Predicting-missing-links-via-significant-paths-LOG.md`
- `.reports/BL-Arxiv-Predicting-missing-links-via-significant-paths-20260817/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260817-Predicting missing links/README.md`
- `.lake-data/DEP-E/DEP-E-20260817-Predicting missing links/predicting_missing_links_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Dataset Baselines/dataset_baselines_manuscript.md` - Dataset Baselines Review - DEP-E; overlap: predicting, missing.
2. `.lake-data/DEP-E/DEP-E-20260731-OS Minimum Paths/os_minimum_paths_manuscript.md` - OS Minimum Paths - DEP-E; overlap: paths, links.
3. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - DMNN Conditional Paths - DEP-E; overlap: paths, missing.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
