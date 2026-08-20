# DEP-A-20260727-QCFuse RAG Cache

#artificial-intelligence #retrieval-augmented-generation #KV-cache #query-compression #long-context #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.05875v1, *QCFuse: Query-Aware Cache Fusion via Compressed View for Efficient RAG Serving*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.05875-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.05875-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: QCFuse makes selective cache recomputation query-aware without requiring a full all-layer view. Chunk-anchor probing conditions the query on compact per-chunk anchors, and critical-layer profiling chooses tokens whose KV entries should be recomputed while the rest of each cached chunk is fused into the current prompt.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat recomputation selection as a calibrated evidence triage model: log false-negative tokens using a shadow full-prefill path and adapt the recomputation budget to measured downstream divergence. The mechanism is weakened if a simple cost-matched selector matches QCFuse after layer profiling and anchor overhead are included.

## Associated DEP Records

- [DEP-A-20260715-FAIR GraphRAG A Retrieval](../DEP-A-20260715-FAIR%20GraphRAG%20A%20Retrieval/README.md) - direct retrieval architecture and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.05875v1
  - Applies to: `2606.05875-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.05875v1
  - Applies to: `2606.05875-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.05875v1
  - Applies to: `2606.05875-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.05875
  - Applies to: `2606.05875-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/uYanJX/QCFuse
  - Applies to: reproducibility context in `2606.05875-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Jianxin Yan
  - arXiv author search: https://arxiv.org/search/?query=Jianxin%20Yan&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Author: Wangze Ni
  - arXiv author search: https://arxiv.org/search/?query=Wangze%20Ni&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Author: Zhenxin Li
  - arXiv author search: https://arxiv.org/search/?query=Zhenxin%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Author: Jiabao Jin
  - arXiv author search: https://arxiv.org/search/?query=Jiabao%20Jin&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Author: Zhitao Shen
  - arXiv author search: https://arxiv.org/search/?query=Zhitao%20Shen&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Author: Haoyang Li
  - arXiv author search: https://arxiv.org/search/?query=Haoyang%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Author: Jia Zhu
  - arXiv author search: https://arxiv.org/search/?query=Jia%20Zhu&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Author: Peng Cheng
  - arXiv author search: https://arxiv.org/search/?query=Peng%20Cheng&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Author: Xuemin Lin
  - arXiv author search: https://arxiv.org/search/?query=Xuemin%20Lin&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Author: Lei Chen
  - arXiv author search: https://arxiv.org/search/?query=Lei%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Author: Kui Ren
  - arXiv author search: https://arxiv.org/search/?query=Kui%20Ren&searchtype=author
  - Applies to: the reviewed paper and `2606.05875-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
