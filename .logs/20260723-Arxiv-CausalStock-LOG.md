# Arxiv DEP Log: CausalStock

- Public date marker: 2026-07-23.
- Selected paper: *CausalStock: Deep End-to-end Causal Discovery for News-driven Stock Movement Prediction*.
- Stable identifiers: arXiv:2411.06391v1; arXiv DOI 10.48550/arXiv.2411.06391; NeurIPS proceedings DOI 10.52202/079017-1504.
- Canonical records: https://arxiv.org/abs/2411.06391 and https://proceedings.neurips.cc/paper_files/paper/2024/hash/54d689d58fe54c92aee2d732fc49fca8-Abstract-Conference.html.

## Selection

- Method: `rg --files -g "*.pdf"` enumerated the private archive; each unique PDF parent directory was one paper unit. Normalized arXiv identifiers were reconciled against Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, this automation's memory, and relevant Black-Lake-Data DEP entries.
- Counts: 75,780 PDFs; 75,777 paper units; 917 observed used identifiers; 282 identifier matches excluded; 185 identifier-incomplete units withheld; 75,310 eligible units.
- Draw: PowerShell `Get-Random` selected zero-based eligible index 20,293, corresponding to zero-based all-unit index 20,438. A diagnostic draw made before the dedup scope was frozen was discarded because it included unrelated identity-report inventories; the final fixed-pool draw was accepted with zero duplicate reselections.
- Dedup: exact arXiv ID, DOI, normalized title, `CausalStock` slug, owning-artifact, automation-memory, related-repository, and preceding-24-hour scans found no prior Arxiv DEP deposit or recent same-paper marker.

## Source Integrity

- Initial state: partial. The existing 1,384,482-byte PDF passed the 10 KB minimum, `%PDF-` header, trailing `%%EOF`, and 17-page parser checks; full-paper HTML was missing.
- Repair: preserved the valid PDF and collected broker-paced metadata HTML plus official arXiv full-paper HTML. The local README, attribution record, machine-readable summary, acquisition receipt, and verification report were updated.
- Final state: complete. Full-paper HTML is 956,847 bytes with 111,467 body characters, a document marker, 91 heading/section markers, and seven paper-structure terms. Metadata HTML is 44,819 bytes. No partial files remain.
- Optional source package: not collected because the TeX endpoint redirected to a route rejected by the archive broker. This does not affect the PDF-plus-full-paper-HTML completion gate.
- Source policy: all PDF, HTML, metadata, receipt, and verification material remains private and local. Temporary review renders stayed outside the repository and were removed after inspection. No source document or `.source/` directory is included in this repository change.

## Outputs

- `.logs/20260723-Arxiv-CausalStock-LOG.md`
- `.reports/BL-Arxiv-CausalStock-20260723/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260723-CausalStock Review/README.md`
- `.lake-data/DEP-E/DEP-E-20260723-CausalStock Review/causalstock_review_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Next-Review Questions

1. Do the learned graph edges survive placebo interventions, sector-stratified permutation tests, and regime-shift evaluation?
2. How much of the reported gain comes from GPT-3.5 scoring versus the lag-dependent causal module under matched compute and data budgets?
3. Does the top-three portfolio result remain after transaction costs, slippage, market impact, turnover constraints, and walk-forward model refreshes?

## Challenges

1. Causal interpretation is conditional on strong observational assumptions and is not validated with interventions or an independent graph ground truth.
2. The primary LLM news encoder is not fully reproducible from the paper because prompt execution details, model snapshot, sampling settings, and cached outputs are incomplete.
3. The financial evaluation is historical and narrow; code, raw LLM scores, seeds, and a cost-aware backtest were not found in the inspected sources.

## Outcome

Source review and public-artifact validation completed. Repository and Slack submission status are recorded in the automation result after remote verification.
