# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P322`
- Public-safe date: 2026-08-19
- Paper: *RAGPerf: An End-to-End Benchmarking Framework for Retrieval-Augmented Generation Systems*
- Identifier: `arXiv:2603.10765`; DOI: `10.48550/arXiv.2603.10765`
- URL: https://arxiv.org/abs/2603.10765

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 60,828 on draw 6.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `RAGPerf-An-End-to-End-Benchmarking-Framework` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 5; source-gate exclusions: 0; reselections: 5.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,314,216 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 15; sampled text inspection: true.
- Full-paper HTML: 371,545 bytes, 98,439 body characters, 75 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-RAGPerf-An-End-to-End-Benchmarking-Framework-LOG.md`
- `.reports/BL-Arxiv-RAGPerf-An-End-to-End-Benchmarking-Framework-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-RAGPerf An End-to-End/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-RAGPerf An End-to-End/ragperf_an_end_to_end_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-How Much Reasoning Do/how_much_reasoning_do_manuscript.md` - How Much Reasoning Do - DEP-E; overlap: benchmarking, retrieval-augmented, systems.
2. `.lake-data/DEP-E/DEP-E-20260819-SEAL-Tag Self-Tag/seal_tag_self_tag_manuscript.md` - SEAL-Tag Self-Tag - DEP-E; overlap: retrieval-augmented, generation, benchmarking, systems.
3. `.lake-data/DEP-E/DEP-E-20260719-DiscourseFlip RAG Risk/discourseflip_rag_risk_manuscript.md` - DiscourseFlip Risk Review; overlap: retrieval-augmented, generation, systems.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
