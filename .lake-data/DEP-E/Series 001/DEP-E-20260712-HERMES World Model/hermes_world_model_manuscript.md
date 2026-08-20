---
title: "HERMES World Model - DEP-E"
generated_at: "2026-07-12 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of HERMES, a unified autonomous-driving model for 3D scene understanding and future point-cloud generation."
source_status: "mixed inspection; URLs only in public deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-12"
temporal_cutoff: "Sources inspected through 2026-07-12"
primary_url: "https://arxiv.org/abs/2501.14729"
stable_identifier: "arXiv:2501.14729; DOI marker 10.48550/arXiv.2501.14729"
confidence_summary: "High for reporting the inspected method and tables; medium for generalization and deployment implications because experiments were not reproduced."
safety_scope: "research, evaluation, and simulation planning only"
distribution_notes: "No original source files redistributed; public URLs and repository-relative references only."
---

# HERMES World Model - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | HERMES arXiv record and HTML | Primary paper | HTML | arXiv:2501.14729; DOI marker 10.48550/arXiv.2501.14729 | https://arxiv.org/abs/2501.14729; https://arxiv.org/html/2501.14729 | Public research record; arXiv terms apply | 2026-07-12 | Inspected |
| S2 | HERMES PDF from private source archive | Primary paper | PDF | arXiv:2501.14729 | Location withheld; public equivalent: https://arxiv.org/pdf/2501.14729 | Inspected locally; not redistributed | 2026-07-12 | Text extracted with `pypdf` |
| S3 | ICCV 2025 open-access paper | Near-primary publication | HTML/PDF | ICCV 2025 accepted paper | https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HERMES_A_Unified_Self-Driving_World_Model_for_Simultaneous_3D_Scene_ICCV_2025_paper.html | CVF open-access version; publisher terms apply | 2026-07-12 | Inspected |
| S4 | Official HERMES repository | Official implementation | Repository | `LMD0311/HERMES`, main branch | https://github.com/LMD0311/HERMES | Apache-2.0 code license visible; dataset licenses remain separate | 2026-07-12 | README and repository structure inspected; code not run |
| S5 | VideoWeave Geometry DEP-E | Related processed artifact | Markdown | DEP-E-20260709-VideoWeave Geometry | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Repository artifact; underlying sources separately attributed | 2026-07-12 | Inspected |
| S6 | VLM Probing DEP-E | Related processed artifact | Markdown | DEP-E-20260712-VLM Probing | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Repository artifact; underlying sources separately attributed | 2026-07-12 | Inspected |
| S7 | Visual world-model hallucination finding | Related source summary | Markdown | DEP-20260628-Tech Intel 0102, item 6 | `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md` | Related summary cites arXiv:2606.27326 | 2026-07-12 | Inspected |

The paper lists Xin Zhou, Dingkang Liang, Sifan Tu, Xiwu Chen, Yikang Ding, Dingyuan Zhang, Feiyang Tan, Hengshuang Zhao, and Xiang Bai as authors. The affiliations are Huazhong University of Science and Technology, MEGVII Technology, Mach Drive, and The University of Hong Kong. The initial arXiv date is 2025-01-24, and the work appears in ICCV 2025. No separate publisher DOI was visible in the inspected sources, so the arXiv DOI marker is retained without implying a distinct proceedings DOI.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S2 | Primary paper | Abstract, Sections 1–6, Tables 1–5, supplementary Tables S1–S5, discussion, and limitations | Identity, mechanism, datasets, results, ablations, compute, and source-disclosed limits | High for reporting | Author-reported evidence; PDF extraction contains minor character artifacts |
| E2 | S3 | Accepted conference paper | Accepted-paper metadata and full-text cross-check | ICCV 2025 status and consistency with the reviewed paper | High | Publication is not independent replication |
| E3 | S4 | Official repository | Repository structure, getting-started guides, release news, citation, and visible license | Public implementation and artifact availability boundary | Medium-high | Code, checkpoints, and processed data were not executed or audited in depth |
| E4 | S5 | Related DEP manuscript | Geometry-latent world generation, spatial-consistency metrics, and implementation observations | Cross-DEP geometry synthesis | Medium | Does not validate HERMES results |
| E5 | S6 | Related DEP manuscript | Fusion, modality, layer, attention-head, mismatch, and leakage probes | Representation-audit synthesis for BEV/text/world-query transfer | Medium | VALUE studies different architectures and datasets |
| E6 | S7 | Related DEP finding | Perceptual, action-marginalized, and scene-diverging hallucinations; coverage-aware adaptation | Failure taxonomy and coverage synthesis | Medium | Source summary was inspected, not the full underlying paper |
| E7 | Repository and memory scans | Process evidence | arXiv IDs, DOI marker, normalized title, slug variants, and recent same-paper markers | Random-selection eligibility and deduplication | High | The used-ID index deliberately over-excludes papers mentioned only as references |

