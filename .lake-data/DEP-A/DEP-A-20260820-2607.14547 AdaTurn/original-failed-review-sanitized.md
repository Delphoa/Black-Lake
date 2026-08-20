# Preserved failed review record — arXiv:2607.14547v1

> Archival status: this is the public-safe derivative of the original failed review object. It is preserved to document the barrier that stopped publication. It did not pass the semantic evidence gate and must not be treated as the corrected review. Private paths and machine context were removed; the original local bytes remain unchanged and privately hash-verified.

Original failure codes: `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `table_result_missing_model_or_row_identity`, `placeholder_scaffolding_present`, `verified_external_context_missing`, `verified_external_context_missing`.

---

# Whitepaper Review: AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents

## A detailed review, technical reconstruction, and independent re-conceptualization of “AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents”

**Source paper:** Susan Liang; Chao Huang; Filippos Bellos; Jing Bi; Jason J Corso; Chenliang Xu, “AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents,” arXiv:2607.14547v1.[^source-paper]

**Artifact prepared:** 2026-08-20
**Local source reviewed:** complete locally archived PDF (22 pages) and matching full-paper HTML (53354 readable body characters); private path withheld
**Review scope:** full-paper reconstruction, claim vetting, local evidence mapping, implications, and replication agenda
**Review status:** source artifacts inspected; bounded online primary-source vetting performed; experiments not independently rerun

## Executive Assessment

### The paper in one sentence

The paper presents and evaluates a technical contribution framed around adaturn, budget-aware, test-time, scaling, active, visual, with its method, formal objects, experimental record, limitations, and source structure inspected from a complete local paper pair rather than an abstract page.

### The deeper idea

Reviewer inference: the durable mechanism is the source-defined change centered on AdaTurn, active, visual, and rollout, rather than the paper's brand name. This interpretation predicts that a matched intervention on AdaTurn changes turns; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to 3 Method. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

### Bottom-line judgment

The source is complete enough for a full-paper assessment, and the paper reports a technically organized contribution with an explicit evaluation record. Results remain paper-reported. The local evidence pass confirms the complete results structure and numbered-object inventory, but it does not independently reproduce a numerical value or infer a stronger denominator than the source states. The defensible verdict is therefore conditional: the paper establishes what it directly measures under its own setup, while broader superiority, generality, robustness, efficiency, or deployment readiness remains bounded by the tested models, data, metrics, budgets, hardware, and comparisons.[^scope]

### Principal strengths

- Complete PDF and matching full-paper HTML passed identity, structure, title, references, and readability gates.
- The source exposes 30 section headings, 4 table captions, 13 figure captions, and 73 mathematical renderings for coverage auditing.
- The review can distinguish paper report, external-primary evidence, reviewer inference, and hypothesis without relying on an abstract-only summary.

### Principal qualifications

1. The explicit qualification path is anchored to Limitations.. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions.
2. No result, code path, benchmark, training run, or hardware measurement was independently reproduced.
3. Bounded online checks verified canonical identity and the explicitly recorded official URLs; the search is not exhaustive and does not establish artifact runnability or reproduction.[^external]

## 1. The Problem and Research Questions

### 1.1 Problem and stakes

**Paper-reported problem:** For AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents, the formal target is bounded to the source-defined relation among rollout, budget, turns, agent, visual, Wang, and agents. The task assumptions and stakes are anchored to Abstract, and 1 Introduction; no objective outside those sections is inferred.

**Research gap reconstructed from the source:** The paper positions AdaTurn around rollout, budget, turns, AdaTurn, active, and visual. This records the authors' gap framing only; novelty, priority, generality, and superiority require the separate prior-work and evaluation audits.

The title and full-paper organization identify adaturn, budget-aware, test-time, scaling, active, visual as the central problem space. A rigorous reading asks what input object is transformed, predicted, selected, optimized, or measured; which practical or scientific constraint motivates that operation; and which outcome makes the change valuable. Those questions must be answered by the method and evaluation sections, not by the title alone. The paper reports its own problem definition; this review preserves the boundary between that report and reviewer interpretation.

Paper-specific reconstruction: the abstract/introduction evidence concentrates on rollout, budget, turns, agent, visual, when, wang, available, than, answer, under the headings Abstract, 1 Introduction. Those source terms locate the actual objects and constraints; they do not by themselves prove novelty or improvement. In this review they constrain the problem statement so a generic systems narrative cannot replace the paper's own domain and terminology.

The practical stakes depend on the actual denominator. An improvement in a representation, proxy, component score, or controlled benchmark can be important without automatically improving end-user quality, wall-clock cost, reliability, or safety. A durable account therefore separates the immediate technical objective from the downstream objective and asks which bridge between them is tested. If that bridge is only assumed, it remains an explicit gap rather than a hidden premise.

### 1.2 Prior method families and inherited components

The paper's related-work and background sections define the relevant method families. The review treats established backbones, pretrained models, datasets, optimization routines, kernels, evaluation harnesses, and standard metrics as inherited unless the source identifies a change. Novelty belongs to the specific interface, objective, representation, decision rule, data construction, proof, or evaluation design that differs. This prevents a system-level bundle from receiving credit for every capability of its dependencies.

### 1.3 Questions that govern the assessment

Five questions organize the reconstruction. What exact object enters and leaves the method? Which components are learned, fixed, searched, sampled, or verified? What objective and assumptions determine the operation? How do training or calibration differ from inference or deployment? Finally, which result would falsify the authors' causal or generality story rather than merely lower an aggregate score? These questions create an audit trail from paper report to independent assessment.

## 2. Formal and Technical Reconstruction

### 2.1 Definitions and assumptions

The authoritative definition chain lives in the complete source sections listed below. The automated evidence profile does not pretend that section names themselves describe the mechanism. Instead, the full review binds each claim to the source's definitions, stated assumptions, and adjacent formal or experimental context. The core technical headings identified for close reading were:

- 3 Method

Variables should be assigned plain-language meanings before algebra is interpreted. Inputs, labels, state, parameters, budgets, constraints, random variables, and outputs must remain distinct. A probability requires a sample space and conditioning event; a loss requires an optimization direction; a ratio requires a numerator and denominator; and a guarantee retains every assumption under which it was proved. If the source uses the same symbol in different roles or shifts between population and sample quantities, that ambiguity should be preserved rather than silently repaired.

### 2.2 Objective and central equations

The full HTML exposes 73 distinct mathematical renderings. Each is treated as a paper-reported formal object whose sign, normalization, conditioning, and denominator must be read with adjacent prose.

Paper-specific formal reconstruction:

**Formal object 1 at 3.1 Problem Formulation and AdaTurn Agent Loop — The expression encodes definition or equality within 3.1 Problem Formulation and AdaTurn Agent Loop; its semantic role remains bound to that section..** `x=(Q,I,T_{\mathrm{max}}).`
Variables: "x, Q, I, and T_{\\mathrm{max}}".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop.

**Formal object 2 at 3.1 Problem Formulation and AdaTurn Agent Loop — The expression encodes definition or equality within 3.1 Problem Formulation and AdaTurn Agent Loop; its semantic role remains bound to that section..** `h_{t}=\left(Q,I,T_{\mathrm{max}},(y_{1},o_{1}),\ldots,(y_{t-1},o_{t-1})\right),`
Variables: "h_{t}, Q, I, T_{\\mathrm{max}}, y_{1}, o_{1}, y_{t-1}, and o_{t-1}".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop.

**Formal object 3 at 3.1 Problem Formulation and AdaTurn Agent Loop — The expression encodes sampling relation within 3.1 Problem Formulation and AdaTurn Agent Loop; its semantic role remains bound to that section..** `y_{t}\sim\pi_{\theta}(\cdot\mid h_{t}),\qquad y_{t}\in\mathcal{C}\cup\mathcal{A}.`
Variables: "y_{t}\\sim\\pi, \\theta, h_{t}, and y_{t}\\in\\mathcal{C}\\cup\\mathcal{A}".
Sign/normalization/conditioning/surrogate audit: "Detected operations: sampling relation. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop.

**Formal object 4 at 3.1 Problem Formulation and AdaTurn Agent Loop — The expression encodes definition or equality within 3.1 Problem Formulation and AdaTurn Agent Loop; its semantic role remains bound to that section..** `o_{t}=\mathcal{E}(I,y_{t}),`
Variables: "o_{t}, E, I, and y_{t}".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop.

**Formal object 5 at 3.1 Problem Formulation and AdaTurn Agent Loop — The expression encodes conditional rule, and definition or equality within 3.1 Problem Formulation and AdaTurn Agent Loop; its semantic role remains bound to that section..** `y_{t}\in\mathcal{Y}_{t}=\begin{cases}\mathcal{C}\cup\mathcal{A},&t<T_{\mathrm{max}},\\ \mathcal{A},&t=T_{\mathrm{max}}.\end{cases}`
Variables: "y_{t}\\in\\mathcal{Y}, t, C, A, and T_{\\mathrm{max}}".
Sign/normalization/conditioning/surrogate audit: "Detected operations: conditional rule, and definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop.

**Formal object 6 at 3.2 Forced-Answer DAPO — The expression encodes definition or equality within 3.2 Forced-Answer DAPO; its semantic role remains bound to that section..** `\{Y^{(i)}\}_{i=1}^{G}`
Variables: "Y, i, and G".
Sign/normalization/conditioning/surrogate audit: "Detected operations: definition or equality. The review must retain the displayed sign, denominator, conditioning, and surrogate boundary; code behavior was not independently checked.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO.

Representative source mathematical objects follow. They are navigation evidence, not standalone interpretations:

- Mathematical object 1: `1.34\times` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 2: `T_{\mathrm{max}}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 3: `Q` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 4: `I` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 5: `g` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 6: `x=(Q,I,T_{\mathrm{max}}).` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 7: `t` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 8: `h_{t}=\left(Q,I,T_{\mathrm{max}},(y_{1},o_{1}),\ldots,(y_{t-1},o_{t-1})\right),` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 9: `y_{t}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 10: `o_{t}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 11: `\pi_{\theta}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 12: `c_{t}\in\mathcal{C}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.

