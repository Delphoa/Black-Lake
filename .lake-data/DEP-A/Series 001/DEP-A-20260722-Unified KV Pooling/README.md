# DEP-A-20260722-Unified KV Pooling

#artificial-intelligence #LLM-serving #KV-cache #storage-systems #NVMe #long-context

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.14779v1, *Unified KV Pooling to Accelerate Long-Context LLM Serving*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.14779-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.14779-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Unified KV Pooling aggregates host-memory and NVMe devices into one logical pool. A global lookup table and bandwidth-aware allocator distribute layers and segments across devices, while an SPDK-based KV passthrough path bypasses filesystem overhead and parallelizes retrieval rather than serializing CPU and SSD I/O.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Expose the pool as a measured storage scheduler with per-segment deadlines, topology-aware placement, non-polling fallback, and multi-tenant admission controls; log when KV retrieval blocks compute or falls back to recompute.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.14779v1
  - Applies to: `2606.14779-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.14779v1
  - Applies to: `2606.14779-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.14779v1
  - Applies to: `2606.14779-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.14779
  - Applies to: `2606.14779-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Minchul Kang
  - arXiv author search: https://arxiv.org/search/?query=Minchul%20Kang&searchtype=author
  - Applies to: the reviewed paper and `2606.14779-whitepaper-review.md`.
- Author: Changyong Shin
  - arXiv author search: https://arxiv.org/search/?query=Changyong%20Shin&searchtype=author
  - Applies to: the reviewed paper and `2606.14779-whitepaper-review.md`.
- Author: Jinwoo Jeong
  - arXiv author search: https://arxiv.org/search/?query=Jinwoo%20Jeong&searchtype=author
  - Applies to: the reviewed paper and `2606.14779-whitepaper-review.md`.
- Author: Jaerim Park
  - arXiv author search: https://arxiv.org/search/?query=Jaerim%20Park&searchtype=author
  - Applies to: the reviewed paper and `2606.14779-whitepaper-review.md`.
- Author: Woohyun Kim
  - arXiv author search: https://arxiv.org/search/?query=Woohyun%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.14779-whitepaper-review.md`.
- Author: Bonyul Gu
  - arXiv author search: https://arxiv.org/search/?query=Bonyul%20Gu&searchtype=author
  - Applies to: the reviewed paper and `2606.14779-whitepaper-review.md`.
- Author: Dongwoo Kang
  - arXiv author search: https://arxiv.org/search/?query=Dongwoo%20Kang&searchtype=author
  - Applies to: the reviewed paper and `2606.14779-whitepaper-review.md`.
- Author: Gyeongsik Yang
  - arXiv author search: https://arxiv.org/search/?query=Gyeongsik%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2606.14779-whitepaper-review.md`.
- Author: Chuck Yoo
  - arXiv author search: https://arxiv.org/search/?query=Chuck%20Yoo&searchtype=author
  - Applies to: the reviewed paper and `2606.14779-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
