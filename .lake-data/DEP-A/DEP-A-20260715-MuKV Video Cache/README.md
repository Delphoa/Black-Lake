# DEP-A-20260715-MuKV Video Cache

#video-question-answering #kv-cache #multimodal-llm #streaming-video #retrieval #compression #whitepaper-review

This archival DEP-A preserves a public-safe, whitepaper-grade review of arXiv:2605.22269v1, “MuKV: Multi-Grained KV Cache Compression for Long Streaming Video Question-Answering.” The complete PDF and full-paper HTML were verified from a local research archive. Those source documents, private cache ledgers, coverage matrices, and validator reports remain local and are not deposited here.

## Contents

- `README.md` — classification, inventory, provenance, relationships, and attribution for this DEP-A.
- `2605.22269-whitepaper-review.md` — validated technical reconstruction, quantitative audit, external primary-source vetting, independent re-conceptualization, coverage ledger, and replication agenda.

## Summary of Items

### `2605.22269-whitepaper-review.md`

The review reconstructs MuKV's patch, frame, and segment cache; attention/frequency dual-signal pruning; semi-hierarchical retrieval; online KV reuse; physical storage and latency measurements; backbone/FPS studies; and all granularity, compression, retrieval, and retention ablations.

## Insights and Relevance

MuKV is a typed episodic video cache whose representation scales preserve complementary evidence. The review finds strong storage and question-time results while separating offline parallel time from total three-prefill compute and identifying privacy, cache-versioning, and amortization requirements.

## Associated DEP Records

The [SeKV Resolution DEP](../DEP-A-20260714-SeKV%20Resolution/README.md) is close conceptual work on resolution-adaptive hierarchical semantic KV memory. It is not the same paper: SeKV targets text long-context inference, while MuKV stores multi-scale video KV blocks. The [Context-Intensive KV DEP](../DEP-A-20260715-Context-Intensive%20KV/README.md) is related systems work on retrieving/offloading KV state under evidence-intensive workloads. No same-paper DEP was verified.

## Attribution Block

- Source URL: https://arxiv.org/abs/2605.22269v1
  - Applies to: `2605.22269-whitepaper-review.md`
  - Notes: Canonical arXiv v1 record and complete paper metadata.
- Source URL: https://arxiv.org/pdf/2605.22269v1
  - Applies to: `2605.22269-whitepaper-review.md`
  - Notes: Canonical public PDF locator; the source was verified locally and withheld from the repository.
- Source URL: https://arxiv.org/html/2605.22269v1
  - Applies to: `2605.22269-whitepaper-review.md`
  - Notes: Canonical public full-paper HTML locator; the source was verified locally and withheld from the repository.
- Source URL: https://doi.org/10.48550/arXiv.2605.22269
  - Applies to: `2605.22269-whitepaper-review.md`
  - Notes: Canonical arXiv DOI.
- Source URL: https://github.com/IMBALDY/MuKV
  - Applies to: `2605.22269-whitepaper-review.md`
  - Notes: Official PyTorch implementation and data/setup guidance; availability was verified, but no independent execution is claimed.
- Author: Junbin Xiao
  - arXiv author search: https://arxiv.org/search/?query=Junbin%20Xiao&searchtype=author
  - Applies to: the reviewed paper and `2605.22269-whitepaper-review.md`.
- Author: Jiajun Chen
  - arXiv author search: https://arxiv.org/search/?query=Jiajun%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2605.22269-whitepaper-review.md`.
- Author: Tianxiang Sun
  - arXiv author search: https://arxiv.org/search/?query=Tianxiang%20Sun&searchtype=author
  - Applies to: the reviewed paper and `2605.22269-whitepaper-review.md`.
- Author: Xun Yang
  - arXiv author search: https://arxiv.org/search/?query=Xun%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2605.22269-whitepaper-review.md`.
- Author: Angela Yao
  - arXiv author search: https://arxiv.org/search/?query=Angela%20Yao&searchtype=author
  - Applies to: the reviewed paper and `2605.22269-whitepaper-review.md`.
