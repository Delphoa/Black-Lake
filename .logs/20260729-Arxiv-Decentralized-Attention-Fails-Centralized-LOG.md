# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260729-5EE3EF9C`
- Deployment item ID: `BLAD-2200-20260729-5EE3EF9C-P03`
- Public-safe date: 2026-07-29
- Paper: *Decentralized Attention Fails Centralized Signals: Rethinking Transformers for Medical Time Series*
- Identifier: `arXiv:2602.18473`; DOI: `10.48550/arXiv.2602.18473`
- URL: https://arxiv.org/abs/2602.18473

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 75,230 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Decentralized-Attention-Fails-Centralized` slug; the 24-hour marker cutoff was 2026-07-28.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 4,477,676 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 21; sampled text inspection: true.
- Full-paper HTML: 855,573 bytes, 94,929 body characters, 77 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260729-Arxiv-Decentralized-Attention-Fails-Centralized-LOG.md`
- `.reports/BL-Arxiv-Decentralized-Attention-Fails-Centralized-20260729/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260729-Decentralized Attention/README.md`
- `.lake-data/DEP-E/DEP-E-20260729-Decentralized Attention/decentralized_attention_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260722-Temporal Feature Matters/temporal_feature_matters_manuscript.md` - Temporal Feature Matters Review - DEP-E; overlap: temporal, quantization.
2. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` - Adversarial Label Noise - DEP-E; overlap: mismatch, training.
3. `.lake-data/DEP-E/DEP-E-20260715-MSAIC ECG/msaic_ecg_manuscript.md` - MSAIC ECG - DEP-E; overlap: ecg, design.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
