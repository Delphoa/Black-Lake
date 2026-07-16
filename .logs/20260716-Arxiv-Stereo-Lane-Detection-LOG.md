# Arxiv DEP Job Log: Stereo Lane Detection

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:1808.09128v1, *Multiple Lane Detection Algorithm Based on Optimised Dense Disparity Map Estimation*
- Publisher DOI: 10.1109/IST.2018.8577122
- Selection: accepted on the first uniform draw
- Source integrity: initial `partial`, repaired to verified `complete`
- Source policy: PDF, full-paper HTML, metadata HTML, cache, and extracted text remain local; none are deposited
- Extraction cache: initial miss; final `cached`

## Random Selection

- Enumeration: `rg --files -g "*.pdf"`
- PDFs / unique parent units: 75,777 / 75,776
- Sampling: PowerShell `Get-Random` over the sorted unique unit list
- Zero-based index: 15,402
- Exclusions: 0
- Reselections: 0

## Dedup Validation

No matching arXiv ID, arXiv DOI, publisher DOI, normalized title, slug, Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, automation-memory entry, or 24-hour same-paper marker was found. The companion repository contained no substantive record for this paper.

## Source Integrity and Cache

- PDF: 5,980,379 bytes with `%PDF-` header and trailing `%%EOF`
- Initial full-paper HTML: missing; official arXiv HTML returned 404
- Repair: approved ar5iv full-paper fallback plus official arXiv metadata, each fetched once
- Full HTML: 292,496 bytes; 31,447 body characters; two document markers; 26 heading/section markers; five structure terms
- Metadata: 42,471 bytes; metadata only
- Source package: not collected; partial files: 0
- Cache: 0.379-second missing-only backfill via `pypdf` and `html-regex`
- Cache text: PDF 24,083 bytes; HTML 31,431 bytes; source absent

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - calibration and timing provenance upstream of stereo disparity and road geometry.
2. `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` - field-vision failure analysis and the difference between workstation and embedded performance.
3. `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` - downstream automated-driving control, mixed-traffic safety, and latency assurance boundaries.

## Output Paths

- `.logs/20260716-Arxiv-Stereo-Lane-Detection-LOG.md`
- `.logs/20260716-Arxiv-Stereo-Lane-Detection-PHASE-LOG.md`
- `.reports/BL-Arxiv-Stereo-Lane-Detection-20260716/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/README.md`
- `.lake-data/DEP-E/DEP-E-20260716-Stereo Lane Detection/stereo_lane_detection_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Does temporal disparity-range propagation retain its speed advantage without accumulating error across calibration drift, occlusion, road grade changes, dropped frames, and recovery events?
2. What precision, recall, false-lane, missed-lane, and latency-tail results emerge under a modern labeled protocol with fixed frame/instance denominators and diverse weather, lighting, markings, and camera rigs?
3. Can confidence and temporal-consistency diagnostics force a safe abstention before lane geometry is consumed by planning or control?

## Challenges

1. The claimed approximately 99% rate is derived from manually counted lanes in six KITTI sequences without a standard ground-truth protocol, confidence intervals, or a broad baseline suite.
2. A 37% disparity-stage speedup still yields 0.21 seconds per 1242-by-375 frame on the reported single-thread CPU, so the complete system is not real time.
3. Reusing the previous disparity-derived road model introduces temporal state whose failure and recovery behavior is not isolated by the reported aggregate counts.

## Known Shortfalls

- The method and prior baseline were not reproduced; no official code or pinned implementation was found.
- Exact sequence IDs, annotation procedure, frame count, lane-count denominator construction, and uncertainty are incomplete.
- Weather, night, worn markings, construction, intersections, calibration error, sensor faults, embedded latency, and safety integration remain unevaluated.

## Submission Record

- Primary artifact commit: pending
- Slack notification: pending
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source artifacts
- Submission status: pending
