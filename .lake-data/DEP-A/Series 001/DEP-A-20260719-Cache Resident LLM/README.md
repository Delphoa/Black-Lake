# DEP-A-20260719-Cache Resident LLM

#artificial-intelligence #CPU-inference #cache-residency #KV-cache #memory-hierarchy #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.25353v1, *Cache-Resident LLM Inference in GB-Scale Last-Level Caches*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.25353-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.25353-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The execution model separates weight-centric transformer operators from attention and KV-cache management so reusable weights can remain in GB-scale last-level cache while state capacity scales independently. Locality-aware placement and a static runtime synchronize only at genuine sub-operator dependencies instead of every operator boundary.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Expose residency, KV pressure, and synchronization stalls as first-class counters and let a controller choose weight-attention partitioning online, falling back to a conventional runtime when the measured cache-hit and dependency-overlap envelope collapses.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.25353v1
  - Applies to: `2606.25353-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.25353v1
  - Applies to: `2606.25353-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.25353v1
  - Applies to: `2606.25353-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.25353
  - Applies to: `2606.25353-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/ggml-org/llama.cpp
  - Applies to: reproducibility context in `2606.25353-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Wanning Zhang
  - arXiv author search: https://arxiv.org/search/?query=Wanning%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.25353-whitepaper-review.md`.
- Author: Tongzhou Gu
  - arXiv author search: https://arxiv.org/search/?query=Tongzhou%20Gu&searchtype=author
  - Applies to: the reviewed paper and `2606.25353-whitepaper-review.md`.
- Author: Marco Canini
  - arXiv author search: https://arxiv.org/search/?query=Marco%20Canini&searchtype=author
  - Applies to: the reviewed paper and `2606.25353-whitepaper-review.md`.
- Author: Ceyu Xu
  - arXiv author search: https://arxiv.org/search/?query=Ceyu%20Xu&searchtype=author
  - Applies to: the reviewed paper and `2606.25353-whitepaper-review.md`.
- Author: Jian Weng
  - arXiv author search: https://arxiv.org/search/?query=Jian%20Weng&searchtype=author
  - Applies to: the reviewed paper and `2606.25353-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
