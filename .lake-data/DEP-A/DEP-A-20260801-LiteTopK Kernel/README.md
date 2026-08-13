# DEP-A-20260801-LiteTopK Kernel

#artificial-intelligence #top-k #sparse-attention #GPU-kernels #long-context #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.11976v2, *LiteTopK: Exploiting the Curse of Dimensionality for a Fused Indexer-TopK Kernel in Long-Context Sparse Attention*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.11976-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.11976-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: To address this issue, we study the distribution of the scores in sparse attention and observe that these scores consistently show a concentration phenomenon, which is brought by the curse of dimensionality in a high-dimensional space (Weber et al. In summary, this work makes the following contributions: We are the first to observe and characterize the distance concentration phenomenon in sparse attention, trace its origin to the well-known curse of dimensionality in high-dimensional spaces, and further exploit this property to improve sparse attention kernel design. We propose LiteTopK, the first indexer-TopK fused kernel, which substantially reduces write-back memory pressure and achieves a 1.24 × 1.24\times speedup over the fastest existing DSA kernel.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat the fused indexer-TopK kernel as a distribution-dependent selection primitive: record dimensionality, score distribution, candidate reduction, exactness checks, and fallback, then test adversarially clustered or low-dimensional regimes where concentration-of-measure assumptions may fail.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.11976v2
  - Applies to: `2607.11976-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.11976v2
  - Applies to: `2607.11976-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.11976v2
  - Applies to: `2607.11976-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.11976
  - Applies to: `2607.11976-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/Heisenberg-Yin/LiteTopK
  - Applies to: reproducibility context in `2607.11976-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://flashml-org.github.io/
  - Applies to: reproducibility context in `2607.11976-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Ziqi Yin
  - arXiv author search: https://arxiv.org/search/?query=Ziqi%20Yin&searchtype=author
  - Applies to: the reviewed paper and `2607.11976-whitepaper-review.md`.
- Author: Jianyang Gao
  - arXiv author search: https://arxiv.org/search/?query=Jianyang%20Gao&searchtype=author
  - Applies to: the reviewed paper and `2607.11976-whitepaper-review.md`.
- Author: Peiqi Yin
  - arXiv author search: https://arxiv.org/search/?query=Peiqi%20Yin&searchtype=author
  - Applies to: the reviewed paper and `2607.11976-whitepaper-review.md`.
- Author: Jiangneng Li
  - arXiv author search: https://arxiv.org/search/?query=Jiangneng%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.11976-whitepaper-review.md`.
- Author: Gao Cong
  - arXiv author search: https://arxiv.org/search/?query=Gao%20Cong&searchtype=author
  - Applies to: the reviewed paper and `2607.11976-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
