# Report-Mark: Semantic Skill MoE

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P08`
- Review date: 2026-07-19
- Review type: source-first robotics policy and safety-gated routing synthesis

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Semantically Structured Mixture-of-Experts for Compositional Robotic Manipulation* |
| Authors | Chengyu Deng; Guanqi Chen; Yizhou Chen; Zejia Liu; Zhiwen Ruan; Guanhua Chen; Jia Pan |
| Stable identifier | arXiv:2605.23477v1 |
| Submission history | Submitted 2026-05-22 |
| DOI | https://doi.org/10.48550/arXiv.2605.23477 |
| Primary record | https://arxiv.org/abs/2605.23477 |
| Full-paper HTML | https://arxiv.org/html/2605.23477 |
| PDF | https://arxiv.org/pdf/2605.23477 |
| Source state | Verified complete after one bounded repair; source files withheld locally. |
| Deployment job ID | `BLAD-2200-20260719-7D93E819` |
| Deployment item ID | `BLAD-2200-20260719-7D93E819-P08` |

## Concise Research Notes

### Problem

Diffusion policies can model precise action distributions but scale poorly across many manipulation tasks. Conventional sparse MoE routers may fragment reusable behavior because their routing signals are not tied to compositional skill structure.

### Method

SMoDP labels demonstrations offline with VLM-generated verb-noun skills and temporal segments. During policy training, a lightweight predictor maps visual/language context into a frozen text-embedding space. The predicted skill conditions a diffusion transformer and routes all action tokens in a chunk through a shared top-k expert decision. Inter-modal contrast aligns predicted skills with language; intra-modal contrast encourages semantically related skills to reuse similar experts. The VLM is not used at inference.

### Evidence

The paper reports leading average success on LIBERO-10/90, stronger low-data performance, and few-shot transfer using 13.7M trainable parameters within a 401M total model. Table I reports LIBERO-10 success 0.520/0.765/0.840 for 1/5/10 demonstrations. Four real-robot tasks use 20 trials each; average success is 91.25% versus 47.50% for MoDE, including 20/20 versus 0/20 on Handoff Cup. Removing both contrastive losses lowers LIBERO-90 average from 0.970 to 0.946. Moderate synthetic annotation noise causes small reported degradation.

### Limits

Verb-noun labels omit force, speed, and trajectory; VLM segmentation can hallucinate or misplace boundaries; long-tail skills remain underrepresented. Real-world evidence totals 80 rollouts across four tasks and lacks broad environment, hardware, operator, failure-severity, and independent replication detail. Reported success does not replace collision, force, reachability, human-presence, or emergency-stop validation.

## Evidence and Attribution

| Claim | Source basis | Reviewer qualification |
|---|---|---|
| Offline semantic labels supervise a lightweight inference-time router. | Sections III-A and III-B. | Direct architecture claim; annotation quality remains a dependency. |
| Shared routing across an action chunk improves consistency. | Equations 6-10. | Mechanistic design, not a safety guarantee. |
| SMoDP reports stronger few-shot transfer. | Table I. | Source-reported benchmark result. |
| Real-world average is 91.25% versus 47.50%. | Table II. | 20 trials per task; narrow setup and no severity-weighted failures. |
| Dual alignment contributes to LIBERO-90 success. | Table III. | Ablation supports complementarity within the reported setup. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - input-dependent routes need stability and real-runtime measures.
2. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` - learned action structure can transfer while failing on rare motions and distribution shift.
3. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` - performance policies should be wrapped by explicit admissibility and fallback control.

## Synthesis Note

### Concept Bridge

SMoDP makes expert routing interpretable at the skill level, but semantic organization and physical admissibility are different layers. DMNN supplies route-stability and systems evaluation for conditional networks. LA-Pose supplies a transfer perspective and warns that learned motion representations can weaken on rare or shifted behaviors. RRT-CBF supplies the missing safety envelope: candidate actions should pass independent state, collision, force, and barrier checks before execution. The combined design is a simulation-first semantic-policy evaluator feeding a separately verified supervisor, not a direct path from language annotation to hardware actuation.

### Potential Implementations

1. Build a simulation-only route audit that measures skill prediction, expert reuse, load balance, route changes, and success by phase.
2. Add an independent admissibility filter that can reject action chunks without consulting the learned router.
3. Create a rare-skill coverage dashboard linking label frequency, annotation confidence, failure severity, and fallback rate.

### Deeper Relationship Observations

1. Semantic routing can improve reuse while concentrating correlated failures when one skill label controls many tasks.
2. Chunk-consistent routing reduces within-chunk switching but can preserve a wrong route for the full chunk.
3. VLM supervision moves cost offline, yet it also moves annotation error into a less visible training dependency.

### Conceptual Similarities

1. SMoDP and DMNN both route inputs through sparse experts and need stability, utilization, and latency evidence.
2. SMoDP skill embeddings and LA-Pose latent actions both compress motion structure for transfer.
3. SMoDP action chunks and RRT-CBF extensions both require a separate notion of admissibility before physical execution.

### MVP Implementations with Code Mock-Ups

1. Route audit record:

```python
def route_record(skill, experts, confidence, success):
    return {"skill": skill, "experts": tuple(experts),
            "confidence": confidence, "success": bool(success)}
```

2. Independent simulated admissibility gate:

```python
def admit(chunk, checks):
    failed = [name for name, check in checks.items() if not check(chunk)]
    return {"allowed": not failed, "failed_checks": failed}
```

3. Rare-skill coverage summary:

```python
def coverage(records, minimum=20):
    counts = {}
    for row in records:
        counts[row["skill"]] = counts.get(row["skill"], 0) + 1
    return {skill: {"count": n, "undercovered": n < minimum}
            for skill, n in counts.items()}
```

### Developer Challenges

1. Skill labels, temporal boundaries, router versions, and expert checkpoints must remain aligned and reproducible.
2. Safety supervisors require conservative state estimation and must remain independent of learned semantic confidence.
3. Sparse expert inference can suffer load imbalance, kernel overhead, and route nondeterminism on target hardware.

### Author Challenges

1. Expand real-world evaluation across robots, environments, operators, object variation, and safety-relevant failures.
2. Quantify annotation correctness and temporal-boundary error against expert human labels.
3. Report failure severity, uncertainty, latency, fallback behavior, and independent replication artifacts.

## Validation Notes

- Random selection: index 35,828 of 75,777 units from 75,790 PDFs; first draw; duplicate exclusions 0; reselections 0.
- Integrity: one bounded partial-to-complete repair; PDF and official HTML verified; cache `cached`; no partials.
- Structure: all required sections; exactly three items per synthesis category; three syntax-checked Python mock-ups.
- Physical safety: only simulation, auditing, and independent gating are proposed; no hardware command, trajectory, or deployable controller is included.
- Public-safety: local paths, exact timestamps, timezone labels, user/machine context, and all source documents withheld.

## Attribution Block

- https://arxiv.org/abs/2605.23477 - canonical metadata, authorship, abstract, and identifier.
- https://arxiv.org/html/2605.23477 - full-paper method, experiments, appendices, and limitations.
- https://arxiv.org/pdf/2605.23477 - validated complete PDF; withheld locally.
- https://doi.org/10.48550/arXiv.2605.23477 - persistent identifier.
- `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - conditional-routing evidence.
- `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` - latent-action transfer evidence.
- `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` - constrained-motion safety evidence.
- PDF, HTML, metadata, extracted text, and cache records were withheld locally; zero source uploads.
