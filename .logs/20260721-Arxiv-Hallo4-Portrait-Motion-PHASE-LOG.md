# Arxiv DEP Phase Log: Hallo4 Portrait Motion

## Public-Safe Run Summary

- Deposit date: 2026-07-21.
- Paper: arXiv:2505.23525v4, *Hallo4: High-Fidelity Dynamic Portrait Animation via Direct Preference Optimization*.
- Run state: artifacts deposited; primary remote verification and Slack notification completed.
- Public-safety rule: only elapsed durations, date-only markers, repository-relative paths, public URLs, counts, and extractor statuses are recorded.

## Phase Metrics

| Phase | Expected | Observed | Result |
|---|---:|---:|---|
| Contract, memory, and repository authority review | 8 min | 9 min | Required skill contracts and both live repository READMEs inspected. |
| Candidate enumeration and uniform draw | 4 min | 1 min | 75,779 PDFs collapsed to 75,776 parent-paper units; index 11,355 selected. |
| Dedup and eligibility validation | 6 min | 2 min | First draw accepted; exclusions 0; reselections 0. |
| Source integrity classification and repair | 15 min | 7 min | Partial unit repaired to complete; PDF/HTML gate passed; zero partials. |
| Extractor preflight and cache extraction | 5 min | 0.9 sec | Preflight 0.284 sec; extraction 0.643 sec; final status `cached`. |
| Full-paper, table, figure, and code review | 35 min | 24 min | PDF/HTML/TeX, nine tables, selected figures, and official repository inspected. |
| Exactly-three related DEP synthesis | 10 min | 6 min | OViP Preference, VideoWeave Geometry, and AR-Drag Motion selected. |
| Artifact drafting and schema validation | 30 min | 11 min | Manuscript, Report-Mark, DEP README, logs, and indexes passed structural, safety, JSON, code, and diff checks. |
| Submission, remote verification, and notification | 15 min | 6 min | Public-output allowlist passed; primary commit pushed and remotely verified; Slack delivered; completion record prepared. |

## Extraction Cache

- Initial cache lookup: miss.
- Refresh mode: `missing-only`.
- Final cache state: `cached`.
- PDF extractor: `pypdf`, status `ok`, 53,699 text bytes.
- PDF fallback: `pdftotext` unavailable; `pypdf` succeeded.
- HTML extractor: `html-regex`, status `ok`, 46,819 text bytes.
- Source extractor: `tarfile`, status `ok`, 193,139 text bytes.
- Cache network use: none; extraction used the repaired local paper unit.
- Private cache manifests, paths, extracted text, and source files are not public artifacts.

## Source Integrity Gate

- Initial classification: `partial` - valid full PDF, missing full-paper HTML.
- Repair strategy: bounded direct HTTPS retrieval through the archive workflow; one strategy owned the target; no credentials; low retry ceiling; explicit target and partial ceilings.
- Final PDF: pass at 10,418,972 bytes with header and EOF checks.
- Final full-paper HTML: pass at 151,929 bytes, 46,119 body characters, 39 headings/sections, seven structure terms, and a document marker.
- Metadata HTML: present, explicitly classified as metadata only.
- Source package: valid archive with 19 entries.
- Unexpected partials: zero.
- Verification status: complete before synthesis.
- Upload policy: all source documents and source-derived files withheld locally; no `.source/` directory.

## Dedup Index Update

- Selected-paper checks: arXiv ID, arXiv DOI, normalized title, slug, output patterns, memory, relevant Black-Lake-Data content, and preceding-24-hour worktree markers.
- Author-inventory hits: two metadata-only rows; not exclusionary.
- Research-deposit hits: zero.
- Reselections: zero.
- Pointer state: `deposited`; schema-valid unique entry includes the remotely verified primary commit URL.

## Expected vs Observed Trajectory

The integrity/cache phases completed faster than their estimates because the existing PDF was valid, official full-paper HTML was available on the first bounded repair cycle, and all three local extractors succeeded. Review was not truncated: methods, metrics, Tables 1-9, selected qualitative/ablation figures, limitations, source text, official code metadata, and exactly three related deposits were inspected. The whole job completed in about 66 minutes, below the 90-120 minute guidance; the shorter trajectory reflects source availability rather than reduced review scope.

## Shortfalls and Follow-Up

- No training, inference, metric recomputation, checkpoint download, or dataset inspection was performed.
- No multi-seed uncertainty, confidence intervals, annotation agreement, or independent user study was available from inspected sources.
- Repo-level license clarity, portable dependency installation, checkpoint naming, training/evaluation scripts, and author-name reconciliation remain unresolved.
- Validation and direct primary submission passed; the completion-record commit carries the final log and dedup-pointer state.
