---
title: "Spiking Pose Tracking - DEP-E"
generated_at: "2026-07-24 (UTC date; exact timestamp withheld)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-first review of event-only 3D human pose tracking with a Spiking Spatiotemporal Transformer."
source_status: "verified complete local PDF, full-paper HTML, metadata, and source package inspected; public URLs cited; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-24"
temporal_cutoff: "Paper v5, official repository, and Black Lake context inspected through 2026-07-24."
primary_url: "https://arxiv.org/abs/2303.09681"
stable_identifier: "arXiv:2303.09681v5; DOI:10.48550/arXiv.2303.09681"
confidence_summary: "High for source identity, method, printed metrics, and visible figures; medium for interpretation; low for independent reproduction because experiments and hardware energy were not rerun."
safety_scope: "consent-aware human-motion research, synthetic evaluation, and auditable edge-perception prototypes"
distribution_notes: "No PDF, HTML, metadata page, source archive, extracted text, render, cache, model, dataset, or private path is redistributed."
---

# Spiking Pose Tracking - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Canonical metadata | HTML | arXiv:2303.09681v5 | https://arxiv.org/abs/2303.09681 | Canonical title, authors, dates, abstract, acceptance comment, and source links. | 2026-07-24 | Inspected |
| S2 | Full paper | Primary artifact | PDF and HTML | arXiv:2303.09681v5 | https://arxiv.org/pdf/2303.09681; https://arxiv.org/html/2303.09681 | Verified complete local copies inspected and withheld; arXiv page links a Creative Commons license. | 2026-07-24 | Full text and selected visual pages inspected |
| S3 | Source package | Primary source | TeX/source archive | arXiv:2303.09681 | https://arxiv.org/e-print/2303.09681 | Retained locally for provenance; not redistributed. | 2026-07-24 | Collected locally |
| S4 | arXiv-issued DOI | Persistent identity | DOI | 10.48550/arXiv.2303.09681 | https://doi.org/10.48550/arXiv.2303.09681 | Persistent arXiv identity, not treated as an independent publisher result. | 2026-07-24 | Inspected |
| S5 | HumanPoseTracking_SNN | Official implementation | GitHub repository | Default branch, 9-commit history visible at inspection | https://github.com/JimmyZou/HumanPoseTracking_SNN | README exposes environment, test command, pretrained-model/test-sample links, and MIT license. | 2026-07-24 | README and visible tree inspected; code not run |
| S6 | FEMOT Tracking DEP | Related research artifact | Markdown | DEP-E-20260720-FEMOT Tracking | `.lake-data/DEP-E/DEP-E-20260720-FEMOT Tracking/femot_tracking_manuscript.md` | Black Lake review of event-camera multi-object tracking and temporal association. | 2026-07-24 | Inspected |
| S7 | Hallo4 Portrait Motion DEP | Related research artifact | Markdown | DEP-E-20260721-Hallo4 Portrait Motion | `.lake-data/DEP-E/DEP-E-20260721-Hallo4 Portrait Motion/hallo4_portrait_motion_manuscript.md` | Black Lake review of temporal motion modulation and skeleton conditioning. | 2026-07-24 | Inspected |
| S8 | Clothed Avatar CAR DEP | Related research artifact | Markdown | DEP-E-20260709-Clothed Avatar CAR | `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` | Black Lake review of SMPL-guided sparse-evidence 3D human reconstruction. | 2026-07-24 | Inspected |
| S9 | Private integrity and process records | Selection and verification provenance | Local records | arXiv:2303.09681 | Local paths withheld | Used only to verify randomness, deduplication, source repair, hashes, and document completeness. | 2026-07-24 | Inspected; not public |

