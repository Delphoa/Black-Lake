# DEP-A-20260813-HyMCache CXL Serving

#artificial-intelligence #KV-cache #CXL #hybrid-memory #LLM-serving #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.18141v1, *HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.18141-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.18141-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: This paper presents HyMCache, a KV-cache framework that integrates CXL-hybrid memory for multi-turn LLM serving. Rather than using CXL memory as a generic memory expansion tier, HyMCache targets remote KV caching for multi-turn and agentic LLM serving. This paper presents HyMCache, a KV-cache framework that integrates CXL-hybrid memory (CXL-HM) for multi-turn LLM serving.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use hybrid-memory KV serving as a tiered placement controller: log hotness, transfer descriptors, CXL and device residency, queue delay, and tail latency, with deterministic fallback when transport or memory-pressure estimates are wrong.

## Associated DEP Records

- [DEP-A-20260809-ScoutAttention Offload](../DEP-A-20260809-ScoutAttention%20Offload/README.md) - direct KV offload, retrieval, and long-context serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.18141v1
  - Applies to: `2607.18141-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.18141v1
  - Applies to: `2607.18141-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.18141v1
  - Applies to: `2607.18141-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.18141
  - Applies to: `2607.18141-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Hakbeom Jang
  - arXiv author search: https://arxiv.org/search/?query=Hakbeom%20Jang&searchtype=author
  - Applies to: the reviewed paper and `2607.18141-whitepaper-review.md`.
- Author: Inho Song
  - arXiv author search: https://arxiv.org/search/?query=Inho%20Song&searchtype=author
  - Applies to: the reviewed paper and `2607.18141-whitepaper-review.md`.
- Author: Sam H. Noh
  - arXiv author search: https://arxiv.org/search/?query=Sam%20H.%20Noh&searchtype=author
  - Applies to: the reviewed paper and `2607.18141-whitepaper-review.md`.
- Author: Jongryool Kim
  - arXiv author search: https://arxiv.org/search/?query=Jongryool%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2607.18141-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
