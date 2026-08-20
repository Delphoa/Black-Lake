# DEP-A-20260714-SeKV Resolution

#arxiv #kv-cache #hierarchical-memory #low-rank-approximation #cpu-offload #semantic-routing #long-context #language-model-inference #machine-learning

This DEP-A entry preserves a public-safe, whitepaper-grade full-paper review of **“SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference,” arXiv:2606.31145v1**. It covers anchors, summaries, coarse attention, CPU factors, routing, mixed-resolution attention, training, experiments, tables, and figures. Complete source documents were verified locally and withheld.

Deposition date: 2026-07-14
Stable paper version: arXiv:2606.31145v1

## Contents

- `README.md` — deposition context, complete inventory, relationships, and attribution.
- `2606.31145-whitepaper-review.md` — validated public-safe full-paper review and independent re-conceptualization.

## Summary of Items

### `README.md`

Defines the stable record, inventories both files, connects verified related records, and supplies attribution.

### `2606.31145-whitepaper-review.md`

Reconstructs the complete memory hierarchy, losses, exact results, ablations, complexity, host-resource omissions, implementation, and replication agenda. The canonical review passed validation at 4,517 words with a 19/20 methodology score.

## Insights and Relevance

SeKV separates routing from answering representation: every span remains cheaply visible, while selected spans regain approximate detail. The review finds the hierarchy is lossy, short-span factor storage can exceed raw KV, and host transfer, reconstruction, reuse, batching, and tail latency remain undermeasured. The public repository helps, but its small history and a configuration mismatch require commit-pinned reproduction.

## Associated DEP Records

- [Delphoa-Labs/Black-Lake-Data DEP-20260702-Tech Intel 0103](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260702-Tech%20Intel%200103) — verified same-paper raw research context. This DEP-A is the owning whitepaper review.
- [`DEP-A-20260714-CompressKV Semantic Heads`](../DEP-A-20260714-CompressKV%20Semantic%20Heads/README.md) — close conceptual semantic KV compression; not the same paper.

No additional same-paper DEP-A or DEP-E was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.31145
- Canonical PDF: https://arxiv.org/pdf/2606.31145
- Canonical full-paper HTML: https://arxiv.org/html/2606.31145
- DOI: https://doi.org/10.48550/arXiv.2606.31145
- Official code: https://github.com/AmirAbaskohi/SeKV
- Authors from the canonical arXiv record:
  - Amirhossein Abaskohi — https://arxiv.org/search/cs?query=Abaskohi%2C+A&searchtype=author
  - Giuseppe Carenini — https://arxiv.org/search/cs?query=Carenini%2C+G&searchtype=author
  - Peter West — https://arxiv.org/search/cs?query=West%2C+P&searchtype=author
  - Yuhang He — https://arxiv.org/search/cs?query=He%2C+Y&searchtype=author
- Applies to: `README.md` and `2606.31145-whitepaper-review.md`.
- Verification note: complete source documents were verified locally and withheld from this repository.
