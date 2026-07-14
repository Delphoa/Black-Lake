# Arxiv DEP Log: iKalibr

## Public-Safe Run Summary

- Date marker: 2026-07-14.
- Actor/tool: Codex recurring Arxiv DEP workflow.
- Action: randomly select one eligible local arXiv paper, enforce the complete-source gate, review it source-first, and prepare a Black Lake DEP-E research deposit.
- Selected paper: *iKalibr: Unified Targetless Spatiotemporal Calibration for Resilient Integrated Inertial Systems*.
- Stable identifiers: arXiv:2407.11420v2; arXiv DOI 10.48550/arXiv.2407.11420; IEEE DOI 10.1109/TRO.2025.3532506.
- Outcome: completed; no blocker remained after local archive repair.

## Random Selection

- Enumeration command class: `rg --files -g "*.pdf"` against the local arXiv archive.
- Candidate paper unit: each unique PDF parent directory.
- PDF candidates: 75,774.
- Candidate paper units: 75,774.
- Random method: PowerShell `Get-Random` uniform index over eligible units after used-ID exclusion.
- Used arXiv IDs observed across the dedup sources: 446.
- Units excluded by used arXiv ID: 93.
- Eligible units: 75,681.
- Selected zero-based eligible index: 46,775.
- Selected arXiv ID: 2407.11420.
- Duplicate rejections and reselections: 0.

## Deduplication and Reselection Validation

- Scanned Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging` records on the live default branch.
- Scanned automation memory for earlier Black Lake Arxiv DEP runs.
- Scanned relevant Black-Lake-Data `.lake-data` and `.reports` records on its live default branch.
- Checked the selected paper by base arXiv ID, arXiv DOI, normalized title phrase, and `iKalibr` slug.
- Selected-paper matches in the dedup locations: 0.
- Public-safe 24-hour cutoff date: 2026-07-13.
- Same-paper recent-window markers: 0.
- Note: the ID index intentionally errs toward exclusion when a reviewed record exposes a canonical arXiv ID.

## Local Source Integrity Gate

- Initial classification: `partial` because a structurally valid PDF was present but full-paper HTML was missing.
- Repair action: preserved the valid PDF; collected official arXiv full-paper HTML, metadata HTML, and the source package; updated the local README, provenance record, machine-readable summary, verification report, and extraction cache.
- PDF verification: 14,684,227 bytes; `%PDF-` header present; trailing `%%EOF` present.
- Full-paper HTML verification: 3,206,014 bytes; 410,677 body characters after script/style/tag removal; document marker present; 151 heading/section markers; at least two paper-structure terms present.
- Metadata HTML: 44,268 bytes and classified as metadata-only, never as the paper document.
- Source package: 13,443,478 bytes with a gzip header.
- Remaining `.part` files: 0.
- Final classification: `complete`; local extraction succeeded for PDF, HTML, and source-package text.
- Source locality: every original source file and extraction cache remained in the private local archive.
- Public source policy: no PDF, HTML, TeX/source archive, cache, or extracted source text was copied into this repository.

## Generated Public Artifacts

- `.logs/20260714-Arxiv-iKalibr-LOG.md`
- `.reports/BL-Arxiv-iKalibr-20260714/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/README.md`
- `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md` publication ownership update.
- `.staging/arxiv-dep-dedup-index.json` public-safe dedup pointer update.

## Related DEP Entries

Exactly three related Black Lake entries were verified:

1. `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md` — a downstream autonomous-driving world model whose multi-camera/LiDAR geometry depends on coherent sensor frames.
2. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` — camera-motion representation learning that overlaps with continuous-time pose estimation and metric-frame validation.
3. `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` — embodied driving control that consumes camera, radar, and LiDAR observations and therefore inherits calibration uncertainty.

## Validation Notes

- Live Black Lake README and `.lake-data/README.md` were read before writing. Their current container rule places this entry under `.lake-data/DEP-E/` and requires the publications index update.
- Live Black-Lake-Data README was read before its records were used for deduplication.
- The manuscript uses the required schema version and exact required headings.
- The Report-Mark contains the required synthesis subsections with exactly three entries in each counted subsection.
- DEP short description `iKalibr Calibration` is 19 characters and within the 25-character limit.
- Source files were withheld locally; no `.source/` directory was created.

## Attribution Block

- Source URL: https://arxiv.org/abs/2407.11420
  - Applies to: selection identity, metadata, and source-gate record.
  - Notes: Canonical public arXiv record for the selected paper.
- Source URL: https://arxiv.org/html/2407.11420
  - Applies to: full-paper integrity and source-first review.
  - Notes: Official full-paper HTML used after local archive repair.
- Source URL: https://github.com/Unsigned-Long/iKalibr
  - Applies to: implementation-availability notes.
  - Notes: Official author-linked repository; code was inspected but not executed.
