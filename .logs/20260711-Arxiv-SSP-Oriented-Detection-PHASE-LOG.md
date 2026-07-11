# Arxiv DEP Phase Log: SSP Oriented Detection

## Public-Safe Run Summary

- `Deposit date`: 2026-07-11.
- `Paper`: arXiv:2506.10601v2, Semantic-decoupled Spatial Partition Guided Point-supervised Oriented Object Detection.
- `Selection`: One uniform zero-based random index, 29,914 of 75,438 paper units.
- `Dedup result`: No prior or same-paper 24-hour marker; 0 exclusions; 0 reselections.
- `Output class`: DEP-E research deposit plus operational logs and Report-Mark.

## Phase Metrics

| Phase | Expected duration | Observed duration | Status | Evidence / outcome |
|---|---:|---:|---|---|
| Governance and memory review | 5 minutes | 4.0 minutes | Complete | Prior run excluded; required skill and public-safety contracts loaded. |
| Candidate enumeration and draw | 5 minutes | 0.1 minutes | Complete | 75,438 PDF-backed paper units; index 29,914. |
| Identifier derivation and dedup | 10 minutes | 2.0 minutes | Complete | arXiv ID, DOI/title/slug scans across repositories, index, and memory; no matches. |
| Extractor preflight and cache | 10 minutes | 0.2 minutes | Complete with fallback | Initial miss; 0.11-second local pass; 3.92-second network backfill. |
| Primary paper and code review | 30 minutes | 8.0 minutes | Complete | Metadata, HTML, TeX source, method, tables, limitations, DOI, and official repo inspected. |
| Related DEP synthesis | 15 minutes | 3.0 minutes | Complete | Exactly three related entries inspected and bridged. |
| Artifact drafting | 30 minutes | 14.0 minutes | Complete | Job log, phase log, Report-Mark, README, and schema-complete manuscript produced. |
| Validation and dedup update | 10 minutes | 5.0 minutes | Complete | Heading/count/path/public-safety/JSON checks and dedup pointer update performed. |
| Commit, push, and notification | 10 minutes | 3.0 minutes | Complete | Atomic artifact commit pushed; Slack notification sent. |

`Whole-job guidance`: The expected trajectory was approximately 125 minutes. Observed phase work remained below that guidance without truncating the source-first review. Fast extraction and local repository search created most of the savings; evidence conflicts were still investigated rather than skipped.

## Extraction Cache

- `Initial cache status`: Miss.
- `Local missing-only result`: Metadata-only.
- `Local extractor result`: PDF failed because `pdftotext` and supported Python PDF modules were unavailable; local HTML and source package were absent.
- `Approved fallback`: Public arXiv HTML and e-print source.
- `Backfill result`: HTML extractor `html-regex` succeeded; source extractor `tarfile` succeeded.
- `Final cache status`: Cached.
- `Text outputs`: HTML text present (5,342 bytes); source text present (123,813 bytes); PDF text absent.
- `Fallback reason`: No local PDF text backend succeeded.
- `Source priority`: Local README/PDF presence first; public arXiv sources only for missing review text and metadata.

## Dedup Index Update

- `Pre-selection index status`: No arXiv:2506.10601 entry.
- `Artifact scans`: No matching arXiv ID, DOI, normalized title, or slug in Black Lake `.logs`, `.reports`, or `.lake-data`.
- `Automation memory`: No matching paper marker; the prior run paper was arXiv:2110.12359.
- `Related repository`: No matching code-search marker in Black-Lake-Data.
- `Same-paper window`: No marker within 24 hours.
- `Post-generation status`: Pointer added with repository-relative artifact paths, source URLs, deposit date, status, and notes.

## Expected vs Observed Trajectory

Selection and cache work were materially faster than their estimates because candidate enumeration used `rg`, the selected unit exposed a stable arXiv ID in its README, and the public source package extracted cleanly. Primary review also benefited from the TeX cache: methods, tables, ablations, and limitations could be inspected directly without OCR.

The evidence-quality path required extra judgment despite the short wall-clock extraction. DOTA-v1.0, DOTA-v1.5, DOTA-v2.0, and annotation-offset prose contain values that differ from nearby tables. The artifact preserves the table/repository values and records conflicts instead of collapsing them.

The drafting phase remained within guidance while retaining the full manuscript schema, exactly counted Synthesis Note elements, and source-level caveats. No phase estimate was used as a reason to truncate the review.

## Shortfalls and Follow-Up

- PDF text extraction remained unavailable; review used arXiv HTML and TeX-source fallback.
- Official code, datasets, pseudo-label archives, checkpoints, and numerical experiments were not executed or independently reproduced.
- Figures were assessed through source captions and surrounding text rather than a dedicated visual figure audit.
- Cross-dataset and offset discrepancies remain unresolved until the authors provide a table-to-config result manifest.
- No source files were collected for deposition because the review did not require redistribution and the manuscript source states a restrictive CC BY-NC-ND license.
