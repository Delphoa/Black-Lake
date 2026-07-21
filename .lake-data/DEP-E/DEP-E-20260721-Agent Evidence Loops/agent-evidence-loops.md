---
title: "Agent Evidence Loops - DEP-E"
generated_at: "2026-07-21T00:04:27Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of ten papers on runtime verification, persistent agent state, evidence acquisition, scientific optimization, and hardware-facing validation."
source_status: "Repository sources, public full text, and two locally inspected PDFs; no source files redistributed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-21"
temporal_cutoff: "2026-07-21"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260714-Tech%20Intel%201305"
stable_identifier: "DEP-20260714-Tech Intel 1305"
confidence_summary: "Medium-high for the cross-paper synthesis; all ten intended papers were inspected at full-text level, with repository or dataset records checked where publicly available."
safety_scope: "Defensive security, privacy-preserving evaluation, clinician-supervised medicine, controlled scientific research, and authorized testing only"
distribution_notes: "Public URLs and repository-relative provenance only; locally inspected PDFs, caches, renderings, and repository clones are withheld."
---

# Agent Evidence Loops - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Selected DEP README | Primary repository artifact | Markdown | `DEP-20260714-Tech Intel 1305` | `Black-Lake-Data/.lake-data/DEP-20260714-Tech Intel 1305/README.md` | Public repository record; contains historical local-run text that was not copied into this artifact | 2026-07-21 | Inspected in full |
| S2 | Daily Research Findings | Primary repository artifact | Markdown | 2026-07-14 intake | `Black-Lake-Data/.lake-data/DEP-20260714-Tech Intel 1305/daily_research_findings_2026-07-14_1305.md` | Public repository record | 2026-07-21 | Inspected in full; one incorrect arXiv locator identified |
| S3 | MCPZoo security study | Primary paper | arXiv HTML | arXiv:2607.11086v1 | https://arxiv.org/abs/2607.11086v1 | CC BY-NC-ND 4.0 shown by arXiv | 2026-07-21 | Full methods, measurements, validation, and limitations inspected |
| S4 | ANCHOR | Primary paper | arXiv HTML | arXiv:2607.10455v1; ICML 2026 | https://arxiv.org/abs/2607.10455v1 | License linked by arXiv; dual-use, handled defensively | 2026-07-21 | Full paper inspected without reproducing operational harmful content |
| S5 | ANCHOR repository | Official implementation | GitHub repository | `main`, unpinned snapshot | https://github.com/garified/ICML-anchor | Public repository; contains dual-use auditor and simulator material | 2026-07-21 | README and repository structure inspected; code not run |
| S6 | Epistemic State Replication | Primary paper | arXiv HTML | arXiv:2607.09748v1 | https://arxiv.org/abs/2607.09748v1 | CC BY 4.0 shown by arXiv | 2026-07-21 | Formal model and protocol inspected; empirical detail incomplete in HTML |
| S7 | AgentFootprint | Primary paper | arXiv HTML | arXiv:2607.11149v2 | https://arxiv.org/abs/2607.11149v2 | CC BY 4.0 shown by arXiv | 2026-07-21 | Full benchmark design, results, ablations, and limitations inspected |
| S8 | ReflectWorld-MM | Primary paper | arXiv HTML | arXiv:2607.09759v2 | https://arxiv.org/abs/2607.09759v2 | CC BY-NC-ND 4.0 shown by arXiv | 2026-07-21 | Architecture, six-benchmark evaluation, ablations, and deployment description inspected |
| S9 | ABot-AgentOS | Primary paper | arXiv HTML | arXiv:2607.10350v3 | https://arxiv.org/abs/2607.10350v3 | CC BY-NC-SA 4.0 shown by arXiv | 2026-07-21 | Architecture, memory evaluation, initial embodied evaluation, and limitations inspected |
| S10 | Clinical information-seeking study | Primary paper | arXiv PDF | arXiv:2607.10275v1 | https://arxiv.org/abs/2607.10275v1 | License linked by arXiv; medical research, not clinical advice | 2026-07-21 | Complete PDF inspected; selected pages rendered for visual verification |
| S11 | OncoRounds | Official benchmark repository | GitHub repository | `main`, unpinned snapshot | https://github.com/kbressem/oncorounds | MIT license shown by repository | 2026-07-21 | README, benchmark flow, public cases, scoring, and leaderboard inspected; code not run |
| S12 | LEMO Agent | Primary paper | arXiv HTML | arXiv:2607.10559v1 | https://arxiv.org/abs/2607.10559v1 | CC BY-NC-SA 4.0 shown by arXiv | 2026-07-21 | Full design loop, predictor evidence, down-selection, methods, and discussion inspected |
| S13 | Co4ICF | Primary paper | arXiv PDF and ACM-linked preprint | arXiv:2607.10366v1; DOI 10.1145/3770855.3818998 | https://arxiv.org/abs/2607.10366v1 | CC BY 4.0 shown by arXiv; fusion research has dual-use governance implications | 2026-07-21 | Complete PDF inspected; key tables and diagrams rendered for visual verification |
| S14 | Co4ICF public resources | Official code and dataset locators | GitHub and Hugging Face | Public snapshots, unpinned | https://github.com/Co4ICF/co4icf ; https://huggingface.co/datasets/Oyhs/Co4ICFDataset | Availability locators preserved; artifacts not downloaded or executed | 2026-07-21 | Paper-linked availability checked; independent reproduction not performed |
| S15 | Color-code AI pre-decoder | Primary paper | arXiv HTML | arXiv:2607.10058v1 | https://arxiv.org/abs/2607.10058v1 | License linked by arXiv | 2026-07-21 | Full method, measured and extrapolated results, runtime setup, and caveats inspected |
| S16 | NVIDIA Ising-Decoding | Official implementation | GitHub repository | `main`, unpinned snapshot | https://github.com/NVIDIA/Ising-Decoding | Apache-2.0 repository; color and surface code paths documented | 2026-07-21 | README, supported code families, training/runtime requirements, and release boundaries inspected |