## Executive Summary

HERMES proposes a unified driving world model that uses one Bird's-Eye View representation for two tasks that are usually separated: describing and answering questions about the current 3D driving scene, and generating future point-cloud evolution. The core mechanism compresses six camera views into BEV tokens, processes them with an InternVL2-derived language model, initializes future world queries from BEV features, enriches those queries through causal attention to the preceding scene and text context, and expands them through a current-to-future link before rendering point clouds.

The paper reports strong open-loop validation results. Against ViDAR, HERMES reduces 3-second Chamfer distance from 1.73 to 1.17, approximately 32.4%. Against OmniDrive, it raises CIDEr from 0.686 to 0.741, approximately 8.0%. A separated-unification baseline preserves similar language scores but produces worse future geometry, while a world-query ablation reports about a 10% generation improvement with a small understanding tradeoff. Supplementary results report 61.9% NuScenes-QA accuracy and provide training, scaling, query-count, and data-alignment details.

The evidence supports the narrower claim that shared BEV and language-conditioned query pathways can improve the paper's chosen generation and understanding metrics in the tested setup. It does not establish closed-loop driving safety, robust perception, future image generation, calibration, long-tail reliability, or causal dependence on language-derived knowledge. Reviewer confidence is high for reporting the source and medium for generalizing beyond nuScenes-derived evaluation. The most useful implementation takeaway is therefore an evaluation architecture: couple spatially grounded generation with causal representation probes and coverage-aware failure testing before treating the model as a simulator or planning substrate.

## Detailed Summary

### Problem Context

Driving world models learn to forecast future observations, often as video, occupancy, or point clouds. Such models can support simulation and planning research, but their latent states are difficult to interpret and they usually do not answer questions about the scene. Driving vision-language models handle descriptions, VQA, and reasoning, yet usually stop at text or action outputs and do not reconstruct future 3D geometry. HERMES frames this separation as a missed opportunity: semantic scene understanding could condition geometric evolution, while a spatially grounded representation could make language reasoning more coherent across multiple cameras.

Two engineering constraints drive the design. First, raw multi-view image tokens are too numerous for a compact language model and do not naturally express cross-camera geometry. Second, simply sharing features between a language model and a separate future generator may fail to transfer scene knowledge across the tasks. HERMES uses BEV for the first problem and world queries plus a current-to-future link for the second.

### World Tokenizer and Renderer

Six current camera images enter an OpenCLIP ConvNeXt-L backbone and single-frame BEVFormer v2. The encoded scene has a 200 by 200 spatial grid with 256 channels. A downsampling block converts this to a 50 by 50 grid and raises the channel dimension, producing 2,500 BEV tokens instead of the roughly 47,000 tokens cited for raw multi-view processing. The compressed BEV is projected into the language-model channel space.

The renderer reverses that process. It upsamples encoded BEV states, creates a height dimension, and uses 3D convolutions to form a volumetric representation. Rays matching the dataset's LiDAR setup sample the volume. A shallow network predicts signed-distance-function values, and differentiable volume rendering integrates depth along each ray. The same renderer reconstructs the current point cloud as an auxiliary task and generates future point clouds.

### Understanding and World Queries

The language branch follows multimodal next-token prediction. BEV tokens and user text prompts enter an InternVL2-derived model so that the system can describe the scene and answer questions. For future generation, HERMES creates one group of world queries per predicted frame. Max pooling over the BEV initializes the queries; future ego-motion and frame embeddings specify the intended time and vehicle motion.

Because the world queries appear after the current BEV and textual context in the causal sequence, they can attend to both. The authors interpret the resulting states as carrying world knowledge from the understanding process. Each sparse query group then acts as key and value in three current-to-future cross-attention blocks, while the encoded current BEV supplies the query. Self-attention and feed-forward layers refine the future BEV states before rendering.

