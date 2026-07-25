# Report-Mark: DASD Reasoning

## Source Metadata

- **Paper:** *Distribution-Aligned Sequence Distillation for Superior Long-CoT Reasoning*.
- **Authors:** Shaotian Yan; Kaiyuan Liu; Chen Shen; Bing Wang; Sinan Fan; Jun Zhang; Yue Wu; Zheng Wang; Jieping Ye.
- **Canonical record:** https://arxiv.org/abs/2601.09088.
- **Full paper:** https://arxiv.org/pdf/2601.09088 and https://arxiv.org/html/2601.09088.
- **Stable identifiers:** arXiv:2601.09088; https://doi.org/10.48550/arXiv.2601.09088.
- **Source date:** submitted 2026-01-14; inspected version arXiv v1.
- **Official implementation and release:** https://github.com/D2I-ai/dasd-thinking and https://huggingface.co/collections/Alibaba-Apsara/dasd-thinking.
- **Source integrity:** initial local state partial; bounded repair produced a complete PDF, full-paper HTML, metadata HTML, and TeX source bundle before synthesis.
- **Distribution:** generated Markdown and public URLs only. All source files, extracted text, cache materials, and rendered pages are withheld locally.

## Concise Research Notes

The paper presents Distribution-Aligned Sequence Distillation (DASD) for long chain-of-thought reasoning. It frames standard supervised fine-tuning on teacher responses as a weak approximation to the teacher's sequence-level distribution and proposes three linked interventions: temperature-scheduled learning, divergence-aware sampling, and mixed-policy distillation.

The dense DASD-4B-Thinking model uses Qwen3-4B-Instruct-2507 as the student and gpt-oss-120b as the teacher. The reported pipeline begins with lower-temperature trajectories for stable learning, moves to higher-temperature trajectories for broader response coverage, prioritizes high teacher-student divergence at the sentence level, and then uses student prefixes plus teacher rewrites to reduce teacher-forcing mismatch.

The primary table reports DASD-4B-Thinking at 88.5 AIME24, 83.3 AIME25, 69.3 LiveCodeBench v5, 67.5 LiveCodeBench v6, and 68.4 GPQA-D. The authors attribute these values to a 448K-sample training set and state that the model/data/code are released. These are source-reported results: no training run, benchmark execution, or independent replication occurred here.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Assessment |
|---|---|---|---|
| E1 | Canonical arXiv record and DOI | title, authors, submitted date, abstract, and public locators | high-confidence identity; abstract not used as full-paper result evidence |
| E2 | Verified PDF, full-paper HTML, and TeX source | method, experiments, tables, conclusion, and references | high for source transcription; no independent reproduction |
| E3 | Rendered PDF pages covering title/abstract, method, evaluation setup, Table 6, and references | visual table/figure legibility, release links, and reported values | high for visual cross-check; font substitutions did not change the displayed numeric table |
| E4 | Official DASD GitHub repository | code tree, training materials, release notes, and stated model/data links | medium-high; repository contents were read but not run |
| E5 | Official DASD Hugging Face collection | published model/data collection entries and release linkage | medium; collection presence is not a replication result |
| E6 | WorkflowLLM, MOSS, and Shuffled Autoregression DEP-E manuscripts | related synthesis about LLM orchestration, context-bearing agents, and autoregressive error control | contextual only; no joint experiment |
| E7 | Public-safe workflow records | random selection, dedup, repair, cache, and source gate | process evidence only |

## Related DEP Entries

1. [WorkflowLLM Enhancing - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260724-WorkflowLLM%20Enhancing/workflowllm_enhancing_manuscript.md)
   - **Source basis:** inspected its source metadata and evidence ledger for arXiv:2411.05451.
   - **Relevance:** both consider how LLM capability is organized into multi-stage workflows; DASD supplies a training-time curriculum while WorkflowLLM addresses orchestration of downstream workflow capability.
2. [MOSS Enabling Code-Driven - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260724-MOSS%20Enabling%20Code-Driven/moss_enabling_code_driven_manuscript.md)
   - **Source basis:** inspected its source metadata and evidence ledger for arXiv:2409.16120.
   - **Relevance:** DASD's conclusion names agentic retrieval and tool use as a future direction; MOSS supplies a concrete context-management and code-driven agent framing for testing that extension.
3. [Shuffled Autoregression - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260724-Shuffled%20Autoregress/shuffled_autoregression_manuscript.md)
   - **Source basis:** inspected its complete-method evidence ledger for arXiv:2306.06367v1.
   - **Relevance:** both address train/inference sequence mismatch and error accumulation with an explicit generation procedure, though one is language distillation and the other motion interpolation.

## Synthesis Note

### Concept Bridge

All four artifacts treat staged computation as a control surface rather than a neutral implementation detail. DASD changes the evidence distribution and student/teacher interaction during training; WorkflowLLM and MOSS manage sequence context and task execution at application time; Shuffled Autoregression alters dependency order to curb rollout error. A shared engineering principle is to make stage boundaries, state provenance, and correction triggers observable and testable.

