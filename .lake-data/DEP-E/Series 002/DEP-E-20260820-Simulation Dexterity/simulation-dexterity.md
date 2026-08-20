---
title: "Simulation Dexterity - DEP-E"
generated_at: "2026-08-20T00:03:02Z"
artifact_type: "DEP research artifact"
primary_subject: "Simulation Pre-training for Dexterity as a source of transferable visuomotor priors for bimanual dexterous manipulation."
source_status: "URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-20"
temporal_cutoff: "2026-08-20"
primary_url: "https://arxiv.org/abs/2608.15917"
stable_identifier: "arXiv:2608.15917v1"
confidence_summary: "Moderate: the full primary manuscript and official project page were inspected, but no code, data, model, simulator, or robot experiment was independently executed."
safety_scope: "Research review and evaluation planning; no physical robot control instructions."
distribution_notes: "Public URLs only; no source files or restricted datasets redistributed."
---

# Simulation Dexterity - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S0 | Selected Black-Lake-Data DEP | Primary intake record | Markdown source bundle | Source commit `e127946890a3fe7d2ffc6d53e2b6e60b14907197` | `Black-Lake-Data/.lake-data/DEP-20260819-Research Data 2234 D0822` | Repository content used as an intake locator; no local path published | 2026-08-20 | Both Markdown files inspected |
| S1 | *Pre-training Visual Dexterity in Simulation* | Primary research artifact | arXiv HTML and metadata | arXiv:2608.15917v1; submitted 2026-08-16 | https://arxiv.org/abs/2608.15917 and https://arxiv.org/html/2608.15917 | arXiv page exposes its perpetual non-exclusive license; redistribution rights for dataset/code were not assessed | 2026-08-20 | Full HTML inspected, including appendix and tables |
| S2 | SPD project page | Official author context | Project website | Access snapshot 2026-08-20 | https://spd.bot/ | Public web surface; no explicit code or dataset license was visible in the inspected page text | 2026-08-20 | Overview, model, experiment, and media sections inspected |
| S3 | `$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control` | Methodological neighbor | arXiv metadata and abstract | arXiv:2410.24164v4 | https://arxiv.org/abs/2410.24164 | Related-reading context only | 2026-08-20 | Canonical record and abstract inspected |
| S4 | *DexUMI* | Alternative data interface | arXiv metadata and abstract | arXiv:2505.21864v3 | https://arxiv.org/abs/2505.21864 | Related-reading context only | 2026-08-20 | Canonical record and abstract inspected |
| S5 | *EgoScale* | Alternative pre-training source | arXiv metadata and abstract | arXiv:2602.16710v1 | https://arxiv.org/abs/2602.16710 | Related-reading context only | 2026-08-20 | Canonical record and abstract inspected |
| S6 | *Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware* | Action-chunking baseline | arXiv metadata and abstract | arXiv:2304.13705v1 | https://arxiv.org/abs/2304.13705 | Related-reading context only | 2026-08-20 | Canonical record and abstract inspected |

Producing organizations for S1 are Stanford University, MIT, and Scale AI. Authors are Sarthak Kamat, Adam Rashid, Satvik Sharma, Aseem Doriwala, Chelsea Finn, Phillip Isola, and C. Karen Liu. The work is an arXiv preprint in Robotics, Artificial Intelligence, and Computer Vision; no peer-reviewed venue was stated on the inspected record.

