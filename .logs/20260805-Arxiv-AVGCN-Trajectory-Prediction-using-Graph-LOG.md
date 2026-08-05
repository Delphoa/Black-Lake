# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260805-6C10E207`
- Deployment item ID: `BLAD-2200-20260805-6C10E207-P06`
- Public-safe date: 2026-08-05
- Paper: *AVGCN: Trajectory Prediction using Graph Convolutional Networks Guided by Human Attention*
- Identifier: `arXiv:2101.05682`; DOI: `10.48550/arXiv.2101.05682`
- URL: https://arxiv.org/abs/2101.05682

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 33,223 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `AVGCN-Trajectory-Prediction-using-Graph` slug; the 24-hour marker cutoff was 2026-08-04.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 749,150 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 7; sampled text inspection: true.
- Full-paper HTML: 398,828 bytes, 45,128 body characters, 42 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260805-Arxiv-AVGCN-Trajectory-Prediction-using-Graph-LOG.md`
- `.reports/BL-Arxiv-AVGCN-Trajectory-Prediction-using-Graph-20260805/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260805-AVGCN Trajectory/README.md`
- `.lake-data/DEP-E/DEP-E-20260805-AVGCN Trajectory/avgcn_trajectory_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260803-Vid2Curve Reconstruction/vid2curve_reconstruction_manuscript.md` - Vid2Curve Reconstruction - DEP-E; overlap: topological, geometric, topology, pose, trajectory.
2. `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` - SSP Detection - DEP-E; overlap: guided, avatar, geometric, topology, motion.
3. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: persistence, convolutional, networks, attention, prediction.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
