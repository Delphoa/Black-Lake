# Report-Mark: SAGE-Nav

- Public run marker: 2026-07-23 (date only)
- Review type: Source-first arXiv paper review and DEP-E synthesis
- Review status: Complete
- Primary identifier: arXiv:2606.25497v1
- DOI: https://doi.org/10.48550/arXiv.2606.25497
- Primary record: https://arxiv.org/abs/2606.25497
- Source policy: Verified local source documents were inspected and withheld; this report contains derived public-safe Markdown only.

## Source Metadata

| Field | Value |
|---|---|
| Title | *SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation* |
| Authors | Hao Su; Yuehao Huang; Yukai Ma; Yong Liu; Jiajun Lv |
| Affiliation reported in paper | Zhejiang University |
| arXiv ID | 2606.25497v1 |
| arXiv DOI | 10.48550/arXiv.2606.25497 |
| Submitted | 2026-06-24 |
| Subject | Robotics (cs.RO) |
| Venue status | arXiv comments state “Accepted by IROS 2026”; no separate proceedings record was inspected |
| License note | The canonical record links the arXiv non-exclusive distribution license; original files remain withheld by workflow policy |
| Complete source gate | Passed after one bounded repair |
| Official implementation | No author-identified code repository was found in the canonical record or bounded public search |

## Local Source Integrity

The unit was initially partial because it contained a valid PDF but no full-paper HTML. The existing 16,110,369-byte PDF passed the minimum-size, `%PDF-`, trailing `%%EOF`, and SHA-256 checks and was preserved. A bounded direct-HTTPS repair added official metadata HTML and the arXiv source archive; official full-paper HTML was unavailable, so the approved ar5iv fallback was used.

The final full-paper HTML is 179,235 bytes and contains 47,690 body characters, three document markers, 61 heading/section markers, and at least five paper-structure term classes. It contains no abstract-only, error, or conversion marker. The local README, attribution record, CSV summary, preflight manifest, and verification report were updated, and zero partial files remained. All eight PDF pages were rendered and visually inspected. No local source or inspection file is included in this repository artifact.

## Concise Research Notes

### Problem

Object-goal navigation requires an embodied agent to locate a named object from egocentric observations. Reactive policies can be efficient locally but lack explicit long-horizon semantic reasoning, while online LLM planners can be slow, difficult to ground, and expensive to invoke at every action.

### Method

SAGE-Nav divides the system into three coupled modules:

- The Hierarchical Global Planner builds an incrementally updated multilevel scene graph, retrieves an instruction-relevant compact subgraph, and uses Qwen2.5-VL-7B to produce semantically grounded waypoint sequences. Planning is asynchronous and is retriggered on subgoal completion or deadlock.
- The Hierarchical Scene Graph Encoder applies three relational graph-convolution layers to CLIP and 3D positional node features, conditions graph representations on the active waypoint, and pools across hierarchy levels into a 64-dimensional waypoint embedding.
- The Goal-aware Alignment-Fusion Network cross-attends visual features to the waypoint embedding and applies an explicit alignment-sensitive gate before a two-layer LSTM actor-critic chooses a discrete navigation action.

The visual backbone is frozen CLIP ViT-B/32. The scene graph uses OpenSEED segmentation, multi-frame fusion, and VLM relation reasoning. Training uses A3C for six million episodes, the best validation checkpoint, and 1,000 test episodes on one source-reported RTX 3090.

### Evidence and Results

Table I reports the following SAGE-Nav outcomes:

| Setting | SR | SPL | DTS |
|---|---:|---:|---:|
| iTHOR, all paths | 82.47% | 42.34% | 0.32 m |
| iTHOR, optimal path at least 5 m | 77.22% | 43.73% | 0.43 m |
| RoboTHOR, all paths | 52.35% | 30.12% | 0.72 m |
| RoboTHOR, optimal path at least 5 m | 40.82% | 22.95% | 1.10 m |

