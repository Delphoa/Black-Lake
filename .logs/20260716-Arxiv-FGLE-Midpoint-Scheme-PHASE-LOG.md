# Arxiv DEP Phase Log: FGLE Midpoint Scheme

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:1601.02301v1
- Selection: first draw, index 47,945 of 75,776 units; dedup clear
- Source: `partial` repaired to verified `complete` with approved ar5iv HTML
- Cache: miss to `cached`; sources and extracted text withheld
- Dedup pointer: deposited with primary commit reference

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Draw and dedup | 8 min | about 3 min | Complete | 75,777 PDFs; 75,776 units; first draw; both repositories and memory clear |
| Source classification | 3 min | under 1 min | Complete | Valid PDF; full-paper HTML missing |
| Repair and verification | 15 min | about 7 min | Complete | Official HTML unavailable; ar5iv fallback and metadata; four records; zero partials |
| Missing-only extraction | 5 min | about 6.3 s | Complete | `pypdf` / `html-regex`; no source package |
| Full-paper review | 25 min | about 22 min | Complete | Scheme, lemmas, four theorems, iteration, two tables, six figures |
| Publisher/code check | 6 min | about 3 min | Complete | Elsevier/arXiv/focused search; no official code identified |
| Related synthesis | 10 min | about 5 min | Complete | Exactly three inspected Black Lake entries |
| Artifact generation | 20 min | about 17 min | Complete | Seven allowlisted artifacts drafted |
| Validation/source gate | 10 min | about 4 min | Complete | Schema, exact counts, public safety, and seven-file staged allowlist passed |
| Repository and Slack | 10 min | about 2 min | Complete | Direct push and Slack notification succeeded |

## Cache and Integrity Metrics

| Field | Value |
|---|---|
| PDF | 1,743,106 bytes; header/EOF pass |
| Full HTML | 2,651,436 bytes; 123,389 body chars; two document markers; 51 headings; six structure terms |
| Metadata / partials | 42,428 bytes metadata only / 0 |
| Initial/final cache | Miss / `cached` |
| Extractors | `pypdf` / `html-regex` / none |
| PDF/HTML/source text | 53,161 / 123,257 / 0 bytes |
| Fallback status | Official HTML unavailable; approved ar5iv full-paper rendering passed |

## Dedup Index Update

- Matches, exclusions, reselections: 0 / 0 / 0
- Pointer: arXiv:1601.02301v1; slug `FGLE-Midpoint-Scheme`
- Commit/status: https://github.com/Delphoa/Black-Lake/commit/0a939dfc7ad7c19d8ed0f1609c29a52648ab42c8 / deposited

## Expected vs Observed Trajectory

Official full-paper HTML was unavailable, but the bounded ar5iv fallback passed the integrity gate. Extraction completed close to the expected cache budget. Full-paper review required additional care because the headline “unconditional” convergence claim and the later uniqueness theorem use different step restrictions; the timebox was not used to collapse those properties.

The remaining review capacity was used to inspect the exact and self-referenced convergence tables, the nonlinear inner iteration, finite-domain truncation, and publisher/code availability. No source payload entered artifact generation.

## Shortfalls and Follow-Up

- No proof checking, code execution, independent solver, manufactured fractional test, domain sweep, or runtime/memory benchmark.
- Inner-iteration convergence and the operational uniqueness regime remain unverified.
- Public allowlist, submission, and Slack delivery completed.
