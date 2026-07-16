# Arxiv DEP Phase Log: DMNN Conditional Paths

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:1902.10949v3
- Selection: first draw, index 61,074 of 75,776 units; dedup clear
- Source: `partial` repaired to verified `complete` with approved ar5iv HTML
- Cache: miss to `cached`; sources and extracted text withheld
- Dedup pointer: deposited with primary commit reference

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Draw and dedup | 8 min | about 3 min | Complete | 75,777 PDFs; 75,776 units; first draw |
| Source classification | 3 min | under 1 min | Complete | Valid PDF; full-paper HTML missing |
| Repair and verification | 15 min | about 7 min | Complete | Official HTML 404; ar5iv fallback and metadata; four local records; zero partials |
| Missing-only extraction | 5 min | 0.864 s | Complete | `pypdf` / `html-regex`; no source package |
| Full-paper review | 25 min | about 18 min | Complete | Mechanism, losses, ImageNet/CIFAR tables, ablation, limitations |
| Code/availability check | 6 min | about 2 min | Complete | Focused paper/arXiv/GitHub check; no official code identified |
| Related synthesis | 10 min | about 4 min | Complete | Exactly three inspected Black Lake entries |
| Artifact generation | 20 min | about 14 min | Complete | Seven allowlisted artifacts drafted |
| Validation/source gate | 10 min | about 4 min | Complete | Schema, exact counts, public safety, and seven-file staged allowlist passed |
| Repository and Slack | 10 min | about 2 min | Complete | Direct push and Slack notification succeeded |

## Cache and Integrity Metrics

| Field | Value |
|---|---|
| PDF | 2,535,345 bytes; header/EOF pass |
| Full HTML | 404,027 bytes; 47,624 body chars; two document markers; 27 headings; five structure terms |
| Metadata / partials | 42,940 bytes metadata only / 0 |
| Initial/final cache | Miss / `cached` |
| Extractors | `pypdf` / `html-regex` / none |
| PDF/HTML/source text | 40,803 / 47,308 / 0 bytes |

## Dedup Index Update

- Matches, exclusions, reselections: 0 / 0 / 0
- Pointer: arXiv:1902.10949v3; slug `DMNN-Conditional-Paths`
- Commit/status: https://github.com/Delphoa/Black-Lake/commit/83242113499e2386f1b52acda4811ee240392ac2 / deposited

## Expected vs Observed Trajectory

The official HTML endpoint was unavailable, but the bounded ar5iv fallback passed the full-paper gate and extraction completed well below estimate. The remaining capacity was used to reconcile execution-rate numbers, distinguish FLOPs from realized device efficiency, inspect the controller ablation, and look for an official implementation.

The whole-job timebox did not truncate the source-first review. No source payload entered artifact generation.

## Shortfalls and Follow-Up

- No reproduction, device profiling, repeated seeds, routing traces, or independent hierarchy-transfer study.
- FLOP reductions remain unverified as latency, memory, energy, or cost savings.
- Public allowlist, submission, and Slack delivery completed.
