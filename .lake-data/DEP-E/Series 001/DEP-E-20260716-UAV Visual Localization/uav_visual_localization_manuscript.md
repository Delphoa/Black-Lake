---
title: "UAV Visual Localization - DEP-E"
generated_at: "2026-07-16"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of hierarchical UAV-to-satellite image matching for absolute visual localization."
source_status: "verified complete PDF and official full-paper HTML inspected; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv:2506.09748v1 and bounded public availability checks inspected through 2026-07-16"
primary_url: "https://arxiv.org/abs/2506.09748v1"
stable_identifier: "arXiv:2506.09748v1; DOI 10.48550/arXiv.2506.09748"
confidence_summary: "High for method and table transcription; medium for comparative conclusions; low for deployment generality."
safety_scope: "offline localization research, evaluation, and human-supervised prototyping; no autonomous flight authorization"
distribution_notes: "Original paper files, metadata HTML, extracted text, cache records, and archive records remain local and are not redistributed."
---

# UAV Visual Localization - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | Usage Notes | Status |
|---|---|---|---|---|---|---|---|
| S1 | Hierarchical Image Matching for UAV Absolute Visual Localization via Semantic and Structural Constraints | Primary metadata | arXiv record | 2506.09748v1; DOI 10.48550/arXiv.2506.09748 | https://arxiv.org/abs/2506.09748v1 | Identity, dates, authors, subjects, license | Inspected |
| S2 | Complete paper | Primary artifact | PDF and official full-paper HTML | v1, 2025-06-11 | https://arxiv.org/pdf/2506.09748; https://arxiv.org/html/2506.09748v1 | Verified local copies withheld | Inspected in full |
| S3 | iKalibr Calibration | Related DEP | Manuscript | DEP-E-20260714 | `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` | Calibration and observability context | Inspected |
| S4 | SSP Oriented Detection | Related DEP | Manuscript | DEP-E-20260711 | `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` | Aerial spatial-prior context | Inspected |
| S5 | AFIDAF Vision Filters | Related DEP | Manuscript | DEP-E-20260715 | `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` | Hierarchical feature and efficiency context | Inspected |
| S6 | Black Lake README | Repository authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Filing and source-locality contract | Inspected |

The authors are Xiangkai Zhang, Xiang Zhou, Mao Chen, Yuchen Lu, Xu Yang, and Zhiyong Liu. The record lists Computer Vision and Pattern Recognition as primary and Robotics as secondary. It reports eight pages and six figures under the arXiv non-exclusive distribution license. No publisher venue, separate publisher DOI, official implementation, trained weights, or usable CS-UAV release locator was identified. The paper's claimed public dataset URL is the literal placeholder `[link]`.

## Evidence Ledger

| ID | Source | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|
| E1 | S1-S2 | Metadata, abstract, full method, figures, equations, Tables I-III, conclusion | Identity, mechanism, reported evaluation | High for reporting | No reproduction |
| E2 | S2, Section III | Retrieval, DINOv2 features, 4D correlation, SoftMNN, SASCM, fine matcher, RANSAC | Pipeline reconstruction | High | Some implementation details and hyperparameters omitted |
| E3 | S2, Table I | AerialVL overall and module-level comparisons | Reported benchmark performance | High for transcription | Some prior-work rows are sparse and unreproduced |
| E4 | S2, Table II | CS-UAV module-level comparison | Self-collected-dataset performance | High for transcription | Dataset release unavailable; possible collection-specific effects |
| E5 | S2, Table III | Retrieval-only and no-SASCM ablation | Component contribution | High for transcription | No uncertainty, multi-seed, or latency ablation |
| E6 | S2, evaluation protocol | Success below 25 m; drift above 50 m; MLE on non-drift segments | Metric interpretation | High | 25-50 m band and drift-excluded mean complicate comparison |
| E7 | S3-S5 | Calibration, spatial-prior, hierarchical feature evidence | Cross-DEP synthesis | Medium | Conceptual context does not validate this method |
| E8 | Process records | Uniform random draw, dedup scan, source repair, cache extraction | Workflow validity | High | Operational rather than scientific evidence |

## Executive Summary

