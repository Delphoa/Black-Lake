# DEP-A-20260815-SAG Dynamic Hyperedges

#artificial-intelligence #RAG #SQL #dynamic-hyperedges #multi-hop-retrieval #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.15971v1, *SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.15971-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.15971-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: HippoRAG 2 first extracts entities and relations offline from documents using an LLM and builds a knowledge graph, then performs multi-hop graph retrieval at query time via Personalized PageRank, representing a leading implementation of the ”offline graph construction + global graph ranking” paradigm and forming a direct mechanistic contrast with SAG’s “query-time dynamic hyperedge” approach. It unifies three capabilities: structured filtering, semantic expansion, and LLM fine ranking in a single pipeline; (2) we design a query-time dynamic hyperedge organization mechanism, enabling higher-order relations to be dynamically activated within a local candidate space around the current query without prior enumeration, and to be deterministically expanded across multiple hops via SQL joins; (3) we systematically evaluate SAG on three multi-hop benchmarks and, through ablation studies, isolate the respective contributions of event-level semantic preservation, dynamic expansion, LLM usage patterns, and candidate budget; (4) we have deployed SAG in a production environment at a scale of hundreds of millions of records, demonstrating the engineering feasibility of this framework under continuous incremental writes and online cost.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat SAG: SQL-Retrieval Augmented Generation with Query-Time Dynamic Hyperedges as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260814-HyGRAG Framework](../DEP-A-20260814-HyGRAG%20Framework/README.md) - direct graph retrieval and relation-aware RAG context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.15971v1
  - Applies to: `2606.15971-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.15971v1
  - Applies to: `2606.15971-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.15971v1
  - Applies to: `2606.15971-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.15971
  - Applies to: `2606.15971-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/Zleap-AI/SAG-Benchmark
  - Applies to: reproducibility context in `2606.15971-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Yuchao Wu
  - arXiv author search: https://arxiv.org/search/?query=Yuchao%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2606.15971-whitepaper-review.md`.
- Author: Junqin Li
  - arXiv author search: https://arxiv.org/search/?query=Junqin%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.15971-whitepaper-review.md`.
- Author: XingCheng Liang
  - arXiv author search: https://arxiv.org/search/?query=XingCheng%20Liang&searchtype=author
  - Applies to: the reviewed paper and `2606.15971-whitepaper-review.md`.
- Author: Yongjie Chen
  - arXiv author search: https://arxiv.org/search/?query=Yongjie%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.15971-whitepaper-review.md`.
- Author: Yinghao Liang
  - arXiv author search: https://arxiv.org/search/?query=Yinghao%20Liang&searchtype=author
  - Applies to: the reviewed paper and `2606.15971-whitepaper-review.md`.
- Author: Linyuan Mo
  - arXiv author search: https://arxiv.org/search/?query=Linyuan%20Mo&searchtype=author
  - Applies to: the reviewed paper and `2606.15971-whitepaper-review.md`.
- Author: Guanxian Li
  - arXiv author search: https://arxiv.org/search/?query=Guanxian%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.15971-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
