# DEP-A-20260814-DGAP KV Restoration

#artificial-intelligence #KV-cache #quantization #logit-restoration #long-context #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.16248v1, *High-accuracy Low-Bit KV-Cache Quantization via Local Distribution Restoration*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.16248-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.16248-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We propose DGAP ( D isagreement- G uided A daptive P recision), a lightweight layer for restoring local distribution fidelity in low-bit KV-cache decoding. We propose DGAP , a lightweight distribution-restoration layer with a risk detector and selective top- K K corrector that restores local candidate distributions without changing the persistent low-bit KV cache. We propose DGAP ( D isagreement- G uided A daptive P recision), a lightweight local distribution-restoration layer for low-bit KV-cache decoding.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat selective logit restoration as an exception-handling layer for extreme quantization: log the risk trigger, restored candidate set, ranking delta, and decode overhead, then test whether calibrated local repairs transfer across models, tasks, and sampling regimes.

## Associated DEP Records

- [DEP-A-20260810-MomentKV](../DEP-A-20260810-MomentKV/README.md) - direct long-context KV-cache eviction and retention context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260804-ReQAT FP4 Reasoning](../../Series%20001/DEP-A-20260804-ReQAT%20FP4%20Reasoning/README.md) - direct low-bit quantization and capability-preservation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.16248v1
  - Applies to: `2607.16248-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.16248v1
  - Applies to: `2607.16248-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.16248v1
  - Applies to: `2607.16248-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.16248
  - Applies to: `2607.16248-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Gradwell Dzikanyanga
  - arXiv author search: https://arxiv.org/search/?query=Gradwell%20Dzikanyanga&searchtype=author
  - Applies to: the reviewed paper and `2607.16248-whitepaper-review.md`.
- Author: Yanqi Pan
  - arXiv author search: https://arxiv.org/search/?query=Yanqi%20Pan&searchtype=author
  - Applies to: the reviewed paper and `2607.16248-whitepaper-review.md`.
- Author: Weihao Yang
  - arXiv author search: https://arxiv.org/search/?query=Weihao%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2607.16248-whitepaper-review.md`.
- Author: Donglei Wu
  - arXiv author search: https://arxiv.org/search/?query=Donglei%20Wu&searchtype=author
  - Applies to: the reviewed paper and `2607.16248-whitepaper-review.md`.
- Author: Wen Xia
  - arXiv author search: https://arxiv.org/search/?query=Wen%20Xia&searchtype=author
  - Applies to: the reviewed paper and `2607.16248-whitepaper-review.md`.
- Author: Hao Huang
  - arXiv author search: https://arxiv.org/search/?query=Hao%20Huang&searchtype=author
  - Applies to: the reviewed paper and `2607.16248-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
