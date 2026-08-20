# DEP-A-20260819-Memory Decoder at Scale

#artificial-intelligence #arXiv #paper-review #memory #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.27919v1, *Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.27919-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.27919-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Segment-level recurrence [ 11 ] , bounded KV caches [ 53 ] , retrieval from distant context [ 52 ] , and RoPE rescaling [ 12 ] improve access to contextual information during inference, but do not address the entanglement between long-term memory and reasoning. In particular, Memory Decoder [ 7 ] demonstrates the effectiveness of pretrained parametric memory with models scaling up to 1B parameters, using WikiText-103 and domain-specific corpora containing only millions of tokens. \githublink https://github.com/LUMIA-Group/MemoryDecoder-at-Scale \githubtext LUMIA-Group/MemoryDecoder-at-Scale \huggingfacelink https://huggingface.co/collections/Rubin-Wei/memorydecoder-at-scale \huggingfacetext Rubin-wei/MemoryDecoder-at-Scale \projectpagelink https://rubin-wei.github.io/memory-decoder-at-scale/ \projectpagetext MemoryDecoder-at-Scale \setheadertitle Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory Memory Decoder [ 7 ] is a standalone parametric memory trained to imitate the behavior of a non-parametric retriever.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Memory Decoder at Scale: A Pretrained, Parametric Long-Term Memory as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.27919v1
  - Applies to: `2607.27919-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.27919v1
  - Applies to: `2607.27919-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.27919v1
  - Applies to: `2607.27919-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.27919
  - Applies to: `2607.27919-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/LUMIA-Group/MemoryDecoder-at-Scale
  - Applies to: reproducibility context in `2607.27919-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/collections/Rubin-Wei/memorydecoder-at-scale
  - Applies to: reproducibility context in `2607.27919-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://rubin-wei.github.io/memory-decoder-at-scale/
  - Applies to: reproducibility context in `2607.27919-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Rubin Wei
  - arXiv author search: https://arxiv.org/search/?query=Rubin%20Wei&searchtype=author
  - Applies to: the reviewed paper and `2607.27919-whitepaper-review.md`.
- Author: Jiaqi Cao
  - arXiv author search: https://arxiv.org/search/?query=Jiaqi%20Cao&searchtype=author
  - Applies to: the reviewed paper and `2607.27919-whitepaper-review.md`.
- Author: Jiarui Wang
  - arXiv author search: https://arxiv.org/search/?query=Jiarui%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.27919-whitepaper-review.md`.
- Author: Junming Zhang
  - arXiv author search: https://arxiv.org/search/?query=Junming%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.27919-whitepaper-review.md`.
- Author: Qipeng Guo
  - arXiv author search: https://arxiv.org/search/?query=Qipeng%20Guo&searchtype=author
  - Applies to: the reviewed paper and `2607.27919-whitepaper-review.md`.
- Author: Bowen Zhou
  - arXiv author search: https://arxiv.org/search/?query=Bowen%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2607.27919-whitepaper-review.md`.
- Author: Zhouhan Lin
  - arXiv author search: https://arxiv.org/search/?query=Zhouhan%20Lin&searchtype=author
  - Applies to: the reviewed paper and `2607.27919-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
