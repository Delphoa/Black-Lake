# DEP-A-20260720-HeadRouter Audio

#artificial-intelligence #audio-language-models #token-pruning #attention-heads #training-free #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2604.23717v1, *HeadRouter: Dynamic Head-Weight Routing for Task-Adaptive Audio Token Pruning in Large Audio Language Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2604.23717-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2604.23717-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: HeadRouter profiles attention heads by audio-task behavior, predicts task-dependent head weights, and aggregates token-importance scores using only the routed head mixture before pruning. It targets the observation that semantic and acoustic tasks rely on different sparse head subsets.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use head routing as a conditional budget allocator with uncertainty: retain a conservative head ensemble when task classification is ambiguous, report raw per-task metrics and latency, and test whether routed heads remain stable across models, noise conditions, and domain shifts.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2604.23717v1
  - Applies to: `2604.23717-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2604.23717v1
  - Applies to: `2604.23717-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2604.23717v1
  - Applies to: `2604.23717-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2604.23717
  - Applies to: `2604.23717-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Peize He
  - arXiv author search: https://arxiv.org/search/?query=Peize%20He&searchtype=author
  - Applies to: the reviewed paper and `2604.23717-whitepaper-review.md`.
- Author: Yaodi Luo
  - arXiv author search: https://arxiv.org/search/?query=Yaodi%20Luo&searchtype=author
  - Applies to: the reviewed paper and `2604.23717-whitepaper-review.md`.
- Author: Xiaoqian Liu
  - arXiv author search: https://arxiv.org/search/?query=Xiaoqian%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2604.23717-whitepaper-review.md`.
- Author: Xuyang Liu
  - arXiv author search: https://arxiv.org/search/?query=Xuyang%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2604.23717-whitepaper-review.md`.
- Author: Jiahang Deng
  - arXiv author search: https://arxiv.org/search/?query=Jiahang%20Deng&searchtype=author
  - Applies to: the reviewed paper and `2604.23717-whitepaper-review.md`.
- Author: Yaosong Du
  - arXiv author search: https://arxiv.org/search/?query=Yaosong%20Du&searchtype=author
  - Applies to: the reviewed paper and `2604.23717-whitepaper-review.md`.
- Author: Bangyu Li
  - arXiv author search: https://arxiv.org/search/?query=Bangyu%20Li&searchtype=author
  - Applies to: the reviewed paper and `2604.23717-whitepaper-review.md`.
- Author: Xiyan Gui
  - arXiv author search: https://arxiv.org/search/?query=Xiyan%20Gui&searchtype=author
  - Applies to: the reviewed paper and `2604.23717-whitepaper-review.md`.
- Author: Yuxuan Chen
  - arXiv author search: https://arxiv.org/search/?query=Yuxuan%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2604.23717-whitepaper-review.md`.
- Author: Linfeng Zhang
  - arXiv author search: https://arxiv.org/search/?query=Linfeng%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2604.23717-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
