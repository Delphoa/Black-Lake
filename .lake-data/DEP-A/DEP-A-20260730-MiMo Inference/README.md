# DEP-A-20260730-MiMo Inference

#artificial-intelligence #LLM-serving #sliding-window-attention #KV-cache #distributed-systems #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.13095v1, *Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.13095-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.13095-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: This article presents an end-to-end engineering practice for the inference system of the MiMo-V2.5 series, covering KVCache management, tiered caching systems, SWA-aware prefix cache trees, scheduling strategies, Prefill/Decode execution pipelines, and multimodal optimizations — systematically realizing the architecture’s theoretical efficiency potential (especially Hybrid SWA) in production. 3.2.1 Architecture Design 3.2.2 Network Optimization 3.2.3 Storage Cost Optimization 3.2.4 Reliability Assurance 3.3 Discussion on Cache Hit Rate 4.1 KVCache and Load-Affinity Scheduling 4.2 TTFT Optimization 5.1 Parallelism Configuration 5.2 Length Bucketing Strategy 5.3 MoE Load Balancing 5.4 Resolving NUMA Conflicts 6.1 GPU Memory Optimization 6.2 MTP Optimization 7.1 Architecture Optimization 7.2 Preprocessing Optimization 7.3 Cache Optimization 8 Afterword References A Contributions and Acknowledgments The MiMo-V2 and MiMo-V2.5 series were among the earliest models to adopt the Hybrid SWA architecture, but at the time, neither mainstream open-source inference frameworks nor caching systems offered complete SWA support. Looking back, the inference efficiency of the MiMo-V2.5 series did not come from a single breakthrough, but from.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Optimize hybrid sliding-window inference as an end-to-end service graph: record attention mode, cache placement, communication, kernel choice, and tail latency under one request identity.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct KV-cache and long-context systems context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.13095v1
  - Applies to: `2607.13095-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.13095v1
  - Applies to: `2607.13095-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.13095v1
  - Applies to: `2607.13095-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.13095
  - Applies to: `2607.13095-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Xiaomi MiMo Team
  - arXiv author search: https://arxiv.org/search/?query=Xiaomi%20MiMo%20Team&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Anqi Liu
  - arXiv author search: https://arxiv.org/search/?query=Anqi%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Aoxin Ma
  - arXiv author search: https://arxiv.org/search/?query=Aoxin%20Ma&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Bo Chen
  - arXiv author search: https://arxiv.org/search/?query=Bo%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Bo Yang
  - arXiv author search: https://arxiv.org/search/?query=Bo%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Chen Wang
  - arXiv author search: https://arxiv.org/search/?query=Chen%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Chen Zhang
  - arXiv author search: https://arxiv.org/search/?query=Chen%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Chengda Tang
  - arXiv author search: https://arxiv.org/search/?query=Chengda%20Tang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Chengwei Wang
  - arXiv author search: https://arxiv.org/search/?query=Chengwei%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Chiheng Lou
  - arXiv author search: https://arxiv.org/search/?query=Chiheng%20Lou&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Depeng Yan
  - arXiv author search: https://arxiv.org/search/?query=Depeng%20Yan&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Fuli Luo
  - arXiv author search: https://arxiv.org/search/?query=Fuli%20Luo&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Gang Wang
  - arXiv author search: https://arxiv.org/search/?query=Gang%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Hailin Zhang
  - arXiv author search: https://arxiv.org/search/?query=Hailin%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Jiale Sun
  - arXiv author search: https://arxiv.org/search/?query=Jiale%20Sun&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Kang Zhou
  - arXiv author search: https://arxiv.org/search/?query=Kang%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Rui Huang
  - arXiv author search: https://arxiv.org/search/?query=Rui%20Huang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Shaohui Liu
  - arXiv author search: https://arxiv.org/search/?query=Shaohui%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Shen Huang
  - arXiv author search: https://arxiv.org/search/?query=Shen%20Huang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Shijie Cao
  - arXiv author search: https://arxiv.org/search/?query=Shijie%20Cao&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Shuaishuai Fan
  - arXiv author search: https://arxiv.org/search/?query=Shuaishuai%20Fan&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Tianling Zhou
  - arXiv author search: https://arxiv.org/search/?query=Tianling%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Xiangwei Deng
  - arXiv author search: https://arxiv.org/search/?query=Xiangwei%20Deng&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Xueyang Xie
  - arXiv author search: https://arxiv.org/search/?query=Xueyang%20Xie&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Xuli Wang
  - arXiv author search: https://arxiv.org/search/?query=Xuli%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Yingchun Lai
  - arXiv author search: https://arxiv.org/search/?query=Yingchun%20Lai&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Yu Yang
  - arXiv author search: https://arxiv.org/search/?query=Yu%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Yuan Zhang
  - arXiv author search: https://arxiv.org/search/?query=Yuan%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Zhen Tang
  - arXiv author search: https://arxiv.org/search/?query=Zhen%20Tang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Zhonghua Deng
  - arXiv author search: https://arxiv.org/search/?query=Zhonghua%20Deng&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Author: Zihan Jiang
  - arXiv author search: https://arxiv.org/search/?query=Zihan%20Jiang&searchtype=author
  - Applies to: the reviewed paper and `2607.13095-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
