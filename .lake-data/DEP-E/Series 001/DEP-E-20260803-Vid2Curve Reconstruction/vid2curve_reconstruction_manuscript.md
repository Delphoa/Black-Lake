---
title: "Vid2Curve Reconstruction - DEP-E"
generated_at: "2026-08-03 (date-only public marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of curve-based camera pose estimation and thin-structure reconstruction from handheld RGB video."
source_status: "verified private source bundle; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-03"
temporal_cutoff: "arXiv:2005.03372v3, published record, project page, and official implementation inspected through 2026-08-03"
primary_url: "https://arxiv.org/abs/2005.03372"
stable_identifier: "arXiv:2005.03372v3; DOI 10.48550/arXiv.2005.03372; DOI 10.1145/3386569.3392476"
confidence_summary: "High for source identity, method, printed tables, figures, runtime, and code surface; medium for generalization because results were not reproduced."
safety_scope: "offline reconstruction research, authorized capture, synthetic evaluation, and audit tooling"
distribution_notes: "Generated Markdown and public URLs only; all original source files, code clones, renders, and caches withheld locally."
---

# Vid2Curve Reconstruction - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Vid2Curve arXiv record | Primary metadata | HTML | arXiv:2005.03372v3 | https://arxiv.org/abs/2005.03372 | Public research metadata; arXiv terms apply. | 2026-08-03 | Inspected |
| S2 | Vid2Curve complete paper | Primary paper | PDF and full-paper HTML | arXiv:2005.03372v3; 12 pages | https://arxiv.org/pdf/2005.03372; https://ar5iv.labs.arxiv.org/html/2005.03372 | Private verified copies inspected; no source file redistributed. | 2026-08-03 | Fully inspected and integrity-verified |
| S3 | Vid2Curve manuscript source | Primary manuscript source | TeX/source package | arXiv:2005.03372v3 | https://arxiv.org/e-print/2005.03372 | Private source package inspected; not redistributed. | 2026-08-03 | Inspected |
| S4 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2005.03372 | https://doi.org/10.48550/arXiv.2005.03372 | Public DOI locator. | 2026-08-03 | Verified |
| S5 | ACM published record | Published version | Journal article | DOI 10.1145/3386569.3392476; TOG 39(4), Article 132 | https://doi.org/10.1145/3386569.3392476 | ACM terms apply. | 2026-08-03 | Identity and venue verified |
| S6 | Vid2Curve project page | Official project context | Web page | SIGGRAPH 2020 project page | https://totoro97.github.io/projects/vid2curve/ | Public author-linked project context. | 2026-08-03 | Inspected |
| S7 | Vid2Curve repository | Official implementation | GitHub repository | `master` at `47c379dec5cca2e2de123a392e0b1f93ceb1048a` | https://github.com/Totoro97/Vid2Curve | GPL-3.0; third-party components separately acknowledged. | 2026-08-03 | README, build, configuration, core modules, license, and examples inspected; code not run |
| S8 | APAP Correspondence DEP-E | Related processed research | Markdown manuscript | DEP-E-20260729-Correspondence Insert | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260729-Correspondence%20Insert/apap_correspondence_manuscript.md | Underlying sources separately attributed. | 2026-08-03 | Inspected |
| S9 | iKalibr Calibration DEP-E | Related processed research | Markdown manuscript | DEP-E-20260714-iKalibr Calibration | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Underlying sources separately attributed. | 2026-08-03 | Inspected |
| S10 | PaceVGGT Frame Pruning DEP-A | Related processed research | Markdown whitepaper review | DEP-A-20260717-PaceVGGT Frame Pruning | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-PaceVGGT%20Frame%20Pruning/2605.08371-whitepaper-review.md | Underlying sources separately attributed. | 2026-08-03 | Inspected |
| S11 | Black Lake repository authorities | Submission rules | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Public repository standards. | 2026-08-03 | Fetched and read |
| S12 | Black-Lake-Data authority | Dedup context | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Read before relying on companion-repository layout. | 2026-08-03 | Fetched and read |

