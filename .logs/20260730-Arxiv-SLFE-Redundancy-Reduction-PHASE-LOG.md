# Arxiv DEP Phase Log — SLFE Redundancy Reduction

## Public-Safe Run Summary

- Paper: arXiv:1805.12305, *Start Late or Finish Early: A Distributed Graph Processing System with Redundancy Reduction*.
- Deposit date: 2026-07-30.
- No exact execution timestamps, local paths, machine identifiers, or source files are recorded in this public log.
- Source-integrity gate: initial state `partial`; repaired state `complete`; review gate passed.
- Public-output policy: only generated Markdown records and the required dedup pointer are eligible for staging. Source documents and cache outputs are withheld locally.

## Phase Metrics

| Phase | Expected duration | Observed duration | Status | Notes |
|---|---:|---:|---|---|
| Candidate enumeration and random draw | 2–10 min | under 1 min | complete | 75,959 PDF candidates; first draw accepted. |
| Dedup and remote-record scan | 5–15 min | about 3 min | complete | No prior public DEP match; one metadata-only inventory row was excluded from duplicate evidence. |
| Source-integrity inspection and repair | 10–30 min | under 1 min | complete | Existing PDF preserved; full-paper HTML and provenance records repaired through the bounded collector. |
| Extraction preflight and cache creation | 2–10 min | under 1 min | complete | Missing-only local extraction; no cache-network fetch. |
| Source-first review and related-DEP synthesis | 25–60 min | about 18 min | complete | PDF, full-paper HTML, metadata, cache outputs, and three repository records inspected. |
| Public artifact drafting and validation | 20–45 min | about 20 min | complete | Schema, attribution, exact-three, public-safety, and allowlist checks scheduled before submission. |

## Extraction Cache

- Preflight: `pypdf` available; `pdftotext` unavailable.
- Cache status: miss to `cached` using missing-only mode.
- Extractors: PDF `pypdf` (fallback reason: `pdftotext` unavailable); HTML `html-regex`; source package unavailable.
- Public-safe outputs: PDF text present (62,748 bytes); HTML text present (80,071 bytes); source text absent because no source package was available.
- Cache methodology: the central archive cache was used only as local processing infrastructure; public artifacts use source-derived findings and public URLs rather than cache paths or extracted text.

## Source Integrity and Repair

- Initial classification: `partial` because a valid PDF existed but no full-paper HTML existed.
- Repair: bounded single-paper collector retrieved metadata HTML and an approved ar5iv full-paper fallback while preserving the valid PDF.
- Verification: PDF valid; full-paper HTML 874,592 bytes with 71,843 extracted body characters, a document marker, 60 heading markers, and seven recognized paper-structure terms; no partial files remained.
- Source package: unavailable; this did not block the complete-source gate because the verified PDF and full-paper HTML were both present.

## Dedup Index Update

- Prior index state: no record for arXiv:1805.12305, its DOI, normalized title, or slug.
- Validation sources: current dedup pointer, Black-Lake `.logs`, `.reports`, `.lake-data`, automation memory, current remote Black-Lake records, and Black-Lake-Data entries.
- Result: unique public research deposit. The index is updated with repository-relative paths, public source URLs, date-only deposit metadata, and the primary submission reference: https://github.com/Delphoa/Black-Lake/commit/d8a5903c.

## Expected vs Observed Trajectory

- Whole-job guidance: 90–120 minutes.
- Observed trajectory: about 43 minutes before submission and Slack notification; source repair, cache generation, and evidence review completed within their estimates.
- Assessment: no reasonable source-first phase was truncated merely to meet an estimate. The shorter trajectory reflects a first-draw selection, successful bounded repair, and local cache extraction.

## Shortfalls and Follow-Up

- No source package, official code repository, environment manifest, or runnable benchmark was available from the inspected canonical record.
- Reported speedups were not independently reproduced; confidence intervals, energy, tail latency, and fault recovery were not evaluated.
- The paper's own limitations identify preprocessing overhead and possible inter-node imbalance; current heterogeneous and dynamic-graph behavior remains unverified.
