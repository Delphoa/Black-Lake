# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260722-A5461BD0`
- Deployment item ID: `BLAD-2200-20260722-A5461BD0-P03`
- Public-safe date: 2026-07-22
- Paper: *Temporal Feature Matters: A Framework for Diffusion Model Quantization*
- Identifier: `arXiv:2407.19547`; DOI: `10.48550/arXiv.2407.19547`
- URL: https://arxiv.org/abs/2407.19547

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 31,486 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Temporal-Feature-Matters` slug; the 24-hour marker cutoff was 2026-07-21.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded archive repair.
- PDF: 19,612,244 bytes with a valid `%PDF-` header and trailing `%%EOF`.
- Full-paper HTML: 1,277,507 bytes, 137,068 body characters, 2 document markers, 77 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260722-Arxiv-Temporal-Feature-Matters-LOG.md`
- `.reports/BL-Arxiv-Temporal-Feature-Matters-20260722/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260722-Temporal Feature Matters/README.md`
- `.lake-data/DEP-E/DEP-E-20260722-Temporal Feature Matters/temporal_feature_matters_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260721-Hallo4 Portrait Motion/hallo4_portrait_motion_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260719-Coordinated CIL/coordinated_cil_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
