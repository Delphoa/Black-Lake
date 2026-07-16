# Arxiv DEP Phase Log: Noisy Poisson Inference

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:2301.00139v1
- Selection: first uniform draw, index 45,743 of 75,776 units
- Dedup: no prior research deposit
- Source integrity: `partial` repaired to verified `complete`
- Cache: miss to `cached`
- Source files: withheld locally; none uploaded
- Dedup index: validated deposited pointer records the primary artifact commit

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Authority, memory, and contracts | 6 min | reused from current batch | Complete | Required skills, schemas, automation memory, and live repository authority loaded |
| Candidate enumeration and draw | 3 min | about 3 s | Complete | 75,777 PDFs; 75,776 units; index 45,743 |
| Dedup validation | 5 min | about 2 min | Complete | Repository, public index, memory, active markers, and companion metadata checked |
| Source classification | 3 min | under 1 min | Complete | Valid PDF; full-paper HTML missing |
| Download preflight | 5 min | about 2 min | Complete | Transfer bounded; ample disk; zero partials or active owner |
| Bounded archive repair | 10 min | about 8 min | Complete | Official HTML unavailable; ar5iv redirect rejected; source and metadata fetched; local HTML derived from verified PDF |
| Integrity verification and records | 5 min | about 5 min | Complete | PDF/HTML/source checks and four local archive records passed |
| Missing-only extraction cache | 5 min | 2.322 s | Complete | `pypdf`, `html-regex`, and `tarfile`; status `cached` |
| Primary paper and code review | 25 min | about 20 min | Complete | Full PDF/HTML/TeX, tables, ADNI study, limitations, and declared code repository inspected |
| Related DEP synthesis | 10 min | about 5 min | Complete | PAC Confidence, Acoustic Phase Retrieval, and Joint Sensing MEC |
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
| PDF / HTML / source text | 175,819 / 170,805 / 348,082 bytes |

## Source Integrity Repair

| Check | Observed | Result |
|---|---:|---|
| PDF | 1,385,919 bytes; header and EOF valid | Pass; preserved |
| Full-paper HTML | 182,059 bytes; 170,802 body characters | Pass; locally rendered from verified PDF |
| Document marker / headings / structure terms | present / 79 / 8 | Pass |
| Metadata HTML | 42,317 bytes | Present; metadata only |
| Source package | 5,848,348 bytes; 105 entries | Pass |
| Partial files | 0 | Pass |
| Final classification | `complete` | Review gate opened |

The official arXiv HTML endpoint did not provide a full paper. The approved ar5iv attempts redirected to the arXiv abstract record; those bytes were preserved locally as metadata and never counted as full-paper HTML. A full-text HTML representation was then generated locally from every page of the already verified PDF and passed the structural gate. This derivative, the PDF, metadata, source package, caches, and extracted text remain local.

## Dedup Index Update

- Initial artifact matches: 0
- Metadata-only inventory matches: 1; not a DEP and not an exclusion
- Exclusions: 0
- Reselections: 0
- New pointer: arXiv:2301.00139v1; slug `Noisy-Poisson-Inference`
- Commit reference: https://github.com/Delphoa/Black-Lake/commit/c64863af639d21e309c873b06a60ad006d48f6ce
- Status: deposited pointer validated with primary commit attribution

## Expected vs Observed Trajectory

The first draw passed dedup but failed the initial complete-source gate because only a valid PDF and nearby metadata existed. The repair exceeded the simple download estimate because both public HTML routes failed as full-paper sources and required an explicit local PDF-to-HTML fallback plus a second validation pass. The extractor itself was much faster than estimated once the complete local unit existed.

Paper review required additional time to separate an asymptotic local-minimum theory from global optimization claims, trace the measurement-error correction through the loss and tests, and inspect the paper-linked repository. Phase estimates did not truncate the review.

## Shortfalls and Follow-Up

- No independent theorem check, implementation execution, or ADNI replication.
- Official full-paper HTML remained unavailable; the validated HTML is a local derivative of the PDF.
- The linked code does not visibly match the reported neuroimaging experiment and lacks an environment, README, and license.
- Overdispersion, covariance misspecification, dependent multiplicity, and external clinical validation remain open.
- Public allowlist passed with exactly seven Markdown/JSON artifacts and no source files; submission and Slack delivery completed.