The paper was submitted on 2020-05-07 and revised as v3 on 2020-05-20. It was published in ACM Transactions on Graphics 39(4), Article 132, as part of SIGGRAPH 2020. The paper identifies curve reconstruction, delicate structures, image-based reconstruction, camera pose estimation, and parametric curve/surface models as its central domain.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4, S5 | Primary and publisher metadata | Title, authors, dates, identifiers, venue, volume, issue, and article number. | Source identity and chronology. | High | Metadata does not establish technical claims. |
| E2 | S2, S3 | Complete primary paper and source | Sections 1-6, Equations 1-8, Figures 1-14, Tables 1-3, references, and source files. | Problem, method, parameters, experiments, results, runtime, and limitations. | High for source reporting | No result was independently reproduced. |
| E3 | S2 | Visual paper evidence | All 12 rendered pages, method diagram, reconstructions, ablations, sensitivity figures, comparisons, and tables. | Layout-aware verification of figures and table values. | High for transcription | Qualitative figures are not blinded or independent evaluation. |
| E4 | S6 | Official project context | Method overview, qualitative galleries, publication identity, code/data pointers, and project framing. | Author-linked public context. | High for identity | Project claims largely restate the paper. |
| E5 | S7 | Official implementation | README, `CMakeLists.txt`, `config.ini`, initialization, curve matching, optimization, occlusion, radius, output, examples, and license. | Implementation surface, dependencies, inputs, outputs, and reproducibility limits. | High for inspected state | Code not compiled; tests and reported outputs not reproduced. |
| E6 | S8 | Related DEP | Evidence-gated correspondence insertion and residual ambiguity. | Correspondence relationship and repair-loop design. | Medium-high | Different panorama-stitching task. |
| E7 | S9 | Related DEP | Calibration parameters, observability, robust residuals, and provenance. | Calibration dependency and upstream integrity. | Medium-high | Different multi-sensor setting. |
| E8 | S10 | Related DEP | Frame scoring, pruning, geometric coverage, camera-pose and 3D-reconstruction evaluation. | Frame-budget and geometry-coverage relationship. | Medium-high | Modern learned transformer rather than curve optimization. |
| E9 | S11, S12 | Repository authorities | DEP class, container path, publication index, source withholding, naming, README, attribution, and commit rules. | Deposit and submission compliance. | High | Process evidence only. |
| E10 | Private selection and verification records | Private process evidence | Candidate enumeration, used-ID exclusion, random draw, dedup, repair, PDF/HTML/source checks, and page rendering. | Eligibility and complete-source gate. | High | Local paths and source bytes intentionally withheld. |

## Executive Summary

Vid2Curve proposes a representation-aligned alternative to point-feature structure-from-motion for thin, textureless, self-occluding objects. It takes a handheld RGB video with known intrinsics, extracts a skeletal curve from each segmented foreground frame, and jointly estimates camera poses plus a connected 3D curve graph. An alternating optimization progressively adds views, rejects self-occluded observations, and regularizes curve geometry. A second phase estimates radii from multi-view foreground widths and generates generalized-cylinder sweep surfaces.

The paper reports strong in-scope evidence. Across nine synthetic models, reconstruction error is below `0.001` and projection error below `0.003`; relative reconstruction error is below 10% except for a 1-3-pixel-wide model. A bucket comparison reports normalized reprojection error below `0.0007`, lower than three listed baselines. Ablations visually support connectivity-aware matching and self-occlusion handling. Sensitivity experiments show deterioration under large shake and boundary noise rather than claiming complete robustness.

The evidence is bounded. Real videos use clean backgrounds, known intrinsics, carefully chosen initial views, and tubular circular cross-sections. The synthetic benchmark is small, real-scene evaluation is mostly qualitative, and no uncertainty or repeated-trial analysis is reported. Runtime ranges from 138 seconds to 25 minutes in two examples, with iterative structure optimization accounting for about 95% of time.

The official repository materially improves inspectability but does not close reproducibility. It exposes a C++14/CMake implementation, two example sequences, input preparation, dependencies, configuration, and OBJ/camera outputs. It was not built during this review, has no active test suite in the inspected tree, and does not provide an immutable command-to-table reproduction receipt. Reviewer confidence is high that the artifact accurately represents the paper and code surface, and medium that the reported performance will generalize beyond the documented capture conditions.

## Detailed Summary

### Problem Context

Thin structures violate assumptions that make conventional image-based reconstruction convenient. They may offer long edges but few stable point features; neighboring branches can look locally identical; their width can approach the sampling limit; and self-occlusion projects multiple 3D branches into the same 2D location. Commodity RGB-D systems add depth but can struggle with small cross-sections, low spatial resolution, black surfaces, and outdoor infrared interference.

Vid2Curve chooses curves as the primary observation and graph as the primary 3D representation. The object is modeled as connected skeletal curves with varying radius. The method uses segmentation and connectivity to preserve thin structures that point clouds or voxel grids can blur, disconnect, or miss.

### Inputs and Preprocessing

