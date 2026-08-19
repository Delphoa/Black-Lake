# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P89`
- Public-safe date: 2026-08-19
- Paper: *PiP: Planning-informed Trajectory Prediction for Autonomous Driving*
- Identifier: `arXiv:2003.11476`; DOI: `10.1007/978-3-030-58589-1_36`
- URL: https://arxiv.org/abs/2003.11476

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 44,128 on draw 28.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: planning.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `PiP-Planning-informed-Trajectory-Prediction-for` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 3; focus exclusions: 24; source-gate exclusions: 0; reselections: 27.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 4,095,442 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 16; sampled text inspection: true.
- Full-paper HTML: 158,744 bytes, 48,870 body characters, 42 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-PiP-Planning-informed-Trajectory-Prediction-for-LOG.md`
- `.reports/BL-Arxiv-PiP-Planning-informed-Trajectory-Prediction-for-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-PiP Planning-informed/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-PiP Planning-informed/pip_planning_informed_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-Occ3D A Large-Scale 3D/occ3d_a_large_scale_3d_manuscript.md` - Occ3D A Large-Scale 3D - DEP-E; overlap: driving, prediction, autonomous.
2. `.lake-data/DEP-E/DEP-E-20260730-TopoDiffuser A/topodiffuser_a_manuscript.md` - TopoDiffuser A - DEP-E; overlap: trajectory, prediction, driving, autonomous.
3. `.lake-data/DEP-E/DEP-E-20260805-AVGCN Trajectory/avgcn_trajectory_manuscript.md` - AVGCN Trajectory - DEP-E; overlap: trajectory, prediction, autonomous.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
