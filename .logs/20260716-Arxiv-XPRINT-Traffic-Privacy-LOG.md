# Arxiv DEP Job Log: XPRINT Traffic Privacy

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2509.00706v1, *X-PRINT: Platform-Agnostic and Scalable Fine-Grained Encrypted Traffic Fingerprinting*
- Selection: accepted on the first uniform draw
- Source integrity: initial `partial`, repaired to verified `complete`
- Safety scope: defensive privacy research and countermeasure evaluation only
- Source policy: PDF, HTML, metadata, packet/URI traces, cache, and extracted text remain local; none are deposited
- Extraction cache: initial miss; final `cached`

## Random Selection

- Enumeration: `rg --files -g "*.pdf"`
- PDFs / unique parent units: 75,777 / 75,776
- Sampling: PowerShell `Get-Random` over the sorted unique unit list
- Zero-based index: 44,195
- Exclusions: 0
- Reselections: 0

## Dedup Validation

No matching arXiv ID, DOI, normalized title, slug, Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, automation-memory entry, companion-repository deposit, or 24-hour same-paper marker was found.

## Source Integrity and Cache

- PDF: 1,824,393 bytes with `%PDF-` header and trailing `%%EOF`
- Initial full-paper HTML: missing
- Repair: official arXiv full-paper and metadata HTML fetched once; no fallback required
- Full HTML: 312,956 bytes; 89,178 body characters; two document markers; 84 heading/section markers; seven structure terms
- Metadata: 43,328 bytes; metadata only
- Source package: not collected; partial files: 0
- Cache: 0.849-second missing-only backfill via `pypdf` and `html-regex`
- Cache text: PDF 92,377 bytes; HTML 88,946 bytes; source absent

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md` - network telemetry governance, privacy, task-specific evaluation, and guarded deployment.
2. `.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md` - channel-specific forensic signatures, benign-traffic calibration, and privacy-minimized operational metadata.
3. `.lake-data/DEP-E/DEP-E-20260715-Control Surfaces/control-surfaces.md` - purpose-bound privacy, instrumentation at the risk mechanism, and sensitive-log retention controls.

## Output Paths

- `.logs/20260716-Arxiv-XPRINT-Traffic-Privacy-LOG.md`
- `.logs/20260716-Arxiv-XPRINT-Traffic-Privacy-PHASE-LOG.md`
- `.reports/BL-Arxiv-XPRINT-Traffic-Privacy-20260716/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/README.md`
- `.lake-data/DEP-E/DEP-E-20260716-XPRINT Traffic Privacy/xprint_traffic_privacy_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. How much privacy protection do padding, randomized delays, batching, multiplexing, and traffic transformation provide against X-PRINT under matched bandwidth, latency, and utility budgets?
2. Do results hold across independent networks, geographies, accounts, devices, accessibility patterns, background loads, QUIC/TLS changes, and applications with no shared backend ownership?
3. Can a privacy-risk auditor estimate behavior leakage with minimized telemetry and fixed-denominator false-positive/false-negative reporting without retaining URIs, payloads, or identity-linked traces?

## Challenges

1. URI labels are produced through controlled MitM decryption and certificate-validation bypass, creating a privileged labeling process with legal, privacy, and reproducibility constraints.
2. “Open world” excludes unrelated applications through a coarse filter and tunes unseen-case thresholds on in-domain data, so the operational universe is narrower than the phrase suggests.
3. The custom dataset, code, collection scripts, labels, and per-run splits were not released, limiting independent verification of leakage, overlap, and uncertainty.

## Known Shortfalls

- The system was not reproduced; no official code, traffic corpus, URI maps, trained models, or environment was identified.
- Countermeasures are discussed qualitatively without a matched privacy/overhead experiment.
- Consent, account data, sensitive URI parameters, annotator handling, regional/legal scope, and retention controls are not fully documented.

## Submission Record

- Primary artifact commit: pending
- Slack notification: pending
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source, traffic, URI, or model artifacts
- Submission status: pending
