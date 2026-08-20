---
title: "HSD FTI-FDet - DEP-E"
generated_at: "2026-07-12 (date-only public marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of heterogeneous self-distillation for resource-constrained freight-train visual fault detection."
source_status: "private archive evidence plus public URLs; no source files deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-12"
temporal_cutoff: "arXiv v1 and publisher article available by 2023-08; repository context inspected through 2026-07-12"
primary_url: "https://arxiv.org/abs/2307.00701"
stable_identifier: "arXiv:2307.00701v1; DOI:10.1016/j.aei.2023.102091"
confidence_summary: "High for source identity and reported tables; medium for interpretation; low for independent reproducibility because code, data, and reruns were unavailable."
safety_scope: "public scholarly review and safety-oriented edge inspection design"
distribution_notes: "Public URLs and repository-relative paths only; private source locations and exact local execution details withheld."
---

# HSD FTI-FDet - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Reference | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Efficient Visual Fault Detection for Freight Train Braking System via Heterogeneous Self Distillation in the Wild | Primary paper | arXiv HTML and PDF | arXiv:2307.00701v1 | https://arxiv.org/abs/2307.00701; https://arxiv.org/html/2307.00701; https://arxiv.org/pdf/2307.00701 | Evidence use only; no source file redistributed. | 2026-07-12 | Full text inspected |
| S2 | Advanced Engineering Informatics article record | Publisher metadata | Journal page and DOI | Volume 57, article 102091 | https://doi.org/10.1016/j.aei.2023.102091; https://www.sciencedirect.com/science/article/pii/S1474034623002197 | Publisher metadata/abstract inspected; no publisher file collected. | 2026-07-12 | Inspected |
| S3 | Private arXiv archive paper unit | Selection and local provenance | README and PDF | arXiv:2307.00701 | Location withheld | Private evidence; not deposited. | 2026-07-12 | Inspected |
| S4 | Extraction cache public summary | Processing evidence | JSON-derived public-safe record | schema 1.0 | Source URLs in S1 | pypdf text extraction succeeded; HTML/source package were absent locally. | 2026-07-12 | Inspected |
| S5 | SSP Detection - DEP-E | Related DEP entry | Markdown | DEP-E-20260711-SSP Oriented Detection | `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` | Processed Black Lake artifact; primary basis arXiv:2506.10601. | 2026-07-12 | Inspected |
| S6 | Tech Intel 1104 | Related DEP entry | Markdown | DEP-20260629-Tech Intel 1104 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260629-Tech%20Intel%201104/daily_research_findings_2026-06-29_1104.md | Finding 5 cites arXiv:2606.27797. | 2026-07-12 | Inspected |
| S7 | Tech Intel 1311 | Related DEP entry | Markdown | DEP-20260711-Tech Intel 1311 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260711-Tech%20Intel%201311/daily_research_findings_2026-07-11_1311.md | Findings 7-9 cite arXiv:2607.08015, 2607.08029, and 2607.08013. | 2026-07-12 | Inspected |
| S8 | Black Lake README | Repository authority | Markdown | main | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public DEP, artifact, attribution, and commit rules. | 2026-07-12 | Live file fetched and read |
| S9 | Black-Lake-Data README | Related repository authority | Markdown | main | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public related-repository layout and provenance rules. | 2026-07-12 | Live file fetched and read |

Paper metadata:

