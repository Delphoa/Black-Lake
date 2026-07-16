# Arxiv DEP Phase Log: FGBench Chemistry

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:2508.01055v4
- Selection: first draw, index 29,946 of 75,776 units; dedup clear
- Source: `partial` repaired to verified `complete` with official HTML
- Cache: miss to `cached`; sources and molecular data withheld
- Dedup pointer: deposited with primary commit reference

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Draw and dedup | 8 min | about 3 min | Complete | 75,777 PDFs; 75,776 units; first draw |
| Source classification | 3 min | under 1 min | Complete | Valid PDF; HTML missing |
| Repair and verification | 15 min | about 6 min | Complete | Official v4 HTML/metadata; four local records; zero partials |
| Missing-only extraction | 5 min | 0.579 s | Complete | `pypdf` / `html-regex`; no source |
| Full-paper review | 25 min | about 18 min | Complete | Construction, task taxonomy, Tables 1-4, appendices, limitations |
| Repository/availability | 10 min | about 5 min | Complete | MIT repo README/tree and dataset locator inspected; nothing downloaded/run |
| Related synthesis | 10 min | about 4 min | Complete | Exactly three inspected entries |
| Artifact generation | 20 min | about 14 min | Complete | Seven artifacts drafted |
| Validation/source gate | 10 min | about 4 min | Complete | Schema, code, YAML, exact counts, public safety, seven-file allowlist passed |
| Repository and Slack | 10 min | about 2 min | Complete | Direct push and Slack notice succeeded |

## Cache and Integrity Metrics

| Field | Value |
|---|---|
| PDF | 5,996,608 bytes; header/EOF pass |
| Official HTML | 351,922 bytes; 65,713 body chars; document marker; 65 headings; six terms |
| Metadata / partials | 46,404 bytes metadata only / 0 |
| Initial/final cache | Miss / `cached` |
| Extractors | `pypdf` / `html-regex` / none |
| PDF/HTML/source text | 66,093 / 65,496 / 0 bytes |

## Dedup Index Update

- Matches, exclusions, reselections: 0 / 0 / 0
- Pointer: arXiv:2508.01055v4; slug `FGBench-Chemistry`
- Commit/status: https://github.com/Delphoa/Black-Lake/commit/d93ca6c28bb42a5910ce032f8709551b00ee0c30 / deposited

## Expected vs Observed Trajectory

Repair and extraction were faster than estimates. That capacity was used to distinguish molecular comparisons from template-expanded QA count, inspect per-task accuracy/validity/RMSE, reconcile the latest v4 metadata, and inventory the official repository rather than treating its availability badge as reproduction.

The scientific boundary remained explicit: molecular-property benchmark results are not evidence of safe molecule or drug design. Source, code, and molecular tables were not copied into Black Lake.

## Shortfalls and Follow-Up

- No reproduction, expert chemistry review, contamination audit, or independent split reconstruction.
- Dataset dependence, rare-group imbalance, numeric-scale comparability, stereochemistry, 3D context, and model contamination remain open.
- Public allowlist, submission, and Slack delivery completed.
