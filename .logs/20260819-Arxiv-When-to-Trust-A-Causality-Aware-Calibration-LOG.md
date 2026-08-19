# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P465`
- Public-safe date: 2026-08-19
- Paper: *When to Trust: A Causality-Aware Calibration Framework for Accurate Knowledge Graph Retrieval-Augmented Generation*
- Identifier: `arXiv:2601.09241`; DOI: `10.48550/arXiv.2601.09241`
- URL: https://arxiv.org/abs/2601.09241

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 23,139 on draw 33.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `When-to-Trust-A-Causality-Aware-Calibration` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 30; source-gate exclusions: 0; reselections: 32.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,322,016 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 334,162 bytes, 69,214 body characters, 76 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-When-to-Trust-A-Causality-Aware-Calibration-LOG.md`
- `.reports/BL-Arxiv-When-to-Trust-A-Causality-Aware-Calibration-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-When to Trust A/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-When to Trust A/when_to_trust_a_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Knowledge Graph/knowledge_graph_manuscript.md` - Knowledge Graph - DEP-E; overlap: retrieval-augmented, knowledge, graph, generation, calibration.
2. `.lake-data/DEP-E/DEP-E-20260819-When Machine Unlearning/when_machine_unlearning_manuscript.md` - When Machine Unlearning - DEP-E; overlap: retrieval-augmented, knowledge, generation, when, calibration.
3. `.lake-data/DEP-E/DEP-E-20260819-BubbleRAG Evidence-Driven/bubblerag_evidence_driven_manuscript.md` - BubbleRAG Evidence-Driven - DEP-E; overlap: retrieval-augmented, knowledge, generation, calibration, when.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
