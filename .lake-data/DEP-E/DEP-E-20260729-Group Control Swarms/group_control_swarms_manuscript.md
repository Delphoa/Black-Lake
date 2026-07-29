---
title: "Group-Control Swarms - DEP-E"
generated_at: "2026-07-29 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of group-control, controllability, and motion-planning tradeoffs for globally actuated microrobot swarms."
source_status: "complete local source bundle verified and withheld; public URLs only in DEP"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-29"
temporal_cutoff: "arXiv v2 revised 2024-12-10; WAFR 2024 and Springer chapter context inspected through the public review date"
primary_url: "https://arxiv.org/abs/2406.13829v2"
stable_identifier: "arXiv:2406.13829v2; DOI 10.48550/arXiv.2406.13829; DOI 10.1007/978-3-032-09967-9_14"
confidence_summary: "High for source identity, model reconstruction, and reported table values; medium for formal and simulation claims; low for physical deployment because proofs and experiments were not independently reproduced."
safety_scope: "offline research review, simulation, and supervised non-actuating implementation planning"
distribution_notes: "Original PDF, HTML, metadata, TeX source, extracted text, renders, and verification records remain local and were not deposited."
---

# Group-Control Swarms - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Reference | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract page | Primary metadata | HTML | arXiv:2406.13829v2 | https://arxiv.org/abs/2406.13829v2 | Public metadata; arXiv non-exclusive distribution context does not authorize repository redistribution of local source files. | 2026-07-29 | Inspected |
| S2 | Group-Control Motion Planning Framework for Microrobot Swarms in a Global Field | Primary paper | PDF and official full-paper HTML | arXiv:2406.13829v2 | https://arxiv.org/pdf/2406.13829v2 ; https://arxiv.org/html/2406.13829v2 | Complete paper inspected; source files withheld locally. | 2026-07-29 | Inspected across all 18 PDF pages and all major HTML sections |
| S3 | arXiv source package | Primary implementation evidence | TeX and figures | arXiv:2406.13829v2 | https://arxiv.org/e-print/2406.13829v2 | Source archive inspected locally for formulas, tables, and captions; not redistributed. | 2026-07-29 | Inspected |
| S4 | Springer chapter | Proceedings metadata | Chapter record | DOI 10.1007/978-3-032-09967-9_14 | https://doi.org/10.1007/978-3-032-09967-9_14 | Bibliographic and publisher terms apply. | 2026-07-29 | Inspected |
| S5 | WAFR 2024 public paper | Proceedings context | PDF | Paper 65 | https://algorithmic-robotics.org/papers/65_Group_Control_Motion_Planni.pdf | Public paper locator; no copy deposited. | 2026-07-29 | Inspected for identity and proceedings context |
| S6 | Black Lake and Black-Lake-Data repository rules | Repository authority | Markdown | live `main` README files and Black Lake `.lake-data/README.md` | https://github.com/Delphoa/Black-Lake/blob/main/README.md ; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md ; https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public repository rules. | 2026-07-29 | Fetched and read |
| S7 | RRT-CBF Motion - DEP-E | Related DEP | Markdown | DEP-E-20260711-RRT-CBF Motion | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md | Processed Black Lake artifact. | 2026-07-29 | Inspected |
| S8 | SAGE-Nav Review - DEP-E | Related DEP | Markdown | DEP-E-20260723-SAGE-Nav Review | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav%20Review/sage_nav_manuscript.md | Processed Black Lake artifact. | 2026-07-29 | Inspected |
| S9 | CrossMaps Rover Mapping - DEP-A | Related DEP | Markdown | DEP-A-20260722-CrossMaps Rover Mapping | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260722-CrossMaps%20Rover%20Mapping/2606.16935-whitepaper-review.md | Processed Black Lake artifact. | 2026-07-29 | Inspected |

### Primary work identity

