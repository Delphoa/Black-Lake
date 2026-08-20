# DEP-A-20260813-AdaMem Personal Agents

#artificial-intelligence #personalized-agents #long-term-memory #memory-selection #language-models #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.21144v1, *AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.21144-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.21144-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: (2) We propose AdaMem , which learns a role-specific Memory Policy from feedback and applies patch-style reflection with failure rollback to decide what to write—a lightweight recipe that drops into existing RAG memory stacks. (3) We build AdaMem-Bench , a personalized long-horizon benchmark with golden-memory annotations, and show that across two extraction LLMs and two feedback modes AdaMem improves QA accuracy by up to +9.0% while shrinking memory volume by 9% ; our analysis localizes the gains to “soft preference” categories (emotions, promises, schedules) and identifies policy inference from weak feedback as the primary remaining bottleneck. AdaMem: Learning What to Remember for Personalized Long-Horizon LLM Agents Xingyu Chen Shanghai Jiao Tong University, Tencent galaxychen@sjtu.edu.cn Rui Wang † † thanks: Corresponding authors.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Model personalized agent memory as a learned write gate with explicit provenance: retain candidate memories, selection probabilities, user identity scope, downstream utility, and deletions, and require counterfactual tests against storing or retrieving everything.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../../Series%20001/DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory lifecycle and systems context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260719-Agent Memory Benchmark](../../Series%20001/DEP-A-20260719-Agent%20Memory%20Benchmark/README.md) - direct memory-agent benchmarking and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.21144v1
  - Applies to: `2606.21144-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.21144v1
  - Applies to: `2606.21144-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.21144v1
  - Applies to: `2606.21144-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.21144
  - Applies to: `2606.21144-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/galaxyChen/AdaMem
  - Applies to: reproducibility context in `2606.21144-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Xingyu Chen
  - arXiv author search: https://arxiv.org/search/?query=Xingyu%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.21144-whitepaper-review.md`.
- Author: Rui Wang
  - arXiv author search: https://arxiv.org/search/?query=Rui%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.21144-whitepaper-review.md`.
- Author: Zhaopeng Tu
  - arXiv author search: https://arxiv.org/search/?query=Zhaopeng%20Tu&searchtype=author
  - Applies to: the reviewed paper and `2606.21144-whitepaper-review.md`.
- Author: Liefeng Bo
  - arXiv author search: https://arxiv.org/search/?query=Liefeng%20Bo&searchtype=author
  - Applies to: the reviewed paper and `2606.21144-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
