# Arxiv DEP Job Log: UAV Visual Localization

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2506.09748v1, *Hierarchical Image Matching for UAV Absolute Visual Localization via Semantic and Structural Constraints*
- Selection: accepted on the first uniform draw
- Source integrity: initial `partial`, repaired to verified `complete`
- Source policy: PDF, full-paper HTML, metadata HTML, cache, and extracted text remain local; none are deposited
- Extraction cache: initial miss; final `cached`

## Random Selection

- Enumeration: `rg --files -g "*.pdf"`
- PDFs / unique parent units: 75,777 / 75,776
- Sampling: PowerShell `Get-Random` over the sorted unique unit list
- Zero-based index: 37,833
- Exclusions: 0
- Reselections: 0

## Dedup Validation

No matching arXiv ID, DOI, normalized title, slug, Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, automation-memory entry, or 24-hour same-paper marker was found. Companion-repository search results were unrelated metadata or topical matches and did not represent a prior deposit of this paper.

## Source Integrity and Cache

- PDF: 1,585,169 bytes with `%PDF-` header and trailing `%%EOF`
- Initial full-paper HTML: missing
- Repair: official arXiv full-paper HTML and metadata fetched once; no fallback was required
- Full HTML: 343,535 bytes; 53,166 body characters; one document marker; 34 heading/section markers; four structure terms
- Metadata: 44,128 bytes; metadata only
- Source package: not collected; partial files: 0
- Cache: 0.472-second missing-only backfill via `pypdf` and `html-regex`
- Cache text: PDF 43,965 bytes; HTML 61,869 bytes; source absent

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - calibration provenance and observability gates for reliable robotic localization pipelines.
2. `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` - explicit spatial priors, geometry constraints, and failure modes in aerial/remote-sensing imagery.
3. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - hierarchical local/global visual feature design and the need to verify efficiency claims on target hardware.

## Output Paths

- `.logs/20260716-Arxiv-UAV-Visual-Localization-LOG.md`
- `.logs/20260716-Arxiv-UAV-Visual-Localization-PHASE-LOG.md`
- `.reports/BL-Arxiv-UAV-Visual-Localization-20260716/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260716-UAV Visual Localization/README.md`
- `.lake-data/DEP-E/DEP-E-20260716-UAV Visual Localization/uav_visual_localization_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. How do success, drift, and fixed-denominator localization errors change across unseen regions, seasons, altitudes, cameras, and satellite-map ages?
2. What accuracy, latency, memory, and energy trade-offs arise when retrieval, DINOv2/SASCM coarse matching, fine matching, and RANSAC are measured separately on flight hardware?
3. Can uncertainty and geometric consistency gates produce calibrated abstention before an erroneous absolute position is consumed by navigation?

## Challenges

1. Mean localization error excludes segments above the 50-meter drift threshold, so the headline error can improve while catastrophic failures remain outside its denominator.
2. The new CS-UAV dataset is described as public, but the inspected paper contains only a literal `[link]` placeholder and no usable release locator.
3. The paper reports no official code, complete runtime profile, multi-seed uncertainty, or evaluation outside Chinese data-collection regions.

## Known Shortfalls

- The method was not reproduced; trained weights, exact retrieval implementation, and official code were not identified.
- The CS-UAV release could not be verified, and the AerialVL combined baselines were copied from prior work because their code was unavailable.
- Deployment claims require fixed-denominator error distributions, map-age stress tests, uncertainty calibration, target-device profiling, and safety review.

## Submission Record

- Primary artifact commit: https://github.com/Delphoa/Black-Lake/commit/4e5061c769397d876e68208e2ec1398d0e5495d5
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784212680379149
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source artifacts
- Submission status: direct default-branch push succeeded; Slack notice delivered