- `Full title`: Efficient Visual Fault Detection for Freight Train Braking System via Heterogeneous Self Distillation in the Wild.
- `Authors`: Yang Zhang, Huilin Pan, Yang Zhou, Mingying Li, Guodong Sun.
- `Affiliations`: Hubei University of Technology; Hubei Key Laboratory of Modern Manufacturing Quality Engineering; Nanjing University.
- `Dates`: arXiv v1 submitted 2023-07-03; journal article published in August 2023.
- `Publication`: *Advanced Engineering Informatics*, volume 57, article 102091.
- `Domain`: visual object detection, freight-train fault inspection, knowledge distillation, edge AI.
- `Code and data`: Not available from inspected sources. The four labeled datasets are described but were not collected or independently accessed.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S2 | Primary paper and publisher record | Title, authors, dates, abstract, DOI, venue. | Source identity and stated contribution. | High | Metadata does not establish reproducibility. |
| E2 | S1, sections 3.1-3.3 | Primary full text | Lightweight backbone, heterogeneous neck/head, feature coordinate attention, distributed box localization, composite losses. | Mechanism and method claims. | High for source reporting | Equations and implementation were not independently reimplemented. |
| E3 | S1, sections 4.1-4.3 and Tables 1-5 | Primary full text | Dataset splits, training setup, seven metrics, ablations, method comparisons, latency, memory, model size. | Author-reported empirical claims. | High for transcription; low for independent validity | No code/data rerun; best-result tuning and hardware-specific measurements. |
| E4 | S1, Figure 9 and conclusion | Primary full text | Uneven-lighting failures and proposed embedded-platform follow-up. | Boundary conditions and research gaps. | High | Failure analysis is narrow and largely qualitative. |
| E5 | S3, S4 | Private selection and extraction evidence | Archive identity, PDF presence, 12-page pypdf extraction, absent local HTML/source package. | Selection and processing methodology. | High | Private locations intentionally withheld. |
| E6 | S5 | Related processed DEP | Spatial partitioning, feature geometry, weak-label localization ambiguity, efficient object detection. | Spatial-prior synthesis. | Medium | Contextual analogy; does not validate HSD FTI-FDet. |
| E7 | S6 | Related raw DEP | Teacher/student asymmetry and topology-aware knowledge-distillation throughput. | Training-systems synthesis. | Medium | Entry is a concise research finding, not a reproduction. |
| E8 | S7 | Related raw DEP | Crossbar-aware compression, component-wise quantization, edge latency/energy, heterogeneous devices. | Hardware-aware deployment synthesis. | Medium | Findings cover adjacent models and hardware, not freight detection directly. |
| E9 | S8, S9 | Repository standards | DEP naming, inventory, attribution, stability, and public-safe deposition rules. | Artifact compliance. | High | Process evidence only. |

## Executive Summary

HSD FTI-FDet addresses a practical tension in freight-train braking inspection: small and ambiguous components must be detected quickly and accurately by hardware operating in uncontrolled outdoor environments. The method uses a lightweight feature extractor, a heterogeneous knowledge neck that preserves positional and cross-channel information, and a heterogeneous knowledge head that represents box localization as a distribution. Self-distillation transfers spatial and localization knowledge between heterogeneous teacher and student paths without relying on a large external teacher at inference time.

Across four author-curated component datasets, the paper reports 98.88% mean correct-detection rate, 0.027 seconds per image (>37 FPS), a 96 MB model, 581 MB training memory, and 1,159 MB testing memory. The authors report faster inference than earlier freight detectors and the strongest accuracy/model-size combination among the compared distillation methods. Ablations support the combined contribution of the neck, head, feature coordinate attention, depthwise-separable convolution, localization losses, and temperature choice.

The evidence supports the claim that HSD FTI-FDet is a promising accuracy-efficiency design under the paper's experimental conditions. It does not establish production readiness. Data and code were unavailable, model-specific tuning was used, all main results were measured on a GTX 2080 Ti, and the paper shows failures under uneven lighting. Reviewer confidence is therefore high for what the paper reports, medium for the architectural interpretation, and low for independent reproducibility or field generalization.

## Detailed Summary

### Problem Context

Freight braking systems depend on components such as bogie block keys, cut-out cocks, dust collectors, and brake-beam fastening bolts. Missing, displaced, or damaged parts can compromise safe operation. Images are acquired outdoors beneath trains, where target components may be small, contaminated, occluded, blurred, or visually similar to the background. This makes both localization and classification difficult while the field device also imposes model-size, compute, and speed constraints.