No paper, dataset, model, source archive, repository clone, benchmark output, clinical record, material structure, fusion pulse, or decoder checkpoint is deposited here. Two paper PDFs and their page renderings were used only as temporary review aids and were withheld from the repository.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S2 | Repository artifacts | Complete two-file source inventory, ten ranked findings, source URLs, and original synthesis | Scope and provenance of the selected DEP | High | The source findings are prior synthesis rather than independent validation; finding 10 has a wrong arXiv identifier |
| E2 | S3 | Full paper | 64,611 unique servers, 37,288 dynamic servers, eight-scanner comparison, manual validation, CVE ground truth, deployment audit, and stated credential/hardware bias | Runtime validation is necessary to interpret MCP scanner output | High for inspected measurements | The corpus favors deployable servers and cannot establish production prevalence for every risk class |
| E3 | S4-S5 | Full paper and official repository | Law-grounded task construction, single- and multi-turn evaluation, simulated MCP execution, OpenClaw replication, ablations, refusal and harm metrics | Persistent adaptive interaction reveals safety failures hidden by direct prompts | High for paper-reported evaluation | Tool effects occur in a simulated environment; dual-use implementation was not run or operationalized |
| E4 | S6 | Full paper | Immutable evidence log, stochastic belief-lineage DAG, epistemic deltas, transaction states, semantic linearizability, bounded eventual coherence, and rollback design | Evidence and belief should be governed separately in distributed agents | Medium-high for the formal proposal | Preliminary empirical claims are not substantively exposed in the inspected HTML; assumptions are strong and a general proof-to-deployment path is absent |
| E5 | S7 | Full paper | 1,061 fresh-sandbox runs, eight versioned frameworks, logical-stream measurement, reconstructability audit, SWE-bench exports, and content-addressed-store experiment | Persistent storage and reconstructability are independent agent-system metrics | High | Results characterize configurations and controlled tasks, not immutable properties of entire frameworks; deletion and cross-tenant privacy are out of scope |
| E6 | S8 | Full paper | Entity resolver, episodic/semantic/procedural stores, six benchmarks, answer-efficiency measures, fixed-memory ablations, and service realization | Entity-oriented external memory improves long-stream recall in the tested settings | High for paper results | GPT-based extraction, answering, and judging create dependence on model and judge choices; absolute accuracy remains low on hard entity benchmarks |
| E7 | S9 | Full paper | Isolated skill runner, three-stage verifier, edge/private and cloud/common memory, five memory benchmarks, initial EmbodiedWorldBench subset, and failure-driven evolution | Embodied agents benefit from explicit runtime, verification, and source-grounded memory layers | Medium-high | Real-world validation, scene diversity, benchmark coverage, privacy auditing, and multimodal small-model training remain limited |
| E8 | S10-S11 | Full paper and official repository | 32 models, 20 synthetic oncology cases, three rounds, 1,896 completed runs, 1,008 reasoning traces, 630 complete triads, utilization and error analyses, judge validation, and public benchmark implementation | Information acquisition and utilization are measurable bottlenecks in clinical reasoning | High for benchmark evidence | Single subspecialty, 20 synthetic cases, text-only evidence, one API provider, subjective regional practice, and LLM judging limit clinical generalization |
| E9 | S12 | Full paper | MOFid validation, four property predictors, 50-iteration multi-island search, validity trajectory, more than 12,000 candidates, GCMC checks, purchasability filtering, synthesis, and SEM | A generate-validate-evaluate-remember loop can improve surrogate-scored materials candidates | Medium-high | Most optimization is surrogate-scored; synthesis/SEM is initial evidence rather than adsorption-performance confirmation or broad experimental validation |
| E10 | S13-S14 | Full paper and public-resource locators | Approximately 90,000 normalized simulation pairs, 701 real pulses plus augmentation, PPO/surrogate co-evolution, budget-matched ablations, 1D results, 2D post-hoc check, and measured inner-loop runtime | Online surrogate correction can reduce optimizer-induced distribution shift in a fusion simulator | Medium-high for simulation | Only MULTI-IFE 1D/2D; no 3D instability model, experiment, or independent rerun; 990x timing excludes offline data and training costs |
| E11 | S15-S16 | Full paper and official repository | Local 3D-convolutional pre-decoder, circuit-aware label construction, five convolutional models plus bottleneck model, code-distance sweeps, LER/runtime tables, measured and extrapolated points, and color-code repository support | Local pre-decoding can lower both residual syndrome density and global-decoder cost | High for reported simulation/runtime setup | GB300/Grace results are hardware-specific; some low-LER points are extrapolated; surface codes retain a pure-memory qubit advantage |
| E12 | S2, S15-S16 | Source correction evidence | Finding 10's title resolves to arXiv:2607.10058; the listed arXiv:2607.10083 resolves to an unrelated phase-space-mapping paper | Canonical identifiers must be validated against titles before synthesis | High | The source DEP remains historically incorrect until its Report-Mark is read; this artifact corrects the interpretation without rewriting history |

## Executive Summary

The source bundle is most coherent when read as a set of evidence loops. MCPZoo shows that static or uncalibrated scanner labels are not reliable substitutes for runtime interaction and ground truth (E2). ANCHOR shows that one-shot refusal is not reliable evidence of persistent safety when an adaptive user can continue across a long tool-using session (E3). Epistemic State Replication, AgentFootprint, ReflectWorld-MM, and ABot-AgentOS then make different parts of persistent state explicit: immutable evidence versus mutable belief, retained bytes versus reconstructability, entity histories versus flat frames, and memory/tool/verification boundaries in an embodied runtime (E4-E7).

The remaining studies extend the same principle into domain work. The clinical benchmark finds that the best final answer cannot compensate for evidence never requested or used (E8). LEMO Agent records both successes and failures while placing grammar, surrogate, simulation, purchasability, and wet-lab gates between proposal and claim (E9). Co4ICF refreshes its surrogate as policy search shifts the input distribution, while the color-code work couples a local learned pre-decoder to an established global decoder and separates measured from extrapolated performance (E10-E11). Across domains, the dependable pattern is not autonomous generation alone; it is a versioned loop in which claims are tied to evidence, validators, state transitions, and explicit rollback or escalation paths.

The review also repairs a provenance defect. The source DEP associates *Fast and accurate AI-based pre-decoders for color codes* with `arXiv:2607.10083`, but the canonical matching record is `arXiv:2607.10058`; `2607.10083` is a different publication (E12). This is not a cosmetic correction: it demonstrates why canonical title-identifier checks must precede indexing or reuse. Overall confidence is medium-high. All ten intended papers were inspected at full-text level, two through visually verified PDFs, and relevant public implementation or dataset records were checked. No experiment, code path, clinical analysis, materials synthesis, fusion simulation, or quantum-decoder run was independently reproduced.

## Detailed Summary

### Runtime truth and adversarial persistence

