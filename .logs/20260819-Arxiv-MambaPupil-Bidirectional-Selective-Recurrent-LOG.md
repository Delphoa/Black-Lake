# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P164`
- Public-safe date: 2026-08-19
- Paper: *MambaPupil: Bidirectional Selective Recurrent model for Event-based Eye tracking*
- Identifier: `arXiv:2404.12083`; DOI: `10.48550/arXiv.2404.12083`
- URL: https://arxiv.org/abs/2404.12083

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 35,733 on draw 44.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: model, recurrent.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `MambaPupil-Bidirectional-Selective-Recurrent` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 5; focus exclusions: 38; source-gate exclusions: 0; reselections: 43.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 10,709,929 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 154,599 bytes, 41,835 body characters, 41 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-MambaPupil-Bidirectional-Selective-Recurrent-LOG.md`
- `.reports/BL-Arxiv-MambaPupil-Bidirectional-Selective-Recurrent-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-MambaPupil Bidirectional/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-MambaPupil Bidirectional/mambapupil_bidirectional_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-S3MOT Monocular 3D Object/s3mot_monocular_3d_object_manuscript.md` - S3MOT Monocular 3D Object - DEP-E; overlap: selective, tracking.
2. `.lake-data/DEP-E/DEP-E-20260819-From Sim-to-Real Toward/from_sim_to_real_toward_manuscript.md` - From Sim-to-Real Toward - DEP-E; overlap: event-based.
3. `.lake-data/DEP-E/DEP-E-20260801-RawBMamba/rawbmamba_manuscript.md` - RawBMamba Review - DEP-E; overlap: bidirectional, selective.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
