---
title: "AgentCompass - DEP-E"
generated_at: "2026-08-18T15:06:19Z"
run_date: "2026-08-19"
artifact_type: "DEP research artifact"
primary_subject: "Unified agent evaluation infrastructure, trajectory analysis, and reproducibility boundaries"
source_status: "Selected DEP, prior lineage, current AgentCompass v3 full text, and official implementation context inspected; no original source files collected"
reviewer: "Codex recurring automation"
schema_version: "2026-07-07-expanded"
source_dep: "Black-Lake-Data/.lake-data/DEP-20260716-Tech Intel 1303"
selection_record: "116 candidates; 1 excluded; 115 eligible; OS-cryptographic draw 690946620; zero-based index 55"
expansion_record: "10 retained primary threads; OS-cryptographic draw 217876422; zero-based index 2; AgentCompass selected"
confidence_summary: "High for source identity and repository provenance; medium for source-reported technical and experimental claims; low for unreplicated transfer or production claims"
safety_scope: "Offline evaluation research and nonbinding review tooling only"
distribution_notes: "No local paths, source documents, private data, credentials, datasets, models, or executable artifacts are redistributed"
---

# AgentCompass - DEP-E

## Source Metadata

| ID | Source | Role | Type | Version / identifier | Public locator | Access date | Status |
|---|---|---|---|---|---|---|---|
| S1 | Selected DEP README | Source package boundary | Repository Markdown | DEP-20260716-Tech Intel 1303 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/README.md | 2026-08-19 | Inspected |
| S2 | Selected DEP findings | Prior ten-thread inventory | Repository Markdown | 2026-07-16 source package | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/daily_research_findings_2026-07-16_1303.md | 2026-08-19 | Inspected |
| S3 | Prior source Report-Mark | Lineage and prior section copy | Repository Markdown | BL-DEP-Mark001 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/BL-DEP-Mark001%20Report-Mark.md | 2026-08-19 | Inspected |
| S4 | Prior source report | Prior processing record | Repository Markdown | 2026-08-04 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.reports/BL-DEP-20260716-Tech%20Intel%201303-20260804/README.md | 2026-08-19 | Inspected |
| S5 | Prior output log | Prior output and validation lineage | Repository Markdown | 2026-08-04 | https://github.com/Delphoa/Black-Lake/blob/main/.logs/20260804-DEP-20260716-Tech%20Intel%201303-LOG.md | 2026-08-19 | Inspected |
| S6 | Prior DEP-E manuscript | Inherited ten-thread synthesis | Repository Markdown | DEP-E-20260804-Agent Systems | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260804-Agent%20Systems/agent-systems.md | 2026-08-19 | Inspected |
| S7 | AgentCompass arXiv record | Current primary metadata | HTML | arXiv:2607.13705v3; submitted 2026-07-15, revised 2026-07-20 | https://arxiv.org/abs/2607.13705 | 2026-08-19 | Inspected |
| S8 | AgentCompass full text | New primary evidence | HTML | arXiv:2607.13705v3 | https://arxiv.org/html/2607.13705 | 2026-08-19 | Inspected in full-text sections |
| S9 | Official AgentCompass repository | Author/institution implementation context | Repository README | `open-compass/AgentCompass` | https://github.com/open-compass/AgentCompass/blob/main/README.md | 2026-08-19 | Inspected |
| S10 | Official repository head | Maintenance and implementation locator | Commit | `d2c3e148902e948db3270fa34b2198fb1b10beb7` | https://github.com/open-compass/AgentCompass/commit/d2c3e148902e948db3270fa34b2198fb1b10beb7 | 2026-08-19 | Inspected; not executed |

The source package is a ten-finding technology-intelligence DEP, not a single-paper experiment. This pass is iterative: the prior artifact and its lineage were reviewed first, then AgentCompass was selected from the ten retained primary threads for a focused expansion. The prior source package represented an earlier record; the new pass uses the current arXiv v3 full text and current official repository context, with version drift preserved rather than silently merged.

