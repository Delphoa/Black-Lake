# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260811-BB3E2A1B`
- Deployment item ID: `BLAD-2200-20260811-BB3E2A1B-P02`
- Public-safe date: 2026-08-11
- Paper: *CoEnv: Driving Embodied Multi-Agent Collaboration via Compositional Environment*
- Identifier: `arXiv:2604.05484`; DOI: `10.48550/arXiv.2604.05484`
- URL: https://arxiv.org/abs/2604.05484

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 66,173 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `CoEnv-Driving-Embodied-Multi-Agent-Collaboration` slug; the 24-hour marker cutoff was 2026-08-10.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 12,397,441 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 31; sampled text inspection: true.
- Full-paper HTML: 606,792 bytes, 82,824 body characters, 109 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260811-Arxiv-CoEnv-Driving-Embodied-Multi-Agent-Collaboration-LOG.md`
- `.reports/BL-Arxiv-CoEnv-Driving-Embodied-Multi-Agent-Collaboration-20260811/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260811-CoEnv Driving Embodied/README.md`
- `.lake-data/DEP-E/DEP-E-20260811-CoEnv Driving Embodied/coenv_driving_embodied_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md` - Semantic Skill MoE Policies; overlap: compositional.
2. `.lake-data/DEP-E/DEP-E-20260720-Context Backdoor/context_backdoor_defense_manuscript.md` - Context Backdoor Defense - DEP-E; overlap: embodied.
3. `.lake-data/DEP-E/DEP-E-20260726-ManipulationNet An/manipulationnet_an_manuscript.md` - ManipulationNet An - DEP-E; overlap: embodied.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