The paper targets UAV absolute visual localization when GNSS is unavailable. Given a downward-looking UAV image and a reference satellite map, the system must identify the corresponding map region and estimate the UAV's absolute position despite cross-source viewpoint, sensor, illumination, season, and appearance differences. The proposed answer is a three-stage hierarchy: retrieve a candidate satellite region, establish semantic/structural coarse correspondences, then refine local matches and estimate a homography.

The coarse module is the central contribution. It extracts dense DINOv2 features from the UAV and satellite images, forms a four-dimensional cosine-similarity tensor, applies a Soft Mutual Nearest Neighbor filter, and processes the result with a symmetric Semantic-Aware and Structure-Constrained Matching module. A hard assignment yields region correspondences under weak supervision. A lightweight convolutional fine matcher then produces keypoints, reliability scores, descriptors, mutual-nearest-neighbor matches, and a RANSAC homography that maps the UAV-image center into satellite coordinates.

Reported averages favor the full pipeline. On AerialVL, success rises from 0.41 for retrieval alone to 0.68 without SASCM and 0.81 with the complete method; reported mean localization error falls from 28.11 m to 22.14 m and 18.73 m. On CS-UAV, the same sequence is 0.54, 0.72, and 0.93 success, with mean error 24.20 m, 21.53 m, and 17.71 m. In module comparisons, the full approach also exceeds SIFT, SuperPoint, and Deep-LK on both datasets.

The strongest defensible conclusion is that semantic/structural coarse correspondence plus learned fine matching improves the paper's evaluated retrieval-localization pipeline. Deployment conclusions remain uncertain. Mean localization error excludes segments beyond the 50 m drift threshold, the self-collected CS-UAV dataset cannot be accessed through the paper, there is no official code or timing breakdown, and evaluation is geographically narrow. A safety-relevant implementation should publish drift-inclusive distributions, calibrated confidence, target-device resource costs, map-age and domain-shift tests, and an explicit abstention interface.

## Detailed Summary

### Problem and Operating Setting

Absolute localization estimates position in a global reference frame. In the paper's setting, a UAV image is matched to a geo-referenced satellite map without depending on relative localization. This is attractive in GNSS-denied environments because errors do not need to accumulate through an odometry chain. It is also difficult: aerial images and satellite imagery can differ in resolution, camera model, angle, season, time, illumination, construction state, and visible object layout.

Traditional local features can fail when low-level textures change across sources. Pure global retrieval may choose a plausible region but lacks enough geometric precision. The paper therefore divides the task into progressively narrower evidence: broad appearance for retrieval, semantic and structural correspondence for coarse alignment, and local convolutional evidence for final geometry.

### Retrieval Stage

The satellite map is cropped into candidate images. The paper describes an off-the-shelf retrieval component that computes global descriptors and uses cosine similarity to select the top-ranked candidate. This stage is necessary for tractability but not sufficient for precise localization. The retrieval-only ablation quantifies that boundary: it succeeds on less than half of AerialVL trajectories on average and just over half of CS-UAV under the stated threshold.

Retrieval errors also constrain every downstream stage. If the correct region is not present in the selected crop, more sophisticated correspondence cannot recover it. A production design should therefore retain top-k candidates or expose retrieval uncertainty rather than silently committing to top-1.

### Semantic and Structural Coarse Matching

The UAV and satellite inputs pass through DINOv2 to produce dense feature maps. Pairwise cosine similarities form a 4D correlation tensor whose axes represent locations in both images. SoftMNN downweights ambiguous matches unless they are mutually strong from both directions. This is meant to suppress repetitive or accidental similarity.

SASCM processes the correlation tensor with three layers of four-dimensional convolution followed by ReLU. Symmetric processing exchanges the two image roles and combines evidence so the relation is less dependent on query/reference ordering. Hard assignment converts the refined correlation into coarse region matches. Training is weakly supervised: the method uses the expected central region of the UAV view and its corresponding satellite region rather than dense point-level cross-source labels.

The coarse stage's value is conceptual as well as empirical. Foundation-model features supply semantic invariance; 4D convolutions inspect correspondence neighborhoods; symmetry and mutuality impose structural consistency. None alone proves correctness. Together they encode an inductive bias that true correspondences should be semantically compatible and locally coherent across both views.

