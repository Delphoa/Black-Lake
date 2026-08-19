# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P120`
- Public-safe date: 2026-08-19
- Paper: *Out of Sight but Not Out of Mind: Hybrid Memory for Dynamic Video World Models*
- Identifier: `arXiv:2603.25716`; DOI: `10.48550/arXiv.2603.25716`
- URL: https://arxiv.org/abs/2603.25716

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 53,131 on draw 6.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: world model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Out-of-Sight-but-Not-Out-of` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 3; focus exclusions: 2; source-gate exclusions: 0; reselections: 5.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 35,259,039 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 22; sampled text inspection: true.
- Full-paper HTML: 213,780 bytes, 54,775 body characters, 58 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Out-of-Sight-but-Not-Out-of-LOG.md`
- `.reports/BL-Arxiv-Out-of-Sight-but-Not-Out-of-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Out of Sight but Not Out/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Out of Sight but Not Out/out_of_sight_but_not_out_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-Cosh-DiT Co-Speech/cosh_dit_co_speech_manuscript.md` - Cosh-DiT Co-Speech - DEP-E; overlap: hybrid, video, memory, but.
2. `.lake-data/DEP-E/DEP-E-20260819-Martian World Model/martian_world_model_manuscript.md` - Martian World Model - DEP-E; overlap: video, world, dynamic, memory, but.
3. `.lake-data/DEP-E/DEP-E-20260819-MoVerse Real-Time Video/moverse_real_time_video_manuscript.md` - MoVerse Real-Time Video - DEP-E; overlap: video, world, memory, but.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
