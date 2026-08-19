# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P175`
- Public-safe date: 2026-08-19
- Paper: *State Space Model Meets Transformer: A New Paradigm for 3D Object Detection*
- Identifier: `arXiv:2503.14493`; DOI: `10.48550/arXiv.2503.14493`
- URL: https://arxiv.org/abs/2503.14493

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 46,829 on draw 12.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: state space model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `State-Space-Model-Meets-Transformer-A-New` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 10; source-gate exclusions: 0; reselections: 11.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 9,186,634 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 24; sampled text inspection: true.
- Full-paper HTML: 350,723 bytes, 89,148 body characters, 68 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-State-Space-Model-Meets-Transformer-A-New-LOG.md`
- `.reports/BL-Arxiv-State-Space-Model-Meets-Transformer-A-New-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-State Space Model Meets/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-State Space Model Meets/state_space_model_meets_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-S3MOT Monocular 3D Object/s3mot_monocular_3d_object_manuscript.md` - S3MOT Monocular 3D Object - DEP-E; overlap: space, object, state, detection.
2. `.lake-data/DEP-E/DEP-E-20260728-HeightFormer Learning/heightformer_learning_manuscript.md` - HeightFormer Learning - DEP-E; overlap: transformer, object, detection, space, state.
3. `.lake-data/DEP-E/DEP-E-20260726-MoE3D Mixture of Experts/moe3d_mixture_of_experts_manuscript.md` - MoE3D Mixture of Experts - DEP-E; overlap: meets, transformer, detection.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
