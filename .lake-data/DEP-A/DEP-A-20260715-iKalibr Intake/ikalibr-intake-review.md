# Calibration as Upstream Evidence Infrastructure

## A whitepaper-grade archival intake review of the iKalibr DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration`  
**Source commit:** `398f692812550135476e8d560be1d2a01fa2982e`  
**Paired task indicator:** `BL-DEPPAIR-20260715-4FAD29AE`  
**Direction:** `DEP-E -> DEP-A`  
**Review date:** 2026-07-15  
**Review scope:** complete two-file repository record; canonical paper, publication, and official-code context; method, equations, experiments, limitations, re-conceptualization, and replication agenda  
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes  
**Reproduction boundary:** no calibration data, software build, container, solver, or experiment was executed.

---

## Executive assessment

The selected DEP-E contains a README and a comprehensive manuscript reviewing iKalibr, a targetless offline system for joint spatial and temporal calibration of heterogeneous inertial sensor rigs. Both tracked files were read in full. The record accounts for IMUs, radars, LiDARs, global-shutter cameras, rolling-shutter cameras, continuous-time B-splines, dynamic initialization, sensor-specific residuals, progressive nonlinear optimization, real-world experiments, runtime, limitations, official code, related Black Lake records, and local source withholding.

The canonical v2 paper was inspected directly across its complete HTML structure, including preliminaries, initialization, optimization, experiments, acknowledgments, authorship statement, references, and appendices.[^paper] The arXiv record and official repository were also checked.[^record][^code] The source is complete, not an abstract page. The paper’s 2025 IEEE Transactions on Robotics identity is linked by DOI, while the review remains pinned to arXiv v2 for method and table evidence.[^journal]

iKalibr’s durable contribution is a coordinated estimation pipeline. A reference IMU fixes the gauge. Rotation and a sensor-dependent linear quantity are represented continuously with cubic B-splines. Initialization derives usable starting states from gyro motion and sensor-inertial alignment. A global factor graph then combines inertial, Doppler, point-to-surfel, and reprojection evidence. Parameters are introduced progressively, and LiDAR associations can be rebuilt after refinement.

The evidence shows broad capability and strong repeatability inside the authors’ experiments. It does not uniformly establish absolute accuracy because many comparisons use CAD, manufacturer values, another calibrator, or no physical ground truth. The source itself exposes important failure boundaries: insufficient six-degree-of-freedom excitation, weak forward translation for small-field-of-view LiDAR, weakly observable IMU intrinsics, association errors, and high camera/SfM cost. Reported runtime for a 40-second all-sensor sequence is 36.482 minutes, of which 28.305 minutes is COLMAP structure from motion.

The independent re-conceptualization is **calibration as upstream evidence infrastructure**. A transform file is not merely configuration; it is a claim about frames, clocks, observability, data, solver version, residuals, and uncertainty. Downstream world models, pose estimators, and controllers inherit that claim. The DEP-E is strongest where it makes this dependency visible and weakest where repeatability may be mistaken for accuracy.

### Principal strengths

- One state model and reference frame cover multiple sensor types and counts.
- Initialization is treated as a structured estimation problem, not a manual precondition.
- Sensor-specific residuals connect raw measurements to a shared continuous trajectory.
- Experiments span minimum sensor primitives and a combined suite with runtime evidence.
- The paper and DEP-E disclose meaningful observability, ground-truth, degeneracy, and cost limitations.

### Principal qualifications

1. Repeatability cannot exclude a stable biased solution.
2. Many “ground truth” values are rough, indirect, or unavailable.
3. Motion excitation requirements may be impractical or unsafe for some platforms.
4. Camera calibration is dominated by offline SfM cost.
5. The official repository is inspectable but was not built, and its license metadata warrants separate review.

---

## 1. The problem and research question

Multi-sensor systems require spatial extrinsics and temporal offsets so measurements of the same event align. Pairwise tools can produce inconsistent chains, require overlapping views or targets, and handle different sensor combinations through separate procedures. Complex rigs may include several IMUs, radars, LiDARs, and cameras with independent clocks and exposure mechanisms.

iKalibr asks whether one targetless, continuous-time, offline estimator can calibrate arbitrary supported combinations as long as at least one IMU is present and the recorded motion makes the parameters observable. “Resilient” means the formulation adapts to the available suite; it does not mean guaranteed recovery under arbitrary motion, noise, or failure.

