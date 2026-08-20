# DEP-A-20260727-Portable Agent Memory

#artificial-intelligence #agent-memory #interoperability #cryptographic-provenance #prompt-injection #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.11032v1, *Portable Agent Memory: A Protocol for Cryptographically-Verified Memory Transfer Across Heterogeneous AI Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.11032-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.11032-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Portable Agent Memory defines a five-component artifact containing entries, state, provenance, working context, and identity preferences. Content-addressed entries form a Merkle-DAG, capability tokens constrain selective disclosure, and a rehydration protocol frames recalled content as data before adapting it to a target model; JSON is the primary transport with optional CBOR compaction.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Add a transfer receipt that binds source artifact hash, disclosed capability scope, target adapter, rehydration prompt, target model version, and post-transfer probes. The protocol is falsified if a content-equivalent baseline achieves the same continuity after matching prompt budget, or if adversarial memories cross the framing boundary in held-out attacks.

## Associated DEP Records

- [DEP-A-20260724-Governed Agent Memory](../DEP-A-20260724-Governed%20Agent%20Memory/README.md) - direct governed persistent-memory and data-foundation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.11032v1
  - Applies to: `2605.11032-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.11032v1
  - Applies to: `2605.11032-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.11032v1
  - Applies to: `2605.11032-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.11032
  - Applies to: `2605.11032-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/nunchi-ai/amcp
  - Applies to: reproducibility context in `2605.11032-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Santhosh Kumar Ravindran
  - arXiv author search: https://arxiv.org/search/?query=Santhosh%20Kumar%20Ravindran&searchtype=author
  - Applies to: the reviewed paper and `2605.11032-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
