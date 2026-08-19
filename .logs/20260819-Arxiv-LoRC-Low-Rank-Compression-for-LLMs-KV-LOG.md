# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P362`
- Public-safe date: 2026-08-19
- Paper: *LoRC: Low-Rank Compression for LLMs KV Cache with a Progressive Compression Strategy*
- Identifier: `arXiv:2410.03111`; DOI: `10.48550/arXiv.2410.03111`
- URL: https://arxiv.org/abs/2410.03111

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 44,459 on draw 7.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: kv cache.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `LoRC-Low-Rank-Compression-for-LLMs-KV` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 6; source-gate exclusions: 0; reselections: 6.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 681,529 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 15; sampled text inspection: true.
- Full-paper HTML: 258,217 bytes, 58,957 body characters, 76 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-LoRC-Low-Rank-Compression-for-LLMs-KV-LOG.md`
- `.reports/BL-Arxiv-LoRC-Low-Rank-Compression-for-LLMs-KV-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-LoRC Low-Rank Compression/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-LoRC Low-Rank Compression/lorc_low_rank_compression_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: low-rank, compression, cache, strategy.
2. `.lake-data/DEP-E/DEP-E-20260817-On the Transformer Growth/on_the_transformer_growth_manuscript.md` - On the Transformer Growth - DEP-E; overlap: progressive, cache, strategy.
3. `.lake-data/DEP-E/DEP-E-20260819-Clo-HDnn A 4 66 TFLOPS W/clo_hdnn_a_4_66_tflops_w_manuscript.md` - Clo-HDnn A 4 66 TFLOPS W - DEP-E; overlap: progressive, cache, strategy.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
