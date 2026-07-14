# Arxiv DEP Log: Quantum Quant Trading

- Run date: 2026-07-14
- Actor: Codex scheduled research workflow
- Selected paper: *Quantum Quantitative Trading: High-Frequency Statistical Arbitrage Algorithm*
- Stable identifiers: arXiv:2104.14214v1; DOI:10.1088/1367-2630/ac7f26
- Public records: https://arxiv.org/abs/2104.14214 and https://doi.org/10.1088/1367-2630/ac7f26
- Outcome: complete source-first review and DEP-E deposit prepared

## Random Selection

- Method: enumerated PDFs with `rg --files -g "*.pdf"`, treated each unique PDF parent as one paper unit, drew a zero-based index uniformly with PowerShell `Get-Random`, and used rejection sampling only if a duplicate marker appeared.
- Candidate paper units: 75,774.
- Known-ID exclusions mapped to archive units: 62, leaving 75,712 units eligible by the repository marker set.
- Draw: zero-based index 60,411.
- Reselections: 0; the first draw was eligible.

## Deduplication Validation

The arXiv ID, journal DOI, normalized title, and slug were absent from Black-Lake `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and Black-Lake-Data code search. No same-paper marker was found within the preceding 24 hours. The repository scan observed 156 distinct public arXiv identifiers before this deposit.

## Local Source Integrity

The selected unit initially contained a valid PDF but no full-paper HTML, so review paused for repair. The existing 222,189-byte PDF was preserved after its `%PDF-` header and trailing `%%EOF` passed. The official arXiv full-paper HTML endpoint was unavailable; the approved ar5iv fallback produced a 1,098,195-byte document with 95,012 body characters, a document marker, 46 heading/section markers, and seven paper-structure terms. Metadata HTML and the TeX source package were also collected locally. The archive README, provenance record, summary CSV, and verification JSON were updated, and no partial files remained.

## Outputs

- `.logs/20260714-Arxiv-Quantum-Quant-Trading-LOG.md`
- `.reports/BL-Arxiv-Quantum-Quant-Trading-20260714/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260714-Quantum Quant Trading/README.md`
- `.lake-data/DEP-E/DEP-E-20260714-Quantum Quant Trading/quantum_quant_trading_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Does the journal version's added `sqrt(N)` factor fully account for data access, or do qRAM construction and state preparation introduce larger end-to-end costs?
2. How do realistic eigenvalue and condition-number distributions for equity portfolios change VTPA's average-query bound?
3. Can a small synthetic benchmark reproduce the preselection and cointegration logic without implying executable trading performance?

## Challenges

1. The selected archive unit required a full-paper HTML repair before synthesis could begin.
2. The arXiv v1 and 2022 journal version expose a material headline-complexity difference that must remain version-pinned.
3. The paper provides theoretical query analysis but no circuit simulation, hardware experiment, trading backtest, or official implementation in the inspected sources.

## Source Handling

Source PDFs, full-paper HTML, metadata HTML, TeX/source archives, extracted text, and caches remain local. No source file was copied, staged, uploaded, attached, or committed; public artifacts use public arXiv/DOI URLs and derived review prose only.
