# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-50A35360`
- Deployment item ID: `BLAD-2200-20260818-50A35360-P02`
- Public-safe date: 2026-08-18
- Paper: *Inner-Probe: Discovering Copyright-related Data Generation in LLM Architecture*
- Identifier: `arXiv:2410.04454`; DOI: `10.1109/TAI.2025.3645710`
- URL: https://arxiv.org/abs/2410.04454

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 9,053 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Inner-Probe-Discovering-Copyright-related-Data` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,349,948 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 15; sampled text inspection: true.
- Full-paper HTML: 422,425 bytes, 89,266 body characters, 80 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Inner-Probe-Discovering-Copyright-related-Data-LOG.md`
- `.reports/BL-Arxiv-Inner-Probe-Discovering-Copyright-related-Data-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Inner-Probe Discovering/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Inner-Probe Discovering/inner_probe_discovering_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260809-NaLA A 3D Native LLM/nala_a_3d_native_llm_manuscript.md` - NaLA A 3D Native LLM - DEP-E; overlap: llm, generation, architecture.
2. `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal/llm_judge_conformal_manuscript.md` - Judge Conformal - DEP-E; overlap: llm, generation, architecture.
3. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: llm, generation, architecture.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