- `Paper title`: Group-Control Motion Planning Framework for Microrobot Swarms in a Global Field
- `Authors`: Siyu Li; Afagh Mehri Shervedani; Miloš Žefran; Igor Paprotny
- `Platform and subject`: arXiv, Robotics (`cs.RO`)
- `Version history`: v1 submitted 2024-06-19; v2 revised 2024-12-10
- `Proceedings context`: Sixteenth Workshop on the Algorithmic Foundations of Robotics, WAFR 2024; later Springer chapter in *Algorithmic Foundations of Robotics XVI, Volume 1*, pages 269-288
- `Local source files`: Withheld. The complete PDF, official full-paper HTML, metadata HTML, source archive, extracted text, page renders, attribution, machine summary, and verification report remain private.
- `Official code`: Not available from inspected author-linked sources. A bounded public search found only bibliographic mirrors and did not establish an official implementation repository.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, dates, version, subject, abstract, and arXiv DOI. | Source identity and stated contribution. | High | Abstract alone cannot validate proofs or results. |
| E2 | S2, pages 1-4 | Primary paper | MicroStressBot dimensions and actuation, PFSM motivation, group allocation, unique bit patterns, switched-system model, and unilateral control. | Problem, hardware abstraction, and group-control mechanism. | High for source reporting | Physical behavior and fabrication assumptions were not tested. |
| E3 | S2, pages 5-9; S3 | Primary paper and TeX | Embedded bilateral vector fields, orientation control, independent translation construction, and position-level STLC claim. | Formal mechanism and controllability claim. | Medium-high for faithful reconstruction | Proof was not independently checked; instantaneous-rotation and small-neighborhood idealizations are material. |
| E4 | S2, pages 9-12; S3 | Primary paper and TeX | Primitive order, subgroup planning abstraction, and RRT complexity proposition. | Control/planning/execution tradeoff. | Medium | Complexity constants and sample scaling are asserted under simplified assumptions; no asymptotic experiment validates them. |
| E5 | S2, pages 12-16; S3 | Primary paper, figures, and tables | Six-robot/four-group numerical optimization and RRT simulations; 20-instance and 10-instance averages. | Empirical feasibility and tradeoff comparisons. | Medium | Simulation-only, small scale, missing variance, seeds, timeouts, code, and independent reproduction. |
| E6 | S2, pages 14-16; S3 | Primary paper and TeX | Table 4 values, sequential narrative, and RRT failure footnote. | Internal consistency review. | High | The source is internally ambiguous, so the correct intended labels cannot be established. |
| E7 | Private integrity record | Local verification evidence | PDF/HTML structural gates, source-archive listing, extracted text, and visual render of every PDF page. | Complete-paper source gate. | High | Private files are intentionally absent from the public DEP. |
| E8 | S4-S5 | Publisher and venue records | WAFR and Springer chapter identity. | Publication context. | High | Does not add independent experimental validation. |
| E9 | S7-S9 | Related DEP evidence | Constrained sampling, fast/slow navigation planning, and persistent semantic state. | Cross-DEP synthesis. | Medium-high | Related works do not validate group-control claims. |

## Executive Summary

*Group-Control Motion Planning Framework for Microrobot Swarms in a Global Field* studies a hard coordination setting: many untethered microrobots share one global electrostatic input, cannot carry conventional controllers, and are therefore massively underactuated. The authors use onboard physical finite-state machines to assign each robot a unique subset of activation groups. A temporal group-selection sequence then makes different robots respond differently to the same global field.

The central theoretical claim is that the resulting switched system is small-time locally controllable in robot positions when group membership is allocated appropriately. The paper states a minimum group count of \(\log_2(n+2)+1\) for \(n\) robots and constructs compound motions that turn unilateral forward/counter-clockwise actuation into bilateral translation and rotation fields. This claim is meaningful but bounded: it concerns positions, relies on idealized same-turning-rate dynamics, approximates some rotations as instantaneous for position control, and was not independently proved in this review.

The paper's most reusable insight is a planning tradeoff. Higher-order Lie-bracket-inspired primitives isolate smaller subgroups and reduce planner dimensionality, but their nested back-and-forth motions lengthen execution. Larger coupled groups can move more robots in parallel and improve path efficiency, but make global planning harder. Six-robot simulations illustrate a middle ground: subgroup-sequential planning is much faster to compute than subgroup-parallel or full coupled RRT planning while avoiding the longest execution path of pure one-robot-at-a-time control.

Confidence is high in the source identity and reported table values, medium in the formal and simulator-level conclusions, and low in physical-deployment readiness. No author-linked code was established, no experiment was reproduced, and no hardware evaluation demonstrates manufacturing tolerance, sensing error, collision margins, dynamic obstacles, or medical/industrial safety.

## Detailed Summary

### Problem and background

The MicroStressBot is described as a 120 micrometer by 60 micrometer by 10 micrometer electrostatic MEMS robot with a forward-motion actuator and a steering arm. Lowering or raising the arm changes whether the robot translates or rotates. Because the entire substrate receives one global voltage signal, individual control must come from differences in how robots interpret a temporal sequence, not from separate command channels.

Earlier selective-response approaches rely on distinct physical parameters such as pull-down voltage or turning rate. The paper argues that such fabrication differentiation scales poorly. Physical finite-state machines instead recognize voltage-level sequences. Group-control combines PFSM modules so each robot belongs to several groups, allowing a compact combinatorial address.

### Group allocation

With \(m-1\) selectable groups, each robot receives a unique nonempty bit pattern that is not the all-ones pattern; a final all-rotate group contains no translating robots. For the six-robot example, three selectable groups plus the all-rotate group provide unique allocations. The source writes \(m=\log_2(n+2)+1\). For arbitrary robot counts, an implementation needs an explicit integer-rounding rule; the paper does not state the ceiling operation even though group count is discrete.

