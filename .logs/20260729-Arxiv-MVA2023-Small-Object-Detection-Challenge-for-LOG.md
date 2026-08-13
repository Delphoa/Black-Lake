# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260729-5EE3EF9C`
- Deployment item ID: `BLAD-2200-20260729-5EE3EF9C-P10`
- Public-safe date: 2026-07-29
- Paper: *MVA2023 Small Object Detection Challenge for Spotting Birds: Dataset, Methods, and Results*
- Identifier: `arXiv:2307.09143`; DOI: `10.23919/MVA57639.2023.10215935`
- URL: https://arxiv.org/abs/2307.09143

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 36,389 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `MVA2023-Small-Object-Detection-Challenge-for` slug; the 24-hour marker cutoff was 2026-07-28.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 9,122,431 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 143,866 bytes, 42,405 body characters, 68 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260729-Arxiv-MVA2023-Small-Object-Detection-Challenge-for-LOG.md`
- `.reports/BL-Arxiv-MVA2023-Small-Object-Detection-Challenge-for-20260729/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260729-MVA2023 Small Object/README.md`
- `.lake-data/DEP-E/DEP-E-20260729-MVA2023 Small Object/mva2023_small_object_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260728-HeightFormer Learning/heightformer_learning_manuscript.md` - HeightFormer Learning - DEP-E; overlap: object, vision, detection.
2. `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` - SSP Detection - DEP-E; overlap: object, detection.
3. `.lake-data/DEP-E/DEP-E-20260724-Visible-Thermal Tiny/visible_thermal_tiny_manuscript.md` - Visible-Thermal Tiny - DEP-E; overlap: object, detection.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