No source files were collected. The paper says the `spd-75h` dataset, `spd-vr` software, and six scenes are released, but the inspected project-page text did not expose stable download or repository locators. Their availability, contents, checksums, and licenses were therefore not verified.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S0 | Primary intake record | DEP inventory, deposited finding, original arXiv locator, and source caveat | Selection provenance and intake boundary | High | Intake summary is abstract-level and contains encoding defects; it is not used for empirical claims |
| E2 | S1 | Primary paper | Introduction, method, Figures 1 and 5 captions, Sections 3-5, Tables 1-5, and Appendix A | Data collection, architecture, fine-tuning, evaluation, ablations, limitations, and hyperparameters | High for what the paper reports | Preprint evidence; no independent execution, raw trials, code, data, or model inspection |
| E3 | S2 | Official project page | Method overview, 75-hour collection description, model description, experiment summary, and rollout presentation | Cross-check of the authors' public framing and media availability | Medium | Page is mutable; videos were not scored independently; no stable release links were visible |
| E4 | S3 | Primary-paper record | Canonical identity and abstract of the flow-model policy cited as architectural context | Related policy-model context | Medium | Abstract-level inspection only; not used to validate SPD results |
| E5 | S4 | Primary-paper record | Canonical identity and abstract of a wearable human-hand interface | Alternative approach to reducing embodiment mismatch | Medium | Abstract-level inspection only; cross-paper metrics are not directly comparable |
| E6 | S5 | Primary-paper record | Canonical identity and abstract of large-scale egocentric human-data pre-training | Alternative data-scaling route | Medium | Abstract-level inspection only; different embodiment, data scale, and evaluation |
| E7 | S6 | Primary-paper record | Canonical identity and abstract of ACT-based bimanual imitation learning | Action-chunking and bimanual behavior-cloning context | Medium | Abstract-level inspection only; different hardware, tasks, and success metrics |

## Executive Summary

Simulation Pre-training for Dexterity (SPD) asks whether human teleoperation in a physics simulator can provide useful pre-training data for real, multi-fingered robot manipulation. Five operators collected about 75 hours of action-labeled demonstrations across six simulated scenes in one week. The authors pre-trained a 222M-parameter causal diffusion transformer, then fully fine-tuned it with roughly 1-2 hours of physical demonstrations per task on a 56-degree-of-freedom bimanual platform. Across five related real-world tasks and 20 trials per checkpoint, the paper reports higher task progress for simulation-pre-trained policies than for the same architecture trained from scratch (E2). The official project page presents the same mechanism and public rollout videos (E3).

The strongest controlled result is architectural: a 32-step history window paired with an 8-step action chunk averaged 76.7% normalized progress after SPD pre-training versus 58.9% from scratch, an approximately 18-point difference reported by the authors. Short chunks without history were unstable, while history supplied temporal context and preserved reactivity (E2). This suggests that transferable dexterity depends on the interaction between data source and policy memory, not only dataset scale.

The evidence supports feasibility on the evaluated platform and task family, not general sim-to-real dexterity. Objects in physical evaluation were similar to those in pre-training; scene diversity was limited; simulator contact parameters were tuned; only 20 trials were run per checkpoint; and code, data, model weights, raw trial records, and hardware were not independently inspected. Reviewer confidence is therefore moderate. SPD is best treated as a promising data-acquisition and representation strategy whose release integrity, sensitivity to simulator mismatch, training variance, and out-of-distribution transfer still require audit.

## Detailed Summary

### Problem and research position

Dexterous robot hands are expensive and fragile data-collection platforms. Conventional robot teleoperation preserves action labels and embodiment, but limits collection throughput. Human video scales more easily, yet it lacks native robot actions and introduces pose-estimation, contact-occlusion, and retargeting errors. SPD occupies a middle position: people teleoperate the target robot embodiment inside simulation, so trajectories retain robot action labels while avoiding continuous use of physical hardware (E2).

The paper's novelty is not simulation-based control by itself. Simulation is used as a multi-task human demonstration source for pre-training a policy that will later be adapted with limited real data. The authors contrast this with task-specific simulation reinforcement learning and with data sources that require post-hoc transfer from human motion.

### Collection mechanism

`spd-vr` streams a MuJoCo scene to a Meta Quest 3 headset. Hand and wrist tracking drive the simulated bimanual robot through inverse kinematics. Simulation runs at 480 Hz; tracking, control, streaming, and recording operate at 60 Hz. Six scenes cover spelling blocks, dishes, mugs, bottles, cups, and Jenga bricks. Task resets randomize prompts, assets, physical properties, and initial object positions. Five operators collected about 2,000 long-horizon episodes over one week (E2).

The appendix specifies 1,930 total episodes and approximately 75 hours. Table 2 lists 1,916 episodes and 4,516 minutes because it omits tasks with fewer than ten episodes. This is a reporting-scope difference rather than evidence of a substantive contradiction, but a released manifest should make the distinction machine-checkable. After collection, spans with more than ten seconds of no hand-object contact are removed. Images are rendered at 224 by 168 pixels, with segmentation-assisted color and texture augmentation plus bilateral symmetry augmentation (E2).

### Real-world alignment

