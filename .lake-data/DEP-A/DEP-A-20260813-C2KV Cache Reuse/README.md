# DEP-A-20260813-C2KV Cache Reuse

#artificial-intelligence #KV-cache #cache-reuse #compression #LLM-serving #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.17715v1, *C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.17715-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.17715-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We propose a non-prefix KV cache reuse framework C 2 ​ KV \text{C}^{2}\text{KV} that enables long documents to be compressed, stored, and directly reused at arbitrary positions. To achieve efficient reuse, the C 2 \text{C}^{2} Extractor injects learnable C 2 \text{C}^{2} Tokens as compressed memory slots, whose interactions are governed by a novel Structured Attention Flow . As illustrated in Figure 3 , existing reuse methods reduce prefill cost by loading cached KVs from memory, but still do not address this storage pressure; moreover, naively applying KV compression to reused blocks leads to severe fidelity loss, as standard compressed representations are not designed to be composable or position-agnostic.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate composable KV reuse as a cache-lineage protocol: record source requests, compression transforms, compatibility checks, reused segments, and quality deltas, and invalidate reuse when model, position, or attention-state assumptions drift.

## Associated DEP Records

- [DEP-A-20260809-ScoutAttention Offload](../DEP-A-20260809-ScoutAttention%20Offload/README.md) - direct KV offload, retrieval, and long-context serving context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260810-MomentKV](../DEP-A-20260810-MomentKV/README.md) - direct long-context KV-cache eviction and retention context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.17715v1
  - Applies to: `2607.17715-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.17715v1
  - Applies to: `2607.17715-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.17715v1
  - Applies to: `2607.17715-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.17715
  - Applies to: `2607.17715-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/s7a9/C2KV
  - Applies to: reproducibility context in `2607.17715-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Chuheng Du
  - arXiv author search: https://arxiv.org/search/?query=Chuheng%20Du&searchtype=author
  - Applies to: the reviewed paper and `2607.17715-whitepaper-review.md`.
- Author: Junyi Chen
  - arXiv author search: https://arxiv.org/search/?query=Junyi%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.17715-whitepaper-review.md`.
- Author: Hanlin Tang
  - arXiv author search: https://arxiv.org/search/?query=Hanlin%20Tang&searchtype=author
  - Applies to: the reviewed paper and `2607.17715-whitepaper-review.md`.
- Author: Kan Liu
  - arXiv author search: https://arxiv.org/search/?query=Kan%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.17715-whitepaper-review.md`.
- Author: Tao Lan
  - arXiv author search: https://arxiv.org/search/?query=Tao%20Lan&searchtype=author
  - Applies to: the reviewed paper and `2607.17715-whitepaper-review.md`.
- Author: Lin Qu
  - arXiv author search: https://arxiv.org/search/?query=Lin%20Qu&searchtype=author
  - Applies to: the reviewed paper and `2607.17715-whitepaper-review.md`.
- Author: Chaoyue Niu
  - arXiv author search: https://arxiv.org/search/?query=Chaoyue%20Niu&searchtype=author
  - Applies to: the reviewed paper and `2607.17715-whitepaper-review.md`.
- Author: Shengzhong Liu
  - arXiv author search: https://arxiv.org/search/?query=Shengzhong%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.17715-whitepaper-review.md`.
- Author: Guihai Chen
  - arXiv author search: https://arxiv.org/search/?query=Guihai%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.17715-whitepaper-review.md`.
- Author: Fan Wu
  - arXiv author search: https://arxiv.org/search/?query=Fan%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2607.17715-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
