# Arxiv DEP Phase Log - Stable Diffusion Depth

## Public-Safe Run Summary

- Deposit date: 2026-07-18.
- Paper: *Stealing Stable Diffusion Prior for Robust Monocular Depth Estimation*.
- Identifier: arXiv:2403.05056v1; DOI `10.48550/arXiv.2403.05056`.
- Random draw: Uniform zero-based `Get-Random` index 45,232 from 75,776 PDF-parent paper units.
- Exclusions/reselections: 0/0.
- Initial source classification: `partial`.
- Final source classification: `complete`.
- Extraction cache: `miss` to `cached` through a local `missing-only` backfill.
- Dedup pointer: Added and finalized with `deposited` status and the primary commit reference.
- Source policy: Source documents, project assets, extracted text, caches, and integrity records remain local. Review-page renderings were removed after inspection. No source file or `.source/` directory is included in the public artifact set.

## Phase Metrics

Durations are elapsed wall-clock estimates rounded for public reporting. Phase expectations are trajectory guides, not hard truncation limits.

| Phase | Expected | Observed | Status | Evidence / Note |
|---|---:|---:|---|---|
| Contract, memory, extractor, and live-repository preflight | 8 min | 16.0 min | Complete | Required skill contracts, automation memory, extractor inventory, live Black Lake README, live Black-Lake-Data README, and repository state inspected |
| Candidate enumeration and dedup validation | 5 min | 5.2 min | Complete | 75,777 PDFs, 75,776 units, first draw accepted; substantive artifact/memory/companion/worktree markers absent |
| Source integrity classification and bounded repair | 12 min | 18.6 min | Complete | Existing PDF preserved; official HTML, metadata, and 30-entry source archive added; strict gate passed; zero partials |
| Extraction cache lookup and missing-only backfill | 3 min | 0.014 min | Complete | Initial miss; extraction command elapsed 0.826 seconds; PDF/HTML/source text present |
| Source, equation, table, figure, project, and repository review | 25 min | 24.1 min | Complete | Full paper and TeX reviewed; pages 7-14 visually inspected; official repository pinned and audited |
| Related DEP exploration and exact-three synthesis | 8 min | 5.4 min | Complete | UAV Visual Localization, VideoWeave Geometry, and Stereo Lane Detection manuscripts inspected |
| Public artifact drafting, publication index, and dedup preparation | 30 min | 27.1 min | Complete | Logs, Report-Mark, schema-complete manuscript, DEP README, publication-index row, and dedup entry prepared |
| Validation, staged allowlist, commit/push, notification, and final record | 15 min | 23.5 min | Complete | All schema/public-safety checks passed; seven allowlisted paths committed directly; remote and Slack links verified; dedup status finalized |

Whole-job guidance is 90-120 minutes. The rounded observed total was about 119.9 minutes, within the upper edge of the intended source-first trajectory. Estimate overruns in contract loading, source repair, and final submission did not truncate paper-body review.

## Extraction Cache

- Preflight fallback order: `pdftotext`, `fitz`, `pypdf`, `PyPDF2`, `pdfminer.six`, HTML, source package.
- Available PDF backend: `pypdf`.
- Initial lookup: Miss; no cache record for the versioned identifier.
- Mode: `missing-only`; network disabled because the repaired unit was locally complete before extraction.
- PDF extractor: `pypdf`, status `ok`, 48,076 text bytes.
- PDF fallback: `pdftotext` unavailable.
- HTML extractor: `html-regex`, status `ok`, 63,736 text bytes.
- Source extractor: `tarfile`, status `ok`, 95,602 text bytes.
- Final cache status: `cached`.
- Cache shortfall: No `pdftotext` backend; `pypdf` completed without blocking the review.

## Source Integrity and Repair

