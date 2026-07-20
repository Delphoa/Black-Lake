---
title: "AR-Drag Motion Control - DEP-E"
generated_at: "2026-07-20"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of AR-Drag, a few-step autoregressive video diffusion model with Self-Rollout and GRPO motion alignment."
source_status: "verified local bundle; original source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-20"
temporal_cutoff: "arXiv v3 revised 2026-03-08; public context checked through 2026-07-20"
primary_url: "https://arxiv.org/abs/2510.08131"
stable_identifier: "arXiv:2510.08131v3; DOI:10.48550/arXiv.2510.08131"
confidence_summary: "High for identity, method, and reported table values; medium for causal and deployment interpretation because results were not independently reproduced."
safety_scope: "research review, bounded evaluation planning, and responsible synthetic-media implementation ideation"
distribution_notes: "Public Markdown only; PDF, HTML, metadata, source package, extracted text, renders, caches, and verification records remain local and were not uploaded."
---

# AR-Drag Motion Control - DEP-E

## Source Metadata

| Field | Value |
|---|---|
| Paper title | *Real-Time Motion-Controllable Autoregressive Video Diffusion* |
| Authors | Kesen Zhao; Jiaxin Shi; Beier Zhu; Junbao Zhou; Xiaolong Shen; Yuan Zhou; Qianru Sun; Hanwang Zhang |
| Source platform | arXiv, Computer Science - Computer Vision and Pattern Recognition |
| Submitted | 2025-10-09 |
| Reviewed revision | arXiv v3, revised 2026-03-08 |
| Venue status | ICLR 2026 Poster |
| Stable identifiers | arXiv:2510.08131v3; DOI:10.48550/arXiv.2510.08131; OpenReview forum `4Q55RwYte9` |
| Subject | Computer Vision and Pattern Recognition (`cs.CV`) |
| Primary URLs | https://arxiv.org/abs/2510.08131; https://arxiv.org/html/2510.08131; https://arxiv.org/pdf/2510.08131; https://arxiv.org/e-print/2510.08131 |
| Project page | https://kesenzhao.github.io/AR-Drag.github.io/ |
| Venue URL | https://iclr.cc/virtual/2026/poster/10011557 |
| License visibility | arXiv links CC BY-NC-ND 4.0; redistribution was not assumed or performed |
| Collected formats | Complete PDF, full-paper HTML, metadata HTML, TeX/source package, extracted text, selected page renders, and local verification records |
| Collection status | Verified complete after a bounded repair supplied missing full-paper HTML and companion artifacts |
| Public path policy | Local source paths are intentionally withheld from this public artifact |
| Code/data status | Supplementary pseudocode and settings were inspected; no official public implementation repository or downloadable 206-clip benchmark was established; no experiment was run |
| Access date | 2026-07-20 |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | Verified complete local bundle for arXiv:2510.08131v3 | Primary paper bundle | Full 20-page paper, equations, Algorithms 1-2, Listings 1-2, Tables 1-3, Figures 1-6, appendix, ethics, reproducibility, limitations | Mechanism, data/evaluation setup, metrics, ablations, stated limitations | High | Experiments were inspected, not reproduced; source files are withheld |
| E2 | https://arxiv.org/abs/2510.08131 | Official metadata | Title, authors, dates, subject, DOI, version history, public artifact links, license | Identity and versioning | High | Abstract alone cannot support empirical claims |
| E3 | https://kesenzhao.github.io/AR-Drag.github.io/ | Official project page | Motivation, pipeline overview, qualitative comparison framing, streaming-input description | Author/project context | Medium-high | Gallery requires JavaScript; qualitative claims were not independently scored |
| E4 | https://iclr.cc/virtual/2026/poster/10011557 | Official venue record | ICLR 2026 Poster status, title, authors, abstract | Publication context | High | Does not provide the full experimental record |
| E5 | https://openreview.net/forum?id=4Q55RwYte9 | Official forum locator | Stable review identity | Publication context | Medium | Forum content was challenge-gated during inspection |
| E6 | Three related Black Lake artifacts | Curated research records | Geometry-aware distillation, bounded KV history, instance-specific context absorption | Cross-DEP synthesis | Medium-high | Their experiments were not rerun here |
| E7 | Live Black Lake and Black-Lake-Data READMEs | Repository authority | DEP layout, attribution, source locality, dedup scope, publication index | Deposit procedure | High | Repository rules, not research evidence |
| E8 | Local source-integrity verification | Verification record | PDF/HTML/source checks, byte counts, structure metrics, zero partials | Complete-source gate | High | Public summary omits local paths and source bytes |

