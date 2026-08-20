# DEP-A-20260727-Memorywire Protocol

#artificial-intelligence #agent-memory #interoperability #protocols #governance #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.01138v2, *memorywire: A Vendor-Neutral Wire Format for Agent Memory Operations*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.01138-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.01138-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: memorywire specifies five vendor-neutral operations—remember, recall, forget, merge, and expire—over semantic, episodic, procedural, and emotional memory types. A Memory facade validates a JSON-Schema request, a router fans out to heterogeneous adapters, Reciprocal Rank Fusion combines recall results, an FSM handles procedural state, and an optional governance plane can intercept writes for approval and audit.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Define a semantic conformance layer with round-trip invariants: write, migrate, recall, merge, expire, and delete the same memory across adapter pairs while checking content, provenance, tenancy, and policy decisions. The portability claim is falsified if adapter-specific loss exceeds declared capability differences on a blinded conformance corpus.

## Associated DEP Records

- [DEP-A-20260724-Governed Agent Memory](../DEP-A-20260724-Governed%20Agent%20Memory/README.md) - direct governed persistent-memory and data-foundation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.01138v2
  - Applies to: `2606.01138-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.01138v2
  - Applies to: `2606.01138-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.01138v2
  - Applies to: `2606.01138-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.01138
  - Applies to: `2606.01138-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/mthamil107/memorywire
  - Applies to: reproducibility context in `2606.01138-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Thamilvendhan Munirathinam
  - arXiv author search: https://arxiv.org/search/?query=Thamilvendhan%20Munirathinam&searchtype=author
  - Applies to: the reviewed paper and `2606.01138-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
