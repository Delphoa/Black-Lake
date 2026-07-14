# DEP-A-20260714-SpectrumKV Transfer

#arxiv #kv-cache #mixed-precision #quantization #disaggregated-serving #data-transfer #long-context #language-model-inference #machine-learning

This DEP-A entry preserves a public-safe, whitepaper-grade full-paper review of **“SpectrumKV: Per-Token Mixed-Precision KV Cache Transfer for Prefill-Decode Disaggregated LLM Serving,” arXiv:2606.08635v1**. It covers allocation, transfer, calibration, theory, experiments, appendices, tables, and figures. Complete source documents were verified locally and withheld.

Deposition date: 2026-07-14
Stable paper version: arXiv:2606.08635v1

## Contents

- `README.md` — deposition context, complete inventory, relationships, and attribution.
- `2606.08635-whitepaper-review.md` — validated public-safe full-paper review and independent re-conceptualization.

## Summary of Items

### `README.md`

Defines the stable record, inventories both files, explains artifact status, and supplies attribution.

### `2606.08635-whitepaper-review.md`

Audits mixed-precision allocation, budget arithmetic, retention claims, theory, hardware, benchmarks, and reproducibility. The canonical review passed validation at 3,587 words with a 19/20 methodology score.

## Insights and Relevance

SpectrumKV treats disaggregated KV transfer as a bit-allocation problem. The review finds that the half-budget case is uniform INT8, random tiers sometimes win below it, one appendix allocation violates its budget, and an adaptive setting must drop tokens despite retain-every-token language. Theory and accelerator capacities also require correction.

## Associated DEP Records

- [`DEP-A-20260714-KVpop`](../DEP-A-20260714-KVpop/README.md) — close conceptual token-adaptive KV compression; an alternative, not the same paper.
- [`DEP-A-20260714-DepthWeave KV`](../DEP-A-20260714-DepthWeave%20KV/README.md) — close conceptual adaptive KV factorization; not a SpectrumKV implementation.

No same-paper DEP or relevant Labs record was verified after the named checks.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.08635
- Canonical PDF: https://arxiv.org/pdf/2606.08635
- Canonical full-paper HTML: https://arxiv.org/html/2606.08635
- DOI: https://doi.org/10.48550/arXiv.2606.08635
- Official code/data status: no author-verified official repository or dataset release was found during the recorded checks.
- Author from the canonical arXiv record:
  - Yang Pengju — https://arxiv.org/search/cs?query=Yang%2C+P&searchtype=author
- Applies to: `README.md` and `2606.08635-whitepaper-review.md`.
- Verification note: complete source documents were verified locally and withheld from this repository.
