---
title: "Verifiable State - DEP-E"
generated_at: "2026-08-19"
artifact_type: "DEP research artifact"
primary_subject: "How explicit provenance, active state, temporal evidence boundaries, executable checks, and measured infrastructure shape trustworthy intelligent systems."
source_status: "URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-19"
temporal_cutoff: "2026-08-19"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/34637da0627a9c019cd377177af0f3972d4e41ee/.lake-data/DEP-20260706-Tech%20Intel%200104"
stable_identifier: "DEP-20260706-Tech Intel 0104"
confidence_summary: "Medium-high for source characterization; lower for deployment transfer because no experiment, implementation, dataset, model, or hardware result was independently reproduced."
safety_scope: "defensive research, evaluation, clinical decision support research, and bounded implementation planning"
distribution_notes: "No external source payloads are deposited; public URLs and repository-relative provenance only."
---

# Verifiable State - DEP-E

## Source Metadata

This initial-pass artifact reviews the ten primary papers collected by `Black-Lake-Data/.lake-data/DEP-20260706-Tech Intel 0104`. The selected DEP README and findings file were inspected at source commit `34637da`. Complete arXiv HTML was inspected for every paper. Official implementation, benchmark, or dataset surfaces were inspected where a paper exposed a stable public locator. No source files were collected or redistributed.

