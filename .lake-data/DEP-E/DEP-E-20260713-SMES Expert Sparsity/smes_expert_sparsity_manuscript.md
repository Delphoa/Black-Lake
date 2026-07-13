---
title: "SMES Expert Sparsity - DEP-E"
generated_at: "2026-07-13"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of sparse expert routing for scalable industrial multi-task recommendation."
source_status: "mixed: private PDF inspected, public URLs recorded, no source files redistributed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-13"
temporal_cutoff: "2026-07-13"
primary_url: "https://arxiv.org/abs/2602.09386"
stable_identifier: "arXiv:2602.09386v1; DOI:10.48550/arXiv.2602.09386"
confidence_summary: "High for source identity and transcription; medium for mechanism interpretation; low for independent reproducibility."
safety_scope: "public scholarly review, privacy-preserving recommendation research, and bounded systems evaluation"
distribution_notes: "Date-only public marker and repository-relative paths; private source locations and exact execution details withheld."
---

# SMES Expert Sparsity - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public-Safe Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | SMES arXiv record | Primary metadata | HTML | arXiv:2602.09386v1; DOI:10.48550/arXiv.2602.09386 | https://arxiv.org/abs/2602.09386 | arXiv exposes a license link; redistribution rights were not inferred. | 2026-07-13 | Inspected |
| S2 | SMES full paper | Primary artifact | PDF | v1; private reviewed copy SHA-256 begins `0531F5F1` | https://arxiv.org/pdf/2602.09386 | PDF contains ACM-style permission text and placeholder publication fields; no file redistributed. | 2026-07-13 | Full text inspected |
| S3 | SMES public HTML locator | Primary artifact locator | HTML | arXiv experimental HTML | https://arxiv.org/html/2602.09386 | Public locator only. | 2026-07-13 | Direct retrieval unavailable |
| S4 | ELDR related DEP | Related processed evidence | Markdown | DEP-20260703-Tech Intel 0103, finding 7 | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260703-Tech%20Intel%200103 | Public repository record; used for conceptual context, not SMES validation. | 2026-07-13 | Inspected |
| S5 | KDFlow related DEP | Related processed evidence | Markdown | DEP-E-20260712-KDFlow LLM Distill | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-KDFlow%20LLM%20Distill | Public repository record; used for systems context. | 2026-07-13 | Inspected |
| S6 | llama.cpp runtime related DEP | Related processed evidence | Markdown | DEP-E-20260712-LlamaCpp-Runtime | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime | Public repository record; used for topology/runtime context. | 2026-07-13 | Inspected |
| S7 | Repository authority files | Process evidence | Markdown | Live default-branch READMEs | https://github.com/Delphoa/Black-Lake/blob/main/README.md ; https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public repository policy. | 2026-07-13 | Fetched and inspected |

**Work identity.** *SMES: Towards Scalable Multi-Task Recommendation via Expert Sparsity* is authored by Yukun Zhang, Si Dong, Xu Wang, Bo Chen, Qinglin Jia, Shengzhe Wang, Jinlong Jiao, Runhan Li, Jiaqing Liu, Chaoyi Ma, Ruiming Tang, Guorui Zhou, Han Li, and Kun Gai of Kuaishou Technology Co., Ltd. arXiv classifies it under Information Retrieval and records submission on 2026-02-10. The PDF still contains placeholder conference, ISBN, DOI, and 2018 template text; those fields are not treated as publication evidence. No official code repository was identified from the inspected arXiv record or paper text.