### Fine Matching and Position Estimation

The fine matcher is a lightweight convolutional network that extracts multi-scale image features and predicts keypoint, reliability, and descriptor information. Mutual nearest neighbors select descriptor correspondences. RANSAC estimates a homography robustly by rejecting inconsistent matches. The UAV image center is mapped through that homography into satellite coordinates, which are then converted into an absolute position.

The coarse and fine networks are trained separately because hard correspondence selection and the matching pipeline are not fully differentiable and joint optimization was unstable. Fine-matcher training uses synthetic transformations of UAV-Visloc images. Known geometric and photometric transformations create pixel-level supervision, including rotation, scaling, and color jitter.

This synthetic strategy provides cheap correspondence labels, but it may not reproduce all UAV-to-satellite differences. Real cross-source changes include map age, height, oblique structure, shadows, occlusion, vegetation, construction, and sensor processing. The gap should be tested explicitly.

### Datasets and Protocol

UAV-Visloc supplies training data: 6,742 UAV images from 11 locations in China. AerialVL supplies public evaluation data with 11 flight sequences in Qingdao ranging from 3.7 to 11 km. CS-UAV is self-collected using a DJI Mavic 2 across nine Changsha trajectories averaging about 10 km and spanning urban, rural, and mountainous forest environments with high-precision onboard GPS.

A localization is counted as successful below 25 m error and as drift above 50 m. Mean localization error is computed on non-drift segments. That last definition is crucial. A low mean can coexist with many catastrophic errors if those errors are removed before averaging. The paper reports success and MLE, but a deployment evaluation should also publish drift fraction, median, percentiles, maximum, and an all-attempt fixed-denominator loss.

### Reported Results

On AerialVL, the complete method reports average success 0.81 and MLE 18.73 m. SIFT reports 0.41/28.09 m, SuperPoint 0.48/26.42 m, and Deep-LK 0.48/26.95 m within the paper's pipeline. AerialVL combined baselines appear for only selected trajectories and are copied from prior work because their code is unavailable.

On CS-UAV, the complete method reports 0.93 success and 17.71 m MLE. SIFT reports 0.56/24.21 m, SuperPoint 0.54/24.64 m, and Deep-LK 0.36/29.78 m. The stronger result on a self-collected dataset is promising but should be separated from independent external validation.

Table III compares retrieval only, the full pipeline without SASCM, and the full pipeline. AerialVL improves from 0.41/28.11 m to 0.68/22.14 m to 0.81/18.73 m. CS-UAV improves from 0.54/24.20 m to 0.72/21.53 m to 0.93/17.71 m. This supports a component contribution, though it does not separate DINOv2, SoftMNN, symmetry, 4D convolution depth, and hard assignment individually.

## Key Claims and Evidence

| Claim | Type | Evidence | Assessment | Confidence |
|---|---|---|---|---|
| Hierarchical cross-source matching improves UAV absolute localization. | Author empirical | E3-E5 | Supported in the two evaluated datasets under the stated protocol. | Medium-high |
| Semantic and structural constraints improve coarse matching. | Author empirical/mechanistic | E2, E5 | The no-SASCM ablation supports the full module; internal factors are not isolated. | Medium |
| The approach is robust across challenging conditions. | Author interpretation | E3-E5 | Multiple terrain/lighting cases are included, but regions, devices, seasons, and map ages are narrow. | Medium-low |
| The fine matcher is lightweight. | Author design claim | E2 | Architecture is described, but target-device latency, memory, energy, and component timing are absent. | Low-medium |
| The complete method reaches 0.81/18.73 m on AerialVL and 0.93/17.71 m on CS-UAV. | Author empirical | E3-E5 | Accurately transcribed averages; MLE excludes drift segments. | High for reporting |
| CS-UAV is publicly accessible. | Author availability claim | S2 | Not operationally supported: the inspected URL is `[link]`. | Low |

## Methodology

This review used a source-first, cache-accelerated workflow. Candidate enumeration used `rg --files -g "*.pdf"` over the local archive, treating each PDF parent as one paper unit. A uniform `Get-Random` index selected unit 37,833 from 75,776 unique units, corresponding to 75,777 PDFs. The first draw was eligible, so there were zero exclusions and zero reselections.

