# DEP-A-20260813-ProxyKV Pruning

#artificial-intelligence #KV-cache #long-context #proxy-pruning #inference-efficiency #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.16360v1, *ProxyKV: Cross-Model Proxy Pruning for Efficient Long-Context LLM Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.16360-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.16360-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We propose ProxyKV ( Figure ˜ 1 (c)), a cross-model proxy pruning framework that offloads scoring to a lightweight intra-family Small-Model Proxy executed asynchronously to the target’s critical path. Efficient long-context inference in Large Language Models (LLMs) is severely constrained by the Key-Value (KV) cache memory wall, yet existing pruning methods force a choice between low-latency heuristics that sacrifice precision and high-precision reconstruction methods that incur prohibitive prefilling overhead. To bridge this scoring-cost–accuracy gap, we propose ProxyKV, a cross-model proxy pruning framework that offloads importance scoring to a lightweight intra-family Small-Model Proxy executed asynchronously to the Large-Model Target.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use cross-model proxy pruning as a compatibility contract: bind proxy and target versions, retain per-layer pruning decisions, measure target-model degradation and transfer cost, and fall back when proxy ranking diverges on new domains or context lengths.

## Associated DEP Records

- [DEP-A-20260810-MomentKV](../DEP-A-20260810-MomentKV/README.md) - direct long-context KV-cache eviction and retention context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260810-AB Sparse Attention](../DEP-A-20260810-AB%20Sparse%20Attention/README.md) - direct adaptive sparse-attention and long-context evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.16360v1
  - Applies to: `2605.16360-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.16360v1
  - Applies to: `2605.16360-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.16360v1
  - Applies to: `2605.16360-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.16360
  - Applies to: `2605.16360-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Junjie Li
  - arXiv author search: https://arxiv.org/search/?query=Junjie%20Li&searchtype=author
  - Applies to: the reviewed paper and `2605.16360-whitepaper-review.md`.
- Author: Jiong Lou
  - arXiv author search: https://arxiv.org/search/?query=Jiong%20Lou&searchtype=author
  - Applies to: the reviewed paper and `2605.16360-whitepaper-review.md`.
- Author: Jie Li
  - arXiv author search: https://arxiv.org/search/?query=Jie%20Li&searchtype=author
  - Applies to: the reviewed paper and `2605.16360-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