## Executive Summary

AR-Drag is a 1.3B-parameter, frame-wise autoregressive image-to-video diffusion model designed for interactive trajectory control. It starts from Wan2.1-1.3B-I2V, learns trajectory conditioning in a bidirectional teacher, distills that teacher into a three-step causal student, replaces teacher-forced history with full Self-Rollout, and applies GRPO using sparse stochastic exploration plus aesthetic and trajectory-alignment rewards.

The strongest reported evidence is Table 1 on a 206-clip author-curated benchmark. AR-Drag reports 0.44-second first-frame latency on one NVIDIA H20, FID 28.98, FVD 187.49, aesthetic quality 4.07, motion smoothness 0.9948, and motion consistency 4.37, the best displayed value in all six columns. Ablations report that removing RL worsens FID to 31.65 and consistency to 4.12, while removing Self-Rollout worsens FID to 38.13 and FVD to 353.75. A bidirectional teacher retains stronger FVD and aesthetic quality but requires 45.64 seconds, so the result is a quality-latency trade rather than uniform dominance.

Confidence is high that the paper reports the method, settings, and numbers: the complete v3 PDF, official HTML, source, rendered tables/figures, appendix, and venue record were inspected. Confidence is medium for causal and deployment claims. No run was reproduced; point estimates lack visible multi-seed uncertainty; Motion Consistency reuses the proposed tracking-based reward; the benchmark and training corpus are not established as public releases; data provenance is limited; and latency covers first-frame generation on one accelerator rather than the entire interactive path.

## Detailed Summary

### Problem and Motivation

Bidirectional video diffusion denoises a complete clip jointly. This can provide strong global coherence, but it delays output and requires future controls before generation begins. Autoregressive video diffusion can emit frames and accept control updates sequentially, yet few-step generation amplifies exposure bias, artifacts, and motion-control error. Standard teacher forcing conditions training on clean history even though inference conditions on the model's own generated frames.

AR-Drag asks whether inference-aligned autoregressive training and reward-driven trajectory control can close that quality gap without giving up interactive latency.

### Stage 1 - Motion Conditioning and Distillation

The training mixture contains approximately 10,000 real and synthetic videos. Synthetic videos are produced with Wan2.1-14B-I2V. An automatic tracker generates trajectories, manual filtering removes sensitive, low-quality, or incorrectly tracked examples, and about 3,000 difficult videos involving occlusion or fast motion are fully annotated. Each example includes a reference image, positive and negative prompts, and trajectory heatmaps.

A bidirectional Wan2.1-1.3B-I2V teacher is fine-tuned with flow matching. Its student replaces bidirectional attention with causal attention and uses DMD plus adversarial losses to reach a three-step frame-wise sampler. The schedule is reported as `t0=1000`, `t1=755`, `t2=522`, `t3=0`; the default chunk size is one and KV cache size is seven frames.

### Self-Rollout

Self-Rollout samples a supervised denoising position for each frame, computes loss at that point, then continues the remaining denoising steps without gradients until a clean model-generated frame is available. That generated frame updates the KV cache and becomes context for the next frame. Self-Forcing instead collapses the remainder of the denoising trajectory into one update, which the paper argues does not match the defined sequential MDP.

The central reviewer interpretation is that Self-Rollout restores a more faithful transition graph; it does not prove that all real inference state is Markov. A fixed-size KV cache, latent decoder state, prompts, scheduler state, and external control stream can still create partial observability or implementation-specific dependence.

### Stage 2 - GRPO and Reward Design

The paper treats each denoising transition as an action in a frame-by-frame MDP. To make a deterministic flow sampler suitable for exploration, it converts one randomly selected denoising step to an SDE update and leaves other steps on the deterministic ODE solver. This selective stochasticity aims to avoid the variance and rollout cost of adding noise at every point in a frame-count-by-step-count horizon.

For each prompt/control condition, a group of sampled videos receives per-frame rewards after full denoising. The quality term is a LAION aesthetic predictor. The motion term uses Co-Tracker to estimate generated trajectories and applies a clipped distance-based reward relative to target trajectories. GRPO standardizes each sample's reward against its group, applies a clipped importance-ratio objective, and regularizes against a reference policy.

