# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260803-11C1283E`
- Deployment item ID: `BLAD-2200-20260803-11C1283E-P07`
- Public-safe date: 2026-08-03
- Paper: *Texturing and Deforming Meshes with Casual Images*
- Identifier: `arXiv:1809.03144`; DOI: `10.48550/arXiv.1809.03144`
- URL: https://arxiv.org/abs/1809.03144

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 11,679 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Texturing-and-Deforming-Meshes-with-Casual` slug; the 24-hour marker cutoff was 2026-08-02.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,047,355 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 6; sampled text inspection: true.
- Full-paper HTML: 140,527 bytes, 24,122 body characters, 39 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260803-Arxiv-Texturing-and-Deforming-Meshes-with-Casual-LOG.md`
- `.reports/BL-Arxiv-Texturing-and-Deforming-Meshes-with-Casual-20260803/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260803-Texturing and Deforming/README.md`
- `.lake-data/DEP-E/DEP-E-20260803-Texturing and Deforming/texturing_and_deforming_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` - CAR Avatar - DEP-E; overlap: meshes, images.
2. `.lake-data/DEP-E/DEP-E-20260803-Vid2Curve Reconstruction/vid2curve_reconstruction_manuscript.md` - Vid2Curve Reconstruction - DEP-E; overlap: meshes, images.
3. `.lake-data/DEP-E/DEP-E-20260716-Hyperbolic Catenaries/hyperbolic_catenaries_manuscript.md` - Hyperbolic Catenaries - DEP-E; overlap: meshes.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
