---
title: "Joint Sensing MEC - DEP-E"
generated_at: "2026-07-15 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of joint sensing, age-of-information, and computation-offloading optimization for MEC-assisted IoT status updates."
source_status: "verified local PDF, full-paper HTML, metadata HTML, and source package; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-15"
temporal_cutoff: "arXiv v1 submitted 2022-10-31; journal publication and author-hosted version cross-checked through 2026-07-15"
primary_url: "https://arxiv.org/abs/2210.17025"
stable_identifier: "arXiv:2210.17025v1; DOI 10.1109/TWC.2023.3261338"
confidence_summary: "High for source identity and formulation; medium for empirical and convergence claims because simulations were not reproduced and no official code was found."
safety_scope: "research review and simulation-only scheduling design; no live control or network authorization"
distribution_notes: "Generated Markdown and public URLs only; all source files, extracted text, and caches withheld locally."
---

# Joint Sensing MEC - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2210.17025v1 | https://arxiv.org/abs/2210.17025 | arXiv non-exclusive distribution license indicated on the record. | 2026-07-15 | Inspected |
| S2 | arXiv paper bundle | Primary paper | PDF, full-paper HTML, TeX source | arXiv:2210.17025v1 | https://arxiv.org/pdf/2210.17025; https://ar5iv.labs.arxiv.org/html/2210.17025; https://arxiv.org/e-print/2210.17025 | Verified private copies were inspected; no source file was redistributed. | 2026-07-15 | Fully inspected and integrity-verified |
| S3 | Journal article | Published version | Author-hosted IEEE article and publisher DOI | IEEE TWC 22(11), 8230-8243; DOI 10.1109/TWC.2023.3261338 | https://www.eng.auburn.edu/~szm0001/papers/TWC2023Chen.pdf; https://doi.org/10.1109/TWC.2023.3261338 | IEEE terms apply; used for publication metadata and consistency checks. | 2026-07-15 | Key sections and metadata inspected |
| S4 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2210.17025 | https://doi.org/10.48550/arXiv.2210.17025 | Persistent arXiv locator. | 2026-07-15 | Verified from arXiv |
| S5 | Extraction cache public summary | Processing evidence | Public-safe JSON summary | schema 1.0; status `cached` | Public URLs from S1-S2 | Local cache paths and extracted text withheld. | 2026-07-15 | PDF, HTML, and source extraction succeeded |
| S6 | Black Lake repository authorities | Deposition rules | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Public repository standards. | 2026-07-15 | Fetched and read |
| S7 | Black-Lake-Data authority | Companion repository rules | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public repository standard used for related-entry and dedup context. | 2026-07-15 | Fetched and read |
| S8 | Self-Learned IDC DEP-E | Related processed artifact | Markdown | DEP-E-20260710-Self Learned IDC | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Self%20Learned%20IDC/self_learned_idc_manuscript.md | Conceptual synthesis only; underlying sources separately attributed. | 2026-07-15 | Inspected |
| S9 | RRT-CBF Motion DEP-E | Related processed artifact | Markdown | DEP-E-20260711-RRT-CBF Motion | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md | Conceptual synthesis only; underlying sources separately attributed. | 2026-07-15 | Inspected |
| S10 | iKalibr Calibration DEP-E | Related processed artifact | Markdown | DEP-E-20260714-iKalibr Calibration | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Conceptual synthesis only; underlying sources separately attributed. | 2026-07-15 | Inspected |

