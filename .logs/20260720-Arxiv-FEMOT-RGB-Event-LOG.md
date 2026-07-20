# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260720-8636EDC7`
- Deployment item ID: `BLAD-2200-20260720-8636EDC7-P04`
- Public-safe run date: 2026-07-20
- Selected paper: *FEMOT: Multi-Object Tracking using Frame and Event Cameras*
- Stable identifier: `arXiv:2606.14094v1`
- Canonical URL: https://arxiv.org/abs/2606.14094

## Random Selection

- Method: `rg --files -g "*.pdf"`, unique parent units, uniform PowerShell `Get-Random` index.
- PDF candidates: 75,779; candidate paper units: 75,776; selected one-based index: 48,183.
- The first draw succeeded without a machine-, user-, path-, timezone-, or timestamp-derived seed.

## Deduplication and Reselection

- Scanned Black Lake logs, reports, DEP-E artifacts and indexes; automation memory; relevant Black-Lake-Data records; and the current-job selected set.
- Keys: arXiv ID, DOI, normalized title, `FEMOT-RGB-Event` slug, and markers on or after the public-safe cutoff date 2026-07-19.
- Duplicate exclusions: 0; reselections: 0.

## Source Integrity

- Initial state: partial; valid PDF present and full-paper HTML absent.
- Repair: official arXiv full-paper and metadata HTML retrieved in one bounded pass.
- PDF: 5,261,316 bytes; `%PDF-` and trailing `%%EOF` passed.
- Full-paper HTML: 267,467 bytes; 80,377 body characters; 2 document markers; 41 headings; 73 paper-structure terms.
- Final state: verified complete. Source files and verification records remain local.

## Public Outputs

- `.logs/20260720-Arxiv-FEMOT-RGB-Event-LOG.md`
- `.reports/BL-Arxiv-FEMOT-RGB-Event-20260720/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260720-FEMOT Tracking/README.md`
- `.lake-data/DEP-E/DEP-E-20260720-FEMOT Tracking/femot_tracking_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Submission Gate

Only the six generated Markdown/JSON paths above are eligible for staging. No PDF, HTML, dataset, image, event stream, archive, cache, extracted source text, or `.source/` content may be uploaded.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md`

Source documents were withheld locally; no source files were uploaded.
