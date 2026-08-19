# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P31`
- Public-safe date: 2026-08-19
- Paper: *DomainRAG: A Chinese Benchmark for Evaluating Domain-specific Retrieval-Augmented Generation*
- Identifier: `arXiv:2406.05654`; DOI: `10.48550/arXiv.2406.05654`
- URL: https://arxiv.org/abs/2406.05654

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 72,917 on draw 16.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `DomainRAG-A-Chinese-Benchmark-for-Evaluating` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 14; source-gate exclusions: 0; reselections: 15.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 721,644 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 186,164 bytes, 50,858 body characters, 42 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-DomainRAG-A-Chinese-Benchmark-for-Evaluating-LOG.md`
- `.reports/BL-Arxiv-DomainRAG-A-Chinese-Benchmark-for-Evaluating-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-DomainRAG A Chinese/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-DomainRAG A Chinese/domainrag_a_chinese_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-RAIR Retrieval-Augmented/rair_retrieval_augmented_manuscript.md` - RAIR Retrieval-Augmented - DEP-E; overlap: chinese, retrieval-augmented.
2. `.lake-data/DEP-E/DEP-E-20260719-DiscourseFlip RAG Risk/discourseflip_rag_risk_manuscript.md` - DiscourseFlip Risk Review; overlap: retrieval-augmented, generation, benchmark.
3. `.lake-data/DEP-E/DEP-E-20260818-Language-Coupled/language_coupled_manuscript.md` - Language-Coupled - DEP-E; overlap: retrieval-augmented, generation, benchmark.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