The key research problem is joint identifiability. Extrinsic translation can trade against trajectory shape; time offset can trade against motion; rolling-shutter readout changes per-row timing; radar Doppler observes velocity components; LiDAR associations depend on provisional transforms; camera scale depends on visual geometry. The method addresses this by using continuous trajectories, sensor-specific constraints, careful initialization, robust losses, and staged optimization.

The practical stakes are upstream. Calibration error propagates into mapping, detection, fusion, world modeling, localization, forecasting, and control. A downstream model can appear weak when the actual defect is a stale transform or clock offset. Conversely, a low residual can hide degeneracy when the motion does not excite an axis.

---

## 2. Technical reconstruction

### 2.1 State and gauge

One IMU is the reference. Its frame and time define the gauge, while other sensors receive extrinsic rotations, translations, and time offsets relative to it. The state also includes rotation and linear spline control points, gravity, IMU biases and relevant intrinsics, rolling-shutter readout times, camera scale/inverse depth terms, and association-related variables.

Rotation is a uniform cubic B-spline on `SO(3)`. Relative control rotations are mapped through the Lie algebra and cumulative basis. The linear spline changes semantics with the suite: acceleration for IMU-only, velocity when radar supplies direct velocity information, and translation when LiDAR or cameras provide pose/geometry. This adaptive representation is a unification device because it models the quantity most directly constrained by available sensors.

### 2.2 Dynamic initialization

Initialization first recovers rotation from gyroscope measurements. With multiple IMUs, relative rotation and timing can be estimated in this stage. Sensor-inertial alignment then combines rotational motion with accelerometer integration, radar velocities, LiDAR/NDT positions, or camera/SfM positions to initialize remaining extrinsics, time offsets, gravity, and linear state. Finally, the appropriate linear B-spline is recovered.

The process is called dynamic because gravity and state can be recovered without assuming an initially static rig. This improves usability but does not remove observability requirements. The paper’s Table II records which parameters are introduced in each case. Initialization quality is central: the final problem is nonlinear, and weak starting states can lead to incorrect associations or local minima.

### 2.3 Associations and residuals

IMU and radar measurements can enter directly. LiDAR and cameras need associations. Multi-LiDAR points create a global map in an octree-like voxel structure; planarity and distance filters select point-to-surfel constraints. Visual structure from motion supplies landmarks and reprojection relations, with inverse depth and global/rolling exposure timing.

Five residual families enter the factor graph: gyroscope, accelerometer, radar Doppler, LiDAR point-to-surfel, and camera reprojection. Cauchy losses reduce the influence of dynamic targets and bad associations. Ceres solves the nonlinear least-squares objective. Robust loss reduces outlier leverage; it does not diagnose systematic bias or guarantee correct correspondence.

### 2.4 Progressive refinement

The solver does not free every variable at once. Early batches preserve more reliable inertial states while refining other sensors and visual variables. Later batches introduce additional IMU-related parameters. With LiDAR, the map and associations are rebuilt after estimates improve. This staged schedule is an implicit regularizer and convergence strategy.

No theorem guarantees global optimality, absolute accuracy, or observability for every suite. “All parameters initialized rigorously” is a source description of the derivation, not proof that every dataset supports them. Diagnostic rank, covariance, and held-out residuals are necessary companions.

---

## 3. Source inventory and integrity assessment

The DEP-E contains exactly `README.md` and `ikalibr_calibration_manuscript.md`. The README provides identity, tags, complete inventory, source-locality policy, item summaries, relevance, and a final Attribution Block. The manuscript supplies metadata, nine evidence groups, architecture and quantitative reconstruction, code status, claims, methodology, constraints, observations, improvements, three implementations, exercises, an MVP, source references, selection/integrity tables, and replication checklist.

The inventory matches the tracked files at the source commit. No PDF, HTML, TeX archive, extracted text, cache, dataset, ROS bag, binary, or `.source` directory exists. Public URLs cover arXiv, DOI, official repository, baseline repositories, and related DEP records. The record distinguishes paper evidence, implementation observations, process evidence, and contextual synthesis.

Direct inspection confirmed arXiv v2, five authors, revision date, full-text links, the published DOI, and the complete article structure. The HTML includes Tables I–IX, Figures 1–9, two appendices, acknowledgments, CRediT statement, and references. The official repository identifies itself as iKalibr multi-sensor calibration and exposes build/tutorial content. Code was not executed.

