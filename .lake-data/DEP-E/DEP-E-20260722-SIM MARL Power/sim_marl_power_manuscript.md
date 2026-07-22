---
title: "SIM MARL Power - DEP-E"
generated_at: "2026-07-22 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of joint AP power allocation and stacked-intelligent-metasurface phase control using NVR-MAPPO."
source_status: "verified local PDF, full-paper HTML, metadata HTML, and source package inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-22"
temporal_cutoff: "arXiv:2502.19675v1 and related public records available through 2026-07-22"
primary_url: "https://arxiv.org/abs/2502.19675v1"
stable_identifier: "arXiv:2502.19675v1; DOI 10.48550/arXiv.2502.19675"
confidence_summary: "High for identity, method transcription, and plotted claims; medium for empirical effectiveness because results were not reproduced and no code or raw data was identified."
safety_scope: "offline wireless-system research, simulation, and evaluation only; no live radio or network-control authority"
distribution_notes: "Generated Markdown and public URLs only. PDF, HTML, source package, extraction material, and render caches remain local."
---

# SIM MARL Power - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2502.19675v1 | https://arxiv.org/abs/2502.19675v1 | arXiv metadata; submitted 2025-02-27; `cs.IT` with `eess.SP` cross-listing. | 2026-07-22 | Inspected |
| S2 | Joint Power Allocation and Phase Shift Design | Primary paper | PDF and full-paper HTML | arXiv:2502.19675v1; six pages | https://arxiv.org/pdf/2502.19675; https://arxiv.org/html/2502.19675v1 | arXiv non-exclusive distribution license linked from S1; private verified copies inspected and withheld. | 2026-07-22 | Fully inspected and integrity-verified |
| S3 | arXiv source package | Primary implementation-level evidence | LaTeX and figures | arXiv:2502.19675v1; 15 readable entries | https://arxiv.org/e-print/2502.19675 | Private source package inspected for equations, algorithm text, captions, and references; not redistributed. | 2026-07-22 | Inspected |
| S4 | arXiv-issued DOI | Persistent identifier | DOI | 10.48550/arXiv.2502.19675 | https://doi.org/10.48550/arXiv.2502.19675 | Persistent arXiv locator. | 2026-07-22 | Verified |
| S5 | Multi-Point ISAC DEP-E | Related processed artifact | Markdown | DEP-E-20260716-Multi-Point ISAC | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Multi-Point%20ISAC/multi_point_isac_manuscript.md | Conceptual synthesis only; does not validate the selected paper. | 2026-07-22 | Inspected |
| S6 | Telecom AI Roadmap DEP-E | Related processed artifact | Markdown | DEP-E-20260711-Telecom AI Roadmap | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Telecom%20AI%20Roadmap/telecom_ai_roadmap_manuscript.md | Operational and governance context only. | 2026-07-22 | Inspected |
| S7 | GPMD Regularized RL DEP-E | Related processed artifact | Markdown | DEP-E-20260716-GPMD Regularized RL | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md | Policy-regularization and convergence context only. | 2026-07-22 | Inspected |
| S8 | Black-Lake repository authorities | Deposition rules | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Governs class, path, index, attribution, source withholding, and commit rules. | 2026-07-22 | Fetched and read |
| S9 | Black-Lake-Data README | Related repository authority | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Used for cross-repository dedup and context. | 2026-07-22 | Fetched and read |
| S10 | Focused public implementation search | Availability check | Search results | title, arXiv ID, and `NVR-MAPPO` queries | https://arxiv.org/abs/2502.19675v1 | No author-identified official implementation was found; absence from a bounded search is not proof of nonexistence. | 2026-07-22 | Completed with limitation |

