# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P82`
- Public-safe date: 2026-08-19
- Paper: *SPikE-SSM: A Sparse, Precise, and Efficient Spiking State Space Model for Long Sequences Learning*
- Identifier: `arXiv:2410.17268`; DOI: `10.1109/TCDS.2026.3698720`
- URL: https://arxiv.org/abs/2410.17268

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 11,724 on draw 11.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: state space model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `SPikE-SSM-A-Sparse-Precise-and-Efficient` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 9; source-gate exclusions: 0; reselections: 10.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 953,870 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 23; sampled text inspection: true.
- Full-paper HTML: 457,916 bytes, 94,252 body characters, 80 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-SPikE-SSM-A-Sparse-Precise-and-Efficient-LOG.md`
- `.reports/BL-Arxiv-SPikE-SSM-A-Sparse-Precise-and-Efficient-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-SPikE-SSM A Sparse/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-SPikE-SSM A Sparse/spike_ssm_a_sparse_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` - Spiking Pose Tracking - DEP-E; overlap: spiking, sequences, long, sparse, state.
2. `.lake-data/DEP-E/DEP-E-20260713-Dynamical Dictionary/dynamical_dictionary_manuscript.md` - Dynamical Dictionary - DEP-E; overlap: spiking, precise, sparse, state.
3. `.lake-data/DEP-E/DEP-E-20260819-MoCom MAV Comms/mocom_mav_comms_manuscript.md` - MoCom MAV Comms - DEP-E; overlap: spiking, long, sparse, state.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
