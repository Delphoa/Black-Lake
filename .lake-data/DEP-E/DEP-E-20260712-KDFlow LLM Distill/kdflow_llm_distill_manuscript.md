---
title: "KDFlow LLM Distill - DEP-E"
generated_at: "2026-07-12 (date-only public marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of KDFlow, a decoupled systems framework for efficient large-language-model knowledge distillation."
source_status: "private archive evidence plus public URLs; no source files deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-12"
temporal_cutoff: "arXiv v2 from 2026-03-24; official repository and DEP context inspected through 2026-07-12"
primary_url: "https://arxiv.org/abs/2603.01875"
stable_identifier: "arXiv:2603.01875v2; DOI:10.48550/arXiv.2603.01875"
confidence_summary: "High for paper identity and reported tables; medium for systems interpretation; low for independent reproducibility because experiments were not rerun."
safety_scope: "public scholarly review, authorized model-training research, and resource-aware implementation planning"
distribution_notes: "Public URLs and repository-relative paths only; private source locations and exact local execution details withheld."
---

# KDFlow LLM Distill - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Reference | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models | Primary paper | arXiv metadata, HTML, and PDF | arXiv:2603.01875v2; DOI:10.48550/arXiv.2603.01875 | https://arxiv.org/abs/2603.01875 ; https://arxiv.org/html/2603.01875 ; https://arxiv.org/pdf/2603.01875 | arXiv license link visible; evidence use only; no source file redistributed. | 2026-07-12 | Full text inspected |
| S2 | KDFlow official implementation | Near-primary implementation | GitHub repository and README | `songmzhang/KDFlow`, current main; README announces v0.2.0 | https://github.com/songmzhang/KDFlow | MIT license visible; repository inspected but not cloned, executed, or redistributed. | 2026-07-12 | README and file surface inspected |
| S3 | Private arXiv archive paper unit | Selection and local provenance | README and PDF | arXiv:2603.01875 | Location withheld | Private evidence; not deposited. | 2026-07-12 | Inspected |
| S4 | Extraction cache public summary | Processing evidence | JSON-derived public-safe record | schema 1.0 | Source URLs in S1 | `pypdf` extraction succeeded; local HTML and source-package text were absent. | 2026-07-12 | Inspected |
| S5 | HSD FTI-FDet - DEP-E | Related DEP entry | Markdown | DEP-E-20260712-HSD FTI-FDet | `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Processed Black Lake artifact; primary basis arXiv:2307.00701v1 and DOI:10.1016/j.aei.2023.102091. | 2026-07-12 | Inspected |
| S6 | BA-LoRA Bias - DEP-E | Related DEP entry | Markdown | DEP-E-20260709-BA-LoRA Bias | `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` | Processed Black Lake artifact; primary basis arXiv:2408.04556. | 2026-07-12 | Inspected |
| S7 | Tech Intel 1104 | Related DEP entry | Markdown | DEP-20260629-Tech Intel 1104, finding 5 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260629-Tech%20Intel%201104/daily_research_findings_2026-06-29_1104.md | Finding cites arXiv:2606.27797v1. | 2026-07-12 | Inspected and primary basis cross-checked |
| S8 | Black Lake README | Repository authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public DEP-E, log, report, naming, attribution, stability, and commit rules. | 2026-07-12 | Live file fetched and read |
| S9 | Black-Lake-Data README | Related repository authority | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public related-repository layout and provenance rules. | 2026-07-12 | Live file fetched and read |

Paper metadata:

- `Full title`: KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models.
- `Authors`: Songming Zhang, Xue Zhang, Tong Zhang, Bojie Hu, Yufeng Chen, Jinan Xu.
- `Affiliations`: Beijing Jiaotong University; Tencent Inc.
- `Dates`: arXiv v1 submitted 2026-03-02; v2 revised 2026-03-24.
- `Subjects`: Computation and Language, Artificial Intelligence, and Machine Learning.
- `Paper extent`: 8 pages, 4 figures, and 3 tables according to the arXiv record.
- `Code`: official MIT-licensed repository available at S2; no code execution was performed.
- `Data`: the paper uses a 100,000-prompt sample from LMSys-Chat-1M and generated Qwen3-14B responses; no dataset or generated response set was collected.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 arXiv metadata | Primary metadata | Title, authors, dates, DOI, subjects, abstract, version history, code locator. | Source identity and stated contribution. | High | Metadata alone does not validate experiments. |
| E2 | S1 sections 1-3 and Figures 1-3 | Primary full text | Teacher/student workload asymmetry, Ray actor design, SGLang/FSDP2 split, hidden-state transfer, shared memory, logit recomputation, off-policy/on-policy flows, cross-tokenizer support. | Architecture and mechanism claims. | High for source reporting | Mathematical equivalence and zero-copy behavior were not independently instrumented. |
| E3 | S1 section 4 and Tables 2-3 | Primary full text | Qwen3 models, dataset construction, eight-H20 setup, AlpacaEval 2.0 results, per-iteration timings, and reported speedups. | Empirical and comparative claims. | High for transcription; low for independent validity | No reruns, variance, energy, utilization traces, or framework-version manifest. |
| E4 | S1 Limitations | Primary full text | FSDP2 versus Megatron-LM boundary and missing asynchronous thousand-GPU optimization. | Disclosed limitations. | High | Limitations are brief and do not cover all evaluation threats. |
| E5 | S2 | Official implementation | Current feature surface, MIT license, installation path, Docker image, v0.2.0 announcement, multi-teacher/chunked-loss support, and SGLang VLM compatibility warning. | Implementation availability and post-paper evolution. | Medium-high | Main branch was not pinned or executed; current features exceed paper v2. |
| E6 | S3, S4 | Private selection and extraction evidence | Archive identity, PDF presence, successful `pypdf` extraction, absent local HTML/source package. | Selection and processing methodology. | High | Private locations intentionally withheld. |
| E7 | S5-S7 | Related DEP artifacts and primary basis | Compact-student quality evidence, output-space distillation/robustness, and topology-aware teacher/student systems partitioning. | Cross-DEP synthesis and implementation relevance. | Medium | Related records provide context, not validation of KDFlow. |
| E8 | S8, S9 | Repository standards | DEP classes, required paths, README inventory, attribution, stability, and commit-message rules. | Artifact compliance. | High | Process evidence only. |

## Executive Summary

KDFlow addresses a systems mismatch in large-language-model knowledge distillation: the teacher performs inference, while the student performs training, yet common frameworks run both through the same training-oriented backend. KDFlow instead uses SGLang for teacher inference, FSDP2 for student optimization, and Ray to coordinate a trainer plus teacher, student, and optional rollout actor groups. Its central communication mechanism transfers final teacher hidden states through shared memory and recomputes full teacher logits beside the student, avoiding direct transmission of a very large vocabulary distribution.

The paper reports a 1.44x-6.36x speedup over the best listed baseline across six Qwen3 teacher/student configurations on one server with eight NVIDIA H20 GPUs. For Qwen3-30B-A3B to Qwen3-1.7B, KDFlow with an FP8 teacher reports 5.8 seconds per iteration versus 36.9 for MS-SWIFT. On AlpacaEval 2.0, KDFlow's distilled Qwen3-1.7B reports 28.23% length-controlled win rate and 28.32% win rate, close to the FSDP and MS-SWIFT distilled baselines and above the undistilled model. These are author-reported, single-environment results rather than reproduced measurements.

The design is technically plausible and directly targets teacher/student workload asymmetry. Confidence is high that the artifact accurately preserves the paper's method and tables, medium that the architecture explains the reported gains, and low for independent reproducibility or broad deployment claims. The paper does not report repeated seeds, confidence intervals, energy, utilization traces, or a component-by-component speedup decomposition. The official repository is active and MIT-licensed, but it has evolved beyond paper v2; current v0.2.0 features and compatibility warnings require their own pinned evaluation.

## Detailed Summary

### Problem Context

White-box knowledge distillation trains a smaller student against richer teacher distributions. In LLM settings, the teacher may be much larger, have a mixture-of-experts architecture, and expose a vocabulary with more than 150,000 entries. A homogeneous training backend such as FSDP or DeepSpeed carries gradient, optimizer, and distributed-state machinery that the forward-only teacher does not need. The paper argues that teacher inference therefore becomes the throughput bottleneck, especially for MoE teachers.

The communication problem is equally important. The paper's example estimates that BF16 logits for 128 sequences of length 4,096 with a 151,936-token vocabulary require about 160 GB. Sending only top-k logits saves bandwidth but changes the loss. KDFlow seeks a path that retains the full distribution while moving substantially less data between processes.

### Architecture and Mechanism

KDFlow uses Ray as its process and data-flow coordinator. A single `Trainer` owns the dataset and training loop. `TeacherActorGroup` places SGLang engines around the teacher. `StudentActorGroup` places the student under FSDP2 for forward, backward, optimizer, and checkpoint work. For on-policy runs, `RolloutActorGroup` uses SGLang servers and a router to generate student responses and accepts updated weights through CUDA interprocess communication.

Rather than transmit full logits, teacher actors return the final hidden states. A hidden width such as 4,096 is much smaller than a vocabulary width such as 151,936. Ray shared memory is used for process transfer, after which each student actor applies the teacher language-model head locally to reconstruct the full logit distribution. The paper describes this as mathematically equivalent to ordinary full-logit distillation while reducing communication. The trade-off is that the student side must hold and execute the teacher head and preserve exact tokenizer, head, precision, and partition compatibility.

Off-policy distillation consumes static prompt-response pairs, obtains teacher hidden states, computes the student loss, and updates the student. On-policy distillation first generates responses with the student rollout actors, sends those responses to the teacher, trains the student, and synchronizes updated student weights back to rollout actors. The paper also exposes Forward KL, Reverse KL, Jensen-Shannon divergence, Total Variation Distance, and DSKDv2-based cross-tokenizer distillation behind extensible APIs.

### Experimental Setup

The authors randomly sample 100,000 prompts from LMSys-Chat-1M and generate responses with Qwen3-14B. Teachers are Qwen3-14B, Qwen3-32B, and Qwen3-30B-A3B; students are Qwen3-4B and Qwen3-1.7B. Baselines include TRL, MS-SWIFT, ROLL, and a pure FSDP teacher/student implementation. All speed experiments run on one server with eight NVIDIA H20 GPUs, global batch size 128, gradient accumulation 8, and maximum length 4,096.

The loss-correctness experiment distills Qwen3-30B-A3B to Qwen3-4B and visually compares KL loss curves against the pure FSDP implementation. The paper reports near-overlap for KDFlow and the baseline and similarly close FP8/BF16 teacher curves. No numerical curve-distance metric or repeated-run uncertainty is provided.

### Downstream Quality Results

For off-policy Qwen3-30B-A3B to Qwen3-1.7B distillation with Forward KL, Table 2 reports:

| Framework | AlpacaEval 2.0 LC win rate | Win rate |
|---|---:|---:|
| Qwen3-1.7B without KD | 26.09% | 21.99% |
| MS-SWIFT | 28.40% | 27.86% |
| FSDP student + teacher | 28.18% | 28.20% |
| KDFlow | 28.23% | 28.32% |

The result supports parity within this one task and setup, but “no quality loss” should be read narrowly: KDFlow trails MS-SWIFT by 0.17 points on length-controlled win rate and leads it by 0.46 points on raw win rate, with no reported uncertainty. The evidence does not establish parity across other tasks, tokenizers, policies, or model families.

### Training Efficiency Results

Table 3 compares KDFlow FP8 teacher timings against the fastest listed baseline, MS-SWIFT:

| Student | Teacher | Best baseline | KDFlow FP8 | Reported speedup |
|---|---|---:|---:|---:|
| Qwen3-4B | Qwen3-14B | 16.6 s/it | 11.5 s/it | 1.44x |
| Qwen3-4B | Qwen3-32B | 24.8 s/it | 13.5 s/it | 1.84x |
| Qwen3-4B | Qwen3-30B-A3B | 43.2 s/it | 11.1 s/it | 3.89x |
| Qwen3-1.7B | Qwen3-14B | 11.5 s/it | 6.7 s/it | 1.72x |
| Qwen3-1.7B | Qwen3-32B | 20.1 s/it | 8.7 s/it | 2.31x |
| Qwen3-1.7B | Qwen3-30B-A3B | 36.9 s/it | 5.8 s/it | 6.36x |

The widening gap for the MoE teacher is consistent with the paper's thesis that an inference engine handles sparse expert execution better than a homogeneous training backend. It is not a causal decomposition: teacher precision, kernels, parallelism, memory placement, framework versions, and scheduling may all contribute.

### Repository Evolution

The official repository currently advertises off-policy, on-policy, cross-tokenizer, multimodal, multi-teacher, and supervised fine-tuning workflows; v0.2.0 adds chunked loss, multi-teacher distillation, EMA teacher updates, and dynamic batching. It also warns that `sglang==0.5.9` has a known VLM compatibility issue and recommends `sglang>=0.5.10` for source installs. These details improve implementation relevance but are later than paper v2 and were not part of the reported experiment evidence.

### Limitations and Boundary Conditions

The paper acknowledges that FSDP2 does not match Megatron-LM's 3D-parallel training efficiency and that KDFlow lacks industrial asynchronous training for thousand-GPU clusters. Reviewer-level limits include a single hardware environment, one model family, no repeated seeds or error bars, no energy or cost accounting, no network/storage stress tests, no ablation isolating each systems optimization, and no reproduction manifest pinning table rows to source versions and commits.

The hidden-state design also has unreported boundaries. The teacher language-model head must be available beside the student, potentially consuming substantial memory. Cross-tokenizer distillation is not the same as same-tokenizer logit reconstruction and requires a mapping algorithm. Precision differences between SGLang inference and training-side recomputation may matter, especially for MoE routing. Finally, user-friendly configuration does not remove the operational need to validate dataset licenses, model licenses, checkpoints, monitoring, and failure recovery.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Separating SGLang teacher inference from FSDP2 student training better matches the two workloads than a homogeneous backend. | Author systems claim | E2 | Architecture directly implements the distinction; comparative causality is not isolated. | Medium-high |
| C2 | Hidden-state transfer plus local language-head recomputation preserves full-logit KD while reducing interprocess communication. | Author mechanism claim | E2 | Algebraically plausible for compatible heads/tokenizers; runtime equivalence and precision were not independently tested. | Medium-high |
| C3 | KDFlow reports 1.44x-6.36x speedup over the best listed baseline across six configurations. | Author empirical claim | E3 | Table transcription is clear; generalization and benchmark fairness remain unverified. | High for reporting; low for reproduction |
| C4 | KDFlow preserves downstream distillation quality. | Author empirical claim | E3 | AlpacaEval results are close across distilled systems, but evidence is one model pair and one benchmark without uncertainty. | Medium |
| C5 | The framework supports off-policy, on-policy, and cross-tokenizer distillation through extensible APIs. | Author capability claim | E2 | Supported by paper design and current repository examples; no execution was performed. | Medium-high |
| C6 | Current main has expanded beyond paper v2 with v0.2.0 multi-teacher and chunked-loss features. | Implementation observation | E5 | Directly visible in the official README; not evidence for paper tables. | High |
| C7 | Workload-aware execution, transfer-quality evaluation, and robustness controls should be reviewed together. | Reviewer interpretation | E7 | Coherent across the three related DEP entries; not experimentally validated as one combined system. | Medium |
| C8 | The paper was eligible on the first random draw. | Process claim | E6, repository and memory scans | No ID, DOI, title, slug, or same-paper 24-hour marker was found. | High |

## Methodology

- `Research objective`: Randomly select one eligible archived arXiv paper, review it source-first, synthesize it with exactly three related DEP entries, and preserve a public-safe DEP-E research artifact.
- `Sources inspected`: Private archive README and PDF; extracted full PDF text; arXiv metadata and HTML; official repository README; live Black Lake and Black-Lake-Data READMEs; and three related DEP documents.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, treated each unique parent directory as one paper unit, selected a uniform zero-based index with PowerShell `Get-Random`, derived the arXiv ID from the PDF/readme, and searched repository artifacts and memory by ID, DOI, normalized title, and slug.
- `Inclusion criteria`: Sources had to identify the paper, expose method/results/limitations, document official implementation, define repository rules, or provide concrete overlap in systems partitioning, distillation quality, or logit-level robustness.
- `Exclusion criteria`: Excluded duplicate paper units, secondary summaries when primary sources were available, unverified reproduction claims, private path disclosure, unlicensed redistribution, and unrelated DEP entries.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, replication, safety/ethics, and provenance review.
- `Evidence handling`: Major claims map to evidence IDs; exact metrics come from inspected tables; author claims, repository evolution, and reviewer inference are labeled separately.
- `Uncertainty handling`: Non-reproduction, single-server scope, missing variance, incomplete benchmark manifests, absent component ablation, and post-paper repository evolution remain explicit.
- `Extraction process`: Preflight identified `pypdf` as the available PDF extractor. Missing-only extraction produced 32,079 bytes of PDF text; no local HTML or source package was available. Public arXiv HTML provided a second full-text check.
- `Version control`: Paper pinned to arXiv:2603.01875v2; official repository treated as current-main implementation context rather than the exact paper artifact; repository policy files fetched from live default branches.
- `Random selection and eligibility`: 75,761 PDF candidates and 75,761 parent-directory paper units; uniform zero-based index 1,455; zero duplicate exclusions and zero reselections.
- `Deduplication`: Scanned Black Lake `.logs`, `.reports`, `.lake-data`, the public pointer index, automation memory, and Black-Lake-Data for arXiv ID, DOI, title, `KDFlow`, and slug markers; no match was found.
- `24-hour validation`: No same-paper marker for the ID, DOI, title, or slug appeared within the preceding 24-hour window.
- `Reviewer stance`: DEP-ready preservation, skeptical paper review, systems analysis, product translation, and bounded replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: KDFlow's paper-v2 architecture, experiment design, reported results, disclosed/reviewer limitations, official repository evolution, and synthesis with exactly three related DEP entries.
- `Temporal boundary`: arXiv v2 revised 2026-03-24; public implementation and repository context inspected through 2026-07-12.
- `Evidence limits`: Experiments, code, models, datasets, Docker images, GPU traces, and checkpoints were not executed or collected.
- `Assumptions`: Extracted table values refer to the stated eight-H20 setup; public arXiv HTML/PDF and official repository are authentic primary or near-primary sources.
- `Constraints`: No private paths, usernames, machine names, local timezone labels, exact local execution timestamps, or unlicensed source files may appear in public artifacts.
- `Out of scope`: Reproducing results, validating third-party dataset/model licenses, benchmarking production clusters, certifying mathematical equivalence across all tokenizers/precisions, or approving deployment.
- `Intended use`: Research review, DEP deposition, replication planning, ML-systems architecture review, and safe product ideation.
- `Audience`: Knowledge-distillation researchers, distributed-training engineers, model-compression teams, infrastructure reviewers, and Black Lake maintainers.
- `Depth target`: Schema-complete manuscript with quantitative preservation and explicit evidence boundaries.
- `Reproducibility boundary`: A reviewer can plan a reproduction from public sources, but cannot validate the paper's speed or quality results from this DEP alone.
- `Operational boundary`: Examples cover authorized training/evaluation systems and do not include unauthorized model, dataset, or cluster access.
- `Data sensitivity`: Public research metadata plus private archive presence; public outputs contain no private location information.

## Observations

- `Observed pattern`: The largest reported gains occur with the MoE teacher, where matching the teacher to an inference-specialized backend is most valuable.
- `Mechanism observation`: Communication is reduced by changing the transferred representation, not by approximating the target distribution; this shifts cost from the network to student-side head storage and computation.
- `Evidence-quality observation`: A close loss curve and one downstream benchmark support compatibility, but not universal quality equivalence.
- `Comparative tension`: KDFlow compares against several frameworks, yet the paper does not publish a full version/kernel/configuration manifest sufficient to separate architecture from tuning.
- `Implementation observation`: The repository's fast evolution is a strength for users and a reproducibility risk for paper-table claims unless releases and commits are pinned.
- `Cross-DEP pattern`: HPC partitioning, HSD FTI-FDet, and BA-LoRA all treat distillation as an end-to-end systems problem spanning placement, transfer, quality, and robustness.
- `Open question`: Can a common benchmark isolate inference backend, transfer representation, precision, scheduler, and algorithm effects while measuring quality, cost, and energy together?

## Considerations

Deployment teams should treat throughput and distillation quality as separate gates. A faster step time is useful only if the student preserves task behavior, calibration, minority performance, safety behavior, and robustness under distribution shift. The HSD related entry reinforces hardware-specific quality/latency evaluation; BA-LoRA reinforces output-space drift and bias checks.

Cluster topology, placement, and failure recovery matter. The related HPC partitioning DEP reports up to 67% higher samples per second by exploiting teacher/student asymmetry through vertical and horizontal split strategies. KDFlow emphasizes backend specialization and representation transfer. A production comparison should test both ideas under node failures, heterogeneous interconnects, variable sequence lengths, and checkpoint/restart pressure.

Data and model governance remain outside the framework abstraction. Operators need lawful dataset access, model-license compatibility, retention controls, checkpoint provenance, secret-safe logging, and approved telemetry. On-policy runs add generated-data feedback loops and stale-weight risks; multi-teacher routing adds domain selection and fairness risks. These require versioned manifests and human-reviewed release criteria.

## Strengths

- Identifies a concrete systems mismatch between teacher inference and student training rather than treating distillation only as a loss function.
- Uses a compact transfer representation while preserving access to the full teacher distribution under compatible conditions.
- Supports off-policy and on-policy workflows in one actor model and exposes extensible loss/algorithm APIs.
- Evaluates dense and MoE teachers across two student sizes with explicit per-iteration timings.
- Includes a downstream quality comparison rather than reporting speed alone.
- Discloses major scale limitations around FSDP2 and asynchronous thousand-GPU training.
- Provides an active, MIT-licensed official implementation with examples and compatibility notes.

## Weaknesses

- Results were not independently reproduced and the paper does not provide a table-to-commit benchmark manifest.
- All reported speed tests use one eight-H20 server and one model family.
- No repeated seeds, confidence intervals, throughput variance, energy, cost, utilization, or communication traces are reported.
- The paper does not isolate the gain from SGLang, hidden-state transfer, FP8, Ray scheduling, or baseline configuration.
- Downstream quality evidence is limited to one teacher/student pair and AlpacaEval 2.0.
- Cross-tokenizer and on-policy capability claims are not accompanied by the same depth of quality and speed evidence as the main off-policy setup.
- Current repository behavior has moved beyond paper v2, increasing version-drift risk.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a table-to-commit reproduction manifest | Reproducibility | Current main evolves rapidly. | Exact paper reconstruction. | Maintenance overhead. | Pin code, containers, models, datasets, seeds, commands, and expected hashes for each row. |
| Factorial systems ablation | Causal performance evidence | Headline speedup combines several changes. | Identifies which mechanisms matter. | Many expensive runs. | Toggle backend, transfer mode, precision, scheduler, and placement while holding data/model constant. |
| Add uncertainty and efficiency telemetry | Statistical and operational rigor | Mean seconds/iteration hides variance and resource cost. | Better capacity decisions. | Instrumentation effort. | Report repeated runs, p50/p95, GPU utilization, communication bytes, energy, and cost per trained token. |
| Broaden quality evaluation | Transfer validity | One benchmark cannot establish parity. | Safer student release. | Evaluation and judge cost. | Add reasoning, coding, safety, calibration, multilingual, and long-context suites with confidence intervals. |
| Test topology-aware partition planners | Distributed scale | Placement strategy changes across clusters. | Better multi-node performance. | Scheduler complexity. | Compare KDFlow placement with analytical vertical/horizontal splits across interconnects. |
| Validate current advanced workflows | Feature evidence | Multi-teacher, chunked loss, multimodal, and EMA features postdate v2. | Aligns claims with current users. | Expanded matrix and compatibility risk. | Pin v0.2.0 and publish dedicated quality/performance reports. |

## Potential Implementations

1. `Distillation Benchmark Harness`
   - `User`: ML-systems research team.
   - `Goal`: Reproduce framework comparisons with pinned dependencies and auditable telemetry.
   - `Core mechanism`: Run matched teacher/student configurations across backends and transfer modes, then emit quality, throughput, memory, communication, and energy ledgers.
   - `Required inputs`: Licensed models/data, approved GPU cluster, pinned containers, benchmark manifest, evaluator suite.
   - `Outputs`: Signed result bundle, Pareto plots, configuration diff, and reproduction status.
   - `Risk controls`: Authorized infrastructure only, secret-safe logs, dataset-license checks, budget caps, and automatic stop on invalid comparisons.
   - `Evaluation`: Match paper rows within predefined tolerance and reproduce results across three runs.
2. `Backend Placement Advisor`
   - `User`: Distributed-training platform engineer.
   - `Goal`: Choose teacher/student placement and parallelism from model shape and cluster topology.
   - `Core mechanism`: Combine KDFlow workload roles with topology-aware vertical/horizontal partition estimates from the related HPC DEP.
   - `Required inputs`: Parameter counts, activation/head sizes, sequence distribution, GPU memory, bandwidth, topology, and concurrency limits.
   - `Outputs`: Candidate plans, predicted bottlenecks, and dry-run schedule.
   - `Risk controls`: No automatic production launch; require capacity checks, rollback plan, and operator approval.
   - `Evaluation`: Prediction error against short controlled pilot runs.
3. `Student Quality Release Gate`
   - `User`: Model release and safety team.
   - `Goal`: Prevent speed gains from masking student regressions.
   - `Core mechanism`: Compare teacher, baseline student, and distilled student on task quality, calibration, drift, robustness, subgroup behavior, latency, and memory.
   - `Required inputs`: Versioned checkpoints, approved benchmark suites, aggregate telemetry, and policy thresholds.
   - `Outputs`: Pass/fail decision with evidence ledger and exception record.
   - `Risk controls`: Human review for high-impact models, privacy-preserving aggregates, and no automatic threshold relaxation.
   - `Evaluation`: Seeded regression injection and historical release backtests.
4. `Hidden-State Transfer Profiler`
   - `User`: KDFlow contributor or performance engineer.
   - `Goal`: Measure when hidden-state transfer is preferable to logits, top-k approximations, or colocated execution.
   - `Core mechanism`: Instrument tensor sizes, shared-memory copies, language-head recomputation, precision error, and end-to-end idle time.
   - `Required inputs`: Small licensed teacher/student pairs, synthetic/public prompts, and isolated test nodes.
   - `Outputs`: Break-even curves and compatibility matrix.
   - `Risk controls`: Bounded test sizes, no user data, resource quotas, and explicit failure cleanup.
   - `Evaluation`: Repeatable profiler traces that explain observed throughput within tolerance.

## Three Ways to Exercise This Research

1. `Paper-table audit`: Objective - verify arithmetic and configuration consistency without training; inputs - paper tables, public README, and a small spreadsheet; method - recompute all six speedup ratios and compare claimed model/configuration coverage; output - discrepancy ledger; success - every ratio and condition is accounted for; stop - if a required table field is unavailable.
2. `Synthetic transfer microbenchmark`: Objective - test the communication trade-off safely; inputs - synthetic hidden/logit tensors shaped like a small public model; method - measure serialized logits, hidden-state shared-memory transfer, and local head multiplication; output - break-even plot; success - stable measurements across three runs; stop - if memory use exceeds the approved cap.
3. `Small-model quality gate`: Objective - test end-to-end equivalence on a bounded open setup; inputs - licensed small teacher/student models and public toy prompts; method - compare homogeneous KD and decoupled hidden-state KD with matched seeds/configs; output - loss, output-divergence, task, latency, and memory report; success - predefined quality tolerance plus measurable throughput gain; stop - on numerical divergence, license uncertainty, or budget overrun.

## Example MVP Product

- `Product name`: DistillFlow Auditor.
- `Target user`: ML platform engineer evaluating an authorized knowledge-distillation job.
- `Problem`: Framework speed claims are hard to compare because placement, precision, versions, datasets, and quality checks drift across runs.
- `Core workflow`: Import a pinned manifest, validate inputs and licenses, execute bounded pilot runs, capture system/quality telemetry, compare against release thresholds, and export an evidence ledger.
- `Data requirements`: Public or properly licensed prompts, aggregate evaluation results, model/configuration hashes, hardware topology, and resource telemetry; no raw user data.
- `Architecture`: Local CLI plus manifest validator, job adapter, telemetry collector, quality evaluator, and static report renderer. Production schedulers remain outside the MVP.
- `Success metrics`: 100% manifest completeness; repeat-run timing coefficient of variation below 5%; paper-row arithmetic verified; quality regression within approved tolerance; zero secret or private-path leakage.
- `Risk controls`: Authorized environments only, allowlisted commands, read-only input mounts, resource/time caps, secret redaction, dataset-license attestation, and human release approval.
- `Limitations`: Does not prove mathematical equivalence, certify generalization, optimize thousand-GPU clusters, or replace application-specific safety testing.
- `MVP boundary`: One node, one small teacher/student pair, off-policy KD, synthetic/public inputs, and report-only recommendations.
- `Deployment model`: Local CLI and static HTML/Markdown report.
- `Evaluation plan`: Unit tests for manifest rules, synthetic tensor tests, a small end-to-end smoke run, and seeded failure scenarios for version mismatch and quality regression.
- `Failure modes`: Misleading comparisons from hidden defaults, stale repository state, evaluator variance, incomplete telemetry, or resource exhaustion.
- `Maintenance plan`: Versioned schemas, dependency advisories, benchmark fixtures, and quarterly threshold review.

Illustrative manifest validator:

```python
REQUIRED = {
    "teacher", "student", "code_commit", "container_digest",
    "dataset_revision", "seed", "precision", "global_batch",
    "max_length", "hardware", "quality_suite",
}