Earlier freight-image systems improved accuracy but remained computationally costly. General object detectors can be accurate yet too large or slow for the target environment. Knowledge distillation offers a compact-student path, but conventional feature imitation may underuse localization uncertainty and can require a computationally expensive teacher. The paper therefore frames the problem as preserving task-specific spatial and localization knowledge while shrinking the deployed detector.

### Architecture and Mechanism

HSD FTI-FDet contains a lightweight backbone, a heterogeneous knowledge neck (HKN), and a heterogeneous knowledge head (HKH). The teacher and student use related but heterogeneous neck/head paths, with the compact student learning privileged feature and output information.

The HKN augments feature-pyramid fusion with feature coordinate attention. Instead of collapsing all spatial information through global average pooling, it encodes horizontal and vertical directions separately, preserving position while modeling long-range cross-channel dependence. Depthwise-separable convolution reduces parameter and memory cost and helps suppress aliasing introduced during upsampling. The reported ablation is important: feature coordinate attention alone reduces CDR, while its combination with depthwise-separable convolution improves it. This suggests the value comes from a coupled design, not an attention module in isolation.

The HKH models bounding-box localization as a general distribution rather than only a point estimate. A fault distribution loss trains the distribution near the label, a fault regression loss refines the predicted position, and a fault classification loss handles class confidence. Kullback-Leibler divergence transfers teacher knowledge to the student. A temperature parameter controls feature-distribution smoothing; the BBK sensitivity table peaks at a temperature of 15.

### Data and Evaluation

The four datasets are derived from earlier freight inspection work and labeled for this study:

| Dataset | Training images | Test images | Component |
|---|---:|---:|---|
| BBK | 5,440 | 2,897 | Bogie block key |
| COH | 815 | 850 | Cut-out cock |
| DCM | 815 | 850 | Dust collector |
| FBM | 1,724 | 1,902 | Missing fastening bolt on brake beam |

The paper evaluates correct detection rate (CDR), missing detection rate (MDR), false detection rate (FDR), training memory, testing memory, inference time, and model size. Images are scaled to 700 x 512 and horizontally flipped with probability 0.5. Models use SGD with momentum 0.9, weight decay 1e-5, batch size 4, a 12-epoch schedule, and learning-rate drops at epochs 8 and 11. Experiments run on one GTX 2080 Ti under Ubuntu 20.04. The authors state that hyperparameters for each Table 5 model were fine-tuned for the greatest result.

### Main Results and Ablations

HSD FTI-FDet is reported at 98.88% mCDR, 0.37% mMDR, 0.75% mFDR, 0.027 seconds per image, 96 MB model size, 581 MB training memory, and 1,159 MB testing memory. It is 2.6 times faster than FTI-FDet and 2.2 times faster than Light FTI-FDet in the paper's comparison, while matching YOLOX inference time. FTI-FDet, Light FTI-FDet, and Cascade R-CNN have slightly higher mCDR, but the paper emphasizes their larger size or slower speed.

On the BBK dataset, the ResNet18 self-distillation baseline is 98.96% CDR and 219 MB. Adding HKN alone reports 99.34% and 190 MB; HKH alone reports 99.90% and 170 MB; combining both reports 99.55% and 96 MB. The combined configuration sacrifices some peak single-module accuracy to achieve the smallest package. Feature coordinate attention plus 7 x 7 depthwise-separable convolution reports 99.34% CDR versus 98.96% for the baseline neck. Temperature 15 reports 99.76% CDR, compared with 99.55% at 10 and 98.76% at 20.

### Limitations and Boundary Conditions

The paper directly identifies reduced robustness in overexposed and underexposed scenes and proposes data expansion and preprocessing augmentation. It does not report repeated seeds, confidence intervals, calibration, energy use, thermal behavior, or latency tails. The component datasets are not available in the inspected sources, preventing independent verification of labels, splits, class balance, leakage, or domain diversity. Because all comparison models are fine-tuned for best results, fairness depends on tuning budgets that are not fully characterized.

