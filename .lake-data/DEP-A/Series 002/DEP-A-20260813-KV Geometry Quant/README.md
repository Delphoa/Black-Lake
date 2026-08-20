# DEP-A-20260813-KV Geometry Quant

#artificial-intelligence #KV-cache #quantization #representation-geometry #regularization #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.17019v1, *Regularize or Localize: When Training-Time KV-Cache Geometry Pays Under Quantization*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.17019-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.17019-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Stage 3 measures the payoff of A1’s directly regularized cache under post-hoc quantization. Under untransformed symmetric group-free quantization the directly regularized model is the only training condition that prefers per-channel over per-token scaling, and its 3-bit symmetric per-channel damage is 4.3 4.3 – 7.9 × 7.9\times smaller than the baseline’s; under the full simulated KIVI-style configuration (mixed arrangement, zero-points, grouped scales), all models reach near-parity (§ 5.5 ). , 2026 ) ), but none regularize the geometry of a standard attention cache during training.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat training-time KV geometry as quantizer-specific co-design: preserve regularizer placement, seed, cache anisotropy, quantizer layout, metadata overhead, and delta-NLL, and reject broad benefits when stronger grouped quantizers erase the advantage.

## Associated DEP Records

- [DEP-A-20260810-MomentKV](../DEP-A-20260810-MomentKV/README.md) - direct long-context KV-cache eviction and retention context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.17019v1
  - Applies to: `2607.17019-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.17019v1
  - Applies to: `2607.17019-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.17019v1
  - Applies to: `2607.17019-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.17019
  - Applies to: `2607.17019-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Libo Sun
  - arXiv author search: https://arxiv.org/search/?query=Libo%20Sun&searchtype=author
  - Applies to: the reviewed paper and `2607.17019-whitepaper-review.md`.
- Author: Po-Wei Harn
  - arXiv author search: https://arxiv.org/search/?query=Po-Wei%20Harn&searchtype=author
  - Applies to: the reviewed paper and `2607.17019-whitepaper-review.md`.
- Author: Zewei Zhang
  - arXiv author search: https://arxiv.org/search/?query=Zewei%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.17019-whitepaper-review.md`.
- Author: Peixiong He
  - arXiv author search: https://arxiv.org/search/?query=Peixiong%20He&searchtype=author
  - Applies to: the reviewed paper and `2607.17019-whitepaper-review.md`.
- Author: Xiao Qin
  - arXiv author search: https://arxiv.org/search/?query=Xiao%20Qin&searchtype=author
  - Applies to: the reviewed paper and `2607.17019-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