Against TSOG, the absolute success-rate margins are 2.43 points for all iTHOR paths, 3.76 points for long-horizon iTHOR, 2.46 points for all RoboTHOR paths, and 2.21 points for long-horizon RoboTHOR. The paper correctly notes that CGI-GAIL retains higher iTHOR SPL, so the evidence does not support an unqualified “best on every metric” reading.

For six object categories withheld from training, Table II reports 75.05% success, 34.05% SPL, and 0.38 m DTS. Removing alignment fusion produces the largest listed success decrease, to 70.65%. Removing LLM reasoning yields 73.30%, and removing unseen-object inference yields 73.84%.

The RoboTHOR efficiency comparison reports 52.4% success, 30.1% SPL, 0.42 seconds average latency, and 9.1 LLM calls per episode. CogNav reports higher success at 54.6% but lower SPL, higher average latency, and more LLM calls. The paper does not fully specify tail latency, network/service conditions, prompt/token cost, cache age, or how asynchronous planner work is amortized into the reported step metric.

### Failure Cases and Limitations

The paper visualizes target-visibility failure, detector confusion, entrapment, and premature termination. These are directly relevant because an incorrect or stale semantic waypoint can produce confident but ineffective low-level behavior.

The evidence remains simulation-only despite language about physical deployment. Baseline numbers are largely adopted from original publications rather than reproduced under one harness. No repeated training seeds, confidence intervals, calibration analysis, full latency distribution, LLM cost accounting, or official implementation package was found. The RoboTHOR description first states 89 apartments with 75 for training/validation and 14 for testing, then reports a 60/5/10 operational split; the relationship between those counts is unclear. Training graphs are preconstructed offline even though deployment graphs are online, which leaves a training-to-runtime state-distribution question.

## Evidence Ledger

| ID | Source | Evidence Used | Supports | Confidence | Limitation |
|---|---|---|---|---|---|
| E1 | arXiv metadata and DOI | Title, authors, submission date, category, comments, source links | Identity and venue-status wording | High | Metadata only |
| E2 | Complete eight-page PDF | Architecture diagrams, equations, datasets, training details, Tables I-IV, trajectories, failure cases | Method and empirical transcription | High for transcription | No independent reproduction |
| E3 | Verified full-paper HTML | Section structure, searchable method and result cross-check | Full-text consistency | High | Approved ar5iv rendering rather than official arXiv HTML |
| E4 | arXiv source archive | Source completeness and equation/table provenance | Source-integrity confidence | High | Source not redistributed or compiled independently |
| E5 | Canonical record and bounded public code search | No official repository link located | Reproducibility boundary | Medium-high | A later or unindexed release may exist |
| E6 | Three related Black Lake manuscripts | Navigation, safety, and fast-slow control relationships | Cross-DEP synthesis | Medium | Related work does not validate SAGE-Nav |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-VG Navigable Space/vg_navigable_space_manuscript.md`
   - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260720-VG%20Navigable%20Space/vg_navigable_space_manuscript.md
   - Relevance: Both systems fuse semantic perception with geometry for navigation. VG-Nav adds explicit traversability costs and predictive uncertainty, supplying a local evidence and abstention layer that SAGE-Nav’s semantic waypoint interface lacks.
   - Source basis: The related manuscript’s reviewed primary paper on visual/geometric sparse-GP navigation, its simulation and small real-world trials, timing evidence, uncertainty, and deployment limitations.
2. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md`
   - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
   - Relevance: SAGE-Nav proposes semantically useful waypoints, while RRT-CBF separates proposal quality from motion admissibility through barrier-constrained extension, tracking, feasibility telemetry, and fallback.
   - Source basis: The related manuscript’s reviewed CBF-RRT formulation, MPC tracking layer, simulated mobile/manipulator examples, and explicit limits around unknown dynamics and solver failure.
