# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260813-F994AA5E`
- Deployment item ID: `BLAD-2200-20260813-F994AA5E-P05`
- Public-safe date: 2026-08-13
- Paper: *Contour Transformer Network for One-shot Segmentation of Anatomical Structures*
- Identifier: `arXiv:2012.01480`; DOI: `10.48550/arXiv.2012.01480`
- URL: https://arxiv.org/abs/2012.01480

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 20,929 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Contour-Transformer-Network-for-One-shot` slug; the 24-hour marker cutoff was 2026-08-12.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 14,464,320 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 286,053 bytes, 71,259 body characters, 75 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260813-Arxiv-Contour-Transformer-Network-for-One-shot-LOG.md`
- `.reports/BL-Arxiv-Contour-Transformer-Network-for-One-shot-20260813/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260813-Contour Transformer/README.md`
- `.lake-data/DEP-E/DEP-E-20260813-Contour Transformer/contour_transformer_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260803-One-shot neural band/one_shot_neural_band_manuscript.md` - One-shot neural band - DEP-E; overlap: one-shot.
2. `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md` - OE-BevSeg Perception - DEP-E; overlap: segmentation, one-shot, network.
3. `.lake-data/DEP-E/DEP-E-20260806-Inception Transformer/inception_transformer_manuscript.md` - Inception Transformer - DEP-E; overlap: transformer, segmentation, network.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
