# Evidence and Priors in Single-Image Avatar Reconstruction

## A detailed review and re-conceptualization of “High-Fidelity Clothed Avatar Reconstruction From a Single Image”

**Source paper:** Tingting Liao, Xiaomei Zhang, Yuliang Xiu, Hongwei Yi, Xudong Liu, Guo-Jun Qi, Yong Zhang, Xuan Wang, Xiangyu Zhu, and Zhen Lei, CVPR 2023, pages 8662–8672.[^paper]
**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR`[^source-dep]
**Source commit:** `a1ffd4737ce95c14f3a15251ee4fbba4403108a5`
**Paired task indicator:** `BL-DEPPAIR-20260714-6EA931AE`
**Direction:** `DEP-E -> DEP-A`
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file DEP-E review; complete 11-page accepted-paper inspection; official repository context; technical, evidentiary, governance, and replication analysis
**Reproduction boundary:** no model, data, checkpoint, or code was run; all metrics are paper reports and were not independently reproduced
**One-way provenance:** source action review-only; source DEP modified: no; files moved: no; files copied: no; new derived data generated: yes

---

## Executive assessment

### The paper in one sentence

CAR reconstructs an animatable clothed human from one RGB image by learning a coarse canonical signed-distance surface, warping it into the observed pose, and optimizing fine surface details against predicted normals from a hyper-network initialization.

### The deeper idea

Single-view reconstruction cannot recover what the camera never observed. CAR manages that underdetermination by assigning different ambiguities to different mechanisms. SMPL and linear blend skinning provide an articulated coordinate system. A learned canonical implicit field supplies a general clothed shape. Predicted normals contribute local surface cues. A posed-space optimization loop restores details that canonical mapping blurs. A hyper-network converts a body prior into a useful starting point so refinement does not begin from random weights.

### Bottom-line judgment

The complete paper supports a strong method and simulation/dataset result under its protocol. CAR reports the lowest Chamfer and point-to-surface errors in its main comparisons across MVP-Human and RenderPeople canonical and posed settings. Ablations generally support SDF representation, canonical normals, and refinement. The evidence is weaker for the broad phrase “in-the-wild high fidelity”: real internet images receive qualitative rather than ground-truth evaluation, the single view cannot determine hidden geometry, and no uncertainty estimate marks prior-driven regions. Code availability improves inspectability, but no reproduction was run and the repository's complete asset/license readiness was not established in this intake.

### Principal strengths

- The two stages divide general shape and high-frequency detail cleanly.
- SDF, normals, and articulation priors are technically aligned with surface reconstruction.
- Evaluation covers canonical and posed outputs, multiple datasets, baselines, ablations, and runtime.
- The hyper-network has a measurable operational role: fewer refinement iterations.

### Principal qualifications

1. A single image provides no direct evidence for occluded or back-facing geometry.
2. Quantitative tests use datasets and synthetically generated training data; internet images are qualitative.
3. Baseline handling is mixed: some official models are used, while ARCH and ARCH++ are retrained by the authors.
4. Consent, identity, demographic coverage, and uncertainty are not core evaluated outcomes.

## 1. The problem the paper is actually solving

High-quality avatar creation normally relies on scanners, multi-camera rigs, depth sensors, or monocular video with temporal optimization. CAR targets a cheaper input: one unconstrained RGB photograph. The desired output is harder than a static visible-surface mesh. It should have clothing details, exist in a canonical pose suitable for animation, reconstruct the original posed geometry, and support reposing.

The problem is ill-posed. Clothing hides body shape; the rear surface and self-occluded regions are absent; camera and pose estimates can be wrong; loose garments break naked-body topology; and local image texture does not uniquely determine depth. Prior methods make different tradeoffs. Pixel-aligned implicit functions can digitize static humans but may smooth detail or fail under unusual poses. Body-conditioned implicit methods add robustness but can overfit the naked-body prior. ARCH-style methods provide a canonical, animatable output but can lose high-frequency clothing geometry. Optimization methods can recover detail but are slow.

CAR asks whether a learning-plus-optimization pipeline can achieve both efficiency and fidelity: learn the broadly plausible canonical surface, then refine the instance using image-derived normals.

## 2. Formal and technical reconstruction

### 2.1 Inputs and coordinate spaces

The input image is passed through existing body-guided models to predict front and back normal maps and an SMPL body. CAR distinguishes canonical space, where articulation is normalized, from posed space, where the person appears in the image. Linear blend skinning maps canonical vertices to the target pose using joint transforms and skinning weights; an inverse mapping brings posed evidence back to canonical coordinates.

This coordinate split is the central representation. Canonical space simplifies animation and shape learning, while posed space preserves image-aligned detail. Errors in pose, body estimate, skinning weights, or camera projection can propagate into both stages.

### 2.2 Canonical implicit model

The first network predicts a signed distance value for a query point. Its inputs combine pixel-aligned image features from predicted normals, the query's canonical normal feature, and a positional encoding of the canonical coordinate. The zero level set defines the reconstructed surface.[^method]

An SDF provides more than inside/outside occupancy. Near the surface, its gradient supplies a normal and should have unit magnitude. CAR trains with three terms. A surface reconstruction term drives SDF values to zero at known surface points and aligns gradients with target normals. An Eikonal term encourages unit gradient for points in the volume. An off-surface term pushes distant points away from the zero level. The paper uses weights 1, 0.1, and 0.1 for these terms.

The network fuses image evidence and geometry prior. Pixel alignment anchors visible cues; canonical normals describe local surface orientation after transformation; position allows the implicit field to represent spatially varying structure. The learned output is a coarse canonical clothed mesh.

### 2.3 Posed-space normal refinement

Canonical mapping can blur or misplace detail because estimated articulation is imperfect. CAR warps the coarse mesh into posed space and fits another SDF network so its rendered or projected surface normals align with predicted front and back normal images. Using an implicit field avoids fixed mesh topology and per-vertex displacement artifacts, which is especially relevant for loose clothing.

The refinement is still constrained by predictions, not direct depth. If the normal estimator hallucinates folds or fails on unusual garments, the optimization can confidently reproduce the mistake.

### 2.4 Hyper-network initialization

Optimizing a new SDF network from random parameters for every person is expensive. CAR trains a hyper-network that consumes an SMPL body mesh and emits the parameter initialization of the refinement SDF. The body is unclothed and topologically regular, making it a stable conditioning object. The initialized network approximates a human body before clothing-specific normal fitting begins.

The paper reports roughly 1,500 refinement iterations with hyper-network initialization versus 3,000 from random initialization. Both stages together average about five minutes on one TITAN X GPU, compared with hours claimed for selected optimization approaches.[^runtime] This is not interactive in the modern product sense, but it is a meaningful reduction for per-subject optimization.

### 2.5 Training details and inherited components

The paper trains the canonical model with Adam, batch size four, 512-by-512 crops, learning rate 1e-3 decayed every three epochs, and surface/near-surface/volume point sampling. The normal prediction network and SMPL estimation come from prior work rather than being new CAR modules. Network layer dimensions and skip connections are specified in the complete paper.

The method's novelty must therefore be scoped: CAR combines inherited body/normal estimators, a canonical SDF with canonical normals, posed-space implicit refinement, and hyper-network initialization. It is not the first pixel-aligned implicit model, SDF, SMPL-conditioned system, or hyper-network.

## 3. Architecture and information flow

The end-to-end pipeline is: ingest RGB image; estimate SMPL pose/body and front/back normals; transform evidence into canonical coordinates; evaluate the canonical SDF; extract a coarse zero-level mesh; apply linear blend skinning into the observed pose; initialize a posed SDF network from the hyper-network; optimize that SDF against image normals; extract the detailed posed surface; and retain a canonical representation for animation/reposing.

Resource allocation is asymmetric. The first stage amortizes learning across people and runs as inference. The second spends per-person optimization budget. The hyper-network shifts part of that budget back into amortized training. This is a learned initialization strategy rather than an end-to-end single forward pass.

The output has no mathematical guarantee of physical truth. The SDF and Eikonal losses impose geometric regularity, while SMPL and normals impose prior/evidence consistency. They cannot prove the unobserved surface is correct. Validation occurs through held-out mesh metrics and qualitative rendering.

## 4. Experimental design and evidence reconstructed

### 4.1 Data

The paper reports training on 100 MVP-Human subjects and 50 RenderPeople subjects. Testing uses 50 MVP-Human scans, 11 RenderPeople scans, and real internet images for qualitative evaluation. The training data are synthetically generated from available scans and poses. The exact subject diversity, licensing, garment distribution, camera distribution, and train-test identity isolation require dataset-level review beyond this paper.

The evaluation separates canonical and posed surfaces. This matters because a method can reconstruct a visually plausible pose yet fail to provide a stable canonical mesh for animation.

### 4.2 Baselines

Static clothed-human baselines include PIFu, PIFuHD, and ICON. Animatable-avatar baselines include ARCH and ARCH++. The paper uses official published models for PIFu, PIFuHD, and ICON, but trains ARCH and ARCH++ on its own training set. This improves data alignment for the avatar methods but makes hyperparameter and implementation parity important.

PIFu-family and ICON models do not provide canonical animatable outputs in the same way, so dashes appear in some table cells. Main-table superiority should be interpreted task by task rather than as one universal ranking.

### 4.3 Metrics

Chamfer distance compares point sets bidirectionally. Point-to-surface distance measures how far predicted points lie from a target surface. Normal error measures orientation agreement. Lower is better for all three. These aggregate metrics can miss local semantic failures: face, hands, hair, hems, garment openings, assistive devices, and occluded backs may matter more than mean distance.

The paper does not report uncertainty intervals, statistical tests, or multiple training seeds in the main table. Mesh samples and alignment procedure also affect distances and must be fixed for reproduction.

## 5. Results: what is reported and what it means

In Table 2, CAR reports MVP-Human canonical Chamfer 1.0572 and P2S 1.0811; posed Chamfer 1.0771, P2S 1.0654, and normal error 0.0902. For RenderPeople, it reports canonical Chamfer 1.5401, P2S 1.4963, normal 0.0821; and posed Chamfer 1.5142, P2S 1.4147, normal 0.0871.[^results]

Those Chamfer and P2S values are the lowest available across the main table. CAR does not win every normal cell: for example, ARCH reports a lower MVP canonical normal error. The paper's broad “best accuracy” wording is therefore most defensible for Chamfer/P2S and the combined evaluated task, not every metric entry.

Qualitative figures show canonical, posed, and reposed avatars, baseline comparisons, and internet images. They support visual plausibility and animation capability, but qualitative selections cannot establish average real-world accuracy. No ground-truth mesh exists for the internet images.

The reported runtime of about five minutes is far faster than hours-long optimization examples but slower than pure feed-forward reconstruction. It was measured on one TITAN X and cannot be directly translated to another GPU without implementation and workload details.

## 6. Ablations and causal evidence

Table 3 compares a baseline without geometry feature or refinement, addition of the geometry feature, and addition of refinement on RenderPeople. Geometry improves Chamfer/P2S, while refinement further improves P2S and normal error but slightly worsens some Chamfer values. The evidence supports complementary roles, not a uniform improvement in every metric.

Table 4 compares occupancy and SDF losses and three geometry features: point-to-joint distance, signed distance to SMPL, and canonical surface normal. The authors conclude SDF and canonical normals are best overall. The displayed values are more nuanced: SDF improves mean P2S and normal error but not mean Chamfer in that comparison, and the best geometry feature depends on the metric. Canonical normal has the lowest mean Chamfer, while signed distance has the lowest mean P2S in the shown rows. This is an internal qualification to the strongest prose claim.

The hyper-network iteration comparison supports faster convergence but would be stronger with equal-quality curves, multiple subjects, and time rather than iteration alone. A direct no-back-normal or corrupted-pose ablation would clarify dependence on inherited estimators.

## 7. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| CAR combines learned canonical shape with optimized posed detail. | Method, Figure 2, equations, and inference pipeline. | Strongly supported. | Relies on inherited SMPL and normal estimators. |
| SDF is better than occupancy. | Table 4 and method rationale. | Partially supported. | Wins some aggregate metrics, not every cell. |
| Canonical normals are the best geometry feature. | Table 4 and qualitative rationale. | Metric-dependent support. | Signed distance has a better mean P2S in displayed values. |
| CAR has the best main-table reconstruction. | Table 2. | Supported for reported Chamfer/P2S. | Not every normal metric; no independent reproduction. |
| Hyper-network initialization accelerates refinement. | 1,500 versus 3,000 iterations and runtime discussion. | Promising and mechanistically credible. | Needs equal-quality timing across more subjects. |
| CAR handles arbitrary clothing and real scenes. | Selected qualitative internet images. | Overbroad. | No ground-truth or distribution-wide real-image evaluation. |
| Outputs are faithful reconstructions. | Dataset metrics and visual examples. | Supported for tested visible/dataset geometry. | Hidden regions remain prior-driven and uncertain. |

## 8. External primary-source context

The Computer Vision Foundation identifies the document as the Open Access version of the accepted CVPR 2023 paper and states that it is identical apart from the watermark.[^paper] The paper is 11 pages including references and ends cleanly. The arXiv record is 2304.03903. The official repository is linked from the paper and provides implementation context.[^code]

Prior-work context includes PIFu/PIFuHD for pixel-aligned surfaces, ICON for normal/body priors, ARCH/ARCH++ for animatable canonical avatars, and optimization/video methods. CAR's novelty is therefore a particular coarse-to-fine composition and hyper-network initialization, not the component families alone.

Artifact classification is “available and inspectable at repository/README level.” It is not “runnable” or “result reproduced.” A complete reproduction would need SMPL assets, dataset access, pretrained normal/body components, checkpoints, dependencies, and clear licenses.

## 9. Independent re-conceptualization: an evidence-prior surface ledger

CAR can be viewed as a ledger that assigns every reconstructed surface region to a mixture of evidence and prior. Visible image features provide direct cues. Predicted normals provide learned local evidence. SMPL provides anatomical and articulation prior. Canonical SDF learning supplies a population prior over clothed shape. Posed refinement enforces instance consistency. Hidden regions lean most heavily on priors.

The current system blends these sources inside a surface without exposing their proportions. A more reviewable system would output a provenance map: visible evidence-supported, cross-view or symmetry inferred, body-prior dominated, normal-model dominated, and optimization-adjusted. This does not change the mesh alone; it changes what a user can trust.

**Boundary of the analogy:** neural features do not decompose cleanly into percentages, and a surface point can depend on global evidence. The ledger would be an operational approximation, not a causal proof.

The interpretation predicts that errors will cluster where prior weight is high: backs, occlusions, loose clothing, hair, and pose-estimation failures. It also suggests uncertainty calibration as a natural extension.

## 10. Research notes and critical considerations

The strongest numerical result can coexist with a visually consequential local failure. Region-stratified metrics should supplement global mesh averages.

“High fidelity” is partly a perceptual claim, yet the paper does not provide user studies or perceptual thresholds. Geometric distance is necessary but not sufficient for perceived identity or garment accuracy.

The normal predictor is a hidden bottleneck. Because both canonical features and refinement use normals, correlated errors may propagate twice. Independent normal-quality stratification is needed.

Human-image reconstruction carries consent and identity risk. A technically accurate method can be misused on third-party photographs. Source-data governance, face/background filtering, retention policy, deletion, and restrictions on public sharing are deployment requirements even though they are not central paper experiments.

The paper reports funding from multiple public and industry programs and acknowledges the relevant support. No conflict or limitation section systematically addresses governance.

## 11. Implications

Scientifically, CAR supports hybrid amortized-plus-optimization reconstruction. System designers can reuse the pattern when one forward pass captures global structure but instance-specific detail needs constrained fitting. The key is a learned initializer and a validator tied to observed evidence.

Appropriate deployment is limited to user-owned or explicitly consented imagery with transparent quality limits. Poor-fit cases include severe occlusion, unsupported garments, children or vulnerable subjects without robust consent, multiple people, nonstandard bodies, and uses requiring metrically verified hidden geometry. Safeguards should include consent records, no default source retention, deletion controls, regional uncertainty, manual preview, watermark/provenance where appropriate, and refusal for third-party identity capture.

## 12. New hypotheses derived from the paper

These are reviewer hypotheses, not established findings.

### Hypothesis 1: uncertainty tracks visibility and normal disagreement

**Proposition:** regional reconstruction error can be predicted from view visibility, disagreement between front/back normal estimates, and distance from SMPL.
**Predicted observation:** an uncertainty model ranks occluded and loose-garment failures above visible torso regions.
**Falsifier:** these signals are uncorrelated with held-out mesh error.
**Minimum test:** synthetic multi-view renders with known visibility and region-level ground truth.

### Hypothesis 2: correlated normal errors dominate refinement failure

**Proposition:** because normals enter both stages, their systematic errors explain more failure variance than SDF architecture choices.
**Predicted observation:** supplying ground-truth normals produces a much larger gain than changing the implicit network.
**Falsifier:** ground-truth normals yield little improvement.
**Minimum test:** cross the normal source and SDF variant in a controlled ablation.

### Hypothesis 3: hyper-network benefit depends on garment distance from the body prior

**Proposition:** initialization saves more time for body-adjacent clothing and less for topology or volume far from SMPL.
**Predicted observation:** iteration savings shrink for dresses, coats, and large accessories.
**Falsifier:** savings are uniform across garment categories.
**Minimum test:** report convergence curves stratified by garment-body distance.

## 13. Replication and falsification agenda

First, pin the paper, official repository commit, environment, pretrained assets, SMPL license, and dataset versions. Verify whether every checkpoint and script named by the README is obtainable and licensed.

Second, reproduce one RenderPeople table using the exact mesh alignment and sampling protocol. Run multiple seeds for trainable components and bootstrap subjects for confidence intervals. Preserve both aggregate and region-level metrics.

Third, rerun Table 4 and reconcile the prose with metric-specific winners. Add no-normal, ground-truth-normal, perturbed-pose, and zero-versus-hyper initialization controls. Plot quality versus iterations and wall time.

Fourth, create a synthetic visibility benchmark with known back surfaces and occlusions. Evaluate visible and hidden regions separately and calibrate uncertainty. Success requires high uncertainty where hidden errors are large.

Fifth, conduct a consented real-image study with multi-view or scan ground truth. Stratify by garment, body shape, pose, camera, skin tone, hair, and assistive devices. Archive failure modes without publishing identity-sensitive inputs.

The method's strongest claims would be falsified if gains disappear under common training/data protocols, if hidden-region error is unacceptable despite good global metrics, or if hyper-network speed does not hold at equal output quality.

## 14. Durable restatement

> CAR combines a learned canonical SDF, articulation/body priors, predicted normals, and a hyper-network-initialized posed-space refinement to build animatable clothed avatars from one image. It reports strong held-out mesh metrics and faster optimization, but unobserved geometry remains prior-driven and real-image fidelity is qualitatively rather than quantitatively established.

The durable lesson is that sparse reconstruction should expose which output regions are supported by observation and which are synthesized by priors.

## Appendix A. Complete table and figure coverage ledger

### Tables

1. **Table 1, implicit-function comparison:** locates CAR among pixel features, body features, normals, and coordinates.
2. **Table 2, main quantitative comparison:** covers canonical/posed MVP-Human and RenderPeople metrics; CAR leads Chamfer/P2S but not every normal cell.
3. **Table 3, module ablation:** baseline, geometry feature, and refinement; gains are metric-dependent.
4. **Table 4, loss and geometry-feature ablation:** SDF versus occupancy and three prior features; prose is stronger than some individual cells.

### Figures

1. **Figure 1:** input, posed reconstruction, canonical reconstruction, and reposed output; states the task.
2. **Figure 2:** complete CAR pipeline; central architecture evidence.
3. **Figure 3:** qualitative baseline comparison on RenderPeople; useful but selected.
4. **Figure 4:** canonical to animated examples; supports animatability.
5. **Figure 5:** internet images; supports plausibility, not measured real-world accuracy.
6. **Figure 6:** module ablation visuals; complements Table 3.

### Equations

- Equation 1 defines the canonical SDF zero set.
- Equations 2–4 define LBS, pixel-aligned features, and transformed normals.
- Equations 5–8 define reconstruction, Eikonal, and off-surface losses.
- Hyper-network and refinement objectives define initialization and normal alignment; all central families were inspected.

## Appendix B. Source and evidence notes

### Primary reviewed artifact

Both DEP-E files were read fully. The CVF paper contains 11 pages, method, experiments, conclusion, acknowledgments, references, four tables, six principal figures, and central equations. The source integrity check found a complete ending and venue identity.

### External primary sources

- https://openaccess.thecvf.com/content/CVPR2023/html/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.html
- https://openaccess.thecvf.com/content/CVPR2023/papers/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.pdf
- https://arxiv.org/abs/2304.03903
- https://github.com/TingtingLiao/CAR

### Evidence boundary

Paper reports are explicitly attributed. Complete primary-paper text and visual/table locations were inspected. The official repository was not cloned or executed, datasets were not downloaded, and metrics were not independently reproduced. Reviewer inference appears in the evidence-prior model, governance analysis, and hypotheses.

## Footnotes

[^paper]: CVPR Open Access record and complete accepted paper: https://openaccess.thecvf.com/content/CVPR2023/html/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.html
[^source-dep]: Immutable source DEP-E: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-Clothed%20Avatar%20CAR
[^method]: Complete paper method and equations: https://openaccess.thecvf.com/content/CVPR2023/papers/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.pdf
[^runtime]: Inference-speed discussion in the complete paper: https://openaccess.thecvf.com/content/CVPR2023/papers/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.pdf
[^results]: Quantitative tables in the complete paper: https://openaccess.thecvf.com/content/CVPR2023/papers/Liao_High-Fidelity_Clothed_Avatar_Reconstruction_From_a_Single_Image_CVPR_2023_paper.pdf
[^code]: Official repository: https://github.com/TingtingLiao/CAR
