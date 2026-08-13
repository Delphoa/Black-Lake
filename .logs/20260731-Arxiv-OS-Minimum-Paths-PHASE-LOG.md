# Arxiv DEP Phase Log: OS Minimum Paths

## Public-Safe Run Summary

- Paper: arXiv:2607.02883v1, *Paths and Intersections: Minimum Realization of Okamura-Seymour Instances*.
- Source state transition: partial to complete after one bounded repair attempt.
- Dedup index status before deposit: no matching pointer. Final pointer status: deposited.
- Timing uses rounded elapsed phase durations only; exact execution timestamps, local paths, and machine context are intentionally omitted.

## Phase Metrics

| Phase | Expected duration | Observed duration | Status | Notes |
|---|---:|---:|---|---|
| Candidate enumeration and dedup | 5-10 minutes | under 5 minutes | complete | 75,957 paper units; first uniform draw accepted; zero exclusions and reselections. |
| Source integrity and repair | 15-25 minutes | under 5 minutes | complete | Existing PDF passed; full-paper HTML and metadata were repaired and verified in one bounded attempt. |
| Missing-only cache extraction | 3-8 minutes | under 5 minutes | complete | PDF and HTML extraction succeeded; source package was unavailable. |
| Source-first review and related-entry selection | 35-50 minutes | about 35 minutes | complete | Primary PDF/HTML, arXiv metadata, related work, and exactly three related DEP entries were inspected. |
| Public artifacts and validation | 20-30 minutes | about 25 minutes | complete | DEP, Report-Mark, logs, publication index, dedup record, public-safety checks, and staged allowlist were reviewed. |
| Submission and notification | 5-10 minutes | under 10 minutes | complete | Direct repository submission and channel notification follow the validated public-only scope. |

## Extraction Cache

- Initial cache status: miss.
- Refresh mode: `missing-only`.
- Final cache status: `cached`.
- PDF extractor: `pypdf` succeeded; `pdftotext` was unavailable.
- HTML extractor: `html-regex` succeeded.
- Source extractor: unavailable because no local source package was available.
- Public-safe text-output summary: PDF text and HTML text are present; source text is absent.
- Repair/backfill status: the source unit was repaired before extraction; cache extraction itself used no network access.

## Dedup Index Update

- Checks covered arXiv ID, DOI, normalized title, slug, prior logs, reports, DEP-E records, the public dedup pointer, automation memory, and relevant Black-Lake-Data material.
- No matching prior Arxiv DEP artifact or same-paper 24-hour marker was found.
- The public pointer records repository-relative artifact paths and canonical public URLs only.

## Expected vs Observed Trajectory

Whole-job guidance is 90-120 minutes. The rounded observed trajectory is approximately 75 minutes. It is below the guidance because selection was accepted on the first draw, source repair completed in one bounded attempt, and the cache populated without retries. The source-first review was not intentionally shortened: the full-paper HTML and PDF were both reviewed, and theorem claims are qualified where no formal proof or runtime reproduction was performed.

## Shortfalls and Follow-Up

- No source package was available, so source-text extraction could not supplement PDF and HTML inspection.
- No author-linked implementation was identified in focused public discovery; no code, proof assistant artifact, or runtime experiment was executed.
- Formal verification of the cited lemmas, numerical robustness testing, and a reference implementation remain follow-up work.
- Source-upload gate: passed. Only generated public-safe Markdown records and the required dedup JSON are eligible for staging; all source documents and derivatives remain local.
