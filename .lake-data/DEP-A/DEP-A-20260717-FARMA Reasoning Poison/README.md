# DEP-A-20260717-FARMA Reasoning Poison

#artificial-intelligence #agent-memory #security #memory-poisoning #provenance #reasoning

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.05029v1, *Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.05029-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.05029-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: FARMA attacks agent memory by inserting forged rationales that look like successful prior reasoning, encouraging later retrieval to self-reinforce the attack. SENTINEL combines five provenance, consistency, and behavioral signals to gate suspicious memory before it affects execution.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Combine cryptographic write authentication with risk-scored quarantine: untrusted rationales may be searched for forensic analysis but cannot directly authorize actions or become positive training evidence without independent confirmation.

## Associated DEP Records

- [DEP-A-20260715-MemDelta Controlled Basel](../DEP-A-20260715-MemDelta%20Controlled%20Basel/README.md) - direct evaluation context: controlled baselines and hidden confounds in agent-memory assessment. This is method context, not a same-paper duplicate.
- [DEP-A-20260717-Latent Cache Integrity](../DEP-A-20260717-Latent%20Cache%20Integrity/README.md) - direct integrity context: provenance, authentication, and adversarial protection for retained model state. This is method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.05029v1
  - Applies to: `2607.05029-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.05029v1
  - Applies to: `2607.05029-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.05029v1
  - Applies to: `2607.05029-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.05029
  - Applies to: `2607.05029-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Neeraj Karamchandani
  - arXiv author search: https://arxiv.org/search/?query=Neeraj%20Karamchandani&searchtype=author
  - Applies to: the reviewed paper and `2607.05029-whitepaper-review.md`.
- Author: Piyush Nagasubramaniam
  - arXiv author search: https://arxiv.org/search/?query=Piyush%20Nagasubramaniam&searchtype=author
  - Applies to: the reviewed paper and `2607.05029-whitepaper-review.md`.
- Author: Sencun Zhu
  - arXiv author search: https://arxiv.org/search/?query=Sencun%20Zhu&searchtype=author
  - Applies to: the reviewed paper and `2607.05029-whitepaper-review.md`.
- Author: Dinghao Wu
  - arXiv author search: https://arxiv.org/search/?query=Dinghao%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2607.05029-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