Physical data uses two upgraded YAM Pro arms, each with a 22-DoF Sharpa Wave hand, and three RealSense D405 cameras. The simulation and real systems align camera placement, hands, arms, and similar objects. Real teleoperation replaces headset hand tracking with Manus gloves for fingers and a Quest controller for wrists. Recorded streams are resampled to a 30 Hz training grid (E2).

This alignment is central to the transfer hypothesis. SPD avoids a human-to-robot embodiment transformation during pre-training, but it does not eliminate the simulation-to-reality gap in appearance, contact, latency, sensing, or actuator dynamics. Fine-tuning supplies the missing physical adaptation.

### Policy and training

The policy is a 222M-parameter diffusion transformer. It consumes interleaved tokens for 56-dimensional proprioception, previous action, multi-view images, and noised future action chunks. Three-camera images are encoded by a frozen DINOv3 ViT-B/16 and pooled through learned queries. An eight-block transformer uses causal, 32-timestep sliding-window attention; an action-denoising expert has 58M parameters. Each training sequence spans 256 timesteps at 30 Hz, while images and action chunks are sampled every eight steps (E2).

Training uses a flow-matching velocity objective. All chunks in a sequence are denoised in parallel under a causal mask, and inference reuses a rolling key-value cache. On action boundaries, ten Euler steps integrate the flow ordinary differential equation and emit eight actions. Pre-training used batch size 64, a fixed learning rate of `1e-3`, 170,000 steps, Muon for matrix parameters, AdamW elsewhere, and Gaussian observation/action noise of 0.03 (E2).

### Evaluation and results

The authors fully fine-tune one policy per physical task using 44-121 minutes and 161-270 episodes. Tasks are bottle tossing, plate racking, cup stacking, Jenga play, and mug hanging. Each checkpoint receives 20 trials per task from randomized initial object placements. Progress is rubric-based and normalized by the maximum score rather than reported only as binary success (E2).

For the chosen 32-step-history, 8-step-chunk configuration, SPD progress scores are 80.6, 93.3, 85.0, 55.6, and 68.8 across the five tasks. The corresponding from-scratch scores are 66.9, 80.0, 65.0, 35.0, and 47.5. Their means are 76.7 and 58.9, respectively. The paper summarizes this as an 18-point gain. The other three window/chunk configurations improve by no more than about three points on average, indicating that the benefit is concentrated in the configuration combining history with short action chunks (E2).

The same architecture and task-specific real demonstrations are used for the pre-trained and from-scratch comparison, which isolates initialization more cleanly than comparisons across model families. However, the manuscript does not provide independent seeds, confidence intervals for the ablation table, raw trial outcomes, or an equal-cost comparison against human-video, mixed-data, or additional-real-data pre-training.

### Conclusion and stated limits

The authors conclude that simulation teleoperation is a viable source of pre-training data for their evaluated real-world dexterous tasks. They explicitly limit the result: simulation physics must be realistic enough for useful operator behavior; current scenes and objects are narrow; and physical evaluation uses objects similar to those seen in simulation. They propose broader scenes, objects, mixed data sources, and reinforcement-learning continuation as future work (E2).

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Five operators collected approximately 75 hours of multi-task simulation demonstrations over one week. | Author claim | E2, E3 | Directly documented; appendix gives 1,930 total episodes while the filtered table accounts for 1,916. | High as source-reported metadata |
| C2 | Simulation-pre-trained checkpoints make more progress than from-scratch behavior cloning on all five evaluated physical tasks. | Author claim / benchmark result | E2 | Supported by the reported 20-trial-per-checkpoint protocol and task-progress plots/table; raw trials were not inspected. | Medium-high |
| C3 | A 32-step history with an 8-step action chunk yields an approximately 18-point average-progress benefit from SPD pre-training. | Author claim / derived check | E2 | Recalculation from Table 1 gives about 76.7% versus 58.9%, consistent with the paper. | High for the reported table |
| C4 | History conditioning lets the policy use shorter, more reactive chunks without losing temporal coherence. | Author interpretation | E2 | The four-way ablation supports the association; it does not isolate every possible architectural or optimization confound. | Medium-high |
| C5 | Simulation teleoperation is a viable pre-training source for real dexterous manipulation. | Author conclusion | E2, E3 | Supported on five related tasks and one bimanual platform; too broad if interpreted as general dexterous transfer. | Medium |
| C6 | SPD's practical value comes from jointly reducing embodiment mismatch and giving the policy temporal memory. | Reviewer interpretation | E2 | Mechanistically consistent with collection alignment and the ablation, but not separately tested as a causal decomposition. | Medium |
| C7 | The current public evidence is sufficient for replication. | Unsupported proposition | E2, E3 | Not established: the paper claims releases, but stable dataset/software/model locators and licenses were not visible in the inspected public page text. | Low |

