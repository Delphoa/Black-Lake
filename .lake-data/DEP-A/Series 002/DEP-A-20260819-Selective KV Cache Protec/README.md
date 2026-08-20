# DEP-A-20260819-Selective KV Cache Protec

#artificial-intelligence #arXiv #paper-review #memory #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.29076v1, *Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.29076-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.29076-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Analog compute-in-memory (CIM) arrays have emerged as a compelling hardware substrate to address this challenge, offering orders-of-magnitude improvements in energy efficiency by performing matrix-vector multiplications (MVMs) directly within memory (Verma et al. We propose an algorithm that selectively computes the most noise-sensitive tokens, including initial sink tokens and the sliding recent-token window, on a higher-precision digital path while retaining the bulk KV cache on analog CIM. These approaches mainly optimize software memory usage and do not address the implications of executing KV-cache attention on analog hardware.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260812-KVBuffer Serving](../DEP-A-20260812-KVBuffer%20Serving/README.md) - direct decode-time KV-cache serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.29076v1
  - Applies to: `2607.29076-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.29076v1
  - Applies to: `2607.29076-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.29076v1
  - Applies to: `2607.29076-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.29076
  - Applies to: `2607.29076-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yuannuo Feng
  - arXiv author search: https://arxiv.org/search/?query=Yuannuo%20Feng&searchtype=author
  - Applies to: the reviewed paper and `2607.29076-whitepaper-review.md`.
- Author: Wenyong Zhou
  - arXiv author search: https://arxiv.org/search/?query=Wenyong%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2607.29076-whitepaper-review.md`.
- Author: Yuang Ma
  - arXiv author search: https://arxiv.org/search/?query=Yuang%20Ma&searchtype=author
  - Applies to: the reviewed paper and `2607.29076-whitepaper-review.md`.
- Author: Yizhe Chen
  - arXiv author search: https://arxiv.org/search/?query=Yizhe%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.29076-whitepaper-review.md`.
- Author: Wenshuai Yao
  - arXiv author search: https://arxiv.org/search/?query=Wenshuai%20Yao&searchtype=author
  - Applies to: the reviewed paper and `2607.29076-whitepaper-review.md`.
- Author: Yuxin Xie
  - arXiv author search: https://arxiv.org/search/?query=Yuxin%20Xie&searchtype=author
  - Applies to: the reviewed paper and `2607.29076-whitepaper-review.md`.
- Author: Ngai Wong
  - arXiv author search: https://arxiv.org/search/?query=Ngai%20Wong&searchtype=author
  - Applies to: the reviewed paper and `2607.29076-whitepaper-review.md`.
- Author: Wang Kang
  - arXiv author search: https://arxiv.org/search/?query=Wang%20Kang&searchtype=author
  - Applies to: the reviewed paper and `2607.29076-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
