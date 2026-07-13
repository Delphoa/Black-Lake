# Report-Mark: KDFlow LLM Distill

## Source Metadata

| Field | Value |
|---|---|
| Paper title | KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models |
| Authors | Songming Zhang; Xue Zhang; Tong Zhang; Bojie Hu; Yufeng Chen; Jinan Xu |
| arXiv ID | 2603.01875v2 |
| DOI | 10.48550/arXiv.2603.01875 |
| Subjects | Computation and Language; Artificial Intelligence; Machine Learning |
| arXiv history | v1 submitted 2026-03-02; v2 revised 2026-03-24 |
| Primary URLs | https://arxiv.org/abs/2603.01875 ; https://arxiv.org/html/2603.01875 ; https://arxiv.org/pdf/2603.01875 ; https://github.com/songmzhang/KDFlow |
| Extraction status | `pypdf` extracted PDF text; local HTML and source-package text were absent |
| Source files deposited | None; no `.source/` folder was created |
| License notes | arXiv exposes its paper-license link; the official KDFlow repository displays an MIT license |

## Concise Research Notes

KDFlow targets a structural mismatch in large-language-model knowledge distillation. The teacher performs only inference, while the student needs forward, backward, optimizer, and checkpoint work. Common frameworks nevertheless run both through a homogeneous training engine. KDFlow assigns teacher inference to SGLang, student optimization to FSDP2, and coordination to Ray.

The process graph contains one trainer and three functional actor groups. Teacher actors return final hidden states. Student actors receive those states through shared memory and apply the teacher language-model head locally to reconstruct the full teacher distribution. This avoids sending a vocabulary-sized tensor across processes. The paper estimates that BF16 logits for 128 sequences of length 4,096 with a 151,936-token vocabulary would occupy about 160 GB, while a 4,096-wide hidden state is much smaller.

Off-policy training consumes static prompt-response pairs. On-policy training first generates responses with a student rollout group, obtains teacher hidden states, updates the student, and synchronizes weights back to rollout actors. The paper exposes Forward KL, Reverse KL, Jensen-Shannon divergence, Total Variation Distance, and DSKDv2-based cross-tokenizer support behind extension APIs.

Experiments sample 100,000 LMSys-Chat-1M prompts and generate responses with Qwen3-14B. Teachers are Qwen3-14B, Qwen3-32B, and Qwen3-30B-A3B; students are Qwen3-4B and Qwen3-1.7B. All efficiency measurements use one server with eight NVIDIA H20 GPUs, global batch size 128, gradient accumulation 8, and maximum sequence length 4,096.

Against the fastest listed baseline, MS-SWIFT, KDFlow with an FP8 teacher reports 1.44x-6.36x speedup across six configurations. The largest result is Qwen3-30B-A3B to Qwen3-1.7B: 5.8 seconds per iteration for KDFlow versus 36.9 for MS-SWIFT. On AlpacaEval 2.0, the KDFlow-distilled Qwen3-1.7B reports 28.23% length-controlled win rate and 28.32% raw win rate, close to FSDP and MS-SWIFT distilled baselines and above the undistilled student. These results were not reproduced.

The paper discloses that FSDP2 remains behind Megatron-LM for 3D-parallel training and that KDFlow lacks asynchronous optimization for thousand-GPU clusters. Additional review limits include a single hardware environment, one model family, no repeated seeds or uncertainty, no energy/cost reporting, no component-level speedup ablation, and no public manifest that pins each table row to exact framework versions and commits.

The current official repository is active and MIT-licensed but has evolved beyond paper v2. Its README announces v0.2.0, multi-teacher routing, chunked loss, EMA teacher updates, dynamic batching, multimodal workflows, and a warning about an older SGLang VLM compatibility bug. These are current implementation observations, not evidence for the paper's evaluated system.

## Evidence and Attribution

