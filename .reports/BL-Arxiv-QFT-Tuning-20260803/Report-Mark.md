# Report-Mark: QFT Tuning

Run date: 2026-08-03

## Source Metadata

- **Title:** *QFT: Quantized Full-parameter Tuning of LLMs with Affordable Resources*
- **Authors:** Zhikai Li, Xiaoxuan Liu, Banghua Zhu, Zhen Dong, Qingyi Gu, and Kurt Keutzer.
- **Identifier:** arXiv:2310.07147v3; DOI `10.48550/arXiv.2310.07147`.
- **Dates:** submitted 2023-10-11; v3 revised 2026-03-18; OpenReview record published 2026-03-03 and modified 2026-03-18.
- **Venue/context:** ICLR 2026 Workshop on Scaling Post-training for LLMs (SPOT), according to the arXiv and OpenReview records.
- **Primary sources:** [arXiv metadata](https://arxiv.org/abs/2310.07147), [arXiv full-paper HTML](https://arxiv.org/html/2310.07147), [arXiv PDF](https://arxiv.org/pdf/2310.07147), and [OpenReview record](https://openreview.net/forum?id=PcKjjZOnfc).
- **Source integrity:** complete after one bounded local repair. The verified PDF was 1,024,104 bytes and the verified full-paper HTML was 259,410 bytes with 56,776 body characters, 25 headings, and 7 paper-structure terms. Source files and private archive paths were withheld from the public repository.
- **Available implementation evidence:** no official code repository was identified on the inspected arXiv or OpenReview surfaces; no implementation was executed.

## Concise Research Notes

### Problem

The paper addresses the memory cost of full-parameter LLM fine-tuning. It argues that standard FP32 Adam stores weights, gradients, momentum, and variance at a cost that makes 7B-scale tuning difficult on commodity GPUs. Parameter-efficient tuning reduces memory but restricts the trainable update space.

### Method

QFT stores weights, gradients, and optimizer states as INT8-oriented representations. It uses Lion for gradients and momentum because its sign-based update has consistent magnitudes and needs only momentum rather than Adam's variance. It uses a hybrid feature quantizer: dense central values are uniformly quantized while a sparse set of outlier features remains in floating point. A stack-based gradient-flow scheme stores quantized layer gradients during backpropagation and retrieves them in LIFO order for updates.

### Evidence and results

The paper reports a LLaMA-2-7B memory profile of 25.3 GB total and 28.9 GB peak for QFT, versus 104 GB total and 129 GB peak for FP32 Adam; the model-state portion is reported as 21% of standard Adam. On the 7B few-shot benchmark average, QFT scores 57.4 versus 58.0 for FT-Adam, 57.9 for FT-Lion, and 57.5 for FT-Bnb. On 13B, QFT and FT-Bnb both score 60.4 while FT-Adam scores 61.2. The paper also reports MT-Bench scores of 5.95 for QFT versus 6.08 for FT-Adam on 7B, and 6.27 versus 6.46 on 13B. QFT is reported to incur a 1.2-1.3x training-time increase from quantize/dequantize overhead.

The source's theory and appendix report that at least 97.9% of sampled update-ratio cases exceed the 1.645 sign-invariance threshold under the paper's error assumptions. The weight quantizer's one-percent sparse outlier setting reduces the reported L2 quantization distance from 436 at zero-percent outlier preservation to 0.619 at one percent, while increasing the weight-memory row from 7.06 GB to 7.42 GB.

### Limitations

The evaluation centers on LLaMA-2 7B and 13B instruction tuning with a 94.1K ShareGPT-derived corpus, three epochs, and fixed training settings. Results were not independently reproduced in this run. The evidence does not establish behavior across newer model families, longer training, distribution shift, repeated seeds, energy cost, or other hardware. MT-Bench uses GPT-4 as an automatic evaluator, and the inspected source does not provide a public implementation link or a complete reproduction manifest.

### Implementation relevance and reviewer interpretation

QFT is best understood as a state-storage and gradient-flow design with a deliberate time-for-memory trade. Its most reusable engineering idea is not “INT8 everywhere” in isolation; it is the separation of dense approximate state, sparse protected state, and a versioned update path that makes the approximation auditable. Reviewer interpretation: a safe implementation should expose quantizer scales, outlier rates, allocator peaks, update-sign changes, and task-quality deltas as first-class evidence rather than treating the headline memory ratio as sufficient.

## Evidence and Attribution

| Evidence | Basis | What it supports | Confidence | Boundary |
|---|---|---|---|---|
| E1 | arXiv metadata record | Identity, authors, version history, DOI, subjects, and venue note. | High | Metadata is not experimental evidence. |
| E2 | arXiv full-paper HTML | Problem framing, quantized Lion, hybrid feature quantizer, integer gradient flow, tables, appendices, and conclusion. | High | Source claims were not independently reproduced. |
| E3 | Verified private PDF and full-paper HTML integrity records | Complete-source gate before review. | High | Integrity does not validate technical claims. |
| E4 | OpenReview record | SPOT/ICLR 2026 context, publication dates, keywords, and CC BY 4.0 visibility. | High | Venue metadata does not validate the reported benchmarks. |
| E5 | `llama-cpp-runtime.md` | Related runtime quantization and compatibility evidence. | Medium-high | Related artifact was not re-run. |
| E6 | `kdflow_llm_distill_manuscript.md` | Related workload separation, hidden-state transfer, memory, and throughput evidence. | Medium-high | Related artifact's experiments were not re-run. |
| E7 | `randlora_full_rank_manuscript.md` | Related parameter-efficient/full-rank and memory/compute tradeoff evidence. | Medium-high | Related artifact's experiments were not re-run. |

## Related DEP Entries

1. [`.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md`](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md) — selected because it records direct evidence about quantization-runtime packaging and a narrow MoE-with-MTP quantization correction; its source basis is the official [llama.cpp b9789 release](https://github.com/ggml-org/llama.cpp/releases/tag/b9789) and [linked commit](https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b).
2. [`.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md`](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-KDFlow%20LLM%20Distill/kdflow_llm_distill_manuscript.md) — selected because it treats teacher inference and student optimization as different resource workloads, transferring hidden states instead of full logits; its source basis is [arXiv:2603.01875](https://arxiv.org/abs/2603.01875) and the [KDFlow implementation](https://github.com/songmzhang/KDFlow).
3. [`.lake-data/DEP-E/DEP-E-20260728-RandLoRA Full-rank/randlora_full_rank_manuscript.md`](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260728-RandLoRA%20Full-rank/randlora_full_rank_manuscript.md) — selected because it compares parameter-efficient memory savings with full-rank update capacity and exposes a compute-for-memory trade; its source basis is [arXiv:2502.00987](https://arxiv.org/abs/2502.00987).

## Synthesis Note

### Concept Bridge

QFT compresses the state carried by a single full-parameter training loop. KDFlow separates teacher inference from student optimization and compresses the cross-process payload to hidden states. RandLoRA restricts the trainable coordinates while recovering full-rank update structure through a random basis. The llama.cpp entry adds the downstream runtime perspective: a quantization idea is only operationally useful when its target model configurations and platform paths are validated. Together, the four records form a resource-aware chain from trainable state representation, through distributed transfer, to runtime compatibility and release evidence.

### Potential Implementations

1. **Quantized-state evidence wrapper:** Add a bounded QFT-style state wrapper that records dense quantizer scale, sparse outlier rate, update-sign flips, allocator peaks, and task-quality deltas for each authorized training run.
2. **Workload-aware adaptation router:** Choose among QFT-like full tuning, KDFlow-like teacher/student separation, and RandLoRA-like low-parameter updates using a declared memory, bandwidth, quality, and latency budget; emit the decision and rejected alternatives as an evidence ledger.
3. **Quantization-to-runtime release gate:** Pair a small-model training smoke test with llama.cpp-style configuration checks so that a memory reduction is accepted only when dequantized checkpoints, target kernels, and downstream inference behavior pass version-pinned tests.

### Deeper Relationship Observations

1. Memory efficiency moves through the system: QFT reduces persistent optimizer state, KDFlow reduces communication payload, RandLoRA reduces trainable degrees of freedom, and llama.cpp reduces deployment representation cost. These are complementary budgets rather than interchangeable claims.
2. Each method protects a different kind of information. QFT protects sparse weight outliers and update direction, KDFlow protects teacher information through hidden-state transfer, and RandLoRA protects update expressivity through basis coverage. The runtime entry shows that protection must be checked again after serialization and execution.
3. The strongest common design pattern is explicit approximation with an observable recovery path. QFT dequantizes for computation, KDFlow reconstructs logits locally, and RandLoRA reconstructs full-rank updates from basis coefficients; each needs a parity test against a less compressed reference.

### Conceptual Similarities

1. All four entries treat representation choices as systems decisions that trade memory or bandwidth for compute and validation burden.
2. All four rely on structured sparsity or structured factorization rather than unbounded precision: sparse outliers, hidden-state width, random bases, or model/runtime quantization layouts.
3. All four make deployment or training feasibility conditional on evidence beyond a single quality score: memory peaks, throughput, compatibility, or reproducibility must be measured.

### MVP Implementations with Code Mock-Ups

1. **State budget ledger:** estimate dense and sparse state memory before an authorized small-model run.

```python
def state_budget(params, bits=8, sparse_fraction=0.01, fp_bytes=4):
    dense = params * (bits / 8) * (1 - sparse_fraction)
    sparse = params * sparse_fraction * fp_bytes
    return {"bytes": dense + sparse, "outlier_fraction": sparse_fraction}
```

2. **Hidden-state transfer break-even check:** compare full-logit transfer with hidden-state transfer plus local head computation using synthetic shapes.

```python
def transfer_plan(tokens, vocab, hidden, bytes_per_value=2):
    logits = tokens * vocab * bytes_per_value
    hidden_payload = tokens * hidden * bytes_per_value
    return {"logit_bytes": logits, "hidden_bytes": hidden_payload,
            "recompute_required": hidden_payload < logits}
```

3. **Adaptation choice ledger:** select a bounded method from declared resource constraints and preserve the rationale.

```python
def choose_method(memory_gb, needs_full_rank, bandwidth_gbps):
    if memory_gb >= 30 and needs_full_rank:
        return "QFT-like full tuning"
    if needs_full_rank:
        return "RandLoRA-like basis updates"
    if bandwidth_gbps < 100:
        return "KDFlow-like hidden-state transfer"
    return "baseline requiring explicit comparison"
```

These mock-ups are planning aids, not production training code. They use no source data, credentials, or external actions. A real implementation must add schema validation, tensor-shape checks, numerical parity tests, license review, and failure logging without sensitive inputs.

### Developer Challenges

1. Build a parity harness that measures memory, communication, wall time, energy, and task quality under identical seeds and data rather than comparing isolated headline metrics.
2. Make approximation metadata durable: scales, sparse masks, basis construction, hidden-state dimensions, kernel versions, and checkpoint conversion rules must travel with each artifact.
3. Design failure handling for numerical drift, outlier growth, bandwidth saturation, unsupported kernels, and checkpoint incompatibility before enabling larger runs.

### Author Challenges

1. Release a version-pinned reference implementation and reproduction manifest that exposes the contribution of each QFT component separately.
2. Extend the evaluation beyond LLaMA-2 and ShareGPT with repeated seeds, newer architectures, longer schedules, independent evaluators, and energy/cost accounting.
3. Compare QFT against contemporary low-bit optimizers, full-rank PEFT, and workload-separated distillation under a common quality-memory-throughput frontier.

## Validation Notes

- The selected unit was initially partial; one bounded brokered repair produced verified full-paper HTML and updated local README, provenance, summary, and verification records.
- PDF gate: minimum size, `%PDF-` header, and trailing `%%EOF` passed.
- Full-paper HTML gate: minimum size, more than 2,000 body characters, article/document structure, at least two headings, and at least two paper-structure terms passed.
- Deduplication: 75,960 PDFs, 75,957 unique parent units, draw 11,795; duplicate exclusions 0; reselections 0; public 24-hour cutoff 2026-08-02.
- Repository output gate: only Markdown artifacts and the required publication-index row were generated; no PDF, HTML, source archive, extracted text, cache, private path, or `.source/` directory was staged.
- Review boundary: no experiment, build, code execution, benchmark reproduction, or model download was performed.

## Attribution Block

- Source URL: https://arxiv.org/abs/2310.07147
  - Applies to: source identity, authors, version history, DOI, subjects, and abstract-level framing.
- Source URL: https://arxiv.org/html/2310.07147
  - Applies to: full-paper method, evidence tables, appendices, limitations, and conclusion.
- Source URL: https://arxiv.org/pdf/2310.07147
  - Applies to: canonical PDF reference and source-integrity cross-check; the private PDF was not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2310.07147
  - Applies to: persistent identifier.
- Source URL: https://openreview.net/forum?id=PcKjjZOnfc
  - Applies to: SPOT/ICLR 2026 workshop context, publication dates, keywords, and license visibility.
- Source URL: https://github.com/ggml-org/llama.cpp/releases/tag/b9789
  - Applies to: related runtime quantization and release evidence.
- Source URL: https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b
  - Applies to: related quantization compatibility correction.
- Source URL: https://arxiv.org/abs/2603.01875
  - Applies to: related KDFlow manuscript evidence.
- Source URL: https://github.com/songmzhang/KDFlow
  - Applies to: related KDFlow implementation context.
- Source URL: https://arxiv.org/abs/2502.00987
  - Applies to: related RandLoRA manuscript evidence.
- Repository path: `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md`
  - Applies to: related DEP synthesis and runtime validation boundary.
- Repository path: `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md`
  - Applies to: related DEP synthesis and workload-aware training boundary.
- Repository path: `.lake-data/DEP-E/DEP-E-20260728-RandLoRA Full-rank/randlora_full_rank_manuscript.md`
  - Applies to: related DEP synthesis and full-rank/parameter-efficiency boundary.
- Source file: private verified arXiv source bundle, withheld locally.
  - Applies to: full-paper review and integrity gate; no source file was uploaded.
