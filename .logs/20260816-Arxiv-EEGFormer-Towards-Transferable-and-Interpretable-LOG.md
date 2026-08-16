# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260816-7EAAB41B`
- Deployment item ID: `BLAD-2200-20260816-7EAAB41B-P06`
- Public-safe date: 2026-08-16
- Paper: *EEGFormer: Towards Transferable and Interpretable Large-Scale EEG Foundation Model*
- Identifier: `arXiv:2401.10278`; DOI: `10.48550/arXiv.2401.10278`
- URL: https://arxiv.org/abs/2401.10278

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 66,277 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `EEGFormer-Towards-Transferable-and-Interpretable` slug; the 24-hour marker cutoff was 2026-08-15.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,541,709 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 6; sampled text inspection: true.
- Full-paper HTML: 115,399 bytes, 30,468 body characters, 53 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260816-Arxiv-EEGFormer-Towards-Transferable-and-Interpretable-LOG.md`
- `.reports/BL-Arxiv-EEGFormer-Towards-Transferable-and-Interpretable-20260816/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260816-EEGFormer Towards/README.md`
- `.lake-data/DEP-E/DEP-E-20260816-EEGFormer Towards/eegformer_towards_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260728-CanCal Towards Real-time/cancal_towards_real_time_manuscript.md` - CanCal Towards Real-time - DEP-E; overlap: towards, large-scale.
2. `.lake-data/DEP-E/DEP-E-20260730-RLHF-V Towards/rlhf_v_towards_manuscript.md` - RLHF-V Towards - DEP-E; overlap: towards.
3. `.lake-data/DEP-E/DEP-E-20260809-Discriminative and/discriminative_and_manuscript.md` - Discriminative and - DEP-E; overlap: towards.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
