# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260722-A5461BD0`
- Deployment item ID: `BLAD-2200-20260722-A5461BD0-P01`
- Public-safe date: 2026-07-22
- Paper: *Few-shot Learning for Multi-label Intent Detection*
- Identifier: `arXiv:2010.05256`; DOI: `10.48550/arXiv.2010.05256`
- URL: https://arxiv.org/abs/2010.05256

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 60,610 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Few-shot-Multi-label` slug; the 24-hour marker cutoff was 2026-07-21.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded archive repair.
- PDF: 504,205 bytes with a valid `%PDF-` header and trailing `%%EOF`.
- Full-paper HTML: 598,313 bytes, 60,123 body characters, 2 document markers, 64 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260722-Arxiv-Few-shot-Multi-label-LOG.md`
- `.reports/BL-Arxiv-Few-shot-Multi-label-20260722/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260722-Few shot Multi label/README.md`
- `.lake-data/DEP-E/DEP-E-20260722-Few shot Multi label/few_shot_multi_label_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260719-MA-VLM PNU Moderation/ma_vlm_pnu_moderation_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
