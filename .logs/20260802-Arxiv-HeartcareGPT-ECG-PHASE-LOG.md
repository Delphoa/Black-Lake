# Arxiv DEP Phase Log

## Public-Safe Run Summary

- Paper: *HeartcareGPT: A Unified Multimodal ECG Suite for Dual Signal-Image Modeling and Understanding* (arXiv:2506.05831v4).
- Selection: uniform random draw over 75,957 unique PDF-parent units; first draw accepted after dedup checks.
- Source state: partial at selection, repaired to complete before review.
- Public source files uploaded: zero. PDF, full-paper HTML, metadata, extracted text, cache, and repair records remain local only; the TeX/source package was unavailable.

## Phase Metrics

| Phase | Expected duration | Observed duration | Status | Notes |
|---|---:|---:|---|---|
| Candidate enumeration and random draw | 5-15 minutes | 3.8 seconds | complete | 75,960 PDFs collapsed to 75,957 parent units. |
| Dedup and exclusion checks | 5-15 minutes | under 1 minute | complete | Public pointer, local hidden artifacts, memory, and metadata-only inventory rows checked. |
| Source integrity validation | 10-20 minutes | under 1 minute final gate | complete | Initial partial state was repaired before synthesis. |
| Bounded source repair | 15-30 minutes | under 1 minute | complete | Public arXiv metadata/full HTML repair succeeded; source package was unavailable; zero partials. |
| Cache preflight, lookup, and extraction | 2-10 minutes | about 1.4 seconds | complete | `missing-only` extraction used local repaired sources; no extraction-network fetch. |
| Source-first review and related-entry synthesis | 30-60 minutes | not separately instrumented | complete | Full cached PDF/HTML text, live arXiv pages, official repository, and three related DEP records inspected. |
| Artifact validation and submission | 15-30 minutes | under 1 minute for local validation | complete | Public-safe scans, schema checks, and allowlist review passed; repository submission and Slack notification are the remaining handoff records. |

## Extraction Cache

- Initial cache status: miss for arXiv:2506.05831.
- Extraction mode: `missing-only` against the selected local paper unit after source repair.
- Final status: `cached`.
- Extractors: `pypdf` for PDF text and `html-regex` for full HTML text; source extractor status `missing` because no source package was available.
- Fallback: `pdftotext` unavailable; `pypdf` succeeded.
- Cached text outputs: PDF 95,075 bytes; HTML 23,812 bytes; source 0 bytes and absent.
- Cache backfill: local source repair supplied the missing full-paper HTML before extraction; extraction did not fetch network sources.

## Dedup Index Update

- Pre-write status: no matching public pointer entry, log, report, DEP-E artifact, automation-memory marker, or same-paper marker within 24 hours.
- Reselection status: not required; first draw accepted.
- Metadata-only matches: author-inventory rows in Black-Lake and Black-Lake-Data only; no research deposit marker.
- Post-write status: one unique pointer entry is prepared for arXiv:2506.05831v4; repository reference is recorded after submission.

## Expected vs Observed Trajectory

- The source-first trajectory completed without truncating method, benchmark, ablation, limitation, appendix, or related-DEP review.
- The repair and extraction phases were faster than their guidance ranges; this did not shorten the review boundary.
- The principal shortfalls are unavailable TeX/source package, unavailable `pdftotext`, no independent reproduction, no clinical-site validation, and no execution of the official repository or models.

## Shortfalls and Follow-Up

- The current evidence supports research use and implementation planning, not diagnosis or clinical deployment.
- A follow-up should audit patient-level split provenance, dataset licensing/consent, rare-condition coverage, calibration, external-site performance, missing-modality behavior, and independent metric computation.
