# DEP-A-20260724-MemAudit Counterfactual

#artificial-intelligence #agent-security #memory-poisoning #counterfactual-audit #provenance #governance

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.23723v1, *MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.23723-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.23723-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: MemAudit is a post-hoc poisoning audit that combines a counterfactual memory-influence score with a memory-consistency graph. Delete-and-replay estimates how much each stored item contributed to the failed answer, while graph anomalies identify memories that conflict with surrounding evidence; high-risk items can then be ranked and removed.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Run counterfactual influence checks in a quarantined replay environment, preserve deletion receipts, and require consistency anomalies plus reproducible harm reduction before removing memory from a shared system.

## Associated DEP Records

- [DEP-A-20260720-MemGate Trust Filter](../DEP-A-20260720-MemGate%20Trust%20Filter/README.md) - direct agent-memory trust and filtering context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.23723v1
  - Applies to: `2605.23723-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.23723v1
  - Applies to: `2605.23723-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.23723v1
  - Applies to: `2605.23723-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.23723
  - Applies to: `2605.23723-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Zhewen Tan
  - arXiv author search: https://arxiv.org/search/?query=Zhewen%20Tan&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: Yilun Yao
  - arXiv author search: https://arxiv.org/search/?query=Yilun%20Yao&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: Huiyan Jin
  - arXiv author search: https://arxiv.org/search/?query=Huiyan%20Jin&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: Wenhan Yu
  - arXiv author search: https://arxiv.org/search/?query=Wenhan%20Yu&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: Guoan Wang
  - arXiv author search: https://arxiv.org/search/?query=Guoan%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: Mengyuan Fan
  - arXiv author search: https://arxiv.org/search/?query=Mengyuan%20Fan&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: liang lu
  - arXiv author search: https://arxiv.org/search/?query=liang%20lu&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: Feng Liu
  - arXiv author search: https://arxiv.org/search/?query=Feng%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: Xiangzheng Zhang
  - arXiv author search: https://arxiv.org/search/?query=Xiangzheng%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: Duohe Ma
  - arXiv author search: https://arxiv.org/search/?query=Duohe%20Ma&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: Tong Yang
  - arXiv author search: https://arxiv.org/search/?query=Tong%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Author: Lin Sun
  - arXiv author search: https://arxiv.org/search/?query=Lin%20Sun&searchtype=author
  - Applies to: the reviewed paper and `2605.23723-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
