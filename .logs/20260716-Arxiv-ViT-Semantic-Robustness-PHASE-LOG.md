# Arxiv DEP Phase Log: ViT Semantic Robustness

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:2507.01788v2
- Selection: first draw, index 30,086 of 75,776 units
- Dedup: no prior substantive deposit
- Source: `partial` repaired to verified `complete` with approved ar5iv fallback
- Cache: miss to `cached`
- Source files: withheld locally; none uploaded
- Dedup index: prepared; commit attribution pending

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Candidate enumeration and draw | 3 min | about 8 s | Complete | 75,777 PDFs; 75,776 units; index 30,086 |
| Dedup validation | 5 min | about 2 min | Complete | Repository, memory, active repository checkouts, and companion repository checked |
| Source classification | 3 min | under 1 min | Complete | PDF valid; full HTML missing |
| Download preflight and fallback | 7 min | about 3 min | Complete | Official HTML 404; approved ar5iv endpoint verified |
| Bounded archive repair | 10 min | under 1 min | Complete | Full HTML and metadata succeeded on first requests |
| Integrity records and verification | 5 min | about 73 min | Complete with delay | Permission review timed out twice; patch-authored records were copied through the authorized boundary and independently validated |
| Missing-only extraction | 5 min | 0.512 s | Complete | `pypdf` and `html-regex`; source absent |
| Full-paper and availability review | 25 min | about 16 min | Complete | Methods, Tables I-III, mitigation, discussion, linked baseline code |
| Related DEP synthesis | 10 min | about 5 min | Complete | Medical Diff VQA, Document Fraud LLM, AFIDAF Vision Filters |
| Artifact generation | 20 min | about 14 min | Complete | Seven public artifacts drafted |
| Validation and source gate | 10 min | about 4 min | Complete | Structural, syntax, count, public-safety, and seven-file allowlist gates passed |
| Repository and Slack | 10 min | pending | Pending | Direct push and channel notice |

## Extraction Cache

| Field | Value |
|---|---|
| Initial / final | Miss / `cached` |
| Mode | `missing-only` |
| Extractors | `pypdf` / `html-regex` / none |
| PDF fallback | `pdftotext` unavailable; `pypdf` succeeded |
| PDF / HTML / source text | 36,652 / 30,928 / 0 bytes |

## Source Integrity Repair

| Check | Observed | Result |
|---|---:|---|
| PDF | 2,364,756 bytes; header/EOF valid | Pass; preserved |
| Official full HTML | HTTP 404 | Missing |
| Approved ar5iv HTML | 100,911 bytes; 26,427 body characters | Pass |
| Document / headings / structure | present / 31 / 5 | Pass |
| Metadata HTML | 42,666 bytes | Metadata only |
| Source package / partials | not collected / 0 | Acceptable / pass |
| Final classification | `complete` | Review gate opened |

## Dedup Index Update

- Substantive matches: 0
- Exclusions / reselections: 0 / 0
- New pointer: arXiv:2507.01788v2; slug `ViT-Semantic-Robustness`
- Commit reference: pending
- Status: prepared

## Expected vs Observed Trajectory

The official HTML gap required the authorized ar5iv fallback, which passed immediately. The archive-record step exceeded its estimate because permission review did not resolve; no source was re-downloaded or treated as progress during that delay. A patch-authored copy workflow produced the four required local records, and the complete-source gate was rerun before extraction.

Review remained source-first despite the time overrun. The paper is short, but its headline claim required separating representation matching, downstream classification failure, pixel similarity, target-embedding similarity, and the unevaluated mitigation proposal. The delay did not justify truncating scientific review.

## Shortfalls and Follow-Up

- No independent optimization, classifier evaluation, code execution, or image inspection by clinicians.
- No official PRM code artifact or pinned experiment manifest.
- Generality and imperceptibility claims need broader models, modalities, institutions, readers, and threat models.
- Public allowlist passed with exactly seven Markdown/JSON artifacts and no source or medical-image files; repository/Slack status remains pending.
