# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P493`
- Public-safe date: 2026-08-19
- Paper: *QMamba: Post-Training Quantization for Vision State Space Models*
- Identifier: `arXiv:2501.13624`; DOI: `10.48550/arXiv.2501.13624`
- URL: https://arxiv.org/abs/2501.13624

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 59,959 on draw 19.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: state space model, state space models.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `QMamba-Post-Training-Quantization-for-Vision` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 5; focus exclusions: 13; source-gate exclusions: 0; reselections: 18.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,353,751 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 34,871 bytes, 6,715 body characters, 13 headings, and 5 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-QMamba-Post-Training-Quantization-for-Vision-LOG.md`
- `.reports/BL-Arxiv-QMamba-Post-Training-Quantization-for-Vision-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-QMamba Post-Training/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-QMamba Post-Training/qmamba_post_training_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - VideoWeave - DEP-E; overlap: post-training, space, state.
2. `.lake-data/DEP-E/DEP-E-20260818-S3MOT Monocular 3D Object/s3mot_monocular_3d_object_manuscript.md` - S3MOT Monocular 3D Object - DEP-E; overlap: space, state, vision.
3. `.lake-data/DEP-E/DEP-E-20260812-CMamba Learned Image/cmamba_learned_image_manuscript.md` - CMamba Learned Image - DEP-E; overlap: space, state.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
