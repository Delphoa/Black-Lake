# DEP-A-20260801-Token Flow Firewall

#artificial-intelligence #agent-security #runtime-auditing #persistent-agents #information-flow #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.08395v1, *Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.08395-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.08395-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Based on this principle, we propose TokenWall, a local runtime enforcement framework for persistent AI agents (Figure 1 (c)). TokenWall operates at semantic transfer boundaries and performs pre-transfer auditing of each token flow before it is committed to memory, passed to tools, or exposed to external interfaces (Figure 1 c), effectively acting as a semantic firewall for agent token flows. Describe the issue below: Abstract 1 Introduction 2 Threat Model 3.1 Token-Flow Abstraction 3.2 Local Semantic Auditing 3.3 Precheck and Fallback Arbitration 4 Experimental Setup 5.1 Attack containment effectiveness (RQ1) 5.2 Efficiency–security trade-off (RQ2) 5.3 Benign behavior preservation (RQ3) 5.4 Design analysis and robustness (RQ4) 6 Related Work 7 Conclusion References A Runtime Procedure B.1 Deterministic Precheck B.2 Small-Auditor Prompt and Output Schema B.3 Escalation Predicate B.4 Large-Arbiter Prompt Judge Protocol.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Model persistent-agent runtime auditing as information-flow accounting over semantic state: record each token-derived state mutation, its source and destination, policy decision, and downstream tool effect, then falsify the firewall by testing transformations that preserve intent while evading its learned categories.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.08395v1
  - Applies to: `2607.08395-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.08395v1
  - Applies to: `2607.08395-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.08395v1
  - Applies to: `2607.08395-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.08395
  - Applies to: `2607.08395-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Puji Wang
  - arXiv author search: https://arxiv.org/search/?query=Puji%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.08395-whitepaper-review.md`.
- Author: Yingchen Zhang
  - arXiv author search: https://arxiv.org/search/?query=Yingchen%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.08395-whitepaper-review.md`.
- Author: Ruqing Zhang
  - arXiv author search: https://arxiv.org/search/?query=Ruqing%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.08395-whitepaper-review.md`.
- Author: Jiafeng Guo
  - arXiv author search: https://arxiv.org/search/?query=Jiafeng%20Guo&searchtype=author
  - Applies to: the reviewed paper and `2607.08395-whitepaper-review.md`.
- Author: Xueqi Cheng
  - arXiv author search: https://arxiv.org/search/?query=Xueqi%20Cheng&searchtype=author
  - Applies to: the reviewed paper and `2607.08395-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
