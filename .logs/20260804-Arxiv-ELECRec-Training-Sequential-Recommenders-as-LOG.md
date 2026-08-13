# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260804-92EFB161`
- Deployment item ID: `BLAD-2200-20260804-92EFB161-P08`
- Public-safe date: 2026-08-04
- Paper: *ELECRec: Training Sequential Recommenders as Discriminators*
- Identifier: `arXiv:2204.02011`; DOI: `10.48550/arXiv.2204.02011`
- URL: https://arxiv.org/abs/2204.02011

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 49,197 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `ELECRec-Training-Sequential-Recommenders-as` slug; the 24-hour marker cutoff was 2026-08-03.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,981,594 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 6; sampled text inspection: true.
- Full-paper HTML: 283,208 bytes, 34,980 body characters, 47 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260804-Arxiv-ELECRec-Training-Sequential-Recommenders-as-LOG.md`
- `.reports/BL-Arxiv-ELECRec-Training-Sequential-Recommenders-as-20260804/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260804-ELECRec Training/README.md`
- `.lake-data/DEP-E/DEP-E-20260804-ELECRec Training/elecrec_training_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-AMAD Anomaly/amad_anomaly_manuscript.md` - AMAD Anomaly Detection - DEP-E; overlap: discriminators, sequential, training.
2. `.lake-data/DEP-E/DEP-E-20260719-MiNet CTR Transfer/minet_ctr_manuscript.md` - Mixed-Interest CTR Transfer; overlap: recommenders, sequential, training.
3. `.lake-data/DEP-E/DEP-E-20260719-DUET Setwise CTR/duet_setwise_ctr_manuscript.md` - Dual Set-Wise CTR Pre-Ranking; overlap: recommenders, training.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
