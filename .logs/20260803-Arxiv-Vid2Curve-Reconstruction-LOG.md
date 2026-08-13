# Black Lake Arxiv DEP Log - Vid2Curve Reconstruction

- Date: 2026-08-03
- Actor: Codex
- Action: source-first random arXiv review and DEP-E deposition
- Outcome: eligible paper selected, local source unit repaired and verified complete, public-safe artifacts generated
- Blockers: none

## Random Selection

- Method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent paper units, arXiv identifier resolution, cross-repository used-ID exclusion, then a uniform PowerShell `Get-Random` index over the eligible array.
- PDF candidates: 75,960.
- Unique PDF-parent units: 75,957.
- Used arXiv base IDs indexed: 1,950.
- Units excluded by used arXiv ID: 545.
- Identifier-incomplete units withheld from the draw: 185.
- Eligible units: 75,227.
- Selected zero-based eligible index: 7,979.
- Selected paper: *Vid2Curve: Simultaneous Camera Motion Estimation and Thin Structure Reconstruction from an RGB Video*.
- Selected identifier: arXiv:2005.03372v3; arXiv DOI 10.48550/arXiv.2005.03372; ACM DOI 10.1145/3386569.3392476.
- Duplicate rejections/reselections after the accepted draw: 0.
- Process note: an earlier in-memory enumeration was terminated before it produced a candidate because its parent-grouping implementation was inefficient. It created no selection record and was replaced by a single-pass unit index before the accepted draw.

## Deduplication and Recency Validation

- Scanned live `Delphoa/Black-Lake` `.logs`, `.reports`, `.lake-data`, and `.staging` content; automation memory; and live `Delphoa-Labs/Black-Lake-Data` `.lake-data`, `.reports`, and `.staging` content.
- Checked arXiv ID, arXiv DOI, ACM DOI, canonical and normalized title, and planned slug.
- Exact same-paper matches: none.
- Public-safe 24-hour cutoff date: 2026-08-02.
- Same-paper recent markers before this run: none.
- Excluded count before the draw: 545 used-ID units plus 185 identifier-incomplete units.

## Local Source Integrity

- Initial classification: partial; a valid full PDF existed, but verified full-paper HTML was absent.
- Repair: preserved the byte-identical PDF and used one bounded attempt per artifact. The approved ar5iv full-paper fallback was collected together with arXiv metadata HTML and the TeX/source package.
- PDF verification: 7,414,944 bytes, `%PDF-` header, trailing `%%EOF`, 12 unencrypted pages.
- Full-paper HTML verification: 513,959 bytes, 70,103 stripped body characters, multiple document markers, 34 heading markers, and five paper-structure terms.
- Source package verification: 8,538,727 bytes with 124 readable entries.
- Partials: 0.
- Archive records updated locally: paper README, attribution/provenance record, machine-readable download summary, acquisition receipt, and verification report.
- Source locality: all PDF, HTML, metadata, source-package, code, render, receipt, and verification files were withheld locally. No source file was copied into the repository and no public `.source/` directory was created.

## Review Boundary

- Inspected the complete PDF, all 12 rendered pages, full-paper HTML, TeX/source package, arXiv metadata, ACM DOI record, author project page, and official implementation at commit `47c379dec5cca2e2de123a392e0b1f93ceb1048a`.
- The official implementation was inspected but not built or executed. It is a C++14/CMake reference implementation with OpenCV, Boost, Ceres, OpenMP, glog, Eigen, optional Pangolin, two bundled examples, GPL-3.0 licensing, and no active test suite found.
- Paper results are treated as author-reported. No camera trajectory, reconstruction table, ablation, runtime, or baseline result was independently reproduced.
- The review preserves the clean-background, known-intrinsics, circular-cross-section, initialization, and compute constraints stated by the paper or implementation.

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260729-Correspondence Insert/apap_correspondence_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`
3. `.lake-data/DEP-A/DEP-A-20260717-PaceVGGT Frame Pruning/2605.08371-whitepaper-review.md`

## Public Outputs

- `.logs/20260803-Arxiv-Vid2Curve-Reconstruction-LOG.md`
- `.reports/BL-Arxiv-Vid2Curve-Reconstruction-20260803/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260803-Vid2Curve Reconstruction/README.md`
- `.lake-data/DEP-E/DEP-E-20260803-Vid2Curve Reconstruction/vid2curve_reconstruction_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

Submission is restricted to the generated Markdown artifacts and the required publication-index update.
