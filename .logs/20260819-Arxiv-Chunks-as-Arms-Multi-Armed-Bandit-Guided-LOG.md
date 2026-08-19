# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P128`
- Public-safe date: 2026-08-19
- Paper: *Chunks as Arms: Multi-Armed Bandit-Guided Sampling for Long-Context LLM Preference Optimization*
- Identifier: `arXiv:2508.13993`; DOI: `10.48550/arXiv.2508.13993`
- URL: https://arxiv.org/abs/2508.13993

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 30,868 on draw 22.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: optimization.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Chunks-as-Arms-Multi-Armed-Bandit-Guided` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 20; source-gate exclusions: 0; reselections: 21.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,280,221 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 17; sampled text inspection: true.
- Full-paper HTML: 341,750 bytes, 66,420 body characters, 53 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Chunks-as-Arms-Multi-Armed-Bandit-Guided-LOG.md`
- `.reports/BL-Arxiv-Chunks-as-Arms-Multi-Armed-Bandit-Guided-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Chunks as Arms/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Chunks as Arms/chunks_as_arms_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-TIS-DPO Token-level/tis_dpo_token_level_manuscript.md` - TIS-DPO Token-level - DEP-E; overlap: preference, sampling, optimization.
2. `.lake-data/DEP-E/DEP-E-20260719-CLOVER Test Benchmark/clover_test_benchmark_manuscript.md` - CLOVER Test Benchmark - DEP-E; overlap: long-context, llm, optimization.
3. `.lake-data/DEP-E/DEP-E-20260818-Hamming Attention/hamming_attention_manuscript.md` - Hamming Attention - DEP-E; overlap: long-context.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
