# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260812-9483C5E4`
- Deployment item ID: `BLAD-2200-20260812-9483C5E4-P07`
- Public-safe date: 2026-08-12
- Paper: *RSMLP: A light Sampled MLP Structure for Incomplete Utterance Rewrite*
- Identifier: `arXiv:2502.12587`; DOI: `10.48550/arXiv.2502.12587`
- URL: https://arxiv.org/abs/2502.12587

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 21,857 on draw 3.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `RSMLP-A-light-Sampled-MLP-Structure-for` slug; the 24-hour marker cutoff was 2026-08-11.
- Duplicate exclusions: 0; source-gate exclusions: 2; reselections: 2.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 389,347 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 5; sampled text inspection: true.
- Full-paper HTML: 128,182 bytes, 27,299 body characters, 38 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260812-Arxiv-RSMLP-A-light-Sampled-MLP-Structure-for-LOG.md`
- `.reports/BL-Arxiv-RSMLP-A-light-Sampled-MLP-Structure-for-20260812/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260812-RSMLP A light Sampled MLP/README.md`
- `.lake-data/DEP-E/DEP-E-20260812-RSMLP A light Sampled MLP/rsmlp_a_light_sampled_mlp_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260805-Light the Night A/light_the_night_a_manuscript.md` - Light the Night A - DEP-E; overlap: light, sampled, structure.
2. `.lake-data/DEP-E/DEP-E-20260812-Matching-Based Selection/matching_based_selection_manuscript.md` - Matching-Based Selection - DEP-E; overlap: incomplete, sampled, structure.
3. `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` - CorrKD Missing Modal - DEP-E; overlap: incomplete, structure.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
