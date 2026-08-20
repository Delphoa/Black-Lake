# DEP-A-20260818-SMEPilot Characterizing O

#artificial-intelligence #arXiv #paper-review #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.16332v1, *SMEPilot: Characterizing and Optimizing LLM Inference with Scalable Matrix Extensions*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.16332-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.16332-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: In particular, it remains unclear how a runtime should schedule matrix extensions and CPU vector cores across inference phases such as prefill and decode, and across operators such as FFN, MoE and attention. To address this problem, we introduce SMEPilot, an accelerated inference engine for CPUs with scalable matrix extensions. 1 Introduction 2.1 LLM Inference 2.2 Scalable Matrix Extension 3.1 SME and CPU Cores: Additive Compute, Shared Bandwidth 3.2 Multi-Ceiling Roofline Model 3.3 Scheduling Insights from the Roofline Analysis 4.1 Tile-level Work Partitioning 4.2 Phase-aware Pipeline Execution 4.3 Layout-aware Runtime 4.4 Execution Plan Generation 5.1 Experimental Setup 5.2 End-to-End Inference 5.3.1 FFN 5.3.2 Prefill Attention 5.3.3 Decode FFN 5.3.4 Decode Attention 5.4 Ablation Study 5.5 Power Consumption 5.6 GPU Inference Comparison 6.1 CPU LLM Inference 6.2 CPU Matrix Extension and SME 7 Discussion and Future Work 8 Conclusion References Modern LLMs are commonly built from Transformer blocks, where each layer alternates between attention and feed-forward network (FFN) computation (Vaswani et al.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat SMEPilot: Characterizing and Optimizing LLM Inference with Scalable Matrix Extensions as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.16332v1
  - Applies to: `2606.16332-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.16332v1
  - Applies to: `2606.16332-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.16332v1
  - Applies to: `2606.16332-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.16332
  - Applies to: `2606.16332-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Feiyang Chen
  - arXiv author search: https://arxiv.org/search/?query=Feiyang%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.16332-whitepaper-review.md`.
- Author: Haibo Chen
  - arXiv author search: https://arxiv.org/search/?query=Haibo%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.16332-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