The authors are Yiyang Zhu, Jiayi Zhang, Enyu Shi, Ziheng Liu, Chau Yuen, and Bo Ai. The inspected record contains one version, submitted on 2025-02-27. No journal reference or non-arXiv publisher DOI appears in the inspected metadata. The work should therefore be treated as an arXiv preprint unless a later authoritative publication record is established.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Primary metadata and DOI | title, authors, subjects, date, version, abstract, identifiers | source identity and chronology | High | metadata does not validate technical claims |
| E2 | S2, S3 | Primary paper and source | system model, equations 1-11, NVR-MAPPO algorithm, simulation description, conclusion | problem, method, assumptions, and author claims | High for transcription | no independent derivation or execution |
| E3 | S2, S3, Figures 3-5 | Primary empirical evidence | convergence curve, layer sweep, meta-atom sweep, captions, and surrounding prose | reported performance trends and numerical comparisons | Medium-high | no raw values, seeds, confidence intervals, or code |
| E4 | S5-S7 | Related DEP evidence | distributed wireless allocation, guarded telecom AI, and regularized policy optimization | conceptual bridges and implementation framing | Medium-high | adjacent work does not validate this paper |
| E5 | S8, S9 | Live repository rules | DEP class, contents, index, source withholding, and attribution | deposit compliance | High | process evidence only |
| E6 | selection and dedup records | Process evidence | PDF enumeration, unit grouping, random draw, identifier reconciliation, and targeted collision scans | eligibility and zero-reselection result | High | title-only duplicates outside inspected indexes remain a residual search risk |
| E7 | private source-integrity records | Verification evidence | byte counts, header/trailer, body-text, document markers, headings, structure terms, hashes, and partial inventory | complete-source gate | High | private paths and source files deliberately withheld |
| E8 | S10 | Availability search | exact-title, arXiv-ID, and method-name searches | code-availability boundary | Medium | a repository may exist outside indexed or author-linked results |

## Executive Summary

The paper studies a stacked-intelligent-metasurface-assisted cell-free massive-MIMO downlink. Distributed access points jointly serve users, and each access point is paired with a programmable multilayer metasurface. The design problem couples per-user power allocation with a large set of continuous phase shifts to maximize total spectral efficiency under per-access-point power constraints.

The proposed solution treats each access-point/metasurface pair as an agent in centralized training with decentralized execution. A shared actor consumes local channel, power, and phase observations; a centralized critic sees broader state. NVR-MAPPO augments MAPPO with a recurrent policy and Gaussian noise concatenated to the critic state, with periodic shuffling across agents, to encourage exploration and reduce early value bias.

The empirical case is entirely simulated. The main setting uses a `100 m x 100 m` area, 28 GHz downlink, `3 dBm` maximum transmit power per access point, `-96 dBm` noise power, and half-wavelength element spacing. Source prose reports at least `50%` higher spectral efficiency for MARL methods than a random-codebook plus water-filling baseline in parameter sweeps, at least `15%` over MADDPG in the layer sweep, and `9.8%` at `N = 64` meta-atoms. The conclusion separately claims about an `18%` convergence advantage over MAPPO. These are author-reported readings of plotted simulations, not independently reproduced estimates.

Reviewer assessment: the paper contributes a useful mapping from a coupled radio-control problem to a multi-agent actor-critic workflow, but the evidence does not establish hardware feasibility, deployment robustness, or causal benefit from noisy values. There is no code, raw data, seed schedule, uncertainty analysis, isolated noisy-value/recurrent ablation, or channel-mismatch test in the inspected bundle. The source TeX also contains an incomplete actor-loss expression, making a reference implementation especially important.

## Detailed Summary

### Problem and System Context

Cell-free massive MIMO distributes access points across a service region and coordinates them through a central processor. The paper adds a stacked intelligent metasurface to every access point so wave-domain phase manipulation contributes to beamforming. The intended benefit is greater beam-pattern flexibility with fewer active radio-frequency resources than a purely digital architecture.

The model contains `L` access points, `K` single-antenna user equipments, `M_AP` antennas per access point, `M` metasurface layers, and `N x N` meta-atoms per layer. Each layer applies a diagonal phase-shift matrix. Propagation between adjacent layers follows a Rayleigh-Sommerfeld expression, and the ordered product of propagation and phase matrices forms the wave-domain beamforming matrix.

### Optimization Target

The received signal and SINR combine coherent contributions across access points and interference from other users. User spectral efficiency is `log2(1 + SINR)`. The objective maximizes the sum over users subject to one power budget per access point, nonnegative allocation variables, and phase angles in `[0, 2*pi)`.

This is a high-dimensional non-convex problem. The paper does not derive a global optimizer or an approximation ratio. Instead, it frames sequential power-and-phase actions as a cooperative decentralized partially observable Markov decision process.

### NVR-MAPPO Mechanism

