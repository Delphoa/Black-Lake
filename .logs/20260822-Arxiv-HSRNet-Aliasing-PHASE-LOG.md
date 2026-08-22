# Black Lake Arxiv DEP Phase Log: HSRNet Aliasing

Public-safe phase metrics for the source-first run. Durations are elapsed phase measurements or bounded review estimates; exact execution timestamps and local paths are withheld.

| Phase | Expected duration | Observed duration | Status | Notes |
|---|---:|---:|---|---|
| Candidate enumeration and immutable index | 30-120 s | about 90 s | complete | 75,967 PDF paths collapsed to 67,990 unique identities. |
| Reservation and dedup validation | 1-10 s | under 2 s | complete | One uniform reservation; no reselect. |
| Source-integrity preflight | 1-30 s | under 5 s | complete | Initial state partial: PDF present, full-paper HTML missing. |
| Local source repair | 60-300 s | about 7 s | complete | Full-paper HTML restored; provenance, summary, and verification records refreshed. |
| Extractor preflight | 1-10 s | under 2 s | complete | `pypdf` available; `pdftotext` unavailable. |
| Missing-only cache extraction | 1-30 s | under 2 s | complete | PDF `pypdf` and HTML-regex succeeded; source package missing; final cache status cached. |
| Source-first review and evidence ledger | 300-900 s | within expected band | complete | Full local text, public metadata, publication metadata, and related entries inspected. |
| Public artifact drafting and validation | 120-300 s | within expected band | complete | Markdown-only package; no source files or local paths. |
| Series allocation and repository deployment | 60-180 s | pending remote audit | in progress | DEP-E ordinal 1667 planned in Series 002; shared lock held for the bounded mutation section. |

## Cache and Source Status

- `Cache hit/miss/backfill`: paper-specific cache was not treated as a hit; missing-only extraction created or filled the record from local sources. The source-repair step backfilled the missing full-paper HTML before extraction. No network was used by the extraction step.
- `Extractor status`: PDF `pypdf ok`; full-paper HTML `html-regex ok`; source package `none/missing` because no local TeX/source archive was available.
- `Final cache status`: `cached`.
- `Integrity status`: complete. PDF met size/header/EOF checks; full-paper HTML met size/body/document-marker/heading/structure-term checks.
- `Public-source status`: source URLs are cited; PDF, HTML, metadata, source package, extracted text, caches, and verification records remain local and were not uploaded.

## Dedup and Reselection Status

- Private candidate index was written before paper-body access and has a SHA-256 sidecar.
- Reservation selected canonical arXiv identity `2206.03361` uniformly from the locked eligible set.
- Repository, reports, lake-data, public dedup pointer, automation memory, and companion-repository markers were checked for arXiv ID, DOI, normalized title, and slug.
- No permanent-dedup match or same-paper marker within 24 hours was found; no reselection was required.
- DEP-E Series validation passed against the shared integration head; allocation plan is ordinal 1667, Series 002.

## Expected-vs-Observed Trajectory

The source-repair phase was required because the selected unit was partial, but the bounded repair completed within the expected range. Cache extraction was faster than the broad estimate because local PDF and full-paper HTML were already available after repair. Review stayed within the expected source-first band. The only open phase is the remote deployment audit.

## Shortfalls and Controls

- No TeX/source package was available; this is recorded as unavailable rather than inferred from the PDF.
- No official code implementation was identified in the inspected public pages; results remain author-reported.
- No independent experiment, runtime trace, or real-degradation benchmark was run.
- The public pointer cannot self-reference the commit that contains it without breaking atomicity; the submission audit reports the commit URL separately.
