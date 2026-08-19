# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P108`
- Public-safe date: 2026-08-19
- Paper: *Accelerating LLM Inference via Dynamic KV Cache Placement in Heterogeneous Memory System*
- Identifier: `arXiv:2508.13231`; DOI: `10.48550/arXiv.2508.13231`
- URL: https://arxiv.org/abs/2508.13231

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 24,671 on draw 52.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: kv cache.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Accelerating-LLM-Inference-via-Dynamic-KV-Cache` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 50; source-gate exclusions: 0; reselections: 51.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 650,419 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 4; sampled text inspection: true.
- Full-paper HTML: 116,281 bytes, 29,253 body characters, 34 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Accelerating-LLM-Inference-via-Dynamic-KV-Cache-LOG.md`
- `.reports/BL-Arxiv-Accelerating-LLM-Inference-via-Dynamic-KV-Cache-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Accelerating LLM/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Accelerating LLM/accelerating_llm_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Accelerating Min-Max/accelerating_min_max_manuscript.md` - Accelerating Min-Max - DEP-E; overlap: accelerating, cache, memory.
2. `.lake-data/DEP-E/DEP-E-20260819-Shadow in the Cache/shadow_in_the_cache_manuscript.md` - Shadow in the Cache - DEP-E; overlap: llm, inference, cache, memory.
3. `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` - HSD FTI-FDet - DEP-E; overlap: heterogeneous, placement, inference, cache, memory.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
