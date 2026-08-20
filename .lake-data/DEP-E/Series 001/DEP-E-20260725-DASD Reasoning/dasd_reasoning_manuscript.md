---
title: "DASD Reasoning - DEP-E"
generated_at: "2026-07-25 (public-safe date-only record)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of Distribution-Aligned Sequence Distillation for long chain-of-thought reasoning."
source_status: "complete local source bundle verified; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-25"
temporal_cutoff: "arXiv v1 and inspected release pages through 2026-07-25"
primary_url: "https://arxiv.org/abs/2601.09088"
stable_identifier: "arXiv:2601.09088; DOI:10.48550/arXiv.2601.09088"
confidence_summary: "High for source identity, source integrity, and transcribed figures/tables; medium for causal attribution; low for unreplicated transfer."
safety_scope: "Research review, synthetic evaluation, and non-consequential implementation planning only."
distribution_notes: "Generated Markdown and public URLs only. Source files, caches, extracted text, and renders remain local and are not redistributed."
---

# DASD Reasoning - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Canonical metadata | HTML | 2601.09088v1 | https://arxiv.org/abs/2601.09088 | Metadata only; not used as full-paper evidence | 2026-07-25 | Inspected |
| S2 | arXiv paper | Primary paper | PDF | 2601.09088v1 | https://arxiv.org/pdf/2601.09088 | Verified private copy; not redistributed | 2026-07-25 | Complete and visually sampled |
| S3 | arXiv rendered paper | Primary paper | HTML | 2601.09088v1 | https://arxiv.org/html/2601.09088 | Verified private copy; not redistributed | 2026-07-25 | Complete and inspected |
| S4 | arXiv source package | Primary source structure | TeX archive | 2601.09088v1 | https://arxiv.org/e-print/2601.09088 | Withheld locally; no redistribution | 2026-07-25 | Collected and extracted locally |
| S5 | DASD official repository | Official implementation context | Git repository | public main branch inspected | https://github.com/D2I-ai/dasd-thinking | Code was read statically, not run | 2026-07-25 | Inspected |
| S6 | DASD collection | Official release context | Model/data collection | DASD-Thinking | https://huggingface.co/collections/Alibaba-Apsara/dasd-thinking | No model or dataset file downloaded | 2026-07-25 | Inspected |
| S7 | WorkflowLLM Enhancing - DEP-E | Related synthesis | Markdown | DEP-E | `.lake-data/DEP-E/DEP-E-20260724-WorkflowLLM Enhancing/workflowllm_enhancing_manuscript.md` | Repository-derived synthesis | 2026-07-25 | Inspected |
| S8 | MOSS Enabling Code-Driven - DEP-E | Related synthesis | Markdown | DEP-E | `.lake-data/DEP-E/DEP-E-20260724-MOSS Enabling Code-Driven/moss_enabling_code_driven_manuscript.md` | Repository-derived synthesis | 2026-07-25 | Inspected |
| S9 | Shuffled Autoregression - DEP-E | Related synthesis | Markdown | DEP-E | `.lake-data/DEP-E/DEP-E-20260724-Shuffled Autoregress/shuffled_autoregression_manuscript.md` | Repository-derived synthesis | 2026-07-25 | Inspected |

**Paper:** *Distribution-Aligned Sequence Distillation for Superior Long-CoT Reasoning* by Shaotian Yan, Kaiyuan Liu, Chen Shen, Bing Wang, Sinan Fan, Jun Zhang, Yue Wu, Zheng Wang, and Jieping Ye. Submitted 2026-01-14; arXiv v1 reviewed.

**Source integrity:** a PDF-only local unit was repaired before review. It now has a valid PDF, full-paper HTML, metadata HTML, TeX archive, refreshed provenance, a machine-readable summary, and a verification report. Every source file remains local and is absent from this DEP.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Official metadata | title, author list, date, abstract, and identifiers | source identity | High | abstract is not experiment evidence |
| E2 | S2-S4 | Complete primary source bundle | method sections, tables, conclusion, and source structure | method and author-reported results | High for transcription | no replication |
| E3 | S2 | Rendered PDF pages and Table 6 | table legibility, reported benchmark values, release links | numeric cross-check | High for transcription | no recomputation |
| E4 | S5 | Official repository | code-tree and training/release documentation | release availability context | Medium-high | repository not executed or audited end-to-end |
| E5 | S6 | Official collection | listed models, data, and paper entry | model/data release context | Medium | collection may change and does not prove reproduction |
| E6 | S7-S9 | Related DEP manuscripts | workflow, agent context, and autoregressive controls | cross-DEP synthesis | Medium | different modalities and evaluations |

