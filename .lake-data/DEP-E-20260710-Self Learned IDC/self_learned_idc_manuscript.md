---
title: "Self-Learned IDC - DEP-E"
generated_at: "2026-07-10 (date-only public marker; exact local timestamp withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of arXiv:2110.12359 on dynamic permutation state representation for integrated decision and control at mixed-traffic signalized intersections."
source_status: "URLs and cache; no source files deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-10"
temporal_cutoff: "arXiv v2 revised 2021-11-10; public sources inspected on the date-only run marker."
primary_url: "https://arxiv.org/abs/2110.12359"
stable_identifier: "arXiv:2110.12359v2; DOI 10.48550/arXiv.2110.12359"
confidence_summary: "Medium-high for source identity, method, and source-reported simulation metrics; lower for reproducibility because code and experiments were not reproduced."
safety_scope: "research review, autonomous-driving safety analysis, synthetic/toy implementation planning only"
distribution_notes: "Repository-relative paths and public URLs only; local execution context withheld."
---

# Self-Learned IDC - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract page | Primary metadata | HTML | arXiv:2110.12359v2 | https://arxiv.org/abs/2110.12359 | Public arXiv page; source files not redistributed. | 2026-07-10 | Inspected |
| S2 | arXiv source package | Primary paper source | TeX source | arXiv:2110.12359v2 | https://arxiv.org/e-print/2110.12359 | Public source package used for cache-backed review; not copied into DEP. | 2026-07-10 | Inspected through cache |
| S3 | arXiv HTML | Primary paper/metadata text | HTML | arXiv:2110.12359v2 | https://arxiv.org/html/2110.12359 | Public arXiv HTML cached for review; no local path published. | 2026-07-10 | Inspected through cache |
| S4 | arXiv PDF | Primary paper reference | PDF | arXiv:2110.12359v2 | https://arxiv.org/pdf/2110.12359 | Public PDF reference; PDF text extraction unavailable locally; PDF not deposited. | 2026-07-10 | Referenced |
| S5 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2110.12359 | https://doi.org/10.48550/arXiv.2110.12359 | Public DOI reference. | 2026-07-10 | Recorded |
| S6 | Local arXiv archive metadata | Selection provenance | README/PDF presence | arXiv:2110.12359 | Local path withheld | Confirmed local paper unit identity; no source file redistributed. | 2026-07-10 | Observed |
| S7 | Black-Lake README | Repository authority | Markdown | origin/main | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public repository standard. | 2026-07-10 | Fetched/read |
| S8 | Black-Lake-Data README | Related repository authority | Markdown | origin/main | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Repository standard read through authenticated access. | 2026-07-10 | Fetched/read |
| S9 | Agent State Review DEP-E | Related DEP | Markdown | DEP-E-20260708-Agent State Review | `.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md` | Repository-relative processed artifact. | 2026-07-10 | Inspected |
| S10 | VideoWeave Geometry DEP-E | Related DEP | Markdown | DEP-E-20260709-VideoWeave Geometry | `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Repository-relative processed artifact. | 2026-07-10 | Inspected |
| S11 | Physical Data AI DEP-E | Related DEP | Markdown | DEP-E-20260710-Physical Data AI | `.lake-data/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` | Repository-relative processed artifact. | 2026-07-10 | Inspected |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | arXiv metadata | Title, authors, arXiv ID/version, DOI, category, abstract, submission/revision dates, PDF/source links. | Source identity and high-level contribution. | High | Abstract cannot validate detailed empirical claims. |
| E2 | S2 | Primary TeX source | Method sections describing dynamic permutation state representation, encoding network, summation, injectivity condition, and IDC formulation. | Core method and state representation claims. | High | Source text was inspected through extraction cache; equations were not independently rederived. |
| E3 | S2 | Primary TeX source | Implementation section describing SUMO intersection, traffic participants, traffic lights, sensors, observations, action design, utility, and constraints. | Evaluation scenario and control constraints. | High | Scenario was not reproduced. |
| E4 | S2 | Primary TeX source | Simulation section and comparison table reporting computation time, comfort, pass time, collisions, and decision compliance. | Reported empirical results. | Medium-high | Metrics are source-reported; no independent simulation or statistical audit was performed. |
| E5 | S3 | arXiv HTML/cache | Abstract, title, authors, DOI, version metadata, source counts, and HTML text presence. | Metadata and cache-backed review support. | High | HTML rendering may omit figure nuance. |
| E6 | S6 | Local archive metadata | Randomly selected archive unit had a readme and PDF for arXiv:2110.12359. | Selection provenance. | Medium | Local path withheld; PDF text not extracted. |
| E7 | S7, S8 | Repository standards | DEP class, README, attribution block, source handling, and raw-data companion repository rules. | Output structure and process compliance. | High | Process evidence only. |
| E8 | S9-S11 | Related DEP manuscripts | State review, spatial/world-model consistency, and physical-system representation discussions. | Related-entry synthesis. | Medium | Related artifacts are not validation evidence for this paper. |
| E9 | Web and GitHub searches | Discovery checks | Title, arXiv ID, and code-search attempts found no official implementation repository. | Code availability assessment. | Medium | Search cannot prove nonexistence. |

## Executive Summary

"Self-learned Intelligence for Integrated Decision and Control of Automated Vehicles at Signalized Intersections" proposes a dynamic permutation state representation for autonomous driving in dense mixed traffic. The paper's central problem is that fixed-dimensional neural policies struggle when the number and ordering of surrounding vehicles, bicycles, and pedestrians changes from moment to moment. Sorting a fixed number of nearby actors can create discontinuous states and can ignore relevant vulnerable road users.

The proposed representation encodes each traffic participant with a neural feature function, sums the encoded features across participant sets, and concatenates the pooled surrounding-state vector with ego, road, traffic-light, and reference-path features. This fixed-dimensional state feeds value and policy networks inside integrated decision and control. The control problem optimizes finite-horizon tracking performance while penalizing safety-constraint violations for participants, road boundaries, and signal lights.

The strongest inspected result is the paper's 100-simulation comparison table. Dynamic permutation IDC reports slightly higher mean control-computation time than fixed permutation IDC, but lower comfort index, similar pass time, fewer collisions, and zero decision-compliance breaks. These metrics are promising but remain source-reported: this run did not reproduce SUMO scenarios, train the networks, execute MPC comparisons, or inspect official code.

## Detailed Summary

### Problem

Urban signalized intersections are difficult for autonomous driving because the ego vehicle must react to mixed traffic, vulnerable road users, signal phases, occlusion, and conflicting paths. The authors argue that existing reinforcement-learning driving systems often simplify the scenario or impose fixed actor counts and sorting rules. In mixed traffic, the number of observed actors changes, and pedestrian/bicycle order can shift rapidly, making fixed permutation state representations brittle.

### Method

The dynamic permutation state representation introduces an encoding network `h(x, phi)` for each observed actor. Vehicle, bicycle, and pedestrian feature vectors are projected into a shared representation and summed. The pooled surrounding-state vector is concatenated with `x_else`, which includes ego-state, traffic-light, tracking-error, and reference-path features. The paper states that this design handles variable actor counts while remaining permutation invariant to actor order.

The representation is incorporated into IDC. For each candidate path, the controller minimizes a finite-horizon tracking objective and uses constraints for safety. A penalty form combines tracking cost and safety cost. The policy, value, and encoding networks are trained offline, and the trained networks are used online to select paths and output steering/acceleration commands.

### Simulation Setup

The implementation builds a SUMO signalized four-way intersection with motor-vehicle lanes, bicycle lanes, sidewalks, and crosswalks. The source reports 400 vehicles, 100 bicycles, and 400 pedestrians per hour on each lane, a six-phase traffic-light system with 120-second cycle time, and random initialization of surrounding participants. The ego vehicle must complete left-turn, straight, and right-turn tasks.

The observation model includes virtual camera, radar, and lidar sensors with stated effective ranges and fields of view. Observed participant features include relative position, speed, heading, length, width, and type. Ego and path features include ego pose/speed/yaw, traffic-light phase, tracking errors, and reference-path points. Actions are front-wheel angle and expected acceleration, bounded by actuator limits.

### Results

The training comparison reports lower policy, tracking, and safety cost for dynamic representation than fixed representation, while value-cost learning is similar. The authors interpret this as evidence that the encoding network improves policy learning because policy learning depends on interaction with the driving environment.

For driving performance, the paper compares dynamic permutation IDC, fixed permutation IDC, and a rule-based SUMO baseline over 100 simulations with random initial ego velocity and maximum episode length of 180 seconds. The reported table is:

| Metric | Dynamic permutation IDC | Fixed permutation IDC | Rule-based |
|---|---:|---:|---:|
| Computing time [ms] | 7.24 (+/- 1.36) | 5.96 (+/- 0.60) | Not reported |
| Comfort index | 2.63 | 3.96 | 4.34 |
| Time to pass [s] | 24.46 (+/- 4.52) | 25.73 (+/- 6.60) | 66.18 (+/- 15.74) |
| Collisions | 1 | 8 | 2 |
| Decision compliance breaks | 0 | 3 | 0 |

The paper also compares the trained IDC policy with MPC on one left-turn episode and states that IDC outputs actions within 10 ms while MPC averages about 1000 ms for that task. This supports the paper's claim that offline-trained IDC can approximate expensive online constrained optimization, but the claim still needs independent reproduction.

### Limitations

The paper source does not provide a code repository in inspected locations. The reported results depend on a custom SUMO scenario, stochastic traffic, sensor assumptions, network architecture, penalty settings, and training schedule. The evaluation is simulated and does not establish real-world safety. The representation's summation mechanism may lose actor-level detail unless paired with diagnostics or attention-like alternatives.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Dynamic permutation state representation can handle variable numbers of observed vehicles, bikes, and pedestrians while preserving a fixed input size. | Author method claim | E2 | Supported by the encoding-plus-summation design in the source text. | High |
| C2 | The representation is permutation invariant to ordering of observed actors. | Author method claim | E2 | Supported for the summation operation; practical quality depends on the learned encoder preserving necessary distinctions. | High for formulation; medium for adequacy |
| C3 | IDC with dynamic permutation representation improves comfort, safety, and compliance compared with fixed permutation IDC in the reported simulation. | Author empirical claim | E4 | Supported by the source table, but not reproduced. | Medium-high for reporting; low for external validity |
| C4 | The approach can output online control commands within a real-time-relevant latency range in the reported setup. | Author empirical/implementation claim | E4 | Source reports 7.24 ms mean computation and under 10 ms control output; hardware and worst-case latency are not fully audited. | Medium |
| C5 | The work is most useful as a state-interface pattern for safety-constrained embodied systems. | Reviewer interpretation | E2, E3, E8 | Reasonable synthesis across method, simulation, and related DEP entries. | Medium |

## Methodology

- `Research objective`: Randomly select one eligible local arXiv paper, review it source-first, and deposit public-safe Black-Lake logs, Report-Mark, DEP-E README, schema-complete manuscript, and dedup pointer.
- `Sources inspected`: Local archive metadata, arXiv abstract page, arXiv HTML, arXiv source package through extraction cache, arXiv DOI, live Black-Lake README, live Black-Lake-Data README, web/GitHub code searches, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated local archive PDFs with `rg --files -g "*.pdf"`, grouped candidates by PDF parent directory, selected a uniform random index with PowerShell `Get-Random`, derived arXiv ID/title from filename and nearby metadata, and searched Black-Lake artifacts, automation memory, and Black-Lake-Data for duplicate markers before acceptance.
- `Inclusion criteria`: Included sources that identify the selected paper, support method/result/limitation claims, define repository deposition rules, or provide concrete conceptual overlap around state, spatial consistency, physical systems, or safety-constrained control.
- `Exclusion criteria`: Did not redistribute source files, run SUMO, train networks, execute code, reproduce metrics, or treat arXiv recommendation widgets as evidence.
- `Analytical approach`: Mixed empirical, conceptual, comparative, implementation, safety/ethics, product research, replication, and DEP-ready provenance review.
- `Evidence handling`: Author claims are tied to evidence IDs. Reviewer interpretations and related-entry synthesis are labeled separately. Quantitative values are preserved as source-reported.
- `Uncertainty handling`: Missing code, failed local PDF extraction, unavailable reproduction, and simulation-only evidence are recorded as limitations.
- `Extraction process`: Ran source-processing preflight; performed local-first `missing-only` extraction; because local extraction produced metadata-only, ran approved public arXiv backfill. Final cache contained HTML and source text, while PDF text remained unavailable.
- `Random selection`: Candidate PDF count and paper-unit count were both 75,438. Selected zero-based index was 22,294. Duplicate reselections were 0.
- `Deduplication and reselection validation`: Scanned Black-Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; checked absent automation memory; searched Black-Lake-Data for arXiv ID and exact title. No prior marker was found for arXiv:2110.12359, DOI, normalized title, or slug.
- `Reviewer stance`: DEP-ready preservation, source-grounded paper report, implementation brief, safety review, and follow-on reproducibility planning.

## Scope, Constraints, and Assumptions

- `Scope`: This artifact reviews arXiv:2110.12359 and connects it to three related DEP entries about state review, spatial/world-model consistency, and physical-system representation.
- `Temporal boundary`: Sources were accessed on the date-only public run marker; the selected paper version is arXiv v2 revised 2021-11-10.
- `Evidence limits`: No experiments were reproduced; no official code repository was found; local PDF text extraction failed; source review relied on arXiv HTML and fetched TeX source.
- `Assumptions`: The arXiv source package corresponds to the selected local archive unit and the local metadata correctly identifies the selected paper.
- `Constraints`: Public output must avoid local absolute paths, usernames, machine identifiers, local timezone labels, and exact local execution timestamps.
- `Out of scope`: Real vehicle deployment claims, SUMO reproduction, controller training, MPC execution, hardware benchmarking, or safety certification.
- `Intended use`: DEP deposition, research triage, implementation planning, and future reproducibility review.
- `Audience`: Black-Lake reviewers, autonomous-driving researchers, ML systems engineers, and safety reviewers.
- `Reproducibility boundary`: A reviewer can follow the public arXiv sources and repository-relative related paths, but cannot reproduce reported results from this artifact alone.
- `Data sensitivity`: Public research sources and repository artifacts only.

## Observations

- `Observed pattern`: The paper reframes mixed-traffic control as a state-representation problem before it becomes a policy-learning problem.
- `Technical implication`: Fixed actor ordering is a fragile interface for dynamic, mixed-agent environments; set-based encodings are a plausible alternative when paired with safety diagnostics.
- `Evidence-quality implication`: The paper reports useful aggregate outcomes, but reproducibility requires code, SUMO network files, random seeds, trained weights, and scenario manifests.
- `Safety implication`: Simulation collisions and compliance counts are necessary but insufficient for real-world safety; near misses, occlusion failures, and vulnerable-road-user stress cases matter.
- `Reviewer hypothesis`: A reusable Black-Lake embodied-agent review template should ask how raw actor observations become state, how safety constraints are represented, and how failures are recorded.

## Considerations

Dynamic permutation state representation is attractive because it matches the variable-cardinality nature of traffic scenes. However, summing learned actor features can make it harder to inspect which actor drove a decision unless the implementation also logs actor-level features, nearest vulnerable road users, minimum margins, and constraint activations. For safety-critical settings, the state representation should be auditable, not merely performant.

The reported real-time computation numbers are promising but incomplete. Production control needs worst-case latency, scheduling jitter, hardware details, fail-safe behavior, and validation under sensor dropouts. The paper's simulation setting is valuable for research, but deployment would require a separate safety case, data governance, scenario coverage, and independent verification.

## Strengths

- The paper addresses a concrete representation failure mode in mixed traffic: variable actor counts and unstable ordering.
- The method has a clear mechanism that can be translated into toy set-encoder and review-card implementations.
- The simulation includes vehicles, bicycles, pedestrians, traffic lights, reference paths, sensor ranges, observation noise, and action limits.
- The reported metrics cover comfort, pass time, collisions, compliance, and computation time, not only reward curves.
- The connection to IDC gives the learned policy a safety-constrained optimization framing rather than an unconstrained black-box action policy.

## Weaknesses

- No official implementation repository was found in inspected sources.
- The paper's results were not reproduced; all metrics remain source-reported.
- The evaluation is simulation-only and depends on scenario design, traffic randomization, and sensor assumptions.
- The summation representation may lose individual actor salience without explicit diagnostics.
- The source does not fully establish robustness across broader intersections, unusual road users, weather, perception errors, or real hardware.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code and SUMO scenario assets | Reproducibility | Reported results depend on training and scenario details. | Enables independent validation. | Cleanup, documentation, and dependency burden. | Reproduce the 100-simulation comparison table. |
| Add actor-level diagnostics | Interpretability | Summed features can hide which actor caused a control choice. | Better safety review and debugging. | More telemetry and privacy review. | Log minimum margins, actor types, and constraint activations per step. |
| Stress-test vulnerable road users | Safety evaluation | Pedestrians and cyclists are central to the method's motivation. | Clearer boundary conditions. | More scenario design effort. | Vary density, occlusion, speed, right-of-way, and signal timing. |
| Report worst-case latency | Real-time control | Mean computation time does not prove control-loop safety. | Stronger deployment evidence. | Requires hardware and profiling protocol. | Measure p95/p99 latency and jitter under maximum actor counts. |
| Compare alternative set encoders | Representation design | Summation is simple but may not be best for actor salience. | Better performance/interpretability tradeoff. | More model variants and ablations. | Compare DeepSets, attention pooling, graph neural networks, and hybrid constraints. |

## Potential Implementations

1. `Mixed-Traffic State Card`
   - `User`: Autonomous-driving reviewer or simulation engineer.
   - `Goal`: Preserve how a controller transforms variable actor observations into a decision state.
   - `Core mechanism`: Record actor counts, state encoder type, pooling function, constraints, metrics, and failure cases in a structured artifact.
   - `Required inputs`: Scenario manifest, actor observations, encoder summary, constraint logs, and metric table.
   - `Outputs`: Markdown/JSON review card and follow-up questions.
   - `Risk controls`: Synthetic/simulated data only; no real pedestrian identity data; no deployment claims.
   - `Evaluation`: Reviewer can trace each aggregate metric to scenario and state-interface assumptions.

2. `Set Encoder Regression Harness`
   - `User`: ML systems engineer.
   - `Goal`: Test whether a set-based state encoder remains stable when actor order changes.
   - `Core mechanism`: Generate synthetic actor lists, permute ordering, compare encoded states and policy decisions, and flag order-sensitive behavior.
   - `Required inputs`: Toy actor records, encoder implementation, optional policy stub.
   - `Outputs`: Permutation-invariance report and failing cases.
   - `Risk controls`: Toy data only; no vehicle-control deployment.
   - `Evaluation`: Encodings remain invariant under actor permutation and change only under meaningful actor changes.

3. `Constraint Margin Ledger`
   - `User`: Safety reviewer.
   - `Goal`: Make safety outcomes inspectable beyond collision counts.
   - `Core mechanism`: Log minimum distance margins by actor type, traffic-light stop-line margins, and action bounds per simulated rollout.
   - `Required inputs`: Simulation traces, participant geometry, signal phase, and controller outputs.
   - `Outputs`: Margin table, near-miss list, and scenario-level summary.
   - `Risk controls`: Repository-relative metadata only; no real-world telemetry.
   - `Evaluation`: Near misses are visible even when aggregate collisions are zero.

## Three Ways to Exercise This Research

1. `Permutation smoke test`: Objective: verify that a toy set encoder produces identical pooled states for permuted actor lists. Inputs: synthetic actors with type, position, speed, and ego features. Method: shuffle actors, encode, compare vectors. Output: pass/fail report. Success criterion: pooled state is invariant to ordering. Safety boundary: toy synthetic data only.
2. `Synthetic intersection card`: Objective: practice reviewing a controller without reproducing the full paper. Inputs: hand-authored scenario manifest, actor counts, fake metric table, and known limitations. Method: fill a Mixed-Traffic State Card and check all source/evidence fields. Output: Markdown card. Success criterion: every claim maps to evidence or a limitation. Safety boundary: no real traffic telemetry.
3. `Margin-ledger prototype`: Objective: move beyond collision counts. Inputs: synthetic rollout with actor distances and traffic-light states. Method: compute minimum margins and flag near misses. Output: CSV/JSON ledger and summary. Success criterion: near-miss cases are visible even without collisions. Safety boundary: not a vehicle controller.

## Example MVP Product

- `Product name`: Intersection State Auditor.
- `Target user`: Simulation engineers and safety reviewers evaluating autonomous-driving research artifacts.
- `Problem`: Paper-level metrics often hide how mixed-traffic observations become controller state and why failures occur.
- `Core workflow`: Import a scenario manifest, actor-observation schema, controller state-interface description, and metric table; validate public-safe provenance; generate a state card, permutation test report, and constraint margin ledger.
- `Data requirements`: Synthetic or simulation-only actor observations, traffic-light phase, ego state, controller outputs, and repository-relative source references.
- `Architecture`: Local CLI or notebook that parses JSON scenario traces, runs invariant checks, computes margin summaries, and emits Markdown/JSON review artifacts.
- `Success metrics`: Percentage of claims with evidence IDs, number of permutation failures found, near-miss coverage, public-safe validation pass rate, and reviewer time to identify state-interface assumptions.
- `Risk controls`: No real-world telemetry by default, no deployment recommendation, source sanitization, explicit simulation-only labels, and manual review for safety-sensitive claims.
- `Limitations`: The MVP would not reproduce the paper's IDC training or prove vehicle safety; it would audit representation and evidence quality around simulated controller claims.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Self-learned Intelligence for IDC | Primary selected paper | Dynamic permutation state representation for mixed-traffic IDC. | https://arxiv.org/abs/2110.12359 ; https://doi.org/10.48550/arXiv.2110.12359 |
| Agent State Review - DEP-E | Related Black-Lake DEP | State as an auditable control/review object. | `.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md` |
| VideoWeave - DEP-E | Related Black-Lake DEP | Spatial/world-model consistency for embodied and simulation-adjacent systems. | `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` |
| Physical Data - DEP-E | Related Black-Lake DEP | Compact physical-system representations and domain-fit review. | `.lake-data/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` |
| SUMO | Simulation platform cited by paper | Traffic simulation context for the paper's experiments. | https://www.eclipse.org/sumo/ |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2110.12359 | Metadata, abstract, version, DOI, authors, source links | 2026-07-10 | Primary arXiv page. |
| R2 | https://arxiv.org/html/2110.12359 | HTML cache and abstract/metadata text | 2026-07-10 | Used through extraction cache. |
| R3 | https://arxiv.org/e-print/2110.12359 | TeX source review | 2026-07-10 | Used through extraction cache; not deposited. |
| R4 | https://arxiv.org/pdf/2110.12359 | Public PDF reference | 2026-07-10 | PDF text unavailable locally; not redistributed. |
| R5 | https://doi.org/10.48550/arXiv.2110.12359 | Persistent DOI | 2026-07-10 | arXiv-issued DOI. |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | DEP output rules | 2026-07-10 | Live upstream README fetched/read. |
| R7 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related raw-data repository rules | 2026-07-10 | Read through authenticated GitHub connector. |
| R8 | `.lake-data/DEP-E-20260708-Agent State Review/agent_state_review.md` | Related-entry synthesis | 2026-07-10 | Existing Black-Lake artifact. |
| R9 | `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Related-entry synthesis | 2026-07-10 | Existing Black-Lake artifact. |
| R10 | `.lake-data/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` | Related-entry synthesis | 2026-07-10 | Existing Black-Lake artifact. |

## Appendix

### Public-Safe Selection Record

- Candidate paper units: 75,438.
- Selection method: uniform random index using PowerShell `Get-Random` after `rg --files -g "*.pdf"` enumeration.
- Selected zero-based index: 22,294.
- Reselections: 0.
- Exclusions during acceptance: no arXiv ID, 0; prior Black-Lake artifact hit, 0; Black-Lake-Data ID/title hit, 0.

### Cache Record

- Pre-run cache status: missing.
- Local extraction mode: `missing-only`.
- Local extraction result: metadata-only because local PDF text extraction failed and no local HTML/source package was present.
- Public backfill: performed after text was missing; public arXiv HTML and source package were fetched.
- Final cache result: cached; HTML text and source text present; PDF text absent.

### Dedup Record

- Dedup index existed before run: no.
- Duplicate markers checked: arXiv ID, DOI, normalized title, slug, and same-paper markers within recent artifacts.
- Accepted status: no prior marker found.
- Dedup pointer path: `.staging/arxiv-dep-dedup-index.json`.
