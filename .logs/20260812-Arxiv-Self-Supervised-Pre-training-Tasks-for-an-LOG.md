# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260812-9483C5E4`
- Deployment item ID: `BLAD-2200-20260812-9483C5E4-P10`
- Public-safe date: 2026-08-12
- Paper: *Self-Supervised Pre-training Tasks for an fMRI Time-series Transformer in Autism Detection*
- Identifier: `arXiv:2409.12304`; DOI: `10.48550/arXiv.2409.12304`
- URL: https://arxiv.org/abs/2409.12304

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 31,543 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Self-Supervised-Pre-training-Tasks-for-an` slug; the 24-hour marker cutoff was 2026-08-11.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,220,662 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 125,804 bytes, 30,362 body characters, 48 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260812-Arxiv-Self-Supervised-Pre-training-Tasks-for-an-LOG.md`
- `.reports/BL-Arxiv-Self-Supervised-Pre-training-Tasks-for-an-20260812/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260812-Self-Supervised/README.md`
- `.lake-data/DEP-E/DEP-E-20260812-Self-Supervised/self_supervised_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260802-MeDSLIP Medical/medslip_medical_manuscript.md` - MeDSLIP Medical - DEP-E; overlap: pre-training, detection.
2. `.lake-data/DEP-E/DEP-E-20260801-CrossNER Adapt/crossner_domain_adaptation_manuscript.md` - CrossNER - DEP-E; overlap: pre-training.
3. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` - LA-Pose Latent Action - DEP-E; overlap: self-supervised, transformer, tasks, detection.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
