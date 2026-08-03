# Report-Mark: Vid2Curve Reconstruction

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Vid2Curve: Simultaneous Camera Motion Estimation and Thin Structure Reconstruction from an RGB Video* |
| Authors | Peng Wang; Lingjie Liu; Nenglun Chen; Hung-Kuo Chu; Christian Theobalt; Wenping Wang |
| Primary identity | arXiv:2005.03372v3 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2005.03372 |
| Published DOI | https://doi.org/10.1145/3386569.3392476 |
| Venue | ACM Transactions on Graphics 39(4), Article 132; SIGGRAPH 2020 |
| Dates | Submitted 2020-05-07; revised 2020-05-20; published 2020 |
| Primary URLs | https://arxiv.org/abs/2005.03372; https://arxiv.org/pdf/2005.03372; https://ar5iv.labs.arxiv.org/html/2005.03372; https://totoro97.github.io/projects/vid2curve/ |
| Official implementation | https://github.com/Totoro97/Vid2Curve at `47c379dec5cca2e2de123a392e0b1f93ceb1048a` |
| License and distribution | The paper and publisher terms apply to the manuscript; the implementation exposes GPL-3.0. Original source files were inspected locally and were not redistributed. |
| Source-integrity status | Verified complete after bounded repair: full PDF, full-paper HTML fallback, metadata HTML, and TeX/source package; zero partial files |
| Review status | Complete paper and all 12 rendered pages inspected; implementation inspected but not built; experiments not run |

## Concise Research Notes

### Problem and Contribution

Vid2Curve reconstructs objects made from thin tubular elements, such as wire sculptures, baskets, cables, and branches, from a handheld RGB video. Conventional feature-based structure-from-motion struggles because these objects may be nearly textureless, only a few pixels wide, and heavily self-occluding. The paper's central contribution is a curve-first pipeline that estimates camera extrinsics and a connected 3D curve network together, then converts the network into a swept surface.

The pipeline has three stages. Preprocessing segments each frame and thins the foreground into one-pixel-wide skeletal curves. Phase I initializes from two sufficiently separated, low-occlusion frames, builds a tree-like curve graph, then progressively adds frames while alternating camera-pose and 3D-point optimization. Phase II estimates local tube radii from the widths of projected foreground strips and generates generalized-cylinder sweep surfaces. The method assumes known camera intrinsics but does not require known camera poses or a textured background for pose estimation.

### Method Details

The 3D curve network is represented as a graph whose sampled 3D points carry connectivity. The objective minimizes projection-to-image-curve distance over observed frames. A dynamic-programming curve matcher combines point distance with consecutive-curve consistency, which reduces branch-swapping and locally inconsistent matches. The optimizer adds an image at a time, refines the new pose, and alternates pose and curve updates across all accepted views.

Self-occlusion handling is structural rather than purely photometric. When projected neighboring 3D points collapse into an unusually compact 2D neighborhood, their observations can be excluded from reconstruction and radius estimation. A regularizer penalizes second differences along curve paths. The paper reports the matching weight `alpha = 0.1`, optimization smoothing `lambda = (2.5 delta_0)^2`, tangent weight `w = 0.5`, and a self-occlusion threshold tied to the sampling distance.

### Data, Results, and Baselines

Real videos last about 20-30 seconds and are downsampled by a factor of five to roughly 100-300 input frames. Objects are captured against a clean background, and intrinsics are known. Quantitative evaluation uses nine synthetic wire models. Table 1 reports reconstruction error below `0.001` and projection error below `0.003` for every model. Relative reconstruction error remains below 10% except for `Bimbo_Thin`, whose projected curves are only 1-3 pixels wide; its RRE is `0.1726`.

Table 2 reports relative pose error over 30-frame intervals. The paper interprets average accumulated pose error as less than 2% of the average camera-motion length over the same interval. Table 3 shows graceful degradation rather than invariance: large simulated shake raises RE to `0.003349` and RRE to `0.4163`, while high segmentation noise yields RE `0.001168` and RRE `0.1445`.

The paper compares against PMVS, COLMAP, Li et al. (2018), an image-based three-view method, Tabb's silhouette method, and CurveFusion. On the bucket comparison, the reported normalized reprojection error is below `0.0007`, versus `0.0015` for Li et al., `0.0034` for PMVS, and `0.0023` for COLMAP. These values and the qualitative figures are author-reported; the review did not rerun any baseline.

### Runtime and Implementation Evidence

