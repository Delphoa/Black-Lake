---
title: "Flow Control - DEP-E"
generated_at: "2026-08-18"
artifact_type: "DEP research artifact"
primary_subject: "Attention on flow control: transformer-based reinforcement learning for lift regulation in highly disturbed flows"
source_status: "Complete local PDF and full-paper HTML verified; source files withheld locally"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-18"
temporal_cutoff: "arXiv v3 and public repository records inspected through 2026-08-18"
primary_url: "https://arxiv.org/abs/2506.10153"
stable_identifier: "arXiv:2506.10153v3; DOI:10.48550/arXiv.2506.10153"
confidence_summary: "High for source-reported method and metrics; medium for cross-DEP synthesis; low for physical deployment readiness"
safety_scope: "Simulation research and offline evaluation only; no physical actuation authorization"
distribution_notes: "Public artifact contains derived Markdown and public locators only; original source files remain private"
---

# Flow Control - DEP-E

## Source Metadata

| Field | Value |
|---|---|
| Title | Attention on flow control: transformer-based reinforcement learning for lift regulation in highly disturbed flows |
| Authors | Zhecheng Liu; Jeff D. Eldredge |
| Identifier | arXiv:2506.10153v3 |
| DOI | https://doi.org/10.48550/arXiv.2506.10153 |
| Submitted / revised | Submitted 2025-06-11; arXiv v3 dated 2025-11-07 |
| Subjects | Fluid Dynamics; Machine Learning |
| Primary evidence | Complete PDF and official full-paper HTML inspected in the private local archive unit; source files withheld |
| Public verification | https://arxiv.org/abs/2506.10153 and https://arxiv.org/html/2506.10153 |
| Code and data | No official code repository or public experiment package was identified in the inspected sources |
| Review boundary | Two-dimensional computational flow at Reynolds number 200; no physical-aircraft or actuator validation |

The paper studies lift regulation of a flat plate exposed to successive, randomly parameterized gusts. The control problem is partially observable: the agent sees ten surface-pressure jump measurements, lift, and pitch state rather than the full flow field. The selected paper's local PDF and full-paper HTML both passed the required integrity gate before review. Original PDF, HTML, metadata HTML, extraction products, and any source package were withheld from this public DEP.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | https://arxiv.org/html/2506.10153 | Primary full-paper HTML | Problem setup, POMDP framing, transformer policy, PPO, reward, pretraining, transfer, results, appendix, limitations | Method and source-reported findings | High | Author-reported study; no independent reproduction |
| E2 | https://arxiv.org/abs/2506.10153 | Primary metadata record | Title, authors, subjects, version history, DOI, public artifact links | Identity and version | High | Metadata page is not treated as full-paper evidence |
| E3 | Private local source unit; public locator https://arxiv.org/pdf/2506.10153 | Primary PDF | Title page, 48-page document integrity, figures/tables cross-check | Independent source-format cross-check | High | Local source path and bytes are withheld |
| E4 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md | Related DEP artifact | Regularized RL, approximation error floors, constraint-validity cautions | Concept bridge on objective design and evaluation | Medium | Adjacent tabular theory, not fluid control |
| E5 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md | Related DEP artifact | Temporal world representation, future-state generation, causal intervention and coverage limits | Concept bridge on latent state and simulator evaluation | Medium | Driving-world model, not aerodynamic control |
| E6 | https://github.com/Delphoa/Black-Lake/blob/main/.reports/BL-Arxiv-AR-Drag-Motion-Control-20260720/Report-Mark.md | Related Report-Mark | Inference-aligned rollout history, MDP/GRPO, bounded KV state, reward dependence | Concept bridge on sequential history and rollout alignment | Medium | Video diffusion domain and different action space |
| E7 | https://github.com/Delphoa/Black-Lake/blob/main/README.md and https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Repository authority | Public layout, DEP naming, source-locality, attribution, and submission rules | Artifact construction and distribution policy | High | Repository guidance is not research evidence |

## Executive Summary

The paper proposes a transformer-based reinforcement-learning controller for a two-dimensional flat plate encountering random sequences of aerodynamic gusts. Because only a short history of surface-pressure signals and kinematic measurements is observed, the task is treated as a partially observable control problem. A transformer maps an observation window into a history-aware representation used by PPO policy and value networks.