### Objectives and Training

Text is trained with the standard autoregressive next-token objective. Point-cloud depth is trained with a weighted L1 loss across the current and three future frames; the total objective adds ten times the depth loss to the language loss. The supplementary material reports three stages:

1. Train the BEV tokenizer and renderer on 12 Hz nuScenes data to reconstruct the current point cloud.
2. Align BEV and text, first training projections and then refining the model with LoRA and broader parameter updates. NuInteract dense captions and OmniDrive-nuScenes scene descriptions support this stage. Masking and caption splicing expand the multi-view image-text set to about 200,000 pairs.
3. Add future-generation modules and jointly train understanding and point-cloud evolution on nuScenes and OmniDrive-nuScenes material.

The reported configuration uses AdamW, 32 NVIDIA H20 GPUs, and 36 epochs in the final stage. These details improve inspectability but do not provide a resource-normalized comparison with every baseline.

### Datasets and Metrics

NuScenes contributes 700 training, 150 validation, and 150 test scenes with six cameras and LiDAR. NuInteract contributes roughly 1.5 million dense language annotations. OmniDrive-nuScenes adds captions and VQA pairs generated with GPT-4. Generation uses Chamfer distance within a bounded 3D region. Understanding uses METEOR, ROUGE, and CIDEr. Supplementary NuScenes-QA results add single-word VQA accuracy.

These metrics capture useful but incomplete properties. Chamfer distance summarizes geometric proximity without directly measuring object identity, semantic severity, collision risk, or rare-agent misses. Text-overlap metrics can reward phrasing similarity without establishing grounded, calibrated, safety-relevant understanding. The evaluation is therefore appropriate evidence for model comparison, not deployment readiness.

### Main Results

HERMES reports 0.59, 0.78, 0.95, and 1.17 Chamfer distance at 0, 1, 2, and 3 seconds. ViDAR reports 1.12, 1.38, and 1.73 at 1–3 seconds and uses a three-second history, whereas HERMES uses only the current multi-view frame. HERMES reports METEOR 0.384, ROUGE 0.327, and CIDEr 0.741. OmniDrive reports 0.380, 0.326, and 0.686. These tables support the paper's headline 32.4% generation and 8.0% CIDEr improvements within the stated validation protocol.

The separated-unification model reports generation 0.60/0.84/1.08/1.37 and understanding 0.384/0.327/0.745. HERMES improves all four generation horizons but is slightly lower on CIDEr. On quarter-data ablations, joint training is also slightly worse than single-task training at some metrics, revealing an optimization cost. This is important negative evidence: the framework does not make every task uniformly better.

### Ablations and Failure Signals

World queries reduce full-data 3-second Chamfer distance by roughly 10% but lower CIDEr by about 1%. Processing the queries through the language model improves generation relative to bypassing it, which supports—but does not causally prove—the proposed transfer story. Max pooling performs better than attention or average pooling for the reported 3-second geometry. Four queries per future group provide the selected tradeoff; more queries do not monotonically help.

A 50 by 50 BEV improves 0-second Chamfer distance and CIDEr over 25 by 25, but its 3-second Chamfer value is slightly worse. Larger language models improve most reported metrics, with 3.8B parameters outperforming 1.8B on CIDEr and 3-second geometry, though the paper uses 1.8B as a compute/performance compromise. Qualitative examples disclose difficulty with significant turns, occlusion, and low-light scenes.

### Source-Disclosed and Reviewer-Identified Limits

