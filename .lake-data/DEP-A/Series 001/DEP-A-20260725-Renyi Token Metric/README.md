# DEP-A-20260725-Renyi Token Metric

#artificial-intelligence #vision-transformers #token-pruning #Renyi-entropy #efficient-inference #multimodal-models

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2603.27900v1, *RÃ©nyi Entropy: A New Token Pruning Metric for Vision Transformers*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2603.27900-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2603.27900-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Col-Ln replaces early-layer CLS attention with a training-free column L-n norm derived from Renyi entropy. It treats attention contributed collectively by all query tokens as the importance signal, so pruning can begin before the class token has developed mature semantics.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat early pruning as a confidence-controlled transition: compare CLS and collective scores, defer pruning when they disagree sharply, and retain a recovery map for later layers.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct efficient-attention and token-budget context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2603.27900v1
  - Applies to: `2603.27900-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2603.27900v1
  - Applies to: `2603.27900-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2603.27900v1
  - Applies to: `2603.27900-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2603.27900
  - Applies to: `2603.27900-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/Wayne0758/SparseAttention
  - Applies to: reproducibility context in `2603.27900-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Wei-Yuan Su
  - arXiv author search: https://arxiv.org/search/?query=Wei-Yuan%20Su&searchtype=author
  - Applies to: the reviewed paper and `2603.27900-whitepaper-review.md`.
- Author: Ruijie Zhang
  - arXiv author search: https://arxiv.org/search/?query=Ruijie%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2603.27900-whitepaper-review.md`.
- Author: Zheng Zhang
  - arXiv author search: https://arxiv.org/search/?query=Zheng%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2603.27900-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
