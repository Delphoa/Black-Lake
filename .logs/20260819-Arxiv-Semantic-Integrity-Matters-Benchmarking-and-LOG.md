# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P453`
- Public-safe date: 2026-08-19
- Paper: *Semantic Integrity Matters: Benchmarking and Preserving High-Density Reasoning in KV Cache Compression*
- Identifier: `arXiv:2502.01941`; DOI: `10.48550/arXiv.2502.01941`
- URL: https://arxiv.org/abs/2502.01941

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 16,605 on draw 3.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: kv cache.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Semantic-Integrity-Matters-Benchmarking-and` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 1; source-gate exclusions: 0; reselections: 2.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,878,826 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 29; sampled text inspection: true.
- Full-paper HTML: 898,009 bytes, 141,630 body characters, 156 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Semantic-Integrity-Matters-Benchmarking-and-LOG.md`
- `.reports/BL-Arxiv-Semantic-Integrity-Matters-Benchmarking-and-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Semantic Integrity/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Semantic Integrity/semantic_integrity_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260708-ConMax Reasoning/conmax_reasoning_manuscript.md` - ConMax - DEP-E; overlap: compression, reasoning, matters, benchmarking, preserving.
2. `.lake-data/DEP-E/DEP-E-20260716-FGBench Chemistry/fgbench_chemistry_manuscript.md` - FGBench Chemistry - DEP-E; overlap: benchmarking, reasoning, preserving, cache, integrity.
3. `.lake-data/DEP-E/DEP-E-20260726-ManipulationNet An/manipulationnet_an_manuscript.md` - ManipulationNet An - DEP-E; overlap: benchmarking, reasoning, semantic, cache, integrity.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
