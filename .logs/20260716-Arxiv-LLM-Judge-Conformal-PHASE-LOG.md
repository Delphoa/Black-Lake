# Arxiv DEP Phase Log: LLM Judge Conformal

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:2509.18658v1
- Selection: first uniform draw, index 29,719 of 75,776 units
- Dedup: no prior deposit; metadata inventory row only
- Source integrity: `partial` repaired to verified `complete`
- Cache: miss to `cached`
- Source files: withheld locally; none uploaded
- Dedup index: validated deposited pointer records the primary artifact commit

## Phase Metrics

Elapsed values are rounded public-safe durations; estimates guide trajectory review rather than impose hard stops.

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Authority, memory, and contracts | 6 min | about 7 min | Complete | Live repository authority plus required source, manuscript, archive, download, DEP, lint, and Slack contracts loaded |
| Candidate enumeration and draw | 3 min | about 4 s | Complete | 75,777 PDFs collapsed to 75,776 units; index 29,719 |
| Dedup validation | 5 min | about 2 min | Complete | Repository, index, memory, active worktrees, and Black-Lake-Data checked |
| Source classification | 3 min | under 1 min | Complete | Valid PDF; full-paper HTML missing |
| Download preflight | 5 min | about 3 min | Complete | Expected transfer under 4 MB; ample free disk; no partials or active owner process |
| Bounded archive repair | 10 min | about 3 s | Complete | Official HTML, metadata, and source archive succeeded; no fallback required |
| Integrity verification and records | 5 min | about 4 min | Complete | PDF/HTML/source checks and local provenance records passed |
| Missing-only extraction cache | 5 min | 1.217 s | Complete | `pypdf`, `html-regex`, and `tarfile`; final status `cached` |
| Primary paper and code review | 25 min | about 15 min | Complete | Full PDF/HTML/TeX and official repository at pinned commit inspected |
| Related DEP synthesis | 10 min | about 5 min | Complete | RLMF Uncertainty, PAC Confidence, and ConMax Reasoning |
| Artifact generation | 20 min | about 12 min | Complete | Logs, Report-Mark, DEP README/manuscript, publication index, and dedup pointer |
| Validation and source gate | 10 min | about 3 min | Complete | Schema, exact counts, code syntax, JSON, public safety, and worktree checks passed; staged allowlist follows |
| Repository and Slack | 10 min | about 2 min | Complete | Direct default-branch push succeeded; Slack notice delivered; record-only follow-up prepared |

## Extraction Cache

| Field | Value |
|---|---|
| Initial lookup | Miss |
| Mode | `missing-only` |
| Network during extraction | None; repaired local bundle used |
| Final status | `cached` |
| PDF extractor | `pypdf`; `pdftotext` unavailable |
| HTML extractor | `html-regex` |
| Source extractor | `tarfile` |
| PDF text | 136,698 bytes |
| HTML text | 160,453 bytes |
| Source text | 342,736 bytes |

## Source Integrity Repair

| Check | Observed | Result |
|---|---:|---|
| PDF | 3,119,581 bytes; header and EOF valid | Pass; existing file preserved |
| Full-paper HTML | 890,619 bytes; 193,341 body characters | Pass |
| Document marker | Present | Pass |
| Heading markers | 115 | Pass |
| Structure terms | 8 | Pass |
| Metadata HTML | 41,526 bytes | Present; metadata only |
| Source package | 2,383,959 bytes; 25 entries | Pass |
| Partial files | 0 | Pass |
| Final classification | `complete` | Review gate opened |

## Dedup Index Update

- Initial artifact matches: 0
- Exclusions: 0
- Reselections: 0
- New pointer: arXiv:2509.18658v1; slug `LLM-Judge-Conformal`
- Commit reference: https://github.com/Delphoa/Black-Lake/commit/72f56304bb93f4906fe75e5fa59ddc73ec34c09e
- Status: deposited pointer validated with primary commit attribution

## Expected vs Observed Trajectory

The first draw passed dedup but failed the initial source gate because full-paper HTML was absent. Review paused as required. The repair stayed far below its disk and retry budgets, used only official arXiv endpoints, and produced no incomplete files. The cache then completed quickly from the verified local bundle.

The source review required extra attention because coverage and efficiency change across judges, datasets, calibration sizes, and conformal methods. The artifact therefore preserves representative exact results while treating broad reliability claims as conditional on exchangeability and the evaluated pipelines.

## Shortfalls and Follow-Up

- No independent experiment rerun or formal proof check was performed.
- No production distribution-shift study was inspected.
- Repository notebooks and scripts were inventoried but not executed.
- Repository submission and Slack delivery completed; the record-only follow-up preserves their immutable links.
