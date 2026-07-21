# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260721-F7EDC854`
- Deployment item ID: `BLAD-2200-20260721-F7EDC854-P08`
- Public-safe date: 2026-07-21
- Paper: *Temporally Consistent Stereo Matching*
- Identifier: `arXiv:2407.11950`; DOI: `10.48550/arXiv.2407.11950`
- URL: https://arxiv.org/abs/2407.11950

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,779 PDFs and 75,776 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 58,472 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Temporally-Consistent` slug; the 24-hour marker cutoff was 2026-07-20.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded archive repair.
- PDF: 5,450,033 bytes with a valid `%PDF-` header and trailing `%%EOF`.
- Full-paper HTML: 231,705 bytes, 71,375 body characters, 2 document markers, 35 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260721-Arxiv-Temporally-Consistent-LOG.md`
- `.reports/BL-Arxiv-Temporally-Consistent-20260721/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260721-Temporally Consistent/README.md`
- `.lake-data/DEP-E/DEP-E-20260721-Temporally Consistent/temporally_consistent_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