- Initial unit: Valid PDF plus brief metadata, but no full-paper HTML; classified `partial`.
- Transfer strategy: Public unauthenticated HTTPS, one active owner, one bounded attempt per artifact, 64 MB total ceiling, 32 MB partial ceiling, no blind restart.
- Existing PDF: 1,385,815 bytes; header and trailing EOF passed; matched the bounded-transfer PDF SHA-256 and was preserved.
- Official full-paper HTML: 326,876 bytes; 61,973 body characters; article and LaTeXML markers; 45 heading/section markers; six structure terms.
- Metadata HTML: 41,897 bytes; metadata-only.
- TeX/source: 4,220,563 bytes; 30 valid archive entries.
- Partial state: Zero partial files and zero partial bytes.
- Local archive records refreshed: README, attribution/provenance, preflight manifest, machine-readable summary, and verification report.
- Final verification: `complete`; research synthesis began only after this pass.

## Dedup Index Update

- Keys checked: arXiv ID/base ID, arXiv DOI, normalized title, slug, and public artifact paths.
- Scan basis: Black Lake public pointer/log/report/DEP records; automation memory; Black-Lake-Data substantive artifacts; active worktrees; public-safe 24-hour cutoff date 2026-07-17.
- Metadata-only inventory rows: Observed and explicitly not treated as deposits.
- Duplicate artifact matches: 0.
- Reselections: 0.
- Public pointer action: Added one unique entry with 5 artifact paths, 7 public source URLs, source-repair/cache notes, and `deposited` status.
- Commit/PR reference: [`fa1850d`](https://github.com/Delphoa/Black-Lake/commit/fa1850d45ca68db9f0148df188d157b95379ddf6).

## Expected vs Observed Trajectory

- Contract/preflight exceeded its estimate because all required skill/reference files and both live repository authorities were read before action.
- Source repair exceeded its estimate because the archive/download safety contracts, bounded-transfer preflight, byte/hash comparison, strict HTML validation, and local provenance records were completed before synthesis.
- Cache extraction substantially beat its estimate because the repaired local unit supplied PDF, official HTML, and a valid TeX archive to all three extractors.
- Full source review finished within estimate despite the earlier overruns. Table values were checked against TeX and visual renderings, and the teacher-mask contradiction was preserved rather than smoothed over.
- Artifact drafting remained within estimate and included the publication index and public pointer rather than postponing repository consistency work.
- Final validation/submission exceeded its phase estimate because the latest default branch was checked twice, the exact seven-path staged allowlist was inspected, public-safety validation was rerun, the remote push was verified, Slack was notified, and public records were finalized. The rounded whole-job total remained within the 90-120 minute guidance, and no remote conflict occurred.

## Submission and Notification

- Repository status: Direct default-branch submission succeeded.
- Primary artifact commit: [`fa1850d`](https://github.com/Delphoa/Black-Lake/commit/fa1850d45ca68db9f0148df188d157b95379ddf6).
- Slack status: Notification delivered to [`#black-lake-artifacts`](https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784362587226529).
- Source-upload gate: Passed. Source files were withheld locally; no source file, cache, extracted text, review rendering, or `.source/` directory was uploaded.

## Shortfalls and Follow-Up

- The official repository contains no executable code, dataset manifest, configs, checkpoints, or weights at the pinned revision, so no reproduction was possible.
- Equations 5-6 conflict with the surrounding teacher-reliability prose; the missing implementation prevents resolution.
- No geometry-preservation distribution, generated-image manifest, prompt/seed inventory, repeated-seed uncertainty, calibration, or independent domain evaluation was available.
- RobotCar night results are metric-mixed rather than a uniform student win; public artifacts preserve that qualification.
- No publisher version or publisher DOI was identified from inspected primary records.
- No paper model, generator component, dataset, or experiment was executed.
- PDF visual rendering emitted nonfatal font-substitution warnings, but inspected diagrams, equations, tables, and captions remained legible.
- Submission, remote verification, Slack notification, and final dedup status completed without a blocker.
