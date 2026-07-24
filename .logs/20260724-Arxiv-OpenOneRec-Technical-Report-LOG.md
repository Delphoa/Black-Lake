# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260724-CF53BCCB`
- Deployment item ID: `BLAD-2200-20260724-CF53BCCB-P01`
- Public-safe date: 2026-07-24
- Paper: *OpenOneRec Technical Report*
- Identifier: `arXiv:2512.24762`; DOI: `10.48550/arXiv.2512.24762`
- URL: https://arxiv.org/abs/2512.24762

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 62,762 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `OpenOneRec-Technical-Report` slug; the 24-hour marker cutoff was 2026-07-23.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,506,648 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 36; sampled text inspection: true.
- Full-paper HTML: 623,628 bytes, 104,641 body characters, 152 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260724-Arxiv-OpenOneRec-Technical-Report-LOG.md`
- `.reports/BL-Arxiv-OpenOneRec-Technical-Report-20260724/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260724-OpenOneRec Technical/README.md`
- `.lake-data/DEP-E/DEP-E-20260724-OpenOneRec Technical/openonerec_technical_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` - 2D-RC OTFS - DEP-E; overlap: abstract, arxiv, page, report, technical.
2. `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` - CAR Avatar - DEP-E; overlap: abstract, arxiv, page, report, technical.
3. `.lake-data/DEP-E/DEP-E-20260709-Mosaic Safety/mosaic_safety_manuscript.md` - Mosaic Safety - DEP-E; overlap: abstract, arxiv, page, report, technical.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