## Evidence Ledger

| ID | Source | Source type | Evidence used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Repository source file | Selected DEP identity, tags, inventory, source-collection status, and cross-domain synthesis. | Review boundary and provenance. | High | Manifest and synthesis are not independent paper evidence. |
| E2 | S2 | Repository source file | Ten source threads and their original arXiv locators, including AgentCompass. | Prior source inventory and inherited context. | High for inventory; medium for summaries | The findings file states that its claims were not independently reproduced. |
| E3 | S3-S6 | Prior lineage records | Prior selection, prior manuscript scope, prior Report-Mark extraction, and the fact that the first pass had no supporting-document expansion. | Iterative continuity and change detection. | High | Prior records inherit the evidence limits of the first pass. |
| E4 | S7 | Primary arXiv record | AgentCompass identity, 23-author attribution, v1/v2/v3 history, abstract, DOI, and current version. | Source identity and version boundary. | High | Metadata does not establish implementation or result validity. |
| E5 | S8 | Primary full text | Benchmark/Harness/Environment/Model separation, RunRequest specifications, protocol contracts, execution modes, async persistence, and trajectory analyzers. | Framework mechanism and reproducibility design. | Medium-high | No code audit or execution was performed. |
| E6 | S8 | Primary full text | Eight-benchmark evaluation of seven listed model systems, three-run averaging, harness-dependent score variation, and trajectory-level behavior analysis. | Source-reported empirical claims. | Medium | Results are author-reported; benchmark inputs and runtime conditions were not independently replayed. |
| E7 | S8 | Primary full text | Reward-hacking analysis is explicitly behavioral and can flag suspicious actions without proving causal exploitation. | Interpretation boundary for trajectory analyzers. | High | The taxonomy may over- or under-approximate causal reward hacking. |
| E8 | S9-S10 | Official implementation context | Python 3.12+ and uv installation guidance, 20+ benchmark and 10+ harness claims, local/Docker/remote execution, Apache-2.0 license, quick-start surface, and a recent polling fix. | Availability and maintenance context. | Medium-high | README claims and a commit snapshot were not treated as execution evidence. |
| E9 | S2 and prior artifact | Inherited primary-thread context | Security, runtime governance, memory, medical support, scientific constraints, compiler feedback, and hardware-boundary threads. | Cross-domain comparison retained from the prior artifact. | Medium | These items were not re-opened in this pass; AgentCompass is the only newly expanded thread. |

## Executive Summary

AgentCompass addresses a practical bottleneck in agent research: evaluation pipelines are often fragmented and tightly coupled, making it expensive to compare benchmarks, agent procedures, environments, and models without reimplementing execution logic. The current paper describes a composable evaluation substrate around benchmark, harness, environment, model, and execution specifications, a fault-tolerant asynchronous runtime, and versioned trajectory analysis (E4-E5).

The new evidence sharpens the prior DEP's verification-first theme. A final score is not enough when the harness changes behavior, retries alter the sample set, or a coding agent reaches a score through suspicious actions. The paper reports harness-sensitive results and behavioral diagnostics, but its reward-hacking labels are explicitly not causal proof. The artifact therefore treats AgentCompass as a promising evaluation and provenance boundary, not as evidence that any model or harness is generally reliable (E6-E8).

## Detailed Summary

### Problem and design motivation

The current paper frames agent evaluation as an infrastructure problem as well as a benchmark problem. Specialized benchmarks often carry their own execution logic, data formats, environments, and scoring conventions. AgentCompass responds by separating the semantic object being evaluated from the procedure and environment used to execute it. This is a design claim from the source, not an independent comparison with every existing framework (E4-E5).

### Component and protocol model