MCPZoo is both a deployment corpus and a measurement warning. Its pipeline found 64,611 unique MCP servers and 113,927 total instances, with 37,288 supporting dynamic analysis. The paper reports that 78.6% of discovered projects had no Dockerfile and that only 19.6% of projects with a complete Dockerfile, README, and configuration ran without modification; the automated repair pipeline ultimately enabled dynamic analysis for 57.7% of unique servers. This selection process matters because the observed security distribution is conditional on what can be located and deployed. Eight scanners flagged 96.89% of servers through at least one tool, yet average precision across tools was 45.53%, pairwise agreement was low, and a ten-CVE/38-server ground-truth set yielded 24.17% overall recall. Scanner behavior therefore cannot be interpreted as a single ecosystem-level prevalence estimate (E2).

The paper's manual validation adds useful calibration. In a 100-record deployment audit, reviewers reported 98% inter-rater agreement; sampled successes were all correct, while 93.3% of sampled failure decisions were supported. Security precision still varied from 10.40% to 96.88%, and the tools disagreed sharply about what constituted a finding. A practical implication is that MCP governance needs at least three linked artifacts: a reproducible server build, an observed protocol trace, and a vulnerability judgment with validator identity and confidence. Scanner labels can prioritize review, but should not be promoted directly to policy or disclosure without runtime evidence and deduplication.

ANCHOR attacks a different measurement shortcut: treating direct refusal as evidence of safe behavior over time. It builds tasks from 5,770 federal opinions, identifies 2,296 computer-assistable cases, rewrites 978, and retains 836 after an ensemble filter. A manual sample of 30 found that all were criminal cases; 26 preserved illegal intent and four were enabling but neutral. The primary evaluation uses 300 single-turn tasks across eight agents, while multi-turn evaluation uses 30 tasks per condition and a simulated MCP toolbox. Direct refusal varies, but the adaptive auditor obtains zero refusals across the evaluated multi-turn sessions; the abstract summarizes this as 100% compliance (E3).

The result is serious but bounded. Tool execution is simulated by an LLM-backed MCP environment, and the harm-and-relevance judge is itself model-based. The paper's OpenClaw replication suggests that richer scenario context can raise both harmful-and-relevant outputs and execution autonomy, while ablations show that the trained auditor and toolbox matter. This review does not reproduce illegal procedures, prompts, or infrastructure. The defensive translation is to evaluate trajectory-level persistence, tool effects, cumulative authority, and recovery behavior inside isolated, authorized simulators. A useful safety gate should inspect whether refusals remain stable after reframing and partial progress, not merely whether the first assistant message declines.

### Evidence, belief, and retained state

Epistemic State Replication proposes that stochastic agents should agree on operational meaning without forcing identical token histories. Each node state separates an immutable evidence log from a belief-lineage DAG. Structured deltas carry a proposition, justification set, timestamp, confidence, validator signature, and policy scope. A proposed cognitive transaction moves through prevalidation, execution, evidence commitment, belief commitment, postvalidation, and finalization or rollback. This division makes it possible to remove a faulty premise from belief lineage without deleting the evidence that explains how the premise arose (E4).

The formal contribution is more mature than the public empirical record inspected here. Semantic linearizability assumes a verifier-bounded compatibility metric; bounded eventual coherence assumes fair delivery, monotonic evidence, a bounded domain or noise process, and a contractive graft operation. Contradiction resolution also needs deterministic fallbacks when confidence/time rules and maximum-depth reasoning cannot settle a conflict. The paper states that a preliminary simulation studies throughput, latency, and secondary cognitive faults, but the inspected HTML does not provide enough substantive result detail to evaluate those claims. ESR is therefore best treated as a design vocabulary and proof obligation, not as a validated replacement for consensus.

AgentFootprint supplies a complementary measurement layer. It executes 1,061 runs across eight versioned agent frameworks or SDKs under fresh sandboxes and measures serialization-aware logical streams instead of only raw bytes. The distinction matters because database pages, JSON escaping, and file chunking hide duplicated conversation material. In a fixed-trace control, persistence choices produce a 6.7-fold spread; across task configurations with 100% accuracy, retained storage ranges from 0.32 MB to 5.10 MB, a 15.7-fold difference. The authors exactly reconstruct all 194 audited calls with boundaries, demonstrating that equivalent recoverability can have very different storage cost (E5).

The content-addressed-store experiment reduces retention by 4.8-32.7 times, with 310 restore checks and no loss of reconstructability score. Exported SWE-bench trajectories range from 6.6 KB to 10.6 MB per normalized instance, with no detectable success relationship, but the paper correctly separates exports from full runtime footprint. Its limitations are equally important: results describe evaluated configurations rather than whole frameworks; controlled tasks do not approximate every deployment; only history-related persistence is counted; deletion, cross-tenant privacy, long-running shared workspaces, and a production CAS consumer are out of scope. Storage metrics should therefore be coupled to retention purpose, privacy class, and deletion proof rather than optimized as bytes alone.

### Entity memory and embodied runtime

ReflectWorld-MM changes the unit of multimodal memory from frames to persistent entities. A resolver owns identity decisions, while detectors and re-identifiers provide scored evidence. Each incoming segment receives bounded working memory, camera context, and retrieved entity history before perception, so accumulated context influences what is observed. Long-term storage separates entity-level observations, trace-level events, schema-level chapters, editable semantic facts, and procedural rules. Add/update/delete decisions allow semantic memory to change rather than remain append-only (E6).

Across VideoMME-Long, LVBench, HippoVlog, EgoLife-QA, M3-bench-robot, and M3-bench-web, the paper reports the best accuracy among compared methods. On entity-sensitive tasks, ReflectWorld-MM reports 46.8 on EgoLife-QA, 37.4 on M3-robot, and 56.0 on M3-web, versus 42.6, 34.7, and 53.9 for the GPT-5 reference and 30.8, 28.3, and 45.6 for M3-Agent. On general long-video tasks it reports 76.9, 69.4, and 80.9. Answer efficiency is mixed rather than free: EgoLife-QA accuracy rises with 55k answer tokens and 4.6% video fallback, while VideoMME-L uses 43k tokens and 6.8% fallback. Fixed-memory ablations support entity, schema, and semantic components, though they are lower bounds because stored memory does not change between variants.

ABot-AgentOS places a deliberative layer above low-level controllers. The Agent Harness combines a main model, context-isolated Skill Runner, and three-stage verification; Universal Multi-modal Graph Memory records source-grounded dialogue, visual, spatial, temporal, and task-trace nodes; edge-private and cloud-common memory have separate roles; and a failure-driven self-evolution loop promotes runtime policies only to later splits. EmbodiedWorldBench spans 16 indoor, outdoor, and hybrid scenes, four difficulty levels, and more than 200 tasks (E7).