The paper explicitly leaves perception tasks and future image generation unimplemented. Reviewer-identified limits include no closed-loop planning evaluation, no calibrated uncertainty, limited evidence for long-tail events, unclear sensitivity to sensor faults, and no object-level failure severity. The future ego-motion condition is supplied, so the model is not an end-to-end planner. The paper's strong point-cloud and language metrics should not be interpreted as proof of safe vehicle behavior.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | One BEV representation can support both scene understanding and future point-cloud generation. | Author architectural claim | E1, E2 | Directly supported by the implemented pipeline and reported dual-task outputs. | High for existence |
| C2 | HERMES reduces 3-second generation error by 32.4% relative to ViDAR. | Author empirical claim | E1, Table 1 / S4 | 1.17 versus 1.73 supports the percentage; different model histories and components complicate broad causal attribution. | High for reported table |
| C3 | HERMES improves CIDEr by 8.0% relative to OmniDrive. | Author empirical claim | E1, Table 1 | 0.741 versus 0.686 supports the relative improvement; CIDEr is not a complete grounding metric. | High for reported table |
| C4 | LLM-processed world queries transfer understanding knowledge into future generation. | Author mechanism claim | E1, Figure 3 and query ablations | Ablations support association and performance contribution, but do not isolate semantic knowledge causally. | Medium |
| C5 | BEV is an effective compression and cross-modal interface. | Author claim supported by ablation | E1, Table 5 and supplement discussion | 2,500-token interface and resolution ablation support usefulness; long-horizon tradeoffs remain. | Medium-high |
| C6 | The official repository makes HERMES materially more reproducible. | Reviewer interpretation | E3 | Code, guides, weights, and processed-data links improve the boundary, but no reproduction occurred and dataset terms remain separate. | Medium |
| C7 | HERMES should be evaluated with causal and coverage-aware diagnostics before simulator use. | Reviewer interpretation | E4, E5, E6 | Strong synthesis from related entries, not an author-validated HERMES result. | Medium |
| C8 | The paper was eligible for this deposit. | Process claim | E7 | No selected-paper marker was found in the required locations or recent window. | High |

## Methodology

- `Research objective`: Review one randomly selected, eligible arXiv paper source-first; preserve its evidence and limitations; relate it to exactly three existing deposits; and produce a schema-complete DEP-E manuscript.
- `Sources inspected`: Private archive PDF and adjacent provenance metadata; arXiv abstract, HTML, and public PDF locator; ICCV 2025 open-access paper; official HERMES repository; live repository README authorities; and exactly three related DEP entries.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, treated each unique PDF parent as a paper unit, drew a uniform `Get-Random` index, resolved identity from nearby metadata, extracted full PDF text with `pypdf`, browsed public primary sources, and searched both repositories for duplicates and conceptual overlap.
- `Inclusion criteria`: Sources had to establish paper identity, support method/results claims, define repository rules, document selection/dedup provenance, or provide concrete overlap in geometry-aware generation, multimodal fusion auditing, or world-model failure coverage.
- `Exclusion criteria`: Secondary summaries were not used for HERMES technical claims. Broad keyword matches without concrete conceptual overlap were excluded. No source file was redistributed.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, safety/ethics, and replication analysis.
- `Evidence handling`: Author claims are separated from reviewer interpretation. Quantitative values are tied to inspected tables. Related DEP entries support synthesis only.
- `Uncertainty handling`: Non-reproduction, metric limits, absent publisher DOI, untested code, dataset-license boundaries, and causal ambiguity are explicit.
- `Extraction process`: `pypdf` extracted 76,272 bytes from the local PDF. Public arXiv HTML and the ICCV paper cross-checked sections, tables, and supplementary details.
- `Version control`: Paper identity is pinned to arXiv:2501.14729 and the ICCV 2025 open-access paper; the official repository's main branch was inspected without executing it.
- `Claim selection`: Priority went to the architecture, datasets, headline comparisons, negative tradeoffs, ablations, source-disclosed limitations, compute, and reproducibility boundary.
- `Cross-checking`: Headline percentages were recomputed from reported table values; methods and venue status were checked across arXiv, ICCV, PDF text, and the official repository.
- `Safety handling`: Implementation examples use synthetic or aggregate metrics and are framed for evaluation and simulation research, not vehicle control.
- `Random selection`: Uniform zero-based index 69,210 over 75,761 unique PDF-parent paper units; the first draw was accepted.
- `Deduplication`: Scanned Black Lake logs, reports, lake-data, automation memory, and relevant Black-Lake-Data entries by arXiv ID, DOI marker, normalized title, and slug. The context contained 363 unique arXiv IDs; 67 candidate units matched an observed ID; none matched this paper.
- `Recent-marker validation`: No same-paper marker was found in the preceding 24 hours; duplicate rejections and reselections were zero.
- `Reviewer stance`: Critical paper report, DEP-ready preservation, implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: HERMES's architecture, training, datasets, reported evidence, limitations, related-deposit synthesis, and bounded implementation implications.
- `Temporal boundary`: Sources inspected through 2026-07-12; primary paper identity is the 2025 arXiv/ICCV work.
- `Evidence limits`: No training, inference, checkpoint validation, dataset download, figure-level quantitative audit, or closed-loop simulation was performed.
- `Assumptions`: The locally archived PDF, arXiv full text, ICCV paper, and official repository describe the same core work; table extraction is accurate where cross-checked.
- `Constraints`: Public artifacts exclude private locations, machine identifiers, timezone labels, exact execution timestamps, and uncollected source files. Dataset and checkpoint terms may differ from the repository's code license.
- `Out of scope`: End-to-end autonomous-driving deployment, safety certification, legal approval, real-vehicle control, dataset redistribution, and production performance claims.
- `Intended use`: Research review, DEP deposition, evaluation planning, replication planning, and safe simulator-tool ideation.
- `Audience`: World-model researchers, autonomous-driving ML engineers, multimodal evaluators, safety reviewers, and Black Lake maintainers.
- `Depth target`: Full schema-complete manuscript with quantitative preservation and implementation translation.
- `Reproducibility boundary`: Public code and guides improve the path to reproduction, but this deposit does not independently verify any result.
- `Operational boundary`: Concepts may inform offline evaluation and simulation; they should not directly actuate a vehicle.
- `Data sensitivity`: Public research records plus privately held source presence; no private location or raw sensor dataset is published.

