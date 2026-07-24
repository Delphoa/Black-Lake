# DEP-A-20260722-SparDA KV Prefetch

#artificial-intelligence #sparse-attention #KV-cache #prefetching #long-context #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.04511v1, *SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.04511-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.04511-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: SparDA adds a Forecast projection beside Q, K, and V. The previous layer's forecast selects blocks for the current layer, exposing CPU-to-GPU KV prefetch one layer early and replacing query-head selection with one compact forecast head per GQA group. Only forecast weights are trained; the sparse backbone remains frozen.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Make forecast confidence a first-class runtime signal: prefetch high-confidence blocks, retain a bounded miss cache, and measure hidden-transfer overlap and late fetches so the scheduler can fall back by layer or workload.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.04511v1
  - Applies to: `2606.04511-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.04511v1
  - Applies to: `2606.04511-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.04511v1
  - Applies to: `2606.04511-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.04511
  - Applies to: `2606.04511-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/NVlabs/SparDA
  - Applies to: reproducibility context in `2606.04511-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Yaosheng Fu
  - arXiv author search: https://arxiv.org/search/?query=Yaosheng%20Fu&searchtype=author
  - Applies to: the reviewed paper and `2606.04511-whitepaper-review.md`.
- Author: Guangxuan Xiao
  - arXiv author search: https://arxiv.org/search/?query=Guangxuan%20Xiao&searchtype=author
  - Applies to: the reviewed paper and `2606.04511-whitepaper-review.md`.
- Author: Xin Dong
  - arXiv author search: https://arxiv.org/search/?query=Xin%20Dong&searchtype=author
  - Applies to: the reviewed paper and `2606.04511-whitepaper-review.md`.
- Author: Song Han
  - arXiv author search: https://arxiv.org/search/?query=Song%20Han&searchtype=author
  - Applies to: the reviewed paper and `2606.04511-whitepaper-review.md`.
- Author: Oreste Villa
  - arXiv author search: https://arxiv.org/search/?query=Oreste%20Villa&searchtype=author
  - Applies to: the reviewed paper and `2606.04511-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