The input is a handheld RGB video with known intrinsics. The paper captures objects against a clean background and segments the foreground with color keying or an advanced video segmentation tool. It then thins each binary mask to a one-pixel medial-axis curve. The implementation expects pre-segmented, undistorted binary images, a camera configuration file, varied viewpoints, and favorable low-occlusion initial frames. It recommends 500x500 to 1000x1000 images.

This preprocessing is part of the method's effective information boundary. It removes the natural-background segmentation problem and assumes distortion has already been handled. Downstream accuracy therefore cannot be separated from mask quality, calibration quality, or the selected first frames.

### Representation and Initialization

The 3D curve network is a graph `G = (P, E)`, where sampled 3D points define geometry and edges define connectivity. Camera extrinsics for each image are optimized together with the point coordinates. Initialization uses two image frames whose provisional camera centers are sufficiently separated. A dynamic-programming matcher pairs their curve samples while respecting local path continuity; the resulting correspondences initialize camera motion and 3D depth.

The initial points are connected by a modified minimum-spanning-tree procedure. Candidate edges are distance-limited; cycle checks and a loop-length threshold preserve a general curve graph rather than forcing a pure tree. Points are then resampled to maintain usable projected density across views.

### Curve Matching and Alternating Optimization

For each new frame, the method first estimates pose and then alternates camera and curve updates. A nearest-point rule can jump between nearby branches or exchange ordering along the curve. Vid2Curve instead evaluates a sequence-level objective that combines projected point distance and consistency between consecutive matched samples. Candidate matches are restricted to a local radius and solved by dynamic programming.

The main objective sums image-space distances between projected 3D points and their matched 2D curves. A tangent-aware distance distinguishes normal and tangent directions, while a second-difference regularizer discourages unstable bending. The paper reports `alpha = 0.1` for matching and a smoothing term controlled by `lambda`; the inspected implementation exposes separate iteration, final, and radius smoothing weights in configuration.

### Self-Occlusion and Surface Reconstruction

When several branches project into the same neighborhood, a 2D observation no longer uniquely constrains one 3D point. The method measures spatial compactness around each projected match. Observations classified as self-occluded are removed from the relevant curve and radius updates. The ablation on a basket shows significant geometry and topology errors when this mechanism is disabled.

After camera and curve estimation, the method assumes the object is a set of generalized cylinders with circular cross-sections. For a projected curve point, the foreground strip width and camera depth give a per-view radius estimate. Non-occluded estimates are aggregated across views, smoothed along the graph, and swept around the centerline to form the final mesh.

### Experimental Design

Real sequences cover wire art, baskets, racks, branches, and related objects. Videos last roughly 20-30 seconds and are downsampled by five to 100-300 frames. The paper uses nine synthetic models for quantitative evaluation and defines reconstruction error, relative reconstruction error, projection error, relative pose error, and topology precision/recall.

The reported evidence includes:

- Table 1: RE below `0.001` and PE below `0.003` across all nine models; RRE below 10% except `Bimbo_Thin` at `0.1726`.
- Table 2: relative pose error measured over 30-frame intervals, interpreted as less than 2% of average motion length over the same span.
- Matching ablation: a naive closest-point search creates missing and redundant grid branches.
- Self-occlusion ablation: disabling detection visibly damages basket geometry and topology.
- Shake sensitivity: large shake raises RE to `0.003349` and RRE to `0.4163`.
- Segmentation sensitivity: high boundary noise yields RE `0.001168` and RRE `0.1445`.
- Bucket comparison: normalized reprojection error below `0.0007`, versus `0.0015` for Li et al., `0.0034` for PMVS, and `0.0023` for COLMAP.

These are paper-reported measurements. The comparisons do not establish a modern population-level benchmark: input assumptions differ across methods, sample size is limited, real data lacks quantitative ground truth, and repeated trials or intervals are absent.

### Performance and Code Surface

The paper reports 138 seconds for the 124-frame Fat Cat example and 25 minutes for the 229-frame Bucket example on an Intel i5-8300H CPU with 16 GB RAM. Initialization and surface reconstruction consume about 3% and 2%; iterative structure optimization consumes about 95%.

The pinned official repository contains 364 tracked files, including 72 C/C++ headers or sources and 286 example files. Its build depends on OpenCV, Boost, Ceres, OpenMP, glog, Eigen, and optional Pangolin. Core modules cover extraction, matching, initialization, view optimization, model optimization, self-occlusion state, graph processing, radius estimation, sweep surfaces, and final OBJ/camera output. The CMake test section is commented out, and no active test files were found. The repository was inspected rather than executed, so runtime and numerical equivalence to the paper remain open.

### Conclusion

