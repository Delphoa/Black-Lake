# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260802-0D11B2FA`
- Deployment item ID: `BLAD-2200-20260802-0D11B2FA-P05`
- Public-safe date: 2026-08-02
- Paper: *N-Grammer: Augmenting Transformers with latent n-grams*
- Identifier: `arXiv:2207.06366`; DOI: `10.48550/arXiv.2207.06366`
- URL: https://arxiv.org/abs/2207.06366

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 36,955 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `N-Grammer-Augmenting-Transformers-with-latent-n` slug; the 24-hour marker cutoff was 2026-08-01.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 404,890 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 227,623 bytes, 40,515 body characters, 49 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260802-Arxiv-N-Grammer-Augmenting-Transformers-with-latent-n-LOG.md`
- `.reports/BL-Arxiv-N-Grammer-Augmenting-Transformers-with-latent-n-20260802/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260802-N-Grammer Augmenting/README.md`
- `.lake-data/DEP-E/DEP-E-20260802-N-Grammer Augmenting/n_grammer_augmenting_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` - VLM Probing - DEP-E; overlap: transformers, latent.
2. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: transformers, latent.
3. `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` - Device Tuning MTL - DEP-E; overlap: transformers, latent.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
