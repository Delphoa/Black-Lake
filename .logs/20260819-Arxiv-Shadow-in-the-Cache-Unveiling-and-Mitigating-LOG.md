# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P131`
- Public-safe date: 2026-08-19
- Paper: *Shadow in the Cache: Unveiling and Mitigating Privacy Risks of KV-cache in LLM Inference*
- Identifier: `arXiv:2508.09442`; DOI: `10.48550/arXiv.2508.09442`
- URL: https://arxiv.org/abs/2508.09442

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 68,862 on draw 15.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: kv cache.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Shadow-in-the-Cache-Unveiling-and-Mitigating` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 13; source-gate exclusions: 0; reselections: 14.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,175,611 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 18; sampled text inspection: true.
- Full-paper HTML: 574,372 bytes, 108,450 body characters, 114 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Shadow-in-the-Cache-Unveiling-and-Mitigating-LOG.md`
- `.reports/BL-Arxiv-Shadow-in-the-Cache-Unveiling-and-Mitigating-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Shadow in the Cache/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Shadow in the Cache/shadow_in_the_cache_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-KSHSeek Data-Driven Appro/kshseek_data_driven_appro_manuscript.md` - KSHSeek Data-Driven Approaches t - DEP-E; overlap: mitigating, privacy, cache.
2. `.lake-data/DEP-E/DEP-E-20260819-A Hierarchical Gradient/a_hierarchical_gradient_manuscript.md` - A Hierarchical Gradient - DEP-E; overlap: mitigating, privacy, cache.
3. `.lake-data/DEP-E/DEP-E-20260723-Unveiling the Lexical Sen/unveiling_the_lexical_sen_manuscript.md` - Unveiling the Lexical Sensitivit - DEP-E; overlap: unveiling, privacy, cache.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
