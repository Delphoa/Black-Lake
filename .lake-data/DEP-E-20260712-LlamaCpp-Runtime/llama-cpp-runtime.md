---
title: "llama.cpp Runtime - DEP-20260712"
generated_at: "2026-07-12T00:03:00Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded expansion of llama.cpp b9789 from the Local AI Intel source DEP."
source_status: "mixed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-12"
primary_url: "https://github.com/ggml-org/llama.cpp/releases/tag/b9789"
stable_identifier: "llama.cpp b9789 / b3ce5cedf4c007b78a45befe839fa3abada03c0b"
---

# llama.cpp Runtime - DEP-20260712

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Selected DEP records | Primary source package | Markdown | DEP-20260625-Local AI Intel 2343 | Black-Lake-Data/.lake-data/DEP-20260625-Local AI Intel 2343/README.md | Generated source context, not independent authority. | 2026-07-12 | Inspected |
| S2 | Prior report, Report-Mark, manuscript, and log | Iterative context | Markdown | 2026-07-09 baseline | Black-Lake/.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md | Used to identify prior scope. | 2026-07-12 | Inspected |
| S3 | llama.cpp b9789 | Primary release | GitHub release | b9789 | https://github.com/ggml-org/llama.cpp/releases/tag/b9789 | Assets not downloaded. | 2026-07-12 | Directly inspected; new evidence |
| S4 | linked commit | Primary commit | GitHub commit | b3ce5cedf4c007b78a45befe839fa3abada03c0b | https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b | Source tree not cloned. | 2026-07-12 | Directly inspected; new evidence |
| S5 | Repository READMEs | Process standard | Markdown | origin/main | https://github.com/Delphoa/Black-Lake | Process evidence only. | 2026-07-12 | Inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S2 | DEP records | Source bundle and prior review. | Selection and iterative context. | High | Generated findings are not independent primary evidence. |
| E2 | S3 | Official release | 27 assets across macOS/iOS, Linux, Android, Windows, and other targets. | Packaging breadth. | High | Assets were not run. |
| E3 | S4 | Official commit | One-file `src/llama-quant.cpp` change from `n_layer()` to `n_layer_all` for stated MoE-with-MTP fix. | Patch scope. | High | Not built or regression-tested. |
| E4 | S5 | README | DEP placement and attribution contract. | Deposit structure. | High | Not technical evidence. |

## Executive Summary

This DEP-E artifact expands the prior Local AI Stack review by directly inspecting the randomly selected llama.cpp b9789 release. The official release lists 27 assets across macOS/iOS, Linux, Android, Windows, and accelerator-oriented builds, and links verified commit b3ce5ce. The commit is a narrow one-file quantization fix for MoE models with MTP, replacing a layer-count field with `n_layer_all` (E2-E3). No binaries, builds, benchmarks, or regression tests were inspected, so no performance, security, or production-readiness claim is made.

## Detailed Summary

The selected DEP treats local AI as a stack of runtimes, hardware, serving, memory, and governance. Its prior DEP-E manuscript was reviewed before this pass. From eleven recorded supporting sources, b9789 was randomly selected. The release inventory includes macOS Apple Silicon and Intel, iOS, Linux CPU/Vulkan/ROCm/OpenVINO/SYCL, Android arm64, and Windows CPU/ARM64/OpenCL Adreno/CUDA/Vulkan/OpenVINO/SYCL/HIP variants. This is inventory evidence, not functional validation. The linked commit changes three counter initializations from `n_layer()` to `n_layer_all`; the stated behavior still needs controlled testing.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | b9789 publishes a 27-asset cross-platform inventory. | Source claim | E2 | Directly supported by the release page. | High |
| C2 | The release links to a verified one-file quantization-field change for the stated MoE-with-MTP fix. | Source claim / implementation observation | E2-E3 | Directly supported by the commit page. | High |
| C3 | Compatibility validation is the appropriate next step. | Reviewer interpretation | E1-E2 | Availability is not validation. | Medium |

## Methodology

- `Research objective`: Expand prior DEP-E context with one randomly selected supporting source.
- `Sources inspected`: Selected DEP records, prior review records, b9789 release, linked commit, repository READMEs.
- `Discovery strategy`: Eleven prior supporting sources were enumerated; b9789 was randomly selected and inspected with its linked commit.
- `Inclusion criteria`: Primary materials directly tied to the source DEP and release thread.
- `Exclusion criteria`: Assets, builds, models, benchmarks, unrelated commits, unsupported performance claims.
- `Analytical approach`: Conceptual, implementation, comparative, and replication-oriented.
- `Evidence handling`: Claims map to E1-E4 and distinguish source claims from interpretation.
- `Uncertainty handling`: Missing execution and benchmark evidence remains explicit.

## Scope, Constraints, and Assumptions

- `Scope`: b9789 and its linked quantization fix.
- `Temporal boundary`: Sources accessed 2026-07-12.
- `Evidence limits`: No asset download, build, benchmark, dependency audit, or full diff review.
- `Assumptions`: The release page and linked commit identify intended provenance.
- `Constraints`: Public-source review only; no external files redistributed; local execution details withheld.
- `Out of scope`: Deployment recommendation, certification, or vulnerability analysis.
- `Intended use`: Provenance-preserving review and compatibility/regression planning.

## Observations

- `Observed pattern`: Packaging spans desktop, mobile, server, and accelerator paths (E2).
- `Technical implication`: A narrow quantization fix needs configuration-aware regression testing (E3).
- `Contradiction or tension`: Broad availability can be mistaken for broad validation.
- `Open question`: Which b9789 assets and MoE-with-MTP configurations have automated regression coverage?

## Considerations

