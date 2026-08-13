# DEP-A-20260730-DeferMem

#artificial-intelligence #agent-memory #evidence-distillation #reinforcement-learning #question-answering #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.22411v1, *DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.22411-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.22411-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: To address this bottleneck, we propose a novel long-term memory framework, namely DeferMem, which defers evidence distillation to query time. DeferMem decouples long-term memory question answering (QA) into two stages: high-recall candidate retrieval and query-conditioned evidence distillation. The memory distiller is trained with DistillPO, our reinforcement learning algorithm, which formulates post-retrieval evidence distillation as a structured action consisting of useful-message selection and evidence rewriting.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Separate high-recall retrieval from query-time evidence distillation, but require every rewritten evidence unit to link back to exact source spans and retain a raw-context escape path.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory systems and lifecycle context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.22411v1
  - Applies to: `2605.22411-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.22411v1
  - Applies to: `2605.22411-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.22411v1
  - Applies to: `2605.22411-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.22411
  - Applies to: `2605.22411-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Jianing Yin
  - arXiv author search: https://arxiv.org/search/?query=Jianing%20Yin&searchtype=author
  - Applies to: the reviewed paper and `2605.22411-whitepaper-review.md`.
- Author: Tan Tang
  - arXiv author search: https://arxiv.org/search/?query=Tan%20Tang&searchtype=author
  - Applies to: the reviewed paper and `2605.22411-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