The resource argument is also incomplete for the intended deployment. GTX 2080 Ti measurements do not establish performance on Raspberry Pi, Jetson Nano, or the rail-side acquisition hardware named as future work. Testing memory being higher than training memory for the proposed model deserves implementation-level explanation. Finally, high mean correct-detection rate can obscure rare but safety-critical false negatives; component-wise recall, calibration, and operational escalation policy are more decision-relevant than a single average.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | HSD FTI-FDet combines a lightweight backbone, heterogeneous neck/head, spatial attention, distributed localization, and self-distillation. | Author method claim | E2 | Directly supported by the method sections and diagrams. | High |
| C2 | The method achieves 98.88% mCDR at 0.027 seconds per image with a 96 MB model. | Author empirical claim | E3 | Table 5 and conclusion agree; not independently reproduced. | High for reporting; low for reproduction |
| C3 | The method is faster than prior freight detectors while using less memory and a smaller model than most compared detectors. | Author comparative claim | E3 | Supported within the paper's hardware/tuning setup; cross-framework fairness remains uncertain. | Medium |
| C4 | HKN and HKH jointly improve the baseline accuracy-resource trade-off. | Author ablation claim | E3 | Component ablations support a trade-off, but no repeated-seed uncertainty is reported. | Medium-high |
| C5 | The detector is appropriate for field deployment. | Author implication | E3, E4 | Only partially supported; embedded-hardware, shift, calibration, and energy evidence are missing. | Low-medium |
| C6 | Spatial priors, asymmetric distillation systems, and hardware-aware compression form a coherent deployment pipeline. | Reviewer interpretation | E6-E8 | Conceptually well aligned across the three related DEP entries; not experimentally validated as one system. | Medium |

## Methodology

- `Research objective`: Randomly select one eligible archived arXiv paper, review it source-first, synthesize it with exactly three related DEP entries, and preserve a public-safe DEP research artifact.
- `Sources inspected`: Private archive README and PDF; extracted full PDF text; arXiv abstract and HTML; publisher metadata; live Black Lake and Black-Lake-Data READMEs; and three related DEP documents.
- `Discovery strategy`: Enumerated PDFs using `rg --files -g "*.pdf"`, treated each parent directory as a paper unit, chose a uniform zero-based index using PowerShell `Get-Random`, derived the arXiv ID from the PDF filename and README, and searched ID, DOI, title phrases, and slug markers across repository artifacts and memory.
- `Inclusion criteria`: Included sources that identify the paper, expose method/results/limitations, define repository rules, or provide concrete overlap in spatial detection, distillation systems, and edge deployment.
- `Exclusion criteria`: Excluded duplicate paper units, secondary summaries when primary material was available, unverified code claims, local path disclosure, source redistribution, and unrelated DEP entries.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, replication, safety/ethics, and provenance review.
- `Evidence handling`: Major claims map to evidence ledger IDs; exact metrics come from inspected tables; author claims and reviewer inference are labeled separately.
- `Uncertainty handling`: Missing code/data, best-result tuning, proprietary dataset composition, single-hardware tests, absent statistical uncertainty, and untested deployment assumptions remain explicit.
- `Extraction process`: Public-safe preflight found no working PDF extractor. After an approved pypdf installation, missing-only extraction produced 56,031 bytes of text from the 12-page private PDF. No local HTML or source package was available. Public arXiv HTML supplied a second full-text check.
- `Version control`: Paper pinned to arXiv:2307.00701v1 and the published article DOI; repository authority files fetched from live default branches.
- `Random selection and eligibility`: 75,761 PDF candidates and 75,761 parent-directory paper units; uniform zero-based index 13,859; selected arXiv:2307.00701; zero duplicate exclusions and zero reselections. Dedup scans covered Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and Black-Lake-Data with a 2026-07-11 date-only 24-hour marker cutoff.
- `Reviewer stance`: DEP-ready preservation, skeptical paper review, product translation, and bounded implementation planning.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's architecture, experiment design, reported results, limitations, deployment relevance, and synthesis with three related DEP entries.
- `Temporal boundary`: Primary paper v1 and journal record from 2023; repository context inspected through 2026-07-12.
- `Evidence limits`: Code, datasets, checkpoints, raw metrics, and embedded-hardware measurements were unavailable; experiments were not rerun.
- `Assumptions`: Table values are transcribed correctly and refer to the stated experimental setup; related DEP summaries accurately represent their cited primary papers.
- `Constraints`: Public-safe output, no private path disclosure, no source redistribution without established permission, and no production safety claim from unreplicated results.
- `Out of scope`: Reimplementation, dataset acquisition, field deployment, certification, legal compliance determination, and safety-case approval.
- `Intended use`: Research review, DEP deposition, replication planning, and edge-inspection product ideation.
- `Audience`: Computer-vision researchers, ML-systems engineers, rail-inspection product teams, and safety reviewers.
- `Reproducibility boundary`: Architecture and evaluation can be planned from the paper, but the headline results cannot be independently reproduced without equivalent data and implementation.
- `Data sensitivity`: Public scholarly sources plus private archive provenance; no personal or operational rail data deposited.

