# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260803-11C1283E`
- Deployment item ID: `BLAD-2200-20260803-11C1283E-P05`
- Public-safe date: 2026-08-03
- Paper: *Can Attention Enable MLPs To Catch Up With CNNs?*
- Identifier: `arXiv:2105.15078`; DOI: `10.48550/arXiv.2105.15078`
- URL: https://arxiv.org/abs/2105.15078

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 21,535 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Can-Attention-Enable-MLPs-To-Catch-Up` slug; the 24-hour marker cutoff was 2026-08-02.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 253,407 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 4; sampled text inspection: true.
- Full-paper HTML: 138,935 bytes, 20,017 body characters, 37 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260803-Arxiv-Can-Attention-Enable-MLPs-To-Catch-Up-LOG.md`
- `.reports/BL-Arxiv-Can-Attention-Enable-MLPs-To-Catch-Up-20260803/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260803-Can Attention Enable MLPs/README.md`
- `.lake-data/DEP-E/DEP-E-20260803-Can Attention Enable MLPs/can_attention_enable_mlps_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - AFIDAF Vision - DEP-E; overlap: mlps, attention.
2. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: catch, attention.
3. `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` - Device Tuning MTL - DEP-E; overlap: cnns, attention.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
