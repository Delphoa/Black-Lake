# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P131`
- Public-safe date: 2026-08-19
- Paper: *Sparse-dLLM: Accelerating Diffusion LLMs with Dynamic Cache Eviction*
- Identifier: `arXiv:2508.02558`; DOI: `10.48550/arXiv.2508.02558`
- URL: https://arxiv.org/abs/2508.02558

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 69,228 on draw 2.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: cache eviction.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Sparse-dLLM-Accelerating-Diffusion-LLMs-with` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 1; source-gate exclusions: 0; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 4,324,940 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 12; sampled text inspection: true.
- Full-paper HTML: 432,847 bytes, 54,955 body characters, 78 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Sparse-dLLM-Accelerating-Diffusion-LLMs-with-LOG.md`
- `.reports/BL-Arxiv-Sparse-dLLM-Accelerating-Diffusion-LLMs-with-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Sparse-dLLM Accelerating/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Sparse-dLLM Accelerating/sparse_dllm_accelerating_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Accelerating LLM/accelerating_llm_manuscript.md` - Accelerating LLM - DEP-E; overlap: accelerating, dynamic, cache, llms.
2. `.lake-data/DEP-E/DEP-E-20260819-Accelerating Min-Max/accelerating_min_max_manuscript.md` - Accelerating Min-Max - DEP-E; overlap: accelerating, cache.
3. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: diffusion, eviction, dynamic, cache.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