The paper lists Shihao Zou, Yuxuan Mu, Wei Ji, Zi-An Wang, Xinxin Zuo, Sen Wang, Weixin Si, and Li Cheng. Version 1 was submitted on 2023-03-16; version 5 was revised on 2025-05-15. The arXiv record states acceptance by IEEE Transactions on Circuits and Systems for Video Technology. No independent publisher DOI was established in this review.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Canonical metadata / DOI | Identity, authors, dates, version, subject, acceptance comment, and public URLs. | Source identity and temporal boundary. | High | Metadata does not validate methods or results. |
| E2 | S2 | Complete primary paper | Introduction, method, equations, Tables I-V, Figures 2-10, experiments, discussion, conclusion, and references. | Architecture, datasets, quantitative claims, ablations, and limitations. | High for reporting | Author-reported evidence; no experiment reproduced. |
| E3 | S2 visual pages | Primary PDF figures/tables | Pages 5, 6, 9, 11, and 13: pipeline, attention mechanism, MMHPSD table, SynEventHPD table, and failure cases. | Cross-check of extracted text and visual evidence. | High for transcription | Still images cannot establish temporal quality. |
| E4 | S5 | Official repository | Environment instructions, pinned SpikingJelly commit, test entry point, pretrained-model/test-sample links, source tree, and MIT license. | Implementation availability and reproduction boundary. | Medium-high | Repository was not cloned, built, or executed; dataset release completeness was not verified. |
| E5 | S6 | Related DEP manuscript | RGB-event tracking benchmark, frequency-aware fusion, and temporal association memory. | Event-tracking and memory concept bridge. | Medium | Different targets, modalities, and metrics. |
| E6 | S7 | Related DEP manuscript | Skeleton/audio temporal-to-channel modulation, motion evaluation, and safety governance. | Motion-preservation and conditioning bridge. | Medium | Generative portrait animation is not pose tracking. |
| E7 | S8 | Related DEP manuscript | SMPL, canonical geometry, SDF refinement, sparse evidence, and occlusion risk. | Structured human-body prior bridge. | Medium | Static avatar reconstruction differs from temporal event tracking. |
| E8 | S9 | Private process evidence | Uniform draw, dedup scan, PDF/HTML hashes and checks, bounded repair, and no-partial verification. | Eligibility and complete-source gate. | High | Private records are intentionally not public locators. |

## Executive Summary

The paper proposes an event-only 3D human pose tracker built as a spiking neural network. Its central design is a Spiking Spatiotemporal Transformer that lets pose evidence flow bidirectionally across the complete space-time spike tensor. Binary spike queries and keys are compared with normalized Hamming similarity rather than dot product, while real-valued values retain regression precision. SEW-ResNet extracts sparse features, and pooled outputs regress SMPL pose, shape, and translation.

The strongest reported evidence is a favorable accuracy/efficiency tradeoff on MMHPSD. At `T=8`, the method reports 9.4G FLOPs, modeled energy 0.0083 J, and errors of 107.2/58.7/44.1 mm for MPJPE, pelvis-aligned MPJPE, and PA-MPJPE. Its PA-MPJPE ties the events-only ResNet-Transformer while using about one-fifth of its FLOPs and about 3.6% of its modeled energy. At `T=64`, the method reports 63.4G FLOPs, 0.058 J, and 111.7/61.9/45.7 mm.

The authors also contribute SynEventHPD, a 45.72-hour synthetic event-pose collection with 9,197 streams and 47 subjects. Mixed real/synthetic training and domain adaptation improve the reported real MMHPSD test errors, but synthetic-only training is weaker, so the source itself exposes a domain gap.

Reviewer confidence is high that the paper's method, printed metrics, and failure cases are represented accurately. Confidence is medium that normalized Hamming attention is broadly reusable, because its direct ablation is supportive but limited to the tested architecture and data. Confidence is low for claims about actual deployment energy: the paper estimates energy from operation counts and published per-operation constants rather than measuring full-system power on neuromorphic or edge hardware.

## Detailed Summary

### Problem Context

Event cameras asynchronously report brightness changes as `(x, t, p)` events. This avoids repeatedly transmitting static pixels and can offer high temporal resolution at low sensor energy. Existing human-pose methods often convert these sparse events into dense images, combine them with grayscale frames, or initialize tracking from a frame-based pose estimator. The paper argues that these choices introduce redundant computation and make tracking vulnerable to the initial frame estimate.

The event-only task is also harder. Static body parts generate few events. A single event camera observes 2D changes, while the output is a full 3D body. Spiking models normally unfold one direction through time, so early predictions may lack future context. Standard dot-product attention is also a poor similarity measure for binary spike vectors: zero-valued query bits discard corresponding key information, and an all-zero query produces zero similarity for every key.

### Architecture

The input event stream is partitioned into sparse binary voxel grids `S_in` across time, height, width, and event channels. A SEW-ResNet backbone produces spike pose features at one-thirty-second spatial resolution. The Spiking Spatiotemporal Transformer then performs attention over the flattened full space-time domain.

