---
title: "FAVLA Fast-Slow - DEP-E"
generated_at: "2026-07-22 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of force-adaptive fast-slow vision-language-action control for contact-rich robotic manipulation."
source_status: "verified complete local PDF, official full-paper HTML, metadata HTML, and source package; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-22"
temporal_cutoff: "arXiv:2602.23648v1 and focused public code-availability search inspected through 2026-07-22"
primary_url: "https://arxiv.org/abs/2602.23648"
stable_identifier: "arXiv:2602.23648v1; DOI:10.48550/arXiv.2602.23648"
confidence_summary: "High for identity, method, tables, figures, and source-reported results; medium for mechanism attribution; low for deployment safety and cross-platform generalization."
safety_scope: "offline analysis and simulation-only evaluation; no unsupervised physical actuation"
distribution_notes: "Generated Markdown and public URLs only; PDF, HTML, source archive, extracted material, renderings, and private verification records were withheld."
---

# FAVLA Fast-Slow - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Primary metadata | HTML | arXiv:2602.23648v1 | https://arxiv.org/abs/2602.23648 | Public metadata; abstract alone was not used for empirical synthesis. | 2026-07-22 | Inspected |
| S2 | FAVLA full paper | Primary paper | PDF | arXiv:2602.23648v1 | https://arxiv.org/pdf/2602.23648 | CC BY 4.0 is linked from the canonical record; verified private copy withheld. | 2026-07-22 | All 16 pages inspected visually and textually |
| S3 | Official full-paper rendering | Primary paper | HTML | arXiv:2602.23648v1 | https://arxiv.org/html/2602.23648 | Verified complete rendering; private copy withheld. | 2026-07-22 | Inspected in full |
| S4 | arXiv source package | Primary manuscript source | TeX/source archive | arXiv:2602.23648v1 | https://arxiv.org/e-print/2602.23648 | Used to cross-check equations, tables, captions, training details, and appendix; withheld. | 2026-07-22 | Inspected |
| S5 | arXiv-issued DOI | Persistent identifier | DOI | 10.48550/arXiv.2602.23648 | https://doi.org/10.48550/arXiv.2602.23648 | Stable locator. | 2026-07-22 | Verified |
| S6 | Semantic Skill MoE Policies | Related Black Lake DEP | Markdown | DEP-E-20260719 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-Semantic%20Skill%20MoE/semantic_skill_moe_manuscript.md | Processed research artifact; underlying sources separately attributed. | 2026-07-22 | Inspected |
| S7 | iKalibr Calibration | Related Black Lake DEP | Markdown | DEP-E-20260714 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Processed research artifact; underlying sources separately attributed. | 2026-07-22 | Inspected |
| S8 | RRT-CBF Motion | Related Black Lake DEP | Markdown | DEP-E-20260711 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md | Processed research artifact; underlying sources separately attributed. | 2026-07-22 | Inspected |

The paper lists Yao Li, Peiyuan Tang, Wuyang Zhang, Chengyang Zhu, Yifan Duan, Weikai Shi, Xiaodong Zhang, Zijiang Yang, Jianmin Ji, and Yanyong Zhang. The canonical record reports submission on 2026-02-27 in `cs.RO`. The manuscript uses an ICML 2026 preprint style, but the inspected sources do not establish acceptance or a proceedings venue. No official implementation link appears in the arXiv record, paper, or source package, and a focused public search found only third-party index pages rather than an author-verified repository. Code, weights, training data, and evaluation scripts therefore remain unavailable from the inspected sources.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5 | Primary metadata | Title, authors, subject, version, submission date, DOI, abstract, and license link | Identity and chronology | High | Metadata does not validate results |
| E2 | S2-S4, sections 1-3 and Figures 1-3 | Complete primary paper | Fast-slow architecture, force adapter, variance target, adaptive scheduler, fixed-noise reuse, and temporal ensemble | Mechanism reconstruction | High for reporting | No implementation or independent derivation |
| E3 | S2-S4, section 4 and Figures 6-8 | Complete primary paper | Per-task success rates, static-frequency comparison, force measurements, and component ablations | Source-reported performance | High for transcription | Single platform, small trial counts, no uncertainty intervals |
| E4 | S2-S4, appendix Tables 3-5 and Figures 9-14 | Complete primary paper | Dataset size, sensor rates, model configuration, training compute, qualitative behavior, and failure cases | Reproducibility boundary and limitations | High for reporting | Dataset and code unavailable; qualitative frames are selected examples |
| E5 | Private integrity records summarized publicly | Process evidence | Preserved valid PDF, repaired companion bundle, verified HTML structure, zero partials, and source-locality checks | Complete-source gate | High | Original records intentionally withheld |
| E6 | S6-S8 | Related processed research | Skill-conditioned action routing, spatiotemporal sensor integrity, and independent constraint layers | Cross-DEP synthesis | Medium | Related DEP entries do not validate FAVLA results |
| E7 | Repository, memory, and companion scans | Process evidence | Random index, candidate counts, identifier/title/slug searches, and prior-24-hour checks | Selection eligibility and deduplication | High | Only the selected unit received full title-level review |