The paper combines three engineering ideas. First, a proportional controller supplies expert trajectories for pretraining when the mid-chord setup makes that baseline useful. Second, task-level transfer moves a policy trained on a simpler single-gust task into multi-gust training. Third, the study changes the pitching pivot from mid-chord to quarter-chord, exposing an added-mass lift term that gives angular acceleration more direct control authority. The third intervention is a physical-design change, not merely a larger neural policy.

The source reports that pretraining reduces early exploration cost, the transformer policy outperforms the best tested proportional baseline as gust sequences become more complex, and transfer makes three-gust training feasible. In a representative eight-gust case, the three-gust-trained quarter-chord controller receives reward 146.98 against an idealized 200. These results are evidence of feasibility in the stated computational environment, not proof of arbitrary-long-horizon physical generalization or deployment readiness.

## Detailed Summary

### Problem Context

Linear control can work for weak or isolated disturbances but can degrade when successive strong gusts interact nonlinearly with the airfoil. The full flow field is unavailable to the controller, and the same policy can encounter trajectories with very different states and rewards. The paper therefore needs both temporal memory and a training strategy that avoids spending most of its budget discovering basic control behavior.

### System and Observation Model

The environment is a viscous incompressible two-dimensional flow around a flat plate at Reynolds number 200. Gusts are introduced as Gaussian body-force fields with randomized parameters and can arrive successively, up to eight in the reported study. The controller receives ten symmetrically placed surface-pressure jump coefficients, lift coefficient, pitch angle, and related kinematic state. The action is piecewise-constant angular acceleration, bounded to represent finite actuation authority and preserve numerical stability.

### Transformer Reinforcement Learning

The source formulates the task as a POMDP. A window of past observations is linearly embedded with positional information, processed by multi-head self-attention, and used as a learned belief-state approximation. PPO then produces the control policy and value estimate. The reward combines lift-tracking error with penalties for control changes and premature episodes caused by an infeasible pitch angle. The selected window is `N=20`, corresponding to approximately 0.6 convective time units in the study.

### Warm Starts and Task Transfer

For mid-chord pitching, a tuned proportional controller provides expert data for policy pretraining. The paper reports that a `Kp=80` expert initialization reaches apparent convergence near episode 100, while a scratch policy is still converging near episode 600 in the single-gust setup. For quarter-chord pitching, a small-gain proportional policy is not useful expert data because the added-mass response makes proportional control overreact at larger gains and produces near-zero actions at small gains. The authors instead transfer a single-gust RL policy into a three-gust task.

### Physical Control Authority

The lift decomposition separates added-mass, gust, and controlled-response terms. Mid-chord pitching removes the direct angular-acceleration contribution from the added-mass term, leaving a controller that must influence lift through integrated angular velocity and pitch. Quarter-chord pitching restores the acceleration-dependent term, so the controller can react more directly without the same magnitude saturation. This is the paper's most important implementation lesson: changing the actuator geometry can improve the effective control channel more than scaling the policy network.

### Source-Reported Evidence and Results

- In single-gust mid-chord evaluation, RL improves on the best tested proportional controller by only about 0.4 reward, while using smoother or lower control effort in representative cases. The paper interprets this as a fine-tuned version of a strong linear baseline rather than a decisive replacement.
- Pretraining with stronger expert data reduces early exploration variance and accelerates apparent convergence in the mid-chord case.
- In quarter-chord single-gust evaluation over 15 random cases, the source reports mean RL reward 90.33 with standard deviation 0.64, compared with 74.29 for the best tested proportional gain `Kp=2`. Large proportional gains produce very negative rewards.
- In the three-gust quarter-chord task, transfer from the single-gust policy takes about 500 episodes and reaches reward near 80, compared with about 1,000 episodes for the single-gust scratch training described by the paper. The learning curve is not fully converged.
- In a representative eight-gust case, the three-gust-trained policy receives reward 146.98, while the single-gust-trained policy receives -51.42 and no-control receives -754.95. The paper explicitly limits this analysis to a representative case because exhaustive evaluation is infeasible.
- An appendix comparison reports that simply doubling the history window from 20 to 40 does not improve performance without retuning and can slightly slow convergence, suggesting that stale observations can dilute a useful signal.

### Reviewer Interpretation

