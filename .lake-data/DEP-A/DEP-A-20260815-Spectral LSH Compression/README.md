# DEP-A-20260815-Spectral LSH Compression

#artificial-intelligence #prompt-compression #locality-sensitive-hashing #Krylov-methods #long-context #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.19368v1, *Spectral-LSH: Sub-Quadratic Prompt Compression via Krylov-Projected Locality-Sensitive Hashing*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.19368-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.19368-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: 3.1 Preliminaries 3.2 Efficient Krylov Eigen-Decomposition via Random Fourier Features 3.3 Spectral-LSH: Hashing in the Attention Eigenspace 3.4 Macro-Token Construction and Positional Aggregation 3.5 Compression Backends 3.6 Adaptive Backend: Routing Between Chunk and Spectral Clustering 3.7 Theoretical Complexity 4.1 Kernel Approximation Error 4.2 Krylov Convergence 4.3 Spectral-LSH Collision Guarantee 5.1 Experimental Setup Two-regime generalization across model families. Algorithm 1 Spectral-LSH Prompt Compression Algorithm 2 Implicit Lanczos for Attention Operator After projecting tokens into the attention eigenspace, we obtain Z ∈ ℝ N × k Z\in\mathbb{R}^{N\times k} . This is why the paper treats Spectral-LSH as a compression heuristic based on attention-like similarity rather than as an exact approximation to the first-layer attention matrix.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Spectral-LSH: Sub-Quadratic Prompt Compression via Krylov-Projected Locality-Sensitive Hashing as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260715-Prompt Compression Wild](../DEP-A-20260715-Prompt%20Compression%20Wild/README.md) - direct prompt-compression evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.19368v1
  - Applies to: `2607.19368-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.19368v1
  - Applies to: `2607.19368-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.19368v1
  - Applies to: `2607.19368-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.19368
  - Applies to: `2607.19368-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Ali Mahdavi
  - arXiv author search: https://arxiv.org/search/?query=Ali%20Mahdavi&searchtype=author
  - Applies to: the reviewed paper and `2607.19368-whitepaper-review.md`.
- Author: Azaseh Zamanifar
  - arXiv author search: https://arxiv.org/search/?query=Azaseh%20Zamanifar&searchtype=author
  - Applies to: the reviewed paper and `2607.19368-whitepaper-review.md`.
- Author: Amirfarhad Farhadi
  - arXiv author search: https://arxiv.org/search/?query=Amirfarhad%20Farhadi&searchtype=author
  - Applies to: the reviewed paper and `2607.19368-whitepaper-review.md`.
- Author: Omid Kashefi
  - arXiv author search: https://arxiv.org/search/?query=Omid%20Kashefi&searchtype=author
  - Applies to: the reviewed paper and `2607.19368-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
