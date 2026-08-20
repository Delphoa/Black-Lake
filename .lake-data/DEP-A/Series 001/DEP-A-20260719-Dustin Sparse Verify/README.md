# DEP-A-20260719-Dustin Sparse Verify

#artificial-intelligence #speculative-decoding #sparse-attention #KV-cache #long-context #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.24957v1, *Dustin: Draft-Augmented Sparse Verification for Efficient Long-Context Generation with Speculative Decoding*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.24957-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.24957-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Dustin sparsifies target-model verification by combining draft-model lookahead attention with historical target attention to select critical KV tokens across a multi-token verification window. It further estimates importance through a small set of semantic-retrieval heads to avoid making token selection more expensive than full attention.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Make verification sparsity adaptive: estimate expected acceptance gain per byte loaded, widen the cache when draft-target disagreement rises, and retain a calibrated dense-verification escape hatch whose triggers are evaluated on distribution shifts.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.24957v1
  - Applies to: `2606.24957-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.24957v1
  - Applies to: `2606.24957-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.24957v1
  - Applies to: `2606.24957-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.24957
  - Applies to: `2606.24957-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: WenHung Lee
  - arXiv author search: https://arxiv.org/search/?query=WenHung%20Lee&searchtype=author
  - Applies to: the reviewed paper and `2606.24957-whitepaper-review.md`.
- Author: Jian-Jia Chen
  - arXiv author search: https://arxiv.org/search/?query=Jian-Jia%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.24957-whitepaper-review.md`.
- Author: Xiaolin Lin
  - arXiv author search: https://arxiv.org/search/?query=Xiaolin%20Lin&searchtype=author
  - Applies to: the reviewed paper and `2606.24957-whitepaper-review.md`.
- Author: Pei-Shuo Wang
  - arXiv author search: https://arxiv.org/search/?query=Pei-Shuo%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.24957-whitepaper-review.md`.
- Author: Chi-Chih Chang
  - arXiv author search: https://arxiv.org/search/?query=Chi-Chih%20Chang&searchtype=author
  - Applies to: the reviewed paper and `2606.24957-whitepaper-review.md`.
- Author: Chun-Che Yang
  - arXiv author search: https://arxiv.org/search/?query=Chun-Che%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2606.24957-whitepaper-review.md`.
- Author: Ning-Chi Huang
  - arXiv author search: https://arxiv.org/search/?query=Ning-Chi%20Huang&searchtype=author
  - Applies to: the reviewed paper and `2606.24957-whitepaper-review.md`.
- Author: Grace Li Zhang
  - arXiv author search: https://arxiv.org/search/?query=Grace%20Li%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.24957-whitepaper-review.md`.
- Author: Kai-Chiang Wu
  - arXiv author search: https://arxiv.org/search/?query=Kai-Chiang%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2606.24957-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
