# DEP-A-20260717-Trajectory Forensics

#artificial-intelligence #agents #security #trajectory-analysis #data-exfiltration #forensics

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.30566v1, *Forensic Trajectory Signatures for Agent Memory Poisoning Detection*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.30566-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.30566-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The study treats agent trajectories as forensic event streams and derives a recall-before-send invariant: successful data exfiltration should be preceded by observable acquisition or recall of the sensitive item. A 19-feature random forest augments the rule with temporal, tool, and content signals.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Replace a flat trajectory classifier with a causal event graph that records data acquisition, transformation, authorization, and egress, then require every sensitive send edge to have an auditable authorized predecessor path.

## Associated DEP Records

- [DEP-A-20260715-MemDelta Controlled Basel](../DEP-A-20260715-MemDelta%20Controlled%20Basel/README.md) - direct evaluation context: controlled baselines and hidden confounds in agent-memory assessment. This is method context, not a same-paper duplicate.
- [DEP-A-20260717-Latent Cache Integrity](../DEP-A-20260717-Latent%20Cache%20Integrity/README.md) - direct integrity context: provenance, authentication, and adversarial protection for retained model state. This is method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.30566v1
  - Applies to: `2606.30566-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.30566v1
  - Applies to: `2606.30566-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.30566v1
  - Applies to: `2606.30566-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.30566
  - Applies to: `2606.30566-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Jun Wen Leong
  - arXiv author search: https://arxiv.org/search/?query=Jun%20Wen%20Leong&searchtype=author
  - Applies to: the reviewed paper and `2606.30566-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
