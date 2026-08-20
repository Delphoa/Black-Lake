# DEP-A-20260813-MIRROR RAG Red Team

#artificial-intelligence #agentic-RAG #red-teaming #MCTS #memory #security

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.26793v1, *MIRROR: Novelty-Constrained Memory-Guided MCTS Red-Teaming for Agentic RAG*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.26793-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.26793-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We introduce MIRROR (Memory-Informed Red-teaming with Retrieval-Restricted Optimization and Rollouts), which performs memory-guided MCTS across attack surfaces (text, image, direct query, orchestrator): retrieved traces induce operator priors and per-case rejection sets, and a deterministic Novelty Gate enforces non-duplication while search refines candidates via mutation operators and simulator rollouts under a fixed query budget. We construct and release ART-SafeBench (v2.0.0) on Hugging Face, generated via our taxonomy-driven generate-and-test pipeline and used as the initialization corpus for MIRROR ’s episodic memory. We present MIRROR , a unified cross-surface framework that performs memory-guided Monte Carlo tree search while conditioning candidate generation on retrieved context under an explicit novelty constraint.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate memory-guided red-teaming as a novelty-bounded search ledger: retain retrieved traces, tree expansions, novelty scores, budgets, and replay verification, and distinguish discovered attack diversity from verified target failures.

## Associated DEP Records

- [DEP-A-20260717-Trajectory Forensics](../../Series%20001/DEP-A-20260717-Trajectory%20Forensics/README.md) - direct long-horizon memory-attack detection and trajectory-security context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260725-RAR Reranking Intake](../../Series%20001/DEP-A-20260725-RAR%20Reranking%20Intake/README.md) - direct retrieval representation, reranking, and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.26793v1
  - Applies to: `2606.26793-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.26793v1
  - Applies to: `2606.26793-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.26793v1
  - Applies to: `2606.26793-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.26793
  - Applies to: `2606.26793-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/FujitsuResearch/mirror
  - Applies to: reproducibility context in `2606.26793-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/datasets/Fujitsu/agentic-rag-redteam-bench
  - Applies to: reproducibility context in `2606.26793-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Inderjeet Singh
  - arXiv author search: https://arxiv.org/search/?query=Inderjeet%20Singh&searchtype=author
  - Applies to: the reviewed paper and `2606.26793-whitepaper-review.md`.
- Author: Andrés Murillo
  - arXiv author search: https://arxiv.org/search/?query=Andr%C3%A9s%20Murillo&searchtype=author
  - Applies to: the reviewed paper and `2606.26793-whitepaper-review.md`.
- Author: Motoyoshi Sekiya
  - arXiv author search: https://arxiv.org/search/?query=Motoyoshi%20Sekiya&searchtype=author
  - Applies to: the reviewed paper and `2606.26793-whitepaper-review.md`.
- Author: Yuki Unno
  - arXiv author search: https://arxiv.org/search/?query=Yuki%20Unno&searchtype=author
  - Applies to: the reviewed paper and `2606.26793-whitepaper-review.md`.
- Author: Junichi Suga
  - arXiv author search: https://arxiv.org/search/?query=Junichi%20Suga&searchtype=author
  - Applies to: the reviewed paper and `2606.26793-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