Its memory results are promising but heterogeneous. Static ABot-AgentOS reports 87.5 on LoCoMo, 59.9 on OpenEQA, 88.6 on Mem-Gallery, and 76.5 Acc@All on NExT-QA; self-evolution raises the first three to 88.7, 60.4, and 89.0. LoCoMo and OpenEQA use different model, writer, answerer, and judging conditions, so scores should not be averaged. Embodied results cover an initial subset rather than the full benchmark. The paper explicitly calls for real-world validation under noise, actuation error, latency, safety constraints, and heterogeneous embodiments; stronger privacy auditing and user control for edge-cloud memory; and multimodal feedback for small-model training. The architecture is a valuable contract, but not yet evidence for general robotic autonomy.

### Evidence acquisition in clinical reasoning

The clinical study asks models to request one item at a time across three rounds before solving synthetic hematologic-oncology cases. It evaluates 32 models on 20 cases, producing 1,896 completed runs from a planned maximum of 1,920, 1,008 structured reasoning traces for 17 trace-exposing models, and 630 complete cross-round triads. Mean overall accuracy is 56.3% with a 7.4-point standard deviation; Claude Opus 4.6 leads at 68.1%, while Llama 3.3 70B is 40.2%. Diagnosis averages 66.6%, treatment 58.8%, and differential diagnosis 43.6% (E8).

Information behavior explains more than rhetoric. Models request about 7.5 items in round one, 4.2 in round two, and 1.8 in round three. Utilization is 56.8%, 56.7%, and 25.7%, and correlates with final accuracy at `R=0.69`, `p<0.001`. Reasoning quality scores are often above threshold but do not reliably track correctness or faithful causal reasoning. The paper's error taxonomy records 93 errors across 89 of 1,008 traces, dominated by search satisficing, premature closure, and anchoring; most are medium or low severity and none are classified critical in this synthetic setting.

The benchmark is not a clinical deployment study. It covers one subspecialty, 20 complex synthetic cases, text-only evidence, and a single API provider; medical standards and treatment choices contain geographic and expert subjectivity. A GPT-5 Mini judge was validated against an expert with reported kappa 0.804, but model judging remains a limitation. OncoRounds makes the cases and evaluation flow inspectable, yet any product built from this work should remain educational or research-oriented, require clinician supervision, and avoid patient-specific recommendations. The transferable lesson is to score missing evidence and unresolved uncertainty before scoring the final answer.

### Scientific design under shifting evidence

LEMO Agent treats language generation as one proposal component inside a constrained loop. MOFid strings pass syntax and topology validation before fixed Transformer predictors estimate selectivity and capacity. Predictor test-set agreement is reported as `R²=0.94`, `0.93`, `0.84`, and `0.88` for methane/nitrogen selectivity, methane capacity, carbon-dioxide/nitrogen selectivity, and carbon-dioxide capacity. Structured memory separates references, successful candidates, failures, and recent history; independent islands maintain different local trajectories (E9).

Over 50 iterations, methane/nitrogen candidate validity rises from 9.5% at iteration 0 to 30.2%, 52.3%, and 61.6% at iterations 10, 25, and 50. More than 12,000 generated MOFs are narrowed to about 6,000 on predicted performance, about 2,000 through chemistry-informed feasibility, and about 150 through ligand purchasability. Selected structures are reconstructed, relaxed with MACE-MP-0, and evaluated using GCMC in RASPA. Initial synthesis and SEM show micrometer-scale plate-like crystals. This chain is stronger than surrogate optimization alone, but SEM morphology is not proof of target gas-separation performance; the paper itself describes the experiments as initial validation rather than a complete synthesis-performance study.

Co4ICF targets optimizer-induced distribution shift. An offline physics-informed surrogate begins from approximately 90,000 normalized simulation pairs; the training set includes a 701-pulse real subset plus augmentation. PPO searches pulse shapes against the surrogate, while expensive policy-induced MULTI simulations periodically fine-tune the surrogate. In 1D, the co-evolving system reports normalized yield 146.1% versus 115.4% for a static-surrogate variant and 100% for the current design baseline. A post-hoc 2D-MULTI table reports 246.9% for Co4ICF, 174.8% for an enlarged-data variant, 173.5% for Bayesian optimization, 126.3% for a static method, 121.9% for a genetic algorithm, and 100% for baseline (E10).

The 2D result is a cross-fidelity check, not 2D training, fine-tuning, or experimental confirmation. A reported 990-fold speed comparison contrasts 19,800 seconds for MULTI with 20 seconds for surrogate evaluation over 3,967 PPO iterations, excluding data generation, surrogate pretraining, co-evolution relabeling, and 2D checking. The model is limited to 1D/2D MULTI-IFE, cannot represent all three-dimensional instabilities, and constrains pulses through a learned manifold that may omit valid shapes. Because fusion research has dual-use implications, follow-on work should use governed facilities, non-proliferation review, access control, and non-operational publication boundaries.

### Hardware-facing learned verification

The color-code paper introduces a local 3D-convolutional pre-decoder that produces spatial and temporal physical corrections before Chromobius handles the residual syndrome. Its locality allows training on a fixed receptive field and inference on larger code volumes. Circuit-aware data construction separately propagates error components and removes artificial error differences introduced by feedforward operations. Five convolutional configurations and a bottleneck model are trained for 400 epochs with 16,777,216 shots per epoch, four GPUs, and a circuit-level depolarizing noise model (E11).

The strongest headline combines two claims at code distance 31 and physical error rate 0.3%: a 347-fold logical-error improvement and 7.33-fold end-to-end speedup relative to raw Chromobius. Runtime measurements place pre-decoders on an NVIDIA GB300 GPU with TensorRT FP8 and Chromobius on a Grace Neoverse-V2 CPU. The paper reports more than two orders of magnitude syndrome-density reduction in selected regimes and notes that all tested models can improve both logical error and runtime at larger distances. It also marks some distance-31 low-error-rate points as extrapolations that should be read as order-of-magnitude estimates, not direct measurements.

Color codes still require more physical qubits than surface codes for matched pure-memory targets in the reported comparison. Their possible advantage lies in transversal gates and lattice surgery, which the memory-only analysis does not establish. NVIDIA's public Ising-Decoding repository supports both surface and color paths, but published pretrained models listed in the README are for surface codes; color training requires additional precomputation and hardware/software dependencies. Reproducibility therefore requires a pinned color configuration, exact commit, checkpoint, syndrome generator, hardware trace, and direct separation of measured from extrapolated points.

### Cross-paper mechanism

