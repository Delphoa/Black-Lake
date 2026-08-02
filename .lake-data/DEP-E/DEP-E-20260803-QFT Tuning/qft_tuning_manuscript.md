---
title: "QFT Tuning - DEP-E"
generated_at: "2026-08-03"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of QFT, a quantized full-parameter tuning framework for LLMs."
source_status: "mixed private verified source bundle plus public URLs; source files withheld locally"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-03"
temporal_cutoff: "2026-08-03"
primary_url: "https://arxiv.org/abs/2310.07147"
stable_identifier: "arXiv:2310.07147v3; DOI: 10.48550/arXiv.2310.07147"
confidence_summary: "High confidence in source identity and method description; medium confidence in transfer because results were not independently reproduced."
safety_scope: "non-sensitive scholarly review and authorized implementation planning"
distribution_notes: "Public URLs and derived Markdown only; private source files and archive paths withheld."
---

# QFT Tuning - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | QFT arXiv record | Primary artifact | Metadata HTML | arXiv:2310.07147v3 | https://arxiv.org/abs/2310.07147 | Public scholarly locator; source file withheld. | 2026-08-03 | Inspected |
| S2 | QFT full paper | Primary artifact | Full-paper HTML | arXiv:2310.07147v3 | https://arxiv.org/html/2310.07147 | Public scholarly locator; source file withheld. | 2026-08-03 | Inspected |
| S3 | QFT PDF | Primary artifact | PDF | arXiv:2310.07147v3 | https://arxiv.org/pdf/2310.07147 | Public scholarly locator; source file withheld. | 2026-08-03 | Integrity checked |
| S4 | OpenReview QFT record | Venue context | Review record | SPOT / ICLR 2026 | https://openreview.net/forum?id=PcKjjZOnfc | CC BY 4.0 visibility recorded on the page; no source file deposited. | 2026-08-03 | Inspected |
| S5 | Private source verification record | Source-integrity evidence | Local companion records | Complete-source gate | Source files withheld locally | Private archive material is not redistributed. | 2026-08-03 | Passed |
| S6 | LlamaCpp Runtime DEP | Related DEP | Markdown | DEP-E-20260712-LlamaCpp-Runtime | `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md` | Repository-derived context; not independent validation here. | 2026-08-03 | Inspected |
| S7 | KDFlow LLM Distill DEP | Related DEP | Markdown | DEP-E-20260712-KDFlow LLM Distill | `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` | Repository-derived context; not independent validation here. | 2026-08-03 | Inspected |
| S8 | RandLoRA Full-rank DEP | Related DEP | Markdown | DEP-E-20260728-RandLoRA Full-rank | `.lake-data/DEP-E/DEP-E-20260728-RandLoRA Full-rank/randlora_full_rank_manuscript.md` | Repository-derived context; not independent validation here. | 2026-08-03 | Inspected |

The private source unit was initially partial because full-paper HTML was missing. A bounded brokered repair produced a verified PDF, full-paper HTML, metadata HTML, provenance, summary, verification report, and receipt. The optional TeX/source package was unavailable. No source file was copied into this DEP.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Official metadata | Title, authors, arXiv ID, v3 date, DOI, subjects, abstract, and venue note. | Source identity and problem framing. | High | Metadata is not experimental evidence. |
| E2 | S2 | Primary full paper | Method sections, algorithms, memory table, benchmark table, MT-Bench table, appendices, and conclusion. | Mechanism, reported results, assumptions, and limitations. | High | No independent reproduction. |
| E3 | S3/S5 | Primary PDF plus private verification | PDF header/EOF and full-paper HTML structural gates. | Complete-source review eligibility. | High | Integrity does not validate research claims. |
| E4 | S4 | OpenReview record | Workshop context, publication dates, keywords, and license visibility. | Publication context. | High | Venue record does not validate benchmarks. |
| E5 | S6 | Related DEP manuscript | Quantization-runtime packaging and a narrow compatibility correction. | Runtime bridge. | Medium-high | Related release was not executed here. |
| E6 | S7 | Related DEP manuscript | Teacher/student workload separation, hidden-state transfer, and memory/throughput tradeoffs. | Distributed-training bridge. | Medium-high | Related experiments were not re-run. |
| E7 | S8 | Related DEP manuscript | Full-rank parameter-efficient adaptation and compute/memory tradeoff. | Adaptation-capacity bridge. | Medium-high | Related experiments were not re-run. |