The DEP-E reports private local PDF, HTML, metadata, and source-package integrity checks. Those local files are not in the selected record, so their byte-level checks are treated as DEP-E-reported provenance. This run directly inspected the complete canonical HTML and metadata, satisfying the non-abstract evidence boundary without adding source documents to the repository.

---

## 4. Architecture and operational pipeline

The operational pipeline begins with sensor inventory and time/frame schemas, then recorded motion, initialization, association construction, progressive optimization, residual/repeatability analysis, and export of calibration parameters. A production-grade wrapper should add pre-solve excitation diagnostics, schema and unit validation, dataset provenance, held-out checks, uncertainty, and a signed evidence card.

The method is offline. Camera configurations depend on COLMAP SfM and dominate runtime. This is not a minor implementation detail: it defines when recalibration feedback is available. Systems that need online drift correction require a separate architecture or carefully bounded incremental extensions.

Calibration results should not be exported as anonymous YAML transforms. Each artifact should bind sensor aliases, firmware/configuration, source sequence, solver commit, parameter units, reference frame, time convention, residual summaries, observability warnings, uncertainty, and validity conditions. Downstream experiments should cite the calibration identifier.

---

## 5. Independent re-conceptualization

### 5.1 Calibration evidence gate

Reviewer inference: iKalibr is best treated as one producer inside a calibration evidence gate. The gate evaluates whether a calibration is sufficiently supported for a declared downstream use. It does not replace the solver. It assembles provenance, excitation, residuals, repeatability, held-out evidence, and policy thresholds.

The analogy breaks because no gate can turn weak data into accurate parameters. It can only expose missing evidence and block overconfident use. Acceptance is not a vehicle-safety certificate.

### 5.2 Multi-modal constraint brokerage

The solver brokers constraints from different modalities into one continuous state. Each modality constrains different derivatives and directions. The adaptive linear spline reflects this. This predicts that suite-specific observability reports will be more useful than one global “success” flag.

### 5.3 Transferable principle

The durable principle is **version the upstream coordinate claim**. Any system combining heterogeneous measurements should preserve the frame/time assumptions that made fusion possible. This applies to robotics, AR, industrial metrology, sensor networks, and multimodal datasets.

---

## 6. Experimental design and evidence reconstructed

The self-collected rig contains two cameras, two LiDARs, two 3D radars, and two IMUs, with 10 Hz exteroceptive sensors and 200/400 Hz inertial sensors. Software synchronization leaves constant offsets to estimate. Sequences span roughly 30–60 seconds in varied settings. Public LI-Calib, TUM GS-RS, and River data extend the evaluation.

Five configurations are reported: multi-IMU, multi-radar-inertial, multi-LiDAR-inertial, multi-camera-inertial, and combined camera/LiDAR/radar/inertial. Comparators include Mix-Cal, X-RIO-related references, OA-Calib, and Kalibr, with pseudo ground truth from CAD, manufacturers, or alternative methods where available.

The paper reports repeated calibration estimates, residual distributions, qualitative alignment, initialization-to-final changes, and runtime. This is broader than a single accuracy table. Yet the evidence mixes repeatability and accuracy. Many dimensions lack independent metrology. Different tools may use different data or assumptions. Short sequences do not establish long-term drift, temperature robustness, remount behavior, or environmental extremes.

The computation test uses Ubuntu 20.04, a 12th-generation Intel Core i9, ten optimization threads, and 40-second sequences. GPU details are not the central runtime driver reported. Camera configurations include a 28.305-minute SfM stage.

---

## 7. Results and quantitative audit

The DEP-E summarizes multi-IMU repeatability near 0.05 cm translation, 0.05 degrees rotation, and 1.0 ms timing. Radar parameters are less repeatable, around 0.8 cm, 0.8 degrees, and 1.8 ms, with Doppler residual standard deviation near 0.25 m/s. Camera estimates differ from target-based Kalibr by roughly 1 cm, 0.1 degrees, and 0.8 ms; rolling-shutter readout differs by less than 0.5 ms, and reprojection residuals are within approximately one pixel. These are source-reported summaries, not independent measurements.