**Source collection.** A pre-existing private archive PDF was inspected and extracted with `pypdf`. The public DEP contains no local path and no `.source/` copy. This is a deliberate redistribution boundary, not a claim that the paper is inaccessible.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, author list, subject, abstract, submission history, DOI, source locators | Identity and stated contribution | High | Abstract-level evidence cannot validate experiments. |
| E2 | S2, sections 1–3.2 | Primary full text | Problem statement, dense/sparse MoE formulation, activation-union bound, progressive routing, deduplicated execution, global load regularization | Mechanism and complexity claims | High for source reporting | Equations and training behavior were not independently implemented. |
| E3 | S2, section 3.3 and Figure 2 | Primary full text | Reindexed grouped GEMM, mapping/reconstruction, profiling-guided workspace pool | Deployment mechanism | High for description | No code, profiler trace, or kernel benchmark is available. |
| E4 | S2, section 4.1 and Table 1 | Primary full text | KuaiRand-1K and Kuaishou experiment descriptions, tasks, baselines, AUC/GAUC metrics | Evaluation setup | Medium-high | Proprietary data, preprocessing, sampling, and full configs are unavailable. |
| E5 | S2, Table 2 and Figure 3 | Primary full text | Offline results, 8% sparsity SMES-L, parameter scaling, reported GAUC/latency trend | Offline and scalability claims | High for transcription; low for reproduction | No seeds, variance, statistical tests, code, or configuration manifest. |
| E6 | S2, Table 3 and Figures 4–5 | Primary full text | Component ablations, hidden/expert sensitivity, task-expert activation visualization | Component and task-allocation claims | Medium-high | Visual/statistical support is incomplete; activation analysis lacks raw distributions. |
| E7 | S2, section 4.7 and conclusion | Primary full text | 3.5% traffic window, online metric lifts, dense-MoE latency comparison, deployment scale | Production claim | Medium-high for reporting | No raw telemetry, confidence intervals, experiment protocol, or independent audit. |
| E8 | Private public-safe extraction summary | Local processing evidence | 75,761 paper units; selected index 48,963; `pypdf` extraction succeeded; local HTML/source absent | Selection, eligibility, and extraction methodology | High | Private locations intentionally withheld. |
| E9 | S4–S6 | Related processed evidence | ELDR routing/locality, KDFlow MoE workload specialization, llama.cpp MoE topology correction | Cross-DEP synthesis | Medium | Related records contextualize but do not validate SMES. |
| E10 | S7 | Repository authority | DEP class, names, inventory, attribution, stability, commit rule | Artifact compliance | High | Process evidence only. |

## Executive Summary

SMES addresses a practical mismatch in multi-task recommender scaling. Dense expert models raise computation and activation memory with every added expert, while tasks with sparse or skewed labels may not benefit from uniform capacity. Naive sparse multi-task routing is not a complete fix: independent top-k routers can select nearly disjoint experts, causing the cross-task union of active experts to approach dense execution, and aggregated traffic can overload a small subset of experts.

The paper proposes progressive expert routing. Each instance first receives a small task-shared expert set selected from pooled task-router probabilities. Every task then receives a limited private set selected outside the shared set. This guarantees shared computation while retaining task-specific capacity and bounds the unique executed-expert union. A global multi-task load-balancing regularizer couples all task routers through aggregate selection frequency and probability mass. Deduplicated execution, a reindexed grouped-GEMM kernel, and profiling-guided workspace allocation are intended to make the sparse model efficient in production.

The authors report consistent gains over listed dense and sparse multi-task baselines on KuaiRand-1K and a proprietary Kuaishou dataset. They further report an average 0.84% GAUC improvement when scaling SMES to 0.6B parameters with a 4 ms latency increase, plus a production A/B test yielding +0.31% watch time and lower latency than a comparable dense MoE. Confidence is high that this artifact accurately preserves the paper's method and reported figures, medium that the proposed mechanisms plausibly contribute to the gains, and low for independent reproducibility or generalization because code, proprietary data, detailed statistics, and a pinned experiment manifest are unavailable.

## Detailed Summary

### Problem Context

Industrial rankers commonly predict many implicit-feedback objectives, such as effective view, long view, click, like, follow, and comment, before combining task outputs into a final score. These tasks differ in frequency, label sparsity, and complexity. The paper's KuaiRand scaling illustration suggests that effective-view quality rises with parameter count while some interaction objectives can flatten or decline. The reviewer interprets this as evidence against a single uniform capacity rule, not proof that larger models inherently harm every sparse task.

Dense multi-gate mixture-of-experts models give every task a router but evaluate every expert. Their expert compute and activation memory therefore grow with the total expert count. Standard sparse top-k routing decouples total parameters from active compute for one task, but multi-task routing introduces a union effect. If task `t` chooses set `K_t`, system cost depends on `U = union(K_t)`, whose size can grow from `k` toward `min(E, T*k)`. A second failure mode arises when several routers concentrate traffic and gradients on the same popular experts.

### Progressive Expert Routing

SMES retains a shared encoder, expert pool, task routers, and task heads. For each instance, its active budget `k` is divided into `k_s` shared experts and `k_a` task-adaptive experts. The shared stage pools normalized task-routing probabilities, optionally weighted by task importance, and takes the top `k_s` experts. Each task then selects `k_a` additional experts from the complement of the shared set. Every task receives exactly `k_s + k_a` experts, while the maximum unique union is bounded by `k_s + T*k_a`.

