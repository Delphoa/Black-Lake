# DEP-A-20260731-MiniPIC Cache

#artificial-intelligence #LLM-serving #KV-cache #prefix-caching #position-independence #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.13126v1, *MiniPIC: Flexible Position-Independent Caching in <100LOC*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.13126-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.13126-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The previously mentioned production systems (vLLM and SGLang) partition the KV cache into fixed-size blocks managed via paged attention [ 9 ] , with prefix caching assigning to each block a hash chained through the preceding block [ 29 ] . Achieving flexible PIC inside a production inference server thus requires an implementation that simultaneously (a) removes positional conflicts from the shared KV cache, (b) gives users control over the effective attention mask, and (c) keeps the engine changes small enough to be maintainable and aligned with the existing architecture: it should not introduce new scheduler request types, new memory management subsystems, or external caching services. MiniPIC leaves K unrotated in memory and extends the kernel: The added work is a cos / sin \cos/\sin table lookup and two fused multiply-adds per K element, a small linear term within the O ​ ( n 2 ) O(n^{2}) attention computation.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat position-independent cache reuse as a typed deployment contract: bind cached state to model, tokenizer, adapter, kernel, and prompt-prefix identities, then require compatibility checks, integrity receipts, and a full-prefill fallback before reuse.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct KV-cache, real-time interaction, and serving-systems context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.13126v1
  - Applies to: `2606.13126-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.13126v1
  - Applies to: `2606.13126-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.13126v1
  - Applies to: `2606.13126-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.13126
  - Applies to: `2606.13126-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Nathan Ordonez
  - arXiv author search: https://arxiv.org/search/?query=Nathan%20Ordonez&searchtype=author
  - Applies to: the reviewed paper and `2606.13126-whitepaper-review.md`.
- Author: Thomas Parnell
  - arXiv author search: https://arxiv.org/search/?query=Thomas%20Parnell&searchtype=author
  - Applies to: the reviewed paper and `2606.13126-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
