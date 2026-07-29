# DEP-A-20260730-KV Compression Stats

#artificial-intelligence #KV-cache #compression #statistical-inference #ablation #validation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.09683v1, *Ablation, Statistical Inference, and Validation for KV-Cache Compression*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.09683-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.09683-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Transformer inference at scale is bounded by memory bandwidth: KV-cache access dominates total memory traffic for long-context generation, and reducing cache size directly translates to latency and throughput improvements. This paper introduces a methodology for controlled evaluation of KV-cache quantization schemes: a set of six synthetic statistical regimes, each designed to isolate one structural assumption of the compression pipeline, together with a statistical framework for distinguishing systematic algorithmic differences from implementation noise. The main findings are: (1) a full ablation over eight QJL variants identifies three non-dominated schemes, eliminating the rest; (2) the statistical validation framework reveals that K-path QJL variance is exponentially amplified by softmax (Jensen’s inequality), while V-path variance is not — a distinction invisible to accuracy-only evaluations; (3) TQ dominates on heavy-tailed data where eigenbasis calibration fails; (4) SQ wins on structured regimes at sufficient budget, provided K and V are calibrated on separate representative sets; and (5) water-filling reduces to uniform allocation in all tested regimes, and the effective semantic dimension d eff d_{\mathrm{eff}}.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Turn KV-compression design into a preregistered statistical pipeline: declare variants and regimes, use paired uncertainty estimates, correct multiplicity, and publish failure surfaces alongside means.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct KV-cache and long-context systems context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.09683v1
  - Applies to: `2607.09683-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.09683v1
  - Applies to: `2607.09683-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.09683v1
  - Applies to: `2607.09683-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.09683
  - Applies to: `2607.09683-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/Dynamis-Labs/spectralquant
  - Applies to: reproducibility context in `2607.09683-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Paolo D'Alberto
  - arXiv author search: https://arxiv.org/search/?query=Paolo%20D%27Alberto&searchtype=author
  - Applies to: the reviewed paper and `2607.09683-whitepaper-review.md`.
- Author: Ashish Siarasao
  - arXiv author search: https://arxiv.org/search/?query=Ashish%20Siarasao&searchtype=author
  - Applies to: the reviewed paper and `2607.09683-whitepaper-review.md`.
- Author: Elliott Delaye
  - arXiv author search: https://arxiv.org/search/?query=Elliott%20Delaye&searchtype=author
  - Applies to: the reviewed paper and `2607.09683-whitepaper-review.md`.
- Author: Rajeev Patwari
  - arXiv author search: https://arxiv.org/search/?query=Rajeev%20Patwari&searchtype=author
  - Applies to: the reviewed paper and `2607.09683-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