## Methodology

- `Research objective`: Determine what SPD establishes about simulation-collected pre-training for dexterous manipulation, preserve its mechanism and evidence, and translate the result into bounded evaluation and implementation paths.
- `Sources inspected`: Both Markdown files in the selected source DEP; the complete arXiv v1 HTML paper including methods, experiments, tables, conclusion, and appendix; the official SPD project page; and canonical arXiv records/abstracts for four methodological neighbors.
- `Discovery strategy`: Began from the selected DEP's primary locator, followed the paper's official project link, inspected the full paper rather than relying on the intake abstract, and used references named by the paper to select authoritative related reading.
- `Inclusion criteria`: Primary or near-primary sources that identify the research object, document its method/results, expose official project context, or clarify a directly relevant alternative data or action-modeling strategy.
- `Exclusion criteria`: Search-result summaries, news, social commentary, and unrelated secondary explanations were excluded. Related papers were not treated as validation of SPD because only their canonical records and abstracts were inspected.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product-research, safety/ethics, and replication analysis.
- `Evidence handling`: Quantitative claims were traced to the paper's tables, sections, or appendix; author claims, reviewer interpretation, derived arithmetic, and unsupported propositions are labeled separately.
- `Uncertainty handling`: Missing release locators, unexecuted artifacts, task similarity, small trial counts, absent seed analysis, and mutable web surfaces are stated as limits rather than inferred away.
- `Extraction process`: Text, table values, figure captions, metadata, and hyperparameters were inspected through official arXiv HTML and the official project page. No PDF figures were independently measured.
- `Version control`: The source DEP is pinned to repository commit `e127946890a3fe7d2ffc6d53e2b6e60b14907197`; the paper is pinned to arXiv v1. The project page is recorded by access date because no commit pin was visible.
- `Cross-checking`: The 18-point ablation claim was recomputed from Table 1. Dataset totals and physical-data durations were compared across the main text and appendix.
- `Reviewer stance`: Source-first manuscript review, critique, DEP-ready preservation, replication planning, and bounded product translation.

## Scope, Constraints, and Assumptions

- `Scope`: SPD's simulated teleoperation data, real-world fine-tuning, policy architecture, five-task evaluation, action-history ablation, release claims, limitations, and practical follow-up paths.
- `Temporal boundary`: Public evidence accessible through 2026-08-20; primary paper version is arXiv:2608.15917v1.
- `Evidence limits`: No raw trajectories, source code, dataset manifest, trained weights, simulator scenes, videos-as-data, hardware logs, or physical robot were inspected or executed. The HTML conversion may omit visual nuance from figures.
- `Assumptions`: Table 2's 1,916-episode total differs from the stated 1,930 because the caption says tasks with fewer than ten episodes are omitted. Progress percentages are interpreted exactly as rubric-normalized scores.
- `Constraints`: Public-source review only; no source-file redistribution; no unsafe physical actuation; no claim of peer review, license clearance, or release completeness beyond inspected evidence.
- `Out of scope`: Reproducing training, scoring rollout videos, validating contact physics, auditing operator demographics, conducting hardware safety testing, estimating full compute cost, or comparing commercial readiness.
- `Intended use`: DEP deposition, research review, replication planning, dataset-governance design, and evaluation backlog creation.
- `Audience`: Robotics researchers, imitation-learning engineers, dataset maintainers, and reviewers assessing sim-to-real evidence.
- `Reproducibility boundary`: The paper provides substantial architecture and training detail, but a complete reproduction still requires the claimed released assets, environment specifications, model initialization, raw evaluation records, and compatible hardware.
- `Operational boundary`: Implementation ideas remain simulation-first or audit-oriented until an authorized robotics safety review establishes physical control limits and emergency procedures.
- `Data sensitivity`: Public research metadata only. Future operator recordings may contain biometric or behavioral traces and should receive consent, retention, and access controls.

