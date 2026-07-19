# DEP-A-20260718-SpotAttention Routing

#artificial-intelligence #sparse-attention #long-context #routing #KV-cache #quantization

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.22874v1, *SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.22874-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.22874-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: SpotAttention attaches a lightweight selector to frozen pretrained attention and distills the backbone attention distribution with KL divergence. It chooses sparse blocks through fixed top-K or a dual top-p rule that allocates per-query, per-layer budgets, while the selector key cache can be quantized.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: calibrate top-p by service risk and layer sensitivity, while logging selected mass, achieved blocks, selector cost, quantization format, and dense-shadow outcomes per request.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.22874v1
  - Applies to: `2606.22874-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.22874v1
  - Applies to: `2606.22874-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.22874v1
  - Applies to: `2606.22874-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.22874
  - Applies to: `2606.22874-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Huzama Ahmad
  - arXiv author search: https://arxiv.org/search/?query=Huzama%20Ahmad&searchtype=author
  - Applies to: the reviewed paper and `2606.22874-whitepaper-review.md`.
- Author: Se-Young Yun
  - arXiv author search: https://arxiv.org/search/?query=Se-Young%20Yun&searchtype=author
  - Applies to: the reviewed paper and `2606.22874-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