The paper authors are Yi Chen, Zheng Chang, Geyong Min, Shiwen Mao, and Timo Hämäläinen. The arXiv record reports one version submitted on 2022-10-31 in `cs.NI`. The later journal article was published in *IEEE Transactions on Wireless Communications*, volume 22, issue 11, pages 8230-8243, November 2023. The journal DOI is `10.1109/TWC.2023.3261338`. A targeted web and GitHub search found no official implementation repository; absence from those searches does not prove that code does not exist.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S3, S4 | Primary and publisher metadata | Title, authors, versions, dates, venue, pages, arXiv ID, and DOI. | Source identity and chronology. | High | Journal page access was supplemented by an author-hosted article and author publication list. |
| E2 | S2 | Full primary paper | Sections III-V, equations 1-29, system model, AoI derivation, energy model, objective, and constraints. | Problem formulation and assumptions. | High | Equations were inspected but not independently rederived end to end. |
| E3 | S2, S3 | Full paper and published version | Algorithms 1-3, potential-game argument, block-coordinate iteration, complexity statements, and appendices. | Optimization mechanism and convergence claims. | Medium-high | The apparent improvement-expression ambiguity and global-optimality gap were not resolved by code. |
| E4 | S2, S3 | Full paper and published version | Simulation setup, parameter table/text, baselines, Figures 4-10, and result discussion. | Source-reported empirical claims and threshold observations. | Medium | No code, seeds, raw values, confidence intervals, or reproduced runs were available. |
| E5 | S2, S3 | Full paper and published version | Assumptions, conclusion, and differences between arXiv and journal framing. | Boundary conditions and reviewer critique. | Medium-high | The paper has no dedicated limitations section. |
| E6 | S5 | Public-safe extraction summary | `pypdf`, HTML-regex, and tar extraction status; text-output presence; fallback reason. | Complete local review coverage and cache methodology. | High | Extracted text can contain typography noise; local records are private. |
| E7 | S6, S7 | Repository authorities | DEP class, filing, publication index, source withholding, README, attribution, and commit rules. | Deposit compliance. | High | Process evidence only. |
| E8 | S8-S10 | Related DEP manuscripts | State/control latency, fresh-state safety gates, spatiotemporal calibration, and staged optimization. | Cross-DEP synthesis. | Medium-high | Related entries do not validate the selected paper's theory or results. |
| E9 | Dedup scans and automation memory | Process evidence | Identifier, DOI, normalized-title, slug, artifact, and recent-marker searches. | Eligibility and reselection validation. | High | Search quality depends on available repository text and normalized identifiers. |

## Executive Summary

The paper studies an MEC-assisted IoT status-update loop in which sampling frequency, repeated sensing, and local-versus-edge computation jointly affect both information freshness and device energy. Its core contribution is to put these decisions inside one weighted objective. Age of information (AoI) penalizes stale status; sensing, transmission, and local computation consume energy; insufficient sensing can generate invalid updates and force the whole sensing-processing cycle to repeat.

The model derives average AoI for periodic, independent status generation as one-half of the sampling interval plus the expected successful processing time. It then formulates a mixed continuous-discrete optimization over sampling intervals, numbers of sensing attempts, and binary offloading choices. The authors decompose the NP-hard problem into three updates: a closed-form sampling-interval step, a bounded enumeration for sensing repetitions, and a potential-game best-response procedure for computation offloading. MISCO alternates these updates until the total weighted cost changes by less than a threshold.

The simulations report that MISCO has the lowest system cost among the tested baselines as device count and computation load vary. They also expose regime changes: with 1,000 megacycles, sensing begins to dominate the sensing-processing ratio above a reported sensing-success threshold near 0.65; with 1,500 megacycles, the transition occurs above about 0.7; and, in the tested configuration, system cost begins to increase when the minimum sampling interval exceeds roughly 1.4 seconds. These values are scenario-specific, not universal control settings.

Reviewer assessment: the paper offers a useful scheduling abstraction and a clear decomposition, but it does not establish production readiness or a global optimum. The evidence is simulation-only, the sensing/channel/task assumptions are narrow, no implementation was found, repeated-seed uncertainty is not reported, and the finite-improvement/monotonic-descent arguments support convergence to a stable iterative point rather than global optimality for the original mixed problem.

## Detailed Summary

### Problem Context

IoT status monitoring has three coupled clocks. Sampling decides when a device creates an update. Sensing determines whether the update correctly captures an environmental event. Processing extracts usable information, either locally or after wireless transmission to an MEC server. Optimizing any one clock in isolation can make another worse: frequent sampling reduces nominal AoI but consumes more energy; longer sensing raises success probability but adds delay; edge execution can reduce compute time but adds transmission energy and interference.

The paper's central design choice is therefore a composite system cost rather than a latency-only objective. For device `i`, the cost combines average AoI with energy consumed per unit time, using weights `mu_t` and `mu_e`. This makes the policy sensitive to application priorities, but it also means the scale and interpretation of those weights are part of the result.

### System and Sensing Model

The model contains `N` independent IoT devices, one base station/control unit, and one nearby MEC server. Each device periodically samples with interval `tau_i`. A task is summarized by data size `d_i` and required CPU cycles `c_i`.

One sensing operation succeeds with probability modeled as `rho_i = exp(-xi D_i^s)`, where distance and an environment-quality parameter determine the result. Repeating sensing `s_i` times gives success probability `P_i(s_i) = 1 - (1-rho_i)^{s_i}`. Sensing time and sensing energy both grow linearly with `s_i`. Feasibility requires the repetitions to fit inside the sampling interval and the final success probability to exceed `p_min`.

This model captures a real design tension but is deliberately compact. It assumes independent repeated attempts, a stationary distance-based success law, and a device that learns validity only after processing. Correlated sensor failures, changing environments, multi-modal sensing, or partial information quality are outside the formulation.

