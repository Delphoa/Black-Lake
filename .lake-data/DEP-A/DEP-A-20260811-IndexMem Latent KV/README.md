# DEP-A-20260811-IndexMem Latent KV

#artificial-intelligence #long-context #KV-cache #learned-eviction #latent-memory #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.25475v2, *IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.25475-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.25475-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The evicted tokens are then used to update a latent memory online , and the memory readout is added as a residual to compensate the main attention stream for the information lost due to eviction. To address this, we propose a lightweight latent memory module that compresses evicted tokens into a compact, online-updated state and provides residual readouts to compensate for the attention contributions lost through KV eviction. Collectively, our method enables accurate long-context inference under a bounded KV budget, delivering consistent improvements on RULER (4K/16K) across Qwen, Mistral, and Llama models (up to 25 points under aggressive eviction), markedly more stable Needle-in-a-Haystack retrieval, and superior LongBench scores and compression curves compared to existing eviction policies.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat learned eviction plus latent recovery as a loss-controlled retention controller: log each gate score, eviction, latent-state update, residual readout, realized memory budget, and downstream miss, then compare against matched-compute eviction without latent compensation under distribution shift.

## Associated DEP Records

- [DEP-A-20260810-MomentKV](../DEP-A-20260810-MomentKV/README.md) - direct long-context KV-cache eviction and retention context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260810-AB Sparse Attention](../DEP-A-20260810-AB%20Sparse%20Attention/README.md) - direct adaptive sparse-attention and long-context evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.25475v2
  - Applies to: `2605.25475-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.25475v2
  - Applies to: `2605.25475-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.25475v2
  - Applies to: `2605.25475-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.25475
  - Applies to: `2605.25475-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Xintong Yang
  - arXiv author search: https://arxiv.org/search/?query=Xintong%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2605.25475-whitepaper-review.md`.
- Author: Hao Gu
  - arXiv author search: https://arxiv.org/search/?query=Hao%20Gu&searchtype=author
  - Applies to: the reviewed paper and `2605.25475-whitepaper-review.md`.
- Author: Binxing Xu
  - arXiv author search: https://arxiv.org/search/?query=Binxing%20Xu&searchtype=author
  - Applies to: the reviewed paper and `2605.25475-whitepaper-review.md`.
- Author: Lujun Li
  - arXiv author search: https://arxiv.org/search/?query=Lujun%20Li&searchtype=author
  - Applies to: the reviewed paper and `2605.25475-whitepaper-review.md`.
- Author: Bei Liu
  - arXiv author search: https://arxiv.org/search/?query=Bei%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2605.25475-whitepaper-review.md`.
- Author: Jiacheng Liu
  - arXiv author search: https://arxiv.org/search/?query=Jiacheng%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2605.25475-whitepaper-review.md`.
- Author: Qiyuan Zhu
  - arXiv author search: https://arxiv.org/search/?query=Qiyuan%20Zhu&searchtype=author
  - Applies to: the reviewed paper and `2605.25475-whitepaper-review.md`.
- Author: Yike Guo
  - arXiv author search: https://arxiv.org/search/?query=Yike%20Guo&searchtype=author
  - Applies to: the reviewed paper and `2605.25475-whitepaper-review.md`.
- Author: Sirui Han
  - arXiv author search: https://arxiv.org/search/?query=Sirui%20Han&searchtype=author
  - Applies to: the reviewed paper and `2605.25475-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