## Executive Summary

Distribution-Aligned Sequence Distillation (DASD) is a staged long-reasoning distillation pipeline for a 4B student model. The authors argue that ordinary supervised fine-tuning on teacher completions underrepresents the teacher's sequence-level distribution, can mismatch student capacity, and leaves exposure bias between teacher forcing and autoregressive inference. DASD combines temperature-scheduled learning, divergence-aware sampling, and mixed-policy distillation.

The paper reports DASD-4B-Thinking at 88.5 AIME24, 83.3 AIME25, 69.3 LiveCodeBench v5, 67.5 LiveCodeBench v6, and 68.4 GPQA-D. Those values were cross-checked in the primary table but not reproduced. The official repository and collection support release availability, not replication. The durable implementation insight is to make trace selection, revision, and rollout correction visible in a reproducible evidence ledger.

## Detailed Summary

### Problem and mechanism

The paper studies long chain-of-thought distillation from a stronger teacher to a compact student. Temperature-scheduled learning starts with lower-temperature trajectories for stable early training and later adds higher-temperature trajectories to broaden output coverage. Divergence-aware sampling prioritizes sentence-level teacher/student mismatch. Mixed-policy distillation takes student-generated prefixes, truncates them, and retains filtered teacher continuations for a lightweight on-policy correction stage.

The dense model uses Qwen3-4B-Instruct-2507 as student and gpt-oss-120b as teacher. The reported data spans mathematics, code generation, scientific reasoning, and instruction following. The authors state that the dense pipeline uses 448K samples and that an MoE preview reuses stage-one data.

### Evaluation

The reported benchmarks are AIME24, AIME25, LiveCodeBench v5/v6, and GPQA-D. The paper says it sampled 64 responses per question at temperature 1.0 and top-p 1.0. Table 6 reports the final model at 88.5, 83.3, 69.3, 67.5, and 68.4 on those respective metrics. Table 7 starts from Qwen3-4B-Instruct-2507 and reports staged improvements to 83.3 AIME25, 67.5 LCB v6, and 68.4 GPQA-D. These are author-reported associations, not independently verified causal effects.

### Release context

The linked official repository describes release and training materials; the Hugging Face collection lists the dense model, MoE preview, and data resources. A credible reuse still requires frozen revisions, licensing review, a data manifest, evaluator versions, compute budget, dependency record, and leakage controls.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Temperature scheduling, divergence-aware sampling, and mixed-policy distillation form DASD. | Author mechanism claim | E2 | Directly supported by method sections and Figure 2. | High |
| C2 | DASD improves reported results for a 4B reasoning model across the listed benchmarks. | Author empirical claim | E2, E3 | Values are transcribed from the primary table; no rerun occurred. | High for transcription; medium for generalization |
| C3 | The staged procedure reduces exposure-bias effects. | Author causal claim | E2, E3 | Table 7 is supportive within the reported setup; independent sensitivity evidence is absent. | Medium |
| C4 | Public release links make the results independently reproducible. | Implied availability claim | E4, E5 | Rejected: release availability is necessary but insufficient for an exact rerun. | High rejection confidence |
| C5 | Trace-level provenance and correction gates are a transferable engineering pattern. | Reviewer interpretation | E2, E6 | Plausible synthesis requiring target-specific experiments. | Medium |

## Methodology

- `Research objective`: preserve the paper's source-grounded mechanism, reported evidence, release context, limitations, and safe implementation implications.
- `Sources inspected`: official metadata; verified PDF, full-paper HTML, metadata HTML, and TeX source; extracted local cache; representative rendered pages; official GitHub repository; official Hugging Face collection; and exactly three related DEP manuscripts.
- `Discovery strategy`: used `rg --files -g "*.pdf"`, grouped by PDF parent unit, used PowerShell `Get-Random` for a uniform draw, checked dedup markers, repaired the source unit before review, then extracted a missing-only cache and inspected release pages.
- `Inclusion criteria`: primary method, tables, evaluation setup, release statements, conclusion, source integrity, and concrete related DEP mechanisms.
- `Exclusion criteria`: abstract-only evidence, prior deposits, source-incomplete units, source redistribution, unexecuted code/data claims, and production-autonomy conclusions.
- `Analytical approach`: empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication planning.
- `Evidence handling`: author claims, transcribed measurements, release observations, and reviewer interpretations are labeled separately.
- `Uncertainty handling`: unreproduced benchmarks, release drift, configuration uncertainty, resource requirements, and transfer risk remain explicit.
- `Random selection and dedup`: 75,777 parent-paper units; zero-based draw index 56,517; first draw accepted; zero duplicate exclusions and reselections; no prior owning artifact or 24-hour marker found.
- `Cache methodology`: after integrity repair, `missing-only` extraction generated local PDF, HTML, and source text with pypdf, HTML regex extraction, and tarfile. No network was used during cache extraction.

