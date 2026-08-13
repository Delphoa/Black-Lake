# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260805-6C10E207`
- Deployment item ID: `BLAD-2200-20260805-6C10E207-P09`
- Public-safe date: 2026-08-05
- Paper: *FiberStars: Visual Comparison of Diffusion Tractography Data between Multiple Subjects*
- Identifier: `arXiv:2005.08090`; DOI: `10.1109/PacificVis52677.2021.00023`
- URL: https://arxiv.org/abs/2005.08090

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 43,486 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `FiberStars-Visual-Comparison-of-Diffusion` slug; the 24-hour marker cutoff was 2026-08-04.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,734,540 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 232,961 bytes, 72,365 body characters, 82 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260805-Arxiv-FiberStars-Visual-Comparison-of-Diffusion-LOG.md`
- `.reports/BL-Arxiv-FiberStars-Visual-Comparison-of-Diffusion-20260805/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260805-FiberStars Visual/README.md`
- `.lake-data/DEP-E/DEP-E-20260805-FiberStars Visual/fiberstars_visual_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260805-Deep Learning for/deep_learning_for_manuscript.md` - Deep Learning for - DEP-E; overlap: avatars, topological, persistence, manifold, avatar.
2. `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` - Spiking Pose Tracking - DEP-E; overlap: avatars, algebraic, avatar, pose, motion.
3. `.lake-data/DEP-E/DEP-E-20260803-Vid2Curve Reconstruction/vid2curve_reconstruction_manuscript.md` - Vid2Curve Reconstruction - DEP-E; overlap: topological, geometric, topology, pose, motion.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
