# DEP-A-20260814-KATA Linear Attention

#artificial-intelligence #linear-attention #kernel-methods #associative-memory #long-context #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.17419v1, *Kernelized Linear Attention: Breaking the Capacity Wall with Symmetric Cones*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.17419-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.17419-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Linear attention must retain the feature–value state: so its dominant storage is n ​ d v nd_{v} ; the feature width alone understates the memory cost. Based ( arora24based ) approximates exp ⁡ ( ⟨ 𝒒 , 𝒌 ⟩ ) \exp(\langle{\bm{q}},{\bm{k}}\rangle) by a degree- 2 2 Taylor map paired with sliding-window attention; LoLA ( mcdermott25lola ) , the Associative Memory layer ( krotov25mam ) , and the GatedDeltaNet-H1/H2 stacks ( yang25gateddeltanet ) concede the pure linear path and reintroduce a small KV cache. We formulate attention recall as a spherical-packing problem and introduce Kernelized Linear Attention Activations (KATA), a framework whose feature maps are derived from first principles by certifying nonnegative attention weights through a self-dual homogeneous cone.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Interpret conic feature maps as geometry-constrained associative state design: audit nonnegativity, interference floors, state size, recurrent updates, and kernel cost, then test whether capacity predictions hold beyond synthetic recall and matched parameter budgets.

## Associated DEP Records

- [DEP-A-20260810-AB Sparse Attention](../DEP-A-20260810-AB%20Sparse%20Attention/README.md) - direct adaptive sparse-attention and long-context evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.17419v1
  - Applies to: `2607.17419-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.17419v1
  - Applies to: `2607.17419-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.17419v1
  - Applies to: `2607.17419-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.17419
  - Applies to: `2607.17419-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/ayghri/kata
  - Applies to: reproducibility context in `2607.17419-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Ayoub Ghriss
  - arXiv author search: https://arxiv.org/search/?query=Ayoub%20Ghriss&searchtype=author
  - Applies to: the reviewed paper and `2607.17419-whitepaper-review.md`.
- Author: Sourav Chakraborty
  - arXiv author search: https://arxiv.org/search/?query=Sourav%20Chakraborty&searchtype=author
  - Applies to: the reviewed paper and `2607.17419-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
