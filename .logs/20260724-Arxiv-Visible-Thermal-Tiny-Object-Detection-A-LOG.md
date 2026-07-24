# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260724-CF53BCCB`
- Deployment item ID: `BLAD-2200-20260724-CF53BCCB-P07`
- Public-safe date: 2026-07-24
- Paper: *Visible-Thermal Tiny Object Detection: A Benchmark Dataset and Baselines*
- Identifier: `arXiv:2406.14482`; DOI: `10.48550/arXiv.2406.14482`
- URL: https://arxiv.org/abs/2406.14482

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 59,192 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Visible-Thermal-Tiny-Object-Detection-A` slug; the 24-hour marker cutoff was 2026-07-23.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 8,235,281 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 16; sampled text inspection: true.
- Full-paper HTML: 1,018,140 bytes, 101,643 body characters, 44 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260724-Arxiv-Visible-Thermal-Tiny-Object-Detection-A-LOG.md`
- `.reports/BL-Arxiv-Visible-Thermal-Tiny-Object-Detection-A-20260724/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260724-Visible-Thermal Tiny/README.md`
- `.lake-data/DEP-E/DEP-E-20260724-Visible-Thermal Tiny/visible_thermal_tiny_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-Rethinking Facial Express/rethinking_facial_express_manuscript.md` - Rethinking Facial Expression Rec - DEP-E; overlap: datasets, benchmark.
2. `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` - SSP Detection - DEP-E; overlap: object, detection.
3. `.lake-data/DEP-E/DEP-E-20260720-FEMOT Tracking/femot_tracking_manuscript.md` - FEMOT Tracking Review - DEP-E; overlap: tracking, benchmark.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