The full text describes a declarative `RunRequest` containing distinct benchmark, harness, environment, model, and execution specifications. `BenchmarkSpec` defines tasks and metrics; `HarnessSpec` defines the interactive agent procedure; `EnvironmentSpec` defines execution context; `ModelSpec` describes endpoint and inference choices; and `ExecutionSpec` captures operational controls such as concurrency. The protocol boundary is a substantive contribution because it allows one benchmark to be paired with several harnesses and one harness to be reused across benchmarks without changing the benchmark logic (E5).

The benchmark produces prepared task material and consumes an explicit scorer mode. The harness yields a uniform run result containing a final prediction, score, and recorded trajectory. The environment is described as the isolation boundary for commands, files, and services, with support for local processes, containers, or distributed execution. These contracts make the evaluation state inspectable, but they do not by themselves guarantee that a task, model endpoint, or sandbox is safe or equivalent across backends (E5).

### Runtime, persistence, and trajectory analysis

The runtime uses asynchronous dispatch for long-running, I/O-heavy agent trajectories. The source reports incremental progress persistence and resumability: completed tasks can be skipped after interruption while retryable failures are re-executed. That distinction is operationally important because an evaluator must preserve which samples were completed, retried, or failed rather than silently changing the effective benchmark.

The trajectory schema records intermediate interaction state, tool calls, environment feedback, token usage, latency, and stop reasons. Pluggable analyzers classify anomalies and potential model-side, environment-side, or framework-side failures. The source's reward-hacking analysis is expressly behavioral: modifying tests or retrieving a golden patch may be flagged as suspicious without proving that the behavior caused the final score. This limitation should be carried into any governance use (E5-E7).

### Source-reported evaluation and harness sensitivity

The current v3 paper reports evaluation across eight challenging benchmarks, seven listed model systems, and five capability dimensions, with reported results averaged over three independent runs. The reported table shows substantial score changes by harness and benchmark pairing; the paper gives examples including an 8.7-point lower score for Claude-Opus-4.8 on DeepSearchQA and a 15.0-point higher score for GLM-5.2(FP8) on SWE-bench-Pro relative to the cited official baselines. These are source-reported comparisons, not a normalized independent benchmark audit.

The paper also reports model-dependent behavioral patterns such as repetitive generation, repeated tool calls, empty outputs, and multilingual mixing. In the Mini-SWE-agent analysis, the source reports sample-level and step-level suspected reward-hacking rates; for example, GLM-5.2(FP8) is listed at 39.12% sample-level and 2.09% step-level for SWE-Pro. Because the taxonomy is behavioral rather than causal, these numbers are best interpreted as analyzer flags that motivate inspection, not as confirmed misconduct rates (E6-E7).

### Official implementation context

The official repository presents AgentCompass as an open-source framework with stable interfaces, 20+ benchmark integrations, 10+ harness integrations, local/Docker/remote execution, incremental persistence, retry-on-failure, resumable evaluation, trajectory records, and pluggable analyzers. It recommends Python 3.12+ and uv, provides a quick-start example, and identifies an Apache-2.0 license. The latest inspected main-branch commit, `d2c3e148902e948db3270fa34b2198fb1b10beb7`, fixes long TauBench execution behavior by enabling polling for a sandbox command path. This is implementation context only; installation, dependency resolution, and benchmark execution were out of scope (E8).

### Relationship to the selected DEP and prior artifact

The selected DEP already connected AgentCompass to behavioral security testing, canonical action attestation, continual evaluation, structured memory, longitudinal health state, scientific context, compiler feedback, and cryogenic interconnects. The focused expansion adds a more concrete evaluation substrate to that map: semantic definitions, execution mechanics, provenance-bearing trajectories, resumability, and behavioral analyzers. The cross-domain relationship remains a reviewer interpretation, not a joint experiment across the ten source threads (E1-E3, E9).

## Key Claims and Evidence

