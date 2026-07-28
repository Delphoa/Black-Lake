# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260728-EB036F17`
- Deployment item ID: `BLAD-2200-20260728-EB036F17-P01`
- Public-safe date: 2026-07-28
- Paper: *RandLoRA: Full-rank parameter-efficient fine-tuning of large models*
- Identifier: `arXiv:2502.00987`; DOI: `10.48550/arXiv.2502.00987`
- URL: https://arxiv.org/abs/2502.00987

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75781 PDFs and 75778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 66236.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant deposited identifiers, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `RandLoRA-Full-rank-parameter-efficient-fine-tuning-of-large` slug; the 24-hour marker cutoff was 2026-07-27.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1072919 bytes with valid `%PDF-` header and trailing `%%EOF`; page markers: 31.
- Full-paper HTML: 1650877 bytes, 69555 body characters, 48 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260728-Arxiv-RandLoRA-Full-rank-parameter-efficient-fine-tuning-of-large-LOG.md`
- `.reports/BL-Arxiv-RandLoRA-Full-rank-parameter-efficient-fine-tuning-of-large-20260728/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260728-RandLoRA Full-rank/README.md`
- `.lake-data/DEP-E/DEP-E-20260728-RandLoRA Full-rank/randlora_full_rank_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` - BA-LoRA Bias - DEP-E; overlap: low-rank adaptation, parameter-efficient tuning, model fine-tuning.
2. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: foundation-model efficiency, compression, tuning.
3. `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` - Device Tuning MTL - DEP-E; overlap: parameter-efficient tuning, device adaptation, compute constraints.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
