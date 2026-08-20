# DEP-A-20260819-vToken Token Level Virtua

#artificial-intelligence #arXiv #paper-review #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.13263v1, *vToken: Token-Level Virtualization for Reclaimable KV Caches*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.13263-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.13263-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Our core idea is to introduce vToken , a lightweight token-level memory virtualization layer between eviction policies and the PagedAttention substrate. We propose vToken , a token-level virtualization layer that decouples logical token liveness from physical block placement. 1 Introduction 2.1 KV Cache and PagedAttention 2.2 KV Eviction Algorithms 2.3.1 Formal Definition 2.3.2 Quantifying the Impact 2.3.3 Algorithm Integration Barrier 3.1 Design Goals and Virtualization Boundary 3.2 Token Table and Logical Address Space 3.3.1 Reclamation Eligibility 3.3.2 Headroom-Aware Admission 3.3.3 Relocation Planning 3.3.4 Stage-Aware Asynchronous Copy 3.4 Integration with the Scheduler 3.5 Correctness Invariants 4 Implementation 5.1 Experimental Setup 5.2 Memory Efficiency 5.3 Sustainable Throughput under Token-Level Eviction 5.4 Capacity Frontier under Memory Pressure 5.5 Overhead and Overlap 5.6 Sensitivity Analysis 5.7 Prefix-Cache Compatibility 5.8 Relocation Correctness and Generation Stability 6 Discussion 7 Related Work 8 Conclusion References Modern autoregressive LLMs generate tokens sequentially.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat vToken: Token-Level Virtualization for Reclaimable KV Caches as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.13263v1
  - Applies to: `2608.13263-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.13263v1
  - Applies to: `2608.13263-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.13263v1
  - Applies to: `2608.13263-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.13263
  - Applies to: `2608.13263-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Yuanhang Gao
  - arXiv author search: https://arxiv.org/search/?query=Yuanhang%20Gao&searchtype=author
  - Applies to: the reviewed paper and `2608.13263-whitepaper-review.md`.
- Author: Xiangrui Yang
  - arXiv author search: https://arxiv.org/search/?query=Xiangrui%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2608.13263-whitepaper-review.md`.
- Author: Yuanfeng Chen
  - arXiv author search: https://arxiv.org/search/?query=Yuanfeng%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2608.13263-whitepaper-review.md`.
- Author: Hongjia Chen
  - arXiv author search: https://arxiv.org/search/?query=Hongjia%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2608.13263-whitepaper-review.md`.
- Author: Qianru Lv
  - arXiv author search: https://arxiv.org/search/?query=Qianru%20Lv&searchtype=author
  - Applies to: the reviewed paper and `2608.13263-whitepaper-review.md`.
- Author: Wenfei Wu
  - arXiv author search: https://arxiv.org/search/?query=Wenfei%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2608.13263-whitepaper-review.md`.
- Author: Dongsheng Li
  - arXiv author search: https://arxiv.org/search/?query=Dongsheng%20Li&searchtype=author
  - Applies to: the reviewed paper and `2608.13263-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