At each step, exactly one group is active. Members translate while nonmembers rotate. This defines an \(m\)-state switched system with a continuous scalar control input. Each robot state is \([x_i,y_i,\theta_i]\) in \(SE(2)\), and the full swarm has \(3n\) state variables.

### From unilateral inputs to position controllability

MicroStressBots cannot directly move backward or rotate clockwise. The paper builds compound sequences using group translations and the all-rotate mode. These sequences synthesize bilateral orientation fields and bilateral group-translation fields. The construction can keep incidental translation inside a small neighborhood by repeating smaller motions, while rotations are treated as instantaneous for the position-control analysis.

The orientation analysis shows that three selected robot orientations can be set exactly under the group-allocation matrix, while nonselected orientations can remain unspecified. The position-level STLC construction then repeatedly pairs unwanted group members, rotates them to cancel their translations, and leaves one target robot translating. Repeating this elimination yields independent translation of any robot in an arbitrary direction.

This is not full pose controllability for every robot and does not establish collision-free implementation of every nested motion. It is a position-level reachability result under the paper's embedded-system assumptions.

### Motion-planning abstraction

The paper defines logical subgroups and associates each with a motion primitive realized by a Lie bracket or nested control sequence. Primitive order counts the control-vector-field generators in the bracket. Higher-order primitives tend to affect fewer robots, reducing coupling in the planner, but are harder and longer to execute.

The motion-planning problem \(M(n,k)\) seeks a collision-free trajectory for \(n\) robots using primitives up to order \(k\). The source proposes an RRT complexity of \(O(nc^n)\) at the fully actuated primitive order and \(O(nc^nL^{k_{\max}-k})\) below it, where \(c\) depends on environment scale/resolution and \(L\) represents first-order bracket complexity. The proposition captures the intended monotone tradeoff, but its constants, sampling assumptions, and practical scaling are not empirically established.

### Primitive construction

Two construction strategies are compared. Numerical optimization randomly chooses a sequence of active groups and optimizes activation durations to minimize path length. Hand-designed primitives recursively remove unwanted robot motion using the STLC proof structure. In the six-robot \(M(6,2)\) illustration, a 35-step numerical sequence is optimized for a small displacement and repeated five times; the hand-designed primitive produces a simpler visible path but embodies a structured back-and-forth maneuver.

### Simulation evidence

The main comparisons use six robots and four groups.

Table 3 reports averages over 20 instances without obstacles:

| Method | Planning runtime | RRT nodes | Path length | Execution time | Reported caveat |
|---|---:|---:|---:|---:|---|
| Numerical optimization | 0.80 s | Not applicable | 181.04 | 76.33 s | Exact target but no collision handling |
| RRT with rotation | 8.88 s | 147.20 | 323.57 | 172.36 s | Stops within a radius-2 neighborhood |
| Original RRT | 393.53 s | 7,736.80 | 332.10 | 110.70 s | No solution in 15 of 20 cases within allotted time |

Table 4 reports averages over 10 obstacle instances:

| Method | Planning runtime | RRT nodes | Path length | Execution time |
|---|---:|---:|---:|---:|
| RRT with rotation | 1,141.38 s | 8,242.75 | 384.62 | 200.57 s |
| Subgroup parallel | 216.15 s | 2,218.01 | 868.66 | 886.04 s |
| Subgroup sequential | 15.38 s | 102.10 | 529.47 | 577.41 s |
| Pure control | 19.44 s | 175.50 | 871.82 | 1,042.47 s |

The reported obstacle results support the claim that subgroup-sequential planning can occupy a useful middle point. They also expose reporting ambiguity. The paragraph assigns 19.44 s to sequential planning even though the table assigns that value to pure control, and the failure footnote names “Original RRT” despite appearing on the “RRT with rotation” row. No raw trials, variance, time limit, seed list, solver version, or code is available to resolve the discrepancy.

### Conclusion and transfer boundary

