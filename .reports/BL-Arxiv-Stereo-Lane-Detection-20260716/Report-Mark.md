# Report-Mark: Stereo Lane Detection

## Review Status

- Paper: arXiv:1808.09128v1; IEEE IST 2018
- Source: verified complete PDF and approved ar5iv full-paper rendering
- Review depth: algorithm, equations, figures, Tables I-II, runtime, conclusion, publication/code availability, and related DEP synthesis
- Reproduction: not performed
- Source distribution: withheld locally; no source upload

## Source Metadata

| Field | Value |
|---|---|
| Title | Multiple Lane Detection Algorithm Based on Optimised Dense Disparity Map Estimation |
| Authors | Han Ma; Yixin Ma; Jianhao Jiao; M. Usman Maqbool Bhutta; Mohammud Junaid Bocus; Lujia Wang; Ming Liu; Rui Fan |
| Identifier | arXiv:1808.09128v1 |
| Publisher DOI | 10.1109/IST.2018.8577122 |
| arXiv DOI | 10.48550/arXiv.1808.09128 |
| Date / venue | submitted 2018-08-28; 2018 IEEE International Conference on Imaging Systems and Techniques |
| Subject | Computer Vision and Pattern Recognition |
| Paper-linked code | No official implementation identified |

## Concise Research Notes

The method uses temporal coherence to reduce dense stereo search. BRISK matches initialize a sparse v-disparity road profile; RANSAC fits a quadratic. Dense disparity from frame `t_n` is then optimized with dynamic programming, fit as the road model, and used to limit row-wise disparity search at `t_n+1` to plus/minus three disparity values around the prediction.

Lane extraction adds bilateral filtering, disparity-based road/obstacle segmentation, Sobel edges, dynamic-programming vertical and horizontal vanishing-point paths, and a likelihood score aligning edge orientation with row-specific vanishing-point direction. It builds substantially on the authors' prior dense-vanishing-point detector.

Across six selected KITTI sequences, the paper counts 3,724 lanes. The new system reports 10 incorrect detections and 14 misses; the prior method reports 14 and 33. This yields approximately 99.36% versus 98.74% under the paper's counted-lane denominator, a 0.62-point gain. Exact sequence IDs and annotation protocol are absent.

The disparity substage is reported 37% faster, while the entire C implementation takes 0.21 seconds per 1242-by-375 frame on a single i7-8700K thread. The paper correctly says it is not real time. Embedded/parallel speed is proposed rather than demonstrated.

## Evidence and Attribution

| ID | Basis | Supports | Boundary |
|---|---|---|---|
| R1 | Full v1 paper | Method, equations, figures, conclusion | Author-reported; no rerun |
| R2 | Tables I-II | Lane counts and comparison | Non-standard/manual denominator; selected sequences |
| R3 | Runtime paragraph | 37% substage reduction and 0.21-second total | No raw trials, variance, tails, or energy |
| R4 | Publisher and availability checks | IST DOI and no identified official code | Time-bounded search |
| R5 | Three DEP manuscripts | Calibration, embedded field vision, control safety | Conceptual context only |
| R6 | Process records | Draw, dedup, repair, cache, source gate | Operational evidence |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - spatial/temporal calibration provenance needed by stereo disparity.
2. `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` - field-lighting failures, compact vision, and embedded evidence gaps.
3. `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` - downstream driving/control latency, safety constraints, and simulation-to-road boundaries.

## Synthesis Note

### Concept Bridge

The lane paper uses temporal road geometry to reduce perception cost; iKalibr shows that such geometry is meaningful only when sensor frames and timestamps are trustworthy; HSD FTI-FDet shows that field robustness and embedded resource claims require direct measurement; Self Learned IDC shows that perception uncertainty and latency become system hazards when consumed by control. The bridge is an offline evidence pipeline that tests calibration, temporal propagation/reset, lane metrics, resource tails, and abstention before any integration decision.

### Potential Implementations

1. **Temporal disparity regression harness** - replay frozen sequences with road-grade, occlusion, dropped-frame, and calibration fault injection.
2. **Fixed-denominator lane evidence card** - sequence IDs, attempted frames/instances, false/missed lanes, geometry, jitter, resets, and confidence intervals.
3. **Embedded perception Pareto profiler** - accuracy, median/P95/P99 latency, memory, energy, and thermal behavior for full versus propagated stereo search.