The contribution is best understood as a coupled design of temporal state estimation, curriculum, and control authority. The transformer addresses partial observability, warm starts reduce simulator interaction cost, and quarter-chord actuation changes the system's reachable response. Treating these as interchangeable "AI improvements" would miss the causal structure of the result.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | A transformer history encoder can support lift regulation from partial surface-pressure observations in the stated simulator. | Author claim | E1, sections II.1-II.2 | Directly supported by the described environment, architecture, and experiments; deployment transfer is untested. | High |
| C2 | Expert pretraining and task-level transfer reduce the training burden in selected configurations. | Author claim | E1, sections III.1 and III.4 | Supported by reported learning curves and episode counts; convergence comparisons are not independently reproduced. | Medium-high |
| C3 | Quarter-chord pitching gives more effective control authority than mid-chord pitching. | Author claim plus physical interpretation | E1, sections III.3-III.4 and lift decomposition | The added-mass decomposition and reported reward/control histories support the mechanism in this simulator. | Medium-high |
| C4 | The learned controller generalizes from finite gust training to an eight-gust test case. | Qualified author claim | E1, section III.4 | Supported only by a representative eight-gust evaluation, not an exhaustive distributional generalization study. | Medium |
| C5 | The main transferable lesson is to align temporal memory, training curriculum, and actuator geometry. | Reviewer interpretation | E1 plus E4-E6 | Cross-DEP synthesis; useful engineering hypothesis rather than a claim tested by the source paper. | Medium |

## Methodology

- `Research objective`: Review the selected paper source-first, identify method/evidence/limitations, and synthesize it with exactly three related Black Lake entries.
- `Sources inspected`: Official arXiv metadata and full-paper HTML; the complete local PDF; live Black Lake and Black-Lake-Data READMEs; live Black Lake entries for GPMD Regularized RL, HERMES World Model, and AR-Drag Motion Control.
- `Discovery strategy`: Enumerated the local archive with `rg --files -g "*.pdf"`; collapsed PDF paths to unique parent-directory paper units; used one uniform zero-based PowerShell `Get-Random` draw.
- `Inclusion criteria`: A candidate had to have an identifiable paper unit, a valid full PDF, a verified full-paper HTML document, and no prior artifact or recent marker for the same paper.
- `Exclusion criteria`: Existing Arxiv DEP artifacts, matching arXiv ID/DOI/title/slug markers, same-paper markers within the 24-hour cutoff, and incomplete or invalid source documents.
- `Random selection record`: 75,967 PDF candidates; 75,964 unique parent-directory paper units; selected zero-based index 38,014; selected arXiv:2506.10153; no manual substitution.
- `Source-integrity repair`: The selected unit began with a valid PDF but no full-paper HTML. A bounded single-paper archive repair fetched the official full-paper HTML and updated the local README, provenance record, machine-readable summary, acquisition receipt, and verification report. The source package was unavailable and was not needed for the review.
- `Deduplication and reselection`: Scanned Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and relevant Black-Lake-Data records for the ID, DOI, normalized title, slug, and 24-hour markers. Exclusions and reselections were both zero.
- `Analytical approach`: Empirical, comparative, implementation, replication, and safety-and-ethics analysis. Author claims are separated from reviewer interpretation and cross-DEP inference.
- `Evidence handling`: Exact metrics retain their evaluation context. The abstract is metadata only; method and result claims rely on full-paper HTML/PDF inspection. Missing code, data, physical validation, and independent reproduction remain visible.
- `Uncertainty handling`: Representative-case results, incomplete convergence, simulator assumptions, and source-reported limitations are labeled rather than generalized to physical deployment.

## Scope, Constraints, and Assumptions

- `Scope`: Transformer-based RL for lift control in the paper's two-dimensional viscous flat-plate simulator, plus bounded cross-DEP implementation synthesis.
- `Temporal boundary`: Public records and related DEP entries inspected through 2026-08-18; paper version is arXiv v3 dated 2025-11-07.
- `Evidence limits`: No experiment, codebase, simulator, hardware controller, or independent benchmark was executed by this review.
- `Assumptions`: Reported reward and episode counts are transcribed from the source and comparable only within the source's stated configurations.
- `Constraints`: Original source files, extraction products, and local archive metadata are private and withheld from the repository and Slack.
- `Safety boundary`: All implementation ideas are offline, simulator-only, or authorized research prototypes; none authorizes physical aircraft actuation.
- `Out of scope`: Real-aircraft control, certification, live sensor integration, autonomous deployment, and claims about arbitrary gust distributions.
- `Intended use`: Research review, reproducibility planning, and design of bounded simulation experiments.

## Observations

