# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260730-2FDDC232`
- Deployment item ID: `BLAD-2200-20260730-2FDDC232-P08`
- Public-safe date: 2026-07-30
- Paper: *Sat3R: Satellite DSM Reconstruction via RPC-Aware Depth Fine-tuning*
- Identifier: `arXiv:2605.07264`; DOI: `10.48550/arXiv.2605.07264`
- URL: https://arxiv.org/abs/2605.07264

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 43,780 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Sat3R-Satellite-DSM-Reconstruction-via-RPC-Aware` slug; the 24-hour marker cutoff was 2026-07-29.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 10,953,178 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 7; sampled text inspection: true.
- Full-paper HTML: 125,589 bytes, 26,059 body characters, 47 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260730-Arxiv-Sat3R-Satellite-DSM-Reconstruction-via-RPC-Aware-LOG.md`
- `.reports/BL-Arxiv-Sat3R-Satellite-DSM-Reconstruction-via-RPC-Aware-20260730/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260730-Sat3R Satellite DSM/README.md`
- `.lake-data/DEP-E/DEP-E-20260730-Sat3R Satellite DSM/sat3r_satellite_dsm_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Urban Visual Intelligence/urban_visual_intelligence_manuscript.md` - Urban Visual Intelligence Review - DEP-E; overlap: imagery, urban, visual.
2. `.lake-data/DEP-E/DEP-E-20260721-Beyond Feature Mapping/beyond_feature_mapping_manuscript.md` - Beyond Feature Mapping Review - DEP-E; overlap: gap, mapping.
3. `.lake-data/DEP-E/DEP-E-20260723-Schwarz Neural Inference/schwarz_neural_inference_manuscript.md` - Schwarz Neural Inference - DEP-E; overlap: domain, inference.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
