# DEP-A-20260805-TGMS BiTemporal Graph

#artificial-intelligence #temporal-graphs #agent-tools #verification #databases #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.10265v1, *TGMS: An Agent-Native Bi-Temporal Graph Management System*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.10265-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.10265-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The compared systems are: TGMS with the full Planner–Executor–Verifier pipeline; vector-RAG over serialized events, with MiniLM retrieval; static-graph RAG over two-hop edge lists from the latest snapshot; and text-to-Cypher over the same events loaded into a standard Kùzu property graph, with the same repair budget. Zep/Graphiti uses a bi-temporal knowledge graph for agent memory [ 21 ] , and TOKI formalizes bitemporal write-time operators for contradiction resolution in relational agent memory [ 27 ] . TGMS shares the bi-temporal foundation of Zep and TOKI but targets temporal graph analytics: the checked artifacts are operator plans and final answer claims rather than memory writes.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat TGMS: An Agent-Native Bi-Temporal Graph Management System as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory systems and lifecycle context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.10265v1
  - Applies to: `2607.10265-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.10265v1
  - Applies to: `2607.10265-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.10265v1
  - Applies to: `2607.10265-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.10265
  - Applies to: `2607.10265-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/zxf-work/tgms
  - Applies to: reproducibility context in `2607.10265-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Xiaofei Zhang
  - arXiv author search: https://arxiv.org/search/?query=Xiaofei%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.10265-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
