# DEP-A-20260720-AsymVLM Pruning

#artificial-intelligence #vision-language-models #token-pruning #multimodal-inference #model-compression #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.29535v1, *AsymVLM: Asymmetric Token Pruning for Efficient Vision-Language Model Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.29535-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.29535-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: AsymVLM applies modality-specific policies: a learned cross-modal scorer and per-sample budget prune spatially redundant visual tokens before prefill, while a temporal threshold evicts text tokens only after the decoding context exceeds a fixed budget. It avoids imposing the same dependency assumptions on vision and autoregressive text.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Model pruning as two calibrated controllers with separate failure budgets. Log achieved visual and text retention, compare against a no-prune shadow sample, and trigger budget expansion when evidence is spatially diffuse or text-state sensitivity rises.

## Associated DEP Records

- [DEP-A-20260714-LCLM Context Compression](../DEP-A-20260714-LCLM%20Context%20Compression/README.md) - direct context-compression method context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.29535v1
  - Applies to: `2605.29535-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.29535v1
  - Applies to: `2605.29535-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.29535v1
  - Applies to: `2605.29535-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.29535
  - Applies to: `2605.29535-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yilin Feng
  - arXiv author search: https://arxiv.org/search/?query=Yilin%20Feng&searchtype=author
  - Applies to: the reviewed paper and `2605.29535-whitepaper-review.md`.
- Author: Ahmed Burak Gulhan
  - arXiv author search: https://arxiv.org/search/?query=Ahmed%20Burak%20Gulhan&searchtype=author
  - Applies to: the reviewed paper and `2605.29535-whitepaper-review.md`.
- Author: Mahmut Taylan Kandemir
  - arXiv author search: https://arxiv.org/search/?query=Mahmut%20Taylan%20Kandemir&searchtype=author
  - Applies to: the reviewed paper and `2605.29535-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