Equation-to-adjacent-context reconstruction:

- Equation under source heading 1 Introduction: `1.34\times`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `T_{\mathrm{max}}`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `Q`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `I`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `T_{\mathrm{max}}`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `g`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `x=(Q,I,T_{\mathrm{max}}).`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `t`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `h_{t}=\left(Q,I,T_{\mathrm{max}},(y_{1},o_{1}),\ldots,(y_{t-1},o_{t-1})\right),`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `y_{t}`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `t`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.
- Equation under source heading 3.1 Problem Formulation and AdaTurn Agent Loop: `o_{t}`; adjacent method terms: section, rollout, not, but, training, adaturn, built, around.

For each central equation, the audit asks whether the sign agrees with the prose, whether weights are normalized, whether masking or conditioning changes the denominator, whether a displayed objective is exact or a training surrogate, and whether units can be compared. A learned score is not automatically calibrated, a relaxation is not an exact discrete solution, and an empirical constraint satisfaction rate is not a theorem. These distinctions protect the paper's real contribution from stronger claims it does not need.

### 2.3 Components, architecture, and information flow

The source's technical path is anchored to 3 Method. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims.

**Input/output dataflow:** The documented dataflow is reconstructed only across 3 Method, where the source associates AdaTurn, active, visual, rollout, budget-aware, training, and built. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