Each access-point/metasurface group is one agent. Local observations include local channel state, the access point's current power vector, and its current phase matrix. Broader state includes relative device positions, propagation matrices, and current SINR. Agents share actor and critic networks. The critic receives global state plus an agent-specific Gaussian-noise vector; the noise is periodically shuffled in the agent dimension. A recurrent policy carries state across time.

The critic minimizes a mean-squared Bellman error, while the actor follows a clipped MAPPO-style objective with an entropy term. Algorithm 1 specifies trajectory collection, replay-buffer insertion, noise shuffling, recurrent hidden-state updates, gradient calculation, and actor/critic updates. The public source is not sufficient for exact reproduction: architecture sizes, optimizer settings, replay details, noise variance and shuffle interval, full reward specification, seeds, and a syntactically complete actor-loss formula are not all supplied.

### Simulation Design and Results

The simulation assigns all users to all access points in a `100 m x 100 m` region. Access points are 10 m high, users are 1.7 m high, SIM thickness is `5*lambda`, downlink frequency is 28 GHz, and adjacent elements use half-wavelength spacing. The source reports an initial four antennas per access point and compares NVR-MAPPO with MAPPO, MADDPG, and a codebook-based method.

Figure 3 uses 250 training episodes with `L = 8`, `K = 4`, `M_AP = 2`, `M = 4`, and `N = 64`. The plotted trajectories suggest faster early NVR-MAPPO convergence than MAPPO but more fluctuation, while final values are close. Figure 4 sweeps one to ten metasurface layers with `L = 8`, `K = 6`, `M_AP = 2`, and `N = 32`. Figure 5 sweeps meta-atoms with `L = 8`, `K = 6`, `M_AP = 2`, and `M = 8`.

The paper's strongest qualitative result is that learned joint control beats the selected fixed codebook baseline within the reported simulation budget. The evidence does not isolate whether improvement comes from CTDE, MAPPO, recurrence, noisy critic inputs, hyperparameter tuning, or baseline weakness. The claim that the system is cost- or energy-efficient is motivational because energy consumption is not reported as an evaluated outcome.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Joint power and SIM phase control can be formulated as a cooperative MARL problem. | Author methodological claim | E2 | Directly represented by the Dec-POMDP and actor-critic construction. | High |
| C2 | Local execution reduces backhaul burden relative to centralized execution. | Author systems claim | E2 | Plausible, but communication volume and latency are not measured. | Medium |
| C3 | Gaussian noisy values plus recurrence accelerate exploration and convergence. | Author causal claim | E2, E3 | Curves are consistent with faster early learning, but there is no clean component ablation. | Medium-low |
| C4 | MARL methods improve sum spectral efficiency by at least 50% over the codebook baseline in the reported sweeps. | Author empirical claim | E3 | Supported by source prose and plots within the chosen settings; not reproduced. | Medium |
| C5 | NVR-MAPPO and MAPPO improve at least 15% over MADDPG in the layer sweep. | Author empirical claim | E3 | Scenario-specific plotted comparison with no uncertainty. | Medium |
| C6 | At `N = 64`, the MAPPO-family methods improve 9.8% over MADDPG. | Author empirical claim | E3 | Direct source statement; denominator and raw values are unavailable. | Medium |
| C7 | NVR-MAPPO has about an 18% convergence advantage over MAPPO. | Author conclusion claim | E2, E3 | The metric is not precisely defined and sits in tension with prose describing only a marginal final advantage. | Low-medium |
| C8 | A deployment-ready controller should treat the learned policy as a candidate generator behind constraint, calibration, and rollback gates. | Reviewer interpretation | E4 | Consistent with related DEP evidence; not tested by the paper. | Medium-high |

## Methodology

