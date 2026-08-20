# Preserved failed review record — arXiv:2604.16029v2

> Archival status: this is the public-safe derivative of the original failed review object. It is preserved to document the barrier that stopped publication. It did not pass the semantic evidence gate and must not be treated as the corrected review. Private paths and machine context were removed; the original local bytes remain unchanged and privately hash-verified.

Original failure codes: `table_result_missing_model_or_row_identity`, `table_result_missing_real_header_or_value`, `table_result_missing_model_or_row_identity`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_model_or_row_identity`, `table_result_missing_real_header_or_value`, `table_result_missing_real_header_or_value`, `table_result_missing_model_or_row_identity`, `table_result_missing_real_header_or_value`, `table_result_missing_model_or_row_identity`, `table_result_missing_real_header_or_value`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `placeholder_scaffolding_present`, `verified_external_context_missing`, `verified_external_context_missing`.

---

# Whitepaper Review: Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning

## A detailed review, technical reconstruction, and independent re-conceptualization of “Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning”

**Source paper:** Jiaxi Bi; Tongxu Luo; Wenyu Du; Zhengyang Tang; Benyou Wang, “Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning,” arXiv:2604.16029v2.[^source-paper]

**Artifact prepared:** 2026-08-20
**Local source reviewed:** complete locally archived PDF (19 pages) and matching full-paper HTML (75996 readable body characters); private path withheld
**Review scope:** full-paper reconstruction, claim vetting, local evidence mapping, implications, and replication agenda
**Review status:** source artifacts inspected; bounded online primary-source vetting performed; experiments not independently rerun

## Executive Assessment

### The paper in one sentence

The paper presents and evaluates a technical contribution framed around cut, your, losses, learning, prune, paths, with its method, formal objects, experimental record, limitations, and source structure inspected from a complete local paper pair rather than an abstract page.

### The deeper idea

Reviewer inference: the durable mechanism is the source-defined change centered on Type, across, tasks, and reasoning, rather than the paper's brand name. This interpretation predicts that a matched intervention on Type changes pruning; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to 3 Methodology: Super Token for Pruning, Robustness across Tasks and Model Scales, B.2 Model-Specific Construction Pipeline. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

### Bottom-line judgment

The source is complete enough for a full-paper assessment, and the paper reports a technically organized contribution with an explicit evaluation record. Results remain paper-reported. The local evidence pass confirms the complete results structure and numbered-object inventory, but it does not independently reproduce a numerical value or infer a stronger denominator than the source states. The defensible verdict is therefore conditional: the paper establishes what it directly measures under its own setup, while broader superiority, generality, robustness, efficiency, or deployment readiness remains bounded by the tested models, data, metrics, budgets, hardware, and comparisons.[^scope]

### Principal strengths

- Complete PDF and matching full-paper HTML passed identity, structure, title, references, and readability gates.
- The source exposes 89 section headings, 16 table captions, 24 figure captions, and 114 mathematical renderings for coverage auditing.
- The review can distinguish paper report, external-primary evidence, reviewer inference, and hypothesis without relying on an abstract-only summary.

### Principal qualifications

1. The explicit qualification path is anchored to Limitations, Limitations., D.3 Discussion: The Advantage of Internal Signals. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions.
2. No result, code path, benchmark, training run, or hardware measurement was independently reproduced.
3. Bounded online checks verified canonical identity and the explicitly recorded official URLs; the search is not exhaustive and does not establish artifact runnability or reproduction.[^external]

## 1. The Problem and Research Questions

### 1.1 Problem and stakes

**Paper-reported problem:** For Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning, the formal target is bounded to the source-defined relation among reasoning, Parallel, paths, STOP, early, thanks, and LRMs. The task assumptions and stakes are anchored to Abstract, and 1 Introduction; no objective outside those sections is inferred.

**Research gap reconstructed from the source:** The paper positions Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning around reasoning, Parallel, paths, Type, across, and tasks. This records the authors' gap framing only; novelty, priority, generality, and superiority require the separate prior-work and evaluation audits.

The title and full-paper organization identify cut, your, losses, learning, prune, paths as the central problem space. A rigorous reading asks what input object is transformed, predicted, selected, optimized, or measured; which practical or scientific constraint motivates that operation; and which outcome makes the change valuable. Those questions must be answered by the method and evaluation sections, not by the title alone. The paper reports its own problem definition; this review preserves the boundary between that report and reviewer interpretation.

Paper-specific reconstruction: the abstract/introduction evidence concentrates on reasoning, stop, parallel, paths, thanks, edu, models, lrms, prohibitive, costs, under the headings Abstract, 1 Introduction. Those source terms locate the actual objects and constraints; they do not by themselves prove novelty or improvement. In this review they constrain the problem statement so a generic systems narrative cannot replace the paper's own domain and terminology.

The practical stakes depend on the actual denominator. An improvement in a representation, proxy, component score, or controlled benchmark can be important without automatically improving end-user quality, wall-clock cost, reliability, or safety. A durable account therefore separates the immediate technical objective from the downstream objective and asks which bridge between them is tested. If that bridge is only assumed, it remains an explicit gap rather than a hidden premise.

### 1.2 Prior method families and inherited components

The paper's related-work and background sections define the relevant method families. The review treats established backbones, pretrained models, datasets, optimization routines, kernels, evaluation harnesses, and standard metrics as inherited unless the source identifies a change. Novelty belongs to the specific interface, objective, representation, decision rule, data construction, proof, or evaluation design that differs. This prevents a system-level bundle from receiving credit for every capability of its dependencies.

### 1.3 Questions that govern the assessment

Five questions organize the reconstruction. What exact object enters and leaves the method? Which components are learned, fixed, searched, sampled, or verified? What objective and assumptions determine the operation? How do training or calibration differ from inference or deployment? Finally, which result would falsify the authors' causal or generality story rather than merely lower an aggregate score? These questions create an audit trail from paper report to independent assessment.

## 2. Formal and Technical Reconstruction

### 2.1 Definitions and assumptions

The authoritative definition chain lives in the complete source sections listed below. The automated evidence profile does not pretend that section names themselves describe the mechanism. Instead, the full review binds each claim to the source's definitions, stated assumptions, and adjacent formal or experimental context. The core technical headings identified for close reading were:

- 3 Methodology: Super Token for Pruning
- Robustness across Tasks and Model Scales
- B.2 Model-Specific Construction Pipeline

Variables should be assigned plain-language meanings before algebra is interpreted. Inputs, labels, state, parameters, budgets, constraints, random variables, and outputs must remain distinct. A probability requires a sample space and conditioning event; a loss requires an optimization direction; a ratio requires a numerator and denominator; and a guarantee retains every assumption under which it was proved. If the source uses the same symbol in different roles or shifts between population and sample quantities, that ambiguity should be preserved rather than silently repaired.

### 2.2 Objective and central equations

The full HTML exposes 114 distinct mathematical renderings. Each is treated as a paper-reported formal object whose sign, normalization, conditioning, and denominator must be read with adjacent prose.

Paper-specific formal reconstruction:

**Formal object 1 at 2.1 Problem Definition — The expression encodes definition or equality within 2.1 Problem Definition; its semantic role remains bound to that section..** `T=\{\tau_{i}\}_{i=1}^{N}`
Variables: "T, i, and N".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition.

**Formal object 2 at 2.1 Problem Definition — The expression encodes sampling relation within 2.1 Problem Definition; its semantic role remains bound to that section..** `\tau_{i}\sim P_{\Theta}(x)`
Variables: "i, P_{\\Theta}, and x".
Sign/normalization/conditioning/surrogate audit: "Detected operations: sampling relation. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition.

**Formal object 3 at 2.1 Problem Definition — The expression encodes definition or equality within 2.1 Problem Definition; its semantic role remains bound to that section..** `\hat{y}=\text{vote}(\{\tau_{i}\}_{i=1}^{N}).`
Variables: "y, i, and N".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition.

**Formal object 4 at The Path Pruning Formulation — The expression encodes definition or equality within The Path Pruning Formulation; its semantic role remains bound to that section..** `\mathcal{P}=\{p_{i}\}_{i=1}^{N}`
Variables: "P, p_{i}\\}, i, and N".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation.

**Formal object 5 at The Path Pruning Formulation — The expression encodes definition or equality within The Path Pruning Formulation; its semantic role remains bound to that section..** `s_{i}=S(p_{i}\mid x,\Theta),`
Variables: "s_{i}, S, p_{i}\\mid, and x".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation.

**Formal object 6 at The Path Pruning Formulation — The expression encodes definition or equality within The Path Pruning Formulation; its semantic role remains bound to that section..** `\hat{y}_{\text{pruned}}=\text{vote}(\{\text{finish}(p_{i})\mid s_{i}\in\{s_{j}\}_{j=1}^{k}\}).`
Variables: "y, p_{i}, s_{i}\\in\\{s, j, and k".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation.

Representative source mathematical objects follow. They are navigation evidence, not standalone interpretations:

- Mathematical object 1: `\Theta` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 2: `x` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 3: `N` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 4: `T=\{\tau_{i}\}_{i=1}^{N}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 5: `\tau_{i}\sim P_{\Theta}(x)` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 6: `\hat{y}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 7: `\hat{y}=\text{vote}(\{\tau_{i}\}_{i=1}^{N}).` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 8: `C\propto N` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 9: `L_{\text{prefix}}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 10: `\mathcal{P}=\{p_{i}\}_{i=1}^{N}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 11: `S` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 12: `s_{i}=S(p_{i}\mid x,\Theta),` — read with adjacent definitions; no symbol meaning is inferred from markup alone.

Equation-to-adjacent-context reconstruction:

- Equation under source heading 2.1 Problem Definition: `\Theta`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading 2.1 Problem Definition: `x`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading 2.1 Problem Definition: `N`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading 2.1 Problem Definition: `T=\{\tau_{i}\}_{i=1}^{N}`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading 2.1 Problem Definition: `\tau_{i}\sim P_{\Theta}(x)`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading 2.1 Problem Definition: `\hat{y}`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading 2.1 Problem Definition: `\hat{y}=\text{vote}(\{\tau_{i}\}_{i=1}^{N}).`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading 2.1 Problem Definition: `N`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading 2.1 Problem Definition: `C\propto N`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading The Path Pruning Formulation: `L_{\text{prefix}}`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading The Path Pruning Formulation: `\mathcal{P}=\{p_{i}\}_{i=1}^{N}`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.
- Equation under source heading The Path Pruning Formulation: `S`; adjacent method terms: type, section, across, tasks, model, pruning, paradigm, but.

For each central equation, the audit asks whether the sign agrees with the prose, whether weights are normalized, whether masking or conditioning changes the denominator, whether a displayed objective is exact or a training surrogate, and whether units can be compared. A learned score is not automatically calibrated, a relaxation is not an exact discrete solution, and an empirical constraint satisfaction rate is not a theorem. These distinctions protect the paper's real contribution from stronger claims it does not need.

### 2.3 Components, architecture, and information flow

The source's technical path is anchored to 3 Methodology: Super Token for Pruning, Robustness across Tasks and Model Scales, B.2 Model-Specific Construction Pipeline. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims.

**Input/output dataflow:** The documented dataflow is reconstructed only across 3 Methodology: Super Token for Pruning, Robustness across Tasks and Model Scales, and B.2 Model-Specific Construction Pipeline, where the source associates Type, across, tasks, reasoning, pruning, paradigm, and efficient. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

| Component | Inherited or novel | Role | Source locator |
|---|---|---|---|
| 3 Methodology: Super Token for Pruning | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with Pruning, paradigm, Methodology, Super, and Token; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2604.16029, 3 Methodology: Super Token for Pruning |
| Robustness across Tasks and Model Scales | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with across, Tasks, Type, Robustness, and Scales; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2604.16029, Robustness across Tasks and Model Scales |
| B.2 Model-Specific Construction Pipeline | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with Model-Specific, Pipeline, Construction, Since, and reasoning; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2604.16029, B.2 Model-Specific Construction Pipeline |

The paper-specific method vocabulary is type, section, across, tasks, model, pruning, paradigm, but, all, scales. This vocabulary was derived from the complete method/architecture paragraphs rather than the title. It identifies the entities that must appear in a faithful architecture reconstruction and creates a falsifiable check: an implementation or summary that omits these named objects is not yet grounded in this paper.

The architecture is reconstructed as an information-flow graph: source identity and inputs enter; inherited and paper-specific components transform or score them; a decision or representation is produced; optional validation or post-processing occurs; and an evaluated outcome leaves the pipeline. Each edge should name the information available at that point. A comparison becomes unfair if one method has access to labels, future requests, privileged metadata, additional context, or a larger tuning budget that another method lacks.

### 2.4 Training, calibration, and inference

Construction-time and runtime work are separate accounting domains. Training may fit parameters, construct representations, estimate thresholds, tune prompts, or learn a policy. Calibration may use held-out examples or measurements. Inference may retrieve, route, compress, classify, generate, search, solve, or verify. Post-processing may enforce a constraint or discard invalid output. A credible efficiency claim says which of these phases is included, which is amortized, and which is external to the reported number.

Training or calibration evidence is explicitly located in B.2 Model-Specific Construction Pipeline. The associated source vocabulary emphasizes type, section, across, tasks, model, pruning, paradigm, but, all, scales.

Paper-specific construction/training sequence:

1. At B.2 Model-Specific Construction Pipeline, the paper reports a training-related operation involving Model-Specific, Pipeline, Construction, Since, reasoning, and capabilities. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, B.2 Model-Specific Construction Pipeline)*
2. At A Unified Taxonomy, the paper reports a training-related operation involving internal, Taxonomy, first, learnable, existing, and research. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, A Unified Taxonomy)*
3. At Contributions, the paper reports a training-related operation involving pruning, Contributions, path, STOP, summary, and makes. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Contributions)*

Inference or runtime evidence is explicitly located in B.2 Model-Specific Construction Pipeline, Formalizing Empirical Findings. Its source vocabulary overlaps type, section, across, tasks, model, pruning, paradigm, but, all, scales.

Paper-specific inference/evaluation sequence:

1. At B.2 Model-Specific Construction Pipeline, the paper reports an inference or deployment action involving Model-Specific, Pipeline, Construction, Since, reasoning, and capabilities. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, B.2 Model-Specific Construction Pipeline)*
2. At Formalizing Empirical Findings, the paper reports an inference or deployment action involving Empirical, approx, Formalizing, Findings, formulation, and input. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings)*
3. At Why Prune Early in Parallel Reasoning?, the paper reports an inference or deployment action involving path, prefix, Reasoning, flawed, Prune, and Early. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Why Prune Early in Parallel Reasoning?)*

The reconstructed operational sequence is: pin input and artifact versions; validate prerequisites; compute the method-specific state or signal; apply the stated decision or objective; materialize the output; execute any downstream consumer; and measure both quality and resource outcomes. This sequence is reviewer inference grounded in the paper's organization. It is a testing model, not an assertion that the authors implemented an identical production controller.[^inference]

### 2.5 Notation and implementation audit

No independent implementation was run. The audit therefore checks internal legibility across equations, prose, captions, appendices, and extracted code/data statements. Apparent inconsistencies remain unresolved unless source evidence explains them. Source availability is classified in levels—declared, reachable, inspectable, runnable, and result-reproducing—and this local phase establishes only the declared/local-source layers.

## 3. Architecture and Complete Operational Pipeline

### 3.1 Representation and state

The documented dataflow is reconstructed only across 3 Methodology: Super Token for Pruning, Robustness across Tasks and Model Scales, and B.2 Model-Specific Construction Pipeline, where the source associates Type, across, tasks, reasoning, pruning, paradigm, and efficient. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

The central representation must be described by shape, type, provenance, lifetime, and relationship to the original input. If it is compressed, selected, latent, retrieved, generated, or aggregated, the review asks what information can be lost and how that loss is detected. If it is learned, the training distribution and version become part of its identity. If it is mutable, update ordering, expiry, and rollback become part of the method rather than operational afterthoughts.

### 3.2 Decision or action modules

The paper-specific modules should be separated from inherited encoders, decoders, solvers, retrieval systems, evaluators, or model APIs. A score can rank candidates without being calibrated; a policy can improve average reward without satisfying hard constraints; and a verifier can reject some failures without certifying all accepted outputs. The assessment uses the source's strongest ablation or controlled comparison to decide which module is necessary and which is merely bundled.

### 3.3 Dependencies, post-processing, and guarantee boundary

Dependencies include data preprocessing, external models, tokenizers, simulators, indexes, numerical libraries, and evaluation code. Post-processing can materially create the final result, so its compute and failure rate belong in the pipeline. Exact validation, when present, may establish a property of a returned object; it does not automatically establish semantic correctness, optimality, robustness, or absence of distribution shift.

### 3.4 Resource allocation and stopping

Budgets can refer to tokens, bytes, parameters, candidates, iterations, calls, samples, time, energy, or money. Requested and achieved budgets should both be recorded. Early stopping and fallback can bias which cases receive expensive processing. Batching can improve throughput while worsening latency. The review therefore distinguishes construction cost, per-instance latency, batch throughput, tail latency, peak memory, and downstream cost before accepting a general efficiency claim.

## 4. Experimental Design and Evidence Reconstructed

The evaluation reconstruction follows Findings 1 ., Findings 2 ., Formalizing Empirical Findings, Further Evaluation and Empirical Analysis, Evaluation metrics., Process-oriented Evaluation, with 16 table captions and 24 figure captions inventoried.

Paper-specific evaluation vocabulary centers on pruning, empirical, attention, model, approx, avg, across, varying, budgets, figure. These terms constrain which datasets, metrics, models, budgets, or operational quantities must be preserved with each reported comparison. They also identify where a later reproduction dossier must look for splits, baselines, hardware, batching, runtime semantics, and uncertainty rather than assuming conventional defaults.

The headings mechanically associated with evaluation and results were:

- Findings 1 .
- Findings 2 .
- Formalizing Empirical Findings
- Further Evaluation and Empirical Analysis
- Evaluation metrics.
- Process-oriented Evaluation

### 4.1 Data, splits, and distribution

| Dataset | Split | Preprocessing | Source locator |
|---|---|---|---|
| data | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: formulation, input, variables, and normalized; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings |
| non-learnable | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: existing, attempt, filter, and paths; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2604.16029, A Unified Taxonomy |
| task-specific | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: existing, attempt, filter, and paths; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2604.16029, A Unified Taxonomy |
| fine-grained | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: existing, attempt, filter, and paths; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2604.16029, A Unified Taxonomy |
| STOP | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: existing, attempt, filter, and paths; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2604.16029, A Unified Taxonomy |

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| no-pruning | Paper-reported comparator at Evaluation metrics.; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2604.16029, Evaluation metrics. |
| subset | Paper-reported comparator at Evaluation metrics.; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2604.16029, Evaluation metrics. |
| high-scoring | Paper-reported comparator at Process-oriented Evaluation; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2604.16029, Process-oriented Evaluation |
| low-scoring | Paper-reported comparator at Process-oriented Evaluation; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2604.16029, Process-oriented Evaluation |
| high-score | Paper-reported comparator at Process-oriented Evaluation; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2604.16029, Process-oriented Evaluation |
| STOP | Paper-reported comparator at Process-oriented Evaluation; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2604.16029, Process-oriented Evaluation |
| self-correction | Paper-reported comparator at Process-oriented Evaluation; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2604.16029, Process-oriented Evaluation |
| low-score | Paper-reported comparator at Process-oriented Evaluation; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2604.16029, Process-oriented Evaluation |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

| Metric | Denominator/conditioning | Direction | Source locator |
|---|---|---|---|
| accuracy | Paper-defined evaluation unit at Evaluation metrics.; exclusions and conditioning were not mechanically resolved | higher is normally better; confirm the paper's definition and conditioning | private full-paper evidence dossier for arXiv:2604.16029, Evaluation metrics. |
| source-defined score | Paper-defined evaluation unit at Process-oriented Evaluation; exclusions and conditioning were not mechanically resolved | higher is normally better; confirm the paper's definition and conditioning | private full-paper evidence dossier for arXiv:2604.16029, Process-oriented Evaluation |

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
| evaluation object at Formalizing Empirical Findings | Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning | comparator retained at the cited source locator; not inferred | 024 tokens | source-defined metric | 1, and 024 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings |
| data | Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning | comparator retained at the cited source locator; not inferred | configuration retained at the cited source locator | source-defined metric | 1.17, 10, 4, 0.46, 0.40, and 4.55 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings |
| evaluation object at Formalizing Empirical Findings | Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning | comparator retained at the cited source locator; not inferred | configuration retained at the cited source locator | source-defined metric | 6 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings |
| STOP | Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning | comparator retained at the cited source locator; not inferred | configuration retained at the cited source locator | source-defined metric | 1 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Further Evaluation and Empirical Analysis |

Bounded exact evidence retained from the paper report:

- Paper report, numeric result in Formalizing Empirical Findings: “In this formulation, all input variables are normalized to units…” (exact numeric tokens: 1, 024).

- No table-caption fragment was included in the bounded verbatim evidence budget.

The correct interpretation retains task, dataset, split, model, baseline, metric, budget, and hardware with each result. A largest reported improvement is an operating point, not a distribution. An average is not a tail guarantee. A component metric can diagnose mechanism without proving end-to-end utility. Where the source reports multiple tables or figures, their relationships should be checked for consistent defaults, denominators, and versioned settings.

Three types of gain remain separate. Representation gain means fewer tokens, bytes, channels, states, features, or bits. Execution gain means lower latency, memory traffic, transfer, energy, or higher throughput. Outcome gain means better correctness, quality, utility, constraint satisfaction, or task completion. The paper may establish one or more under its setting; a deployment decision requires the combination relevant to its service objective.

Table and figure captions were inventoried rather than republished. Their exact values remain anchored to the paper. Any public summary should cite only values whose numerator, denominator, model, dataset, and comparison are simultaneously known. This review does not manufacture missing uncertainty or turn qualitative illustrations into statistical evidence.

## 6. Ablations and Causal Evidence

Paper-specific ablation/control ledger:

Not applicable: No explicit removal, variant, or sensitivity result was resolved from the extracted evidence; causal necessity is not inferred. (source locator: private full-paper evidence dossier for arXiv:2604.16029, ablation inventory).

Ablations are persuasive when one named component changes while model, data, budget, training effort, and implementation quality stay fixed. The complete source was screened for removals, swaps, budget sweeps, sensitivity tests, and failure examples. If multiple elements change together, the result supports the bundle more strongly than any individual mechanism. If a simple cost-matched control is missing, the causal interpretation remains limited.

Randomness must be classified as training seeds, inference seeds, data-generation seeds, checkpoint-selection variance, or hyperparameter-search variance. Repeated inference does not prove training robustness. A named significance test should identify its independence unit and paired design. The practical importance of an effect is separate from statistical detectability, especially when a large benchmark makes very small changes significant.

Author-stated limitations:

- The author-side qualification at 6 Conclusion concerns reasoning, existing, research, internal, STOP, and address. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, 6 Conclusion)*
- The author-side qualification at Limitations concerns Limitations, pioneering, instantiation, internal, learnable, and paradigm. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Limitations)*
- The author-side qualification at Limitations. concerns Limitations, Verification, Extreme, Scales, current, and evaluation. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Limitations.)*
- The author-side qualification at Limitations. concerns pruning, fixed, prefix, Limitations, Structural, and Flexibility. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Limitations.)*

Reviewer-identified limitations:

- No independent reproduction was performed for arXiv:2604.16029v2; pruning, empirical, attention, and approx remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Further Evaluation and Empirical Analysis, and Evaluation metrics.)*
- The dossier inventories 89 headings, 16 tables, 24 figures, and 114 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, complete coverage inventory)*

The explicit qualification path is anchored to Limitations, Limitations., D.3 Discussion: The Advantage of Internal Signals. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 0 candidate sentences and the limitation/discussion vocabulary internal, stop, pruning, reasoning, type, research, potential, representations, prefix, external. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning: paper-reported problem claim centered on reasoning, Parallel, paths, and STOP | Located at Abstract; extracted numeric markers: 1, 84%, 90%, and 3 (private full-paper evidence dossier for arXiv:2604.16029, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning: paper-reported mechanism claim centered on Type, across, tasks, and reasoning | Located at 3 Methodology: Super Token for Pruning; extracted numeric markers: 3.1, 3.2, 2024, and 1 (private full-paper evidence dossier for arXiv:2604.16029, 3 Methodology: Super Token for Pruning) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning: paper-reported result claim centered on pruning, empirical, attention, and approx | Located at Further Evaluation and Empirical Analysis; extracted numeric markers: 1, 2, 7, and 024 (private full-paper evidence dossier for arXiv:2604.16029, Further Evaluation and Empirical Analysis) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2604.16029v2), [canonical PDF](https://arxiv.org/pdf/2604.16029v2), [canonical full-paper HTML](https://arxiv.org/html/2604.16029v2), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2604.16029). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2604.16029v2)*
- **Predecessor/prior work (blocked):** The bounded online record did not verify a noncanonical predecessor or prior-work source URL; the corresponding field-level claim remains unvalidated. *(evidence locator: online-vetting check for arXiv:2604.16029)*
- **Alternative or benchmark (checked):** The bounded online record verified reachability for https://bijiaxihh.github.io/STOP. Reachability does not establish ownership, completeness, runnability, or result reproduction. *(evidence locator: https://bijiaxihh.github.io/STOP)*
- **Code/data (blocked):** The bounded online record did not verify a noncanonical code or data artifact URL; the corresponding field-level claim remains unvalidated. *(evidence locator: online-vetting check for arXiv:2604.16029)*

Verified official primary-source links from the bounded check:

- Bounded primary-source check verified: https://bijiaxihh.github.io/STOP

Access-blocked or unverified URL evidence: not recorded

Prior-work and alternatives evidence: "bounded_to_canonical_arxiv_record_and_paper_declared_primary_links" This is a bounded search record, not an exhaustive map of the field.

Code/data and reproduction evidence: "link_reachability_only; repository contents were not downloaded, built, or executed" Reachability and metadata do not mean that code or data were executed, that dependencies were installed, or that a reported result reproduced.

Paper-declared external candidates were recorded as follows:

- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/accessible_HTML.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/license/index.html#licenses-available
- Paper-declared URL, not opened in this phase: https://bijiaxihh.github.io/STOP
- Paper-declared URL, not opened in this phase: https://maa.org/math-competitions/american-invitational-mathematics-examination-aime
- Paper-declared URL, not opened in this phase: https://developer.nvidia.com/blog/llm-inference-benchmarking-how-much-does-your-llm-inference-cost/
- Paper-declared URL, not opened in this phase: https://openai.com/index/learning-to-reason-with-llms/
- Paper-declared URL, not opened in this phase: https://openai.com/index/gpt-oss-model-card/
- Paper-declared URL, not opened in this phase: https://openreview.net/forum?id=Ti67584b98
- Paper-declared URL, not opened in this phase: https://math.nist.gov/~BMiller/LaTeXML/
- Paper-declared URL, not opened in this phase: https://github.com/arXiv/html_feedback/issues
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML

Their presence is discovery evidence, not proof that an artifact is official, available, licensed, runnable, or reproducing the paper. A later online-vetting phase should use primary sources, record HTTP/access limits, verify ownership and linkage, inspect release and license state, and distinguish artifact availability from runnable or result-reproducing status. Until then the publication status remains: arXiv preprint; no separate peer-reviewed venue inferred without an official venue source.

The isolated Black Lake checkout was used only for repository-readiness and dedupe context. A same-paper DEP-A would block a new owning record; a DEP-E or directly corresponding implementation is associated context rather than a duplicate. Background citations do not transfer evidence or claims to this paper.[^association]

## 9. Independent Re-conceptualization

Reviewer inference: the durable mechanism is the source-defined change centered on Type, across, tasks, and reasoning, rather than the paper's brand name. This interpretation predicts that a matched intervention on Type changes pruning; it is not an author claim or theorem.

Re-conceptualize the contribution as an evidence-linked state transition: pin source identity, record the method-specific decision, measure realized resource and outcome effects, and retain a conservative fallback whose trigger can be falsified on held-out conditions. This is reviewer inference and proposal, not an author claim and not an experimentally validated architecture.[^inference]

The mechanism can be viewed as a governed handoff between evidence, decision, execution, and outcome. Evidence identifies the source state and the signal the method uses. Decision records the action or representation chosen under a budget. Execution records what the system actually did, including fallback and resource use. Outcome records task quality and failure. The mapping is useful because it predicts what must be logged; it breaks when the paper studies a purely formal object with no operational transition.

A second bounded analogy is experimental portfolio control. Different baselines, budgets, and ablations are portfolio arms whose information access and cost must be matched. This analogy highlights selection bias and incomplete frontiers, but it does not imply that the paper uses an online bandit or that deployment should optimize only one scalar reward. Its falsifiable prediction is that the proposed mechanism's advantage should shrink when information access and complete cost are carefully matched if the original gain came mainly from comparison asymmetry.

## 10. Research Notes, Limitations, and Evidence Boundary

The complete local PDF and full-paper HTML for arXiv:2604.16029v2 were inspected. The PDF passed size, header, EOF, parse, page-count, title, structure, and references checks. The HTML passed size, readable-body, document-marker, heading, structure, title, and identity checks. Abstract HTML was metadata only and did not qualify as the paper body.[^integrity]

The coverage pass includes introduction, method or formal analysis, experiments or results, discussion or conclusion, references, appendices where exposed, tables, figures, equations, footnotes, disclosures, and code/data language. Extraction can lose visual layout and some mathematical semantics; the ledger records this boundary rather than claiming that every graphic was numerically reproduced.

Paper-specific qualification inventory: limitation/discussion terms internal, stop, pruning, reasoning, type, research, potential, representations, prefix, external; disclosure/funding language Acknowledgment, Limitations, limitation; code/data language GitHub, Code, checkpoint, reproducibility, dataset; appendix headings Appendix A Related Work, Appendix B Data Construction Details, Appendix C Detailed Experimental Settings, Appendix D Ablation: Data Quality vs. Architecture, Appendix E Derivation and Validation of the Scaling Law, Appendix F Detailed Latency and Throughput Benchmarking, Appendix G Extended Attention Analysis. These are evidence pointers. A missing extracted term is not proof that a disclosure, artifact, or limitation does not exist.

Evidence layers remain explicit. Layer A is what the paper reports. Layer B contains the bounded primary records actually checked online; its conclusions are limited to the recorded identity, publication, and artifact-access evidence. Layer C is reviewer inference, including the governed-handoff interpretation. Layer D is a hypothesis or proposal, including deployment controls and falsification tests. A sentence is not silently promoted between layers.

Paper/prose/table consistency checks:

| Issue/check | Assessment | Source locator |
|---|---|---|
| Canonical ID, version, title, authors, PDF hash, and HTML hash were reconciled for arXiv:2604.16029v2; full quantitative table/prose/code consistency was not independently rerun. | identity consistency checked; quantitative and implementation consistency remain unresolved | source-integrity and online identity receipts for arXiv:2604.16029v2 |

Substantive evidence boundary: The profile binds arXiv:2604.16029v2 to a complete local PDF and full-paper HTML, 89 headings, 16 tables, 24 figures, and 114 extracted mathematical objects, and 1 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

The explicit qualification path is anchored to Limitations, Limitations., D.3 Discussion: The Advantage of Internal Signals. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. No experiment, benchmark, training run, code path, hardware measurement, dataset, service rollout, or security test was independently rerun. This methodology produces auditability, observability, and traceable evidence; it is not security certification.

The evidence-derived methodology score is 20/20: source integrity 2, full paper coverage 2, technical fidelity 2, quantitative fidelity 2, external vetting 2, claim calibration 2, reconceptualization 2, research value 2, provenance 2, durability 2. The score is computed from source integrity, complete coverage, paper-specific method/equation/training/inference evidence, numeric/table/figure evidence, and whether bounded external vetting was actually performed. It rates the review artifact's coverage and evidence discipline. It does not rate the paper's truth and cannot substitute for subject-matter peer review, actual reproduction, or security assessment.

## 11. Potential Implications

### 11.1 Scientific implications

The paper's durable scientific value depends on whether the named mechanism predicts outcomes beyond the exact benchmark coordinate. Publishing full frontiers, per-instance failures, achieved budgets, uncertainty, and versioned configurations would let later work test the explanation instead of comparing isolated maxima. Negative results under shifted data, models, or budgets are especially informative because they locate the mechanism's boundary.

### 11.2 System-design implications

Builders should place the optimized path behind an observable budget and fallback controller. Source, model, data, and configuration versions should be pinned. The controller should log why an action occurred, realized rather than requested cost, validation status, and downstream outcome. Shadow comparison against a conservative path can expose drift and tail regressions before the method becomes irreversible infrastructure.

### 11.3 Deployment and governance

Derived representations can preserve sensitive, licensed, or incorrect content. Access, retention, deletion, correction, provenance, and tenant isolation should follow the information after transformation. Appropriate use requires monitored assumptions and a measurable refusal or fallback path. Poor fit includes untested distributions, absent outcome joins, hidden preprocessing cost, or settings where failure cannot be detected before harm.

## 12. New Falsifiable Hypotheses

### Hypothesis 1: Matched removal of Type

**Proposition:** Reviewer hypothesis: the source-linked Type operation is causally responsible for part of the reported pruning behavior.
**Predicted observation:** Removing or neutralizing Type under matched data and compute will measurably weaken pruning.
**Falsifying observation:** A competent matched control without Type preserves the same pruning distribution within uncertainty.
**Minimum test:** Run a paired, seed-controlled ablation at Further Evaluation and Empirical Analysis and archive per-instance outcomes and resource use.
**Evidence locator:** private full-paper evidence dossier for arXiv:2604.16029, 3 Methodology: Super Token for Pruning, and Robustness across Tasks and Model Scales

### Hypothesis 2: Boundary transfer for Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning

**Proposition:** Reviewer hypothesis: the relation between Type, and across and pruning, and empirical weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2604.16029, Further Evaluation and Empirical Analysis, and Evaluation metrics.

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2604.16029, Further Evaluation and Empirical Analysis, and Evaluation metrics..
2. **Reproduce the end-to-end Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning path** Success: the source-defined Type, across, and tasks and pruning, and empirical are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2604.16029, 3 Methodology: Super Token for Pruning, and Robustness across Tasks and Model Scales.
3. **Falsify the reviewer mechanism thesis for Type** Success: a matched intervention on Type predicts a corresponding change in pruning Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2604.16029, 3 Methodology: Super Token for Pruning, and Robustness across Tasks and Model Scales.

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning should be remembered as a tested relation between Type, across, and tasks and pruning, empirical, and attention under the configurations at Further Evaluation and Empirical Analysis, and Evaluation metrics., not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The caption frames this object around Pruning, Desideratum, Unified, Taxonomy, Path, and categorize.; result: Paper-reported numeric markers: 1, and 2; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 1 caption |
| Table 2 | Purpose: The caption frames this object around best, across, various, benchmarks, result, and bolded.; result: Paper-reported numeric markers: 2; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 2 caption |
| Table 3 | Purpose: The caption frames this object around labels, Performance, comparison, hard, MC-estimated, and soft.; result: Paper-reported numeric markers: 3, 1, and 32; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 3 caption |
| Table 4 | Purpose: The caption frames this object around Comparing, STOP, module, simple, linear, and classifier.; result: Paper-reported numeric markers: 4; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 4 caption |
| Table 5 | Purpose: The caption frames this object around prefix, Effect, number, STOP, tokens, and DS-Qwen-2.5-1.5B.; result: Paper-reported numeric markers: 5, 2.5, 1, 2024, and 2048; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 5 caption |
| Table 6 | Purpose: The caption frames this object around Effect, LoRA, rank, DS-Qwen-2.5-1.5B, and AIME.; result: Paper-reported numeric markers: 6, 2.5, 1, and 2024; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 6 caption |
| Table 7 | Purpose: The caption frames this object around Inference, overhead, analysis, STOP, achieves, and near-zero.; result: Paper-reported numeric markers: 7; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 7 caption |
| Table 8 | Purpose: The caption frames this object around Generalization, ZebraLogic, STOP, robustly, generalizes, and beyond.; result: Paper-reported numeric markers: 8; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 8 caption |
| Table 9 | Purpose: The caption frames this object around AIMO3, competition, setting, tool, and GPT-OSS-120B.; result: Paper-reported numeric markers: 9; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 9 caption |
| Table 10 | Purpose: The caption frames this object around data, Statistics, model-specific, training, Prefixes, and extracted.; result: Paper-reported numeric markers: 10; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 10 caption |
| Table 11 | Purpose: The caption frames this object around Training, Cost, Supervision, Construction, number, and pairs.; result: Paper-reported numeric markers: 11, 8 ×, and 32; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 11 caption |
| Table 12 | Purpose: The caption frames this object around Training, hyperparameters, across, and scales.; result: Paper-reported numeric markers: 12; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 12 caption |
| Table 13 | Purpose: The caption frames this object around Type, Data, Architecture, external, retrain, and Ablation.; result: Paper-reported numeric markers: 13, and 8; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 13 caption |
| Table 14 | Purpose: The caption frames this object around task, GPQA, Science, Short-Horizon, Recommended, and inverse.; result: Paper-reported numeric markers: 14, 1, -1, 8, and 650; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 14 caption |
| Table 15 | Purpose: The caption frames this object around task, AIME, Math, Long-Horizon, Recommended, and inverse.; result: Paper-reported numeric markers: 15, 1, -1, 11, and 950; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 15 caption |
| Table 16 | Purpose: The caption frames this object around Throughput, cost, explicit, verification, drop, and Breakdown.; result: Paper-reported numeric markers: 16, 1.74%, 17.71%, 3 %, 3, and 0.59%; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 16 caption |
| Figure 1 | Purpose: The caption frames this object around early, pruning, necessity, errors, often, and lead.; result: Paper-reported numeric markers: 1; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure 1 caption |
| Figure 2 | Purpose: The caption frames this object around taxonomy, path, and pruning.; result: Paper-reported numeric markers: 2; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure 2 caption |
| Figure 3 | Purpose: The caption frames this object around inference, process, comprises, three, stages, and caching.; result: Paper-reported numeric markers: 3; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure 3 caption |
| Figure 4 | Purpose: The caption frames this object around Performance, compute, four, types, math, and stem.; result: Paper-reported numeric markers: 4; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure 4 caption |
| Figure inventory item 5 | Purpose: The caption frames this object around prefix, GPQA, and text.; result: Paper-reported numeric markers: 512; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 5 caption |
| Figure inventory item 6 | Purpose: The caption frames this object around prefix, GPQA, and text.; result: Paper-reported numeric markers: 1024; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 6 caption |
| Figure inventory item 7 | Purpose: The caption frames this object around prefix, AIME, and text.; result: Paper-reported numeric markers: 2048; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 7 caption |
| Figure inventory item 8 | Purpose: The caption frames this object around prefix, AIME, and text.; result: Paper-reported numeric markers: 4096; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 8 caption |
| Figure 5 | Purpose: The caption frames this object around prefix, Performance, comparison, different, retention, and ratios.; result: Paper-reported numeric markers: 5; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure 5 caption |
| Figure 6 | Purpose: The caption frames this object around ratio, Inverse, retention, gamma, compute-to-prefix, and theoretical.; result: Paper-reported numeric markers: 6, 1, -1, and 7; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure 6 caption |
| Figure inventory item 11 | Purpose: The caption frames this object around High-scoring, and Path.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 11 caption |
| Figure inventory item 12 | Purpose: The caption frames this object around Low-scoring, and Path.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 12 caption |
| Figure 7 | Purpose: The caption frames this object around STOP, paths, Attention, Analysis, Decision-Making, and High-scoring.; result: Paper-reported numeric markers: 7; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure 7 caption |
| Figure 8 | Purpose: The caption frames this object around MC-based, construction, prefix, potential, and supervision.; result: Paper-reported numeric markers: 8; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure 8 caption |
| Figure inventory item 15 | Purpose: The caption frames this object around AIME, prefix, Optimal, gamma, shifts, and aggressive.; result: Paper-reported numeric markers: 2024, and 2048; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 15 caption |
| Figure inventory item 16 | Purpose: The caption frames this object around AIME, prefix, Longer, context, enables, and stable.; result: Paper-reported numeric markers: 2024, and 4096; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 16 caption |
| Figure inventory item 17 | Purpose: The caption frames this object around GPQA, prefix, Higher, compute, budgets, and drive.; result: Paper-reported numeric markers: 512; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 17 caption |
| Figure inventory item 18 | Purpose: The caption frames this object around GPQA, prefix, Scaling, behavior, remains, and consistent.; result: Paper-reported numeric markers: 1024; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 18 caption |
| Figure 9 | Purpose: The caption frames this object around Empirical, optimization, surfaces, Impact, retention, and ratio.; result: Paper-reported numeric markers: 9; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure 9 caption |
| Figure inventory item 20 | Purpose: The caption frames this object around High-scoring, Case, module, focuses, logical, and negation.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 20 caption |
| Figure inventory item 21 | Purpose: The caption frames this object around Low-scoring, Case, Attention, concentrates, heavily, and answer.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 21 caption |
| Figure inventory item 22 | Purpose: The caption frames this object around High-scoring, Case, Similar, module, attends, and logical.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 22 caption |
| Figure inventory item 23 | Purpose: The caption frames this object around Low-scoring, Case, module, demonstrates, premature, and closure.; result: Paper-reported numeric markers: none mechanically isolated; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure inventory item 23 caption |
| Figure 10 | Purpose: The caption frames this object around STOP, paths, Extended, Visualization, Attention, and Maps.; result: Paper-reported numeric markers: 10; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Figure 10 caption |
| Equations | 114 distinct mathematical renderings exposed by HTML; representative objects listed in Section 2.2. | Central objects were inventoried with sign, normalization, conditioning, and denominator checks; no numerical reproduction. |
| Sections | 89 headings exposed by the full HTML. | Every heading was screened; method, evaluation, results, limitations, references, and appendices were mapped where present. |

Appendix and supplementary coverage:

- Appendix A Related Work
- Appendix B Data Construction Details
- Appendix C Detailed Experimental Settings
- Appendix D Ablation: Data Quality vs. Architecture
- Appendix E Derivation and Validation of the Scaling Law
- Appendix F Detailed Latency and Throughput Benchmarking
- Appendix G Extended Attention Analysis

Complete section inventory:

- Report GitHub Issue
- Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning
- Abstract
- 1 Introduction
- Why Prune Early in Parallel Reasoning?
- A Unified Taxonomy
- Further Evaluation and Empirical Analysis
- Contributions
- 2 A Unified Taxonomy of Path Pruning
- 2.1 Problem Definition
- The Path Pruning Formulation
- 2.2 A Unified Taxonomy of Pruning Signal Generators
- Two Desiderata for Signal Generators
- Desideratum 1 .
- Desideratum 2 .
- External Signal Source
- Type I .
- Type II .
- Internal Signal Source
- Type III .
- Type IV .
- 3 Methodology: Super Token for Pruning
- 3.1 Motivation for Type IV Pruning
- 3.2 Instantiation of Type IV Pruning: STOP
- Components
- Training: Learn to Use Internal Information
- Training Cost
- Inference: “Launch-Check-Resume”
- 4 A Close Look at Path Pruning through the Lens of Signal Generators
- 4.1 On the Effectiveness of Pruning
- Standardized protocol.
- Evaluation metrics.
- Performance Hierarchy across Four Types Pruning
- Findings 1 .
- 4.2 On the Scalability of Pruning
- Robustness across Tasks and Model Scales
- Findings 2 .
- 5 A Closer Look at STOP
- 5.1 Determining the Optimal remaining ratios
- Consistent Empirical Trends across Various Settings
- Formalizing Empirical Findings
- Applying the Empirical Guideline
- 5.2 Ablations and Analysis
- Ablation: Quality of the Supervision Signal
- Findings 3 .
- Ablation: Necessity of Critique Adapter
- Findings 4 .
- Ablation: Sensitivity to Design Choices
- Findings 5 .
- Analysis: Computational Overhead
- Analysis: Generalization to Non-Math/STEM Tasks
- Analysis: Generalization to Tool Use
- 5.3 How STOP Attends
- Process-oriented Evaluation
- 6 Conclusion
- Acknowledgment
- Limitations
- Limitations.
- Future Directions.
- References
- Appendix A Related Work
- A.1 Parallel Reasoning
- A.2 Path Pruning (Prefix Rejection)
- Appendix B Data Construction Details
- B.1 Source Benchmarks and Decontamination
- B.2 Model-Specific Construction Pipeline
- Difficulty Stratification (Filtering).
- Prefix Generation.
- Potential Estimation via MC Rollouts.
- MC Score Calculation.
- Data Statistics and Insights.
- B.3 Training Cost Details
- Appendix C Detailed Experimental Settings
- C.1 Infrastructure and Sampling Configuration
- C.2 Evaluation Protocol
- C.3 Prompt Templates and Input Format
- C.4 STOP Module Training Details
- C.5 Baseline Descriptions
- Appendix D Ablation: Data Quality vs. Architecture
- D.1 Motivation and Setup
- D.2 Detailed Analysis
- D.3 Discussion: The Advantage of Internal Signals
- Appendix E Derivation and Validation of the Scaling Law
- E.1 Empirical Observations on Optimal Retention
- E.2 Recommended Retention Guidelines
- Appendix F Detailed Latency and Throughput Benchmarking
- F.1 Metric Definitions
- F.2 Quantitative Analysis
- Appendix G Extended Attention Analysis

This ledger is completeness evidence, not reproduction. It records that each exposed section and numbered object was screened without reproducing the paper's tables, figures, or long captions.

## 16. Source and Evidence Notes

- Canonical arXiv record: https://arxiv.org/abs/2604.16029v2
- Canonical PDF: https://arxiv.org/pdf/2604.16029v2
- Canonical full-paper HTML: https://arxiv.org/html/2604.16029v2
- arXiv DOI resolver: https://doi.org/10.48550/arXiv.2604.16029
- Reviewed identity: arXiv:2604.16029v2
- Complete authors: Jiaxi Bi; Tongxu Luo; Wenyu Du; Zhengyang Tang; Benyou Wang
- Locally archived full PDF and full-paper HTML were verified; private path withheld.
- No source PDF, HTML, archive, extracted text, validator, or private index belongs in the public DEP-A package.
- Online primary-source vetting status: performed and receipt-linked; alternatives are not exhaustive and no experiment was independently reproduced.

## 17. Footnotes

[^source-paper]: Canonical paper identity and version are linked at https://arxiv.org/abs/2604.16029v2; the locally archived complete PDF and full-paper HTML were reconciled to this identity.
[^scope]: Paper report means content attributable to the authors and supported by the reviewed artifact; it is not independent reproduction.
[^integrity]: Source integrity requires a matching complete PDF and full-paper HTML with identity, version, title, structure, references, and readable-body checks.
[^inference]: Reviewer inference labels a mechanism-level interpretation derived from source evidence rather than asserted by the authors.
[^external]: External primary evidence was limited to receipt-linked official records and URLs. Availability or publication status does not imply artifact runnability, result reproduction, or exhaustive prior-work coverage.
[^association]: An associated DEP is contextual evidence, not a duplicate and not proof of the reviewed paper's claims.