## Scope, Constraints, and Assumptions

- `Scope`: the research problem, three-stage mechanism, reported benchmark evidence, release context, limitations, and bounded research translation.
- `Temporal boundary`: arXiv v1 and public release pages inspected through 2026-07-25.
- `Evidence limits`: no model, dataset, code, configuration, benchmark, or inference execution; no cost, throughput, safety, or license audit.
- `Assumptions`: the paper's links identify the reviewed official repository and model/data collection.
- `Constraints`: local-source-only handling, public-safe records, synthetic or authorized evaluation only, and no autonomous consequential action.
- `Out of scope`: performance reproduction, production deployment, benchmark-leadership claims beyond the paper's setup, and downloading model/data artifacts.
- `Intended use`: research review, DEP preservation, replication planning, and safe evaluation-prototype design.
- `Reproducibility boundary`: credible replication needs frozen revisions, training/evaluation manifests, hardware/dependency records, seeds, and benchmark hygiene.

## Observations

- `Observed pattern`: the method changes both the training-trace distribution and student/teacher rollout relationship rather than only applying a post-hoc filter.
- `Observed pattern`: staged gains are displayed, but the table cannot substitute for repeated-seed or matched-compute evidence.
- `Technical implication`: trace provenance should include teacher revision, temperature, selection rationale, filter result, student checkpoint, prefix transformation, and evaluation partition.
- `Contradiction or tension`: public release links enable follow-on work, while the paper-exact reproduction boundary remains unresolved until releases are run and pinned.
- `Open question`: whether sentence-level divergence selection remains beneficial after changing teacher family, tokenizer, domain, verifier, or contamination controls.

## Considerations

Use authorized public or synthetic tasks, a versioned data manifest, explicit retention limits, and an evaluation-only tool boundary. Higher reasoning scores do not justify tool access, private-data access, or consequential authority. Mixed-policy collection should prevent benchmark leakage, record every model revision and rejection reason, and send uncertain cases to human review.

## Strengths

- Clear three-component mechanism connecting coverage, capacity alignment, and train/inference mismatch.
- Complete source bundle supports method, table, figure, and reference cross-checking beyond the abstract.
- Reported table compares compact and larger models across mathematics, code, and scientific reasoning.
- Official releases provide a concrete starting point for a governed replication plan.

## Weaknesses

- Results, ablations, and releases were not independently reproduced in this review.
- No repeated-seed uncertainty, matched-compute controls, or filter/teacher-drift sensitivity is reported in the inspected evidence.
- Public availability does not settle dataset license, contamination, infrastructure, configuration, or checkpoint-version requirements.
- Long-context deployment introduces resource, safety, latency, and monitoring constraints that benchmark scores do not measure.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Paper-exact release manifest | Reproducibility | Bind data, model, code, evaluator, and seeds | Credible reruns | Maintenance burden | Recreate Table 6 from pinned inputs |
| Matched-compute multi-seed ablations | Causal evidence | Separate mechanism benefit from scale and variance | Better attribution | More compute | Paired seed/bootstrap analysis |
| Prefix and filter sensitivity matrix | Mixed-policy boundary | Reveal dependence on repair choices | Safer transfer | Larger experiment grid | Report accuracy, length, calibration, and leakage checks |
| Provenance-aware evaluation harness | Operations | Prevent silent revision or data drift | Auditable comparisons | Engineering overhead | Manifest validation and deterministic smoke tests |

## Potential Implementations

1. **Distillation trace auditor** - Records authorized synthetic/public trace metadata, version information, selection reason, filter result, and split membership; outputs trace receipts and drift warnings; evaluates provenance completeness under a no-private-data policy.
2. **Prefix-repair benchmark harness** - Compares teacher-forced, student-rollout, and repaired-prefix variants on a frozen authorized benchmark; outputs correctness, abstention, length, calibration, and cost summaries; uses no live tools and enforces a spend cap.
3. **Workflow handoff gate** - Combines a trace receipt, calibration check, policy validator, and human escalation route; outputs allow, abstain, or escalate; uses inert allowlisted tools and a rollback path.

## Three Ways to Exercise This Research