- `Research objective`: Preserve a source-grounded account of the paper's radio model, NVR-MAPPO mechanism, evidence, limits, and implementation relevance.
- `Sources inspected`: Verified six-page PDF, full-paper HTML, metadata HTML, LaTeX source and figures, arXiv record/DOI, both live repository READMEs, three related Black-Lake manuscripts, and a focused public code search.
- `Discovery strategy`: Used `rg --files -g "*.pdf"` over the local archive, grouped each PDF parent as one paper unit, and read adjacent metadata only after selection.
- `Random selection`: `75,780` PDFs formed `75,777` unique units. Identifier reconciliation found `266` already-used units among `1,100` normalized identifiers, leaving `75,511` eligible units. PowerShell `Get-Random` selected the first accepted rejection-sampling draw. The unit occupied zero-based index `38,440` in the canonical all-unit ordering and `38,300` in the fully reconciled eligible ordering.
- `Deduplication`: Scanned Black-Lake logs, reports, DEP entries, the public dedup index, automation memory, and relevant live Black-Lake-Data entries for arXiv ID, DOI, normalized title, and slug, including recent same-paper markers. No owning artifact matched; reselections: `0`.
- `Source-integrity handling`: The initial unit was partial: its `2,290,516`-byte PDF passed header and trailer checks, but full-paper HTML was missing. A single bounded repair preserved that PDF and collected full-paper HTML, metadata HTML, and the source package. The local README, attribution record, machine-readable summary, and verification report were updated before review.
- `Integrity verification`: PDF began with `%PDF-`, ended with `%%EOF`, and parsed as six pages. Full-paper HTML was `459,959` bytes with `55,804` body characters, a document marker, `44` section/heading markers, and six structure terms. The source archive was `3,167,313` bytes with 15 readable entries. No partial files remained.
- `Extraction process`: Visually inspected all six rendered pages, read the full source TeX, checked figure captions and curves, and compared claims with the metadata and HTML structure.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/operations, product research, and replication analysis.
- `Evidence handling`: Author claims, source evidence, and reviewer interpretations are labeled separately; numerical claims remain attributed to the source unless reproduced.
- `Uncertainty handling`: Missing code, raw values, seeds, uncertainty, hardware tests, and implementation details are explicit evidence gaps.
- `Distribution`: All original source files, extracted material, caches, renders, and local records remain outside the repository. No `.source/` directory is created.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2502.19675v1, its complete source bundle, the selected simulation claims, and implementation implications for offline evaluation.
- `Temporal boundary`: sources available through 2026-07-22; later revisions or publications require a difference review.
- `Evidence limits`: no official code, raw curves, trained model, replay traces, configuration manifest, or independent reproduction was identified.
- `Assumptions`: the plotted labels and prose use consistent spectral-efficiency units and baseline configurations; this was not machine-verified from raw data.
- `Constraints`: no live radio control, spectrum use, operational network changes, private telemetry, or hardware claims are authorized.
- `Out of scope`: rederiving electromagnetic equations, proving convergence, measuring energy efficiency, or certifying regulatory compliance.
- `Intended use`: research review, replication planning, simulation tooling, and pre-deployment control-policy auditing.
- `Reproducibility boundary`: source equations and figures are inspectable, but the experiment cannot be recreated faithfully without missing hyperparameters, reward/action encoding, and code.
- `Data sensitivity`: inspected sources are public; original files and local processing records are nevertheless withheld by repository policy.

## Observations

- `Observed pattern`: NVR-MAPPO's clearest plotted distinction is faster early training with greater fluctuation, not a large final-value separation from MAPPO.
- `Terminology tension`: the abstract calls the algorithm fully distributed, while training uses a centralized critic and shared global information. Decentralized execution is supported; fully distributed training is not.
- `Evidence tension`: the conclusion's `18%` convergence advantage lacks a precise metric and should not be merged with the reported `15%`, `9.8%`, or `50%` spectral-efficiency comparisons.
- `Reproducibility issue`: the source TeX's actor-loss expression has missing clipping-bound terms, while the algorithm omits several settings needed to reproduce the curves.
- `Systems implication`: local observations may reduce execution-time backhaul, but centralized training, CSI collection, model distribution, and synchronization still have material communication cost.
- `Reviewer hypothesis`: the practical value is a constrained candidate-policy workflow that compares learned joint control against strong optimization baselines under stale/noisy CSI and hardware nonidealities.

## Considerations

Real metasurfaces have discrete or imperfect phase control, mutual coupling, calibration drift, insertion loss, latency, and controller limits. A policy trained with continuous ideal phases may produce infeasible commands. A simulator should therefore model quantization, delayed control, temperature/calibration shifts, and projection onto an allowlisted action space.

CSI freshness and communication cost are operational variables, not background constants. Evaluation should measure backhaul bytes, update rate, decision latency, policy-staleness failures, and performance under missing agents. A controller should fail closed or fall back to a deterministic feasible allocation when state validity is uncertain.