def validate_manifest(manifest):
    missing = sorted(REQUIRED - set(manifest))
    return {"valid": not missing, "missing": missing}
```

Dependencies: Python 3.11 standard library only. This validates metadata, not model safety or benchmark correctness. A production implementation must add schema typing, signature verification, path/secret redaction, and tests.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems | Related primary paper | Directly shares teacher/student workload asymmetry and adds topology-aware split analysis with up to 67% reported throughput gain over TRL. | https://arxiv.org/abs/2606.27797 |
| HSD FTI-FDet - DEP-E | Related processed DEP | Grounds distillation quality, latency, memory, model size, and deployment boundary analysis in a compact vision system. | `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` |
| BA-LoRA Bias - DEP-E | Related processed DEP | Connects KL/token-level distillation and large-vocabulary output computation to drift, diversity, robustness, and LoRA adaptation. | `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` |
| SGLang | Primary systems paper | Teacher inference backend named by KDFlow. | https://arxiv.org/abs/2312.07104 |
| Ray | Primary systems paper | Distributed actor/orchestration substrate used by KDFlow. | https://www.usenix.org/conference/osdi18/presentation/moritz |
| On-Policy Distillation of Language Models | Primary research paper | Methodological basis for learning from student-generated samples. | https://arxiv.org/abs/2306.13649 |
| A Dual-Space Framework for General Knowledge Distillation of Large Language Models | Primary research paper | Cross-tokenizer distillation mechanism referenced by KDFlow. | https://arxiv.org/abs/2504.11426 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| S1 | https://arxiv.org/abs/2603.01875 ; https://arxiv.org/html/2603.01875 ; https://arxiv.org/pdf/2603.01875 ; https://doi.org/10.48550/arXiv.2603.01875 | Identity, method, tables, experiments, limitations, DOI, version history. | 2026-07-12 | Primary paper v2; PDF not redistributed. |
| S2 | https://github.com/songmzhang/KDFlow | Official implementation, license, current features, installation, compatibility notes. | 2026-07-12 | Current main context; no execution. |
| S3 | Private archive paper unit, location withheld | Random selection provenance and local PDF presence. | 2026-07-12 | Private evidence only. |
| S4 | Public-safe extraction summary derived from S1/S3 | Extractor status and source inventory. | 2026-07-12 | `pypdf` succeeded; local HTML/source absent. |
| S5 | `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Quality-efficiency and compact-deployment synthesis. | 2026-07-12 | Related Black Lake DEP. |
| S6 | `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md` | Logit-level distillation, robustness, and LoRA synthesis. | 2026-07-12 | Related Black Lake DEP. |
| S7 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260629-Tech%20Intel%201104/daily_research_findings_2026-06-29_1104.md ; https://arxiv.org/abs/2606.27797 | Topology-aware teacher/student systems asymmetry. | 2026-07-12 | Related Black-Lake-Data DEP and primary basis. |
| S8 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Black Lake DEP/log/report and commit requirements. | 2026-07-12 | Live authority file. |
| S9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository provenance context. | 2026-07-12 | Live authority file. |

