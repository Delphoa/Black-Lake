# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-50A35360`
- Deployment item ID: `BLAD-2200-20260818-50A35360-P06`
- Public-safe date: 2026-08-18
- Paper: *Learning Latent Transmission and Glare Maps for Lens Veiling Glare Removal*
- Identifier: `arXiv:2511.17353`; DOI: `10.48550/arXiv.2511.17353`
- URL: https://arxiv.org/abs/2511.17353

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 32,925 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Learning-Latent-Transmission-and-Glare-Maps-for` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 30,981,085 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 19; sampled text inspection: true.
- Full-paper HTML: 352,304 bytes, 79,415 body characters, 74 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-Learning-Latent-Transmission-and-Glare-Maps-for-LOG.md`
- `.reports/BL-Arxiv-Learning-Latent-Transmission-and-Glare-Maps-for-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-Learning Latent/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-Learning Latent/learning_latent_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Controlling Latent/controlling_latent_manuscript.md` - Controlling Latent Review - DEP-E; overlap: removal, latent, lens.
2. `.lake-data/DEP-E/DEP-E-20260725-Removal then Selection A/removal_then_selection_a_manuscript.md` - Removal then Selection A - DEP-E; overlap: removal.
3. `.lake-data/DEP-E/DEP-E-20260814-Privacy-Preserving/privacy_preserving_manuscript.md` - Privacy-Preserving - DEP-E; overlap: removal.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
