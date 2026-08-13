# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260812-9483C5E4`
- Deployment item ID: `BLAD-2200-20260812-9483C5E4-P03`
- Public-safe date: 2026-08-12
- Paper: *Open Set Relation Extraction via Unknown-Aware Training*
- Identifier: `arXiv:2306.04950`; DOI: `10.48550/arXiv.2306.04950`
- URL: https://arxiv.org/abs/2306.04950

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 59,824 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Open-Set-Relation-Extraction-via-Unknown-Aware` slug; the 24-hour marker cutoff was 2026-08-11.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,265,076 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 258,033 bytes, 62,925 body characters, 66 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260812-Arxiv-Open-Set-Relation-Extraction-via-Unknown-Aware-LOG.md`
- `.reports/BL-Arxiv-Open-Set-Relation-Extraction-via-Unknown-Aware-20260812/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260812-Open Set Relation/README.md`
- `.lake-data/DEP-E/DEP-E-20260812-Open Set Relation/open_set_relation_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260728-RAPL Relation-Aware/rapl_relation_aware_manuscript.md` - RAPL Relation-Aware - DEP-E; overlap: relation, extraction, open, set.
2. `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise/adversarial_label_noise_manuscript.md` - Adversarial Label Noise - DEP-E; overlap: training, set, extraction.
3. `.lake-data/DEP-E/DEP-E-20260723-ScaleEnv Scaling Environm/scaleenv_scaling_environm_manuscript.md` - ScaleEnv Scaling Environment Syn - DEP-E; overlap: training, set, extraction.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