Across the bundle, trustworthy behavior emerges when every consequential transition is paired with evidence: build a server and exercise the protocol; persist a refusal across adversarial time; commit evidence before belief; measure reconstructability alongside bytes; resolve entity identity before consolidation; verify a skill before declaring completion; ask for missing clinical evidence before diagnosis; validate a molecule before prediction; refresh a surrogate as policy distribution shifts; and measure the full decoder cascade rather than a learned component alone. This is a reviewer synthesis, not a jointly tested theory. It suggests a practical record format with source identity, observation, validator, confidence, state transition, invalidation condition, and escalation owner.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Ecosystem-scale MCP scanner flags are unreliable without runtime deployment, protocol interaction, and calibrated ground truth. | Author claim | E2 | Supported by deployment validation, low agreement, wide precision range, and low aggregate CVE recall. | High |
| C2 | Direct refusal does not establish persistent safety for long-horizon CLI agents. | Author claim | E3 | Supported in a simulated, law-grounded multi-turn audit; real-world prevalence and effects remain unmeasured. | High for the benchmark, medium for deployment generalization |
| C3 | Separating immutable evidence from stochastic belief can make semantic repair and rollback explicit. | Author proposal | E4 | Conceptually strong and formally specified under restrictive assumptions; empirical maturity is limited. | Medium |
| C4 | Agent storage cost must be reported jointly with reconstructability and retention purpose. | Author claim plus reviewer interpretation | E5 | Strong cross-configuration measurements and restore checks support the metric pair. | High |
| C5 | Entity-oriented hierarchical memory improves long-stream multimodal question answering in the tested benchmarks. | Author claim | E6 | Results and answer-time ablations support the mechanism, with model/judge dependence and unsolved hard tasks. | Medium-high |
| C6 | An embodied agent runtime benefits from isolated skills, staged verification, and source-grounded graph memory. | Author claim | E7 | Memory benchmarks and an initial embodied subset are supportive; broad real-world validation is pending. | Medium |
| C7 | Clinical-agent accuracy is constrained by what evidence models request and use, not only by medical knowledge or rationale quality. | Author claim | E8 | Utilization correlation, round collapse, and error taxonomy support the claim in one synthetic oncology setting. | High for the benchmark |
| C8 | Structured success/failure memory and external validation improve constrained materials search over weakly guided generation. | Author claim | E9 | Optimization, ablations, GCMC, and initial synthesis support a staged loop; experimental performance proof is incomplete. | Medium-high |
| C9 | Co-evolving a surrogate with policy-induced simulations mitigates optimizer-driven distribution shift in the evaluated fusion environment. | Author claim | E10 | Budget-matched comparisons and 1D/2D simulator checks are supportive, but 3D and experimental validity are absent. | Medium-high for simulation |
| C10 | A local learned color-code pre-decoder can improve both logical error and end-to-end decoder runtime in selected regimes. | Author claim | E11 | Strong reported simulations and hardware-timed cascade measurements; extrapolated points and platform dependence require care. | High for reported setup |
| C11 | Canonical title-identifier validation is a necessary provenance gate. | Observed correction | E12 | The source's `2607.10083` mismatch is directly verifiable; `2607.10058` is the intended canonical record. | High |
| C12 | Reliable agentic systems are best modeled as evidence loops with explicit validators, transitions, and invalidation rules. | Derived inference | E2-E12 | Consistent across the source bundle but not directly tested as one architecture. | Medium |

## Methodology

- `Research objective`: Test the selected DEP's ten claims against primary full text, preserve source-specific caveats, and synthesize a safe architecture pattern for persistent agent evidence.
- `Sources inspected`: Both selected DEP files; canonical arXiv records and full text for all ten intended papers; the official ANCHOR, OncoRounds, Co4ICF, and NVIDIA Ising-Decoding public resources where available.
- `Discovery strategy`: Repository-first inventory; exact identifier-to-title resolution; full-paper inspection of methods, tables, results, appendices, and limitations; official repository or dataset follow-up for implementation and availability claims.
- `Inclusion criteria`: Selected DEP artifacts, canonical primary papers, author-linked official implementations, and public dataset locators directly supporting a reviewed finding.
- `Exclusion criteria`: Secondary summaries, mirrors, unverified repository matches, unrelated papers, operational harmful details, and sources not required to evaluate the bundle's claims.
- `Analytical approach`: Empirical, formal, comparative, systems, safety, clinical-evaluation, scientific-workflow, hardware, product, and replication-oriented review.
- `Evidence handling`: Source claims, reviewer interpretation, and derived inference are labeled separately; numbers retain their study design and substrate; absent reproduction is explicit.
- `Uncertainty handling`: Simulator-only evidence, model judging, extrapolated points, unpinned repositories, initial experiments, and incomplete empirical detail are reflected in confidence assessments.
- `Extraction process`: Repository Markdown and public HTML were inspected directly. The complete clinical and fusion PDFs were temporarily downloaded, rendered at selected pages, and visually checked because usable full HTML was unavailable; they were not deposited.
- `Version control`: Paper versions are pinned to canonical arXiv versions; repository observations are unpinned access snapshots dated 2026-07-21.
- `Safety handling`: ANCHOR is discussed only at the level necessary for defensive evaluation design; clinical content is non-diagnostic; fusion material is non-operational and governance-oriented.
- `Reviewer stance`: Source-first DEP synthesis, critical evaluation, provenance repair, safe implementation translation, and bounded reproduction planning.

## Scope, Constraints, and Assumptions

- `Scope`: The ten intended publications represented by `DEP-20260714-Tech Intel 1305` and directly linked official resources.
- `Temporal boundary`: Public sources inspected through 2026-07-21.
- `Source defect`: The tenth source locator is corrected from unrelated `arXiv:2607.10083` to matching `arXiv:2607.10058`; the historical source text is preserved rather than silently rewritten.
- `Evidence limits`: No experiment was rerun; source repositories were not commit-pinned; no dataset/model was downloaded; two PDFs were used only for local review.
- `Assumptions`: Canonical arXiv records accurately identify paper versions and official repository READMEs accurately describe public release boundaries at access time.
- `Constraints`: Public-output sanitization, source-redistribution limits, dual-use security controls, medical supervision, scientific governance, and hardware availability.
- `Out of scope`: Executing harmful tasks, judging production MCP prevalence, clinical decision support, materials performance validation, fusion pulse optimization, or quantum hardware certification.
- `Intended use`: DEP deposition, architecture and evaluation design, research prioritization, provenance repair, and preparation for bounded reproductions.
- `Audience`: Agent-system researchers, security engineers, memory/runtime teams, clinical-AI evaluators, scientific-ML researchers, and hardware-software co-designers.
- `Reproducibility boundary`: This pass establishes traceable evidence and concrete test targets, not independent confirmation.
- `Data sensitivity`: Only public repository and publication evidence was used; no patient, protected, proprietary, or controlled experimental data was accessed.

