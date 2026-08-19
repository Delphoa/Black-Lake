# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P33`
- Public-safe date: 2026-08-19
- Paper: *CWM: An Open-Weights LLM for Research on Code Generation with World Models*
- Identifier: `arXiv:2510.02387`; DOI: `10.48550/arXiv.2510.02387`
- URL: https://arxiv.org/abs/2510.02387

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 16,356 on draw 8.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: world model.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `CWM-An-Open-Weights-LLM-for-Research` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 7; source-gate exclusions: 0; reselections: 7.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,556,676 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 58; sampled text inspection: true.
- Full-paper HTML: 2,461,034 bytes, 234,151 body characters, 120 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-CWM-An-Open-Weights-LLM-for-Research-LOG.md`
- `.reports/BL-Arxiv-CWM-An-Open-Weights-LLM-for-Research-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-CWM An Open-Weights LLM/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-CWM An Open-Weights LLM/cwm_an_open_weights_llm_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` - HERMES World Model - DEP-E; overlap: world, generation.
2. `.lake-data/DEP-E/DEP-E-20260809-NaLA A 3D Native LLM/nala_a_3d_native_llm_manuscript.md` - NaLA A 3D Native LLM - DEP-E; overlap: llm, generation.
3. `.lake-data/DEP-E/DEP-E-20260818-Inner-Probe Discovering/inner_probe_discovering_manuscript.md` - Inner-Probe Discovering - DEP-E; overlap: llm, generation.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
