# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P98`
- Public-safe date: 2026-08-19
- Paper: *ArchRAG: Attributed Community-based Hierarchical Retrieval-Augmented Generation*
- Identifier: `arXiv:2502.09891`; DOI: `10.1609/aaai.v40i19.38619`
- URL: https://arxiv.org/abs/2502.09891

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 19,051 on draw 12.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `ArchRAG-Attributed-Community-based-Hierarchical` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 11; source-gate exclusions: 0; reselections: 11.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,246,469 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 20; sampled text inspection: true.
- Full-paper HTML: 556,090 bytes, 88,037 body characters, 75 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-ArchRAG-Attributed-Community-based-Hierarchical-LOG.md`
- `.reports/BL-Arxiv-ArchRAG-Attributed-Community-based-Hierarchical-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-ArchRAG Attributed/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-ArchRAG Attributed/archrag_attributed_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-A-RAG Scaling Agentic/a_rag_scaling_agentic_manuscript.md` - A-RAG Scaling Agentic - DEP-E; overlap: retrieval-augmented, hierarchical, generation.
2. `.lake-data/DEP-E/DEP-E-20260819-BookRAG A Hierarchical/bookrag_a_hierarchical_manuscript.md` - BookRAG A Hierarchical - DEP-E; overlap: retrieval-augmented, hierarchical, generation.
3. `.lake-data/DEP-E/DEP-E-20260719-DiscourseFlip RAG Risk/discourseflip_rag_risk_manuscript.md` - DiscourseFlip Risk Review; overlap: retrieval-augmented, generation, attributed.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
