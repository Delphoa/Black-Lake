# DEP-A-20260727-SproutRAG Tree

#artificial-intelligence #retrieval-augmented-generation #tree-search #information-extraction #reasoning #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.18381v1, *SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.18381-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.18381-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: SproutRAG uses sentence-level embeddings and learned inter-sentence attention to build a bottom-up binary tree whose internal nodes receive progressive embeddings. At query time, hierarchical beam search retrieves across leaves and internal nodes, then optional reranking and generation operate on a common evidence-unit budget. The joint training objective separates retrieval alignment from attention-structure supervision.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: View the hierarchy as a learned evidence-budget scheduler: log which granularity wins for each query and test whether attention-derived structure predicts multi-sentence relevance better than a cost-matched semantic tree under corpus shift. Falsification would be failure to retain the reported information-efficiency advantage after matching indexing, reranking, and evidence-expansion cost.

## Associated DEP Records

- [DEP-A-20260715-FAIR GraphRAG A Retrieval](../DEP-A-20260715-FAIR%20GraphRAG%20A%20Retrieval/README.md) - direct retrieval architecture and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.18381v1
  - Applies to: `2606.18381-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.18381v1
  - Applies to: `2606.18381-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.18381v1
  - Applies to: `2606.18381-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.18381
  - Applies to: `2606.18381-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/AmirAbaskohi/SproutRAG
  - Applies to: reproducibility context in `2606.18381-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Amirhossein Abaskohi
  - arXiv author search: https://arxiv.org/search/?query=Amirhossein%20Abaskohi&searchtype=author
  - Applies to: the reviewed paper and `2606.18381-whitepaper-review.md`.
- Author: Issam H. Laradji
  - arXiv author search: https://arxiv.org/search/?query=Issam%20H.%20Laradji&searchtype=author
  - Applies to: the reviewed paper and `2606.18381-whitepaper-review.md`.
- Author: Peter West
  - arXiv author search: https://arxiv.org/search/?query=Peter%20West&searchtype=author
  - Applies to: the reviewed paper and `2606.18381-whitepaper-review.md`.
- Author: Giuseppe Carenini
  - arXiv author search: https://arxiv.org/search/?query=Giuseppe%20Carenini&searchtype=author
  - Applies to: the reviewed paper and `2606.18381-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
