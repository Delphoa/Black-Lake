# DEP-A-20260819-Practical Online KV Cache

#artificial-intelligence #arXiv #paper-review #KV-cache #agents #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.00902v1, *Practical Online KV Cache Compaction for LLM Agents: An Empirical Study*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.00902-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.00902-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: On Gemma-4-31B , both methods slightly exceed the baseline, which partly reflects the fact that some no-compaction trajectories run out of memory even at batch size 1, whereas compaction keeps their KV caches within the limit. To study this design space, we present a systematic empirical evaluation of how existing KV cache compaction methods behave when adapted to agent tasks. 5.1 Task Performance and Serving Efficiency on Larger Models 5.2 Behavioral Effects of Compaction 6 Conclusion References A.1 Package and Hardware A.2 Generation Hyperparameters A.3 Compaction Algorithm Details A.4 Evaluation Details A.5 Bootstrap Confidence Intervals A.6 Full Results on Larger Models A.7 Larger-Model Serving Simulation A large body of work reduces KV memory by retaining only selected cached tokens.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Practical Online KV Cache Compaction for LLM Agents: An Empirical Study as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260812-KVBuffer Serving](../DEP-A-20260812-KVBuffer%20Serving/README.md) - direct decode-time KV-cache serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.00902v1
  - Applies to: `2608.00902-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.00902v1
  - Applies to: `2608.00902-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.00902v1
  - Applies to: `2608.00902-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2608.00902
  - Applies to: `2608.00902-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yujian Liu
  - arXiv author search: https://arxiv.org/search/?query=Yujian%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2608.00902-whitepaper-review.md`.
- Author: Jiabao Ji
  - arXiv author search: https://arxiv.org/search/?query=Jiabao%20Ji&searchtype=author
  - Applies to: the reviewed paper and `2608.00902-whitepaper-review.md`.
- Author: Li An
  - arXiv author search: https://arxiv.org/search/?query=Li%20An&searchtype=author
  - Applies to: the reviewed paper and `2608.00902-whitepaper-review.md`.
- Author: Rohit Jain
  - arXiv author search: https://arxiv.org/search/?query=Rohit%20Jain&searchtype=author
  - Applies to: the reviewed paper and `2608.00902-whitepaper-review.md`.
- Author: Gungor Polatkan
  - arXiv author search: https://arxiv.org/search/?query=Gungor%20Polatkan&searchtype=author
  - Applies to: the reviewed paper and `2608.00902-whitepaper-review.md`.
- Author: Siyu Zhu
  - arXiv author search: https://arxiv.org/search/?query=Siyu%20Zhu&searchtype=author
  - Applies to: the reviewed paper and `2608.00902-whitepaper-review.md`.
- Author: Shiyu Chang
  - arXiv author search: https://arxiv.org/search/?query=Shiyu%20Chang&searchtype=author
  - Applies to: the reviewed paper and `2608.00902-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
