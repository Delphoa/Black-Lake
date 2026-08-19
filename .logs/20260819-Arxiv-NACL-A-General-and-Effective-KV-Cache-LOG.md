# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P287`
- Public-safe date: 2026-08-19
- Paper: *NACL: A General and Effective KV Cache Eviction Framework for LLMs at Inference Time*
- Identifier: `arXiv:2408.03675`; DOI: `10.48550/arXiv.2408.03675`
- URL: https://arxiv.org/abs/2408.03675

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 71,109 on draw 7.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: cache eviction, kv cache.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `NACL-A-General-and-Effective-KV-Cache` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 6; source-gate exclusions: 0; reselections: 6.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 948,756 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 14; sampled text inspection: true.
- Full-paper HTML: 262,166 bytes, 61,073 body characters, 110 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-NACL-A-General-and-Effective-KV-Cache-LOG.md`
- `.reports/BL-Arxiv-NACL-A-General-and-Effective-KV-Cache-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-NACL A General and/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-NACL A General and/nacl_a_general_and_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Sparse-dLLM Accelerating/sparse_dllm_accelerating_manuscript.md` - Sparse-dLLM Accelerating - DEP-E; overlap: eviction, llms, cache, time.
2. `.lake-data/DEP-E/DEP-E-20260819-How Much Reasoning Do/how_much_reasoning_do_manuscript.md` - How Much Reasoning Do - DEP-E; overlap: llms, inference, cache, time.
3. `.lake-data/DEP-E/DEP-E-20260726-TRACE Unlocking Effective/trace_unlocking_effective_manuscript.md` - TRACE Unlocking Effective - DEP-E; overlap: effective, inference, cache, time.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
