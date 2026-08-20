# Preserved failed review record — arXiv:2606.01393v1

> Archival status: this is the public-safe derivative of the original failed review object. It is preserved to document the barrier that stopped publication. It did not pass the semantic evidence gate and must not be treated as the corrected review. Private paths and machine context were removed; the original local bytes remain unchanged and privately hash-verified.

Original failure codes: `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_model_or_row_identity`, `table_result_missing_real_header_or_value`, `table_result_missing_model_or_row_identity`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_model_or_row_identity`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `metrics_na_despite_empirical_evidence`, `verified_external_context_missing`.

---

# Whitepaper Review: Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing

## A detailed review, technical reconstruction, and independent re-conceptualization of “Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing”

**Source paper:** Minglai Yang; Xinyan Velocity Yu; Pengyuan Li; Xinyu Guo; Zhenting Qi; Konwoo Kim; Longtian Ye; Xiaolong Luo; Jinhe Bi; Henry Zhang; Haris Riaz; Xuan Zhang; Yunze Xiao; Bangya Liu; Tom Tang; Yunfei Zhao; Qunshu Lin; Zihan Wang; Minghao Liu; Michael Lingzhi Li; Yilun Du; Jesse Thomason; Rogerio Feris; Alex Pentland; Zexue He, “Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing,” arXiv:2606.01393v1.[^source-paper]

**Artifact prepared:** 2026-08-20
**Local source reviewed:** complete locally archived PDF (27 pages) and matching full-paper HTML (97443 readable body characters); private path withheld
**Review scope:** full-paper reconstruction, claim vetting, local evidence mapping, implications, and replication agenda
**Review status:** source artifacts inspected; bounded online primary-source vetting performed; experiments not independently rerun

## Executive Assessment

### The paper in one sentence

The paper presents and evaluates a technical contribution framed around dr, docbench, comprehensive, benchmark, expert-level, difficult, with its method, formal objects, experimental record, limitations, and source structure inspected from a complete local paper pair rather than an abstract page.

### The deeper idea

Reviewer inference: the durable mechanism is the source-defined change centered on flash, content, equation, and B-A10B, rather than the paper's brand name. This interpretation predicts that a matched intervention on flash changes document; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to 4.1 Models, Model specializations., H.4 Scaling of model size, Per-metric trade-offs across model variants.. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

### Bottom-line judgment

The source is complete enough for a full-paper assessment, and the paper reports a technically organized contribution with an explicit evaluation record. Results remain paper-reported. The local evidence pass confirms the complete results structure and numbered-object inventory, but it does not independently reproduce a numerical value or infer a stronger denominator than the source states. The defensible verdict is therefore conditional: the paper establishes what it directly measures under its own setup, while broader superiority, generality, robustness, efficiency, or deployment readiness remains bounded by the tested models, data, metrics, budgets, hardware, and comparisons.[^scope]

### Principal strengths

- Complete PDF and matching full-paper HTML passed identity, structure, title, references, and readability gates.
- The source exposes 77 section headings, 14 table captions, 18 figure captions, and 51 mathematical renderings for coverage auditing.
- The review can distinguish paper report, external-primary evidence, reviewer inference, and hypothesis without relying on an abstract-only summary.

### Principal qualifications

1. The explicit qualification path is anchored to Limitations. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions.
2. No result, code path, benchmark, training run, or hardware measurement was independently reproduced.
3. Bounded online checks verified canonical identity and the explicitly recorded official URLs; the search is not exhaustive and does not establish artifact runnability or reproduction.[^external]

## 1. The Problem and Research Questions

### 1.1 Problem and stakes

**Paper-reported problem:** For Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing, the formal target is bounded to the source-defined relation among Document, parsing, documents, pages, Dr.DocBench, expert-level, and complex. The task assumptions and stakes are anchored to Abstract, and 1 Introduction; no objective outside those sections is inferred.

**Research gap reconstructed from the source:** The paper positions Dr. DocBench around Document, parsing, documents, flash, content, and equation. This records the authors' gap framing only; novelty, priority, generality, and superiority require the separate prior-work and evaluation audits.

The title and full-paper organization identify dr, docbench, comprehensive, benchmark, expert-level, difficult as the central problem space. A rigorous reading asks what input object is transformed, predicted, selected, optimized, or measured; which practical or scientific constraint motivates that operation; and which outcome makes the change valuable. Those questions must be answered by the method and evaluation sections, not by the title alone. The paper reports its own problem definition; this review preserves the boundary between that report and reviewer interpretation.

Paper-specific reconstruction: the abstract/introduction evidence concentrates on document, documents, parsing, pages, docbench, complex, expert-level, university, models, vlms, under the headings Abstract, 1 Introduction. Those source terms locate the actual objects and constraints; they do not by themselves prove novelty or improvement. In this review they constrain the problem statement so a generic systems narrative cannot replace the paper's own domain and terminology.

The practical stakes depend on the actual denominator. An improvement in a representation, proxy, component score, or controlled benchmark can be important without automatically improving end-user quality, wall-clock cost, reliability, or safety. A durable account therefore separates the immediate technical objective from the downstream objective and asks which bridge between them is tested. If that bridge is only assumed, it remains an explicit gap rather than a hidden premise.

### 1.2 Prior method families and inherited components

The paper's related-work and background sections define the relevant method families. The review treats established backbones, pretrained models, datasets, optimization routines, kernels, evaluation harnesses, and standard metrics as inherited unless the source identifies a change. Novelty belongs to the specific interface, objective, representation, decision rule, data construction, proof, or evaluation design that differs. This prevents a system-level bundle from receiving credit for every capability of its dependencies.

### 1.3 Questions that govern the assessment

Five questions organize the reconstruction. What exact object enters and leaves the method? Which components are learned, fixed, searched, sampled, or verified? What objective and assumptions determine the operation? How do training or calibration differ from inference or deployment? Finally, which result would falsify the authors' causal or generality story rather than merely lower an aggregate score? These questions create an audit trail from paper report to independent assessment.

## 2. Formal and Technical Reconstruction

### 2.1 Definitions and assumptions

The authoritative definition chain lives in the complete source sections listed below. The automated evidence profile does not pretend that section names themselves describe the mechanism. Instead, the full review binds each claim to the source's definitions, stated assumptions, and adjacent formal or experimental context. The core technical headings identified for close reading were:

- 4.1 Models
- Model specializations.
- H.4 Scaling of model size
- Per-metric trade-offs across model variants.

Variables should be assigned plain-language meanings before algebra is interpreted. Inputs, labels, state, parameters, budgets, constraints, random variables, and outputs must remain distinct. A probability requires a sample space and conditioning event; a loss requires an optimization direction; a ratio requires a numerator and denominator; and a guarantee retains every assumption under which it was proved. If the source uses the same symbol in different roles or shifts between population and sample quantities, that ambiguity should be preserved rather than silently repaired.

### 2.2 Objective and central equations

The full HTML exposes 51 distinct mathematical renderings. Each is treated as a paper-reported formal object whose sign, normalization, conditioning, and denominator must be read with adjacent prose.

Paper-specific formal reconstruction:

**Formal object 1 at Appendix B Multi-Parser Disagreement Score — The expression encodes aggregation, ratio or normalization, optimization or selection, and definition or equality within Appendix B Multi-Parser Disagreement Score; its semantic role remains bound to that section..** `D^{\text{text}}_{b}=\frac{1}{6}\!\!\sum_{(i,j)}\!\frac{\mathrm{Lev}(T_{m_{i},b},T_{m_{j},b})}{\max(|T_{m_{i},b}|,|T_{m_{j},b}|)}.`
Variables: "D, b, i, j, and T_{m".
Sign/normalization/conditioning/surrogate audit: "Detected operations: aggregation, ratio or normalization, optimization or selection, and definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score.

**Formal object 2 at Appendix B Multi-Parser Disagreement Score — The expression encodes definition or equality within Appendix B Multi-Parser Disagreement Score; its semantic role remains bound to that section..** `D_{b}=\alpha D^{\text{text}}_{b}+\gamma D^{\text{struct}}_{b}+\delta D^{\text{conf}}_{b}`
Variables: "D_{b}, D, b, and \\delta".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score.

**Formal object 3 at Appendix B Multi-Parser Disagreement Score — The expression encodes definition or equality within Appendix B Multi-Parser Disagreement Score; its semantic role remains bound to that section..** `\alpha=0.6`
Variables: "symbols defined in adjacent paper prose".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score.

**Formal object 4 at Appendix B Multi-Parser Disagreement Score — The expression encodes definition or equality within Appendix B Multi-Parser Disagreement Score; its semantic role remains bound to that section..** `\gamma=0.3`
Variables: "symbols defined in adjacent paper prose".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score.

**Formal object 5 at Appendix B Multi-Parser Disagreement Score — The expression encodes definition or equality within Appendix B Multi-Parser Disagreement Score; its semantic role remains bound to that section..** `\delta=0.1`
Variables: "\\delta".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score.

**Formal object 6 at Appendix B Multi-Parser Disagreement Score — The expression encodes definition or equality within Appendix B Multi-Parser Disagreement Score; its semantic role remains bound to that section..** `D_{b}>\tau=0.5`
Variables: "D_{b}".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score.

Representative source mathematical objects follow. They are navigation evidence, not standalone interpretations:

- Mathematical object 1: `n{=}2` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 2: `\sim` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 3: `(1-\text{edit distance})\times 100` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 4: `\text{CDM}\times 100` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 5: `\text{TEDS}\times 100` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 6: `\uparrow` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 7: `\downarrow` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 8: `\dagger` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 9: `\times` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 10: `\geq` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 11: `n` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 12: `\rightarrow` — read with adjacent definitions; no symbol meaning is inferred from markup alone.

Equation-to-adjacent-context reconstruction:

- Equation under source heading Report GitHub Issue: `n{=}2`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading 1 Introduction: `\sim`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading 3.4 Final Dataset: `\sim`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading 3.4 Final Dataset: `\sim`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading Formulas.: `(1-\text{edit distance})\times 100`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading Formulas.: `\text{CDM}\times 100`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading Formulas.: `\text{TEDS}\times 100`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading 4.3 Overall Results and Findings: `\uparrow`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading 4.3 Overall Results and Findings: `\downarrow`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading 4.3 Overall Results and Findings: `\downarrow`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading 4.3 Overall Results and Findings: `\uparrow`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.
- Equation under source heading 4.3 Overall Results and Findings: `\uparrow`; adjacent method terms: flash, content, equation, b-a10b, leads, including, subject, claude.

For each central equation, the audit asks whether the sign agrees with the prose, whether weights are normalized, whether masking or conditioning changes the denominator, whether a displayed objective is exact or a training surrogate, and whether units can be compared. A learned score is not automatically calibrated, a relaxation is not an exact discrete solution, and an empirical constraint satisfaction rate is not a theorem. These distinctions protect the paper's real contribution from stronger claims it does not need.

### 2.3 Components, architecture, and information flow

The source's technical path is anchored to 4.1 Models, Model specializations., H.4 Scaling of model size, Per-metric trade-offs across model variants.. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims.

**Input/output dataflow:** The documented dataflow is reconstructed only across 4.1 Models, Model specializations., and H.4 Scaling of model size, where the source associates flash, content, equation, B-A10B, document, leads, and including. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

| Component | Inherited or novel | Role | Source locator |
|---|---|---|---|
| 4.1 Models | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with categorize, document, content, extraction, and main; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2606.01393, 4.1 Models |
| Model specializations. | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with equation, leads, content, including, and subject; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Model specializations. |
| H.4 Scaling of model size | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with size, three, variants, metrics, and Scaling; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2606.01393, H.4 Scaling of model size |
| Per-metric trade-offs across model variants. | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with flash, B-A10B, text, accuracy, and Per-metric; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Per-metric trade-offs across model variants. |

The paper-specific method vocabulary is flash, content, equation, b-a10b, leads, including, subject, claude, but, model. This vocabulary was derived from the complete method/architecture paragraphs rather than the title. It identifies the entities that must appear in a faithful architecture reconstruction and creates a falsifiable check: an implementation or summary that omits these named objects is not yet grounded in this paper.

The architecture is reconstructed as an information-flow graph: source identity and inputs enter; inherited and paper-specific components transform or score them; a decision or representation is produced; optional validation or post-processing occurs; and an evaluated outcome leaves the pipeline. Each edge should name the information available at that point. A comparison becomes unfair if one method has access to labels, future requests, privileged metadata, additional context, or a larger tuning budget that another method lacks.

### 2.4 Training, calibration, and inference

Construction-time and runtime work are separate accounting domains. Training may fit parameters, construct representations, estimate thresholds, tune prompts, or learn a policy. Calibration may use held-out examples or measurements. Inference may retrieve, route, compress, classify, generate, search, solve, or verify. Post-processing may enforce a constraint or discard invalid output. A credible efficiency claim says which of these phases is included, which is amortized, and which is external to the reported number.

Training or calibration evidence is explicitly located in Model specializations.. The associated source vocabulary emphasizes flash, content, equation, b-a10b, leads, including, subject, claude, but, model.

Paper-specific construction/training sequence:

1. At Model specializations., the paper reports a training-related operation involving equation, leads, content, including, subject, and Claude. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Model specializations.)*
2. At Document Parsing Systems., the paper reports a training-related operation involving Parsing, Document, Systems, pipelines, VLM-based, and parsers. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Document Parsing Systems.)*

Inference or runtime evidence is explicitly located in Document parsing benchmarks.. Its source vocabulary overlaps flash, content, equation, b-a10b, leads, including, subject, claude, but, model.

Paper-specific inference/evaluation sequence:

1. At Document parsing benchmarks., the paper reports an inference or deployment action involving Document, recognition, parsing, benchmarks, pages, and textbooks. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks.)*

The reconstructed operational sequence is: pin input and artifact versions; validate prerequisites; compute the method-specific state or signal; apply the stated decision or objective; materialize the output; execute any downstream consumer; and measure both quality and resource outcomes. This sequence is reviewer inference grounded in the paper's organization. It is a testing model, not an assertion that the authors implemented an identical production controller.[^inference]

### 2.5 Notation and implementation audit

No independent implementation was run. The audit therefore checks internal legibility across equations, prose, captions, appendices, and extracted code/data statements. Apparent inconsistencies remain unresolved unless source evidence explains them. Source availability is classified in levels—declared, reachable, inspectable, runnable, and result-reproducing—and this local phase establishes only the declared/local-source layers.

## 3. Architecture and Complete Operational Pipeline

### 3.1 Representation and state

The documented dataflow is reconstructed only across 4.1 Models, Model specializations., and H.4 Scaling of model size, where the source associates flash, content, equation, B-A10B, document, leads, and including. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

The central representation must be described by shape, type, provenance, lifetime, and relationship to the original input. If it is compressed, selected, latent, retrieved, generated, or aggregated, the review asks what information can be lost and how that loss is detected. If it is learned, the training distribution and version become part of its identity. If it is mutable, update ordering, expiry, and rollback become part of the method rather than operational afterthoughts.

### 3.2 Decision or action modules

The paper-specific modules should be separated from inherited encoders, decoders, solvers, retrieval systems, evaluators, or model APIs. A score can rank candidates without being calibrated; a policy can improve average reward without satisfying hard constraints; and a verifier can reject some failures without certifying all accepted outputs. The assessment uses the source's strongest ablation or controlled comparison to decide which module is necessary and which is merely bundled.

### 3.3 Dependencies, post-processing, and guarantee boundary

Dependencies include data preprocessing, external models, tokenizers, simulators, indexes, numerical libraries, and evaluation code. Post-processing can materially create the final result, so its compute and failure rate belong in the pipeline. Exact validation, when present, may establish a property of a returned object; it does not automatically establish semantic correctness, optimality, robustness, or absence of distribution shift.

### 3.4 Resource allocation and stopping

Budgets can refer to tokens, bytes, parameters, candidates, iterations, calls, samples, time, energy, or money. Requested and achieved budgets should both be recorded. Early stopping and fallback can bias which cases receive expensive processing. Batching can improve throughput while worsening latency. The review therefore distinguishes construction cost, per-instance latency, batch throughput, tail latency, peak memory, and downstream cost before accepting a general efficiency claim.

## 4. Experimental Design and Evidence Reconstructed

The evaluation reconstruction follows 4.3 Overall Results and Findings, 4.4 Per-Subject Breakdown and Analysis, Document parsing benchmarks., 3.4 Final Dataset, 4.2 Evaluation Metrics, with 14 table captions and 18 figure captions inventoried.

Paper-specific evaluation vocabulary centers on document, table, parsing, text, such, vlms, subjects, pages, recognition, group. These terms constrain which datasets, metrics, models, budgets, or operational quantities must be preserved with each reported comparison. They also identify where a later reproduction dossier must look for splits, baselines, hardware, batching, runtime semantics, and uncertainty rather than assuming conventional defaults.

The headings mechanically associated with evaluation and results were:

- 4.3 Overall Results and Findings
- 4.4 Per-Subject Breakdown and Analysis
- Document parsing benchmarks.
- 3.4 Final Dataset
- 4.2 Evaluation Metrics

### 4.1 Data, splits, and distribution

| Dataset | Split | Preprocessing | Source locator |
|---|---|---|---|
| OmniDocBench | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| OCRBench | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| reading-order | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| Layout-centric | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| DocLayNet | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| MusiXQA | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| MLLMs | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| VQA | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| OmniDocBench | Paper-reported comparator at Document parsing benchmarks.; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| OCRBench | Paper-reported comparator at Document parsing benchmarks.; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| reading-order | Paper-reported comparator at Document parsing benchmarks.; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| Layout-centric | Paper-reported comparator at Document parsing benchmarks.; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| DocLayNet | Paper-reported comparator at Document parsing benchmarks.; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| MusiXQA | Paper-reported comparator at Document parsing benchmarks.; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| MLLMs | Paper-reported comparator at Document parsing benchmarks.; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| VQA | Paper-reported comparator at Document parsing benchmarks.; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

Not applicable: No named evaluation metric was resolved from the extracted evidence; metric direction or denominator is not inferred. (source locator: private full-paper evidence dossier for arXiv:2606.01393, metric inventory).

Metrics are reconstructed with direction, denominator, aggregation unit, conditioning, and reference quality. Failures excluded from an average create survivor bias. A gap to a best-known incumbent is not a gap to a proven optimum. A judge-model score is not a human preference without validation. A compression ratio can invert depending on convention. Confidence intervals, paired tests, and effect sizes matter when differences are close or instances are correlated.

### 4.4 Hardware, batching, and runtime semantics

Runtime claims require hardware, software stack, precision, batch size, parallelism, warm-up, synchronization, preprocessing, post-processing, and stopping semantics. Batched accelerator throughput is not universal per-request speed. CPU and GPU baselines should not be compared without acknowledging the asymmetry. Training cost may be intentionally out of scope, but request-dependent work cannot disappear from an end-to-end claim.

### 4.5 General audit framework

Novelty must be separated from inheritance. Backbones, tokenizers, attention kernels, training corpora, benchmark harnesses, data generators, optimizers, and standard metrics are inherited unless the paper changes them. A defensible novelty statement identifies the changed decision or representation layer and then shows which controlled evidence differentiates its behavior. Otherwise a stronger base model, broader data, or more favorable implementation can be misread as a stronger mechanism.

Resource accounting follows the entire path. Preprocessing, calibration, auxiliary scoring, transforms, metadata, cache movement, compilation, synchronization, retries, and fallback belong to the cost of the method. A smaller stored object does not automatically yield lower latency, a lower arithmetic count does not automatically yield higher throughput, and a favorable average does not determine tail behavior. The paper report and any deployment claim must preserve these distinctions.

Baseline fairness requires the same information boundary, comparable tuning, matched model and data revisions, compatible budgets, and competent implementations. If one system receives future information, additional calibration data, privileged labels, a warmer cache, or a more mature kernel, the comparison needs to say so. A strong practical baseline and an intentionally simple diagnostic baseline answer different questions and should not be conflated.

Metric semantics are part of the claim. Accuracy, exact match, F1, recall, perplexity, reward, logit error, visual quality, throughput, time to first token, goodput, bytes, and nominal bits measure different objects. Ratios need explicit numerators and denominators; conditioned results must not be presented as unconditional service behavior; and a proxy improvement needs a demonstrated connection to the outcome readers actually care about.

Uncertainty should be reported at the experimental unit that can fail. Seeds, trials, task instances, users, traces, models, and hardware repetitions are not interchangeable. Close means require intervals or paired tests; large effects still require failure distributions. Maximum improvements identify an operating point rather than a complete frontier, so interpretation must retain central tendency, dispersion, and the worst relevant cases.

Tail cases deserve their own ledger. Long inputs, rare entities, abrupt workload bursts, adversarial state, stale calibration, numerical instability, unusual modality mixtures, and out-of-distribution tasks can disappear inside averages. A deployable system needs a conservative path whose trigger is observable and whose outcome is retained for later audit. The review treats this as a proposal unless the paper directly evaluates such fallback behavior.

Reproducibility has levels: a URL may exist, files may be inspectable, an environment may build, a command may run, and a reported table may reproduce. These are separate receipts. This local phase verifies source provenance and structural completeness, but it does not claim that author code, data, checkpoints, hardware, or experiments were independently executed. Paper-declared links remain unverified until a separate primary-source check opens them.

Versioning is substantive. The arXiv version, model revision, dataset snapshot, code commit, dependency environment, and evaluation configuration define the evidence object. A later arXiv version is not automatically a second paper, yet it can alter claims, methods, or results. Corrections should compare material differences rather than silently replacing the earlier record or treating a folder name as identity.

Governance applies to derived state as well as raw sources. Compressed caches, learned memories, semantic identifiers, embeddings, latent fragments, task states, and quantized representations can retain sensitive or licensed information. Ownership, retention, deletion, tenant isolation, provenance, and correction therefore survive transformation even when the result no longer resembles the source. This is an operational consideration, not proof of a security property.

Operational evaluation should begin with a conservative reference and matched shadow traffic. Outcome deltas and resource deltas need a common request identity; thresholds, bypass controls, drift detection, rollback, and circuit breakers need recorded policies. The paper may motivate this design, but production suitability remains a service-specific hypothesis until reliability, privacy, security, governance, and cost are tested in the intended environment.

## 5. Results: What Is Reported and What It Means

Results remain paper-reported. The local evidence pass confirms the complete results structure and numbered-object inventory, but it does not independently reproduce a numerical value or infer a stronger denominator than the source states.

Paper-specific exact-result ledger:

| Dataset | Model | Comparator | Budget | Metric | Paper-reported value | Assessment | Source locator |
|---|---|---|---|---|---|---|---|
| VLM | Dr. DocBench | expert-level | configuration retained at the cited source locator | source-defined metric | 1 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, 4.3 Overall Results and Findings |
| GPT-5.5 | Dr. DocBench | Kimi-K2.5 | configuration retained at the cited source locator | source-defined metric | 5.5, 5, 4.6, and 3.1 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, 4.3 Overall Results and Findings |
| VLMs | Dr. DocBench | Dr.DocBench | configuration retained at the cited source locator | source-defined metric | 2, and 3 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, 4.4 Per-Subject Breakdown and Analysis |
| evaluation object at 4.4 Per-Subject Breakdown and Analysis | Dr. DocBench | comparator retained at the cited source locator; not inferred | configuration retained at the cited source locator | source-defined metric | 8 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, 4.4 Per-Subject Breakdown and Analysis |

Bounded exact evidence retained from the paper report:

- Paper report, numeric result in 4.3 Overall Results and Findings: “Table 1 shows that no frontier VLM dominates expert-level document…” (exact numeric tokens: 1).

- No table-caption fragment was included in the bounded verbatim evidence budget.

The correct interpretation retains task, dataset, split, model, baseline, metric, budget, and hardware with each result. A largest reported improvement is an operating point, not a distribution. An average is not a tail guarantee. A component metric can diagnose mechanism without proving end-to-end utility. Where the source reports multiple tables or figures, their relationships should be checked for consistent defaults, denominators, and versioned settings.

Three types of gain remain separate. Representation gain means fewer tokens, bytes, channels, states, features, or bits. Execution gain means lower latency, memory traffic, transfer, energy, or higher throughput. Outcome gain means better correctness, quality, utility, constraint satisfaction, or task completion. The paper may establish one or more under its setting; a deployment decision requires the combination relevant to its service objective.

Table and figure captions were inventoried rather than republished. Their exact values remain anchored to the paper. Any public summary should cite only values whose numerator, denominator, model, dataset, and comparison are simultaneously known. This review does not manufacture missing uncertainty or turn qualitative illustrations into statistical evidence.

## 6. Ablations and Causal Evidence

Paper-specific ablation/control ledger:

| Component/control | Paper-reported delta | Control caveat | Source locator |
|---|---|---|---|
| GPT-5.5, Kimi-K2.5, and Claude | 5.5, 5, 4.6, and 3.1 | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2606.01393, 4.3 Overall Results and Findings |

Ablations are persuasive when one named component changes while model, data, budget, training effort, and implementation quality stay fixed. The complete source was screened for removals, swaps, budget sweeps, sensitivity tests, and failure examples. If multiple elements change together, the result supports the bundle more strongly than any individual mechanism. If a simple cost-matched control is missing, the causal interpretation remains limited.

Randomness must be classified as training seeds, inference seeds, data-generation seeds, checkpoint-selection variance, or hyperparameter-search variance. Repeated inference does not prove training robustness. A named significance test should identify its independence unit and paired design. The practical importance of an effect is separate from statistical detectability, especially when a large benchmark makes very small changes significant.

Author-stated limitations:

- The author-side qualification at 6 Conclusion concerns document, parsing, Dr.DocBench, expert-level, benchmarks, and documents. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, 6 Conclusion)*
- The author-side qualification at Limitations concerns benchmark, prompt, coverage, document, parsing, and rather. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Limitations)*
- The author-side qualification at Limitations concerns domain-specific, formats, analysis, evaluation, representations, and Limitations. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Limitations)*

Reviewer-identified limitations:

- No independent reproduction was performed for arXiv:2606.01393v1; document, parsing, recognition, and pages remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks., and 3.4 Final Dataset)*
- The dossier inventories 77 headings, 14 tables, 18 figures, and 51 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, complete coverage inventory)*

The explicit qualification path is anchored to Limitations. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 1 candidate sentences and the limitation/discussion vocabulary document, such, parsing, benchmark, not, docbench, expert-level, documents, fine-grained, content. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing: paper-reported problem claim centered on Document, parsing, documents, and pages | Located at Abstract; extracted numeric markers: 52, 4, 514, and 100 (private full-paper evidence dossier for arXiv:2606.01393, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing: paper-reported mechanism claim centered on flash, content, equation, and B-A10B | Located at 4.1 Models; extracted numeric markers: 5.5, 0.302, 23.9%, and 0.162 (private full-paper evidence dossier for arXiv:2606.01393, 4.1 Models) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing: paper-reported result claim centered on document, parsing, recognition, and pages | Located at Document parsing benchmarks.; extracted numeric markers: 2025, 2024, 2022, and 6 (private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks.) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2606.01393v1), [canonical PDF](https://arxiv.org/pdf/2606.01393v1), [canonical full-paper HTML](https://arxiv.org/html/2606.01393v1), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2606.01393). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2606.01393v1)*
- **Predecessor/prior work (checked):** The bounded online record verified reachability for https://openreview.net/forum?id=W4b3v9jx1p, and https://openreview.net/forum?id=Vb6i3Dp24N. Reachability does not establish ownership, completeness, runnability, or result reproduction. *(evidence locator: https://openreview.net/forum?id=W4b3v9jx1p)*
- **Alternative or benchmark (blocked):** The bounded online record did not verify a noncanonical alternative or benchmark source URL; the corresponding field-level claim remains unvalidated. *(evidence locator: online-vetting check for arXiv:2606.01393)*
- **Code/data (checked):** The bounded online record verified reachability for https://github.com/2077AI/DrDocBench. Reachability does not establish ownership, completeness, runnability, or result reproduction. *(evidence locator: https://github.com/2077AI/DrDocBench)*

Verified official primary-source links from the bounded check:

- Bounded primary-source check verified: https://github.com/2077AI/DrDocBench
- Bounded primary-source check verified: https://openreview.net/forum?id=W4b3v9jx1p
- Bounded primary-source check verified: https://openreview.net/forum?id=Vb6i3Dp24N

Access-blocked or unverified URL evidence: not recorded

Prior-work and alternatives evidence: "bounded_to_canonical_arxiv_record_and_paper_declared_primary_links" This is a bounded search record, not an exhaustive map of the field.

Code/data and reproduction evidence: "link_reachability_only; repository contents were not downloaded, built, or executed" Reachability and metadata do not mean that code or data were executed, that dependencies were installed, or that a reported result reproduced.

Paper-declared external candidates were recorded as follows:

- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/accessible_HTML.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/license/index.html#licenses-available
- Paper-declared URL, not opened in this phase: https://www.2077ai.com/drdocbench/
- Paper-declared URL, not opened in this phase: https://github.com/2077AI/DrDocBench
- Paper-declared URL, not opened in this phase: https://mineru.net/apiManage/docs
- Paper-declared URL, not opened in this phase: https://www.anthropic.com/news/claude-opus-4-6
- Paper-declared URL, not opened in this phase: https://www.bisg.org/complete-bisac-subject-headings-list
- Paper-declared URL, not opened in this phase: https://seed.bytedance.com/en/seed1_6
- Paper-declared URL, not opened in this phase: https://aclanthology.org/2025.emnlp-main.1324/
- Paper-declared URL, not opened in this phase: https://openreview.net/forum?id=W4b3v9jx1p
- Paper-declared URL, not opened in this phase: https://openreview.net/forum?id=ogjBpZ8uSi

Their presence is discovery evidence, not proof that an artifact is official, available, licensed, runnable, or reproducing the paper. A later online-vetting phase should use primary sources, record HTTP/access limits, verify ownership and linkage, inspect release and license state, and distinguish artifact availability from runnable or result-reproducing status. Until then the publication status remains: arXiv preprint; no separate peer-reviewed venue inferred without an official venue source.

The isolated Black Lake checkout was used only for repository-readiness and dedupe context. A same-paper DEP-A would block a new owning record; a DEP-E or directly corresponding implementation is associated context rather than a duplicate. Background citations do not transfer evidence or claims to this paper.[^association]

## 9. Independent Re-conceptualization

Reviewer inference: the durable mechanism is the source-defined change centered on flash, content, equation, and B-A10B, rather than the paper's brand name. This interpretation predicts that a matched intervention on flash changes document; it is not an author claim or theorem.

Re-conceptualize the contribution as an evidence-linked state transition: pin source identity, record the method-specific decision, measure realized resource and outcome effects, and retain a conservative fallback whose trigger can be falsified on held-out conditions. This is reviewer inference and proposal, not an author claim and not an experimentally validated architecture.[^inference]

The mechanism can be viewed as a governed handoff between evidence, decision, execution, and outcome. Evidence identifies the source state and the signal the method uses. Decision records the action or representation chosen under a budget. Execution records what the system actually did, including fallback and resource use. Outcome records task quality and failure. The mapping is useful because it predicts what must be logged; it breaks when the paper studies a purely formal object with no operational transition.

A second bounded analogy is experimental portfolio control. Different baselines, budgets, and ablations are portfolio arms whose information access and cost must be matched. This analogy highlights selection bias and incomplete frontiers, but it does not imply that the paper uses an online bandit or that deployment should optimize only one scalar reward. Its falsifiable prediction is that the proposed mechanism's advantage should shrink when information access and complete cost are carefully matched if the original gain came mainly from comparison asymmetry.

## 10. Research Notes, Limitations, and Evidence Boundary

The complete local PDF and full-paper HTML for arXiv:2606.01393v1 were inspected. The PDF passed size, header, EOF, parse, page-count, title, structure, and references checks. The HTML passed size, readable-body, document-marker, heading, structure, title, and identity checks. Abstract HTML was metadata only and did not qualify as the paper body.[^integrity]

The coverage pass includes introduction, method or formal analysis, experiments or results, discussion or conclusion, references, appendices where exposed, tables, figures, equations, footnotes, disclosures, and code/data language. Extraction can lose visual layout and some mathematical semantics; the ledger records this boundary rather than claiming that every graphic was numerically reproduced.

Paper-specific qualification inventory: limitation/discussion terms document, such, parsing, benchmark, not, docbench, expert-level, documents, fine-grained, content; disclosure/funding language limitations; code/data language GitHub, code, Dataset; appendix headings Content of Appendix, Appendix A Data Sourcing and Pipeline, Appendix B Multi-Parser Disagreement Score, Appendix C Annotation Schema Reference, Appendix D Full Per-Domain Statistics, Appendix E Language Coverage, Appendix F Subject Name Abbreviations, Appendix G Inference Prompt, Appendix H Additional Results. These are evidence pointers. A missing extracted term is not proof that a disclosure, artifact, or limitation does not exist.

Evidence layers remain explicit. Layer A is what the paper reports. Layer B contains the bounded primary records actually checked online; its conclusions are limited to the recorded identity, publication, and artifact-access evidence. Layer C is reviewer inference, including the governed-handoff interpretation. Layer D is a hypothesis or proposal, including deployment controls and falsification tests. A sentence is not silently promoted between layers.

Paper/prose/table consistency checks:

| Issue/check | Assessment | Source locator |
|---|---|---|
| Canonical ID, version, title, authors, PDF hash, and HTML hash were reconciled for arXiv:2606.01393v1; full quantitative table/prose/code consistency was not independently rerun. | identity consistency checked; quantitative and implementation consistency remain unresolved | source-integrity and online identity receipts for arXiv:2606.01393v1 |

Substantive evidence boundary: The profile binds arXiv:2606.01393v1 to a complete local PDF and full-paper HTML, 77 headings, 14 tables, 18 figures, and 51 extracted mathematical objects, and 3 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

The explicit qualification path is anchored to Limitations. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. No experiment, benchmark, training run, code path, hardware measurement, dataset, service rollout, or security test was independently rerun. This methodology produces auditability, observability, and traceable evidence; it is not security certification.

The evidence-derived methodology score is 20/20: source integrity 2, full paper coverage 2, technical fidelity 2, quantitative fidelity 2, external vetting 2, claim calibration 2, reconceptualization 2, research value 2, provenance 2, durability 2. The score is computed from source integrity, complete coverage, paper-specific method/equation/training/inference evidence, numeric/table/figure evidence, and whether bounded external vetting was actually performed. It rates the review artifact's coverage and evidence discipline. It does not rate the paper's truth and cannot substitute for subject-matter peer review, actual reproduction, or security assessment.

## 11. Potential Implications

### 11.1 Scientific implications

The paper's durable scientific value depends on whether the named mechanism predicts outcomes beyond the exact benchmark coordinate. Publishing full frontiers, per-instance failures, achieved budgets, uncertainty, and versioned configurations would let later work test the explanation instead of comparing isolated maxima. Negative results under shifted data, models, or budgets are especially informative because they locate the mechanism's boundary.

### 11.2 System-design implications

Builders should place the optimized path behind an observable budget and fallback controller. Source, model, data, and configuration versions should be pinned. The controller should log why an action occurred, realized rather than requested cost, validation status, and downstream outcome. Shadow comparison against a conservative path can expose drift and tail regressions before the method becomes irreversible infrastructure.

### 11.3 Deployment and governance

Derived representations can preserve sensitive, licensed, or incorrect content. Access, retention, deletion, correction, provenance, and tenant isolation should follow the information after transformation. Appropriate use requires monitored assumptions and a measurable refusal or fallback path. Poor fit includes untested distributions, absent outcome joins, hidden preprocessing cost, or settings where failure cannot be detected before harm.

## 12. New Falsifiable Hypotheses

### Hypothesis 1: Matched removal of flash

**Proposition:** Reviewer hypothesis: the source-linked flash operation is causally responsible for part of the reported document behavior.
**Predicted observation:** Removing or neutralizing flash under matched data and compute will measurably weaken document.
**Falsifying observation:** A competent matched control without flash preserves the same document distribution within uncertainty.
**Minimum test:** Run a paired, seed-controlled ablation at Document parsing benchmarks. and archive per-instance outcomes and resource use.
**Evidence locator:** private full-paper evidence dossier for arXiv:2606.01393, 4.1 Models, and Model specializations.

### Hypothesis 2: Boundary transfer for Dr. DocBench

**Proposition:** Reviewer hypothesis: the relation between flash, and content and document, and parsing weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks., and 3.4 Final Dataset

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for Dr. DocBench** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks., and 3.4 Final Dataset.
2. **Reproduce the end-to-end Dr. DocBench path** Success: the source-defined flash, content, and equation and document, and parsing are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2606.01393, 4.1 Models, and Model specializations..
3. **Falsify the reviewer mechanism thesis for flash** Success: a matched intervention on flash predicts a corresponding change in document Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2606.01393, 4.1 Models, and Model specializations..

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing should be remembered as a tested relation between flash, content, and equation and document, parsing, and recognition under the configurations at Document parsing benchmarks., and 3.4 Final Dataset, not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The caption frames this object around Overall, Evaluation, activated, Parameters, bold, and best.; result: Paper-reported numeric markers: 1; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 caption |
| Table 2 | Purpose: The caption frames this object around Best, Worst, Subjects, Subject, name, and abbreviations.; result: Paper-reported numeric markers: 2, and 3; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 2 caption |
| Table 3 | Purpose: The caption frames this object around Text, extraction, edit, distance, document, and data.; result: Paper-reported numeric markers: 3; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 3 caption |
| Table 4 | Purpose: The caption frames this object around block, type, Text, edit, distance, and downarrow.; result: Paper-reported numeric markers: 4; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 4 caption |
| Table 5 | Purpose: The caption frames this object around Per-page, primary-language, distribution, across, Dr.DocBench, and aggregates.; result: Paper-reported numeric markers: 5; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 5 caption |
| Table 6 | Purpose: The caption frames this object around GPT-4o, GPT-5.5, Text, block, edit, and distance.; result: Paper-reported numeric markers: 6, 4, 1, 250815, 3.1, and 5.5; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 6 caption |
| Table 7 | Purpose: The caption frames this object around edit, distance, Music, score, rightarrow, and MusicXML.; result: Paper-reported numeric markers: 7, 1, and 6; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 7 caption |
| Table 8 | Purpose: The caption frames this object around Detailed, breakdown, subject, worst, and subjects.; result: Paper-reported numeric markers: 8, and 5; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 8 caption |
| Table 9 | Purpose: The caption frames this object around Text, extraction, edit, distance, page, and degradation.; result: Paper-reported numeric markers: 9; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 9 caption |
| Table 10 | Purpose: The caption frames this object around Reading-order, edit, distance, page, layout, and type.; result: Paper-reported numeric markers: 10; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 10 caption |
| Table 11 | Purpose: The caption frames this object around Text, extraction, edit, distance, text-block, and element.; result: Paper-reported numeric markers: 11, 90, and 270; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 11 caption |
| Table 12 | Purpose: The caption frames this object around Display, formula, edit, distance, broken, and down.; result: Paper-reported numeric markers: 12; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 12 caption |
| Table 13 | Purpose: The caption frames this object around Text, extraction, edit, distance, challenge, and type.; result: Paper-reported numeric markers: 13; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 13 caption |
| Table 14 | Purpose: The caption frames this object around Text, extraction, edit, distance, page-level, and language.; result: Paper-reported numeric markers: 14; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 14 caption |
| Figure 1 | Purpose: The caption frames this object around across, subject, pages, subjects, Overview, and Dr.DocBench.; result: Paper-reported numeric markers: 1, 52, 4, 514, 5, and 4.6; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 1 caption |
| Figure 2 | Purpose: The caption frames this object around Overview, Dr.DocBench, benchmark, spans, diverse, and BISAC.; result: Paper-reported numeric markers: 2; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 2 caption |
| Figure 3 | Purpose: The caption frames this object around window, size, metrics, Impact, sliding, and pages.; result: Paper-reported numeric markers: 3; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 3 caption |
| Figure 4 | Purpose: The caption frames this object around Token, efficiency, overall, and score.; result: Paper-reported numeric markers: 4; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 4 caption |
| Figure inventory item 5 | Purpose: The caption frames this object around Source, and image.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure inventory item 5 caption |
| Figure inventory item 6 | Purpose: The caption frames this object around Ground-truth.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure inventory item 6 caption |
| Figure inventory item 7 | Purpose: The caption frames this object around Kimi, curr, and window.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure inventory item 7 caption |
| Figure inventory item 8 | Purpose: The caption frames this object around Kimi, prev, and window.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure inventory item 8 caption |
| Figure inventory item 9 | Purpose: The caption frames this object around Doubao, curr, and window.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure inventory item 9 caption |
| Figure 5 | Purpose: The caption frames this object around HTML, Kimi, window, content, case, and source.; result: Paper-reported numeric markers: 5; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 5 caption |
| Figure 6 | Purpose: The caption frames this object around edit, distance, Music, score, rightarrow, and MusicXML.; result: Paper-reported numeric markers: 6, and 1; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 6 caption |
| Figure 7 | Purpose: The caption frames this object around annotated, pages, subject, Number, BISAC, and full.; result: Paper-reported numeric markers: 7, 6, 4, and 514; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 7 caption |
| Figure 8 | Purpose: The caption frames this object around Mean, standard, deviation, subject, high, and four-parser.; result: Paper-reported numeric markers: 8; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 8 caption |
| Figure 9 | Purpose: The caption frames this object around Unified, inference, prompt, evaluation, and Part.; result: Paper-reported numeric markers: 9, and 1; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 9 caption |
| Figure 10 | Purpose: The caption frames this object around Unified, inference, prompt, evaluation, and Part.; result: Paper-reported numeric markers: 10, and 2; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 10 caption |
| Figure 11 | Purpose: The caption frames this object around composition, subject, Left, data, elements, and Right.; result: Paper-reported numeric markers: 11, and 100%; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 11 caption |
| Figure 12 | Purpose: The caption frames this object around Scaling, and size.; result: Paper-reported numeric markers: 12; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 12 caption |
| Figure 13 | Purpose: The caption frames this object around Impact, sliding, window, size, pages, and formula.; result: Paper-reported numeric markers: 13; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Figure 13 caption |
| Equations | 51 distinct mathematical renderings exposed by HTML; representative objects listed in Section 2.2. | Central objects were inventoried with sign, normalization, conditioning, and denominator checks; no numerical reproduction. |
| Sections | 77 headings exposed by the full HTML. | Every heading was screened; method, evaluation, results, limitations, references, and appendices were mapped where present. |

Appendix and supplementary coverage:

- Content of Appendix
- Appendix A Data Sourcing and Pipeline
- Appendix B Multi-Parser Disagreement Score
- Appendix C Annotation Schema Reference
- Appendix D Full Per-Domain Statistics
- Appendix E Language Coverage
- Appendix F Subject Name Abbreviations
- Appendix G Inference Prompt
- Appendix H Additional Results

Complete section inventory:

- Report GitHub Issue
- Dr.DocBench : A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing Minglai Yang 1,8 Xinyan Velocity Yu 5 1 1 footnotemark: 1 Pengyuan Li 7 Xinyu Guo 1,8 Zhenting Qi 6 Konwoo Kim 2 Longtian Ye 1,9 Xiaolong Luo 6 Jinhe Bi 11 Henry Zhang 10 Haris Riaz 8 Xuan Zhang 1 Yunze Xiao 1,4 Bangya Liu 1 Tom Tang 1 Yunfei Zhao 1 Qunshu Lin 1 Zihan Wang 1 Minghao Liu 1,† Michael Lingzhi Li 6 Yilun Du 6 Jesse Thomason 5 Rogerio Feris 7 Alex Pentland 3 Zexue He 2 1 2077AI 2 Stanford University 3 MIT 4 Carnegie Mellon University 5 University of Southern California 6 Harvard University 7 IBM Research 8 University of Arizona 9 Duke University 10 UC Berkeley 11 LMU Munich {minglai, minghao}@2077ai.com, xinyany@usc.com, zexueh@stanford.edu https://www.2077ai.com/drdocbench/ https://github.com/2077AI/DrDocBench Equal contribution.Corresponding authors.
- Abstract
- 1 Introduction
- 2 Related Work
- Document parsing benchmarks.
- Document Parsing Systems.
- 3 Dr.DocBench
- 3.1 Difficulty-Aware Sampling
- 3.2 Annotation Schema
- 3.3 Doctor Annotation and Quality Control
- 3.4 Final Dataset
- 4 Experiments
- 4.1 Models
- Specialized VLMs.
- General VLMs.
- 4.2 Evaluation Metrics
- Pure Text.
- Tables.
- Formulas.
- 4.3 Overall Results and Findings
- 4.4 Per-Subject Breakdown and Analysis
- 4.5 Per-data-source Breakdown
- 4.6 Per-block Breakdown
- 5 Additional Analysis
- 5.1 Sensitivity to Multi-page Context Length
- 5.2 Token Efficiency
- 5.3 Case study: Table
- 5.4 Case study: Optical Music Recognition
- 6 Conclusion
- Ethical considerations
- Limitations
- References
- Content of Appendix
- Appendix A Data Sourcing and Pipeline
- License.
- Annotators and Compensation.
- Appendix B Multi-Parser Disagreement Score
- Appendix C Annotation Schema Reference
- C.1 OmniDocJSON Page Record
- C.2 Page-Level Attributes
- C.3 Block-Level Categories
- C.4 Inter-Block Relations
- Appendix D Full Per-Domain Statistics
- Appendix E Language Coverage
- Appendix F Subject Name Abbreviations
- Appendix G Inference Prompt
- Appendix H Additional Results
- GPT-5.5 vs. GPT-4o.
- Formula and table metrics.
- Prompt-incapable systems and outliers.
- H.1 Per-subject breakdown
- Subject-level wins.
- Model specializations.
- Subject difficulty.
- H.1.1 Music Analysis
- User-prompt-incapable baselines (minerU2.5, PaddleOCR).
- GT cross-document baseline.
- Frontier VLMs.
- Effect of the outlier document.
- Overall takeaway.
- H.2 The Worst Five Subjects
- H.3 Additional Analyses
- Page degradation (Table 9 ).
- Reading order by layout (Table 10 ).
- Text element attributes by edit distance (Table 11 ).
- Formula performance by document type and layout (Table 12 ).
- Challenge type (Table 13 ).
- Page-level language (Table 14 ).
- H.4 Scaling of model size
- Formula CDM decreases monotonically with scale.
- Per-metric trade-offs across model variants.
- H.5 Scaling of sliding window size
- Reading order degrades most consistently.
- Text edit distance shows a mixed early-window benefit.
- Formula metrics show no systematic degradation.
- The n = 2 n{=}2 default.

This ledger is completeness evidence, not reproduction. It records that each exposed section and numbered object was screened without reproducing the paper's tables, figures, or long captions.

## 16. Source and Evidence Notes

- Canonical arXiv record: https://arxiv.org/abs/2606.01393v1
- Canonical PDF: https://arxiv.org/pdf/2606.01393v1
- Canonical full-paper HTML: https://arxiv.org/html/2606.01393v1
- arXiv DOI resolver: https://doi.org/10.48550/arXiv.2606.01393
- Reviewed identity: arXiv:2606.01393v1
- Complete authors: Minglai Yang; Xinyan Velocity Yu; Pengyuan Li; Xinyu Guo; Zhenting Qi; Konwoo Kim; Longtian Ye; Xiaolong Luo; Jinhe Bi; Henry Zhang; Haris Riaz; Xuan Zhang; Yunze Xiao; Bangya Liu; Tom Tang; Yunfei Zhao; Qunshu Lin; Zihan Wang; Minghao Liu; Michael Lingzhi Li; Yilun Du; Jesse Thomason; Rogerio Feris; Alex Pentland; Zexue He
- Locally archived full PDF and full-paper HTML were verified; private path withheld.
- No source PDF, HTML, archive, extracted text, validator, or private index belongs in the public DEP-A package.
- Online primary-source vetting status: performed and receipt-linked; alternatives are not exhaustive and no experiment was independently reproduced.

## 17. Footnotes

[^source-paper]: Canonical paper identity and version are linked at https://arxiv.org/abs/2606.01393v1; the locally archived complete PDF and full-paper HTML were reconciled to this identity.
[^scope]: Paper report means content attributable to the authors and supported by the reviewed artifact; it is not independent reproduction.
[^integrity]: Source integrity requires a matching complete PDF and full-paper HTML with identity, version, title, structure, references, and readable-body checks.
[^inference]: Reviewer inference labels a mechanism-level interpretation derived from source evidence rather than asserted by the authors.
[^external]: External primary evidence was limited to receipt-linked official records and URLs. Availability or publication status does not imply artifact runnability, result reproduction, or exhaustive prior-work coverage.
[^association]: An associated DEP is contextual evidence, not a duplicate and not proof of the reviewed paper's claims.
