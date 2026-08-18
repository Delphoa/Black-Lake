# DEP-A-20260819-ExaGEMM Exploration Frame

#artificial-intelligence #arXiv #paper-review #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.14622v1, *ExaGEMM: Exploration Framework for CPU-Driven ML Inference via Associative In-Register Computing for Low-Bit GEMM*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.14622-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.14622-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We present ExaGEMM , a workload-/budget-aware RTL/ISA/kernel co-design and exploration framework for register-resident LUT-based low-bit GEMM on CPUs. 1 Introduction 2 Background and Motivation 3.1.1 Framework Overview 3.1.2 Parameterized Execution Space 3.1.3 Hardware Mapping to a SIMD Slice 3.1.4 Instruction Primitives and Instruction-Level Merging 3.2.1 Feasibility and Cost Models 3.2.2 Kernel Selection and Support Ranking 4.1 Experimental Setup 4.2.1 Search Space Reduction 4.2.2 Modeling Fidelity 4.3 Primitive-Side Efficiency Landscapes 4.4 End-to-End Comparative Evaluation 5 Conclusion References Figure 2 summarizes the overall ExaGEMM flow. In other words, ExaGEMM does not propose a new accelerator array; it exposes a CPU-native support point that extends the SIMD slice just enough to make in-register table-driven low-bit GEMM practical.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat ExaGEMM: Exploration Framework for CPU-Driven ML Inference via Associative In-Register Computing for Low-Bit GEMM as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.14622v1
  - Applies to: `2607.14622-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.14622v1
  - Applies to: `2607.14622-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.14622v1
  - Applies to: `2607.14622-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.14622
  - Applies to: `2607.14622-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Hyunwoo Oh
  - arXiv author search: https://arxiv.org/search/?query=Hyunwoo%20Oh&searchtype=author
  - Applies to: the reviewed paper and `2607.14622-whitepaper-review.md`.
- Author: Suyeon Jang
  - arXiv author search: https://arxiv.org/search/?query=Suyeon%20Jang&searchtype=author
  - Applies to: the reviewed paper and `2607.14622-whitepaper-review.md`.
- Author: Hanning Chen
  - arXiv author search: https://arxiv.org/search/?query=Hanning%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2607.14622-whitepaper-review.md`.
- Author: Sanggeon Yun
  - arXiv author search: https://arxiv.org/search/?query=Sanggeon%20Yun&searchtype=author
  - Applies to: the reviewed paper and `2607.14622-whitepaper-review.md`.
- Author: Ryozo Masukawa
  - arXiv author search: https://arxiv.org/search/?query=Ryozo%20Masukawa&searchtype=author
  - Applies to: the reviewed paper and `2607.14622-whitepaper-review.md`.
- Author: Mohsen Imani
  - arXiv author search: https://arxiv.org/search/?query=Mohsen%20Imani&searchtype=author
  - Applies to: the reviewed paper and `2607.14622-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
