# Arxiv DEP Phase Log: AVA Vignetting Attack

## Public-Safe Run Context

- Deposit date: 2026-07-22.
- Selected paper: *AVA: Adversarial Vignetting Attack against Visual Recognition*.
- Stable identifiers: arXiv:2105.05558; DOI:10.24963/ijcai.2021/145.
- Selection: uniform random index 13,681 over 75,777 unique paper units; first draw accepted.
- Whole-job guidance: 90-120 minutes, used as trajectory guidance rather than a hard review cutoff.

## Phase Metrics

| Phase | Expected | Observed | Status | Notes |
|---|---:|---:|---|---|
| Contract, memory, and live repository review | 8 min | about 10 min | complete | Read required skill contracts and live repository policies before selection. |
| Candidate enumeration and random draw | 4 min | under 1 min | complete | 75,780 PDFs collapsed to 75,777 parent paper units. |
| Dedup and recent-marker validation | 6 min | about 4 min | complete | No identifier, DOI, title, slug, or 24-hour marker collision. |
| Source integrity classification and repair | 15 min | about 8 min | complete | Initial state partial; approved fallback supplied verified full-paper HTML while preserving the valid PDF. |
| Extractor preflight and cache population | 5 min | under 2 min | complete | `missing-only`; cache miss backfilled to cached. Extraction itself completed in 1.745 seconds. |
| Full-paper, source, figure, table, and implementation review | 35 min | about 22 min | complete | Eight pages visually inspected; numeric and source-level consistency checks performed. |
| Related DEP synthesis | 10 min | about 7 min | complete | Exactly three conceptually overlapping deposits inspected. |
| Artifact drafting and validation | 30 min | about 18 min | complete | Five new artifacts plus two index updates; schema, count, syntax, JSON, and public-safety checks passed. |
| Allowlist, submission, and Slack notification | 15 min | about 5 min | complete | Seven-file allowlist passed; primary commit was remotely verified and Slack delivery succeeded. |

## Source-Integrity Metrics

| Check | Result |
|---|---|
| Initial classification | partial |
| Final classification | complete |
| PDF size / header / EOF | 5,822,468 bytes / pass / pass |
| Full HTML size | 474,183 bytes |
| HTML body characters | 49,452 |
| Document marker | pass |
| Heading markers | 29 |
| Structure terms | 6 |
| Partial artifacts | 0 |
| Repair outcome | verified ar5iv full-paper fallback; local provenance records refreshed |

## Cache and Extractor Status

- Preflight fallback order: `pdftotext`, `fitz`, `pypdf`, `PyPDF2`, `pdfminer`, HTML, source package.
- Available primary PDF fallback: `pypdf`.
- Unavailable preferred tool: `pdftotext`.
- Cache lookup: miss.
- Backfill: successful.
- Final cache state: cached.
- Extractors: `pypdf` for PDF text, HTML regex extraction for the full-paper rendering, and `tarfile` for the source package.
- Extracted text sizes: PDF 45,226 bytes; HTML 50,561 bytes; source package 89,749 bytes.
- Network during cache extraction: none.

## Dedup Index Status

The first draw passed the public index, repository artifact, automation-memory, active-worktree, and related-data checks. Duplicate exclusions and reselections were both zero. The pointer is finalized with deposited status and the remotely verified primary commit.

## Expected-vs-Observed Trajectory

The first-draw acceptance and single bounded repair pass kept selection, repair, and extraction below their estimates. Review time was still spent on the complete source, source representation, all PDF pages, result tables, and a discrepancy between prose and Table 2. The rounded phase total was about 77 minutes, below the whole-job guidance because selection, repair, cache extraction, and submission completed without retries; evidence review was not truncated.

## Shortfalls

1. The official arXiv HTML route did not provide a usable full paper, so the verified ar5iv rendering was required.
2. `pdftotext` was unavailable; extraction used the successful `pypdf` fallback.
3. No official code, execution environment, seed-level results, uncertainty estimates, or physical-camera experiment was found; no empirical reproduction was attempted.

## Public-Output Gate

The gate passed with exactly seven files: six generated Markdown artifacts or indexes and the required derived dedup JSON. PDF, HTML, TeX/source archives, extracted text, caches, renders, metadata snapshots, and local provenance files remained outside the repository. Staged-name, public-safety, JSON, schema, exact-count, Python syntax, and whitespace checks passed. Primary commit [4000bc7283145a6a128ffe0c66ff63c8a2bd14b3](https://github.com/Delphoa/Black-Lake/commit/4000bc7283145a6a128ffe0c66ff63c8a2bd14b3) was remotely verified; the Slack notification was delivered to `#black-lake-artifacts`.
