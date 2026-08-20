# DEP-A-20260727-Depth Attention

#artificial-intelligence #attention #depth-adaptation #language-models #efficient-inference #architecture

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.05014v2, *Depth-Attention: Cross-Layer Value Mixing for Language Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.05014-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.05014-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Depth-Attention lets a current-layer query attend over keys from selected earlier layers at the same token position and mix their values before ordinary sequence attention. It reuses standard query, key, and value-cache slots, storing the mixed value in place rather than retaining extra hidden-state memory.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Interpret depth attention as a learned residual-state router and test whether its weights predict which layers can be skipped or compressed. Falsification would be equal performance from a parameter-free static cross-layer average or disappearance of gains at matched training compute and optimized kernels.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct cache-budget and efficient-attention context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.05014v2
  - Applies to: `2606.05014-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.05014v2
  - Applies to: `2606.05014-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.05014v2
  - Applies to: `2606.05014-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.05014
  - Applies to: `2606.05014-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Boyi Zeng
  - arXiv author search: https://arxiv.org/search/?query=Boyi%20Zeng&searchtype=author
  - Applies to: the reviewed paper and `2606.05014-whitepaper-review.md`.
- Author: Yiqin Hao
  - arXiv author search: https://arxiv.org/search/?query=Yiqin%20Hao&searchtype=author
  - Applies to: the reviewed paper and `2606.05014-whitepaper-review.md`.
- Author: Zitong Wang
  - arXiv author search: https://arxiv.org/search/?query=Zitong%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.05014-whitepaper-review.md`.
- Author: Shixiang Song
  - arXiv author search: https://arxiv.org/search/?query=Shixiang%20Song&searchtype=author
  - Applies to: the reviewed paper and `2606.05014-whitepaper-review.md`.
- Author: He Li
  - arXiv author search: https://arxiv.org/search/?query=He%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.05014-whitepaper-review.md`.
- Author: Feichen Song
  - arXiv author search: https://arxiv.org/search/?query=Feichen%20Song&searchtype=author
  - Applies to: the reviewed paper and `2606.05014-whitepaper-review.md`.
- Author: Yifan Liu
  - arXiv author search: https://arxiv.org/search/?query=Yifan%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2606.05014-whitepaper-review.md`.
- Author: Ziwei He
  - arXiv author search: https://arxiv.org/search/?query=Ziwei%20He&searchtype=author
  - Applies to: the reviewed paper and `2606.05014-whitepaper-review.md`.
- Author: Xinbing Wang
  - arXiv author search: https://arxiv.org/search/?query=Xinbing%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.05014-whitepaper-review.md`.
- Author: Zhouhan Lin
  - arXiv author search: https://arxiv.org/search/?query=Zhouhan%20Lin&searchtype=author
  - Applies to: the reviewed paper and `2606.05014-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