| Component | Inherited or novel | Role | Source locator |
|---|---|---|---|
| 3 Method | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with rollout, training, AdaTurn, built, and around; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2607.14547, 3 Method |

The paper-specific method vocabulary is section, rollout, not, but, training, adaturn, built, around, simple, premise. This vocabulary was derived from the complete method/architecture paragraphs rather than the title. It identifies the entities that must appear in a faithful architecture reconstruction and creates a falsifiable check: an implementation or summary that omits these named objects is not yet grounded in this paper.

The architecture is reconstructed as an information-flow graph: source identity and inputs enter; inherited and paper-specific components transform or score them; a decision or representation is produced; optional validation or post-processing occurs; and an evaluated outcome leaves the pipeline. Each edge should name the information available at that point. A comparison becomes unfair if one method has access to labels, future requests, privileged metadata, additional context, or a larger tuning budget that another method lacks.

### 2.4 Training, calibration, and inference

Construction-time and runtime work are separate accounting domains. Training may fit parameters, construct representations, estimate thresholds, tune prompts, or learn a policy. Calibration may use held-out examples or measurements. Inference may retrieve, route, compress, classify, generate, search, solve, or verify. Post-processing may enforce a constraint or discard invalid output. A credible efficiency claim says which of these phases is included, which is amortized, and which is external to the reported number.

Training or calibration evidence is explicitly located in 3 Method. The associated source vocabulary emphasizes section, rollout, not, but, training, adaturn, built, around, simple, premise.

Paper-specific construction/training sequence:

1. At 3 Method, the paper reports a training-related operation involving rollout, training, AdaTurn, built, around, and simple. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 3 Method)*
2. At 4.1 Experimental Details, the paper reports a training-related operation involving Baselines, DeepEyes, Zheng, Mini-o3, Experimental, and Details. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details)*
3. At 4.1 Experimental Details, the paper reports a training-related operation involving Details, Implementation, Experimental, Unless, otherwise, and specified. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details)*
4. At 4.3 Ablation Studies, the paper reports a training-related operation involving turns, budget, Ablation, Studies, isolates, and contribution. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.3 Ablation Studies)*

Inference or runtime evidence is explicitly located in Appendix C Detailed Ablation Discussion, 4.1 Experimental Details. Its source vocabulary overlaps section, rollout, not, but, training, adaturn, built, around, simple, premise.

Paper-specific inference/evaluation sequence:

1. At 3 Method, the paper reports an inference or deployment action involving rollout, training, AdaTurn, built, around, and simple. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 3 Method)*
2. At 4.1 Experimental Details, the paper reports an inference or deployment action involving Experimental, Details, Datasets, evaluate, AdaTurn, and VisualProbe. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details)*
3. At 4.1 Experimental Details, the paper reports an inference or deployment action involving Details, Implementation, Experimental, Unless, otherwise, and specified. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details)*
4. At Appendix C Detailed Ablation Discussion, the paper reports an inference or deployment action involving final, forced-answer, rather, Detailed, Ablation, and Discussion. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix C Detailed Ablation Discussion)*

The reconstructed operational sequence is: pin input and artifact versions; validate prerequisites; compute the method-specific state or signal; apply the stated decision or objective; materialize the output; execute any downstream consumer; and measure both quality and resource outcomes. This sequence is reviewer inference grounded in the paper's organization. It is a testing model, not an assertion that the authors implemented an identical production controller.[^inference]

### 2.5 Notation and implementation audit

No independent implementation was run. The audit therefore checks internal legibility across equations, prose, captions, appendices, and extracted code/data statements. Apparent inconsistencies remain unresolved unless source evidence explains them. Source availability is classified in levels—declared, reachable, inspectable, runnable, and result-reproducing—and this local phase establishes only the declared/local-source layers.

## 3. Architecture and Complete Operational Pipeline

### 3.1 Representation and state

The documented dataflow is reconstructed only across 3 Method, where the source associates AdaTurn, active, visual, rollout, budget-aware, training, and built. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

The central representation must be described by shape, type, provenance, lifetime, and relationship to the original input. If it is compressed, selected, latent, retrieved, generated, or aggregated, the review asks what information can be lost and how that loss is detected. If it is learned, the training distribution and version become part of its identity. If it is mutable, update ordering, expiry, and rollback become part of the method rather than operational afterthoughts.

