# Arxiv DEP Phase Log

## Public-Safe Run Summary

- Run date: `20260804`.
- Paper: CogPortrait, arXiv `2605.28056v1`.
- Source state: initial partial; repaired to verified complete PDF plus full-paper HTML before review.
- Final source status: complete; source package unavailable; source files withheld locally.
- Public-output scope: generated Markdown artifacts and the required derived dedup JSON only.

## Phase Metrics

| Phase | Expected duration | Observed elapsed | Outcome |
|---|---:|---:|---|
| Candidate enumeration and uniform draw | 5-10 minutes | 8.1 seconds | 75,957 parent-paper units; index 43,688 accepted |
| Dedup and source-state classification | 5-15 minutes | 2.0 seconds | No duplicate or recent marker; initial partial state recorded |
| Bounded source repair and verification | 10-30 minutes | 17.6 seconds | Official full-paper HTML saved and verified; no retry loop |
| Extractor preflight and missing-only cache | 1-5 minutes | 0.7 seconds | Cache created as `cached`; no extractor network backfill |
| Source-first paper review | 30-60 minutes | Not separately instrumented | Completed from PDF, full-paper HTML, metadata, and cache outputs |
| Related DEP exploration and synthesis | 10-20 minutes | Not separately instrumented | Three live repository manuscripts inspected and used |

## Extraction Cache

- Initial cache lookup: miss; the selected paper had no usable central cache record before extraction.
- Mode: `missing-only` against the selected local paper unit.
- Final status: `cached`.
- PDF extractor: `pypdf`, status `ok`; `pdftotext` unavailable, recorded as fallback reason.
- HTML extractor: `html-regex`, status `ok`.
- Source extractor: `none`, status `missing`; no local TeX/source package was available.
- Final text outputs: PDF text present, HTML text present, source text absent.
- Cache backfill: not applicable; this was a single-paper missing-only extraction rather than an archive-wide backfill.
- Network during extraction: none.

## Dedup Index Update

- Live Black-Lake dedup index fetched before writing.
- Exact arXiv ID, DOI, normalized title, slug, log, report, DEP, and relevant Black-Lake-Data searches returned no prior artifact.
- Reselection status: not required; first draw remained eligible.
- Final index action: add one `deposited` entry with repository-relative artifact paths and public source URLs.

## Expected vs Observed Trajectory

- Whole-job guidance: 90-120 minutes for a complete source-first review and public submission.
- Machine-controlled phases completed well below their expected envelopes because the official HTML transfer succeeded on the first bounded repair pass and local extraction was fast.
- Review and synthesis phases were not separately timed, but no source, method, result, related-entry, or safety review was truncated solely because an estimate was exceeded.

## Shortfalls and Follow-Up

- Source package acquisition was unavailable from the e-print route; no source-text cache could be produced.
- No official implementation, checkpoint, or reproducible runtime was located in the inspected source material.
- No model inference, video generation, metric recomputation, or user-study replication was performed.
- Review follow-up should prioritize benchmark release/licensing, rater protocol, seed variance, matched-component ablations, and consent-aware synthetic-media evaluation.
