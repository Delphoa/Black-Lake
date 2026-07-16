---
title: "DMNN Conditional Paths - DEP-E"
generated_at: "2026-07-16"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of dynamic multi-path conditional computation for vision networks."
source_status: "verified complete v3 PDF and approved ar5iv full-paper HTML inspected; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv:1902.10949v3 and focused public code-availability search inspected through 2026-07-16"
primary_url: "https://arxiv.org/abs/1902.10949v3"
stable_identifier: "arXiv:1902.10949v3; DOI 10.48550/arXiv.1902.10949"
confidence_summary: "High for method and table transcription; medium for comparative interpretation; low for realized deployment efficiency."
safety_scope: "research analysis only; no production-performance authorization"
distribution_notes: "Paper files, metadata HTML, caches, and extracted text were not redistributed."
---

# DMNN Conditional Paths - DEP-E

## Source Metadata

| ID | Source | Role | Identifier / Version | Public Locator | Status |
|---|---|---|---|---|---|
| S1 | Dynamic Multi-path Neural Network | Primary metadata/full PDF | arXiv:1902.10949v3 | https://arxiv.org/abs/1902.10949v3 | Full PDF inspected |
| S2 | ar5iv rendering | Primary full-paper HTML fallback | 1902.10949 | https://ar5iv.labs.arxiv.org/html/1902.10949 | Verified full text inspected |
| S3 | arXiv DOI | Stable identifier | 10.48550/arXiv.1902.10949 | https://doi.org/10.48550/arXiv.1902.10949 | Resolved |
| S4 | AFIDAF Vision Filters | Related DEP | DEP-E-20260715 | `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` | Inspected |
| S5 | HSD FTI-FDet | Related DEP | DEP-E-20260712 | `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Inspected |
| S6 | SMES Expert Sparsity | Related DEP | DEP-E-20260713 | `.lake-data/DEP-E/DEP-E-20260713-SMES Expert Sparsity/smes_expert_sparsity_manuscript.md` | Inspected |
| S7 | Black Lake README | Repository authority | live default branch | https://github.com/Delphoa/Black-Lake | Inspected before writing |

Authors: Yingcheng Su, Shunfeng Zhou, Yichao Wu, Tian Su, Ding Liang, Jiaheng Liu, Dixin Zheng, Yingxu Wang, Junjie Yan, and Xiaolin Hu. Submitted 2019-02-28 and revised 2019-04-07. The arXiv record uses the arXiv non-exclusive distribution license. No official code repository was identified in the inspected record, paper, or focused GitHub search.

## Evidence Ledger

| ID | Source basis | Evidence class | Supports | Confidence | Limitation |
|---|---|---|---|---|---|
| E1 | S1/S2, architecture and controller sections | Primary method | sub-block paths, gates, previous-state/category controller | High | no code audit |
| E2 | S1/S2, loss section | Primary method | classification, category supervision, resource target | High | implementation details incomplete |
| E3 | S1/S2, ImageNet Table 1 | Primary empirical | ResNet/MobileNet accuracy-FLOP points | High for transcription | author implementations; no uncertainty |
| E4 | S1/S2, CIFAR-100 table | Primary empirical | four-path error/FLOP result | High for transcription | one dataset/setup |
| E5 | S1/S2, controller ablation | Primary empirical | previous state and category information | High for transcription | isolated configuration |
| E6 | S1/S2, discussion | Primary resource claim | controller overhead and dynamic behavior | Medium-high | FLOP estimate, no device telemetry |
| E7 | Focused public search | Availability | no official implementation identified | Medium | search may miss unlinked code |
| E8 | S4-S6 | Related processed research | efficiency/runtime/deployment synthesis | Medium | adjacent models/domains |
| E9 | Selection, verification, cache, and dedup records | Process evidence | eligibility and source integrity | High | public summary omits local identifiers |

## Executive Summary

Dynamic Multi-path Neural Network (DMNN) makes residual and MobileNet blocks conditionally executable at sub-block granularity. A controller uses the current feature, previous controller state, and supervised category information during training to choose paths. A resource-constrained objective encourages a target execution rate, so different inputs can receive different effective width and depth.

The paper reports attractive FLOP-accuracy points. Its two-path DMNN-50 at target rate 0.5 gives 23.50% ImageNet top-1 error at 2.28G FLOPs, nearly equal to the authors' ResNet-50 at 23.51% and 3.96G. A comparable DMNN-101 point reports 21.95% at 4.21G versus 22.02% at 7.67G. The evidence supports conditional capacity as an architectural hypothesis, not an end-to-end speed proof: device latency, memory, energy, compiler behavior, repeated seeds, and routing stability are absent.

## Detailed Summary

### Problem and Motivation

Static convolutional networks spend the same nominal computation on easy and difficult inputs. Earlier dynamic networks often skip whole blocks, adjusting depth but retaining a coarse decision boundary. DMNN seeks finer control by partitioning each block into `N` sub-block paths. Activating different subsets varies effective width as well as depth and creates multiple computational routes.

### Architecture

Each transformed residual/MobileNet block contains candidate sub-block paths and a gate vector. The current controller receives a feature-derived representation and a previous-controller state, so decisions can depend on both current content and earlier routing context. Category-supervised components teach semantically informed decisions during training and are removed at inference.

### Objective

Training combines the task classification loss, category/controller supervision, and a resource term that penalizes deviation from a target execution rate. The rate is a soft control over average active computation, not a guarantee of latency on a particular runtime.

### Results

On ImageNet, the authors' ResNet-50 reports 23.51% top-1 error, 25.56M parameters, and 3.96G FLOPs. DMNN-50 with two paths and target 0.5 reports 23.50%, 24.67M, and 2.28G (57.6% of reference FLOPs). A four-path target-0.7 version reports 22.32%, 25.81M, and 3.17G. The authors' ResNet-101 reports 22.02% at 7.67G; two-path DMNN-101 at target 0.5 reports 21.95% at 4.21G (54.9%).

For MobileNetV2, the paper reports 28.09% error at 0.30G for its baseline and 27.74% at 0.27G for a two-path target-0.9 DMNN. On CIFAR-100, ResNet-50 reports 27.55% error at 0.33G; four-path DMNN-50 at target 0.7 reports 26.15% at 0.26G.

The controller ablation at a two-path target-0.7 setting reports 23.25% error for a DMNN baseline, 23.09% with previous state, 23.20% with category information, and 22.57% with both; the corresponding static ResNet is 23.51%. This supports the combined controller within that setup but does not isolate training-budget or regularization effects across seeds.

## Key Claims and Evidence

| Claim | Type | Evidence | Assessment | Confidence |
|---|---|---|---|---|
| Sub-block gates vary effective width and depth per input. | Method | E1 | Directly described; implementation unavailable. | High |
| Category and previous-controller information improve routing. | Empirical | E5 | Combined ablation is best in one setting. | Medium-high |
| DMNN-50 matches the authors' ResNet-50 error at 57.6% FLOPs. | Empirical | E3 | Numerically supported; no latency inference. | High for report |
| DMNN-101 matches the authors' ResNet-101 error at 54.9% FLOPs. | Empirical | E3 | Numerically supported within author baselines. | High for report |
| DMNN improves computation efficiency in deployment. | Implication | E3/E6 | Plausible, but device/runtime evidence is missing. | Low-medium |
| Controller overhead is negligible. | Resource claim | E6 | About 0.02% ResNet-50 FLOPs reported; other overhead omitted. | Medium |
| First random draw was eligible. | Process | E9 | ID/title/slug/DOI and 24-hour scans were clear. | High |

## Methodology

- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, treated unique PDF parent directories as paper units, chose a uniform zero-based index using PowerShell `Get-Random`, and inspected adjacent metadata.
- `Source integrity`: Classified the selected unit before review. Its valid PDF lacked full-paper HTML, so the workflow attempted official arXiv HTML, received an unavailable response, used the approved ar5iv fallback, and validated byte size, body text, document markers, headings, and paper-structure terms.
- `Cache methodology`: Ran `document_source_processing.py extract-arxiv` in `missing-only` mode against the paper unit with the central archive cache. The miss became `cached`; PDF and HTML text were extracted with `pypdf` and `html-regex`. No source package was collected.
- `Deduplication`: Searched Black Lake logs, reports, DEP-E paths, staging index, automation memory, and relevant Black-Lake-Data entries for exact/base arXiv ID, DOI, normalized title, and slug, including same-paper markers within 24 hours. No match occurred; no reselection was needed.
- `Review`: Inspected full method, objectives, principal ImageNet/CIFAR tables, controller ablation, limitations, public metadata, and a focused code-availability search. No result was reproduced.
- `Related synthesis`: Selected exactly three inspected Black Lake deposits for concrete overlap in efficiency proxies, compact-vision deployment metrics, and sparse routing/runtime behavior.
- `Distribution`: Public artifacts contain original review prose and derived status data only. PDF, HTML, metadata, cache, and extracted text remain local.

## Scope, Constraints, and Assumptions

- Reported numbers are author results, not reproduced findings.
- FLOPs approximate arithmetic and do not establish latency, energy, peak memory, throughput, or cost.
- Accuracy comparisons use the paper's training recipes and some author reimplementations; equal-budget fairness is not fully established.
- Category-supervised routing assumes a training hierarchy. Generalization without that hierarchy is unknown.
- No official implementation was found, limiting architecture, controller, and runtime verification.
- Public source citations are supplied, but original source documents are deliberately not redistributed.

## Observations

- The most compelling DMNN points preserve or improve reported accuracy while reducing estimated FLOPs by roughly 42-45% relative to author baselines.
- Higher target execution rates can improve accuracy beyond the static baseline, so the gate acts as adaptive capacity rather than pruning alone.
- Controller ablation suggests routing context and category supervision are complementary.
- The paper's parameter narrative is less clean than its compute narrative: several DMNN configurations have similar parameter counts to their same-depth baselines.
- Dynamic per-example routing may conflict with uniform accelerator batches even when average active FLOPs decline.

## Considerations

An implementation should measure the entire execution path: gate inference, mask materialization, branch scheduling, kernel launches, memory reads, synchronization, fallback behavior, and batch fragmentation. Results should be stratified by device, compiler, precision, batch/concurrency, input difficulty, route signature, and percentile latency.

Scientific evaluation should add repeated seeds, confidence intervals, corruption and distribution-shift suites, calibration, per-class performance, route entropy, route agreement, and hierarchy-free transfer. Frequent route signatures could be compiled into static subgraphs, but rare or unstable signatures need a bounded fallback.

## Strengths

- Fine-grained conditional paths generalize whole-block skipping to adaptive width and depth.
- The objective exposes an explicit resource-rate control rather than relying only on post-hoc pruning.
- ImageNet and CIFAR results cover ResNet and MobileNetV2 families.
- Controller ablation directly tests two central information sources.
- Category-specific training components are removed for inference, limiting nominal controller overhead.

## Weaknesses

- No measured device latency, energy, peak memory, throughput, tail behavior, or compiler analysis.
- No official code, checkpoints, route traces, or pinned reproduction environment were identified.
- No repeated seeds, confidence intervals, or statistical tests.
- Some comparisons depend on author reimplementations and potentially unequal training effects.
- Training-time category hierarchy may constrain transfer to unseen taxonomies and unlabeled domains.
- Larger path counts and runtime consequences are not systematically explored.

## Potential Improvements

1. Publish complete code, checkpoints, configs, hierarchy maps, seeds, route traces, and exact baseline recipes.
2. Report matched-hardware latency, memory, energy, throughput, compilation time, and percentile results across batch sizes.
3. Optimize a compiler-aware cost model rather than FLOPs alone and compare it with rate-only training.
4. Test route stability and accuracy under corruption, shift, unseen classes, hierarchy removal, and new datasets.
5. Compare against static width/depth scaling, pruning, early exit, mixture-of-experts, and compiled route-specialization baselines under equal training budgets.

## Potential Implementations

| Implementation | Purpose | Required evidence | Main risk | Acceptance signal |
|---|---|---|---|---|
| Route telemetry profiler | Measure whether sparsity survives the runtime | masks, kernels, latency, memory, power | instrumentation overhead | lower p95 cost at matched accuracy |
| Route-specialized compiler | Turn common dynamic paths into static graphs | route frequency and stability | signature explosion | bounded compile set plus safe fallback |
| Budget controller service | Select resource target per device/SLO | calibrated Pareto curves | control instability | SLO compliance under load |

## Three Ways to Exercise This Research

### 1. Reconstruct the Reported Frontier

- Implement the stated two-path ResNet-50 controller and author baseline under a shared recipe.
- Verify top-1 error, active-path rate, parameters, and FLOPs across targets.
- Use at least three seeds and report confidence intervals.
- Reject the claim if static width/depth controls match the frontier under equal budgets.

### 2. Test Runtime Realization

- Compile dense and dynamic models for GPU, CPU, and mobile/NPU targets.
- Measure warm/cold p50/p95/p99 latency, throughput, peak memory, and energy across batch sizes.
- Record route signatures, kernel count, occupancy, and branch fragmentation.
- Accept efficiency only where end-to-end metrics improve at matched quality.

### 3. Stress Routing Semantics

- Evaluate corruption, class shift, unseen taxonomies, resolution shift, and hierarchy-free training.
- Measure route agreement across seeds/augmentations and per-class route entropy.
- Inspect whether difficult inputs receive more useful compute rather than merely different compute.
- Add a dense fallback for unstable or out-of-distribution routes.

## Example MVP Product

### Conditional Inference Auditor

- `Purpose`: Determine whether a dynamic network's claimed active compute becomes real target-device efficiency.
- `Inputs`: model/checkpoint, controller configuration, target runtime/device, evaluation data, quality and SLO thresholds.
- `Core mechanism`: capture per-example paths; cluster route signatures; correlate them with correctness and system telemetry; compare dense, dynamic, and compiled-static variants.
- `Outputs`: accuracy-resource Pareto plot, route heatmap, route-stability report, p50/p95/p99 latency, peak memory, energy, and unsupported-route fallback log.
- `Evaluation`: matched-accuracy cost, SLO violations, route entropy/agreement, compilation coverage, and corruption/shift robustness.
- `Safety boundary`: advisory benchmarking only; deployment requires target-owner review, monitoring, and rollback.

## Related Research and Reading

1. [AFIDAF Vision Filters](../../DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md) - demonstrates why parameter and FLOP efficiency need hardware evidence.
2. [HSD FTI-FDet](../../DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md) - supplies latency, memory, size, and deployment-failure dimensions for compact vision.
3. [SMES Expert Sparsity](../../DEP-E-20260713-SMES%20Expert%20Sparsity/smes_expert_sparsity_manuscript.md) - connects routed sparsity with load balance, grouped execution, temporary memory, and production latency.

## Source References

1. Su, Y., Zhou, S., Wu, Y., et al. *Dynamic Multi-path Neural Network*. arXiv:1902.10949v3. https://arxiv.org/abs/1902.10949v3
2. Full-paper PDF. https://arxiv.org/pdf/1902.10949
3. Approved full-paper HTML fallback. https://ar5iv.labs.arxiv.org/html/1902.10949
4. arXiv DOI. https://doi.org/10.48550/arXiv.1902.10949
5. AFIDAF Vision Filters DEP-E. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md`
6. HSD FTI-FDet DEP-E. `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`
7. SMES Expert Sparsity DEP-E. `.lake-data/DEP-E/DEP-E-20260713-SMES Expert Sparsity/smes_expert_sparsity_manuscript.md`

