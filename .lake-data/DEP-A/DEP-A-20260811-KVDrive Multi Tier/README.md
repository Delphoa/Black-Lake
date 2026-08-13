# DEP-A-20260811-KVDrive Multi Tier

#artificial-intelligence #LLM-serving #KV-cache #SSD-offload #multi-tier-memory #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.18071v1, *KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.18071-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.18071-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: To address these challenges, we propose KVDrive , a holistic multi-tier KV cache management system spanning GPU memory, host DRAM, and SSD. In summary, this paper makes the following contributions: We present KVDrive , a holistic multi-tier KV cache management system that sustains efficient long-context LLM inference under tight GPU cache budgets. KVDrive advances three fundamental capabilities: it adapts cache management to attention behavior to maximize reuse and minimize redundant data movement; it restructures the decoding pipeline to overlap I/O- and CPU/GPU compute-bound stages, eliminating stalls across heterogeneous resources; and it harmonizes data movement across memory tiers to unlock scalable long-context inference far beyond GPU and DRAM limits.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate multi-tier KV storage as an observable scheduler: trace placement, reuse, SSD and host transfers, pipeline overlap, queueing delay, tail latency, and accuracy at each budget, with a dense-cache fallback when attention locality or storage latency departs from the calibrated regime.

## Associated DEP Records

- [DEP-A-20260809-ScoutAttention Offload](../DEP-A-20260809-ScoutAttention%20Offload/README.md) - direct KV offload, retrieval, and long-context serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.18071v1
  - Applies to: `2605.18071-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.18071v1
  - Applies to: `2605.18071-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.18071v1
  - Applies to: `2605.18071-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.18071
  - Applies to: `2605.18071-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Jian Lin
  - arXiv author search: https://arxiv.org/search/?query=Jian%20Lin&searchtype=author
  - Applies to: the reviewed paper and `2605.18071-whitepaper-review.md`.
- Author: Jiazhi Mi
  - arXiv author search: https://arxiv.org/search/?query=Jiazhi%20Mi&searchtype=author
  - Applies to: the reviewed paper and `2605.18071-whitepaper-review.md`.
- Author: Zicong Hong
  - arXiv author search: https://arxiv.org/search/?query=Zicong%20Hong&searchtype=author
  - Applies to: the reviewed paper and `2605.18071-whitepaper-review.md`.
- Author: Haodong Wang
  - arXiv author search: https://arxiv.org/search/?query=Haodong%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2605.18071-whitepaper-review.md`.
- Author: Qianli Liu
  - arXiv author search: https://arxiv.org/search/?query=Qianli%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2605.18071-whitepaper-review.md`.
- Author: Haodyue Zhang
  - arXiv author search: https://arxiv.org/search/?query=Haodyue%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2605.18071-whitepaper-review.md`.
- Author: Peng Li
  - arXiv author search: https://arxiv.org/search/?query=Peng%20Li&searchtype=author
  - Applies to: the reviewed paper and `2605.18071-whitepaper-review.md`.
- Author: Song Guo
  - arXiv author search: https://arxiv.org/search/?query=Song%20Guo&searchtype=author
  - Applies to: the reviewed paper and `2605.18071-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
