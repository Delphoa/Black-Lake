# Report-Mark: SD-Search

## Source Metadata

| Field | Value |
|---|---|
| Title | SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning |
| Authors | Yufei Ma; Zihan Liang; Ben Chen; Zhipeng Qian; Huangyu Dai; Lingtao Mao; Xuxin Zhang; Chenyi Lei; Wenwu Ou |
| Identifier | arXiv:2605.18299v1 |
| DOI | https://doi.org/10.48550/arXiv.2605.18299 |
| Submitted | 2026-05-18 |
| Venue | arXiv; cs.AI, cs.CL, cs.IR |
| Source state | Verified complete local PDF, full-paper HTML, metadata HTML, and source package; all source files withheld |
| License note | arXiv record displays CC BY 4.0; public deposit contains derived Markdown only |
| Access date | 2026-08-01 |

## Concise Research Notes

SD-Search addresses a credit-assignment gap in search-augmented reasoning. Outcome-reward RL gives every action in a rollout the same trajectory-level advantage, even though individual search queries differ in usefulness. The paper uses one policy in two conditioning modes: a student sees inference-time context, while a teacher sees a hindsight block containing search-only sibling rollouts and Correct/Incorrect outcome labels. The student matches the teacher at search-query token positions with a top-k-truncated Jensen-Shannon divergence, added to GRPO after a warmup.

The authors report seven QA benchmarks, Qwen2.5-3B and Qwen2.5-7B backbones, a fixed December 2018 Wikipedia corpus, an E5-base-v2 retriever, and three retrieved passages per query. The 3B base model reaches 0.428 average Exact Match; the 7B instruct model reaches 0.476. Five seeds are reported for the 3B base comparison: 0.428 ± 0.008 for SD-Search, 0.404 ± 0.008 for AutoRefine, and 0.429 ± 0.007 for Thinker. A 200-step 3B run is reported at 11.9 hours on 8×H800 versus 10.3 hours for AutoRefine, a 15.5% end-to-end overhead.

## Evidence and Attribution

| ID | Evidence | Basis | Assessment |
|---|---|---|---|
| E1 | Identity, authors, date, subjects, DOI, and license | arXiv metadata record | High confidence source metadata |
| E2 | Motivation, trajectory format, hindsight block, future masking, outcome conditioning, JSD, and total objective | Full-paper HTML, PDF text, and TeX/source text | High confidence transcription |
| E3 | Seven-benchmark tables, 3B/7B comparisons, five-seed appendix, ablations, and training-cost breakdown | Full paper and source package | High for author-reported numbers; no independent rerun |
| E4 | Limitations: dependence on scorable gold answers and degeneration under all-success/all-failure groups | Limitations and scaling sections | High confidence source limitation |
| E5 | Token-cost/evidence-allocation, distillation, and RL neighboring records | Three related Black-Lake DEP manuscripts | Medium confidence contextual bridge |
| E6 | Uniform draw, dedup checks, repair gate, cache status, and source-withholding policy | Public-safe process logs and private validation records | High for process status; local details intentionally omitted |

## Related DEP Entries

1. `.lake-data/DEP-A/DEP-A-20260727-Token Tax RAG/2606.20898-whitepaper-review.md` — compares retrieval and long-context evidence-allocation regimes and proposes a cost-correctness frontier; this grounds SD-Search's search-policy gains in evidence-access and token-budget tradeoffs. Public record: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260727-Token%20Tax%20RAG/2606.20898-whitepaper-review.md
2. `.lake-data/DEP-E/DEP-E-20260725-DASD Reasoning/dasd_reasoning_manuscript.md` — reviews temperature-scheduled, divergence-aware, and mixed-policy sequence distillation; this is the closest training-objective neighbor for distribution alignment and rollout mismatch. Public record: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260725-DASD%20Reasoning/dasd_reasoning_manuscript.md
3. `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` — analyzes regularized policy optimization and convergence boundaries; this frames SD-Search as an RL objective extension whose empirical gains still require objective-validity and compute-matched checks. Public record: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md

## Synthesis Note

### Concept Bridge

SD-Search turns rollout history into a privileged, training-only teacher signal. The bridge to Black Lake is a three-layer evidence budget: Token Tax RAG asks when broader evidence access is worth its cost; DASD asks how distributional and on-policy mismatch should shape student updates; GPMD asks what objective and regularization imply for stability. SD-Search combines those concerns at query-decision granularity, but does not yet resolve open-ended scoring, policy drift, or independent compute accounting.

### Potential Implementations

1. **Query-credit receipt generator.** For an authorized synthetic QA corpus, record each search query, retrieved-document coverage, outcome label, and teacher-student divergence, then emit auditable per-query credit receipts without changing the production policy.
2. **Sandboxed search-policy trainer.** Add the JSD term and future-masking checks to a local GRPO trainer using public toy QA data, with a fixed retriever, reproducible seeds, and a hard stop when outcome groups become label-homogeneous.
3. **Evidence-budget controller.** Combine query-quality estimates with token-cost and cache-aware signals to choose between another retrieval step and a larger context window; evaluate only on held-out public questions and report quality-cost frontiers.

### Deeper Relationship Observations

