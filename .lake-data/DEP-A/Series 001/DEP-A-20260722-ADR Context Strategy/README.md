# DEP-A-20260722-ADR Context Strategy

#artificial-intelligence #software-architecture #architecture-decision-records #context-engineering #LLMs #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2604.03826v2, *Context Matters: Evaluating Context Strategies for Automated ADR Generation Using LLMs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2604.03826-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2604.03826-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The study compares no-history, all-history, first-K, last-K, and retrieval-augmented context strategies for generating Architecture Decision Records from a target title and prior ADR sequence. Four heterogeneous LLMs are evaluated, and RAFG retrieves semantically related historical decisions when recency is insufficient.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Build an ADR assistant with a recency-first default, retrieval only when a constraint classifier detects cross-cutting scope, and an evidence panel that distinguishes repository facts from generated rationale and flags external or undocumented assumptions.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2604.03826v2
  - Applies to: `2604.03826-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2604.03826v2
  - Applies to: `2604.03826-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2604.03826v2
  - Applies to: `2604.03826-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2604.03826
  - Applies to: `2604.03826-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://zenodo.org/records/18370195
  - Applies to: reproducibility context in `2604.03826-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Aviral Gupta
  - arXiv author search: https://arxiv.org/search/?query=Aviral%20Gupta&searchtype=author
  - Applies to: the reviewed paper and `2604.03826-whitepaper-review.md`.
- Author: Rudra Dhar
  - arXiv author search: https://arxiv.org/search/?query=Rudra%20Dhar&searchtype=author
  - Applies to: the reviewed paper and `2604.03826-whitepaper-review.md`.
- Author: Daniel Feitosa
  - arXiv author search: https://arxiv.org/search/?query=Daniel%20Feitosa&searchtype=author
  - Applies to: the reviewed paper and `2604.03826-whitepaper-review.md`.
- Author: Karthik Vaidhyanathan
  - arXiv author search: https://arxiv.org/search/?query=Karthik%20Vaidhyanathan&searchtype=author
  - Applies to: the reviewed paper and `2604.03826-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
