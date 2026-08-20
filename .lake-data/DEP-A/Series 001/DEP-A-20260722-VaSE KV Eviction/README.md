# DEP-A-20260722-VaSE KV Eviction

#artificial-intelligence #KV-cache #cache-eviction #reasoning-models #sparse-attention #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.03928v1, *Value-Aware Stochastic KV Cache Eviction for Reasoning Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.03928-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.03928-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: VaSE is a training-free decode-phase eviction recipe. It reserves cache slots for value vectors with unusually large dynamic range and samples the remaining entries stochastically from attention- or diversity-based scores, preserving both high-magnitude value states and cache diversity under a fixed budget.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Reserve cache capacity from a calibrated risk score combining value range, attention, and eviction uncertainty; record stochastic seeds and catastrophic-loop detectors, and restore full or selection-based attention when reasoning degenerates.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.03928v1
  - Applies to: `2606.03928-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.03928v1
  - Applies to: `2606.03928-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.03928v1
  - Applies to: `2606.03928-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.03928
  - Applies to: `2606.03928-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/terarachang/VaSE
  - Applies to: reproducibility context in `2606.03928-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Ting-Yun Chang
  - arXiv author search: https://arxiv.org/search/?query=Ting-Yun%20Chang&searchtype=author
  - Applies to: the reviewed paper and `2606.03928-whitepaper-review.md`.
- Author: Harvey Yiyun Fu
  - arXiv author search: https://arxiv.org/search/?query=Harvey%20Yiyun%20Fu&searchtype=author
  - Applies to: the reviewed paper and `2606.03928-whitepaper-review.md`.
- Author: Deqing Fu
  - arXiv author search: https://arxiv.org/search/?query=Deqing%20Fu&searchtype=author
  - Applies to: the reviewed paper and `2606.03928-whitepaper-review.md`.
- Author: Chenghao Yang
  - arXiv author search: https://arxiv.org/search/?query=Chenghao%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2606.03928-whitepaper-review.md`.
- Author: Jesse Thomason
  - arXiv author search: https://arxiv.org/search/?query=Jesse%20Thomason&searchtype=author
  - Applies to: the reviewed paper and `2606.03928-whitepaper-review.md`.
- Author: Robin Jia
  - arXiv author search: https://arxiv.org/search/?query=Robin%20Jia&searchtype=author
  - Applies to: the reviewed paper and `2606.03928-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
