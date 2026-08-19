# DEP-A-20260820-Beyond Capacity Scalable

#artificial-intelligence #arXiv #paper-review #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.14333v1, *Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.14333-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.14333-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: These paths are implemented using Universal Chiplet Interconnect Express (UCIe) links that connect the GPU I/O die to the HBM and HBF base dies and directly connect the two memory base dies [ 46 , 4 ] . Therefore, DASH elevates HBF beyond a capacity-extension tier, making it a first-class component of the GPU memory system for large-scale MoE inference. Describe the issue below: Abstract I Introduction II-A 1 Transformer Layer II-A 2 Continuous Batching Serving HBF Structure HBF Characteristics III-A Limitations of Existing Capacity Scaling III-B Latency Challenges in HBF IV-A UCIe-Based Unified Memory Interconnect HBF Base Die HBM Base Die V-A 1 Placement Along Architecture V-A 2 Placement Within HBF Parallel HBM/HBF Read Dual-Path HBF Read Direct Prefill Write HBM-to-HBF KV Writeback V-C Lookahead Expert Execution Models Baselines and HBF Configuration Simulation VI-B Throughput and End-to-End Latency VI-C Comparison with CPU–GPU Offloading Strategies VI-D Impact of Lookahead Expert Execution VI-E Continuous-Batching Serving VI-F Sensitivity Analysis VI-G Cost Sensitivity and Interconnect Scalability VI-H HBF Endurance VII Related Work VIII Conclusion References Fig.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Beyond Capacity: Scalable MoE LLM Inference via High-Bandwidth Flash with Direct GPU and HBM Paths as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.14333v1
  - Applies to: `2608.14333-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.14333v1
  - Applies to: `2608.14333-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.14333v1
  - Applies to: `2608.14333-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2608.14333
  - Applies to: `2608.14333-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/scale-snu/LLMSimulator
  - Applies to: reproducibility context in `2608.14333-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Seeyeon Kim
  - arXiv author search: https://arxiv.org/search/?query=Seeyeon%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2608.14333-whitepaper-review.md`.
- Author: Juhyeong Jin
  - arXiv author search: https://arxiv.org/search/?query=Juhyeong%20Jin&searchtype=author
  - Applies to: the reviewed paper and `2608.14333-whitepaper-review.md`.
- Author: Joo-Young Kim
  - arXiv author search: https://arxiv.org/search/?query=Joo-Young%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2608.14333-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