Expert outputs are deduplicated across tasks. If several tasks select the same expert for one instance, that expert is evaluated once, then its output is reused with task-specific routing weights. This converts shared routing overlap into concrete compute reuse. The design does not guarantee that the upper bound is always small; it makes the shared/private budget an explicit system control.

### Cross-Task Load Regularization

The regularizer measures each expert's realized selection frequency and router probability mass across every task and mini-batch instance. Multiplying and summing those quantities penalizes experts that are both frequently selected and strongly preferred at the aggregate system level. Unlike per-router balancing, it targets hotspots created jointly by multiple objectives. The full loss adds this term with coefficient `beta` to the weighted task loss.

The mechanism is plausible, and Table 3 shows lower GAUC when the regularizer is removed on all displayed tasks. However, the paper does not expose raw load distributions, expert-capacity overflow rates, gradient statistics, or sensitivity to `beta`, so training-stability claims remain only partially auditable.

### Execution and Memory Path

Sparse deduplicated routing creates ragged expert batches. SMES gathers instances by active expert into a packed tensor, records a back-map from instance/expert pairs to packed rows, executes grouped GEMM across expert segments, then reconstructs each task representation using the map and task routing weights. A shared GPU workspace is preallocated in pages, with capacity chosen from offline profiling of active-expert demand.

This design tackles a real boundary: algorithmic sparsity can be erased by dynamic allocation, gather/scatter, synchronization, or poor kernel occupancy. Yet no standalone kernel table isolates gather cost, grouped-GEMM speed, allocator contention, or comparison with standard sparse-MoE runtimes. The paper's end-to-end latency curve therefore supports the combined system, not the individual cause of each speedup.

### Evaluation Setup

The public benchmark is KuaiRand-1K, described as 1,000 users, 4,369,953 items, approximately 11.7 million instances, 92 features, and 12 tasks. The industrial Kuaishou description focuses on 400 million users and 50 billion daily interaction logs, with 21 tasks overall and four core reported tasks: Effective-view, Long-view, Click, and Like. Baselines are MMoE, PLE, MoME, HoME, and RankMixer. AUC and user-weighted GAUC are the offline metrics.

SMES-S is configured near the baseline parameter budget. SMES-L expands expert capacity while retaining an 8% sparsity ratio. The PDF does not provide a reproducibility appendix with train/validation/test dates, feature definitions, optimizer schedule, seeds, negative sampling, early stopping, serving hardware, or precise routing budgets for every row.

### Offline and Ablation Results

Table 2 reports SMES-S as the best shown result across all displayed public and industrial tasks. Relative to the underlined best baseline, the paper reports public-dataset improvements ranging from +0.04% to +1.64% across AUC/GAUC columns and industrial improvements from +0.01% to +0.49%. SMES-L further raises every displayed metric while scaling from approximately 386M to 510M parameters on KuaiRand and from approximately 273M to 633M on the industrial setup.

The scalability figure reports that increasing SMES to 0.6B parameters yields an average GAUC gain of 0.84% with 4 ms added latency, while the dense comparison's latency rises more steeply. Table 3 removes shared experts, adaptive experts, or the regularizer; the full model has the highest shown GAUC on every listed task. Expert-count sensitivity appears stronger than hidden-width sensitivity, and the activation visualization is described as assigning more experts to denser tasks and fewer to sparse tasks.

These results support internal consistency: each proposed component has a displayed ablation, and additional sparse capacity correlates with improved metrics. They do not establish independent causality. Statistical uncertainty, hyperparameter-search parity, raw activation data, and matched kernel/runtime conditions are missing.

### Online Evidence

The paper reports a Kuaishou Single Page A/B test using 3.5% of production traffic from 2025-10-25 through 2025-10-31. Only HoME is said to be replaced with SMES while other components and hyperparameters remain unchanged. Reported lifts are +0.31% user watch time, +0.64% Like, +1.56% Follow, and +2.45% Comment. The authors also report 50% lower inference latency than a dense MoE baseline of comparable capacity and deployment serving more than 400 million daily users.

For a production recommender, these effect sizes may be operationally meaningful. The evidence remains one organization's author report: no sample counts, confidence intervals, guardrail metrics, novelty effects, multiple-testing correction, traffic randomization details, rollback criteria, or long-term holdout are provided.

### Limitations and Boundary Conditions

