# DEP-A-20260731-Merged Conversational IR

#artificial-intelligence #conversational-search #model-merging #information-retrieval #reranking #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.08540v1, *Improving Ad-hoc Search Effectiveness for Conversational Information Retrieval via Model Merging*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.08540-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.08540-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Models in this merged space consistently recover a large portion of the ad-hoc effectiveness on MS MARCO, while incurring only a moderate degradation in conversational retrieval performance, for instance QRACDR-Q MG-MS reduced NDCG@3 decrease on MS MARCO from -14% to -3% while keeping similar performance on QReCC as QRACDR-Q. 3 , while MTL alleviates forgetting, our model merging approach matches or exceeds its performance across both conversational and ad-hoc retrieval tasks—without requiring gradient-based optimization or access to the original source training data (-3.7% NDCG@3 drop for MTL and -5.1% for QRACDR-T MG-MS in MS MARCO). Problem Datasets and Metrics Models Merging Optimization 4.2.1 Can model merging construct conversational retrievers with improved ad-hoc retrieval capabilities?

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat model merging for conversational retrieval as a portfolio allocation problem: retain each specialist checkpoint, record merge coefficients, test per-turn failure surfaces, and roll back when merged behavior loses complementary expertise.

## Associated DEP Records

- [DEP-A-20260725-RAR Reranking Intake](../DEP-A-20260725-RAR%20Reranking%20Intake/README.md) - direct retrieval reranking and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.08540v1
  - Applies to: `2607.08540-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.08540v1
  - Applies to: `2607.08540-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.08540v1
  - Applies to: `2607.08540-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.08540
  - Applies to: `2607.08540-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/RayaneA7/model-merging-CIR
  - Applies to: reproducibility context in `2607.08540-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Ahmed Rayane Kebir
  - arXiv author search: https://arxiv.org/search/?query=Ahmed%20Rayane%20Kebir&searchtype=author
  - Applies to: the reviewed paper and `2607.08540-whitepaper-review.md`.
- Author: Jose G. Moreno
  - arXiv author search: https://arxiv.org/search/?query=Jose%20G.%20Moreno&searchtype=author
  - Applies to: the reviewed paper and `2607.08540-whitepaper-review.md`.
- Author: Lynda Tamine
  - arXiv author search: https://arxiv.org/search/?query=Lynda%20Tamine&searchtype=author
  - Applies to: the reviewed paper and `2607.08540-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
