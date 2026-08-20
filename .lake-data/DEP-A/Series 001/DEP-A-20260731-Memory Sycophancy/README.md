# DEP-A-20260731-Memory Sycophancy

#artificial-intelligence #agent-memory #sycophancy #alignment #mitigation #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.10949v1, *Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.10949-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.10949-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Finally, we propose several evaluation metrics to measure sycophancy in memory-augmented LLMs. Motivated by these findings, we propose two simple mitigation strategies: (1) strictly including assistant turns along with user turns in memory extraction, (2) summarizing the chat conversation using an LLM instead of memory extraction. A successful mitigation should reduce sycophancy while at least matching baseline LoCoMo-MC10 accuracy; trading memory utility for sycophancy reduction is not a practical improvement.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Add an anti-sycophancy validity layer to memory retrieval that separates remembered user claims from independently supported facts, measures agreement pressure, and triggers clarification when retrieved preference conflicts with external evidence.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory systems and lifecycle context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260719-Agent Memory Benchmark](../DEP-A-20260719-Agent%20Memory%20Benchmark/README.md) - direct agent-memory benchmark and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.10949v1
  - Applies to: `2606.10949-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.10949v1
  - Applies to: `2606.10949-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.10949v1
  - Applies to: `2606.10949-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.10949
  - Applies to: `2606.10949-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://huggingface.co/datasets/Percena/locomo-mc10
  - Applies to: reproducibility context in `2606.10949-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Shelly Bensal
  - arXiv author search: https://arxiv.org/search/?query=Shelly%20Bensal&searchtype=author
  - Applies to: the reviewed paper and `2606.10949-whitepaper-review.md`.
- Author: Axel Magnuson
  - arXiv author search: https://arxiv.org/search/?query=Axel%20Magnuson&searchtype=author
  - Applies to: the reviewed paper and `2606.10949-whitepaper-review.md`.
- Author: Aparna Balagopalan
  - arXiv author search: https://arxiv.org/search/?query=Aparna%20Balagopalan&searchtype=author
  - Applies to: the reviewed paper and `2606.10949-whitepaper-review.md`.
- Author: Daniel M. Bikel
  - arXiv author search: https://arxiv.org/search/?query=Daniel%20M.%20Bikel&searchtype=author
  - Applies to: the reviewed paper and `2606.10949-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