Vid2Curve demonstrates that line-like scene structure can be reconstructed more faithfully when the representation, correspondence rule, and occlusion logic preserve curve connectivity. Its strongest contribution is a coherent pipeline with inspectable geometry and well-motivated ablations. Its largest transfer risk is hidden preprocessing: clean masks, known intrinsics, undistortion, initialization quality, and circular cross-sections carry much of the practical burden.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Curve correspondences can estimate camera motion without background point features. | Author method claim | E2, E3, E5 | Mechanism is directly specified and implemented; accuracy remains bounded by masks, intrinsics, visibility, and initialization. | High for mechanism, medium for generality |
| C2 | Joint pose and curve optimization reconstructs complex thin structures from handheld RGB video. | Author claim | E2-E4 | Qualitative and synthetic evidence support the claim in documented conditions; no independent reproduction. | Medium-high |
| C3 | Connectivity-aware matching is materially better than naive nearest-point matching. | Author ablation claim | E2-E3 | Grid ablation shows missing and redundant branches under the naive rule. | Medium-high |
| C4 | Self-occlusion detection preserves geometry and topology. | Author ablation claim | E2-E3 | Basket ablation is visually strong but lacks repeated quantitative trials. | Medium |
| C5 | Synthetic RE is below `0.001` and PE below `0.003` across the reported models. | Benchmark result | E2-E3 | Values match Table 1; the benchmark is small and not independently rerun. | High for transcription |
| C6 | Average 30-frame pose error is below 2% of average 30-frame camera motion. | Author interpretation | E2-E3 | Consistent with Table 2 and surrounding prose; depends on the chosen normalization and synthetic paths. | Medium-high |
| C7 | The method outperforms listed image-, depth-, and silhouette-based baselines. | Author comparative claim | E2-E3 | Supported for selected figures and one reported bucket metric, not as a broad ranking. | Medium |
| C8 | The official repository is a reproducible reference implementation. | Potential extrapolation | E5 | Inspectable implementation exists, but environment, tests, and command-to-table reproduction were not verified. | Medium-low |
| C9 | A modern pipeline should log calibration, frame, match, occlusion, and topology evidence together. | Reviewer interpretation | E2, E5-E8 | Strong synthesis across the primary work and three related DEP artifacts. | Medium-high |

## Methodology

- `Research objective`: Review one randomly selected local arXiv paper source-first, enforce the complete-paper gate, and create a schema-complete DEP-E research artifact with exactly three verified DEP relationships.
- `Sources inspected`: Complete PDF, all 12 rendered pages, verified full-paper HTML, TeX/source package, arXiv metadata, arXiv and ACM DOI records, author project page, official repository at a pinned commit, live repository authorities, and three related DEP artifacts.
- `Discovery strategy`: Enumerated the local archive with `rg --files -g "*.pdf"`, collapsed PDFs to unique parent units, derived arXiv IDs from names, built a cross-repository used-paper index, withheld identifier-incomplete units, and used PowerShell `Get-Random` over the eligible array.
- `Inclusion criteria`: Primary or near-primary sources that identify the selected paper, substantiate method/results/code claims, define repository rules, or provide concrete overlap in correspondence, calibration, or multi-view frame coverage.
- `Exclusion criteria`: Abstract-only empirical claims, secondary summaries as technical authority, unrelated keyword hits, unverified same-paper code mirrors, and source files not authorized for public deposition.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product-research, and replication analysis.
- `Evidence handling`: Author claims, printed results, repository observations, reviewer interpretations, and implementation proposals are labeled separately. Quantitative claims retain dataset, normalization, and reproduction caveats.
- `Uncertainty handling`: Missing repeated trials, real-scene ground truth, code execution, modern baselines, and reproduction receipts remain explicit.
- `Extraction process`: Reconciled rendered PDF pages, searchable full-paper HTML, TeX/source inventory, printed tables, figures, equations, code modules, configuration, and public metadata.
- `Version control`: Paper pinned to arXiv:2005.03372v3; official implementation pinned to `47c379dec5cca2e2de123a392e0b1f93ceb1048a`.
- `Reviewer stance`: DEP-ready preservation, critical paper report, implementation audit, safe product translation, and replication planning.

Random selection used a uniform PowerShell `Get-Random` index after deterministic enumeration and used-ID exclusion. The archive contained 75,960 PDFs in 75,957 unique parent units. A 1,950-ID used-paper index excluded 545 units; 185 identifier-incomplete units were withheld; 75,227 units remained eligible. Zero-based index 7,979 selected arXiv:2005.03372. An earlier inefficient in-memory grouping attempt was terminated before producing any selection and was discarded. Exact ID, both DOI values, normalized title, slug, and 24-hour checks found no duplicate, so reselection count was zero.

