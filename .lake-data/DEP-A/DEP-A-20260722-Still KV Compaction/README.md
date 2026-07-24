# DEP-A-20260722-Still KV Compaction

#artificial-intelligence #KV-cache #context-compression #long-context #Perceiver #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.07878v1, *Still: Amortized KV Cache Compaction in a Single Forward Pass*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.07878-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.07878-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Still trains a small per-layer Perceiver compactor against a frozen base model. A single forward pass synthesizes compact K/V states instead of selecting source rows; position-free compaction supports reuse, and iterative chunked compaction applies the transform repeatedly for horizons beyond the training prefix.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat synthesized cache as a sensitive derived document state with uncertainty and source-version binding; route needle/citation tasks to retrieval, and train recurrence explicitly to a fixed absolute budget with periodic full-context shadow checks.

## Associated DEP Records

- [DEP-A-20260714-LCLM Context Compression](../DEP-A-20260714-LCLM%20Context%20Compression/README.md) - direct context-compression method context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.07878v1
  - Applies to: `2606.07878-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.07878v1
  - Applies to: `2606.07878-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.07878v1
  - Applies to: `2606.07878-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.07878
  - Applies to: `2606.07878-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Charles O'Neill
  - arXiv author search: https://arxiv.org/search/?query=Charles%20O%27Neill&searchtype=author
  - Applies to: the reviewed paper and `2606.07878-whitepaper-review.md`.
- Author: Alex Sandomirsky
  - arXiv author search: https://arxiv.org/search/?query=Alex%20Sandomirsky&searchtype=author
  - Applies to: the reviewed paper and `2606.07878-whitepaper-review.md`.
- Author: Harry Partridge
  - arXiv author search: https://arxiv.org/search/?query=Harry%20Partridge&searchtype=author
  - Applies to: the reviewed paper and `2606.07878-whitepaper-review.md`.
- Author: Mudith Jayasekara
  - arXiv author search: https://arxiv.org/search/?query=Mudith%20Jayasekara&searchtype=author
  - Applies to: the reviewed paper and `2606.07878-whitepaper-review.md`.
- Author: Max Kirkby
  - arXiv author search: https://arxiv.org/search/?query=Max%20Kirkby&searchtype=author
  - Applies to: the reviewed paper and `2606.07878-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
