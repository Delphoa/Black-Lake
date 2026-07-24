# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260724-CF53BCCB`
- Deployment item ID: `BLAD-2200-20260724-CF53BCCB-P02`
- Public-safe date: 2026-07-24
- Paper: *OmniSQL: Synthesizing High-quality Text-to-SQL Data at Scale*
- Identifier: `arXiv:2503.02240`; DOI: `10.48550/arXiv.2503.02240`
- URL: https://arxiv.org/abs/2503.02240

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 63,249 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `OmniSQL-Synthesizing-High-quality-Text-to-SQL` slug; the 24-hour marker cutoff was 2026-07-23.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 8,052,512 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 15; sampled text inspection: true.
- Full-paper HTML: 472,123 bytes, 111,721 body characters, 86 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260724-Arxiv-OmniSQL-Synthesizing-High-quality-Text-to-SQL-LOG.md`
- `.reports/BL-Arxiv-OmniSQL-Synthesizing-High-quality-Text-to-SQL-20260724/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260724-OmniSQL Synthesizing/README.md`
- `.lake-data/DEP-E/DEP-E-20260724-OmniSQL Synthesizing/omnisql_synthesizing_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: across, all, automatically, code, concerns.
2. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` - LA-Pose Latent Action - DEP-E; overlap: achieves, across, code, coverage, dataset.
3. `.lake-data/DEP-E/DEP-E-20260714-RLMF Uncertainty/rlmf_uncertainty_manuscript.md` - RLMF Uncertainty - DEP-E; overlap: across, all, automatically, available, code.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
