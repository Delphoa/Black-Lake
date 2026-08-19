# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P36`
- Public-safe date: 2026-08-19
- Paper: *WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG*
- Identifier: `arXiv:2603.23497`; DOI: `10.48550/arXiv.2603.23497`
- URL: https://arxiv.org/abs/2603.23497

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 2,835 on draw 9.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: world model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `WildWorld-A-Large-Scale-Dataset-for-Dynamic` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 7; source-gate exclusions: 0; reselections: 8.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 4,278,409 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 157,041 bytes, 52,021 body characters, 46 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-WildWorld-A-Large-Scale-Dataset-for-Dynamic-LOG.md`
- `.reports/BL-Arxiv-WildWorld-A-Large-Scale-Dataset-for-Dynamic-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-WildWorld A Large-Scale/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-WildWorld A Large-Scale/wildworld_a_large_scale_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Improving Generative/improving_generative_manuscript.md` - Improving Generative - DEP-E; overlap: generative, world, explicit.
2. `.lake-data/DEP-E/DEP-E-20260819-Data-driven Modeling of/data_driven_modeling_of_manuscript.md` - Data-driven Modeling of - DEP-E; overlap: generative, modeling, explicit.
3. `.lake-data/DEP-E/DEP-E-20260804-In-Context World Modeling/in_context_world_modeling_manuscript.md` - In-Context World Modeling - DEP-E; overlap: world, modeling, explicit.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