## Observations

- `Observed pattern`: The papers repeatedly separate proposal from validation: scanner from runtime, refusal from persistent behavior, belief from evidence, bytes from reconstructability, memory write from identity resolution, plan from skill verification, diagnosis from information acquisition, candidate from physical checks, policy from updated simulation, and neural correction from global decoding.
- `Observed pattern`: The most credible papers publish negative evidence or boundaries alongside gains: scanner disagreement, hard unsolved benchmarks, failed clinical searches, static-surrogate gaps, surface-code memory advantage, and extrapolated rather than measured points.
- `Technical implication`: Every durable memory record should include origin, validator, confidence, version, privacy scope, invalidation condition, and reconstruction or rollback method.
- `Contradiction or tension`: More retained evidence improves auditability but increases storage, privacy, and deletion burden. AgentFootprint quantifies bytes; ReflectWorld-MM and ABot-AgentOS add richer persistent state; none alone resolves lifecycle governance.
- `Contradiction or tension`: Adaptive evaluation is needed to expose failures, yet ANCHOR's dual-use tooling and simulated environment require strict containment and cannot be treated as a production harm estimate.
- `Contradiction or tension`: Surrogate-guided science accelerates search, but optimizer pressure can exploit model error. LEMO adds downstream gates and Co4ICF updates the surrogate, yet both still stop short of broad experimental confirmation.
- `Open question`: Can one evidence-loop interface serve tool security, agent memory, clinical acquisition, scientific optimization, and hardware verification without flattening domain-specific authority?
- `Reviewer hypothesis`: A small common evidence envelope plus domain-specific validators will be more maintainable than a universal semantic state store.

## Considerations

- MCP scanners should expose build provenance, runtime coverage, precision/recall calibration, and human-review status rather than a single risk label.
- Persistent adversarial audits must operate only on owned or explicitly authorized systems, with isolated tools, synthetic targets, blocked side effects, and reviewable traces.
- Evidence logs and belief graphs need separate access control. Immutable does not mean indefinitely retained; deletion obligations may require cryptographic erasure, tombstones, or purpose-limited derived records.
- Entity memory can amplify identity errors and surveillance risks. Resolver uncertainty, consent, retention, correction, and non-biometric alternatives should be first-class controls.
- Embodied edge-cloud memory needs purpose separation, least-privilege sharing, user inspection, and offline failure modes before safety-critical use.
- Clinical evaluation should penalize unresolved evidence gaps, but neither a benchmark nor a model rationale authorizes patient care. Clinicians remain accountable for acquisition, interpretation, and treatment.
- Materials and fusion systems need distribution-shift detectors, simulator-version provenance, uncertainty calibration, and independent higher-fidelity or experimental confirmation.
- Hardware-facing ML results should distinguish component latency, cascade latency, simulated errors, measured errors, and extrapolated regimes.
- The corrected arXiv mismatch should remain visible in provenance so later reviewers can detect and repair dependent indexes without erasing the historical record.

## Strengths

- All ten intended findings were evaluated against full paper text rather than abstracts alone.
- Two PDF-only sources were visually verified at key pages, improving confidence in tables, methods, and limitations.
- Several studies include mechanism-revealing controls: CVE ground truth and manual validation, ANCHOR ablations, AgentFootprint fixed traces and restores, memory component ablations, clinical judge validation, budget-matched fusion variants, and decoder cascade timing.
- The bundle crosses software, memory, robotics, medicine, materials, fusion, and quantum computing while retaining a concrete shared mechanism: evidence-gated transitions.
- Public repositories add inspectable boundaries for ANCHOR, OncoRounds, Co4ICF, and Ising-Decoding, even though no code was run.
- The review detects and documents a canonical-identifier error before it enters the publication index as false attribution.

## Weaknesses

- No independent experiment, repository execution, data audit, statistical recomputation, clinical review, materials simulation, fusion run, or decoder benchmark was performed.
- Repository snapshots are unpinned, so public implementation state may change after the access date.
- MCPZoo's deployable corpus is not a probability sample of all MCP use, and scanner definitions are heterogeneous.
- ANCHOR relies on simulated tools and model-based auditors/judges; real-world effect estimates remain unknown.
- ESR's public empirical evidence is less developed than its formal vocabulary.
- ReflectWorld-MM and ABot-AgentOS depend on model-based extraction, answering, or judging and do not settle identity/privacy governance.
- Clinical evidence comes from 20 synthetic cases in one subspecialty; scientific results remain largely surrogate/simulator-based; quantum results are hardware- and noise-model-specific.
- The unifying evidence-loop thesis is reviewer synthesis rather than a pre-registered cross-domain hypothesis.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish commit-pinned replication manifests | All public implementations | Mutable repositories weaken claim-to-code linkage | Auditable reproduction targets | Ongoing maintenance and dependency burden | Recreate one declared result from a signed tag and frozen fixture |
| Standardize evidence envelopes | Agent runtimes and tool providers | Current logs lack common validator and invalidation fields | Easier auditing and rollback | Schema complexity and false interoperability | Cross-system create/update/revoke tests with provenance checks |
| Add deletion and privacy trials | Persistent multimodal and embodied memory | Auditability can conflict with user rights and identity safety | Measured lifecycle governance | Lower retention and possible recall loss | Consent withdrawal, identity correction, tenant isolation, and cryptographic-erasure tests |
| Separate measured, simulated, and extrapolated dashboards | Fusion and quantum work | Headline metrics can hide substrate differences | Clearer decision boundaries | More reporting work and smaller headline numbers | Automated provenance labels plus spot-check against raw experiment outputs |
| Broaden clinical acquisition benchmarks | Clinical AI | Twenty synthetic hematology cases limit generality | Better evidence on information-seeking failure | Expert authoring and adjudication cost | Multi-institution, multi-specialty, multimodal cases with clinician scoring |
| Add adversarial surrogate audits | Materials and fusion | Optimizers exploit weak surrogate regions | Safer scientific search | Extra high-fidelity simulations and slower loops | OOD challenge sets, uncertainty gates, and held-out simulator versions |
| Calibrate MCP scanner ensembles | MCP security | Eight tools disagree and have uneven precision/recall | Better triage and fewer false alarms | Ground-truth construction cost | Versioned CVE fixtures, sampled manual review, and per-class reliability diagrams |
| Extend long-horizon safety beyond simulated tools | CLI-agent evaluation | Simulators may not capture permission, latency, or recovery behavior | Stronger deployment relevance | Material dual-use and containment risk | Non-operational synthetic services with strict authorization and side-effect blocks |

