# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P119`
- Public-safe date: 2026-08-19
- Paper: *Enhancing Local Search for MaxSAT with Deep Differentiation Clause Weighting*
- Identifier: `arXiv:2512.05619`; DOI: `10.48550/arXiv.2512.05619`
- URL: https://arxiv.org/abs/2512.05619

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 25,749 on draw 9.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: search.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Enhancing-Local-Search-for-MaxSAT-with-Deep` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 7; source-gate exclusions: 0; reselections: 8.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 289,240 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 8; sampled text inspection: true.
- Full-paper HTML: 349,620 bytes, 60,004 body characters, 46 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Enhancing-Local-Search-for-MaxSAT-with-Deep-LOG.md`
- `.reports/BL-Arxiv-Enhancing-Local-Search-for-MaxSAT-with-Deep-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Enhancing Local Search/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Enhancing Local Search/enhancing_local_search_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Coordinated CIL/coordinated_cil_manuscript.md` - Input-Output Coordinated CIL; overlap: weighting.
2. `.lake-data/DEP-E/DEP-E-20260819-SpeeD Time Steps/speed_time_steps_manuscript.md` - SpeeD Time Steps - DEP-E; overlap: weighting.
3. `.lake-data/DEP-E/DEP-E-20260724-WorkflowLLM Enhancing/workflowllm_enhancing_manuscript.md` - WorkflowLLM Enhancing - DEP-E; overlap: enhancing.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
