# DEP-A-20260719-WiSP Expert Paging

#artificial-intelligence #mixture-of-experts #expert-paging #KV-cache #working-set #low-resource-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.21868v1, *WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.21868-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.21868-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: WiSP treats routed expert weights and the KV cache as competing GPU working sets. A routing-aware LRU expert pager preserves byte-identical outputs, while MV-WSA allocates VRAM between expert capacity and KV admission by equalizing marginal latency benefit per byte, either offline or online.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Estimate expert and KV marginal curves continuously with safe probes, include PCIe queueing and admission discontinuities, and use a constrained controller that changes pool sizes only when predicted gain exceeds migration cost and a stability margin.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.21868v1
  - Applies to: `2606.21868-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.21868v1
  - Applies to: `2606.21868-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.21868v1
  - Applies to: `2606.21868-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.21868
  - Applies to: `2606.21868-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/ggml-org/llama.cpp
  - Applies to: reproducibility context in `2606.21868-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://github.com/kvcache-ai/ktransformers
  - Applies to: reproducibility context in `2606.21868-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Jiamu Zhang
  - arXiv author search: https://arxiv.org/search/?query=Jiamu%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.21868-whitepaper-review.md`.
- Author: Liang Wu
  - arXiv author search: https://arxiv.org/search/?query=Liang%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2606.21868-whitepaper-review.md`.
- Author: Mayank Darbari
  - arXiv author search: https://arxiv.org/search/?query=Mayank%20Darbari&searchtype=author
  - Applies to: the reviewed paper and `2606.21868-whitepaper-review.md`.
- Author: Liangjie Hong
  - arXiv author search: https://arxiv.org/search/?query=Liangjie%20Hong&searchtype=author
  - Applies to: the reviewed paper and `2606.21868-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
