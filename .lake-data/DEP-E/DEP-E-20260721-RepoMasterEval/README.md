# DEP-E-20260721-RepoMasterEval

#code-completion #software-engineering #benchmark #repository-context #mutation-testing #test-adequacy #evaluation #research

## Context

This DEP-E preserves a source-grounded review of *RepoMasterEval: Evaluating Code Completion via Real-World Repositories* (`arXiv:2408.03519v2`). The review focuses on realistic fill-in-the-middle task construction, repository-context retrieval, executable evaluation, mutation-guided test augmentation, and the limits of the reported industrial correlation. The paper was selected by a uniform random draw after repository-wide identifier deduplication.

The local source gate initially classified the archive unit as partial because only a valid PDF was present. A bounded repair preserved that PDF and added verified full-paper HTML, metadata HTML, and a readable source archive to the local archive. All original source files, extracted material, renderings, and repair records remain local; this public DEP contains Markdown only and has no `.source/` directory.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, synthesis relevance, and source attribution.
- `repomastereval_manuscript.md`
  - Schema-complete manuscript covering source metadata, evidence ledger, benchmark construction, reported results, limitations, implementation paths, related DEP synthesis, and selection/integrity validation.

## Summary of Items

### `README.md`

Records the deposit's scope, public source locators, source-withholding policy, and relationship to existing Black Lake research.

### `repomastereval_manuscript.md`

Reviews a 288-task Python/TypeScript benchmark built from six real repositories. RepoMasterEval masks test-covered code at line, block, and function granularity; supplies prefix, suffix, and up to five BM25-retrieved snippets; and evaluates model outputs by executing repository tests. The manuscript reconstructs mutation-guided augmentation, the ten-model comparison, the industry correlation claim, and evidence gaps around public artifact availability, leakage, statistical uncertainty, and transfer.

## Insights and Relevance

RepoMasterEval's durable lesson is that code-completion evaluation is a three-part contract: context must resemble the actual completion surface, tests must reject functionally wrong alternatives without requiring textual identity, and the benchmark must predict a downstream outcome that users care about. The related Repository Context Modalities DEP makes context selection an explicit quality-cost frontier; CLOVER separates execution from requirement and coverage satisfaction; Smart Coverage Goals shows that adding or removing coverage objectives changes a Pareto balance rather than producing a universally better suite. Together, the four records motivate a versioned evaluation harness that audits context, test adequacy, and product correlation separately before combining them into a release gate.

## Attribution Block

- Source URL: https://arxiv.org/abs/2408.03519
  - Applies to: `README.md`, `repomastereval_manuscript.md`.
  - Notes: Canonical arXiv metadata, version history, authorship, subject, DOI, and license locator.
- Source URL: https://arxiv.org/pdf/2408.03519
  - Applies to: `repomastereval_manuscript.md`.
  - Notes: Complete current PDF used for methods, tables, figures, results, and limitations; local copy withheld.
- Source URL: https://arxiv.org/html/2408.03519v1
  - Applies to: `repomastereval_manuscript.md`.
  - Notes: Verified complete-paper HTML fallback used for structural cross-checking; local copy withheld.
- Source URL: https://arxiv.org/e-print/2408.03519
  - Applies to: `repomastereval_manuscript.md`.
  - Notes: TeX/source bundle used to cross-check method and result tables; local archive withheld.
- Source URL: https://doi.org/10.48550/arXiv.2408.03519
  - Applies to: `README.md`, `repomastereval_manuscript.md`.
  - Notes: arXiv-issued DOI.
- Source URL: https://conf.researchr.org/details/ase-2025/ase-2025-industry-showcase/50/RepoMasterEval-Evaluating-Code-Completion-via-Real-World-Repositories
  - Applies to: `repomastereval_manuscript.md`.
  - Notes: Official ASE 2025 Industry Showcase program record.
- Source URL: https://creativecommons.org/licenses/by-nc-sa/4.0/
  - Applies to: `README.md`, `repomastereval_manuscript.md`.
  - Notes: License linked from the arXiv record; no original source file is redistributed here.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-Repo%20Context%20Modalities/2604.13725-whitepaper-review.md
  - Applies to: `repomastereval_manuscript.md`.
  - Notes: Related DEP evidence on repository-context compression and code-task quality-cost tradeoffs.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-CLOVER%20Test%20Benchmark/clover_test_benchmark_manuscript.md
  - Applies to: `repomastereval_manuscript.md`.
  - Notes: Related DEP evidence on executable test generation, coverage-aware context, and layered evaluator contracts.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260717-Smart%20Coverage%20Goals/smart_coverage_goals_manuscript.md
  - Applies to: `repomastereval_manuscript.md`.
  - Notes: Related DEP evidence on mutation, coverage-goal selection, and objective tradeoffs.