Reward maximization can starve users even when sum spectral efficiency improves. Production-oriented work should report minimum-user rate, outage probability, power/energy, fairness, tail latency, convergence failures, and constraint violations in addition to the mean sum metric.

## Strengths

- Jointly models access-point power and multilayer phase decisions rather than optimizing one in isolation.
- Connects a concrete electromagnetic propagation model to the MARL state and action design.
- Uses CTDE to separate rich training information from local execution observations.
- Compares multiple learning baselines and a traditional codebook method across layer and meta-atom sweeps.
- The compact source bundle exposes equations, algorithm pseudocode, and figure assets for audit.

## Weaknesses

- All effectiveness evidence is simulation-only and comes from one six-page preprint.
- No official code, raw values, seeds, error bars, configuration manifest, or environment implementation was identified.
- No component ablation separates recurrence, noisy values, shuffling, or shared networks.
- The codebook baseline may be weak; no strong alternating-optimization or oracle comparison is supplied.
- Energy-efficiency motivation is not evaluated with an energy metric.
- Hardware nonidealities, imperfect/stale CSI, phase quantization, fronthaul cost, fairness, and failures are not tested.
- The actor-loss source expression and `18%` convergence statement are insufficiently specified for reliable reproduction.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code, configs, seeds, raw curves, and a corrected loss equation | Reproducibility | The current bundle cannot recreate the experiment. | Auditable results and faster extension. | Maintenance and environment burden. | Rebuild every figure from a pinned manifest and compare data hashes. |
| Add factorial ablations for noise, shuffling, recurrence, CTDE, and network sharing | Causal evidence | Current comparisons bundle several mechanisms. | Identifies what actually causes the gain. | More training runs. | Multi-seed effect sizes with confidence intervals. |
| Compare against alternating optimization, projected gradient, and small-instance oracle solutions | Baselines | A random codebook is not a demanding optimization baseline. | Better calibration of MARL value. | Solver engineering and scale limits. | Report optimality gaps on small cases and runtime-quality frontiers at scale. |
| Model discrete phases, calibration error, stale CSI, missing agents, and fronthaul limits | System realism | Ideal continuous control may not transfer. | More credible deployment boundary. | Larger simulator and parameter uncertainty. | Stress tests with constraint-violation and tail metrics. |
| Add energy, fairness, outage, latency, and control-cost objectives | Objective validity | Sum spectral efficiency alone hides operational harm. | Multi-objective decision support. | Pareto-selection complexity. | Publish complete frontiers and hard-constraint violations. |

## Potential Implementations

1. **SIM-MARL Reproduction Harness**
   - `User`: wireless-ML research team.
   - `Goal`: reconstruct the reported curves and isolate NVR-MAPPO components.
   - `Core mechanism`: a seeded simulator with swappable actor-critic, recurrence, noise, shuffling, and baseline modules.
   - `Required inputs`: public equations, synthetic channels, explicit action constraints, configuration manifests, and seeds.
   - `Outputs`: raw curves, effect sizes, confidence intervals, constraint logs, and provenance hashes.
   - `Risk controls`: simulation-only, no radio interface, deterministic export allowlist.
   - `Evaluation`: figure reconstruction plus factorial ablation and small-instance oracle comparison.

2. **Metasurface Policy Feasibility Gate**
   - `User`: testbed engineer before any authorized hardware experiment.
   - `Goal`: reject infeasible or stale learned commands.
   - `Core mechanism`: validate CSI age, power budgets, phase quantization, controller rate, and fallback availability before a candidate action can leave simulation.
   - `Required inputs`: synthetic candidate actions, modeled hardware limits, state timestamps, and calibration version.
   - `Outputs`: accept/reject decision, projected safe action, reason codes, and audit record.
   - `Risk controls`: defaults to offline mode; no device credentials; explicit human authorization for any testbed adapter.
   - `Evaluation`: fault injection for stale state, out-of-range power, invalid phase, missing agents, and rollback.

