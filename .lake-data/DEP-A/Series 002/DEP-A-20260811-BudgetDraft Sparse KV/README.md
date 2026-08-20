# DEP-A-20260811-BudgetDraft Sparse KV

#artificial-intelligence #speculative-decoding #KV-cache #multi-budget-training #acceptance-rate #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.00144v1, *BudgetDraft: Acceptance-Aware Multi-View Training for Sparse-KV Speculative Decoding*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.00144-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.00144-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We propose BudgetDraft, which combines acceptance-aware alignment with multi-budget sparse-view training to produce a budget-invariant drafter that recovers acceptance rates across all sparsity levels. BudgetDraft uses acceptance-aware top-1 supervision together with multi-view sparse training under multi-view KV sampling, making the drafter robust to sparse-cache conditions and budget variation in deployment. BudgetDraft: Acceptance-Aware Multi-View Training for Sparse-KV Speculative Decoding Liang He 1,∗ Jingbo Wen 2 Qishi Zhan 3 Yixiong Chen 4 Kangning Cui 5 Qizhen Lan 6 Xilu Wang 7,∗ 1 Shanghai Institute of Optics and Fine Mechanics 2 The University of Sydney 3 Marquette University 4 Johns Hopkins University 5 Wake Forest University 6 University of Texas Health Science Center at Houston 7 University of Surrey hel@siom.ac.cn, wangxilu@surrey.ac.uk ∗ Corresponding authors

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate multi-budget speculative drafting as an acceptance-controlled policy: log sampled training budgets, sparse views, teacher targets, verifier acceptances, rejected spans, KV memory, and end-to-end latency, then fall back to ordinary autoregressive decoding when acceptance or speedup leaves the validated envelope.

## Associated DEP Records

- [DEP-A-20260805-Speculative PrePosition](../DEP-A-20260805-Speculative%20PrePosition/README.md) - direct speculative inference and position-sensitive acceleration context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260810-AB Sparse Attention](../DEP-A-20260810-AB%20Sparse%20Attention/README.md) - direct adaptive sparse-attention and long-context evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.00144v1
  - Applies to: `2606.00144-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.00144v1
  - Applies to: `2606.00144-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.00144v1
  - Applies to: `2606.00144-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.00144
  - Applies to: `2606.00144-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Liang He
  - arXiv author search: https://arxiv.org/search/?query=Liang%20He&searchtype=author
  - Applies to: the reviewed paper and `2606.00144-whitepaper-review.md`.
- Author: Jingbo Wen
  - arXiv author search: https://arxiv.org/search/?query=Jingbo%20Wen&searchtype=author
  - Applies to: the reviewed paper and `2606.00144-whitepaper-review.md`.
- Author: Qishi Zhan
  - arXiv author search: https://arxiv.org/search/?query=Qishi%20Zhan&searchtype=author
  - Applies to: the reviewed paper and `2606.00144-whitepaper-review.md`.
- Author: Yixiong Chen
  - arXiv author search: https://arxiv.org/search/?query=Yixiong%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.00144-whitepaper-review.md`.
- Author: Kangning Cui
  - arXiv author search: https://arxiv.org/search/?query=Kangning%20Cui&searchtype=author
  - Applies to: the reviewed paper and `2606.00144-whitepaper-review.md`.
- Author: Qizhen Lan
  - arXiv author search: https://arxiv.org/search/?query=Qizhen%20Lan&searchtype=author
  - Applies to: the reviewed paper and `2606.00144-whitepaper-review.md`.
- Author: Xilu Wang
  - arXiv author search: https://arxiv.org/search/?query=Xilu%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.00144-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
