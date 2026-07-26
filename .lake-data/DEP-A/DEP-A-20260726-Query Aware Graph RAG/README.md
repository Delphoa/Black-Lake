# DEP-A-20260726-Query Aware Graph RAG

#artificial-intelligence #graph-RAG #spreading-activation #multihop-QA #Neo4j #retrieval

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.30133v1, *Query-Aware Spreading Activation for Multi-Hop Retrieval over Knowledge Graphs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.30133-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.30133-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Query-Aware Spreading Activation performs graph retrieval with a per-step cosine gate inside one Cypher query. Activation propagates only when the next node remains aligned with the query, limiting indiscriminate expansion while keeping execution database-native.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Calibrate the gate per query using held-out uncertainty, report recall lost at each hop, and add a bounded rescue pass when early pruning removes every viable reasoning path.

## Associated DEP Records

- [DEP-A-20260715-FAIR GraphRAG A Retrieval](../DEP-A-20260715-FAIR%20GraphRAG%20A%20Retrieval/README.md) - direct governed graph retrieval context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.30133v1
  - Applies to: `2606.30133-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.30133v1
  - Applies to: `2606.30133-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.30133v1
  - Applies to: `2606.30133-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.30133
  - Applies to: `2606.30133-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/kinfi4/qasa-graph-rag
  - Applies to: reproducibility context in `2606.30133-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Illia Makarov
  - arXiv author search: https://arxiv.org/search/?query=Illia%20Makarov&searchtype=author
  - Applies to: the reviewed paper and `2606.30133-whitepaper-review.md`.
- Author: Mykola Glybovets
  - arXiv author search: https://arxiv.org/search/?query=Mykola%20Glybovets&searchtype=author
  - Applies to: the reviewed paper and `2606.30133-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
