# DEP-A-20260717-Origin Bound Memory

#artificial-intelligence #agent-memory #security #provenance #authorization #multi-agent-systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.24322v1, *Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.24322-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.24322-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: TMA-NM binds a memory item's authority to its write-time origin, propagates that authority non-malleably through later summaries or tool echoes, and permits elevation only through independent trusted corroboration or fresh user authorization. An act-time gate mediates consequential actions while an append-only verdict log preserves decision evidence.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat every memory-derived action as an origin-bound capability whose authority can only stay constant or decrease under transformation; require diversity-aware elevation evidence and retain the act-gate receipt for audit.

## Associated DEP Records

- [DEP-A-20260715-MemDelta Controlled Basel](../DEP-A-20260715-MemDelta%20Controlled%20Basel/README.md) - direct evaluation context: controlled baselines and hidden confounds in agent-memory assessment. This is method context, not a same-paper duplicate.
- [DEP-A-20260717-Latent Cache Integrity](../DEP-A-20260717-Latent%20Cache%20Integrity/README.md) - direct integrity context: provenance, authentication, and adversarial protection for retained model state. This is method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.24322v1
  - Applies to: `2606.24322-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.24322v1
  - Applies to: `2606.24322-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.24322v1
  - Applies to: `2606.24322-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.24322
  - Applies to: `2606.24322-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/yedidel/mem-inv-bench
  - Applies to: reproducibility context in `2606.24322-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/datasets/anonymos-2321135/MEM-INV-Bench
  - Applies to: reproducibility context in `2606.24322-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Yedidel Louck
  - arXiv author search: https://arxiv.org/search/?query=Yedidel%20Louck&searchtype=author
  - Applies to: the reviewed paper and `2606.24322-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
