# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P08`
- Public-safe date: 2026-08-18
- Paper: *The Role of Model Confidence on Bias Effects in Measured Uncertainties for Vision-Language Models*
- Identifier: `arXiv:2506.16724`; DOI: `10.48550/arXiv.2506.16724`
- URL: https://arxiv.org/abs/2506.16724

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 20,934 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `The-Role-of-Model-Confidence-on-Bias` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 621,684 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 17; sampled text inspection: true.
- Full-paper HTML: 408,769 bytes, 73,381 body characters, 113 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-The-Role-of-Model-Confidence-on-Bias-LOG.md`
- `.reports/BL-Arxiv-The-Role-of-Model-Confidence-on-Bias-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-The Role of Model/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-The Role of Model/the_role_of_model_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - OViP Preference - DEP-E; overlap: vision-language, bias, role.
2. `.lake-data/DEP-E/DEP-E-20260818-ChartMuseum Testing/chartmuseum_testing_manuscript.md` - ChartMuseum Testing - DEP-E; overlap: vision-language, measured, role.
3. `.lake-data/DEP-E/DEP-E-20260814-Bias Behind the Wheel/bias_behind_the_wheel_manuscript.md` - Bias Behind the Wheel - DEP-E; overlap: bias, measured, role.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
