# DEP-A-20260724-ReasonAlloc KV Routing

#artificial-intelligence #reasoning-models #KV-cache #resource-allocation #long-context #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.11164v1, *ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.11164-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.11164-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: ReasonAlloc treats decoding-time KV compression as hierarchical resource routing. Offline calibration captures an architecture-specific non-monotonic layer-demand profile, while an online router reallocates each layer budget across heads from current token-importance scores.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Version an architecture demand profile, continuously audit its drift, and route head budgets online only inside hard per-layer and global memory envelopes with a conservative uniform fallback.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct cache-budget and efficient-attention context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.11164v1
  - Applies to: `2606.11164-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.11164v1
  - Applies to: `2606.11164-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.11164v1
  - Applies to: `2606.11164-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.11164
  - Applies to: `2606.11164-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Wenhao Liu
  - arXiv author search: https://arxiv.org/search/?query=Wenhao%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2606.11164-whitepaper-review.md`.
- Author: Hao Shi
  - arXiv author search: https://arxiv.org/search/?query=Hao%20Shi&searchtype=author
  - Applies to: the reviewed paper and `2606.11164-whitepaper-review.md`.
- Author: Yunhe Li
  - arXiv author search: https://arxiv.org/search/?query=Yunhe%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.11164-whitepaper-review.md`.
- Author: Weizhi Fei
  - arXiv author search: https://arxiv.org/search/?query=Weizhi%20Fei&searchtype=author
  - Applies to: the reviewed paper and `2606.11164-whitepaper-review.md`.
- Author: Xiangyuan Wang
  - arXiv author search: https://arxiv.org/search/?query=Xiangyuan%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.11164-whitepaper-review.md`.
- Author: Mengzhe Ruan
  - arXiv author search: https://arxiv.org/search/?query=Mengzhe%20Ruan&searchtype=author
  - Applies to: the reviewed paper and `2606.11164-whitepaper-review.md`.
- Author: Hanxu Hou
  - arXiv author search: https://arxiv.org/search/?query=Hanxu%20Hou&searchtype=author
  - Applies to: the reviewed paper and `2606.11164-whitepaper-review.md`.
- Author: Peisong Wang
  - arXiv author search: https://arxiv.org/search/?query=Peisong%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.11164-whitepaper-review.md`.
- Author: Linqi Song
  - arXiv author search: https://arxiv.org/search/?query=Linqi%20Song&searchtype=author
  - Applies to: the reviewed paper and `2606.11164-whitepaper-review.md`.
- Author: Shuang Qiu
  - arXiv author search: https://arxiv.org/search/?query=Shuang%20Qiu&searchtype=author
  - Applies to: the reviewed paper and `2606.11164-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
