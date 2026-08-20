# DEP-A-20260731-AdaMerge Tokens

#artificial-intelligence #computer-vision #vision-transformers #token-merging #efficient-inference #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.27465v1, *AdaMerge: Salience-Aware Adaptive Token Merging for Training-Free Acceleration of Vision Transformers*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.27465-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.27465-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: ‡ At comparable merge counts, Full AdaMerge ( r max = 24 r_{\max}{=}24 , 70.7 tokens merged, 84.13%) outperforms Adaptive r only (68.8 tokens merged, 83.62%) by + 0.51 +0.51 %p, even while merging more tokens, confirming that the accuracy gain stems from the quality of merging decisions rather than from a reduced merge count. To rule out the hypothesis that AdaMerge ’s gain stems merely from merging fewer tokens, we compare at comparable merge counts: Full AdaMerge at r max = 24 r_{\max}{=}24 (70.7 tokens merged, 84.13%) outperforms Adaptive r r only (68.8 tokens merged, 83.62%) by + 0.51 +0.51 %p despite merging more tokens , confirming that the advantage arises from merging quality rather than reduced count. To our knowledge, AdaMerge is the first to combine salience-weighted similarity and adaptive per-layer reduction into a single training-free token merging framework, advancing the accuracy–FLOPs Pareto frontier of ViT acceleration.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Allocate token merging from calibrated salience while protecting rare or decision-critical regions, logging per-layer merge maps, monitoring accuracy drift by subgroup, and retaining an unmerged inference path for ambiguous or high-consequence inputs.

## Associated DEP Records

- [DEP-A-20260716-K Token Merging](../DEP-A-20260716-K%20Token%20Merging/README.md) - direct token-merging and representation-compression context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.27465v1
  - Applies to: `2605.27465-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.27465v1
  - Applies to: `2605.27465-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.27465v1
  - Applies to: `2605.27465-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.27465
  - Applies to: `2605.27465-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Semi Lee
  - arXiv author search: https://arxiv.org/search/?query=Semi%20Lee&searchtype=author
  - Applies to: the reviewed paper and `2605.27465-whitepaper-review.md`.
- Author: Hyejin Go
  - arXiv author search: https://arxiv.org/search/?query=Hyejin%20Go&searchtype=author
  - Applies to: the reviewed paper and `2605.27465-whitepaper-review.md`.
- Author: Hyesong Choi
  - arXiv author search: https://arxiv.org/search/?query=Hyesong%20Choi&searchtype=author
  - Applies to: the reviewed paper and `2605.27465-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
