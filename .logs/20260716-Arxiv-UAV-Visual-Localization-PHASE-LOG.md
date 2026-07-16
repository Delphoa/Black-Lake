# Arxiv DEP Phase Log: UAV Visual Localization

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:2506.09748v1
- Selection: first draw, index 37,833 of 75,776 units
- Dedup: no prior substantive deposit
- Source: `partial` repaired to verified `complete` with official arXiv HTML
- Cache: miss to `cached`
- Source files: withheld locally; none uploaded
- Dedup index: pending deposited pointer and primary commit reference

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Candidate enumeration and draw | 3 min | about 8 s | Complete | 75,777 PDFs; 75,776 units; index 37,833 |
| Dedup validation | 5 min | about 2 min | Complete | Repository, memory, active checkouts, and companion context checked |
| Source classification | 3 min | under 1 min | Complete | PDF valid; full HTML missing |
| Download preflight | 5 min | about 1 min | Complete | Bounded single-paper repair; no partial bytes accepted |
| Archive repair | 10 min | under 1 min | Complete | Official full HTML and metadata succeeded on first requests |
| Integrity records and verification | 5 min | about 4 min | Complete | README, attribution, CSV summary, and JSON report updated; gate rerun |
| Missing-only extraction | 5 min | 0.472 s | Complete | `pypdf` and `html-regex`; source absent |
| Full-paper and availability review | 25 min | about 18 min | Complete | Method, datasets, Tables I-III, ablation, limitations, code/data availability |
| Related DEP synthesis | 10 min | about 5 min | Complete | iKalibr, SSP Oriented Detection, AFIDAF Vision Filters |
| Artifact generation | 20 min | about 16 min | Complete | Seven public artifacts drafted |
| Validation and source gate | 10 min | about 5 min | Complete | Structural, syntax, count, public-safety, and seven-file allowlist checks passed |
| Repository and Slack | 10 min | pending | Pending | Direct default-branch submission and channel notice |

## Extraction Cache

| Field | Value |
|---|---|
| Initial / final | Miss / `cached` |
| Mode | `missing-only` |
| Extractors | `pypdf` / `html-regex` / none |
| PDF fallback | `pypdf` succeeded; no text fallback required |
| PDF / HTML / source text | 43,965 / 61,869 / 0 bytes |

## Source Integrity Repair

| Check | Observed | Result |
|---|---:|---|
| PDF | 1,585,169 bytes; header/EOF valid | Pass; preserved |
| Official full HTML | 343,535 bytes; 53,166 body characters | Pass |
| Document / headings / structure | present / 34 / 4 | Pass |
| Metadata HTML | 44,128 bytes | Metadata only |
| Source package / partials | not collected / 0 | Acceptable / pass |
| Final classification | `complete` | Review gate opened |

## Dedup Index Update

- Substantive matches: 0
- Exclusions / reselections: 0 / 0
- New pointer: arXiv:2506.09748v1; slug `UAV-Visual-Localization`
- Commit reference: pending
- Status: draft pointer pending submission validation

## Expected vs Observed Trajectory

The source repair was materially faster than the estimate because the official full-paper HTML and metadata endpoints both succeeded on the first bounded requests. Extraction was also faster than expected because the PDF and HTML adapters produced complete cache text without fallback. The saved time was used to inspect the success/error denominator, per-dataset tables, component ablation, dataset-release claim, and code availability rather than truncating the source-first review.

The review trajectory remains within the whole-job guidance. The most important evidence tension is not extraction cost but evaluation interpretation: mean localization error is reported only for non-drift segments, while deployment decisions require drift-inclusive distributions and abstention behavior. Related-entry synthesis was bounded to three repository artifacts with direct conceptual overlap.

## Shortfalls and Follow-Up

- No reproduction, model execution, source-package inspection, or target-device benchmark was performed.
- No usable CS-UAV release URL or official method repository was found; the paper's placeholder is not a release.
- Geographic, seasonal, camera, map-age, and adversarial generalization remain open.
- Public allowlist passed with exactly seven Markdown/JSON artifacts and no source files; repository and Slack steps remain pending.