## Observations

- `Observed pattern`: The best compact result is not the most accurate ablation. HKN+HKH yields 99.55% CDR but the smallest 96 MB model, making the contribution explicitly Pareto-oriented.
- `Technical implication`: Feature coordinate attention helps only when paired with an operation that controls redundant/aliased information, warning against treating attention as a standalone improvement.
- `Contradiction or tension`: A 90 MB Light FTI-FDet model is slightly smaller than the proposed 96 MB model, so “smallest model” is accurate only within particular comparison groups, especially distillation methods.
- `Open question`: Why does the proposed method report higher testing memory than training memory, and how is each memory number measured?
- `Reviewer hypothesis`: Spatially gated distillation could improve rare-fault recall by transferring teacher information only at component boundaries and ambiguous regions, but this requires direct ablation.

## Considerations

- Safety-critical evaluation should prioritize per-component false negatives, calibration, uncertainty, and escalation coverage over mean CDR alone.
- Field cameras introduce lighting, vibration, contamination, viewpoint, and maintenance drift; monitoring must detect these shifts before automated decisions are trusted.
- Compression choices are hardware-specific. Quantization or pruning that looks efficient by model size can increase latency or energy on a particular accelerator.
- Teacher/student training topology affects cost and reproducibility even when the deployed student is small; placement and throughput should be logged as part of the artifact.
- Dataset governance matters: capture conditions, label protocol, split construction, rare-event prevalence, and privacy/safety restrictions must be documented.
- A deployment should fail safe: low-confidence, out-of-distribution, or sensor-quality failures route to a human rather than silently producing an “all clear.”

## Strengths

- The work addresses accuracy, speed, memory, and model size together, matching the actual multi-objective nature of edge inspection.
- Method sections connect spatial feature preservation, localization uncertainty, and distillation rather than relying on a generic compression recipe.
- Four component datasets and seven metrics provide broader evidence than a single accuracy number.
- Ablations expose interactions between feature coordinate attention and depthwise-separable convolution and show the trade-off between peak accuracy and package size.
- The paper includes a visible uneven-lighting failure case and names embedded hardware as future validation, making at least one boundary condition explicit.

## Weaknesses

