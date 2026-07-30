# DEP-A-20260731-ReMP Reconfiguration

#artificial-intelligence #LLM-serving #model-parallelism #reconfiguration #availability #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.18741v1, *ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.18741-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.18741-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Consequently, the vast majority of production systems remain stuck with static, fixed parallel configurations We present ReMP—a low-downtime, runtime model-parallel reconfiguration framework tailored for large language model (LLM) inference serving. Experimental results on two 8-GPU platforms, NVIDIA H100 and RTX 5090, demonstrate that ReMP makes runtime model-parallelism reconfiguration practical for mainstream LLM serving. ReMP achieves dynamic adjustment through three key techniques: (1) decoupling the model parallelism topology from runtime state to avoid full service reconstruction; (2) designing a two-dimensional KV cache migration mechanism to preserve reusable cache states after TP/PP changes; and (3) implementing end-to-end online reconfiguration.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Turn memory reconfiguration into a closed-loop controller with declared state, bounded actions, tail-latency and quality constraints, rollback checkpoints, and counterfactual evaluation that distinguishes controller benefit from workload drift.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct KV-cache, real-time interaction, and serving-systems context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.18741v1
  - Applies to: `2606.18741-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.18741v1
  - Applies to: `2606.18741-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.18741v1
  - Applies to: `2606.18741-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.18741
  - Applies to: `2606.18741-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Haipeng Yuan
  - arXiv author search: https://arxiv.org/search/?query=Haipeng%20Yuan&searchtype=author
  - Applies to: the reviewed paper and `2606.18741-whitepaper-review.md`.
- Author: Kaining Zheng
  - arXiv author search: https://arxiv.org/search/?query=Kaining%20Zheng&searchtype=author
  - Applies to: the reviewed paper and `2606.18741-whitepaper-review.md`.
- Author: Yongshu Bai
  - arXiv author search: https://arxiv.org/search/?query=Yongshu%20Bai&searchtype=author
  - Applies to: the reviewed paper and `2606.18741-whitepaper-review.md`.
- Author: Yuchen Zhang
  - arXiv author search: https://arxiv.org/search/?query=Yuchen%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.18741-whitepaper-review.md`.
- Author: Yunquan Zhang
  - arXiv author search: https://arxiv.org/search/?query=Yunquan%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.18741-whitepaper-review.md`.
- Author: Baodong Wu
  - arXiv author search: https://arxiv.org/search/?query=Baodong%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2606.18741-whitepaper-review.md`.
- Author: Xiang Gao
  - arXiv author search: https://arxiv.org/search/?query=Xiang%20Gao&searchtype=author
  - Applies to: the reviewed paper and `2606.18741-whitepaper-review.md`.
- Author: Daning Cheng
  - arXiv author search: https://arxiv.org/search/?query=Daning%20Cheng&searchtype=author
  - Applies to: the reviewed paper and `2606.18741-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
