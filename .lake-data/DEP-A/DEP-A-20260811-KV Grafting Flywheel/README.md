# DEP-A-20260811-KV Grafting Flywheel

#artificial-intelligence #KV-cache #knowledge-reuse #content-addressing #verification #efficiency

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.14431v1, *Smarter and Cheaper at Once: Byte-Exact KV-Cache Grafting Turns a Frozen Small Model into a Verified-Knowledge Flywheel*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.14431-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.14431-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: A frozen small model can be made smarter (it solves problems it provably could not before) and cheaper (it pays a tiny fraction of the tokens and energy) at the same time, by adding verified knowledge as byte-exact KV state and retrieving it by graft. The contribution, demonstrated end to end and measured, is the verified-knowledge flywheel: solve a problem once, verify it, freeze the verified solution as a byte-exact KV block, keep it forever on disk at zero accelerator memory, route to it, and graft it in place of re-deriving; and, because the block is a plain file, copy it to a fresh server where it grafts byte-identical and functions with no re-solve. A frozen 12B model is made measurably more capable and dramatically cheaper at the same time, using a single mechanism: verified knowledge is deposited once as a byte-exact key-value (KV) state artifact and later restored, by graft, into a fresh inference context.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat byte-exact KV grafts as content-addressed capability caches: bind artifacts to model, weights, tokenizer, runtime, rotary position, hardware class, prompt bytes, and verification hashes, reject any compatibility drift, and recompute from source when integrity or provenance cannot be proved.

## Associated DEP Records

- [DEP-A-20260810-MomentKV](../DEP-A-20260810-MomentKV/README.md) - direct long-context KV-cache eviction and retention context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260727-Programmable KV](../DEP-A-20260727-Programmable%20KV/README.md) - direct programmable KV-state reuse and serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.14431v1
  - Applies to: `2607.14431-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.14431v1
  - Applies to: `2607.14431-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.14431v1
  - Applies to: `2607.14431-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.14431
  - Applies to: `2607.14431-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Sietse Schelpe
  - arXiv author search: https://arxiv.org/search/?query=Sietse%20Schelpe&searchtype=author
  - Applies to: the reviewed paper and `2607.14431-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
