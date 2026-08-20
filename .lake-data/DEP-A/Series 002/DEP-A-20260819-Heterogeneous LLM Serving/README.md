# DEP-A-20260819-Heterogeneous LLM Serving

#artificial-intelligence #arXiv #paper-review #RAG #memory #attention #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.03555v1, *Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.03555-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.03555-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: ( O5 ) Retrieval-based sparse attention still calls for near-memory processing, but it changes what such a design must provide: the compute must remain colocated with the KV cache and index keys, sustain a higher OI than prior designs assume, and accommodate operations that vary across models. A KARAT device combines LPDDR memory, which provides high memory capacity per watt, with general-purpose PNM (GPNM) cores that sustain the OI of the target operations while supporting diverse retrieval-based sparse attention algorithms. To meet the requirements of retrieval-based sparse attention, we propose a heterogeneous decode-phase serving system for long-context LLMs (Fig.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.03555v1
  - Applies to: `2608.03555-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.03555v1
  - Applies to: `2608.03555-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.03555v1
  - Applies to: `2608.03555-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.03555
  - Applies to: `2608.03555-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Hyungkyu Ham
  - arXiv author search: https://arxiv.org/search/?query=Hyungkyu%20Ham&searchtype=author
  - Applies to: the reviewed paper and `2608.03555-whitepaper-review.md`.
- Author: Junhyeong Bae
  - arXiv author search: https://arxiv.org/search/?query=Junhyeong%20Bae&searchtype=author
  - Applies to: the reviewed paper and `2608.03555-whitepaper-review.md`.
- Author: Seungheon Lee
  - arXiv author search: https://arxiv.org/search/?query=Seungheon%20Lee&searchtype=author
  - Applies to: the reviewed paper and `2608.03555-whitepaper-review.md`.
- Author: Myeongjae Jeon
  - arXiv author search: https://arxiv.org/search/?query=Myeongjae%20Jeon&searchtype=author
  - Applies to: the reviewed paper and `2608.03555-whitepaper-review.md`.
- Author: Gwangsun Kim
  - arXiv author search: https://arxiv.org/search/?query=Gwangsun%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2608.03555-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