## Observations

- `Observed pattern`: HERMES's strongest contribution is an interface design—BEV plus world queries—rather than a new language model or a new renderer in isolation.
- `Observed tradeoff`: Better future geometry does not always coincide with better language metrics; world queries and joint optimization can slightly reduce CIDEr.
- `Technical implication`: Evaluation should track a Pareto surface across geometry horizons, language grounding, compute, and failure slices instead of one aggregate score.
- `Evidence-quality implication`: The separated-unification baseline supports cross-task interaction, but it does not isolate whether gains come from semantic knowledge, added capacity, or a better optimization route.
- `Cross-source pattern`: The official repository's release material narrows the reproducibility gap compared with a paper-only artifact, yet execution and dataset governance still require separate review.
- `Cross-DEP pattern`: VideoWeave supplies geometry-consistency framing, VLM Probing supplies representation diagnostics, and the hallucination finding supplies coverage-aware failure analysis.
- `Open question`: How much future geometry changes when the text context is counterfactually edited while BEV input and ego-motion remain fixed?
- `Reviewer hypothesis`: Object-centric and scene-divergence metrics will reveal failures that average Chamfer distance underweights.

## Considerations

HERMES operates in a safety-critical domain, so model evaluation must distinguish simulation research from vehicle control. A future point cloud can be geometrically close on average while missing a cyclist, misplacing a barrier, or producing an implausible scene branch. Caption overlap can remain high while the answer is uncalibrated or wrong about a rare hazard. Release gates should therefore include object recall by severity, collision-relevant geometry, temporal identity, counterfactual consistency, calibration, and scenario coverage.

Data governance is also central. NuScenes, NuInteract, OmniDrive-nuScenes, pretrained vision encoders, language models, processed annotations, checkpoints, and repository code may have different licenses and usage restrictions. The visible Apache-2.0 code license does not automatically grant redistribution or commercial rights for every dataset and model artifact. A reproduction should build a source inventory before download or training.

Operational cost is nontrivial. The reported setup uses 32 H20 GPUs and multi-stage alignment. A practical evaluation MVP should start with released checkpoints, frozen-feature probes, small scenario slices, and aggregate metrics. Training from scratch is unnecessary for testing the central research question: whether language-conditioned query pathways contribute robust, causally meaningful geometry improvements.

The official HERMES++ follow-up shows that the research direction is evolving. Comparisons must pin versions because later designs may alter geometry constraints, future-link mechanisms, data, and benchmarks. This artifact reviews HERMES, not HERMES++.

## Strengths

- The paper identifies a real representational gap between driving world models and driving vision-language models.
- BEV is a defensible interface for compressing six views while retaining cross-view spatial relationships.
- The world-query/current-to-future design offers a concrete path for semantic context to affect future geometry.
- Results cover both specialist baselines and a separated-unification baseline, making the unification claim more testable.
- Ablations disclose non-monotonic effects from query count, pooling choice, BEV size, language-model scale, and horizon length.
- Supplementary material reports training stages, hardware, schedules, auxiliary objectives, and extra VQA results.
- Public code, guides, weights, and processed-data release material improve inspectability.
- The paper explicitly names perception and future images as missing capabilities rather than implying completeness.

