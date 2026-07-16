# Arxiv DEP Phase Log: Stereo Lane Detection

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:1808.09128v1
- Selection: first draw, index 15,402 of 75,776 units
- Dedup: no prior substantive deposit
- Source: `partial` repaired to verified `complete` with approved ar5iv fallback
- Cache: miss to `cached`
- Source files: withheld locally; none uploaded
- Dedup index: validated deposited pointer records the primary artifact commit

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Candidate enumeration and draw | 3 min | about 4 s | Complete | 75,777 PDFs; 75,776 units; index 15,402 |
| Dedup validation | 5 min | about 3 min | Complete | IDs, both DOIs, title, artifacts, memory, companion repository, and recent markers checked |
| Source classification | 3 min | under 1 min | Complete | PDF valid; full HTML missing |
| Download preflight and fallback | 7 min | about 2 min | Complete | Existing PDF preserved; official HTML 404; bounded ar5iv fallback authorized |
| Archive repair | 10 min | about 2 min | Complete | ar5iv full paper and official metadata passed on first successful requests |
| Integrity records and verification | 5 min | about 4 min | Complete | README, attribution, CSV summary, and JSON report updated; gate rerun |
| Missing-only extraction | 5 min | 0.379 s | Complete | `pypdf` and `html-regex`; source absent |
| Full-paper and availability review | 25 min | about 14 min | Complete | Algorithm, equations, Tables I-II, runtime, conclusions, publisher DOI, code search |
| Related DEP synthesis | 10 min | about 5 min | Complete | iKalibr, HSD FTI-FDet, Self Learned IDC |
| Artifact generation | 20 min | about 15 min | Complete | Seven public artifacts drafted |
| Validation and source gate | 10 min | about 5 min | Complete | Structural, syntax, code, YAML, count, public-safety, and seven-file allowlist checks passed |
| Repository and Slack | 10 min | about 2 min | Complete | Direct default-branch push and Slack notice succeeded |

## Extraction Cache

| Field | Value |
|---|---|
| Initial / final | Miss / `cached` |
| Mode | `missing-only` |
| Extractors | `pypdf` / `html-regex` / none |
| PDF fallback | `pdftotext` unavailable; `pypdf` succeeded |
| PDF / HTML / source text | 24,083 / 31,431 / 0 bytes |

## Source Integrity Repair

| Check | Observed | Result |
|---|---:|---|
| PDF | 5,980,379 bytes; header/EOF valid | Pass; preserved |
| Official full HTML | HTTP 404 | Missing |
| Approved ar5iv HTML | 292,496 bytes; 31,447 body characters | Pass |
| Document / headings / structure | present / 26 / 5 | Pass |
| Metadata HTML | 42,471 bytes | Metadata only |
| Source package / partials | not collected / 0 | Acceptable / pass |
| Final classification | `complete` | Review gate opened |

## Dedup Index Update

- Substantive matches: 0
- Exclusions / reselections: 0 / 0
- New pointer: arXiv:1808.09128v1; slug `Stereo-Lane-Detection`
- Commit reference: https://github.com/Delphoa/Black-Lake/commit/c3270f583b0a43f962067afdcb7c76a19c8d8d7c
- Status: deposited pointer validated with primary commit attribution

## Expected vs Observed Trajectory

The official HTML route failed as expected for an older arXiv record, but the approved ar5iv fallback passed the complete-paper gate immediately. Cache extraction was faster than estimated because `pypdf` and the HTML adapter succeeded without secondary fallback. The time saved supported a full reading of the temporal disparity mechanism, dynamic-programming road/vanishing-point model, lane counts, runtime statement, and the relationship between the reported relative speedup and non-real-time end-to-end performance.

Review was not shortened because the paper is five pages. Its central evidence requires reconstructing the denominator behind “99%,” comparing 10 incorrect plus 14 missed lanes against the prior method's 14 plus 33, and separating a 37% disparity-stage reduction from the 0.21-second full-frame runtime. These distinctions control the practical interpretation.

## Shortfalls and Follow-Up

- No reproduction, image-level annotation audit, code execution, or embedded benchmark was performed.
- No official code was identified; the sequence and annotation manifest is incomplete.
- Temporal recovery, calibration drift, adverse conditions, modern baselines, uncertainty, and safety routing remain open.
- Public allowlist passed with exactly seven Markdown/JSON artifacts and no source files; submission and Slack delivery completed.
