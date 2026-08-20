# DEP-A-20260814-PagedWeight MoE

#artificial-intelligence #mixture-of-experts #weight-quantization #LLM-serving #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.16184v1, *PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.16184-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.16184-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Our Work: We propose PagedWeight, a novel management method for MoE LLM serving that dynamically quantizes MoE model’s weights at runtime and balances the choice of quantization with the KV cache and context sizes. PagedWeight is a higher-level system that focuses on LLM memory management at serving time, adapting dynamic, mixed-precision quantization of MoE weights as one of its key techniques to counter KV cache memory pressure. We propose PagedWeight, a novel management method for MoE LLM serving that dynamically quantizes MoE model’s weights at runtime and balances expert-weight precision with the KV cache sizes.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate dynamic expert-weight quantization as a quality-aware memory balancer: log expert precision, KV pressure, routing frequency, latency, and task quality, with hysteresis and a higher-precision fallback when workload or expert importance shifts.

## Associated DEP Records

- [DEP-A-20260717-CrossPool Cold MoE](../../Series%20001/DEP-A-20260717-CrossPool%20Cold%20MoE/README.md) - direct disaggregated mixture-of-experts serving and routing context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260804-KernelFlume Serving](../../Series%20001/DEP-A-20260804-KernelFlume%20Serving/README.md) - direct LLM-serving latency and systems-efficiency context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.16184v1
  - Applies to: `2607.16184-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.16184v1
  - Applies to: `2607.16184-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.16184v1
  - Applies to: `2607.16184-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.16184
  - Applies to: `2607.16184-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yuchen Yang
  - arXiv author search: https://arxiv.org/search/?query=Yuchen%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2607.16184-whitepaper-review.md`.
- Author: Yifan Zhao
  - arXiv author search: https://arxiv.org/search/?query=Yifan%20Zhao&searchtype=author
  - Applies to: the reviewed paper and `2607.16184-whitepaper-review.md`.
- Author: Anisha Dasgupta
  - arXiv author search: https://arxiv.org/search/?query=Anisha%20Dasgupta&searchtype=author
  - Applies to: the reviewed paper and `2607.16184-whitepaper-review.md`.
- Author: Sasa Misailovic
  - arXiv author search: https://arxiv.org/search/?query=Sasa%20Misailovic&searchtype=author
  - Applies to: the reviewed paper and `2607.16184-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