## Weaknesses

- Experiments are concentrated on nuScenes-derived data and do not demonstrate broad geographic, weather, cultural, sensor, or long-tail generalization.
- Chamfer distance and language-overlap metrics do not measure safety-critical object severity, planning consequence, or calibration.
- The world-query ablation supports contribution but not causal semantic transfer; extra parameters and optimization pathways remain alternative explanations.
- Ground-truth future ego-motion narrows the generation task and does not test planning.
- Joint training shows small language and longer-horizon costs in some ablations.
- No perception-task integration, future image generation, or closed-loop evaluation is provided.
- The reported hardware footprint is substantial, and resource-normalized comparisons are limited.
- This review did not execute the released code, verify checkpoints, or reproduce datasets and metrics.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add object- and risk-weighted geometry metrics | Evaluation | Chamfer distance can hide rare but severe misses | Better alignment with driving consequence | Requires reliable annotations and severity policy | Compare ranking stability against Chamfer and human safety review |
| Run causal world-query interventions | Mechanism | Attention-based access does not prove knowledge transfer | Stronger attribution of gains to semantic conditioning | Intervention design may create out-of-distribution states | Query masking, feature patching, text counterfactuals, and region-level geometry deltas |
| Add uncertainty and calibration outputs | Reliability | Predictions are treated as point estimates | Safer downstream use and selective simulation | Calibration can vary by slice and horizon | Reliability diagrams, conformal coverage, abstention tests |
| Expand long-tail scenario coverage | Generalization | Average nuScenes performance may miss rare failures | Better robustness evidence | Data collection and labeling cost | Versioned slices for weather, occlusion, rare agents, and unusual maneuvers |
| Integrate perception and future images as evaluated branches | Completeness | Authors identify both as absent | Broader unified world representation | Multi-task interference and compute | Pareto analysis across perception, text, point cloud, and image metrics |
| Publish exact artifact pins and end-to-end reproduction scripts | Reproducibility | README-level availability is not a verified reproduction | Lower audit and onboarding cost | Ongoing maintenance burden | Clean-room run with checkpoint hashes, environment lock, expected outputs, and license inventory |

## Potential Implementations

1. `World-Model Evaluation Harness`
   - `User`: Autonomous-driving research and model-release teams.
   - `Goal`: Compare checkpoints across geometry, language grounding, calibration, cost, and scenario coverage.
   - `Core mechanism`: Load public aggregate outputs or offline predictions, compute horizon and slice metrics, and issue a versioned evidence bundle.
   - `Required inputs`: Synthetic or licensed evaluation scenes, predictions, reference point clouds, captions/answers, scenario labels, and model metadata.
   - `Outputs`: Metrics, failure slices, confidence intervals, artifact hashes, and a release-gate decision.
   - `Risk controls`: Offline-only operation, no vehicle actuation, dataset-license checks, aggregate reporting, and explicit non-certification label.
   - `Evaluation`: Recompute paper metrics on a small pinned slice, verify determinism, then add object- and coverage-level tests.

2. `World-Query Causal Auditor`
   - `User`: Multimodal interpretability researchers.
   - `Goal`: Test whether text-enriched queries causally affect the correct future geometry.
   - `Core mechanism`: Mask, swap, patch, or counterfactually edit query and text features while keeping BEV and ego-motion fixed.
   - `Required inputs`: Released checkpoint, instrumented intermediate activations, synthetic prompts, and offline scenes.
   - `Outputs`: Region-level geometry changes, causal effect summaries, and failure examples.
   - `Risk controls`: Authorized research environment, read-only checkpoint use, synthetic text counterfactuals, and no live control integration.
   - `Evaluation`: Positive controls, null interventions, randomized baselines, and repeated seeds.

3. `Coverage-Aware Scenario Curator`
   - `User`: Simulation and dataset teams.
   - `Goal`: Prioritize evaluation scenes where the model is likely to hallucinate or diverge.
   - `Core mechanism`: Embed scene/action coverage, score disagreement or uncertainty, and sample under-covered slices for review.
   - `Required inputs`: Public or licensed simulator trajectories, aggregate model outputs, scenario taxonomy, and slice budgets.
   - `Outputs`: Ranked scenarios, coverage maps, and acquisition recommendations.
   - `Risk controls`: Simulator-only loop, no autonomous scraping, privacy review, and human approval for dataset changes.
   - `Evaluation`: Measure reduction in unseen-slice failure rate under a fixed annotation budget.