The paper contains no dedicated limitations section. Reviewer-identified limits include unreleased code, inaccessible proprietary data and infrastructure, one public benchmark, missing statistical detail, no calibration/fairness/tail-user analysis, limited system ablation, no cost or energy accounting, and placeholder venue metadata. The paper's dataset scale statements also require clearer definitions of daily active users, corpus users, items, and interaction windows. Findings should not be generalized to other recommender domains, non-binary objectives, small deployments, or different hardware without testing.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Independent task-wise sparse routing can expand the unique expert union and create cross-task load skew. | Author analytical claim | E2 | The union bound is direct; the severity in real systems is plausible but raw distributions are absent. | Medium-high |
| C2 | Progressive shared/private routing bounds distinct expert execution while retaining task-specific capacity. | Author mechanism claim | E2 | True by construction for stated budgets; downstream quality depends on learned routing. | High for formulation |
| C3 | Global multi-task load regularization improves performance and expert balance. | Author mechanism and empirical claim | E2, E6 | Table 3 supports metric contribution; balanced-utilization evidence is mostly qualitative. | Medium |
| C4 | SMES-S outperforms listed baselines on every displayed public and industrial task. | Author empirical claim | E4, E5 | Table transcription supports the statement; fairness and uncertainty cannot be audited. | High for reporting; low for reproduction |
| C5 | Sparse scaling reaches a 0.84% average GAUC gain at 0.6B parameters with 4 ms added latency. | Author empirical claim | E5 | Figure text directly reports it; hardware and repeated measurements are not specified sufficiently. | Medium-high for reporting |
| C6 | The production A/B test improves watch time and interaction metrics and reduces latency versus dense MoE. | Author production claim | E7 | Experiment window and traffic share are stated; significance procedure and raw telemetry are absent. | Medium |
| C7 | Sparse recommendation should be validated as a routing-to-runtime contract, not only a model architecture. | Reviewer interpretation | E3, E7, E9 | Supported conceptually across SMES and the three related DEP entries. | Medium |
| C8 | The paper was eligible on the first random draw. | Process claim | E8, repository and memory scans | No ID, DOI, title, slug, or 24-hour same-paper marker was found. | High |

## Methodology

