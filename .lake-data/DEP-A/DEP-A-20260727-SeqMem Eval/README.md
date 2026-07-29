# DEP-A-20260727-SeqMem Eval

#artificial-intelligence #agent-memory #continual-learning #forgetting #benchmarking #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.15384v1, *Is One Score Enough? Rethinking the Evaluation of Sequentially Evolving LLM Memory*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.15384-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.15384-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: SeqMem-Eval evaluates external prompt-mediated memory as it evolves over a stream of tasks, replacing one terminal score with diagnostics for online utility, hold-out generalization, backward transfer, forgetting, and efficiency. It examines the full performance trajectory and retained competence rather than only the final memory state.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Turn the diagnostics into a memory-update gate: accept an update only if estimated online benefit exceeds predicted backward-transfer and forgetting risk on a rolling sentinel set. Falsification would be terminal accuracy reliably predicting all diagnostic dimensions across shuffled orders and held-out tasks.

## Associated DEP Records

- [DEP-A-20260719-Agent Memory Benchmark](../DEP-A-20260719-Agent%20Memory%20Benchmark/README.md) - direct agent-memory benchmark and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.15384v1
  - Applies to: `2605.15384-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.15384v1
  - Applies to: `2605.15384-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.15384v1
  - Applies to: `2605.15384-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.15384
  - Applies to: `2605.15384-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/ShenGroup/SeqMem-Eval
  - Applies to: reproducibility context in `2605.15384-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Songwei Dong
  - arXiv author search: https://arxiv.org/search/?query=Songwei%20Dong&searchtype=author
  - Applies to: the reviewed paper and `2605.15384-whitepaper-review.md`.
- Author: Zihan Chen
  - arXiv author search: https://arxiv.org/search/?query=Zihan%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2605.15384-whitepaper-review.md`.
- Author: Chengshuai Shi
  - arXiv author search: https://arxiv.org/search/?query=Chengshuai%20Shi&searchtype=author
  - Applies to: the reviewed paper and `2605.15384-whitepaper-review.md`.
- Author: Peng Wang
  - arXiv author search: https://arxiv.org/search/?query=Peng%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2605.15384-whitepaper-review.md`.
- Author: Jundong Li
  - arXiv author search: https://arxiv.org/search/?query=Jundong%20Li&searchtype=author
  - Applies to: the reviewed paper and `2605.15384-whitepaper-review.md`.
- Author: Cong Shen
  - arXiv author search: https://arxiv.org/search/?query=Cong%20Shen&searchtype=author
  - Applies to: the reviewed paper and `2605.15384-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