## Executive Summary

QFT proposes a way to make full-parameter LLM fine-tuning fit smaller GPU memory budgets by quantizing weights, gradients, and optimizer states, then designing the update path around those representations. The method combines a quantization-robust Lion optimizer, a dense/sparse hybrid weight quantizer that protects a small outlier set, and a stack-based gradient-flow scheme for integer-stored weights (E2).

The paper reports 25.3 GB total and 28.9 GB peak memory for QFT when fine-tuning LLaMA-2-7B, compared with 104 GB total and 129 GB peak for FP32 Adam; the model-state row is reported as 21% of standard Adam. Reported benchmark averages remain close to full-precision baselines: 57.4 for QFT versus 58.0 for FT-Adam on 7B, and 60.4 versus 61.2 on 13B. The paper reports a 1.2-1.3x time increase from quantize/dequantize overhead (E2).

Author claims are supported as source characterization, but not as independently reproduced results. Reviewer interpretation: QFT's durable contribution is a coordinated approximation contract in which dense state is compressed, sparse exceptions are preserved, and update recovery is observable. Transfer to other models or production settings remains uncertain because the inspected evaluation is narrow and no public implementation or reproduction manifest was identified on the primary surfaces.

## Detailed Summary

### Problem context

Full-parameter fine-tuning offers more update capacity than parameter-efficient methods, but standard training stores several full-size state tensors. The paper frames FP32 Adam as especially expensive because weights, gradients, momentum, and variance dominate the memory budget. Mixed precision reduces arithmetic precision but retains an FP32 master copy, while PEFT reduces trainable parameters at the cost of a restricted update space (E2).

### Method and mechanism

QFT uses uniform quantization for gradients and momentum. It selects Lion because Lion tracks momentum without Adam's variance and applies sign-based updates with consistent magnitude. Under additive, bounded Gaussian quantization-error assumptions, the paper derives a condition under which the update sign is likely to remain invariant. Its appendix reports that at least 97.9% of sampled cases satisfy the stated ratio threshold in the inspected setting (E2).

Weights are harder to quantize because sparse outliers expand the dynamic range while carrying potentially important representational information. QFT decomposes a weight matrix into a dense central component and a sparse outlier component. The dense component is quantized; the sparse component remains in floating point and is stored in a sparse format. The paper chooses a one-percent outlier threshold as a memory/accuracy compromise and updates thresholds lazily once per epoch (E2).

The integer training pipeline dequantizes weights for floating-point computation, computes gradients layer by layer, quantizes gradients for retention on a global stack, and pops them in reverse order during the quantized Lion update. The LIFO ordering is intended to provide constant-time gradient access without asking ordinary floating-point autograd to own gradients for integer parameters (E2).

### Experimental setup

The evaluation uses LLaMA-2 7B and 13B models, a 94.1K ShareGPT-derived instruction dataset, three epochs, global batch size 128, learning rate 2e-5, and language-model evaluation harness benchmarks. It compares QFT with LoRA, FP32 Adam full tuning, FP32 Lion full tuning, and Bitsandbytes-based tuning. MT-Bench is scored by GPT-4, and the source also includes qualitative examples (E2).

### Results

Table 1 reports QFT's 7B total and peak memory at 25.3 GB and 28.9 GB, against 104 GB and 129 GB for FP32 Adam. Table 2 reports 7B few-shot averages of 57.4 for QFT, 58.0 for FT-Adam, 57.9 for FT-Lion, and 57.5 for FT-Bnb. For 13B, QFT and FT-Bnb are both 60.4, while FT-Adam is 61.2. Table 3 reports QFT MT-Bench scores of 5.95 for 7B and 6.27 for 13B, versus 6.08 and 6.46 for FT-Adam. The paper reports comparable loss convergence and a 1.2-1.3x time penalty (E2).

### Limitations and conclusion