- No inspected code, public dataset, checkpoint, or independent reproduction supports the headline results.
- The evaluation uses one desktop GPU rather than the embedded platforms that motivate the method.
- Best-result fine-tuning across comparison models may create unequal tuning budgets, and no repeated-seed uncertainty is reported.
- Mean CDR/MDR/FDR do not expose component-specific safety risk, calibration, prevalence effects, or operational false-alarm burden.
- Uneven lighting is the only deeply visible failure analysis; occlusion, contamination, viewpoint shift, motion blur, multi-fault scenes, and sensor drift need systematic stress tests.
- The smallest-model claim requires qualification because Light FTI-FDet is listed at 90 MB versus 96 MB for HSD FTI-FDet.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code, splits, checkpoints, and label protocol | Reproducibility | Independent review is currently blocked. | Verifiable claims and easier transfer. | Data rights and maintenance effort. | External rerun with hashes and pinned environment. |
| Add lighting/domain augmentation and shift evaluation | Robustness | The disclosed failure is uneven exposure. | Lower field false negatives. | Synthetic shifts may not match reality. | Held-out sites, seasons, cameras, and controlled corruptions. |
| Report calibration and component-wise metrics | Safety evaluation | Mean CDR hides rare-component risk. | Better thresholds and escalation policy. | More complex evaluation. | Reliability curves, per-class recall, expected calibration error. |
| Benchmark on Jetson/Raspberry Pi-class targets | Deployment evidence | Desktop GPU speed is not the target constraint. | Real latency, energy, memory, and thermal data. | Porting and kernel variability. | Repeated p50/p95/p99 runs with power/temperature logging. |
| Add spatially masked distillation | Method | Related SSP work suggests partitions can focus localization knowledge. | Better ambiguous-boundary learning. | Mask error can suppress useful signal. | Controlled ablation against full-map distillation. |
| Profile asymmetric teacher placement | Training systems | Related DEP evidence suggests topology affects distillation throughput. | Lower training cost and clearer scaling. | Infrastructure complexity. | Samples/second, utilization, memory, and convergence parity. |

## Potential Implementations

### Rail-Side Inspection Gate

- `User`: Freight maintenance inspector.
- `Goal`: Flag missing or displaced braking components without treating uncertain frames as safe.
- `Core mechanism`: Compact HSD-style detector plus lighting/OOD gate and human review queue.
- `Required inputs`: Calibrated undercarriage images, component taxonomy, validation thresholds, sensor-health telemetry.
- `Outputs`: Bounding boxes, fault class, confidence, shift flags, and review decision.
- `Risk controls`: Fail-safe escalation, immutable image/decision audit, per-site calibration, no autonomous train-control action.
- `Evaluation`: Per-component recall, false alarms per train, calibration, p95 latency, and shift-detection coverage.

### Distillation Experiment Service

- `User`: ML systems engineer.
- `Goal`: Compare teacher/student necks, heads, transfer losses, and placement strategies reproducibly.
- `Core mechanism`: Versioned experiment matrix with spatial-mask and full-map distillation, topology profiles, and artifact hashes.
- `Required inputs`: Licensed dataset, teacher/student configs, hardware inventory, evaluation contract.
- `Outputs`: Pareto front for recall, latency, memory, model size, and training cost.
- `Risk controls`: Split isolation, seed repetition, provenance capture, and leakage checks.
- `Evaluation`: Repeated-seed metrics, throughput, utilization, convergence, and reproducible package export.

### Hardware-Aware Packaging Pipeline

- `User`: Edge deployment engineer.
- `Goal`: Choose quantization/pruning/runtime variants by measured target behavior.
- `Core mechanism`: Compile each candidate for each target, calibrate on representative data, reject candidates below safety thresholds, then rank by energy and latency.
- `Required inputs`: Student checkpoint, calibration set, target devices, runtime toolchains, acceptance thresholds.
- `Outputs`: Signed package, device-specific benchmark report, and rollback metadata.
- `Risk controls`: Minimum recall/calibration gates, thermal soak, rollback, dependency pinning, and canary deployment.
- `Evaluation`: p50/p95/p99 latency, energy per frame, peak memory, thermal throttling, and fault recall.

## Three Ways to Exercise This Research

