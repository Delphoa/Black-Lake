# Arxiv DEP Phase Log: Multi-Point ISAC

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:2208.07592v2
- Selection: first uniform draw, index 53,616 of 75,776 units
- Dedup: no prior deposit; metadata inventory row only
- Source integrity: `partial` repaired to verified `complete`
- Cache: miss to `cached`
- Source files: withheld locally; none uploaded
- Dedup index: validated deposited pointer records the primary artifact commit

## Phase Metrics

Elapsed values are rounded public-safe durations; estimates guide trajectory review rather than impose hard stops.

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Authority, memory, and contracts | 6 min | reused from the current five-run batch | Complete | Live repository authority and required source, manuscript, archive, download, DEP, lint, and Slack contracts already loaded |
| Candidate enumeration and draw | 3 min | about 4 s | Complete | 75,777 PDFs collapsed to 75,776 units; index 53,616 |
| Dedup validation | 5 min | about 2 min | Complete | Repository, index, memory, active worktree, and Black-Lake-Data checked |
| Source classification | 3 min | under 1 min | Complete | Valid PDF; full-paper HTML missing |
| Download preflight | 5 min | about 2 min | Complete | Expected transfer under 12 MB; ample free disk; no partials or active owner process |
| Bounded archive repair | 10 min | about 5 s | Complete | Official HTML unavailable; ar5iv fallback plus metadata and source archive succeeded |
| Integrity verification and records | 5 min | about 4 min | Complete | PDF/HTML/source checks and local provenance records passed |
| Missing-only extraction cache | 5 min | 1.527 s | Complete | `pypdf`, `html-regex`, and `tarfile`; final status `cached` |
| Primary paper review | 25 min | about 13 min | Complete | Full PDF/HTML/TeX, equations, appendix proof, figures, and references inspected |
| Related DEP synthesis | 10 min | about 4 min | Complete | Joint Sensing MEC, 2D-RC OTFS, and Telecom AI Roadmap |
| Artifact generation | 20 min | about 12 min | Complete | Logs, Report-Mark, DEP README/manuscript, publication index, and dedup pointer |
| Validation and source gate | 10 min | about 3 min | Complete | Schema, exact counts, code syntax, JSON uniqueness, public safety, and seven-file staged allowlist passed |
| Repository and Slack | 10 min | about 4 min | Complete | Concurrent index entry preserved by rebase; direct default-branch push and Slack notice succeeded |

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
| PDF text | 31,902 bytes |
| HTML text | 58,990 bytes |
| Source text | 41,816 bytes |

## Source Integrity Repair

| Check | Observed | Result |
|---|---:|---|
| PDF | 1,345,194 bytes; header and EOF valid | Pass; existing file preserved |
| Full-paper HTML | 954,733 bytes; 71,826 body characters | Pass; ar5iv fallback |
| Document marker | Present | Pass |
| Heading markers | 32 | Pass |
| Structure terms | 7 | Pass |
| Metadata HTML | 42,643 bytes | Present; metadata only |
| Source package | 6,933,844 bytes; 9 entries | Pass |
| Partial files | 0 | Pass |
| Final classification | `complete` | Review gate opened |

## Dedup Index Update

- Initial artifact matches: 0
- Exclusions: 0
- Reselections: 0
- New pointer: arXiv:2208.07592v2; slug `Multi-Point-ISAC`
- Commit reference: https://github.com/Delphoa/Black-Lake/commit/d7b708a76a0872c0014fec4f828bbde0263cc6a0
- Status: deposited pointer validated with primary commit attribution

## Expected vs Observed Trajectory

The first draw passed dedup but failed the initial source gate because full-paper HTML was absent. Review paused as required. The official arXiv HTML endpoint did not provide a paper, so the bounded repair used the approved ar5iv fallback. The PDF, fallback HTML, metadata page, and source archive then passed the complete-paper checks with no partial files.

Extraction was substantially faster than estimated because the repaired bundle was local and compact. Source review stayed within its trajectory; the greatest interpretive load was separating the exact heterogeneous-error voting model from its averaged-error surrogate and distinguishing convergence on the surrogate problem from global optimality of the original mixed objective.

## Shortfalls and Follow-Up

- No independent simulation or optimization rerun was performed.
- No official code repository was identified.
- Robustness to correlated observations, channel uncertainty, mobility, and device churn remains unmeasured.
- Repository submission and Slack delivery completed; the record-only follow-up preserves their immutable links.
