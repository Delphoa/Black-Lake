# DEP-A-20260727-MemLineage Security

#artificial-intelligence #agent-memory #security #provenance #cryptography #tool-governance

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.14421v1, *MemLineage: Lineage-Guided Enforcement for LLM Agent Memory*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.14421-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.14421-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: MemLineage surrounds a persistent memory store with provenance metadata, per-principal Ed25519 signatures, an RFC-6962-style append-only Merkle log, a weighted derivation DAG, verifier-aware retrieval, and a sensitive-action gate. Trust labels propagate across sufficiently strong derivation edges, allowing recall while preventing a memory descended from external content from authorizing a sensitive tool action.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat action authority as a parameter-level property rather than a context-level label: record which exact retrieved values justify each tool argument and require every value's lineage receipt at dispatch. The mechanism is falsified if an adaptive attacker can preserve a permitted lineage label while causally controlling a sensitive argument in a held-out tool environment.

## Associated DEP Records

- [DEP-A-20260720-MemGate Trust Filter](../DEP-A-20260720-MemGate%20Trust%20Filter/README.md) - direct memory trust, provenance, and action-gating context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.14421v1
  - Applies to: `2605.14421-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.14421v1
  - Applies to: `2605.14421-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.14421v1
  - Applies to: `2605.14421-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.14421
  - Applies to: `2605.14421-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Ciyan Ouyang
  - arXiv author search: https://arxiv.org/search/?query=Ciyan%20Ouyang&searchtype=author
  - Applies to: the reviewed paper and `2605.14421-whitepaper-review.md`.
- Author: Rui Hou
  - arXiv author search: https://arxiv.org/search/?query=Rui%20Hou&searchtype=author
  - Applies to: the reviewed paper and `2605.14421-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