### Deeper Relationship Observations

1. iKalibr turns stereo calibration from a static assumption into an evidence dependency; temporal disparity propagation can amplify small spatial or timing errors across frames.
2. HSD FTI-FDet and the lane detector both report efficiency relative to a baseline while leaving the intended embedded platform as future work, so workstation gains cannot be treated as field readiness.
3. Self Learned IDC makes the denominator problem operational: a small rate of hallucinated or missed lanes may dominate safety even when average perception accuracy appears high.

### Conceptual Similarities

1. Each artifact relies on structured state—calibration parameters, road profiles, spatial features, or traffic participants—to constrain a hard inference problem.
2. Each needs component-level diagnostics and provenance because endpoint performance alone cannot identify hidden assumption failures.
3. Each distinguishes promising simulation/workstation evidence from the stronger evidence required for real physical control.

### MVP Implementations with Code Mock-ups

1. **Count contract**

```python
def lane_rate(total: int, incorrect: int, missed: int) -> float:
    if total <= 0 or min(incorrect, missed) < 0 or incorrect + missed > total:
        raise ValueError("invalid lane-count denominator")
    return (total - incorrect - missed) / total
```

2. **Temporal reset gate**

```python
def temporal_route(inliers: int, residual: float, frame_gap: int) -> str:
    if frame_gap != 1 or inliers < 20 or residual > 2.5:
        return "reset_and_review"
    return "propagate_candidate"
```

3. **Latency budget validator**

```python
def validate_latency(p99_ms: float, budget_ms: float) -> None:
    if p99_ms <= 0 or budget_ms <= 0:
        raise ValueError("positive timing values required")
    if p99_ms > budget_ms:
        raise RuntimeError("tail latency exceeds declared budget")
```

### Developer Challenges

1. Preserving stereo coordinate, rectification, disparity, road-model, vanishing-point, and lane-topology conventions across a temporal pipeline.
2. Producing deterministic resets and fault injection without leaking restricted road imagery or silently changing evaluation denominators.
3. Profiling tail latency and energy accurately on embedded hardware while controlling warm-up, synchronization, throttling, and workload variation.

### Author Challenges

1. Release exact KITTI sequence IDs, annotations, calibration, source code, environment, and per-frame outputs under a usable license.
2. Evaluate temporal failure/recovery, calibration drift, adverse conditions, modern baselines, uncertainty, and fixed-denominator geometry metrics.
3. Demonstrate the parallel/embedded hypothesis with complete accuracy-resource measurements and a safety-oriented abstention interface.

## Validation Notes

- Random draw: index 15,402 from 75,776 unique units; first draw; zero exclusions/reselections.
- Dedup: no matching ID, either DOI, title, slug, artifact, memory entry, companion entry, or 24-hour marker.
- Source state: valid PDF plus missing full HTML was `partial`; official HTML 404; approved ar5iv repair passed; final `complete`.
- PDF: 5,980,379 bytes, `%PDF-`, trailing `%%EOF`.
- HTML: 292,496 bytes, 31,447 body characters, two document markers, 26 heading/section markers, five structure terms.
- Cache: miss to `cached` in 0.379 seconds; PDF/HTML text 24,083/31,431 bytes; no source bundle.
- Availability: publisher DOI verified; no official code identified.
- Artifact validation: schema, headings, exact counts, JSON, public-safety, and allowlist checked before submission.
- Source-upload rule: PDF, HTML, metadata, caches, extracted text, imagery, and archive records remain local.

## Attribution Block

- Primary source: Han Ma; Yixin Ma; Jianhao Jiao; M. Usman Maqbool Bhutta; Mohammud Junaid Bocus; Lujia Wang; Ming Liu; Rui Fan, *Multiple Lane Detection Algorithm Based on Optimised Dense Disparity Map Estimation* (2018).
- arXiv: https://arxiv.org/abs/1808.09128v1
- Full-paper rendering: https://ar5iv.labs.arxiv.org/html/1808.09128
- PDF: https://arxiv.org/pdf/1808.09128
- Publisher DOI: https://doi.org/10.1109/IST.2018.8577122
- arXiv DOI: https://doi.org/10.48550/arXiv.1808.09128
- Artifact nature: independent source-grounded review; author-reported values were not reproduced.
- Source handling: original documents and extraction/cache material were withheld locally; no source file was uploaded.
