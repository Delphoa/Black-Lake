# DEP-A-20260819-When Does Memory Help

#artificial-intelligence #arXiv #paper-review #memory #agents #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.28224v1, *When Does Memory Help Multi-Trajectory Inference for Tool-Use LLM Agents?*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.28224-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.28224-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: This setting supports both memory abstractions (observational feedback for fact extraction; error signals for reflection) and exposes a structural constraint: when the environment is non-serializable ( 21 ) (state cannot be forked), beam search and MCTS are infeasible, leaving memory-augmented best-of- N N as the only viable multi-trajectory strategy. We propose a unified framework that decomposes memory along the scope × \times abstraction axes, derives four memory methods as concrete instantiations, and evaluates them in an experiment matrix ( 4 4 memory methods × \times 3 3 inference strategies × \times 4 4 benchmarks spanning 3 3 tool-use environments, minus structurally inadmissible combinations). Three findings on when memory helps: (F1) memory’s accuracy effect is search-method-dependent — Reflection reaches significance only under MCTS, while cross-sibling injection helps only diversity-starved beam search; (F2) under MCTS on the harder benchmark (KGQA), Reflection and Raw Sibling produce statistically indistinguishable accuracy despite operating on different memory abstractions; (F3) fact extraction is accuracy-neutral but improves efficiency on tasks with reusable environmental structure (§ 5 ).

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat When Does Memory Help Multi-Trajectory Inference for Tool-Use LLM Agents? as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.28224v1
  - Applies to: `2605.28224-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.28224v1
  - Applies to: `2605.28224-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.28224v1
  - Applies to: `2605.28224-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2605.28224
  - Applies to: `2605.28224-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Xinzhe Li
  - arXiv author search: https://arxiv.org/search/?query=Xinzhe%20Li&searchtype=author
  - Applies to: the reviewed paper and `2605.28224-whitepaper-review.md`.
- Author: Yaguang Tao
  - arXiv author search: https://arxiv.org/search/?query=Yaguang%20Tao&searchtype=author
  - Applies to: the reviewed paper and `2605.28224-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
