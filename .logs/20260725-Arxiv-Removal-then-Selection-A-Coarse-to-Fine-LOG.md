# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260725-FF48EE13`
- Deployment item ID: `BLAD-2200-20260725-FF48EE13-P02`
- Public-safe date: 2026-07-25
- Paper: *Removal then Selection: A Coarse-to-Fine Fusion Perspective for RGB-Infrared Object Detection*
- Identifier: `arXiv:2401.10731`; DOI: `10.1109/TITS.2025.3638627`
- URL: https://arxiv.org/abs/2401.10731

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 4,759 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Removal-then-Selection-A-Coarse-to-Fine` slug; the 24-hour marker cutoff was 2026-07-24.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 11,111,328 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 589,298 bytes, 83,351 body characters, 66 headings, and 5 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260725-Arxiv-Removal-then-Selection-A-Coarse-to-Fine-LOG.md`
- `.reports/BL-Arxiv-Removal-then-Selection-A-Coarse-to-Fine-20260725/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260725-Removal then Selection A/README.md`
- `.lake-data/DEP-E/DEP-E-20260725-Removal then Selection A/removal_then_selection_a_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Beyond Feature Mapping/beyond_feature_mapping_manuscript.md` - Beyond Feature Mapping Review - DEP-E; overlap: integrating, superior, feature.
2. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md` - Smart Coverage Goals - DEP-E; overlap: redundant, selection.
3. `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` - CorrKD Missing Modal - DEP-E; overlap: modalities, multimodal.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