Spike query and key tensors are produced by linear spiking layers with positional encoding and batch normalization. A non-spiking linear branch produces real-valued values. Normalized Hamming similarity becomes the attention score, values are aggregated, and the result is converted back into spikes. Residual SEW functions and a spiking feed-forward network produce the final spike feature tensor.

The authors motivate Hamming similarity with a binary-embedding result related to the Johnson-Lindenstrauss lemma: with sufficient binary embedding dimension, normalized Hamming similarity bounds and approximates the corresponding real-vector cosine similarity under the stated random-projection assumptions. In practice the paper uses a differentiable algebraic form of Hamming similarity for training.

The output spike tensor is spatially average-pooled. Three parallel linear heads regress SMPL shape parameters, pose parameters, and global translations for every time step. Training combines pose geodesic loss, shape/translation Euclidean losses, and 2D/3D joint losses.

### SynEventHPD

SynEventHPD combines synthetic event streams derived from Human3.6M, AMASS, PHSPD, and MMHPSD. For AMASS, the authors animate one of 13 avatars and render RGB video before event synthesis. The resulting meta-dataset reports:

- 47 subjects;
- 9,197 event streams;
- 45.72 total hours;
- 0.30 minutes average stream length; and
- SMPL annotations.

The paper contrasts this with MMHPSD's 15 subjects, 178 streams, and 4.39 hours, and DHP19's 17 subjects, 33 streams, and 0.80 hours. Pose-distribution visualization suggests broader variety, but t-SNE coverage is qualitative and does not establish demographic, sensor, clothing, or real-domain diversity.

### Experimental Setup

MMHPSD experiments follow the prior train/test split. `T=8` represents two seconds of training input and one second at test; `T=64` represents eight seconds at test, with longer randomized training windows. Events are converted into `256 x 256 x 4` voxel grids. The selected model uses SEW-ResNet50, two attention layers, one head, hidden dimension 1024, and 47.7M parameters.

Training uses SpikingJelly, one NVIDIA A100 80 GB GPU, batch size 8, learning rate 0.01 with cosine annealing, 20 epochs for `T=8`, and 25 epochs for `T=64`. The paper compares video/grayscale-event methods, events-only ANN models, a mixed SNN/ANN model, and several SNN baselines.

Evaluation reports MPJPE, pelvis-aligned MPJPE, PA-MPJPE, FLOPs, and modeled energy. MAC operations are assigned 4.6 pJ and accumulate operations 0.9 pJ using a cited 45 nm technology estimate. These values are a model-level proxy, not an end-to-end energy meter.

### Main Results

| Model / setting | Input | T | FLOPs | Modeled energy | MPJPE | PEL-MPJPE | PA-MPJPE |
|---|---:|---:|---:|---:|---:|---:|---:|
| ResNet-TF | Events | 8 | 50.5G | 0.23 J | 108.5 | 59.9 | 44.1 |
| EventHPE (MPS) | Gray frame + events | 8 | 49.3G | 0.22 J | Not reported | 65.1 | 46.5 |
| Proposed SNN | Events | 8 | 9.4G | 0.0083 J | 107.2 | 58.7 | 44.1 |
| ResNet-TF | Events | 64 | 403.8G | 1.85 J | 114.2 | 66.0 | 50.1 |
| EventHPE (MPS) | Gray frame + events | 64 | 354.2G | 1.63 J | Not reported | 66.8 | 48.1 |
| Proposed SNN | Events | 64 | 63.4G | 0.058 J | 111.7 | 61.9 | 45.7 |

The proposed model has the best reported errors among the events-only SNN baselines and stays closer to its short-window accuracy at `T=64` than the compared ANN models. It does not dominate every result in the table: EventHPE with ground-truth initial pose reports lower PA-MPJPE, but this is an upper-bound setting that supplies unavailable perfect starting information.

For SynEventHPD, the proposed model's real-only training reports 107.2/58.7/44.1 mm. Real-plus-synthetic reports 103.1/58.4/43.8 mm, and adding domain adaptation reports 99.2/55.8/42.9 mm. Synthetic-only reports 110.7/59.4/45.0 mm. This supports value from mixed synthetic data in the tested split while preserving the synthetic/real gap.

### Ablations

The strongest method-specific ablation compares attention score functions. Normalized Hamming similarity reports PEL-MPJPE 58.7, versus 62.8 for scaled dot product, 61.7 for normalized Euclidean, and 62.3 for normalized Manhattan similarity.

