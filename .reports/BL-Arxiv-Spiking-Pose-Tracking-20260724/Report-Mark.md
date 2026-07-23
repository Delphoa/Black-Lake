# Report-Mark: Spiking Pose Tracking

Public-safe run date: 2026-07-24

## Source Metadata

| Field | Value |
|---|---|
| Title | Highly Efficient 3D Human Pose Tracking from Events with Spiking Spatiotemporal Transformer |
| Authors | Shihao Zou; Yuxuan Mu; Wei Ji; Zi-An Wang; Xinxin Zuo; Sen Wang; Weixin Si; Li Cheng |
| Stable identifier | arXiv:2303.09681v5 |
| Submitted / revised | 2023-03-16 / 2025-05-15 |
| Venue status | The arXiv record states acceptance by IEEE TCSVT |
| DOI | https://doi.org/10.48550/arXiv.2303.09681 |
| Primary record | https://arxiv.org/abs/2303.09681 |
| Full paper | https://arxiv.org/html/2303.09681 and https://arxiv.org/pdf/2303.09681 |
| Official implementation | https://github.com/JimmyZou/HumanPoseTracking_SNN |
| Source integrity | Initially partial; repaired to verified complete before review |
| Distribution boundary | Source documents and local processing records were withheld; public URLs only |

## Concise Research Notes

### Problem

Event cameras emit sparse, asynchronous brightness-change events, but many human-pose systems densify them into frames or require grayscale images. The paper argues that this discards the event stream's computational advantage and leaves event-only 3D pose tracking underexplored.

### Method

The authors convert events into binary sparse voxel grids, extract spike features with SEW-ResNet, and fuse the entire space-time tensor with a Spiking Spatiotemporal Transformer. The attention mechanism uses normalized Hamming similarity between binary spike queries and keys rather than dot products; a real-valued value branch improves accuracy at a small modeled energy cost. Average pooling and three linear heads regress SMPL pose, shape, and global translation for every time step.

### Evidence and Results

On the real MMHPSD test set at `T=8`, the proposed 47.7M-parameter model reports 9.4G FLOPs, modeled energy of 0.0083 J, MPJPE 107.2 mm, pelvis-aligned MPJPE 58.7 mm, and PA-MPJPE 44.1 mm. At `T=64`, it reports 63.4G FLOPs, 0.058 J, and errors of 111.7/61.9/45.7 mm. The authors summarize this as using at most 19.1% of the FLOPs and about 3.6% of the modeled energy of selected ANN-based event-pose systems.

The paper introduces SynEventHPD: 9,197 synthetic streams, 47 subjects, and 45.72 hours drawn from EventH36M, EventAMASS, EventPHSPD, and SynMMHPSD. For the proposed model, real-only training reports 107.2/58.7/44.1 mm, real-plus-synthetic reports 103.1/58.4/43.8 mm, and adding domain adaptation reports 99.2/55.8/42.9 mm. Synthetic-only training is weaker, exposing a real/synthetic domain gap.

The main attention ablation reports pelvis-aligned MPJPE 58.7 for normalized Hamming similarity versus 62.8 for scaled dot product, 61.7 for normalized Euclidean similarity, and 62.3 for normalized Manhattan similarity. Real-valued values plus Hamming score 58.7 at 0.00826 J, compared with binary values plus dot product at 62.0 and 0.00806 J.

### Limitations

Event cameras provide little evidence for stationary body parts and only 2D measurements for a 3D task. Occlusion and missing temporal context remain visible failure modes. The energy figures are analytical estimates derived from MAC/AC operation counts and 45 nm per-operation constants, not measured system power. Experiments use a single A100 for training, but no repeated-seed uncertainty, wall-clock latency, or neuromorphic-hardware measurements are reported. The synthetic dataset improves the reported real test split only after mixed training and domain adaptation; broader cross-camera and population generalization is unestablished.

### Implementation Relevance

The reusable design is not limited to pose tracking: preserve sparse observations, use a representation-aware similarity function, aggregate evidence bidirectionally across time, and keep explicit structured priors for underdetermined outputs. A credible product should also expose spike density, occlusion, temporal-support, and calibration signals rather than returning an unqualified pose.

### Reviewer Interpretation