1. `Paper-to-benchmark audit`: Objective—test whether the reported trade-off is internally consistent. Inputs—the paper tables and a structured metric sheet. Method—recompute speed ratios, Pareto dominance, and claim qualifiers. Output—a discrepancy ledger. Success—every headline number maps to a table row and hardware condition. Stop condition—unresolvable source inconsistency is recorded rather than guessed.
2. `Synthetic shift gate`: Objective—exercise the uneven-lighting limitation safely. Inputs—public toy component images or synthetic shapes. Method—apply exposure/contrast shifts, run a placeholder detector score, and route shifted frames to review. Output—coverage versus review-load curve. Success—no shifted low-confidence sample is silently accepted. Stop condition—if calibration data are insufficient, do not set a production threshold.
3. `Hardware Pareto smoke test`: Objective—compare small model variants on available edge hardware. Inputs—non-sensitive sample frames and two exported toy detectors. Method—measure latency, memory, and energy while enforcing a fixed recall proxy. Output—a device-specific candidate ranking. Success—measurements are repeated and versioned. Stop condition—thermal throttling or runtime mismatch invalidates the run.

## Example MVP Product

- `Product name`: RailSight Review Gate.
- `Target user`: Freight-train maintenance inspection teams.
- `Problem`: Fast visual screening is valuable, but environmental shift and rare false negatives make fully automated clearance unsafe.
- `Core workflow`: Ingest a frame; check sensor/lighting quality; run the compact detector; calibrate confidence; accept only high-confidence in-distribution detections; route all other frames to a reviewer; preserve evidence and reviewer resolution.
- `Data requirements`: Licensed component images with site/camera metadata, explicit train/site split policy, lighting and occlusion tags, and a review-only synthetic development set.
- `Architecture`: Local edge inference, deterministic quality gate, compact detector, calibrated decision layer, append-only audit log, and review dashboard. No automatic actuation.
- `Success metrics`: Per-component recall above the safety target, bounded false alarms per train, calibrated confidence, p95 latency below the operational budget, and complete audit coverage.
- `Risk controls`: Human confirmation for faults and uncertain negatives, site-specific canaries, shift alarms, signed model packages, rollback, and periodic revalidation.
- `Limitations`: The MVP does not diagnose mechanical severity, replace mandated inspection, or establish regulatory compliance. It depends on representative licensed data and target-hardware testing.
- `MVP boundary`: One camera type, four component classes, offline reviewer queue, no train-control integration.
- `Deployment model`: Local-only edge service with a browser review console on the operator network.
- `Evaluation plan`: Offline split audit, corruption suite, calibration test, hardware soak, shadow deployment, and human-factor review before any operational use.
- `Failure modes`: Over/underexposure, occlusion, dirty lens, unseen component variant, confidence miscalibration, thermal throttling, and review backlog.
- `Maintenance plan`: Versioned datasets and thresholds, monthly drift review, device telemetry, dependency monitoring, and rollback drills.

## Related Research and Reading

| Related DEP entry | Type | Relevance | Source/reference basis |
|---|---|---|---|
| `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` | Processed Black Lake DEP-E manuscript | Adds explicit spatial partitions, boundary priors, and weak-label localization analysis to the detector-design side of the synthesis. | Inspected DEP manuscript; primary reference https://arxiv.org/abs/2506.10601. |
| https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260629-Tech%20Intel%201104/daily_research_findings_2026-06-29_1104.md | Black-Lake-Data DEP finding | Finding 5 reframes teacher/student asymmetry as a topology and throughput problem for scalable distillation. | Inspected DEP finding; primary reference https://arxiv.org/abs/2606.27797. |
| https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260711-Tech%20Intel%201311/daily_research_findings_2026-07-11_1311.md | Black-Lake-Data DEP findings | Findings 7-9 connect compression to non-ideal accelerators, component-wise quantization, energy, latency, and heterogeneous edge devices. | Inspected DEP findings; primary references https://arxiv.org/abs/2607.08015, https://arxiv.org/abs/2607.08029, and https://arxiv.org/abs/2607.08013. |