The value-branch ablation exposes a useful tradeoff. Binary values with dot product report 62.0 at 0.00806 J. Real values with Hamming similarity report 58.7 at 0.00826 J, a 3.3 mm improvement for about 2.5% higher modeled energy. Real values make the final architecture not purely binary, which should be explicit when estimating hardware sparsity.

Increasing hidden dimension beyond 1024 yields diminishing or negative returns in the tested setting. Additional attention layers and deeper backbones improve some results, but each attention layer adds about 20M parameters, so capacity and overfitting remain material.

### Failure Modes and Boundary

Failure figures show occluded arms and elbows and cases without useful temporal context. The authors propose longer accumulation windows, multi-scale temporal processing, multi-view events, direct 3D-joint output, and neuromorphic acceleration as future directions.

Longer accumulation is not free: it trades latency and motion blur/aliasing against event coverage. Multi-view systems add calibration and association failures. Direct joints remove SMPL parameterization complexity but lose a full body-surface prior. Hardware acceleration can change the balance between sparse attention, real-valued value aggregation, memory transfer, and regression heads.

Human-pose sensing can also be identity- and behavior-sensitive. Deployment should use consented or synthetic subjects, minimize retention, document monitoring purpose, and avoid turning inferred motion into an unqualified statement about a person.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The method is the first event-only SNN framework for 3D human pose tracking. | Author novelty claim | E2 | Consistent with the paper's related-work review, but priority was not independently exhaustively searched. | Medium |
| C2 | Bidirectional spatiotemporal attention improves pose tracking over the SEW-ResNet backbone and tested spiking transformers. | Author empirical claim | E2, Table III/V | Directly supported by reported comparisons and ablations. | High for reporting |
| C3 | Normalized Hamming similarity is better suited than dot product for binary spike attention. | Author mechanism and empirical claim | E2, E3, Proposition 1, Table V | The binary-vector argument and direct ablation are persuasive within scope; broader generality is untested. | Medium-high |
| C4 | The model reaches ANN-comparable accuracy with much lower operation-count energy estimates. | Author empirical/efficiency claim | E2, Table III | Supported by the printed table; physical system energy and latency were not measured. | High for table, low for deployment energy |
| C5 | SynEventHPD improves real-set performance when mixed with real data and domain adaptation. | Author empirical claim | E2, E3, Table IV | Supported in the reported split; synthetic-only weakness and transfer boundary remain. | High for reporting |
| C6 | An auditable system should expose current-event, temporal, and prior-driven support for each pose. | Reviewer interpretation | E2, E5-E7 | Derived from failure cases and the three related DEP bridges; not a paper claim. | Medium |

## Methodology

- `Research objective`: Randomly select one eligible local arXiv paper unit, require complete source integrity, review the work source-first, and create a public-safe Black Lake log, Report-Mark, DEP-E manuscript, publication-index row, and dedup pointer.
- `Sources inspected`: Complete paper PDF and HTML, arXiv metadata and DOI, local source-package provenance, official implementation repository, live Black Lake filing standards, private integrity/process records, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, grouped unique parent directories into paper units, used uniform PowerShell `Get-Random`, derived identity from the unit readme and filename, then verified the canonical arXiv record.
- `Inclusion criteria`: Evidence had to establish identity, directly support method/results/limitations, define implementation availability, prove process eligibility/integrity, or provide concrete event/pose/motion overlap.
- `Exclusion criteria`: Abstract-only synthesis, source files, private paths, exact execution timestamps, unverified claims, unrelated keyword hits, and background citations without direct use were excluded.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Printed metrics are labeled author-reported. Reviewer interpretations are marked separately. Extracted full text was cross-checked against rendered pages for the pipeline, attention design, main results, synthetic-data results, and failure cases.
- `Uncertainty handling`: Missing reproduction, hardware energy, repeated seeds, confidence intervals, demographic/sensor transfer evidence, and dataset-release completeness are stated rather than inferred.
- `Random selection methodology`: 75,780 PDF candidates collapsed to 75,777 unique PDF-parent units. A uniform zero-based `Get-Random` draw selected index 53,213. The selected ID was `2303.09681`.
- `Dedup/reselection validation`: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, and automation memory were scanned for arXiv ID, DOI, normalized title, and slug. The 24-hour cutoff was 2026-07-23. Exclusions: 0. Reselections: 0.
- `Source-integrity methodology`: Initial state was partial. A bounded, credential-free, one-paper repair preserved a valid PDF that matched the fresh copy, obtained official full-paper HTML, metadata, and source locally, updated companion records, and passed the required PDF/HTML/no-partial gates before review.
- `Reviewer stance`: Skeptical paper report, DEP-ready preservation, implementation translation, and safety-aware replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: The event-only SNN pose pipeline, binary attention geometry, SynEventHPD, MMHPSD evidence, efficiency estimates, failure modes, implementation surface, and synthesis with three Black Lake entries.
- `Temporal boundary`: Paper v5 and public sources inspected through 2026-07-24.
- `Evidence limits`: No training, inference, metric, dataset, pretrained model, or repository code was executed. No physical energy or latency test was performed.
- `Assumptions`: The arXiv base endpoints served the current v5 paper; printed tables reflect the authors' runs; the preserved PDF and repaired HTML correspond to the same current work.
- `Constraints`: Source files remain local. Public artifacts omit local paths, machine/user names, timezone labels, and exact execution times. Human-motion data is potentially sensitive.
- `Out of scope`: Production surveillance, non-consensual monitoring, dataset redistribution, model deployment, exhaustive novelty search, and legal clearance.
- `Intended use`: Research review, DEP deposition, replication planning, sparse-perception design, and safety-aware product ideation.
- `Audience`: Event-vision researchers, neuromorphic engineers, motion/pose researchers, robotics teams, and responsible-AI reviewers.
- `Reproducibility boundary`: Public code and paper sources define an entry point, but results cannot be reproduced from this manuscript alone.
- `Data sensitivity`: Public research artifacts; downstream human event streams and pose traces can reveal identity, activity, health, or location and require consent and minimization.