### Transmission and Computation

The offloading decision is binary. Local execution incurs CPU latency `c_i/f_i` and a per-cycle device-energy cost. Edge execution adds uplink transmission latency and energy, then uses server frequency `f_e`. The uplink rate follows a shared-channel interference model, so one device's offloading choice can reduce another device's rate.

The server also has a data-capacity threshold. The paper proposes an availability-request mechanism and, when overloaded, removes the largest data tasks until the threshold is restored. This makes the constraint operational, but the removal policy raises fairness and starvation questions because large tasks are disadvantaged regardless of urgency or marginal freshness benefit.

### AoI Derivation

An update becomes valid only after successful sensing and processing. Because a sensing-processing attempt can fail and repeat, the expected successful processing time is the one-attempt time divided by the sensing-success probability. Under periodic generation and independence between inter-generation time and processing time, the average AoI becomes:

`Delta_i(s_i, tau_i, x) = 0.5 * tau_i + T_i^(1,prcs)(s_i,x) / P_i(s_i)`.

This equation is the conceptual hinge of the paper. It exposes two distinct causes of staleness: waiting to sample and waiting to obtain a valid processed update. It also makes poor sensing quality multiplicatively expensive because processing time is paid again when attempts fail.

### Joint Objective and Decomposition

Energy per unit time includes sensing plus either transmission or local-computation energy, divided by the sampling interval. The complete optimization minimizes the sum of device costs subject to sensing-time, binary-offload, minimum-sampling, minimum-success, and server-capacity constraints. Continuous sampling intervals and discrete sensing/offloading variables make the feasible region non-convex; the authors classify the problem as NP-hard.

The decomposition has three steps:

1. **Sampling interval:** With sensing and offloading fixed, differentiating the cost yields a square-root stationary point, clipped to the minimum sampling interval.
2. **Sensing repetitions:** With other choices fixed, a bounded enumeration increments repetitions while cost decreases, relying on the relaxed sensing-cost curve's convex shape.
3. **Offloading:** Each device chooses local or edge execution based on an interference threshold. A potential-game argument gives at least one Nash equilibrium and finite improvement under sequential best-response updates.

MISCO then alternates the three steps. The journal version explicitly describes the outer procedure as block coordinate descent. The paper argues convergence because each update decreases a lower-bounded total cost. That is a useful termination argument, but for a non-convex mixed problem it should not be read as proof of global optimality.

### Simulation Setup and Results

The simulation places devices randomly in a `50 m x 50 m` MEC coverage area. Representative parameters include `0.2 s` per sensing operation, `500 KB` task size, `1,000` megacycles per task, `100 MHz` bandwidth, `100 mW` transmit power, local CPU frequencies from `0.8` to `1.0 GHz`, and a `20 GHz` MEC server. The arXiv version compares against greedy sensing, instant/zero-wait sampling, best-response offloading, and all-edge offloading; the journal version additionally discusses stochastic-gradient offloading.

The source reports these qualitative findings:

- MISCO's weighted cost remains below the tested baselines as the number of IoT devices grows, with a larger advantage when uplink interference makes all-edge execution unattractive.
- As computation load rises, all methods become more expensive and MISCO approaches all-edge behavior because local processing becomes slow.
- Sensing dominates total sensing-processing time when success requirements are high and compute load is modest; processing dominates at high computation loads.
- In the tested setup, cost stays relatively flat for low sensing-success thresholds and rises after about `0.7` because the constraint forces additional sensing.
- In the tested setup, minimum sampling intervals above about `1.4 s` increase AoI enough to raise total cost.
- Iteration count grows with device population and then saturates when interference makes local execution preferable for most devices.

No raw points, seed schedule, confidence intervals, hardware runtime, or code were found. The figures demonstrate the intended trends but do not establish robustness across traffic models, fading, sensing correlations, or real device workloads.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Jointly modeling sampling, sensing validity, and computation reveals an AoI-energy tradeoff that isolated optimization misses. | Author formulation claim | E2 | Directly supported by the objective and derived AoI/energy terms under the paper's assumptions. | High for formulation |
| C2 | Average AoI equals half the periodic sampling interval plus success-adjusted processing time. | Author analytical claim | E2 | Supported by the renewal-area derivation, conditional on independence and periodic generation. | Medium-high |
| C3 | The offloading game has a Nash equilibrium and finite improvement property. | Author theoretical claim | E3 | The paper supplies a potential-game argument; it was not independently proved or machine-checked. | Medium-high |
| C4 | MISCO converges because each coordinate update lowers a bounded objective. | Author theoretical claim | E3 | Plausible as a descent/termination statement, but it does not establish the global optimum of the original NP-hard problem. | Medium |
| C5 | MISCO produces the lowest system cost among the tested baselines. | Author empirical claim | E4 | Supported by source-reported simulation figures only; no independent reproduction or uncertainty analysis. | Medium |
| C6 | Thresholds near `0.7` success probability and `1.4 s` sampling interval are useful operating points. | Author empirical interpretation | E4 | Valid only for the reported parameterization; unsafe to generalize as universal policy. | Low-medium |
| C7 | Calibration and state freshness should be treated as inputs to an MEC scheduling policy, not as invisible constants. | Reviewer interpretation | E8 | Supported conceptually across related entries; not tested by this paper. | Medium-high |

