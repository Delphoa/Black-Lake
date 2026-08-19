# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P375`
- Public-safe date: 2026-08-19
- Paper: *MIRAGE: Misleading Retrieval-Augmented Generation via Black-box and Query-agnostic Poisoning Attacks*
- Identifier: `arXiv:2512.08289`; DOI: `10.48550/arXiv.2512.08289`
- URL: https://arxiv.org/abs/2512.08289

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 43,711 on draw 7.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `MIRAGE-Misleading-Retrieval-Augmented-Generation` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 6; source-gate exclusions: 0; reselections: 6.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,839,035 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 26; sampled text inspection: true.
- Full-paper HTML: 735,829 bytes, 157,224 body characters, 97 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-MIRAGE-Misleading-Retrieval-Augmented-Generation-LOG.md`
- `.reports/BL-Arxiv-MIRAGE-Misleading-Retrieval-Augmented-Generation-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-MIRAGE Misleading/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-MIRAGE Misleading/mirage_misleading_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Practical Poisoning/practical_poisoning_manuscript.md` - Practical Poisoning - DEP-E; overlap: poisoning, attacks, retrieval-augmented, generation, misleading.
2. `.lake-data/DEP-E/DEP-E-20260719-DiscourseFlip RAG Risk/discourseflip_rag_risk_manuscript.md` - DiscourseFlip Risk Review; overlap: black-box, retrieval-augmented, generation, poisoning, attacks.
3. `.lake-data/DEP-E/DEP-E-20260819-UniC-RAG Universal/unic_rag_universal_manuscript.md` - UniC-RAG Universal - DEP-E; overlap: attacks, retrieval-augmented, generation, poisoning, misleading.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
