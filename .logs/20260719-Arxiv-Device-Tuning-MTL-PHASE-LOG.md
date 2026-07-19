# Arxiv DEP Phase Log - Device Tuning MTL

## Public-Safe Run Summary

- Deposit date: 2026-07-19.
- Selected paper: *Device Tuning for Multi-Task Large Model*.
- Identifier: `arXiv:2302.10820v1`; DOI `10.48550/arXiv.2302.10820`.
- Random draw: Uniform PowerShell `Get-Random` zero-based index 74,319 from 75,776 unique PDF-parent paper units.
- Exclusions/reselections: 0/0.
- Source state: Initial `partial`; repaired and verified `complete` before synthesis.
- Cache state: Initial miss; `missing-only` local extraction finished `cached`.
- Dedup state: Clear across public pointer, logs, reports, DEPs, automation memory, companion repository, and active-worktree 24-hour markers.
- Source policy: PDF, HTML, metadata, TeX/source, cache, extracted text, and integrity records remained local and were not uploaded; temporary review renderings were removed after inspection.

## Phase Metrics

Durations are rounded elapsed observations; estimates guide trajectory review rather than truncate source-first work.

| Phase | Expected | Observed | Status | Evidence |
|---|---:|---:|---|---|
| Contract, memory, live repository authorities, and extractor preflight | 8 min | about 10 min | Complete | Required skill contracts and both repository READMEs inspected; live Black Lake filing rules confirmed |
| Candidate enumeration and dedup validation | 5 min | about 4 min | Complete | 75,778 PDFs / 75,776 units; first draw accepted; exact ID/title/DOI/slug and recent-marker checks clear |
| Source integrity classification and bounded repair | 12 min | about 10 min | Complete | Existing PDF preserved; metadata, approved ar5iv full paper, and 10-entry source archive collected; strict gate passed |
| Extraction cache lookup and missing-only backfill | 3 min | under 1 min | Complete | Initial miss; extraction command 0.352 seconds; PDF/HTML/source text present |
| Source, equation, table, figure, workshop, successor, and code review | 25 min | about 18 min | Complete | Four-page paper fully screened; all pages visually inspected; official workshop/successor records and code availability checked |
| Related DEP exploration and exact-three synthesis | 8 min | about 4 min | Complete | Edge Cloud Split, K Token Merging, and DMNN Conditional Paths inspected |
| Public artifact drafting, publication index, and dedup preparation | 30 min | about 24 min | Complete | Logs, Report-Mark, schema-complete manuscript, DEP README, publication row, and pointer prepared |
| Validation, staged allowlist, commit/push, notification, and final record | 15 min | Pending final record | In progress | Repository and notification results are filled after verification |

## Extraction Cache

- Preflight fallback order: `pdftotext`, `fitz`, `pypdf`, `PyPDF2`, `pdfminer.six`, HTML, source package.
- Available PDF backend: `pypdf`.
- Initial lookup: Miss for the versioned identifier.
- Mode: `missing-only`; network disabled during extraction because source repair had already produced a complete local unit.
- PDF extractor: `pypdf`, status `ok`, 17,777 text bytes.
- PDF fallback: `pdftotext` unavailable.
- HTML extractor: `html-regex`, status `ok`, 19,172 text bytes.
- Source extractor: `tarfile`, status `ok`, 35,052 text bytes.
- Final cache status: `cached`.
- Cache public-safety validation: One summary checked, zero findings.

## Source Integrity and Repair

- Initial unit: Valid PDF plus brief metadata README, but no full-paper HTML; classified `partial`.
- Transfer preflight: Public unauthenticated endpoints; one active strategy/owner; 32 MB total ceiling; 16 MB partial ceiling; two-attempt cap; no credential use or automatic restart; free-space floor passed.
- Existing PDF: 290,141 bytes; header and trailing EOF passed; preserved without redownload.
- Official arXiv HTML: Unavailable for this paper during the bounded check.
- Approved ar5iv full-paper HTML: 77,672 bytes; 18,911 body characters; document markers; 30 headings/sections; five structure terms.
- Metadata HTML: 40,205 bytes; metadata-only.
- TeX/source: 4,510,675 bytes; valid archive listing with 10 entries.
- Partial state: Zero partial files and zero partial bytes.
- Local archive records refreshed: README, attribution/provenance, preflight manifest, machine-readable summary, and verification report.
- Final verification: `complete`; synthesis began only after this pass.

## Dedup Index Update

- Keys checked: arXiv version/base ID, arXiv DOI, normalized title, slug, and public artifact paths.
- Scan basis: Black Lake public pointer/log/report/DEP records; automation memory; Black-Lake-Data substantive artifacts; active worktrees; and a public-safe 24-hour cutoff.
- Exact companion-repository ID/title matches: 0.
- Generic companion-repository term hits: Metadata-only inventory pages; not deposits and not same-paper matches.
- Duplicate artifact matches: 0.
- Reselections: 0.
- Public pointer action: Add one unique entry with five artifact paths, public source URLs, source-repair/cache notes, and submission status.
- Commit/PR reference: Pending remote verification.

## Expected vs Observed Trajectory

- Contract loading exceeded a minimal preflight because the required source-processing, manuscript, download-safety, archive, DEP, and PDF contracts were read and both live repository authorities were verified before mutation.
- Source repair remained bounded: the valid PDF was preserved, the unavailable official HTML endpoint was not retried blindly, and the approved ar5iv fallback passed the full-paper structure gate on its first transfer.
- Cache extraction substantially beat its estimate because the repaired unit supplied compatible PDF, HTML, and tar sources to all three local extractors.
- Full review finished within estimate because the paper is four pages, but it still included complete text/source inspection, visual inspection of every page, two tables, two figures, equations, references, official workshop context, successor context, and a focused code search.
- The review did not smooth over missing evidence: multi-task behavior, gradient normalization, training settings, and device/cloud system costs remain explicit gaps.
- Final submission work remains open only until validation, the staged source-upload gate, remote verification, and Slack read-back complete.

## Submission and Notification

- Repository status: Pending verified submission.
- Primary artifact commit/PR: Pending.
- Slack status: Pending notification to `#black-lake-artifacts` after repository submission.
- Source-upload gate: Must pass before any commit; no source file, cache, extracted text, review rendering, or `.source/` directory is allowed.

## Shortfalls and Follow-Up

- No official implementation, configuration, checkpoint, dataset manifest, or environment was found; no experiment was reproduced.
- The paper does not specify the pooling operator beyond sequence reduction, the device/cloud transport representation, the split location, or the claimed gradient-normalization procedure.
- ImageNet-1k is the only reported benchmark; no multi-task task list, per-task results, transfer results, or task-interference analysis is present.
- No training recipe, data augmentation, image resolution, optimizer, schedule, epochs, batch size, pretraining source, seed count, or uncertainty is disclosed.
- No FLOP, latency, throughput, memory, energy, bandwidth, serialized-byte, privacy, outage, or tail-behavior measurement is reported.
- Table 2 compares widely different parameter counts, so it is not a clean matched-budget efficiency frontier.
- PDF rendering emitted nonfatal font warnings, but the two figures, equations, and two tables remained legible.
