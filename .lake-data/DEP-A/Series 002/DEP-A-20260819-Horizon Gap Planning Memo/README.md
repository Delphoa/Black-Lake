# DEP-A-20260819-Horizon Gap Planning Memo

#artificial-intelligence #arXiv #paper-review #memory #agents #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.06663v1, *The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.06663-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.06663-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We organize the survey around six categories that track a task’s lifecycle: planning decides what to do (§3); memory decides what information that decision draws on (§4); execution control decides how the resulting actions are run and recovered from when they fail (§5); training decides how the underlying policy learns to act well over many steps (§6); evaluation decides whether any of this actually works (§7); and foundations covers the theory of why long horizons degrade performance at all, and the oversight problem of running an agent for a long time without a human watching every step (§8). (1) A disambiguation of long-horizon, long-context, and long-term memory, and a six-category taxonomy — planning, memory, execution, training, evaluation, foundations — crossed with a second axis (where the horizon is carried: within-context, within-task-beyond- context, or cross-task-persistent) that organizes every technical section (§2). This survey’s delta is to organize instead around horizon as the cross-cutting axis: rather than asking “what memory mechanisms exist” or “what planning strategies exist” in isolation, we ask, for every stage of the pipeline, what breaks first as the required horizon grows, and what compensates — which.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.06663v1
  - Applies to: `2608.06663-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.06663v1
  - Applies to: `2608.06663-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.06663v1
  - Applies to: `2608.06663-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.06663
  - Applies to: `2608.06663-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Mingguang Chen
  - arXiv author search: https://arxiv.org/search/?query=Mingguang%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2608.06663-whitepaper-review.md`.
- Author: Licheng Wang
  - arXiv author search: https://arxiv.org/search/?query=Licheng%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2608.06663-whitepaper-review.md`.
- Author: Bo Qu
  - arXiv author search: https://arxiv.org/search/?query=Bo%20Qu&searchtype=author
  - Applies to: the reviewed paper and `2608.06663-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