Multi-LiDAR results expose a specific weakness: forward translation for the Livox Avia is poorly constrained under the demonstrated motion and field of view. The combined configuration retains that limitation. This negative result is valuable because it links a parameter failure to geometry and excitation rather than hiding it in an average.

Reported total runtimes in minutes are 0.072 (multi-IMU), 0.284 (multi-radar-inertial), 6.325 (multi-LiDAR-inertial), 29.332 (multi-camera-inertial), and 36.482 (all sensor types). The progression shows that association and SfM dominate complex suites. Runtime comparisons require identical sequence length and hardware, which the table provides for the reported cases.

The results support broad offline applicability and good repeatability under tested conditions. They do not prove sub-centimeter/sub-millisecond accuracy across all sensors. The independent assessment is **strong method coverage, promising repeated estimates, limited absolute-ground-truth evidence, and explicit suite-specific failure modes**.

---

## 8. Ablations and causal evidence

The paper presents initialization-to-final parameter changes and multiple suite configurations, but not a complete ablation of dynamic initialization, adaptive spline choice, Cauchy loss, progressive scheduling, map rebuild, or each residual family. Consequently, the causal contribution of each component remains partly inferred.

A high-value ablation would start the same datasets from naive, pairwise, and derived initialization and report convergence rate, wrong minima, residuals, and parameter error against metrology. Another would optimize all variables jointly from the start versus progressive batches. A third would freeze associations versus rebuild them.

Randomness is less obvious than in neural training, but association thresholds, spline knots, initial alignment, feature extraction, and solver tolerances can affect results. Repeatability across capture sessions is reported; solver sensitivity across configurations should also be archived.

---

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| One framework supports heterogeneous targetless spatiotemporal calibration. | Shared state, residual families, five suite experiments. | Strongly supported as formulation and implementation scope. | Requires at least one IMU and adequate observability. |
| Dynamic initialization improves convergence. | Derived initialization and staged results are documented. | Supported mechanistically; causal magnitude unresolved. | No comprehensive naive-initialization ablation. |
| iKalibr is highly accurate. | Repeatability and comparisons are favorable. | Promising but limited. | Physical ground truth is rough or absent for many parameters. |
| iKalibr is highly repeatable. | Tables III–VIII report low standard deviations for many sensors. | Supported under tested captures. | Stable bias remains possible; radar and LiDAR axes are weaker. |
| Targetless camera calibration is comparable to Kalibr. | Small reported differences and similar reprojection scale. | Supported under the reported setup. | Kalibr has target-derived scale and better translation repeatability. |
| One-shot joint calibration is superior to pairwise chains. | Shared reference and combined experiment. | Plausible but not comprehensively proven. | Full pairwise end-to-end comparison is absent. |
| The method is practical. | Public code and bounded sequences exist. | Practical for offline research; context-dependent. | Camera/all-sensor runtime and excitation are material constraints. |
| A successful solver output is safe for deployment. | No safety certification evidence. | Not established. | Needs uncertainty, held-out checks, and downstream acceptance policy. |

---

## 10. External primary-source context

The canonical arXiv record pins v2 and links the journal DOI.[^record] The complete HTML confirms the full technical and experimental structure. The IEEE DOI identifies the later publication in Transactions on Robotics.[^journal] The official repository exposes C++17/ROS-style calibration tooling and continued feature development.[^code]

The DEP-E connects iKalibr with HERMES, LA-Pose, and Self-Learned IDC. These are downstream consumers of spatial and temporal integrity: world modeling, learned ego-motion representation, and driving control. The connection is analytical, not experimental. None of those records validates iKalibr.

Baseline context includes Kalibr, OA-Calib/LI-Calib, Mix-Cal, and X-RIO. This review preserves their roles without claiming exhaustive contemporary superiority. Current repository features such as RGB-D support are later implementation state and are not retroactively treated as paper experiments.

---

## 11. Research notes and critical considerations

Observability should be an explicit artifact. The system should estimate per-axis sensitivity or information before optimization and disclose unobservable or weak directions. A global success flag hides the Livox forward-translation failure pattern.

Repeatability and accuracy must remain separate fields. A report should label reference type: independent metrology, manufacturer specification, CAD, target-based comparator, or unavailable. Confidence should be calibrated against held-out error rather than inferred from solver convergence.

Associations can fail systematically in dynamic scenes, sparse geometry, low texture, blur, or non-overlapping coverage. Robust loss reduces individual outliers but can still converge around biased structures. Hold-out measurements and perturbation tests are needed.

