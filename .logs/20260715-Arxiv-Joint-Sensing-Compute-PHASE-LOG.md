# Arxiv DEP Phase Log: Joint Sensing MEC

## Public-Safe Run Summary

- Deposit date: 2026-07-15
- Selected paper: arXiv:2210.17025, *Joint Optimization of Sensing and Computation for Status Update in Mobile Edge Computing Systems*
- Selection: first uniform draw, zero-based index 7,665 of 75,776 units
- Dedup: no prior ID, DOI, normalized-title, slug, artifact, memory, or recent-window marker
- Source integrity: initial `partial`; repaired to verified `complete`
- Source files: withheld locally; none uploaded or copied into the repository
- Cache: initial miss; final `cached`
- Dedup index: validation passed; update prepared for submission

## Phase Metrics

Elapsed values are rounded public-safe durations. Expected durations guide trajectory review and are not hard stop limits.

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Authority, memory, skill contract, and extractor preflight | 5 min | about 3.5 min | Complete | Live Black Lake, `.lake-data`, and Black-Lake-Data READMEs read; required skills/references loaded; `pypdf` available |
| Candidate enumeration and random draw | 3 min | 6.6 s | Complete | 75,776 unique PDF-parent units; index 7,665 |
| Detailed dedup and recent-marker validation | 5 min | about 1.0 min | Complete | Public index, repository artifacts, automation memory, Black-Lake-Data, and worktrees checked |
| Source integrity classification | 3 min | under 1 min | Complete | Initial `partial`: valid PDF, missing full-paper HTML |
| Bounded archive repair transfer | 10 min | 4.1 s | Complete | One attempt per artifact; 40 MB target ceiling; 10 MB partial ceiling; no credentials |
| Repair integration and complete-source verification | 5 min | about 2.0 min | Complete | PDF hash match; HTML structural gate; README/attribution/summary/verification updated; zero partials |
| Missing-only extraction cache | 5 min | 0.8 s | Complete | Initial miss became `cached`; PDF, HTML, and source text present |
| Primary-paper and published-version review | 25 min | about 7.5 min | Complete | Model, equations, algorithms, simulations, appendices, publication metadata, and code search inspected |
| Related DEP exploration and exact-three synthesis | 10 min | about 3.0 min | Complete | Self-Learned IDC, RRT-CBF Motion, and iKalibr Calibration selected |
| Artifact generation | 20 min | about 6.0 min | Complete | Job log, phase log, Report-Mark, README, manuscript, index, and dedup update |
| Validation and source-upload gate | 10 min | about 2.5 min | Complete | Heading/count/schema, JSON, public-safe scan, Python mock-up parsing, and working-tree allowlist passed; staged allowlist is rechecked immediately before commit |
| Repository submission and Slack notice | 10 min | pending final measurement | Pending | Direct default-branch push preferred; branch/PR fallback if denied |

## Extraction Cache

| Field | Value |
|---|---|
| Initial lookup | Miss |
| Mode | `missing-only` |
| Network during extraction | None; repaired local bundle used |
| Final status | `cached` |
| PDF extractor | `pypdf` (`pdftotext` unavailable) |
| HTML extractor | `html-regex` |
| Source extractor | `tarfile` |
| Fallback status | Successful PDF fallback to `pypdf` |
| PDF text | Present, 69,290 bytes |
| HTML text | Present, 102,224 bytes |
| Source text | Present, 84,754 bytes |

## Source Integrity Repair

| Check | Observed | Result |
|---|---:|---|
| Existing PDF | 803,785 bytes; `%PDF-`; trailing `%%EOF` | Pass |
| Downloaded PDF | Exact hash match with existing PDF | Pass; original preserved |
| Full-paper HTML | 1,182,606 bytes; 120,156 body characters | Pass |
| Document marker | Present | Pass |
| Heading/section markers | 77 | Pass |
| Paper-structure terms | 7 | Pass |
| Metadata HTML | 42,171 bytes | Present; metadata only |
| TeX/source package | 479,154 bytes | Present locally |
| Remaining partial files | 0 | Pass |
| Final source classification | `complete` | Review gate opened |

## Dedup Index Update

- Initial selected-paper matches: 0 after private repair-input cleanup
- Exclusions: 0
- Reselections: 0
- New pointer: arXiv:2210.17025v1; DOI `10.1109/TWC.2023.3261338`; slug `Joint-Sensing-Compute`
- Artifact paths: job log, phase log, Report-Mark, DEP-E directory/manuscript, and publication index owner
- Source URLs: arXiv abstract/PDF/e-print, ar5iv full-paper fallback, arXiv DOI, journal DOI, and author-hosted journal article
- Commit or PR reference: pending primary submission
- Status: prepared for `deposited`

## Expected vs Observed Trajectory

The run stayed within the whole-job guidance even though integrity repair was not part of an ideal cache-hit path. The repair transfer itself was short, but the gate correctly paused review until full structural validation, archive-record updates, and cache extraction completed. Paper review was faster than the nominal estimate because all three extraction modes succeeded and the paper has a compact analytical/simulation structure.

The remaining risk is validation/submission rather than evidence collection. Repository changes must remain confined to generated Markdown and the derived dedup JSON. Any source document, cache, extracted text, local path, or private repair file in the staged set is a hard stop.

## Shortfalls and Follow-Up

- No official code, raw result values, deterministic seeds, or executable environment was found.
- No simulation, formal proof, equilibrium audit, or energy/network measurement was reproduced.
- The source's apparent cost-improvement ambiguity and global-optimality wording remain unresolved.
- Scenario-specific thresholds should not be generalized beyond the reported parameterization.
- Tail latency, queueing, correlated sensing errors, calibration uncertainty, admission fairness, and hard freshness violations need follow-up evaluation.
