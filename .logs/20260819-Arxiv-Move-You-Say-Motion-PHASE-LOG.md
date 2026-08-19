# Black Lake Arxiv DEP Phase Log

## Public-Safe Run Summary

- Paper: Move as You Say, Interact as You Can: Language-guided Human Motion Generation with Scene Affordance
- arXiv: 2403.18036v1
- DEP date: 2026-08-19
- Job type: source-first arXiv review with extraction-cache acceleration
- Overall trajectory: approximately 15 minutes against a 4–12 minute expected range
- Result: source-integrity gate passed; public-safe artifacts committed and pushed; Slack notification pending
- Source locality: original PDFs, full-paper HTML, metadata, extracted text, caches, and acquisition records remain local and are not part of the public artifact set.

## Phase Metrics

| Phase | Expected duration | Observed duration | Result |
| --- | ---: | ---: | --- |
| Candidate enumeration and uniform draw | 15–60 seconds | approximately 54 seconds | 75,967 PDFs reduced to 75,964 paper units; draw index 6,095 accepted |
| Deduplication and reselection validation | 10–45 seconds | approximately 20 seconds | No matching arXiv ID, DOI, title, slug, or 24-hour marker |
| Local source-integrity repair | 5–120 seconds | approximately 9 seconds | Valid PDF retained; full-paper HTML restored and verified |
| Extractor preflight and missing-only cache | 1–15 seconds | approximately 1 second | Cache status cached; pypdf and html-regex fallbacks succeeded |
| Source-first review | 60–240 seconds | approximately 105 seconds | PDF, full HTML, metadata, abstract, project page, and official code evidence reviewed |
| Related DEP exploration | 15–90 seconds | approximately 25 seconds | Three concrete overlap entries selected and inspected |
| Artifact drafting | 60–300 seconds | approximately 180 seconds | All required public-safe artifacts drafted |
| Validation and submission | 60–240 seconds | approximately 30 seconds | Allowlist, JSON, schema, direct push, and remote read-back passed; Slack notification pending |

## Extraction Cache

- Mode: missing-only
- Status: cached
- HTML extractor: html-regex, successful
- PDF extractor: pypdf, successful
- Fallback reason: pdftotext unavailable
- Source extractor: not run because no local source package was available
- Source counts: HTML 3, PDF 1, readme 2, summary CSV 1
- Derived text outputs: HTML 81,944 bytes; PDF 71,123 bytes; source text 0 bytes
- Public source references: arXiv abstract, HTML, PDF, e-print, DOI, project page, and official implementation repository

## Source Integrity Gate

| Check | Observed | Status |
| --- | ---: | --- |
| PDF size | 7,719,158 bytes | passed |
| PDF header | %PDF- | passed |
| PDF trailing marker | %%EOF | passed |
| Full-paper HTML size | 392,926 bytes | passed |
| HTML body characters after script/style removal | 94,235 | passed |
| Article or LaTeXML marker | present | passed |
| Section or heading markers | 108 | passed |
| Paper-structure terms | 7 | passed |
| Partial download markers | none | passed |

## Deduplication Index Update

- Index path: .staging/arxiv-dep-dedup-index.json
- arXiv base ID: 2403.18036
- DOI: 10.48550/arXiv.2403.18036
- Existing match: none
- Duplicate exclusions: 0
- Reselections: 0
- Artifact status: deposited; direct commit and push complete
- Commit reference: https://github.com/Delphoa/Black-Lake/commit/6ae5c4b1

## Expected Versus Observed Trajectory

Selection, deduplication, repair, and cache phases remained within their expected ranges. Review and drafting were longer than the compact expected band because the initial unit needed repair and the source-first pass compared the paper with three related DEP entries. The additional time produced a verified full-paper evidence base rather than an abstract-only synthesis.

## Shortfalls and Follow-up

- The local source archive had no usable source package for this paper; implementation-level claims are based on the paper, public HTML, project page, and official repository README.
- No experiments, checkpoints, or restricted datasets were executed.
- Slack notification remains to be completed before the run is final.