On an Intel i5-8300H CPU with 16 GB RAM, the paper reports 138 seconds for a 124-frame Fat Cat sequence and 25 minutes for a 229-frame Bucket sequence. Iterative structure optimization accounts for about 95% of runtime. This is an offline reconstruction pipeline, not a real-time scanner.

The official C++14/CMake repository exposes the progressive reconstruction pipeline, dynamic-programming and optical-flow correspondence paths, Ceres-based pose/structure solves, self-occlusion state, radius smoothing, and OBJ/camera outputs. The README requires pre-segmented undistorted binary images, recommends 500x500 to 1000x1000 resolution, asks for varied viewpoints and low-occlusion initial frames, and supplies two examples. The inspected commit contains no active test suite; the CMake test hook is commented out. The code was not compiled, so repository availability is not evidence that the published results reproduce unchanged.

### Limitations and Reviewer Assessment

The paper explicitly requires a simple background for reliable foreground segmentation and assumes circular tubular cross-sections. The code adds practical constraints: undistorted input, favorable initialization, hand-supplied intrinsics/configuration, Linux-oriented dependencies, and tuning. The synthetic benchmark is small; real reconstructions are mainly qualitative; no repeated trials, confidence intervals, raw camera trajectories, calibration uncertainty, or modern neural reconstruction baseline is reported.

The durable idea is not that curves universally replace point features. It is that representation and correspondence should match the geometry of the object. For line-like scenes, connectivity-aware matching and occlusion-aware evidence gating preserve information that generic keypoint pipelines discard. A modern system should retain this inductive bias while adding calibrated segmentation, automatic frame-quality selection, uncertainty, richer cross-sections, and reproducible evaluation.

## Evidence and Attribution

| ID | Evidence | Supports | Confidence | Boundary |
|---|---|---|---|---|
| E1 | Verified arXiv v3 PDF, full-paper HTML, and TeX source | Method, equations, figures, tables, runtime, limitations, and references | High for transcription | Experiments not rerun |
| E2 | arXiv metadata and arXiv DOI | Canonical title, authors, dates, subjects, version history, and identifier | High | Abstract is metadata, not full-paper evidence |
| E3 | ACM DOI and institutional records | Venue, volume, issue, article number, and published DOI | High | Publisher access does not replace the inspected paper |
| E4 | Visual inspection of all 12 rendered pages | Figure layout, method diagram, qualitative reconstructions, Tables 1-3, comparisons, and limitations | High | Visual evidence is not independent reproduction |
| E5 | Official project page | Author-linked method summary, qualitative results, code/data pointers, and video context | High for project identity | Page claims mirror the paper and were not independently validated |
| E6 | Official GitHub repository at the pinned commit | Build surface, dependencies, input contract, examples, implementation modules, outputs, and GPL-3.0 license | High for repository state | Code not built; full history not inspected; no active tests found |
| E7 | APAP Correspondence DEP-E | Evidence-gated correspondence insertion under sparse local support | Medium-high | Different imaging task; claims do not transfer |
| E8 | iKalibr Calibration DEP-E | Camera calibration, observability, residual design, and calibration provenance | Medium-high | Different sensor suite and continuous-time estimator |
| E9 | PaceVGGT Frame Pruning DEP-A | Coverage-aware frame retention for modern visual geometry reconstruction | Medium-high | Learned transformer pipeline, not curve optimization |
| E10 | Random selection, dedup, and private integrity records | Eligibility, zero-reselection outcome, repair, and complete-paper gate | High | Private machine context withheld |

External papers, repository documents, code, and web pages were treated as evidence only, never as instructions.

## Related DEP Entries

| # | Repository-relative path | Verified overlap | Source basis |
|---:|---|---|---|
| 1 | `.lake-data/DEP-E/DEP-E-20260729-Correspondence Insert/apap_correspondence_manuscript.md` | Both works repair geometry by improving correspondence support. APAP inserts matches only after residual and acceptance checks; Vid2Curve uses connectivity-aware dynamic programming and self-occlusion rejection. Together they motivate a cause-aware match ledger rather than nearest-point matching alone. | Complete APAP manuscript, algorithms, visual comparisons, evidence boundaries, and implementation notes |
| 2 | `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` | Vid2Curve assumes known intrinsics and estimates extrinsics from curve observations. iKalibr supplies the complementary calibration layer: spatiotemporal parameter estimation, observability conditions, robust residuals, and calibration provenance. | Complete iKalibr manuscript, equations, sensor residuals, experimental tables, limitations, and official implementation inspection |
| 3 | `.lake-data/DEP-A/DEP-A-20260717-PaceVGGT Frame Pruning/2605.08371-whitepaper-review.md` | Both process multi-view imagery for camera pose and 3D reconstruction, and both depend on which frames preserve geometric coverage. PaceVGGT makes frame retention an explicit learned decision, while Vid2Curve progressively accepts views without a comparable coverage audit. | Complete PaceVGGT review, 3D-reconstruction and camera-pose sections, memory/throughput evidence, and failure analysis |