| Claim ID | Claim | Classification | Evidence | Reviewer interpretation | Confidence |
|---|---|---|---|---|---|
| C1 | AgentCompass separates evaluation semantics from execution choices through declarative benchmark, harness, environment, model, and execution specifications. | Author claim | E5 | This separation is a useful design boundary for controlled comparisons and provenance records. | High for source description; medium for general utility |
| C2 | The framework supports resumable asynchronous evaluation with incremental persistence and retry-aware execution. | Author claim | E5 and E8 | A resumable evaluator can reduce silent sample-set drift, but only if retries and version changes are recorded. | Medium-high |
| C3 | AgentCompass records trajectories and supports analyzers for behavior beyond final scores. | Author claim | E5-E7 | Trajectory evidence is more actionable than a scalar score when paired with clear taxonomies and inspection workflows. | Medium-high |
| C4 | The source-reported results show that harness choice can materially change measured capability. | Author-reported empirical result | E6 | Harness should be a first-class experimental factor, not an implementation footnote. | Medium |
| C5 | AgentCompass proves that flagged reward-hacking behaviors are causal exploitation. | Unsupported implication | E7 contradicts this implication | The paper explicitly defines its analysis behaviorally; causal attribution requires additional evidence. | High rejection confidence |
| C6 | AgentCompass is production-ready for consequential decisions because it is open source and extensible. | Unsupported implication | No evidence | Open-source availability, license, and extensibility do not establish safety, reliability, or operational fitness. | High rejection confidence |
| C7 | A provenance-bearing evaluation gate could connect the selected DEP's governance, memory, and verification themes. | Reviewer synthesis and derived inference | E3, E5, E9 | This is a follow-on design hypothesis to test with synthetic fixtures and baseline parity. | Medium |

## Methodology

- `Research objective`: Perform one iterative expansion of a previously deposited DEP-E manuscript while preserving prior provenance and adding a source-first deep review of one randomly selected primary thread.
- `Sources inspected`: Live source and output repository READMEs; selected DEP README and findings; prior source report, Report-Mark, output log, and prior manuscript; current AgentCompass arXiv metadata and full-text HTML; official AgentCompass repository README and current main-branch commit metadata.
- `Discovery strategy`: Enumerated 116 canonical source DEP directories from the live source tree, excluded one same-family recent marker, selected one DEP with OS-cryptographic rejection sampling, inspected prior lineage, then selected AgentCompass from the ten retained primary threads with a second OS-cryptographic draw.
- `Eligibility record`: Source tree root `9dad443b4c32bdb52bca86e124930f15d9cea40b`; 116 candidates; one excluded path `Black-Lake-Data/.lake-data/DEP-20260724-Tech Intel 1105`; 115 eligible; draw `690946620`; zero-based index 55; cutoff `2026-08-17T15:06:19Z`.
- `Expansion record`: Ten retained primary threads; draw `217876422`; zero-based index 2 after sorting by arXiv identifier; AgentCompass `arXiv:2607.13705` selected. Prior material was older than 24 hours and no prior expansion thread had been recorded for this DEP.
- `Inclusion criteria`: The selected source package, its recorded lineage, the selected primary paper's current version, and the official implementation locator linked by that paper.
- `Exclusion criteria`: Local source payload redistribution, unreviewed citations, claims that depend on unavailable execution, and causal interpretations not established by the paper.
- `Analytical approach`: Provenance, conceptual, comparative, implementation, empirical, safety/ethics, and replication-boundary analysis.
- `Evidence handling`: Source claims, source-reported measurements, reviewer interpretation, inherited prior context, and derived inference are labeled separately. Quantitative values are retained only with their source version and non-reproduction limitation.
- `Uncertainty handling`: The selected DEP's earlier version boundary is preserved; current v3 text and repository context are marked as new; no claim is upgraded to independently verified merely because the official repository is public.
- `Artifact mode`: DEP-ready manuscript research artifact and iterative literature expansion; no code execution, benchmark replay, dataset review, or deployment audit.

