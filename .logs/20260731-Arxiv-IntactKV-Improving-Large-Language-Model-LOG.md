# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260731-3D09E72F`
- Deployment item ID: `BLAD-2200-20260731-3D09E72F-P08`
- Public-safe date: 2026-07-31
- Paper: *IntactKV: Improving Large Language Model Quantization by Keeping Pivot Tokens Intact*
- Identifier: `arXiv:2403.01241`; DOI: `10.48550/arXiv.2403.01241`
- URL: https://arxiv.org/abs/2403.01241

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 18,353 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `IntactKV-Improving-Large-Language-Model` slug; the 24-hour marker cutoff was 2026-07-30.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 38,384,022 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 26; sampled text inspection: true.
- Full-paper HTML: 799,663 bytes, 95,638 body characters, 117 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260731-Arxiv-IntactKV-Improving-Large-Language-Model-LOG.md`
- `.reports/BL-Arxiv-IntactKV-Improving-Large-Language-Model-20260731/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260731-IntactKV Improving Large/README.md`
- `.lake-data/DEP-E/DEP-E-20260731-IntactKV Improving Large/intactkv_improving_large_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: quantization, pruning, improving, sparsity, tokens.
2. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: quantization, pruning, sparsity, tokens, compression.
3. `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md` - Telecom AI Roadmap - DEP-E; overlap: quantization, pruning, improving, compression, language.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