## Executive Summary

FAVLA separates slow semantic context from faster contact-aware action revision. A 2.6B-parameter vision-language backbone processes two camera views, language, and force history into cached context and predicts near-future force variance. A 300M-parameter action expert reuses that cache, receives current proprioception and force tokens, injects force through layerwise cross-attention, and may run multiple times inside one visual cycle. The predicted variance controls the number of action-expert executions, while fixed noise and temporal ensembling reduce inconsistency among overlapping action chunks.

The paper reports an unweighted mean success rate of 80.8% across four real-robot tasks, versus 67.0% for the strongest mean baseline, ForceVLA. FAVLA also reports lower average peak contact forces than every listed baseline on Gear Assembly and Box Flipping. The most informative evidence is the combination of per-task comparisons, cumulative component ablations, static-frequency comparisons, and explicit failure cases. The evidence is still preliminary: evaluation totals 85 trials per method across one platform, no confidence intervals or repeated training seeds are reported, Box Flipping is a three-way success-rate tie rather than a unique win, and the paper does not isolate each added component with a full factorial ablation.

The largest reproducibility gap concerns temporal resolution. Demonstrations record force/torque and end-effector state at 200 Hz, but all streams are synchronized and downsampled to 30 Hz for the training dataset. The paper motivates retaining 100-1000 Hz force cues and describes a faster action expert, yet it does not fully specify which force samples, sensor-to-policy latency, or actual wall-clock control rates are used during evaluation. Confidence is high in the reported paper contents, medium that the design components jointly cause the measured gains, and low that the evidence supports deployment safety or generalization beyond the tested rig and tasks.

## Detailed Summary

### Problem Context

Contact-rich manipulation requires semantic planning and rapid response to impact, jamming, slip, and force spikes. Conventional VLA pipelines commonly update an expensive vision-language model infrequently and execute predicted action chunks largely open loop. Adding force as another token stream does not by itself solve two mismatches: vision may dominate the token budget, and camera and force sensors operate at different rates. FAVLA treats the mismatch as an architectural scheduling problem rather than only a fusion problem.

### Architecture and Mechanism

At each slow cycle, the model consumes an external RGB image, a wrist RGB image, a language instruction, current seven-dimensional end-effector/gripper state, and force/torque histories. A Temporal Convolutional Network maps six-axis force/torque sequences into four force tokens. The slow PaliGemma-based VLM concatenates vision, language, and historical force tokens and exposes layerwise key/value caches to the action expert.

The action expert generates 32-step, seven-dimensional delta-pose/gripper action chunks using conditional flow matching. Its force adapter cross-attends noisy action tokens to the latest force tokens after self-attention and adds the force-conditioned update in each transformer layer. This differs from merely concatenating force tokens at the prefix and is intended to keep sparse interaction cues visible at the action-generation point.

A force-variance head reads a learned VLM token and regresses an exponentially smoothed, weighted variance of future six-dimensional force/torque over the action horizon. The target is square-rooted, scaled, and passed through `tanh`; the auxiliary loss weight is 0.1. At inference, the normalized prediction selects at least one and up to a configured maximum number of action-expert calls for the next slow cycle. Repeated calls reuse one noise sample, and temporal ensembling smooths overlapping chunks.

### Data, Training, and Evaluation

