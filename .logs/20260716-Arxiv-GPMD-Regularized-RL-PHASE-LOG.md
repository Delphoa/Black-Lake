# Arxiv DEP Phase Log: GPMD Regularized RL

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:2105.11066v4; publisher DOI 10.1137/21M1456789
- Selection: first draw, index 8,809 of 75,776 units; dedup clear
- Source: `partial` repaired to verified `complete` with approved ar5iv HTML
- Cache: miss to `cached`; sources and extracted text withheld
- Dedup pointer: deposited with primary commit reference

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Draw and dedup | 8 min | about 3 min | Complete | 75,777 PDFs; 75,776 units; first draw |
| Source classification | 3 min | under 1 min | Complete | Valid PDF; full-paper HTML absent |
| Repair and verification | 15 min | about 7 min | Complete | Official HTML unavailable; ar5iv fallback and metadata; four local records; zero partials |
| Missing-only extraction | 5 min | about 1.5 s | Complete | `pypdf` / `html-regex`; no source package |
| Full-paper review | 25 min | about 20 min | Complete | Algorithm, Theorems 1-2, proofs, experiments, discussion, limitations |
| Publisher/code check | 8 min | about 4 min | Complete | SIAM record verified; focused GitHub search found no official implementation |
| Related synthesis | 10 min | about 5 min | Complete | Exactly three inspected entries across both repositories |
| Artifact generation | 20 min | about 15 min | Complete | Seven allowlisted artifacts drafted |
| Validation/source gate | 10 min | about 4 min | Complete | Schema, exact counts, public safety, and seven-file staged allowlist passed |
| Repository and Slack | 10 min | about 4 min | Complete | Non-overlapping remote DEP-A batch preserved by rebase; direct push and Slack notification succeeded |

## Cache and Integrity Metrics

| Field | Value |
|---|---|
| PDF | 992,721 bytes; header/EOF pass |
| Full HTML | 5,461,972 bytes; 267,300 body chars; two document markers; 86 headings; six terms |
| Metadata / partials | 45,526 bytes metadata only / 0 |
| Initial/final cache | Miss / `cached` |
| Extractors | `pypdf` / `html-regex` / none |
| PDF/HTML/source text | 107,685 / 267,835 / 0 bytes |

## Dedup Index Update

- Matches, exclusions, reselections: 0 / 0 / 0
- Pointer: arXiv:2105.11066v4; slug `GPMD-Regularized-RL`
- Commit/status: https://github.com/Delphoa/Black-Lake/commit/0bf2bd70e4854638cec0c338bb3f5d23858addd4 / deposited

## Expected vs Observed Trajectory

The older paper required the approved HTML fallback, but the large rendering passed immediately and extraction stayed well below estimate. The review capacity was used to separate value/Q convergence from policy convergence, iteration complexity from sample/runtime cost, and mathematical regularization from operational safety.

The whole-job timebox did not truncate the source-first review. No source payload entered artifact generation.

## Shortfalls and Follow-Up

- No proof checking, implementation, rollout experiment, real benchmark, or independent sample-complexity derivation.
- Publisher record confirms publication, but no official code was identified.
- Public allowlist, submission, and Slack delivery completed.