Dedup validation checked arXiv ID, DOI, normalized title, slug, prior Arxiv DEP logs, Report-Mark directories, DEP-E manuscripts, the public dedup pointer, automation memory, active repository context, companion-repository context, and same-paper markers within 24 hours. No prior substantive artifact was found.

The selected source initially had a valid full PDF but lacked full-paper HTML, so its state was `partial`. The archive was repaired with one bounded request each for official arXiv full-paper HTML and metadata. The PDF passed size, header, and trailing-EOF checks. The repaired HTML passed size, body-text, document-marker, heading, and paper-structure checks. Local README, provenance, machine-readable summary, and verification report were updated before review opened.

The document-processing extractor then ran `extract-arxiv` in `missing-only` mode against the selected paper unit with the central cache. The cache changed from miss to `cached` in 0.472 seconds. `pypdf` produced 43,965 bytes of PDF text and `html-regex` produced 61,869 bytes of HTML text; no source bundle was collected. Source documents and extraction outputs remain local.

Scientific synthesis inspected the full paper rather than relying on the abstract. Claims were tied to sections, equations, tables, and availability evidence. Related DEP entries were selected only after their manuscripts were inspected for concrete overlap. No model, dataset, or code was executed.

## Scope, Constraints, and Assumptions

- Scope covers the paper's visual-localization mechanism, reported experiments, implementation relevance, evidence quality, and three related Black Lake entries.
- Reported numbers are author results, not independently reproduced measurements.
- The review assumes the arXiv v1 paper is the authoritative public scientific record available at the cutoff.
- “Robust” is interpreted only within the evaluated sequences and thresholds, not as a safety guarantee.
- Mean localization error is preserved as defined by the paper and explicitly labeled drift-excluding.
- No usable official implementation, weights, or CS-UAV release was found in bounded checks; absence from those checks is not proof that none will ever exist.
- Safety discussion is reviewer-added because the paper does not establish a flight-control assurance case.

## Observations

- Coarse-to-fine role separation is well matched to the problem: retrieval limits search, semantic structure bridges source gaps, and local geometry supplies precision.
- The success gains in Table III are large enough to justify component-level reproduction, but SASCM's internal mechanisms need finer ablation.
- CS-UAV outperforms AerialVL for the full method, which could reflect favorable data conditions as well as genuine robustness.
- Top-1 retrieval creates a hidden single point of failure; top-k recovery and retrieval recall are not fully exposed.
- Homography-based center mapping assumes a geometry that may degrade with relief, oblique views, tall structures, or rolling-shutter effects.
- “Lightweight” is not quantified at system level. DINOv2, 4D correlation, retrieval, and RANSAC all contribute operational cost.
- The 25 m success threshold may be appropriate for some mission contexts and unsafe for others. Task-specific tolerances matter.
- The missing CS-UAV link weakens reproducibility more than a prose limitation because independent evaluation cannot reconstruct the primary self-collected benchmark.

## Considerations

### Evaluation Integrity

Publish all-attempt denominators. At minimum include success rate, drift rate, median, P90/P95/P99, conditional MLE, fixed-denominator clipped loss, and time-to-recovery after failure. Report confidence intervals across flights and geographic holdouts rather than treating frames as independent.

### Operational Safety

An absolute-localization estimate should include uncertainty and evidence quality. Low retrieval margin, sparse coarse matches, poor spatial coverage, unstable homography, or large RANSAC residuals should trigger abstention. The system should not authorize control transitions by itself.

### Privacy and Dual Use

UAV imagery can expose people, private property, and sensitive infrastructure. Data governance should minimize capture, restrict access, define retention, and audit downstream use. GNSS-denied localization also has dual-use implications; deployment review should consider legal authority and mission boundaries.

### Reproducibility

Release dataset cards, checksums, train/test geography, map acquisition dates, camera calibration, preprocessing, exact retrieval model, DINOv2 variant, matcher configuration, seeds, weights, and a pinned environment. A literal placeholder is not an availability artifact.

## Strengths

