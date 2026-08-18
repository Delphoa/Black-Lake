# DEP-A-20260819-WitCert Sound Runtime Ris

#artificial-intelligence #arXiv #paper-review #KV-cache #model-compression #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.28699v1, *WitCert: Sound Runtime Risk Observability and Gating for KV-Cache Quantization*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.28699-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.28699-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: (a) No measurable quality cost from the certificate : WitCert and RTN-INT8 are at the same error level ( 9.0 × 10 − 3 9.0\!\times\!10^{-3} vs 8.5 × 10 − 3 8.5\!\times\!10^{-3} ), and the extra memory is the 16.1 16.1 B/tok/head FP16 outlier bypass ( + 12.5 % +12.5\% over the 129 129 B of RTN-INT8, + 6.3 % +6.3\% over the 256 256 B FP16 key), bought in exchange for a runtime TV upper bound. We call the runtime quantity the meter : a sound upper bound on the attention total variation, reported as min ⁡ ( 1 , ⋅ ) \min(1,\cdot) since TV ≤ 1 \mathrm{TV}\leq 1 always. An operator therefore learns directly that 18.8% of (layer, head, step) triples carry no guarantee at the current threshold—the deployed form of the runtime observability layer proposed in the introduction.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat WitCert: Sound Runtime Risk Observability and Gating for KV-Cache Quantization as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260812-KVBuffer Serving](../DEP-A-20260812-KVBuffer%20Serving/README.md) - direct decode-time KV-cache serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.28699v1
  - Applies to: `2607.28699-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.28699v1
  - Applies to: `2607.28699-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.28699v1
  - Applies to: `2607.28699-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.28699
  - Applies to: `2607.28699-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Fanzhe Wei
  - arXiv author search: https://arxiv.org/search/?query=Fanzhe%20Wei&searchtype=author
  - Applies to: the reviewed paper and `2607.28699-whitepaper-review.md`.
- Author: Li Liu
  - arXiv author search: https://arxiv.org/search/?query=Li%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.28699-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
