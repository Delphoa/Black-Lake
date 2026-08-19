# DEP-A-20260819-OasisKV Scaling Decode KV

#artificial-intelligence #arXiv #paper-review #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.08097v1, *OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.08097-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.08097-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Sparse attention ( 11 ; 31 ; 37 ) reduces KV reads by attending to only a subset of historical tokens for next-token decoding, but does not reduce the memory capacity required to retain the full KV cache in the HBM. Rather than transferring the full KV cache from prefill nodes to decode nodes, OasisKV allows decode GPUs to remotely access only the KV-cache blocks they need through lookahead-driven sparse prefetching. In summary, this paper makes the following contributions: We design a KV-cache prefetching framework that expands effective in-decode memory capacity using off-GPU memory.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat OasisKV: Scaling In-Decode KV Cache Beyond HBM with Lookahead Sparse Prefetching as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.08097v1
  - Applies to: `2608.08097-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.08097v1
  - Applies to: `2608.08097-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.08097v1
  - Applies to: `2608.08097-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.08097
  - Applies to: `2608.08097-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Can Xiao
  - arXiv author search: https://arxiv.org/search/?query=Can%20Xiao&searchtype=author
  - Applies to: the reviewed paper and `2608.08097-whitepaper-review.md`.
- Author: Sukmin Cho
  - arXiv author search: https://arxiv.org/search/?query=Sukmin%20Cho&searchtype=author
  - Applies to: the reviewed paper and `2608.08097-whitepaper-review.md`.
- Author: Junbong We
  - arXiv author search: https://arxiv.org/search/?query=Junbong%20We&searchtype=author
  - Applies to: the reviewed paper and `2608.08097-whitepaper-review.md`.
- Author: Zhixiong Niu
  - arXiv author search: https://arxiv.org/search/?query=Zhixiong%20Niu&searchtype=author
  - Applies to: the reviewed paper and `2608.08097-whitepaper-review.md`.
- Author: Jianyi Cheng
  - arXiv author search: https://arxiv.org/search/?query=Jianyi%20Cheng&searchtype=author
  - Applies to: the reviewed paper and `2608.08097-whitepaper-review.md`.
- Author: Yiren Zhao
  - arXiv author search: https://arxiv.org/search/?query=Yiren%20Zhao&searchtype=author
  - Applies to: the reviewed paper and `2608.08097-whitepaper-review.md`.
- Author: Youngjin Kwon
  - arXiv author search: https://arxiv.org/search/?query=Youngjin%20Kwon&searchtype=author
  - Applies to: the reviewed paper and `2608.08097-whitepaper-review.md`.
- Author: Yongqiang Xiong
  - arXiv author search: https://arxiv.org/search/?query=Yongqiang%20Xiong&searchtype=author
  - Applies to: the reviewed paper and `2608.08097-whitepaper-review.md`.
- Author: Rui Ma
  - arXiv author search: https://arxiv.org/search/?query=Rui%20Ma&searchtype=author
  - Applies to: the reviewed paper and `2608.08097-whitepaper-review.md`.
- Author: Junyi Liu
  - arXiv author search: https://arxiv.org/search/?query=Junyi%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2608.08097-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
