# DEP-A-20260820-Aborted but Not Forgotten

#artificial-intelligence #arXiv #paper-review #KV-cache #agents #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.15939v1, *Aborted but Not Forgotten: KV-Cache Retention Breaks Rollback Consistency in Language Agents*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.15939-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.15939-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We are careful not to claim observational rollback consistency is violated on every model; we claim the Layer-1 invariant is, and that resistance is a behavioral margin that can erode with the next prompt or fine-tune, which is why a state-level fix (§ 4 ) is the robust remedy. Frameworks expose rejection, pause, rollback and abort; an application that dislikes a proposed action rejects it, drops the branch from its transcript, and proceeds as if it never happened. (C2, identification) The retained-KV rollback-consistency channel: across seven families the stale KV alone flips a typed downstream effect and reproduces the in-text effect, with a length/position-matched control excluding a positional confound, an end-to-end session-app replication, a framework-default reproduction needing only the documented transformers cache-reuse path with no tensor surgery, and a reproduction inside a first-class rollback API (LangGraph time-travel) where a verified logical rollback still leaves the KV stale (§ 3 ).

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Aborted but Not Forgotten: KV-Cache Retention Breaks Rollback Consistency in Language Agents as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260812-KVBuffer Serving](../DEP-A-20260812-KVBuffer%20Serving/README.md) - direct decode-time KV-cache serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.15939v1
  - Applies to: `2608.15939-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.15939v1
  - Applies to: `2608.15939-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.15939v1
  - Applies to: `2608.15939-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2608.15939
  - Applies to: `2608.15939-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/ggml-org/llama.cpp
  - Applies to: reproducibility context in `2608.15939-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/docs/transformers/en/kv_cache
  - Applies to: reproducibility context in `2608.15939-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Guijia Zhang
  - arXiv author search: https://arxiv.org/search/?query=Guijia%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2608.15939-whitepaper-review.md`.
- Author: Harry Yang
  - arXiv author search: https://arxiv.org/search/?query=Harry%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2608.15939-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