The robot is a dual-arm Monte platform with 7-DoF X-ARM arms, wrist RGB-D cameras, an external camera, and wrist-mounted six-axis force/torque sensing. The four tasks are USB Insertion, Gear Assembly, Box Flipping, and Board Wiping. The dataset contains 260 teleoperated trajectories, 198,250 frames, and about 1.84 hours: 80 trajectories each for USB and Gear, and 50 each for Box and Wiping. Force/torque and end-effector state are recorded at 200 Hz; camera images are recorded at 30 Hz; the appendix says all streams are synchronized and downsampled to 30 Hz.

Each task uses a separately fine-tuned model. The VLM and action expert initialize from `pi_0`, receive LoRA adapters, and train for 30,000 iterations with batch size 8 and cosine-decayed AdamW learning rate from `2.5e-5` to `1e-6`. Training reportedly takes about six hours per task model on one NVIDIA A100 80GB GPU. The TCN force encoder has 25.2M parameters and the force-variance predictor 1.6M parameters.

Evaluation uses 25 USB, 30 Gear, 20 Box, and 10 Wiping trials per method. The paper compares vision-only `pi_0`, `pi_0 + Force`, TA-VLA, ForceVLA, and FAVLA. All baselines are fine-tuned on the collected task data with LoRA.

| Method | USB Insertion | Gear Assembly | Box Flipping | Board Wiping | Reported Unweighted Mean |
|---|---:|---:|---:|---:|---:|
| `pi_0` | 48.0% | 63.3% | 50.0% | 10.0% | 42.8% |
| `pi_0 + Force` | 76.0% | 80.0% | 50.0% | 60.0% | 66.5% |
| TA-VLA | 36.0% | 83.3% | 80.0% | 50.0% | 62.3% |
| ForceVLA | 68.0% | 70.0% | 80.0% | 50.0% | 67.0% |
| FAVLA | 80.0% | 93.3% | 80.0% | 70.0% | 80.8% |

FAVLA improves the reported unweighted mean by 13.8 percentage points over ForceVLA and 38.0 points over vision-only `pi_0`. It is highest on USB, Gear, and Wiping, but ties TA-VLA and ForceVLA at 80% on Box. Because task denominators differ, the paper's unweighted mean is not the same as pooling successful trials: FAVLA's chart values correspond to about 71 successes in 85 trials, or 83.5% when trial-weighted. The unweighted task mean is a defensible choice, but it should be named explicitly.

Average peak force is 7.7 N for FAVLA on Gear and 9.9 N on Box. The vision-only baseline records 12.0 N and 12.2 N respectively. The strongest non-FAVLA force values are 10.9 N on Gear and 10.0 N on Box, so the practical margin over the best listed force-aware comparator is much narrower on Box than the comparison with vision-only `pi_0` suggests.

### Ablations and Failure Evidence

The cumulative component table starts at 50% Box / 10% Wiping for vision only, rises to 65% / 60% with the force-injected action expert, to 70% / 60% after force-variance prediction, and to 80% / 70% after adaptive inference. This supports the full construction and a strong force-injection effect, but cumulative additions do not isolate interactions or establish that the variance head alone improves both tasks.

For static action-expert ratios `n=1,2,4`, the frequency chart reports USB success of 52%, 52%, and 60% and Gear success of 70%, 77%, and 90%. Adaptive scheduling reports 80% and 93% (rounded in the figure). The result supports phase-dependent scheduling in these two tasks, but the paper does not report latency, compute, energy, action-update timing, or a matched average-number-of-calls baseline.

