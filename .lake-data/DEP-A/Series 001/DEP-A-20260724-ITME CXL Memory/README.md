# DEP-A-20260724-ITME CXL Memory

#artificial-intelligence #CXL #disaggregated-memory #KV-cache #prefetching #hardware-systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.12556v2, *ITME: Inference Tiered Memory Expansion with Disaggregated CXL-Hybrid Memories*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.12556-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.12556-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: ITME places a byte-addressable CXL-hybrid memory tier between host memory and conventional remote storage. Hardware-managed DRAM caches NAND, while software exploits predictable model-weight and prefix-KV access to pipeline DMA transfers across GPU, host, NIC, and the disaggregated tier.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat CXL-hybrid expansion as a recoverable prefetch tier with explicit hit/miss telemetry, read-priority budgets, recomputation receipts, and admission control when miss bandwidth falls below the serving objective.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct cache-budget and efficient-attention context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.12556v2
  - Applies to: `2606.12556-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.12556v2
  - Applies to: `2606.12556-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.12556v2
  - Applies to: `2606.12556-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.12556
  - Applies to: `2606.12556-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Hakbeom Jang
  - arXiv author search: https://arxiv.org/search/?query=Hakbeom%20Jang&searchtype=author
  - Applies to: the reviewed paper and `2606.12556-whitepaper-review.md`.
- Author: Younghoon Min
  - arXiv author search: https://arxiv.org/search/?query=Younghoon%20Min&searchtype=author
  - Applies to: the reviewed paper and `2606.12556-whitepaper-review.md`.
- Author: Sunwoong Kim
  - arXiv author search: https://arxiv.org/search/?query=Sunwoong%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.12556-whitepaper-review.md`.
- Author: Taeyoung Ahn
  - arXiv author search: https://arxiv.org/search/?query=Taeyoung%20Ahn&searchtype=author
  - Applies to: the reviewed paper and `2606.12556-whitepaper-review.md`.
- Author: Hanyee Kim
  - arXiv author search: https://arxiv.org/search/?query=Hanyee%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.12556-whitepaper-review.md`.
- Author: Youngpyo Joo
  - arXiv author search: https://arxiv.org/search/?query=Youngpyo%20Joo&searchtype=author
  - Applies to: the reviewed paper and `2606.12556-whitepaper-review.md`.
- Author: Hoshik Kim
  - arXiv author search: https://arxiv.org/search/?query=Hoshik%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.12556-whitepaper-review.md`.
- Author: Jongryool Kim
  - arXiv author search: https://arxiv.org/search/?query=Jongryool%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.12556-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
