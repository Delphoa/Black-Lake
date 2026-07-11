# Report-Mark: RRT-CBF Motion

Public-safe run date: 2026-07-11

## Source Metadata

| Field | Value |
|---|---|
| Paper title | RRT-CBF Based Motion Planning |
| Authors | Leonas Liu; Yingfan Zhang; Larry Zhang; Mehbi Kermanshabi |
| arXiv ID | 2410.00343v1 |
| DOI | 10.48550/arXiv.2410.00343 |
| Source platform | arXiv; Robotics and Systems and Control |
| Submission date | 2024-10-01 |
| Primary sources | https://arxiv.org/abs/2410.00343 ; https://arxiv.org/pdf/2410.00343 |
| Source files deposited | None; no `.source/` directory was created |
| Local archive context | Metadata and PDF presence confirmed; location withheld from public output |

## Concise Research Notes

- **Problem:** The paper addresses collision-free motion planning where randomized tree search must respect robot dynamics and safety constraints around static obstacles, moving obstacles, and other robots. It also extends the same barrier-based steering idea to manipulators.
- **Method:** For mobile robots, a goal-biased steering RRT generates reference paths. A quadratic program enforces exponential control barrier function constraints while growing the tree, and a short-horizon MPC layer (`N = 3`) tracks those paths while treating other robots and circles as obstacles. A priority order makes each later robot avoid earlier robots. For manipulators, links are over-approximated as cylinders, obstacles as spheres, and active barrier constraints steer sampled configurations through a quadratic program.
- **Evidence/results:** The source presents simulation figures for a single robot, four robots with static circles, four robots with constant-velocity dynamic circles, a nonlinear point robot, a two-link arm with four obstacles, and a four-position-DoF Baxter arm with one spherical obstacle. The authors report collision-free trajectories in those illustrated cases and positive active barrier values for the Baxter example. These are source-reported simulation demonstrations, not reproduced results.
- **Limitations:** The evaluation does not report repeated-trial success rates, runtime distributions, path-cost comparisons, statistical tests, solver infeasibility rates, or hardware experiments. Dynamic obstacles are assumed to have known constant velocity; mobile robots use simplified dynamics; the priority strategy can disadvantage later robots; and the manipulator geometry uses sphere/cylinder approximations and activation thresholds. An official code repository was not found in inspected sources.
- **Implementation relevance:** The strongest transferable pattern is a layered planner: randomized global exploration proposes motion, a barrier-constrained optimizer makes local extensions admissible, and a receding-horizon tracker continuously repairs execution. A production system would need explicit feasibility fallbacks, uncertainty-aware prediction, worst-case latency evidence, and barrier-margin telemetry.
- **Reviewer interpretation:** The paper is useful as an integration blueprint, but its safety language should be read as conditional on the stated model and numerical solver assumptions. The figures demonstrate feasibility cases; they do not establish general safety, optimality, or real-time readiness.

## Evidence and Attribution

| ID | Evidence | Source basis | Use | Confidence |
|---|---|---|---|---|
| E1 | Title, authors, categories, version, DOI, submission date, page and figure counts. | arXiv abstract page | Bibliographic identity | High |
| E2 | CBF-RRT-MPC formulation, priority rule, obstacle model, horizon, and simulation parameters. | Primary PDF, Sections 1-5 | Method and mobile-robot evidence | High for source reporting; not independently derived |
| E3 | Point-robot, two-link, and Baxter formulations and illustrated results. | Primary PDF, Sections 6-8 | Manipulator evidence | High for source reporting; not reproduced |
| E4 | Known-velocity assumptions, settling deviation, proposed nonlinear/unknown-dynamics work, ellipsoid and temporal-logic extensions. | Primary PDF and conclusion | Limitation analysis | High |
| E5 | Related constrained vehicle control, asynchronous embodied control, and verified/fallback control patterns. | Three inspected DEP entries and their cited arXiv pages | Cross-DEP synthesis | Medium; conceptual context only |

## Related DEP Entries

1. `.lake-data/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md`
   - **Why selected:** It studies integrated decision and constrained control for autonomous vehicles around variable traffic participants, directly overlapping with dynamic obstacle representation, receding-horizon action, and safety evaluation.
   - **Source basis:** The DEP manuscript and its primary arXiv source, https://arxiv.org/abs/2110.12359, were inspected.
2. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260711-Tech Intel 0104/daily_research_findings_2026-07-11_0104.md`
   - **Why selected:** Its LingBot-VA 2.0 finding emphasizes causal video-action modeling, asynchronous closed-loop inference, and re-grounding on current observations, complementing the selected paper's model-based planner/tracker split.
   - **Source basis:** The DEP artifact, README attribution, and https://arxiv.org/abs/2607.08639 were inspected.
3. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260705-Tech Intel 0104/daily_research_findings_2026-07-05_0104.md`
   - **Why selected:** Its autonomous grid-control finding wraps a learned controller with rapid constraint verification, dynamic certification, and a conventional fallback, providing a mature safety-stack analogue for robot motion planning.
   - **Source basis:** The DEP artifact, README attribution, and https://arxiv.org/abs/2607.02379 were inspected.

## Synthesis Note

### Concept Bridge

All four works separate nominal action generation from a safety or freshness mechanism. RRT-CBF Motion uses stochastic exploration, barrier-constrained steering, and MPC tracking; Self Learned IDC compresses variable traffic state before constrained control; LingBot-VA re-grounds asynchronous predictions on the latest observation; and autonomous grid control screens learned actions, certifies dynamics, and falls back when proposals fail. Together they suggest that dependable embodied control is not one model but a contract among state representation, proposal generation, constraint checking, execution, and recovery.