The appendix names four failure types: force ambiguity causes premature USB gripper opening; gear misalignment can still exceed the safety threshold; overly cautious box force can cause slip; and incorrect wiping trajectories leave residue. These failures are valuable because they show that lower average peak force is not equivalent to correct contact interpretation or safe completion.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | A slow VLM plus force-injected fast action expert can revise action chunks using newer contact information. | Author method claim | E2 | Directly specified in equations and diagrams; runtime implementation unavailable. | High for reporting |
| C2 | FAVLA improves average task success by 13.8 points over the strongest reported mean baseline. | Author empirical claim | E3 | Numerically supported by the unweighted per-task means. | High for transcription; medium for generalization |
| C3 | FAVLA performs best across all tasks. | Author empirical claim | E3 | Overstated: Box Flipping is a three-way tie at 80%. | High |
| C4 | Adaptive frequency is better than static ratios. | Author empirical claim | E3 | Supported on USB and Gear in one chart; compute and matched-call controls are missing. | Medium-high |
| C5 | FAVLA reduces manipulation force. | Author empirical claim | E3 | Supported for average peak force on two tasks; no variance, full traces, impulse metrics, or safety-event rate is reported. | Medium-high |
| C6 | The method preserves high-frequency force cues. | Author mechanism claim | E2, E4 | Plausible architecturally, but training data are downsampled to 30 Hz and evaluation control rates are under-specified. | Medium-low |
| C7 | The first random draw was eligible and source-complete before review. | Process claim | E5, E7 | Dedup was clear; bounded repair converted a partial unit to complete before synthesis. | High |

## Methodology

- `Research objective`: Review one uniformly selected eligible archive paper source-first, preserve evidence and uncertainty, connect it to exactly three related DEP entries, and produce a DEP-ready public manuscript.
- `Sources inspected`: Canonical arXiv metadata, complete 16-page PDF, official full-paper HTML, TeX/source package, license link, focused public code search, live Black Lake and Black-Lake-Data README authorities, and exactly three related Black Lake manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, grouped them by unique parent directory, sorted the units, and drew one zero-based index uniformly with PowerShell `Get-Random`.
- `Inclusion criteria`: Sources had to establish identity, mechanism, data, evaluation, limitations, source integrity, repository rules, or direct conceptual overlap.
- `Exclusion criteria`: Abstract-only material, third-party summaries, unverified code claims, and tangential DEP records were excluded from evidence. Original source files were excluded from the public repository by design.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product-research, replication, and provenance analysis.
- `Evidence handling`: Major claims map to evidence IDs; author claims and reviewer interpretations are labeled separately; numbers were cross-checked across PDF figures, HTML tables, and TeX sources.
- `Uncertainty handling`: Missing seeds, intervals, code, datasets, runtime rates, latency, and independent reproduction remain visible as limitations.
- `Extraction process`: The full HTML and TeX sections were read directly. All 16 PDF pages were rendered and visually inspected inside the private archive; temporary renderings were removed after inspection.
- `Version control`: Review is pinned to arXiv:2602.23648v1. No official software commit exists in the inspected source set.
- `Random selection`: 75,780 PDF files represented 75,777 unique PDF-parent units. The uniform draw selected zero-based index 47,262. The first draw was accepted with zero duplicate exclusions, zero other exclusions, and zero reselections.
- `Deduplication`: Searches covered Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, relevant Black-Lake-Data trees, arXiv ID, DOI, normalized title, slug family, and prior-24-hour markers. One metadata-only author-inventory row was found; it is not a processed DEP artifact.
- `Reviewer stance`: Skeptical paper review, DEP preservation, simulation-first implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2602.23648v1 and exactly three processed DEP entries addressing action routing, sensor calibration, and safety constraints.
- `Temporal boundary`: Public sources and repository context inspected through 2026-07-22.
- `Evidence limits`: No code, weights, dataset, run logs, training seeds, confidence intervals, full force traces, wall-clock control rates, latency distributions, or hardware reproduction were available.
- `Assumptions`: Figure percentages accurately represent the stated trial counts; the TeX source corresponds to the inspected PDF; baseline fine-tuning followed the stated common recipe.
- `Constraints`: Physical-robot examples are safety-relevant. Proposed implementations remain offline or simulation-only until independent controls, calibration, and human supervision are established.
- `Out of scope`: Reproducing training, validating the robot safety envelope, comparing every cited tactile/force model, or certifying industrial deployment.
- `Intended use`: Research review, DEP deposition, benchmark design, simulation planning, and engineering handoff.
- `Audience`: Robotics researchers, embodied-AI engineers, control engineers, and safety reviewers.
- `Reproducibility boundary`: The architecture can be reconstructed conceptually, but exact replication requires unavailable code, task data, force preprocessing, timing details, sensor calibration, and evaluation protocols.
- `Data sensitivity`: Scholarly sources are public; robot trajectories and sensor data were not collected into this deposit.