## Three Ways to Exercise This Research

1. `Table-level reproduction`: Objective—verify headline arithmetic and metric semantics. Inputs—the paper's reported tables. Method—recompute relative improvements, check directions, and record baseline differences. Output—a signed metric ledger. Success criterion—all values and percentage claims reconcile. Stop condition—any ambiguous metric definition or incomparable baseline is flagged rather than resolved by assumption.
2. `Synthetic query intervention`: Objective—test the world-query transfer hypothesis without training. Inputs—a released checkpoint, a small licensed or synthetic scene set, fixed ego-motion, and counterfactual text prompts. Method—mask or swap query/text states and measure localized future-geometry change. Output—causal effect plots and null-control comparisons. Success criterion—effects are repeatable, spatially meaningful, and stronger than random interventions. Stop condition—instrumentation changes model behavior or produces invalid latent states.
3. `Coverage stress test`: Objective—find failure concentration beyond average Chamfer distance. Inputs—a simulator-only scenario suite with weather, occlusion, rare agents, and turns. Method—compute geometry, object, calibration, and divergence metrics by slice. Output—a public-safe aggregate coverage report. Success criterion—every approved slice has enough samples and explicit uncertainty. Stop condition—dataset rights, privacy, or safety review is incomplete.

## Example MVP Product

- `Product name`: HERMES Evidence Gate.
- `Target user`: Research teams reviewing autonomous-driving world-model checkpoints.
- `Problem`: Aggregate point-cloud and caption metrics do not reveal whether a model is robust, grounded, or safe enough for simulation research.
- `Core workflow`: Import offline aggregate predictions; validate provenance and schemas; compute horizon, object, text-grounding, calibration, and coverage metrics; run approved query ablations; compare against versioned limits; export a signed Markdown/JSON evidence bundle.
- `Data requirements`: Synthetic or properly licensed offline scenes, reference point clouds, scenario labels, captions/answers, and checkpoint/version metadata. No live vehicle data is required for the MVP.
- `Architecture`: Local CLI plus deterministic metric library, optional checkpoint adapter, slice registry, policy file, and static report generator.
- `Success metrics`: Deterministic reruns; 100% scenario-slice inventory coverage; exact reconciliation of paper table arithmetic; zero missing provenance fields; known-failure fixtures correctly rejected.
- `Risk controls`: Offline-only; no actuation API; no claim of safety certification; allowlisted datasets; aggregate outputs; checkpoint and config hashing; human approval for policy changes.
- `Limitations`: Cannot prove real-world safety, cannot replace closed-loop testing, and depends on the quality of scenario labels and reference geometry.
- `MVP boundary`: Evaluation and evidence packaging only; no training, route planning, dataset acquisition, or real-time inference.
- `Deployment model`: Local CLI or isolated batch job.
- `Evaluation plan`: Unit-test metric arithmetic, replay synthetic failures, compare with manual review, then run a small licensed checkpoint slice.
- `Failure modes`: Metric implementation errors, scenario leakage, mislabeled slices, incomparable baselines, and false confidence from sparse rare-event data.
- `Maintenance plan`: Version metric definitions, datasets, thresholds, adapters, and expected-output fixtures; review licenses and checkpoint compatibility each release.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| HERMES official implementation | Official repository | Code, setup, data/weights, usage, and release boundary | https://github.com/LMD0311/HERMES |
| HERMES++ | Author follow-up | Extends the unified driving-world-model direction; separate work outside this review's evidence scope | https://arxiv.org/abs/2604.28196 |
| ViDAR | Generation baseline | Image-based future point-cloud forecasting baseline used in HERMES comparisons | https://arxiv.org/abs/2312.17655 |
| OmniDrive | Understanding baseline/data context | Driving VLM and caption/VQA context used by HERMES | https://arxiv.org/abs/2405.01533 |
| BEVFormer v2 | Representation component | Core BEV architecture used by the tokenizer | https://arxiv.org/abs/2211.10439 |
| InternVL | Language/vision backbone context | Foundation for the HERMES language model | https://arxiv.org/abs/2312.14238 |
| VideoWeave Geometry DEP-E | Related Black Lake artifact | Geometry-aware world generation and spatial consistency | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` |
| VLM Probing DEP-E | Related Black Lake artifact | Fusion, attention, and representation diagnostics | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` |
| Visual world-model hallucination finding | Related Black-Lake-Data artifact | Coverage-aware failure taxonomy for world models | `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2501.14729 | Identity, authors, date, abstract, source URLs | 2026-07-12 | Primary arXiv record |
| R2 | https://arxiv.org/html/2501.14729 | Full method, experiments, tables, supplementary details, limitations | 2026-07-12 | Primary full-text evidence |
| R3 | https://arxiv.org/pdf/2501.14729 | Public equivalent of inspected local PDF | 2026-07-12 | No PDF copied into the DEP |
| R4 | https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HERMES_A_Unified_Self-Driving_World_Model_for_Simultaneous_3D_Scene_ICCV_2025_paper.html | ICCV 2025 publication status and accepted paper | 2026-07-12 | Near-primary publication source |
| R5 | https://github.com/LMD0311/HERMES | Official code, guides, release, and license status | 2026-07-12 | Code not executed |
| R6 | `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` | Related geometry/world-model synthesis | 2026-07-12 | Existing processed artifact |
| R7 | `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Related representation-audit synthesis | 2026-07-12 | Existing processed artifact |
| R8 | `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md` | Related hallucination/coverage synthesis | 2026-07-12 | Item 6 cites arXiv:2606.27326 |
| R9 | https://arxiv.org/abs/2604.28196 | Author follow-up locator | 2026-07-12 | Context only; not evidence for HERMES metrics |

