# DEP-A-20260722-SentAttack Retrieval

#artificial-intelligence #dense-retrieval #adversarial-attacks #retrieval-augmented-generation #black-box-attacks #security

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.03456v1, *SentAttack: A Sentence-Level Black-Box Adversarial Attack Method for Dense Retrieval Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.03456-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.03456-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: SentAttack first extracts a surrogate dense retriever by repeatedly querying a black-box top-k interface. It then clusters relevant-document embeddings, concatenates centroid-derived sentences with a low-ranked target document, and refines candidates through a query/centroid objective and gradient-guided synonym beam search.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Evaluate retrieval systems with rank-query rate limits, ingestion provenance, semantic-drift detectors, and cross-encoder contradiction checks; retain adversarial canaries and measure attack cost, detectability, and downstream answer harm together.

## Associated DEP Records

- [DEP-A-20260715-FAIR GraphRAG A Retrieval](../DEP-A-20260715-FAIR%20GraphRAG%20A%20Retrieval/README.md) - direct governed graph retrieval context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.03456v1
  - Applies to: `2607.03456-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.03456v1
  - Applies to: `2607.03456-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.03456v1
  - Applies to: `2607.03456-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.03456
  - Applies to: `2607.03456-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Luping Wei
  - arXiv author search: https://arxiv.org/search/?query=Luping%20Wei&searchtype=author
  - Applies to: the reviewed paper and `2607.03456-whitepaper-review.md`.
- Author: Yamin Hu
  - arXiv author search: https://arxiv.org/search/?query=Yamin%20Hu&searchtype=author
  - Applies to: the reviewed paper and `2607.03456-whitepaper-review.md`.
- Author: Sihan Shang
  - arXiv author search: https://arxiv.org/search/?query=Sihan%20Shang&searchtype=author
  - Applies to: the reviewed paper and `2607.03456-whitepaper-review.md`.
- Author: Shiyin Wang
  - arXiv author search: https://arxiv.org/search/?query=Shiyin%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.03456-whitepaper-review.md`.
- Author: Wenjian Luo
  - arXiv author search: https://arxiv.org/search/?query=Wenjian%20Luo&searchtype=author
  - Applies to: the reviewed paper and `2607.03456-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
