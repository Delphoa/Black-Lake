# DEP-A-20260804-OmniPilot GPU Advisor

#artificial-intelligence #LLM-serving #GPU-clusters #uncertainty-calibration #resource-allocation #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.01579v1, *OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.01579-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.01579-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The OmniPilot architecture (Figure 1 ) is built around three core, evaluated components: the conformally calibrated cost model, the out-of-distribution abstention layer, and the decision-coupled placement advisor. Describe the issue below: Abstract 1.1 First-attempt failures on shared clusters are expensive 1.2 The gap 1.3 Contributions 2.1 The cluster 2.2 The inference launch decision space 2.3 The measurement-stale problem 3.1 System Architecture 3.2.1 Design and feature engineering 3.2.2 Calibration, abstention, and accuracy 3.3.1 Economic utility 3.3.2 A launch-success prior from cluster data 4.1 Setup 4.2 Placement accuracy 4.3 Out-of-distribution behavior and calibration 4.4 Ablations and data efficiency 4.5 Threats to validity 5.1 Cluster telemetry: a negative result 5.2 What the cluster data provides 5.3 Quantization introduces complex performance dynamics rather than monotonic gains 5.4 Feature-before-data as a general method 5.5 Scope and future work 6. Conclusion Declarations References Appendix A: Supplementary Figures Appendix B: Supplementary Tables C.1 Telemetry collectors and store schema C.2 Gated model updates C.3 Held-out-cell recalibration and the nested confirmation C.4 Benchmark-gate internals Shared GPU.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat OmniPilot: An Uncertainty-Aware LLM Inference Advisor for Heterogeneous GPU Clusters as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260802-AgentServeSim](../DEP-A-20260802-AgentServeSim/README.md) - direct LLM-serving workload and systems-evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.01579v1
  - Applies to: `2607.01579-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.01579v1
  - Applies to: `2607.01579-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.01579v1
  - Applies to: `2607.01579-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.01579
  - Applies to: `2607.01579-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/dmbala/HPC_Tools
  - Applies to: reproducibility context in `2607.01579-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: D. Balamurugan
  - arXiv author search: https://arxiv.org/search/?query=D.%20Balamurugan&searchtype=author
  - Applies to: the reviewed paper and `2607.01579-whitepaper-review.md`.
- Author: Thomas W. Bush
  - arXiv author search: https://arxiv.org/search/?query=Thomas%20W.%20Bush&searchtype=author
  - Applies to: the reviewed paper and `2607.01579-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