## Observations

- `Observed pattern`: SPD converts simulator access and human operator time into on-embodiment action data, trading physical wear and reset cost for simulator-fidelity and operator-behavior risk.
- `Observed pattern`: The largest pre-training benefit appears only when policy memory and action horizon are configured together. Treating chunk length as an isolated hyperparameter would miss this interaction.
- `Technical implication`: A transfer benchmark should vary data source, embodiment alignment, context length, and chunk length factorially; otherwise gains may be attributed to "simulation pre-training" that actually depend on one architectural regime.
- `Technical implication`: Rubric-normalized partial progress captures meaningful near-success behavior, but deployment decisions also need binary completion, intervention, collision, force, latency, and damage metrics.
- `Contradiction or tension`: The paper describes released artifacts, yet stable release locators were not visible on the inspected project surface. This may be a publication-timing or extraction limitation, but the current review cannot treat the assets as verified.
- `Open question`: How much of the gain survives on objects, contact properties, camera placements, tasks, or dexterous hands that are materially dissimilar from pre-training?
- `Reviewer hypothesis`: Simulation teleoperation may be most valuable as a structured motor-prior layer combined with smaller quantities of real and human-video data, rather than as a single-source replacement.

## Considerations

Physical deployment adds hazards absent from normalized progress scores: pinching, self-collision, dropped objects, thermal limits, unexpected contact forces, camera occlusion, actuator faults, and operator proximity. Any real implementation needs workspace exclusion zones, torque and velocity limits, watchdogs, emergency stops, anomaly detection, and staged approval from simulation to instrumented bench tests.

Dataset governance also matters. Operator motion can encode behavioral signatures, and reconstruction logs may expose headset or workflow metadata. A production collection system should minimize identity data, separate consent records, document compensation, define retention, and make per-episode provenance and deletion status auditable.

Operationally, the collection economics remain incomplete. Five operators produced 75 hours in a week, but the paper does not expose total annotation effort, simulator-authoring time, hardware and compute cost, rejected/reverted trajectory ratios, calibration labor, or energy use. These should be measured before claiming a cost advantage over additional physical collection or human-video pipelines.

Evaluation should avoid one-number transfer claims. Report per-task stage completion, full success, safety violations, intervention rate, time to completion, calibration sensitivity, uncertainty across seeds, and degradation under controlled visual and physics shifts. The current 20-trial protocol is useful but too small to resolve many rare failure modes.

## Strengths

- The study addresses a real bottleneck: dexterous hands are harder to teleoperate and scale than parallel-jaw systems.
- The pre-training data is action-labeled on the target embodiment, avoiding a major source of post-hoc pose and action inference.
- The comparator uses the same policy architecture and physical demonstrations, making initialization the main experimental difference.
- The paper describes collection rates, scene/task composition, model architecture, training hyperparameters, fine-tuning sizes, and task-scoring rubrics in enough detail to define a serious replication plan.
- The history/chunk ablation tests a concrete control-design mechanism rather than reporting only an aggregate pre-training gain.
- The authors disclose key boundary conditions: tuned physics, limited diversity, and similarity between simulated and physical objects.

## Weaknesses

