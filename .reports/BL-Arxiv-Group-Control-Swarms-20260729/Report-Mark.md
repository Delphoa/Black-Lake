# Report-Mark: Group-Control Swarms

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Group-Control Motion Planning Framework for Microrobot Swarms in a Global Field* |
| Authors | Siyu Li; Afagh Mehri Shervedani; Miloš Žefran; Igor Paprotny |
| arXiv | [2406.13829v2](https://arxiv.org/abs/2406.13829v2), submitted 2024-06-19 and revised 2024-12-10 |
| arXiv DOI | [10.48550/arXiv.2406.13829](https://doi.org/10.48550/arXiv.2406.13829) |
| Proceedings context | WAFR 2024; Springer Proceedings in Advanced Robotics, volume 37, pages 269-288 |
| Chapter DOI | [10.1007/978-3-032-09967-9_14](https://doi.org/10.1007/978-3-032-09967-9_14) |
| Primary evidence | Complete 18-page PDF, official full-paper HTML, TeX source, arXiv metadata, WAFR public paper, and Springer chapter record |
| Source integrity | Verified complete after a bounded local repair; all original source and cache files withheld locally |
| Code status | No author-linked public implementation was established in a bounded search; no code or experiment was run |
| Public review date | 2026-07-29 |

## Concise Research Notes

The paper asks how a swarm of MicroStressBots can reach individual positions when every robot receives the same global electrostatic signal. Its answer is **group-control**: each robot receives an onboard physical finite-state-machine configuration that makes it belong to a unique subset of activation groups. Activating one group translates its members while the others rotate, producing an addressable switched system without one unique command channel per robot.

For \(n\) robots, the paper states that \(m=\log_2(n+2)+1\) groups suffice for unique allocation and position-level small-time local controllability (STLC). The construction converts unilateral forward/counter-clockwise actuation into bilateral vector fields through compound motions, shows bounded orientation control, and recursively eliminates unwanted translations until one robot can be translated independently. This is a formal source claim under idealized dynamics; it is not a hardware validation.

The planning layer introduces logical subgroups and Lie-bracket-inspired motion primitives. Higher-order primitives affect fewer robots and reduce planner coupling, but require more nested back-and-forth motion. Lower-order primitives move more robots in parallel and can shorten execution paths, but increase the dimensionality and computational cost of planning. The paper summarizes this with an RRT complexity expression of \(O(nc^nL^{k_{\max}-k})\) under its modeling assumptions.

The simulation evidence uses six robots and four groups. In the collision-free comparison averaged over 20 instances, numerical optimization reports 0.80 s planning runtime and path length 181.04; RRT with rotation reports 8.88 s and 323.57; original RRT reports 393.53 s and 332.10, with 15 of 20 original-RRT cases failing within the allotted time. In the obstacle comparison averaged over 10 instances, subgroup-sequential planning reports 15.38 s runtime, 529.47 path length, and 577.41 s execution, compared with 216.15 s, 868.66, and 886.04 s for subgroup-parallel planning.

The strongest empirical conclusion is therefore bounded: the selected subgroup structure can move planning to a more favorable point on a computation-versus-execution tradeoff in the shown simulator. The evidence does not establish general swarm-scale performance, physical reliability, manufacturing feasibility, robustness to model error, or safety in medical or industrial deployment.

## Evidence and Attribution

| ID | Evidence | Supports | Reviewer assessment |
|---|---|---|---|
| E1 | [arXiv record](https://arxiv.org/abs/2406.13829v2) | Identity, authors, dates, abstract, subject, version, and arXiv DOI | High-confidence metadata |
| E2 | [Official HTML](https://arxiv.org/html/2406.13829v2) and [PDF](https://arxiv.org/pdf/2406.13829v2) | Dynamics, group allocation, STLC argument, motion primitives, simulations, tables, figures, and conclusion | High confidence for what the source states; formal claims were not independently proved |
| E3 | Official TeX source, withheld locally | Exact formulas, table values, captions, and source-level wording | High confidence for transcription; redistribution was not authorized |
| E4 | [Springer chapter DOI](https://doi.org/10.1007/978-3-032-09967-9_14) and [WAFR paper](https://algorithmic-robotics.org/papers/65_Group_Control_Motion_Planni.pdf) | Proceedings context and later chapter identity | High-confidence bibliographic context |
| E5 | PDF page renders and integrity report, withheld locally | Eighteen-page visual inspection, table/figure checks, and complete-paper gate | High confidence for source completeness; no source file deposited |
| E6 | Three inspected Black Lake entries | Cross-DEP synthesis on safe sampling, fast/slow planning, and persistent navigation state | Medium-high conceptual relevance; does not validate the selected paper |

The source's own reporting contains two tensions. First, the sequential-planning paragraph states 19.44 s, while Table 4 lists 15.38 s for subgroup sequential and 19.44 s for pure control. Second, Table 4 marks the “RRT with rotation” row with a footnote whose text says “Original RRT” failed in eight of ten cases. This review uses the table cells for quantitative comparisons and preserves both ambiguities instead of resolving them by assumption.

## Related DEP Entries

1. [RRT-CBF Motion - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md) - Direct overlap in RRT planning, continuous motion generation, collision avoidance, execution tracking, and the distinction between simulated feasibility and physical safety.
2. [SAGE-Nav Review - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260723-SAGE-Nav%20Review/sage_nav_manuscript.md) - A fast/slow architecture where semantic waypoints are planned asynchronously and consumed by a higher-frequency controller, paralleling the separation between primitive design and low-level group execution.
3. [CrossMaps Rover Mapping - DEP-A](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260722-CrossMaps%20Rover%20Mapping/2606.16935-whitepaper-review.md) - Confidence-aware semantic mapping supplies a persistent state layer for navigation, complementing a control paper that assumes the planner already has reliable robot and obstacle state.

## Synthesis Note

### Concept Bridge

The four records form a layered autonomy stack. CrossMaps focuses on how a robot constructs and retains a queryable world state. SAGE-Nav turns structured state into sparse high-level waypoints while keeping local control fast. Group-control compiles desired swarm motion into hardware-constrained subgroup primitives. RRT-CBF adds a constraint-aware mechanism for rejecting or reshaping unsafe sampled motion. The combined design is not present in any one source, but it suggests a testable interface: `state snapshot -> waypoint/goal -> constrained plan -> primitive schedule -> tracked execution -> updated state`.

### Potential Implementations

1. **Constraint-aware swarm simulator:** Add control-barrier or reachability checks to group-control RRT extensions, logging minimum obstacle distance, rejected extensions, primitive order, path length, and execution cost.
2. **Fast/slow primitive scheduler:** Plan subgroup sequences at a slower cadence, cache them with state/version identifiers, and let a deterministic controller execute only while the schedule remains fresh and feasible.
3. **Confidence-gated world-state adapter:** Convert rover-style confidence-aware mapping into conservative obstacle and robot-state bounds before swarm planning, with explicit abstention when pose or map confidence is insufficient.

### Deeper Relationship Observations

1. Each source reduces a large search space by introducing a structured intermediate representation: semantic cells, scene-graph waypoints, subgroup primitives, or barrier-constrained edges.
2. Each intermediate representation can become stale or wrong; therefore version, age, uncertainty, and fallback state belong at the interface, not only inside the originating module.
3. Compute is shifted rather than eliminated: richer primitives simplify global planning but make execution longer, while richer state and safety checks improve decisions but add sensing, optimization, and monitoring cost.

### Conceptual Similarities

1. All four systems separate proposal from execution instead of treating navigation as one opaque policy.
2. All rely on bounded abstractions that are useful only while their assumptions hold: map confidence, waypoint validity, barrier-model accuracy, and primitive realizability.
3. All need outcome-level evaluation in addition to internal metrics; path success, collision margin, deadline compliance, and recovery behavior matter more than an isolated planner score.

### MVP Implementations with Code Mock-Ups

1. **Group allocation compiler**

```python
from math import ceil, log2

def allocate_groups(robot_count: int) -> dict[int, tuple[int, ...]]:
    if robot_count < 1:
        raise ValueError("robot_count must be positive")
    group_count = ceil(log2(robot_count + 2)) + 1
    selectable = group_count - 1
    codes = range(1, (1 << selectable) - 1)
    return {
        robot: tuple(bit for bit in range(selectable) if code & (1 << bit))
        for robot, code in zip(range(robot_count), codes)
    }
```

The explicit ceiling turns the paper's real-valued expression into an integer implementation rule. A production compiler would also verify PFSM capacity, forbidden all-zero/all-one assignments, fabrication constraints, and the dedicated all-rotate group.

2. **Planner tradeoff scorer**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Trial:
    planner_seconds: float
    path_length: float
    execution_seconds: float
    success: bool

def score(trial: Trial, weights=(1.0, 0.05, 0.2)) -> float:
    if not trial.success:
        return float("inf")
    return (
        weights[0] * trial.planner_seconds
        + weights[1] * trial.path_length
        + weights[2] * trial.execution_seconds
    )
```

This mock-up forces failed trials into the objective instead of averaging only successful paths. A real benchmark should use paired trials, uncertainty intervals, explicit timeouts, and safety constraints rather than one scalar alone.

3. **Evidence-gated primitive release**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Gate:
    state_age_ms: int
    min_clearance: float
    model_error: float
    primitive_verified: bool

def releasable(gate: Gate) -> bool:
    return (
        gate.state_age_ms <= 100
        and gate.min_clearance >= 0.25
        and gate.model_error <= 0.05
        and gate.primitive_verified
    )
```

The numbers are synthetic test thresholds, not physical specifications. The safe behavior when the gate fails is simulator stop or supervised hold, never unreviewed actuation.

### Developer Challenges

1. Reproducing the paper requires source code, seeds, timeout values, solver details, primitive libraries, and scenario manifests that were not established in public author-linked artifacts.
2. A planner must account for non-instantaneous rotations, actuation noise, sensing delay, model mismatch, and collision risk during the back-and-forth motions used to synthesize bilateral behavior.
3. Combining mapping, high-level planning, barrier checks, primitive compilation, and control introduces clock, version, queueing, and failure-propagation problems that average runtime does not reveal.

### Author Challenges

1. Clarify the integer group-count rule, the Table 4 sequential-runtime mismatch, and which RRT variant the failure footnote actually describes.
2. Publish code, configurations, trial-level results, seeds, timeouts, solver settings, and hardware-independent regression tests for every reported table and figure.
3. Extend evaluation beyond six simulated robots to manufacturing variation, noisy sensing and actuation, dynamic obstacles, physical prototypes, and statistically reported scale curves.

## Validation Notes

- Required `rg --files -g "*.pdf"` selection used 75,781 PDFs and 75,778 parent-directory paper units.
- Conservative deduplication observed 1,547 used base identifiers, excluded 425 used-ID units, withheld 185 identifier-incomplete units, and drew accepted eligible index 72,419 from 75,168 units.
- Exact arXiv ID, DOI, normalized title, and slug checks found no prior same-paper deposit; the 24-hour cutoff was 2026-07-28.
- Initial source state was partial because full-paper HTML was absent. A bounded repair preserved the valid PDF and collected official HTML, metadata HTML, and the source archive.
- The final PDF and HTML passed all required structural gates; the source archive listed 56 entries; all 18 pages were rendered and visually inspected; no partials remained.
- Exactly three related DEP entries were inspected and used.
- Source claims and reviewer interpretations are labeled separately.
- Three code mock-ups are synthetic, offline, and non-actuating.
- All source files were withheld locally. No `.source/` directory was created and no PDF, HTML, archive, cache, extracted text, render, or private verification record was uploaded.
- Public-output path, identity, timezone, timestamp, source-file, and encoding scans are required before submission.

## Attribution Block

- Source URL: https://arxiv.org/abs/2406.13829v2
  - Applies to: `Report-Mark.md`
  - Notes: Canonical metadata, abstract, dates, authors, subject, and DOI.
- Source URL: https://arxiv.org/html/2406.13829v2
  - Applies to: `Report-Mark.md`
  - Notes: Official full-paper evidence for the mechanism, proof, experiments, limitations, tables, and figures.
- Source URL: https://arxiv.org/pdf/2406.13829v2
  - Applies to: `Report-Mark.md`
  - Notes: Public locator for the visually inspected 18-page PDF; source file withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2406.13829
  - Applies to: `Report-Mark.md`
  - Notes: Stable arXiv DOI.
- Source URL: https://doi.org/10.1007/978-3-032-09967-9_14
  - Applies to: `Report-Mark.md`
  - Notes: Springer chapter DOI and proceedings identity.
- Source URL: https://algorithmic-robotics.org/papers/65_Group_Control_Motion_Planni.pdf
  - Applies to: `Report-Mark.md`
  - Notes: WAFR public paper record.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - Applies to: `Report-Mark.md`
  - Notes: Related DEP on constrained RRT motion planning.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260723-SAGE-Nav%20Review/sage_nav_manuscript.md
  - Applies to: `Report-Mark.md`
  - Notes: Related DEP on fast/slow semantic navigation planning.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260722-CrossMaps%20Rover%20Mapping/2606.16935-whitepaper-review.md
  - Applies to: `Report-Mark.md`
  - Notes: Related DEP on confidence-aware rover mapping and state.
- Source files: Withheld locally.
  - Applies to: `Report-Mark.md`
  - Notes: No paper source, metadata snapshot, archive, extracted text, render, summary, attribution record, or private verification artifact was deposited.
