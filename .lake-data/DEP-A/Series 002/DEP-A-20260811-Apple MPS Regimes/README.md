# DEP-A-20260811-Apple MPS Regimes

#artificial-intelligence #Apple-MPS #LLM-inference #KV-cache #latency #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.08913v2, *Non-Monotonic Latency in Apple MPS Decoding: KV Cache Interactions and Execution Regimes*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.08913-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.08913-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Instead, we uncover a more critical phenomenon: autoregressive decoding on MPS exhibits non-monotonic latency scaling, with abrupt latency regimes emerging under specific decoding configurations and particularly pronounced under KV cache. Through controlled experiments, we demonstrate that (1) the instability is not explained by model size or memory limits alone, (2) it emerges during decoding rather than prefill, and (3) KV cache remains nominally faster at all tested lengths, but its practical advantage is largely neutralized at pathological decoding configurations (speedup collapses from 4.9 4.9 – 20.3 × 20.3\times to 1.9 × 1.9\times ), while cache-off runs still show residual non-monotonicity. We further show that key–value (KV) cache interacts strongly with these pathological execution regimes: KV caching remains beneficial overall, but its practical speedup collapses sharply within anomalous configurations, while cache-disabled decoding still exhibits residual non-monotonic behavior.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use Apple MPS decoding measurements as a versioned execution-regime map: pin hardware and software stacks, record prefill/decode boundaries, cache state, synchronization, memory telemetry, and repeated latency distributions, then route around pathological configurations instead of extrapolating smooth scaling.

## Associated DEP Records

- [DEP-A-20260810-AsyncTLS](../DEP-A-20260810-AsyncTLS/README.md) - direct long-context sparse-attention runtime and latency context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.08913v2
  - Applies to: `2605.08913-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.08913v2
  - Applies to: `2605.08913-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.08913v2
  - Applies to: `2605.08913-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.08913
  - Applies to: `2605.08913-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Willy Fitra Hendria
  - arXiv author search: https://arxiv.org/search/?query=Willy%20Fitra%20Hendria&searchtype=author
  - Applies to: the reviewed paper and `2605.08913-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