## Observations

- `Observed pattern`: The best-supported novelty is representation alignment: sparse events feed spiking layers, and binary features use a binary-aware similarity measure.
- `Technical implication`: Future/past attention is most valuable where a current time slice lacks pose evidence, but this should be measured jointly with latency and leakage from future context.
- `Evidence tension`: The headline energy reduction is large, while the energy model omits sensor, memory, dense kernels, real-valued values, regression, and platform overhead.
- `Dataset implication`: Synthetic motion expands pose variety, but the real/synthetic gap remains and domain adaptation carries much of the final gain.
- `Reliability implication`: A valid SMPL body can still be wrong at specific joints; output plausibility is not the same as observation support.
- `Reviewer hypothesis`: A per-joint evidence ledger would make event-pose systems substantially safer and easier to debug than a single aggregate confidence score.

## Considerations

Sparse execution must be demonstrated at the kernel and system level. Flattening full space-time attention can create a large logical attention matrix even if inputs are sparse. Hardware evaluation should report sparse utilization, memory traffic, dense fallbacks, value-branch precision, batch size, sensor I/O, and idle power.

Evaluation should include slow/static starts, abrupt motion, varying accumulation windows, clothing changes, self-occlusion, external occluders, sensor hot pixels, threshold drift, lighting interference, missing events, camera motion, and cross-camera transfer. Multi-view extensions require calibration uncertainty and identity/track reset tests.

Human-motion products need affirmative consent, purpose limitation, access controls, retention expiry, deletion, and provenance. Pose uncertainty should be exposed per joint and per time interval. Systems should avoid inferring sensitive activities or health states beyond their validated purpose.

## Strengths

- The architecture matches event sparsity and spike representation rather than densifying by default.
- The normalized Hamming attention claim has both a conceptual binary-vector argument and a direct score-function ablation.
- The paper compares ANN, mixed, and multiple SNN baselines at short and long temporal windows.
- SynEventHPD materially expands the event-pose training inventory and its domain gap is acknowledged in the experiments.
- Failure figures and discussion identify static regions, occlusion, insufficient temporal context, and 2D-to-3D ambiguity.
- The official repository provides a concrete test surface, environment guidance, pinned SpikingJelly revision, pretrained-model links, and an MIT license.

## Weaknesses

