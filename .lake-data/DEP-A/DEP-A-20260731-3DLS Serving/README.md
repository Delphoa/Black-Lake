# DEP-A-20260731-3DLS Serving

#artificial-intelligence #LLM-serving #disaggregated-systems #3D-integration #scheduling #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.01617v1, *3DLS: A 3D Logic-Stacked Architecture for Disaggregated LLM Serving*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.01617-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.01617-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: 1 shows that when PD-disaggregated serving with TP is mapped onto a conventional 2D/2.5D chiplet architecture [ 5 ] , KV-cache transfer and decode-side TP collectives are forced to share the same lateral die-to-die (D2D) interconnect. To address this limitation, we propose 3DLS, a logic-on-logic 3D-stacked chiplet architecture for PD-disaggregated LLM serving with TP. We propose 3DLS, a logic-on-logic 3D-stacked chiplet architecture that separates traffic classes by routing KV-cache transfers through vertical interconnects while preserving decode-side TP collectives on the lateral D2D fabric.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate disaggregated 3D serving as a measured service graph: version geometry, appearance, and network state separately; route work from live tail-latency evidence; and retain a monolithic safe mode when placement or transfer estimates become stale.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct KV-cache, real-time interaction, and serving-systems context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.01617v1
  - Applies to: `2607.01617-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.01617v1
  - Applies to: `2607.01617-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.01617v1
  - Applies to: `2607.01617-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.01617
  - Applies to: `2607.01617-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Jaehun Lee
  - arXiv author search: https://arxiv.org/search/?query=Jaehun%20Lee&searchtype=author
  - Applies to: the reviewed paper and `2607.01617-whitepaper-review.md`.
- Author: In-Jun Jung
  - arXiv author search: https://arxiv.org/search/?query=In-Jun%20Jung&searchtype=author
  - Applies to: the reviewed paper and `2607.01617-whitepaper-review.md`.
- Author: Joo-Young Kim
  - arXiv author search: https://arxiv.org/search/?query=Joo-Young%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2607.01617-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
