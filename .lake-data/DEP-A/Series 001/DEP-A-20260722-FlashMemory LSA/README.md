# DEP-A-20260722-FlashMemory LSA

#artificial-intelligence #long-context #sparse-attention #KV-cache #memory-indexing #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.09079v2, *FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.09079-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.09079-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: FlashMemory adds Lookahead Sparse Attention to DeepSeek-V4-Flash. A decoupled neural memory indexer predicts which historical compressed-attention chunks will matter over the next 64 decode steps; a CPU cold pool retains history and selected chunks move to GPU HBM. Training labels use top-p filtering plus cross-layer majority voting.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate lookahead retrieval as a prefetch predictor with calibrated miss probability, reserve a dense-global escape budget for MRCR-like tasks, and record every cold-pool fetch, late miss, and accuracy fallback by context length.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.09079v2
  - Applies to: `2606.09079-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.09079v2
  - Applies to: `2606.09079-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.09079v2
  - Applies to: `2606.09079-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.09079
  - Applies to: `2606.09079-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/libertywing/FlashMemory-Deepseek-V4
  - Applies to: reproducibility context in `2606.09079-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/libertywing/FlashMemory-Deepseek-V4
  - Applies to: reproducibility context in `2606.09079-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Yan Wang
  - arXiv author search: https://arxiv.org/search/?query=Yan%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Qifan Zhang
  - arXiv author search: https://arxiv.org/search/?query=Qifan%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Jiachen Yu
  - arXiv author search: https://arxiv.org/search/?query=Jiachen%20Yu&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Tian Liang
  - arXiv author search: https://arxiv.org/search/?query=Tian%20Liang&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Dongyang Ma
  - arXiv author search: https://arxiv.org/search/?query=Dongyang%20Ma&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Xiang Hu
  - arXiv author search: https://arxiv.org/search/?query=Xiang%20Hu&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Zibo Lin
  - arXiv author search: https://arxiv.org/search/?query=Zibo%20Lin&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Chunyang Li
  - arXiv author search: https://arxiv.org/search/?query=Chunyang%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Zhichao Wang
  - arXiv author search: https://arxiv.org/search/?query=Zhichao%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Miao Peng
  - arXiv author search: https://arxiv.org/search/?query=Miao%20Peng&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Nuo Chen
  - arXiv author search: https://arxiv.org/search/?query=Nuo%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Jia Li
  - arXiv author search: https://arxiv.org/search/?query=Jia%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Yujiu Yang
  - arXiv author search: https://arxiv.org/search/?query=Yujiu%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Haitao Mi
  - arXiv author search: https://arxiv.org/search/?query=Haitao%20Mi&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Author: Dong Yu
  - arXiv author search: https://arxiv.org/search/?query=Dong%20Yu&searchtype=author
  - Applies to: the reviewed paper and `2606.09079-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