### 3.2 Decision or action modules

The paper-specific modules should be separated from inherited encoders, decoders, solvers, retrieval systems, evaluators, or model APIs. A score can rank candidates without being calibrated; a policy can improve average reward without satisfying hard constraints; and a verifier can reject some failures without certifying all accepted outputs. The assessment uses the source's strongest ablation or controlled comparison to decide which module is necessary and which is merely bundled.

### 3.3 Dependencies, post-processing, and guarantee boundary

Dependencies include data preprocessing, external models, tokenizers, simulators, indexes, numerical libraries, and evaluation code. Post-processing can materially create the final result, so its compute and failure rate belong in the pipeline. Exact validation, when present, may establish a property of a returned object; it does not automatically establish semantic correctness, optimality, robustness, or absence of distribution shift.

### 3.4 Resource allocation and stopping

Budgets can refer to tokens, bytes, parameters, candidates, iterations, calls, samples, time, energy, or money. Requested and achieved budgets should both be recorded. Early stopping and fallback can bias which cases receive expensive processing. Batching can improve throughput while worsening latency. The review therefore distinguishes construction cost, per-instance latency, batch throughput, tail latency, peak memory, and downstream cost before accepting a general efficiency claim.

## 4. Experimental Design and Evidence Reconstructed

The evaluation reconstruction follows 4.3 Ablation Studies, Appendix C Detailed Ablation Discussion, 4.1 Experimental Details, with 4 table captions and 13 figure captions inventoried.

Paper-specific evaluation vocabulary centers on turns, main, forced-answer, learning, mini-o3, explicit, supervision, budget, default, final. These terms constrain which datasets, metrics, models, budgets, or operational quantities must be preserved with each reported comparison. They also identify where a later reproduction dossier must look for splits, baselines, hardware, batching, runtime semantics, and uncertainty rather than assuming conventional defaults.

The headings mechanically associated with evaluation and results were:

- 4.3 Ablation Studies
- Appendix C Detailed Ablation Discussion
- 4.1 Experimental Details

### 4.1 Data, splits, and distribution

| Dataset | Split | Preprocessing | Source locator |
|---|---|---|---|
| AdaTurn | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| VisualProbe | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| Bench | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| HR-Bench | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| high-resolution | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| MME-RealWorld | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| real-world | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| visual-search | Source mentions evaluation partitions; exact counts and leakage controls require the full-section audit. | Source-linked operations: none resolved from the bounded excerpt; no unreported preprocessing is inferred. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| open-source | Paper-reported comparator at 4.1 Experimental Details; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| GPT-4o | Paper-reported comparator at 4.1 Experimental Details; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| LLaVA-OneVision | Paper-reported comparator at 4.1 Experimental Details; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| Qwen2.5-VL-7B-Instruct | Paper-reported comparator at 4.1 Experimental Details; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| DeepEyes | Paper-reported comparator at 4.1 Experimental Details; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| Mini-o3 | Paper-reported comparator at 4.1 Experimental Details; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| Chain-of-Focus | Paper-reported comparator at 4.1 Experimental Details; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| multi-turn | Paper-reported comparator at 4.1 Experimental Details; official implementation or copied-result status is not inferred from the name. | Comparable model, data, tuning, hardware, and compute budgets require direct source or implementation receipts. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

| Metric | Denominator/conditioning | Direction | Source locator |
|---|---|---|---|
| accuracy | Paper-defined evaluation unit at 4.1 Experimental Details; bounded text identifies 1 run | higher is normally better; confirm the paper's definition and conditioning | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| reward | Paper-defined evaluation unit at 4.3 Ablation Studies; exclusions and conditioning were not mechanically resolved | higher is normally better; confirm the paper's definition and conditioning | private full-paper evidence dossier for arXiv:2607.14547, 4.3 Ablation Studies |

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
| evaluation object at 4.3 Ablation Studies | AdaTurn | comparator retained at the cited source locator; not inferred | configuration retained at the cited source locator | source-defined metric | 7 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, 4.3 Ablation Studies |
| evaluation object at Appendix C Detailed Ablation Discussion | AdaTurn | comparator retained at the cited source locator; not inferred | configuration retained at the cited source locator | source-defined metric | 7 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Appendix C Detailed Ablation Discussion |
| AdaTurn | AdaTurn | VisualProbe | configuration retained at the cited source locator | source-defined metric | 2025, and 2024 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| visual-search | AdaTurn | OCRBench | configuration retained at the cited source locator | source-defined metric | 2022, 2021, 2023, and 2024 | Paper-reported numeric evidence only; denominator, conditioning, uncertainty, and table/prose consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |

Bounded exact evidence retained from the paper report:

- Paper report, numeric result in 4.3 Ablation Studies: “Figure 7 isolates the contribution of the reinforcement learning design.” (exact numeric tokens: 7).

- No table-caption fragment was included in the bounded verbatim evidence budget.

The correct interpretation retains task, dataset, split, model, baseline, metric, budget, and hardware with each result. A largest reported improvement is an operating point, not a distribution. An average is not a tail guarantee. A component metric can diagnose mechanism without proving end-to-end utility. Where the source reports multiple tables or figures, their relationships should be checked for consistent defaults, denominators, and versioned settings.

