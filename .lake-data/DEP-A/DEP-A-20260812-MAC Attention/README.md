# DEP-A-20260812-MAC Attention

#artificial-intelligence #attention #long-context #serving #GPU-kernels #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2604.00235v1, *MAC-Attention: a Match-Amend-Complete Scheme for Fast and Accurate Attention Computation*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2604.00235-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2604.00235-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Table 4 shows that MAC-Attention consistently achieves a ≥ 99 % \geq 99\% hit ratio while maintaining comparable accuracy to full attention. We propose Match–Amend–Complete (MAC) Attention , a fidelity and access‑preserving reuse scheme that matches pre‑RoPE queries using an L2, dimension‑aware threshold, amends a short high‑mass band near the reuse boundary, and completes with an associative, numerically stable log‑domain merge . Describe the issue below: MAC-Attention: a Match–Amend–Complete Scheme for Fast and Accurate Attention Computation Even with I/O-aware kernels, the dominant cost at long context decoding remains memory traffic: streaming large KV regions from high-bandwidth memory (HBM) Dao et al.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate attention reuse as an approximate proposal followed by a bounded exact correction: record match identity, correction band, tail computation, numerical merge, and fallback so speedups remain separable from match-rate assumptions and fidelity checks.

## Associated DEP Records

- [DEP-A-20260810-AsyncTLS](../DEP-A-20260810-AsyncTLS/README.md) - direct long-context sparse-attention runtime and latency context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260727-Programmable KV](../DEP-A-20260727-Programmable%20KV/README.md) - direct programmable KV-state reuse and serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2604.00235v1
  - Applies to: `2604.00235-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2604.00235v1
  - Applies to: `2604.00235-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2604.00235v1
  - Applies to: `2604.00235-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2604.00235
  - Applies to: `2604.00235-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/YJHMITWEB/MAC-Attention
  - Applies to: reproducibility context in `2604.00235-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Jinghan Yao
  - arXiv author search: https://arxiv.org/search/?query=Jinghan%20Yao&searchtype=author
  - Applies to: the reviewed paper and `2604.00235-whitepaper-review.md`.
- Author: Sam Adé Jacobs
  - arXiv author search: https://arxiv.org/search/?query=Sam%20Ad%C3%A9%20Jacobs&searchtype=author
  - Applies to: the reviewed paper and `2604.00235-whitepaper-review.md`.
- Author: Walid Krichene
  - arXiv author search: https://arxiv.org/search/?query=Walid%20Krichene&searchtype=author
  - Applies to: the reviewed paper and `2604.00235-whitepaper-review.md`.
- Author: Masahiro Tanaka
  - arXiv author search: https://arxiv.org/search/?query=Masahiro%20Tanaka&searchtype=author
  - Applies to: the reviewed paper and `2604.00235-whitepaper-review.md`.
- Author: Dhabaleswar K Panda
  - arXiv author search: https://arxiv.org/search/?query=Dhabaleswar%20K%20Panda&searchtype=author
  - Applies to: the reviewed paper and `2604.00235-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