The selected unit initially had a valid PDF but no verified full-paper HTML. Review paused. A bounded repair preserved the byte-identical PDF, collected approved ar5iv full-paper HTML, arXiv metadata HTML, and the source package, refreshed private provenance/summary/verification records, and passed the complete-paper gate before synthesis.

## Scope, Constraints, and Assumptions

- `Scope`: One paper, its official implementation surface, its published evidence, and exactly three related Black Lake artifacts.
- `Temporal boundary`: Paper v3, official public artifacts, and repository context inspected through 2026-08-03.
- `Evidence limits`: No code build, reconstruction run, baseline execution, camera-trajectory audit, dataset redistribution, or table reproduction. Real-scene outputs are mainly qualitative.
- `Assumptions`: The verified PDF, HTML, and source package represent the same arXiv v3 work. Printed table values are transcribed as source claims. The pinned repository is author-linked and relevant, but not necessarily an immutable reproduction of every experiment.
- `Constraints`: Public output excludes source files, private archive paths, machine context, exact local timestamps, and local timezone labels. Capture and evaluation should use authorized objects and imagery.
- `Out of scope`: Real-time deployment, surveillance, identity inference, autonomous safety decisions, broad benchmark superiority, and production authorization.
- `Intended use`: Research review, replication planning, geometry-pipeline design, audit tooling, and DEP deposition.
- `Audience`: Computer-vision researchers, graphics engineers, reconstruction-tool developers, robotics perception teams, and research reviewers.
- `Depth target`: Full manuscript report with source, code, visual, experimental, and implementation analysis.
- `Reproducibility boundary`: The public repository and examples make a build attempt possible, but the published tables cannot be reproduced from this artifact without a pinned toolchain, input manifests, evaluation scripts, expected outputs, and hardware/run details.
- `Operational boundary`: Offline, authorized reconstruction and synthetic evaluation only. No inference about people, ownership, or safety-critical scene state.
- `Data sensitivity`: Public research metadata and source URLs; no raw private video or source files redistributed.

## Observations

- `Observed pattern`: Performance collapses first at the sampling boundary. The `Bimbo_Thin` model projects to 1-3 pixels and is the only Table 1 case above 10% RRE.
- `Observed pattern`: The method's strongest ablations are topological rather than photometric: wrong branch association and unhandled self-occlusion create missing, redundant, or crossed structure.
- `Technical implication`: Calibration and segmentation errors should be tracked as first-class inputs because they alter every downstream pose, point, radius, and topology estimate.
- `Technical implication`: Progressive view addition creates an opportunity for coverage-aware frame selection, but unsafe pruning could remove the only view that disambiguates a junction.
- `Contradiction or tension`: The paper frames capture as handheld and accessible, yet requires clean backgrounds, known intrinsics, low-occlusion initialization, undistorted masks, and minutes of offline compute.
- `Reviewer hypothesis`: A hybrid system that learns segmentation and frame quality but keeps an explicit curve graph and auditable optimizer may generalize better than a fully opaque end-to-end mesh predictor for thin structures.
- `Open question`: How much of the reported advantage survives natural backgrounds, specular wires, moving branches, noncircular sections, rolling shutter, uncertain intrinsics, or learned modern baselines?

## Considerations

### Evaluation

Use fixed scene-level train/validation/test partitions for any learned component. Publish masks, calibration, trajectories, meshes, frame lists, metric code, and repeated-trial uncertainty. Report failure rates at junctions and 1-3-pixel widths, not only averaged geometric distance.

### Calibration and Capture

Check intrinsics, distortion, rolling shutter, blur, baseline, and view coverage before optimization. Preserve an immutable capture manifest. Low-quality first frames can poison initialization, so initial-pair selection should expose scores and permit abstention.

### Correspondence and Topology

Maintain accepted/rejected match evidence, branch identity, residual cause, and self-occlusion state. Reprojection error alone cannot distinguish wrong calibration, wrong segmentation, repeated structure, missing views, or wrong topology.

### Operations and Cost

The iterative curve update is the principal bottleneck. Frame budgeting, graph sparsification, parallel residual evaluation, and warm-starting are plausible, but every optimization must report geometry and topology retained under the achieved budget. A fast plausible mesh is not a successful reconstruction.

### Privacy, Safety, and Governance

Use authorized captures, minimize retention of incidental background imagery, and process locally when scenes may contain people or private spaces. Do not infer identity or ownership from reconstructed geometry. Preserve source provenance, model/config versions, and correction history.

## Strengths