The paper concludes that group-control makes position controllability possible with logarithmically many physical groups and that logical subgroups can simplify high-dimensional planning. The source suggests microassembly and drug-delivery relevance. This review treats those as long-term application motivations, not deployment evidence: no biological environment, physical swarm, manufacturing yield, sensing pipeline, or safety case was tested.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Unique subset-based group allocation differentiates robots under a single global signal. | Author method claim | E2 | Directly supported as a combinatorial and switched-system construction. | High |
| C2 | Position-level STLC is achievable with the stated group-control allocation. | Author formal claim | E3 | Source supplies a constructive argument; independent proof review and physical validation are absent. | Medium-high |
| C3 | The minimum number of groups is \(\log_2(n+2)+1\). | Author formal/design claim | E2-E3 | Supported for the paper's capacity construction, but integer rounding and arbitrary-\(n\) wording need clarification. | Medium |
| C4 | Higher-order, smaller-subgroup primitives simplify planning while increasing execution effort. | Author theoretical and empirical claim | E4-E5 | Qualitatively supported by the abstraction and six-robot simulations. | Medium |
| C5 | Subgroup-sequential planning provides an effective planning/execution compromise. | Author empirical claim | E5-E6 | Supported within Table 4, but internal runtime wording, missing variance, and small scale limit strength. | Medium |
| C6 | The framework is applicable to larger swarms. | Author implication | E4-E5 | Not established empirically beyond six robots; the complexity argument alone is insufficient. | Low-medium |
| C7 | A deployable stack should connect confidence-bounded state, high-level goals, constrained plans, primitive compilation, and monitored execution. | Reviewer synthesis | E9 | Strong conceptual bridge across the four records, not a demonstrated combined system. | Medium |

## Methodology

- `Research objective`: Randomly select one eligible archived arXiv paper, enforce a complete-source gate, review it source-first, synthesize it with exactly three related DEP entries, and create a public-safe DEP-E research artifact.
- `Sources inspected`: Complete primary PDF; official arXiv full-paper HTML and metadata; TeX source; WAFR public paper; Springer chapter record; live Black Lake and Black-Lake-Data README rules; three related Black Lake entries; and the publication index.
- `Discovery strategy`: Enumerated private archive PDFs with `rg --files -g "*.pdf"`, treated unique parent directories as paper units, resolved IDs from PDF filenames, built a conservative used-ID set from both repositories and automation memory, and selected a uniform eligible index with PowerShell `Get-Random`.
- `Inclusion criteria`: Evidence was included when it established paper identity, model assumptions, proof structure, reported quantitative results, internal inconsistencies, publication context, repository rules, or direct planning/navigation overlap.
- `Exclusion criteria`: Abstract-only summaries, unverified code claims, generic robotics records, and source files lacking public-deposition authorization were excluded. No original source file was redistributed.
- `Analytical approach`: Mixed conceptual, formal-structure, empirical, comparative, implementation, safety/ethics, product, replication, and provenance review.
- `Evidence handling`: Major claims map to evidence IDs. Author claims, table values, reviewer interpretation, and cross-DEP proposals are labeled separately.
- `Uncertainty handling`: Missing proof reproduction, code, raw trials, seeds, variance, hardware evidence, and inconsistent table prose remain visible as limitations.
- `Extraction process`: The local gate validated PDF bytes and trailer, parsed all 18 pages, stripped scripts/styles from official HTML, inspected TeX tables/formulas, listed the source archive, produced local text caches, and rendered every PDF page for visual review.
- `Version control`: The paper is pinned to arXiv v2; the public artifact uses stable arXiv and chapter DOIs. Private checksums remain in the local verification record.
- `Cross-checking`: Abstract claims were checked against model, propositions, tables, figures, and conclusion. Table values were checked against both rendered PDF pages and TeX source.
- `Random selection`: 75,781 PDFs; 75,778 parent units; 1,547 observed used base IDs; 425 used-ID exclusions; 185 identifier-incomplete exclusions; 75,168 eligible units; accepted zero-based eligible index 72,419.
- `Discarded attempt`: One earlier in-memory enumeration returned no retrievable selection record and was discarded before target acceptance. It did not produce a review target.
- `Deduplication`: Searched Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and Black-Lake-Data `origin/main` equivalents. Exact ID, DOI, canonical/normalized title, and slug checks found no prior same-paper deposit. The 24-hour cutoff was 2026-07-28.
- `Reviewer stance`: Skeptical source review, DEP-ready preservation, bounded implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2406.13829v2, its WAFR/Springer identity, and exactly three related DEP entries concerning motion safety, planning/control decomposition, and navigation state.
- `Temporal boundary`: Primary paper pinned to v2 revised 2024-12-10; public records inspected on the date-only review marker.
- `Evidence limits`: No official code, raw trial data, environment bundle, seed list, timeout specification, hardware experiment, fabrication study, or independent reproduction was established.
- `Assumptions`: The published PDF/HTML/TeX describe the intended method; page/table values are the source of record; simulator units and execution-time calculations follow the source's unstated implementation.
- `Constraints`: Source files remain local; public output contains no local paths or machine identifiers; code mock-ups are synthetic and non-actuating; no medical or industrial safety claim is made.
- `Out of scope`: Proving STLC independently, reproducing RRT or optimization results, fabricating PFSM robots, operating a physical swarm, or certifying collision safety.
- `Intended use`: Research review, DEP deposition, simulator planning, replication design, and architecture discussion.
- `Audience`: Robotics and control researchers, motion-planning engineers, microrobotics teams, simulator developers, and evidence reviewers.
- `Depth target`: Schema-complete manuscript report with empirical and implementation translation.
- `Reproducibility boundary`: The source supports conceptual reconstruction but not exact numerical reproduction without code, configs, trials, seeds, solver versions, and timeouts.
- `Operational boundary`: Any physical actuation requires a separate safety case, validated hardware, independent emergency stop, controlled environment, and human authorization.
- `Data sensitivity`: Public scholarly sources only; no personal or restricted dataset is involved.