3. `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md`
   - Public URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-FAVLA%20Fast-Slow/favla_fast_slow_manuscript.md
   - Relevance: Both architectures cache a slower semantic representation and adapt it into faster action generation. FAVLA makes the scheduling and freshness problem concrete through force-conditioned action updates; SAGE-Nav makes it concrete through asynchronous waypoint planning and gated visual-topological fusion.
   - Source basis: The related manuscript’s reviewed fast-slow VLA architecture, adaptive action-expert scheduling, multi-rate timing tension, physical task results, and failure analysis.

## Synthesis Note

### Concept Bridge

Together, the four artifacts describe a layered navigation stack with distinct responsibilities. SAGE-Nav supplies semantic waypoint planning and a learned alignment interface. VG Navigable Space supplies geometry/semantics conflict handling and uncertainty-driven abstention. RRT-CBF Motion supplies an independent admissibility and fallback layer. FAVLA Fast-Slow supplies systems questions about cache age, conditional compute, and rate mismatch. The resulting principle is that semantic planning, local traversability, motion safety, and timing freshness should be independently observable and testable. Aggregate success or low average latency cannot substitute for evidence at those interfaces.

### Potential Implementations

1. **Waypoint trace auditor:** Reconstruct graph revisions, compact-subgraph retrieval, prompt/response identifiers, parsed waypoints, replanning triggers, cache age, low-level actions, and outcomes from authorized offline traces.
2. **Semantic-to-safe planning simulator:** Feed synthetic semantic waypoints through uncertainty-aware traversability scoring and a mocked constraint/fallback layer, then measure completion, detours, infeasibility, abstention, and recovery.
3. **Matched-accounting benchmark:** Compare SAGE-Nav-style asynchronous planning with reactive, synchronous-LLM, and static-graph baselines under identical episodes, compute, seeds, prompts, graph updates, and end-to-end latency accounting.

### Deeper Relationship Observations

1. SAGE-Nav and FAVLA both make a slower representation reusable, but the relevant freshness variable differs: graph/waypoint age in navigation versus force/context age in contact manipulation.
2. VG-Nav’s uncertainty exposes when local semantic and geometric evidence disagree, while SAGE-Nav’s learned gate does not by itself provide calibrated abstention; combining them suggests a separate evidence state outside the fusion network.
3. RRT-CBF shows why an interpretable waypoint is not yet a safe trajectory: semantic desirability, geometric feasibility, dynamic admissibility, and execution tracking are separate claims with separate failure modes.

### Conceptual Similarities

1. Each artifact decomposes long-horizon intent from short-horizon execution through an explicit intermediate representation.
2. Each uses a compact control signal—waypoint embedding, traversability cost and variance, barrier margin, or force-variance schedule—to modulate downstream decisions.
3. Each depends on boundary telemetry such as state age, uncertainty, feasibility, latency, and fallback status that aggregate task success does not reveal.

### MVP Implementations with Code Mock-ups

#### 1. Waypoint Freshness Contract

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Waypoint:
    label: str
    graph_revision: int
    created_step: int


def accept_waypoint(item: Waypoint, current_revision: int, step: int) -> bool:
    same_graph = item.graph_revision == current_revision
    fresh = 0 <= step - item.created_step <= 20
    return same_graph and fresh and bool(item.label.strip())


print(accept_waypoint(Waypoint("kitchen", 7, 100), 7, 112))
```

This dependency-free mock-up makes graph revision and cache age explicit. A real system also needs clock reconciliation, parser validation, deadlock semantics, and a deterministic invalid-plan response.

#### 2. Uncertainty-Aware Candidate Filter

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Candidate:
    name: str
    semantic_score: float
    traversability: float
    uncertainty: float


def choose(candidates: list[Candidate], uncertainty_limit: float) -> str:
    safe = [c for c in candidates if c.traversability > 0.6 and c.uncertainty <= uncertainty_limit]
    if not safe:
        return "abstain"
    return max(safe, key=lambda c: c.semantic_score).name


demo = [Candidate("hallway", 0.8, 0.9, 0.1), Candidate("stairs", 0.9, 0.4, 0.2)]
print(choose(demo, uncertainty_limit=0.25))
```

