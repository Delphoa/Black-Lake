# DEP-A-20260719-Edge Cloud Split

#artificial-intelligence #edge-cloud-inference #privacy #KV-cache #speculative-decoding #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.13093v1, *Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.13093-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.13093-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The endpoint owns prompt preprocessing, embeddings, cache authorization, speculative proposals, a low-dimensional slice of the vocabulary head, and final sampling; the cloud runs the authorized decoder, maintains the admitted KV state, verifies drafts, and returns the complementary projection. Quantized tensor messages use AES-GCM in transit, while endpoint-local LoRA and draft parameters remain undisclosed.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat cache authorization and projection disclosure as an explicit per-request privacy budget, with measured leakage probes, abort-to-local policies, and a Pareto controller that selects split depth, quantization, masking, and speculative horizon from device and network telemetry.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.13093v1
  - Applies to: `2607.13093-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.13093v1
  - Applies to: `2607.13093-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.13093v1
  - Applies to: `2607.13093-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.13093
  - Applies to: `2607.13093-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yi Li
  - arXiv author search: https://arxiv.org/search/?query=Yi%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.13093-whitepaper-review.md`.
- Author: Chen Li
  - arXiv author search: https://arxiv.org/search/?query=Chen%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.13093-whitepaper-review.md`.
- Author: Jiexiong Liu
  - arXiv author search: https://arxiv.org/search/?query=Jiexiong%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.13093-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
