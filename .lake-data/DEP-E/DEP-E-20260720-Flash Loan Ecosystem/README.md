# DEP-E-20260720-Flash Loan Ecosystem

#defi #flash-loans #measurement #smart-contracts #anomaly-detection #security #research-review

Public-safe context: job `BLAD-2200-20260720-8636EDC7`, item `BLAD-2200-20260720-8636EDC7-P09`, uniformly selected `arXiv:2010.12252v3`. The PDF-only unit was repaired with verified approved full-paper HTML before review. Local paths, exact execution times, wallet data, transaction traces, and source documents are withheld.

## Contents

- `README.md` - context, inventory, defensive/source boundary, synthesis, and attribution.
- `flash_loan_ecosystem_manuscript.md` - schema-complete review of the early flash-loan measurement, evidence limits, defensive applications, and related DEP synthesis.

No `.source/` exists. No wallet, key, chain extract, transaction trace, contract source, script, PDF, HTML, cache, or extracted source text is deposited.

## Summary of Items

The paper analyzes about one billion Ethereum transactions through 2021-01-31 and reports 76,303 flash-loan transactions across Aave, dYdX, and UniswapV2. It proposes provider-specific identification patterns, reports rising use, and describes arbitrage, wash trading, liquidation, and collateral swap as application categories.

Evidence is historical and unreproduced. Provider rows and headline totals need clarified uniqueness/overlap semantics; detector transfer across protocol versions and modern chains is untested. The review therefore treats the work as a taxonomy and measurement baseline rather than a present-day prevalence estimate or security verdict.

## Insights and Relevance

A useful derivative is a read-only, provenance-first risk evidence gate. SAILFISH adds static state-risk context, CausalTAD adds shift-aware anomaly framing, and PAC Confidence adds finite-sample threshold uncertainty. Human review, abstention, privacy controls, and non-accusatory defaults remain mandatory.

## Attribution Block

- https://arxiv.org/abs/2010.12252 - metadata and locators.
- https://ar5iv.labs.arxiv.org/html/2010.12252 - verified full paper; local copy withheld.
- https://arxiv.org/pdf/2010.12252 - verified PDF; local copy withheld.
- https://doi.org/10.1145/3457977.3460301 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-SAILFISH%20Vetting - related contract-vetting DEP.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260711-CausalTAD%20Trajectory - related anomaly DEP.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence - related calibration DEP.
- Source files: verified PDF, full-paper HTML, metadata HTML, and integrity records; all withheld locally with zero source-document uploads.