1. **Synthetic trace-selection study:** create a small toy corpus, record temperatures and selection receipts, and stop if any retained trace lacks split or revision metadata.
2. **Frozen prefix-repair comparison:** test teacher-forced, student-rollout, and repaired-prefix paths on an authorized fixed benchmark, and stop if matched-compute, leakage, or seed controls fail.
3. **Offline workflow-gate prototype:** route synthetic task state through allow/abstain/escalate decisions, and stop before any live-tool or consequential-system connection.

## Example MVP Product

- `Product name`: Distillation Evidence Gate.
- `Target user`: research engineer or model-evaluation lead.
- `Problem`: reasoning-distillation experiments can lose trace provenance and overstate unreplicated benchmark gains.
- `Core workflow`: import a pinned manifest, record trace decisions, compare bounded variants, validate leakage/version rules, and emit an evidence card for human review.
- `Data requirements`: synthetic or authorized public tasks, versioned model identifiers, split manifest, and no personal or restricted data.
- `Architecture`: local trace recorder, manifest validator, experiment runner, metric analyzer, leakage sentinel, evidence store, and review UI.
- `Success metrics`: provenance coverage, reproducible fixtures, baseline parity, detected drift, useful abstentions, and reviewer agreement.
- `Risk controls`: local-only default, synthetic data, no credentials, no live tools, bounded budget, access control, audit logs, and rollback.
- `Limitations`: it cannot reproduce the paper without the full release environment and does not certify factuality, safety, or deployment fitness.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| WorkflowLLM Enhancing - DEP-E | Related DEP | Training-stage provenance can feed into controlled workflow orchestration. | `.lake-data/DEP-E/DEP-E-20260724-WorkflowLLM Enhancing/workflowllm_enhancing_manuscript.md` |
| MOSS Enabling Code-Driven - DEP-E | Related DEP | Future agentic capability needs safe context and execution boundaries. | `.lake-data/DEP-E/DEP-E-20260724-MOSS Enabling Code-Driven/moss_enabling_code_driven_manuscript.md` |
| Shuffled Autoregression - DEP-E | Related DEP | Cross-domain account of explicit generation schedules and rollout-error control. | `.lake-data/DEP-E/DEP-E-20260724-Shuffled Autoregress/shuffled_autoregression_manuscript.md` |
| DASD official repository | Official implementation | Release documentation, training materials, and configuration context. | https://github.com/D2I-ai/dasd-thinking |
| DASD Hugging Face collection | Official release | Model/data collection and linked paper context. | https://huggingface.co/collections/Alibaba-Apsara/dasd-thinking |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2601.09088 | identity, authors, date, abstract | 2026-07-25 | metadata only |
| R2 | https://arxiv.org/pdf/2601.09088 | primary text, figures, tables | 2026-07-25 | private verified copy withheld |
| R3 | https://arxiv.org/html/2601.09088 | primary text and section structure | 2026-07-25 | private verified copy withheld |
| R4 | https://arxiv.org/e-print/2601.09088 | TeX source structure | 2026-07-25 | private source package withheld |
| R5 | https://doi.org/10.48550/arXiv.2601.09088 | persistent identifier | 2026-07-25 | arXiv DOI |
| R6 | https://github.com/D2I-ai/dasd-thinking | official code/release context | 2026-07-25 | inspected, not executed |
| R7 | https://huggingface.co/collections/Alibaba-Apsara/dasd-thinking | official model/data collection | 2026-07-25 | inspected, no download |
| R8 | `.lake-data/DEP-E/DEP-E-20260724-WorkflowLLM Enhancing/workflowllm_enhancing_manuscript.md` | workflow relationship | 2026-07-25 | repository-relative synthesis |
| R9 | `.lake-data/DEP-E/DEP-E-20260724-MOSS Enabling Code-Driven/moss_enabling_code_driven_manuscript.md` | agent-context relationship | 2026-07-25 | repository-relative synthesis |
| R10 | `.lake-data/DEP-E/DEP-E-20260724-Shuffled Autoregress/shuffled_autoregression_manuscript.md` | autoregressive-control relationship | 2026-07-25 | repository-relative synthesis |

## Appendix

### Replication Checklist

- Pin the paper, code commit, model revision, data revision, and benchmark snapshots.
- Verify licenses, access conditions, and data governance before downloading or processing release assets.
- Recreate filters and temperature schedules with sample counts and rejection reasons.
- Run repeated seeds and matched-compute baselines for each stage and ablation.
- Separate teacher-forced, student-rollout, and mixed-policy partitions to prevent leakage.
- Record hardware, dependency, tokenizer, decoding, evaluator, and stop-budget settings.
- Keep source documents and raw releases out of public DEP commits unless separately authorized.
