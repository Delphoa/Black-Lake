# Arxiv DEP Phase Log

## Public-Safe Run Summary

- Deposit date: 2026-07-10
- Selected paper slug: Self-Learned-IDC
- arXiv ID: 2110.12359
- Cache mode: local-first `missing-only`, followed by approved public arXiv backfill because local text extraction was missing.
- Repository scope: generated `.logs`, `.reports`, `.lake-data`, and `.staging/arxiv-dep-dedup-index.json` artifacts only.

## Phase Metrics

| Phase | Expected Duration | Observed Duration | Status | Notes |
|---|---:|---:|---|---|
| Skill and repository preflight | 2-4 minutes | about 3 minutes | complete | Required source-processing and manuscript contracts were read; upstream README state was fetched/read. |
| Extractor preflight | under 1 minute | under 1 second | complete with shortfall | Default Python environment lacked PDF extractors. |
| Candidate enumeration | 1-3 minutes | 3.6 seconds | complete | `rg --files -g "*.pdf"` found 75,438 paper units. |
| Random selection and local dedup | under 2 minutes | 3.8 seconds | complete | First random index was accepted; no local duplicate hit. |
| Cache lookup and local extraction | under 1 minute | 0.2 seconds | partial | Initial cache miss; local extraction produced metadata-only. |
| Public arXiv backfill | 1-3 minutes | 3.0 seconds | complete | HTML and source text were cached; PDF text remained unavailable. |
| Source review and related-entry synthesis | 20-45 minutes | about 30 minutes | complete | arXiv abstract, cached source text, local metadata, repository READMEs, code searches, and related DEP manuscripts were inspected. |
| Artifact generation and validation | 10-25 minutes | about 15 minutes | complete | Logs, Report-Mark, DEP README, manuscript, and dedup pointer were generated and sanitized. |
| Submission and notification | 3-10 minutes | pending at artifact-write time | pending | Commit/push and Slack notification are recorded after validation. |

## Extraction Cache

- Cache hit/miss/backfill: miss, then backfilled from public arXiv sources.
- Initial local extraction status: metadata-only.
- Final cache status: cached.
- HTML extractor: `html-regex`, status ok.
- Source extractor: `tarfile`, status ok.
- PDF extractor: unavailable/failed.
- Fallback reason: PDF text extractor unavailable; public arXiv HTML/source were used for reviewable text.
- Public-safe cache fields used: arXiv ID, title, source URLs, source counts, extractor statuses, text output presence, and cache status.

## Dedup Index Update

- Pre-run dedup index status: not present in the checked upstream state.
- Accepted arXiv ID: 2110.12359.
- DOI recorded: 10.48550/arXiv.2110.12359.
- Normalized title recorded: self-learned intelligence for integrated decision and control of automated vehicles at signalized intersections.
- Artifact paths recorded: log, phase log, Report-Mark, DEP directory, DEP manuscript.
- Status: staged for deposition during artifact generation; updated to deposited after commit/push.

## Expected vs Observed Trajectory

The extractor-acceleration layer helped after public backfill: once HTML/source were fetched, the source text was sufficient for method, simulation, result, and conclusion review. The main deviation was the unavailable PDF extractor, which made the first local-only cache pass metadata-only. The job stayed within the whole-job source-first timebox because the paper source package supplied the required technical detail after network backfill.

## Shortfalls and Follow-Up

- Local PDF text extraction remains unavailable in the default runtime; future runs should add `pdftotext`, `pypdf`, `PyPDF2`, `fitz`, or `pdfminer.six` to reduce network fallback.
- No official code repository was found; reproducibility remains blocked unless source authors publish implementation artifacts or a reviewer reconstructs a minimal SUMO/IDC setup.
- The paper reports simulation metrics, but this run did not reproduce training, controller rollout, MPC comparison, or traffic randomization.
- The final phase log intentionally omits local absolute paths, usernames, machine names, local timezone labels, and exact local execution timestamps.
