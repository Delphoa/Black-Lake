# DEP-E-20260713-SMES Expert Sparsity

#recommender-systems #multi-task-learning #mixture-of-experts #sparse-routing #model-scaling #ml-systems #production-evaluation #arxiv

Public-safe deposition context: on 2026-07-13, one paper unit was selected uniformly from 75,761 unique PDF-parent units and accepted on the first draw after repository, memory, related-repository, and 24-hour duplicate checks. The manuscript reviews arXiv:2602.09386v1 source-first and separates author-reported results from reviewer interpretation. No local path, exact execution timestamp, or private source file is included.

## Contents

- `README.md` — DEP manifest, package summary, relevance notes, and source attribution.
- `smes_expert_sparsity_manuscript.md` — Schema-complete research manuscript covering the paper's routing mechanism, load-balancing regularizer, deployment path, empirical evidence, limitations, and bounded implementation ideas.

No `.source/` directory is included. The reviewed PDF was already present in a private archive, and repository redistribution permission was not assumed. Public locators are preserved below.

## Summary of Items

- `README.md` matters because it records the repository-compliant inventory, public-safe selection context, source policy, and provenance needed for later review.
- `smes_expert_sparsity_manuscript.md` matters because it converts the selected paper into a traceable evidence ledger, claims map, implementation analysis, replication plan, and cross-DEP synthesis while preserving uncertainty around proprietary experiments and unreleased code.

## Insights and Relevance

SMES frames sparse mixture-of-experts recommendation as a cross-layer systems problem. Its task-shared and task-adaptive routing bounds the union of experts activated by multiple objectives, while global load regularization, deduplicated execution, grouped GEMM, and workspace planning aim to convert model sparsity into actual latency savings. Related Black Lake records reinforce that this conversion depends on locality-aware routing, inference-specialized runtimes, and topology-correct quantization/runtime handling. The work is relevant to scalable recommender serving, but its production claims remain author-reported because the industrial dataset, implementation, telemetry, and full statistical protocol are unavailable.

## Attribution Block

- Source URL: https://arxiv.org/abs/2602.09386
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Primary metadata, abstract, authorship, submission history, subject, DOI, and source locators.
- Source URL: https://arxiv.org/pdf/2602.09386
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Primary full-text locator supporting method, experiment, result, and limitation analysis; no PDF was redistributed.
- Source URL: https://arxiv.org/html/2602.09386
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Public HTML locator; direct web retrieval was unavailable, so substantive claims rely on the inspected PDF.
- Source URL: https://doi.org/10.48550/arXiv.2602.09386
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Stable arXiv-issued DOI.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260703-Tech%20Intel%200103
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Related DEP containing the inspected ELDR expert-routing finding.
- Source URL: https://arxiv.org/abs/2607.00466
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Primary basis recorded for the ELDR related finding.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260712-KDFlow%20LLM%20Distill
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Related processed DEP on workload-aware MoE inference and throughput.
- Source URL: https://arxiv.org/abs/2603.01875
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Primary basis recorded by the KDFlow related DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E-20260712-LlamaCpp-Runtime
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Related processed DEP on an MoE-with-MTP quantization/runtime correction.
- Source URL: https://github.com/ggml-org/llama.cpp/releases/tag/b9789
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Official runtime release recorded by the related DEP.
- Source URL: https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b
  - Applies to: `smes_expert_sparsity_manuscript.md`
  - Notes: Official MoE-with-MTP correction recorded by the related DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`, `smes_expert_sparsity_manuscript.md`
  - Notes: Live Black Lake deposition, attribution, stability, and commit authority read before drafting.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `README.md`, `smes_expert_sparsity_manuscript.md`
  - Notes: Live related-repository provenance and DEP context read before drafting.
