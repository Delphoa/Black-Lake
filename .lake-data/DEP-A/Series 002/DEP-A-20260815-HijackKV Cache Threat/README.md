# DEP-A-20260815-HijackKV Cache Threat

#artificial-intelligence #KV-cache #cache-reuse #security #position-independence #LLM-serving

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.19957v1, *HijackKV: New Threat in Position-Independent KV Cache Reuse*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.19957-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.19957-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Recent system research proposes efficiency-driven optimizations that relax prefix and position constraints, including (i) position-independent KV reuse [ yao2025cacheblend , hu2025epic , wang2025mepic , yang2025kvshare , yang2025kvlink ] , which enables chunk-level reuse if the tokens match, regardless of original prefix. Figure 3 illustrates HijackKV , our attack framework targeting position-independent KV cache reuse. HijackKV is most relevant to real-time, position-independent, cross-user KV reuse, such as agent-based or multi-turn serving, and is less applicable to chunk-then-cache RAG pipelines where chunks are encoded independently.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat HijackKV: New Threat in Position-Independent KV Cache Reuse as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260813-C2KV Cache Reuse](../DEP-A-20260813-C2KV%20Cache%20Reuse/README.md) - direct KV-cache reuse and isolation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.19957v1
  - Applies to: `2607.19957-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.19957v1
  - Applies to: `2607.19957-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.19957v1
  - Applies to: `2607.19957-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.19957
  - Applies to: `2607.19957-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yichi Zhang
  - arXiv author search: https://arxiv.org/search/?query=Yichi%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.19957-whitepaper-review.md`.
- Author: Zhiqi Wang
  - arXiv author search: https://arxiv.org/search/?query=Zhiqi%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.19957-whitepaper-review.md`.
- Author: Huan Zhang
  - arXiv author search: https://arxiv.org/search/?query=Huan%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.19957-whitepaper-review.md`.
- Author: Yuchen Yang
  - arXiv author search: https://arxiv.org/search/?query=Yuchen%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2607.19957-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
