# DEP-A-20260809-LLM Agent Privacy

#artificial-intelligence #LLM-agents #privacy #data-governance #survey #security

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.26627v1, *Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.26627-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.26627-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We motivate a data-centric view of agent privacy and explain why an LLM agent that works with data, which we call a data agent, has privacy properties different from those of stateless chatbots and generic tool-using agents (Sections 1 and 2 ). A data agent chains a retrieval, a query, an aggregation, a memory write, and a message to a peer, and each step may have its own protection, yet there is no framework that composes those protections into an end-to-end guarantee. We survey the privacy of LLM agents from a data-centric view, organizing the field around the data an agent touches rather than by attack type, and we use data agent as shorthand for an LLM agent that works with data.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Agents That Know Too Much: A Data-Centric Survey of Privacy in LLM Agents as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../../Series%20001/DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory lifecycle, privacy, and governance context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.26627v1
  - Applies to: `2606.26627-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.26627v1
  - Applies to: `2606.26627-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.26627v1
  - Applies to: `2606.26627-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.26627
  - Applies to: `2606.26627-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Nada Lahjouji
  - arXiv author search: https://arxiv.org/search/?query=Nada%20Lahjouji&searchtype=author
  - Applies to: the reviewed paper and `2606.26627-whitepaper-review.md`.
- Author: Ashwin Gerard Colaco
  - arXiv author search: https://arxiv.org/search/?query=Ashwin%20Gerard%20Colaco&searchtype=author
  - Applies to: the reviewed paper and `2606.26627-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
