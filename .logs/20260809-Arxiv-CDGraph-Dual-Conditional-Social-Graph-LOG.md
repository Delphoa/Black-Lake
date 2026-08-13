# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260809-2E4CB30E`
- Deployment item ID: `BLAD-2200-20260809-2E4CB30E-P10`
- Public-safe date: 2026-08-09
- Paper: *CDGraph: Dual Conditional Social Graph Synthesizing via Diffusion Model*
- Identifier: `arXiv:2311.01729`; DOI: `10.48550/arXiv.2311.01729`
- URL: https://arxiv.org/abs/2311.01729

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 33,498 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `CDGraph-Dual-Conditional-Social-Graph` slug; the 24-hour marker cutoff was 2026-08-08.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,574,342 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 19; sampled text inspection: true.
- Full-paper HTML: 1,212,046 bytes, 72,598 body characters, 54 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260809-Arxiv-CDGraph-Dual-Conditional-Social-Graph-LOG.md`
- `.reports/BL-Arxiv-CDGraph-Dual-Conditional-Social-Graph-20260809/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260809-CDGraph Dual Conditional/README.md`
- `.lake-data/DEP-E/DEP-E-20260809-CDGraph Dual Conditional/cdgraph_dual_conditional_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md` - Telecom AI Roadmap - DEP-E; overlap: synthesizing, diffusion, conditional.
2. `.lake-data/DEP-E/DEP-E-20260719-MA-VLM PNU Moderation/ma_vlm_pnu_moderation_manuscript.md` - MA-VLM Moderation - DEP-E; overlap: social, dual, conditional.
3. `.lake-data/DEP-E/DEP-E-20260802-Heartcare ECG/heartcare_ecg_manuscript.md` - Heartcare ECG - DEP-E; overlap: dual, diffusion, conditional.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