- `Research objective`: Preserve and critically assess SMES as a DEP-ready paper report, including its mechanism, evidence, constraints, systems implications, and bounded implementation paths.
- `Sources inspected`: Private full PDF; public arXiv abstract/metadata; live Black Lake and Black-Lake-Data READMEs; exactly three related DEP entries and their recorded primary bases.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`; treated unique PDF parent directories as paper units; used uniform `Get-Random`; inspected nearby metadata; ran local PDF extraction; checked public arXiv metadata; searched repository refs, worktrees, memory, recent paths, and Black-Lake-Data for duplicate markers; searched DEP content for concrete conceptual overlap.
- `Inclusion criteria`: Evidence had to identify the paper, expose method/results, define repository rules, or provide direct overlap in expert routing, sparse inference, or MoE runtime correctness.
- `Exclusion criteria`: Abstract-only quantitative inference, generic arXiv recommender widgets, uninspected citations, unsupported code/reproducibility claims, duplicate deposits, private path disclosure, and unlicensed source redistribution.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, replication, privacy/safety, and provenance review.
- `Evidence handling`: Major claims map to evidence IDs; author claims, direct measurements, process evidence, and reviewer interpretations are labeled separately.
- `Uncertainty handling`: Missing code/data, proprietary infrastructure, unavailable statistical details, inaccessible public HTML during the run, placeholder metadata, and non-reproduction remain explicit.
- `Extraction process`: Preflight found `pypdf` available and `pdftotext` unavailable. Missing-only extraction produced full PDF text; no local HTML or source package was present.
- `Version control`: Paper pinned to arXiv:2602.09386v1. Related repository artifacts were read from live default branches.
- `Claim selection`: Central routing, regularization, runtime, offline, ablation, scalability, and online claims were prioritized; exact figures were taken from inspected paper text and tables.
- `Cross-checking`: Abstract figures were checked against section 4.7; Table 2 parameter/result claims were checked against surrounding text; related DEP descriptions were checked against their recorded primary bases.
- `Safety handling`: Examples use synthetic aggregate routing data, exclude user-level behavior, and make no production recommendation.
- `Reviewer stance`: Source-preserving summary, critique, systems synthesis, product translation, and replication planning.
- `Random selection and eligibility`: 75,761 PDFs produced 75,761 unique paper units. Uniform zero-based index 48,963 selected arXiv:2602.09386. The first draw was accepted; duplicate exclusions and reselections were both zero.
- `Deduplication`: Searched arXiv ID, arXiv DOI, normalized title, `SMES`, and `SMES-Expert-Sparsity` across Black Lake artifacts, available refs/worktrees, recent 24-hour paths, automation memory, and Black-Lake-Data. No match was found.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2602.09386v1, its inspected PDF/metadata, and three concrete related DEP records.
- `Temporal boundary`: Evidence available through 2026-07-13.
- `Evidence limits`: No official code, industrial dataset, production telemetry, raw routing distributions, public experiment manifest, or independent reproduction was available. Public arXiv HTML could not be directly retrieved during this run.
- `Assumptions`: Extracted equations and tables faithfully represent the PDF; arXiv metadata identifies the intended v1 paper; repository default branches represent current public records.
- `Constraints`: No private paths, user data, exact execution timestamps, local timezone labels, or source files are published. Redistribution permission was not assumed.
- `Out of scope`: Reproducing the model, auditing Kuaishou systems, validating business causality, assessing recommender fairness in production, or recommending deployment.
- `Intended use`: DEP preservation, research review, implementation planning, benchmark design, and follow-on replication.
- `Audience`: Recommender researchers, ML-systems engineers, evaluation leads, and repository reviewers.
- `Depth target`: Full manuscript review with evidence ledger and implementation translation.
- `Reproducibility boundary`: Public KuaiRand experiments may be approximated if code/configuration becomes available; industrial and online results cannot currently be reproduced from inspected evidence.
- `Operational boundary`: Routing and telemetry are discussed conceptually with aggregate synthetic examples only.
- `Data sensitivity`: Public paper metadata plus proprietary user-interaction claims reported only in aggregate.

## Observations

- `Observed pattern`: SMES treats the unique cross-task expert union, not per-router top-k alone, as the serving-cost unit.
- `Technical implication`: Shared routing is simultaneously a representation choice and a compute-deduplication primitive.
- `Technical implication`: A sparse model requires runtime support for ragged execution and bounded temporary memory; parameter sparsity alone is not a latency guarantee.
- `Evidence-quality observation`: The paper combines public offline, proprietary offline, ablation, scaling, activation, and production evidence, but each layer lacks enough artifacts for independent reproduction.
- `Contradiction or tension`: The activation visualization suggests sparse tasks receive fewer experts, while the formal per-task budget is described as fixed; the paper should clarify whether displayed variation reflects distinct activated experts over data, task weights, or another deployment rule.
- `Metadata tension`: The arXiv record is from 2026, while the PDF contains unresolved 2018 conference template fields and a placeholder publisher DOI.
- `Cross-DEP pattern`: ELDR, KDFlow, and llama.cpp show that routing, placement, backend specialization, and topology correctness can each determine whether MoE capacity yields practical efficiency.
- `Open question`: Does the shared/private budget remain optimal when task prevalence, label delay, or business weights drift?
- `Reviewer hypothesis`: A Pareto objective over quality, union size, skew, locality, and tail latency would provide a more auditable system target than GAUC plus average latency alone.

## Considerations

Production recommendation affects users, creators, content exposure, and business objectives. A routing change should therefore be reviewed not only for aggregate watch time but also for calibration, tail-task recall, exposure concentration, subgroup impacts, delayed feedback, and guardrail metrics. Sparse tasks may be precisely the objectives most vulnerable to silent regression.

Monitoring should capture aggregate expert selection, unique-union size, overflow/fallback rate, grouped-GEMM utilization, workspace contention, and per-task quality. Raw user features or identifiers are unnecessary for most of these diagnostics and should not be logged. Load-balancing thresholds must account for legitimate specialization so that equal utilization is not mistaken for optimal behavior.

Serving comparisons need matched hardware, batch/concurrency distributions, feature pipelines, precision, kernels, caching, and traffic mixes. A 50% latency reduction against dense MoE does not isolate the benefit of routing from grouped GEMM, allocator design, tuning, or baseline implementation. Cost, energy, operational complexity, and failure recovery are also missing from the paper.

Governance should require a staged rollout, predeclared primary/guardrail metrics, confidence intervals, multiple-testing control, rollback rules, and longer-term holdouts. The artifact does not provide legal, privacy, or safety approval for using interaction data or deploying personalized ranking changes.

## Strengths

- Identifies multi-task activation union and aggregate expert skew as system-level failure modes rather than applying single-task sparse MoE unchanged.
- Makes the shared/private expert budget explicit and mathematically bounds distinct execution.
- Couples routing with deduplicated execution, a ragged compute kernel, and memory planning.
- Evaluates a public benchmark and a large proprietary setting against dense and sparse multi-task baselines.
- Includes component ablations, parameter-scaling curves, sensitivity analysis, activation visualization, and a production A/B report.
- Reports business metrics together with inference latency, which is more decision-useful than accuracy-only scaling.

## Weaknesses

- No official implementation, pinned configuration manifest, or public reproduction instructions were identified.
- Industrial data, serving stack, and online telemetry are unavailable for audit.
- Offline tables omit repeated seeds, uncertainty, statistical tests, and hyperparameter-search parity.
- Online claims omit sample counts, confidence intervals, randomization details, guardrails, multiple-testing controls, and long-term holdouts.
- System components are not isolated with standalone kernel, allocator, communication, or energy measurements.
- Activation-balance evidence is largely qualitative and does not expose raw utilization or overflow distributions.
- Placeholder conference and DOI text weakens publication-status clarity.
- Fairness, calibration, exposure, robustness, and tail-population effects are not evaluated.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code and a table-to-config manifest | Reproducibility | Current results cannot be independently recreated. | Auditable public baseline and faster follow-up research. | Engineering and licensing work. | Reproduce KuaiRand rows across at least three seeds. |
| Publish full routing/load telemetry | Mechanism validation | GAUC does not prove bounded union or balanced utilization. | Tests whether the proposed mechanism behaves as intended. | Must aggregate safely and avoid user-level logs. | Report union-size, skew, overflow, entropy, and task-coverage distributions. |
| Isolate each systems optimization | Performance attribution | End-to-end latency cannot separate routing from kernels and allocation. | Clear causal speedup decomposition. | Benchmark maintenance and hardware variance. | Factorial ablation of routing, deduplication, grouped GEMM, and workspace pool. |
| Expand public datasets and task regimes | Generalization | One public benchmark is narrow. | Better boundary mapping across sparsity and scale. | Dataset compatibility and tuning cost. | Matched experiments on multiple public multi-task datasets. |
| Add calibration, fairness, and tail analyses | Stakeholder safety | Aggregate engagement can hide subgroup or sparse-task harm. | Safer release decisions and clearer tradeoffs. | Requires carefully governed slice definitions. | Predeclared slices, calibration error, exposure metrics, and worst-slice deltas. |
| Strengthen online experiment reporting | Causal evidence | Significance is asserted without protocol detail. | More credible production claims. | May expose sensitive business practices if not aggregated. | Publish anonymized design, power analysis, intervals, guardrails, and holdout duration. |
| Resolve publication metadata and licensing | Provenance | Placeholder fields create ambiguity. | Cleaner citation and redistribution decisions. | Administrative coordination. | Update arXiv version with final venue/rights metadata. |

## Potential Implementations

1. **Routing Union Audit Harness**
   - `User`: Recommender-model researcher.
   - `Goal`: Determine whether a proposed router actually bounds unique expert execution while preserving task coverage.
   - `Core mechanism`: Replay synthetic or public router scores through naive top-k and shared/private routing; compute union size, load skew, task overlap, and stability under simulated drift.
   - `Required inputs`: Public/synthetic task scores, expert count, shared/private budgets, task weights.
   - `Outputs`: Distribution plots, budget Pareto table, and evidence ledger.
   - `Risk controls`: No user-level records; deterministic seeds; strict size limits; report-only output.
   - `Evaluation`: Known synthetic cases, invariant tests, and repeated drift simulations.
2. **Sparse Serving Profiler**
   - `User`: ML-systems engineer.
   - `Goal`: Measure when model sparsity produces end-to-end latency and memory gains.
   - `Core mechanism`: Benchmark routing, gather/reindex, grouped GEMM, reconstruction, allocation, and queueing separately under controlled expert-union distributions.
   - `Required inputs`: Synthetic tensors, approved hardware, pinned kernels/runtime, bounded concurrency profiles.
   - `Outputs`: Latency decomposition, memory peaks, occupancy, and break-even curves.
   - `Risk controls`: Isolated environment, resource caps, no production traffic, reproducible manifests.
   - `Evaluation`: Three-run variance targets and matched dense/sparse comparisons.
3. **Multi-Task Release Evidence Gate**
   - `User`: Recommendation release and governance team.
   - `Goal`: Prevent aggregate gains from masking task, subgroup, or system regressions.
   - `Core mechanism`: Join offline quality/calibration, routing balance, latency, cost, privacy, and staged online guardrails into a human-reviewed decision record.
   - `Required inputs`: Aggregate approved metrics, versioned model/config identifiers, experiment protocol, rollback thresholds.
   - `Outputs`: Pass/fail/exception record with linked evidence and uncertainty.
   - `Risk controls`: Minimum-cell thresholds, no raw user logs, predeclared metrics, human approval, automatic rollback triggers.
   - `Evaluation`: Historical backtests and seeded regression scenarios.

## Three Ways to Exercise This Research

1. `Synthetic union-bound check`: Objective — verify routing invariants; inputs — small deterministic router-score matrices; steps — implement naive top-k and shared/private selection, sweep `k_s`/`k_a`, and calculate unique unions; output — invariant and Pareto report; success criterion — measured union never exceeds `k_s + T*k_a` and test cases expose naive activation growth; stop condition — any invariant failure or ambiguous implementation.
2. `Public-table audit`: Objective — test arithmetic and evidence completeness without training; inputs — the PDF's Tables 1–3 and Figure 3 annotations; steps — transcribe rows, recompute stated improvements, list missing configuration/statistical fields, and map each claim to a source location; output — discrepancy ledger; success criterion — every reported number used by this artifact is traceable; stop condition — a figure value cannot be recovered reliably.
3. `Bounded runtime microbenchmark`: Objective — estimate when deduplicated sparse execution wins; inputs — synthetic tensors, a small expert pool, pinned hardware/runtime, and approved resource limits; steps — compare dense, independent sparse, and deduplicated sparse paths across union sizes; output — latency/memory break-even curves; success criterion — repeat-run coefficient of variation below 5% and an explained crossover point; stop condition — resource cap, instability, or unmatched configurations.

## Example MVP Product

- `Product name`: ExpertRoute Evidence Lab.
- `Target user`: Recommender and ML-systems team evaluating a multi-task sparse router before a controlled pilot.
- `Problem`: Parameter count and per-task top-k do not reveal actual cross-task expert execution, load hotspots, latency cost, or task regressions.
- `Core workflow`: Import a versioned synthetic/public score bundle; validate schema; run naive and candidate routers; profile union/load behavior; optionally run bounded synthetic kernels; attach offline quality metrics; render a release-readiness evidence report.
- `Data requirements`: Synthetic or public aggregate router scores, expert/task configuration, approved offline metrics, hardware/runtime manifest; no raw user identifiers or features.
- `Architecture`: Local CLI and library for routing simulation, aggregate metrics, optional profiler adapter, static Markdown/HTML renderer, and signed manifest. Production deployment and traffic control remain outside the MVP.
- `Success metrics`: 100% configuration completeness; routing invariant coverage; deterministic simulation; repeat-run timing variation below 5%; zero private-data/path leakage; all recommendations linked to evidence.
- `Risk controls`: Local-only default, allowlisted inputs, schema validation, minimum aggregation thresholds, resource/time caps, redacted logs, and mandatory human review.
- `Limitations`: Does not reproduce Kuaishou results, prove business uplift, certify fairness, or validate production kernels at fleet scale.
- `MVP boundary`: One node, synthetic/public aggregate inputs, three router strategies, report-only output, no production integration.
- `Deployment model`: Local CLI with static evidence bundle.
- `Evaluation plan`: Unit tests for bounds and deduplication, property tests for route sets, golden public-table fixtures, profiler smoke tests, and seeded skew/drift cases.
- `Failure modes`: Incorrect task-score normalization, hidden configuration drift, misleading averages, unstable runtime measurements, or treating synthetic results as production evidence.
- `Maintenance plan`: Versioned schemas, pinned benchmark fixtures, dependency review, and explicit metric-definition changes.

Illustrative bounded routing core:

```python
def progressive_routes(task_rankings, shared, private):
    shared_set = set(task_rankings["pooled"][:shared])
    routes = {}
    for task, ranked in task_rankings.items():
        if task == "pooled":
            continue
        extra = [expert for expert in ranked if expert not in shared_set][:private]
        routes[task] = shared_set | set(extra)
    return routes