- Five tasks on one bimanual platform do not establish general dexterous manipulation or cross-embodiment transfer.
- Twenty trials per checkpoint and no visible multi-seed training analysis limit confidence in variance and rare-event behavior.
- Physical objects are similar to pre-training objects, weakening the evidence for broad out-of-distribution generalization.
- There is no equal-budget comparison against more physical demonstrations, large-scale human video, wearable interfaces, reinforcement learning, or mixed-source pre-training.
- The effect of simulator parameter quality is asserted in limitations but not mapped through a sensitivity study.
- Public release claims could not be verified from stable links visible in the inspected project-page text; code, data, weights, licenses, and raw evaluation records remain unaudited.
- Progress rubrics reward partial completion but do not expose safety, damage, intervention, speed, or repeatability.
- Operator diversity, learning curves, fatigue, collection rejection rates, and behavior coverage are insufficiently characterized for dataset-quality conclusions.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish versioned asset manifests with licenses, hashes, scene versions, and expected checks | Reproducibility | Release claims need stable, auditable objects | Independent teams can reconstruct the evidence boundary | Storage, maintenance, and license review | Fresh-environment download and checksum audit |
| Run multi-seed pre-training and fine-tuning with raw trial release | Statistical validity | One training realization may overstate robustness | Variance estimates and stronger causal attribution | Substantial compute and robot time | Confidence intervals, hierarchical task analysis, and preregistered comparisons |
| Sweep contact, friction, mass, latency, texture, and camera mismatch | Simulator sensitivity | Transfer may depend on tuned scenes | Identifies which simulator properties require fidelity | Large factorial experiment | Response surfaces and held-out physical conditions |
| Add dissimilar objects, unseen scenes, novel tasks, and alternate hands | Generalization | Current evaluation remains close to pre-training | Measures the breadth of the learned motor prior | New hardware and data collection | Cross-object, cross-scene, cross-task, and cross-embodiment splits |
| Compare simulation, physical, human-video, wearable, and mixed pre-training at matched budgets | Comparative evidence | Data-source economics and transfer quality are unresolved | Supports rational portfolio decisions | Hard cost normalization and heterogeneous pipelines | Fixed-compute, fixed-human-hour, and fixed-dollar studies |
| Add force, collision, intervention, latency, and damage metrics | Safety and operations | Progress can hide unsafe behavior | Deployment-relevant failure accounting | Instrumentation and conservative test design | Safety-event taxonomy and stop-threshold audit |

## Potential Implementations

### 1. Versioned simulation-collection registry

- `User`: Robotics dataset teams.
- `Goal`: Make every episode reconstructable and auditable.
- `Core mechanism`: Store task prompt, scene version, asset IDs, physics parameters, operator pseudonym, reset seed, contact filters, augmentations, and acceptance/revert events alongside trajectory hashes.
- `Required inputs`: Simulator metadata, collection events, consent records, and storage manifests.
- `Outputs`: Dataset card, lineage graph, per-episode manifest, quality dashboard, and deletion ledger.
- `Risk controls`: Pseudonymization, least-privilege access, biometric-data review, retention limits, and license validation.
- `Evaluation`: Reconstruction rate, manifest completeness, duplicate detection, and audit turnaround time.

### 2. Sim-to-real transfer audit harness

- `User`: Policy researchers and safety reviewers.
- `Goal`: Measure which controlled shifts break transfer.
- `Core mechanism`: Generate a matrix of physics, appearance, sensor, latency, and object shifts; run pre-declared checkpoints and compare partial progress, full success, intervention, and safety events.
- `Required inputs`: Versioned simulator, approved checkpoints, task rubrics, physical calibration records, and bounded robot access.
- `Outputs`: Transfer curves, failure clusters, confidence intervals, and a release decision report.
- `Risk controls`: Simulation-first gates, workspace isolation, velocity/force limits, watchdogs, and human stop authority.
- `Evaluation`: Repeatability, sensitivity coverage, failure detection, and agreement between simulation and physical ranking.

### 3. History/chunk design evaluator

- `User`: Imitation-learning engineers.
- `Goal`: Choose context and action horizons without conflating memory and reactivity.
- `Core mechanism`: Train a factorial grid over history window, action chunk, inference frequency, and data initialization using fixed datasets and compute budgets.
- `Required inputs`: Safe recorded trajectories, model configuration, task rubrics, and deterministic experiment manifests.
- `Outputs`: Pareto frontier for progress, latency, temporal consistency, compute, and safety events.
- `Risk controls`: Offline replay and simulation by default; no automatic transition to physical actuation.
- `Evaluation`: Multi-seed performance, latency, calibration, and robustness under occlusion and perturbation.

## Three Ways to Exercise This Research

1. `Table-reproduction audit`: Objective - verify the reported ablation arithmetic; inputs - Table 1 values and the published scoring definition; method - recompute per-configuration means and differences in a small deterministic notebook; output - a checked summary table; success criterion - exact agreement after stated rounding; stop condition - any cell cannot be traced to the primary paper. Safety boundary - no robot or private data is used.
2. `Synthetic transfer matrix`: Objective - test the evaluation logic without released SPD assets; inputs - a toy manipulation simulator, synthetic trajectories, four history/chunk configurations, and fixed seeds; method - introduce controlled visual and dynamics shifts and measure progress plus safety proxies; output - transfer curves and failure labels; success criterion - the harness detects known injected shifts; stop condition - metrics fail to separate the seeded conditions. Safety boundary - simulation only.
3. `Release-readiness review`: Objective - determine whether SPD can be independently replicated; inputs - public paper, project page, any later official dataset/code/model links, licenses, and checksums; method - build an artifact bill of materials and attempt a clean metadata-only validation before downloading large assets; output - reproducibility scorecard and blocker list; success criterion - every claimed release has a stable version, license, integrity record, and documented expected output; stop condition - redistribution or access terms are unclear.

