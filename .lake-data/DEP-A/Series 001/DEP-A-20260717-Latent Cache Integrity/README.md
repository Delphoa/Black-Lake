# DEP-A-20260717-Latent Cache Integrity

#artificial-intelligence #multi-agent-systems #llm-security #kv-cache #integrity #cryptography

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.28958v1, *When Latent Agents Lie: KV-Cache Integrity in Multi-Agent LLM Collaboration*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.28958-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.28958-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The study lets specialist agents send both a visible commitment and a full KV-cache payload to a coordinator, then distinguishes visible-message deception from hidden-state tampering. Its protection binds agent, session, model, commitment, tensor metadata, and payload digest in an HMAC-SHA256 manifest.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat latent memory as a signed, content-addressed capability with tenant, model, session, expiry, and visible-commitment bindings, plus a semantic cross-check that can decline uninspectable state.

## Associated DEP Records

- [DEP-A-20260716-KV Memory Hierarchy](../DEP-A-20260716-KV%20Memory%20Hierarchy/README.md) - direct method context: reviewed survey of KV-cache representation, movement, reuse, and memory hierarchy. This is method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.28958v1
  - Applies to: `2606.28958-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.28958v1
  - Applies to: `2606.28958-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.28958v1
  - Applies to: `2606.28958-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.28958
  - Applies to: `2606.28958-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Luís Brito
  - arXiv author search: https://arxiv.org/search/?query=Lu%C3%ADs%20Brito&searchtype=author
  - Applies to: the reviewed paper and `2606.28958-whitepaper-review.md`.
- Author: Carlos Baquero
  - arXiv author search: https://arxiv.org/search/?query=Carlos%20Baquero&searchtype=author
  - Applies to: the reviewed paper and `2606.28958-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
