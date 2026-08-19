# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P57`
- Public-safe date: 2026-08-19
- Paper: *Group-based control of large-scale micro-robot swarms with on-board Physical Finite-State Machines*
- Identifier: `arXiv:2208.08614`; DOI: `10.48550/arXiv.2208.08614`
- URL: https://arxiv.org/abs/2208.08614

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 33,160 on draw 30.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: finite state.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Group-based-control-of-large-scale-micro` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 27; source-gate exclusions: 0; reselections: 29.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,783,274 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 7; sampled text inspection: true.
- Full-paper HTML: 246,336 bytes, 47,057 body characters, 51 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Group-based-control-of-large-scale-micro-LOG.md`
- `.reports/BL-Arxiv-Group-based-control-of-large-scale-micro-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Group-based control of/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Group-based control of/group_based_control_of_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md` - Group-Control Swarms - DEP-E; overlap: swarms, finite-state, machines, physical, control.
2. `.lake-data/DEP-E/DEP-E-20260819-Listwise Policy/listwise_policy_manuscript.md` - Listwise Policy - DEP-E; overlap: group-based, control.
3. `.lake-data/DEP-E/DEP-E-20260819-LLM-FSM Scaling Large/llm_fsm_scaling_large_manuscript.md` - LLM-FSM Scaling Large - DEP-E; overlap: finite-state, large-scale, control.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
