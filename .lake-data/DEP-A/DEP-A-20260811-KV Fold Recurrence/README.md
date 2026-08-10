# DEP-A-20260811-KV Fold Recurrence

#artificial-intelligence #long-context #KV-cache #recurrence #training-free #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.12471v1, *KV-Fold: One-Step KV-Cache Recurrence for Long-Context Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.12471-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.12471-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Our contributions are as follows: We propose KV-Fold, a simple inference-time protocol that turns a frozen pretrained transformer into a recurrent long-context model by carrying the accumulated KV cache across chunks as the accumulator in a left fold, without architectural changes, special memory tokens, or fine-tuning. KV-Fold achieves 100 % 100\% exact-match retrieval at every tested distance, matching full attention exactly, while isolated chunks remain at 0 % 0\% . The KV-Fold recurrence does not reduce total memory consumption below full attention: the cache at chain depth N N stores the same information that a full forward over N ​ C NC tokens would store.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat KV folding as a recurrent state-transport protocol: checkpoint numerical drift and semantic retention at every fold, distinguish exact needle retrieval from general understanding, and require a full-context fallback when recurrence depth, model family, or chunk boundaries leave the validated envelope.

## Associated DEP Records

- [DEP-A-20260810-MomentKV](../DEP-A-20260810-MomentKV/README.md) - direct long-context KV-cache eviction and retention context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.12471v1
  - Applies to: `2605.12471-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.12471v1
  - Applies to: `2605.12471-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.12471v1
  - Applies to: `2605.12471-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.12471
  - Applies to: `2605.12471-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Alireza Nadali
  - arXiv author search: https://arxiv.org/search/?query=Alireza%20Nadali&searchtype=author
  - Applies to: the reviewed paper and `2605.12471-whitepaper-review.md`.
- Author: Patrick Cooper
  - arXiv author search: https://arxiv.org/search/?query=Patrick%20Cooper&searchtype=author
  - Applies to: the reviewed paper and `2605.12471-whitepaper-review.md`.
- Author: Ashutosh Trivedi
  - arXiv author search: https://arxiv.org/search/?query=Ashutosh%20Trivedi&searchtype=author
  - Applies to: the reviewed paper and `2605.12471-whitepaper-review.md`.
- Author: Alvaro Velasquez
  - arXiv author search: https://arxiv.org/search/?query=Alvaro%20Velasquez&searchtype=author
  - Applies to: the reviewed paper and `2605.12471-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
