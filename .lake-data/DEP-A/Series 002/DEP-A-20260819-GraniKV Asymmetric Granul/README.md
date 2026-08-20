# DEP-A-20260819-GraniKV Asymmetric Granul

#artificial-intelligence #arXiv #paper-review #KV-cache #agents #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.15584v1, *GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.15584-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.15584-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We introduce GraniKV , an asymmetric-granularity KV-cache paging layer that splits the KV pool into a contiguous HOT pool for shared prefixes and a token-level COLD pool for per-request suffix and decoded tokens. To the best of our knowledge, GraniKV is the first system to apply asymmetric paging granularity to the KV cache of a production paged-serving engine, and the first to make fat-GEMM shared-prefix attention ( Juravsky et al. GraniKV resolves this by asymmetric granularity KV-cache paging , guided by three goals: Contiguous prefix storage.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat GraniKV: Asymmetric Granularity KV-Cache Paging for Multi-Agent Systems with Long Shared Prefix as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.15584v1
  - Applies to: `2608.15584-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.15584v1
  - Applies to: `2608.15584-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.15584v1
  - Applies to: `2608.15584-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.15584
  - Applies to: `2608.15584-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Jinhyun Jeon
  - arXiv author search: https://arxiv.org/search/?query=Jinhyun%20Jeon&searchtype=author
  - Applies to: the reviewed paper and `2608.15584-whitepaper-review.md`.
- Author: Sungjoo Yoo
  - arXiv author search: https://arxiv.org/search/?query=Sungjoo%20Yoo&searchtype=author
  - Applies to: the reviewed paper and `2608.15584-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
