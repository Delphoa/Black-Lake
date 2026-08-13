# Arxiv DEP Phase Log

## Public-Safe Run Summary

- Run date: 2026-08-06
- Paper: arXiv:2205.12956v2, *Inception Transformer*.
- Selection: 75,957 parent-paper units; uniform PowerShell `Get-Random` zero-based draw 74,770; first draw accepted.
- Source state: initially partial; repaired to complete before review. Final PDF and full-paper HTML passed validation. Source package unavailable and withheld locally.
- Public-output policy: only derived Markdown/JSON records are eligible for staging; local source files, caches, extracted text, and repair evidence remain private.

## Phase Metrics

| Phase | Expected duration | Observed duration | Result |
|---|---:|---:|---|
| Candidate enumeration and draw | under 5 minutes | about 2 seconds | 75,960 PDFs; 75,957 units; draw accepted |
| Dedup and reselection checks | under 10 minutes | about 5 seconds | ID/DOI/title/slug checks clear; reselections 0 |
| Source integrity repair | under 20 minutes | about 13 seconds | PDF preserved; full-paper HTML repaired via approved fallback |
| Extractor preflight | under 2 minutes | under 1 second | `pypdf` available; `pdftotext` unavailable |
| Missing-only cache extraction | under 5 minutes | under 1 second | `cached`; PDF and HTML text present; source text absent |
| Source-first review and related exploration | 45–75 minutes | not separately instrumented | Full paper, official code surface, and exactly three related DEPs inspected |
| Synthesis and validation | 15–30 minutes | not separately instrumented | Required headings/counts/public-safety checks performed |

## Extraction Cache

- Initial status: miss; no prior cache manifest was present for this paper.
- Mode: `missing-only`, local-first, after the source integrity gate.
- Final status: `cached`.
- Extractors: PDF `pypdf` status `ok`; HTML `html-regex` status `ok`; source `none` status `missing` because the TeX/source package was unavailable.
- Fallback reason: `pdftotext unavailable`; `pypdf` supplied PDF text.
- Public-safe cache summary: 56,686 bytes PDF text; 64,248 bytes HTML text; 0 bytes source text. Cache artifacts remain local.
- Network during extraction: none; public network was used only for the bounded source repair before extraction.

## Dedup Index Update

- Pre-write status: no matching public pointer for arXiv:2205.12956, DOI 10.48550/arXiv.2205.12956, normalized title, or slug.
- Scope checked: `.staging` dedup index; Black Lake `.logs`, `.reports`, and `.lake-data`; automation memory; relevant Black-Lake-Data entries.
- Final status: one unique deposited pointer added with repository-relative artifact paths and public source URLs.

## Expected vs Observed Trajectory

- Whole-job guidance: approximately 90–120 minutes for a complete source-first single-paper run.
- Observed trajectory: the instrumented acquisition/cache stages completed quickly; the end-to-end review and synthesis phases were not separately timed. No phase estimate caused source, table, figure, code-surface, related-DEP, or validation truncation.
- The initial missing HTML was repaired before synthesis, so this run did not rely on abstract-only evidence.

## Shortfalls and Follow-Up

- No official training, inference, benchmark rerun, checkpoint validation, or device profiling was performed.
- No valid TeX/source package was obtained; source-text extraction is therefore unavailable.
- Reproduction remains bounded by public dataset access, legacy dependency versions, multi-GPU cost, and missing run-level uncertainty/energy records.
- Manual review and final submission durations were not separately instrumented; this is recorded rather than inferred as a precise timestamp.

## Attribution Block

- Source URL: https://arxiv.org/abs/2205.12956
  - Applies to: phase metrics, paper identity, and public selection record.
  - Notes: Public metadata locator; source files withheld locally.
- Source URL: https://ar5iv.labs.arxiv.org/html/2205.12956
  - Applies to: full-paper HTML repair and method/results evidence.
  - Notes: Approved fallback used after official arXiv HTML returned 404.
- Source URL: https://doi.org/10.48550/arXiv.2205.12956
  - Applies to: stable identifier.
  - Notes: Public DOI locator.
