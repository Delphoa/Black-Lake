# DEP-A-20260718-Keyless Attention

#artificial-intelligence #attention #KV-cache #value-space #transformers #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.21848v1, *Keyless Attention: Value-Space Routing and Value-Only Caching for Efficient Transformers*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.21848-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.21848-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Keyless Attention removes the key projection and routes queries directly in value space, producing a Value-Only Cache. At factorization depth three, a learned value-space routing matrix replaces the key projection while keeping the same projection-matrix count as standard QKV attention.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: evaluate keyless layers as a selectively deployed architectural option, with total-memory and end-to-end throughput accounting plus dense-QKV fallback checkpoints at matched training compute.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.21848v1
  - Applies to: `2606.21848-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.21848v1
  - Applies to: `2606.21848-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.21848v1
  - Applies to: `2606.21848-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.21848
  - Applies to: `2606.21848-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Xin Gao
  - arXiv author search: https://arxiv.org/search/?query=Xin%20Gao&searchtype=author
  - Applies to: the reviewed paper and `2606.21848-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
