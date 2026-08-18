# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-BBEE0F31`
- Deployment item ID: `BLAD-2200-20260818-BBEE0F31-P32`
- Public-safe date: 2026-08-18
- Paper: *A Better and Faster End-to-End Model for Streaming ASR*
- Identifier: `arXiv:2011.10798`; DOI: `10.48550/arXiv.2011.10798`
- URL: https://arxiv.org/abs/2011.10798

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 12,200 on draw 9.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: model, streaming.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `A-Better-and-Faster-End-to-End` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 8; source-gate exclusions: 0; reselections: 8.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 287,270 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 5; sampled text inspection: true.
- Full-paper HTML: 107,027 bytes, 32,357 body characters, 55 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-A-Better-and-Faster-End-to-End-LOG.md`
- `.reports/BL-Arxiv-A-Better-and-Faster-End-to-End-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-A Better and Faster/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-A Better and Faster/a_better_and_faster_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260809-Streaming/streaming_manuscript.md` - Streaming - DEP-E; overlap: streaming, better.
2. `.lake-data/DEP-E/DEP-E-20260818-Learning-Augmented/learning_augmented_manuscript.md` - Learning-Augmented - DEP-E; overlap: streaming, better.
3. `.lake-data/DEP-E/DEP-E-20260818-Streaming Autoregressive/streaming_autoregressive_manuscript.md` - Streaming Autoregressive - DEP-E; overlap: streaming, better.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
