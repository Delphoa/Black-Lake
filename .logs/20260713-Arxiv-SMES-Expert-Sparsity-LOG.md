# Arxiv DEP Job Log: SMES Expert Sparsity

## Public-Safe Run Summary

- Date: 2026-07-13
- Actor/tool: Codex recurring Arxiv DEP workflow
- Action: Uniformly select one local arXiv paper unit, validate eligibility, perform a source-first review, and prepare the required Black Lake artifacts.
- Selected paper: **SMES: Towards Scalable Multi-Task Recommendation via Expert Sparsity**
- Stable identifier: arXiv:2602.09386v1; DOI: 10.48550/arXiv.2602.09386
- Outcome: Eligible on the first draw; full PDF text and public arXiv metadata were inspected; artifacts were generated and validated.
- Blockers: None.

## Selection and Deduplication

- Enumeration command: `rg --files -g "*.pdf"` against the private source archive.
- Paper-unit rule: each unique PDF parent directory counted as one paper unit; nearby metadata files were inspected with the selected unit.
- Candidate count: 75,761 paper units from 75,761 PDFs.
- Random method: PowerShell `Get-Random` over the complete, sorted set of unique paper-unit directories.
- Selected zero-based index: 48,963.
- Duplicate exclusion count: 0.
- Reselection count: 0.
- Acceptance: first draw accepted.
- Dedup keys: arXiv ID `2602.09386`, DOI `10.48550/arXiv.2602.09386`, normalized title, `SMES`, and `SMES-Expert-Sparsity` slug.
- Dedup scope: Black Lake `.logs`, `.reports`, `.lake-data`, public staging pointers, all available repository refs and worktrees, recent 24-hour artifact paths, automation memory, and relevant Black-Lake-Data paths/content.
- Validation result: no matching deposit or same-paper marker was found.

## Source Processing

- Local-first extractor preflight selected `pypdf`; `pdftotext` was unavailable.
- PDF extraction succeeded; local HTML and source-package inputs were absent, so cache status was partial.
- Public arXiv abstract metadata and the local full PDF text were inspected.
- Source files collected into the public DEP: no. The existing private archive PDF was not redistributed because repository redistribution permission was not assumed.

## Output Paths

- `.logs/20260713-Arxiv-SMES-Expert-Sparsity-LOG.md`
- `.reports/BL-Arxiv-SMES-Expert-Sparsity-20260713/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260713-SMES Expert Sparsity/README.md`
- `.lake-data/DEP-E/DEP-E-20260713-SMES Expert Sparsity/smes_expert_sparsity_manuscript.md`

## Related DEP Entries

1. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260703-Tech Intel 0103` — ELDR connects expert-aware routing to serving latency and load-aware placement.
2. `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill` — separates sparse MoE inference from training workloads and measures throughput consequences.
3. `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime` — records a topology-sensitive MoE quantization/runtime correction and the need for configuration-specific regression evidence.

## Next-Review Questions

1. Can the public KuaiRand result table be reproduced from a released implementation with pinned seeds, preprocessing, and router budgets?
2. How do shared/private expert budgets affect per-task calibration and tail-task quality under label-distribution drift?
3. Which portion of the reported latency improvement comes from routing sparsity, deduplicated execution, grouped GEMM, and workspace allocation individually?

## Challenges

1. The industrial dataset, production serving stack, and traffic-level measurements are not independently accessible.
2. The paper reports statistical significance for online gains without exposing confidence intervals, test details, or repeated-run distributions.
3. Placeholder conference and DOI fields in the PDF complicate venue interpretation, while no official code artifact was identified from inspected sources.

## Public-Safety Validation

- Artifacts use date-only markers and repository-relative paths.
- No home directory, username, drive path, machine name, workspace root, local timezone label, or exact local execution timestamp is included.