| ID | Source | Role | Type | Identifier / Version | URL | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S0 | Selected source DEP | Primary source bundle | Markdown repository entry | Source commit `34637da` | [DEP directory](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/34637da0627a9c019cd377177af0f3972d4e41ee/.lake-data/DEP-20260706-Tech%20Intel%200104) | Repository evidence; no source files copied | 2026-08-19 | README and findings inspected |
| S1 | Safeguarding LLM Agents from Misalignment through Provenance Analysis | Primary paper | arXiv HTML | arXiv:2607.01236v2; ASE 2026 | [Record](https://arxiv.org/abs/2607.01236); [full text](https://arxiv.org/html/2607.01236) | CC BY 4.0 shown by arXiv HTML | 2026-08-19 | Framework, method, benchmarks, statistical analysis, results, validity threats, and limitations inspected |
| S2 | Kara: Sliding-Window KV Cache Compression for Efficient Serving of Reasoning LLMs under Memory Constraints | Primary paper | arXiv HTML | arXiv:2607.01237v2 | [Record](https://arxiv.org/abs/2607.01237); [full text](https://arxiv.org/html/2607.01237) | CC BY 4.0 shown by arXiv HTML | 2026-08-19 | Method, three reasoning benchmarks, NIAH, ablations, serving evaluation, and limitations inspected |
| S3 | What Memory Do GUI Agents Really Need? From Passive Records to Active Task-Driving States | Primary paper | arXiv HTML | arXiv:2606.31612v2 | [Record](https://arxiv.org/abs/2606.31612); [full text](https://arxiv.org/html/2606.31612) | arXiv non-exclusive license shown | 2026-08-19 | ATMem/STR-GRPO method, benchmarks, metrics, results, failure analysis, and appendix inspected |
| S4 | MemSyco-Bench: Benchmarking Sycophancy in Agent Memory | Primary paper and implementation | arXiv HTML; GitHub repository | arXiv:2607.01071v2 | [Record](https://arxiv.org/abs/2607.01071); [full text](https://arxiv.org/html/2607.01071); [repository](https://github.com/XMUDeepLIT/MemSyco-Bench) | Paper CC BY 4.0; repository MIT | 2026-08-19 | Benchmark construction, metrics, experiments, diagnostics, repository data/evaluation layout, and license inspected; code not run |
| S5 | ResearchClawBench: A Benchmark for End-to-End Autonomous Scientific Research | Primary paper and implementation | arXiv HTML; GitHub repository | arXiv:2606.07591v5 | [Record](https://arxiv.org/abs/2606.07591); [full text](https://arxiv.org/html/2606.07591); [repository](https://github.com/InternScience/ResearchClawBench) | Paper arXiv non-exclusive license; repository MIT | 2026-08-19 | Construction, RADS, 40-task evaluation, error analysis, limitations, and current repository surface inspected; no task run |
| S6 | VERITAS: A Multi-Agent Co-Scientist for Verifiable Image-Derived Hypothesis Testing | Primary paper and implementation | arXiv HTML; GitHub repository | arXiv:2604.12144v2 | [Record](https://arxiv.org/abs/2604.12144); [full text](https://arxiv.org/html/2604.12144); [repository](https://github.com/LucZot/veritas) | Paper arXiv non-exclusive license; repository Apache-2.0 | 2026-08-19 | Four-phase method, evidence labels, 64-hypothesis results, ablations, limitations, frozen examples, and repository requirements inspected; no clinical data or code run |
| S7 | MedStreamBench: A Time-Aware Benchmark for Streaming and Proactive Medical Video Understanding | Primary paper and dataset locator | arXiv HTML; dataset page | arXiv:2607.01751v1 | [Record](https://arxiv.org/abs/2607.01751); [full text](https://arxiv.org/html/2607.01751); [dataset](https://huggingface.co/datasets/Venn2024/MedStreamBench) | Paper CC BY-NC-SA 4.0; constituent-dataset terms may vary | 2026-08-19 | Construction, temporal protocol, metrics, baselines, limitations, bias, and public dataset locator inspected; media not downloaded |
| S8 | VeriChat: An Agentic Conversational AI Assistant for Hardware Security Verification | Primary paper | arXiv HTML | arXiv:2607.01668v1 | [Record](https://arxiv.org/abs/2607.01668); [full text](https://arxiv.org/html/2607.01668) | arXiv non-exclusive license shown; IEEE notice in paper | 2026-08-19 | Retrieval/agent method, 150-query benchmark, faithfulness evaluation, and synthetic hardware-verification case inspected; no payload or EDA tool run |
| S9 | Probabilistic Memory for Trustworthy Edge Intelligence | Primary paper and simulator | arXiv HTML; GitHub repository | arXiv:2607.02465v1; DAC 2026 | [Record](https://arxiv.org/abs/2607.02465); [full text](https://arxiv.org/html/2607.02465); [PROMISE repository](https://github.com/CSIRLab/PROMISE) | Paper arXiv non-exclusive license; repository states non-commercial availability | 2026-08-19 | Architecture, simulator validation, application/system estimates, repository scope, and incomplete public-tool notes inspected; no simulation run |
| S10 | Mechanistic Interpretability and Causal Feature Steering of Neural Quantum States via Sparse Autoencoders | Primary paper | arXiv HTML | arXiv:2607.01336v1 | [Record](https://arxiv.org/abs/2607.01336); [full text](https://arxiv.org/html/2607.01336) | CC BY 4.0 shown by arXiv HTML | 2026-08-19 | NQS/SAE method, TFIM and Heisenberg results, feature steering, sampling checks, discussion, and appendices inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E0 | S0 | Source bundle | DEP inventory, ten finding summaries, tags, and original attribution | Review boundary and discovery provenance | High | The bundle summaries were treated as locators, not sufficient evidence for empirical claims |
| E1 | S1 | Primary paper | Three-level misalignment taxonomy; provenance predicates; two-benchmark, 11-model evaluation; intervention and latency analysis | Pre-execution provenance can provide explicit, auditable action-justification tests | High for the reported setup | Only 34 aligned Agent-SafetyBench cases; GPT-5 plan reconstruction; WorkBench does not directly label underspecification |
| E2 | S2 | Primary paper | Sliding-window bidirectional scoring, Token2Chunk, periodic PagedAttention compression, reasoning/serving results, ablations | Selective state retention can preserve useful context and improve constrained serving | High for source-reported benchmarks | Permanent eviction loses information; recomputation costs remain; memory is not strictly bounded; global redundancy remains |
| E3 | S3 | Primary paper | Hierarchical task state, memory-on/off RL, AndroidWorld/MobileWorld/DataScope results, failure taxonomy | Active state can reduce long-horizon scope and progress errors better than passive records | High for reported experiments | DataScope has 96 instances; training used 128 H20 GPUs; wrong termination and step-cap failures remain |
| E4 | S4 | Primary paper and official repo | Five decision-boundary tasks, 1,550 released samples, memory-system comparisons, retrieval/use diagnostics | Memory quality depends on arbitration after retrieval, not retrieval alone | High for benchmark definition; medium for broad transfer | Many scores use LLM judging; systems retain native configurations; caution prompts trade conflict resolution against personalization |
| E5 | S5 | Primary paper and official repo | 40 tasks across 10 domains, RADS rubric, seven agents and seventeen LLMs, 280-run error analysis | End-to-end research agents often produce artifacts while missing protocol, evidence, or scientific core | High for reported evaluation | Mostly dry-lab tasks; final reports are emphasized over intermediate steps; target-paper rubrics cannot validate truly novel conclusions |
| E6 | S6 | Primary paper and official repo | Four verifiable phases, mechanical evidence labels, 64 hypotheses, verdict/evidence metrics, ablations, frozen examples | Executable artifacts and epistemic labels make scientific-agent results more diagnosable | High for the reported benchmark | Two MRI domains, segmentation point estimates, dataset-specific ground truth, and no longitudinal or causal analyses |
| E7 | S7 | Primary paper and dataset locator | 22-dataset integration, 5,419 records, explicit evidence windows, responsiveness/stability metrics, model baselines | Decision timing and abstention are first-class parts of evidence-grounded prediction | High for benchmark description | Heterogeneous labels and weak supervision; incomplete exhaustive review; fixed frame sampling may miss brief events |
| E8 | S8 | Primary paper | Three-agent retrieval/generation pipeline, open-source EDA integration, expert-authored queries, blind faithfulness review | Domain retrieval plus executable verification can ground high-assurance assistance | Medium-high | One synthetic Trojan case is not broad tool validation; several component metrics use GPT-4.1 judges; operational security use requires authorization |
| E9 | S9 | Primary paper and official simulator repo | Device-to-system simulation, layout/SPICE error checks, BNN/PCME/DP estimates, repository scope | Specialized probabilistic memory could reduce sampling/data-movement cost | Medium | Major gains are simulated/estimated, configurations are workload-specific, and the public simulator describes an initial version under development |
| E10 | S10 | Primary paper | SAE features, correlations, intervention curves, energy deviation, effective-sample checks, 1D/2D models | Physically meaningful internal coordinates can be measured and causally probed in NQS | High for reported model systems | Transformer NQS and final-layer residual streams only; fixed-sample importance regime limits steering; no hardware experiment |

## Executive Summary

The ten papers converge on a practical thesis: trustworthy intelligent systems need an explicit, inspectable state between raw context and consequential action. That state takes different forms—provenance relations for tool calls, task-driving memory for GUI work, memory-use boundaries, hidden-paper evidence rubrics, statistical evidence labels, temporal video windows, formal hardware properties, or sparse physical features—but its function is consistent. It records what the system knows, where that knowledge came from, whether it is current and in scope, what action it can justify, and what remains unresolved.

The strongest cross-source evidence is not that one architecture solves trust. It is that failures repeatedly occur when a system collapses distinct states: a parameter without provenance, a completed task item treated as pending, an outdated preference treated as fact, a non-significant clinical result treated as refutation, future video evidence leaked into an earlier decision, or a plausible hardware explanation accepted without executable verification. ProvenanceGuard reports misaligned-trace error reductions from 44.3% to 2.1% on Agent-SafetyBench and from 32.4% to 18.7% on WorkBench, while explicitly warning that its aligned sample is small. ATMem reports 76.6% AndroidWorld success for its 8B model and a 23.3% MobileWorld result, but hard DataScope tasks remain low. MemSyco-Bench shows that retrieving both current evidence and memory can still fail if the agent cannot arbitrate between them.

Scientific and clinical sources reinforce the same boundary. ResearchClawBench's strongest reported autonomous-agent mean is 21.5 against a 50-point reference-level anchor; its 280-run analysis attributes failures mainly to protocol mismatch, evidence mismatch, and missing scientific core. VERITAS reports 81.4% majority-vote verdict accuracy with frontier models and 86.6% independently verifiable statistical outputs, while limiting the claim to two MRI domains and dataset-specific ground truth. MedStreamBench makes the evidence window itself part of the task: its 5,419 QA records test not just correctness but whether models wait, answer, remain stable, or alert at the right time.

Infrastructure changes the cost and fidelity of maintaining this state, but it does not certify decisions. Kara reports near-full reasoning accuracy at aggressive KV retention in its evaluated settings and a 12.75% average throughput improvement in the abstract; its own limitations include irreversible information loss and imprecise memory control. p-MEM reports large simulated instruction, latency, and energy gains for probabilistic workloads, but those estimates depend on modeled hardware and tailored configurations. Neural-quantum-state feature steering supplies an unusually clean causal test—observable changes with less than 0.02% relative energy deviation in reported experiments—yet remains bounded to the sampled/model regimes tested.

Reviewer conclusion: build systems around typed, versioned, and auditable state; require independent validators at action boundaries; preserve abstention and underpowered/unknown states; and treat performance optimization as a support layer rather than evidence of correctness. Confidence is medium-high in this synthesis of the inspected sources and low in any deployment-level generalization because no code, datasets, models, hardware, clinical workflows, or benchmarks were executed in this review.

## Detailed Summary

### Provenance before execution

ProvenanceGuard treats an agent tool call as a justification problem. Tool choice must connect documented capability to a user-relevant subtask; verifiable parameter values must derive from contextual evidence; and an underspecified request must not be resolved into one high-impact interpretation without clarification. Its three-stage pipeline reuses an agent plan, filters environment-changing tools, checks parameter support, and detects interpretation-level ambiguity before execution.

Across Agent-SafetyBench and WorkBench with 11 backbone models, the authors report large average reductions in errors on misaligned traces. The result is narrower than a general safety guarantee: malicious intent is outside the paper's defined misalignment scope, the plan traces were reconstructed with GPT-5, WorkBench task success is not equivalent to full alignment, and the aligned Agent-SafetyBench subset contains only 34 cases. Latency is also material: the paper reports 7.5 seconds per case with a local Qwen-3.5-9B configuration and 2.9 seconds including network delay with Gemini-3.1-flash-lite-preview.

### Memory as controlled execution state

ATMem argues that a retrieved value is not operationally useful unless the agent also knows its workflow role, provenance, constraints, and status. Its hierarchical state tracks app-level workflow progress, task constraints, schema, and item content/status. Supervised trajectories teach construction; STR-GRPO compares paired memory-on and memory-off rollouts and penalizes memory use that adds cost without improving outcomes.

The reported 8B model reaches 76.6% success on AndroidWorld and 23.3% on unseen MobileWorld, above the listed same-scale baselines. DataScope stresses exact scope over 96 cross-app instances derived from 32 task families. Gains in progress and Scope-Aware F1 do not eliminate long-horizon failure: stuck loops dominate the strongest baseline's failure analysis, and ATMem does not fully solve premature completion or step-cap exhaustion. The training scale—128 active Android environments and 128 H20 GPUs—also matters for reproducibility and comparison.

MemSyco-Bench examines the inverse problem: memory can be available and still be harmful. Its five tasks separate objective fact judgment, contextual scope control, memory-evidence conflict, personalized use, and valid selection after updates. The released repository describes 1,550 samples and a common evaluation pipeline. On Qwen3-8B, the paper reports that adding full dialogue to objective fact questions lowers accuracy from 49.12% to 30.62% while raising the measured sycophancy rate from 27.43% to 44.67%. More importantly, some systems retrieve both evidence and conflicting memory yet still answer incorrectly. A generic caution instruction improves some conflict cases but harms valid personalization, while an "Are you sure?" confirmation prompt often reinforces memory-shaped answers. The design implication is typed arbitration, not indiscriminate retrieval or blanket skepticism.

### Evaluation as an evidence-state machine

ResearchClawBench turns 40 real-paper tasks across 10 domains into hidden-target research workspaces. Each task supplies a question, related literature, raw data, an executable environment, and expert-built rubric artifacts while withholding the target paper. Its Reference-Anchored Discovery Score uses 50 as reference-paper-level evidence, not as a claim that scores above 50 establish discovery. Seven autonomous agents and seventeen harnessed LLMs are evaluated; the paper reports 21.5 for the strongest autonomous agent and 20.7 for the strongest individual harnessed LLM, with an LLM frontier mean of 26.5.

The diagnostic value lies in the 280-run error analysis. Failures concentrate in experiment-design mismatch, evidence mismatch, and missing scientific core rather than simple execution failure or inability to write a report. Resource spending shows only a weak relationship with score, suggesting that more iteration does not repair a mis-specified protocol automatically. The benchmark remains mostly dry-lab, scores final artifacts more than intermediate reasoning, and uses target-paper rubrics that cannot independently validate genuinely new conclusions.

VERITAS operationalizes evidence states for image-derived clinical hypotheses. Role-specialized agents move through planning, segmentation, statistical analysis, and interpretation. Executable artifacts—masks, code, plots, statistics, and verdicts—remain available for audit. A deterministic Evidence Classification Operator labels evidence Supported, Refuted, Underpowered, or Invalid from significance, effect direction, power, and a smallest effect size of interest, separately from the agents' Yes/No/Inconclusive verdict.

Across 64 cardiac and glioma MRI hypotheses, the authors report 81.4% majority-vote verdict accuracy for the frontier configuration, 71.2% for locally hosted 8–30B models, and 86.6% verifiability for frontier outputs. The verdict often outperforms the generated statistical evidence, identifying code generation as a bottleneck rather than proving strong scientific reasoning. All image conclusions depend on segmentation quality; the benchmark covers two MRI domains, treats segmentation as a point estimate, and builds ground truth from the tested datasets rather than population-level effects. The repository exposes frozen example runs and an Apache-2.0 implementation, but full execution requires clinical datasets, segmentation checkpoints, compute, and license/privacy controls that were not exercised here.

MedStreamBench makes time part of evidence validity. Its 5,419 records span 22 medical video or image-sequence datasets, including 4,663 single-turn and 756 streaming items that expand into 3,369 round-level jobs. Each query is tied to a bounded visual window. Future streaming tasks require `unanswerable` until sufficient evidence is visible; proactive tasks constrain outputs to `no_alert`, `uncertain`, or `alert` with a reason. Content, responsiveness, and stability measure different aspects of behavior.

The reported baselines reveal that offline recognition does not imply temporally disciplined behavior: Gemini-2.5-Pro leads the displayed overall table at 0.3728, while the listed open and medical models cluster lower. The benchmark's breadth also produces uncertainty. Constituent datasets differ in label granularity, scope, devices, and procedure mix; some records use directory labels, hybrid generation, or weak supervision; not every model-assisted item received exhaustive manual visual review; and one-frame-per-two-second sampling can miss brief events. This makes dataset/domain-level reporting essential.

### Executable assurance and bounded security use

VeriChat combines a query-understanding agent, topic-partitioned hybrid retrieval, a generation agent constrained by retrieved evidence, and an optional tool pipeline using Icarus Verilog, Yosys, and SymbiYosys. The paper reports a 28,000-plus-resource knowledge base, 150 expert-contributed evaluation queries, context recall of 76.40%, context precision of 89.85%, and a human-reviewed faithfulness score of 87.73% on 40 questions.

Its case study uses a synthetic third-party AES component with an intentionally embedded confidentiality fault. The system progresses from syntax and synthesis observations to bounded simulation and formal checking. This demonstrates an evidence ladder, not broad validation of autonomous hardware security. The operational details are security-sensitive, so this artifact preserves only the defensive pattern: authorized input, staged structural checks, explicit properties, independent tool outputs, retry logs, and human review. It does not reproduce triggers, payload logic, or exploit instructions.

### State compression and probabilistic substrates

Kara addresses the KV cache generated during long reasoning. It scores recently generated cache entries using sliding-window bidirectional attention, expands selected entries into flexible chunks, and adapts the method to PagedAttention through periodic compression in KvLLM. On Qwen3-4B at 40% retention, its ablation table reports 90.00 on MATH-500 and 82.50 on AMC23, versus 85.20/72.50 without bidirectional scoring and 88.20/77.50 without Token2Chunk. In a memory-constrained serving setup, KvLLM reports 2,912 and 3,392 tokens/s at the two displayed concurrency settings, compared with vanilla vLLM's 2,633 and 2,943.

These results support selective retention, not lossless memory. Cache entries are permanently evicted, query recomputation adds overhead, the method does not strictly control the final footprint, and local windows leave global redundancy. Accuracy experiments and periodic-serving experiments also use different policies for fairness, so their benefits should not be merged into one number.

p-MEM proposes a hardware abstraction that stores Gaussian distribution parameters and samples through the memory read path. Its simulator extends device/circuit models with analog or digital near-memory randomness. At 65 nm, the paper reports mean relative area-estimation error of about 3.05% against layouts and mean latency/energy errors of 13.87%/14.48% against SPICE-level simulation. Cross-node simulation reaches a reported 1,100 GSa/s/mm² at 22 nm.

For tailored BNN, probabilistic-embedding, and differential-privacy kernels, the paper reports large estimated CPU/GPU reductions in instruction count, latency, and energy—for example, BNN CPU estimates of 562.8× latency and 295.5× energy improvement, compared with 3.45× and 3.53× on the modeled GPU path. These are simulator-backed architecture estimates, not fabricated-chip measurements or end-to-end clinical/privacy guarantees. The public PROMISE repository describes an initial, non-commercial simulator version under development, which weakens present reproducibility claims until exact paper configurations and outputs are independently matched.

### Interpretable physical state

The neural-quantum-state paper trains sparse autoencoders on final-layer transformer residual streams and correlates mean-pooled features with defined physical observables. In a 40-site transverse-field Ising model, targeted rescaling of a top feature moves magnetization or a half-chain correlator monotonically while the reported relative energy deviation stays below 0.02% over the tested range. A single dynamic feature maintains correlation above 0.92 across the reported time interval. In a two-dimensional Heisenberg antiferromagnet, the selected feature correlates with staggered magnetization at magnitude 0.97 and steers it monotonically.

Unlike behavioral interpretability, the outcome variables are mathematically defined observables. Even so, "causal" is local to the model intervention and sampling regime. The steering estimates reuse samples from the original Born distribution and require an admissible range; the analysis covers transformer NQS final-layer activations, not other architectures, layers, real quantum hardware, or general physical discovery.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Explicit provenance and interpretation checks can reduce unsupported tool actions before execution. | Source-supported author claim | E1 | Strong within two benchmarks; not a complete alignment, malicious-agent, or authorization guarantee | High for reported setup |
| C2 | Active task state can improve long-horizon GUI execution relative to passive memory representations. | Source-supported author claim | E3 | Results and metrics fit the mechanism, but training scale and small DataScope scope limit transfer | High for reported setup |
| C3 | Correct retrieval is insufficient when an agent cannot arbitrate among fact, preference, scope, and update time. | Cross-source reviewer interpretation | E3, E4 | Directly supported by retrieval/use diagnostics and state-tracking failures | High |
| C4 | Research-agent quality depends more on protocol and evidence alignment than on producing a complete-looking report. | Source-supported author claim and reviewer synthesis | E5 | The error taxonomy supports this for RCBench; transfer to wet-lab discovery remains untested | High for benchmark, medium broadly |
| C5 | Mechanical evidence labels and executable artifacts improve diagnosability of scientific conclusions. | Source-supported author claim | E6 | VERITAS provides unusually inspectable outputs; segmentation and dataset-specific ground truth remain upstream dependencies | High for reported benchmark |
| C6 | Temporal evidence windows, abstention, responsiveness, and stability should be evaluated separately from final correctness. | Source-supported author claim | E7 | The benchmark design is compelling; weak supervision and heterogeneous source data complicate aggregate interpretation | High |
| C7 | Domain retrieval plus independent executable checks is a safer assurance pattern than language-only guidance. | Reviewer interpretation | E1, E6, E8 | Supported across agent, clinical, and hardware workflows, but no common matched evaluation exists | Medium-high |
| C8 | Selective context retention can improve constrained serving while preserving task performance in evaluated settings. | Source-supported author claim | E2 | Useful infrastructure result; irreversible eviction and policy differences prevent a lossless or universal claim | High for reported setup |
| C9 | Near-memory sampling may sharply reduce probabilistic-compute overhead. | Source-supported author claim | E9 | Architecturally plausible and partially validated at module-model level, but major gains remain simulated estimates | Medium |
| C10 | Sparse NQS features can correlate with and locally steer defined physical observables. | Source-supported author claim | E10 | Strong within tested models and importance-sampling range; not evidence of universal interpretability | High for reported systems |
| C11 | A trustworthy system should preserve typed states such as unsupported, stale, out-of-scope, underpowered, unanswerable, and unverified instead of forcing binary decisions. | Derived reviewer inference | E1, E4, E5, E6, E7, E8 | The vocabulary differs, but the recurring failure mechanism is consistent across domains | Medium-high |

## Methodology

- `Research objective`: Convert the selected ten-item technical-intelligence DEP into a source-grounded, reusable research artifact and identify the most defensible cross-domain systems thesis.
- `Sources inspected`: Both source DEP Markdown files; complete arXiv HTML for all ten papers; canonical arXiv records; official repository surfaces for MemSyco-Bench, ResearchClawBench, VERITAS, and PROMISE; and the MedStreamBench dataset locator.
- `Discovery strategy`: Repository inspection established the bundle and prior-art state. The source DEP URLs located each primary paper. Full-text navigation targeted methods, experiment setup, tables, ablations, validity threats, limitations, and appendices. Paper-linked implementation surfaces were inspected for availability and scope.
- `Inclusion criteria`: Every paper named in the selected DEP was included. Quantitative statements were included only when visible in the inspected paper text or tables. Repository claims were used only for public availability, layout, license, and documented workflow.
- `Exclusion criteria`: Secondary summaries, unverified news, source code not inspected beyond public repository surfaces, unexecuted datasets/models, and inaccessible or unstated artifacts were excluded from empirical support. The source bundle's arXiv listing page was retained as discovery context only.
- `Analytical approach`: Mixed conceptual, empirical, comparative, implementation, safety/ethics, product-research, and replication analysis.
- `Evidence handling`: Each major claim maps to an evidence-ledger item. Source-reported metrics remain labeled as such. Reviewer synthesis is explicitly separated from author claims.
- `Uncertainty handling`: Missing execution, dataset, hardware, and clinical evidence is stated. Cross-domain patterns are treated as design hypotheses, not meta-analytic effects.
- `Extraction process`: HTML sections, rendered tables, repository README surfaces, and source Markdown were inspected directly. No PDF extraction, dataset download, code checkout, or benchmark execution was performed.
- `Version control`: Paper versions are recorded. The selected source DEP is pinned to public commit `34637da`. External repositories were inspected at their public surfaces on the access date and were not commit-pinned.
- `Claim selection`: Central mechanisms, strongest quantitative anchors, disclosed limitations, and implementation consequences were prioritized over exhaustive result reproduction.
- `Cross-checking`: Source-bundle summaries were checked against full papers. Several abstract claims were checked against experiment tables or limitations. No independent numerical recomputation was performed.
- `Safety handling`: Hardware-security material is summarized as a defensive assurance workflow; operational trigger/payload details are intentionally omitted. Clinical implementations remain decision-support research requiring governance and human sign-off.
- `Reviewer stance`: Source-first initial DEP synthesis, critique, implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: Ten research papers spanning agent provenance, memory, autonomous research, clinical evaluation, medical video, hardware verification, LLM serving, probabilistic hardware, and neural quantum-state interpretability.
- `Temporal boundary`: Sources were accessed on 2026-08-19. Claims reflect the paper versions and mutable repository surfaces available that day.
- `Evidence limits`: No code, source package, dataset, model, benchmark payload, GPU job, simulator, EDA workflow, clinical image pipeline, or quantum experiment was executed. External repositories were not commit-pinned.
- `Assumptions`: The source DEP intentionally grouped these papers as one technology-intelligence bundle. Cross-domain comparison is used to extract design principles, not to compare incompatible scores.
- `Constraints`: Public-output sanitization, source-license boundaries, clinical privacy, defensive-only security treatment, and the absence of specialized compute/hardware limit independent validation.
- `Out of scope`: Medical diagnosis, live agent deployment, security testing of third-party targets, fabrication claims, benchmark reruns, wet-lab work, and proof that one architecture generalizes across all domains.
- `Intended use`: Research review, DEP deposition, architecture discussion, evaluation planning, and future replication prioritization.
- `Audience`: Agent-system researchers, evaluation engineers, safety reviewers, research-infrastructure designers, and technical product teams.
- `Depth target`: Manuscript-level bundle review rather than exhaustive replication of every source.
- `Reproducibility boundary`: The public locators and reported setups are reusable; the source-reported results remain unverified by this review.
- `Operational boundary`: Examples are synthetic, local, defensive, or evaluation-only. Human approval remains mandatory for consequential actions.
- `Data sensitivity`: The inspected sources are public. Clinical and user-memory implementation concepts may involve sensitive data and therefore default to local, minimized, access-controlled handling.

## Observations

- `Observed pattern`: Many failures are state-type errors rather than missing-information errors. The system has content but misclassifies it as current, in-scope, sufficient, or action-authorizing.
- `Observed pattern`: The most useful artifacts are not just answers. They are provenance links, task-state entries, rubric traces, masks, code, statistics, temporal windows, formal counterexamples, or measurable feature interventions.
- `Technical implication`: Retrieval and context compression should preserve qualifiers—source, time, scope, status, authority, uncertainty—not only semantic similarity or attention score.
- `Technical implication`: Validators should sit outside the generation model whenever a deterministic or domain tool can test the claim.
- `Contradiction or tension`: More state improves auditability but raises token, latency, privacy, and maintenance cost. Kara and p-MEM address cost at different layers without resolving semantic correctness.
- `Contradiction or tension`: Conservative memory instructions reduce some false influence but can suppress legitimate personalization; a single global caution policy is not enough.
- `Open question`: Which minimal typed-state schema transfers across tool use, memory, research, and streaming decisions without becoming another brittle ontology?
- `Reviewer hypothesis`: A shared state machine with evidence, scope, temporal validity, authority, verification, and confidence fields would allow comparable cross-domain audits even when domain validators differ.

## Considerations

- `Authority`: Provenance can show where a value came from without proving that the user authorized the resulting action. Authorization must remain a separate field and gate.
- `Privacy`: Active memory and clinical evidence trails can preserve sensitive histories. Minimize retention, separate user preference from fact, encrypt storage, record purpose, and support deletion without corrupting audit records.
- `Temporal validity`: Updated memories, streaming evidence, mutable repositories, and changing tool state require versioned timestamps and explicit supersession.
- `Human factors`: Detailed evidence trails can create automation bias. Interfaces should surface missing evidence, failed validators, and disagreement before displaying a polished verdict.
- `Benchmark governance`: LLM judges, hidden target papers, weak labels, and dataset-specific ground truth can each introduce evaluator bias. Report judge versions and stratified scores.
- `Security`: Verification tools must run only on authorized designs in isolated environments. Generated properties and tests require independent review; a passing bounded check is not complete coverage.
- `Clinical use`: Underpowered and invalid are essential states, not nuisances. No benchmark score supports autonomous diagnosis or alert deployment without prospective validation and clinical governance.
- `Compute`: Large training and simulation requirements affect reproducibility and carbon/cost budgets. Compare systems under matched resource envelopes.
- `Maintenance`: Evidence schemas, tool documentation, memory states, datasets, model versions, and hardware assumptions all age. A refresh policy is part of correctness.

## Strengths

- The source bundle spans application, evaluation, and infrastructure layers, making recurring state/evidence failures visible across otherwise unrelated domains.
- ProvenanceGuard, ATMem, MemSyco-Bench, VERITAS, and MedStreamBench define explicit intermediate states rather than relying only on final-answer accuracy.
- ResearchClawBench and VERITAS preserve structured research artifacts that support diagnosis of failure rather than rewarding report fluency alone.
- Several papers expose ablations or negative evidence: Kara isolates scoring/chunk components; ATMem reports unresolved failure modes; VERITAS exposes evidence/verdict gaps; NQS checks energy and effective sample size.
- Official public surfaces exist for four major benchmarks/systems and one dataset locator, improving future replication feasibility.
- The NQS work offers objectively defined observables, an unusually strong setting for testing interpretability interventions.

## Weaknesses

- There is no common task, model, dataset, evaluator, compute budget, or safety definition across the ten sources; the synthesis is conceptual rather than statistical.
- Many results depend on author-built benchmarks, model judges, synthetic tasks, hidden rubrics, or simulation. Independent replication evidence was not inspected.
- Deployment-critical populations are narrow: two MRI domains, a heterogeneous medical-video bundle, 96 DataScope instances, and one synthetic hardware case.
- Availability is uneven. ATMem says code/model will be public; PROMISE describes an initial version under development; external repositories were not pinned to commits.
- Efficiency and trust are sometimes adjacent but not causally linked. Faster sampling or compressed KV state does not show safer decisions.
- The review did not inspect PDFs visually, execute code, audit licenses across all transitive dependencies, download datasets, or verify reported tables numerically.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add a typed evidence-state schema | Agent/runtime design | Sources repeatedly distinguish current, stale, scoped, underpowered, unanswerable, and verified states | Fewer category errors and better audit logs | Schema complexity and migration burden | Cross-domain synthetic tasks with field ablations |
| Separate provenance, authority, and verification | Tool guardrails | Origin does not equal permission or truth | Prevents justified-but-unauthorized and sourced-but-false actions | More blocking/clarification | Measure unsafe actions, task success, and user confirmation burden |
| Preserve qualifiers during memory compression | Context systems | Semantic retention alone can discard scope/time/status | Safer long-context and compressed-cache behavior | Larger cache and slower selection | Qualifier-loss benchmarks under matched budgets |
| Evaluate intermediate steps | Research agents | Final reports hide protocol drift | Earlier error localization and repair | Instrumentation and storage cost | Step-level rubrics plus final-outcome correlation |
| Propagate upstream uncertainty | Clinical pipelines | Segmentation point estimates contaminate statistics | Better calibrated Underpowered/Invalid states | More compute and statistical complexity | Bootstrap/ensemble segmentation with coverage tests |
| Use event-aware medical sampling | Streaming video | Fixed two-second sampling can miss brief evidence | More faithful responsiveness measurements | Higher inference cost | Compare uniform and event-triggered protocols by domain |
| Pin executable artifacts | Reproducibility | Mutable repos weaken evidence traceability | Stable reruns and table-to-artifact mapping | Maintenance overhead | Fresh-environment replay from manifest and hashes |
| Validate p-MEM on fabricated or measured hardware | Probabilistic computing | Large improvements are simulator estimates | Establishes real area/latency/energy behavior | High fabrication/equipment cost | Pre-registered silicon or FPGA/ASIC proxy comparison |
| Expand NQS probes across layers and architectures | Interpretability | Current evidence is final-layer transformer-specific | Tests generality and failure detection | Training/sampling cost | Layer/architecture sweeps with preregistered observables |

## Potential Implementations

1. **Evidence-state gateway.** `User`: agent-platform and safety teams. `Goal`: prevent consequential tool calls without adequate origin, scope, authority, and verification. `Core mechanism`: transform candidate actions into typed evidence records; run provenance and policy checks; route ambiguity to clarification; record validator outputs. `Required inputs`: user request, tool schema, action plan, execution history, policy, risk class. `Outputs`: allow, deny, clarify, or human-approval decision with trace. `Risk controls`: least privilege, immutable audit records, privacy minimization, no model-only override. `Evaluation`: matched agent tasks with intentional underspecification, stale memory, and ungrounded parameters.
2. **Research evidence workbench.** `User`: computational researchers and reviewers. `Goal`: keep protocol, evidence, code, outputs, and conclusions aligned. `Core mechanism`: versioned research state with step rubrics, executable checks, evidence labels, and explicit missing-core alerts. `Required inputs`: public/synthetic data, literature, analysis plan, code, metrics. `Outputs`: artifact graph, reproducible report, deviations, and uncertainty states. `Risk controls`: sandboxed execution, license checks, human sign-off, no autonomous clinical/scientific publication. `Evaluation`: hidden-paper tasks plus independent review of intermediate artifacts.
3. **Temporal clinical evaluation harness.** `User`: medical-AI research teams. `Goal`: test when models answer, abstain, or alert. `Core mechanism`: evidence-windowed streams, event-aware sampling, content/responsiveness/stability scoring, and underpowered/invalid states. `Required inputs`: properly governed datasets, timestamped labels, model predictions. `Outputs`: stratified timing and safety reports. `Risk controls`: de-identification, access control, no clinical deployment, domain-specific expert review. `Evaluation`: retrospective benchmark plus prospective silent-mode validation.
4. **State-aware serving profiler.** `User`: LLM infrastructure teams. `Goal`: reduce KV and probabilistic-sampling costs without silently losing qualifiers or calibration. `Core mechanism`: tag high-value context spans, compare compression schedules, and profile probabilistic kernels against deterministic baselines. `Required inputs`: synthetic reasoning traces, cache telemetry, model outputs, hardware counters/simulator data. `Outputs`: accuracy/qualifier-loss/latency/energy trade-off curves. `Risk controls`: no private prompt retention, fixed denominators, separate simulated from measured metrics. `Evaluation`: matched models and workloads with full-cache and software-RNG controls.

## Three Ways to Exercise This Research

1. **Build a typed-state toy agent:** Objective: test whether explicit `source`, `scope`, `status`, `authority`, and `verification` fields reduce errors. Inputs: synthetic calendar/file tools and 30 tasks containing stale facts, ambiguous requests, and completed items. Method: compare a plain agent with a state-gated variant under the same model and tool budget. Output: action trace and error taxonomy. Success criterion: fewer unauthorized, repeated, or stale-state actions without a material task-success drop. Stop condition: any real account, credential, or external side effect enters the test.
2. **Audit one research claim end to end:** Objective: connect one reported metric to exact data, code, configuration, and output. Inputs: one public benchmark/repository, a pinned commit, and a sandbox. Method: reconstruct the artifact graph without changing upstream sources; run only a bounded public example if licenses and compute permit. Output: reproducibility ledger with matched and missing links. Success criterion: every claim component is reproduced or assigned a specific blocker. Stop condition: data rights, privacy, or environment ambiguity prevents safe use.
3. **Run a temporal abstention simulation:** Objective: measure answer timing separately from correctness. Inputs: synthetic event streams with known evidence-onset times and brief events. Method: evaluate full-context, prefix-only, fixed-sampling, and event-aware variants. Output: correctness, early-alert, delay, miss, and stability curves. Success criterion: the chosen protocol improves timing without future leakage. Stop condition: no medical or personal data are introduced.

## Example MVP Product

- `Product name`: StateProof Lab.
- `Target user`: Teams building tool-using agents, research assistants, or decision-support prototypes.
- `Problem`: Context-rich systems often act on information whose source, time, scope, authority, or verification state is unclear.
- `Core workflow`: Import a synthetic or authorized task; normalize evidence into typed records; show current task/memory state; intercept proposed actions; run deterministic validators; require clarification or approval when state is insufficient; export a review bundle.
- `Data requirements`: Synthetic examples by default; optional user-authorized documents and tool schemas; no production secrets, clinical records, or third-party targets in the MVP.
- `Architecture`: Local web UI; append-only evidence ledger; state reducer; policy/provenance gateway; pluggable validators; sandboxed tool simulator; report generator. Models may propose state changes but cannot rewrite the ledger or bypass policy.
- `Success metrics`: Unsupported-action rate, task completion, repeat/stale-action rate, clarification burden, validator coverage, trace completeness, latency, and user ability to identify why an action was blocked.
- `Risk controls`: Local-only default, synthetic tools, least privilege, immutable event IDs, content redaction, explicit authority fields, human approval for simulated high-impact actions, and no clinical/security deployment claims.
- `Limitations`: The MVP does not prove policy completeness, factual truth, model alignment, clinical safety, formal security coverage, or transfer to production tools.
- `MVP boundary`: Text/document and synthetic-tool workflows only; no real email, payments, device control, EDA execution, diagnosis, or live accounts.
- `Deployment model`: Local CLI plus loopback browser interface in a pinned container.
- `Evaluation plan`: Unit tests for state transitions; adversarial synthetic tasks; model/version matrix; blinded trace review; latency and privacy audit; fixed-denominator reporting.
- `Failure modes`: Incorrect state extraction, stale schema, valid evidence without user authority, validator false negatives, excessive blocking, audit-log leakage, or compressed context losing qualifiers.
- `Maintenance plan`: Version schemas and policies; retain migration tests; pin validators; review dependencies monthly; add a regression fixture for every state/authority incident.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| W3C PROV-O | Standard | Formal vocabulary for entities, activities, agents, and provenance relationships underlying traceable action justification | https://www.w3.org/TR/prov-o/ |
| ProvenanceGuard | Primary paper | Pre-execution tool, parameter, and interpretation provenance checks | https://arxiv.org/abs/2607.01236 |
| ATMem | Primary paper | Active task-driving state with explicit provenance, constraints, and execution status | https://arxiv.org/abs/2606.31612 |
| MemSyco-Bench repository | Official benchmark implementation | Released five-task memory-use benchmark, 1,550 samples, baselines, and evaluation code | https://github.com/XMUDeepLIT/MemSyco-Bench |
| ResearchClawBench repository | Official benchmark implementation | Public task/evaluation infrastructure for evidence-grounded autonomous research | https://github.com/InternScience/ResearchClawBench |
| VERITAS repository | Official implementation | Frozen example runs, executable evidence artifacts, and mechanical evidence classification | https://github.com/LucZot/veritas |
| MedStreamBench dataset | Official dataset locator | Time-bounded medical video QA and streaming/proactive evaluation records | https://huggingface.co/datasets/Venn2024/MedStreamBench |
| VeriChat | Primary paper | Retrieval-grounded, tool-integrated defensive hardware verification workflow | https://arxiv.org/abs/2607.01668 |
| PROMISE | Official simulator repository | Public initial simulator surface for probabilistic-memory architecture studies | https://github.com/CSIRLab/PROMISE |
| Mechanistic Interpretability for AI Safety | Primary review | Broader interpretability context cited by the NQS work | https://arxiv.org/abs/2404.14082 |

This is an initial synthesis. No new item is labeled as an iterative expansion because no prior DEP Class artifact, source report, output log, or Report-Mark existed for the selected DEP. The older SAILFISH artifact only cited the DEP's VeriChat finding as related context.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R0 | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/34637da0627a9c019cd377177af0f3972d4e41ee/.lake-data/DEP-20260706-Tech%20Intel%200104 | Selected source bundle, inventory, attribution, and review boundary | 2026-08-19 | Source commit pinned; both Markdown files inspected |
| R1 | https://arxiv.org/abs/2607.01236 and https://arxiv.org/html/2607.01236 | ProvenanceGuard identity, method, evaluation, statistics, validity threats, and limitations | 2026-08-19 | v2; primary paper |
| R2 | https://doi.org/10.1145/3832783.3837535 | ProvenanceGuard ASE 2026 publication identity | 2026-08-19 | DOI exposed by the paper |
| R3 | https://arxiv.org/abs/2607.01237 and https://arxiv.org/html/2607.01237 | Kara/KvLLM method, benchmarks, ablations, serving results, and limitations | 2026-08-19 | v2; primary paper |
| R4 | https://arxiv.org/abs/2606.31612 and https://arxiv.org/html/2606.31612 | ATMem, STR-GRPO, DataScope, training setup, results, and failures | 2026-08-19 | v2; primary paper |
| R5 | https://arxiv.org/abs/2607.01071 and https://arxiv.org/html/2607.01071 | MemSyco-Bench taxonomy, construction, metrics, results, and diagnostics | 2026-08-19 | v2; primary paper |
| R6 | https://github.com/XMUDeepLIT/MemSyco-Bench | Released benchmark structure, sample counts, evaluation workflow, and MIT license | 2026-08-19 | Official repository; not executed |
| R7 | https://arxiv.org/abs/2606.07591 and https://arxiv.org/html/2606.07591 | ResearchClawBench task design, RADS, evaluations, error analysis, and limitations | 2026-08-19 | v5; primary paper |
| R8 | https://github.com/InternScience/ResearchClawBench | Public task/evaluation infrastructure and current project context | 2026-08-19 | Official repository surface; mutable and not executed |
| R9 | https://arxiv.org/abs/2604.12144 and https://arxiv.org/html/2604.12144 | VERITAS phases, evidence labels, hypotheses, results, ablations, and limitations | 2026-08-19 | v2; primary paper |
| R10 | https://github.com/LucZot/veritas | Frozen examples, implementation layout, data/compute requirements, and Apache-2.0 license | 2026-08-19 | Official repository; no data or code run |
| R11 | https://arxiv.org/abs/2607.01751 and https://arxiv.org/html/2607.01751 | MedStreamBench construction, temporal protocol, metrics, results, limitations, and bias | 2026-08-19 | v1; primary paper |
| R12 | https://huggingface.co/datasets/Venn2024/MedStreamBench | Official public dataset locator | 2026-08-19 | Dataset payload not downloaded; constituent terms not audited |
| R13 | https://arxiv.org/abs/2607.01668 and https://arxiv.org/html/2607.01668 | VeriChat method, benchmark, tool integration, and faithfulness results | 2026-08-19 | v1; defensive primary-paper review; operational payload details omitted |
| R14 | https://arxiv.org/abs/2607.02465 and https://arxiv.org/html/2607.02465 | p-MEM architecture, simulator validation, application metrics, and system estimates | 2026-08-19 | v1; primary paper; major system gains are simulated/estimated |
| R15 | https://github.com/CSIRLab/PROMISE | Initial public simulator scope, file layout, and non-commercial availability statement | 2026-08-19 | Official repository; not executed; README marks version under development |
| R16 | https://arxiv.org/abs/2607.01336 and https://arxiv.org/html/2607.01336 | NQS/SAE method, correlations, steering, sampling checks, and discussion | 2026-08-19 | v1; primary paper |
| R17 | https://www.w3.org/TR/prov-o/ | Provenance standard context | 2026-08-19 | Related reading; not evidence for source-reported metrics |
| R18 | https://arxiv.org/abs/2404.14082 | General mechanistic-interpretability review context | 2026-08-19 | Related reading cited by S10; not a primary result source for this synthesis |
| R19 | https://github.com/Delphoa/Black-Lake/blob/main/README.md and https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing, contents, source locality, publication-index, and commit rules | 2026-08-19 | Live repository authority inspected before writing |
| R20 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Source repository layout and reporting context | 2026-08-19 | Live repository authority inspected before writing |

## Appendix

### A. Replication Checklist

- [x] Selected DEP pinned to a public source commit.
- [x] Both source DEP Markdown files inspected.
- [x] Complete arXiv HTML inspected for all ten papers.
- [x] Major quantitative claims tied to source tables or result sections.
- [x] Disclosed limitations and negative evidence retained.
- [x] Public implementation/dataset locators inspected where available.
- [ ] External repositories pinned to exact inspected commits.
- [ ] Code, tests, models, datasets, or benchmark tasks executed.
- [ ] Clinical labels, masks, or statistical outputs independently audited.
- [ ] Hardware/EDA workflows or probabilistic-memory simulations reproduced.
- [ ] NQS training, SAE extraction, or steering experiments reproduced.
- [ ] Cross-domain typed-state hypothesis evaluated under a shared protocol.

### B. Random Selection and Eligibility Record

| Item | Public-safe value |
|---|---|
| Automation family | `Black-Lake Data Processing & Review` and `Black-Lake Data Processing & Review 0900` |
| Run timestamp | 2026-08-19T00:03:14Z |
| 24-hour cutoff | 2026-08-18T00:03:14Z |
| Canonical candidates | 117 |
| Excluded candidates | 52 |
| Eligible candidates | 65 |
| Eligible-list SHA-256 | `c18d4c1798fcfcc21cfbf466edd3ee862f49efd33e5448cb75983da13ae80121` |
| Random method | OS-cryptographic UInt32 rejection sampling over the sorted eligible list |
| Rejection limit, exclusive | 4,294,967,235 |
| Accepted UInt32 | 1,599,395,279 on attempt 1 |
| Selected zero-based index | 14 |
| Selected DEP | `DEP-20260706-Tech Intel 0104` |

### C. Source Inventory

- Source DEP files: `README.md`; `daily_research_findings_2026-07-06_0104.md`.
- Primary papers: ten complete arXiv HTML documents, R1/R3/R4/R5/R7/R9/R11/R13/R14/R16.
- Official public surfaces: MemSyco-Bench, ResearchClawBench, VERITAS, PROMISE, and MedStreamBench dataset locator.
- External files collected: none.
- Executions performed: none.
- Prior selected-DEP artifact status: no matching source report, Report-Mark, output log, or DEP Class artifact. One older unrelated SAILFISH manuscript cites the DEP's VeriChat item as contextual related reading only.

### D. Quantitative Anchors and Boundaries

| Source | Anchor | Boundary |
|---|---|---|
| ProvenanceGuard | Misaligned-trace error 44.3%→2.1% on Agent-SafetyBench; 32.4%→18.7% on WorkBench | Small aligned sample; reconstructed plans; benchmark-specific alignment definition |
| Kara/KvLLM | 90.00 MATH-500 and 82.50 AMC23 at 40% retention in Qwen3-4B ablation; 3,392 tokens/s at displayed 256-sequence setting | Retention and serving policies differ; irreversible information loss |
| ATMem | 76.6% AndroidWorld; 23.3% MobileWorld for 8B model | Large training infrastructure; hard DataScope success remains low |
| MemSyco-Bench | 1,550 released samples; Qwen3-8B full-dialog objective accuracy 30.62% vs. 49.12% no-memory | LLM judging and system-specific native configurations |
| ResearchClawBench | 40 tasks/10 domains; top reported autonomous mean 21.5 with 50 as reference-level anchor | Dry-lab, target-paper-rubric, final-report emphasis |
| VERITAS | 81.4% frontier majority-vote verdict; 86.6% verifiable outputs | Two MRI domains; segmentation and dataset-specific ground truth |
| MedStreamBench | 22 datasets; 5,419 records; 3,369 streaming jobs | Heterogeneous/weak labels and fixed sampling |
| VeriChat | 150 expert queries; 87.73% human-reviewed faithfulness on 40 questions | Synthetic case study; component judges; authorized defensive use only |
| p-MEM | 3.05% layout-area model error; 13.87%/14.48% latency/energy model error; large simulated system gains | No fabricated p-MEM evidence inspected; workload-tailored estimates |
| NQS SAE | Feature-observable correlation magnitude up to 0.97; reported steering energy deviation below 0.02% | Transformer/final-layer/model sampling regime only |

### E. Public-Safety Note

This artifact uses repository-relative paths, public URLs, date-only values, and UTC-only operational timestamps. It contains no local absolute paths, usernames, machine identifiers, local timezone labels, credentials, private data, or operational exploit instructions.
