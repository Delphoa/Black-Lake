# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260816-7EAAB41B`
- Deployment item ID: `BLAD-2200-20260816-7EAAB41B-P02`
- Public-safe date: 2026-08-16
- Paper: *Learning Nonparametric Human Mesh Reconstruction from a Single Image without Ground Truth Meshes*
- Identifier: `arXiv:2003.00052`; DOI: `10.48550/arXiv.2003.00052`
- URL: https://arxiv.org/abs/2003.00052

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 48,002 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Learning-Nonparametric-Human-Mesh-Reconstruction` slug; the 24-hour marker cutoff was 2026-08-15.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 7,677,963 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 255,707 bytes, 49,854 body characters, 51 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260816-Arxiv-Learning-Nonparametric-Human-Mesh-Reconstruction-LOG.md`
- `.reports/BL-Arxiv-Learning-Nonparametric-Human-Mesh-Reconstruction-20260816/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260816-Learning Nonparametric/README.md`
- `.lake-data/DEP-E/DEP-E-20260816-Learning Nonparametric/learning_nonparametric_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260803-Texturing and Deforming/texturing_and_deforming_manuscript.md` - Texturing and Deforming - DEP-E; overlap: meshes, reconstruction, human.
2. `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` - CAR Avatar - DEP-E; overlap: reconstruction, meshes, mesh, ground, truth.
3. `.lake-data/DEP-E/DEP-E-20260803-Vid2Curve Reconstruction/vid2curve_reconstruction_manuscript.md` - Vid2Curve Reconstruction - DEP-E; overlap: reconstruction, meshes, mesh, ground, truth.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
