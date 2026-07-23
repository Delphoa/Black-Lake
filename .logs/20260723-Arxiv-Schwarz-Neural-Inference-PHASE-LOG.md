# Arxiv DEP Phase Log: Schwarz Neural Inference

## Public-Safe Run Context

- Deposit date: 2026-07-23.
- Selected paper: *Operator Learning with Domain Decomposition for Geometry Generalization in PDE Solving*.
- Stable identifiers: arXiv:2504.00510v2; DOI:10.48550/arXiv.2504.00510.
- Venue: ICLR 2026 Poster.
- Selection: uniform random index 57,700 over 75,777 unique paper units; first draw accepted.
- Whole-job guidance: 90-120 minutes, used as trajectory guidance rather than a hard review cutoff.

## Phase Metrics

| Phase | Expected | Observed | Status | Notes |
|---|---:|---:|---|---|
| Contract, memory, and live repository review | 8 min | about 12 min | complete | Required skill contracts, prior automation state, and live repository policies were read before selection. |
| Candidate enumeration and random draw | 4 min | under 1 min | complete | 75,780 PDFs collapsed to 75,777 parent paper units. |
| Dedup and recent-marker validation | 6 min | about 3 min | complete | No identifier, DOI, title, slug, deposit, memory, or 24-hour collision. |
| Source integrity classification and repair | 15 min | about 7 min | complete | Existing valid PDF preserved; official metadata, full HTML, and source package collected in one bounded pass. |
| Extractor preflight and cache population | 5 min | under 2 min | complete | `missing-only`; extraction completed in 0.860 seconds and the cache became fully cached. |
| Full-paper, theorem, figure, table, and code review | 35 min | about 34 min | complete | Full source representations, targeted visual pages, runtime appendix, and official code surface inspected. |
| Related DEP synthesis | 10 min | about 9 min | complete | Exactly three conceptually overlapping deposits inspected. |
| Artifact drafting and validation | 30 min | about 27 min | complete | Five new artifacts plus two public index updates prepared and validated. |
| Allowlist, submission, and Slack notification | 15 min | about 11 min | complete | Seven-file allowlist passed; the rebased commit reached the default branch and Slack delivery succeeded. |

## Source-Integrity Metrics

| Check | Result |
|---|---|
| Initial classification | partial |
| Final classification | complete |
| PDF size / header / EOF | 3,294,807 bytes / pass / pass |
| Full HTML size | 497,212 bytes |
| HTML body characters | 95,618 |
| Document marker | pass |
| Heading markers | 79 |
| Structure terms | 8 |
| Source archive entries | 78 |
| Partial artifacts | 0 |
| Repair outcome | official arXiv full-paper HTML and source package verified; local provenance records refreshed |

## Cache and Extractor Status

- Preflight fallback order: `pdftotext`, `fitz`, `pypdf`, `PyPDF2`, `pdfminer`, HTML, source package.
- Available PDF fallback: `pypdf`.
- Unavailable preferred tool: `pdftotext`.
- Cache lookup: miss.
- Backfill: successful.
- Final cache state: cached.
- Extractors: `pypdf` for PDF text, HTML regex extraction for full-paper HTML, and `tarfile` for the source package.
- Extracted text sizes: PDF 82,660 bytes; HTML 95,313 bytes; source package 209,706 bytes.
- Extractor fallback: `pypdf` used because `pdftotext` was unavailable.
- Network during cache extraction: none.

## Dedup Index Status

The first draw passed public-index, repository-artifact, automation-memory, active-recent-branch, and companion-data checks. One metadata-only companion inventory row was not treated as a prior deposit. Duplicate exclusions and reselections were zero. The new pointer contains the complete artifact path set, public source URLs, deposited status, and primary commit reference.

## Expected-vs-Observed Trajectory

Selection, deduplication, repair, and extraction completed below their combined estimate because the first draw was eligible and official arXiv full-paper HTML succeeded on the bounded repair pass. Review time was intentionally spent on the theorem proof, complete result table, convergence plots, runtime appendix, official code surface, and exactly three related deposits. The source-first review was not truncated when the theorem gap and runtime evidence required deeper checking. Total observed work was about 106 minutes, within the 90-120 minute whole-job guidance.

## Shortfalls

1. `pdftotext` was unavailable; the successful `pypdf` fallback supplied PDF text.
2. The displayed theorem proof does not establish that SNI iterates are Cauchy: its final upper bound retains a fixed `2c'` term.
3. No experiment was rerun, and the observed official code head postdates the paper without an inspected tagged paper release or end-to-end reproduction record.

## Public-Output Gate

The staged allowlist contained exactly seven public files: five generated Markdown artifacts, the DEP-E publication index, and the required derived dedup JSON. PDF, HTML, metadata HTML, source archives, extracted text, caches, integrity records, repair bundles, and temporary page renders remained outside the staged set. Staged-name, public-safety, JSON, schema, exact-count, and whitespace checks passed before push; the direct default-branch push and Slack notification succeeded.