- `Observed pattern`: Quarter-chord geometry changes the control channel by exposing an acceleration-dependent added-mass term; this is a system-design lever, not just a policy-design lever.
- `Observed pattern`: The paper's strongest RL advantage appears when gust sequences create nonlinear history dependence; the single-gust mid-chord advantage is small.
- `Observed pattern`: More history is not automatically better. The `N=40` appendix result suggests that irrelevant past observations can dilute optimization without retuning.
- `Technical implication`: A controller should log observation age, sensor coverage, action saturation, and the physical contribution of each actuation path, not only episode reward.
- `Contradiction or tension`: The abstract emphasizes arbitrarily long gust sequences, while the strongest long-horizon evidence is a representative eight-gust case and incomplete training curves.
- `Open question`: How robust are the learned belief state and quarter-chord advantage to sensor noise, delay, missing channels, Reynolds-number changes, and actuator dynamics?
- `Reviewer hypothesis`: A structured controller that combines a short learned history with an explicit low-order flow or actuator model may achieve better transfer than a transformer-only policy.

## Considerations

The reward contains a useful tradeoff between tracking, smoothness, and feasible configuration, but reward quality is not equivalent to physical safety. A future implementation should measure true constraint violations, action saturation, sensor delay, and failure recovery separately from reward. The source's computational flow solver also narrows the evidence: 2D flat-plate dynamics at one Reynolds number do not establish performance for 3D aircraft, new gust spectra, or hardware.

For deployment-oriented research, the next layer should be an offline safety gate: hold the policy in a simulator, compare it with a verified baseline, enforce hard pitch and acceleration limits, and require a human-approved transition before any hardware test. The related GPMD entry reinforces that objective regularization must be checked against ground-truth constraints; HERMES reinforces scenario coverage and causal intervention; AR-Drag reinforces inference-aligned rollout auditing and independent evaluation.

## Strengths

- The paper connects POMDP history encoding to a concrete sparse-sensor flow-control problem.
- Pretraining and task transfer are tied to simulator cost rather than presented as generic additions.
- The pivot-location study adds a physical mechanism and lift decomposition to the neural-policy comparison.
- Results include multiple gust regimes, mid- versus quarter-chord configurations, learning curves, and an observation-window appendix.
- The paper explicitly reports limitations around observation windows, sensors, rewards, architecture, actuation, and controllability.

## Weaknesses

- The long-horizon generalization evidence is dominated by representative cases rather than a broad distributional test.
- The environment is a 2D flat plate at one Reynolds number with idealized sensors and bounded angular acceleration.
- Observation history length, sensor placement, reward weights, and transformer capacity are not systematically explored.
- The baseline comparison is incomplete for a deployment claim; the paper leaves PID and broader model-based or robust-control comparisons for future work.
- No independently runnable public code/data package was identified in the inspected sources, and no experiment was reproduced.
- Reward values can conflate lift tracking, smooth actuation, and early termination, so cross-configuration comparisons require care.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Sensor and delay sweep | Robustness | Sparse pressure observations may change under noise, lag, or dropout | Reveals belief-state failure boundaries | More simulator runs and tuning | Fixed seeds across noise/delay/dropout strata |
| Baseline expansion | Comparative validity | P control is not enough for all pivot configurations | Separates RL benefit from baseline weakness | PID, MPC, robust, and model-based tuning cost | Equal compute and matched reward/constraint reporting |
| Long-horizon distributional evaluation | Generalization | One representative eight-gust case is insufficient | Estimates tail failure and drift | Larger simulation budget | Held-out gust process, many seeds, confidence intervals |
| Physics-aware policy audit | Interpretability | Attention weights alone do not prove physical reasoning | Links actions to lift components and sensors | Instrumentation may perturb runs | Counterfactual sensor masking and lift-decomposition checks |
| Hardware-transfer gate | Deployment | Idealized actuation and flow differ from devices | Safer transition to experiments | Requires actuator and wind-tunnel characterization | Offline sim, shadow mode, then bounded human-approved tests |

## Potential Implementations