- The pipeline expresses a clear hierarchy aligned with global-to-local uncertainty.
- Semantic features and correspondence-space structure directly address cross-source appearance differences.
- Two evaluation datasets include long flight sequences and varied terrain.
- Component ablation demonstrates that both learned matching and SASCM contribute under the paper's metrics.
- Comparisons place SIFT, SuperPoint, and Deep-LK inside a common retrieval pipeline.
- The method avoids depending on relative localization, limiting cumulative odometry drift in principle.

## Weaknesses

- CS-UAV is not reproducibly accessible from the paper.
- No official code, trained weights, or pinned implementation is identified.
- MLE excludes drift segments, obscuring catastrophic errors in the average.
- No uncertainty intervals, multi-seed variation, or statistical tests are reported.
- Evaluation is geographically narrow and does not isolate seasons, map age, devices, altitude, weather, or viewpoint.
- The “lightweight” claim lacks latency, memory, throughput, energy, and embedded-hardware measurements.
- The ablation does not isolate each SASCM mechanism or DINOv2 dependency.
- Homography assumptions and terrain/structure failure cases are not characterized quantitatively.

## Potential Improvements

1. Release CS-UAV and code with checksums, license, dataset card, flight/map timestamps, split geography, and exact environment.
2. Add drift-inclusive and fixed-denominator metrics with trajectory bootstrap intervals and recovery behavior.
3. Evaluate leave-city-out, leave-season-out, leave-device-out, map-age, altitude, weather, oblique-view, and structural-change splits.
4. Report retrieval recall@k and propagate multiple candidates through coarse/fine matching.
5. Calibrate an abstention score from retrieval margin, mutual-match density, spatial coverage, homography residuals, and temporal consistency.
6. Profile each stage on workstation and embedded flight hardware, including peak memory and energy.
7. Ablate DINOv2 backbone/scale, SoftMNN, symmetric processing, 4D-convolution depth, hard assignment, and synthetic transformation families.
8. Test non-planar and rolling-shutter cases and compare homography with geometry models that account for terrain relief.
9. Compare stronger modern cross-view retrieval and matching baselines under the same released protocol.
10. Add privacy, misuse, geographic-bias, and operational-safety documentation.

## Potential Implementations

### Localization Evidence Card

A versioned record for every evaluation run containing source/map vintages, geographic split, retrieval recall, success/drift distributions, uncertainty calibration, hardware profile, and withheld-source policy. This makes denominator changes and dataset leakage visible.

### Confidence-Gated Offline Localizer

An offline research service that returns candidate position, confidence, diagnostic evidence, and `abstain` rather than only coordinates. It would reject low retrieval margin, insufficient spatial match coverage, degenerate homography, or excessive residuals.

### Cross-Region Regression Harness

A deterministic benchmark that replays authorized flight sequences against frozen map vintages, evaluates unseen cities/seasons/devices, and emits drift-inclusive reports. It would store only public-safe metrics and provenance, not imagery.

## Three Ways to Exercise This Research

1. **Synthetic geometry replay** - Objective: validate coarse/fine mechanics on generated planar scenes; inputs: synthetic texture/semantic regions and known homographies; method: compare retrieval-only, no-SASCM, and full stages under appearance transforms; output: match overlays and fixed-denominator error tables; success: known mappings recover within declared tolerance; stop: halt on nondeterminism or coordinate ambiguity.
2. **Authorized cross-domain benchmark** - Objective: measure generalization; inputs: consented flight sequences, frozen satellite-map vintages, and geography-held-out splits; method: vary season, altitude, camera, and map age; output: success, drift, percentile error, calibration, and failure taxonomy; success: predeclared performance and confidence targets hold; stop: no control use and halt if privacy or split provenance is incomplete.
3. **Target-device profiling** - Objective: test the “lightweight” claim; inputs: pinned models and representative workstation/embedded devices; method: time retrieval, DINOv2, 4D correlation, fine matching, and RANSAC separately; output: latency, peak memory, energy, and accuracy Pareto curves; success: a declared mission budget is met without hidden fallback; stop: halt on thermal throttling, missing synchronization, or unpinned software.

## Example MVP Product

### Evidence-Gated Localization Auditor