Verify assets, checksums, dependencies, hardware compatibility, and model behavior in authorized environments. Local runtimes can improve data locality while shifting patching and access-control responsibility. The inspected set does not establish the security posture of release assets or dependencies.

## Strengths

- Official release and directly linked verified commit provide strong provenance.
- Patch scope is narrow and inspectable.
- Prior records make the expansion traceable.

## Weaknesses

- Release inventory is not a functional test or benchmark.
- No assets, source trees, checksums, CI results, or model configurations were collected.
- The broad DEP cannot establish complete runtime behavior.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Capture asset manifest and checksums | Provenance | Inventory is not frozen evidence. | Better audit trail. | Storage policy review. | Compare with official metadata. |
| Build a small MoE-with-MTP regression case | Quantization | The fix targets a boundary. | Tests stated correction. | Authorized hardware/model access. | Version-pinned synthetic reproduction. |
| Create a platform matrix | Validation | Assets are not execution evidence. | Separates published from validated targets. | Hardware cost. | Record model and result. |

## Potential Implementations

- `Release Compatibility Registry`: User - runtime maintainer; goal - track smoke-tested assets; mechanism - join release metadata to controlled test records; inputs - official metadata and synthetic prompts; outputs - version-pinned matrix; risk controls - checksums and human review; evaluation - traceable pass/fail coverage.
- `Quantization Regression Corpus`: User - runtime QA engineer; goal - detect MoE-with-MTP regressions; mechanism - run licensed or synthetic fixtures; inputs - authorized fixtures and pinned builds; outputs - regression report; risk controls - isolated environment; evaluation - deterministic behavior.

## Three Ways to Exercise This Research

1. `Release inventory audit`: Record b9789 platform and accelerator classes from the official page without downloads; success is a source-linked inventory; stop if metadata is ambiguous.
2. `Synthetic quantization regression`: In an authorized isolated environment, compare expected behavior across pinned builds using a tiny approved fixture; success is a reproducible result; stop if policy or licensing is unresolved.
3. `Compatibility gap review`: Map each published asset to an approved test record or explicit evidence gap; success is no unsupported status claim; stop if records contain sensitive workload data.

## Example MVP Product

- `Product name`: Runtime Release Evidence Board
- `Target user`: Engineer evaluating a local LLM runtime.
- `Problem`: Release pages do not show independently validated environments.
- `Core workflow`: Import inventory, attach synthetic test records, display gaps, export review.
- `Data requirements`: Public metadata and non-sensitive authorized test records.
- `Architecture`: Internal app with versioned metadata, evidence validation, and read-only reports.
- `Success metrics`: Assets with traceable metadata and adoption claims linked to tests.
- `Risk controls`: URL/checksum validation, least privilege, synthetic inputs, human approval.
- `Limitations`: Does not prove performance, security, or universal compatibility.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| **New in this pass: llama.cpp b9789 release** | Official runtime release | Direct inspection added 27-asset inventory and release-to-commit linkage. | https://github.com/ggml-org/llama.cpp/releases/tag/b9789 |
| **New in this pass: llama.cpp b3ce5ce commit** | Official runtime commit | Direct inspection added n_layer_all detail for the MoE-with-MTP fix. | https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b |
| vLLM v0.23.0 release | Official serving release | Prior self-hosted serving and accelerator thread. | https://github.com/vllm-project/vllm/releases/tag/v0.23.0 |
| Ollama v0.30.10 release | Official local runtime release | Prior Apple Silicon MLX thread. | https://github.com/ollama/ollama/releases/tag/v0.30.10 |
| FactoryLLM | arXiv preprint | Prior local/open-source RAG evaluation thread. | https://arxiv.org/abs/2606.14119 |
| Agent Memory | arXiv preprint | Prior stateful-agent memory thread. | https://arxiv.org/abs/2606.06448 |
| Toward Secure LLM Agents | arXiv preprint | Prior tool, authority, and persistent-state governance thread. | https://arxiv.org/abs/2606.10749 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | Black-Lake-Data/.lake-data/DEP-20260625-Local AI Intel 2343/README.md | DEP identity and attribution. | 2026-07-12 | Repository-relative; local execution context withheld. |
| R2 | Black-Lake-Data/.lake-data/DEP-20260625-Local AI Intel 2343/daily_research_findings_2026-06-25_2343.md | Local-AI source bundle. | 2026-07-12 | Source-package context. |
| R3 | Black-Lake/.lake-data/DEP-E-20260709-Local AI Stack/local-ai-research.md | Prior scope and baseline. | 2026-07-12 | Iterative context. |
| R4 | Black-Lake/.logs/20260709-DEP-20260625-Local AI Intel 2343-LOG.md | Prior validation backlog. | 2026-07-12 | Iterative context. |
| R5 | https://github.com/ggml-org/llama.cpp/releases/tag/b9789 | **New:** tag, linked commit, and 27-asset inventory. | 2026-07-12 | Official release directly inspected; assets not collected. |
| R6 | https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b | **New:** title, one-file scope, and field change. | 2026-07-12 | Official verified commit directly inspected. |

## Appendix

- `Automation family`: Black-Lake Data Processing & Review; Black-Lake Data Processing & Review 0900
- `Selected DEP`: Black-Lake-Data/.lake-data/DEP-20260625-Local AI Intel 2343
- `Candidate count`: 41; `Excluded count`: 1; `Eligible count`: 40.
- `24-hour cutoff`: 2026-07-11T00:03:00Z.
- `Supporting-source candidate count`: 11; random expansion selection: llama.cpp b9789 release.
- `Source inventory`: no new source files; evidence is repository-relative Markdown and public URLs.
