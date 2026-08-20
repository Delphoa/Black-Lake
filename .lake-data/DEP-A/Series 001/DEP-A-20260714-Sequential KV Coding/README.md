# DEP-A-20260714-Sequential KV Coding

#arxiv #kv-cache #source-coding #entropy #probabilistic-tries #quantization #long-context #language-model-inference #machine-learning

This DEP-A entry preserves a public-safe, whitepaper-grade full-paper review of **“Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit,” arXiv:2604.15356v1**. The review reconstructs the conditional-entropy argument, probabilistic-language-trie layer, predictive residual layer, rate–distortion claims, arithmetic, asymptotics, limitations, external primary-source checks, and an independent re-conceptualization. A complete PDF and full-paper HTML were verified from a local archive; source documents remain local and are withheld from this repository.

Deposition date: 2026-07-14  
Stable paper version: arXiv:2604.15356v1

## Contents

- `README.md` — deposition context, complete inventory, relationships, and attribution.
- `2604.15356-whitepaper-review.md` — validated public-safe full-paper review and independent re-conceptualization.

## Summary of Items

### `README.md`

Defines the stable record, inventories both files, explains the source-coding relevance, links verified conceptual work, and records complete public provenance.

### `2604.15356-whitepaper-review.md`

Audits the entropy theorem against cache access semantics, corrects the stated 70B memory arithmetic, analyzes PLT direction inconsistencies and candidate-prediction cost, records the absence of experiments, and proposes a time–space–distortion replication program. The validator passed the canonical review at 5,150 words.

## Insights and Relevance

The paper correctly distinguishes independent vector coding from sequential coding with side information. Its entropy result does not yet yield a useful cache codec: token IDs already provide the low-rate symbolic description if full model recomputation is free. Practical value requires measured storage, reconstruction compute, random-access latency, and attention distortion under one decoder contract.

## Associated DEP Records

- [DEP-A-20260714-CompressKV Semantic Heads](../DEP-A-20260714-CompressKV%20Semantic%20Heads/README.md) — close conceptual alternative using semantic retrieval signals to retain KV heads. It is not the same paper and does not validate sequential coding.

No same-paper DEP-A, DEP-E, or relevant Delphoa-Labs/Black-Lake-Data record was verified after checking class indexes, DEP READMEs, logs, reports, arXiv ID, DOI, normalized title, method, and implementation.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2604.15356
- Canonical PDF: https://arxiv.org/pdf/2604.15356
- Canonical full-paper HTML: https://arxiv.org/html/2604.15356
- DOI: https://doi.org/10.48550/arXiv.2604.15356
- TurboQuant sources: https://arxiv.org/abs/2504.19874 and https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/
- Exact prefix-caching design: https://docs.vllm.ai/en/v0.7.2/design/v1/prefix_caching.html
- PLT predecessor: https://arxiv.org/abs/2604.06228
- Author from the canonical arXiv record:
  - Gregory Magarshak — https://arxiv.org/search/cs?query=Magarshak%2C+G&searchtype=author
- Applies to: `README.md` and `2604.15356-whitepaper-review.md`.
- Verification note: complete source documents were verified locally and withheld from this repository.
