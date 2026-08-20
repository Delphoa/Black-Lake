# DEP-A-20260717-HMA Serve Disaggregation

#artificial-intelligence #distributed-systems #llm-serving #prefill-decode #kv-cache #accelerators

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.29986v1, *HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.29986-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.29986-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: HMA-Serve assigns compute-heavy prefill to GDDR accelerators and memory-heavy decode to HBM GPUs. It applies phase-wise precision, overlaps per-layer KV transfer with later prefill, and defers dequantization until data reaches the decode device.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use an online phase-placement optimizer fed by measured rooflines, transfer queues, quality probes, and current cost, with a same-vendor fallback when conversion or network debt grows.

## Associated DEP Records

- [DEP-A-20260716-KV Memory Hierarchy](../DEP-A-20260716-KV%20Memory%20Hierarchy/README.md) - direct method context: reviewed survey of KV-cache representation, movement, reuse, and memory hierarchy. This is method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.29986v1
  - Applies to: `2606.29986-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.29986v1
  - Applies to: `2606.29986-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.29986v1
  - Applies to: `2606.29986-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.29986
  - Applies to: `2606.29986-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Zhixiang Wei
  - arXiv author search: https://arxiv.org/search/?query=Zhixiang%20Wei&searchtype=author
  - Applies to: the reviewed paper and `2606.29986-whitepaper-review.md`.
- Author: Yun Wang
  - arXiv author search: https://arxiv.org/search/?query=Yun%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.29986-whitepaper-review.md`.
- Author: James Yen
  - arXiv author search: https://arxiv.org/search/?query=James%20Yen&searchtype=author
  - Applies to: the reviewed paper and `2606.29986-whitepaper-review.md`.
- Author: Mingyuan Xia
  - arXiv author search: https://arxiv.org/search/?query=Mingyuan%20Xia&searchtype=author
  - Applies to: the reviewed paper and `2606.29986-whitepaper-review.md`.
- Author: Zhengwei Qi
  - arXiv author search: https://arxiv.org/search/?query=Zhengwei%20Qi&searchtype=author
  - Applies to: the reviewed paper and `2606.29986-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