| ID | Evidence | Source Basis | Use | Confidence |
|---|---|---|---|---|
| E1 | arXiv metadata provides title, authors, ID, DOI, v1/v2 dates, subjects, page/figure/table count, and code locator. | arXiv abstract page | Bibliographic identity | High |
| E2 | Ray coordinates a trainer plus rollout, teacher, and student actor groups; SGLang serves the teacher and FSDP2 trains the student. | Paper sections 1 and 3; Figures 1-2 | Core architecture | High for reporting |
| E3 | Teacher hidden states move through shared memory and the student side recomputes full teacher logits with the teacher head. | Paper section 3.2; Figure 3 | Communication mechanism | High for description; medium for untested equivalence |
| E4 | The paper supports off-policy, on-policy, multiple divergences, and DSKDv2 cross-tokenizer distillation. | Paper sections 3.3-3.4 | Capability scope | High for source claim; medium without execution |
| E5 | Table 2 reports 28.23% LC win rate and 28.32% win rate for KDFlow on AlpacaEval 2.0. | Paper section 4.3 and Table 2 | Downstream quality evidence | High for transcription; low for reproduction |
| E6 | Table 3 reports 1.44x-6.36x speedup across six Qwen3 configurations on eight H20 GPUs. | Paper sections 4.1 and 4.4; Table 3 | Efficiency evidence | High for transcription; low for reproduction |
| E7 | FSDP2/Megatron-LM and missing asynchronous large-cluster optimization are explicit limits. | Paper Limitations section | Boundary conditions | High |
| E8 | Official current main exposes MIT licensing, v0.2.0 features, examples, Docker guidance, and a SGLang VLM compatibility warning. | Official GitHub README | Implementation evolution | Medium-high; current main not executed |
| E9 | Three related DEP entries provide compact-student quality, output-space robustness, and topology-aware systems-partitioning context. | Inspected Black Lake and Black-Lake-Data artifacts plus cited arXiv basis | Synthesis bridge | Medium; contextual only |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`
   - Relevance: Both artifacts use teacher/student transfer to make deployment more practical and must balance accuracy, model size, memory, and latency. HSD FTI-FDet supplies a compact-vision counterpoint in which the best resource trade-off is not always the single most accurate ablation, cautioning against throughput-only optimization.
   - Source basis: The related manuscript's source metadata, architecture, Tables 1-5 synthesis, limitations, evidence ledger, and quality/resource observations were inspected.

2. `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`
   - Relevance: BA-LoRA uses KL consistency and token-level temperature distillation in output space, directly connecting to KDFlow's full-logit reconstruction and divergence APIs. Its focus on drift, representation collapse, noisy overfit, minority performance, and LoRA adaptation supplies the robustness gate that KDFlow's systems benchmark does not provide.
   - Source basis: The related manuscript's method, logit-level regularizers, reported robustness results, limitations, code boundary, and output-space interpretation were inspected.

3. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260629-Tech Intel 1104/daily_research_findings_2026-06-29_1104.md`
   - Relevance: Finding 5 is the closest systems neighbor. It also rejects symmetric teacher/student handling and uses topology-aware vertical/horizontal partitioning, reporting up to 67% more samples per second than TRL. KDFlow specializes backends and transfer representation; the related work specializes placement and split strategy.
   - Source basis: The DEP finding and its attribution were inspected, and its cited primary arXiv abstract for “Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems” (arXiv:2606.27797v1) was cross-checked.

## Synthesis Note

### Concept Bridge

KDFlow shifts knowledge distillation from a single-backend training recipe to a three-layer systems problem. The execution layer must exploit teacher/student asymmetry, as both KDFlow and the HPC partitioning entry argue. The transfer layer must preserve useful behavior while compressing the deployed model, as HSD FTI-FDet demonstrates through accuracy, latency, memory, and model-size trade-offs. The assurance layer must detect knowledge drift, collapse, bias, and noisy overfit, as BA-LoRA frames through output-space regularization. A credible distillation platform therefore needs placement evidence, transfer-quality evidence, and robustness evidence in the same release record.

### Potential Implementations

1. `KD Systems Reproduction Harness`: Pin paper-era KDFlow and baseline commits, reconstruct all six Table 3 configurations, capture repeated timing/utilization/communication/energy traces, and connect each result to a manifest.
2. `Teacher-Student Placement Advisor`: Combine backend specialization with topology-aware vertical/horizontal split estimates to propose bounded pilot configurations for a given cluster and model pair.
3. `Distilled Student Release Gate`: Compare teacher, base student, and distilled student on task quality, calibration, drift, minority performance, safety behavior, latency, memory, and cost before promotion.

### Deeper Relationship Observations

1. KDFlow and the HPC partitioning work independently identify the same root cause - teacher and student are asymmetric workloads - but optimize different axes: backend/representation versus topology/placement.
2. HSD FTI-FDet shows that the smallest or fastest distilled artifact may sacrifice a peak accuracy ablation, so KDFlow's framework benchmark should expose a Pareto frontier rather than one throughput winner.
3. BA-LoRA's output-space constraints imply that full-logit availability is not only a fidelity concern; it is an interface for drift, diversity, bias, and robustness objectives that top-k transfer may obscure.

### Conceptual Similarities

1. All three related entries make hidden implementation structure explicit: teacher/student placement, heterogeneous transfer paths, and output-space regularization each change what evidence must be collected.
2. Each entry distinguishes deployability from raw model quality by adding resource, topology, latency, memory, or robustness constraints.
3. Each entry requires controlled comparisons because aggregate gains can be confounded by hardware, tuning budget, tokenizer, precision, dataset composition, or framework defaults.