## Observations

- `Observed pattern`: FAVLA turns sensor-rate mismatch into a conditional-compute design: slow context is cached while fast action generation is selectively repeated.
- `Technical implication`: A useful reproduction must log both semantic-cycle and action-expert timing, sensor sample age, cache age, number of expert calls, and force events.
- `Contradiction or tension`: The motivation emphasizes 100-1000 Hz force cues, but the described training corpus downsamples recorded 200 Hz force to 30 Hz.
- `Contradiction or tension`: “Best across all tasks” conflicts with the 80% three-way tie on Box Flipping.
- `Derived observation`: Unequal task trial counts make the reported 80.8% unweighted mean differ from the approximately 83.5% pooled-trial rate.
- `Open question`: Does adaptive scheduling outperform a static policy with the same average number of action-expert calls and the same sensor-to-action latency?
- `Reviewer hypothesis`: The largest transferable gain may come from putting fresh force information close to the action tokens, while the variance scheduler mainly allocates when that pathway is exercised.

## Considerations

Physical deployment requires more than average success and peak force. Evaluation should include force impulse, contact duration, overshoot, collision/safety-stop rate, object damage, missed contact, slip, action jerk, end-to-end latency, deadline misses, and recovery success. All measures need distributions and confidence intervals.

Sensor integrity is a first-class dependency. Calibration error, timestamp drift, frame mismatch, force bias, saturation, temperature, and tool changes can corrupt the very signal used for adaptive scheduling. Every run should bind a calibration identifier and freshness check to the model/evaluation manifest.

The variance head predicts a future statistic from current context, so errors can cause both underreaction and unnecessary repeated inference. A fail-closed system needs maximum force/velocity envelopes, stale-input rejection, bounded compute, a deterministic fallback, emergency-stop integration, and human supervision independent of model confidence.

The dataset is small and task-specific. The qualitative perturbations are useful but do not replace pre-registered distribution-shift tests across objects, friction, compliance, wear, lighting, camera occlusion, sensor dropout, and operators.

## Strengths

- The design matches different semantic and contact timescales instead of forcing every modality into one update rate.
- Force is injected directly into multiple action-expert layers, giving a clear alternative to prefix concatenation.
- The scheduler has an explicit supervised target and a bounded minimum execution count.
- The evaluation includes four physical tasks, force-aware baselines, component ablations, frequency ablations, force measurements, and explicit failure examples.
- Tables and figures provide enough detail to reconstruct the headline arithmetic and identify the Box tie and averaging convention.
- The appendix exposes dataset size, sensor rates, model sizes, LoRA settings, compute, augmentations, and failure modes.

## Weaknesses

- No official code, model weights, dataset, evaluation scripts, or pinned environment were identified.
- Trial counts are small, training seeds are absent, and no uncertainty intervals or statistical tests are reported.
- The paper does not fully specify actual VLM/AE/control frequencies, sensor-to-action latency, force-window sampling, or average adaptive compute.
- Training data are downsampled to 30 Hz despite the high-frequency-force motivation.
- Component ablations are cumulative rather than factorial, so interactions are not isolated.
- The adaptive-frequency comparison lacks a matched-average-compute baseline and latency/energy accounting.
- Peak force is reported only as an average for two tasks, without distributions, impulses, duration, or safety-event counts.
- Baseline parity is difficult to audit without code and complete tuning details.
- Claims of broad robustness/generalization rely substantially on selected qualitative sequences.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish code, data schema, checkpoints, configs, and timing traces | Reproducibility | Current implementation details are insufficient for exact replication | Auditable method and baseline parity | Maintenance, rights, and storage work | Clean-environment reproduction of every figure/table |
| Report actual multi-rate timing | Systems | Architectural “fast” does not establish wall-clock control rate | Connects method to reactive-control claims | Instrumentation overhead | p50/p95/p99 sensor age, VLM/AE latency, call count, and deadline misses |
| Add matched-compute scheduler controls | Causal attribution | Adaptive frequency may simply use more action-expert calls | Isolates scheduling value | More experiments | Match average/peak calls for static, oracle, random, threshold, and adaptive policies |
| Preserve native-rate force or compare rates | Data pipeline | 30 Hz downsampling may remove the targeted cue | Tests whether high-rate force drives gains | Larger sequences and synchronization burden | 30/60/100/200 Hz ablation with identical tasks and seeds |
| Add repeated trials and hierarchical uncertainty | Statistics | Per-task denominators are small and unequal | Honest uncertainty and pooled/task-level interpretation | More robot time | Binomial intervals plus mixed-effects or hierarchical analysis |
| Expand contact safety metrics | Safety | Mean peak force hides timing and rare hazards | Better safety and quality assessment | Sensor calibration and annotation effort | Force distribution, impulse, duration, stop/damage/slip rates, and recovery |
| Test sensor/calibration failures | Robustness | Scheduler depends on force integrity | Reveals unsafe failure paths | Hardware-in-loop complexity | Bias, drift, dropout, saturation, delay, remount, and stale-cache fault injection |

