# DEP-A-20260719-AuthSelect Integrity

#artificial-intelligence #agent-memory #graph-retrieval #selection-integrity #provenance #security

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.12290v1, *Selection Integrity for LLM Graph Memory: An Accumulability Criterion for Information-Flow-Blind Retrieval*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.12290-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.12290-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The paper identifies a selection-integrity channel: unauthenticated structural writes can change which authenticated records a graph-memory selector returns, so provenance checks on retrieved content see only valid evidence after the attack has already altered selection. AuthSelect recomputes selection on the authenticated subgraph before evidence reaches the agent.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Make selection provenance explicit: emit a proof object containing the authenticated subgraph version, selector configuration, candidate margins, and influence budget; block high-impact actions when small unauthenticated perturbations can change top-k membership.

## Associated DEP Records

- [DEP-A-20260715-FAIR GraphRAG A Retrieval](../DEP-A-20260715-FAIR%20GraphRAG%20A%20Retrieval/README.md) - direct governed graph retrieval context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.12290v1
  - Applies to: `2606.12290-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.12290v1
  - Applies to: `2606.12290-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.12290v1
  - Applies to: `2606.12290-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.12290
  - Applies to: `2606.12290-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/langchain-ai/langgraph
  - Applies to: reproducibility context in `2606.12290-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://github.com/getzep/graphiti
  - Applies to: reproducibility context in `2606.12290-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Zeming Fei
  - arXiv author search: https://arxiv.org/search/?query=Zeming%20Fei&searchtype=author
  - Applies to: the reviewed paper and `2606.12290-whitepaper-review.md`.
- Author: Hongming Fei
  - arXiv author search: https://arxiv.org/search/?query=Hongming%20Fei&searchtype=author
  - Applies to: the reviewed paper and `2606.12290-whitepaper-review.md`.
- Author: Xiaoyang Wang
  - arXiv author search: https://arxiv.org/search/?query=Xiaoyang%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.12290-whitepaper-review.md`.
- Author: Yang yang
  - arXiv author search: https://arxiv.org/search/?query=Yang%20yang&searchtype=author
  - Applies to: the reviewed paper and `2606.12290-whitepaper-review.md`.
- Author: Prosanta Gope
  - arXiv author search: https://arxiv.org/search/?query=Prosanta%20Gope&searchtype=author
  - Applies to: the reviewed paper and `2606.12290-whitepaper-review.md`.
- Author: Biplab Sikdar
  - arXiv author search: https://arxiv.org/search/?query=Biplab%20Sikdar&searchtype=author
  - Applies to: the reviewed paper and `2606.12290-whitepaper-review.md`.
- Author: Ying Zhang
  - arXiv author search: https://arxiv.org/search/?query=Ying%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.12290-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
