# Report-Mark: DMNN Conditional Paths

## Review Status

- Paper: arXiv:1902.10949v3, *Dynamic Multi-path Neural Network*
- Source: verified complete PDF plus approved ar5iv full-paper HTML
- Review: architecture, controller, objective, ImageNet/CIFAR evidence, ablations, and limitations
- Reproduction: none; source files and extracted text withheld

## Source Metadata

| Field | Value |
|---|---|
| Title | Dynamic Multi-path Neural Network |
| Authors | Yingcheng Su; Shunfeng Zhou; Yichao Wu; Tian Su; Ding Liang; Jiaheng Liu; Dixin Zheng; Yingxu Wang; Junjie Yan; Xiaolin Hu |
| ID / DOI | arXiv:1902.10949v3 / 10.48550/arXiv.1902.10949 |
| Dates | Submitted 2019-02-28; revised 2019-04-07 |
| Availability | arXiv non-exclusive license; no official code identified |

## Concise Research Notes

DMNN replaces each residual or MobileNet block with several gated sub-block paths. A lightweight controller uses the current feature representation, prior controller state, and category supervision during training to select paths, while an execution-rate objective targets a FLOP budget. Category-specific components are removed for inference; reported controller overhead is about 0.02% of ResNet-50 FLOPs.

On ImageNet, DMNN-50 with two paths at target rate 0.5 reports 23.50% top-1 error at 2.28G FLOPs, versus the authors' ResNet-50 at 23.51% and 3.96G. DMNN-101 at the same target reports 21.95% at 4.21G versus ResNet-101 at 22.02% and 7.67G. A higher-compute DMNN-50 variant reports 22.32% at 3.17G. On CIFAR-100, a four-path model reports 26.15% error at 0.26G versus ResNet-50 at 27.55% and 0.33G.

The evidence supports a useful conditional-capacity mechanism but not a deployment-speed conclusion. FLOPs omit branching, launch, occupancy, batching, memory, and controller costs. Results lack repeated seeds and independent reproduction, and class-hierarchy supervision raises a transfer question.

## Evidence and Attribution

| ID | Evidence | Boundary |
|---|---|---|
| R1 | Full paper method and equations | mechanism reconstructed; no implementation audit |
| R2 | ImageNet/CIFAR tables | author-reported; FLOPs are not measured latency |
| R3 | Controller ablation | supports prior-state/category components in one setting |
| R4 | Resource/overhead discussion | model-level estimate; no hardware telemetry |
| R5 | Focused GitHub/arXiv availability search | no official code found; absence is not proof none exists |
| R6 | Three related DEP manuscripts | conceptual context only |
| R7 | Selection, repair, cache, and dedup records | operational evidence |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - parameter/FLOP efficiency versus missing device evidence.
2. `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` - compact vision with explicit latency, memory, model-size, and field-failure measures.
3. `.lake-data/DEP-E/DEP-E-20260713-SMES Expert Sparsity/smes_expert_sparsity_manuscript.md` - routing sparsity, active compute, load balance, grouped execution, and temporary-memory concerns.

## Synthesis Note

### Concept Bridge

DMNN provides the architectural idea of input-conditional paths. AFIDAF shows why parameters and FLOPs must be separated from realized efficiency; HSD FTI-FDet supplies a practical multi-metric edge-vision measurement frame; SMES shows that routed sparsity becomes useful only when runtime scheduling, load, memory, and kernels preserve it. Together they define a compiler-aware conditional-inference benchmark rather than a FLOP-only leaderboard.

### Potential Implementations

1. **Conditional-path profiler** - capture path masks, per-layer utilization, p50/p95/p99 latency, peak memory, energy, and accuracy under matched budgets.
2. **Routing-stability dashboard** - compare route entropy and agreement across seeds, corruptions, classes, resolutions, and batch sizes.
3. **Static-specialization compiler** - cluster frequent route signatures and compile bounded static subgraphs with a dense fallback.

### Deeper Relationship Observations

1. DMNN and SMES share an active-subgraph objective, but vision-path gates and recommendation experts stress different utilization and load-balance failure modes.
2. AFIDAF's nearly unchanged FLOPs despite lower parameters mirrors DMNN's warning in reverse: a single resource proxy cannot establish system efficiency.
3. HSD FTI-FDet's device metrics reveal the evidence DMNN needs most, while its desktop-GPU limitation shows that even measured latency does not transfer automatically.

### Conceptual Similarities

1. All four artifacts separate nominal capacity from the portion activated for an input or deployment.
2. All require multi-objective evaluation across quality, compute, memory, and system behavior.
3. All expose a gap between architecture-level efficiency and target-hardware performance.

### MVP Implementations with Code Mock-ups

1. **Route utilization ledger**

```python
def route_rate(mask: list[int]) -> float:
    return sum(mask) / max(1, len(mask))
```

2. **Latency-aware acceptance**

```python
def accept(error: float, p95_ms: float, budget: tuple[float, float]) -> bool:
    return error <= budget[0] and p95_ms <= budget[1]
```

3. **Stable-route test**

```python
def agreement(a: list[int], b: list[int]) -> float:
    return sum(x == y for x, y in zip(a, b)) / max(1, len(a))
```

### Developer Challenges

1. Efficiently executing per-example dynamic graphs without fragmenting batches or losing accelerator occupancy.
2. Capturing route, latency, memory, and energy telemetry with reproducible compiler and hardware metadata.
3. Building static fallbacks and safety bounds for unstable or unsupported route patterns.

### Author Challenges

1. Release code, checkpoints, exact training recipes, hierarchy mappings, seeds, and route traces.
2. Report matched-device latency, memory, energy, batch/concurrency sensitivity, uncertainty, and corruption/shift results.
3. Test hierarchy-free training, unseen taxonomies, compiler-aware objectives, and comparisons under equal training budgets.

## Validation Notes

- Uniform first draw: index 61,074/75,776; no exclusions, reselections, or duplicate markers.
- PDF 2,535,345 bytes with valid header/EOF; ar5iv HTML 404,027 bytes with 47,624 body chars, 27 headings, and five structure terms; final source state complete.
- Cache miss to cached in 0.864 seconds; 40,803/47,308 PDF/HTML text bytes; no source package.
- No model/code execution. Focused code search found bibliographic indexes but no official implementation.
- Schema, exact-count, public-safety, and seven-file no-source allowlist are validated before submission.

## Attribution Block

- Paper: https://arxiv.org/abs/1902.10949v3
- HTML/PDF: https://ar5iv.labs.arxiv.org/html/1902.10949 ; https://arxiv.org/pdf/1902.10949
- DOI: https://doi.org/10.48550/arXiv.1902.10949
- Nature: independent review; no result reproduced; no source, cache, or extracted-text file uploaded.