- **User**: robotics researchers and safety reviewers evaluating an offline visual-localization build.
- **Problem**: headline success/MLE values hide drift, domain shift, confidence, and device cost.
- **Input**: public-safe run manifests and metrics produced from authorized local imagery and frozen map data.
- **Core flow**: validate provenance; ingest per-attempt candidates and diagnostics; compute fixed-denominator errors; calibrate abstention on a held-out split; render trajectory, domain, and resource summaries.
- **Output**: a signed Markdown/JSON evidence card with success, drift, error percentiles, calibration, map/data vintages, and stage timings.
- **Architecture**: local adapters, schema validator, metric engine, calibration module, immutable provenance ledger, and report renderer.
- **Safety boundary**: analysis only; it neither stores source imagery in public outputs nor sends navigation commands.
- **MVP success**: the same frozen inputs reproduce the report; every coordinate has a denominator and provenance; withheld-source checks pass.
- **Non-goals**: autonomous flight, covert surveillance, real-time weapons guidance, or claims of universal robustness.

Illustrative contract:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class LocalizationAttempt:
    error_m: float
    retrieval_margin: float
    inliers: int
    residual_px: float

def evaluate(attempt: LocalizationAttempt) -> dict:
    drift = attempt.error_m > 50.0
    confidence_ok = (
        attempt.retrieval_margin >= 0.10
        and attempt.inliers >= 12
        and attempt.residual_px <= 3.0
    )
    return {
        "success_25m": attempt.error_m < 25.0,
        "drift_50m": drift,
        "route": "review" if drift or not confidence_ok else "candidate_only",
    }
```

The thresholds are placeholders requiring calibration. `candidate_only` means an estimate may enter further evaluation; it does not authorize control.

## Related Research and Reading

| Entry | Relationship | Source Basis | Boundary |
|---|---|---|---|
| iKalibr Calibration | Reliable localization depends on spatial/temporal calibration, excitation observability, and provenance upstream of perception. | `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` | Calibration does not validate cross-view matching. |
| SSP Oriented Detection | Both use explicit spatial/structural constraints in aerial or remote-sensing imagery and face brittle geometry under overlap, low contrast, and scene complexity. | `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` | Different task and supervision regime. |
| AFIDAF Vision Filters | Both separate local/global visual roles in hierarchical feature pipelines and require direct hardware/robustness measurement. | `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` | AFIDAF does not test localization or DINOv2 matching. |

## Source References

1. Zhang, Xiangkai; Zhou, Xiang; Chen, Mao; Lu, Yuchen; Yang, Xu; Liu, Zhiyong. “Hierarchical Image Matching for UAV Absolute Visual Localization via Semantic and Structural Constraints.” arXiv:2506.09748v1, 2025. https://arxiv.org/abs/2506.09748v1
2. Full-paper HTML: https://arxiv.org/html/2506.09748v1
3. PDF: https://arxiv.org/pdf/2506.09748
4. DOI: https://doi.org/10.48550/arXiv.2506.09748
5. Related DEP: `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md`
6. Related DEP: `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md`
7. Related DEP: `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md`

## Appendix

### Workflow Provenance

- Candidate set: 75,777 PDFs across 75,776 unique parent units.
- Uniform draw: zero-based index 37,833; accepted first draw.
- Dedup: no substantive match by identifier, DOI, normalized title, slug, artifact scan, memory, or recent marker.
- Initial source class: `partial` because the PDF was valid and full-paper HTML was missing.
- Repair: official full-paper and metadata HTML fetched once; no ar5iv fallback needed.
- Final source class: verified `complete` after PDF and full-HTML gates passed.
- Cache: miss to `cached`, `missing-only`, using `pypdf` and `html-regex`.
- Redistribution: no PDF, HTML, metadata, source archive, cache, extracted text, imagery, model, or dataset was deposited.

### Metric Interpretation Note

Let `e_i` be position error for attempt `i`. The paper's success rate counts `e_i < 25 m`; drift identifies `e_i > 50 m`; reported MLE averages only non-drift segments. A fixed-denominator supplement should retain all attempts, for example reporting the empirical distribution of `e_i`, drift rate, and a predeclared clipped loss. This is a reviewer recommendation, not a claim that the paper's values are incorrect.
