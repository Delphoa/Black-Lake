# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P02`
- Public-safe date: 2026-08-18
- Paper: *MASt3R-Fusion: Integrating Feed-Forward Visual Model with IMU, GNSS for High-Functionality SLAM*
- Identifier: `arXiv:2509.20757`; DOI: `10.48550/arXiv.2509.20757`
- URL: https://arxiv.org/abs/2509.20757

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 32,095 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `MASt3R-Fusion-Integrating-Feed-Forward-Visual` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 35,218,530 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 15; sampled text inspection: true.
- Full-paper HTML: 455,256 bytes, 85,680 body characters, 57 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-MASt3R-Fusion-Integrating-Feed-Forward-Visual-LOG.md`
- `.reports/BL-Arxiv-MASt3R-Fusion-Integrating-Feed-Forward-Visual-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-MASt3R-Fusion Integrating/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-MASt3R-Fusion Integrating/mast3r_fusion_integrating_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260804-A GNSS Aided Initial/a_gnss_aided_initial_manuscript.md` - A GNSS Aided Initial - DEP-E; overlap: gnss, visual.
2. `.lake-data/DEP-E/DEP-E-20260721-Beyond Feature Mapping/beyond_feature_mapping_manuscript.md` - Beyond Feature Mapping Review - DEP-E; overlap: integrating.
3. `.lake-data/DEP-E/DEP-E-20260731-Deep Learning for/deep_learning_for_manuscript.md` - Deep Learning for - DEP-E; overlap: integrating.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
