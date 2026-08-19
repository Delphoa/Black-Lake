# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-7C79A486`
- Deployment item ID: `BLAD-2200-20260819-7C79A486-P05`
- Public-safe date: 2026-08-19
- Paper: *Prior-Guided DETR for Ultrasound Nodule Detection*
- Identifier: `arXiv:2601.02212`; DOI: `10.48550/arXiv.2601.02212`
- URL: https://arxiv.org/abs/2601.02212

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 717 on draw 1.

## Research Focus Eligibility

- One-time focus: No one-time topic focus was requested..
- Matched categories: unrestricted.
- Matched title/abstract terms or phrases: not applicable.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Prior-Guided-DETR-for-Ultrasound-Nodule` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 21,501,961 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 20; sampled text inspection: true.
- Full-paper HTML: 421,899 bytes, 83,218 body characters, 71 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Prior-Guided-DETR-for-Ultrasound-Nodule-LOG.md`
- `.reports/BL-Arxiv-Prior-Guided-DETR-for-Ultrasound-Nodule-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Prior-Guided DETR for/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Prior-Guided DETR for/prior_guided_detr_for_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260730-Self-supervised TransUNet/self_supervised_transunet_manuscript.md` - Self-supervised TransUNet - DEP-E; overlap: ultrasound, detection.
2. `.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md` - 2D-RC OTFS - DEP-E; overlap: detection.
3. `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md` - CausalTAD Trajectory - DEP-E; overlap: detection.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
