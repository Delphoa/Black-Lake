# DEP-A-20260805-ELDR MoE Routing

#artificial-intelligence #mixture-of-experts #LLM-serving #routing #expert-locality #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.00466v2, *ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.00466-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.00466-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We present ELDR , an expert-locality-aware decode router for PD-disaggregated MoE serving. ELDR integrates into an existing PD-disaggregated serving stack as a thin layer: a request router in front of the prefill–decode workers and a prefill-time hook that records per-block (1) expert signatures alongside the KV cache, with offline routing state loaded once at startup. During serving, ELDR leaves the standard PD pipeline intact and adds two lightweight steps: signature capture during prefill and a routing decision at the prefill–decode handoff: The router sends the request to a prefill worker using prefix-aware routing.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Operate expert-locality routing as predictive cache affinity under a load constraint: retain signatures, cluster assignments, cache lineage, worker load, expert-fetch traffic, and tail latency so locality gains cannot hide imbalance or model-specific overfitting.

## Associated DEP Records

- [DEP-A-20260717-CrossPool Cold MoE](../DEP-A-20260717-CrossPool%20Cold%20MoE/README.md) - direct disaggregated mixture-of-experts serving and routing context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.00466v2
  - Applies to: `2607.00466-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.00466v2
  - Applies to: `2607.00466-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.00466v2
  - Applies to: `2607.00466-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.00466
  - Applies to: `2607.00466-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Sangjin Choi
  - arXiv author search: https://arxiv.org/search/?query=Sangjin%20Choi&searchtype=author
  - Applies to: the reviewed paper and `2607.00466-whitepaper-review.md`.
- Author: Sukmin Cho
  - arXiv author search: https://arxiv.org/search/?query=Sukmin%20Cho&searchtype=author
  - Applies to: the reviewed paper and `2607.00466-whitepaper-review.md`.
- Author: Yifan Xiong
  - arXiv author search: https://arxiv.org/search/?query=Yifan%20Xiong&searchtype=author
  - Applies to: the reviewed paper and `2607.00466-whitepaper-review.md`.
- Author: Ziyue Yang
  - arXiv author search: https://arxiv.org/search/?query=Ziyue%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2607.00466-whitepaper-review.md`.
- Author: Youngjin Kwon
  - arXiv author search: https://arxiv.org/search/?query=Youngjin%20Kwon&searchtype=author
  - Applies to: the reviewed paper and `2607.00466-whitepaper-review.md`.
- Author: Peng Cheng
  - arXiv author search: https://arxiv.org/search/?query=Peng%20Cheng&searchtype=author
  - Applies to: the reviewed paper and `2607.00466-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
