# DEP-A-20260804-KernelFlume Serving

#artificial-intelligence #LLM-serving #distributed-systems #KV-cache #long-context #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.29207v1, *KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.29207-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.29207-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: 1 Introduction 2.1 Agentic Long-Context Decoding 2.2 Scaling Long-Context Decoding 2.3 Need for Elasticity in Dynamic Decoding 2.4 Limitations of Existing Elastic Scaling 3.1 Kernel-level Disaggregation 3.2 Workflow of Elastic Decoding 4.1 Elastic Communication 4.2 Elastic Scaling Policy 5.1 Query-First Attention 5.2 Kernel Pipelining 6.1 Implementation and Setup Attention-node scaling. KernelFlume answers the first two questions with elastic attention communication (§ 4.1 ), which separates endpoint selection from graph execution, and answers the third with a scaling policy (§ 4.2 ). We evaluate whether KernelFlume can add KV capacity without degrading decode latency, by elastically scaling from one attention node (1A) to seven attention nodes (7A) as each request’s context grows autoregressively (Figure 8 ): when the tail A node’s KV approaches its budget, the controller appends a new weightless A node.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat KernelFlume: Elastic Core-Attention Scaling for Agentic Long-Context Decoding as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260802-AgentServeSim](../DEP-A-20260802-AgentServeSim/README.md) - direct LLM-serving workload and systems-evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.29207v1
  - Applies to: `2606.29207-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.29207v1
  - Applies to: `2606.29207-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.29207v1
  - Applies to: `2606.29207-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.29207
  - Applies to: `2606.29207-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Guangyu Xiang
  - arXiv author search: https://arxiv.org/search/?query=Guangyu%20Xiang&searchtype=author
  - Applies to: the reviewed paper and `2606.29207-whitepaper-review.md`.
- Author: Xueze Kang
  - arXiv author search: https://arxiv.org/search/?query=Xueze%20Kang&searchtype=author
  - Applies to: the reviewed paper and `2606.29207-whitepaper-review.md`.
- Author: Lin Zhang
  - arXiv author search: https://arxiv.org/search/?query=Lin%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.29207-whitepaper-review.md`.
- Author: Wenxiang Lin
  - arXiv author search: https://arxiv.org/search/?query=Wenxiang%20Lin&searchtype=author
  - Applies to: the reviewed paper and `2606.29207-whitepaper-review.md`.
- Author: Shaohuai Shi
  - arXiv author search: https://arxiv.org/search/?query=Shaohuai%20Shi&searchtype=author
  - Applies to: the reviewed paper and `2606.29207-whitepaper-review.md`.
- Author: Yuxin Wang
  - arXiv author search: https://arxiv.org/search/?query=Yuxin%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.29207-whitepaper-review.md`.
- Author: Xiaowen Chu
  - arXiv author search: https://arxiv.org/search/?query=Xiaowen%20Chu&searchtype=author
  - Applies to: the reviewed paper and `2606.29207-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