1. `Sparse-flow belief controller`: User: flow-control researchers. Goal: learn a short-history policy from pressure and kinematic signals. Core mechanism: transformer encoder plus PPO or a model-based alternative, with explicit action and pitch limits. Required inputs: licensed simulator, sensor model, gust generator, baseline controller, and seed manifest. Outputs: policy checkpoint, action traces, lift/error ledger, and saturation report. Risk controls: simulator-only operation, hard constraints, no live actuation API, and human approval for any hardware transition. Evaluation: held-out gust distributions, sensor faults, baseline parity, and multiple seeds.
2. `Curriculum and transfer profiler`: User: teams managing expensive CFD or robotics simulation. Goal: quantify whether expert initialization and task transfer reduce valid training cost. Core mechanism: compare scratch, expert-pretrained, and source-task-transferred policies under identical budgets. Required inputs: source/target task definitions, checkpoints, reward decomposition, and compute ledger. Outputs: learning curves, sample/episode savings, transfer regressions, and stopping criteria. Risk controls: no claim of generalization from reward alone; require target-task stress tests and independent metrics. Evaluation: convergence confidence intervals, wall-clock cost, and failure rates.
3. `Actuator-authority design study`: User: aero-control and mechanism designers. Goal: test whether pivot or actuator placement changes controllability more than policy capacity. Core mechanism: sweep pivot locations and actuator limits while decomposing lift into gust, added-mass, and controlled-response terms. Required inputs: validated simulator, geometry variants, actuator dynamics, and physical constraints. Outputs: control-authority maps and policy-performance Pareto fronts. Risk controls: no physical deployment; retain hard envelope limits and report model mismatch. Evaluation: action saturation, tracking error, control effort, and robustness across gust families.

## Three Ways to Exercise This Research

1. `Reproduce the single-gust comparison`: Objective: compare scratch, P-pretrained, and RL policies in the mid-chord simulator. Inputs: a licensed or synthetic equivalent simulator, the paper's public description, fixed seeds, and a proportional baseline. Method: match observation window, action bounds, reward terms, and evaluation cases; record episode reward, lift error, control effort, and saturation. Output: a public-safe metric ledger and learning curves. Success criterion: configuration and metric directions reconcile with the source. Stop condition: any missing parameter or license issue is documented rather than guessed.
2. `Stress the belief-state boundary`: Objective: test history and partial-observation robustness without hardware. Inputs: a toy or authorized simulator, pressure traces, controlled noise/delay/dropout, and the `N=20` versus `N=40` history variants. Method: sweep observation quality and compare a transformer policy with a fixed-history baseline. Output: failure slices and calibration/abstention notes. Success criterion: performance degradation is localized and reproducible. Stop condition: the policy violates hard envelope limits or the observation transformation cannot be audited.
3. `Run an actuator-authority ablation`: Objective: separate neural-policy benefit from pivot geometry. Inputs: the same policy family, mid- and quarter-chord action models, lift decomposition, and matched compute. Method: evaluate tracking, effort, saturation, and reward across held-out gust sequences. Output: a control-authority report with confidence intervals. Success criterion: any claimed geometry advantage persists across seeds and gust families. Stop condition: a result depends only on a single representative trajectory.

## Example MVP Product

