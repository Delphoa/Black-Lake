# DEP-A-20260812-TF Engram SSD

#artificial-intelligence #external-memory #SSD #LLM-inference #prefetching #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.07388v1, *TF-Engram: A Train-Free Engram with SSD-Backed Memory for Large Language Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.07388-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.07388-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: To address these issues, we propose TF-Engram , a train-free Engram with SSD-backed memory for large language models. The system analysis further shows that large TF-Engram tables can be constructed with moderate offline cost, while the SSD-backed hierarchy substantially reduces GPU memory demand compared with GPU-resident memory. System evaluation shows that large TF-Engram tables can be built with moderate offline cost, SSD-backed storage substantially reduces GPU memory demand, and predictive prefetching recovers much of the throughput loss caused by external memory access.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat SSD-backed engrams as a tiered semantic cache with explicit collision, freshness, and prefetch risk: bind phrase entries to corpus and encoder versions, measure misprefetch cost, and revert to the frozen backbone when fetched state is stale or uncertain.

## Associated DEP Records

- [DEP-A-20260717-Agent Memory Systems](../../Series%20001/DEP-A-20260717-Agent%20Memory%20Systems/README.md) - direct agent-memory lifecycle and systems context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260809-ScoutAttention Offload](../DEP-A-20260809-ScoutAttention%20Offload/README.md) - direct KV offload, retrieval, and long-context serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.07388v1
  - Applies to: `2607.07388-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.07388v1
  - Applies to: `2607.07388-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.07388v1
  - Applies to: `2607.07388-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.07388
  - Applies to: `2607.07388-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yutang Ma
  - arXiv author search: https://arxiv.org/search/?query=Yutang%20Ma&searchtype=author
  - Applies to: the reviewed paper and `2607.07388-whitepaper-review.md`.
- Author: Kecheng Huang
  - arXiv author search: https://arxiv.org/search/?query=Kecheng%20Huang&searchtype=author
  - Applies to: the reviewed paper and `2607.07388-whitepaper-review.md`.
- Author: Xikun Jiang
  - arXiv author search: https://arxiv.org/search/?query=Xikun%20Jiang&searchtype=author
  - Applies to: the reviewed paper and `2607.07388-whitepaper-review.md`.
- Author: Zili Shao
  - arXiv author search: https://arxiv.org/search/?query=Zili%20Shao&searchtype=author
  - Applies to: the reviewed paper and `2607.07388-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
