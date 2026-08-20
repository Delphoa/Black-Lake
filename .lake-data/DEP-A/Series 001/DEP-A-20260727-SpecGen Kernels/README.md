# DEP-A-20260727-SpecGen Kernels

#artificial-intelligence #speculative-decoding #GPU-kernels #code-generation #efficient-inference #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.17518v1, *SpecGen: Accelerating Agentic Kernel Optimization with Speculative Generation*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.17518-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.17518-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: SpecGen exploits otherwise idle reasoning time by forking non-reasoning candidate generations at selected points in a reasoning trace. Candidate kernels are validated and profiled in parallel; satisfactory kernels terminate the original reasoning early, resource pools adapt to arrival rate, and spare GPU memory holds remote KV state to avoid repeated prefixes.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat every speculative branch as a portfolio-search order with a cost basis, validation receipt, and stop reason. A falsifying experiment would show that equal-resource parallel non-reasoning search or a better scheduling baseline matches SpecGen once remote-cache and pool-management overhead are included.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.17518v1
  - Applies to: `2606.17518-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.17518v1
  - Applies to: `2606.17518-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.17518v1
  - Applies to: `2606.17518-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.17518
  - Applies to: `2606.17518-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Jihu Guo
  - arXiv author search: https://arxiv.org/search/?query=Jihu%20Guo&searchtype=author
  - Applies to: the reviewed paper and `2606.17518-whitepaper-review.md`.
- Author: Sitian Lu
  - arXiv author search: https://arxiv.org/search/?query=Sitian%20Lu&searchtype=author
  - Applies to: the reviewed paper and `2606.17518-whitepaper-review.md`.
- Author: Tenghui Ma
  - arXiv author search: https://arxiv.org/search/?query=Tenghui%20Ma&searchtype=author
  - Applies to: the reviewed paper and `2606.17518-whitepaper-review.md`.
- Author: Wei Gao
  - arXiv author search: https://arxiv.org/search/?query=Wei%20Gao&searchtype=author
  - Applies to: the reviewed paper and `2606.17518-whitepaper-review.md`.
- Author: Zhisheng Ye
  - arXiv author search: https://arxiv.org/search/?query=Zhisheng%20Ye&searchtype=author
  - Applies to: the reviewed paper and `2606.17518-whitepaper-review.md`.
- Author: Xingcheng Zhang
  - arXiv author search: https://arxiv.org/search/?query=Xingcheng%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.17518-whitepaper-review.md`.
- Author: Dahua Lin
  - arXiv author search: https://arxiv.org/search/?query=Dahua%20Lin&searchtype=author
  - Applies to: the reviewed paper and `2606.17518-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