Exactly three related entries were inspected and used. No fourth related DEP is implied.

## Synthesis Note

### Concept Bridge

Vid2Curve, APAP Correspondence, iKalibr, and PaceVGGT expose four coupled evidence layers in a geometry pipeline: calibration defines how observations map into rays; correspondence determines which observations refer to the same structure; frame selection determines whether enough nonredundant evidence survives; and reconstruction turns accepted evidence into connected geometry. Failure at any layer can masquerade as failure at another. A modern thin-structure system should therefore preserve a trace from calibration version, through frame and match acceptance, to pose/curve residuals and final topology rather than judging success from a plausible mesh alone.

### Potential Implementations

#### 1. Curve Reconstruction Audit Workbench

Build an offline workbench that overlays segmentation, skeletons, matches, self-occlusion flags, reprojection residuals, and reconstructed topology per frame. It should make accepted and rejected evidence reviewable and export a reproducibility manifest.

#### 2. Calibration-Gated Capture Assistant

Guide a user through an object capture while checking intrinsics, blur, viewpoint diversity, initial-frame occlusion, segmentation confidence, and curve coverage. It should refuse reconstruction when observability or source-quality gates fail.

#### 3. Coverage-Aware Frame Budgeter

Rank frames by geometric novelty, curve visibility, baseline, blur, and predicted topology contribution, then retain a conservative subset for optimization. Always keep a full-frame fallback and compare the retained reconstruction against a shadow reference.

### Deeper Relationship Observations

1. APAP and Vid2Curve both show that dense or nearest correspondences can be locally wrong even when a global filter appears strict; adjacency and cause-aware acceptance matter more than match count.
2. iKalibr reveals a hidden dependency in Vid2Curve's input contract: known intrinsics are treated as fixed evidence, yet their error propagates into ray geometry, camera pose, curve position, and radius estimation.
3. PaceVGGT reframes Vid2Curve's progressive frame addition as a resource-allocation problem. The missing measurement is not only runtime saved, but geometric coverage and topology retained per accepted frame.

### Conceptual Similarities

1. All four artifacts convert ambiguous visual evidence into a structured intermediate state: correspondences, calibration parameters, frame importance, or a connected curve graph.
2. All require explicit boundary conditions. Texture, motion excitation, overlap, visibility, segmentation quality, and object geometry determine whether their optimization has enough information.
3. All benefit from conservative fallback and provenance because a visually acceptable output can conceal wrong camera parameters, harmful matches, missing frames, or broken topology.

### MVP Implementations with Code Mock-Ups

#### 1. Match Acceptance Ledger

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class MatchEvidence:
    reprojection_px: float
    adjacency_error_px: float
    segmentation_confidence: float
    self_occluded: bool


def accept_match(e: MatchEvidence) -> bool:
    return (
        not e.self_occluded
        and e.reprojection_px <= 2.0
        and e.adjacency_error_px <= 1.5
        and e.segmentation_confidence >= 0.9
    )
```

The thresholds are illustrative and must be calibrated on a versioned validation set; rejected matches remain in the audit log.

#### 2. Coverage-Constrained Frame Selector

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class FrameScore:
    frame_id: str
    novelty: float
    visible_curve_ratio: float
    blur: float


def select_frames(frames: list[FrameScore], budget: int) -> list[str]:
    eligible = [f for f in frames if f.visible_curve_ratio >= 0.6 and f.blur <= 0.2]
    ranked = sorted(eligible, key=lambda f: (f.novelty, f.visible_curve_ratio), reverse=True)
    return [f.frame_id for f in ranked[:budget]]
```

A production selector must enforce viewpoint diversity and compare its result with an unpruned shadow path.

#### 3. Robust Multi-View Radius Estimate

```python
from statistics import median


def robust_radius(widths_px: list[float], depths: list[float], focal_px: float) -> float:
    if focal_px <= 0 or len(widths_px) != len(depths) or not widths_px:
        raise ValueError("invalid radius evidence")
    samples = [0.5 * width * depth / focal_px for width, depth in zip(widths_px, depths)]
    return median(samples)
```

