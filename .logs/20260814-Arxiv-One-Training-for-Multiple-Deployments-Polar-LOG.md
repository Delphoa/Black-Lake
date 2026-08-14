# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260814-24737ACA`
- Deployment item ID: `BLAD-2200-20260814-24737ACA-P05`
- Public-safe date: 2026-08-14
- Paper: *One Training for Multiple Deployments: Polar-based Adaptive BEV Perception for Autonomous Driving*
- Identifier: `arXiv:2304.00525`; DOI: `10.48550/arXiv.2304.00525`
- URL: https://arxiv.org/abs/2304.00525

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 15,866 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `One-Training-for-Multiple-Deployments-Polar` slug; the 24-hour marker cutoff was 2026-08-13.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 5,533,478 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 8; sampled text inspection: true.
- Full-paper HTML: 170,066 bytes, 41,942 body characters, 42 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260814-Arxiv-One-Training-for-Multiple-Deployments-Polar-LOG.md`
- `.reports/BL-Arxiv-One-Training-for-Multiple-Deployments-Polar-20260814/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260814-One Training for Multiple/README.md`
- `.lake-data/DEP-E/DEP-E-20260814-One Training for Multiple/one_training_for_multiple_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260803-ADReFT Adaptive Decision/adreft_adaptive_decision_manuscript.md` - ADReFT Adaptive Decision - DEP-E; overlap: driving, adaptive, autonomous, training, one.
2. `.lake-data/DEP-E/DEP-E-20260805-Light the Night A/light_the_night_a_manuscript.md` - Light the Night A - DEP-E; overlap: driving, autonomous, perception, one.
3. `.lake-data/DEP-E/DEP-E-20260814-Bias Behind the Wheel/bias_behind_the_wheel_manuscript.md` - Bias Behind the Wheel - DEP-E; overlap: driving, autonomous, adaptive, one.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
