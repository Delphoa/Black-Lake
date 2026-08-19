# DEP-A-20260819-LinearKV One Cached State

#artificial-intelligence #arXiv #paper-review #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.11231v1, *LinearKV: One Cached State Suffices for Position-Independent Caching in Hybrid LLMs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.11231-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.11231-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We propose LinearKV, a training-free PIC framework for hybrid LLMs such as Granite, OLMo, and Qwen. Moreover, LinearKV shows that one cached state suffices as the linear-layer initializer: keeping just a single matched chunk’s cached linear state is remarkably robust across architectures (C2). In summary, this paper makes three contributions: We formalize position-independent caching for hybrid LLMs as a decoupled-initialization framework, identifying linear-state initialization —mapping the K K cached states to one initial state—as the single hybrid-specific operation, within which existing full-attention PIC selectors are reused unchanged.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat LinearKV: One Cached State Suffices for Position-Independent Caching in Hybrid LLMs as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.11231v1
  - Applies to: `2608.11231-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.11231v1
  - Applies to: `2608.11231-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.11231v1
  - Applies to: `2608.11231-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.11231
  - Applies to: `2608.11231-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Yirui Liu
  - arXiv author search: https://arxiv.org/search/?query=Yirui%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2608.11231-whitepaper-review.md`.
- Author: Ruoling Qi
  - arXiv author search: https://arxiv.org/search/?query=Ruoling%20Qi&searchtype=author
  - Applies to: the reviewed paper and `2608.11231-whitepaper-review.md`.
- Author: Longwen Wang
  - arXiv author search: https://arxiv.org/search/?query=Longwen%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2608.11231-whitepaper-review.md`.
- Author: Xuaner Wu
  - arXiv author search: https://arxiv.org/search/?query=Xuaner%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2608.11231-whitepaper-review.md`.
- Author: Jian Chen
  - arXiv author search: https://arxiv.org/search/?query=Jian%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2608.11231-whitepaper-review.md`.
- Author: Yuxin Jin
  - arXiv author search: https://arxiv.org/search/?query=Yuxin%20Jin&searchtype=author
  - Applies to: the reviewed paper and `2608.11231-whitepaper-review.md`.
- Author: Jiawei Shao
  - arXiv author search: https://arxiv.org/search/?query=Jiawei%20Shao&searchtype=author
  - Applies to: the reviewed paper and `2608.11231-whitepaper-review.md`.
- Author: Xuelong Li
  - arXiv author search: https://arxiv.org/search/?query=Xuelong%20Li&searchtype=author
  - Applies to: the reviewed paper and `2608.11231-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
