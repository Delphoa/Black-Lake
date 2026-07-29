# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260728-EB036F17`
- Deployment item ID: `BLAD-2200-20260728-EB036F17-P07`
- Public-safe date: 2026-07-28
- Paper: *HeightFormer: Learning Height Prediction in Voxel Features for Roadside Vision Centric 3D Object Detection via Transformer*
- Identifier: `arXiv:2503.10777`; DOI: `10.48550/arXiv.2503.10777`
- URL: https://arxiv.org/abs/2503.10777

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75825 PDFs and 75822 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 4079.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant deposited identifiers, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `HeightFormer-Learning-Height-Prediction-in-Voxel-Features-for-Roadside` slug; the 24-hour marker cutoff was 2026-07-27.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 17260126 bytes with valid `%PDF-` header and trailing `%%EOF`; page markers: 13.
- Full-paper HTML: 466426 bytes, 37018 body characters, 14 headings, and 5 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260728-Arxiv-HeightFormer-Learning-Height-Prediction-in-Voxel-Features-for-Roadside-LOG.md`
- `.reports/BL-Arxiv-HeightFormer-Learning-Height-Prediction-in-Voxel-Features-for-Roadside-20260728/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260728-HeightFormer Learning/README.md`
- `.lake-data/DEP-E/DEP-E-20260728-HeightFormer Learning/heightformer_learning_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-UAV Visual Localization/uav_visual_localization_manuscript.md` - UAV Visual Localization - DEP-E; overlap: autonomous, details, detection.
2. `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md` - OE-BevSeg Perception - DEP-E; overlap: applied, attention, distribution.
3. `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md` - Stereo Lane Detection - DEP-E; overlap: detection, distribution, local.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
