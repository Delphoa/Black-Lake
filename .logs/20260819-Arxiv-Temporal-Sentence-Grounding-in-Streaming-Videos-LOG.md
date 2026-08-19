# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P94`
- Public-safe date: 2026-08-19
- Paper: *Temporal Sentence Grounding in Streaming Videos*
- Identifier: `arXiv:2308.07102`; DOI: `10.1145/3581783.3612120`
- URL: https://arxiv.org/abs/2308.07102

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 23,148 on draw 6.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: streaming, temporal.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Temporal-Sentence-Grounding-in-Streaming-Videos` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 5; source-gate exclusions: 0; reselections: 5.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 5,858,433 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 259,963 bytes, 67,271 body characters, 80 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Temporal-Sentence-Grounding-in-Streaming-Videos-LOG.md`
- `.reports/BL-Arxiv-Temporal-Sentence-Grounding-in-Streaming-Videos-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Temporal Sentence/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Temporal Sentence/temporal_sentence_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260809-Streaming/streaming_manuscript.md` - Streaming - DEP-E; overlap: streaming, temporal.
2. `.lake-data/DEP-E/DEP-E-20260818-A Better and Faster/a_better_and_faster_manuscript.md` - A Better and Faster - DEP-E; overlap: streaming, temporal.
3. `.lake-data/DEP-E/DEP-E-20260818-Learning-Augmented/learning_augmented_manuscript.md` - Learning-Augmented - DEP-E; overlap: streaming, temporal.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