1. The useful unit of supervision is not the whole answer trajectory but the decision surface where a query changes the evidence available to later reasoning.
2. Privileged context is valuable only when its leakage boundary is explicit; future masking is therefore an information-flow control, not merely a feature ablation.
3. Search quality, distillation quality, and RL stability are coupled through the rollout group: a homogeneous group removes the contrast that supplies the dense signal.

### Conceptual Similarities

1. SD-Search and DASD both align a student to richer distributional evidence while acknowledging that teacher-forced or privileged traces can mismatch inference-time behavior.
2. SD-Search and Token Tax RAG both treat evidence access as a resource-allocation decision whose value must be measured against token or latency cost.
3. SD-Search and GPMD both modify policy optimization with an auxiliary objective or regularizer, making stability and boundary conditions part of the claim rather than implementation detail.

### MVP Implementations with Code Mock-ups

1. **Synthetic query-credit ledger.**

```python
from dataclasses import dataclass

@dataclass
class QueryReceipt:
    query: str
    retrieved_ids: tuple[str, ...]
    answer_score: float
    jsd: float

def make_receipt(query, retrieved_ids, answer_score, jsd):
    return QueryReceipt(query, tuple(retrieved_ids), float(answer_score), float(jsd))
```

2. **Future-masking guard.**

```python
def mask_rollout(spans):
    """Keep only search spans for a training-only hindsight view."""
    return [text for kind, text in spans if kind == "search"]

def safe_hindsight(group):
    return [{"search": mask_rollout(item["spans"]),
             "label": item["label"]} for item in group]
```

3. **Held-out quality-cost gate.**

```python
def accept_policy(candidate, baseline, min_gain=0.01, max_cost_ratio=1.15):
    gain = candidate["exact_match"] - baseline["exact_match"]
    cost_ratio = candidate["tokens"] / max(baseline["tokens"], 1)
    return gain >= min_gain and cost_ratio <= max_cost_ratio
```

### Developer Challenges

1. Implementing masking and label alignment without leaking documents, answers, or downstream reasoning into the teacher context.
2. Measuring query-level gains with matched retriever snapshots, rollout groups, seeds, compute, and evaluation splits.
3. Detecting group-homogeneous outcomes and preventing a degenerate auxiliary loss from suppressing useful exploration.

### Author Challenges

1. Extend the method beyond gold-answer tasks with calibrated, auditable outcome or preference signals.
2. Establish whether the method remains useful when all-success and all-failure groups are common at larger model scales.
3. Release a version-pinned implementation and data/configuration manifest that enables independent reproduction of the reported tables and cost claims.

## Validation Notes

- Required source integrity gate passed before review; initial partial state was repaired and re-verified.
- Cache methodology was local-first, `missing-only`, and central-cache based; final status was `cached` with PDF, HTML, and source text present.
- Dedup/reselection validation found no prior marker and required no reselection.
- No source files, caches, extracted text, local paths, usernames, machine names, exact execution timestamps, or local timezone labels are included in this public artifact.
- No training, benchmark rerun, official-code execution, or independent reproduction was claimed.

## Source References

| ID | Reference | Supports | Access date | Notes |
|---|---|---|---|---|
| S1 | https://arxiv.org/abs/2605.18299 | Identity, authors, date, subjects, DOI, abstract, license link | 2026-08-01 | Canonical metadata record |
| S2 | https://arxiv.org/html/2605.18299 | Full method, experiments, tables, limitations, conclusion, appendices | 2026-08-01 | Official full-paper HTML |
| S3 | https://arxiv.org/pdf/2605.18299 | PDF integrity and text cross-check | 2026-08-01 | Source file withheld locally |
| S4 | https://arxiv.org/e-print/2605.18299 | TeX/source structure, equations, tables, appendices | 2026-08-01 | Source archive withheld locally |
| S5 | https://doi.org/10.48550/arXiv.2605.18299 | Persistent identifier | 2026-08-01 | arXiv-issued DOI |
| S6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260727-Token%20Tax%20RAG/2606.20898-whitepaper-review.md | Retrieval/evidence-budget context | 2026-08-01 | Related DEP, not primary evidence for SD-Search |
| S7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260725-DASD%20Reasoning/dasd_reasoning_manuscript.md | Distillation and rollout-mismatch context | 2026-08-01 | Related DEP, not primary evidence for SD-Search |
| S8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md | RL objective and stability context | 2026-08-01 | Related DEP, not primary evidence for SD-Search |

## Attribution Block

- Source URL: https://arxiv.org/abs/2605.18299
  - Applies to: all source identity and metadata fields.
- Source URL: https://arxiv.org/html/2605.18299
  - Applies to: method, experiments, limitations, and conclusion sections.
- Source URL: https://arxiv.org/pdf/2605.18299
  - Applies to: PDF integrity and text cross-checks.
- Source URL: https://arxiv.org/e-print/2605.18299
  - Applies to: equations, tables, appendices, and source structure.
- Source URL: https://doi.org/10.48550/arXiv.2605.18299
  - Applies to: persistent identity.
- Source files: verified local PDF, full-paper HTML, metadata HTML, source package, extracted text, and cache.
  - Applies to: source-first review only; all source files were withheld and none were uploaded.