## Methodology

- `Research objective`: Select one eligible local arXiv paper uniformly, enforce the complete-source gate, review it source-first, connect it to exactly three related DEP entries, and create a schema-complete public-safe DEP-E artifact.
- `Sources inspected`: Verified arXiv PDF, full-paper HTML, metadata HTML, TeX/source extraction, public arXiv record, author-hosted journal article, publisher DOI metadata, author publication metadata, live repository authorities, automation memory, dedup locations, and three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`; treated each unique PDF parent as one paper unit; selected a uniform PowerShell `Get-Random` index; derived the arXiv ID from the filename and README; then checked arXiv ID, DOI, normalized title, slug, artifact paths, automation memory, Black-Lake-Data searches, and recent worktree markers.
- `Inclusion criteria`: Sources had to identify the work, directly support method/result/limitation claims, define repository rules, establish selection integrity, or provide concrete conceptual overlap with sensing integrity, fresh-state control, or state-to-action latency.
- `Exclusion criteria`: Abstract-only HTML was rejected as the paper. Search/recommender pages were not used as technical evidence. Source files, caches, extracted text, and local filesystem details were excluded from public output.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Author claims, reviewer interpretations, and process evidence are separated. Quantitative statements remain source-reported and map to evidence IDs.
- `Uncertainty handling`: Non-reproduction, missing code, model assumptions, version differences, possible equation ambiguity, and limited empirical reporting are explicit.
- `Extraction process`: Preflight found `pypdf` but not `pdftotext`. Missing-only extraction used `pypdf`, HTML-regex, and `tarfile`; all three completed, with `pypdf` recorded as the fallback because `pdftotext` was unavailable.
- `Cache methodology`: The selected paper began as a cache miss. After source-integrity repair, missing-only extraction produced a `cached` record with 69,290 bytes of PDF text, 102,224 bytes of HTML text, and 84,754 bytes of source text.
- `Random selection`: 75,776 PDF-parent paper units; zero-based random index 7,665; the first draw was eligible; duplicate exclusions 0; reselections 0.
- `Deduplication and reselection validation`: No prior marker was found in the public dedup index, Black Lake logs/reports/DEPs, automation memory, relevant Black-Lake-Data searches, or other active worktree artifacts after excluding the temporary private repair input. No same-paper marker was found within the preceding 24 hours.
- `Version control`: Primary technical review is pinned to arXiv v1. The journal DOI and author-hosted published version were inspected for publication metadata and consistency, but no exhaustive line-by-line version diff was performed.
- `Reviewer stance`: DEP-ready preservation, skeptical paper review, bounded implementation translation, and reproducibility planning.

## Scope, Constraints, and Assumptions

- `Scope`: The sensing-sampling-processing model, AoI/energy objective, MISCO decomposition, source-reported simulations, publication context, and relationship to exactly three existing Black Lake DEP entries.
- `Temporal boundary`: arXiv v1 submitted 2022-10-31; journal publication metadata and public related artifacts inspected through the date-only 2026-07-15 marker.
- `Evidence limits`: No simulation, algorithm, code, or hardware benchmark was executed. No official code repository was found. Journal and preprint versions were not exhaustively diffed.
- `Assumptions`: Periodic and independent update generation; repeated independent sensing attempts; stationary distance-based sensing quality; binary local/edge execution; modeled shared-channel interference; stable task descriptors; and source-reported equations/units are materially correct.
- `Constraints`: Original sources remain local. Public artifacts contain only derived Markdown, repository-relative paths, stable identifiers, and public URLs. Any live network/control use requires separate authorization and safety review.
- `Out of scope`: Global-optimality proof, formal verification, real-device deployment, workload tracing, radio emulation, reproducing figures, and selecting production values for `p_min`, `tau_min`, or the objective weights.
- `Intended use`: Research deposition, implementation ideation, replication planning, and review of freshness-aware edge scheduling.
- `Audience`: Edge-computing researchers, IoT systems engineers, control reviewers, and Black Lake maintainers.
- `Reproducibility boundary`: The equations and pseudocode can seed a toy simulator, but exact figures require missing code, seeds, raw values, and environment details.
- `Data sensitivity`: Public scholarly sources only; local source-document and cache locations withheld.

## Observations

- `Observed pattern`: The paper treats sensing failure as repeated processing delay, which makes sensing quality a first-class freshness variable rather than a separate perception metric.
- `Technical implication`: A production scheduler would need timestamps and validity/confidence from the sensing pipeline; otherwise it cannot evaluate the success-adjusted AoI term.
- `Observed pattern`: Offloading value changes with other devices' choices because interference couples their rates, making static per-device offload rules incomplete.
- `Contradiction or tension`: The paper repeatedly calls outputs optimal, while its NP-hard decomposition, potential-game equilibrium, and block-coordinate descent support a stable local solution more directly than a global optimum.
- `Evidence-quality implication`: The reported `0.7` and `1.4 s` thresholds are visually useful sensitivity markers but are not portable constants.
- `Open question`: How would correlated sensing failures, bursty arrivals, queueing at the MEC server, and time-varying radio channels change the decomposition and convergence behavior?
- `Reviewer hypothesis`: The most reusable artifact is not the MISCO algorithm alone, but a freshness-energy evidence ledger that makes every scheduling decision traceable to state age, sensing validity, energy, interference, and capacity.

## Considerations

The cost weights combine time and energy with different units. A real deployment must document normalization, stakeholder priorities, battery-health policy, and how unsafe staleness is bounded rather than merely traded away. High-consequence monitoring may require a hard AoI constraint in addition to a weighted objective.

Server admission deserves more attention. Removing the largest tasks is simple, but it can starve high-value sensors or tasks whose large payloads are essential. Alternatives should measure urgency, marginal freshness gain, safety class, deadline, and fairness. They should also report how often edge capacity is denied and what local fallback occurs.

The model assumes validity is discovered after processing. Modern sensor systems may expose confidence earlier, fuse multiple modalities, or stream partial results. A useful extension would separate observation confidence, semantic validity, and final computation quality rather than encode all failure in one Bernoulli sensing probability.

Operational evidence should include p95/p99 decision latency, queue depth, radio retries, server contention, energy measurement error, state-clock synchronization, stale-decision rejection, and fail-safe behavior. Average system cost alone can conceal rare but unacceptable freshness failures.

## Strengths

- The paper couples sensing validity and processing delay instead of treating status updates as always valid.
- The AoI derivation gives a compact mechanism for explaining why failed sensing multiplies processing cost.
- The three-part decomposition is easy to audit conceptually and maps to distinct engineering subsystems.
- The offloading model captures strategic interference rather than assuming independent device decisions.
- Simulations cover device count, computation load, sensing threshold, sampling threshold, and convergence behavior.
- The journal publication and author-hosted article provide strong source identity and a more polished framing of the method.

## Weaknesses

- Evaluation is simulation-only; no hardware, network trace, sensor dataset, or measured power result is presented.
- No official code, configuration bundle, raw values, deterministic seeds, or automated figure reproduction was found.
- Repeated-trial distributions, confidence intervals, robustness tests, and statistical comparisons are absent.
- Independent periodic arrivals and independent sensing attempts limit realism for correlated physical events and bursty traffic.
- The server-capacity rule can be unfair to large tasks and does not model queueing or service scheduling in depth.
- Convergence does not establish the global optimum, despite some source wording suggesting optimality.
- The extracted improvement expression appears to subtract identical-looking cost terms, leaving an implementation-critical ambiguity without code or erratum resolution.
- Scenario-specific thresholds are discussed as recommendations without a broad sensitivity or transfer study.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code, configs, seeds, and raw figure values | Reproducibility | Current figures cannot be independently reconstructed. | Auditable claims and easier extensions. | Maintenance and environment burden. | Rebuild every figure in a pinned environment and compare hashes/data. |
| Clarify equilibrium and improvement equations | Theory/implementation | The cost-improvement expression is ambiguous and global-optimality language is too strong. | Correct implementations and calibrated claims. | Requires author or erratum review. | Provide a checked derivation and unit tests over toy games. |
| Add stochastic queues and time-varying channels | System realism | MEC contention is more than a data-capacity threshold. | Better transfer to operational networks. | Larger state space and more difficult analysis. | Compare against packet-level simulation and public traces. |
| Model correlated and confidence-valued sensing | Sensing realism | Bernoulli independent attempts collapse important failure structure. | Better handling of environmental and multi-modal uncertainty. | Requires sensor data and calibration. | Fit/validate models on authorized public sensing datasets. |
| Replace largest-task eviction with value-aware admission | Fairness | Payload size alone can starve important tasks. | Better urgency, safety, and fairness behavior. | Policy complexity and possible gaming. | Report per-device delay, denial, AoI, and energy distributions. |
| Report hard freshness violations and tail latency | Safety/operations | Mean cost hides rare stale decisions. | Stronger reliability evidence. | More trials and logging. | Stress queues/radio failures and measure p95/p99 plus violation counts. |

## Potential Implementations

1. **Freshness-Energy Policy Auditor**
   - `User`: IoT research or platform-review team.
   - `Goal`: Check whether a proposed scheduler's decisions are traceable to freshness, sensing validity, energy, interference, and capacity evidence.
   - `Core mechanism`: Replay public or synthetic traces, calculate per-device AoI/energy components, and produce a decision ledger.
   - `Required inputs`: Synthetic timestamps, validity probabilities, task sizes/cycles, radio estimates, device/server compute rates, and policy outputs.
   - `Outputs`: Cost decomposition, hard freshness violations, admission decisions, fairness metrics, and source-linked report.
   - `Risk controls`: Simulation-only; no live device credentials or actuator path; fail closed on missing units/timestamps.
   - `Evaluation`: Deterministic replay, seeded edge cases, dimensional checks, and comparison with hand-calculated toy cases.

2. **MEC Offloading Game Sandbox**
   - `User`: Networking researcher or graduate course.
   - `Goal`: Explore how interference and server limits change local-versus-edge decisions.
   - `Core mechanism`: Implement the binary best-response game on synthetic devices and compare equilibria with exhaustive search for small `N`.
   - `Required inputs`: Toy channel gains, powers, task descriptors, energy weights, and capacity limits.
   - `Outputs`: Equilibrium trajectory, global-gap estimate for small cases, denial/fairness ledger, and convergence plot.
   - `Risk controls`: Synthetic parameters only; no network scanning or radio control.
   - `Evaluation`: Exhaustive oracle for `N <= 12`, multiple initialization orders, and invariant/property tests.

3. **Fresh-State Edge Gate**
   - `User`: Simulation-stage embodied-control engineer.
   - `Goal`: Reject stale or invalid observations before an edge-computed action is authorized.
   - `Core mechanism`: Combine calibrated sensor timestamps, a validity/confidence threshold, maximum AoI, and an explicit local fallback.
   - `Required inputs`: Timestamped synthetic sensor records, calibration version, confidence, edge result time, and fallback policy.
   - `Outputs`: Accept/reject decision, reason code, observed AoI, and fallback event.
   - `Risk controls`: No live actuation; mandatory stale-state rejection; human-reviewed thresholds; source-local data stays private.
   - `Evaluation`: Inject clock offsets, delayed packets, low-confidence observations, and edge timeouts.

## Three Ways to Exercise This Research

1. `Equation-level toy audit`: Objective: reconstruct AoI and energy cost for two synthetic devices. Inputs: a small hand-authored parameter table. Method: calculate sensing success, repeated processing time, AoI, energy, and total cost under local/edge choices. Output: a checked worksheet or script. Success criterion: independent calculations match and units are explicit. Stop condition: any source symbol or unit remains ambiguous.
2. `Small-game exhaustive comparison`: Objective: measure the gap between best-response equilibrium and the global minimum. Inputs: synthetic cases with at most 12 devices. Method: enumerate all binary offload profiles and compare with multiple best-response orders. Output: gap and convergence distributions. Success criterion: every equilibrium is reproducible and any suboptimality is visible. Stop condition: do not generalize toy gaps to production networks.
3. `Freshness fault injection`: Objective: test whether a simulated edge gate rejects stale observations. Inputs: synthetic timestamps, confidence values, calibration offsets, and timeouts. Method: inject delay, clock skew, and sensing failures; record decisions and fallbacks. Output: violation/fallback ledger. Success criterion: all over-age or invalid cases fail closed. Stop condition: no live actuator or uncontrolled network interface may be connected.

## Example MVP Product

- `Product name`: FreshEdge Replay.
- `Target user`: IoT and edge-computing research teams reviewing scheduling policies before a simulator or testbed deployment.
- `Problem`: Weighted average cost plots do not reveal why a device sampled, repeated sensing, offloaded, was denied edge capacity, or exceeded a hard freshness bound.
- `Core workflow`: Import a synthetic/public trace and policy decisions; validate units and timestamps; calculate per-device AoI, sensing-success adjustment, energy, interference, and capacity; compare decisions with simple baselines; emit a Markdown/JSON evidence report.
- `Data requirements`: Date-free synthetic device IDs, sampling/generation/completion timestamps, sensing outcomes or probabilities, task sizes/cycles, modeled channel rates, compute rates, energy coefficients, and policy decisions.
- `Architecture`: Local CLI; schema validator; deterministic replay engine; plug-in policy adapter; exhaustive oracle for small cases; metric reducer; public-safe report renderer.
- `Success metrics`: 100% rejection of malformed units/timestamps in a test corpus; exact agreement with hand calculations; deterministic replay hashes; complete decision reason coverage; zero source-document or local-path leakage.
- `Risk controls`: Offline/simulation-only operation, allowlisted export fields, no credentials, no radio/device control, explicit non-certification language, and hard freshness-violation reporting.
- `Limitations`: The MVP audits modeled decisions; it cannot prove real sensor validity, radio behavior, energy use, control safety, or global optimality at scale.
- `MVP boundary`: No live telemetry, device actuation, wireless control, private operational traces, or automated production policy deployment.
- `Deployment model`: Local CLI or notebook with repository-friendly Markdown/JSON output.
- `Evaluation plan`: Unit tests for equations, property tests for monotonic cases, exhaustive small-game comparison, fault-injection scenarios, and independent reviewer agreement.
- `Failure modes`: Incorrect units, clock skew, missing events, misleading probability estimates, silent fallback, unfair admission, policy adapter drift, and overgeneralization from synthetic traces.
- `Maintenance plan`: Version the schema/equations, preserve a regression corpus, pin dependencies, and require review when adding new sensing or queueing models.

## Related Research and Reading

| Item | Type | Relevance | Public locator |
|---|---|---|---|
| Joint Optimization of Sensing and Computation | Primary paper | Reviewed AoI-energy sensing and MEC-offloading framework. | https://arxiv.org/abs/2210.17025 |
| Published IEEE TWC version | Published primary source | Publication record and polished block-coordinate formulation. | https://doi.org/10.1109/TWC.2023.3261338 |
| Self-Learned IDC DEP-E | Related Black Lake research | Connects heterogeneous sensor observations and state representation to real-time constrained control; motivates preserving state age and decision latency. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Self%20Learned%20IDC/self_learned_idc_manuscript.md |
| RRT-CBF Motion DEP-E | Related Black Lake research | Treats state age, solver latency, safety margins, and fallbacks as control-loop evidence; complements AoI with hard admissibility. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md |
| iKalibr Calibration DEP-E | Related Black Lake research | Shows that sensor timestamps and spatial calibration are upstream integrity conditions; its staged refinement parallels decomposed iterative optimization. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md |
| Age of Information survey | Primary background | Foundational AoI definitions and status-update systems context cited by the paper. | https://doi.org/10.1109/JSAC.2021.3065072 |
| Energy-Efficient Joint Optimization with Mean-Field Game | Published follow-on context | Later large-population sensing/computation optimization direction involving Zheng Chang. | https://doi.org/10.1109/JIOT.2024.3443701 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2210.17025 | Identity, abstract, authors, submission date, category, arXiv DOI, license, and source links. | 2026-07-15 | Primary metadata. |
| R2 | https://arxiv.org/pdf/2210.17025 | Full paper, equations, algorithms, simulations, figures/captions, appendices, and references. | 2026-07-15 | Public equivalent; verified local PDF withheld. |
| R3 | https://ar5iv.labs.arxiv.org/html/2210.17025 | Full-paper HTML used after the official arXiv HTML endpoint was unavailable for this paper. | 2026-07-15 | Passed full-paper integrity checks; local copy withheld. |
| R4 | https://arxiv.org/e-print/2210.17025 | TeX/source extraction and equation/section cross-check. | 2026-07-15 | Source package withheld locally. |
| R5 | https://doi.org/10.48550/arXiv.2210.17025 | Persistent arXiv identifier. | 2026-07-15 | Primary DOI locator. |
| R6 | https://doi.org/10.1109/TWC.2023.3261338 | Journal DOI and publication identity. | 2026-07-15 | Publisher locator. |
| R7 | https://www.eng.auburn.edu/~szm0001/papers/TWC2023Chen.pdf | Published article metadata, formulation, algorithms, and simulation discussion. | 2026-07-15 | Author-hosted IEEE article; no file deposited. |
| R8 | https://www.eng.auburn.edu/~szm0001/publications-bib.html | Journal volume, issue, pages, year, and DOI cross-check. | 2026-07-15 | Author publication list. |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository deposition and source-withholding rules. | 2026-07-15 | Live default branch inspected. |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E container and publication-index authority. | 2026-07-15 | Live default branch inspected. |
| R11 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository context used before related-entry exploration. | 2026-07-15 | Live default branch inspected. |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Self%20Learned%20IDC/self_learned_idc_manuscript.md | Related-entry synthesis around sensor state and control latency. | 2026-07-15 | Does not validate selected-paper claims. |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md | Related-entry synthesis around fresh-state safety gates and fallback. | 2026-07-15 | Does not validate selected-paper claims. |
| R14 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Related-entry synthesis around spatiotemporal sensing integrity and staged optimization. | 2026-07-15 | Does not validate selected-paper claims. |
| R15 | https://doi.org/10.1109/JSAC.2021.3065072 | AoI survey background. | 2026-07-15 | Near-primary related reading. |
| R16 | https://doi.org/10.1109/JIOT.2024.3443701 | Later sensing/computation optimization context. | 2026-07-15 | Related reading; not used to validate selected results. |

## Appendix

### A. Random Selection and Dedup Record

| Field | Value |
|---|---|
| Enumeration | `rg --files -g "*.pdf"` |
| Paper unit | Unique PDF parent directory |
| Candidate units | 75,776 |
| Random method | Uniform PowerShell `Get-Random` index |
| Selected zero-based index | 7,665 |
| Selected ID | 2210.17025 |
| Exclusions before acceptance | 0 |
| Duplicate reselections | 0 |
| Detailed matches | 0 by ID, DOI, normalized title, slug, or artifact marker |
| Same-paper markers in prior 24 hours | 0 |

### B. Complete-Source Integrity Record

The selected unit was initially `partial`: its PDF was complete, but full-paper HTML was absent. Review paused. A bounded one-paper repair downloaded a companion bundle; the downloaded PDF hash matched the preserved PDF exactly. Full-paper HTML used the approved ar5iv fallback because official arXiv HTML was unavailable. Metadata HTML, TeX source, README, attribution, machine summary, and verification records were updated locally before review resumed.

| Check | Observed | Result |
|---|---:|---|
| PDF bytes | 803,785 | Pass: at least 10 KB |
| PDF header | `%PDF-` | Pass |
| PDF trailing marker | `%%EOF` present | Pass |
| Downloaded/preserved PDF hash | Identical | Pass; valid original preserved |
| Full-paper HTML bytes | 1,182,606 | Pass: at least 5 KB |
| HTML body characters | 120,156 | Pass: at least 2,000 |
| HTML article/main/LaTeXML marker | Present | Pass |
| HTML heading/section markers | 77 | Pass: at least 2 |
| Paper-structure terms | Introduction, Method, Approach, Results, Conclusion, References, Appendix | Pass: at least 2 |
| Metadata HTML | 42,171 bytes; metadata only | Pass; not counted as paper |
| TeX/source package | 479,154 bytes | Collected locally and extracted |
| Remaining partial files | 0 | Pass |
| Final classification | `complete` | Gate passed |

### C. Extraction Cache Record

| Field | Value |
|---|---|
| Initial status | Miss |
| Mode | `missing-only` |
| Final status | `cached` |
| PDF extractor | `pypdf` (`pdftotext` unavailable) |
| HTML extractor | `html-regex` |
| Source extractor | `tarfile` |
| PDF text | 69,290 bytes |
| HTML text | 102,224 bytes |
| Source text | 84,754 bytes |
| Network during extraction | None; local repaired bundle used |

### D. Replication Checklist

- [ ] Pin arXiv v1, the journal article, and any future errata or code release.
- [ ] Reconcile the cost-improvement expression and document the exact potential function.
- [ ] Implement dimensional/unit checks for every objective term.
- [ ] Reproduce the square-root sampling update and bounded sensing enumeration on hand-calculated cases.
- [ ] Compare best-response equilibria with exhaustive global optima for small device populations.
- [ ] Publish deterministic simulation seeds, raw values, and figure-generation scripts.
- [ ] Add bursty queues, time-varying channels, correlated sensing errors, and heterogeneous deadlines.
- [ ] Report tail AoI, hard freshness violations, denial/fairness metrics, and fallback behavior.
- [ ] Keep all paper/source/cache files outside public repository output.

### E. Source Locality Statement

The verified PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, private manifest, and cache remain local. This public DEP contains no original source file, no `.source/` directory, and no local filesystem locator.
