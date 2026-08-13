# DEP-A-20260806-Ragged ViT Attention

#artificial-intelligence #vision-transformers #ragged-attention #token-pruning #GPU-kernels #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2604.15408v2, *Dispatch-Aware Ragged Attention for Pruned Vision Transformers*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2604.15408-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2604.15408-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Our system consists of three components: (1) a fused token packer, (2) a bidirectional ragged attention kernel, and (3) integration into end-to-end pruned ViT inference. FlashAttention-2 [ 8 ] provides such an API ( flash_attn_varlen_func ), and PyTorch’s NestedTensor path [ 10 ] offers a framework-native alternative. PyTorch’s NestedTensor SDPA [ 10 ] provides a framework-native ragged attention path.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Dispatch-Aware Ragged Attention for Pruned Vision Transformers as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260801-Collaborative VLM Prune](../DEP-A-20260801-Collaborative%20VLM%20Prune/README.md) - direct vision-language efficiency and pruning context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2604.15408v2
  - Applies to: `2604.15408-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2604.15408v2
  - Applies to: `2604.15408-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2604.15408v2
  - Applies to: `2604.15408-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2604.15408
  - Applies to: `2604.15408-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/saifmb0/sparse-vits
  - Applies to: reproducibility context in `2604.15408-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Seifeldin Abdellatif
  - arXiv author search: https://arxiv.org/search/?query=Seifeldin%20Abdellatif&searchtype=author
  - Applies to: the reviewed paper and `2604.15408-whitepaper-review.md`.
- Author: Ahmad Almasri
  - arXiv author search: https://arxiv.org/search/?query=Ahmad%20Almasri&searchtype=author
  - Applies to: the reviewed paper and `2604.15408-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