## Observations

- `Observed pattern`: Group membership acts like a hardware-level code, while subgroup primitives act like a planning-level instruction set. Their design cannot be optimized independently.
- `Technical implication`: Planner metrics should include primitive compilation cost and realized execution, not just tree-search time or geometric path length.
- `Observed pattern`: The STLC proof moves complexity into nested cancellation motions. Formal reachability can therefore coexist with poor execution efficiency or collision exposure.
- `Contradiction or tension`: The paper argues for larger-swarm applicability but evaluates only six robots and does not report an empirical scaling curve.
- `Contradiction or tension`: The sequential-runtime prose and the Table 4 failure footnote do not align with their marked table cells.
- `Open question`: How do manufacturing variation, sensing noise, stale state, finite rotation time, substrate nonuniformity, and actuator failure change the controllability construction?
- `Reviewer hypothesis`: A constraint-aware planner that selects among preverified primitive bundles could retain group-control's compact addressing while rejecting high-risk cancellation motions.

## Considerations

**Physical realism:** The bilateral vector fields are synthesized from unilateral motions, and rotations are treated as instantaneous for position control. A physical controller must account for time, swept volume, drift, transient coupling, and collisions during the synthesis path.

**State estimation:** The formal model assumes robot pose and obstacle state are available. A real system needs uncertainty-bounded sensing, identity tracking, clock synchronization, stale-state rejection, and conservative obstacle inflation.

**Manufacturing and calibration:** PFSM group membership, voltage thresholds, turning radii, and actuator behavior must survive fabrication variation and aging. The paper deliberately avoids unique turning-rate fabrication, but group-control still needs reliable group recognition and repeatable motion.

**Planner accounting:** Planning runtime, path length, and execution time are different objectives. Failed trials and timeouts must remain in the denominator; otherwise a method that solves only easy instances can look artificially efficient.

**Safety and application claims:** Microassembly and drug delivery are motivations, not evaluated use cases. Medical deployment would require biocompatibility, localization, containment, fail-safe retrieval, regulatory evidence, and patient-specific risk analysis beyond this paper.

**Governance:** A primitive library should be versioned with its model assumptions, verified domain, calibration state, known failure cases, and revocation rule. A planner must not silently reuse a primitive after hardware or environment changes.

## Strengths

- The paper connects a physical addressing mechanism, switched-system control, formal controllability, planning abstraction, and simulation in one coherent framework.
- Unique subset allocation offers a compact conceptual alternative to one unique physical response per robot.
- The constructive STLC argument explains where independent motion comes from instead of treating controllability as a black-box numerical observation.
- The primitive-order abstraction makes the planner/control/execution tradeoff explicit and testable.
- Tables 3 and 4 report planning runtime, tree size, path length, and execution time rather than presenting only one favorable metric.
- The complete public paper and TeX source make formal and numerical claims inspectable even though implementation code is absent.

## Weaknesses