### Potential Implementations

1. **Barrier-Aware Action Gateway:** Put every proposed robot action through a small constraint service that returns an admissible action, barrier margins, solver status, and fallback reason.
2. **Fresh-State Replanning Loop:** Pair an asynchronous learned proposer with a deterministic CBF/MPC corrector that re-grounds each rollout on the newest observation before execution.
3. **Multi-Agent Safety Ledger:** Record priority order, active obstacles, minimum margins, rejected proposals, fallback activations, and per-agent delay to expose both safety and fairness costs.

### Deeper Relationship Observations

1. The shared architectural unit is not the policy; it is the proposal-verification-execution loop, with explicit evidence at each boundary.
2. State freshness and constraint validity are coupled: a mathematically valid barrier evaluated on stale actor state can still authorize unsafe motion.
3. Fallback quality determines the real safety envelope because infeasible optimization, delayed observations, or out-of-distribution proposals are normal operational events.

### Conceptual Similarities

1. Each work converts variable physical context into a bounded control interface before acting.
2. Each work uses a fast online layer to compensate for a more expensive planning, learning, or prediction process.
3. Each work makes deployment credibility depend on more than task success: latency, constraint margins, state coverage, and recovery behavior matter.

### MVP Implementations with Code Mock-Ups

1. **Toy Barrier Gate**

```python
from dataclasses import dataclass

@dataclass
class GateResult:
    velocity: float
    margin: float
    fallback: bool

def barrier_gate(proposed: float, distance: float, safe_distance: float) -> GateResult:
    margin = distance - safe_distance
    if margin <= 0.0:
        return GateResult(velocity=0.0, margin=margin, fallback=True)
    return GateResult(velocity=min(proposed, margin), margin=margin, fallback=False)
```

2. **Fresh-State Guard**

```python
def accept_plan(plan_observation_id: int, latest_observation_id: int) -> bool:
    """Reject a plan whenever a newer observation is available."""
    return plan_observation_id == latest_observation_id
```

3. **Safety Ledger Row**

```python
def ledger_row(agent_id: str, margin: float, solver_ok: bool, priority: int) -> dict:
    return {
        "agent_id": agent_id,
        "minimum_margin": round(margin, 3),
        "solver_status": "ok" if solver_ok else "fallback",
        "priority": priority,
    }
```

### Developer Challenges

1. Demonstrate deterministic fallback behavior for infeasible CBF-QP or MPC steps without silently freezing the robot in a new hazard.
2. Measure worst-case end-to-end latency from sensing through state update, planning, verification, and actuation under maximum obstacle count.
3. Test whether the multi-robot priority rule preserves both minimum safety margins and bounded delay for every robot.

### Author Challenges

1. Release code, seeds, scenario files, solver settings, and evaluation scripts sufficient to reproduce every simulation figure.
2. Add matched baselines and repeated trials that report runtime, path length, success, infeasibility, and minimum barrier-margin distributions.
3. Replace constant known obstacle velocity with bounded uncertainty, occlusion, and behavior changes, then document the safety/fallback boundary.

## Validation Notes

- The live Black Lake and Black-Lake-Data README files were fetched before drafting.
- Random selection used 75,438 unique PDF parent-directory units; selected index 25,971; duplicate/reselection count 0; 24-hour cutoff 2026-07-10.
- The primary arXiv PDF was inspected across methods, simulations, conclusion, and references. Native text extraction succeeded through a private local cache; standard cache extraction remained partial. No local source file was deposited.
- Source claims, reviewer interpretation, and cross-DEP inference are labeled separately.
- Required synthesis subsections contain exactly three requested items each.
- Public artifacts use date-only markers, repository-relative paths, public URLs, and withheld-local-context notes.

## Attribution Block

- Source URL: https://arxiv.org/abs/2410.00343
  - Applies to: paper identity, abstract, authors, version, subject classes, DOI, and source links.
  - Notes: Primary arXiv metadata page inspected.
- Source URL: https://arxiv.org/pdf/2410.00343
  - Applies to: methods, equations, simulations, figures/captions, limitations, conclusion, and references.
  - Notes: Primary 20-page paper inspected; PDF not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2410.00343
  - Applies to: persistent paper identifier.
  - Notes: arXiv-issued DOI.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: artifact layout, DEP-E naming, contents, attribution, and commit rules.
  - Notes: Live repository authority fetched before writing.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related raw DEP layout and attribution interpretation.
  - Notes: Live related-repository authority fetched before use.
- Repository path: `.lake-data/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md`
  - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260710-Self%20Learned%20IDC/self_learned_idc_manuscript.md
  - Applies to: constrained vehicle-control synthesis.
  - Source reference: https://arxiv.org/abs/2110.12359
- Repository path: `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260711-Tech Intel 0104/daily_research_findings_2026-07-11_0104.md`
  - Public URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260711-Tech%20Intel%200104/daily_research_findings_2026-07-11_0104.md
  - Applies to: asynchronous, re-grounded robot-control synthesis.
  - Source reference: https://arxiv.org/abs/2607.08639
- Repository path: `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260705-Tech Intel 0104/daily_research_findings_2026-07-05_0104.md`
  - Public URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260705-Tech%20Intel%200104/daily_research_findings_2026-07-05_0104.md
  - Applies to: constraint-verification and fallback-control synthesis.
  - Source reference: https://arxiv.org/abs/2607.02379
