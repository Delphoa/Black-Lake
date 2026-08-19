# DEP-A-20260819-SAGE SLO Aware Adaptive

#artificial-intelligence #arXiv #paper-review #RAG #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.08237v1, *SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.08237-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.08237-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: While these approaches demonstrate that adaptive retrieval can improve factuality and efficiency, they are not directly optimized for production SLOs: many require additional LLM calls, involve complex multi-step protocols, or optimize surrogate objectives that only indirectly reflect latency percentiles and cost. We introduce SAGE, an SLO-aware adaptive retrieval policy that predicts, for each query, an appropriate retrieval budget k k before generation. Our contributions are threefold: (1) we formulate production RAG deployment as a decision problem under explicit latency and cost SLOs, exposing why fixed- k k retrieval is misaligned with heterogeneous query difficulty; (2) we propose SAGE, a learned SLO-aware adaptive retrieval policy that uses only retrieval-side features and offline labels from budget sweeps to select query-specific budgets with negligible runtime overhead; and (3) we provide an extensive empirical study showing that SAGE substantially improves SLO compliance and latency, reduces retrieval cost, and generalizes across datasets and LLM families without retraining, making it a practical building block for production RAG systems.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.08237v1
  - Applies to: `2608.08237-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.08237v1
  - Applies to: `2608.08237-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.08237v1
  - Applies to: `2608.08237-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.1109/CoDIT70676.2026.11631166
  - Applies to: `2608.08237-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Muhammad Faizan Raza
  - arXiv author search: https://arxiv.org/search/?query=Muhammad%20Faizan%20Raza&searchtype=author
  - Applies to: the reviewed paper and `2608.08237-whitepaper-review.md`.
- Author: Shuo
  - arXiv author search: https://arxiv.org/search/?query=Shuo&searchtype=author
  - Applies to: the reviewed paper and `2608.08237-whitepaper-review.md`.
- Author: Yang
  - arXiv author search: https://arxiv.org/search/?query=Yang&searchtype=author
  - Applies to: the reviewed paper and `2608.08237-whitepaper-review.md`.
- Author: Satish Mahadevan Srinivasan
  - arXiv author search: https://arxiv.org/search/?query=Satish%20Mahadevan%20Srinivasan&searchtype=author
  - Applies to: the reviewed paper and `2608.08237-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
