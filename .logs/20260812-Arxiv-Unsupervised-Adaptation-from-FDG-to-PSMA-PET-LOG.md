# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260812-9483C5E4`
- Deployment item ID: `BLAD-2200-20260812-9483C5E4-P04`
- Public-safe date: 2026-08-12
- Paper: *Unsupervised Adaptation from FDG to PSMA PET/CT for 3D Lesion Detection under Label Shift*
- Identifier: `arXiv:2603.13666`; DOI: `10.48550/arXiv.2603.13666`
- URL: https://arxiv.org/abs/2603.13666

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 59,515 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Unsupervised-Adaptation-from-FDG-to-PSMA-PET` slug; the 24-hour marker cutoff was 2026-08-11.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,391,316 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 5; sampled text inspection: true.
- Full-paper HTML: 118,930 bytes, 27,571 body characters, 33 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260812-Arxiv-Unsupervised-Adaptation-from-FDG-to-PSMA-PET-LOG.md`
- `.reports/BL-Arxiv-Unsupervised-Adaptation-from-FDG-to-PSMA-PET-20260812/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260812-Unsupervised Adaptation/README.md`
- `.lake-data/DEP-E/DEP-E-20260812-Unsupervised Adaptation/unsupervised_adaptation_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260725-CLCI-Net Cross-Level/clci_net_cross_level_manuscript.md` - CLCI-Net Cross-Level - DEP-E; overlap: lesion, shift, detection, under.
2. `.lake-data/DEP-E/DEP-E-20260731-Generalizable CT-Free PET/generalizable_ct_free_pet_manuscript.md` - Generalizable CT-Free PET - DEP-E; overlap: pet, shift, detection, under.
3. `.lake-data/DEP-E/DEP-E-20260722-Few shot Multi label/few_shot_multi_label_manuscript.md` - Few shot Multi label Review - DEP-E; overlap: label, detection, shift, under.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