- `Product name`: Flow Control Evidence Gate.
- `Target user`: Researchers reviewing learned controllers before simulator-to-hardware progression.
- `Problem`: Reward improvements can hide action saturation, observation faults, baseline weakness, or poor transfer across disturbance regimes.
- `Core workflow`: Register a simulator and policy version; run matched baselines and held-out gust suites; compute lift, effort, saturation, constraint, and latency metrics; compare results with a human-approved release policy; export a signed evidence bundle.
- `Data requirements`: Synthetic or licensed flow trajectories, sensor/action schemas, simulator version, checkpoint/config hashes, baseline outputs, and scenario labels.
- `Architecture`: Local CLI or isolated batch runner with a deterministic metric library, scenario registry, policy adapter, constraint checker, and Markdown/JSON report generator.
- `Success metrics`: Reproducible metric ledgers, complete scenario coverage, zero hidden action-limit violations, and exact reconciliation of source-reported table values where reproduced.
- `Risk controls`: Simulator-only default, no physical actuation endpoint, allowlisted inputs, hard envelope checks, independent evaluator, and human approval for policy changes.
- `Limitations`: Cannot prove real-world safety or replace wind-tunnel, hardware, or certification testing; depends on simulator fidelity and scenario coverage.
- `MVP boundary`: Evidence generation and offline comparison only; no training orchestration, live control, or autonomous deployment.
- `Deployment model`: Local CLI or isolated batch job.
- `Evaluation plan`: Unit-test metric arithmetic, replay fixed failure fixtures, compare against paper tables, then run held-out disturbance suites.
- `Failure modes`: Simulator mismatch, reward hacking, sensor leakage, hidden saturation, stale checkpoints, and false confidence from sparse scenarios.
- `Maintenance plan`: Version policy adapters, metrics, simulator manifests, thresholds, scenario catalogs, and expected outputs; review source licenses each release.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| GPMD Regularized RL - DEP-E | Related Black Lake DEP | Shows how regularization and explicit approximation-error budgets can shape policy updates, while warning that objective constraints are not ground-truth safety guarantees. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md |
| HERMES World Model - DEP-E | Related Black Lake DEP | Connects temporal latent state, future-state generation, causal intervention, and coverage-aware evaluation in a simulator-heavy safety domain. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md |
| AR-Drag Motion Control Report-Mark | Related Black Lake Report-Mark | Treats sequential rollout history, training-inference alignment, bounded memory, and reward dependence as first-class control concerns. | https://github.com/Delphoa/Black-Lake/blob/main/.reports/BL-Arxiv-AR-Drag-Motion-Control-20260720/Report-Mark.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2506.10153 | Identity, authors, version history, subjects, DOI, and public artifact links | 2026-08-18 | Primary metadata record |
| R2 | https://arxiv.org/html/2506.10153 | Full problem, method, experiments, tables, appendix, and limitations | 2026-08-18 | Primary full-text source |
| R3 | https://arxiv.org/pdf/2506.10153 | Public equivalent of the inspected complete PDF | 2026-08-18 | PDF withheld from the DEP |
| R4 | Private local source unit, path withheld | PDF/HTML integrity check and page-level cross-check | 2026-08-18 | Original source files remain local and were not uploaded |
| R5 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md | Related regularized-RL and constraint-validity synthesis | 2026-08-18 | Existing processed DEP artifact |
| R6 | https://arxiv.org/abs/2105.11066v4 | Primary paper behind the GPMD related DEP | 2026-08-18 | Related-source locator used by the DEP |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HERMES%20World%20Model/hermes_world_model_manuscript.md | Related world-model, temporal-state, and coverage synthesis | 2026-08-18 | Existing processed DEP artifact |
| R8 | https://arxiv.org/abs/2501.14729 and https://arxiv.org/html/2501.14729 | Primary paper behind the HERMES related DEP | 2026-08-18 | Related-source locators used by the DEP |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.reports/BL-Arxiv-AR-Drag-Motion-Control-20260720/Report-Mark.md | Related rollout-history and sequential-control synthesis | 2026-08-18 | Existing processed Report-Mark |
| R10 | https://arxiv.org/abs/2510.08131 and https://arxiv.org/html/2510.08131 | Primary paper behind the AR-Drag related Report-Mark | 2026-08-18 | Related-source locators used by the report |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public repository layout and source-locality policy | 2026-08-18 | Repository authority |
| R12 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository and DEP attribution policy | 2026-08-18 | Repository authority |

## Appendix

### Selection and Validation Record

- Candidate enumeration used `rg --files -g "*.pdf"` against the local arXiv archive.
- The scan returned 75,967 PDF candidates and 75,964 unique parent-directory paper units.
- One uniform PowerShell `Get-Random` draw selected zero-based index 38,014; no manual selection was used.
- Dedup scans covered Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and relevant Black-Lake-Data records. The paper's base/versioned ID, DOI, normalized title, and slug were not found; exclusions and reselections were zero.
- Initial source state was partial because full-paper HTML was missing. A bounded local repair fetched official full-paper HTML and updated the archive unit's README, provenance record, machine-readable summary, acquisition receipt, and verification report.
- Final source state was complete: PDF 5,012,809 bytes, `%PDF-` header, trailing `%%EOF`; full-paper HTML 406,905 bytes, 110,564 body characters, document marker, 21 heading markers, and 27 structure-term matches.
- No PDF, HTML, metadata page, source archive, extracted text, cache, or local archive path was copied into this repository or Slack.

### Reproduction Checklist

- Pin arXiv v3 and the exact simulator configuration.
- Match Reynolds number, grid/time settings, gust parameterization, sensor layout, action bounds, reward weights, observation window, PPO settings, and pivot location.
- Compare scratch, proportional-pretrained, and transferred policies under matched seeds and compute budgets.
- Report lift error, control effort, action saturation, termination rate, reward components, wall-clock cost, and confidence intervals.
- Add sensor noise/delay/dropout, held-out gust processes, and independent safety/constraint metrics.
- Keep any hardware transition outside this artifact and require separate review and authorization.
