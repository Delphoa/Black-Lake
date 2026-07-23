# DEP-A-20260724-MawForge MoE Cache

#artificial-intelligence #mixture-of-experts #memory-management #local-inference #cache #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.09686v1, *MawForge: Memory-Bounded Expert Materialization for Local Mixture-of-Experts Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.09686-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.09686-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: MawForge converts sparse MoE activation into bounded residency by keeping common tensors resident while materializing routed expert payloads from split packs into a fixed-size cache. A static budget check rejects unsafe model/context/cache cells before load, and route-aware telemetry selects an operating point rather than maximizing cache hit rate.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Make expert-cache admission a measured control loop with an explicit memory envelope, per-model pressure telemetry, and pre-load rejection; optimize goodput under pressure rather than hit rate in isolation.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct cache-budget and efficient-attention context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.09686v1
  - Applies to: `2607.09686-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.09686v1
  - Applies to: `2607.09686-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.09686v1
  - Applies to: `2607.09686-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.09686
  - Applies to: `2607.09686-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Craig Opie
  - arXiv author search: https://arxiv.org/search/?query=Craig%20Opie&searchtype=author
  - Applies to: the reviewed paper and `2607.09686-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
