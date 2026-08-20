# DEP-A-20260819-TopoGuard Graph Theory Ba

#artificial-intelligence #arXiv #paper-review #RAG #security #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.20437v1, *TopoGuard: Graph Theory Based Defenses Against Split-Knowledge Attacks on RAG*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.20437-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.20437-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We show, via experiments, that existing defense filters remain ineffective against split-knowledge attacks, even when provided with the full concatenated retrieval context. ( 2023 ) to classify split-knowledge attacks 1 1 1 All text-based baselines (TextFilter, LlamaGuard-2/3, LLM-as-a-Judge) score the full retrieval context as a single concatenated input rather than per-document, so their AUROC reflects the structural nature of split-knowledge attacks rather than an artifact of independent document scoring. We design four split-knowledge attack detectors based on Spectral Gap ( λ 2 \lambda_{2} ), Fiedler Conductance, Modularity, and an entity-augmented hybrid (TopoGuard- λ 2 \lambda_{2} +Entity), which score retrieved documents and can achieve higher accuracy against existing baselines.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat TopoGuard: Graph Theory Based Defenses Against Split-Knowledge Attacks on RAG as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.20437v1
  - Applies to: `2607.20437-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.20437v1
  - Applies to: `2607.20437-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.20437v1
  - Applies to: `2607.20437-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.20437
  - Applies to: `2607.20437-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Chahana Dahal
  - arXiv author search: https://arxiv.org/search/?query=Chahana%20Dahal&searchtype=author
  - Applies to: the reviewed paper and `2607.20437-whitepaper-review.md`.
- Author: Zuobin Xiong
  - arXiv author search: https://arxiv.org/search/?query=Zuobin%20Xiong&searchtype=author
  - Applies to: the reviewed paper and `2607.20437-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
