# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260804-92EFB161`
- Deployment item ID: `BLAD-2200-20260804-92EFB161-P10`
- Public-safe date: 2026-08-04
- Paper: *A GNSS Aided Initial Alignment Method for MEMS-IMU Based on Backtracking Algorithm and Backward Filtering*
- Identifier: `arXiv:2202.13700`; DOI: `10.48550/arXiv.2202.13700`
- URL: https://arxiv.org/abs/2202.13700

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 33,327 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `A-GNSS-Aided-Initial-Alignment-Method-for` slug; the 24-hour marker cutoff was 2026-08-03.
- Duplicate exclusions: 0; source-gate exclusions: 2; reselections: 2.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 15,533,740 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 741,785 bytes, 57,208 body characters, 27 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260804-Arxiv-A-GNSS-Aided-Initial-Alignment-Method-for-LOG.md`
- `.reports/BL-Arxiv-A-GNSS-Aided-Initial-Alignment-Method-for-20260804/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260804-A GNSS Aided Initial/README.md`
- `.lake-data/DEP-E/DEP-E-20260804-A GNSS Aided Initial/a_gnss_aided_initial_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md` - OE-BevSeg Perception - DEP-E; overlap: backward, filtering, alignment, algorithm, initial.
2. `.lake-data/DEP-E/DEP-E-20260716-UAV Visual Localization/uav_visual_localization_manuscript.md` - UAV Visual Localization - DEP-E; overlap: gnss, alignment, initial.
3. `.lake-data/DEP-E/DEP-E-20260804-RPDG Incremental Grad/rpdg_incremental_gradient_manuscript.md` - RPDG Incremental Gradient - DEP-E; overlap: backtracking, algorithm, initial.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
