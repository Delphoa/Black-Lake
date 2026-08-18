# Arxiv DEP Phase Log

## Public-Safe Run Summary

- Paper: arXiv:2104.14786v1, “Editable Free-Viewpoint Video using a Layered Neural Representation.”
- Run date: 2026-08-18. Exact local execution time and timezone are withheld.
- Whole-job trajectory: approximately 22 minutes of active tool work before artifact drafting; below the 90–120 minute guidance because the first random draw was eligible, the single repair completed in one bounded attempt, and extraction was local and fast. Source-first review was not truncated because a phase estimate was exceeded.
- Final state: source gate passed, cache status `cached`, dedup pointer pending final commit reference, public artifacts generated locally, no source files uploaded.

## Phase Metrics

| Phase | Expected duration | Observed elapsed duration | Status | Notes |
|---|---:|---:|---|---|
| Candidate enumeration and random draw | 1–3 min | about 5 sec | complete | 75,967 PDFs collapsed to 75,964 parent units; zero-based draw 34,230. |
| Dedup and recent-marker validation | 3–8 min | about 3 sec of search-tool time | complete | Local Black Lake, dedup index, memory, and relevant Black-Lake-Data searches had no matching ID/title/slug/DOI. |
| Source-integrity classification | 2–5 min | about 1 min | complete | Initial state was partial: PDF present, full-paper HTML missing. |
| Bounded source repair | 5–20 min | about 7 sec of process time | complete | Official full-paper HTML saved and verified; PDF preserved; source package unavailable. |
| Cache preflight and missing-only extraction | 1–5 min | about 1 sec of process time | complete | HTML and PDF text cached; source text absent. |
| Source-first paper review | 20–45 min | about 8 min active review | complete | Full PDF text, full-paper HTML text, metadata, project page, official repository README/config/demo, and visual Table 1 inspection reviewed. |
| Related DEP exploration | 10–20 min | about 3 min active review | complete | Exactly three concrete-overlap entries selected. |
| Artifact drafting and validation | 20–40 min | pending final repository validation | in progress | Public-safe logs, report, manuscript, README, and dedup pointer are being prepared. |

## Extraction Cache

- Initial cache state: `miss` for arXiv:2104.14786.
- Final cache state: `cached`.
- PDF extractor: `pypdf`, status `ok`; fallback reason: `pdftotext unavailable`.
- HTML extractor: `html-regex`, status `ok`.
- Source extractor: `none`, status `missing`; the archive repair reported the source package unavailable.
- Public-safe derived outputs: PDF text present, full-paper HTML text present, source text absent.
- Network during extraction: none; extraction used the repaired local paper unit.

## Dedup Index Update

- Local dedup index checked before acceptance: no arXiv ID, DOI, normalized title, slug, or artifact-path match.
- Black Lake logs, reports, and lake-data checked before acceptance: no match.
- Automation memory checked before acceptance: no match; the prior run concerned Inception Transformer.
- Relevant Black-Lake-Data repository searches for the arXiv ID and normalized title: no results.
- Same-paper marker within the preceding 24 hours: none observed.
- Reselection status: no reselection required.
- Final pointer status: a new `deposited` entry will be added with repository-relative artifact paths and public source URLs; the final commit/PR reference will be filled after submission.

## Expected vs Observed Trajectory

- Expected: enumerate → dedup → complete-source gate → repair if needed → local cache extraction → source-first review → three related entries → public-safe artifact validation → atomic submission.
- Observed: the expected order was followed. The first random draw needed source repair but remained eligible; review began only after independent PDF/HTML verification and cache completion.
- Expected-duration comparison: enumeration, repair, and extraction were materially faster than guidance; review and synthesis remained source-first and were not shortened to fit the estimate.

## Shortfalls and Follow-Up

- `pdftotext` was unavailable; `pypdf` provided usable PDF text with symbol-encoding noise.
- The source package was unavailable, so no TeX/source text or source files were collected for public deposition.
- The official code repository was inspected but not executed; the dataset was not downloaded.
- No independent metric reproduction, multi-seed study, raw-prediction audit, or full camera-view Table 1 recomputation was performed.
- Table 1 contains a printed inconsistency: the bold `Ours` SSIM and MAE values do not dominate all baselines in the stated metric directions, despite the caption/prose claiming broad superiority. Future review should inspect the original metric script and raw outputs.
- No source files were uploaded or attached; public artifacts cite public URLs and explicitly state source locality.

## Attribution Block

- Source URL: https://arxiv.org/abs/2104.14786
  - Applies to: all phase identity and metadata fields.
- Source URL: https://arxiv.org/html/2104.14786
  - Applies to: extraction and source-first review evidence.
- Source URL: https://arxiv.org/pdf/2104.14786
  - Applies to: source-integrity and visual table checks.
- Source URL: https://github.com/DarlingHang/st-nerf
  - Applies to: official implementation availability and reproducibility boundary.