- The group-count formula does not state integer rounding for arbitrary \(n\).
- The proof depends on idealizations including equal turning rates, small-neighborhood cancellation, and effectively instantaneous rotations for position analysis.
- The experiments cover six simulated robots and do not establish the claimed larger-swarm scaling behavior.
- No variance, confidence interval, seed list, trial-level data, solver version, hardware specification, or explicit timeout value accompanies the reported averages.
- Numerical optimization omits collision handling in its strongest result, limiting fairness against obstacle-aware planners.
- The sequential-runtime prose conflicts with Table 4, and the RRT failure footnote appears attached to a differently named row.
- No author-linked public implementation, hardware experiment, or manufacturing-tolerance evaluation was established.
- Position-level STLC does not by itself guarantee full-pose control, collision-free execution, robustness, or deployability.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| State an integer group-count theorem | Formal specification | Group count is discrete but the formula lacks rounding. | Unambiguous capacity and implementation rule. | Minor editorial/proof update. | Enumerate all \(n\) across several group counts and verify allowed codewords. |
| Publish code and trial manifests | Reproducibility | Tables cannot be regenerated from the paper alone. | Auditable results and easier extension. | Maintenance and dependency burden. | One command reproduces every table/figure from pinned seeds and configs. |
| Release trial-level outcomes | Statistics | Means hide failures and dispersion. | Confidence intervals, paired tests, and honest timeout accounting. | Larger artifacts and analysis. | Report success, timeout, runtime, nodes, path, execution, and minimum clearance per trial. |
| Correct Table 4 wording and footnote | Evidence integrity | Current labels are internally inconsistent. | Reliable downstream interpretation. | Low. | Author erratum or revised source with change note. |
| Add scaling sweeps | External validity | Six robots do not establish large-swarm behavior. | Empirical compute/control frontiers. | Growing simulation cost. | Sweep robot count, group count, primitive order, obstacle density, and target coupling. |
| Model non-ideal actuation | Physical realism | Instantaneous and exact motions understate risk. | More credible transfer to hardware. | Calibration and simulation complexity. | Inject delay, noise, turning-radius spread, missed group activation, and drift. |
| Integrate constrained local planning | Safety | Back-and-forth primitives can collide during synthesis. | Explicit swept-volume and clearance control. | Solver latency and conservatism. | Compare RRT, RRT-CBF, and reachability-gated extensions on matched cases. |
| Validate physical prototypes | Deployment boundary | Simulation cannot establish fabrication or sensing reliability. | Evidence for or against practical feasibility. | Hardware cost and safety risk. | Begin with speed-limited bench tests, external tracking, containment, and emergency stop. |

## Potential Implementations

### Group-code and PFSM compiler

- `User`: Microrobotics control and fabrication teams.
- `Goal`: Convert robot count and group constraints into unique allowed membership codes.
- `Core mechanism`: Apply an explicit ceiling to the group-count rule, reserve forbidden patterns, generate PFSM module assignments, and verify code uniqueness.
- `Required inputs`: Robot count, PFSM capacity, forbidden states, voltage-sequence catalog, and fabrication constraints.
- `Outputs`: Group matrix, per-robot PFSM assignment, capacity report, and validation cases.
- `Risk controls`: Offline-only; no voltage driver; human review; reject ambiguous or over-capacity allocations.
- `Evaluation`: Exhaustive codeword validation and fault injection for lost or duplicated memberships.

### Primitive verification library

- `User`: Control and simulation engineers.
- `Goal`: Store reusable subgroup motions with explicit validity domains.
- `Core mechanism`: Compile nested control sequences into versioned primitives annotated with affected robots, swept regions, execution time, model assumptions, and calibration bounds.
- `Required inputs`: Switched-system model, group matrix, robot geometry, actuator limits, and obstacle representation.
- `Outputs`: Verified primitive catalog, counterexamples, risk labels, and revocation triggers.
- `Risk controls`: Simulator gate; conservative geometry; fail closed outside the verified domain; no physical export without approval.
- `Evaluation`: Property tests, reachability checks, randomized perturbations, and comparison with direct simulation.

### Multi-objective swarm planner

- `User`: Motion-planning researchers.
- `Goal`: Choose group and subgroup primitives while balancing compute, path length, execution, failure, and clearance.
- `Core mechanism`: Run matched planning trials over primitive-order frontiers and retain Pareto-optimal plans rather than collapsing every objective into one mean.
- `Required inputs`: Pinned scenarios, primitive library, goals, obstacles, timeouts, and objective weights.
- `Outputs`: Plan set, per-trial evidence, Pareto plots, failure ledger, and replay bundle.
- `Risk controls`: Offline simulation; deterministic replay; failures remain in denominators; no physical driver.
- `Evaluation`: Paired seeds across RRT variants, subgroup schedules, and constraint-aware planners.

### State-to-execution safety adapter

- `User`: Robotics systems teams.
- `Goal`: Bind map/pose confidence and high-level goals to a fresh, feasible primitive schedule.
- `Core mechanism`: Version state snapshots, validate waypoint and clearance assumptions, compile a plan, release primitives only while gates remain satisfied, and stop on stale or contradictory evidence.
- `Required inputs`: Pose distributions, obstacle map, waypoint, primitive catalog, model revision, and timing budget.
- `Outputs`: Released/withheld decision, reason code, schedule, expected clearance, and execution receipt.
- `Risk controls`: Conservative uncertainty bounds, state-age limits, independent stop channel, and supervised escalation.
- `Evaluation`: Fault injection for stale maps, pose jumps, missed activations, solver timeout, and model-version mismatch.

## Three Ways to Exercise This Research

