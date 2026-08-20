# DEP-A-20260819-InferScale GPU Native KV

#artificial-intelligence #arXiv #paper-review #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.27090v1, *InferScale: GPU-Native KV Injection for Personalized LLM Serving*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.27090-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.27090-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: InferScale is a data-systems co-design: it maintains two GPU-resident indices over the same memory, keyed by a shared identifier, an approximate-nearest-neighbor index over semantic embeddings for retrieval and a pre-RoPE KV store for injection, and manages them across an GDDR/host-DRAM hierarchy. We design and implement InferScale as a vLLM KV-connector plugin that combines GPU-resident semantic retrieval with reusable KV storage, requiring no modifications to the serving engine, no model fine-tuning, and no changes to existing retrieval pipelines ( Section 3 ). We then describe retrieval-based memory systems, whose token-layer interface motivates InferScale ’s attention-layer injection.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat InferScale: GPU-Native KV Injection for Personalized LLM Serving as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.27090v1
  - Applies to: `2607.27090-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.27090v1
  - Applies to: `2607.27090-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.27090v1
  - Applies to: `2607.27090-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2607.27090
  - Applies to: `2607.27090-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Peter Li
  - arXiv author search: https://arxiv.org/search/?query=Peter%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.27090-whitepaper-review.md`.
- Author: Prashant Pandey
  - arXiv author search: https://arxiv.org/search/?query=Prashant%20Pandey&searchtype=author
  - Applies to: the reviewed paper and `2607.27090-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
