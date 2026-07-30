# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260730-2FDDC232`
- Deployment item ID: `BLAD-2200-20260730-2FDDC232-P03`
- Public-safe date: 2026-07-30
- Paper: *TopoDiffuser: A Diffusion-Based Multimodal Trajectory Prediction Model with Topometric Maps*
- Identifier: `arXiv:2508.00303`; DOI: `10.48550/arXiv.2508.00303`
- URL: https://arxiv.org/abs/2508.00303

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 60,681 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `TopoDiffuser-A-Diffusion-Based-Multimodal` slug; the 24-hour marker cutoff was 2026-07-29.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 825,167 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 6; sampled text inspection: true.
- Full-paper HTML: 120,153 bytes, 39,705 body characters, 61 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260730-Arxiv-TopoDiffuser-A-Diffusion-Based-Multimodal-LOG.md`
- `.reports/BL-Arxiv-TopoDiffuser-A-Diffusion-Based-Multimodal-20260730/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260730-TopoDiffuser A/README.md`
- `.lake-data/DEP-E/DEP-E-20260730-TopoDiffuser A/topodiffuser_a_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` - HERMES World Model - DEP-E; overlap: future, unified, generation.
2. `.lake-data/DEP-E/DEP-E-20260728-MI-Motion Review/mi_motion_manuscript.md` - MI-Motion - DEP-E; overlap: motion, prediction, benchmark.
3. `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md` - OE-BevSeg Perception - DEP-E; overlap: lidar, bird, s-eye-view.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
