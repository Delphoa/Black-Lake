# DEP-A-20260725-Stellar Disk Retrieval

#artificial-intelligence #multimodal-retrieval #documents #late-interaction #storage-systems #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.19960v1, *Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.19960-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.19960-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Stellar fine-tunes a multimodal model to emit sparse lexical document representations for candidate filtering, then performs token-level late interaction only on those candidates. Document embeddings stay on disk in a balanced-cluster layout and a cost model chooses efficient reads and score fusion.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate lexical filtering as a recall-constrained admission stage with per-query coverage estimates, disk-read telemetry, and a broader fallback when the sparse and late-interaction scores disagree.

## Associated DEP Records

- [DEP-A-20260715-FAIR GraphRAG A Retrieval](../DEP-A-20260715-FAIR%20GraphRAG%20A%20Retrieval/README.md) - direct governed retrieval and evidence-graph context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.19960v1
  - Applies to: `2606.19960-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.19960v1
  - Applies to: `2606.19960-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.19960v1
  - Applies to: `2606.19960-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.19960
  - Applies to: `2606.19960-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/ZJU-DAILY/Stellar
  - Applies to: reproducibility context in `2606.19960-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Yuxiang Guo
  - arXiv author search: https://arxiv.org/search/?query=Yuxiang%20Guo&searchtype=author
  - Applies to: the reviewed paper and `2606.19960-whitepaper-review.md`.
- Author: Zhonghao Hu
  - arXiv author search: https://arxiv.org/search/?query=Zhonghao%20Hu&searchtype=author
  - Applies to: the reviewed paper and `2606.19960-whitepaper-review.md`.
- Author: Yuren Mao
  - arXiv author search: https://arxiv.org/search/?query=Yuren%20Mao&searchtype=author
  - Applies to: the reviewed paper and `2606.19960-whitepaper-review.md`.
- Author: Yuhang Liu
  - arXiv author search: https://arxiv.org/search/?query=Yuhang%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2606.19960-whitepaper-review.md`.
- Author: Congcong Ge
  - arXiv author search: https://arxiv.org/search/?query=Congcong%20Ge&searchtype=author
  - Applies to: the reviewed paper and `2606.19960-whitepaper-review.md`.
- Author: Xiaolu Zhang
  - arXiv author search: https://arxiv.org/search/?query=Xiaolu%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.19960-whitepaper-review.md`.
- Author: Jun Zhou
  - arXiv author search: https://arxiv.org/search/?query=Jun%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2606.19960-whitepaper-review.md`.
- Author: Yunjun Gao
  - arXiv author search: https://arxiv.org/search/?query=Yunjun%20Gao&searchtype=author
  - Applies to: the reviewed paper and `2606.19960-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