3. **Wireless Control Frontier Explorer**
   - `User`: radio-resource researcher or product reviewer.
   - `Goal`: compare sum spectral efficiency with fairness, energy, latency, and control overhead.
   - `Core mechanism`: replay identical synthetic scenarios across NVR-MAPPO, MAPPO, optimization, and simple feasible baselines.
   - `Required inputs`: scenario distributions, channel seeds, cost models, user-rate constraints, and baseline adapters.
   - `Outputs`: Pareto frontier, tail metrics, optimality gaps where available, and evidence-linked report.
   - `Risk controls`: public or synthetic inputs only; no live network authority.
   - `Evaluation`: repeated seeds, distribution shift, calibrated failure thresholds, and independent review.

## Three Ways to Exercise This Research

1. **Reproduce and ablate**: Objective: test whether noisy values or recurrence causes faster early convergence. Inputs: a toy seeded SIM-aided cell-free simulator and corrected MAPPO loss. Steps: reconstruct the baseline, then toggle noise, shuffling, and recurrence one at a time. Output: learning curves, confidence intervals, and effect sizes. Success criterion: independent runs reproduce the direction of the source claim. Stop condition: halt if the baseline cannot be matched or the loss remains ambiguous.
2. **Calibrate against optimization**: Objective: measure the learned policy's quality rather than only its relative curve. Inputs: small synthetic instances with continuous and quantized phases. Steps: solve an exhaustive or high-quality optimization oracle where tractable, run learned and heuristic policies, and compute optimality gaps plus runtime. Output: a size-stratified quality-cost frontier. Success criterion: gaps and constraint violations are reported for every method. Stop condition: do not extrapolate past the instance sizes where the oracle is trustworthy.
3. **Stress the deployment boundary**: Objective: determine whether the policy remains feasible under nonideal state and hardware. Inputs: synthetic CSI delay, phase error, calibration drift, missing agents, and fronthaul caps. Steps: inject faults, pass actions through a feasibility gate, and compare fallback behavior. Output: failure taxonomy, tail metrics, and rollback evidence. Success criterion: no invalid action bypasses the gate. Stop condition: retain simulation-only status if state validity or fallback cannot be demonstrated.

## Example MVP Product

- `Product name`: SIM Policy Replay.
- `Target user`: wireless-ML researchers reviewing a joint power-and-phase policy before a simulator or authorized testbed.
- `Problem`: aggregate reward curves do not show whether actions were feasible, fair, robust to stale CSI, or better than strong optimization baselines.
- `Core workflow`: import a versioned synthetic scenario and candidate policy trace; validate dimensions and units; project actions to modeled hardware limits; recompute SINR and spectral efficiency; compare with deterministic and optimization baselines; emit a public-safe evidence report.
- `Data requirements`: synthetic positions and channel matrices, modeled propagation and phase limits, power budgets, timestamps, candidate actions, baseline outputs, seeds, and configuration versions.
- `Architecture`: local CLI; schema validator; deterministic channel/reward calculator; constraint gate; baseline adapter; metric reducer; Markdown/JSON renderer.
- `Success metrics`: exact agreement with hand-worked toy cases; deterministic replay hashes; zero unreported constraint violations; complete seed/config coverage; confidence intervals for repeated runs.
- `Risk controls`: offline by default; no credentials, device drivers, or spectrum-control path; allowlisted export fields; explicit non-certification language; human review before any adapter is developed.
- `Limitations`: the MVP audits modeled traces and cannot prove electromagnetic accuracy, hardware safety, spectrum compliance, real energy use, or general deployment performance.
- `MVP boundary`: no live telemetry, radio actuation, private operational data, automatic policy deployment, or autonomous network changes.
- `Deployment model`: local CLI or notebook using public or synthetic inputs.
- `Evaluation plan`: unit tests for equations and constraints, property tests for monotonic cases, small-instance oracle checks, repeated seeds, and fault injection.
- `Failure modes`: unit mismatch, stale CSI, invalid phase projection, inconsistent reward accounting, baseline under-tuning, hidden random seeds, simulator drift, and overgeneralization from synthetic results.
- `Maintenance plan`: pin schemas and equations, version baseline adapters, preserve regression scenarios, and require review when hardware or channel models change.

## Related Research and Reading

### Exactly Three Related DEP Entries

