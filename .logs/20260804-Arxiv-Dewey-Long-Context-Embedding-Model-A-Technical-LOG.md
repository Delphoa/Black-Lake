# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260804-92EFB161`
- Deployment item ID: `BLAD-2200-20260804-92EFB161-P03`
- Public-safe date: 2026-08-04
- Paper: *Dewey Long Context Embedding Model: A Technical Report*
- Identifier: `arXiv:2503.20376`; DOI: `10.48550/arXiv.2503.20376`
- URL: https://arxiv.org/abs/2503.20376

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 38,583 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Dewey-Long-Context-Embedding-Model-A-Technical` slug; the 24-hour marker cutoff was 2026-08-03.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 229,650 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 5; sampled text inspection: true.
- Full-paper HTML: 157,646 bytes, 26,113 body characters, 16 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260804-Arxiv-Dewey-Long-Context-Embedding-Model-A-Technical-LOG.md`
- `.reports/BL-Arxiv-Dewey-Long-Context-Embedding-Model-A-Technical-20260804/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260804-Dewey Long Context/README.md`
- `.lake-data/DEP-E/DEP-E-20260804-Dewey Long Context/dewey_long_context_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md` - ConMax - DEP-E; overlap: embedding, long, context.
2. `.lake-data/DEP-E/DEP-E-20260721-AMAD Anomaly/amad_anomaly_manuscript.md` - AMAD Anomaly Detection - DEP-E; overlap: embedding, long, context.
3. `.lake-data/DEP-E/DEP-E-20260721-Feature Denoising/feature_denoising_manuscript.md` - Feature Denoising - DEP-E; overlap: embedding, long, context.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
