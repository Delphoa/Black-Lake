# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P391`
- Public-safe date: 2026-08-19
- Paper: *How Mobile World Model Guides GUI Agents?*
- Identifier: `arXiv:2605.10347`; DOI: `10.48550/arXiv.2605.10347`
- URL: https://arxiv.org/abs/2605.10347

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 44,006 on draw 22.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: world model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `How-Mobile-World-Model-Guides-GUI-Agents` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 18; source-gate exclusions: 1; reselections: 21.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 21,099,476 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 45; sampled text inspection: true.
- Full-paper HTML: 646,626 bytes, 130,656 body characters, 109 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-How-Mobile-World-Model-Guides-GUI-Agents-LOG.md`
- `.reports/BL-Arxiv-How-Mobile-World-Model-Guides-GUI-Agents-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-How Mobile World Model/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-How Mobile World Model/how_mobile_world_model_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-MobileWorldBench Towards/mobileworldbench_towards_manuscript.md` - MobileWorldBench Towards - DEP-E; overlap: mobile, agents, world, how.
2. `.lake-data/DEP-E/DEP-E-20260730-MCPWorld Benchmark/mcpworld_manuscript.md` - MCPWorld - DEP-E; overlap: gui, agents, how.
3. `.lake-data/DEP-E/DEP-E-20260819-ARPO End-to-End Policy/arpo_end_to_end_policy_manuscript.md` - ARPO End-to-End Policy - DEP-E; overlap: gui, agents, how.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
