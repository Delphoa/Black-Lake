# Arxiv DEP Phase Log: Adversarial Label Noise

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Paper: arXiv:2110.03135v4
- Selection: first draw, index 27,298 of 75,776 units; dedup clear
- Source: `partial` repaired to verified `complete` with official arXiv HTML
- Cache: miss to `cached`; sources and extracted text withheld
- Dedup pointer: prepared; primary commit reference pending

## Phase Metrics

| Phase | Expected | Observed | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Draw and dedup | 8 min | about 3 min | Complete | 75,777 PDFs; 75,776 units; first draw; both titles checked |
| Source classification | 3 min | under 1 min | Complete | Valid PDF; full-paper HTML missing |
| Repair and verification | 15 min | about 5 min | Complete | Official HTML and metadata; four records; zero partials |
| Missing-only extraction | 5 min | about 1.6 s | Complete | `pypdf` / `html-regex`; nonfatal image warning; no source package |
| Full-paper review | 25 min | about 20 min | Complete | Mechanism, theory, five result tables, limitations |
| Code/availability check | 6 min | about 3 min | Complete | Paper, proceedings, focused search; no official code identified |
| Related synthesis | 10 min | about 5 min | Complete | Exactly three inspected Black Lake entries |
| Artifact generation | 20 min | about 16 min | Complete | Seven allowlisted artifacts drafted |
| Validation/source gate | 10 min | about 4 min | Complete | Schema, exact counts, public safety, and seven-file staged allowlist passed |
| Repository and Slack | 10 min | pending | Pending | Direct push and Slack notification |

## Cache and Integrity Metrics

| Field | Value |
|---|---|
| PDF | 1,348,139 bytes; header/EOF pass |
| Full HTML | 2,396,107 bytes; 236,587 body chars; two document markers; 78 headings; seven structure terms |
| Metadata / partials | 43,194 bytes metadata only / 0 |
| Initial/final cache | Miss / `cached` |
| Extractors | `pypdf` / `html-regex` / none |
| PDF/HTML/source text | 89,772 / 236,019 / 0 bytes |
| Extractor shortfall | One image XForm decode warning; text outputs completed |

## Dedup Index Update

- Matches, exclusions, reselections: 0 / 0 / 0
- Pointer: arXiv:2110.03135v4; slug `Adversarial-Label-Noise`
- Commit/status: pending / prepared

## Expected vs Observed Trajectory

Official full-paper HTML repaired the initial partial unit without fallback. Extraction completed well below estimate despite one image-object warning; paper text remained available from both PDF and HTML cache products. Remaining review time was used to distinguish the existential total-variation results from operational calibration and to trace results across five tables.

The whole-job timebox did not truncate the source-first review. No source payload entered artifact generation.

## Shortfalls and Follow-Up

- No reproduction, repeated seeds, semantic annotation study, adaptive-attack audit, or independent calibration-transfer test.
- The extra teacher and validation workflow remain incompletely costed.
- Public allowlist validation completed; submission and Slack delivery remain to be completed.
