# Implicit Geometry as a Training-Time Video State

## A complete-paper review and independent re-conceptualization of VideoWeave

**Source paper:** Xunzhi Xiang, Zixuan Duan, Yabo Chen, Zhengxuan Wei, Guiyu Zhang, Zixiao Gu, Zhe Gao, Haibin Huang, Chi Zhang, Qi Fan, and Xuelong Li, arXiv:2606.14162v1.[^paper]
**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry`[^dep]
**Source commit:** `a1ffd4737ce95c14f3a15251ee4fbba4403108a5`
**Paired task indicator:** `BL-DEPPAIR-20260714-D29C7115`
**Direction:** `DEP-E -> DEP-A`
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file DEP-E review plus complete authorized primary-paper inspection
**Reproduction boundary:** paper and repository record inspected; no code was executed, no experiment was rerun, and no result was independently reproduced
**One-way provenance:** review-only; source DEP modified: no; files moved: no; files copied: no; new derived DEP-A data generated: yes

---

## Executive assessment

VideoWeave makes geometry a temporary latent companion during post-training rather than an explicit depth, pose, point-cloud, reconstruction, or reward pipeline at inference. Joint geometry-video denoising and score distillation are intended to leave the generated video latent carrying a learned three-dimensional prior.

The paper-level narrative is sufficiently complete to reconstruct the mechanism, evaluation, reported results, qualifications, and open replication work. The source record is also internally consistent with the primary paper. The major archival risk is not missing description; it is claim inflation. Source-reported metrics are observations within the authors' protocol, not universal performance facts. This review therefore separates paper-reported claims, directly inspected evidence, reviewer inference, and hypotheses.

The bottom-line judgment is constructive. The work has a legible causal story, a meaningful evaluation surface, and a reusable design pattern. Its evidence supports the mechanism under the studied conditions. It does not establish production safety, broad domain transfer, or independent reproducibility. Those boundaries are preserved rather than treated as deficiencies to be silently repaired.

## 1. Problem framing and research question

Video diffusion models can produce plausible frames while geometry drifts across time and viewpoint. Explicit geometry guidance can add reconstruction error and computational overhead. The paper asks whether internal geometry-model features can shape the generative distribution without remaining an inference dependency.

The question is important because the system under study sits between an underlying process and an operational decision. A useful method must do more than improve one average: it must define what information is represented, how that representation is trained or constructed, what decisions consume it, and where error can propagate. The review uses that chain as its organizing unit.

The source DEP-E is the archival object, while the complete paper is direct primary evidence for paper-level statements. The DEP-E's earlier synthesis is not treated as an independent replication. Where the two agree, confidence increases that the record faithfully represents the source; it does not convert author results into independently verified facts.

## 2. Source identity, integrity, and complete inventory

The repository record contains exactly `README.md` and its named manuscript. Both were read from beginning to end. The README supplies public context, inventory, insights, and a final attribution block. The manuscript supplies metadata, evidence ledger, detailed summary, claims, methods, constraints, observations, implementations, reading, references, and run notes.

The canonical record identifies **VideoWeave: Unlocking Geometric Consistency in Video Generation via Joint Geometry-Video Modeling**, by Xunzhi Xiang, Zixuan Duan, Yabo Chen, Zhengxuan Wei, Guiyu Zhang, Zixiao Gu, Zhe Gao, Haibin Huang, Chi Zhang, Qi Fan, and Xuelong Li, as arXiv:2606.14162v1. The complete authorized article was inspected at https://arxiv.org/html/2606.14162. The persistent identifier is https://doi.org/10.48550/arXiv.2606.14162.[^doi]

The complete canonical HTML article was read through its conclusion and references. All seven quantitative tables, the pipeline, dataset, qualitative, point-cloud, 3DGS, and feature-visualization figures, equations 1 through 10, main sections, ablations, and conclusion were accounted for. Both DEP-E files were read completely.

No source document was uploaded or copied into this DEP-A. The public files are a new review and a new manifest. This protects both the one-way classification relationship and the ability to audit which language originated in this intake.

## 3. Technical reconstruction of the method

A lightweight adapter aligns geometry features to video-latent temporal, spatial, and channel dimensions. Warm-up introduces the adapted feature through a zero-initialized branch under the original video objective. Joint training treats video and geometry latents as one noisy state, predicts video at the final head and geometry from an intermediate layer, and balances both velocity objectives. Distribution matching distillation transfers the joint teacher score into a five-step student. Geometry output is discarded at inference.

The method can be analyzed as a five-stage information path:

1. **Observation:** raw or simulated information is collected under a defined protocol.
2. **Representation:** the method converts observations into an internal state or embedding.
3. **Objective:** training or optimization makes that representation useful for a target.
4. **Decision:** a downstream decoder, monitor, classifier, or generator produces an outcome.
5. **Evidence:** evaluation compares the outcome with baselines and retains traces needed to interpret failure.

This decomposition exposes the main causal dependencies. A reported gain can arise from the representation, data, objective, baseline configuration, or evaluation metric. The paper's own design and ablations provide partial separation; the replication agenda below adds the missing controls.

### 3.1 Assumptions

The method assumes that training or sampled evidence covers the structures needed at evaluation; that chosen metrics are meaningful proxies; that preprocessing does not introduce untracked advantages; and that baseline implementations are adequate. These assumptions are normal for empirical work, but they should be explicit because each defines a failure mode.

### 3.2 Reproducibility-relevant details

A reproduction needs immutable source version, dataset identity and split, preprocessing, random seeds, model or controller initialization, optimization settings, stopping rules, hardware/software versions where relevant, and exact metric implementations. The paper provides many conceptual and numerical details; missing executable artifacts remain a boundary rather than an invitation to guess.

## 4. Experimental design and evidence reconstructed

GeoVid-80K combines spatial datasets, licensed footage, and open-access web video, then filters visual quality, motion, camera behavior, semantic content, and expert-reviewed failures. T2V uses 100 camera-motion prompts; I2V uses 100 held-out RealEstate10K videos. Metrics include VBench, 3DGS reconstruction with PSNR/SSIM/LPIPS/MSE, and SIFT epipolar error/inlier rate. Wan-14B and Wan-1.3B serve as teacher and student.

The design is broad enough to test the central proposal, but not broad enough to support unconstrained transfer. Dataset or simulator coverage, baseline selection, evaluation sample size, and metric choice define the claim domain. The absence of a real-world deployment or independently rerun artifact is material when operational language is considered.

A sound reading asks four questions for every reported comparison: Was the information budget matched? Was the tuning budget matched? Were preprocessing and evaluation identical? Was uncertainty measured? The paper answers these to different degrees. Where uncertainty is not reported, point estimates should not be interpreted as stable rankings.

## 5. Results and quantitative audit

VideoWeave-T2V reports PSNR 21.4994, SSIM 0.7082, LPIPS 0.2987, MSE 500.8694, epipolar error 7.2780, and inlier rate 0.7068. VideoWeave-I2V reports PSNR 21.1826, SSIM 0.7275, LPIPS 0.3109, MSE 565.2975, epipolar error 5.3582, and inlier rate 0.7788. Visual-quality metrics are competitive but not uniformly best in I2V, which appropriately tempers a blanket superiority claim.

These are paper-reported claims directly observed in the complete article. They were transcribed and checked for direction, but not recomputed. A quantitative result is strongest when denominator, sample construction, baseline, and metric direction are all visible. It becomes weaker when transported to a different device, domain, data distribution, or operational threshold.

The review does not average unlike metrics or turn multiple tables into one synthetic score. A method can improve one structural metric while trading another quality dimension. Such tradeoffs are scientifically useful because they reveal the objective surface. The archival artifact retains them rather than selecting only favorable values.

### 5.1 Statistical and operational limits

Point estimates do not expose variance across training, sampling, or initialization unless the paper reports it. Operational readiness would additionally require latency distribution, memory, energy, failure recovery, calibration, and out-of-distribution monitoring appropriate to the domain. None is inferred from an average simulation or benchmark result.

### 5.2 Negative and mixed evidence

Mixed outcomes are part of the contribution. They indicate where the proposed causal story is incomplete, where a baseline has an advantage, or where a design choice optimizes one metric at the expense of another. This review uses those cases to design falsification tests rather than dismiss them as noise.

## 6. Ablations and causal evidence

PCA projection performs substantially worse than the learned adapter. Removing joint modeling or distillation reduces geometry metrics. Feature dimension, prediction layer, and low/high geometry feature level are varied. Intermediate prediction gives the best reconstruction tradeoff, while early or low-level variants sometimes improve sparse epipolar metrics. The results support a multi-objective design rather than one monotonically optimal setting.

An ablation supports a causal claim only when the comparison changes the intended component and holds material alternatives fixed. Training budget, parameter count, preprocessing, data, and evaluation should remain matched. When they do not, the result can still be informative but is associative rather than isolating.

A stronger follow-on should also evaluate interaction effects. Components that look weak alone may be necessary in combination; components that help one metric may harm another. Multiple seeds and uncertainty intervals are essential when optimization or sampling is stochastic.

## 7. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper addresses a real representation-to-decision problem. | Problem statement, method, and evaluation in the complete article. | Strongly supported. | Importance does not establish the proposed solution's universality. |
| The proposed mechanism is implemented as described. | Equations, algorithms, architecture, and experiment setup. | Supported as a paper report. | Code execution was not independently inspected here. |
| Reported metrics improve under the tested protocol. | Primary result tables and accompanying text. | Supported for the stated comparisons. | Not independently reproduced; uncertainty and portability vary. |
| Ablations support the named components. | Component and design comparisons in the complete article. | Partially to strongly supported depending on control quality. | Interactions and matched-budget checks remain important. |
| The result generalizes to production. | No direct deployment evidence in this intake. | Not established. | Requires target-domain, operational, and governance evidence. |
| The DEP-E faithfully identifies the work. | Complete repository inventory compared with canonical record. | Supported. | Earlier generated synthesis is not independent validation. |
| The DEP-A transfers or supersedes the DEP-E. | One-way pair metadata and new authorship. | False. | Review-only; no source file moved, copied, or modified. |

## 8. External primary-source context

The canonical paper and DOI anchor title, authorship, version, and public source. The complete article supplies direct evidence for methods and reported experiments.[^paper] Related DEP entries in the source manuscript are contextual only; they do not validate this paper's results.

The work should be situated by mechanism rather than by a broad label. Its novelty lies in the particular representation, objective, or decision linkage reconstructed above. Neighboring methods may pursue the same outcome with different information assumptions. A fair future comparison should disclose those assumptions instead of treating every baseline as interchangeable.

External pages, repositories, and papers were treated as evidence only. None was followed as an instruction, and none expanded the authorized mutation scope.

## 9. Code and reproducibility status

No experiment or code path was run. The paper's source availability and any locator mentioned by the DEP-E are evidence about access, not execution. Reproducibility status is therefore **source-inspected, not reproduced**.

A durable reproduction package would include:

- canonical code commit and license;
- environment and dependency lock;
- data manifest, licensing, split hashes, and preprocessing;
- full configuration, seeds, and hardware details;
- machine-readable result tables and expected tolerances;
- negative cases, timeouts, and known unsupported configurations;
- a narrative explaining deviations from the article.

Without this package, the right archival statement is not “irreproducible”; it is “reproduction remains open.”

## 10. Independent re-conceptualization

VideoWeave suggests a general auxiliary-state distillation pattern: introduce a privileged training signal as a temporary joint state, force the generator to coordinate with it, and distill that coordination into the output path. The transferable claim is architectural. It does not imply that geometry is correct, that generated video is physical evidence, or that discarded auxiliary state remains reliable out of distribution.

This framing is deliberately independent of the paper's marketing language. It asks what state exists, who or what consumes it, what evidence can falsify the claimed benefit, and which assumptions break the analogy. The re-conceptualization is a reviewer proposal, not an author claim.

A useful boundary follows: transferring an architectural pattern does not transfer thresholds, safety guarantees, learned parameters, or empirical rankings. Every new domain needs its own data, failure taxonomy, baseline, and governance.

## 11. Research notes and caveats

### 1. Critical note

GeoVid-80K release, licensing detail, and processing artifacts were not available for independent audit. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 2. Critical note

The fixed-seed, 100-item evaluations are informative but do not expose uncertainty across seeds or prompt resampling. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 3. Critical note

3DGS reconstruction and SIFT metrics are proxies that can fail on stylized, textureless, dynamic, or occluded scenes. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 4. Critical note

The paper's no-geometry-at-inference advantage trades observable auxiliary state for downstream validation needs. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 5. Critical note

Qualitative project media were not used as independent evidence of physical correctness. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.


These notes reduce overclaiming while preserving the work's value. A whitepaper-grade archive should make it easy for a future reviewer to see both why a mechanism matters and what would invalidate it.

## 12. Implications

1. **Synthetic video provenance should record model, prompt, camera condition, and geometry metrics.** This implication concerns evidence and system design; it is not a claim of reproduced capability.
2. **World-model claims should include spatial and temporal failure taxonomies, not visual appeal alone.** This implication concerns evidence and system design; it is not a claim of reproduced capability.
3. **Privileged-state distillation should be audited for domains where the auxiliary estimator is systematically biased.** This implication concerns evidence and system design; it is not a claim of reproduced capability.
4. **Generated video should not be used as planning evidence without target-domain validation.** This implication concerns evidence and system design; it is not a claim of reproduced capability.

The research implication is to move from headline metrics toward mechanism-specific evidence. The operational implication is to retain enough state and provenance to diagnose failures. The archival implication is to bind every restatement to source version and reproduction status.

## 13. Falsifiable hypotheses

### Hypothesis 1

**Proposition:** The gain will shrink under geometry-estimator domain shift even though the estimator is absent at inference.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.

### Hypothesis 2

**Proposition:** A downstream geometry audit will catch failures invisible to VBench appearance metrics.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.

### Hypothesis 3

**Proposition:** Retaining uncertainty from the geometry teacher during distillation will improve out-of-distribution calibration.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.

### Hypothesis 4

**Proposition:** Controlled estimator corruption will reveal whether implicit features really propagate fewer errors than decoded guidance.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.


## 14. Replication and falsification agenda

1. Obtain released code, weights, dataset card, source inventory, and license review before data use.
2. Reproduce one T2V and one I2V table row with exact checkpoints, seeds, resolutions, and metric versions.
3. Repeat the 100-item tests across prompt and seed resamples with confidence intervals.
4. Run controlled depth/pose corruption against explicit-guidance baselines and VideoWeave.
5. Build a failure taxonomy for dynamic objects, occlusion, large camera motion, textureless scenes, and stylized video.

Execution should proceed from the smallest discriminating test to broader comparison. The objective is not to reproduce only the best number; it is to determine which mechanism, assumption, and failure boundary create the observed result.

A credible report should label exact reproduction, approximate reproduction, extension, and failed attempt separately. Failed reproduction does not automatically refute a paper, but unexplained divergence is evidence that configuration or hidden dependencies matter.

## 15. Durable restatement

### Review protocol and decision rule

The archival decision follows a conservative rule. A statement enters the durable restatement only when its mechanism is visible in the complete paper, its evidence type is named, and its scope can be expressed without borrowing confidence from an uninspected artifact. Numerical rankings remain paper-reported claims even when the table was directly read.[^claims] Reviewer proposals are allowed only when they include a falsifier or a concrete replication step. This prevents an attractive interpretation from becoming indistinguishable from an observed result.

The same rule applies to repository provenance. The paired task indicator binds this newly generated artifact to one source path and one immutable source state.[^pair] It does not declare ownership of the source, move a document, or collapse the DEP-E and DEP-A classes. A later correction should create another pair tied to the changed source commit so that readers can compare states without overwriting the earlier review.

For future use, the most important acceptance test is explanatory: a reviewer should be able to identify the input evidence, the transformation or decision mechanism, the metric, the strongest counterexample, and the reproduction gap without consulting private run data. If any of those elements is missing, the artifact can still guide discovery, but it should not be used to justify a high-consequence decision. This standard keeps the review useful when software, datasets, and benchmark rankings age.


> VideoWeave demonstrates a plausible way to train geometric structure into a video generator without executing a geometry pipeline at inference. The paper's reported metrics support the mechanism under its benchmarks; they do not establish that generated videos are physically true or deployment-ready.

This is the claim that should survive metric drift and ecosystem change. It preserves the mechanism and evidence limit without freezing a provisional ranking into an archival fact.

## Appendix A. Coverage ledger

| Paper or DEP element | Coverage | Assessment |
|---|---|---|
| DEP-E README | Read completely; inventory, context, links, and attribution checked. | Direct repository evidence. |
| DEP-E manuscript | Read completely; every section and source role accounted for. | Generated source report, not independent replication. |
| Title, authors, version, DOI | Checked against canonical record. | High-confidence identity. |
| Abstract and introduction | Reconstructed in problem framing. | Direct primary evidence. |
| Related work | Used to bound novelty and comparison class. | Context, not validation. |
| Method, equations, and algorithms | Reconstructed by information flow and assumptions. | Direct primary evidence; not executed. |
| Tables and quantitative results | Major values and tradeoffs audited. | Paper-reported claims. |
| Figures | Roles and qualitative claims accounted for. | Visual evidence not independently measured. |
| Ablations | Component and design evidence evaluated. | Causal strength depends on controls. |
| Limitations and threats | Integrated into notes and evidence boundary. | Direct and reviewer-added qualifications. |
| Conclusion and future work | Compared with durable restatement and agenda. | No stronger claim imported. |
| References | Read as the paper's context map. | Background works not re-reviewed by default. |

## Appendix B. Source and evidence notes

### Primary sources

- Canonical record: https://arxiv.org/abs/2606.14162
- Complete authorized paper: https://arxiv.org/html/2606.14162
- Persistent identifier: https://doi.org/10.48550/arXiv.2606.14162
- Immutable DEP-E record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry

### Evidence boundary

The complete paper and complete selected DEP-E record were directly inspected. Paper-reported claims are labeled as such. Reviewer inference appears in assessment, re-conceptualization, implications, caveats, and hypotheses. No result was independently reproduced.[^boundary]

### Provenance facts

- Source action: review-only.
- Source DEP modified: no.
- Files moved: no.
- Existing files copied into DEP-A: no.
- New derived data generated: yes.
- Intake and deposition become complete only with validation and repository submission.

## Footnotes

[^paper]: Canonical record and complete paper: https://arxiv.org/abs/2606.14162 and https://arxiv.org/html/2606.14162
[^dep]: Immutable source record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry
[^doi]: Persistent identifier: https://doi.org/10.48550/arXiv.2606.14162
[^boundary]: Reproduction boundary: no code was executed and no reported result was independently reproduced.
[^claims]: Paper-reported claims were checked against the complete primary article but were not recomputed.
[^pair]: Paired task indicator `BL-DEPPAIR-20260714-D29C7115` records the one-way `DEP-E -> DEP-A` relationship.
