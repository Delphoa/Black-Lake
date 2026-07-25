# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260725-FF48EE13`
- Deployment item ID: `BLAD-2200-20260725-FF48EE13-P07`
- Public-safe date: 2026-07-25
- Paper: *Improved Counting and Localization from Density Maps for Object Detection in 2D and 3D Microscopy Imaging*
- Identifier: `arXiv:2203.15691`; DOI: `10.48550/arXiv.2203.15691`
- URL: https://arxiv.org/abs/2203.15691

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 66,655 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Improved-Counting-and-Localization-from-Density` slug; the 24-hour marker cutoff was 2026-07-24.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,456,964 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 298,763 bytes, 28,703 body characters, 31 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260725-Arxiv-Improved-Counting-and-Localization-from-Density-LOG.md`
- `.reports/BL-Arxiv-Improved-Counting-and-Localization-from-Density-20260725/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260725-Improved Counting and/README.md`
- `.lake-data/DEP-E/DEP-E-20260725-Improved Counting and/improved_counting_and_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` - SSP Detection - DEP-E; overlap: object, detection.
2. `.lake-data/DEP-E/DEP-E-20260724-Visible-Thermal Tiny/visible_thermal_tiny_manuscript.md` - Visible-Thermal Tiny - DEP-E; overlap: object, detection.
3. `.lake-data/DEP-E/DEP-E-20260725-Removal then Selection A/removal_then_selection_a_manuscript.md` - Removal then Selection A - DEP-E; overlap: object, detection.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
