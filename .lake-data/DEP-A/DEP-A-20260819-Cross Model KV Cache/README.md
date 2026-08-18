# DEP-A-20260819-Cross Model KV Cache

#artificial-intelligence #arXiv #paper-review #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.03893v1, *Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.03893-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.03893-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Figure 1: Cross-model KV cache transfer pipeline. Building on this observation, we propose a closed-form per-head ridge mapper (§ 3 ) that combines three components: per-head ridge regression fit from a small calibration set, cross-layer source selection where each target layer draws from its top- k k most predictive source layers, and content-space (RoPE-stripped) mapping that decouples positional rotation from semantic content so the fit transfers across context lengths. We propose a gradient-free framework for cross-model KV cache transfer based on per-head ridge regression.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping for Prefill Reuse as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260812-KVBuffer Serving](../DEP-A-20260812-KVBuffer%20Serving/README.md) - direct decode-time KV-cache serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.03893v1
  - Applies to: `2608.03893-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.03893v1
  - Applies to: `2608.03893-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.03893v1
  - Applies to: `2608.03893-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2608.03893
  - Applies to: `2608.03893-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Taekyung Heo
  - arXiv author search: https://arxiv.org/search/?query=Taekyung%20Heo&searchtype=author
  - Applies to: the reviewed paper and `2608.03893-whitepaper-review.md`.
- Author: Rasoul Shafipour
  - arXiv author search: https://arxiv.org/search/?query=Rasoul%20Shafipour&searchtype=author
  - Applies to: the reviewed paper and `2608.03893-whitepaper-review.md`.
- Author: Ritchie Zhao
  - arXiv author search: https://arxiv.org/search/?query=Ritchie%20Zhao&searchtype=author
  - Applies to: the reviewed paper and `2608.03893-whitepaper-review.md`.
- Author: Maximilian Golub
  - arXiv author search: https://arxiv.org/search/?query=Maximilian%20Golub&searchtype=author
  - Applies to: the reviewed paper and `2608.03893-whitepaper-review.md`.
- Author: Mohammad Mahdi Kamani
  - arXiv author search: https://arxiv.org/search/?query=Mohammad%20Mahdi%20Kamani&searchtype=author
  - Applies to: the reviewed paper and `2608.03893-whitepaper-review.md`.
- Author: Ritika Borkar
  - arXiv author search: https://arxiv.org/search/?query=Ritika%20Borkar&searchtype=author
  - Applies to: the reviewed paper and `2608.03893-whitepaper-review.md`.
- Author: Makesh Tarun Chandran
  - arXiv author search: https://arxiv.org/search/?query=Makesh%20Tarun%20Chandran&searchtype=author
  - Applies to: the reviewed paper and `2608.03893-whitepaper-review.md`.
- Author: Pantea Zardoshti
  - arXiv author search: https://arxiv.org/search/?query=Pantea%20Zardoshti&searchtype=author
  - Applies to: the reviewed paper and `2608.03893-whitepaper-review.md`.
- Author: Bita Darvish Rouhani
  - arXiv author search: https://arxiv.org/search/?query=Bita%20Darvish%20Rouhani&searchtype=author
  - Applies to: the reviewed paper and `2608.03893-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
