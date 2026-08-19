# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P18`
- Public-safe date: 2026-08-19
- Paper: *UniC-RAG: Universal Knowledge Corruption Attacks to Retrieval-Augmented Generation*
- Identifier: `arXiv:2508.18652`; DOI: `10.48550/arXiv.2508.18652`
- URL: https://arxiv.org/abs/2508.18652

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 13,890 on draw 2.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `UniC-RAG-Universal-Knowledge-Corruption-Attacks` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 1; source-gate exclusions: 0; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 558,047 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 21; sampled text inspection: true.
- Full-paper HTML: 438,114 bytes, 95,340 body characters, 75 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-UniC-RAG-Universal-Knowledge-Corruption-Attacks-LOG.md`
- `.reports/BL-Arxiv-UniC-RAG-Universal-Knowledge-Corruption-Attacks-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-UniC-RAG Universal/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-UniC-RAG Universal/unic_rag_universal_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Practical Poisoning/practical_poisoning_manuscript.md` - Practical Poisoning - DEP-E; overlap: attacks, retrieval-augmented, generation.
2. `.lake-data/DEP-E/DEP-E-20260819-SafeDriveRAG Towards Safe/safedriverag_towards_safe_manuscript.md` - SafeDriveRAG Towards Safe - DEP-E; overlap: retrieval-augmented, knowledge, generation.
3. `.lake-data/DEP-E/DEP-E-20260819-DRAK Unlocking Molecular/drak_unlocking_molecular_manuscript.md` - DRAK Unlocking Molecular - DEP-E; overlap: retrieval-augmented, knowledge.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