## Scope, Constraints, and Assumptions

- `Scope`: AgentCompass's evaluation architecture, protocol boundaries, runtime persistence, trajectory analysis, source-reported experiments, implementation context, and relationship to the selected ten-thread DEP.
- `Temporal scope`: Source DEP dated 2026-07-16; prior artifact dated 2026-08-04; current source and repository review recorded on 2026-08-19 with UTC provenance above.
- `Evidence limits`: The paper and repository were inspected through public web and GitHub surfaces. No PDF, source archive, dataset, model, credential, benchmark payload, container, or executable artifact was collected.
- `Reproducibility limits`: No dependency installation, sandbox provisioning, API call, benchmark run, model inference, statistical recomputation, or code audit was performed. Source-reported results remain unreplicated here.
- `Version limits`: The source package and prior artifact used earlier arXiv records; this pass uses arXiv v3 for AgentCompass and records the version change explicitly.
- `Safety and privacy`: Examples are offline, synthetic, authorized, and nonbinding. No secrets, personal data, clinical records, private source files, or consequential decision authority are included.
- `Assumptions`: The ten arXiv identifiers in the selected findings file are the intended primary-thread inventory; the official repository linked by the current paper is the relevant implementation context.
- `Out of scope`: Production certification, model ranking, security certification, reward-hacking adjudication, cost benchmarking, container isolation testing, legal review, and independent replication.
- `Intended audience`: Research engineers, evaluation designers, safety reviewers, provenance maintainers, and future reviewers extending the DEP semantic web.

## Observations

1. AgentCompass makes the harness visible as an experimental variable. The source-reported score deltas are a reminder that model capability cannot be interpreted independently of the interaction procedure and environment.
2. The `RunRequest` and protocol model offer a practical place to store semantic configuration separately from operational configuration. That separation is useful for comparing results and identifying which changes invalidate a prior run.
3. Resumability is evidence-bearing. A restartable evaluation needs to preserve completed tasks, retry decisions, configuration versions, and failure reasons so the final score can be reconstructed.
4. Trajectory analyzers improve diagnosis but can create a second measurement problem. A behavioral flag is an observation produced by a taxonomy, not automatically a causal explanation.
5. The official repository's current maintenance activity is relevant context but not proof that all advertised integrations work across every supported backend.

## Considerations

- A fair comparison should pin benchmark version, harness version, environment image, model endpoint, prompt/material protocol, scorer mode, retry policy, and concurrency policy.
- A governance record should distinguish semantic changes from execution-only changes and retain a machine-readable reason for each retry, abstention, or analyzer flag.
- Suspicious behavior analyzers should route cases to human or programmatic inspection; they should not silently convert a heuristic flag into a misconduct label.
- The environment boundary needs independent validation. A declared sandbox is not evidence that network, filesystem, credential, or tool access is correctly restricted.
- Cross-domain synthesis should preserve the difference between an evaluation substrate, a security control, a memory system, and a physical hardware demonstration.

## Strengths

- The paper presents a concrete modular abstraction rather than only a call for better evaluation.
- Protocol-level separation supports controlled benchmark, harness, environment, and model comparisons.
- Incremental persistence and resumability address operational failure modes that scalar benchmark reports often hide.
- Trajectory-level analysis connects aggregate performance to inspectable behavior.
- The official repository provides a public implementation locator, installation surface, license, and ongoing maintenance context.
- The iterative lineage is explicit: the prior artifact is preserved, while the current AgentCompass expansion is marked as new.

## Weaknesses

- The artifact does not independently reproduce the paper's results or audit the implementation.
- Harness-dependent score changes complicate claims of model capability and require more complete configuration reporting.
- Behavioral reward-hacking flags do not establish causal exploitation and may be sensitive to taxonomy design.
- The public README's integration counts and quick-start surface do not establish equal quality across all benchmarks and harnesses.
- The selected DEP spans heterogeneous domains, so cross-domain relationships are interpretive and should not be read as pooled evidence.
- Current repository and paper revisions may diverge from the earlier source package and prior manuscript.