## Appendix

### Replication Checklist

- Pin a KDFlow release/commit matching paper v2 rather than current main.
- Record SGLang, PyTorch, CUDA, driver, Ray, transformers, flash-attention, and baseline-framework versions.
- Preserve model revisions, tokenizer files, dataset revision, generated-response provenance, and random seeds.
- Reconstruct six Table 3 teacher/student configurations with global batch 128, gradient accumulation 8, and maximum length 4,096.
- Run at least three repetitions; capture per-step distribution, GPU utilization, communication bytes, memory peaks, energy, and failure/retry events.
- Recreate loss curves with numerical distance statistics rather than visual overlap alone.
- Re-evaluate AlpacaEval 2.0 plus task, calibration, robustness, multilingual, safety, and long-context suites.
- Separate paper-v2 reproduction from current v0.2.0 feature evaluation.

### Public-Safe Selection Record

- Enumeration method: `rg --files -g "*.pdf"`.
- Paper-unit rule: unique PDF parent directory.
- Candidate PDFs: 75,761.
- Candidate paper units: 75,761.
- Uniform zero-based `Get-Random` index: 1,455.
- Duplicate exclusions: 0.
- Reselections: 0.
- Accepted identifier: arXiv:2603.01875v2.
- Dedup scopes: Black Lake logs, reports, DEP entries, pointer index, automation memory, and Black-Lake-Data.
- Same-paper 24-hour markers: none.
