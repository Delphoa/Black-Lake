# Report-Mark: MI-Motion

## Source Metadata

| Field | Value |
|---|---|
| Paper | *The MI-Motion Dataset and Benchmark for 3D Multi-Person Motion Prediction* |
| Authors | Xiaogang Peng; Xiao Zhou; Yikai Luo; Hao Wen; Yu Ding; Zizhao Wu |
| Identifier | arXiv:2306.13566v2; DOI: 10.48550/arXiv.2306.13566 |
| Submitted / revised | 2023-06-23 / 2023-06-26 |
| Primary sources | https://arxiv.org/abs/2306.13566; https://arxiv.org/html/2306.13566; https://arxiv.org/pdf/2306.13566 |
| Source state | Complete local PDF, metadata HTML, full-paper HTML, and source archive verified; all source files withheld locally |

## Concise Research Notes

MI-Motion is a 3D multi-person motion-prediction benchmark with five scenes, three-to-six-person interactions, 167k pose frames, and a Social Temporal Graph Convolutional Network baseline. SocialTGCN combines a pose-refine module, social-temporal GCN encoder, and TCN decoder.

The paper evaluates HRI, MRT, TBIFormer, and SocialTGCN at short, long, and ultra-long horizons. It reports 25 observed frames, 25 predicted frames, and another autoregressive 25 frames for the ultra-long horizon. Four non-crowd scenes use an 80/20 split; Complex Crowd is testing-only.

The source-reported results are mixed rather than a uniform win. At 400 ms, SocialTGCN reports AJPE of 53 mm in Park and 46 mm in Street, but in Special Locations its GJPE is 199 mm versus 189 mm for MRT and TBIFormer and its RFDE is 174 mm versus 144 mm for MRT. Its 0.320 G reported FLOPs is lower than the listed comparators, but end-to-end runtime conditions are not fully characterized.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Qualification |
|---|---|---|---|
| E1 | Official arXiv record | Title, authors, version, DOI, dates, abstract | Metadata is not sufficient for empirical claims |
| E2 | Verified full-paper HTML and PDF pages 1, 6, 8, and 20 | Dataset design, protocol, benchmark tables, ablations, visual layout | Results were inspected, not reproduced |
| E3 | Official MI-Motion project page | Dataset-access and supplementary-code statements | Access page does not establish a public repository or reproduction package |
| E4 | InterDance DEP-E | Reactive 3D duet motion and interaction-data overlap | Separate paper and task |
| E5 | LA-Pose DEP-E | Sequence-derived latent motion and pose-representation overlap | Camera pose is distinct from body-motion forecasting |
| E6 | RRT-CBF Motion DEP-E | Multi-agent trajectories and explicit safety constraints | Planning is not a direct forecasting baseline |

## Related DEP Entries

| Entry | Basis for relationship |
|---|---|
| .lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md | Both works center 3D interactive motion. InterDance supplies reactive duet-generation context, while MI-Motion evaluates forecasting. |
| .lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md | Both use temporal sequences to represent motion. LA-Pose is a representation-learning neighbor, not a direct body-motion comparator. |
| .lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md | Both reason about multi-entity trajectories and global motion. RRT-CBF adds constraints that MI-Motion does not certify. |

## Synthesis Note

### Concept Bridge

MI-Motion supplies a benchmark for interacting human trajectories; the related DEP entries frame adjacent representation, reactive-generation, and constraint-aware layers. This is an evaluative bridge, not a claim that their methods are interchangeable.

### Potential Implementations

1. **Interaction-aware forecasting benchmark:** retain MI-Motion-style horizons and add fixed manifests, repeated seeds, and confidence intervals.
2. **Latent-motion diagnostic layer:** compare a supervised SocialTGCN-style predictor with a LA-Pose-inspired representation using authorized inputs.
3. **Forecast-to-safety simulator:** feed synthetic predicted trajectories to an RRT-CBF-style monitor that reports clearance and infeasibility without controlling hardware.

### Deeper Relationship Observations

1. Multi-person motion needs relative body configuration and global trajectory reasoning; AJPE, GJPE, and RFDE expose different parts of that distinction.
2. Interactive-data realism is a data-construction question as well as a model question.
3. A forecast may be numerically accurate yet operationally unsafe; trajectory prediction should be evaluated separately from constraint satisfaction.

### Conceptual Similarities

1. MI-Motion and InterDance treat interaction as structured motion rather than independent single-person sequences.
2. MI-Motion and LA-Pose use temporal transitions as information-bearing signals for spatial reasoning.
3. MI-Motion and RRT-CBF require an explicit treatment of multiple entities' global positions over time.

### MVP Implementations with Code Mock-ups

1. **Root-relative pose normalization** makes a minimal representation before model comparison.

~~~python
def root_relative(points, root):
    return [[value - anchor for value, anchor in zip(point, root)]
            for point in points]
~~~

2. **Scene-aware split checking** prevents a designated test-only scene from entering training.

~~~python
def validate_scene_split(train_scenes, test_scenes, held_out):
    if set(train_scenes) & set(test_scenes) or held_out in train_scenes:
        raise ValueError("invalid scene partition")
    return True
~~~

3. **Trajectory-drift logging** reports an evaluation signal without acting on people or devices.

~~~python
def mean_root_drift(predicted, expected):
    if len(predicted) != len(expected) or not predicted:
        raise ValueError("aligned nonempty trajectories required")
    return sum(abs(p - e) for p, e in zip(predicted, expected)) / len(predicted)
~~~

### Developer Challenges

1. Preserve joint-order, coordinate-frame, sampling-rate, and person-identity conventions across every baseline.
2. Reproduce the reported split while adding leakage-resistant cross-scene and repeated-seed evaluations.
3. Distinguish plausible interaction, global drift, collisions, and static-pose collapse.

### Author Challenges

1. Reconcile the paper's 210- and 217-sequence descriptions through a versioned public manifest.
2. Publish a reproducible benchmark package with code, configurations, splits, data-access terms, and baseline revisions.
3. Report uncertainty, per-scene denominators, and broader failure slices beyond selected qualitative examples.

## Validation Notes

- Source gate passed: preserved PDF, metadata HTML, full-paper HTML, and source archive are local-only; PDF header/trailer and HTML structure checks passed.
- Public safety passed: no local paths, machine details, usernames, timezones, exact execution times, PDFs, HTML, source archives, caches, or extracted source text are included.
- Structural checks passed: exactly three related entries, three potential implementations, three deeper observations, three conceptual similarities, three MVP mock-ups, three developer challenges, and three author challenges.
- The three Python mock-ups are pure functions for synthetic or authorized evaluation data only.

## Attribution Block

- Source URL: https://arxiv.org/abs/2306.13566
  - Applies to: source identity, authors, dates, abstract, and identifier.
  - Notes: Canonical metadata source; original files were withheld locally.
- Source URL: https://arxiv.org/html/2306.13566
  - Applies to: method, dataset, evaluation, tables, and limitations.
  - Notes: Full-paper source inspected; original HTML was withheld locally.
- Source URL: https://mi-motion.github.io/
  - Applies to: dataset access and supplementary-code context.
  - Notes: Official project page, not an independently reproduced artifact.