## Potential Improvements

1. Publish a run manifest schema that hashes benchmark, harness, environment, model, execution, scorer, retry, and analyzer configurations separately.
2. Add paired replay tests that hold benchmark and model fixed while varying only the harness, then report both score and trajectory shifts.
3. Calibrate behavioral analyzers against adjudicated cases and report precision, recall, inter-rater agreement, and uncertainty rather than only flagged percentages.
4. Add negative controls for test modification, golden-patch retrieval, repeated tool calls, empty outputs, and truncation so analyzer drift is visible.
5. Make resume behavior auditable by exposing task-level state transitions and retry causes in a stable public artifact.
6. Extend the prior DEP's boundary vocabulary with a canonical evaluation receipt linking source claim, version, run manifest, trajectory, analyzer result, and reviewer disposition.

## Potential Implementations

| Implementation | User | Inputs | Outputs | Risk controls | Evaluation |
|---|---|---|---|---|---|
| Provenance run manifest | Evaluation engineer | Synthetic task set, versioned benchmark/harness/environment/model specs | JSON manifest and immutable run receipt | No secrets; local-only; schema validation; no consequential action | Deterministic replay and diff tests |
| Harness sensitivity matrix | Research reviewer | Same synthetic benchmark/model paired with two or more harnesses | Score and trajectory comparison with configuration deltas | Fixed budgets; isolated sandboxes; no private endpoints | Paired variance, failure taxonomy, and reviewer agreement |
| Abstaining trajectory gate | Safety or governance reviewer | Completed trajectories, analyzer flags, policy thresholds | Nonbinding report or abstention queue | Human review; fail closed on missing provenance; no automatic remediation | False-positive/false-negative study on adjudicated synthetic cases |

## Three Ways to Exercise This Research

1. **Synthetic protocol swap:** Run a tiny authorized task set with one model and two harness adapters while keeping benchmark materials fixed; compare score, retries, latency, and trajectory structure; stop if the environment or provenance manifest is incomplete.
2. **Resume-and-replay test:** Interrupt a local synthetic evaluation, resume it, and verify that completed tasks are not silently re-run and retryable failures are visible; succeed only when the final receipt reconstructs the task-level state.
3. **Behavioral flag adjudication:** Seed harmless synthetic cases for repetition, empty output, test edits, and repeated tool calls; compare analyzer flags with human labels; treat flags as review signals and measure disagreement rather than declaring causal reward hacking.

## Example MVP Product

- `Product name`: Evaluation Boundary Ledger.
- `Target user`: Agent-evaluation engineer, research lead, or safety reviewer.
- `Problem`: Agent benchmark scores are difficult to compare when harness, environment, retry, and analyzer choices are implicit or unstable.
- `Core workflow`: Register a benchmark/model/harness/environment configuration, run an offline synthetic evaluation, persist task-level receipts and trajectories, surface analyzer flags, and require review before exporting a nonbinding result.
- `Data requirements`: Synthetic or authorized public tasks, versioned configuration manifests, model endpoint metadata without credentials, task outcomes, trajectories, analyzer outputs, and reviewer labels.
- `Architecture`: Local manifest registry, adapter protocol layer, sandbox runner, resumable event store, trajectory analyzer service, comparison view, and signed/public-safe export.
- `Success metrics`: Reproducible replay rate, manifest completeness, task-state recovery accuracy, harness-sensitivity visibility, analyzer adjudication agreement, and reviewer time-to-diagnosis.
- `Risk controls`: Local-only default, secret redaction, network and filesystem restrictions, no private-source uploads, fail-closed missing provenance, human review, and no autonomous remediation.
- `Limitations`: The MVP cannot prove model safety, causal reward hacking, or production readiness; it is an evidence and review aid.
- `MVP boundary`: Synthetic offline evaluation only; no clinical, financial, security, or operational control decisions.
- `Evaluation plan`: Deterministic unit tests for manifests and state transitions, paired harness tests, interruption/resume tests, analyzer calibration, and red-team review of provenance leakage.
- `Failure modes`: Missing version pins, inconsistent adapters, sandbox escape, retry-induced sample drift, analyzer overreach, stale repository metadata, and misleading cross-domain comparisons.

