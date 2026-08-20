# Arxiv DEP Phase Log

## Public-Safe Run Summary

- Paper: arXiv:2603.15690v1, *Loosely-Structured Software: Engineering Context, Structure, and Evolution Entropy in Runtime-Rewired Multi-Agent Systems*.
- Selection: uniform zero-based PowerShell `Get-Random` draw `71,465` from `75,964` parent-paper units; first draw accepted.
- Source gate: initial partial unit repaired to a verified complete PDF/full-paper HTML pair before review.
- Public-safe submission scope: generated Markdown logs, Report-Mark, DEP README/manuscript, and the required dedup/status JSON only.
- Source policy: source files, extracted text, cache records, provenance records, and renders were retained locally and withheld from the public repository.

## Phase Metrics

| Phase | Expected duration | Observed duration | Result |
|---|---:|---:|---|
| Candidate enumeration and random selection | 30–180 seconds | about 8 seconds | Completed; 75,964 parent-paper units |
| Dedup and reselection validation | 30–180 seconds | about 6 seconds | Completed; zero exclusions and reselections |
| Source integrity validation and repair | 60–300 seconds | about 18 seconds | Completed; one bounded repair, final gate passed |
| Extractor preflight and cache extraction | 15–120 seconds | about 3 seconds | Completed in `missing-only` mode |
| Source review and evidence ledger | 180–900 seconds | rounded operational estimate: about 420 seconds | Completed from local full-text cache plus public arXiv records |
| Related DEP exploration | 60–300 seconds | rounded operational estimate: about 120 seconds | Completed; exactly three related entries selected |
| Synthesis, validation, and submission preparation | 180–600 seconds | measured during artifact generation and checks | Completed; public-safe artifacts validated and no source files in scope |

Durations are elapsed or rounded operational measurements; public artifacts intentionally omit exact local execution timestamps and timezone labels.

## Extraction Cache

- Initial cache lookup: miss for the selected paper.
- Mode: `missing-only`, local-first, central archive cache.
- Final status: `cached`.
- PDF extractor: `pypdf`, successful; fallback reason `pdftotext unavailable`.
- HTML extractor: `html-regex`, successful.
- Source extractor: not run because the source package was unavailable.
- Cached text outputs: PDF text present (`98,815` bytes); HTML text present (`99,588` bytes); source text absent.
- Network backfill: used only for the mandatory source-integrity repair, not for cache extraction.

## Dedup Index Update

- Pre-write lookup: no matching ID, DOI, normalized title, slug, artifact path, memory marker, Black-Lake-Data search result, or 24-hour marker.
- Entry fields: arXiv ID, arXiv-issued DOI, normalized title, slug, public artifact paths, source URLs, deposit date, status, and source-withheld notes.
- Update status: generated entry pending final commit reference; commit/PR field will be populated after remote submission.

## Expected vs Observed Trajectory

- Expected: select one unseen paper, repair and verify source locality, cache reusable text, review primary evidence, synthesize one DEP-E deposit, validate public safety, and submit an atomic public-safe change.
- Observed: the first uniform draw was eligible; the missing full-paper HTML was repaired once; the cache reached `cached`; no official code repository was identified; review evidence was sufficient for a bounded conceptual and empirical report.
- Trajectory shortfall: review and related-exploration durations were rounded estimates rather than separately instrumented phase timers.

## Shortfalls and Follow-Up

- No independent code, dataset, or benchmark reproduction was performed.
- No official implementation repository was found from the arXiv record or GitHub repository search.
- RepoBench-R results are source-reported and depend on the stated model/API, candidate pool, and prompt budgets.
- The comprehensive workflow uses subjective reviewer scoring, an intentionally limited experiment-agent pass, and human control points; it is not a standardized end-to-end benchmark.
- The source package was unavailable, so no source text entered the cache.
