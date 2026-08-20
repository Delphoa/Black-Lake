# DEP-A-20260722-ARC KV Caching

#artificial-intelligence #LLM-serving #KV-cache #cache-eviction #adaptive-systems #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.21238v1, *Recency/Frequency Adaptive KV Caching for Large Language Model Serving*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.21238-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.21238-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The system integrates Adaptive Replacement Cache behavior into vLLM prefix caching, dynamically partitioning capacity between recently and frequently reused KV blocks so one workload cannot flush another as readily as under pure LRU.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Tune recency/frequency allocation against saved compute and tail latency rather than hit count alone, isolate tenants, bound ghost metadata, and publish trace-conditioned decisions with a rollback to LRU when adaptation is unstable.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.21238v1
  - Applies to: `2606.21238-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.21238v1
  - Applies to: `2606.21238-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.21238v1
  - Applies to: `2606.21238-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.21238
  - Applies to: `2606.21238-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- External primary source: https://github.com/Y-aang/vllm-ARC
  - Applies to: reproducibility context in `2606.21238-whitepaper-review.md`.
  - Notes: primary provenance or artifact context; availability does not establish independent reproduction.
- Author: Yang Shen
  - arXiv author search: https://arxiv.org/search/?query=Yang%20Shen&searchtype=author
  - Applies to: the reviewed paper and `2606.21238-whitepaper-review.md`.
- Author: Meghana Madhyastha
  - arXiv author search: https://arxiv.org/search/?query=Meghana%20Madhyastha&searchtype=author
  - Applies to: the reviewed paper and `2606.21238-whitepaper-review.md`.
- Author: Robert Underwood
  - arXiv author search: https://arxiv.org/search/?query=Robert%20Underwood&searchtype=author
  - Applies to: the reviewed paper and `2606.21238-whitepaper-review.md`.
- Author: Bogdan Nicolae
  - arXiv author search: https://arxiv.org/search/?query=Bogdan%20Nicolae&searchtype=author
  - Applies to: the reviewed paper and `2606.21238-whitepaper-review.md`.
- Author: Randal Burns
  - arXiv author search: https://arxiv.org/search/?query=Randal%20Burns&searchtype=author
  - Applies to: the reviewed paper and `2606.21238-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
