# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260811-BB3E2A1B`
- Deployment item ID: `BLAD-2200-20260811-BB3E2A1B-P03`
- Public-safe date: 2026-08-11
- Paper: *PA-RNet: Perturbation-Aware Residual Network for Robust Multimodal Time Series Forecasting*
- Identifier: `arXiv:2508.04750`; DOI: `10.48550/arXiv.2508.04750`
- URL: https://arxiv.org/abs/2508.04750

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 64,903 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `PA-RNet-Perturbation-Aware-Residual-Network-for` slug; the 24-hour marker cutoff was 2026-08-10.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,433,431 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 36; sampled text inspection: true.
- Full-paper HTML: 3,472,407 bytes, 175,122 body characters, 65 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260811-Arxiv-PA-RNet-Perturbation-Aware-Residual-Network-for-LOG.md`
- `.reports/BL-Arxiv-PA-RNet-Perturbation-Aware-Residual-Network-for-20260811/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260811-PA-RNet/README.md`
- `.lake-data/DEP-E/DEP-E-20260811-PA-RNet/pa_rnet_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260729-Decentralized Attention/decentralized_attention_manuscript.md` - Decentralized Attention - DEP-E; overlap: series, time.
2. `.lake-data/DEP-E/DEP-E-20260802-Heartcare ECG/heartcare_ecg_manuscript.md` - Heartcare ECG - DEP-E; overlap: multimodal, residual, network, time.
3. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: multimodal, network, time.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
