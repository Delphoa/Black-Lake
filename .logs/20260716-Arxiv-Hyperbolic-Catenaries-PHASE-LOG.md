# Arxiv DEP Phase Log: Hyperbolic Catenaries

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2211.15297v2, *Catenaries and minimal surfaces of revolution in hyperbolic space*
- Selection: first uniform draw, zero-based index 43,368 of 75,776 paper units
- Dedup: no prior ID, DOI, normalized-title, slug, artifact, memory, or recent-window marker; one metadata-only author-inventory row did not exclude the paper
- Source integrity: initial `partial`; repaired to verified `complete`
- Source files: withheld locally; none uploaded or copied into the repository
- Cache: initial miss; final `cached`
- Dedup index: validated deposited pointer records the primary artifact commit

## Phase Metrics

Elapsed values are rounded public-safe durations. Expected durations guide trajectory review and are not hard stop limits.

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Authority, memory, and skill contracts | 6 min | about 5 min | Complete | Live Black Lake, filing, and Black-Lake-Data READMEs read; required source, manuscript, archive, download-safety, DEP, and Slack contracts loaded |
| Candidate enumeration and random draw | 3 min | 4.8 s | Complete | 75,777 PDFs collapsed to 75,776 unique parent units; index 43,368 |
| Detailed dedup and recent-marker validation | 5 min | about 1.4 min | Complete | Public index, repository artifacts, memory, Black-Lake-Data, and active worktrees checked |
| Source integrity classification | 3 min | under 1 min | Complete | Initial `partial`: valid PDF, missing full-paper HTML |
| Download preflight | 5 min | 3.1 s | Complete | Direct-HTTP content lengths discovered; 2.31 MB expected transfer against more than 1 TB free; one official request plus one HTML fallback allowed |
| Bounded archive repair transfer | 10 min | 2.1 s | Complete | Official arXiv HTML, metadata, and source archive succeeded on first attempts; zero incomplete files |
| Repair integration and complete-source verification | 5 min | about 2.6 min | Complete | README, attribution, machine summary, and verification report updated; all integrity thresholds passed |
| Extractor preflight and missing-only cache | 5 min | 1.3 s | Complete | Preflight 0.6 s; extraction 0.747 s; initial miss became `cached` |
| Primary-paper and publisher-version review | 25 min | about 12 min | Complete | Full arXiv v2 PDF/HTML/TeX plus open publisher HTML, figures, theorem wording, DOI, and version differences inspected |
| Related DEP exploration and exact-three synthesis | 10 min | about 4 min | Complete | Flag Hardy Operators, iKalibr Calibration, and CoreMem Geometry selected |
| Artifact generation | 20 min | about 8 min | Complete | Job log, phase log, Report-Mark, README, manuscript, publication index, and dedup pointer |
| Validation and source-upload gate | 10 min | about 4 min | Complete | Schema, exact-count, code-parse, JSON, public-safety, exact-seven allowlist, and zero-source checks passed |
| Repository submission and Slack notice | 10 min | about 2 min | Complete | Direct default-branch push succeeded; Slack notice delivered; record-only follow-up prepared |

## Extraction Cache

| Field | Value |
|---|---|
| Initial lookup | Miss |
| Mode | `missing-only` |
| Network during extraction | None; the repaired local bundle was used |
| Final status | `cached` |
| PDF extractor | `pypdf` because `pdftotext` was unavailable |
| HTML extractor | `html-regex` |
| Source extractor | `tarfile` |
| Fallback status | Successful PDF fallback to `pypdf` |
| PDF text | Present, 43,846 bytes |
| HTML text | Present, 193,203 bytes |
| Source text | Present, 78,385 bytes |

## Source Integrity Repair

| Check | Observed | Result |
|---|---:|---|
| Existing PDF | 277,685 bytes; `%PDF-`; trailing `%%EOF` | Pass; original preserved |
| Full-paper HTML | 2,239,423 bytes; 221,596 body characters | Pass |
| Document marker | Present | Pass |
| Heading/section markers | 44 | Pass |
| Paper-structure terms | 4 | Pass |
| Metadata HTML | 41,096 bytes | Present; metadata only |
| TeX/source package | 33,851 bytes; archive listing succeeded | Present locally |
| Remaining partial files | 0 | Pass |
| Final source classification | `complete` | Review gate opened |

## Dedup Index Update

- Initial selected-paper artifact matches: 0
- Exclusions: 0
- Reselections: 0
- New pointer: arXiv:2211.15297v2; journal DOI `10.1017/prm.2024.56`; slug `Hyperbolic-Catenaries`
- Artifact paths: job log, phase log, Report-Mark, DEP-E directory/manuscript, and publication index owner
- Source URLs: arXiv abstract, PDF, HTML, e-print, arXiv DOI, and journal DOI
- Commit reference: https://github.com/Delphoa/Black-Lake/commit/8f2019df187cb84678562a03bbb8899ea069781e
- Status: deposited pointer validated with primary commit attribution

## Expected vs Observed Trajectory

The first draw passed dedup but not the source-integrity gate. The workflow correctly paused paper review, performed a small bounded repair, validated complete PDF and full-paper HTML independently, and only then built the cache and began synthesis. The cache miss did not create a meaningful delay because all three local extractors succeeded.

Review exceeded a simple preprint-only path because the peer-reviewed publisher version materially improves the paper: it states the main equivalence explicitly, corrects the hyperbolic curvature scaling, and adds numerical examples. That extra cross-version inspection was kept within the whole-job guidance and exposed both improvements and a surviving equation typo.

## Shortfalls and Follow-Up

- No formal proof checker or independent mathematical referee pass was performed.
- The publisher's numerical examples lack an inspected code or initial-condition manifest and were not reproduced.
- The hyperbolic and parabolic families lack an identified intrinsic characterization or obvious first integral.
- Boundary-value existence, uniqueness, stability, embeddedness, and global-minimizer questions remain open in this review.
- Repository submission and Slack delivery completed; the record-only follow-up preserves their immutable links.