The source demonstrates a narrow but meaningful trade: lower memory for additional quantization/dequantization work and more complex state handling. The inspected evidence does not show repeated-seed uncertainty, energy measurement, broad architecture coverage, longer-run stability, or independent code reproduction. The conclusion that QFT enables affordable full-parameter tuning is therefore best preserved as a claim bounded to the reported LLaMA-2 experiments and resource assumptions (E2).

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | QFT quantizes weights, gradients, and optimizer states to reduce full-parameter tuning memory. | Author claim | E2 | Directly supported by the method and memory sections. | High |
| C2 | Lion's sign-based update is robust to the paper's modeled quantization error. | Author claim | E2 | The proof is conditional on additive bounded Gaussian error assumptions. | Medium-high |
| C3 | Sparse outlier preservation improves weight approximation at modest memory cost. | Author claim | E2 | Supported by the one-percent threshold ablation in Appendix D. | High within the reported layer/setting |
| C4 | QFT preserves comparable benchmark performance to full-precision baselines in the reported LLaMA-2 setup. | Author claim | E2 | Tables support near-parity, but the comparison lacks independent reproduction and repeated-run uncertainty. | Medium-high |
| C5 | The main engineering contribution is an auditable separation of compressed dense state, protected sparse state, and update recovery. | Reviewer interpretation | E2, E5-E7 | A cross-source interpretation, not a direct author claim. | Medium |
| C6 | A fair successor evaluation should compare memory, bandwidth, compute, quality, and reproducibility together. | Reviewer interpretation | E2, E5-E7 | Testable implementation recommendation derived from the four reviewed artifacts. | Medium |

## Methodology

- `Research objective`: Preserve QFT's source-grounded problem, mechanism, reported evidence, limitations, and bounded implementation relevance while bridging exactly three related DEP entries.
- `Sources inspected`: Official arXiv metadata and full-paper HTML, the canonical PDF, the OpenReview record, private source-integrity companions, and the three related Black Lake manuscripts and their cited public sources.
- `Discovery strategy`: Enumerated the local archive with `rg --files -g "*.pdf"`, treated each unique PDF parent as one paper unit, selected a uniform random index with PowerShell `Get-Random`, and derived the identifier from the unit readme and filename.
- `Inclusion criteria`: Full-paper source unit passed PDF and HTML integrity gates; primary method, experiment, appendix, and limitation evidence was included; related entries had concrete overlap with quantization, training resources, adaptation capacity, or runtime validation.
- `Exclusion criteria`: Previously deposited papers, same-paper recent markers, abstract-only units, invalid or incomplete source units after bounded repair, private source-file redistribution, unreproduced deployment claims, and unrelated DEP context.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, safety/ethics, replication, and provenance analysis.
- `Evidence handling`: Major claims are mapped to E1-E7 and labeled as source claims or reviewer interpretations. Reported metrics are kept within the model, dataset, baseline, and evaluator settings stated by the source.
- `Uncertainty handling`: Missing implementation, missing independent reproduction, narrow model coverage, and transfer uncertainty are explicit rather than inferred away.
- `Random selection and deduplication`: 75,960 PDFs collapsed to 75,957 paper units; selected index 11,795; duplicate exclusions 0; reselections 0; public 24-hour cutoff 2026-08-02. Scans covered Black-Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and related Black-Lake-Data search context.
- `Source-integrity repair`: The selected unit was initially partial because full-paper HTML was absent. One bounded brokered repair completed the local source bundle; no source files were uploaded.

## Scope, Constraints, and Assumptions

- `Scope`: QFT v3's problem, method, reported LLaMA-2 experiments, appendices, limitations, related DEP synthesis, and safe implementation planning.
- `Temporal boundary`: Public and repository sources accessed 2026-08-03; paper version pinned to arXiv v3 revised 2026-03-18.
- `Evidence limits`: No code, build, model, dataset, benchmark, or energy experiment was independently run. Source package acquisition was unavailable.
- `Assumptions`: The arXiv v3 record and OpenReview record refer to the same reviewed work; the three related repository manuscripts accurately preserve their own cited evidence for this cross-source synthesis.
- `Constraints`: Source files remain private; public artifacts contain only derived Markdown and public locators. Implementation examples are bounded to synthetic, authorized, non-consequential evaluation.
- `Out of scope`: Production deployment, automatic checkpoint conversion, claims of universal GPU compatibility, and any independent performance certification.
- `Intended use`: DEP deposition, future reviewer handoff, controlled replication planning, and resource-aware training design.
- `Audience`: LLM training engineers, model-compression researchers, systems evaluators, and Black Lake reviewers.
- `Reproducibility boundary`: The paper's method and reported tables are inspectable; reproduction requires exact code, kernels, checkpoints, data preparation, seeds, and hardware configuration.
- `Data sensitivity`: Public scholarly sources; private archive copies and extraction companions are withheld.

## Observations

