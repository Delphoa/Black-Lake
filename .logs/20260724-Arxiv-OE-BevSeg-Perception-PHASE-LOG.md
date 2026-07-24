# Arxiv DEP Phase Log: OE-BevSeg Perception

## Public-Safe Run Summary

- Deposit date: 2026-07-24.
- Paper: https://arxiv.org/abs/2407.13137.
- Workflow: uniform local selection, repository/memory dedup, complete-source gate, bounded archive repair, missing-only cache extraction, full-paper/code/related-DEP review, schema-complete artifact generation, public-safety validation, allowlisted submission, and notification.
- Source policy: all PDF, HTML, metadata, TeX/source, cache, extracted text, integrity records, and temporary renders were withheld locally.
- Timing policy: observed durations are rounded public-safe phase measurements; the extractor duration is taken from its machine-readable manifest. Exact execution timestamps and local timezone details are intentionally omitted.

## Phase Metrics

| Phase | Expected Duration | Observed Duration | Status | Evidence / Notes |
|---|---:|---:|---|---|
| Contract, memory, authority, and extractor preflight | 5-10 min | 6.4 min | Complete | Required skill contracts, automation memory, live repository README, filing rules, and extractor capabilities inspected |
| Candidate enumeration, random draw, identity, and dedup | 5-10 min | 7.1 min | Complete | 75,780 PDFs collapsed to 75,777 units; index 20,731; first draw; zero exclusions/reselections |
| Source-integrity classification, bounded repair, and final verification | 10-20 min | 11.8 min | Complete | Initial `partial`; final PDF/full-paper-HTML/source bundle `complete`; zero partial files |
| Missing-only extraction cache | under 2 min | 0.366 sec | Complete | Initial miss to `cached`; PDF/HTML/source text all present |
| Full-paper, table, figure, publisher, and official-code review | 30-45 min | 34.2 min | Complete | Full 14-page paper, source tables, rendered key pages, IEEE metadata, and pinned repository surface inspected |
| Related DEP exploration and exactly-three selection | 10-15 min | 9.6 min | Complete | HERMES World Model, Stable Diffusion Depth, and iKalibr Calibration selected for concrete overlap |
| Manuscript, Report-Mark, DEP README, job log, and index authoring | 30-45 min | 34.8 min | Complete | Schema-complete manuscript and exact-count Report-Mark synthesis drafted |
| Structural, syntax, link, public-safety, and source-upload gates | 15-25 min | Pending final measurement | In progress | Final validation and staged allowlist inspection occur before push |
| Repository submission and remote verification | 10-20 min | Pending final measurement | Pending | Primary commit URL will be recorded after remote verification |
| Slack notification | under 5 min | Pending final measurement | Pending | Notification follows successful repository submission |

## Extraction Cache

- Initial cache lookup: miss.
- Extraction mode: `missing-only`.
- Final cache status: `cached`.
- PDF extractor: `pypdf`, status `ok`.
- PDF fallback reason: `pdftotext` unavailable.
- HTML extractor: HTML extraction, status `ok`.
- Source extractor: `tarfile`, status `ok`.
- PDF text: 57,733 bytes.
- HTML text: 93,976 bytes.
- Source text: 97,727 bytes.
- Network use during extraction: none.
- Cache shortfall: preferred `pdftotext` backend was unavailable; the successful `pypdf` output was used and cross-checked against HTML/source text and rendered pages.

## Source-Integrity Gate

- Initial classification: `partial`.
- Blocking gap: full-paper HTML missing.
- Repair strategy: one bounded official arXiv companion-bundle attempt with conservative target and partial ceilings; existing valid PDF preserved.
- Repair retries: 0.
- Final classification: `complete`.
- PDF: 8,611,139 bytes; valid header and trailing EOF; 14 pages.
- Full-paper HTML: 698,205 bytes; 102,901 body characters; document marker present; five heading/section markers; five paper-structure terms; distinct from metadata HTML.
- Metadata HTML: 44,851 bytes.
- Source archive: 12,059,926 bytes; valid; 18 entries.
- Unexpected partials: 0.
- Local companion records: README, attribution, machine-readable summary, preflight manifest, and verification report updated.

## Dedup Index Update

- Pre-review check: no matching arXiv ID, publisher DOI, normalized title, slug, prior Arxiv DEP artifact, memory entry, substantive companion-repository result, or 24-hour same-paper marker.
- Metadata-only inventory hit: present and explicitly non-excluding.
- Entry action: new pointer added.
- Entry count after addition: 65.
- Initial public status: `review_validated`.
- Commit/PR reference: pending primary remote commit.
- Finalization action: update this phase log and the pointer to `deposited` with the remotely verified primary artifact commit.

## Expected vs Observed Trajectory

The source repair and cache phases were faster than their envelopes because official companion artifacts were available on the first bounded attempt and all local extractors except `pdftotext` succeeded. Review time remained within guidance despite inspecting paper tables, all rendered pages, the publisher record, and the official code surface. Related-DEP exploration was slightly below estimate because three strong local matches were already present and could be verified directly.

Authoring remained within its envelope. The overall job is expected to finish near the 90-120 minute guidance; validation/submission may extend the trajectory if a concurrent remote change requires a fetch/rebase or if any public-safety/source-upload gate fails. No source, table, figure, code-surface, or related-DEP review was truncated to meet a phase estimate.

## Shortfalls and Follow-Up

- `Extractor`: `pdftotext` unavailable; `pypdf` succeeded.
- `Scientific reproduction`: no dataset, model, checkpoint, training, evaluation, or metric recomputation was run.
- `Paper evidence`: no repeated seeds, confidence intervals, statistical tests, resource tails, calibration-error sweep, sensor-fault sweep, aggregate adverse-condition study, or closed-loop outcome.
- `Release evidence`: paper-matched scripts, dependencies, checkpoints, expected outputs, and an apparently executable multimodal Mamba path were not established from the inspected public repository surface.
- `Version boundary`: the later IEEE journal full text was not inspected; DOI and publication metadata were recorded without assuming exact text identity with arXiv v1.
- `Submission`: pending final validation, allowlisted staging, remote push verification, pointer finalization, and Slack read-back.