## Potential Implementations

1. **Multi-rate contact replay auditor**
   - `User`: Robotics evaluation engineer.
   - `Goal`: Determine whether a policy actually uses newer force information between semantic updates.
   - `Core mechanism`: Replay synchronized vision, state, force, cache, scheduler, and action traces; compute sensor age, update ratios, force-event response, and missed deadlines.
   - `Required inputs`: Approved offline trace schema, calibration identifier, model/config hashes, task outcomes, and force safety labels.
   - `Outputs`: Timing/evidence card and failure slices.
   - `Risk controls`: Offline-only, no robot driver, allowlisted aggregate export, and source-data retention outside the DEP.
   - `Evaluation`: Detect seeded delay/dropout faults and reproduce known call schedules deterministically.
2. **Adaptive scheduler benchmark**
   - `User`: Embodied-AI researcher.
   - `Goal`: Compare learned scheduling with static, matched-compute, random, threshold, and oracle policies.
   - `Core mechanism`: Run a simulator or frozen replay with identical action experts and fixed compute budgets.
   - `Required inputs`: Public/synthetic contact traces, policy outputs, task simulator, and cost model.
   - `Outputs`: Success-force-latency-compute frontier with intervals.
   - `Risk controls`: Simulation only; no physical commands; deterministic seeds and bounded scenarios.
   - `Evaluation`: Improvement at matched average and maximum calls, not only unconstrained success.
3. **Layered contact safety gate**
   - `User`: Robot controls and safety team.
   - `Goal`: Keep learned action chunks inside independently defined force, velocity, workspace, and solver limits.
   - `Core mechanism`: Combine calibration freshness, state-age checks, force envelopes, constraint evaluation, and a deterministic fallback around a mocked FAVLA proposal interface.
   - `Required inputs`: Synthetic state/force streams, constraint policy, fallback status, and action proposals.
   - `Outputs`: Allow/reject/fallback decisions with evidence traces.
   - `Risk controls`: Simulation-only MVP, fail-closed behavior, no hardware interface, and human review before any later stage.
   - `Evaluation`: Zero released actions when any calibration, freshness, constraint, or fallback gate is invalid.

## Three Ways to Exercise This Research

1. **Reconstruct the evidence arithmetic:** Objective: verify every success and force comparison. Inputs: transcribed Figure 6 and Tables 1-2. Method: map percentages to trial counts, compute unweighted and pooled rates, and add binomial intervals. Output: a reproducible evidence table. Success criterion: all source values reconcile and averaging conventions are explicit. Stop condition: any percentage cannot map to the stated denominator. Safety boundary: numerical analysis only.
2. **Synthetic multi-rate replay:** Objective: test whether fresh force reduces response delay. Inputs: generated force spikes, slow visual context, a stub action expert, and fixed/adaptive schedulers. Method: sweep sensor rate, delay, dropout, and compute budget. Output: response-time and false-trigger curves. Success criterion: the adaptive rule improves response at matched compute without increasing unsafe triggers. Stop condition: timing assumptions are not versioned. Safety boundary: synthetic data and no actuation.
3. **Constraint-and-fallback drill:** Objective: verify that learned proposals cannot bypass independent limits. Inputs: synthetic actions, force envelopes, stale-state flags, calibration status, and a safe-stop stub. Method: inject overshoot, delay, solver failure, and sensor faults. Output: rejection/fallback ledger. Success criterion: every invalid condition fails closed. Stop condition: any path emits an action with missing evidence. Safety boundary: simulation-only.

