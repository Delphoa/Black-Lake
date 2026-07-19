# DEP-A-20260717-HYPIC Position Cache

#artificial-intelligence #llm-serving #hybrid-attention #position-independent-cache #rag #prefill

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.01299v2, *HYPIC: Accelerating Hybrid-Attention LLM Serving with Position-Independent Caching*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.01299-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.01299-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: HYPIC caches, for linear-attention layers, each segment's cumulative transition operator and zero-start end state so independently cached segments can be composed. For full-attention layers it recomputes small seam windows at boundaries, and it parallelizes cache-miss prefill across instances.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Version transition operators by model and segment hash, monitor seam disagreement on sampled requests, and widen or abandon reuse when accumulated composition error exceeds a task threshold.

## Associated DEP Records

- [DEP-A-20260716-KV Memory Hierarchy](../DEP-A-20260716-KV%20Memory%20Hierarchy/README.md) - direct method context: reviewed survey of KV-cache representation, movement, reuse, and memory hierarchy. This is method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.01299v2
  - Applies to: `2607.01299-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.01299v2
  - Applies to: `2607.01299-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.01299v2
  - Applies to: `2607.01299-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.01299
  - Applies to: `2607.01299-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yifei Liu
  - arXiv author search: https://arxiv.org/search/?query=Yifei%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.01299-whitepaper-review.md`.
- Author: Juntong Wu
  - arXiv author search: https://arxiv.org/search/?query=Juntong%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2607.01299-whitepaper-review.md`.
- Author: Yang Liu
  - arXiv author search: https://arxiv.org/search/?query=Yang%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.01299-whitepaper-review.md`.
- Author: Junhao Hu
  - arXiv author search: https://arxiv.org/search/?query=Junhao%20Hu&searchtype=author
  - Applies to: the reviewed paper and `2607.01299-whitepaper-review.md`.
- Author: Minghao Li
  - arXiv author search: https://arxiv.org/search/?query=Minghao%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.01299-whitepaper-review.md`.
- Author: Xiaoxu Chen
  - arXiv author search: https://arxiv.org/search/?query=Xiaoxu%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.01299-whitepaper-review.md`.
- Author: Weihang Chen
  - arXiv author search: https://arxiv.org/search/?query=Weihang%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.01299-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
