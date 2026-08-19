# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P175`
- Public-safe date: 2026-08-19
- Paper: *DOGR: Leveraging Document-Oriented Contrastive Learning in Generative Retrieval*
- Identifier: `arXiv:2502.07219`; DOI: `10.48550/arXiv.2502.07219`
- URL: https://arxiv.org/abs/2502.07219

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 23,653 on draw 7.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: learning, retrieval.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `DOGR-Leveraging-Document-Oriented-Contrastive` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 4; source-gate exclusions: 0; reselections: 6.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 442,992 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 190,249 bytes, 51,247 body characters, 61 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-DOGR-Leveraging-Document-Oriented-Contrastive-LOG.md`
- `.reports/BL-Arxiv-DOGR-Leveraging-Document-Oriented-Contrastive-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-DOGR Leveraging/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-DOGR Leveraging/dogr_leveraging_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-BeatDance A Beat-Based/beatdance_a_beat_based_manuscript.md` - BeatDance A Beat-Based - DEP-E; overlap: contrastive, retrieval.
2. `.lake-data/DEP-E/DEP-E-20260819-X-CLIP End-to-End/x_clip_end_to_end_manuscript.md` - X-CLIP End-to-End - DEP-E; overlap: contrastive, retrieval.
3. `.lake-data/DEP-E/DEP-E-20260819-Enhancing Large Vision/enhancing_large_vision_manuscript.md` - Enhancing Large Vision - DEP-E; overlap: leveraging, contrastive.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
