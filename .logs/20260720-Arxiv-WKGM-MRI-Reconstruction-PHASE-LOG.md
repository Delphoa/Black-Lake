# Arxiv DEP Phase Log - WKGM MRI Reconstruction

## Public-Safe Run Summary

- Deposit date: 2026-07-20.
- Selected paper: *WKGM: Weight-K-space Generative Model for Parallel Imaging Reconstruction*.
- Identifier: `arXiv:2205.03883v4`; DOI `10.1002/nbm.5005`.
- Random draw: Uniform PowerShell `Get-Random` zero-based index 53,793 from 75,776 unique PDF-parent paper units.
- Exclusions/reselections: 0/0.
- Source state: Initial `partial`; repaired and verified `complete` before synthesis.
- Cache state: Initial miss; `missing-only` local extraction finished `cached`.
- Dedup state: Clear across public pointer, logs, reports, DEPs, automation memory, companion repository, and active-worktree 24-hour markers.
- Source policy: PDF, HTML, metadata, invalid endpoint responses, cache, extracted text, integrity records, and temporary review renderings remained local and were not uploaded.

## Phase Metrics

Durations are rounded elapsed observations; estimates guide trajectory review rather than truncate source-first work.

| Phase | Expected | Observed | Status | Evidence |
|---|---:|---:|---|---|
| Contract, memory, live repository authorities, and extractor preflight | 8 min | about 15 min | Complete | Required skill contracts, automation memory, repository READMEs, filing rules, and extraction fallback inspected |
| Candidate enumeration and dedup validation | 5 min | about 3 min | Complete | 75,778 PDFs / 75,776 units; first draw accepted; exact ID/title/DOI/slug and recent-marker checks clear |
| Source integrity classification and bounded repair | 12 min | about 10 min | Complete | Existing PDF preserved; two abstract-only HTML responses rejected; PDF-derived full-text HTML passed; invalid e-print response preserved |
| Extraction cache lookup and missing-only backfill | 3 min | under 1 min | Complete | Initial miss; extraction command 2.458 seconds; PDF and HTML text present; source package unavailable |
| Source, equation, table, figure, publisher, and code review | 25 min | about 20 min | Complete | Full paper screened; six evidence-bearing pages rendered; journal record and official repository files inspected |
| Related DEP exploration and exact-three synthesis | 8 min | about 4 min | Complete | Hypercomplex MRI, Residual Gaussian CBCT, and Acoustic Phase Retrieval inspected |
| Public artifact drafting, publication index, and dedup preparation | 30 min | about 25 min | Complete | Logs, Report-Mark, schema-complete manuscript, DEP README, publication row, and pointer prepared |
| Validation, staged allowlist, commit/push, notification, and final record | 15 min | Pending | In progress | Final public-safety, schema, staged-set, remote, and Slack gates remain |

The source-first trajectory was not truncated when the repair path exceeded the nominal fast path. The official arXiv and ar5iv HTML responses were both rejected as abstract-only; the review began only after a provenance-labeled PDF-derived full-text rendering passed the complete-paper gate.

## Extraction Cache

- Preflight fallback order: `pdftotext`, `fitz`, `pypdf`, `PyPDF2`, `pdfminer.six`, HTML, source package.
- Available PDF backend: `pypdf`.
- Initial lookup: Miss for the versioned identifier.
- Mode: `missing-only`; network disabled during extraction because source repair had already produced a complete local unit.
- PDF extractor: `pypdf`, status `ok`, 62,576 text bytes.
- PDF fallback: `pdftotext` unavailable.
- HTML extractor: `html-regex`, status `ok`, 59,793 text bytes.
- Source extractor: `none`, status `missing`; the e-print response was a PDF rather than a readable source archive.
- Final cache status: `cached`.
- Cache action: Local missing-only backfill completed from the repaired unit; no network cache fetch was used.

## Source Integrity and Repair

