# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-BBEE0F31`
- Deployment item ID: `BLAD-2200-20260818-BBEE0F31-P18`
- Public-safe date: 2026-08-18
- Paper: *S3MOT: Monocular 3D Object Tracking with Selective State Space Model*
- Identifier: `arXiv:2504.18068`; DOI: `10.48550/arXiv.2504.18068`
- URL: https://arxiv.org/abs/2504.18068

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 73,793 on draw 31.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: state space model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `S3MOT-Monocular-3D-Object-Tracking-with` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 30; source-gate exclusions: 0; reselections: 30.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 14,235,461 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 14; sampled text inspection: true.
- Full-paper HTML: 496,342 bytes, 90,923 body characters, 45 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-S3MOT-Monocular-3D-Object-Tracking-with-LOG.md`
- `.reports/BL-Arxiv-S3MOT-Monocular-3D-Object-Tracking-with-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-S3MOT Monocular 3D Object/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-S3MOT Monocular 3D Object/s3mot_monocular_3d_object_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md` - Stable Diffusion Depth - DEP-E; overlap: monocular, state.
2. `.lake-data/DEP-E/DEP-E-20260812-CMamba Learned Image/cmamba_learned_image_manuscript.md` - CMamba Learned Image - DEP-E; overlap: space, state.
3. `.lake-data/DEP-E/DEP-E-20260818-Swimba Switch Mamba Model/swimba_switch_mamba_model_manuscript.md` - Swimba Switch Mamba Model - DEP-E; overlap: space, state.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