## Appendix

### Replication Checklist

- Pin the exact HERMES commit, checkpoint hashes, environment, CUDA stack, and evaluation configuration.
- Inventory licenses and access terms for nuScenes, NuInteract, OmniDrive-nuScenes, InternVL2, OpenCLIP, BEVFormer v2, checkpoints, and processed data.
- Recreate the 0–3 second Chamfer protocol, including the reported spatial bounds.
- Recreate METEOR, ROUGE, CIDEr, and NuScenes-QA evaluation with pinned tokenization and answer normalization.
- Verify the separated-unification and world-query ablations with repeated seeds.
- Add object-level, risk-weighted, calibration, and scenario-slice metrics.
- Test counterfactual text and query interventions with null controls.
- Report accelerator hours, memory, wall-clock time, and resource-normalized comparisons.

### Selection and Dedup Record

- Candidate enumeration: 75,761 PDFs and 75,761 unique PDF-parent units.
- Selection: Uniform PowerShell `Get-Random`, zero-based index 69,210.
- Dedup context: 363 unique arXiv IDs; 67 candidate units matched an observed ID.
- Selected-paper matches by arXiv ID, DOI marker, normalized title, or slug: 0.
- Same-paper markers in the preceding 24 hours: 0.
- Duplicate rejections: 0.
- Reselections: 0.

### Source Inventory

- Original source files deposited: None.
- Public source URLs: arXiv record/HTML/PDF, ICCV open-access paper, and official repository.
- Local extraction cache: Used for review only; not deposited and no location is published.

## Attribution Block

- Source URL: https://arxiv.org/abs/2501.14729
  - Applies to: metadata, abstract, stable identifier, and paper identity.
  - Notes: Primary public arXiv record.
- Source URL: https://arxiv.org/html/2501.14729
  - Applies to: full method, datasets, experiments, ablations, supplementary material, and limitations.
  - Notes: Primary full-text source.
- Source URL: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HERMES_A_Unified_Self-Driving_World_Model_for_Simultaneous_3D_Scene_ICCV_2025_paper.html
  - Applies to: ICCV 2025 publication context and accepted-paper cross-check.
  - Notes: Computer Vision Foundation open-access source.
- Source URL: https://github.com/LMD0311/HERMES
  - Applies to: official code, setup, release, and license status.
  - Notes: Repository inspected; code and checkpoints not executed.
- Repository source: `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`
  - Applies to: related geometry-aware generation synthesis.
  - Notes: Existing Black Lake artifact.
- Repository source: `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
  - Applies to: related representation-audit synthesis.
  - Notes: Existing Black Lake artifact.
- Repository source: `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md`
  - Applies to: related visual-world-model hallucination and coverage synthesis.
  - Notes: Existing Black-Lake-Data artifact, item 6.
