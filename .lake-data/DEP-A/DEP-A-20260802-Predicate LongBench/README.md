# DEP-A-20260802-Predicate LongBench

#artificial-intelligence #long-context #benchmarking #reasoning #difficulty-analysis #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.08284v1, *Understanding Axes of Difficulty For Long Context Tasks Via PredicateLongBench*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.08284-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.08284-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Motivated by this state of affairs, we present PredicateLongBench , a new family of tasks that retains simplicity while combining different approaches to scale difficulty across multiple axes. Our main contributions are as follows: (1) We present PredicateLongBench , a family of tasks that are algorithmically simple yet pose a challenge for frontier LLMs, (2) We systematically define and explore multiple axes for increasing task difficulty and present variants of simple retrieval tasks that scale the difficulty across these axes, (3) We devise predicates for constraint satisfaction that allow us to scale the difficulty of simple retrieval tasks along these axes, (4) We conduct experiments on the structure of the context (specifically distractors) and show that the structure has a large impact on frontier model peformance on these tasks, (5) We explore increasing difficulty along a new axis, namely, search space, which can be scaled up even while keeping context token budgets fixed. We find that frontier models struggle to perform well as we scale up the difficulty of tasks along our axes, demonstrating the utility of our benchmark in understanding the limitations of current long-context capabilities.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat long-context evaluation as a difficulty surface rather than one aggregate score: version every predicate generator, axis setting, context distribution, and exact answer, then require monotonicity checks and adversarial boundary cases before claiming context gains.

## Associated DEP Records

- [DEP-A-20260717-Constrained LongEval](../DEP-A-20260717-Constrained%20LongEval/README.md) - direct long-context evaluation and benchmark-design context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.08284v1
  - Applies to: `2607.08284-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.08284v1
  - Applies to: `2607.08284-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.08284v1
  - Applies to: `2607.08284-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.08284
  - Applies to: `2607.08284-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Siddhartha Jain
  - arXiv author search: https://arxiv.org/search/?query=Siddhartha%20Jain&searchtype=author
  - Applies to: the reviewed paper and `2607.08284-whitepaper-review.md`.
- Author: Ameya Velingker
  - arXiv author search: https://arxiv.org/search/?query=Ameya%20Velingker&searchtype=author
  - Applies to: the reviewed paper and `2607.08284-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
