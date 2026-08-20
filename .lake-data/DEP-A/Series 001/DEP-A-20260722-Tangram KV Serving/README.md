# DEP-A-20260722-Tangram KV Serving

#artificial-intelligence #KV-cache #LLM-serving #memory-management #continuous-batching #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.06302v2, *Tangram: Unlocking Non-Uniform KV Cache Compression for Efficient Multi-turn LLM Serving*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.06302-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.06302-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Tangram makes non-uniform per-head KV compression compatible with continuous batching. Offline calibrated head budgets eliminate dynamic reclamation, budget-clustered ragged pages group heads with similar retention, and an ahead-of-time workload split map balances CUDA work across SMs.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Maintain budget profiles as versioned calibrations with online coverage tests, automatically widen or invalidate a head budget after violations, and compare realized fragmentation, quality, and tail latency against a dynamic fallback.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.06302v2
  - Applies to: `2606.06302-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.06302v2
  - Applies to: `2606.06302-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.06302v2
  - Applies to: `2606.06302-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.06302
  - Applies to: `2606.06302-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/aiha-lab/TANGRAM
  - Applies to: reproducibility context in `2606.06302-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Hyungmin Kim
  - arXiv author search: https://arxiv.org/search/?query=Hyungmin%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.06302-whitepaper-review.md`.
- Author: Minsoo Kim
  - arXiv author search: https://arxiv.org/search/?query=Minsoo%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.06302-whitepaper-review.md`.
- Author: Hongseok Kim
  - arXiv author search: https://arxiv.org/search/?query=Hongseok%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.06302-whitepaper-review.md`.
- Author: Jungwook Choi
  - arXiv author search: https://arxiv.org/search/?query=Jungwook%20Choi&searchtype=author
  - Applies to: the reviewed paper and `2606.06302-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