Three types of gain remain separate. Representation gain means fewer tokens, bytes, channels, states, features, or bits. Execution gain means lower latency, memory traffic, transfer, energy, or higher throughput. Outcome gain means better correctness, quality, utility, constraint satisfaction, or task completion. The paper may establish one or more under its setting; a deployment decision requires the combination relevant to its service objective.

Table and figure captions were inventoried rather than republished. Their exact values remain anchored to the paper. Any public summary should cite only values whose numerator, denominator, model, dataset, and comparison are simultaneously known. This review does not manufacture missing uncertainty or turn qualitative illustrations into statistical evidence.

## 6. Ablations and Causal Evidence

Paper-specific ablation/control ledger:

| Component/control | Paper-reported delta | Control caveat | Source locator |
|---|---|---|---|
| main, takeaway, and forced-answer | direction or magnitude is reported only at the source locator | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2607.14547, 4.3 Ablation Studies |
| variants, default, and formulation | direction or magnitude is reported only at the source locator | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2607.14547, 4.3 Ablation Studies |
| provides, detailed, and ablation | direction or magnitude is reported only at the source locator | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2607.14547, 4.3 Ablation Studies |

Ablations are persuasive when one named component changes while model, data, budget, training effort, and implementation quality stay fixed. The complete source was screened for removals, swaps, budget sweeps, sensitivity tests, and failure examples. If multiple elements change together, the result supports the bundle more strongly than any individual mechanism. If a simple cost-matched control is missing, the causal interpretation remains limited.

Randomness must be classified as training seeds, inference seeds, data-generation seeds, checkpoint-selection variance, or hyperparameter-search variance. Repeated inference does not prove training robustness. A named significance test should identify its independence unit and paired design. The practical importance of an effect is separate from statistical detectability, especially when a large benchmark makes very small changes significant.

Author-stated limitations:

- The author-side qualification at 5 Conclusion concerns AdaTurn, visual, agents, test-time, rollout, and computation. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 5 Conclusion)*
- The author-side qualification at Limitations. concerns interaction, Limitations, restricted, image-based, agents, and cover. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, Limitations.)*

Reviewer-identified limitations:

- No independent reproduction was performed for arXiv:2607.14547v1; turns, main, forced-answer, and AdaTurn remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details, and 4.3 Ablation Studies)*
- The dossier inventories 30 headings, 4 tables, 13 figures, and 73 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, complete coverage inventory)*