## Example MVP Product

- `Product name`: ContactLoop Audit.
- `Target user`: Robotics researchers reviewing multi-rate contact-aware policies before simulator or hardware studies.
- `Problem`: Success-rate charts do not prove that high-rate force reached action generation in time, that adaptive compute was fairly compared, or that proposals stayed inside an independent safety envelope.
- `Core workflow`: Import a versioned offline trace manifest; validate frames, units, calibration, and timestamps; reconstruct semantic and action-expert cycles; detect force events; score response delay and compute; run a mocked constraint/fallback gate; export Markdown and JSON evidence cards.
- `Data requirements`: Synthetic or authorized offline time-series aggregates, model/config identifiers, task labels, calibration version, scheduler decisions, action proposals, and constraint outcomes. Raw robot data remain outside public outputs.
- `Architecture`: Local CLI, schema validator, deterministic trace aligner, event detector, scheduler comparator, constraint/fallback simulator, and public-safe exporter.
- `Success metrics`: Deterministic reruns, detection of seeded delay/dropout/unit faults, matched-compute comparisons, complete evidence lineage, zero raw source files exported, and zero allowed actions when a gate is invalid.
- `Risk controls`: No robot drivers, no network requirement, allowlisted fields, fail-closed schema and timing checks, explicit non-certification label, and human approval before any expansion.
- `Limitations`: Cannot reproduce unavailable FAVLA weights/data, prove physical safety, model unobserved contact physics, or replace platform-specific validation.
- `MVP boundary`: Offline evidence analysis and synthetic constraint drills only; no training, online control, or hardware actuation.
- `Deployment model`: Local CLI or notebook in an approved research environment.
- `Evaluation plan`: Unit/frame schema tests, deterministic timing fixtures, seeded faults, known averaging cases, and independent reviewer comparison.
- `Failure modes`: Timestamp wrap, unit mismatch, stale calibration, incomplete traces, hidden scheduler calls, force saturation, mislabeled outcomes, and overly permissive fallback assumptions.
- `Maintenance plan`: Version trace schemas, gate policies, and comparison methods; retain a synthetic regression suite; require re-review after any model, sensor, or timing change.

## Related Research and Reading

Exactly three Black Lake DEP entries were selected for concrete conceptual overlap:

| Item | Type | Relevance | Repository-Relative Path / Public URL |
|---|---|---|---|
| Semantic Skill MoE Policies | Related DEP | Both separate semantic context from action generation and enforce consistency across action chunks. The DEP adds auditable skill-conditioned routing, rare-skill coverage, and route-stability questions that complement FAVLA's force-conditioned execution. | `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md` / https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-Semantic%20Skill%20MoE/semantic_skill_moe_manuscript.md |
| iKalibr Calibration | Related DEP | FAVLA depends on correctly aligned camera, proprioception, and force streams. The calibration DEP supplies the spatial/temporal provenance, excitation, drift, and downstream evidence gates that FAVLA assumes but does not evaluate. | `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` / https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md |
| RRT-CBF Motion | Related DEP | FAVLA proposes learned actions and lower forces; RRT-CBF distinguishes performance from admissibility through explicit constraints, state freshness, solver status, tracking, and fallback. | `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` / https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2602.23648 | Identity, authors, submission date, abstract, DOI, license, and source links | 2026-07-22 | Primary metadata; abstract not used alone for results |
| R2 | https://arxiv.org/pdf/2602.23648 | Full method, figures, tables, experiments, appendix, and failure cases | 2026-07-22 | Complete private copy inspected and withheld |
| R3 | https://arxiv.org/html/2602.23648 | Full-text cross-check, equations, captions, tables, and references | 2026-07-22 | Verified complete rendering |
| R4 | https://arxiv.org/e-print/2602.23648 | TeX equations, exact tables, captions, data/training details, and appendix | 2026-07-22 | Source archive withheld |
| R5 | https://doi.org/10.48550/arXiv.2602.23648 | Persistent identity | 2026-07-22 | arXiv-issued DOI |
| R6 | https://creativecommons.org/licenses/by/4.0/ | License identified by the canonical arXiv record | 2026-07-22 | Source files still withheld by task policy |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-Semantic%20Skill%20MoE/semantic_skill_moe_manuscript.md | Action-chunk routing and semantic-control synthesis | 2026-07-22 | Related DEP 1 of 3 |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Multi-sensor timing/calibration synthesis | 2026-07-22 | Related DEP 2 of 3 |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md | Constraint, tracking, and fallback synthesis | 2026-07-22 | Related DEP 3 of 3 |