## Appendix

### Selected Quantitative Record

| Model | Top-1 error (%) | Parameters | FLOPs | Reviewer note |
|---|---:|---:|---:|---|
| ResNet-50 (authors) | 23.51 | 25.56M | 3.96G | reference |
| DMNN-50, N=2, target=.5 | 23.50 | 24.67M | 2.28G | 57.6% FLOP ratio |
| DMNN-50, N=4, target=.7 | 22.32 | 25.81M | 3.17G | higher quality/compute |
| ResNet-101 (authors) | 22.02 | 44.55M | 7.67G | reference |
| DMNN-101, N=2, target=.5 | 21.95 | 43.12M | 4.21G | 54.9% FLOP ratio |
| MobileNetV2 (authors) | 28.09 | 3.50M | 0.30G | reference |
| DMNN MobileNetV2, N=2, target=.9 | 27.74 | 3.63M | 0.27G | modest reduction |

### Provenance and Distribution

- Random draw: uniform zero-based index 61,074 among 75,776 unique paper units; first draw accepted.
- Source gate: valid PDF plus verified full-paper HTML after approved fallback; metadata HTML never counted as paper content.
- Cache: missing-only extraction changed miss to cached in 0.864 seconds; source package absent.
- Dedup: exact ID, DOI, normalized title, slug, artifact, memory, companion-repository, and 24-hour scans clear.
- Distribution: no PDF, HTML, metadata, source archive, cache, extracted text, or local archive reference is included in the repository.
