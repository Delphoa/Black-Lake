# DEP-A-20260722-Cartridges at Scale

#artificial-intelligence #document-memory #KV-cache #retrieval-augmented-generation #long-context #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.04557v1, *Cartridges at Scale: Training Modular KV Caches over Large Document Collections*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.04557-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.04557-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Cartridges at Scale trains one modular KV cartridge per document while exposing each cartridge to distractors through mixed-visibility batches. A budget manager rotates cartridge pools between GPU and persistent storage, per-cartridge warmup corrects sparse update schedules, and improved self-study generation uses a stronger question model with proportional document sampling.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat cartridges as versioned document replicas with retrieval confidence, per-document compression limits learned from held-out questions, provenance/deletion hooks, and a text fallback when numerical or citation-critical evidence is not recoverable.

## Associated DEP Records

- [DEP-A-20260714-LCLM Context Compression](../DEP-A-20260714-LCLM%20Context%20Compression/README.md) - direct context-compression method context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.04557v1
  - Applies to: `2606.04557-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.04557v1
  - Applies to: `2606.04557-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.04557v1
  - Applies to: `2606.04557-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.04557
  - Applies to: `2606.04557-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Momchil Hardalov
  - arXiv author search: https://arxiv.org/search/?query=Momchil%20Hardalov&searchtype=author
  - Applies to: the reviewed paper and `2606.04557-whitepaper-review.md`.
- Author: Gonzalo Iglesias
  - arXiv author search: https://arxiv.org/search/?query=Gonzalo%20Iglesias&searchtype=author
  - Applies to: the reviewed paper and `2606.04557-whitepaper-review.md`.
- Author: Adrià de Gispert
  - arXiv author search: https://arxiv.org/search/?query=Adri%C3%A0%20de%20Gispert&searchtype=author
  - Applies to: the reviewed paper and `2606.04557-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