### Potential Implementations

1. **Curriculum evidence ledger:** record temperature, filter decision, teacher revision, and student checkpoint for every synthetic reasoning trace.
2. **Prefix-repair evaluator:** use synthetic tasks to measure whether teacher rewrites of student prefixes improve completion correctness without hiding regressions in answer length or refusal behavior.
3. **Agent handoff controller:** connect a trained reasoning model to workflow tools only after context, provenance, uncertainty, and authorization checks pass.

### Deeper Relationship Observations

1. DASD and Shuffled Autoregression both target a distribution shift between a teacher-forced training history and self-generated inference history, but they intervene through data revision versus dependency topology.
2. DASD's diversity/stability tradeoff resembles WorkflowLLM and MOSS's need to preserve rich context while constraining the execution state that drives a particular action.
3. The releases make implementation possible, yet all three LLM-related entries retain the same review boundary: source availability does not establish benchmark parity, robust transfer, or production readiness.

### Conceptual Similarities

1. Each selected entry models a multi-stage process whose later state depends on explicitly documented earlier state.
2. Each needs an auditable distinction between a source-supported mechanism and an unreplicated performance claim.
3. Each benefits from a fail-closed validation layer that rejects missing provenance, invalid dependency state, or unbounded external action.

### MVP Implementations With Code Mock-ups

1. **Trace Provenance Card**

```python
def trace_card(trace_id, temperature, teacher_revision, filter_passed):
    return {"trace": trace_id, "temperature": temperature,
            "teacher_revision": teacher_revision, "eligible": bool(filter_passed)}
```

This toy record keeps provenance separate from model output and contains no training data.

2. **Safe Prefix-Repair Gate**

```python
def allow_prefix_repair(prefix_ok, teacher_allowed, synthetic_task):
    return bool(prefix_ok and teacher_allowed and synthetic_task)
```

The gate permits only authorized synthetic evaluation and does not call a model or tool.

3. **Rollout Boundary Check**

```python
def rollout_receipt(step, known_state, confidence):
    return {"step": step, "continue": known_state and confidence >= 0.8}
```

The receipt expresses a review threshold; production calibration and human oversight remain required.

### Developer Challenges

1. Reproducing the paper requires version-pinned models, teacher access, data filters, training configuration, benchmark snapshots, and sufficient compute, not merely a public repository.
2. A mixed-policy implementation must prevent leakage between teacher completions, student prefixes, evaluation data, and final benchmark reports.
3. Any agent extension needs strict tool authorization, context isolation, model-version tracing, and safe rollback rather than treating improved reasoning scores as permission to act.

### Author Challenges

1. Publish a paper-exact manifest covering sample provenance, data filtering, temperature schedule, model revisions, training commands, and benchmark evaluator versions.
2. Report repeated-seed uncertainty, contamination controls, and matched-compute baselines for each ablation rather than only point estimates.
3. Document the boundary conditions of mixed-policy distillation, especially prefix length, quality filtering, teacher drift, safety filtering, and degradation cases.

## Validation Notes

- Random selection: 75,780 PDFs collapsed to 75,777 parent-paper units; zero-based index 56,517; first draw accepted; 0 duplicate exclusions and 0 reselections.
- Dedup: arXiv ID, DOI, normalized title, slug, Black Lake artifacts, Black-Lake-Data entries, automation memory, and preceding-24-hour markers showed no owning duplicate.
- Source integrity: the initial PDF-only unit was repaired before review. The PDF passed size/header/EOF checks; full-paper HTML passed size, body, marker, heading, and structure checks; no partials remained.
- Review coverage: complete HTML and TeX structure, representative rendered PDF pages, benchmark tables, official code release, and official model/data collection were inspected. No code or experiment was executed.
- Public safety and upload gate: no local absolute path, username, machine identifier, exact local timestamp, source file, extracted text, cache, or review render is present. No source document was staged, uploaded, attached, or deposited.

## Attribution Block

- Source URL: https://arxiv.org/abs/2601.09088
  - Applies to: this report and the DEP-E manuscript.
  - Notes: canonical identity, authors, date, and public source locators.
- Source URL: https://arxiv.org/pdf/2601.09088
  - Applies to: method, table, and visual cross-checking.
  - Notes: verified private copy inspected; source file withheld.
- Source URL: https://arxiv.org/html/2601.09088
  - Applies to: full-paper structure, method, experiments, and conclusion.
  - Notes: verified private copy inspected; source file withheld.
- Source URL: https://github.com/D2I-ai/dasd-thinking
  - Applies to: implementation and release availability context.
  - Notes: official repository inspected statically; code was not executed.
- Source URL: https://huggingface.co/collections/Alibaba-Apsara/dasd-thinking
  - Applies to: model and data release context.
  - Notes: public collection inspected; no model or dataset file was downloaded.
- Source files: PDF, full-paper HTML, metadata HTML, TeX archive, cache, extracted text, repair record, and rendered pages.
  - Applies to: all generated artifacts.
  - Notes: withheld locally; zero source-document uploads.