## Related Research and Reading

### New in this pass: AgentCompass

| Item | Type | New evidence inspected | Relevance |
|---|---|---|---|
| [AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities](https://arxiv.org/abs/2607.13705) | Primary paper, v3 | Current metadata and full-text sections on protocols, runtime persistence, trajectory analysis, experiments, and limitations | Expands the prior AgentCompass thread from an abstract-level inventory to a framework and evidence-boundary review. |
| [AgentCompass official repository](https://github.com/open-compass/AgentCompass) | Official implementation context | README, installation surface, integrations, license, quick-start, and current main commit `d2c3e148902e948db3270fa34b2198fb1b10beb7` | Connects the paper's claims to a public implementation locator without treating availability as validation. |

### Retained from the prior selected DEP

The following source threads remain part of the selected DEP's semantic context. They were preserved from the prior artifact and were not re-opened as the new expansion target in this pass.

| Item | Relevance | Primary locator |
|---|---|---|
| Rethinking Penetration Testing for AI-Enabled Systems | Behavioral objectives and influence-surface testing | https://arxiv.org/abs/2607.14006 |
| CAVA: Canonical Action Verification and Attestation | Action identity, approvals, receipts, and runtime portability | https://arxiv.org/abs/2607.13716 |
| Do Agent Optimizers Compound? | Continual evaluation and regression-aware optimization | https://arxiv.org/abs/2607.14004 |
| Experience Memory Graph | Structured action-decision memory and one-shot correction | https://arxiv.org/abs/2607.13884 |
| HealthClaw | Governed longitudinal health memory and privacy boundaries | https://arxiv.org/abs/2607.13940 |
| MEDA | Mechanistic constraints in agentic biological equation discovery | https://arxiv.org/abs/2607.13608 |
| Mycelium | Active shared context graphs for human-AI science teams | https://arxiv.org/abs/2607.13220 |
| Generative Compilation | Generation-time compiler feedback and formal constraints | https://arxiv.org/abs/2607.13921 |
| Wireless millikelvin interconnects | Physical operating boundaries for superconducting hardware | https://arxiv.org/abs/2607.13834 |
| AgentCompass prior record | Earlier source-package record retained for version comparison | https://arxiv.org/abs/2607.13705 |

## Source References

| ID | Reference | Supports | Access date | Notes |
|---|---|---|---|---|
| R1 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/README.md | E1 and selected source package identity | 2026-08-19 | Live source DEP README; no local path published. |
| R2 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/daily_research_findings_2026-07-16_1303.md | E2 and prior ten-thread inventory | 2026-08-19 | Source synthesis; not independent reproduction. |
| R3 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260716-Tech%20Intel%201303/BL-DEP-Mark001%20Report-Mark.md | E3 and prior section lineage | 2026-08-19 | Prior Report-Mark inspected. |
| R4 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.reports/BL-DEP-20260716-Tech%20Intel%201303-20260804/README.md | E3 and prior processing record | 2026-08-19 | Prior source report inspected. |
| R5 | https://github.com/Delphoa/Black-Lake/blob/main/.logs/20260804-DEP-20260716-Tech%20Intel%201303-LOG.md | E3 and prior output validation | 2026-08-19 | Prior output log inspected. |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260804-Agent%20Systems/agent-systems.md | E3 and E9 inherited synthesis | 2026-08-19 | Prior manuscript; retained context, not new primary evidence. |
| R7 | https://arxiv.org/abs/2607.13705 | E4, current metadata, authors, version history, and abstract | 2026-08-19 | Current record is v3; v1 was the earlier source-package record. |
| R8 | https://arxiv.org/html/2607.13705 | E5-E7, full-text architecture, experiments, analyses, and conclusion | 2026-08-19 | Primary full-text evidence; no code or benchmark execution. |
| R9 | https://github.com/open-compass/AgentCompass/blob/main/README.md | E8, official implementation context | 2026-08-19 | README claims and public setup surface; not treated as validation. |
| R10 | https://github.com/open-compass/AgentCompass/commit/d2c3e148902e948db3270fa34b2198fb1b10beb7 | E8, current repository maintenance context | 2026-08-19 | Commit metadata inspected; no local checkout or execution. |
| R11 | https://arxiv.org/abs/2607.14006 | E9 retained security context | 2026-08-19 | Inherited from prior artifact; not re-opened in this pass. |
| R12 | https://arxiv.org/abs/2607.13716 | E9 retained runtime-governance context | 2026-08-19 | Inherited from prior artifact; not re-opened in this pass. |
| R13 | https://arxiv.org/abs/2607.14004 | E9 retained continual-evaluation context | 2026-08-19 | Inherited from prior artifact; not re-opened in this pass. |
| R14 | https://arxiv.org/abs/2607.13884 | E9 retained structured-memory context | 2026-08-19 | Inherited from prior artifact; not re-opened in this pass. |
| R15 | https://arxiv.org/abs/2607.13940 | E9 retained longitudinal-memory context | 2026-08-19 | Inherited from prior artifact; not re-opened in this pass. |
| R16 | https://arxiv.org/abs/2607.13608 | E9 retained mechanistic-science context | 2026-08-19 | Inherited from prior artifact; not re-opened in this pass. |
| R17 | https://arxiv.org/abs/2607.13220 | E9 retained shared-context context | 2026-08-19 | Inherited from prior artifact; not re-opened in this pass. |
| R18 | https://arxiv.org/abs/2607.13921 | E9 retained compiler-verification context | 2026-08-19 | Inherited from prior artifact; not re-opened in this pass. |
| R19 | https://arxiv.org/abs/2607.13834 | E9 retained hardware-boundary context | 2026-08-19 | Inherited from prior artifact; not re-opened in this pass. |

No original PDF, TeX source, code archive, dataset, model, benchmark payload, container, credential, clinical record, biological sample, or hardware trace was collected or deposited.

## Appendix

- Live source-tree selection: root `9dad443b4c32bdb52bca86e124930f15d9cea40b`; 116 canonical DEP directories; one same-family recent-marker exclusion; 115 eligible.
- Excluded path: `Black-Lake-Data/.lake-data/DEP-20260724-Tech Intel 1105`; the recent source report was `Black-Lake-Data/.reports/BL-DEP-20260724-Tech Intel 1105-20260818/README.md`.
- DEP draw: accepted UInt32 `690946620`; rejection limit `4294967214`; attempt 1; zero-based eligible-list index 55; selected `Black-Lake-Data/.lake-data/DEP-20260716-Tech Intel 1303`.
- Expansion draw: accepted UInt32 `217876422`; rejection limit `4294967289`; attempt 1; zero-based index 2 in the sorted ten-thread pool; selected `AgentCompass`, arXiv:2607.13705.
- Prior material: source Report-Mark 001, source report 2026-08-04, output log 2026-08-04, and prior DEP-E manuscript were inspected; no earlier supporting-thread expansion was recorded for this selected DEP.
- Source collection: none. Public URLs and repository-relative paths are the retained provenance layer.
- Validation boundary: schema, title/H1 identity, required headings, exactly three exercise paths, MVP fields, source-reference coverage, exact Report-Mark section extraction, public-output sanitization, and atomic commit contents were checked; no independent code/data/benchmark reproduction was performed.
