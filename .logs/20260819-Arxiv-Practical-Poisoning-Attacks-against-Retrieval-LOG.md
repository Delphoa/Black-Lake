# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P262`
- Public-safe date: 2026-08-19
- Paper: *Practical Poisoning Attacks against Retrieval-Augmented Generation*
- Identifier: `arXiv:2504.03957`; DOI: `10.48550/arXiv.2504.03957`
- URL: https://arxiv.org/abs/2504.03957

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 32,018 on draw 1.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Practical-Poisoning-Attacks-against-Retrieval` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 801,431 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 509,393 bytes, 75,780 body characters, 62 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Practical-Poisoning-Attacks-against-Retrieval-LOG.md`
- `.reports/BL-Arxiv-Practical-Poisoning-Attacks-against-Retrieval-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Practical Poisoning/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Practical Poisoning/practical_poisoning_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-DiscourseFlip RAG Risk/discourseflip_rag_risk_manuscript.md` - DiscourseFlip Risk Review; overlap: retrieval-augmented, generation, poisoning, attacks.
2. `.lake-data/DEP-E/DEP-E-20260818-A-RAG Scaling Agentic/a_rag_scaling_agentic_manuscript.md` - A-RAG Scaling Agentic - DEP-E; overlap: retrieval-augmented, generation, practical.
3. `.lake-data/DEP-E/DEP-E-20260818-Language-Coupled/language_coupled_manuscript.md` - Language-Coupled - DEP-E; overlap: retrieval-augmented, generation, practical.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
