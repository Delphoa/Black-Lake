# DEP-A-20260818-uva irlab conv at

#artificial-intelligence #arXiv #paper-review #RAG #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.11945v1, *uva-irlab-conv at SemEval-2026 Task 8: Multi-Turn RAG with Learned Sparse Retrieval and Listwise Reranking*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.11945-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.11945-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Our approach follows a multi-stage retrieval-augmented generation (RAG) pipeline combining conversational query rewriting, learned sparse retrieval (LSR), and LLM-based reranking. Describe the issue below: Abstract 1 Introduction 2 Background 3 System Overview 4 Experimental setup 5 Results 6 Conclusion 7 Acknowledgments References A Prompts Our system implements a multi-stage cascading RAG pipeline combining LLM-based conversational query rewriting, learned sparse retrieval, pointwise and LLM listwise reranking, and final response generation. Task A - Retrieval nDCG @1 @5* @10 (best baseline) GPT-OSS-20b QR + ELSER – 0.4795 – LSR w/ LION-SP-8B (retrieval) 0.4910 0.4841 0.5343 + Qwen3-Reranker-8B (pointwise) 0.5120 0.5477 0.5921 + GPT-4.1 Listwise Reranking ( † \dagger ) 0.5331 0.5475 0.5943 (Rank 2 out of 38) Table 1: Retrieval performance of our submission on Task A of the MT-RAG SemEval 2026 MTRAG Task 8.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat uva-irlab-conv at SemEval-2026 Task 8: Multi-Turn RAG with Learned Sparse Retrieval and Listwise Reranking as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260814-RAG Chunk Coverage](../DEP-A-20260814-RAG%20Chunk%20Coverage/README.md) - benchmark context for evidence coverage and retrieval failure. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.11945v1
  - Applies to: `2606.11945-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.11945v1
  - Applies to: `2606.11945-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.11945v1
  - Applies to: `2606.11945-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.11945
  - Applies to: `2606.11945-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Simon Lupart
  - arXiv author search: https://arxiv.org/search/?query=Simon%20Lupart&searchtype=author
  - Applies to: the reviewed paper and `2606.11945-whitepaper-review.md`.
- Author: Kidist Amde Mekonnen
  - arXiv author search: https://arxiv.org/search/?query=Kidist%20Amde%20Mekonnen&searchtype=author
  - Applies to: the reviewed paper and `2606.11945-whitepaper-review.md`.
- Author: Zahra Abbasiantaeb
  - arXiv author search: https://arxiv.org/search/?query=Zahra%20Abbasiantaeb&searchtype=author
  - Applies to: the reviewed paper and `2606.11945-whitepaper-review.md`.
- Author: Mohammad Aliannejadi
  - arXiv author search: https://arxiv.org/search/?query=Mohammad%20Aliannejadi&searchtype=author
  - Applies to: the reviewed paper and `2606.11945-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
