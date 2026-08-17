# DEP-A-20260818-BiSCo LLM Lookup Free

#artificial-intelligence #arXiv #paper-review #model-compression #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.08643v1, *BiSCo-LLM: Lookup-Free Binary Spherical Coding for Extreme Low-Bit Large Language Model Compression*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.08643-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.08643-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Recent sub-2-bit and 2–3-bit studies support this view: Squeeze10-LLM relies on staged mixed precision and activation-level supervision rather than uniform scalar reconstruction, while ICQuant explicitly models outlier statistics to reduce range expansion and bit overhead in extreme compression regimes [ 81 , 33 ] . Describe the issue below: Abstract I Introduction II-A Low-Bit Quantization of Large Language Models II-B Vector-Quantized and Structured-Code Weight Compression II-C Codebook-Free Discrete Representation Learning II-D Outliers, Saliency, and Low-Rank Compensation III-A Problem Formulation and Bit Accounting III-B Pipeline Overview III-C Unit-Sphere Binary Weight Mapping III-D Second-Stage Residual BSQ Compression III-E Auxiliary 8-Bit Sensitive-Channel Path III-F Category-Wise Recovery Distillation Category-batched codec optimization. Although these methods target pruning rather than dense low-bit coding, they provide an important lesson for extreme compression: channels or structures should not be treated uniformly, and calibration activations or gradients can provide useful proxies for preserving model function.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat BiSCo-LLM: Lookup-Free Binary Spherical Coding for Extreme Low-Bit Large Language Model Compression as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.08643v1
  - Applies to: `2607.08643-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.08643v1
  - Applies to: `2607.08643-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.08643v1
  - Applies to: `2607.08643-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.08643
  - Applies to: `2607.08643-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yuantian Shao
  - arXiv author search: https://arxiv.org/search/?query=Yuantian%20Shao&searchtype=author
  - Applies to: the reviewed paper and `2607.08643-whitepaper-review.md`.
- Author: Peisong Wang
  - arXiv author search: https://arxiv.org/search/?query=Peisong%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.08643-whitepaper-review.md`.
- Author: Zhilei Liu
  - arXiv author search: https://arxiv.org/search/?query=Zhilei%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.08643-whitepaper-review.md`.
- Author: Chuangyi Li
  - arXiv author search: https://arxiv.org/search/?query=Chuangyi%20Li&searchtype=author
  - Applies to: the reviewed paper and `2607.08643-whitepaper-review.md`.
- Author: Yuanteng Chen
  - arXiv author search: https://arxiv.org/search/?query=Yuanteng%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.08643-whitepaper-review.md`.
- Author: Pengcheng Xie
  - arXiv author search: https://arxiv.org/search/?query=Pengcheng%20Xie&searchtype=author
  - Applies to: the reviewed paper and `2607.08643-whitepaper-review.md`.
- Author: Yiwu Yao
  - arXiv author search: https://arxiv.org/search/?query=Yiwu%20Yao&searchtype=author
  - Applies to: the reviewed paper and `2607.08643-whitepaper-review.md`.
- Author: Zhihui Wei
  - arXiv author search: https://arxiv.org/search/?query=Zhihui%20Wei&searchtype=author
  - Applies to: the reviewed paper and `2607.08643-whitepaper-review.md`.
- Author: Jian Cheng
  - arXiv author search: https://arxiv.org/search/?query=Jian%20Cheng&searchtype=author
  - Applies to: the reviewed paper and `2607.08643-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
