# Arxiv DEP Phase Log

## Public-Safe Run Summary

- Run date: `20260805`.
- Paper: Memory Shot for Long-Term Dialogue, arXiv `2606.28338v1`.
- Source state: initial partial; repaired to verified complete PDF plus full-paper HTML before review.
- Final source status: complete; source package unavailable; source files withheld locally.
- Public-output scope: generated Markdown artifacts, publication-index row, and the required derived dedup JSON only.

## Phase Metrics

| Phase | Expected duration | Observed elapsed | Outcome |
| --- | ---: | ---: | --- |
| Candidate enumeration and uniform draw | 5-10 minutes | 2.9 seconds | 75,957 parent-paper units; index 48,270 accepted |
| Dedup and source-state classification | 5-15 minutes | about 4 seconds | No duplicate or recent marker; initial partial state recorded |
| Bounded source repair and verification | 10-30 minutes | 17.8 seconds | Official full-paper HTML saved and verified; no retry loop |
| Extractor preflight and missing-only cache | 1-5 minutes | 0.9 seconds | Cache created as `cached`; no extractor network backfill |
| Source-first paper review | 30-60 minutes | Not separately instrumented | Completed from PDF, full-paper HTML, metadata, cache outputs, public arXiv HTML, and official code README/scripts |
| Related DEP exploration and synthesis | 10-20 minutes | Not separately instrumented | Three repository manuscripts inspected and used |
| Artifact drafting, validation, and submission | 20-40 minutes | Completed; submission commit `4875db7a` | Public-safe validator returned 0 findings; seven-file allowlist passed; commits pushed directly to `main`; Slack notification sent |

## Extraction Cache

- Initial cache lookup: miss; no usable central cache record existed for this paper before extraction.
- Mode: `missing-only` against the selected local paper unit.
- Final status: `cached`.
- PDF extractor: `pypdf`, status `ok`; `pdftotext` unavailable, recorded as fallback reason.
- HTML extractor: `html-regex`, status `ok`.
- Source extractor: `none`, status `missing`; no local TeX/source package was available.
- Final text outputs: PDF text present (89,744 bytes), HTML text present (71,302 bytes), source text absent.
- Cache backfill: not applicable; this was a single-paper missing-only extraction rather than an archive-wide backfill.
- Network during extraction: none.

## Dedup Index Update

- Live Black-Lake and Black-Lake-Data README context was fetched before writing.
- Exact arXiv ID, DOI, normalized title, slug, log, report, DEP, automation-memory, and relevant Black-Lake-Data searches returned no prior Arxiv DEP artifact.
- Reselection status: not required; first draw remained eligible.
- Final index action: add one `deposited` entry with repository-relative artifact paths and public source URLs.

## Expected vs Observed Trajectory

- Whole-job guidance: 90-120 minutes for a complete source-first review and public submission.
- Machine-controlled phases completed below their expected envelopes because one bounded repair pass succeeded and local extraction was fast.
- Review and synthesis phases were not separately timed, but no source, method, result, related-entry, or safety review was truncated solely because a phase estimate was exceeded.

## Submission and Notification

- Primary public commit: https://github.com/Delphoa/Black-Lake/commit/4875db7a03e1013f6e1e43345dfbd640f7e11bb0
- Final dedup-pointer and phase-log commit: https://github.com/Delphoa/Black-Lake/commit/c8028bcb
- Slack status: posted to `#black-lake-artifacts`; permalink: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1785911361970749

## Shortfalls and Follow-Up

- Source package acquisition was unavailable; no source-text cache could be produced.
- No experiment, model inference, benchmark rerun, metric recomputation, or visual-memory generation was performed.
- The official repository exposes script-based pipelines, hard-coded path assumptions, and Qwen3-VL/vLLM dependencies; no runnable environment or checkpoint was provisioned in this run.
- Follow-up should prioritize deletion/contradiction handling, privacy and accessibility controls for rendered memory, multi-seed matched-compute evaluation, judge calibration, and concurrent end-to-end serving measurements.
