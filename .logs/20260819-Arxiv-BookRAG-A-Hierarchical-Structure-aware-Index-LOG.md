# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P182`
- Public-safe date: 2026-08-19
- Paper: *BookRAG: A Hierarchical Structure-aware Index-based Approach for Retrieval-Augmented Generation on Complex Documents*
- Identifier: `arXiv:2512.03413`; DOI: `10.48550/arXiv.2512.03413`
- URL: https://arxiv.org/abs/2512.03413

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 55,423 on draw 35.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `BookRAG-A-Hierarchical-Structure-aware-Index` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 5; focus exclusions: 29; source-gate exclusions: 0; reselections: 34.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,093,031 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 20; sampled text inspection: true.
- Full-paper HTML: 872,669 bytes, 98,595 body characters, 91 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-BookRAG-A-Hierarchical-Structure-aware-Index-LOG.md`
- `.reports/BL-Arxiv-BookRAG-A-Hierarchical-Structure-aware-Index-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-BookRAG A Hierarchical/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-BookRAG A Hierarchical/bookrag_a_hierarchical_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-A-RAG Scaling Agentic/a_rag_scaling_agentic_manuscript.md` - A-RAG Scaling Agentic - DEP-E; overlap: retrieval-augmented, hierarchical, generation.
2. `.lake-data/DEP-E/DEP-E-20260819-Breaking the Static Graph/breaking_the_static_graph_manuscript.md` - Breaking the Static Graph - DEP-E; overlap: retrieval-augmented, generation, structure-aware.
3. `.lake-data/DEP-E/DEP-E-20260719-DiscourseFlip RAG Risk/discourseflip_rag_risk_manuscript.md` - DiscourseFlip Risk Review; overlap: retrieval-augmented, generation, documents.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
