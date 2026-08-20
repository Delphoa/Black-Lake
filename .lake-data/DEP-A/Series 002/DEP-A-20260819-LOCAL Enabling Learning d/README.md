# DEP-A-20260819-LOCAL Enabling Learning d

#artificial-intelligence #arXiv #paper-review #agents #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.15241v1, *LOCAL: Enabling Learning On-device Contiguously for Agent LLMs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.15241-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.15241-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: To enable contiguous learning for on-device LLM agents, we present LOCAL, a single-GPU runtime in which inference and adaptation share the same model instance without interrupting each other. 1 Introduction 2.1 On-Device LLM Agents 2.2 Online RL for On-Device Agents 2.3 Co-Locating Inference and Training 2.4 Challenges of On-Device Inference-Training Coexistence 3 System Overview 4.1 Task Model 4.2 Foreground Priority and Cooperative Training 4.3 Timeslice-Aware Background Admission 5.1 Agent-Scoped KV Identity 5.2 Hot-Prefix Statistics 5.3 Scheduler-Visible Stale-Coverage Prefill 5.4 Priority-Based Retention and Offload 6.1 Cross-Agent Pre-Prefill 6.2 Memory-Pressure Offload Requests 6.3 Integration with the Core Runtime 7.1 Experimental Setup 7.2 Foreground-Aware Scheduling 7.3 Interruptible Training 7.4 Comparison with Full-LoRA Sleep/Train 7.5 Stale-Coverage Prefill 7.6 Cross-Agent Pre-Prefill 7.7 Memory Pressure 7.8 Summary 8 Related Work 9 Conclusion References On-device LLM deployment keeps private data local, reduces dependence on network services, and can respond to users when connectivity is unavailable. The runtime sits between a local agent API and a single model instance and is organized into three components that.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat LOCAL: Enabling Learning On-device Contiguously for Agent LLMs as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.15241v1
  - Applies to: `2608.15241-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.15241v1
  - Applies to: `2608.15241-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.15241v1
  - Applies to: `2608.15241-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.15241
  - Applies to: `2608.15241-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Xinxin Liu
  - arXiv author search: https://arxiv.org/search/?query=Xinxin%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2608.15241-whitepaper-review.md`.
- Author: Jiaxin Li
  - arXiv author search: https://arxiv.org/search/?query=Jiaxin%20Li&searchtype=author
  - Applies to: the reviewed paper and `2608.15241-whitepaper-review.md`.
- Author: Zibo Wang
  - arXiv author search: https://arxiv.org/search/?query=Zibo%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2608.15241-whitepaper-review.md`.
- Author: Yun Ji
  - arXiv author search: https://arxiv.org/search/?query=Yun%20Ji&searchtype=author
  - Applies to: the reviewed paper and `2608.15241-whitepaper-review.md`.
- Author: Zhangqi Zhu
  - arXiv author search: https://arxiv.org/search/?query=Zhangqi%20Zhu&searchtype=author
  - Applies to: the reviewed paper and `2608.15241-whitepaper-review.md`.
- Author: Qing Hu
  - arXiv author search: https://arxiv.org/search/?query=Qing%20Hu&searchtype=author
  - Applies to: the reviewed paper and `2608.15241-whitepaper-review.md`.
- Author: Zhibin Wang
  - arXiv author search: https://arxiv.org/search/?query=Zhibin%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2608.15241-whitepaper-review.md`.
- Author: Rong Gu
  - arXiv author search: https://arxiv.org/search/?query=Rong%20Gu&searchtype=author
  - Applies to: the reviewed paper and `2608.15241-whitepaper-review.md`.
- Author: Sheng Zhong
  - arXiv author search: https://arxiv.org/search/?query=Sheng%20Zhong&searchtype=author
  - Applies to: the reviewed paper and `2608.15241-whitepaper-review.md`.
- Author: Chen Tian
  - arXiv author search: https://arxiv.org/search/?query=Chen%20Tian&searchtype=author
  - Applies to: the reviewed paper and `2608.15241-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
