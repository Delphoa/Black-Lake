# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260723-FCF6DE3F`
- Deployment item ID: `BLAD-2200-20260723-FCF6DE3F-P06`
- Public-safe date: 2026-07-23
- Paper: *Unveiling the Lexical Sensitivity of LLMs: Combinatorial Optimization for Prompt Enhancement*
- Identifier: `arXiv:2405.20701`; DOI: `10.48550/arXiv.2405.20701`
- URL: https://arxiv.org/abs/2405.20701

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 22,626 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` records, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Unveiling-the-Lexical-Sensitivity-of` slug; the 24-hour marker cutoff was 2026-07-22.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,348,887 bytes with a valid `%PDF-` header and trailing `%%EOF`; page count: 27; sampled text inspection: true.
- Full-paper HTML: 699,015 bytes, 103,433 body characters, 83 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260723-Arxiv-Unveiling-the-Lexical-Sensitivity-of-LOG.md`
- `.reports/BL-Arxiv-Unveiling-the-Lexical-Sensitivity-of-20260723/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260723-Unveiling the Lexical Sen/README.md`
- `.lake-data/DEP-E/DEP-E-20260723-Unveiling the Lexical Sen/unveiling_the_lexical_sen_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-MA-VLM PNU Moderation/ma_vlm_pnu_moderation_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260723-ScaleEnv Scaling Environm/scaleenv_scaling_environm_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