1. **Allocation audit:** Objective - verify the combinatorial group-count rule. Inputs - robot counts from 1 to 128 and allowed/forbidden membership patterns. Method - generate codes using an explicit ceiling, check uniqueness and capacity, and compare with the paper's equality cases. Output - allocation matrix and counterexample report. Success criterion - every robot has one unique allowed code and no capacity claim is exceeded. Stop condition - any ambiguity in rounding or reserved patterns. Safety boundary - pure offline enumeration.
2. **Matched six-robot replay:** Objective - reconstruct the reported planner tradeoff. Inputs - one pinned six-robot/four-group simulator, published start/goal states, two obstacle circles, explicit seeds, and timeouts. Method - run numerical optimization, RRT with rotation, original RRT, subgroup parallel, subgroup sequential, and pure control on paired trials. Output - trial-level runtime, success, nodes, path length, execution, clearance, and failure reasons. Success criterion - every published metric is either reproduced within a declared tolerance or explained by a traceable difference. Stop condition - missing scenario or solver detail prevents matched execution. Safety boundary - simulator only.
3. **Non-ideality stress test:** Objective - test whether the controllability construction remains useful under physical uncertainty. Inputs - synthetic turning-radius spread, missed group activations, finite rotation duration, pose noise, and obstacle inflation. Method - perturb one factor at a time and jointly, replay verified primitives, and record failure/clearance distributions. Output - robustness envelope and primitive revocation rules. Success criterion - the safe operating region is explicit and independently replayable. Stop condition - any primitive exits containment or violates the modeled safety margin. Safety boundary - no physical actuation.

## Example MVP Product

- `Product name`: Group-Control Tradeoff Lab
- `Target user`: Robotics researchers evaluating group-control before hardware work.
- `Problem`: The paper's planner/control/execution tradeoff is difficult to reproduce and easy to misread from averages alone.
- `Core workflow`: Configure robot count and group codes; load a pinned simulator; generate or import primitive bundles; run matched planners on shared seeds; compare success, runtime, tree size, path, execution, clearance, and failure; export an evidence report.
- `Data requirements`: Synthetic robot geometry, group matrices, start/goal states, obstacle maps, primitive definitions, seeds, timeouts, solver versions, and trial outcomes.
- `Architecture`: Local web UI or notebook; deterministic simulator; allocation compiler; primitive verifier; planner adapters; metric recorder; report generator.
- `Success metrics`: Reproducible trials; zero hidden failures; complete timeout accounting; paired comparisons; version-pinned exports; and clear identification of source contradictions.
- `Risk controls`: Offline-only; no robot driver, voltage interface, or medical workflow; synthetic defaults; containment checks; explicit non-certification banner; human approval before any physical integration.
- `Limitations`: Cannot prove the paper's theorem, model real fabrication without calibration data, establish biological safety, or replace hardware testing.
- `MVP boundary`: Six to twelve simulated robots, static circular obstacles, published planner families, and evidence reporting; no online sensing or actuation.
- `Deployment model`: Local notebook or browser application on one workstation.
- `Evaluation plan`: Golden allocation tests, deterministic scenario replays, fault injection, table-reproduction checks, and code review of metric denominators.
- `Failure modes`: Silent exclusion of failed trials, mismatched timeouts, stale primitive assumptions, solver nondeterminism, inconsistent units, and misleading scalar aggregation.
- `Maintenance plan`: Pin dependencies and solver versions; version scenario/primitive schemas; retain negative trials; rerun golden cases on every change.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| RRT-CBF Motion - DEP-E | Related DEP and primary-paper review | Adds barrier-constrained sampled motion, multi-robot avoidance, execution tracking, and a clear simulation-to-safety boundary. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md |
| SAGE-Nav Review - DEP-E | Related DEP and primary-paper review | Provides a fast/slow planner-controller split, cached waypoints, replanning triggers, and simulator-to-physical caveats. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav%20Review/sage_nav_manuscript.md |
| CrossMaps Rover Mapping - DEP-A | Related DEP and primary-paper review | Supplies a confidence-aware persistent mapping layer and emphasizes pose drift, dynamic objects, and untested navigation outcomes. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260722-CrossMaps%20Rover%20Mapping/2606.16935-whitepaper-review.md |
| Algorithmic Foundations of Robotics XVI, Volume 1 | Official proceedings | Places the paper within WAFR 2024 multi-robot and planning research. | https://link.springer.com/book/10.1007/978-3-032-09967-9 |
| Group-Control Motion Planning Framework | Official chapter | Stable publisher identity for the selected work. | https://doi.org/10.1007/978-3-032-09967-9_14 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2406.13829v2 | Title, authors, version history, abstract, category, and arXiv DOI. | 2026-07-29 | Primary metadata. |
| R2 | https://arxiv.org/html/2406.13829v2 | Complete method, proofs, simulations, tables, figures, conclusion, and references. | 2026-07-29 | Official full-paper HTML inspected; local copy withheld. |
| R3 | https://arxiv.org/pdf/2406.13829v2 | Visual source for all 18 pages, equations, figures, and tables. | 2026-07-29 | Local PDF and renders withheld. |
| R4 | https://arxiv.org/e-print/2406.13829v2 | TeX formulas, tables, captions, and source wording. | 2026-07-29 | Local source archive withheld. |
| R5 | https://doi.org/10.48550/arXiv.2406.13829 | Persistent arXiv identifier. | 2026-07-29 | DOI record. |
| R6 | https://doi.org/10.1007/978-3-032-09967-9_14 | Springer chapter identity. | 2026-07-29 | Publisher context. |
| R7 | https://algorithmic-robotics.org/papers/65_Group_Control_Motion_Planni.pdf | WAFR 2024 paper and venue context. | 2026-07-29 | No source file deposited. |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout, DEP content, attribution, source-withholding, and commit rules. | 2026-07-29 | Live repository authority. |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index requirements. | 2026-07-29 | Live repository authority. |
| R10 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository layout and source-deposition authority used before scanning its live dedup surfaces. | 2026-07-29 | Live related-repository authority. |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md | Related constrained-motion evidence. | 2026-07-29 | Related DEP 1 of 3. |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav%20Review/sage_nav_manuscript.md | Related fast/slow navigation-planning evidence. | 2026-07-29 | Related DEP 2 of 3. |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260722-CrossMaps%20Rover%20Mapping/2606.16935-whitepaper-review.md | Related confidence-aware mapping evidence. | 2026-07-29 | Related DEP 3 of 3. |
| R14 | Local complete-paper bundle | PDF/HTML integrity, TeX inspection, extracted text, and page renders. | 2026-07-29 | Withheld locally; no path or file deposited. |

