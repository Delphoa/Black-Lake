# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260725-FF48EE13`
- Deployment item ID: `BLAD-2200-20260725-FF48EE13-P03`
- Public-safe date: 2026-07-25
- Paper: *CLCI-Net: Cross-Level fusion and Context Inference Networks for Lesion Segmentation of Chronic Stroke*
- Identifier: `arXiv:1907.07008`; DOI: `10.1007/978-3-030-32248-9_30`
- URL: https://arxiv.org/abs/1907.07008

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 29,720 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `CLCI-Net-Cross-Level-fusion-and-Context` slug; the 24-hour marker cutoff was 2026-07-24.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,492,402 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 57,009 bytes, 19,887 body characters, 33 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260725-Arxiv-CLCI-Net-Cross-Level-fusion-and-Context-LOG.md`
- `.reports/BL-Arxiv-CLCI-Net-Cross-Level-fusion-and-Context-20260725/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260725-CLCI-Net Cross-Level/README.md`
- `.lake-data/DEP-E/DEP-E-20260725-CLCI-Net Cross-Level/clci_net_cross_level_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-Habitat Synthetic Scenes/habitat_synthetic_scenes_manuscript.md` - Habitat Synthetic Scenes - DEP-E; overlap: navigation, scale, scene.
2. `.lake-data/DEP-E/DEP-E-20260724-A Large Scale Study of/a_large_scale_study_of_manuscript.md` - A Large Scale Study of - DEP-E; overlap: similarity, scale.
3. `.lake-data/DEP-E/DEP-E-20260723-Schwarz Neural Inference/schwarz_neural_inference_manuscript.md` - Schwarz Neural Inference - DEP-E; overlap: neural, inference.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