This reward is practical but not neutral. Tracker error, occlusion, object ambiguity, and aesthetic-model bias can become training pressure. Because Motion Consistency is also computed from the proposed reward model, independent trackers and human raters are needed to measure whether optimization generalizes beyond the reward oracle.

### Experiments and Results

Training uses AdamW at learning rate `1e-5` on eight NVIDIA H20 GPUs without LoRA. The benchmark contains 206 clips with diverse trajectories and scenes. First-frame latency is measured on one H20. DragNUWA, DragAnything, Tora, MagicMotion, and an adapted Self-Forcing baseline are compared.

| Method | First-frame latency (s) | FID | FVD | Aesthetic | Motion smoothness | Motion consistency |
|---|---:|---:|---:|---:|---:|---:|
| DragNUWA | 94.26 | 36.31 | 376.39 | 3.30 | 0.9759 | 3.71 |
| Tora | 176.51 | 32.84 | 283.43 | 3.86 | 0.9855 | 3.97 |
| MagicMotion | 1426.37 | 30.04 | 230.53 | 4.01 | 0.9871 | 3.95 |
| Self-Forcing | 0.95 | 34.47 | 315.87 | 3.70 | 0.9920 | 4.06 |
| AR-Drag | 0.44 | 28.98 | 187.49 | 4.07 | 0.9948 | 4.37 |

The table supports a strong result within the reported setup, not a universal ranking. Baseline model sizes differ, preprocessing boundaries are not fully itemized, and all values are source-reported point estimates.

### Ablations and Boundary Evidence

Without RL, latency remains 0.44 seconds while FID/FVD worsen to 31.65/210.35 and motion consistency to 4.12. Without Self-Rollout, FID/FVD degrade to 38.13/353.75, with visible artifacts in Figure 4. The teacher model reports FVD 151.46 and aesthetic 4.15 at 45.64 seconds. A chunk-size-three variant reaches FID 27.47 and FVD 179.23 but takes 0.94 seconds. Cache sizes 15 and 25 make small changes relative to the default seven-frame cache.

The paper's limitation section says physically implausible or exaggerated controls may not be followed because training data and the reward prioritize plausible motion. It proposes parallel sampling to reduce latency further. It does not provide a failure taxonomy for tracker loss, identity drift, non-physical animation, repeated control reversals, adversarial inputs, or long streaming sessions.

### Safety, Ethics, and Reproducibility

The ethics statement says experiments use de-identified data without personally identifiable information and follow the ICLR Code of Ethics. That is useful but incomplete for a generative-video system: de-identification does not itself establish consent, copyright/license compatibility, representativeness, or safe downstream use. Interactive reenactment, impersonation, non-consensual editing, and deceptive media need product-level controls.

The reproducibility statement points to supplementary code, configurations, and instructions. The source package contains detailed algorithms and pseudocode, but no official public repository or downloadable benchmark was established from the inspected arXiv, project, venue, and exact release searches. Search absence is an access boundary, not proof that artifacts cannot exist elsewhere.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | AR-Drag combines motion-conditioned distillation, Self-Rollout, selective stochasticity, and GRPO in a 1.3B few-step AR video model. | Author mechanism claim | E1 | Directly supported by method equations, algorithms, and settings. | High |
| C2 | Self-Rollout conditions later frames on fully generated model history and better matches inference than teacher forcing or collapsed Self-Forcing. | Author mechanism claim | E1 | Supported as an implementation distinction; “restores the Markov property” remains conditional on the state definition. | Medium-high |
| C3 | AR-Drag reports the best displayed value in all six Table 1 columns. | Author empirical claim | E1 | Table visually verified; values are point estimates on an author-curated benchmark. | High for transcription; medium for generalization |
| C4 | First-frame latency is 0.44 seconds on one H20. | Author systems claim | E1 | Supported for the reported measurement; not end-to-end interactive latency or hardware-portable evidence. | High for reported value |
| C5 | RL materially improves fidelity and motion alignment. | Author causal claim | E1 | Removing RL worsens every displayed quality/motion metric while latency is fixed; multi-seed uncertainty is absent. | Medium-high |
| C6 | Self-Rollout is necessary for quality. | Author causal claim | E1 | The removal ablation shows large FID/FVD degradation and visual artifacts; implementation bundles may still contain confounders. | Medium-high |
| C7 | AR-Drag follows arbitrary desired motion. | Reviewer assessment of implied scope | E1 | Not established; the paper explicitly identifies non-physical controls as out of distribution. | High |
| C8 | The system is independently reproducible from public artifacts. | Reviewer assessment | E1-E5 | Not established from inspected sources; detailed pseudocode is not an end-to-end release. | Medium-high |