- `Observed pattern`: QFT's largest reported gain comes from state representation, not from reducing the task's trainable parameter count.
- `Technical implication`: Sparse exceptions and quantizer metadata are part of the model state contract, not incidental implementation details.
- `Contradiction or tension`: A 21% model-state footprint is attractive, but QFT adds compute overhead and state-management complexity that may move the bottleneck to kernels, allocator behavior, or checkpoint handling.
- `Cross-source pattern`: KDFlow compresses a communication boundary, RandLoRA compresses trainable coordinates, and llama.cpp validates a deployment boundary; QFT compresses persistent training state.
- `Open question`: Whether these boundaries can be composed without double-counting approximation error or shifting cost into an unmeasured subsystem remains unresolved.
- `Reviewer hypothesis`: A common evidence ledger could expose a Pareto frontier across memory, bandwidth, compute, quality, and reproducibility more clearly than isolated method-specific scores.

## Considerations

QFT-like training must monitor numerical drift, outlier growth, update-sign flips, quantizer-scale changes, allocator peaks, checkpoint conversion, and downstream behavior. Model and dataset licenses need review before any authorized reproduction. A lower memory footprint can widen access to training while making correctness harder to inspect, so each checkpoint should carry quantization metadata and a reference-comparison result. Deployment decisions should not rely on the paper's benchmark parity alone, especially where model output affects people or durable system state.

The related entries add operational tradeoffs. KDFlow shows that communication reduction can require local reconstruction work and strict shape/tokenizer compatibility. RandLoRA shows that parameter efficiency can preserve a different notion of update capacity but incur basis-combination compute. The llama.cpp entry shows that a quantization change needs configuration-specific runtime regression evidence. These are complementary constraints, not substitutes for QFT validation.

## Strengths

- The paper targets a concrete bottleneck and reports both memory and quality evidence.
- The method decomposes quantization risk into optimizer state, weight outliers, and gradient flow rather than treating all tensors identically.
- The appendices expose assumptions, threshold selection, and a sign-invariance diagnostic that make follow-on tests possible.
- The full-paper source is available for inspection, and the public arXiv/OpenReview records provide stable identity and version context.
- The cross-DEP bridge connects training-state compression to communication compression, full-rank adaptation, and runtime compatibility.

## Weaknesses

- The evaluated model family, corpus, schedule, and hardware setting are narrow relative to the general “LLM” framing.
- No independent reproduction, repeated-seed uncertainty, energy accounting, or public implementation was established in this review.
- The Lion robustness argument depends on error assumptions that may not capture correlated, layerwise, or non-Gaussian quantization behavior during training.
- The benchmark averages can hide task-specific regressions, and MT-Bench depends on an automatic evaluator.
- The time-for-memory trade is reported as a multiplier without a full systems breakdown of kernel, allocator, checkpoint, and host-memory costs.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release a version-pinned reference implementation and manifest | Reproducibility | The method is difficult to validate from prose alone. | Repeatable baselines and ablations. | Maintenance and dependency burden. | Reproduce Tables 1-3 on one authorized setup. |
| Add repeated seeds and architecture shifts | Statistical validity | Single-run parity may be unstable or model-specific. | Better uncertainty and transfer estimates. | More compute and data governance. | Report distributions, not only means. |
| Instrument quantization overhead | Systems evaluation | The 1.2-1.3x time multiplier is not a causal breakdown. | Identify kernel and memory bottlenecks. | Profiling overhead and hardware dependence. | Compare per-layer quantize/dequantize, allocator, and checkpoint costs. |
| Add update-sign and outlier drift diagnostics | Numerical robustness | Initial thresholds may fail during longer training. | Early warning for instability. | Telemetry storage and review effort. | Trigger controlled fallback or checkpoint rejection. |

## Potential Implementations

1. **Authorized small-model QFT harness**
   - `User`: Training engineer evaluating memory-constrained full tuning.
   - `Goal`: Measure whether quantized state reduces verified peak memory without unacceptable quality loss.
   - `Core mechanism`: Wrap dense quantization, sparse outlier retention, quantized Lion state, and a stack-based gradient ledger around a small public model.
   - `Required inputs`: Licensed model and dataset, version-pinned kernels, seed, quantizer configuration, and FP32 reference run.
   - `Outputs`: Memory ledger, quality comparison, update-sign drift report, and checkpoint metadata.
   - `Risk controls`: Local-only processing, no secrets, bounded model size, human review, and explicit fallback to the reference path.
   - `Evaluation`: Compare peak memory, wall time, task metrics, numerical divergence, and failure recovery under matched seeds.