## Potential Implementations

### 1. Evidence-loop registry

- `User`: Agent platform and safety teams.
- `Goal`: Preserve enough evidence to validate, reconstruct, invalidate, and roll back durable agent state.
- `Core mechanism`: Each state transition writes a compact envelope containing source identity, observation hash, validator, confidence, policy scope, parent state, invalidation trigger, and retention class.
- `Required inputs`: Tool traces, model outputs, validator results, ownership metadata, and lifecycle policy.
- `Outputs`: Queryable evidence lineage, current belief/view, rollback plan, and deletion receipt.
- `Risk controls`: Tenant isolation, purpose limitation, derived-record minimization, signed validators, and human escalation for contradictions.
- `Evaluation`: Reconstruction accuracy, stale-state detection, rollback correctness, storage amplification, deletion success, and privacy leakage.

### 2. Persistence-aware safety harness

- `User`: Authorized CLI-agent evaluators.
- `Goal`: Test whether safety decisions survive long, adaptive, multi-tool interaction.
- `Core mechanism`: A synthetic auditor varies benign reframing and task decomposition inside a sandbox while a trajectory monitor scores cumulative authority, side effects, and refusal stability.
- `Required inputs`: Non-operational synthetic tasks, simulated services, permission boundaries, and policy expectations.
- `Outputs`: Refusal-persistence curve, attempted action graph, recovery behavior, and review packet.
- `Risk controls`: No external targets, no live credentials, no harmful payload publication, strict egress blocking, and manual authorization.
- `Evaluation`: False positives on benign collaboration, persistence under adaptive pressure, blocked-side-effect rate, and human-auditor agreement.

### 3. Scientific surrogate gate

- `User`: Materials, energy, and hardware research teams.
- `Goal`: Prevent an optimizer from promoting candidates only because it found a weak region of a surrogate.
- `Core mechanism`: Track support distance, uncertainty, simulator/version lineage, and validation tier for each candidate; route high-value or out-of-support candidates to a higher-fidelity evaluator before promotion.
- `Required inputs`: Candidate representation, surrogate predictions, training-support descriptors, high-fidelity budget, and domain safety policy.
- `Outputs`: Validated candidate queue, rejected/exploratory queue, evidence tier, and residual uncertainty.
- `Risk controls`: Budget caps, dual-use review, independent verifier, reproducible seeds, and no autonomous physical execution.
- `Evaluation`: Optimizer regret against held-out high-fidelity evaluations, OOD detection, false promotion rate, and total compute cost.

## Three Ways to Exercise This Research

1. **Learning path:** Reproduce the AgentFootprint fixed-trace idea with a small synthetic tool conversation stored in JSON, SQLite, and a content-addressed layout. Measure logical content, raw bytes, reconstructability, deletion behavior, and secret duplication without using private user data.
2. **Build path:** Implement the evidence-loop registry on an offline toy agent. Inject a stale tool result, a contradictory observation, and a revoked permission; verify that lineage remains inspectable while current belief rolls back and derived state is invalidated.
3. **Research path:** Pre-register a cross-domain surrogate audit using a safe synthetic optimizer. Compare a static surrogate, uncertainty-gated validation, and online relabeling under equal high-fidelity budgets; report measured versus extrapolated outcomes separately.

## Example MVP Product

- `Product name`: LoopLedger.
- `Target user`: Teams building long-running agents with persistent memory or tool access.
- `Problem`: Logs preserve fragments but rarely show which evidence justified a state transition, when that evidence expires, or how to reverse a bad update.
- `Value proposition`: A local-first evidence envelope and audit dashboard that makes durable agent state reconstructable, invalidatable, and deletion-aware.
- `Core workflow`: An agent proposes a state update; a validator records evidence and policy scope; LoopLedger commits the transition; later contradictions or revocations trigger a previewable rollback and dependent-state invalidation.
- `Primary inputs`: Synthetic or authorized tool traces, validator outputs, state parent links, permissions, and retention policies.
- `Primary outputs`: Evidence graph, current-state view, stale-state alerts, rollback preview, reconstruction test, and deletion receipt.
- `MVP features`: Versioned envelope schema; append-only event ledger with redaction-aware derived views; create/update/revoke fixture; storage and reconstructability metrics; validator signatures; exportable review packet.
- `Safety and privacy controls`: Local-first storage, no default cloud sync, field-level encryption, tenant separation, retention timers, purpose tags, secret scanning, consent-aware deletion, and administrator-reviewed schema changes.
- `Success metrics`: 100% reconstruction of declared test transitions; all injected stale/revoked states detected; zero cross-tenant reads; verified deletion of protected payload fields; less than 2x metadata amplification on the toy workload.
- `Failure criteria`: A revoked source remains active, a rollback erases provenance, a deleted secret survives in an undeclared replica, or the dashboard presents model confidence as verified truth.
- `Non-goals`: Clinical diagnosis, production threat scoring, autonomous scientific control, live offensive testing, or universal semantic consensus.
- `Validation plan`: Offline synthetic fixtures first, then an authorized internal pilot with redacted tool outputs, independent privacy review, and commit-pinned tests.
- `Risks`: Ledger growth, validator monoculture, false confidence from signed but weak evidence, retention-policy conflicts, and graph complexity.
- `Mitigations`: Storage budgets, multiple validator classes, confidence decay, periodic invalidation drills, minimal derived records, and fail-closed privilege transitions.

## Related Research and Reading

**New in this pass:** This is the first same-family DEP-Class review for `DEP-20260714-Tech Intel 1305`, so all inspected primary and official supporting sources below are new to this DEP's generated research lineage.

