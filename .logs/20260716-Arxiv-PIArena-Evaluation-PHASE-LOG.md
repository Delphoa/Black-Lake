# Arxiv DEP Phase Log: PIArena Evaluation

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:2604.08499v1
- Selection: first uniform draw, index 1,108 of 75,776 units
- Dedup: no prior research deposit; one metadata-only inventory row
- Source integrity: `partial` repaired to verified `complete`
- Cache: miss to `cached`
- Source files: withheld locally; none uploaded
- Dedup index: prepared; primary commit attribution pending

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Authority, memory, and contracts | 8 min | about 8 min | Complete | Automation memory, required skills, schemas, repository submission rules, and Slack contract loaded |
| Candidate enumeration and draw | 3 min | about 16 s | Complete | 75,777 PDFs; 75,776 units; index 1,108 |
| Dedup validation | 5 min | under 1 min | Complete | Repository, dedup index, memory, active repository checkouts, and companion repository checked |
| Source classification | 3 min | under 1 min | Complete | Valid PDF; full-paper HTML missing |
| Download preflight | 5 min | about 1 min | Complete | Known official endpoints and sizes; ample disk; zero partials; no active transfer owner |
| Bounded archive repair | 10 min | under 1 min | Complete | Official full HTML and metadata succeeded on first requests |
| Integrity verification and records | 5 min | about 4 min | Complete | PDF/HTML checks, hashes, README, attribution, CSV, and JSON report passed |
| Missing-only extraction cache | 5 min | 0.762 s | Complete | `pypdf` and `html-regex`; status `cached` |
| Primary paper and code review | 25 min | about 18 min | Complete | Full PDF/HTML, main tables, appendix, limitations, official code README and metadata inspected |
| Related DEP synthesis | 10 min | about 5 min | Complete | Agent Systems Review, Agent Memory Forensics, and Judge Conformal |
| Artifact generation | 20 min | about 15 min | Complete | Logs, report, DEP, publication index, and dedup pointer |
| Validation and source gate | 10 min | about 4 min | Complete | Schema, exact counts, code syntax, JSON uniqueness, public safety, and seven-file allowlist passed |
| Repository and Slack | 10 min | pending | Pending | Direct default-branch submission and channel notice |

## Extraction Cache

| Field | Value |
|---|---|
| Initial lookup | Miss |
| Mode | `missing-only` |
| Network during extraction | None; repaired local bundle used |
| Final status | `cached` |
| PDF / HTML / source extractors | `pypdf` / `html-regex` / none |
| PDF fallback reason | `pdftotext` unavailable; `pypdf` succeeded |
| PDF / HTML / source text | 98,133 / 101,304 / 0 bytes |

## Source Integrity Repair

| Check | Observed | Result |
|---|---:|---|
| PDF | 1,081,223 bytes; header and EOF valid | Pass; preserved |
| Full-paper HTML | 675,320 bytes; 86,861 body characters | Pass; official arXiv |
| Document marker / heading markers / structure terms | present / 84 / 6 | Pass |
| Metadata HTML | 42,741 bytes | Present; metadata only |
| Source package | Not collected | Not required for complete classification |
| Partial files | 0 | Pass |
| Final classification | `complete` | Review gate opened |

## Dedup Index Update

- Initial substantive artifact matches: 0
- Metadata-only inventory matches: 1
- Exclusions: 0
- Reselections: 0
- New pointer: arXiv:2604.08499v1; slug `PIArena-Evaluation`
- Commit reference: pending
- Status: prepared

## Expected vs Observed Trajectory

The first draw passed dedup but lacked full-paper HTML, so review paused. Official arXiv repair succeeded on the first bounded requests and left zero partial files. Cache extraction was much faster than estimated because the repaired unit supplied both verified PDF and full HTML.

Review remained within the full-paper timebox. The central difficulty was not source availability but measurement interpretation: PIArena combines heterogeneous utility metrics, judge-based ASR, unavailable attack-time utility for detection defenses, and an adaptive search procedure. Phase estimates did not truncate the review.

## Shortfalls and Follow-Up

- No independent benchmark run, code execution, model invocation, dependency audit, or dataset verification.
- No comprehensive evaluator calibration across the 1,700 benchmark samples.
- No held-out adaptive-strategy or multilingual robustness study was identified.
- Task-aligned disinformation motivates content verification, but the paper does not implement or evaluate that system-level control.
- Public allowlist passed with exactly seven Markdown/JSON artifacts and no source files; repository submission and Slack delivery remain pending.