2. **Resource-aware adaptation router**
   - `User`: Platform engineer choosing between full tuning, PEFT, or distillation.
   - `Goal`: Select a method from declared memory, bandwidth, quality, and latency constraints.
   - `Core mechanism`: Use a QFT-like memory estimator, a KDFlow-like payload estimator, and a RandLoRA-like trainable-coordinate estimator before a run.
   - `Required inputs`: Model sizes, layer widths, available memory, link bandwidth, quality tolerance, and authorized test budget.
   - `Outputs`: Method recommendation, rejected alternatives, predicted bottleneck, and validation plan.
   - `Risk controls`: No autonomous production switch, conservative thresholds, immutable decision record, and reviewer approval.
   - `Evaluation`: Measure predicted versus observed resource use and quality under a small-model matrix.

3. **Quantization release gate**
   - `User`: Runtime or model-release maintainer.
   - `Goal`: Verify that a compressed training checkpoint remains usable in declared inference configurations.
   - `Core mechanism`: Attach quantizer metadata and run model-output, memory, and compatibility smoke tests across pinned runtime builds.
   - `Required inputs`: Checkpoint, quantizer metadata, tokenizer, target runtime, synthetic prompts, and reference outputs.
   - `Outputs`: Release evidence card, pass/fail matrix, known gaps, and rollback pointer.
   - `Risk controls`: Synthetic or public prompts, no consequential action, checksums, isolated execution, and human release approval.
   - `Evaluation`: Check output parity, memory peak, latency, unsupported kernels, and deterministic artifact provenance.

## Three Ways to Exercise This Research

1. `Memory-only accounting`: Use synthetic tensor shapes and the paper's Table 1 dimensions to compare FP32, mixed precision, and QFT-like state budgets. Output a traceable spreadsheet or Markdown ledger. Success is arithmetic agreement with the source table; stop if a dimension or accounting assumption is missing.
2. `Small-model numerical probe`: On an authorized public small model, compare dense uniform quantization with dense-plus-sparse outlier retention for weight reconstruction and update-sign stability. Output error distributions and an outlier-sensitivity report. Success is a reproducible, bounded result; stop on license, memory, or numerical-instability concerns.
3. `Cross-method resource matrix`: Use synthetic hidden/logit tensors and a low-rank basis to compare QFT-like state storage, KDFlow-like transfer, and RandLoRA-like trainable coordinates. Output memory, payload, compute, and quality-proxy ledgers. Success is an explicit Pareto comparison; stop before any production or consequential deployment.

## Example MVP Product

- `Product name`: Quantized Training Evidence Board.
- `Target user`: LLM training engineer, evaluator, or model-release reviewer.
- `Problem`: Memory-saving training methods report different resource and quality measures, making safe comparison difficult.
- `Core workflow`: Import a versioned experiment manifest, compute predicted state/payload budgets, attach authorized run telemetry, compare against a reference, and require review before release.
- `Data requirements`: Public or authorized model metadata, synthetic/public evaluation inputs, quantizer metadata, resource telemetry, and reference outputs.
- `Architecture`: Local manifest validator, resource estimator, experiment adapter, metric store, provenance ledger, report generator, and human-review interface.
- `Success metrics`: Prediction error for memory/throughput, quality parity, numerical-drift detection, reproducible reruns, and zero private-path leaks.
- `Risk controls`: Local-only sensitive processing, no secrets in logs, source-file withholding, checksums, access control, bounded compute, rollback, and no autonomous consequential actions.
- `Limitations`: The MVP does not implement QFT, certify arbitrary hardware, or establish production readiness; it only makes evidence comparable.
- `MVP boundary`: Small public models and synthetic resource probes; no large model downloads or unattended training.
- `Deployment model`: Local batch or notebook workflow with Markdown/JSON outputs.
- `Evaluation plan`: Deterministic smoke tests, reference parity, shape validation, resource-budget checks, and reviewer acceptance criteria.
- `Failure modes`: Missing metadata, non-comparable baselines, outlier drift, unsupported kernels, allocator surprises, checkpoint mismatch, and overconfident transfer.
- `Maintenance plan`: Version-pin runtimes and kernels, refresh baseline manifests, preserve historical evidence, and rerun release gates after dependency changes.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| LlamaCpp Runtime - DEP-E | Related DEP entry | Quantization-runtime packaging, compatibility correction, and the distinction between published availability and executed validation. | `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md` |
| KDFlow LLM Distill - DEP-E | Related DEP entry | Workload-aware teacher/student separation, hidden-state transfer, local logit reconstruction, and memory/throughput tradeoffs. | `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` |
| RandLoRA Full-rank - DEP-E | Related DEP entry | Parameter-efficient memory use with full-rank update structure and explicit compute overhead. | `.lake-data/DEP-E/DEP-E-20260728-RandLoRA Full-rank/randlora_full_rank_manuscript.md` |