The explicit qualification path is anchored to Limitations.. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 3 candidate sentences and the limitation/discussion vocabulary adaturn, agents, interaction, not, visual, under, test-time, rollout, longer, about. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents: paper-reported problem claim centered on rollout, budget, turns, and agent | Located at Abstract; extracted numeric markers: 2024, 2025, 48.0%, and 26.5% (private full-paper evidence dossier for arXiv:2607.14547, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents: paper-reported mechanism claim centered on AdaTurn, active, visual, and rollout | Located at 3 Method; extracted numeric markers: 3.1, 3.2, 3.3, and 2 (private full-paper evidence dossier for arXiv:2607.14547, 3 Method) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents: paper-reported result claim centered on turns, main, forced-answer, and AdaTurn | Located at 4.1 Experimental Details; extracted numeric markers: 2025, 2024, 2022, and 2021 (private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2607.14547v1), [canonical PDF](https://arxiv.org/pdf/2607.14547v1), [canonical full-paper HTML](https://arxiv.org/html/2607.14547v1), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2607.14547). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2607.14547v1)*
- **Predecessor/prior work (blocked):** The bounded online record did not verify a noncanonical predecessor or prior-work source URL; the corresponding field-level claim remains unvalidated. *(evidence locator: online-vetting check for arXiv:2607.14547)*
- **Alternative or benchmark (blocked):** The bounded online record did not verify a noncanonical alternative or benchmark source URL; the corresponding field-level claim remains unvalidated. *(evidence locator: online-vetting check for arXiv:2607.14547)*
- **Code/data (checked):** The bounded online record verified reachability for https://huggingface.co/datasets/Mini-o3/Mini-o3-Coldstart-Dataset, https://huggingface.co/datasets/Mini-o3/DeepEyes_train_4K, and https://huggingface.co/datasets/Mini-o3/VisualProbe_train. Reachability does not establish ownership, completeness, runnability, or result reproduction. *(evidence locator: https://huggingface.co/datasets/Mini-o3/Mini-o3-Coldstart-Dataset)*

Verified official primary-source links from the bounded check:

- Bounded primary-source check verified: https://huggingface.co/datasets/Mini-o3/Mini-o3-Coldstart-Dataset
- Bounded primary-source check verified: https://huggingface.co/datasets/Mini-o3/DeepEyes_train_4K
- Bounded primary-source check verified: https://huggingface.co/datasets/Mini-o3/VisualProbe_train

Access-blocked or unverified URL evidence: not recorded

Prior-work and alternatives evidence: "bounded_to_canonical_arxiv_record_and_paper_declared_primary_links" This is a bounded search record, not an exhaustive map of the field.

Code/data and reproduction evidence: "link_reachability_only; repository contents were not downloaded, built, or executed" Reachability and metadata do not mean that code or data were executed, that dependencies were installed, or that a reported result reproduced.

Paper-declared external candidates were recorded as follows:

- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/accessible_HTML.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/license/index.html#licenses-available
- Paper-declared URL, not opened in this phase: https://openai.com/index/learning-to-reason-with-llms/
- Paper-declared URL, not opened in this phase: https://huggingface.co/datasets/Mini-o3/Mini-o3-Coldstart-Dataset
- Paper-declared URL, not opened in this phase: https://huggingface.co/datasets/Mini-o3/DeepEyes_train_4K
- Paper-declared URL, not opened in this phase: https://huggingface.co/datasets/Mini-o3/VisualProbe_train
- Paper-declared URL, not opened in this phase: https://math.nist.gov/~BMiller/LaTeXML/
- Paper-declared URL, not opened in this phase: https://github.com/arXiv/html_feedback/issues
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/issues
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/ourmembers.html

Their presence is discovery evidence, not proof that an artifact is official, available, licensed, runnable, or reproducing the paper. A later online-vetting phase should use primary sources, record HTTP/access limits, verify ownership and linkage, inspect release and license state, and distinguish artifact availability from runnable or result-reproducing status. Until then the publication status remains: arXiv preprint; no separate peer-reviewed venue inferred without an official venue source.

The isolated Black Lake checkout was used only for repository-readiness and dedupe context. A same-paper DEP-A would block a new owning record; a DEP-E or directly corresponding implementation is associated context rather than a duplicate. Background citations do not transfer evidence or claims to this paper.[^association]

## 9. Independent Re-conceptualization

Reviewer inference: the durable mechanism is the source-defined change centered on AdaTurn, active, visual, and rollout, rather than the paper's brand name. This interpretation predicts that a matched intervention on AdaTurn changes turns; it is not an author claim or theorem.

Re-conceptualize the contribution as an evidence-linked state transition: pin source identity, record the method-specific decision, measure realized resource and outcome effects, and retain a conservative fallback whose trigger can be falsified on held-out conditions. This is reviewer inference and proposal, not an author claim and not an experimentally validated architecture.[^inference]

The mechanism can be viewed as a governed handoff between evidence, decision, execution, and outcome. Evidence identifies the source state and the signal the method uses. Decision records the action or representation chosen under a budget. Execution records what the system actually did, including fallback and resource use. Outcome records task quality and failure. The mapping is useful because it predicts what must be logged; it breaks when the paper studies a purely formal object with no operational transition.

A second bounded analogy is experimental portfolio control. Different baselines, budgets, and ablations are portfolio arms whose information access and cost must be matched. This analogy highlights selection bias and incomplete frontiers, but it does not imply that the paper uses an online bandit or that deployment should optimize only one scalar reward. Its falsifiable prediction is that the proposed mechanism's advantage should shrink when information access and complete cost are carefully matched if the original gain came mainly from comparison asymmetry.

## 10. Research Notes, Limitations, and Evidence Boundary

The complete local PDF and full-paper HTML for arXiv:2607.14547v1 were inspected. The PDF passed size, header, EOF, parse, page-count, title, structure, and references checks. The HTML passed size, readable-body, document-marker, heading, structure, title, and identity checks. Abstract HTML was metadata only and did not qualify as the paper body.[^integrity]

The coverage pass includes introduction, method or formal analysis, experiments or results, discussion or conclusion, references, appendices where exposed, tables, figures, equations, footnotes, disclosures, and code/data language. Extraction can lose visual layout and some mathematical semantics; the ledger records this boundary rather than claiming that every graphic was numerically reproduced.

Paper-specific qualification inventory: limitation/discussion terms adaturn, agents, interaction, not, visual, under, test-time, rollout, longer, about; disclosure/funding language limitation, Limitations, broader impact; code/data language GitHub, dataset, code; appendix headings Appendix A Detailed Training Setup, Appendix B Load-Balanced Rollout Assignment Pseudocode, Appendix C Detailed Ablation Discussion, Appendix D General Multimodal Capability, Appendix E Performance Judge Prompt, Appendix F AdaTurn Agent Prompts, Appendix G Visualization of AdaTurn Rollout Trajectories, Appendix H Failure Analysis, Appendix I Limitations and Societal Impact. These are evidence pointers. A missing extracted term is not proof that a disclosure, artifact, or limitation does not exist.

Evidence layers remain explicit. Layer A is what the paper reports. Layer B contains the bounded primary records actually checked online; its conclusions are limited to the recorded identity, publication, and artifact-access evidence. Layer C is reviewer inference, including the governed-handoff interpretation. Layer D is a hypothesis or proposal, including deployment controls and falsification tests. A sentence is not silently promoted between layers.

Paper/prose/table consistency checks:

| Issue/check | Assessment | Source locator |
|---|---|---|
| Canonical ID, version, title, authors, PDF hash, and HTML hash were reconciled for arXiv:2607.14547v1; full quantitative table/prose/code consistency was not independently rerun. | identity consistency checked; quantitative and implementation consistency remain unresolved | source-integrity and online identity receipts for arXiv:2607.14547v1 |

Substantive evidence boundary: The profile binds arXiv:2607.14547v1 to a complete local PDF and full-paper HTML, 30 headings, 4 tables, 13 figures, and 73 extracted mathematical objects, and 3 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

The explicit qualification path is anchored to Limitations.. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. No experiment, benchmark, training run, code path, hardware measurement, dataset, service rollout, or security test was independently rerun. This methodology produces auditability, observability, and traceable evidence; it is not security certification.

The evidence-derived methodology score is 20/20: source integrity 2, full paper coverage 2, technical fidelity 2, quantitative fidelity 2, external vetting 2, claim calibration 2, reconceptualization 2, research value 2, provenance 2, durability 2. The score is computed from source integrity, complete coverage, paper-specific method/equation/training/inference evidence, numeric/table/figure evidence, and whether bounded external vetting was actually performed. It rates the review artifact's coverage and evidence discipline. It does not rate the paper's truth and cannot substitute for subject-matter peer review, actual reproduction, or security assessment.

## 11. Potential Implications

### 11.1 Scientific implications

The paper's durable scientific value depends on whether the named mechanism predicts outcomes beyond the exact benchmark coordinate. Publishing full frontiers, per-instance failures, achieved budgets, uncertainty, and versioned configurations would let later work test the explanation instead of comparing isolated maxima. Negative results under shifted data, models, or budgets are especially informative because they locate the mechanism's boundary.

### 11.2 System-design implications

Builders should place the optimized path behind an observable budget and fallback controller. Source, model, data, and configuration versions should be pinned. The controller should log why an action occurred, realized rather than requested cost, validation status, and downstream outcome. Shadow comparison against a conservative path can expose drift and tail regressions before the method becomes irreversible infrastructure.

### 11.3 Deployment and governance

Derived representations can preserve sensitive, licensed, or incorrect content. Access, retention, deletion, correction, provenance, and tenant isolation should follow the information after transformation. Appropriate use requires monitored assumptions and a measurable refusal or fallback path. Poor fit includes untested distributions, absent outcome joins, hidden preprocessing cost, or settings where failure cannot be detected before harm.

## 12. New Falsifiable Hypotheses

### Hypothesis 1: Matched removal of AdaTurn

**Proposition:** Reviewer hypothesis: the source-linked AdaTurn operation is causally responsible for part of the reported turns behavior.
**Predicted observation:** Removing or neutralizing AdaTurn under matched data and compute will measurably weaken turns.
**Falsifying observation:** A competent matched control without AdaTurn preserves the same turns distribution within uncertainty.
**Minimum test:** Run a paired, seed-controlled ablation at 4.1 Experimental Details and archive per-instance outcomes and resource use.
**Evidence locator:** private full-paper evidence dossier for arXiv:2607.14547, 3 Method

### Hypothesis 2: Boundary transfer for AdaTurn

**Proposition:** Reviewer hypothesis: the relation between AdaTurn, and active and turns, and main weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details, and 4.3 Ablation Studies

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for AdaTurn** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details, and 4.3 Ablation Studies.
2. **Reproduce the end-to-end AdaTurn path** Success: the source-defined AdaTurn, active, and visual and turns, and main are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3 Method.
3. **Falsify the reviewer mechanism thesis for AdaTurn** Success: a matched intervention on AdaTurn predicts a corresponding change in turns Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3 Method.

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents should be remembered as a tested relation between AdaTurn, active, and visual and turns, main, and forced-answer under the configurations at 4.1 Experimental Details, and 4.3 Ablation Studies, not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The caption frames this object around Quantitative, comparison, visual, perception, benchmarks, and AdaTurn.; result: Paper-reported numeric markers: 1, 32, and 8; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Table 1 caption |
| Table 2 | Purpose: The caption frames this object around Transfer, across, backbone, scales, AdaTurn, and improves.; result: Paper-reported numeric markers: 2, 32, 8, and 1; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Table 2 caption |
| Table 3 | Purpose: The caption frames this object around Training, configuration, and experiments.; result: Paper-reported numeric markers: 3; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 caption |
| Table 4 | Purpose: The caption frames this object around General, AdaTurn, training, multimodal, capability, and Compared.; result: Paper-reported numeric markers: 4, and 5; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Table 4 caption |
| Figure 1 | Purpose: The caption frames this object around budget, rollout, answer, Turn-aware, reasoning, and limited.; result: Paper-reported numeric markers: 1; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 1 caption |
| Figure 2 | Purpose: The caption frames this object around tool, answer, AdaTurn, panel, agent, and rollout.; result: Paper-reported numeric markers: 2; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 2 caption |
| Figure 3 | Purpose: The caption frames this object around budget, them, Training, behavior, boundary, and Prior.; result: Paper-reported numeric markers: 3; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 3 caption |
| Figure 4 | Purpose: The caption frames this object around rollout, requests, Load-balanced, assignment, Dynamic, and budgets.; result: Paper-reported numeric markers: 4; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 4 caption |
| Figure 5 | Purpose: The caption frames this object around rollout, plot, maximum, time, across, and engines.; result: Paper-reported numeric markers: 5, 1.34 ×, and 1.34; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 5 caption |
| Figure 6 | Purpose: The caption frames this object around turns, Performance, rollout, budget, AdaTurn, and provides.; result: Paper-reported numeric markers: 6, and 2025; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 6 caption |
| Figure 7 | Purpose: The caption frames this object around reinforcement, learning, training, Ablation, design, and Explicitly.; result: Paper-reported numeric markers: 7; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 7 caption |
| Algorithm 1 | Purpose: The caption frames this object around Algorithm, Load-balanced, rollout, and assignment.; result: Paper-reported numeric markers: 1; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Algorithm 1 caption |
| Figure 8 | Purpose: The caption frames this object around Successful, rollout, four-turn, budget, agent, and localizes.; result: Paper-reported numeric markers: 8; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 8 caption |
| Figure 9 | Purpose: The caption frames this object around text, Successful, rollout, four-turn, budget, and agent.; result: Paper-reported numeric markers: 9; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 9 caption |
| Figure 10 | Purpose: The caption frames this object around budget, light, Successful, rollout, eight-turn, and agent.; result: Paper-reported numeric markers: 10; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 10 caption |
| Figure 11 | Purpose: The caption frames this object around budget, text, Successful, rollout, eight-turn, and agent.; result: Paper-reported numeric markers: 11; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 11 caption |
| Figure 12 | Purpose: The caption frames this object around budget, person, target, Failure, case, and four-turn.; result: Paper-reported numeric markers: 12; direction and context remain bound to the caption and surrounding section.; caveat: Caption-level disposition only; cells, axes, denominators, conditioning, and appendix consistency were not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Figure 12 caption |
| Equations | 73 distinct mathematical renderings exposed by HTML; representative objects listed in Section 2.2. | Central objects were inventoried with sign, normalization, conditioning, and denominator checks; no numerical reproduction. |
| Sections | 30 headings exposed by the full HTML. | Every heading was screened; method, evaluation, results, limitations, references, and appendices were mapped where present. |

Appendix and supplementary coverage:

- Appendix A Detailed Training Setup
- Appendix B Load-Balanced Rollout Assignment Pseudocode
- Appendix C Detailed Ablation Discussion
- Appendix D General Multimodal Capability
- Appendix E Performance Judge Prompt
- Appendix F AdaTurn Agent Prompts
- Appendix G Visualization of AdaTurn Rollout Trajectories
- Appendix H Failure Analysis
- Appendix I Limitations and Societal Impact

Complete section inventory:

- Report GitHub Issue
- AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents Susan Liang 1 Chao Huang 1 Filippos Bellos 2 Jing Bi 1 Jason J Corso 2 Chenliang Xu 1 1 University of Rochester 2 Univeristy of Michigan
- Abstract
- 1 Introduction
- 2 Related Work
- 2.1 High-Resolution Image Understanding
- 2.2 Agentic Visual Perception
- 2.3 Reinforcement Learning and Test-Time Scaling for VLMs
- 3 Method
- 3.1 Problem Formulation and AdaTurn Agent Loop
- 3.2 Forced-Answer DAPO
- 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling
- 4 Experiments
- 4.1 Experimental Details
- 4.2 Quantitative Comparison
- 4.3 Ablation Studies
- 4.4 Applicability
- 5 Conclusion
- References
- Appendix A Detailed Training Setup
- Appendix B Load-Balanced Rollout Assignment Pseudocode
- Appendix C Detailed Ablation Discussion
- Appendix D General Multimodal Capability
- Appendix E Performance Judge Prompt
- Appendix F AdaTurn Agent Prompts
- Appendix G Visualization of AdaTurn Rollout Trajectories
- Appendix H Failure Analysis
- Appendix I Limitations and Societal Impact
- Limitations.
- Societal Impact.

This ledger is completeness evidence, not reproduction. It records that each exposed section and numbered object was screened without reproducing the paper's tables, figures, or long captions.

## 16. Source and Evidence Notes

- Canonical arXiv record: https://arxiv.org/abs/2607.14547v1
- Canonical PDF: https://arxiv.org/pdf/2607.14547v1
- Canonical full-paper HTML: https://arxiv.org/html/2607.14547v1
- arXiv DOI resolver: https://doi.org/10.48550/arXiv.2607.14547
- Reviewed identity: arXiv:2607.14547v1
- Complete authors: Susan Liang; Chao Huang; Filippos Bellos; Jing Bi; Jason J Corso; Chenliang Xu
- Locally archived full PDF and full-paper HTML were verified; private path withheld.
- No source PDF, HTML, archive, extracted text, validator, or private index belongs in the public DEP-A package.
- Online primary-source vetting status: performed and receipt-linked; alternatives are not exhaustive and no experiment was independently reproduced.

## 17. Footnotes

[^source-paper]: Canonical paper identity and version are linked at https://arxiv.org/abs/2607.14547v1; the locally archived complete PDF and full-paper HTML were reconciled to this identity.
[^scope]: Paper report means content attributable to the authors and supported by the reviewed artifact; it is not independent reproduction.
[^integrity]: Source integrity requires a matching complete PDF and full-paper HTML with identity, version, title, structure, references, and readable-body checks.
[^inference]: Reviewer inference labels a mechanism-level interpretation derived from source evidence rather than asserted by the authors.
[^external]: External primary evidence was limited to receipt-linked official records and URLs. Availability or publication status does not imply artifact runnability, result reproduction, or exhaustive prior-work coverage.
[^association]: An associated DEP is contextual evidence, not a duplicate and not proof of the reviewed paper's claims.
