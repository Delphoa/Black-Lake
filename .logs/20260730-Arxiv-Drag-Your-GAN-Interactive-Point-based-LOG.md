# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260730-2FDDC232`
- Deployment item ID: `BLAD-2200-20260730-2FDDC232-P07`
- Public-safe date: 2026-07-30
- Paper: *Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold*
- Identifier: `arXiv:2305.10973`; DOI: `10.1145/3588432.3591500`
- URL: https://arxiv.org/abs/2305.10973

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 15,176 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Drag-Your-GAN-Interactive-Point-based` slug; the 24-hour marker cutoff was 2026-07-29.
- Duplicate exclusions: 1; source-gate exclusions: 0; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 12,073,894 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 323,511 bytes, 66,133 body characters, 72 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260730-Arxiv-Drag-Your-GAN-Interactive-Point-based-LOG.md`
- `.reports/BL-Arxiv-Drag-Your-GAN-Interactive-Point-based-20260730/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260730-Drag Your GAN Interactive/README.md`
- `.lake-data/DEP-E/DEP-E-20260730-Drag Your GAN Interactive/drag_your_gan_interactive_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` - Spiking Pose Tracking - DEP-E; overlap: pose, human, tracking.
2. `.lake-data/DEP-E/DEP-E-20260721-Controlling Latent/controlling_latent_manuscript.md` - Controlling Latent Review - DEP-E; overlap: controlling, image, generative.
3. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` - RRT-CBF Motion - DEP-E; overlap: tracking, motion, control.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
