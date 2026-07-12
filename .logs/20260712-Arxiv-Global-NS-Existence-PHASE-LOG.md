# Arxiv DEP Phase Log: Global NS Existence

## Public-Safe Run Summary

- `Deposit date`: 2026-07-12.
- `Paper`: arXiv:2102.09229v2, Global Existence of Strong and Weak Solutions to 2D Compressible Navier-Stokes System in Bounded Domains with Large Data and Vacuum.
- `Selection`: One uniform zero-based random index, 17,885 of 75,761 PDF-backed paper units.
- `Dedup result`: No prior or same-paper 24-hour marker; 0 exclusions; 0 reselections.
- `Output class`: DEP-E research deposit plus operational logs and Report-Mark.

## Phase Metrics

| Phase | Expected duration | Observed duration | Status | Evidence / outcome |
|---|---:|---:|---|---|
| Governance and memory review | 5 minutes | 4.0 minutes | Complete | Prior runs excluded; required cache, manuscript, deposition, and public-safety contracts loaded. |
| Candidate enumeration and draw | 5 minutes | 0.1 minutes | Complete | 75,761 PDF-parent paper units; index 17,885. |
| Identifier derivation and dedup | 10 minutes | 0.3 minutes | Complete | ID, DOI, title, and slug scans across both repositories, index, and memory; no match. |
| Extractor preflight and cache | 10 minutes | 0.1 minutes | Complete with fallback | Initial miss; local `pypdf` extraction succeeded in 0.944 seconds. |
| Primary paper and publication review | 30 minutes | 12.0 minutes | Complete | Full PDF text, theorem/proof structure, arXiv metadata, and Springer record inspected. |
| Related DEP synthesis | 15 minutes | 4.0 minutes | Complete | Exactly three related entries inspected and bridged without treating them as proof evidence. |
| Artifact drafting | 30 minutes | 18.0 minutes | Complete | Job log, phase log, Report-Mark, README, and schema-complete manuscript produced. |
| Validation and dedup update | 10 minutes | 6.0 minutes | Complete | Heading, count, JSON, path, attribution-order, and public-safety checks performed. |
| Commit, push, and notification | 10 minutes | 3.0 minutes | Pending at draft time | Atomic artifact commit, push, and Slack post follow validation. |

`Whole-job guidance`: The expected trajectory was approximately 125 minutes. The observed trajectory remained below that guidance without truncating theorem, proof-mechanism, limitation, related-entry, or schema review. Durations are public-safe elapsed estimates rather than exact local timestamps.

## Extraction Cache

- `Initial cache status`: Miss; the cache files were first created on the date-only run marker.
- `Refresh mode`: `missing-only`.
- `Local extractor result`: PDF text succeeded through `pypdf`; `pdftotext` was unavailable.
- `Local source inventory`: One PDF and adjacent metadata README records.
- `Final cache status`: Partial, because PDF text is present while local HTML and source-package text are absent.
- `Text outputs`: PDF text present (72,259 bytes); HTML text absent; source text absent.
- `Fallback reason`: `pdftotext` unavailable, so the extractor used `pypdf`.
- `Network backfill`: Not used for paper-body extraction; public arXiv and publisher metadata pages were read separately for authoritative metadata.
- `Source priority`: Local PDF and adjacent metadata first, then public primary metadata records.

## Dedup Index Update

- `Pre-selection index status`: No arXiv:2102.09229 entry.
- `Artifact scans`: No matching arXiv ID, DOI, normalized title, or slug in Black Lake `.logs`, `.reports`, or `.lake-data`.
- `Automation memory`: No matching paper marker; the prior remembered papers were arXiv:2110.12359 and arXiv:2506.10601v2.
- `Related repository`: No matching repository-search marker in Black-Lake-Data.
- `Same-paper window`: No marker within 24 hours.
- `Post-generation status`: Pointer added with repository-relative artifact paths, source URLs, deposit date, status, and notes.

## Expected vs Observed Trajectory

Candidate enumeration and local extraction were materially faster than their estimates because `rg` found the archive units quickly, the nearby README exposed the arXiv ID, and `pypdf` was available. The saved time was used to inspect the paper's theorem statements, pull-back Green-function construction, boundary commutator estimate, density-bound closure, higher-order estimates, and final approximation arguments.

The paper has no experimental dataset, code, or numerical benchmark to reproduce. The appropriate evidence standard was therefore structural proof review: identify assumptions, theorem conclusions, key lemmas, parameter thresholds, and unverified steps. Existing DEP entries were used only for implementation and review-pattern synthesis.

The drafting phase retained every required manuscript heading, the exactly counted Synthesis Note elements, and explicit uncertainty about formal proof correctness. No phase estimate was used to shorten the review.

## Shortfalls and Follow-Up

- Mathematical symbol extraction contains encoding noise; theorem and equation references were checked contextually, but the artifact is not a formula-perfect transcription.
- The proof was not mechanically checked, independently refereed, or reproduced in a proof assistant.
- The source-identified regime `1 < beta <= 4/3` remains unresolved.
- No official code or formalization repository was identified from the inspected primary records.
- No source files were collected for deposition; the DEP uses public URLs and generated analysis only.