- Representation matches the target geometry: curves and graph connectivity are primary rather than incidental.
- Joint camera/curve optimization removes dependence on textured-background point features.
- Dynamic-programming matching explicitly uses local connectivity and is supported by a targeted ablation.
- Self-occlusion handling is integrated into geometry and radius estimation rather than treated only as image noise.
- Quantitative metrics cover geometry, projection, pose, and topology on synthetic ground truth.
- Sensitivity experiments disclose deterioration under blur and segmentation noise.
- Runtime decomposition identifies iterative optimization as the dominant cost.
- An author-linked GPL-3.0 reference implementation and example inputs are publicly inspectable.

## Weaknesses

- Clean-background segmentation and known intrinsics remove two major natural-scene problems.
- Circular tubular cross-sections exclude flattened, braided, ribbon-like, or irregular thin structures.
- The synthetic benchmark contains only nine models; real-scene evaluation is mainly qualitative.
- Baseline inputs and assumptions differ, limiting the strength of comparative claims.
- No seeds, repeat counts, confidence intervals, calibration uncertainty, or raw trajectory evaluation package is reported.
- Initialization depends on favorable first frames and sufficient translation, but no automatic observability score is evaluated.
- Offline runtime reaches 25 minutes for one 229-frame example.
- The official code lacks an active test suite and was not accompanied by a verified command-to-table reproduction contract.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Learned segmentation with uncertainty and abstention | Preprocessing | Clean backgrounds are the largest capture restriction | Natural-scene coverage with explicit confidence | Domain shift and false masks | Scene-held-out tests with mask/topology error and abstention curves |
| Calibration-aware joint refinement | Geometry | Fixed intrinsics can bias pose, curve, and radius | Lower systematic error and visible calibration confidence | More gauge/observability complexity | Synthetic perturbation sweeps plus calibration ground truth |
| Coverage-aware initial pair and frame selection | Compute and convergence | Progressive views vary in novelty and ambiguity | Faster optimization and fewer initialization failures | Pruning unique evidence | Pareto curves for runtime, pose, topology, and coverage |
| Noncircular cross-section model | Surface representation | Real wires, branches, and fabricated structures are not always circular | More faithful surfaces | More parameters and ambiguity | Ground-truth scans stratified by cross-section type |
| Cause-aware correspondence gate | Matching | Residuals mix occlusion, calibration, blur, and repeated patterns | Fewer harmful branch swaps | Requires labeled failure causes | Match calibration and topology-failure audit |
| Modern baseline and hybrid evaluation | Comparative evidence | 2020 baselines do not cover current neural geometry systems | Current transfer boundary | High compute and tuning burden | Matched-input, matched-calibration, repeated-scene benchmark |
| Reproducible release manifest | Reproducibility | Inspectable code is not a table reproduction receipt | Independent validation and regression testing | Maintenance work | Clean build, two example runs, table-script checks, expected hashes |

## Potential Implementations

### 1. Thin-Structure Capture Auditor

- `User`: researcher, preservation specialist, or graphics technician.
- `Goal`: determine whether a video has enough calibrated, non-occluded evidence for reconstruction.
- `Core mechanism`: score blur, segmentation confidence, baseline, view novelty, curve visibility, and initial-pair observability before running the optimizer.
- `Required inputs`: authorized video, intrinsics, distortion model, segmentation masks, and capture policy.
- `Outputs`: pass/abstain decision, recommended frame set, risk slices, and public-safe manifest.
- `Risk controls`: local processing, no identity analysis, scene authorization, and conservative abstention.
- `Evaluation`: initialization success, topology accuracy, retained coverage, and reviewer agreement.

### 2. Curve Evidence Workbench

- `User`: computer-vision developer or reconstruction reviewer.
- `Goal`: diagnose why a reconstruction fails.
- `Core mechanism`: synchronize frame masks, skeletons, matches, pose residuals, self-occlusion flags, graph updates, and topology events.
- `Required inputs`: sequence, calibration, optimizer trace, match ledger, and reconstructed graph.
- `Outputs`: visual audit, rejected-evidence report, failure classification, and reproducibility bundle.
- `Risk controls`: redaction of incidental imagery, immutable source hashes, and no source upload by default.
- `Evaluation`: root-cause accuracy on seeded failures and time-to-diagnosis.

### 3. Hybrid Neural-Explicit Reconstructor

