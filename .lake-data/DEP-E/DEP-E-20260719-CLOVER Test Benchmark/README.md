# DEP-E-20260719-CLOVER Test Benchmark

#software-testing #test-generation #code-llm #benchmark #long-context #coverage #verification #research

DEP class: DEP-E

Deposition date: 2026-07-19

Subject title: CLOVER: A Test Case Generation Benchmark with Coverage, Long-Context, and Verification

This public-safe DEP-E entry preserves a source-grounded review of arXiv:2502.08806v1. The selected archive unit passed the mandatory complete-source gate after its missing full-paper HTML was repaired. Original PDF, HTML, metadata, TeX/source, extraction, and verification files remain in the private local archive and are not included here.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, synthesis relevance, and final source attribution.
- `clover_test_benchmark_manuscript.md`
  - Schema-complete manuscript covering source metadata, evidence ledger, benchmark construction, coverage-calibrated context, three tasks, reported results, limitations, implementation paths, exactly three related DEP entries, selection/dedup evidence, and the local source-integrity receipt.

No `.source/` directory is present because source deposition and redistribution were not authorized.

## Summary of Items

### `README.md`

This file records what was deposited and why, states the source-locality boundary, and maps every public source URL to the generated manuscript. It is the entry point for downstream reviewers and agents.

### `clover_test_benchmark_manuscript.md`

The manuscript reviews CLOVER, a benchmark built from 12 Python repositories and 845 unique problems across assertion completion, target-aware test implementation, and coverage-oriented test implementation. It reconstructs the paper's coverage-calibrated oracle context, separates execution from requirement-satisfying success, preserves key table results and a table/prose discrepancy, and records that the promised official code/data release was not established during this review. It also translates the work into safe, isolated evaluation and context-selection designs without claiming reproduction.

## Insights and Relevance

CLOVER shows why test generation needs layered verification: a test can parse and execute yet fail to use the requested target or cover every required block. Its coverage-ranked oracle context also reveals that more code is not automatically better context. The three related DEP entries extend this result in complementary directions: Smart Coverage Goals treats coverage criteria as an objective-budget problem; TACO treats terminal output as a task-conditioned compression problem; ContextWeaver treats long-horizon coding evidence as a dependency and validation-lineage problem. Together they motivate a governed pipeline that selects objectives, preserves traceable evidence, runs generated code in isolation, and records distinct execution and requirement outcomes.

## Attribution Block

- Source URL: https://arxiv.org/abs/2502.08806
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Canonical metadata, authors, version, subjects, DOI, license, and artifact locators.
- Source URL: https://arxiv.org/pdf/2502.08806
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Public equivalent of the verified local PDF used for full-paper and visual review; not redistributed.
- Source URL: https://arxiv.org/html/2502.08806
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Official full-paper HTML used for method, result, limitation, and appendix inspection; not redistributed.
- Source URL: https://arxiv.org/e-print/2502.08806
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: TeX/source package used locally for table, prompt, bibliography, and release-locator checks; not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2502.08806
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Persistent arXiv DOI.
- Source URL: https://openreview.net/forum?id=gPpQa4PGEZ
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Official DL4C @ ICLR 2025 venue, date, track, and license record.
- Source URL: https://jiacheng-xu.github.io/
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Author-maintained publication context; no result claim imported.
- Source URL: https://huggingface.co/papers/2502.08806
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Discovery-only release cross-check; no linked model or dataset was observed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`, `clover_test_benchmark_manuscript.md`.
  - Notes: Live repository authority for layout, naming, attribution, source locality, and submission.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`, `clover_test_benchmark_manuscript.md`.
  - Notes: Live DEP-E filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Live related-repository authority read before dedup and related-entry reliance.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Related DEP entry for coverage-goal selection and test-generation objective governance.
- Source URL: https://arxiv.org/abs/2208.04096
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Primary source named by the Smart Coverage Goals DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260715-TACO%20Terminal%20Context/2604.19572-whitepaper-review.md
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Related DEP entry for adaptive observation filtering and terminal/software-engineering evaluation.
- Source URL: https://arxiv.org/abs/2604.19572v3
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Primary source named by the TACO DEP.
- Source URL: https://github.com/multimodal-art-projection/TACO
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Official implementation context named by the TACO DEP; not executed here.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-ContextWeaver%20Selective%20a/2604.23069-whitepaper-review.md
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Related DEP entry for dependency-structured memory and validation lineage.
- Source URL: https://arxiv.org/abs/2604.23069v1
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: Primary source named by the ContextWeaver DEP.
- Source URL: https://arxiv.org/abs/2410.00752
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: TestGenEval primary paper locator for related benchmark context.
- Source URL: https://arxiv.org/abs/2409.17561
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: TestBench primary paper locator for related benchmark context.
- Source URL: https://openreview.net/forum?id=VTF8yNQM66
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: SWE-bench official venue record for executable benchmark context.
- Source URL: https://arxiv.org/abs/2409.07440
  - Applies to: `clover_test_benchmark_manuscript.md`.
  - Notes: SUPER primary paper locator for repository-execution agent evaluation.
