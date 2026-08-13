# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260731-3D09E72F`
- Deployment item ID: `BLAD-2200-20260731-3D09E72F-P07`
- Public-safe date: 2026-07-31
- Paper: *SFOOD: A Multimodal Benchmark for Comprehensive Food Attribute Analysis Beyond RGB with Spectral Insights*
- Identifier: `arXiv:2507.04412`; DOI: `10.48550/arXiv.2507.04412`
- URL: https://arxiv.org/abs/2507.04412

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 71,179 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `SFOOD-A-Multimodal-Benchmark-for-Comprehensive` slug; the 24-hour marker cutoff was 2026-07-30.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 12,111,900 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 18; sampled text inspection: true.
- Full-paper HTML: 354,467 bytes, 68,054 body characters, 63 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260731-Arxiv-SFOOD-A-Multimodal-Benchmark-for-Comprehensive-LOG.md`
- `.reports/BL-Arxiv-SFOOD-A-Multimodal-Benchmark-for-Comprehensive-20260731/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260731-SFOOD A Multimodal/README.md`
- `.lake-data/DEP-E/DEP-E-20260731-SFOOD A Multimodal/sfood_a_multimodal_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-WKGM MRI Reconstruction/wkgm_mri_reconstruction_manuscript.md` - WKGM MRI Reconstruction - DEP-E; overlap: spectral, comprehensive, attribute, benchmark.
2. `.lake-data/DEP-E/DEP-E-20260718-Pixel Point Transfer/pixel_point_transfer_manuscript.md` - Pixel-Point Transfer - DEP-E; overlap: rgb, attribute, multimodal, benchmark.
3. `.lake-data/DEP-E/DEP-E-20260720-FEMOT Tracking/femot_tracking_manuscript.md` - FEMOT Tracking Review - DEP-E; overlap: rgb, attribute, multimodal, benchmark.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