1. [Multi-Point ISAC](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Multi-Point%20ISAC/multi_point_isac_manuscript.md) - direct overlap in distributed wireless nodes, coupled mode/power decisions, central coordination, and simulation-only evidence; it provides a non-RL allocation comparison point.
2. [Telecom AI Roadmap](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Telecom%20AI%20Roadmap/telecom_ai_roadmap_manuscript.md) - connects telecom AI proposals to digital-twin testing, typed policy gates, authorization, monitoring, and rollback rather than unconstrained network authority.
3. [GPMD Regularized RL](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md) - offers a sharper policy-regularization and error-floor vocabulary that exposes what NVR-MAPPO does not yet prove about convergence or approximation error.

### Primary and Near-Primary Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Joint Power Allocation and Phase Shift Design | Selected primary paper | NVR-MAPPO method and simulation evidence. | https://arxiv.org/abs/2502.19675v1 |
| Multi-Point ISAC primary paper | Methodological neighbor | Coupled wireless allocation with an optimization-based alternative. | https://arxiv.org/abs/2208.07592v2 |
| Large-Scale AI in Telecom | Systems and governance context | Telecom AI deployment constraints and guarded control-plane framing. | https://arxiv.org/abs/2503.04184v1 |
| Generalized Policy Mirror Descent | RL theory context | Regularization geometry, convergence scope, and approximation error floors. | https://arxiv.org/abs/2105.11066v4 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| S1 | https://arxiv.org/abs/2502.19675v1 | identity, authors, subjects, version, abstract, license link | 2026-07-22 | Primary metadata. |
| S2 | https://arxiv.org/pdf/2502.19675; https://arxiv.org/html/2502.19675v1 | complete method, figures, equations, results, limitations | 2026-07-22 | Verified private copies inspected; files withheld. |
| S3 | https://arxiv.org/e-print/2502.19675 | source TeX, algorithm, captions, figure inventory | 2026-07-22 | Verified private source package inspected; file withheld. |
| S4 | https://doi.org/10.48550/arXiv.2502.19675 | persistent identity | 2026-07-22 | arXiv-issued DOI. |
| S5 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Multi-Point%20ISAC/multi_point_isac_manuscript.md | distributed wireless allocation bridge | 2026-07-22 | Related DEP, not validation. |
| S6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-Telecom%20AI%20Roadmap/telecom_ai_roadmap_manuscript.md | operational telecom AI bridge | 2026-07-22 | Related DEP, not validation. |
| S7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md | regularized-RL bridge | 2026-07-22 | Related DEP, not validation. |
| S8 | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | public artifact and source-withholding rules | 2026-07-22 | Live default branch inspected. |
| S9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | cross-repository context and dedup scope | 2026-07-22 | Live default branch inspected. |
| S10 | https://arxiv.org/abs/2502.19675v1 | implementation availability boundary | 2026-07-22 | No official code link in the record or inspected paper; focused search found none. |

## Appendix

### Replication Checklist

- Correct and publish the complete actor objective and every NVR-MAPPO hyperparameter.
- Pin code, dependencies, channel generator, action encoding, reward normalization, seeds, and hardware.
- Reconstruct Figures 3-5 from raw exported values before changing the model.
- Add component ablations and strong optimization baselines.
- Report mean, dispersion, tail performance, constraint violations, runtime, memory, communication, energy, and fairness.
- Test quantized phases, calibration error, stale/noisy CSI, missing agents, and out-of-distribution geometry.

### Source Integrity Summary

The selected unit began as partial because full-paper HTML was absent. One bounded local-only repair preserved the valid PDF and collected verified full-paper HTML, metadata HTML, and the source package. The complete-source gate passed before review. All original and derived source-processing files remain local and were excluded from repository staging.

## Attribution Block

- Source URL: https://arxiv.org/abs/2502.19675v1
  - Applies to: this manuscript.
  - Notes: Canonical metadata and version record.
- Source URL: https://arxiv.org/pdf/2502.19675
  - Applies to: method, equations, figures, simulations, results, and critique.
  - Notes: Complete PDF inspected privately; source file withheld.
- Source URL: https://arxiv.org/html/2502.19675v1
  - Applies to: structural and full-text cross-checking.
  - Notes: Complete HTML inspected privately; source file withheld.
- Source URL: https://arxiv.org/e-print/2502.19675
  - Applies to: source-level equation, algorithm, caption, and figure inspection.
  - Notes: Source package inspected privately; source file withheld.
