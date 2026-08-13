# DEP-A-20260801-Cross Layer Sparse Attn

#artificial-intelligence #sparse-attention #cross-layer-routing #long-context #efficiency #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.06467v1, *You Only Index Once: Cross-Layer Sparse Attention with Shared Routing*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.06467-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.06467-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: This sparse index is also produced only once and is shared across the following cross-decoder layers, allowing them to reuse the same selected KV positions instead of recomputing layer-specific sparse routing. This overview highlights the main design principle of cross-layer sparse attention: when several decoder layers read from the same memory, the expensive routing decision should also be tied to that memory and shared across layers. Through KV sharing, it retains YOCO’s advantages in pre-filling and KV-cache storage, while shared-index sparse retrieval improves decoding efficiency by avoiding repeated dense global attention and repeatedly recomputed routing.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: View cross-layer shared routing as an amortized index decision: retain the originating layer evidence, reuse span, divergence signal, and repair path, then measure when one index remains semantically adequate and when layer-specific attention requires recomputation.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.06467v1
  - Applies to: `2606.06467-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.06467v1
  - Applies to: `2606.06467-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.06467v1
  - Applies to: `2606.06467-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.06467
  - Applies to: `2606.06467-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yutao Sun
  - arXiv author search: https://arxiv.org/search/?query=Yutao%20Sun&searchtype=author
  - Applies to: the reviewed paper and `2606.06467-whitepaper-review.md`.
- Author: Yanqi Zhang
  - arXiv author search: https://arxiv.org/search/?query=Yanqi%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.06467-whitepaper-review.md`.
- Author: Li Dong
  - arXiv author search: https://arxiv.org/search/?query=Li%20Dong&searchtype=author
  - Applies to: the reviewed paper and `2606.06467-whitepaper-review.md`.
- Author: Jianyong Wang
  - arXiv author search: https://arxiv.org/search/?query=Jianyong%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.06467-whitepaper-review.md`.
- Author: Furu Wei
  - arXiv author search: https://arxiv.org/search/?query=Furu%20Wei&searchtype=author
  - Applies to: the reviewed paper and `2606.06467-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
