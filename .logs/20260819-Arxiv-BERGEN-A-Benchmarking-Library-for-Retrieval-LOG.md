# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P415`
- Public-safe date: 2026-08-19
- Paper: *BERGEN: A Benchmarking Library for Retrieval-Augmented Generation*
- Identifier: `arXiv:2407.01102`; DOI: `10.48550/arXiv.2407.01102`
- URL: https://arxiv.org/abs/2407.01102

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 56,872 on draw 47.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `BERGEN-A-Benchmarking-Library-for-Retrieval` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 8; focus exclusions: 38; source-gate exclusions: 0; reselections: 46.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 906,478 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 29; sampled text inspection: true.
- Full-paper HTML: 673,809 bytes, 111,070 body characters, 89 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-BERGEN-A-Benchmarking-Library-for-Retrieval-LOG.md`
- `.reports/BL-Arxiv-BERGEN-A-Benchmarking-Library-for-Retrieval-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-BERGEN A Benchmarking/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-BERGEN A Benchmarking/bergen_a_benchmarking_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-RAGPerf An End-to-End/ragperf_an_end_to_end_manuscript.md` - RAGPerf An End-to-End - DEP-E; overlap: benchmarking, retrieval-augmented, generation.
2. `.lake-data/DEP-E/DEP-E-20260819-How Much Reasoning Do/how_much_reasoning_do_manuscript.md` - How Much Reasoning Do - DEP-E; overlap: benchmarking, retrieval-augmented.
3. `.lake-data/DEP-E/DEP-E-20260819-SEAL-Tag Self-Tag/seal_tag_self_tag_manuscript.md` - SEAL-Tag Self-Tag - DEP-E; overlap: retrieval-augmented, generation, benchmarking.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
