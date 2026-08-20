# DEP-A-20260819-TEMPO Makespan Aware Expe

#artificial-intelligence #arXiv #paper-review #memory #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.13057v2, *TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.13057-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.13057-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Across three windows spanning two node pairs, medians against same-window static: dynamic − 0.8 -0.8 to − 3.4 % -3.4\% , TEMPO − 1.8 -1.8 to − 3.8 % -3.8\% , the topology-aware split − 3.4 -3.4 to − 5.3 % -5.3\% , LP − 38 -38 to − 50 % -50\% on decode-heavy workloads yet only − 2.5 % -2.5\% on the prefill-heavy one (its per-layer solve amortizes over long steps: the depth story within a single model). 2.3 What proxy mispricing costs on real batches 2.4 Mixed regimes are the common case 3.1 Fixed-charge makespan dispatch 3.2 The phase diagram 3.3 Scale extrapolation 4.1 Black-box calibration on the deployed pipeline 4.2 The tempo_fast solver 4.3 Communication- and topology-aware dispatch 4.4 SGLang integration 5.1 Wall-clock microbenchmark (8-GPU Testbed A, EP8) What the deployed-pipeline fit identifies—and what it does not. (i) The best fixed policy flips across the map : activation balancing wins at small B B (memory-bound), token-LP at large B B (compute-bound), and the boundary moves with s s , replication, and shape.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat TEMPO: Makespan-Aware Expert-Parallel Load Balancing Across Memory- and Compute-Bound Regimes as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.13057v2
  - Applies to: `2608.13057-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.13057v2
  - Applies to: `2608.13057-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.13057v2
  - Applies to: `2608.13057-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.13057
  - Applies to: `2608.13057-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Jie Li
  - arXiv author search: https://arxiv.org/search/?query=Jie%20Li&searchtype=author
  - Applies to: the reviewed paper and `2608.13057-whitepaper-review.md`.
- Author: Chenxin Jia
  - arXiv author search: https://arxiv.org/search/?query=Chenxin%20Jia&searchtype=author
  - Applies to: the reviewed paper and `2608.13057-whitepaper-review.md`.
- Author: Jinliang Shen
  - arXiv author search: https://arxiv.org/search/?query=Jinliang%20Shen&searchtype=author
  - Applies to: the reviewed paper and `2608.13057-whitepaper-review.md`.
- Author: Cunzhuang Liu
  - arXiv author search: https://arxiv.org/search/?query=Cunzhuang%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2608.13057-whitepaper-review.md`.
- Author: Ruiyi Ding
  - arXiv author search: https://arxiv.org/search/?query=Ruiyi%20Ding&searchtype=author
  - Applies to: the reviewed paper and `2608.13057-whitepaper-review.md`.
- Author: Jianwen Xian
  - arXiv author search: https://arxiv.org/search/?query=Jianwen%20Xian&searchtype=author
  - Applies to: the reviewed paper and `2608.13057-whitepaper-review.md`.
- Author: Kang He
  - arXiv author search: https://arxiv.org/search/?query=Kang%20He&searchtype=author
  - Applies to: the reviewed paper and `2608.13057-whitepaper-review.md`.
- Author: Chengru Song
  - arXiv author search: https://arxiv.org/search/?query=Chengru%20Song&searchtype=author
  - Applies to: the reviewed paper and `2608.13057-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