The strongest evidence supports an accuracy/efficiency tradeoff within the paper's evaluation setup, not a universal energy claim. Normalized Hamming attention is compelling because its binary-feature geometry matches the spike representation and because the ablation is direct. The remaining question is whether this advantage survives physical sensor noise, hardware kernels, domain shift, and severe occlusion.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Boundary |
|---|---|---|---|
| E1 | Full arXiv PDF and HTML, including method, Tables I-V, Figures 2-10, discussion, and appendix references | Architecture, datasets, metrics, ablations, limitations | Author-reported results; not independently reproduced |
| E2 | Visual inspection of PDF pages 5, 6, 9, 11, and 13 | Pipeline, Hamming-attention diagram, main results table, synthetic-data evidence, failure cases | Still-page inspection cannot prove temporal quality |
| E3 | arXiv metadata and version history | Title, authors, dates, version, acceptance comment, DOI | Metadata does not validate results |
| E4 | Official implementation repository README and visible tree | Code/test surface, dependency guidance, pretrained-model and sample links, MIT license | Repository was not executed; no release artifact was verified |
| E5 | Private integrity and process records | Uniform selection, dedup, PDF/HTML validation, bounded repair | Local paths and source files are intentionally withheld |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-FEMOT Tracking/femot_tracking_manuscript.md`
   - Relevance: FEMOT studies synchronized frame/event multi-object tracking with multimodal fusion and temporal association memory, providing the closest Black Lake bridge for event-camera tracking and long-range identity continuity.
   - Source basis: The DEP reviews `arXiv:2606.14094` and the official FEMOT repository, reporting benchmark scale, FEMOTR design, tracking metrics, and event-accumulation limitations.

2. `.lake-data/DEP-E/DEP-E-20260721-Hallo4 Portrait Motion/hallo4_portrait_motion_manuscript.md`
   - Relevance: Hallo4 preserves fast audio/skeleton motion through temporal-to-channel modulation and evaluates motion-conditioned human rendering, complementing the selected paper's bidirectional temporal fusion of pose evidence.
   - Source basis: The DEP reviews `arXiv:2505.23525v4`, its official repository, temporal modulation ablations, preference training, and motion-quality tradeoffs.

3. `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md`
   - Relevance: CAR uses SMPL and explicit geometric priors to infer a clothed 3D human from sparse, occluded visual evidence, directly connecting to the selected paper's SMPL regression and underdetermined 2D-to-3D pose problem.
   - Source basis: The DEP reviews `arXiv:2304.03903v1`, CVPR 2023 material, source TeX, and the official CAR repository.

## Synthesis Note

### Concept Bridge

The four works separate a difficult perception-and-motion system into complementary evidence channels. Spiking Pose Tracking provides sparse event sensing, bidirectional temporal attention, and structured pose regression. FEMOT shows that event streams benefit from calibrated multimodal fusion and explicit temporal association memory. Hallo4 treats high-frequency motion as information that can be lost by temporal compression. CAR demonstrates that SMPL and canonical geometry priors stabilize human reconstruction when observations are incomplete.

Together they suggest an evidence-aware human-motion stack: event-native sensing feeds a sparse temporal encoder; association memory decides which history remains trustworthy; motion-preserving conditioning protects fast dynamics; and a structured body prior converts incomplete features into 3D hypotheses. The system should output both the pose and a provenance/confidence record describing event density, temporal support, occlusion, prior dependence, and any frame/skeleton side information.

### Potential Implementations

1. **Sparse multi-view pose tracker**: Fuse multiple event cameras with calibration-aware association memory, then use Hamming attention to aggregate sparse temporal evidence before SMPL or direct-joint regression.
2. **Consent-aware motion-avatar controller**: Drive a user-owned avatar from event-derived pose features while retaining high-frequency skeleton cues through temporal-to-channel modulation and attaching provenance/watermarks.
3. **Occlusion evidence auditor**: Compare event-only, RGB-event, and structured-prior reconstructions, labeling each joint by observed support, temporal support, and prior-driven inference.

### Deeper Relationship Observations

1. Each work treats lost information differently: event sparsity avoids recording static redundancy, FEMOT preserves cross-sensor evidence, Hallo4 protects high-frequency motion across a latent bottleneck, and CAR restores unobserved geometry with explicit priors.
2. Temporal context and geometric priors are substitutes only up to a point; time can recover a briefly occluded joint, while a body prior is still needed when the joint remains unseen or the event stream is silent.
3. Efficiency claims become credible only when representation, memory, and hardware are evaluated together; sparse tensors can lose their advantage if kernels densify attention, retain long histories, or depend on expensive non-spiking regressors.

### Conceptual Similarities

1. All four systems impose structure on an underdetermined task rather than relying on unconstrained end-to-end prediction.
2. All four depend on temporal or canonical alignment so that evidence from different times, sensors, or poses can be compared in a common space.
3. All four expose a precision-versus-efficiency frontier: more views, memory, real-valued features, channel expansion, or refinement can improve quality while increasing compute and operational complexity.

### MVP Implementations with Code Mock-Ups

#### MVP 1: Hamming-Attention Probe

Evaluate binary similarity functions on synthetic spike sequences with controlled sparsity and occlusion.

```python
def normalized_hamming(query, key):
    if len(query) != len(key) or not query:
        raise ValueError("equal non-empty vectors required")
    matches = sum(int(a == b) for a, b in zip(query, key))
    return matches / len(query)