- Energy is modeled from operation counts rather than measured end-to-end on target hardware.
- Results are point estimates without repeated seeds, confidence intervals, or statistical tests.
- The paper does not establish cross-camera, cross-subject, demographic, clothing, or broad real-world generalization.
- Dataset provenance, licensing, synthesis fidelity, and full release status need a stronger data card.
- Full space-time attention, real-valued values, and SMPL regression may reduce the practical sparsity advantage.
- Occlusion and missing-event failure modes remain material, and the model does not output calibrated per-joint uncertainty.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Measure physical energy and latency | Systems | Operation-count estimates omit platform overhead. | Credible deployment tradeoff. | Hardware/kernel engineering. | Power instrumentation across edge GPU and neuromorphic targets. |
| Add calibrated per-joint evidence scores | Reliability | Plausible SMPL poses can hide unsupported joints. | Better review and fallback decisions. | Calibration data and UI complexity. | Reliability diagrams by occlusion/event density. |
| Publish a SynEventHPD data card | Dataset governance | Synthetic diversity and licenses are not fully auditable. | Safer reuse and clearer transfer boundary. | Provenance and maintenance work. | Source inventory, license audit, leakage checks, subgroup coverage. |
| Test sparse attention kernels | Efficiency | Logical sparsity may not yield physical savings. | Honest memory/compute profile. | Specialized implementation. | Kernel utilization, memory traffic, dense-fallback counters. |
| Add multi-view and sensor-noise experiments | Robustness | Single-view 2D events underdetermine occluded 3D joints. | Better depth and occlusion handling. | Calibration and data cost. | Controlled multi-view, noise, drift, and dropout benchmarks. |
| Compare direct joints against SMPL | Output design | SMPL adds structure but also parameterization error. | Clearer prior/accuracy tradeoff. | Two decoder families. | Matched backbone, loss, compute, and uncertainty evaluation. |

## Potential Implementations

1. **Sparse Pose Evidence Auditor**
   - `User`: Pose researchers and robotics safety reviewers.
   - `Goal`: Explain which joints are supported by events, temporal context, and a body prior.
   - `Core mechanism`: Instrument the model to export spike density, attention support, occlusion flags, and decoder-prior contribution.
   - `Required inputs`: Consented or synthetic event sequences, calibration, model outputs, and ground truth for evaluation.
   - `Outputs`: Per-joint evidence ledger, pose trace, warnings, and DEP-ready report.
   - `Risk controls`: Local-only raw data, retention expiry, no identity inference, and human review.
   - `Evaluation`: Calibration error, occlusion error, false-confidence rate, and reviewer agreement.

2. **Neuromorphic Pose Benchmark Harness**
   - `User`: Edge and neuromorphic engineers.
   - `Goal`: Replace analytical energy claims with comparable physical measurements.
   - `Core mechanism`: Run identical preprocessed streams and pose heads across reference GPU, edge accelerator, and neuromorphic hardware.
   - `Required inputs`: Public/authorized sequences, pinned model, hardware counters, external power meter, and metric implementation.
   - `Outputs`: Accuracy, wall energy, latency, memory, sparse utilization, and thermal profile.
   - `Risk controls`: Synthetic/consented data, offline evaluation, and no persistent identity store.
   - `Evaluation`: Joules per sequence, tail latency, PA-MPJPE, and accuracy-energy Pareto frontier.

3. **Multi-View Event Pose Prototype**
   - `User`: Robotics or motion-capture researchers.
   - `Goal`: Reduce occlusion ambiguity without abandoning event-native processing.
   - `Core mechanism`: Calibrate two event cameras, associate body evidence across views, apply sparse temporal attention, and regress joints plus uncertainty.
   - `Required inputs`: Two synchronized event streams, calibration, test poses, and view-dropout labels.
   - `Outputs`: 3D joints, confidence, calibration residuals, and failure ledger.
   - `Risk controls`: Controlled lab use, consent, minimal retention, and explicit camera/view provenance.
   - `Evaluation`: Occlusion-sliced error, calibration sensitivity, view-dropout robustness, energy, and latency.

## Three Ways to Exercise This Research

1. `Binary similarity micro-benchmark`: Objective - compare Hamming, dot-product, Euclidean, and Manhattan scores under controlled spike density and occlusion; inputs - synthetic binary vectors; method - sweep sparsity/noise and measure retrieval of known matches; output - accuracy and calibration curves; success - Hamming advantage and failure boundary are explicit; stop - synthetic data only.
2. `Temporal-support ablation`: Objective - isolate gains from past-only, future-only, and bidirectional context; inputs - public or consented event sequences with occlusion labels; method - mask temporal directions and event windows; output - per-joint error by support regime; success - early-time and occluded-joint effects are quantified; stop - no identity inference or raw-data publication.
3. `Physical deployment audit`: Objective - test whether reported compute savings survive a real platform; inputs - pinned model, short authorized sequences, power meter, and hardware counters; method - measure preprocessing through output; output - energy/latency/accuracy Pareto report; success - every modeled energy component maps to a measured quantity; stop - if sparse kernels densify or instrumentation is incomplete.

