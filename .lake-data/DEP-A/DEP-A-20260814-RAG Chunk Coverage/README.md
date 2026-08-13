# DEP-A-20260814-RAG Chunk Coverage

#software-testing #retrieval-augmented-generation #test-coverage #fault-detection #benchmarks #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.18155v1, *Testing Retrieval-Augmented Generation Systems with Chunk Coverage*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.18155-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.18155-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Algorithm 1 Coverage-guided test generation with Chunk Coverage CC enables a coverage-guided approach to test generation for RAG systems by providing explicit feedback on which parts of the retrieval space have been exercised by a test suite. We compare CC-guided test generation/selection (see Section 4.4 for details) against both baselines in terms of coverage growth and achieved CC under a fixed testing budget, assessing whether CC provides principled guidance for achieving faster and more comprehensive exploration of retrieval behaviour. Zaharia (2023) ARES: an automated evaluation framework for retrieval-augmented generation systems .

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use chunk coverage as structural test adequacy rather than answer quality: retain corpus version, chunking, query-to-chunk hits, attainable-coverage bounds, and detected faults, and require complementary oracle-based checks before deployment claims.

## Associated DEP Records

- [DEP-A-20260725-RAR Reranking Intake](../DEP-A-20260725-RAR%20Reranking%20Intake/README.md) - direct retrieval representation, reranking, and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.18155v1
  - Applies to: `2607.18155-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.18155v1
  - Applies to: `2607.18155-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.18155v1
  - Applies to: `2607.18155-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.18155
  - Applies to: `2607.18155-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/dbr7/issta26-chunk-coverage-artifact
  - Applies to: reproducibility context in `2607.18155-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Jinhan Kim
  - arXiv author search: https://arxiv.org/search/?query=Jinhan%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2607.18155-whitepaper-review.md`.
- Author: Samuele Pasini
  - arXiv author search: https://arxiv.org/search/?query=Samuele%20Pasini&searchtype=author
  - Applies to: the reviewed paper and `2607.18155-whitepaper-review.md`.
- Author: Paolo Tonella
  - arXiv author search: https://arxiv.org/search/?query=Paolo%20Tonella&searchtype=author
  - Applies to: the reviewed paper and `2607.18155-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
