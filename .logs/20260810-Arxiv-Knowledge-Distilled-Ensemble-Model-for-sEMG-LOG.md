# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260810-B3B6846E`
- Deployment item ID: `BLAD-2200-20260810-B3B6846E-P06`
- Public-safe date: 2026-08-10
- Paper: *Knowledge Distilled Ensemble Model for sEMG-based Silent Speech Interface*
- Identifier: `arXiv:2308.06533`; DOI: `10.48550/arXiv.2308.06533`
- URL: https://arxiv.org/abs/2308.06533

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 13,095 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Knowledge-Distilled-Ensemble-Model-for-sEMG` slug; the 24-hour marker cutoff was 2026-08-09.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 10,448,059 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 6; sampled text inspection: true.
- Full-paper HTML: 221,033 bytes, 31,513 body characters, 50 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260810-Arxiv-Knowledge-Distilled-Ensemble-Model-for-sEMG-LOG.md`
- `.reports/BL-Arxiv-Knowledge-Distilled-Ensemble-Model-for-sEMG-20260810/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260810-Knowledge Distilled/README.md`
- `.lake-data/DEP-E/DEP-E-20260810-Knowledge Distilled/knowledge_distilled_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-Cued Speech MLLM/cued_speech_mllm_manuscript.md` - Cued Speech MLLM Review - DEP-E; overlap: speech.
2. `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` - KDFlow LLM Distill - DEP-E; overlap: knowledge, distilled.
3. `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` - CorrKD Missing Modal - DEP-E; overlap: knowledge, interface.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