```

Dependencies are Python's standard library only for this illustrative function. Production code would need numeric validation, deterministic tie handling, device kernels, privacy review, failure cleanup, and benchmark tests.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| ELDR finding in DEP-20260703-Tech Intel 0103 | Related Black-Lake-Data DEP | Routes disaggregated MoE decode requests using predicted expert locality; complements SMES's within-model routing with serving placement and reported latency evidence. Primary basis recorded as arXiv:2607.00466. | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260703-Tech%20Intel%200103 |
| KDFlow LLM Distill - DEP-E | Related Black Lake DEP | Shows that MoE inference efficiency depends on assigning forward-only expert execution to an inference-specialized backend rather than a uniform training stack. Primary basis recorded as arXiv:2603.01875. | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-KDFlow%20LLM%20Distill |
| llama.cpp Runtime - DEP-E | Related Black Lake DEP | Preserves a topology-sensitive MoE-with-MTP quantization correction, underscoring configuration-specific runtime tests for sparse expert models. | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2602.09386 | Identity, abstract, authors, date, subject, DOI, source locators | 2026-07-13 | Primary metadata. |
| R2 | https://arxiv.org/pdf/2602.09386 | Full method, results, tables, figures, system design, online report | 2026-07-13 | Primary full-text locator; reviewed private copy not redistributed. |
| R3 | https://arxiv.org/html/2602.09386 | Public full-text locator | 2026-07-13 | Direct retrieval unavailable; not used for substantive claims. |
| R4 | https://doi.org/10.48550/arXiv.2602.09386 | Stable arXiv-issued DOI | 2026-07-13 | Identifier only. |
| R5 | Private public-safe extraction summary derived from R1/R2 | Selection, source inventory, extractor status | 2026-07-13 | `pypdf` succeeded; local HTML/source absent; no private location published. |
| R6 | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260703-Tech%20Intel%200103 ; https://arxiv.org/abs/2607.00466 | ELDR expert-routing/locality context | 2026-07-13 | Related DEP and its recorded primary basis. |
| R7 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-KDFlow%20LLM%20Distill ; https://arxiv.org/abs/2603.01875 | MoE inference-backend and throughput context | 2026-07-13 | Related processed DEP and recorded primary basis. |
| R8 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime | MoE topology/runtime validation context | 2026-07-13 | Related processed DEP. |
| R9 | https://github.com/ggml-org/llama.cpp/releases/tag/b9789 ; https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b | Official release and MoE-with-MTP correction basis recorded by R8 | 2026-07-13 | Used only for related-entry context. |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Black Lake paths, DEP classes, README, attribution, stability, commit rules | 2026-07-13 | Live default-branch authority. |
| R11 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository provenance and DEP context | 2026-07-13 | Live default-branch authority. |

## Appendix

### Selection and Deduplication Record

- Candidate enumeration: `rg --files -g "*.pdf"` against the private archive.
- Paper unit: unique PDF parent directory, with nearby metadata treated as part of the unit.
- Candidate units: 75,761.
- Random method: uniform PowerShell `Get-Random` over the sorted unit list.
- Zero-based index: 48,963.
- Selected ID: arXiv:2602.09386.
- Duplicate exclusions: 0.
- Reselections: 0.
- Dedup markers: arXiv ID, arXiv DOI, normalized title, `SMES`, and artifact slug.
- Checked surfaces: Black Lake `.logs`, `.reports`, `.lake-data`, staging pointers, refs/worktrees, recent 24-hour artifact paths, automation memory, and Black-Lake-Data paths/content.
- Result: eligible on first draw; no same-paper marker found.

### Replication Checklist

- Obtain or implement a version-pinned SMES reference with explicit license.
- Freeze KuaiRand revision, preprocessing, feature schema, splits, sampling, and task labels.
- Record encoder, expert architecture, expert count, `k_s`, `k_a`, task weights, regularization coefficient, optimizer, schedule, seeds, batch size, and stopping rule.
- Reproduce all listed baselines with matched search budgets and hardware/runtime settings.
- Run at least three seeds and report confidence intervals for AUC/GAUC differences.
- Capture unique-expert union, selection frequency, probability mass, overflow, entropy, gradient distribution, and per-task calibration.
- Profile routing, gather/reindex, grouped GEMM, reconstruction, allocation, end-to-end latency, memory, utilization, energy, and cost separately.
- Test label-sparsity, task-prevalence, and traffic-distribution shifts.
- Predeclare online primary and guardrail metrics, power analysis, multiple-testing controls, rollback criteria, and long-term holdout.
- Audit privacy, fairness, exposure, and data-governance boundaries before any real-user experiment.
