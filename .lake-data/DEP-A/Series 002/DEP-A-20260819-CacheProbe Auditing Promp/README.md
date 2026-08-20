# DEP-A-20260819-CacheProbe Auditing Promp

#artificial-intelligence #arXiv #paper-review #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.30613v1, *CacheProbe: Auditing Prompt Cache Isolation in Gateway APIs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.30613-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.30613-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: [ 1 ] describe prompt caching, a method in which key-value attention states can be cached and reused upon an initial request to an LLM. This paper investigates whether OpenRouter’s API gateway architecture introduces prompt caching vulnerabilities that bypass provider-level prompt cache isolation guarantees, and it finds that it does . If a match is found, the provider can reuse the cached KV attention states for the matching prefix and only compute the attention states for the unique tokens in the prompt.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat CacheProbe: Auditing Prompt Cache Isolation in Gateway APIs as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.30613v1
  - Applies to: `2605.30613-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.30613v1
  - Applies to: `2605.30613-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.30613v1
  - Applies to: `2605.30613-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.30613
  - Applies to: `2605.30613-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Ryan Fahey
  - arXiv author search: https://arxiv.org/search/?query=Ryan%20Fahey&searchtype=author
  - Applies to: the reviewed paper and `2605.30613-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
