# DEP-A-20260816-Dynamic RAG Privacy

#artificial-intelligence #RAG #differential-privacy #dynamic-queries #privacy-utility #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.14811v1, *Is External Database Protection Static in Retrieval-Augmented Generation? Rethinking Privacy Preservation under Dynamic Queries*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.14811-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.14811-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We propose a Prompt-Aware Dynamic Hierarchical Differential Privacy protection framework. Describe the issue below: Abstract I Introduction II-A Privacy protection for Token-level Generation II-B Privacy protection for External Databases II-C Privacy protection for Training stage III Preliminary IV-A Retrieval and Text Preprocessing IV-B 1 Risk-aware semantic similarity IV-B 2 Field sensitivity IV-B 3 Risk assessment IV-C 1 Candidate text generation IV-C 2 Utility function design IV-C 3 Semantic exponential mechanism construction IV-C 4 Hierarchical DP protection V-A 1 Datasets V-A 2 Baselines V-A 3 Experimental Setup V-B 1 Results on Medical Dialog V-B 2 Results on ODQA V-C 1 Results on Targeted Attack V-C 2 Results on Untargeted Attack V-D 1 Impact of Privacy Budgets V-D 2 Impact of the retrieved number of documents V-D 3 Impact of Model Choice V-E Hyperparameter Choice V-F Efficiency Analysis VI- 1 limitation References -A Missing experimental results Step 1: Laplace Mechanism for Risk Score. Existing privacy-preserving RAG approaches can be broadly categorized into three directions: (1) token-level generation protection based on differential privacy, (2) protection based on external databases, and (3) other privacy protection.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Is External Database Protection Static in Retrieval-Augmented Generation? Rethinking Privacy Preservation under Dynamic Queries as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260814-TurboVec Private RAG](../DEP-A-20260814-TurboVec%20Private%20RAG/README.md) - direct RAG privacy and utility context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.14811v1
  - Applies to: `2607.14811-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.14811v1
  - Applies to: `2607.14811-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.14811v1
  - Applies to: `2607.14811-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.14811
  - Applies to: `2607.14811-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Gang Zhang
  - arXiv author search: https://arxiv.org/search/?query=Gang%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.14811-whitepaper-review.md`.
- Author: Mingyu Tian
  - arXiv author search: https://arxiv.org/search/?query=Mingyu%20Tian&searchtype=author
  - Applies to: the reviewed paper and `2607.14811-whitepaper-review.md`.
- Author: Xukun Luan
  - arXiv author search: https://arxiv.org/search/?query=Xukun%20Luan&searchtype=author
  - Applies to: the reviewed paper and `2607.14811-whitepaper-review.md`.
- Author: Yuanchi Ma
  - arXiv author search: https://arxiv.org/search/?query=Yuanchi%20Ma&searchtype=author
  - Applies to: the reviewed paper and `2607.14811-whitepaper-review.md`.
- Author: Jinyan Liu
  - arXiv author search: https://arxiv.org/search/?query=Jinyan%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.14811-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