## Example MVP Product

- `Product name`: DexTransfer Auditbench
- `Target user`: Robotics research teams comparing pre-training sources before committing scarce physical robot time.
- `Problem`: Sim-to-real claims are difficult to compare because data lineage, simulator mismatch, policy horizon, physical task rubrics, and safety events are recorded inconsistently.
- `Core workflow`: Import versioned experiment manifests; validate dataset and checkpoint provenance; define controlled shift matrices; register offline or simulation runs; record physical runs only after safety approval; compute per-task progress, full success, interventions, safety events, and uncertainty; export a signed review report.
- `Data requirements`: Public paper metadata, versioned dataset manifests, simulator parameters, policy configurations, anonymized operator provenance, task rubrics, raw trial outcomes, and safety-event labels. The MVP can begin with synthetic manifests and no biometric data.
- `Architecture`: Local-first CLI and web report; schema-validated YAML/JSON manifests; content-addressed artifact registry; runner adapters for approved simulators; metrics engine; immutable evidence ledger; optional physical-run adapter behind an explicit authorization gate.
- `Success metrics`: At least 95% manifest-field completeness; deterministic metric reproduction; zero unapproved physical commands; detection of all seeded provenance defects; confidence intervals and raw-trial traces for every published aggregate.
- `Risk controls`: Local processing by default, pseudonymous operator IDs, no raw headset imagery in logs, access control, signed manifests, simulation-first workflow, physical-control kill switch, force/velocity limits, and independent safety approval.
- `Limitations`: The MVP validates evidence and experiment structure; it does not make a policy safe, reproduce SPD without released assets, or guarantee simulator fidelity.
- `MVP boundary`: Metadata validation, synthetic experiments, and report generation only; no autonomous robot deployment.
- `Deployment model`: Local CLI plus browser dashboard in an authorized research environment.
- `Evaluation plan`: Unit tests for schema and arithmetic, golden synthetic manifests, injected provenance faults, repeated fixed-seed simulator runs, and a safety review before any hardware adapter is enabled.
- `Failure modes`: Incorrect task mappings, hidden dataset overlap, stale simulator versions, mis-scaled progress rubrics, missing trials, or accidental leakage of operator identifiers.
- `Maintenance plan`: Version schemas, pin simulator adapters, refresh source locators, preserve migration logs, and require governance review for new physical platforms.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| `$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control` | Primary paper | Flow-matching robot-policy architecture and long action-chunk context cited by SPD; useful for separating architectural inheritance from SPD's data-source contribution | https://arxiv.org/abs/2410.24164 |
| *DexUMI: Using Human Hand as the Universal Manipulation Interface for Dexterous Manipulation* | Primary paper | Wearable hardware and visual adaptation offer an alternate route to reducing human-to-robot embodiment mismatch | https://arxiv.org/abs/2505.21864 |
| *EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data* | Primary paper | Large-scale human-video pre-training is the most direct alternative to SPD's simulation-first data strategy | https://arxiv.org/abs/2602.16710 |
| *Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware* | Primary paper | Introduces Action Chunking with Transformers and a real-demonstration baseline for bimanual imitation learning | https://arxiv.org/abs/2304.13705 |
| SPD project page | Official project surface | Provides author-curated rollout videos and the public description of collection, model, and experiments; future release links should be verified here or through an official repository | https://spd.bot/ |

