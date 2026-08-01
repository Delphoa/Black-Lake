# Arxiv DEP Phase Log

## Public-Safe Run Summary

- Paper: *SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning* (arXiv:2605.18299v1).
- Selection: uniform random draw over 75,957 unique PDF-parent units; first draw accepted.
- Source state: partial at selection, repaired to complete before review.
- Public source files uploaded: zero. Source files remain local only.

## Phase Metrics

| Phase | Expected duration | Observed duration | Status | Notes |
|---|---:|---:|---|---|
| Candidate enumeration and random draw | 5-15 minutes | 8.8 seconds | complete | 75,960 PDFs collapsed to 75,957 parent units. |
| Dedup and exclusion checks | 5-15 minutes | under 1 minute | complete | ID, DOI, title, slug, artifact, memory, and recent-marker checks passed. |
| Source integrity validation | 10-20 minutes | 1.1 seconds for final gate | complete | Initial partial state was repaired before synthesis. |
| Bounded source repair | 15-30 minutes | 4.6 seconds transfer command | complete | Public arXiv metadata/full HTML/source repair succeeded; zero partials. |
| Cache preflight and extraction | 2-10 minutes | 0.8 seconds | complete | Local-only extraction; no cache-network fetch. |
| Source-first review and related-entry synthesis | 30-60 minutes | not separately instrumented | complete | Full cached PDF/HTML/source text and three related DEP records inspected. |
| Artifact validation and submission | 15-30 minutes | command-level checks complete | complete | Public allowlist, schema, and JSON validation passed; remote submission follows the local log generation. |

## Extraction Cache

- Initial cache status: miss.
- Extraction mode: `missing-only` against the selected local paper unit.
- Final status: cached.
- Extractors: `pypdf` for PDF text, `html-regex` for full HTML text, and `tarfile` for source text.
- Fallback: `pdftotext` unavailable; `pypdf` succeeded.
- Cached text outputs: PDF 74,741 bytes; HTML 81,329 bytes; source 203,151 bytes.
- Cache backfill: local source repair supplied the missing full-paper HTML and source package before extraction; no network was used by extraction.

## Dedup Index Update

- Pre-write status: no matching public pointer entry, log, report, DEP-E artifact, automation-memory marker, or 24-hour marker.
- Reselection status: not required.
- Post-write status: one unique deposited entry for arXiv:2605.18299; commit reference is added after remote submission when known.

## Expected vs Observed Trajectory

- The source-first trajectory completed without truncating method, ablation, limitation, appendix, or related-DEP review.
- The integrity phase exceeded the initial no-repair expectation because the local unit was partial; the bounded repair completed successfully.
- The cache phase was faster than its estimate because all repaired source types were present locally and extractable.
- Whole-job guidance remains 90-120 minutes for future runs; this run's command-level metrics were shorter, while synthesis time was not separately instrumented.

## Shortfalls and Follow-Up

- No independent training, inference, benchmark rerun, or code execution was performed.
- No official implementation was identified in the inspected source bundle or focused public search.
- The cache manifest contains local paths by design and remains outside the public artifact set.
- The final staged allowlist must contain only the generated Markdown artifacts and the derived dedup JSON; source files, caches, extracted text, and repair records must remain unstaged.

## Attribution Block

- Source URL: https://arxiv.org/abs/2605.18299
  - Applies to: source identity and public metadata.
- Source URL: https://arxiv.org/html/2605.18299
  - Applies to: full-paper extraction and review evidence.
- Source URL: https://arxiv.org/pdf/2605.18299
  - Applies to: PDF integrity validation and PDF extraction.
- Source URL: https://arxiv.org/e-print/2605.18299
  - Applies to: source-package extraction and structure cross-checks.