- Initial unit: Valid PDF plus brief metadata README, but no full-paper HTML; classified `partial`.
- Transfer preflight: Public unauthenticated endpoints; one active strategy/owner; 100 MB total ceiling; 20 MB partial ceiling; one attempt per artifact; no credential use or automatic restart; free-space floor passed.
- Existing PDF: 1,884,860 bytes; 11 pages; header and trailing EOF passed; preserved without replacement.
- Official arXiv HTML: Returned the abstract/metadata page and was rejected because its hash matched metadata.
- Approved ar5iv fallback: Returned the same abstract/metadata page and was rejected because its hash matched metadata.
- Final full-text HTML: Locally derived page-by-page from the verified PDF; 62,379 bytes; 59,163 body characters; article/main marker; 23 heading/section markers; five structure terms; title present; hash distinct from metadata.
- Metadata HTML: 43,052 bytes; metadata-only.
- TeX/source: Unavailable. The e-print response began with `%PDF-` and was not a tar archive; it was classified and preserved locally as an invalid response.
- Partial state: Zero partial files and zero partial bytes after repair.
- Local archive records refreshed: README, attribution/provenance, preflight manifest, machine-readable summary, and verification report.
- Final verification: `complete`; synthesis began only after this pass.

## Dedup Index Update

- Keys checked: arXiv version/base ID, publisher DOI, arXiv DOI, normalized title, slug, and public artifact paths.
- Scan basis: Black Lake public pointer/log/report/DEP records; automation memory; Black-Lake-Data substantive artifacts; active worktree; and a public-safe 24-hour cutoff.
- Exact companion-repository ID/title matches: 0.
- Duplicate artifact matches: 0.
- Reselections: 0.
- Public pointer action: Add one unique entry with publication index, DEP, logs, report, public source URLs, repair/cache notes, and submission status.
- Commit/PR reference: Pending repository submission.

## Expected vs Observed Trajectory

- Contract loading exceeded the minimal estimate because the source-processing, manuscript, download-safety, archive, DEP, PDF, and Slack contracts were read before mutation, and both live repository authorities were checked.
- Candidate enumeration and dedup completed quickly because the first uniform draw was unique across all required keys and repositories.
- Source repair required two negative HTML determinations. The workflow rejected validator false positives instead of treating abstract-only content as a paper.
- Cache extraction substantially beat its estimate because the verified PDF and local full-text HTML were already available; `pypdf` and the HTML extractor completed locally.
- Full review stayed within its estimate while covering all equations, both algorithms, eight tables, thirteen figures/captions, visual renders, the journal record, and the official code surface.
- Related synthesis used three direct mechanism/evaluation bridges and excluded looser keyword-only matches.
- The review preserves counterevidence: SVD-WKGM is not uniformly superior, and the paper does not establish statistical, clinical, or systems-level deployment readiness.
- Final submission status will be recorded only after the exact staged allowlist, remote push, Slack delivery, and public pointer update are verified.

## Submission and Notification

- Repository status: Pending final validation and submission.
- Commit or PR: Pending.
- Slack status: Pending notification to `#black-lake-artifacts` after repository submission.
- Source-upload gate: Prepared to reject every PDF, HTML, metadata page, source response, cache file, extracted source text, integrity record, temporary rendering, local archive path, or `.source/` directory.

## Shortfalls and Follow-Up

- No result was reproduced; the code, datasets, checkpoint, and environment were not downloaded or executed.
- External evaluation appears slice- or image-level in several comparisons, and sample counts are not consistently exposed.
- No repeated seeds, confidence intervals, hypothesis tests, calibration curves, pathology-preservation analysis, or blinded reader study is reported.
- The 500 training images are described as coming from one healthy volunteer and are augmented to 4,000 single-coil images, limiting claims about subject-level diversity.
- PSNR and SSIM do not establish diagnostic non-inferiority or failure safety under scanner, coil, protocol, anatomy, pathology, or motion shift.
- The paper reports 1,000 predictor-corrector iterations and optional repeated singular-value decompositions but no latency, peak memory, energy, or cost evidence.
- SVD-WKGM combines weighting, high-dimensional augmentation, score modeling, data consistency, and SAKE, leaving attribution and matched-compute fairness incomplete.
- The official repository has runnable-looking entry points but no root dependency lock or license file; the README's non-commercial notice needs legal review before reuse.