The three related entries are conceptual bridges, not independent validation of QFT. Their public source bases are listed in `## Source References`.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2310.07147 | Identity, authors, version history, DOI, subject classification, and abstract. | 2026-08-03 | Official metadata. |
| R2 | https://arxiv.org/html/2310.07147 | Method, equations, algorithms, tables, appendices, limitations, and conclusion. | 2026-08-03 | Official full paper. |
| R3 | https://arxiv.org/pdf/2310.07147 | PDF source and canonical integrity reference. | 2026-08-03 | Private copy withheld. |
| R4 | https://doi.org/10.48550/arXiv.2310.07147 | Persistent identifier. | 2026-08-03 | arXiv-issued DOI. |
| R5 | https://openreview.net/forum?id=PcKjjZOnfc | SPOT/ICLR 2026 workshop context, publication dates, keywords, and CC BY 4.0 visibility. | 2026-08-03 | Venue record. |
| R6 | https://github.com/ggml-org/llama.cpp/releases/tag/b9789 | Related runtime release inventory and quantization context. | 2026-08-03 | Used through related DEP. |
| R7 | https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b | Related MoE-with-MTP quantization compatibility correction. | 2026-08-03 | Used through related DEP. |
| R8 | https://arxiv.org/abs/2603.01875 | Related KDFlow paper identity and method context. | 2026-08-03 | Used through related DEP. |
| R9 | https://github.com/songmzhang/KDFlow | Related KDFlow implementation context. | 2026-08-03 | Used through related DEP; not executed. |
| R10 | https://arxiv.org/abs/2502.00987 | Related RandLoRA paper identity and full-rank PEFT context. | 2026-08-03 | Used through related DEP. |
| R11 | `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md` | Related runtime quantization and compatibility synthesis. | 2026-08-03 | Repository-relative artifact inspected. |
| R12 | `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` | Related workload-aware training and transfer synthesis. | 2026-08-03 | Repository-relative artifact inspected. |
| R13 | `.lake-data/DEP-E/DEP-E-20260728-RandLoRA Full-rank/randlora_full_rank_manuscript.md` | Related full-rank PEFT and compute/memory synthesis. | 2026-08-03 | Repository-relative artifact inspected. |
| R14 | Private verified source bundle, source files withheld locally | Full-paper review and integrity-gate evidence. | 2026-08-03 | No source file was uploaded or deposited. |

## Appendix

### Selection and eligibility record

- Candidate enumeration: `rg --files -g "*.pdf"`.
- PDF candidates: 75,960.
- Unique parent-directory paper units: 75,957.
- Random method: uniform PowerShell `Get-Random` zero-based index.
- Selected index: 11,795.
- Selected identifier: arXiv:2310.07147.
- Duplicate exclusions: 0.
- Reselections: 0.
- Public 24-hour cutoff: 2026-08-02.
- Dedup scan locations: Black-Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and related Black-Lake-Data search context.

### Source-integrity record

- Initial state: partial; valid PDF present, full-paper HTML absent.
- Repair: one bounded brokered single-paper repair.
- Final state: complete; PDF and full-paper HTML gates passed.
- Optional source package: unavailable and withheld.
- Source locality: PDF, HTML, metadata, extraction companions, cache, provenance, verification records, and receipts remained private; no source file or `.source/` directory was uploaded.

### Reproduction checklist

1. Pin arXiv v3, model revisions, dataset preparation, seed, optimizer settings, quantizer settings, kernels, and runtime versions.
2. Reproduce the 7B memory table with allocator peaks separated from model state, activations, and temporary buffers.
3. Re-run the 7B/13B task tables with repeated seeds and independent evaluation where possible.
4. Ablate Lion, sparse outlier retention, and stack-based gradient flow separately.
5. Compare QFT, KDFlow-style transfer, RandLoRA-style adaptation, and runtime quantization on a common resource-quality ledger.

The checklist is a follow-up plan, not evidence that reproduction occurred in this run.
