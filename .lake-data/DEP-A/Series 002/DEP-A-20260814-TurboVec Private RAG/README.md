# DEP-A-20260814-TurboVec Private RAG

#artificial-intelligence #private-retrieval #vector-search #quantization #enterprise-RAG #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.16973v1, *TurboVec: A Case Study in Cost-Efficient Private Retrieval for Enterprise RAG via Codebook-Oblivious Quantization*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.16973-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.16973-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Codebook-based membership inference evaluation (Section VI ): Under a narrow threat model and a specific quantization-error attack on synthetic d=256 data, TurboVec’s codebook-oblivious design reduces attack accuracy to near-random versus PQ codebooks (see Limitation 3). User queries are embedded, matched against a shared multi-tenant vector store using codebook-oblivious 4-bit quantization, and filtered at the kernel level via per-request allowlists before retrieval results are passed to the LLM. We study TurboVec, an open-source vector index built on TurboQuant [ 1 ] —a codebook-oblivious scalar quantizer that derives quantization boundaries analytically from known distributional properties of high-dimensional, L2-normalized embeddings, requiring no corpus-dependent training.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat codebook-oblivious quantization as a joint memory, privacy, and filtering contract: version rotations and calibration, test membership leakage under explicit threat models, and compare selective-query recall against matched-memory alternatives.

## Associated DEP Records

- [DEP-A-20260725-RAR Reranking Intake](../../Series%20001/DEP-A-20260725-RAR%20Reranking%20Intake/README.md) - direct retrieval representation, reranking, and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.16973v1
  - Applies to: `2607.16973-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.16973v1
  - Applies to: `2607.16973-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.16973v1
  - Applies to: `2607.16973-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.16973
  - Applies to: `2607.16973-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Navnit Shukla
  - arXiv author search: https://arxiv.org/search/?query=Navnit%20Shukla&searchtype=author
  - Applies to: the reviewed paper and `2607.16973-whitepaper-review.md`.
- Author: Kamal Pandey
  - arXiv author search: https://arxiv.org/search/?query=Kamal%20Pandey&searchtype=author
  - Applies to: the reviewed paper and `2607.16973-whitepaper-review.md`.
- Author: Omsankar Tiwari
  - arXiv author search: https://arxiv.org/search/?query=Omsankar%20Tiwari&searchtype=author
  - Applies to: the reviewed paper and `2607.16973-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