Calibration ages. Temperature, vibration, impact, maintenance, remounting, firmware, clock behavior, and lens changes can invalidate parameters. A maintenance ledger should connect each dataset and model evaluation to the calibration version used.

The official repository’s licensing signals should be resolved before redistribution. The DEP-E notes a BSD-style notice, Apache text, and incomplete package metadata. This is an implementation-governance gap, not a scientific refutation.

Calibration captures may contain faces, plates, buildings, and location traces. Data minimization, access control, retention limits, and public-safe aggregate reporting are required.

---

## 12. Potential implications

Scientifically, iKalibr shows how continuous-time state and modality-specific residuals can unify diverse calibration tasks. The broader lesson is to model the directly observed derivative—acceleration, velocity, or translation—rather than force one representation across all suites.

For engineering, calibration should be part of experiment provenance. Dataset manifests, model evaluations, and fusion logs should record the exact calibration identifier and its evidence card. This enables root-cause analysis when performance changes.

For deployment, an evidence gate can block use when excitation is insufficient, residuals are inconsistent, uncertainty is high, or parameters are stale. It should not automatically recalibrate or control a vehicle.

For governance, source-data privacy, software licenses, solver provenance, and acceptance thresholds need separate owners. A calibration tool is not a certification process.

---

## 13. Falsifiable hypotheses

### Hypothesis 1: pre-solve observability predicts bad axes

**Proposition:** A per-axis excitation/information diagnostic will predict the Livox-like translation failures before optimization.  
**Motivating evidence:** The paper connects forward translation error to limited field of view and insufficient motion.  
**Predicted observation:** Low diagnostic scores correlate with larger blinded metrology error.  
**Falsifier:** Diagnostics fail to distinguish accurate and inaccurate axes.  
**Minimum test:** Synthetic trajectories plus public sequences with controlled motion and known perturbations.

### Hypothesis 2: held-out residuals detect stable bias

**Proposition:** Residuals on measurements excluded from optimization will identify repeatable but biased calibrations better than in-sample residuals.  
**Motivating evidence:** Repeatability dominates several tables while absolute ground truth is limited.  
**Predicted observation:** Biased solutions show a larger held-out gap despite similar in-sample fit.  
**Falsifier:** Held-out residuals do not correlate with metrology error.  
**Minimum test:** Targetless fitting with independent target/metrology evaluation.

### Hypothesis 3: calibration perturbation explains downstream failures

**Proposition:** Small spatial/time perturbations will produce characteristic degradation curves in fusion and pose systems.  
**Motivating evidence:** Related DEP records depend on coherent geometry and timing.  
**Predicted observation:** Specific metrics respond monotonically within bounded perturbation ranges.  
**Falsifier:** Downstream results are insensitive or non-repeatable.  
**Minimum test:** Authorized offline dataset and frozen evaluator, with no live control.

---

## 14. Deployment and governance considerations

Appropriate use is offline calibration research and evidence generation in controlled environments. Poor fit includes unsupervised online correction, direct live-vehicle actuation, or acceptance without excitation and uncertainty checks.

Required safeguards include frame/unit schemas, reference-clock declaration, pre-solve observability, independent ground truth where possible, held-out residuals, uncertainty, versioned solver and data, privacy review, license bill of materials, human approval, rollback, and downstream calibration identifiers. Reports must state that acceptance is not a safety certificate.

---

## 15. Replication and falsification agenda

First, pin arXiv v2, the official repository commit, compiler, ROS distribution, Ceres and bundled dependencies, configuration files, and dataset revisions. Resolve licenses before redistributing any environment or dataset.

Second, reproduce one minimum suite—multi-IMU or radar-inertial—before the combined system. Verify units, frames, time conventions, initialization states, residual distributions, and table values. Archive failures and convergence diagnostics.

Third, add independent metrology for spatial and temporal parameters. Report accuracy separately from repeatability, with per-axis uncertainty and reference quality. Use repeated captures across motion, temperature, remounting, and environment.

Fourth, isolate causal components: derived versus naive initialization, joint versus progressive optimization, robust loss variants, fixed versus rebuilt associations, and spline choices. Measure convergence, error, runtime, and failure rate.