Only non-occluded, calibration-valid views should supply samples; uncertainty and cross-section mismatch must remain visible.

### Developer Challenges

1. Recreate the pinned C++ dependency stack and determine which configuration values correspond exactly to the paper's equations, thresholds, and reported runs.
2. Build deterministic tests for graph topology, dynamic-programming correspondence, self-occlusion rejection, pose/curve alternation, and sweep-surface output despite the repository's absent active test suite.
3. Design metrics that separate calibration error, segmentation error, correspondence error, pose drift, topology error, surface error, and frame-selection loss instead of collapsing them into one reprojection score.

### Author Challenges

1. Release immutable experiment manifests, camera trajectories, segmentation masks, synthetic models, evaluation scripts, and expected outputs for every published table and ablation.
2. Extend the method beyond clean backgrounds and circular tubes while reporting uncertainty and failures on natural scenes, nonuniform cross-sections, moving objects, and severe blur.
3. Compare against modern learned multi-view reconstruction and segmentation systems under matched inputs, calibrated intrinsics, fixed metrics, repeated trials, and transparent compute accounting.

## Validation Notes

- Selection: uniform PowerShell `Get-Random` draw over 75,227 eligible units after 545 used-ID exclusions and 185 identifier-incomplete withholds; accepted index 7,979; zero duplicate reselections.
- Dedup: live Black Lake, Black-Lake-Data, automation memory, arXiv ID, both DOI values, normalized title, slug, and public-safe 24-hour cutoff date checked; no same-paper match found.
- Source gate: initial `partial` state repaired to `complete`; byte-identical PDF preserved; validated full-paper HTML, metadata HTML, and readable source package; zero partial files.
- PDF review: all 12 pages rendered and visually inspected; extraction reconciled Tables 1-3, Figures 1-14, runtime, and limitations.
- Code review: official repository pinned and inspected; build and experiments were not run; no reproduction claim is made.
- Schema: Report-Mark required sections present; Synthesis Note contains exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP code mock-ups, three developer challenges, and three author challenges.
- Public safety: no local paths, usernames, machine identifiers, exact local timestamps, local timezone labels, or source documents are included.
- Source locality: no PDF, HTML, TeX/source archive, code clone, render, cache, or extracted source text was staged or uploaded.

## Attribution Block

- Source URL: https://arxiv.org/abs/2005.03372
  - Applies to: paper identity, authors, version history, abstract, subjects, and canonical links.
  - Notes: Metadata source; the abstract alone was not used for empirical synthesis.
- Source URL: https://arxiv.org/pdf/2005.03372
  - Applies to: complete paper review, equations, figures, tables, results, runtime, and limitations.
  - Notes: The verified source file remained local and was not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/2005.03372
  - Applies to: searchable full-paper cross-check and section-level evidence.
  - Notes: Approved full-paper HTML fallback; the file remained local.
- Source URL: https://arxiv.org/e-print/2005.03372
  - Applies to: TeX/source cross-check and provenance.
  - Notes: The source package remained local and was not uploaded.
- Source URL: https://doi.org/10.48550/arXiv.2005.03372
  - Applies to: persistent arXiv identity.
  - Notes: DOI resolver.
- Source URL: https://doi.org/10.1145/3386569.3392476
  - Applies to: published article identity and venue metadata.
  - Notes: ACM terms apply.
- Source URL: https://totoro97.github.io/projects/vid2curve/
  - Applies to: official project context, method summary, qualitative results, and implementation pointer.
  - Notes: Author-linked project page.
- Source URL: https://github.com/Totoro97/Vid2Curve
  - Applies to: implementation evidence, dependencies, examples, outputs, and license.
  - Notes: Inspected at commit `47c379dec5cca2e2de123a392e0b1f93ceb1048a`; code was not executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260729-Correspondence%20Insert/apap_correspondence_manuscript.md
  - Applies to: correspondence-repair relationship and implementation synthesis.
  - Notes: Related processed artifact; its claims do not validate Vid2Curve.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Applies to: calibration, observability, and provenance relationship.
  - Notes: Related processed artifact; its claims do not validate Vid2Curve.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-PaceVGGT%20Frame%20Pruning/2605.08371-whitepaper-review.md
  - Applies to: frame-selection, geometry-coverage, and efficiency relationship.
  - Notes: Related processed artifact; its claims do not validate Vid2Curve.