queries = [[0, 0, 0, 0], [1, 0, 1, 0]]
keys = [[0, 0, 0, 0], [1, 1, 0, 0]]
scores = [[normalized_hamming(q, k) for k in keys] for q in queries]
```

#### MVP 2: Joint Evidence Ledger

Track whether each pose joint is supported by current events, temporal memory, or a body prior.

```python
def joint_evidence(event_hits, memory_hits, prior_used):
    ledger = []
    for joint, event_score in event_hits.items():
        temporal = memory_hits.get(joint, 0.0)
        ledger.append({
            "joint": joint,
            "event_support": round(event_score, 3),
            "temporal_support": round(temporal, 3),
            "prior_driven": bool(prior_used.get(joint, False)),
            "review": event_score + temporal < 0.4,
        })
    return ledger
```

#### MVP 3: Multi-Objective Deployment Gate

Reject a model promotion when accuracy, physical energy, latency, or occlusion reliability is missing.

```python
def deployment_gate(metrics):
    required = {"pa_mpjpe_mm", "wall_energy_j", "latency_ms", "occlusion_error_mm"}
    missing = sorted(required - metrics.keys())
    if missing:
        return {"ok": False, "missing": missing}
    limits = {
        "pa_mpjpe_mm": 55.0,
        "wall_energy_j": 0.10,
        "latency_ms": 40.0,
        "occlusion_error_mm": 85.0,
    }
    failed = [name for name, limit in limits.items() if metrics[name] > limit]
    return {"ok": not failed, "failed": failed}
```

### Developer Challenges

1. Implement sparse Hamming attention without silently densifying the space-time tensor, and publish kernel-level memory and energy measurements.
2. Design a calibration and reset policy for association memory so stale identities or poses do not contaminate long event sequences.
3. Make every 3D joint auditable by separating current-event evidence, future/past temporal evidence, and SMPL/prior contribution.

### Author Challenges

1. Evaluate the model on physical neuromorphic or edge hardware with measured energy, end-to-end latency, and sparse-kernel utilization.
2. Release a documented SynEventHPD data card with source licenses, synthesis pipeline, subject/motion coverage, split leakage analysis, and real-domain transfer results.
3. Extend the evaluation to multi-view events and direct 3D-joint output while reporting uncertainty under occlusion, static poses, sensor noise, and cross-camera shift.

## Validation Notes

- Random selection used a uniform `Get-Random` index over 75,777 unique PDF-parent units; selected index 53,213.
- No prior arXiv DEP artifact or same-paper 24-hour marker was found; exclusions and reselections were both zero.
- Source state changed from partial to complete before review. The PDF was at least 10 KB, began with `%PDF-`, ended with `%%EOF`, and matched the bounded repair copy. Full-paper HTML exceeded 5 KB and 2,000 body characters, had a document marker, 43 heading markers, all eight checked paper-structure terms, and a hash distinct from the abstract page.
- Paper claims were cross-checked in extracted full text and visually on architecture, result, synthetic-data, and failure-case pages.
- Experiments, datasets, pretrained models, and physical energy measurements were not rerun.
- No source file, local path, machine name, local timezone, or exact execution timestamp is included.

## Attribution Block

- https://arxiv.org/abs/2303.09681
  - Applies to: Source identity, title, authors, dates, version, acceptance comment, abstract, and public artifact links.
- https://arxiv.org/html/2303.09681
  - Applies to: Full-paper method, experiments, results, limitations, and references; local copy withheld.
- https://arxiv.org/pdf/2303.09681
  - Applies to: Full-paper and visual table/figure review; local copy withheld.
- https://arxiv.org/e-print/2303.09681
  - Applies to: Locally retained source-package provenance; source archive withheld.
- https://doi.org/10.48550/arXiv.2303.09681
  - Applies to: Persistent arXiv identity.
- https://github.com/JimmyZou/HumanPoseTracking_SNN
  - Applies to: Official implementation availability, dependency guidance, test surface, and license observation.
- `.lake-data/DEP-E/DEP-E-20260720-FEMOT Tracking/femot_tracking_manuscript.md`
  - Applies to: Event-camera tracking, fusion, temporal association, and benchmark bridge; source basis `https://arxiv.org/abs/2606.14094`.
- `.lake-data/DEP-E/DEP-E-20260721-Hallo4 Portrait Motion/hallo4_portrait_motion_manuscript.md`
  - Applies to: Skeleton-conditioned temporal-motion and representation bridge; source basis `https://arxiv.org/abs/2505.23525`.
- `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md`
  - Applies to: SMPL, sparse-evidence reconstruction, occlusion, and structured-prior bridge; source basis `https://arxiv.org/abs/2304.03903`.
- Source files and private integrity records
  - Applies to: Source-integrity and selection verification only; all were withheld locally and none were uploaded.
