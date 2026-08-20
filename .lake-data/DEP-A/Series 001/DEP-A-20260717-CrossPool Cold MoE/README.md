# DEP-A-20260717-CrossPool Cold MoE

#artificial-intelligence #distributed-systems #llm-serving #mixture-of-experts #kv-cache #gpu-memory

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.24506v2, *CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.24506-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.24506-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: CrossPool separates stable MoE FFN weights from transient KV cache into distinct GPU pools. A planner and virtualizer allocate shared KV capacity, while a layer-wise pipeline hides hidden-state transfers and persistent kernels reduce control overhead.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: A production control plane would expose per-pool reservations, transfer debt, fragmentation, and tenant attribution, then degrade to colocated execution before the cross-pool pipeline violates a tail-latency SLO.

## Associated DEP Records

- [DEP-A-20260716-KV Memory Hierarchy](../DEP-A-20260716-KV%20Memory%20Hierarchy/README.md) - direct method context: reviewed survey of KV-cache representation, movement, reuse, and memory hierarchy. This is method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.24506v2
  - Applies to: `2606.24506-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.24506v2
  - Applies to: `2606.24506-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.24506v2
  - Applies to: `2606.24506-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.24506
  - Applies to: `2606.24506-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Zhuoren Ye
  - arXiv author search: https://arxiv.org/search/?query=Zhuoren%20Ye&searchtype=author
  - Applies to: the reviewed paper and `2606.24506-whitepaper-review.md`.
- Author: Tianyu Wo
  - arXiv author search: https://arxiv.org/search/?query=Tianyu%20Wo&searchtype=author
  - Applies to: the reviewed paper and `2606.24506-whitepaper-review.md`.
- Author: Dinghao Xue
  - arXiv author search: https://arxiv.org/search/?query=Dinghao%20Xue&searchtype=author
  - Applies to: the reviewed paper and `2606.24506-whitepaper-review.md`.
- Author: Mingming Zhang
  - arXiv author search: https://arxiv.org/search/?query=Mingming%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.24506-whitepaper-review.md`.
- Author: Yuchen Teng
  - arXiv author search: https://arxiv.org/search/?query=Yuchen%20Teng&searchtype=author
  - Applies to: the reviewed paper and `2606.24506-whitepaper-review.md`.
- Author: Chunming Hu
  - arXiv author search: https://arxiv.org/search/?query=Chunming%20Hu&searchtype=author
  - Applies to: the reviewed paper and `2606.24506-whitepaper-review.md`.
- Author: Renyu Yang
  - arXiv author search: https://arxiv.org/search/?query=Renyu%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2606.24506-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
