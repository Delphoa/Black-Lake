# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260809-2E4CB30E`
- Deployment item ID: `BLAD-2200-20260809-2E4CB30E-P03`
- Public-safe date: 2026-08-09
- Paper: *NaLA: A 3D Native LLM Layout Agent for High-quality 3D Scene Generation*
- Identifier: `arXiv:2606.29395`; DOI: `10.48550/arXiv.2606.29395`
- URL: https://arxiv.org/abs/2606.29395

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 45,087 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `NaLA-A-3D-Native-LLM-Layout-Agent` slug; the 24-hour marker cutoff was 2026-08-08.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 23,250,345 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 27; sampled text inspection: true.
- Full-paper HTML: 487,687 bytes, 63,137 body characters, 87 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260809-Arxiv-NaLA-A-3D-Native-LLM-Layout-Agent-LOG.md`
- `.reports/BL-Arxiv-NaLA-A-3D-Native-LLM-Layout-Agent-20260809/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260809-NaLA A 3D Native LLM/README.md`
- `.lake-data/DEP-E/DEP-E-20260809-NaLA A 3D Native LLM/nala_a_3d_native_llm_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md` - SAGE-Nav Review - DEP-E; overlap: navigable, robotic, robot, navigation, scene.
2. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: orchestration, workflows, queries, tools, agents.
3. `.lake-data/DEP-E/DEP-E-20260805-AgentEconomist/agent_economist_manuscript.md` - AgentEconomist - DEP-E; overlap: database, instruction, tools, agents, query.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
