# DEP-A-20260724-Tiara Memory-Side NIC

#artificial-intelligence #RDMA #memory-side-computing #SmartNIC #distributed-systems #hardware-systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.13708v1, *Tiara: A Programmable Line-Rate ISA for Remote Memory Access*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.13708-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.13708-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Tiara defines a compact, pre-registered, statically verifiable instruction set for memory-side NIC operators. Sixteen 64-bit registers and bounded pointer-chasing instructions let an FPGA NIC follow dependent remote-memory indirections locally, collapsing multiple network exchanges without involving the remote CPU.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat registered near-data operators as signed capabilities with instruction hashes, memory-region bounds, tenant budgets, runtime telemetry, and a safe RDMA fallback; test admission under contention as well as microbenchmark speed.

## Associated DEP Records

- [DEP-A-20260714-LCLM Context Compression](../DEP-A-20260714-LCLM%20Context%20Compression/README.md) - direct context-compression method context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.13708v1
  - Applies to: `2606.13708-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.13708v1
  - Applies to: `2606.13708-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.13708v1
  - Applies to: `2606.13708-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.13708
  - Applies to: `2606.13708-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/bojieli/Tiara
  - Applies to: reproducibility context in `2606.13708-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Bojie Li
  - arXiv author search: https://arxiv.org/search/?query=Bojie%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.13708-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
