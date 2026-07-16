# Arxiv DEP Phase Log: Biometric Identity Gaps

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:2605.18238v1
- Selection: first uniform draw, index 28,438 of 75,776 units
- Dedup: no prior research deposit
- Source integrity: `partial` repaired to verified `complete`
- Cache: miss to `cached`
- Source files: withheld locally; none uploaded
- Dedup index: validated deposited pointer records the primary artifact commit

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Authority, memory, and contracts | 6 min | reused from current batch | Complete | Required skills, schemas, memory, and live repository authority loaded |
| Candidate enumeration and draw | 3 min | about 3 s | Complete | 75,777 PDFs; 75,776 units; index 28,438 |
| Dedup validation | 5 min | about 2 min | Complete | Repository, index, memory, active worktrees, and companion repository checked |
| Source classification | 3 min | under 1 min | Complete | Valid 25-page PDF; full-paper HTML missing |
| Download preflight | 5 min | about 2 min | Complete | Expected transfer under 20 MB; ample disk; zero partials; no active transfer owner |
| Bounded archive repair | 10 min | about 15 s | Complete | Official HTML, metadata, and source archive succeeded within bounded requests |
| Integrity verification and records | 5 min | about 4 min | Complete | PDF/HTML/source checks and four local archive records passed |
| Missing-only extraction cache | 5 min | 1.4 s | Complete | `pypdf`, `html-regex`, and `tarfile`; status `cached` |
| Primary paper and availability review | 25 min | about 20 min | Complete | Full PDF/HTML/TeX, equations, tables, appendix, ethics, limitations, and lab availability metadata inspected |
| Related DEP synthesis | 10 min | about 5 min | Complete | Document Fraud LLM, BA-LoRA Bias, and Mosaic Safety |
| Artifact generation | 20 min | about 12 min | Complete | Logs, report, DEP, index, and dedup pointer |
| Validation and source gate | 10 min | about 3 min | Complete | Schema, exact counts, code syntax, JSON uniqueness, public safety, and seven-file allowlist passed |
| Repository and Slack | 10 min | about 3 min | Complete | Direct default-branch push and Slack notice succeeded |

## Extraction Cache

| Field | Value |
|---|---|
| Initial lookup | Miss |
| Mode | `missing-only` |
| Network during extraction | None; repaired local bundle used |
| Final status | `cached` |
| PDF / HTML / source extractors | `pypdf` / `html-regex` / `tarfile` |
| PDF fallback reason | `pdftotext` unavailable; `pypdf` succeeded |
| PDF / HTML / source text | 84,547 / 112,658 / 152,886 bytes |

## Source Integrity Repair

| Check | Observed | Result |
|---|---:|---|
| PDF | 8,894,821 bytes; 25 pages; header and EOF valid | Pass; preserved |
| Full-paper HTML | 658,614 bytes; 109,692 body characters | Pass; official arXiv |
| Document marker / headings / structure terms | present / 49 / 6 | Pass |
| Metadata HTML | 44,131 bytes | Present; metadata only |
| Source package | 8,262,552 bytes; 24 entries | Pass |
| Partial files | 0 | Pass |
| Final classification | `complete` | Review gate opened |

## Dedup Index Update

- Initial artifact matches: 0
- Exclusions: 0
- Reselections: 0
- New pointer: arXiv:2605.18238v1; slug `Biometric-Identity-Gaps`
- Commit reference: https://github.com/Delphoa/Black-Lake/commit/50e88f2c5a4338e5aae1c9d55d71a728be55b813
- Status: deposited pointer validated with primary commit attribution

## Expected vs Observed Trajectory

The first draw passed dedup but lacked full-paper HTML, so review paused. Official arXiv repair succeeded on the first bounded requests and left zero partial files. Cache extraction was much faster than estimated because the repaired local unit was complete.

Review took the expected full-paper interval because the abstract's million-scale language required separation into embedding allocation, image realization, open-world evaluation, and detector claims. The paper's appendix usefully labels the capacity model an approximation and audits some independence/uniformity assumptions, while the main text contains a small table/text inconsistency and stronger safety language than the evidence supports. Phase estimates did not truncate review.

## Shortfalls and Follow-Up

- No independent reproduction, model execution, dataset audit, or capacity recalculation.
- No official code/project/data release was linked by the paper or authors' lab metadata at inspection time.
- No cross-encoder, demographic, site, device, attack, or longitudinal study was found.
- The ethical analysis does not fully address identity fraud, anthropomorphic deception, enrollment abuse, consent, or resemblance outside the chosen gallery/encoder.
- Public allowlist passed with exactly seven Markdown/JSON artifacts and no source or biometric artifacts; submission and Slack delivery completed.