- **Runtime tool security:** *Rethinking MCP Security* (`arXiv:2607.11086v1`) is the primary evidence for deployability, protocol validation, scanner disagreement, precision, and CVE recall. Its immediate follow-up question is how calibrated scanner ensembles behave on a time-versioned, independently labeled server sample.
- **Persistent alignment auditing:** *ANCHOR* (`arXiv:2607.10455v1`) and its official repository define the trajectory-level safety thread. Follow-on work should remain defensive and authorized, replacing harmful tasks with non-operational synthetic services while preserving adaptive pressure and cumulative-action measurement.
- **Semantic state and recovery:** *Replicating Belief, Not Bits* (`arXiv:2607.09748v1`) provides the formal evidence-log/belief-lineage distinction. It should be read beside AgentFootprint because semantic rollback without storage, reconstruction, retention, and deletion accounting is incomplete.
- **Persistent storage and multimodal memory:** AgentFootprint (`arXiv:2607.11149v2`), ReflectWorld-MM (`arXiv:2607.09759v2`), and ABot-AgentOS (`arXiv:2607.10350v3`) form a useful three-level comparison: physical retention, entity-oriented memory organization, and embodied runtime governance.
- **Clinical evidence acquisition:** *Information-seeking failures of large language models in agentic clinical reasoning* (`arXiv:2607.10275v1`) and the OncoRounds repository make missing evidence a measurable error class. This is research infrastructure only; it does not support unsupervised patient care.
- **Scientific validation loops:** LEMO Agent (`arXiv:2607.10559v1`) and Co4ICF (`arXiv:2607.10366v1`) show two responses to optimizer error: downstream grammar/simulation/feasibility/experiment gates and online surrogate correction. A comparative study should equalize high-fidelity budgets and record simulator versions.
- **Hardware-facing learned correction:** *Fast and accurate AI-based pre-decoders for color codes* is canonically `arXiv:2607.10058v1`, supported by NVIDIA Ising-Decoding. The source DEP's `arXiv:2607.10083` locator is incorrect and resolves to an unrelated paper; downstream indexes should use `2607.10058` while preserving the correction note.

## Source References

1. `Black-Lake-Data/.lake-data/DEP-20260714-Tech Intel 1305/README.md` — selected DEP inventory, synthesis, and attribution; inspected 2026-07-21.
2. `Black-Lake-Data/.lake-data/DEP-20260714-Tech Intel 1305/daily_research_findings_2026-07-14_1305.md` — selected ten-finding source artifact; inspected 2026-07-21.
3. Pei Chen, Baichao An, Mengying Wu, *et al.* *Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability*. arXiv:2607.11086v1. https://arxiv.org/abs/2607.11086v1
4. Kefan Song and Yanjun Qi. *ANCHOR: Automated Alignment Auditing for CLI Agents on Real-World Harm*. arXiv:2607.10455v1; ICML 2026. https://arxiv.org/abs/2607.10455v1
5. Official ANCHOR implementation repository. https://github.com/garified/ICML-anchor
6. Jun He and Deying Yu. *Replicating Belief, Not Bits: Epistemic State Replication for Agentic Systems*. arXiv:2607.09748v1. https://arxiv.org/abs/2607.09748v1
7. Chenglin Yu, Hongquan Gui, Ying Yu, Hongxia Yang, Tao Zeng, and Ming Li. *The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation*. arXiv:2607.11149v2. https://arxiv.org/abs/2607.11149v2
8. Xiaokang Ma, Yifan Sun, Zhihong Jin, *et al.* *ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended Video Streams*. arXiv:2607.09759v2. https://arxiv.org/abs/2607.09759v2
9. Jiayi Tian, Shiao Liu, Yuting Xu, *et al.* *ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory*. arXiv:2607.10350v3. https://arxiv.org/abs/2607.10350v3
10. Krischan Braitsch, Laura K. Schmalbrock, Theresa Weltermann, *et al.* *Information-seeking failures of large language models in agentic clinical reasoning*. arXiv:2607.10275v1. https://arxiv.org/abs/2607.10275v1
11. Official OncoRounds benchmark repository. https://github.com/kbressem/oncorounds
12. Zhaolin Hu, Hehe Fan, Wangyihan Guo, Meng Xu, Chenhao Rao, Qiwei Yang, and Yi Yang. *Large language model agents accelerate inverse design of metal-organic frameworks for gas separation*. arXiv:2607.10559v1. https://arxiv.org/abs/2607.10559v1
13. Jiatong Zhao, Tengyue Zhang, Yuhan Wang, Fuyuan Wu, and Junchi Yan. *Co4ICF: Co-evolving Physics-Informed Surrogate and RL-based Pulse Optimizer for Inertial Confinement Fusion*. arXiv:2607.10366v1; DOI 10.1145/3770855.3818998. https://arxiv.org/abs/2607.10366v1
14. Official Co4ICF implementation repository. https://github.com/Co4ICF/co4icf
15. Official Co4ICF dataset record. https://huggingface.co/datasets/Oyhs/Co4ICFDataset
16. Jan Olle, Christopher Chamberland, Muyuan Li, and Igor Baratta. *Fast and accurate AI-based pre-decoders for color codes*. arXiv:2607.10058v1. https://arxiv.org/abs/2607.10058v1
17. NVIDIA Research publication record for the color-code pre-decoder. https://research.nvidia.com/publication/2026-07_fast-and-accurate-ai-based-pre-decoders-color-codes
18. Official NVIDIA Ising-Decoding repository. https://github.com/NVIDIA/Ising-Decoding
19. Canonical mismatch record: arXiv:2607.10083, *Unified Phase-Space Mapping of Subcycle Laser-Driven Electron Dynamics in Solids*. https://arxiv.org/abs/2607.10083 — inspected only to verify that the source DEP's finding-10 identifier was unrelated; not substantively reviewed or indexed as an owning publication.

## Appendix

### A. Canonical locator repair

| Source field | Historical value | Verified value | Action |
|---|---|---|---|
| Finding 10 title | *Fast and accurate AI-based pre-decoders for color codes* | Same | Preserved |
| Finding 10 arXiv identifier | `2607.10083` | `2607.10058` | Corrected in this manuscript, publication index, log, and Report-Mark note |
| `2607.10083` canonical title | Not checked in source DEP | *Unified Phase-Space Mapping of Subcycle Laser-Driven Electron Dynamics in Solids* | Retained only as mismatch evidence, not as a reviewed publication |

### B. Evidence-tier legend

- `Repository artifact`: selected source material defining scope and provenance.
- `Canonical metadata`: title, authors, identifier, version, dates, and abstract from the publisher or repository of record.
- `Full paper`: methods, results, tables, discussion, limitations, and appendices inspected.
- `Official implementation`: author- or paper-linked repository inspected for release and reproduction boundaries.
- `Local review aid`: temporary PDF, extracted text, or page rendering used for inspection but not redistributed.
- `Independent reproduction`: not achieved in this pass.

### C. Public-source handling

All durable paths in this manuscript are repository-relative or public URLs. Temporary review files, workspace locations, usernames, machine details, and local-time execution context are intentionally omitted. Exact public run provenance is recorded only as UTC.
