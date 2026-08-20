# DEP-A-20260813-Risk Sensitive Memory

#artificial-intelligence #coding-agents #contextual-bandits #memory-retrieval #abstention #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2604.27283v1, *Learning When to Remember: Risk-Sensitive Contextual Bandits for Abstention-Aware Memory Retrieval in LLM-Based Coding Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2604.27283-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2604.27283-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: First, we define coding-agent issue-memory reuse as an abstention-aware, risk-sensitive contextual-bandit problem, motivated by the concrete failure modes encountered above. We introduce RSCB-MC , a risk-sensitive contextual bandit memory controller that decides whether an agent should use no memory, inject the top resolution, summarize multiple candidates, perform high-precision or high-recall retrieval, abstain, or ask for feedback. Keywords: LLM coding agents; issue memory; contextual bandits; risk-sensitive reinforcement learning; abstention; retrieval-augmented generation; automated debugging; automated program repair.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat memory retrieval for coding agents as a risk-sensitive abstention policy: log retrieved issue evidence, action, confidence, failure cost, and no-memory counterfactual, with repository-specific calibration and rollback when reuse harms correctness.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../../Series%20001/DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory lifecycle and systems context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260802-Coding Agent Context](../../Series%20001/DEP-A-20260802-Coding%20Agent%20Context/README.md) - direct repository-scale coding-agent and verification context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2604.27283v1
  - Applies to: `2604.27283-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2604.27283v1
  - Applies to: `2604.27283-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2604.27283v1
  - Applies to: `2604.27283-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2604.27283
  - Applies to: `2604.27283-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/PhiniteLab/codex-issue-memory
  - Applies to: reproducibility context in `2604.27283-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Mehmet Iscan
  - arXiv author search: https://arxiv.org/search/?query=Mehmet%20Iscan&searchtype=author
  - Applies to: the reviewed paper and `2604.27283-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