- `User`: graphics or robotics research team.
- `Goal`: combine learned perception with explicit auditable geometry.
- `Core mechanism`: neural segmentation and frame-quality scoring feed a curve graph, calibration-aware matcher, robust pose/structure optimizer, and uncertainty-aware sweep surface.
- `Required inputs`: public or authorized videos, calibration, segmentation model, graph optimizer, and evaluation ground truth.
- `Outputs`: curve OBJ, mesh OBJ, camera poses, uncertainty fields, and provenance.
- `Risk controls`: synthetic/public development data, full-frame fallback, uncertainty thresholds, and human review.
- `Evaluation`: geometry/topology accuracy, calibration, runtime, failure coverage, and ablations against neural-only and explicit-only systems.

## Three Ways to Exercise This Research

1. `Paper-table audit`: Objective: validate metric semantics without running reconstruction. Inputs: verified Tables 1-3, metric definitions, and selected figures. Method: reconstruct a typed table with units, normalization, denominators, directionality, and caveats. Output: metric audit sheet. Success criterion: every number has a model, error definition, normalization, and evidence locator. Stop condition: any value cannot be reconciled across PDF and HTML. Safety boundary: public metadata and local source review only.
2. `Synthetic correspondence stress test`: Objective: isolate branch-swapping and self-occlusion failures. Inputs: a toy 3D wire graph, known cameras, rendered masks, and controlled blur/noise. Method: compare nearest-point matching, connectivity-aware matching, and occlusion rejection. Output: pose, geometry, and topology error curves. Success criterion: controlled failures reproduce the qualitative mechanisms without claiming paper-level reproduction. Stop condition: calibration or renderer mismatch dominates the intended variable. Safety boundary: synthetic data only.
3. `Pinned implementation smoke plan`: Objective: turn repository availability into a reproducible build receipt. Inputs: the pinned commit, declared dependencies, two bundled examples, and an isolated environment. Method: build, run both examples, record configs and outputs, and compare only repository-documented artifacts. Output: build/run manifest and failure report. Success criterion: deterministic output identities across two clean runs. Stop condition: missing dependency, license conflict, or undocumented input prevents a clean run. Safety boundary: offline examples; no private capture data.

## Example MVP Product

- `Product name`: CurveCapture Auditor
- `Target user`: vision researchers, graphics engineers, and digitization teams working with authorized thin objects.
- `Problem`: Reconstruction can fail invisibly when calibration, segmentation, frame coverage, correspondence, or topology evidence is weak.
- `Core workflow`: Import video and calibration; validate source integrity; segment and skeletonize; score initial pairs and frames; run curve-based reconstruction or abstain; visualize match/occlusion/topology evidence; export geometry plus an audit manifest.
- `Data requirements`: Authorized RGB video, camera intrinsics and distortion, segmentation masks or local segmentation model, frame-quality scores, optimizer traces, and optional synthetic ground truth.
- `Architecture`: Local CLI and review UI; capture validator; segmentation adapter; curve extractor; frame/initial-pair selector; correspondence ledger; robust camera/curve optimizer; sweep-surface module; metrics and Markdown/JSON exporter.
- `Success metrics`: Initialization success rate, RE/RRE/PE, pose error, topology precision/recall, calibration error, abstention calibration, runtime, and percentage of outputs with complete provenance.
- `Risk controls`: Local-only default, explicit capture authorization, incidental-background redaction, no identity inference, immutable version/config records, uncertainty thresholds, and manual acceptance before export.
- `Limitations`: Cannot guarantee natural-scene segmentation, noncircular geometry, real-time operation, or paper-result reproduction. A plausible mesh may still be wrong.
- `MVP boundary`: Offline audit and reconstruction of static tubular structures; no autonomous navigation or surveillance use.
- `Deployment model`: Local workstation CLI plus optional browser-based localhost review UI.
- `Evaluation plan`: Unit tests on synthetic graphs; seeded calibration/mask/match failures; two bundled implementation examples; repeated reconstruction checks; human audit of failure labels.
- `Failure modes`: Poor initial pair, ambiguous repeated branches, missing views, blur, wrong intrinsics, self-occlusion, noncircular cross-section, incomplete masks, and silent topology repair.
- `Maintenance plan`: Pin dependencies and code commits, version thresholds, retain regression scenes, monitor segmentation/calibration drift, and require migration notes for output-schema changes.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Vid2Curve | Primary paper | Selected work under review | https://arxiv.org/abs/2005.03372; https://doi.org/10.1145/3386569.3392476 |
| Vid2Curve project page | Official project context | Method overview, results gallery, video, and implementation pointer | https://totoro97.github.io/projects/vid2curve/ |
| Vid2Curve repository | Official implementation | C++ reference pipeline, examples, dependencies, and configuration | https://github.com/Totoro97/Vid2Curve |
| APAP Correspondence - DEP-E | Related processed research | Evidence-gated local correspondence repair under sparse support | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260729-Correspondence%20Insert/apap_correspondence_manuscript.md |
| iKalibr Calibration - DEP-E | Related processed research | Calibration observability, residuals, and provenance upstream of geometry | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md |
| PaceVGGT Frame Pruning - DEP-A | Related processed research | Coverage-aware frame selection for camera pose and 3D reconstruction | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-PaceVGGT%20Frame%20Pruning/2605.08371-whitepaper-review.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2005.03372 | Canonical identity, authors, dates, subjects, links, and version history | 2026-08-03 | Metadata only; not the empirical evidence base |
| R2 | https://arxiv.org/pdf/2005.03372 | Complete paper, figures, tables, equations, results, runtime, and limitations | 2026-08-03 | Verified private copy inspected; not redistributed |
| R3 | https://ar5iv.labs.arxiv.org/html/2005.03372 | Full-paper searchable cross-check | 2026-08-03 | Approved fallback; verified private copy inspected |
| R4 | https://arxiv.org/e-print/2005.03372 | TeX/source cross-check and provenance | 2026-08-03 | Verified private source package; not redistributed |
| R5 | https://doi.org/10.48550/arXiv.2005.03372 | Persistent arXiv identifier | 2026-08-03 | DOI resolver |
| R6 | https://doi.org/10.1145/3386569.3392476 | Published article and venue identity | 2026-08-03 | ACM terms apply |
| R7 | https://totoro97.github.io/projects/vid2curve/ | Official project summary and implementation pointer | 2026-08-03 | Author-linked project page |
| R8 | https://github.com/Totoro97/Vid2Curve | Official code, dependencies, examples, input/output contract, and license | 2026-08-03 | Pinned commit inspected; code not run |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260729-Correspondence%20Insert/apap_correspondence_manuscript.md | Correspondence repair relationship | 2026-08-03 | Related artifact; does not validate primary claims |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Calibration and observability relationship | 2026-08-03 | Related artifact; does not validate primary claims |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-PaceVGGT%20Frame%20Pruning/2605.08371-whitepaper-review.md | Frame-selection and geometry-coverage relationship | 2026-08-03 | Related artifact; does not validate primary claims |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Root deposition, naming, attribution, source-locality, and commit rules | 2026-08-03 | Live repository authority |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP class, container, publication-index, and filing rules | 2026-08-03 | Live repository authority |
| R14 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion-repository layout used for dedup context | 2026-08-03 | Fetched before reliance |