## Appendix

### Selection and Dedup Record

| Field | Value |
|---|---|
| Enumeration | `rg --files -g "*.pdf"` against the private archive |
| Candidate PDFs | 75,780 |
| Unique PDF-parent paper units | 75,777 |
| Random method | Sorted unique units plus uniform PowerShell `Get-Random` index |
| Selected zero-based index | 47,262 |
| Selected ID | arXiv:2602.23648 |
| Duplicate exclusions | 0 |
| Other exclusions | 0 |
| Reselections | 0 |
| Inventory-only match | One metadata row; not a processed DEP artifact |
| Prior-24-hour same-paper markers | 0 |

### Complete-Source Integrity Record

The initial unit was partial: a valid 22,218,424-byte PDF was present, but full-paper HTML and the companion verification bundle were missing. Review stopped. One bounded direct-HTTPS repair preserved the PDF and collected official metadata HTML, official full-paper HTML, and the source archive. The local README, attribution/provenance, CSV summary, preflight manifest, and verification report were updated before review resumed.

| Check | Observed | Result |
|---|---:|---|
| PDF bytes | 22,218,424 | Pass: at least 10 KB |
| PDF header | `%PDF-` | Pass |
| PDF trailing marker | `%%EOF` present | Pass |
| Full-paper HTML bytes | 212,377 | Pass: at least 5 KB |
| HTML body characters | 56,054 | Pass: at least 2,000 |
| HTML article/main/LaTeXML marker | Present | Pass |
| HTML heading/section markers | 54 | Pass: at least 2 |
| Paper-structure term classes | 7 | Pass: at least 2 |
| Abstract/error/conversion marker | Absent | Pass |
| Metadata HTML | 43,391 bytes; metadata only | Present; not counted as the paper |
| Source archive | 20,843,348 bytes | Present; withheld |
| Remaining partial files | 0 | Pass |
| Final classification | `complete` | Gate passed |

### Reproducibility Checklist

- [ ] Obtain an author-verified code release, checkpoint, dataset manifest, baseline configs, and evaluation scripts.
- [ ] Pin robot, controller, camera, force sensor, calibration, firmware, units, coordinate frames, and time bases.
- [ ] Specify actual sensor, VLM, action-expert, and actuation rates plus all queueing and end-to-end latencies.
- [ ] Compare native and downsampled force rates under identical seeds and task setups.
- [ ] Reproduce the five methods with equal data, tuning budgets, LoRA placement, checkpoints, and stopping rules.
- [ ] Add repeated training seeds and more physical trials with task-level and hierarchical uncertainty.
- [ ] Match adaptive and static policies by average and maximum action-expert calls.
- [ ] Report force distributions, impulse, duration, safety stops, damage, slip, jerk, and recovery.
- [ ] Inject calibration, delay, dropout, bias, saturation, stale-cache, and compute-overrun faults.
- [ ] Keep physical testing supervised and inside independently reviewed force, velocity, workspace, and fallback limits.

### Source Locality Statement

The verified PDF, full-paper HTML, metadata HTML, source archive, extracted material, provenance records, and temporary renderings remained in the private archive. Temporary page renderings were removed after visual review. This public DEP contains no source document, no private filesystem locator, and no `.source/` directory.

## Attribution Block

- Sources R1-R6 support the paper identity, license, method, data, experiments, figures, tables, failure cases, and source-integrity summary.
- Sources R7-R9 support conceptual synthesis only and do not validate FAVLA's empirical results.
- The reviewer-derived weighted-rate calculation, tie qualification, reproduction priorities, and implementation proposals are interpretations grounded in the cited source values.
- Original source files were withheld locally and were not uploaded, staged, copied, or attached.