### MVP Implementations with Code Mock-ups

1. `Speedup Ledger`

```python
def speedup_rows(baseline, candidate):
    return [
        {"case": k, "baseline_s": baseline[k], "candidate_s": candidate[k],
         "speedup": round(baseline[k] / candidate[k], 2)}
        for k in sorted(set(baseline) & set(candidate))
    ]
```

2. `Manifest Completeness Gate`

```python
REQUIRED = {"teacher", "student", "commit", "container", "data", "seed",
            "precision", "batch", "max_length", "hardware", "quality_suite"}

def manifest_gate(record):
    missing = sorted(REQUIRED - set(record))
    return {"pass": not missing, "missing": missing}
```

3. `Student Delta Gate`

```python
def release_gate(base, distilled, limits):
    deltas = {k: distilled[k] - base[k] for k in limits}
    failed = {k: v for k, v in deltas.items() if v < limits[k]}
    return {"pass": not failed, "deltas": deltas, "failed": failed}
```

### Developer Challenges

1. Reproduction requires paper-era commits, containers, model/tokenizer revisions, generated-response provenance, exact baseline settings, and access to eight matched H20 GPUs.
2. Hidden-state transfer must preserve head/tokenizer/precision compatibility while controlling teacher-head memory, shared-memory lifetime, backpressure, and process-failure cleanup.
3. Current multi-teacher, multimodal, on-policy, and chunked-loss features expand the state graph and require dedicated correctness, staleness, routing, and regression tests.

### Author Challenges

1. Publish a versioned benchmark manifest mapping every table row and loss curve to exact code commits, containers, datasets, model revisions, seeds, and commands.
2. Add factorial ablations and telemetry that isolate SGLang, hidden-state transfer, FP8, Ray scheduling, placement, and baseline configuration effects.
3. Expand quality evidence beyond one AlpacaEval setup with repeated seeds, uncertainty, multilingual/reasoning/coding/safety tests, and current-feature evaluations.

## Validation Notes

- Required output paths are repository-relative and public-safe.
- No private absolute paths, home directories, usernames, machine names, workspace roots, local timezone labels, or exact local execution timestamps are present.
- Random selection used uniform zero-based index 1,455 over 75,761 paper units; zero exclusions and zero reselections occurred.
- Dedup scans covered Black Lake `.logs`, `.reports`, `.lake-data`, the public pointer index, automation memory, and Black-Lake-Data; no same-paper or 24-hour marker was found.
- Related DEP synthesis contains exactly three inspected repository entries.
- Synthesis Note contains exactly three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP implementations with code mock-ups, three developer challenges, and three author challenges.
- Paper-v2 claims are separated from current official-repository features; no experiment, training run, or benchmark reproduction is implied.
- No source files were collected into the DEP.

## Attribution Block

- Source URL: https://arxiv.org/abs/2603.01875
  - Applies to: paper identity, authors, DOI, v1/v2 dates, subjects, abstract, and code locator.
  - Notes: Primary arXiv metadata page inspected.
- Source URL: https://arxiv.org/html/2603.01875
  - Applies to: architecture, workflows, communication mechanism, experiments, results, and limitations.
  - Notes: Public arXiv full text inspected and cross-checked with private PDF extraction.
- Source URL: https://arxiv.org/pdf/2603.01875
  - Applies to: canonical paper reference, figures, tables, and limitations.
  - Notes: Private archived PDF inspected; no PDF file redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2603.01875
  - Applies to: persistent arXiv identifier.
  - Notes: DataCite DOI for the arXiv record.
- Source URL: https://github.com/songmzhang/KDFlow
  - Applies to: official implementation, MIT license, current examples/features, installation, and compatibility notes.
  - Notes: Repository README inspected; code, containers, models, and data were not executed or redistributed.
- Repository path: `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`
  - Applies to: compact-student quality, latency, memory, model-size, and deployment synthesis.
  - Notes: Existing Black Lake DEP manuscript inspected.
- Repository path: `.lake-data/DEP-E/DEP-E-20260709-BA-LoRA Bias/ba-lora-bias-manuscript.md`
  - Applies to: output-space distillation, robustness, drift, bias, and LoRA synthesis.
  - Notes: Existing Black Lake DEP manuscript inspected.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260629-Tech%20Intel%201104/daily_research_findings_2026-06-29_1104.md
  - Applies to: topology-aware teacher/student partitioning synthesis.
  - Notes: Existing Black-Lake-Data DEP finding inspected; primary basis https://arxiv.org/abs/2606.27797.