## Appendix

### A. Random selection and deduplication record

| Field | Value |
|---|---|
| Enumeration command | `rg --files -g "*.pdf"` |
| Candidate unit | Unique PDF parent directory |
| PDF count | 75,781 |
| Parent-unit count | 75,778 |
| Used arXiv base IDs observed | 1,547 |
| Units excluded by used ID | 425 |
| Identifier-incomplete units withheld | 185 |
| Eligible units | 75,168 |
| Random generator | PowerShell `Get-Random`, uniform index over the eligible array |
| Accepted zero-based eligible index | 72,419 |
| Accepted paper | arXiv:2406.13829, *Group-Control Motion Planning Framework for Microrobot Swarms in a Global Field* |
| Duplicate rejections after accepted draw | 0 |
| Discarded pre-acceptance attempts | 1 in-memory enumeration with no retrievable selection record |
| 24-hour cutoff date | 2026-07-28 |
| Dedup surfaces | Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`; automation memory; Black-Lake-Data `origin/main` equivalents |

### B. Source-integrity verification

| Artifact | Required gate | Observed result | Status |
|---|---|---|---|
| PDF | At least 10 KB, `%PDF-` header, trailing `%%EOF` | 1,700,463 bytes; valid header/trailer; 18 unencrypted pages | Pass |
| Full-paper HTML | At least 5 KB, at least 2,000 body characters, document marker, at least two headings, at least two structure terms | 861,863 bytes; 90,587 body characters; document marker; 44 headings; five structure terms | Pass |
| Metadata HTML | Metadata only; not counted as paper | 40,273 bytes | Present |
| Source archive | Readable archive when collected | 2,365,568 bytes; 56 entries | Pass |
| Visual review | Render sufficient pages to inspect layout, tables, and figures | All 18 pages rendered; title page and result pages inspected at full resolution | Pass |
| Partials | No unexpected `.part` files | Zero | Pass |

Initial classification was `partial` because full-paper HTML was missing. The valid existing PDF was preserved. One bounded official-arXiv repair collected full-paper HTML, metadata HTML, and the source archive; no fallback was required. The local README, attribution record, machine-readable summary, extracted-text caches, render set, and verification report were updated before review proceeded.

### C. Replication checklist

- [ ] Pin arXiv v2, all public source URLs, code revision if released, solver versions, and operating system.
- [ ] Publish the group matrix, primitive catalog, robot radius/turning parameters, and all scenario assets.
- [ ] State the integer rounding rule for group count and enumerate allowed/forbidden codewords.
- [ ] Record every seed, timeout, success/failure, planning runtime, RRT nodes, path length, execution time, and minimum clearance.
- [ ] Reconcile the 15.38/19.44-second sequential-planning discrepancy and the Table 4 RRT footnote.
- [ ] Reproduce the six-robot tables with paired trials and uncertainty intervals.
- [ ] Sweep robot count, group count, primitive order, obstacle density, and model noise.
- [ ] Include finite rotation time, pose uncertainty, actuation error, missed group activation, and collision checks during cancellation motions.
- [ ] Keep a conservative simulator stop/fallback and never infer physical safety from successful simulation alone.
- [ ] Archive negative trials and publish a machine-readable evidence ledger.