The filter is a synthetic planning aid, not a robot controller. Production use would require calibrated uncertainty, dynamic obstacles, map-frame validity, and independent collision protection.

#### 3. Evidence-Gated Action Receipt

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    waypoint_fresh: bool
    perception_fresh: bool
    traversable: bool
    constraint_feasible: bool
    fallback_ready: bool


def receipt(evidence: Evidence) -> str:
    valid = all((
        evidence.waypoint_fresh,
        evidence.perception_fresh,
        evidence.traversable,
        evidence.constraint_feasible,
    ))
    if valid:
        return "allow_mock_action"
    return "fallback" if evidence.fallback_ready else "stop"


print(receipt(Evidence(True, True, True, False, True)))
```

This receipt demonstrates fail-closed composition. It cannot establish barrier invariance, real-time guarantees, calibrated perception, or physical safety.

### Developer Challenges

1. Reconstruct and instrument the complete asynchronous contract: graph updates, prompt inputs, LLM responses, waypoint parsing, cache age, replanning triggers, deadlock detection, network/service latency, and action-loop deadlines.
2. Build a fair multi-system benchmark that pins scene splits, sensors, detector versions, prompts, LLM endpoints, compute, seeds, success definitions, baseline tuning, and amortized plus tail-latency accounting.
3. Integrate learned waypoint guidance with independently testable traversability, state-freshness, constraint-feasibility, and safe-stop interfaces that cannot be bypassed by model confidence.

### Author Challenges

1. Release code, prompts, scene-graph schemas, parser logic, configs, checkpoints, seeds, evaluation scripts, and exact baseline reproduction notes sufficient to recreate Tables I-IV.
2. Clarify RoboTHOR split accounting and report repeated-seed confidence intervals, per-category denominators, checkpoint-selection effects, end-to-end latency distributions, LLM token/cost totals, and planner failure rates.
3. Validate the system on physical robots with detector/graph staleness, occlusion, dynamic obstacles, entrapment, communication delay, and independently governed collision and safe-stop controls.

## Validation Notes

- Complete-source integrity passed before review; metadata-only HTML was never counted as the paper.
- The valid PDF was preserved during one bounded repair; official metadata HTML, approved ar5iv full-paper HTML, and the arXiv source package completed the private source bundle.
- All eight PDF pages, architecture figures, Tables I-IV, trajectories, and failure visualizations were inspected; no experiment or code was executed.
- Related synthesis contains exactly three DEP entries with repository-relative paths, public URLs, relevance, and source basis.
- The Synthesis Note contains exactly three potential implementations, deeper relationship observations, conceptual similarities, MVP code mock-ups, developer challenges, and author challenges.
- The three Python mock-ups use only the standard library and are prepared for syntax validation.
- Public-safety review targets private paths, usernames, machine names, local timezone labels, exact execution timestamps, and source-document leakage.
- No source file was uploaded; repository scope is generated Markdown only.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.25497
  - Applies to: title, authors, identifier, version, submission date, abstract, subject, venue-status comment, DOI, license link, and public source locators.
- Source URL: https://arxiv.org/pdf/2606.25497
  - Applies to: complete method, equations, architecture figures, datasets, Tables I-IV, trajectories, failure cases, and conclusions; inspected locally and withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/2606.25497
  - Applies to: verified full-paper text cross-check after the official HTML endpoint was unavailable; inspected locally and withheld.
- Source URL: https://arxiv.org/e-print/2606.25497
  - Applies to: source-package provenance and full-paper completeness; source archive withheld.
- Source URL: https://doi.org/10.48550/arXiv.2606.25497
  - Applies to: persistent paper identification.
- Related repository sources:
  - https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260720-VG%20Navigable%20Space/vg_navigable_space_manuscript.md
  - https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260722-FAVLA%20Fast-Slow/favla_fast_slow_manuscript.md
- Source files: Withheld locally; none were uploaded, staged, copied, or attached.
