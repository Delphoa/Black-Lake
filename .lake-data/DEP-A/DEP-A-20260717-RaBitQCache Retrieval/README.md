# DEP-A-20260717-RaBitQCache Retrieval

#artificial-intelligence #machine-learning #long-context #sparse-attention #kv-cache #quantization

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.31519v1, *RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.31519-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.31519-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: RaBitQCache randomly rotates cached keys, binarizes them for a fast attention proxy, combines binary and INT4 arithmetic, and uses adaptive Top-p retrieval instead of a fixed Top-k budget. Asynchronous pipelining and lazy updates are systems components intended to hide proxy maintenance.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: A stronger system would expose a calibrated probability that excluded tokens contain material attention mass and would fall back to exact attention when that probability breaches a service threshold.

## Associated DEP Records

- [DEP-A-20260716-KV Memory Hierarchy](../DEP-A-20260716-KV%20Memory%20Hierarchy/README.md) - direct method context: reviewed survey of KV-cache representation, movement, reuse, and memory hierarchy. This is method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.31519v1
  - Applies to: `2606.31519-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.31519v1
  - Applies to: `2606.31519-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.31519v1
  - Applies to: `2606.31519-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.31519
  - Applies to: `2606.31519-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/Sakuraaa0/RaBitQCache
  - Applies to: reproducibility context in `2606.31519-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Wenhao Li
  - arXiv author search: https://arxiv.org/search/?query=Wenhao%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.31519-whitepaper-review.md`.
- Author: Jinhao Dong
  - arXiv author search: https://arxiv.org/search/?query=Jinhao%20Dong&searchtype=author
  - Applies to: the reviewed paper and `2606.31519-whitepaper-review.md`.
- Author: Hailin Zhang
  - arXiv author search: https://arxiv.org/search/?query=Hailin%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.31519-whitepaper-review.md`.
- Author: Wenhang Shi
  - arXiv author search: https://arxiv.org/search/?query=Wenhang%20Shi&searchtype=author
  - Applies to: the reviewed paper and `2606.31519-whitepaper-review.md`.
- Author: Wei Lu
  - arXiv author search: https://arxiv.org/search/?query=Wei%20Lu&searchtype=author
  - Applies to: the reviewed paper and `2606.31519-whitepaper-review.md`.
- Author: Xiaoyong Du
  - arXiv author search: https://arxiv.org/search/?query=Xiaoyong%20Du&searchtype=author
  - Applies to: the reviewed paper and `2606.31519-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