## Example MVP Product

- `Product name`: Pose Evidence Gate
- `Target user`: Event-vision engineers, robotics reviewers, and model-release owners.
- `Problem`: Efficient pose models can output plausible but unsupported joints and can claim energy savings without physical evidence.
- `Core workflow`: Import public model metadata and authorized evaluation summaries; validate source integrity; ingest per-joint support metrics; check accuracy, calibration, latency, and physical energy; export a release decision and evidence ledger.
- `Data requirements`: Aggregate or synthetic evaluation records, metric definitions, hardware measurements, event-density bins, occlusion labels, and repository provenance. Raw human event streams are not required for the gate.
- `Architecture`: Local CLI, YAML/JSON schema validator, metric-direction registry, evidence-ledger builder, policy checks, and Markdown exporter.
- `Success metrics`: Complete evidence coverage, seeded issue detection, calibrated uncertainty, stable report hashes, and zero private-path/source leaks.
- `Risk controls`: Local-only by default, no raw biometric data, consent/provenance fields, retention expiry, source allowlist, and human approval for release.
- `Limitations`: The MVP validates evidence completeness and consistency; it does not prove model correctness, consent legality, or hardware generality.
- `MVP boundary`: Audit and release gating only, not live pose inference.
- `Evaluation plan`: Unit tests for missing fields, direction errors, unsupported joints, privacy leaks, and hardware-measurement gaps; reviewer comparison against a plain benchmark table.
- `Failure modes`: Incorrect metric schema, incomparable hardware runs, missing occlusion labels, and aggregate scores that hide subgroup failures.

Minimal dependency-free validator:

```python
REQUIRED = {
    "source": {"paper_url", "model_revision"},
    "quality": {"pa_mpjpe_mm", "occlusion_error_mm"},
    "systems": {"wall_energy_j", "latency_ms", "sparse_utilization"},
    "governance": {"consent_scope", "retention_policy"},
}

def validate_release(record):
    findings = []
    for section, fields in REQUIRED.items():
        missing = sorted(fields - set(record.get(section, {})))
        if missing:
            findings.append({"section": section, "missing": missing})
    unsupported = [
        joint["joint"] for joint in record.get("joint_evidence", [])
        if joint.get("confidence", 0.0) > 0.8 and joint.get("observed_support", 0.0) < 0.2
    ]
    if unsupported:
        findings.append({"section": "joint_evidence", "overconfident": unsupported})
    return {"ok": not findings, "findings": findings}
```

