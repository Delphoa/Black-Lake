# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P165`
- Public-safe date: 2026-08-19
- Paper: *How Much Reasoning Do Retrieval-Augmented Models Add beyond LLMs? A Benchmarking Framework for Multi-Hop Inference over Hybrid Knowledge*
- Identifier: `arXiv:2602.10210`; DOI: `10.48550/arXiv.2602.10210`
- URL: https://arxiv.org/abs/2602.10210

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 14,031 on draw 6.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: retrieval augmented.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `How-Much-Reasoning-Do-Retrieval-Augmented-Models` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 5; source-gate exclusions: 0; reselections: 5.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,383,012 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 12; sampled text inspection: true.
- Full-paper HTML: 1,053,619 bytes, 81,396 body characters, 73 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-How-Much-Reasoning-Do-Retrieval-Augmented-Models-LOG.md`
- `.reports/BL-Arxiv-How-Much-Reasoning-Do-Retrieval-Augmented-Models-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-How Much Reasoning Do/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-How Much Reasoning Do/how_much_reasoning_do_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-Are LLMs Capable of/are_llms_capable_of_manuscript.md` - Are LLMs Capable of - DEP-E; overlap: benchmarking, llms, reasoning, how.
2. `.lake-data/DEP-E/DEP-E-20260819-SafeDriveRAG Towards Safe/safedriverag_towards_safe_manuscript.md` - SafeDriveRAG Towards Safe - DEP-E; overlap: retrieval-augmented, knowledge, how.
3. `.lake-data/DEP-E/DEP-E-20260819-Tug-of-War Between/tug_of_war_between_manuscript.md` - Tug-of-War Between - DEP-E; overlap: retrieval-augmented, knowledge, how.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