Synthesis: the primary paper identifies which spatial and localization information a compact detector should preserve; SSP supplies a structured spatial-prior mechanism; topology-aware distillation addresses how to train the teacher/student pair efficiently; and hardware-aware compression determines which student variant actually works on the target device. This is an inference from the inspected sources, not a jointly validated result.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2307.00701 | Identity, authors, abstract, dates, primary locator. | 2026-07-12 | Primary source. |
| R2 | https://arxiv.org/html/2307.00701 | Full method, tables, ablations, results, limitations. | 2026-07-12 | Primary full text. |
| R3 | https://arxiv.org/pdf/2307.00701 | Public PDF locator corresponding to private inspected PDF. | 2026-07-12 | Not redistributed. |
| R4 | https://doi.org/10.1016/j.aei.2023.102091 | Publication identity. | 2026-07-12 | DOI record. |
| R5 | https://www.sciencedirect.com/science/article/pii/S1474034623002197 | Publisher abstract, highlights, volume/article metadata. | 2026-07-12 | Near-primary publisher page. |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | DEP and attribution authority. | 2026-07-12 | Live default-branch file. |
| R7 | `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md` | Related spatial object-detection synthesis. | 2026-07-12 | Processed repository source. |
| R8 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository layout and provenance authority. | 2026-07-12 | Live default-branch file. |
| R9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260629-Tech%20Intel%201104/daily_research_findings_2026-06-29_1104.md | Related distillation-systems finding. | 2026-07-12 | Processed repository source. |
| R10 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260711-Tech%20Intel%201311/daily_research_findings_2026-07-11_1311.md | Related edge-compression and hardware findings. | 2026-07-12 | Processed repository source. |
| R11 | https://arxiv.org/abs/2506.10601 | Primary basis cited by R7. | 2026-07-12 | Contextual source. |
| R12 | https://arxiv.org/abs/2606.27797 | Primary basis cited by R9. | 2026-07-12 | Contextual source. |
| R13 | https://arxiv.org/abs/2607.08015 | Crossbar-aware compression basis cited by R10. | 2026-07-12 | Contextual source. |
| R14 | https://arxiv.org/abs/2607.08029 | Hardware-aware small-VLM quantization basis cited by R10. | 2026-07-12 | Contextual source. |
| R15 | https://arxiv.org/abs/2607.08013 | Heterogeneous edge-learning basis cited by R10. | 2026-07-12 | Contextual source. |

## Appendix

### Selection and Dedup Record

- Enumeration: `rg --files -g "*.pdf"` against the private archive.
- Candidate PDFs: 75,761.
- Unique parent-directory paper units: 75,761.
- Random selection: uniform PowerShell `Get-Random` index.
- Selected zero-based index: 13,859.
- Selected identifier: arXiv:2307.00701.
- Dedup keys: arXiv ID, DOI, normalized title, and HSD FTI-FDet slug.
- Scan locations: Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and Black-Lake-Data.
- 24-hour cutoff: 2026-07-11 date-only public marker.
- Exclusions: 0.
- Reselections: 0.

### Replication Checklist

- [ ] Obtain a legally usable equivalent dataset and document capture/label protocol.
- [ ] Pin code, framework, dependencies, and model configuration.
- [ ] Reproduce dataset splits and all seven reported metrics.
- [ ] Run at least three seeds and report uncertainty.
- [ ] Verify HKN, HKH, FCA, depthwise-separable convolution, loss, and temperature ablations.
- [ ] Benchmark GTX-class and at least two edge targets with latency tails, energy, memory, and thermal logs.
- [ ] Add calibration, component-wise recall, shift, lighting, occlusion, contamination, and multi-fault tests.
- [ ] Document discrepancies rather than tuning against the final test set.

### Source Inventory

No source files are deposited. The private archive README/PDF and private extraction cache were inspected but withheld. Public URLs R1-R15 preserve source identity and review context.