Dependencies: Python 3.10+ only. Production use needs schema versioning, signatures, access controls, audit logging, and independent review.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Highly Efficient 3D Human Pose Tracking | Primary paper | Reviewed work on event-only spiking pose tracking and Hamming attention. | https://arxiv.org/abs/2303.09681 |
| HumanPoseTracking_SNN | Official implementation | Environment, code/test surface, assets, and license context. | https://github.com/JimmyZou/HumanPoseTracking_SNN |
| FEMOT Tracking | Black Lake DEP-E | Event-camera tracking, multimodal fusion, and temporal association memory. | `.lake-data/DEP-E/DEP-E-20260720-FEMOT Tracking/femot_tracking_manuscript.md` |
| Hallo4 Portrait Motion | Black Lake DEP-E | Motion-preserving temporal conditioning and skeleton-driven human rendering. | `.lake-data/DEP-E/DEP-E-20260721-Hallo4 Portrait Motion/hallo4_portrait_motion_manuscript.md` |
| Clothed Avatar CAR | Black Lake DEP-E | SMPL and geometry priors for sparse, occluded 3D human evidence. | `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2303.09681 | Identity, authors, dates, version, abstract, acceptance comment, source links. | 2026-07-24 | Canonical metadata. |
| R2 | https://arxiv.org/html/2303.09681 | Full method, experiments, tables, discussion, limitations, and references. | 2026-07-24 | Verified full-paper HTML; local copy withheld. |
| R3 | https://arxiv.org/pdf/2303.09681 | Full paper and visual review of architecture, tables, dataset results, and failure cases. | 2026-07-24 | Verified PDF; local copy and renders withheld. |
| R4 | https://arxiv.org/e-print/2303.09681 | Source-package provenance. | 2026-07-24 | Collected locally and withheld. |
| R5 | https://doi.org/10.48550/arXiv.2303.09681 | Persistent arXiv identity. | 2026-07-24 | arXiv-issued DOI. |
| R6 | https://github.com/JimmyZou/HumanPoseTracking_SNN | Official implementation, environment, test command, assets, and license. | 2026-07-24 | Inspected, not run. |
| R7 | `.lake-data/DEP-E/DEP-E-20260720-FEMOT Tracking/femot_tracking_manuscript.md` | Event-camera tracking and association-memory synthesis. | 2026-07-24 | Related Black Lake artifact; primary basis https://arxiv.org/abs/2606.14094. |
| R8 | `.lake-data/DEP-E/DEP-E-20260721-Hallo4 Portrait Motion/hallo4_portrait_motion_manuscript.md` | Temporal-motion and skeleton-conditioning synthesis. | 2026-07-24 | Related Black Lake artifact; primary basis https://arxiv.org/abs/2505.23525. |
| R9 | `.lake-data/DEP-E/DEP-E-20260709-Clothed Avatar CAR/clothed_avatar_car_manuscript.md` | SMPL, sparse-evidence, and 3D-prior synthesis. | 2026-07-24 | Related Black Lake artifact; primary basis https://arxiv.org/abs/2304.03903. |
| R10 | Private integrity and processing records, paths withheld | Selection, deduplication, source repair, document integrity, and no-source-upload checks. | 2026-07-24 | Not a public source; no local path disclosed. |

## Appendix

### Random Selection and Deduplication Record

- `Enumeration`: `rg --files -g "*.pdf"` over the private arXiv archive.
- `PDF candidate count`: 75,780.
- `Paper-unit rule`: One unit per unique PDF parent directory.
- `Unique paper-unit count`: 75,777.
- `Random method`: Uniform PowerShell `Get-Random`.
- `Selected zero-based index`: 53,213.
- `Selected identifier`: arXiv:2303.09681.
- `Duplicate scan`: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, and automation memory.
- `Matching keys`: arXiv ID, DOI, normalized title, and slug.
- `24-hour cutoff`: 2026-07-23.
- `Duplicate exclusions`: 0.
- `Reselections`: 0.

### Source-Integrity Record

- Initial source state: `partial`.
- Existing PDF: 3,910,461 bytes; size, `%PDF-` header, and trailing `%%EOF` passed.
- Repair: One bounded, credential-free companion-bundle attempt with 40 MB total and 10 MB partial ceilings.
- PDF consistency: Existing and repair copies had identical SHA-256 hashes.
- Full-paper HTML: 1,006,692 bytes; 118,431 body characters; document marker present; 43 heading markers; all eight checked paper-structure terms present; distinct from abstract metadata.
- Companion records: README, attribution, machine summary, provenance, and verification report updated locally.
- Partials: 0.
- Final source state: `complete`.
- Source distribution: No source file or private processing artifact was uploaded.

### Replication Checklist

- Pin paper v5, repository revision, environment, SpikingJelly commit, model asset hash, and dataset revision.
- Reproduce Table III and Table V with repeated seeds and confidence intervals.
- Record preprocessing, spike threshold, event accumulation, firing rates, dense fallbacks, and value precision.
- Measure end-to-end latency, memory traffic, wall energy, and sensor I/O on target hardware.
- Publish SynEventHPD provenance, licenses, synthesis settings, splits, leakage analysis, and domain-transfer slices.
- Add static-start, occlusion, noise, lighting, camera-motion, slow-motion, and multi-view tests.
- Report per-joint uncertainty and observed/temporal/prior evidence.
- Preserve consent, retention, deletion, and purpose-limitation records for human data.

### Validation Checklist

- Required manuscript headings are present and ordered.
- YAML `title` and H1 are identical and no more than 40 characters.
- Evidence ledger and source references cover every material source.
- Author claims and reviewer interpretations are separated.
- `## Three Ways to Exercise This Research` contains exactly three paths.
- `## Example MVP Product` contains all required fields and a bounded code example.
- Exactly three related Black Lake DEP entries are synthesized.
- Random selection, deduplication, reselection, and complete-source methodology are explicit.
- No local absolute path, username, machine name, local timezone label, exact execution timestamp, source file, or `.source/` directory is public.
