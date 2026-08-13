# DEP-A-20260730-NeuSymMS

#artificial-intelligence #agent-memory #neuro-symbolic-AI #knowledge-graphs #governance #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.17596v2, *NeuSymMS: A Hybrid Neuro-Symbolic Memory System for Persistent, Self-Curating LLM Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.17596-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.17596-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Conversation-log retrieval : The LoCoMo benchmark by Snap Research (ACL 2024) demonstrated that while long-context LLMs and RAG improve memory capabilities by 12–20%, they still lag significantly behind human performance, especially in temporal reasoning (by 41%) [ 1 ] . NeuSymMS contributes a production-oriented, hybrid neuro-symbolic memory system that (i) represents user knowledge as scoped triples; (ii) uses LLMs only for neural fact extraction; and (iii) delegates classification, contradiction handling, and lifecycle management to a CLIPS-based expert system. As an example of the read path, assume the database contains long-term facts: When the user asks: “What languages do I know?” the system issues a query for active user-scoped facts, orders them by memory type, access count, and recency, and formats a context block: This block is injected into the LLM’s system prompt, enabling responses such as: “Based on what I know about you, you’re proficient in Python and Go.” NeuSymMS is implemented as a Memory System inside the Nexa platform [ 34 ] , exposed both via backend APIs and a UI.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Combine neural extraction with symbolic lifecycle rules, but expose every deduplication, contradiction, promotion, and pruning decision as an auditable state transition.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory systems and lifecycle context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.17596v2
  - Applies to: `2605.17596-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.17596v2
  - Applies to: `2605.17596-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.17596v2
  - Applies to: `2605.17596-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.17596
  - Applies to: `2605.17596-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Mujahid Sultan
  - arXiv author search: https://arxiv.org/search/?query=Mujahid%20Sultan&searchtype=author
  - Applies to: the reviewed paper and `2605.17596-whitepaper-review.md`.
- Author: Sri Thuraisamy
  - arXiv author search: https://arxiv.org/search/?query=Sri%20Thuraisamy&searchtype=author
  - Applies to: the reviewed paper and `2605.17596-whitepaper-review.md`.
- Author: Daya Rajaratnam
  - arXiv author search: https://arxiv.org/search/?query=Daya%20Rajaratnam&searchtype=author
  - Applies to: the reviewed paper and `2605.17596-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