This is an initial synthesis. No item is labeled as a new iterative expansion because no prior exact `.reports` stub, output `.logs` entry, Report-Mark, or derived DEP Class artifact was found for the selected source DEP.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R0 | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/e127946890a3fe7d2ffc6d53e2b6e60b14907197/.lake-data/DEP-20260819-Research%20Data%202234%20D0822 | Selected intake record, source inventory, and original paper locator | 2026-08-20 | Both Markdown files inspected; source text contains encoding defects, so empirical evidence was taken from the primary paper |
| R1 | https://arxiv.org/abs/2608.15917 | Canonical title, authors, categories, v1 date, DOI locator, and project link | 2026-08-20 | Primary arXiv record |
| R2 | https://arxiv.org/html/2608.15917 | Full method, data, architecture, experiments, ablations, limitations, appendix, tables, and references | 2026-08-20 | Primary full text; code, data, model, and hardware not executed |
| R3 | https://spd.bot/ | Official overview, public rollout surface, model summary, and experiment framing | 2026-08-20 | Mutable official page; no stable dataset/code release locator was visible in inspected text |
| R4 | https://arxiv.org/abs/2410.24164 | Related flow-model robot-policy context | 2026-08-20 | Canonical record and abstract inspected; not evidence for SPD metrics |
| R5 | https://arxiv.org/abs/2505.21864 | Related wearable-interface and embodiment-adaptation context | 2026-08-20 | Canonical record and abstract inspected; not directly benchmark-comparable |
| R6 | https://arxiv.org/abs/2602.16710 | Related large-scale egocentric human-data context | 2026-08-20 | Canonical record and abstract inspected; not directly benchmark-comparable |
| R7 | https://arxiv.org/abs/2304.13705 | Related action-chunking and bimanual imitation-learning context | 2026-08-20 | Canonical record and abstract inspected; not directly benchmark-comparable |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/README.md and https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E classification, filing, inventory, source-locality, publication-index, and commit rules | 2026-08-20 | Live repository authority inspected before writing |
| R9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Canonical source DEP and report conventions | 2026-08-20 | Live repository authority inspected before writing |

No external source files were collected. No code, dataset, model, simulator scene, benchmark pipeline, VR system, physical robot, video-scoring workflow, or training run was executed.

## Appendix

### Replication Checklist

| Requirement | Current Status | Needed for Independent Validation |
|---|---|---|
| Versioned `spd-75h` manifest | Claimed released; stable locator not verified | Episode IDs, scene/task taxonomy, durations, hashes, license, operator governance, and split rules |
| `spd-vr` source and scenes | Claimed released; stable locator not verified | Commit/tag, dependencies, MuJoCo/Madrona versions, scene assets, contact parameters, reset seeds, and expected checks |
| Policy training code | Not verified | Architecture config, initialization, optimizer versions, augmentations, data loader, logging, and deterministic smoke test |
| Pre-trained and fine-tuned weights | Not verified | Checkpoints, hashes, licenses, model card, and expected offline outputs |
| Raw evaluation records | Not inspected | Trial seeds, initial states, videos, rubric labels, interventions, failures, and scorer agreement |
| Physical bill of materials | Partially described in paper | Exact hardware revisions, firmware, camera calibration, control gains, limits, and safety procedures |
| Statistical plan | Incomplete for replication | Multiple seeds, preregistered primary outcomes, confidence intervals, and correction for multiple comparisons |

### Derived Ablation Means

| History Window | Action Chunk | SPD Mean Progress | From-Scratch Mean Progress | Difference |
|---:|---:|---:|---:|---:|
| 1 | 8 | 13.4% | 10.9% | +2.5 points |
| 1 | 32 | 34.0% | 33.3% | +0.7 points |
| 32 | 8 | 76.7% | 58.9% | +17.8 points |
| 32 | 32 | 49.3% | 46.9% | +2.4 points |

Means are reviewer calculations from Table 1 and are rounded to one decimal place. They verify the paper's approximately 18-point statement for the selected configuration but do not add independent experimental evidence.

## Attribution Block

- Primary source DEP: `Black-Lake-Data/.lake-data/DEP-20260819-Research Data 2234 D0822` at source commit `e127946890a3fe7d2ffc6d53e2b6e60b14907197`.
- Primary paper: https://arxiv.org/abs/2608.15917 and https://arxiv.org/html/2608.15917.
- Official project context: https://spd.bot/.
- Related primary records: https://arxiv.org/abs/2410.24164, https://arxiv.org/abs/2505.21864, https://arxiv.org/abs/2602.16710, and https://arxiv.org/abs/2304.13705.
- Source files collected: none.