## Appendix

### Replication Checklist

- [ ] Pin the official repository commit and all C++ dependencies.
- [ ] Record compiler, CMake, OpenCV, Boost, Ceres, glog, Eigen, OpenMP, and optional Pangolin versions.
- [ ] Preserve immutable input-frame, mask, calibration, and configuration manifests.
- [ ] Build and run both bundled examples in a clean environment.
- [ ] Record curve OBJ, mesh OBJ, camera poses, logs, runtime, and output hashes.
- [ ] Implement unit tests for curve matching, graph formation, self-occlusion, pose update, radius smoothing, and output topology.
- [ ] Recreate metric definitions and verify Table 1-3 normalization on synthetic ground truth.
- [ ] Add repeated trials, uncertainty, failure denominators, and calibration perturbation sweeps.
- [ ] Compare full-frame and coverage-budgeted runs with topology-preserving fallbacks.
- [ ] Publish only derived public-safe reports unless source redistribution is separately authorized.

### Source Integrity and Selection Record

- Initial source state: `partial` because full-paper HTML was missing.
- Final source state: `complete` after bounded repair.
- PDF: 7,414,944 bytes; valid header and trailing EOF; 12 unencrypted pages.
- Full-paper HTML: 513,959 bytes; 70,103 body characters; document markers, 34 headings, and five structure terms.
- Source archive: 8,538,727 bytes; 124 readable entries.
- Partial files after repair: 0.
- Selection: 75,960 PDFs; 75,957 parent units; 1,950 used IDs; 545 used-ID exclusions; 185 identifier-incomplete withholds; 75,227 eligible; zero-based index 7,979; zero reselections.
- Dedup sources: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and Black-Lake-Data `.lake-data`, `.reports`, and `.staging`.
- Dedup keys: arXiv ID, arXiv DOI, ACM DOI, normalized title, slug, and public-safe 24-hour cutoff date.

### Distribution Boundary

No PDF, full-paper HTML, metadata HTML, TeX/source archive, code clone, render, cache, extracted source text, or private filesystem locator is included in this DEP. Source files were withheld locally, no public `.source/` directory was created, and no source file is authorized for repository or Slack upload by this run.
