# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P35`
- Public-safe date: 2026-08-19
- Paper: *Approximated Doubly Robust Search Relevance Estimation*
- Identifier: `arXiv:2208.07671`; DOI: `10.1145/3511808.3557145`
- URL: https://arxiv.org/abs/2208.07671

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 34,902 on draw 8.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: search.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Approximated-Doubly-Robust-Search-Relevance` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 7; source-gate exclusions: 0; reselections: 7.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 577,283 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 373,847 bytes, 74,629 body characters, 80 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Approximated-Doubly-Robust-Search-Relevance-LOG.md`
- `.reports/BL-Arxiv-Approximated-Doubly-Robust-Search-Relevance-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Approximated Doubly/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Approximated Doubly/approximated_doubly_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md` - Stable Diffusion Depth - DEP-E; overlap: estimation, robust, relevance.
2. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` - LA-Pose Latent Action - DEP-E; overlap: estimation, robust, search, relevance.
3. `.lake-data/DEP-E/DEP-E-20260803-Vid2Curve Reconstruction/vid2curve_reconstruction_manuscript.md` - Vid2Curve Reconstruction - DEP-E; overlap: estimation, robust, search, relevance.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
