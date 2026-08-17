# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260817-2C1A830E`
- Deployment item ID: `BLAD-2200-20260817-2C1A830E-P01`
- Public-safe date: 2026-08-17
- Paper: *STRUCTSENSE: A Task-Agnostic Agentic Framework for Structured Information Extraction with Human-In-The-Loop Evaluation and Benchmarking*
- Identifier: `arXiv:2507.03674`; DOI: `10.48550/arXiv.2507.03674`
- URL: https://arxiv.org/abs/2507.03674

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 58,998 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `STRUCTSENSE-A-Task-Agnostic-Agentic-Framework` slug; the 24-hour marker cutoff was 2026-08-16.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,775,852 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 21; sampled text inspection: true.
- Full-paper HTML: 354,085 bytes, 79,281 body characters, 129 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260817-Arxiv-STRUCTSENSE-A-Task-Agnostic-Agentic-Framework-LOG.md`
- `.reports/BL-Arxiv-STRUCTSENSE-A-Task-Agnostic-Agentic-Framework-20260817/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260817-STRUCTSENSE A/README.md`
- `.lake-data/DEP-E/DEP-E-20260817-STRUCTSENSE A/structsense_a_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260805-AgentEconomist/agent_economist_manuscript.md` - AgentEconomist - DEP-E; overlap: human-in-the-loop, agentic, information, structured, extraction.
2. `.lake-data/DEP-E/DEP-E-20260727-Kimi K2 5 Visual Agentic/kimi_k2_5_visual_agentic_manuscript.md` - Kimi K2 5 Visual Agentic - DEP-E; overlap: agentic, structured, extraction.
3. `.lake-data/DEP-E/DEP-E-20260809-ECHO Prune to act trace/echo_prune_to_act_trace_manuscript.md` - ECHO Prune to act trace - DEP-E; overlap: agentic, structured, extraction.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
