# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260809-2E4CB30E`
- Deployment item ID: `BLAD-2200-20260809-2E4CB30E-P06`
- Public-safe date: 2026-08-09
- Paper: *Discriminative and Semantic Feature Selection for Place Recognition towards Dynamic Environments*
- Identifier: `arXiv:2103.10023`; DOI: `10.48550/arXiv.2103.10023`
- URL: https://arxiv.org/abs/2103.10023

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 63,827 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Discriminative-and-Semantic-Feature-Selection` slug; the 24-hour marker cutoff was 2026-08-08.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,686,875 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 6; sampled text inspection: true.
- Full-paper HTML: 181,179 bytes, 36,142 body characters, 42 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260809-Arxiv-Discriminative-and-Semantic-Feature-Selection-LOG.md`
- `.reports/BL-Arxiv-Discriminative-and-Semantic-Feature-Selection-20260809/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260809-Discriminative and/README.md`
- `.lake-data/DEP-E/DEP-E-20260809-Discriminative and/discriminative_and_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-UAV Visual Localization/uav_visual_localization_manuscript.md` - UAV Visual Localization - DEP-E; overlap: place, recognition, environments, feature, semantic.
2. `.lake-data/DEP-E/DEP-E-20260721-Feature Denoising/feature_denoising_manuscript.md` - Feature Denoising - DEP-E; overlap: place, recognition, environments, feature, semantic.
3. `.lake-data/DEP-E/DEP-E-20260719-CLOVER Test Benchmark/clover_test_benchmark_manuscript.md` - CLOVER Test Benchmark - DEP-E; overlap: discriminative, environments, dynamic, semantic, selection.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