Fifth, build an observability and downstream-sensitivity program. Predict weak axes before solve, then perturb accepted calibration parameters and measure frozen world-model, pose, or fusion metrics offline.

The highest-priority falsifier is an independent metrology study showing stable but materially biased solutions despite favorable repeatability and residuals. That would narrow the claims and change acceptance policy.

---

## 16. Durable restatement

> iKalibr unifies targetless calibration of heterogeneous inertial sensor suites through continuous-time trajectories, derived initialization, modality-specific residuals, and progressive joint optimization. The paper demonstrates broad offline capability and strong repeatability, but absolute accuracy remains unevenly grounded and observability, association quality, and camera runtime materially constrain use.

The durable archival lesson is that calibration is an upstream evidence claim. Preserve not just transforms, but the data, frames, clocks, excitation, solver, residuals, uncertainty, reference quality, and downstream validity conditions that make those transforms believable.

---

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment | Boundary |
|---|---|---|---|
| DEP-E README | inventory, source policy, relevance, attribution | Sections 3 and 10 | repository metadata |
| Manuscript metadata/evidence | versions, sources, code, related DEPs | Sections 3 and 10 | code not run |
| Paper Sections I–II | problem and calibration families | Sections 1 and 10 | novelty scoped |
| Section III and equations | sensor models, B-splines, state | Section 2 | equations not rederived |
| Section IV / Figures 1–5 | system overview and sensor geometry | Sections 2 and 4 | diagrams qualitative |
| Section V / Table II | dynamic initialization and state recovery | Section 2 | no causal ablation |
| Section VI | associations, residuals, factor graph, progressive batches | Sections 2 and 4 | solver not executed |
| Section VII / Tables III–VIII | suite experiments and parameters | Sections 6 and 7 | mixed ground truth |
| Table IX | computation profile | Section 7 | author hardware/setup |
| Figures 6–9 | rig, repeated estimates, residuals, convergence/geometry | Sections 6–8 | visual evidence not reproduced |
| Section VIII | conclusion, limitations, future work | Sections 11 and 16 | boundaries retained |
| Appendices A–B | supplementary derivations/details | technical coverage in Section 2 | not independently rederived |
| Acknowledgments/CRediT/references | provenance and context | Section 10 | no hidden empirical claims inferred |
| DEP proposals and MVP | evidence gate, benchmark, maintenance ledger | Sections 12–15 | reviewer proposals |
| DEP integrity appendix | local PDF/HTML/source checks | Appendix B | private bytes unavailable here |

All nine numbered tables, nine numbered figures, central equation families, both appendices, and source-disclosed limitations are accounted for at the level material to the DEP record.

---

## Appendix B. Source and evidence notes

### Primary reviewed artifact

The complete source record `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration` at commit `398f692812550135476e8d560be1d2a01fa2982e` was inspected.[^dep] Both tracked files were read in full. Source action was review-only; no source file was modified, moved, copied, renamed, or reclassified.

### Directly inspected primary evidence

- https://arxiv.org/abs/2407.11420
- https://arxiv.org/html/2407.11420
- https://doi.org/10.1109/TRO.2025.3532506
- https://github.com/Unsigned-Long/iKalibr
- https://github.com/Delphoa/Black-Lake/commit/398f692812550135476e8d560be1d2a01fa2982e

### Evidence boundary

The complete DEP-E, canonical metadata, complete HTML paper, publisher locator, and official repository surface were inspected. No dataset, source archive, ROS bag, container, code, or solver was executed or committed. Reported measurements remain author-reported unless explicitly identified as direct metadata or structural inspection. Independent reproduction was not performed.

### Provenance pair

`BL-DEPPAIR-20260715-4FAD29AE` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. Intake/deposition become complete only with atomic submission of the DEP-A and both ledger rows.

---

## Footnotes

[^paper]: Chen et al., “iKalibr: Unified Targetless Spatiotemporal Calibration for Resilient Integrated Inertial Systems,” arXiv:2407.11420v2, complete HTML at https://arxiv.org/html/2407.11420.
[^record]: Canonical arXiv version and full-text links: https://arxiv.org/abs/2407.11420.
[^journal]: IEEE Transactions on Robotics publication DOI: https://doi.org/10.1109/TRO.2025.3532506.
[^code]: Official implementation: https://github.com/Unsigned-Long/iKalibr.
[^dep]: Source DEP-E: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration.
