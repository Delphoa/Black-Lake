# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260721-F7EDC854`
- Deployment item ID: `BLAD-2200-20260721-F7EDC854-P03`
- Public-safe date: 2026-07-21
- Paper: *Urban Visual Intelligence: Studying Cities with AI and Street-level Imagery*
- Identifier: `arXiv:2301.00580`; DOI: `10.48550/arXiv.2301.00580`
- URL: https://arxiv.org/abs/2301.00580

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,779 PDFs and 75,776 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 66,698 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Urban-Visual-Intelligence` slug; the 24-hour marker cutoff was 2026-07-20.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded archive repair.
- PDF: 2,121,699 bytes with a valid `%PDF-` header and trailing `%%EOF`.
- Full-paper HTML: 202,230 bytes, 109,730 body characters, 2 document markers, 51 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260721-Arxiv-Urban-Visual-Intelligence-LOG.md`
- `.reports/BL-Arxiv-Urban-Visual-Intelligence-20260721/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260721-Urban Visual Intelligence/README.md`
- `.lake-data/DEP-E/DEP-E-20260721-Urban Visual Intelligence/urban_visual_intelligence_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
