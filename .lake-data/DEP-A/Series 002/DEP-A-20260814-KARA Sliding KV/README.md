# DEP-A-20260814-KARA Sliding KV

#artificial-intelligence #KV-cache #reasoning-models #sliding-window #LLM-serving #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.01237v2, *KARA: Efficient Reasoning LLM Serving via Sliding-Window KV Cache Compression*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.01237-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.01237-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: To overcome these limitations, we propose Kara, a sliding-window KV cache compression method that performs decoding-time compression only on the recently generated context. In summary, our main contributions are as follows: We propose Kara, a KV cache compression method that uses sliding-window bidirectional attention to identify candidate discrete KV pairs and employs a Token2Chunk module to generate chunks with contiguous KV pairs. We adapt Kara to PagedAttention and develop KvLLM, an inference framework that supports applying KV cache compression to improve decoding efficiency in memory-constrained environments.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Model sliding-window cache compression as periodic semantic compaction: preserve window boundaries, token-to-chunk expansion decisions, per-block survival, and throughput, and compare against equal-memory eviction policies under changing reasoning lengths.

## Associated DEP Records

- [DEP-A-20260810-MomentKV](../DEP-A-20260810-MomentKV/README.md) - direct long-context KV-cache eviction and retention context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260810-AB Sparse Attention](../DEP-A-20260810-AB%20Sparse%20Attention/README.md) - direct adaptive sparse-attention and long-context evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.01237v2
  - Applies to: `2607.01237-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.01237v2
  - Applies to: `2607.01237-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.01237v2
  - Applies to: `2607.01237-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.01237
  - Applies to: `2607.01237-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Shen Han
  - arXiv author search: https://arxiv.org/search/?query=Shen%20Han&searchtype=author
  - Applies to: the reviewed paper and `2607.01237-whitepaper-review.md`.
- Author: Yuyang Wu
  - arXiv author search: https://arxiv.org/search/?query=Yuyang%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2607.01237-whitepaper-review.md`.
- Author: Junpu Yu
  - arXiv author search: https://arxiv.org/search/?query=Junpu%20Yu&searchtype=author
  - Applies to: the reviewed paper and `2607.01237-whitepaper-review.md`.
- Author: Olexandr Isayev
  - arXiv author search: https://arxiv.org/search/?query=Olexandr%20Isayev&searchtype=author
  - Applies to: the reviewed paper and `2607.01237-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
