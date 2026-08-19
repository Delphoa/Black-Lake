# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P197`
- Public-safe date: 2026-08-19
- Paper: *When Machine Unlearning Meets Retrieval-Augmented Generation (RAG): Keep Secret or Forget Knowledge?*
- Identifier: `arXiv:2410.15267`; DOI: `10.48550/arXiv.2410.15267`
- URL: https://arxiv.org/abs/2410.15267

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 52,547 on draw 45.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `When-Machine-Unlearning-Meets-Retrieval` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 9; focus exclusions: 35; source-gate exclusions: 0; reselections: 44.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,140,127 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 16; sampled text inspection: true.
- Full-paper HTML: 393,949 bytes, 95,481 body characters, 97 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-When-Machine-Unlearning-Meets-Retrieval-LOG.md`
- `.reports/BL-Arxiv-When-Machine-Unlearning-Meets-Retrieval-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-When Machine Unlearning/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-When Machine Unlearning/when_machine_unlearning_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md` - FOLTR Unlearning - DEP-E; overlap: forget, unlearning, keep, machine, when.
2. `.lake-data/DEP-E/DEP-E-20260819-SafeDriveRAG Towards Safe/safedriverag_towards_safe_manuscript.md` - SafeDriveRAG Towards Safe - DEP-E; overlap: retrieval-augmented, knowledge, generation, rag, when.
3. `.lake-data/DEP-E/DEP-E-20260819-UniC-RAG Universal/unic_rag_universal_manuscript.md` - UniC-RAG Universal - DEP-E; overlap: retrieval-augmented, knowledge, generation, rag, when.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