## Methodology

- `Research objective`: Preserve a full-paper, source-grounded assessment of AR-Drag's mechanism, reported evidence, limitations, implementation implications, and relation to existing Black Lake research.
- `Sources inspected`: Complete v3 PDF, official full-paper HTML, metadata HTML, TeX/source package, extracted PDF text, rendered pages containing Tables 1-3, Figures 1, 4, and 6, Algorithms 1-2, data settings and limitations; arXiv metadata; official project page; ICLR poster record; OpenReview locator; exact public release searches; live repository READMEs; and exactly three related DEP entries.
- `Discovery strategy`: Uniform random selection from deduplicated local PDF-parent units, local full-text/PDF/source inspection, public primary-record verification, repository-relative related-entry search, and bounded title/ID/release searches.
- `Inclusion criteria`: Primary or official sources, full-paper evidence, directly relevant Black Lake entries, and claims traceable to inspected methods, tables, figures, appendices, or metadata.
- `Exclusion criteria`: Abstract-only synthesis, unverified aggregators, unrelated citations, local paths in public text, source-file deposition, and claims not supported by inspected evidence.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Extraction process`: PDF text extraction plus visual page rendering were reconciled with official HTML and source files. Numerical claims were checked against tables and surrounding prose.
- `Version control`: The review pins arXiv v3 and date-only access context. Related DEP paths are pinned to current repository locations.
- `Evidence handling`: Author claims, reviewer interpretations, repository rules, and local verification evidence are separated. Each major claim maps to an evidence-ledger item.
- `Uncertainty handling`: Unreproduced metrics remain author reports; inaccessible or absent artifacts are described as availability boundaries; no missing detail is inferred.
- `Reviewer stance`: DEP-ready paper report, skeptical critique, implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: AR-Drag's v3 paper, official context, source integrity, three directly related DEP entries, and public-safe implementation/evaluation implications.
- `Temporal boundary`: Sources checked through 2026-07-20; reviewed paper revision dated 2026-03-08.
- `Evidence limits`: No training, inference, benchmark, latency, tracker, human-rating, or code execution was reproduced. OpenReview interactive content was challenge-gated. Public code and benchmark releases were not established.
- `Assumptions`: Table values and appendix descriptions accurately represent the authors' runs; public URLs identify the reviewed work; the configured local integrity tests are sufficient to distinguish complete sources from abstract/error payloads.
- `Constraints`: Source documents must remain local; public text may not expose private filesystem or machine information; media generation raises privacy, consent, copyright, and misuse risks.
- `Out of scope`: Production deployment, face/identity editing, offensive synthetic-media generation, legal advice, and claims of universal real-time behavior.
- `Intended use`: Research review, DEP deposition, benchmark design, product-gate definition, and replication backlog.
- `Audience`: Video-generation researchers, ML systems engineers, evaluation engineers, and responsible-AI/product reviewers.
- `Reproducibility boundary`: The algorithm can be reconstructed conceptually; reported results cannot be independently reproduced without versioned code, data, metrics, weights, and expected outputs.
- `Data sensitivity`: Public research metadata and source documents; training data may include human imagery, so downstream implementations must apply stricter consent and retention controls than the paper documents.

## Observations

- `Observed pattern`: The strongest quality collapse is tied to removing Self-Rollout, while the smaller but consistent degradation from removing RL affects both fidelity and control. Inference-aligned history appears foundational; reward optimization refines it.
- `Observed pattern`: The teacher retains the best FVD and aesthetic score, while AR-Drag dominates latency and several other metrics. Distillation trades some teacher ceiling for responsiveness rather than surpassing the teacher everywhere.
- `Technical implication`: Selective stochasticity is a variance-budgeting mechanism. It may transfer to other long-horizon generative policies where full stochastic rollout is too expensive.
- `Technical implication`: A seven-frame KV cache is part of the operational state. Cache policy, eviction, isolation, and drift monitoring deserve first-class metrics even though cache size sensitivity is mild in Table 3.
- `Contradiction or tension`: Motion Consistency improves under the same tracking-based reward family used for training. This is informative but not fully independent validation.
- `Open question`: Whether frame-wise denoising remains stable for substantially longer interactive sessions is not established by the 206-clip evaluation.
- `Reviewer hypothesis`: Combining inference-aligned Self-Rollout with explicit cache-governance mechanisms from PackForcing or ISPA could improve long-stream stability, but may alter the MDP and require retraining.

## Considerations

- **Evaluation**: Add multiple seeds, paired bootstrap intervals, per-trajectory failures, tracker-independent metrics, blinded raters, and public test identities.
- **Latency**: Measure control capture, trajectory encoding, diffusion, KV update, VAE decode, data transfer, rendering, and display separately at P50/P95/P99.
- **Data governance**: Publish source categories, collection rights, consent basis, demographic/content strata, synthetic proportions, exclusion reasons, annotator conditions, and retention policy.
- **Safety**: Require provenance signals, visible or cryptographic disclosure where appropriate, consent checks for identifiable subjects, misuse detection, abuse reporting, and refusal for non-consensual impersonation.
- **Privacy**: Keep user images and trajectories local or ephemeral by default; avoid raw media telemetry; isolate caches per user/session; provide deletion receipts.
- **Reward risk**: Monitor reward/evaluator disagreement and adversarial examples. A tracker can be confidently wrong under occlusion or texture ambiguity.
- **Operations**: Provide fallbacks for invalid trajectories, tracker loss, decoder failure, resource pressure, and drift. Real-time systems need graceful degradation rather than silent low-quality output.
- **Maintenance**: Pin backbone, VAE, tracker, aesthetic predictor, scheduler, kernels, and hardware. Each component change can shift both reward and latency.

## Strengths

- The paper connects a concrete train-inference mismatch to a concrete full-rollout correction.
- The GRPO formulation is adapted to frame-wise video generation with explicit state, action, transition, and reward definitions.
- Selective stochasticity addresses an actual long-horizon variance/cost problem rather than adding exploration indiscriminately.
- A matched-data Self-Forcing baseline strengthens the autoregressive comparison.
- Table 2 separates RL, Self-Rollout, initial backbone, and teacher contributions.
- The appendix includes data scale, resolution buckets, loss weights, algorithms, pseudocode, parameter analysis, reward curves, limitations, ethics, and reproducibility statements.
- Reported results cover fidelity, temporal behavior, control, and latency.

## Weaknesses

- Statistical uncertainty and seed stability are not reported for headline metrics.
- The 206-clip benchmark and approximately 10,000-video training mixture are not sufficiently public or provenance-rich for audit.
- Motion Consistency is evaluator-coupled to the proposed reward, and no independent blinded user study is reported.
- Latency is first-frame only on one H20 and omits the complete interactive path.
- Baseline size, optimization, and systems boundaries are heterogeneous.
- The Markov-property language depends on the chosen state definition and can overstate what Self-Rollout establishes.
- Long-horizon error, identity drift, occlusion failure, abrupt control changes, and adversarial trajectories lack quantitative failure distributions.
- Public end-to-end code, weights, configurations, and expected outputs were not established from inspected sources.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Independent motion evaluation | Metrics | Reduce reward-oracle dependence | Stronger controllability evidence | Multiple trackers and raters increase cost | Pre-register metrics; compare reward, tracker ensemble, and blinded ratings |
| Multi-seed and paired uncertainty | Experiments | Point estimates can hide training variance | Better causal attribution | Several eight-H20 runs are expensive | Three or more seeds with paired bootstrap intervals |
| Public benchmark/data card | Data | Enable audit of trajectory and scene coverage | Reproducibility and bias analysis | Licensing and privacy review | Release legal subset or synthetic equivalent with hashes and schema |
| End-to-end latency accounting | Systems | First-frame compute is not user-perceived latency | Portable performance boundary | Instrumentation can perturb timing | P50/P95/P99 traces on H20, A100, consumer GPU, and edge targets |
| Long-stream cache study | Reliability | Seven-frame cache may hide long-horizon failure | Drift and memory policy evidence | Longer clips cost compute and review | Sweep duration/cache policy; report identity and trajectory failure curves |
| Reward red-team | Safety/evaluation | Tracker/aesthetic proxies can be exploited | Reduced reward hacking | Requires adversarial generation and review | Occlusion, texture, impossible-motion, and prompt-injection suites |
| Consent/provenance ledger | Governance | De-identification does not resolve rights | Safer dataset and product use | Collection/documentation burden | Sample-based provenance audit and deletion workflow test |

## Potential Implementations

### 1. Interactive Motion Preview

- `User`: Video artist working with licensed or self-owned images.
- `Goal`: Preview trajectory edits with low latency before high-quality rendering.
- `Core mechanism`: A short-horizon AR-Drag-style preview model maintains per-session KV state and regenerates from the last accepted frame.
- `Required inputs`: Consented reference image, prompt, trajectory points, hardware profile.
- `Outputs`: Watermarked preview, latency trace, control-confidence overlay, provenance receipt.
- `Risk controls`: Local/ephemeral media, identity-consent confirmation, cache isolation, refusal for non-consensual impersonation, provenance marking.
- `Evaluation`: End-to-end latency, independent trajectory error, human preference, failure rate, and deletion tests.

### 2. Rollout Integrity Lab

- `User`: Video-model training engineer.
- `Goal`: Compare teacher forcing, Self-Forcing, and Self-Rollout under matched conditions.
- `Core mechanism`: Instrument the denoising transition graph, cache contents, stochastic step, reward components, gradients, and fallback path.
- `Required inputs`: Versioned toy and licensed video datasets, model checkpoints, seeds, schedulers, metrics.
- `Outputs`: Transition audit, reproducibility bundle, reward/evaluator disagreement report, quality-cost frontier.
- `Risk controls`: Synthetic data by default, no raw-media logging, bounded compute, deterministic dry runs, artifact hashes.
- `Evaluation`: State-transition invariants, repeated-run variance, cache drift, latency, and ablation parity.

### 3. Motion-Control Audit Suite

- `User`: Independent evaluator or responsible-AI reviewer.
- `Goal`: Test whether trajectory following survives beyond the training reward.
- `Core mechanism`: Generate consented/synthetic clips, score with independent trackers and blinded raters, and stratify by occlusion, speed, style, physical plausibility, and duration.
- `Required inputs`: Released model/API, legal test images, trajectories, evaluator ensemble, hardware trace.
- `Outputs`: Calibration curves, failure gallery, confidence intervals, misuse findings, release recommendation.
- `Risk controls`: No public identity cloning, content filters, rater safeguards, retention limits, disclosure labels.
- `Evaluation`: Pre-registered thresholds and reproducible signed result bundles.

## Three Ways to Exercise This Research

1. `Paper-table audit`: Objective - verify claims without model execution. Inputs - public PDF/HTML and a clean worksheet. Method - re-enter Tables 1-3, recompute deltas, map every number to hardware/metric context, and flag missing uncertainty. Output - signed table ledger. Success criterion - zero transcription/context discrepancies. Stop condition - any source/version mismatch.
2. `Synthetic rollout simulation`: Objective - test the state-transition idea safely. Inputs - synthetic frame IDs, a toy KV cache, deterministic and one-step-stochastic transitions. Method - compare teacher forcing, collapsed cache updates, and full rollout under controlled perturbations. Output - invariant and failure report. Success criterion - injected order/cache faults are detected. Stop condition - simulation requires real user media or uncontrolled compute.
3. `Independent evaluation design`: Objective - pre-register a credible replication. Inputs - consented benchmark plan, multiple trackers, rater protocol, hardware matrix, seeds, and thresholds. Method - define metrics, strata, exclusions, latency boundary, privacy controls, and statistical analysis before generation. Output - executable protocol. Success criterion - another team can run it without interpretation. Stop condition - code/data rights or consent remain unresolved.

## Example MVP Product

- `Product name`: Motion Preview Gate.
- `Target user`: Video designer needing rapid, governed trajectory previews from owned or licensed images.
- `Problem`: High-quality bidirectional generation is too slow for iterative control, while fast previews may drift, misuse identities, or hide latency/failure boundaries.
- `Core workflow`: Confirm media rights and identity consent; draw a trajectory; create a low-resolution short-horizon preview; show independent motion-confidence and latency components; accept, revise, or discard; optionally hand off an accepted plan to a separate high-quality renderer.
- `Data requirements`: User-owned/licensed reference image, prompt, trajectory coordinates, ephemeral session cache, synthetic evaluation set, no raw-media analytics by default.
- `Architecture`: Local or isolated preview service; control encoder; few-step frame-wise generator; per-session bounded KV state; independent tracker ensemble; latency tracer; provenance/disclosure component; deletion receipt service.
- `Success metrics`: P95 end-to-end preview latency under one second on target hardware; independently measured trajectory error below a pre-registered threshold; no cross-session cache leakage; high deletion success; calibrated confidence; low unsafe-request pass rate.
- `Risk controls`: Consent and rights gate, identity-sensitive refusal rules, session isolation, ephemeral retention, disclosure watermark/metadata, safety filter, rate limits, audit log without raw media, human escalation.
- `Limitations`: Not a production renderer; cannot guarantee physically impossible motion; tracker confidence can fail; hardware portability is unproven; no claim of paper-level metric reproduction.
- `MVP boundary`: Single image, short clip, low resolution, synthetic/consented tests, no public-figure or third-party identity editing.
- `Deployment model`: Local workstation or isolated enterprise service.
- `Evaluation plan`: Synthetic smoke tests, consented user study, tracker/rater agreement, multi-hardware latency traces, cache-isolation test, misuse red team, deletion audit.
- `Failure modes`: Occlusion-induced tracker error, identity drift, saturated/artifact frames, impossible trajectories, stale cache, misleading confidence, unsafe identity request.
- `Maintenance plan`: Pin and review model, VAE, tracker, aesthetic evaluator, scheduler, kernels, policy rules, and hardware profiles; rerun acceptance tests on every change.

## Related Research and Reading

### Exactly Three Related DEP Entries

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| VideoWeave Geometry | Black Lake DEP-E | Few-step video-diffusion distillation plus training-time structural latents; complements AR-Drag's sequential-history alignment with geometry consistency | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md |
| PackForcing Video | Black Lake DEP-A | Bounded, partitioned autoregressive-video KV history and long-horizon drift; directly extends the cache-governance problem | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-PackForcing%20Video/2603.25730-whitepaper-review.md |
| ISPA Video Memory | Black Lake DEP-A | Instance-specific absorption of autoregressive video history into temporary parameters; alternative state representation to AR-Drag's explicit KV frames | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-ISPA%20Video%20Memory/2607.00712-whitepaper-review.md |

### Primary and Near-Primary Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| From Slow Bidirectional to Fast Autoregressive Video Diffusion Models | Primary baseline paper | Self-Forcing lineage and fast AR video distillation compared by AR-Drag | https://arxiv.org/abs/2412.07772 |
| Wan: Open and Advanced Large-Scale Video Generative Models | Backbone paper | Wan2.1-1.3B-I2V and 14B synthetic-data generator | https://arxiv.org/abs/2503.20314 |
| Tora: Trajectory-oriented Diffusion Transformer | Primary baseline paper | Trajectory-controlled bidirectional DiT baseline | https://arxiv.org/abs/2407.21705 |
| CoTracker3 | Primary tracker paper | Automatic trajectory extraction and motion reward dependency | https://arxiv.org/abs/2410.11831 |
| DeepSeekMath | Primary optimization paper | GRPO family used for group-relative policy optimization | https://arxiv.org/abs/2402.03300 |
| VideoWeave | Related primary paper | Geometry-aware joint video modeling and few-step distillation | https://arxiv.org/abs/2606.14162 |
| PackForcing | Related primary paper | Bounded KV history for long autoregressive video generation | https://arxiv.org/abs/2603.25730v1 |
| ISPA Video Memory | Related primary paper | Historical-context absorption for memory-efficient AR video generation | https://arxiv.org/abs/2607.00712v1 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2510.08131 | Identity, version, DOI, subject, license, artifact links | 2026-07-20 | Official metadata; abstract-only content not used for empirical claims |
| R2 | https://arxiv.org/html/2510.08131 | Full method, results, appendix, limitations | 2026-07-20 | Complete official full-paper HTML verified locally |
| R3 | https://arxiv.org/pdf/2510.08131 | Visual tables, figures, algorithms, pagination | 2026-07-20 | Complete PDF verified and selected pages rendered locally |
| R4 | https://arxiv.org/e-print/2510.08131 | TeX/source provenance and supplementary pseudocode | 2026-07-20 | Source package verified locally; withheld from deposit |
| R5 | https://doi.org/10.48550/arXiv.2510.08131 | Stable DOI identity | 2026-07-20 | arXiv-issued DOI |
| R6 | https://kesenzhao.github.io/AR-Drag.github.io/ | Official project and qualitative context | 2026-07-20 | No official public code repository established on inspected page |
| R7 | https://iclr.cc/virtual/2026/poster/10011557 | ICLR 2026 Poster status | 2026-07-20 | Official venue record |
| R8 | https://openreview.net/forum?id=4Q55RwYte9 | Forum identity | 2026-07-20 | Interactive forum content challenge-gated |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-VideoWeave%20Geometry/videoweave_geometry_manuscript.md | Related geometry/video distillation synthesis | 2026-07-20 | One of exactly three related DEP entries |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-PackForcing%20Video/2603.25730-whitepaper-review.md | Related autoregressive KV-history synthesis | 2026-07-20 | One of exactly three related DEP entries |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-ISPA%20Video%20Memory/2607.00712-whitepaper-review.md | Related context-absorption synthesis | 2026-07-20 | One of exactly three related DEP entries |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout, source locality, attribution | 2026-07-20 | Live repository authority |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication index | 2026-07-20 | Live DEP authority |
| R14 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion-repository context and dedup scope | 2026-07-20 | Live companion authority |

## Appendix

### Random Selection and Deduplication

- `Enumeration`: `rg --files -g "*.pdf"` returned 75,778 PDFs, collapsed to 75,776 unique PDF-parent paper units.
- `Identity normalization`: arXiv IDs were derived from filenames, folder names, and nearby metadata, normalized without version suffix for deduplication.
- `Dedup corpus`: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; current Black-Lake-Data `.lake-data` and `.reports`.
- `Counts`: 1,007 used identifiers; 222 excluded units; 0 identifier-incomplete units; 75,554 eligible units.
- `Draw`: PowerShell `Get-Random` selected zero-based eligible index 14,671 uniformly on the first draw.
- `Acceptance keys`: base/versioned ID, DOI, exact/normalized title, and `AR-Drag` slug; no prior owning artifact or preceding-24-hour marker found.
- `Reselections`: zero.

### Source-Integrity Receipt

- `Initial state`: partial; PDF complete, full-paper HTML missing.
- `Repair policy`: one bounded official-arXiv companion-bundle attempt, 200 MB total ceiling, 50 MB partial ceiling, no credentials, valid PDF reused unchanged.
- `PDF`: 34,931,055 bytes; `%PDF-` header; trailing `%%EOF`.
- `Full-paper HTML`: 356,542 bytes; 88,798 body characters; document marker; 63 headings/sections; eight structure terms; not abstract-only.
- `Metadata HTML`: 42,779 bytes; metadata only.
- `Source archive`: 32,494,867 bytes; 34 readable entries.
- `Partials`: zero.
- `Final state`: complete; review began only after the gate passed.
- `Local records`: README, attribution/provenance, CSV summary, JSON verification, extracted text, and rendered pages remain local.
- `Upload gate`: no source document or source-derived cache is included in Git, GitHub, a PR, or Slack.

### Replication Checklist

- Pin arXiv v3, paper/source hashes, backbone, VAE, tracker, aesthetic predictor, scheduler, kernels, optimizer, hardware, data snapshot, benchmark IDs, prompts, and seeds.
- Recreate the motion-conditioned teacher, DMD/adversarial student, Self-Rollout cache updates, selective stochastic step, and GRPO reward components separately.
- Match first-frame and end-to-end latency boundaries; include preprocessing, decode, transfer, and display.
- Recompute Tables 1-3 with multiple seeds, confidence intervals, independent trackers, and blinded raters.
- Publish failure cases by trajectory type, occlusion, physical plausibility, duration, subject, resolution, and hardware.
- Audit data rights, consent, de-identification, exclusion, annotator conditions, and deletion paths before any product use.

## Attribution Block

- Primary work: *Real-Time Motion-Controllable Autoregressive Video Diffusion*, Kesen Zhao et al., arXiv:2510.08131v3, ICLR 2026 Poster.
- Canonical record: https://arxiv.org/abs/2510.08131
- DOI: https://doi.org/10.48550/arXiv.2510.08131
- Official project: https://kesenzhao.github.io/AR-Drag.github.io/
- Source files withheld: PDF, HTML, metadata, TeX/source, extracted text, renders, caches, and verification records remain local and were not uploaded.
