# DEP-A-20260727-GQE Sparse Queries

#artificial-intelligence #grouped-query-attention #KV-cache #language-models #efficient-inference #scaling

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.20945v2, *Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.20945-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.20945-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Grouped Query Experts adds token-wise sparse routing over query heads inside each fixed grouped-query-attention group while leaving all key-value heads dense. A router activates top-k query experts per token, preserving the GQA cache layout and reducing query-head computation instead of sparsifying stored KV state.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use routing entropy and per-expert load as first-class observability signals, with a dense fallback for tokens whose top-k margin is small. The claim is falsified if matched-kernel dense head reduction or static head masks achieve the same quality-compute frontier across larger scales.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct cache-budget and efficient-attention context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.20945v2
  - Applies to: `2606.20945-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.20945v2
  - Applies to: `2606.20945-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.20945v2
  - Applies to: `2606.20945-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.20945
  - Applies to: `2606.20945-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Vishesh Tripathi
  - arXiv author search: https://arxiv.org/search/?query=Vishesh%20Tripathi&searchtype=author
  - Applies to: the reviewed paper and `2606.20945-whitepaper-review.md`.
- Author: Abhay Kumar
  - arXiv author search: https://arxiv.org/search/?query=Abhay%20Kumar&searchtype=author
  - Applies to: the reviewed paper and `2606.20945-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
