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

Reviewer inference: the durable mechanism is the source-defined change centered on AdaTurn, active, visual, and rollout, rather than the paper's brand name. This interpretation predicts that a matched intervention on AdaTurn changes Mini-o3; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to 3 Method. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

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

**Paper-reported problem:** For AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents, the formal target is bounded to the source-defined relation among rollout, turns, budget, visual, agent, AdaTurn, and budgets. The task assumptions and stakes are anchored to Abstract, and 1 Introduction; no objective outside those sections is inferred.

**Research gap reconstructed from the source:** The paper positions AdaTurn around rollout, turns, budget, AdaTurn, active, and visual. This records the authors' gap framing only; novelty, priority, generality, and superiority require the separate prior-work and evaluation audits.

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

**Formal object 1 at 1 Introduction — Formula 1 under 1 Introduction is classified as a paper-defined mathematical relation; adjacent prose centers on rollout, introduce, load-balanced, scheduler, reduces, imbalance, and the expression links times..** `1.34\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 1 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to 1 Introduction.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 1 Introduction, formal object 1.

**Formal object 2 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 2 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, Section, AdaTurn, budget, image, question, and the expression links T_{\mathrm{max}}..** `T_{\mathrm{max}}`
Variables: "T_{\\mathrm{max}}".
Sign/normalization/conditioning/surrogate audit: "Formula 2 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T_{\\mathrm{max}}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 2.

**Formal object 3 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 3 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on input, denote, user, question, image, mathrm, and the expression links Q..** `Q`
Variables: "Q".
Sign/normalization/conditioning/surrogate audit: "Formula 3 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Q; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 3.

**Formal object 4 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 4 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on input, denote, user, question, image, mathrm, and the expression links I..** `I`
Variables: "I".
Sign/normalization/conditioning/surrogate audit: "Formula 4 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: I; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 4.

**Formal object 5 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 5 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on input, denote, user, question, image, mathrm, and the expression links g..** `g`
Variables: "g".
Sign/normalization/conditioning/surrogate audit: "Formula 5 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: g; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 5.

**Formal object 6 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 6 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on input, denote, user, question, image, mathrm, and the expression links x, Q, I, T_{\mathrm{max}}..** `x=(Q,I,T_{\mathrm{max}}).`
Variables: "x, Q, I, T_{\\mathrm{max}}".
Sign/normalization/conditioning/surrogate audit: "Formula 6 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x, Q, I, T_{\\mathrm{max}}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 6.

**Formal object 7 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 7 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on turn, agent, conditions, interaction, history, and the expression links t..** `t`
Variables: "t".
Sign/normalization/conditioning/surrogate audit: "Formula 7 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: t; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 7.

**Formal object 8 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 8 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on turn, sequence, mathcal, agent, conditions, interaction, and the expression links h_{t}, left, Q, I, T_{\mathrm{max}}, y_{1}, o_{1}, ldots..** `h_{t}=\left(Q,I,T_{\mathrm{max}},(y_{1},o_{1}),\ldots,(y_{t-1},o_{t-1})\right),`
Variables: "h_{t}, left, Q, I, T_{\\mathrm{max}}, y_{1}, o_{1}, ldots, y_{t-1}, o_{t-1}, right".
Sign/normalization/conditioning/surrogate audit: "Formula 8 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: h_{t}, left, Q, I, T_{\\mathrm{max}}, y_{1}, o_{1}, ldots, y_{t-1}, o_{t-1}, right; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 8.

**Formal object 9 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 9 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on sequence, turn, mathcal, where, token, generated, and the expression links y_{t}..** `y_{t}`
Variables: "y_{t}".
Sign/normalization/conditioning/surrogate audit: "Formula 9 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{t}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 9.

**Formal object 10 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 10 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on sequence, turn, mathcal, where, token, generated, and the expression links o_{t}..** `o_{t}`
Variables: "o_{t}".
Sign/normalization/conditioning/surrogate audit: "Formula 10 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: o_{t}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 10.

**Formal object 11 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 11 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on sequence, turn, mathcal, where, token, generated, and the expression links pi, theta..** `\pi_{\theta}`
Variables: "pi, theta".
Sign/normalization/conditioning/surrogate audit: "Formula 11 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: pi, theta; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 11.

**Formal object 12 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 12 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on sequence, turn, mathcal, where, token, generated, and the expression links c_{t}\in\mathcal{C}..** `c_{t}\in\mathcal{C}`
Variables: "c_{t}\\in\\mathcal{C}".
Sign/normalization/conditioning/surrogate audit: "Formula 12 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c_{t}\\in\\mathcal{C}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 12.

**Formal object 13 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 13 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on sequence, turn, mathcal, where, token, generated, and the expression links a_{t}\in\mathcal{A}..** `a_{t}\in\mathcal{A}`
Variables: "a_{t}\\in\\mathcal{A}".
Sign/normalization/conditioning/surrogate audit: "Formula 13 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: a_{t}\\in\\mathcal{A}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 13.

**Formal object 14 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 14 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, sequence, turn, tool, observation, where, and the expression links y_{t}\sim\pi, theta, h_{t}, qquad, y_{t}\in\mathcal{C}\cup\mathcal{A}..** `y_{t}\sim\pi_{\theta}(\cdot\mid h_{t}),\qquad y_{t}\in\mathcal{C}\cup\mathcal{A}.`
Variables: "y_{t}\\sim\\pi, theta, h_{t}, qquad, y_{t}\\in\\mathcal{C}\\cup\\mathcal{A}".
Sign/normalization/conditioning/surrogate audit: "Formula 14 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{t}\\sim\\pi, theta, h_{t}, qquad, y_{t}\\in\\mathcal{C}\\cup\\mathcal{A}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 14.

**Formal object 15 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 15 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, mathrm, tool, executor, returns, observation, and the expression links y_{t}\in\mathcal{C}..** `y_{t}\in\mathcal{C}`
Variables: "y_{t}\\in\\mathcal{C}".
Sign/normalization/conditioning/surrogate audit: "Formula 15 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{t}\\in\\mathcal{C}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 15.

**Formal object 16 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 16 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, mathrm, tool, executor, returns, observation, and the expression links t, T_{\mathrm{max}}..** `t<T_{\mathrm{max}}`
Variables: "t, T_{\\mathrm{max}}".
Sign/normalization/conditioning/surrogate audit: "Formula 16 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: t, T_{\\mathrm{max}}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 16.

**Formal object 17 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 17 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, mathrm, tool, executor, returns, observation, and the expression links mathcal, E..** `\mathcal{E}`
Variables: "mathcal, E".
Sign/normalization/conditioning/surrogate audit: "Formula 17 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, E; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 17.

**Formal object 18 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 18 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, mathrm, tool, executor, returns, observation, and the expression links o_{t}, mathcal, E, I, y_{t}..** `o_{t}=\mathcal{E}(I,y_{t}),`
Variables: "o_{t}, mathcal, E, I, y_{t}".
Sign/normalization/conditioning/surrogate audit: "Formula 18 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: o_{t}, mathcal, E, I, y_{t}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 18.

**Formal object 19 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 19 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a evaluation or scoring relation; adjacent prose centers on becomes, part, next-turn, history., mathcal, rollout, and the expression links y_{t}\in\mathcal{A}..** `y_{t}\in\mathcal{A}`
Variables: "y_{t}\\in\\mathcal{A}".
Sign/normalization/conditioning/surrogate audit: "Formula 19 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{t}\\in\\mathcal{A}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 19.

**Formal object 20 at 3.1 Problem Formulation and AdaTurn Agent Loop — Formula 20 under 3.1 Problem Formulation and AdaTurn Agent Loop is classified as a evaluation or scoring relation; adjacent prose centers on answer, turn, final, becomes, part, next-turn, and the expression links y_{t}\in\mathcal{Y}, t, mathcal, C, cup, A, T_{\mathrm{max}}..** `y_{t}\in\mathcal{Y}_{t}=\begin{cases}\mathcal{C}\cup\mathcal{A},&t<T_{\mathrm{max}},\\ \mathcal{A},&t=T_{\mathrm{max}}.\end{cases}`
Variables: "y_{t}\\in\\mathcal{Y}, t, mathcal, C, cup, A, T_{\\mathrm{max}}".
Sign/normalization/conditioning/surrogate audit: "Formula 20 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{t}\\in\\mathcal{Y}, t, mathcal, C, cup, A, T_{\\mathrm{max}}; meanings remain tied to 3.1 Problem Formulation and AdaTurn Agent Loop.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.1 Problem Formulation and AdaTurn Agent Loop, formal object 20.

**Formal object 21 at 3.2 Forced-Answer DAPO — Formula 21 under 3.2 Forced-Answer DAPO is classified as a optimization objective or loss; adjacent prose centers on Policy, adopt, Decoupled, Clip, Dynamic, Sampling, and the expression links x..** `x`
Variables: "x".
Sign/normalization/conditioning/surrogate audit: "Formula 21 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 21.

**Formal object 22 at 3.2 Forced-Answer DAPO — Formula 22 under 3.2 Forced-Answer DAPO is classified as a optimization objective or loss; adjacent prose centers on Policy, adopt, Decoupled, Clip, Dynamic, Sampling, and the expression links Y, i, G..** `\{Y^{(i)}\}_{i=1}^{G}`
Variables: "Y, i, G".
Sign/normalization/conditioning/surrogate audit: "Formula 22 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, i, G; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 22.

**Formal object 23 at 3.2 Forced-Answer DAPO — Formula 23 under 3.2 Forced-Answer DAPO is classified as a optimization objective or loss; adjacent prose centers on Policy, adopt, Decoupled, Clip, Dynamic, Sampling, and the expression links R, i, G..** `\{R^{(i)}\}_{i=1}^{G}`
Variables: "R, i, G".
Sign/normalization/conditioning/surrogate audit: "Formula 23 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, i, G; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 23.

**Formal object 24 at 3.2 Forced-Answer DAPO — Formula 24 under 3.2 Forced-Answer DAPO is classified as a optimization objective or loss; adjacent prose centers on Policy, DAPO, adopt, Decoupled, Clip, Dynamic, and the expression links hat, A, i, R, G, j, mathrm, delta..** `\hat{A}^{(i)}=\frac{R^{(i)}-\frac{1}{G}\sum_{j=1}^{G}R^{(j)}}{\mathrm{Std}(\{R^{(j)}\}_{j=1}^{G})+\delta},`
Variables: "hat, A, i, R, G, j, mathrm, delta".
Sign/normalization/conditioning/surrogate audit: "Formula 24 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) G. Variables audited: hat, A, i, R, G, j, mathrm, delta; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 24.

**Formal object 25 at 3.2 Forced-Answer DAPO — Formula 25 under 3.2 Forced-Answer DAPO is classified as a optimization objective or loss; adjacent prose centers on where, dots, mathrm, rollout, delta, small, and the expression links Y, i, y, dots, T_{\mathrm{max}}}..** `Y^{(i)}=[y^{(i)}_{1},\dots,y^{(i)}_{T_{\mathrm{max}}}]`
Variables: "Y, i, y, dots, T_{\\mathrm{max}}}".
Sign/normalization/conditioning/surrogate audit: "Formula 25 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, i, y, dots, T_{\\mathrm{max}}}; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 25.

**Formal object 26 at 3.2 Forced-Answer DAPO — Formula 26 under 3.2 Forced-Answer DAPO is classified as a optimization objective or loss; adjacent prose centers on where, dots, mathrm, rollout, delta, small, and the expression links delta..** `\delta`
Variables: "delta".
Sign/normalization/conditioning/surrogate audit: "Formula 26 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: delta; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 26.

**Formal object 27 at 3.2 Forced-Answer DAPO — Formula 27 under 3.2 Forced-Answer DAPO is classified as a optimization objective or loss; adjacent prose centers on where, rollout, dots, mathrm, delta, small, and the expression links mathcal, L, theta, mathbb, E, left, i, G..** `\mathcal{L}_{\text{DAPO}}(\theta)=-\mathbb{E}\left[\frac{1}{\sum_{i=1}^{G}|Y^{(i)}|}\sum_{i=1}^{G}\sum_{k}\min\!\left(\rho_{i,k}\hat{A}_{i,k},\mathrm{clip}(\rho_{i,k},1-\epsilon_{\mathrm{low}},1+\epsilon_{\mathrm{high}})\hat{A}_{i,k}\right)\right]`
Variables: "mathcal, L, theta, mathbb, E, left, i, G, Y, k, rho, hat, A, mathrm, epsilon, right".
Sign/normalization/conditioning/surrogate audit: "Formula 27 operator audit: minimization, expectation, fraction or division; explicit negative term present; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, L, theta, mathbb, E, left, i, G, Y, k, rho, hat, A, mathrm, epsilon, right; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 27.

**Formal object 28 at 3.2 Forced-Answer DAPO — Formula 28 under 3.2 Forced-Answer DAPO is classified as a paper-defined mathematical relation; adjacent prose centers on where, token, rollout, token-wise, importance, ratio, and the expression links hat, A, i, k..** `\hat{A}_{i,k}=\hat{A}^{(i)}`
Variables: "hat, A, i, k".
Sign/normalization/conditioning/surrogate audit: "Formula 28 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, A, i, k; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 28.

**Formal object 29 at 3.2 Forced-Answer DAPO — Formula 29 under 3.2 Forced-Answer DAPO is classified as a paper-defined mathematical relation; adjacent prose centers on where, token, rollout, token-wise, importance, ratio, and the expression links k..** `k`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 29 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 29.

**Formal object 30 at 3.2 Forced-Answer DAPO — Formula 30 under 3.2 Forced-Answer DAPO is classified as a paper-defined mathematical relation; adjacent prose centers on where, token, rollout, token-wise, importance, ratio, and the expression links Y, i..** `Y^{(i)}`
Variables: "Y, i".
Sign/normalization/conditioning/surrogate audit: "Formula 30 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, i; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 30.

**Formal object 31 at 3.2 Forced-Answer DAPO — Formula 31 under 3.2 Forced-Answer DAPO is classified as a paper-defined mathematical relation; adjacent prose centers on token-wise, epsilon_, mathrm, high, advantages, where, and the expression links rho, i, k, pi, theta, left, y, x..** `\rho_{i,k}=\frac{\pi_{\theta}\!\left(y^{(i)}_{k}\mid x,y^{(i)}_{<k}\right)}{\pi_{\theta_{\mathrm{old}}}\!\left(y^{(i)}_{k}\mid x,y^{(i)}_{<k}\right)}.`
Variables: "rho, i, k, pi, theta, left, y, x, right, mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 31 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: rho, i, k, pi, theta, left, y, x, right, mathrm; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 31.

**Formal object 32 at 3.2 Forced-Answer DAPO — Formula 32 under 3.2 Forced-Answer DAPO is classified as a paper-defined mathematical relation; adjacent prose centers on epsilon_, mathrm, high, advantages, different, clip, and the expression links epsilon, mathrm..** `\epsilon_{\mathrm{low}}`
Variables: "epsilon, mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 32 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: epsilon, mathrm; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 32.

**Formal object 33 at 3.2 Forced-Answer DAPO — Formula 33 under 3.2 Forced-Answer DAPO is classified as a paper-defined mathematical relation; adjacent prose centers on epsilon_, mathrm, high, advantages, different, clip, and the expression links epsilon, mathrm..** `\epsilon_{\mathrm{high}}`
Variables: "epsilon, mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 33 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: epsilon, mathrm; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 33.

**Formal object 34 at 3.2 Forced-Answer DAPO — Formula 34 under 3.2 Forced-Answer DAPO is classified as a optimization objective or loss; adjacent prose centers on boundary, rollout., mathrm, policy, cases, central, and the expression links t, T_{\mathrm{max}}..** `t=T_{\mathrm{max}}`
Variables: "t, T_{\\mathrm{max}}".
Sign/normalization/conditioning/surrogate audit: "Formula 34 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: t, T_{\\mathrm{max}}; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 34.

**Formal object 35 at 3.2 Forced-Answer DAPO — Formula 35 under 3.2 Forced-Answer DAPO is classified as a paper-defined mathematical relation; adjacent prose centers on rollout, mathrm, tool, address, Forced-Answer, DAPO, and the expression links h_{T, mathrm..** `h_{T_{\mathrm{max}}}^{-}`
Variables: "h_{T, mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 35 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: h_{T, mathrm; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 35.

**Formal object 36 at 3.2 Forced-Answer DAPO — Formula 36 under 3.2 Forced-Answer DAPO is classified as a evaluation or scoring relation; adjacent prose centers on mathrm, rollout, tool, control, answer., address, and the expression links tilde, Y, i, T_{\mathrm{max}}, left, h_{T, mathrm, a..** `\tilde{Y}^{(i)}=\begin{cases}Y^{(i)},&\text{if }Y^{(i)}\text{ emits an answer within }T_{\mathrm{max}},\\ \left(h_{T_{\mathrm{max}}}^{-(i)},\tilde{a}_{T_{\mathrm{max}}}^{(i)}\right),&\text{if }y_{T_{\mathrm{max}}}^{(i)}\in\mathcal{C},\end{cases}`
Variables: "tilde, Y, i, T_{\\mathrm{max}}, left, h_{T, mathrm, a, T_{\\mathrm{max}}}^{, right, y_{T, in, mathcal, C".
Sign/normalization/conditioning/surrogate audit: "Formula 36 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tilde, Y, i, T_{\\mathrm{max}}, left, h_{T, mathrm, a, T_{\\mathrm{max}}}^{, right, y_{T, in, mathcal, C; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 36.

**Formal object 37 at 3.2 Forced-Answer DAPO — Formula 37 under 3.2 Forced-Answer DAPO is classified as a evaluation or scoring relation; adjacent prose centers on mathrm, where, tilde, theta, cdot, budget-exhausted, and the expression links tilde, a, T_{\mathrm{max}}}^{, i, sim, pi, theta, h_{T..** `\tilde{a}_{T_{\mathrm{max}}}^{(i)}\sim\pi_{\theta}(\cdot\mid h_{T_{\mathrm{max}}}^{-(i)},b_{T_{\mathrm{max}}})`
Variables: "tilde, a, T_{\\mathrm{max}}}^{, i, sim, pi, theta, h_{T, mathrm, b_{T".
Sign/normalization/conditioning/surrogate audit: "Formula 37 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tilde, a, T_{\\mathrm{max}}}^{, i, sim, pi, theta, h_{T, mathrm, b_{T; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 37.

**Formal object 38 at 3.2 Forced-Answer DAPO — Formula 38 under 3.2 Forced-Answer DAPO is classified as a evaluation or scoring relation; adjacent prose centers on mathrm, where, tilde, theta, cdot, budget-exhausted, and the expression links b_{T, mathrm..** `b_{T_{\mathrm{max}}}`
Variables: "b_{T, mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 38 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: b_{T, mathrm; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 38.

**Formal object 39 at 3.2 Forced-Answer DAPO — Formula 39 under 3.2 Forced-Answer DAPO is classified as a optimization objective or loss; adjacent prose centers on mathrm, where, tilde, theta, cdot, budget-exhausted, and the expression links R, i, lambda, mathrm, r_{\mathrm{acc}}, tilde, Y, g..** `R^{(i)}=\lambda_{\mathrm{acc}}\,r_{\mathrm{acc}}(\tilde{Y}^{(i)},g)+\lambda_{\mathrm{fmt}}\,r_{\mathrm{fmt}}(\tilde{Y}^{(i)}).`
Variables: "R, i, lambda, mathrm, r_{\\mathrm{acc}}, tilde, Y, g, r_{\\mathrm{fmt}}".
Sign/normalization/conditioning/surrogate audit: "Formula 39 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, i, lambda, mathrm, r_{\\mathrm{acc}}, tilde, Y, g, r_{\\mathrm{fmt}}; meanings remain tied to 3.2 Forced-Answer DAPO.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.2 Forced-Answer DAPO, formal object 39.

**Formal object 40 at 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling — Formula 40 under 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling is classified as a paper-defined mathematical relation; adjacent prose centers on rollout, engine., assigned, request, accumulated, budgets, and the expression links r_{n}..** `r_{n}`
Variables: "r_{n}".
Sign/normalization/conditioning/surrogate audit: "Formula 40 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: r_{n}; meanings remain tied to 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling, formal object 40.

**Formal object 41 at 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling — Formula 41 under 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling is classified as a paper-defined mathematical relation; adjacent prose centers on rollout, engine., assigned, request, accumulated, budgets, and the expression links T_{n}..** `T_{n}`
Variables: "T_{n}".
Sign/normalization/conditioning/surrogate audit: "Formula 41 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T_{n}; meanings remain tied to 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling, formal object 41.

**Formal object 42 at 4.2 Quantitative Comparison — Formula 42 under 4.2 Quantitative Comparison is classified as a paper-defined mathematical relation; adjacent prose centers on HR-Bench, AdaTurn, MME-RealWorld., Table, reports, main, and the expression links symbols defined beside the formula..** `+12.5\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 42 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 4.2 Quantitative Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.2 Quantitative Comparison, formal object 42.

**Formal object 43 at 4.2 Quantitative Comparison — Formula 43 under 4.2 Quantitative Comparison is classified as a paper-defined mathematical relation; adjacent prose centers on HR-Bench, AdaTurn, MME-RealWorld., Table, reports, main, and the expression links symbols defined beside the formula..** `+10.9\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 43 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 4.2 Quantitative Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.2 Quantitative Comparison, formal object 43.

**Formal object 44 at 4.2 Quantitative Comparison — Formula 44 under 4.2 Quantitative Comparison is classified as a paper-defined mathematical relation; adjacent prose centers on HR-Bench, AdaTurn, MME-RealWorld., Table, reports, main, and the expression links symbols defined beside the formula..** `+6.0\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 44 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 4.2 Quantitative Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.2 Quantitative Comparison, formal object 44.

**Formal object 45 at 4.2 Quantitative Comparison — Formula 45 under 4.2 Quantitative Comparison is classified as a paper-defined mathematical relation; adjacent prose centers on HR-Bench, AdaTurn, MME-RealWorld., Table, reports, main, and the expression links symbols defined beside the formula..** `+6.8\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 45 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 4.2 Quantitative Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.2 Quantitative Comparison, formal object 45.

**Formal object 46 at 4.2 Quantitative Comparison — Formula 46 under 4.2 Quantitative Comparison is classified as a paper-defined mathematical relation; adjacent prose centers on HR-Bench, AdaTurn, MME-RealWorld., Table, reports, main, and the expression links symbols defined beside the formula..** `+7.9\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 46 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 4.2 Quantitative Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.2 Quantitative Comparison, formal object 46.

**Formal object 47 at 4.2 Quantitative Comparison — Formula 47 under 4.2 Quantitative Comparison is classified as a paper-defined mathematical relation; adjacent prose centers on HR-Bench, AdaTurn, MME-RealWorld., Table, reports, main, and the expression links symbols defined beside the formula..** `+13.9\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 47 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 4.2 Quantitative Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.2 Quantitative Comparison, formal object 47.

**Formal object 48 at Appendix A Detailed Training Setup — Formula 48 under Appendix A Detailed Training Setup is classified as a paper-defined mathematical relation; adjacent prose centers on Mini-o3, rollout, datasets, https, huggingface.co, AdaTurn, and the expression links times..** `1\times 10^{-5}`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 48 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Appendix A Detailed Training Setup.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix A Detailed Training Setup, formal object 48.

**Formal object 49 at Appendix A Detailed Training Setup — Formula 49 under Appendix A Detailed Training Setup is classified as a paper-defined mathematical relation; adjacent prose centers on Mini-o3, rollout, datasets, https, huggingface.co, AdaTurn, and the expression links times..** `1\times 10^{-6}`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 49 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Appendix A Detailed Training Setup.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix A Detailed Training Setup, formal object 49.

**Formal object 50 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 50 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links P..** `P`
Variables: "P".
Sign/normalization/conditioning/surrogate audit: "Formula 50 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: P; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 50.

**Formal object 51 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 51 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links mathcal, S..** `\mathcal{S}`
Variables: "mathcal, S".
Sign/normalization/conditioning/surrogate audit: "Formula 51 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 51.

**Formal object 52 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 52 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links R..** `R`
Variables: "R".
Sign/normalization/conditioning/surrogate audit: "Formula 52 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 52.

**Formal object 53 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 53 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links O..** `O`
Variables: "O".
Sign/normalization/conditioning/surrogate audit: "Formula 53 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 53.

**Formal object 54 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 54 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links P_{1}, dots, P_{k}..** `P_{1},\dots,P_{k}`
Variables: "P_{1}, dots, P_{k}".
Sign/normalization/conditioning/surrogate audit: "Formula 54 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: P_{1}, dots, P_{k}; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 54.

**Formal object 55 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 55 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links k, mathcal, S..** `k=|\mathcal{S}|`
Variables: "k, mathcal, S".
Sign/normalization/conditioning/surrogate audit: "Formula 55 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k, mathcal, S; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 55.

**Formal object 56 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 56 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links i..** `i=1`
Variables: "i".
Sign/normalization/conditioning/surrogate audit: "Formula 56 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: i; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 56.

**Formal object 57 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 57 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links O_{i}\leftarrow\text{Generate}, P_{i}..** `O_{i}\leftarrow\text{Generate}(P_{i})`
Variables: "O_{i}\\leftarrow\\text{Generate}, P_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 57 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O_{i}\\leftarrow\\text{Generate}, P_{i}; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 57.

**Formal object 58 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 58 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links L, leftarrow, dots..** `L\leftarrow[0,\dots,0]`
Variables: "L, leftarrow, dots".
Sign/normalization/conditioning/surrogate audit: "Formula 58 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L, leftarrow, dots; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 58.

**Formal object 59 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 59 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links s, in, mathcal, S..** `s\in\mathcal{S}`
Variables: "s, in, mathcal, S".
Sign/normalization/conditioning/surrogate audit: "Formula 59 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s, in, mathcal, S; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 59.

**Formal object 60 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 60 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links A, leftarrow, emptyset, dots..** `A\leftarrow[\emptyset,\dots,\emptyset]`
Variables: "A, leftarrow, emptyset, dots".
Sign/normalization/conditioning/surrogate audit: "Formula 60 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: A, leftarrow, emptyset, dots; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 60.

**Formal object 61 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 61 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links symbols defined beside the formula..** `Idx`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 61 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 61.

**Formal object 62 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 62 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links R..** `R[idx]`
Variables: "R".
Sign/normalization/conditioning/surrogate audit: "Formula 62 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 62.

**Formal object 63 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 63 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links in..** `idx\in Idx`
Variables: "in".
Sign/normalization/conditioning/surrogate audit: "Formula 63 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: in; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 63.

**Formal object 64 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 64 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links s, leftarrow, L..** `s^{*}\leftarrow\arg\min_{s}L[s]`
Variables: "s, leftarrow, L".
Sign/normalization/conditioning/surrogate audit: "Formula 64 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s, leftarrow, L; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 64.

**Formal object 65 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 65 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links A, s..** `A[s^{*}]`
Variables: "A, s".
Sign/normalization/conditioning/surrogate audit: "Formula 65 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: A, s; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 65.

**Formal object 66 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 66 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links L, s, leftarrow, R..** `L[s^{*}]\leftarrow L[s^{*}]+R[idx]`
Variables: "L, s, leftarrow, R".
Sign/normalization/conditioning/surrogate audit: "Formula 66 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L, s, leftarrow, R; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 66.

**Formal object 67 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 67 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links S_{i}\in\mathcal{S}..** `S_{i}\in\mathcal{S}`
Variables: "S_{i}\\in\\mathcal{S}".
Sign/normalization/conditioning/surrogate audit: "Formula 67 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S_{i}\\in\\mathcal{S}; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 67.

**Formal object 68 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 68 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links A, i..** `A[i]`
Variables: "A, i".
Sign/normalization/conditioning/surrogate audit: "Formula 68 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: A, i; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 68.

**Formal object 69 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 69 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links O_{i}\leftarrow\text{Generate}, P, A, i..** `O_{i}\leftarrow\text{Generate}(P[A[i&#93;&#93;)`
Variables: "O_{i}\\leftarrow\\text{Generate}, P, A, i".
Sign/normalization/conditioning/surrogate audit: "Formula 69 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O_{i}\\leftarrow\\text{Generate}, P, A, i; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 69.

**Formal object 70 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 70 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links O_{i}..** `O_{i}`
Variables: "O_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 70 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O_{i}; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 70.

**Formal object 71 at Appendix B Load-Balanced Rollout Assignment Pseudocode — Formula 71 under Appendix B Load-Balanced Rollout Assignment Pseudocode is classified as a constraint or formal-analysis relation; adjacent prose centers on rollout, budget, final, forced-answer, rather, than, and the expression links O..** `\text{Concat}(O)`
Variables: "O".
Sign/normalization/conditioning/surrogate audit: "Formula 71 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O; meanings remain tied to Appendix B Load-Balanced Rollout Assignment Pseudocode.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix B Load-Balanced Rollout Assignment Pseudocode, formal object 71.

**Formal object 72 at Appendix G Visualization of AdaTurn Rollout Trajectories — Formula 72 under Appendix G Visualization of AdaTurn Rollout Trajectories is classified as a constraint or formal-analysis relation; adjacent prose centers on under, budget, Figures, successful, trajectories, model, and the expression links T_{\max}..** `T_{\max}=4`
Variables: "T_{\\max}".
Sign/normalization/conditioning/surrogate audit: "Formula 72 operator audit: maximization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T_{\\max}; meanings remain tied to Appendix G Visualization of AdaTurn Rollout Trajectories.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix G Visualization of AdaTurn Rollout Trajectories, formal object 72.

**Formal object 73 at Appendix G Visualization of AdaTurn Rollout Trajectories — Formula 73 under Appendix G Visualization of AdaTurn Rollout Trajectories is classified as a constraint or formal-analysis relation; adjacent prose centers on under, budget, Figures, successful, trajectories, model, and the expression links T_{\max}..** `T_{\max}=8`
Variables: "T_{\\max}".
Sign/normalization/conditioning/surrogate audit: "Formula 73 operator audit: maximization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T_{\\max}; meanings remain tied to Appendix G Visualization of AdaTurn Rollout Trajectories.".
Source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix G Visualization of AdaTurn Rollout Trajectories, formal object 73.

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
4. At Appendix A Detailed Training Setup, the paper reports a training-related operation involving Mini-o3, datasets, https, huggingface.co, supervised, and fine-tuning. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix A Detailed Training Setup)*

Inference or runtime evidence is explicitly located in Appendix C Detailed Ablation Discussion, 4.1 Experimental Details. Its source vocabulary overlaps section, rollout, not, but, training, adaturn, built, around, simple, premise.

Paper-specific inference/evaluation sequence:

1. At 3 Method, the paper reports an inference or deployment action involving rollout, training, AdaTurn, built, around, and simple. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 3 Method)*
2. At 4.1 Experimental Details, the paper reports an inference or deployment action involving Experimental, Details, Datasets, evaluate, AdaTurn, and VisualProbe. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details)*
3. At 4.1 Experimental Details, the paper reports an inference or deployment action involving Details, Implementation, Experimental, Unless, otherwise, and specified. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details)*
4. At Appendix A Detailed Training Setup, the paper reports an inference or deployment action involving Mini-o3, datasets, https, huggingface.co, supervised, and fine-tuning. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix A Detailed Training Setup)*

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
| HR-Bench | The evidence at 4.1 Experimental Details names partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to HR-Bench was stated in the captured paragraphs at 4.1 Experimental Details; none is imputed. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |
| ChartQA | The evidence at References names partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to ChartQA was stated in the captured paragraphs at References; none is imputed. | private full-paper evidence dossier for arXiv:2607.14547, References |
| DocVQA | The evidence at References names partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to DocVQA was stated in the captured paragraphs at References; none is imputed. | private full-paper evidence dossier for arXiv:2607.14547, References |
| Mini-o3-Coldstart-Dataset | The evidence at Appendix A Detailed Training Setup names partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to Mini-o3-Coldstart-Dataset was stated in the captured paragraphs at Appendix A Detailed Training Setup; none is imputed. | private full-paper evidence dossier for arXiv:2607.14547, Appendix A Detailed Training Setup |
| OCRBench | The evidence at Appendix D General Multimodal Capability names training partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to OCRBench was stated in the captured paragraphs at Appendix D General Multimodal Capability; none is imputed. | private full-paper evidence dossier for arXiv:2607.14547, Appendix D General Multimodal Capability |
| CV-Bench | The evidence at Appendix D General Multimodal Capability names training partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to CV-Bench was stated in the captured paragraphs at Appendix D General Multimodal Capability; none is imputed. | private full-paper evidence dossier for arXiv:2607.14547, Appendix D General Multimodal Capability |
| ScienceQA | The evidence at Appendix D General Multimodal Capability names training partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to ScienceQA was stated in the captured paragraphs at Appendix D General Multimodal Capability; none is imputed. | private full-paper evidence dossier for arXiv:2607.14547, Appendix D General Multimodal Capability |

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| hard | Table 1 lists hard as a numeric comparison row under 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling. | Neither the Table 1 caption nor its row label establishes whether hard was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 1 row hard |
| GPT-4o | Table 1 lists GPT-4o as a numeric comparison row under 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling. | Neither the Table 1 caption nor its row label establishes whether GPT-4o was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 1 row GPT-4o |
| LLaVA-OneVision | Table 1 lists LLaVA-OneVision as a numeric comparison row under 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling. | Neither the Table 1 caption nor its row label establishes whether LLaVA-OneVision was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 1 row LLaVA-OneVision |
| Qwen2.5-VL-Instruct | Table 1 lists Qwen2.5-VL-Instruct as a numeric comparison row under 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling. | Neither the Table 1 caption nor its row label establishes whether Qwen2.5-VL-Instruct was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 1 row Qwen2.5-VL-Instruct |
| Pixel Reasoner | Table 1 lists Pixel Reasoner as a numeric comparison row under 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling. | Neither the Table 1 caption nor its row label establishes whether Pixel Reasoner was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 1 row Pixel Reasoner |
| Qwen3-VL-4B-Instruct | Table 2 lists Qwen3-VL-4B-Instruct as a numeric comparison row under 4.4 Applicability. | Neither the Table 2 caption nor its row label establishes whether Qwen3-VL-4B-Instruct was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 2 row Qwen3-VL-4B-Instruct |
| Qwen3-VL-8B-Instruct | Table 2 lists Qwen3-VL-8B-Instruct as a numeric comparison row under 4.4 Applicability. | Neither the Table 2 caption nor its row label establishes whether Qwen3-VL-8B-Instruct was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 2 row Qwen3-VL-8B-Instruct |
| Batch size | Table 3 lists Batch size as a numeric comparison row under Appendix A Detailed Training Setup. | Neither the Table 3 caption nor its row label establishes whether Batch size was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 row Batch size |
| Learning rate | Table 3 lists Learning rate as a numeric comparison row under Appendix A Detailed Training Setup. | Neither the Table 3 caption nor its row label establishes whether Learning rate was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 row Learning rate |
| Epochs | Table 3 lists Epochs as a numeric comparison row under Appendix A Detailed Training Setup. | Neither the Table 3 caption nor its row label establishes whether Epochs was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 row Epochs |
| Reward weights | Table 3 lists Reward weights as a numeric comparison row under Appendix A Detailed Training Setup. | Neither the Table 3 caption nor its row label establishes whether Reward weights was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 row Reward weights |
| Minimum image pixels | Table 3 lists Minimum image pixels as a numeric comparison row under Appendix A Detailed Training Setup. | Neither the Table 3 caption nor its row label establishes whether Minimum image pixels was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 row Minimum image pixels |
| Maximum image pixels | Table 3 lists Maximum image pixels as a numeric comparison row under Appendix A Detailed Training Setup. | Neither the Table 3 caption nor its row label establishes whether Maximum image pixels was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 row Maximum image pixels |
| Dynamic rollout turns | Table 3 lists Dynamic rollout turns as a numeric comparison row under Appendix A Detailed Training Setup. | Neither the Table 3 caption nor its row label establishes whether Dynamic rollout turns was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 row Dynamic rollout turns |
| Context length | Table 3 lists Context length as a numeric comparison row under Appendix A Detailed Training Setup. | Neither the Table 3 caption nor its row label establishes whether Context length was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 row Context length |
| Compute | Table 3 lists Compute as a numeric comparison row under Appendix A Detailed Training Setup. | Neither the Table 3 caption nor its row label establishes whether Compute was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 row Compute |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

| Metric | Denominator/conditioning | Direction | Source locator |
|---|---|---|---|
| HR-Bench / 62.0 / 61.2 / 68.2 / - / 74.0 / 73.2 / 68.9 / 77.5 / 75.7 | Table 1 reports HR-Bench / 62.0 / 61.2 / 68.2 / - / 74.0 / 73.2 / 68.9 / 77.5 / 75.7 as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2607.14547, Table 1 header HR-Bench / 62.0 / 61.2 / 68.2 / - / 74.0 / 73.2 / 68.9 / 77.5 / 75.7 |
| HR-Bench / 58.3 / 54.0 / 62.7 / - / 66.9 / 69.5 / 63.2 / 73.3 / 71.1 / 73.4 | Table 1 reports HR-Bench / 58.3 / 54.0 / 62.7 / - / 66.9 / 69.5 / 63.2 / 73.3 / 71.1 / 73.4 as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2607.14547, Table 1 header HR-Bench / 58.3 / 54.0 / 62.7 / - / 66.9 / 69.5 / 63.2 / 73.3 / 71.1 / 73.4 |
| OCR-Related / OCRBench | Table 4 reports OCR-Related / OCRBench as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2607.14547, Table 4 header OCR-Related / OCRBench |
| OCR-Related / ChartQA | Table 4 reports OCR-Related / ChartQA as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2607.14547, Table 4 header OCR-Related / ChartQA |
| OCR-Related / DocVQA (val) | Table 4 reports OCR-Related / DocVQA (val) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2607.14547, Table 4 header OCR-Related / DocVQA (val) |
| General / CV-Bench | Table 4 reports General / CV-Bench as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2607.14547, Table 4 header General / CV-Bench |
| Reasoning / MathVista (testmini) | Table 4 reports Reasoning / MathVista (testmini) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2607.14547, Table 4 header Reasoning / MathVista (testmini) |
| Reasoning / ScienceQA (img) | Table 4 reports Reasoning / ScienceQA (img) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2607.14547, Table 4 header Reasoning / ScienceQA (img) |

Metrics are reconstructed with direction, denominator, aggregation unit, conditioning, and reference quality. Failures excluded from an average create survivor bias. A gap to a best-known incumbent is not a gap to a proven optimum. A judge-model score is not a human preference without validation. A compression ratio can invert depending on convention. Confidence intervals, paired tests, and effect sizes matter when differences are close or instances are correlated.

### 4.4 Hardware, batching, and runtime semantics

Quality-v2 paper-specific hardware/runtime evidence:

- At 1 Introduction, the paper's hardware/runtime paragraph names latency. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 1 Introduction)*
- At 1 Introduction, the paper's hardware/runtime paragraph names throughput. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 1 Introduction)*
- At 1 Introduction, the paper's hardware/runtime paragraph names throughput. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 1 Introduction)*
- At 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling, the paper's hardware/runtime paragraph names latency. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling)*
- At 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling, the paper's hardware/runtime paragraph names batch, latency. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling)*
- At Appendix G Visualization of AdaTurn Rollout Trajectories, the paper's hardware/runtime paragraph names under, budget, Figures, successful, trajectories, model, representative, tight. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, Appendix G Visualization of AdaTurn Rollout Trajectories)*
- At Societal Impact., the paper's hardware/runtime paragraph names latency. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, Societal Impact.)*


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
| Table 1 | Model / hard / medium / easy / V* / MME-RealWorld | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | HR-Bench / 62.0 / 61.2 / 68.2 / - / 74.0 / 73.2 / 68.9 / 77.5 / 75.7; HR-Bench / 58.3 / 54.0 / 62.7 / - / 66.9 / 69.5 / 63.2 / 73.3 / 71.1 / 73.4 | HR-Bench / 62.0 / 61.2 / 68.2 / - / 74.0 / 73.2 / 68.9 / 77.5 / 75.7=4K; HR-Bench / 58.3 / 54.0 / 62.7 / - / 66.9 / 69.5 / 63.2 / 73.3 / 71.1 / 73.4=8K | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Table 1 row 2 |
| Table 4 | Qwen2.5-VL-7B-Instruct | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | OCR-Related / OCRBench; OCR-Related / ChartQA; OCR-Related / DocVQA (val); General / CV-Bench; Reasoning / MathVista (testmini); Reasoning / ScienceQA (img) | OCR-Related / OCRBench=81.5; OCR-Related / ChartQA=79.6; OCR-Related / DocVQA (val)=94.6; General / CV-Bench=73.9; Reasoning / MathVista (testmini)=68.2; Reasoning / ScienceQA (img)=89.0 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Table 4 row 3 |
| Table 4 | Mini-o3 | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | OCR-Related / OCRBench; OCR-Related / ChartQA; OCR-Related / DocVQA (val); General / CV-Bench; Reasoning / MathVista (testmini); Reasoning / ScienceQA (img) | OCR-Related / OCRBench=83.8; OCR-Related / ChartQA=77.4; OCR-Related / DocVQA (val)=94.8; General / CV-Bench=74.4; Reasoning / MathVista (testmini)=68.8; Reasoning / ScienceQA (img)=84.5 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2607.14547, Table 4 row 5 |
| result context at Appendix C Detailed Ablation Discussion | AdaTurn | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 1.34 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2607.14547, Appendix C Detailed Ablation Discussion |
| result context at 4.1 Experimental Details | AdaTurn | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 32, 8, 1 run | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details |

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

- No independent reproduction was performed for arXiv:2607.14547v1; Mini-o3, rollout, turns, and budget remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details, and Appendix A Detailed Training Setup)*
- The dossier inventories 30 headings, 4 tables, 13 figures, and 73 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2607.14547, complete coverage inventory)*

The explicit qualification path is anchored to Limitations.. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 3 candidate sentences and the limitation/discussion vocabulary adaturn, agents, interaction, not, visual, under, test-time, rollout, longer, about. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper frames AdaTurn as a contribution to rollout, turns, budget, visual. | Problem framing is located in the profile's named introduction/problem headings; no numbered section marker is treated as a measurement. (private full-paper evidence dossier for arXiv:2607.14547, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| The reported mechanism centers on AdaTurn, active, visual, rollout. | Method and formula evidence is bound to the named method headings and formula-specific operator audits. (private full-paper evidence dossier for arXiv:2607.14547, 3 Method) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Table 1 reports measured outcomes for Model / hard / medium / easy / V* / MME-RealWorld across HR-Bench / 62.0 / 61.2 / 68.2 / - / 74.0 / 73.2 / 68.9 / 77.5 / 75.7, HR-Bench / 58.3 / 54.0 / 62.7 / - / 66.9 / 69.5 / 63.2 / 73.3 / 71.1 / 73.4. | Quality-v2 paper-report result values: 1.34, 32, 8, 1 run (private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2607.14547v1), [canonical PDF](https://arxiv.org/pdf/2607.14547v1), [canonical full-paper HTML](https://arxiv.org/html/2607.14547v1), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2607.14547). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2607.14547v1)*
- **Predecessor/prior work (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 1 Introduction; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2403.11703)*
- **Alternative or benchmark (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 4.1 Experimental Details; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2310.02255)*
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

Reviewer inference: the durable mechanism is the source-defined change centered on AdaTurn, active, visual, and rollout, rather than the paper's brand name. This interpretation predicts that a matched intervention on AdaTurn changes Mini-o3; it is not an author claim or theorem.

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

Substantive evidence boundary: The profile binds arXiv:2607.14547v1 to a complete local PDF and full-paper HTML, 30 headings, 4 tables, 13 figures, and 73 extracted mathematical objects, and 5 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

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

**Proposition:** Reviewer hypothesis: the source-linked AdaTurn operation is causally responsible for part of the reported Mini-o3 behavior.
**Predicted observation:** Removing or neutralizing AdaTurn under matched data and compute will measurably weaken Mini-o3.
**Falsifying observation:** A competent matched control without AdaTurn preserves the same Mini-o3 distribution within uncertainty.
**Minimum test:** Run a paired, seed-controlled ablation at 4.1 Experimental Details and archive per-instance outcomes and resource use.
**Evidence locator:** private full-paper evidence dossier for arXiv:2607.14547, 3 Method

### Hypothesis 2: Boundary transfer for AdaTurn

**Proposition:** Reviewer hypothesis: the relation between AdaTurn, and active and Mini-o3, and rollout weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details, and Appendix A Detailed Training Setup

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for AdaTurn** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2607.14547, 4.1 Experimental Details, and Appendix A Detailed Training Setup.
2. **Reproduce the end-to-end AdaTurn path** Success: the source-defined AdaTurn, active, and visual and Mini-o3, and rollout are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3 Method.
3. **Falsify the reviewer mechanism thesis for AdaTurn** Success: a matched intervention on AdaTurn predicts a corresponding change in Mini-o3 Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2607.14547, 3 Method.

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents should be remembered as a tested relation between AdaTurn, active, and visual and Mini-o3, rollout, and turns under the configurations at 4.1 Experimental Details, and Appendix A Detailed Training Setup, not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The Table 1 caption centers on report, Table, Quantitative, comparison, visual, perception, benchmarks.; its parsed headers include Model, GPT-4o, across 14 rows and 106 cells.; result: Model / SEAL / DyFo / Chain-of-Focus=32; VisualProbe / -=48.0; VisualProbe / -=50.4; VisualProbe / -=67.0; V* / 75.4 / 81.2 / 88.0=88.2; HR-Bench / -=77.5; HR-Bench / -=73.3; MME-RealWorld / -=65.5; caveat: Interpret Table 1 with its spanning headers and caption under 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2607.14547, Table 1 caption and object |
| Table 2 | Purpose: The Table 2 caption centers on report, Table, Transfer, across, backbone, scales., AdaTurn; its parsed headers include Model, VisualProbe, V*, HR-Bench, MME-RealWorld, hard, medium, across 12 rows and 90 cells.; result: Model=32; VisualProbe=46.3; VisualProbe=53.9; VisualProbe=69.1; V*=90.2; HR-Bench=80.0; HR-Bench=77.3; MME-RealWorld=66.0; caveat: Interpret Table 2 with its spanning headers and caption under 4.4 Applicability; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2607.14547, Table 2 caption and object |
| Table 3 | Purpose: The Table 3 caption centers on Table, Training, configuration, used, experiments.; its parsed headers include Configuration, Framework, Training data, across 20 rows and 60 cells.; result: Supervised fine-tuning / LLaMA-Factory / Mini-o3 cold-start dataset / – / 10% warmup + cosine decay / true / false=1; Supervised fine-tuning / LLaMA-Factory / Mini-o3 cold-start dataset / – / 10% warmup + cosine decay / true / false=10; Supervised fine-tuning / LLaMA-Factory / Mini-o3 cold-start dataset / – / 10% warmup + cosine decay / true / false=-5; Reinforcement learning / VERL / DeepEyes_train_4K + VisualProbe_train / 16 / 32 / none / false=1; Reinforcement learning / VERL / DeepEyes_train_4K + VisualProbe_train / 16 / 32 / none / false=10; Reinforcement learning / VERL / DeepEyes_train_4K + VisualProbe_train / 16 / 32 / none / false=-6; caveat: Interpret Table 3 with its spanning headers and caption under Appendix A Detailed Training Setup; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2607.14547, Table 3 caption and object |
| Table 4 | Purpose: The Table 4 caption centers on General, AdaTurn, training., Table, multimodal, capability, Compared; its parsed headers include OCR-Related, General, Reasoning, Model, OCRBench, ChartQA, DocVQA (val), across 6 rows and 39 cells.; result: OCR-Related / OCRBench=81.5; OCR-Related / ChartQA=79.6; OCR-Related / DocVQA (val)=94.6; General / CV-Bench=73.9; Reasoning / MathVista (testmini)=68.2; Reasoning / ScienceQA (img)=89.0; caveat: Interpret Table 4 with its spanning headers and caption under Appendix D General Multimodal Capability; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2607.14547, Table 4 caption and object |
| Figure 1 | Purpose: The Figure 1 caption identifies a quantitative plot or comparison centered on budget, rollout, when, answer., Figure, Turn-aware, reasoning, under.; result: The caption makes a qualitative claim about budget, rollout, when, answer., Figure, Turn-aware; no plotted value is inferred from pixels.; caveat: The caption under Abstract was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 1 caption and object |
| Figure 2 | Purpose: The Figure 2 caption identifies a architecture or pipeline schematic centered on tool, answer., AdaTurn., panel, agent, model, rollout, budget.; result: The caption makes a qualitative claim about tool, answer., AdaTurn., panel, agent, model; no plotted value is inferred from pixels.; caveat: The caption under 3.1 Problem Formulation and AdaTurn Agent Loop was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 2 caption and object |
| Figure 3 | Purpose: The Figure 3 caption identifies a paper-specific visual object centered on budget, them, Figure, Training, behavior, boundary., Prior, methods.; result: The caption makes a qualitative claim about budget, them, Figure, Training, behavior, boundary.; no plotted value is inferred from pixels.; caveat: The caption under 3.2 Forced-Answer DAPO was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 3 caption and object |
| Figure 4 | Purpose: The Figure 4 caption identifies a paper-specific visual object centered on rollout, requests, Figure, Load-balanced, assignment., Dynamic, budgets, create.; result: The caption makes a qualitative claim about rollout, requests, Figure, Load-balanced, assignment., Dynamic; no plotted value is inferred from pixels.; caveat: The caption under 3.2 Forced-Answer DAPO was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 4 caption and object |
| Figure 5 | Purpose: The Figure 5 caption identifies a quantitative plot or comparison centered on rollout, plot, reports, maximum, time, across, engines, Figure.; result: Caption-reported measured values: 1.34; caveat: The caption under 3.3 Dynamic Rollout Budgets and Load-Balanced Scheduling was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 5 caption and object |
| Figure 6 | Purpose: The Figure 6 caption identifies a quantitative plot or comparison centered on turns, Figure, Performance, rollout, budget., AdaTurn, provides, favorable.; result: The caption makes a qualitative claim about turns, Figure, Performance, rollout, budget., AdaTurn; no plotted value is inferred from pixels.; caveat: The caption under 4.1 Experimental Details was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 6 caption and object |
| Figure 7 | Purpose: The Figure 7 caption identifies a quantitative plot or comparison centered on reinforcement, learning, training, Figure, Ablation, design., Explicitly, final-turn.; result: The caption makes a qualitative claim about reinforcement, learning, training, Figure, Ablation, design.; no plotted value is inferred from pixels.; caveat: The caption under 4.3 Ablation Studies was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 7 caption and object |
| Algorithm 1 | Purpose: The Algorithm 1 caption identifies a paper-specific visual object centered on Algorithm, Load-balanced, rollout, assignment.; result: The caption makes a qualitative claim about Algorithm, Load-balanced, rollout, assignment; no plotted value is inferred from pixels.; caveat: The caption under Appendix B Load-Balanced Rollout Assignment Pseudocode was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Algorithm 1 caption and object |
| Figure 8 | Purpose: The Figure 8 caption identifies a architecture or pipeline schematic centered on Figure, Successful, rollout, under, four-turn, budget., agent, localizes.; result: The caption makes a qualitative claim about Figure, Successful, rollout, under, four-turn, budget.; no plotted value is inferred from pixels.; caveat: The caption under Appendix G Visualization of AdaTurn Rollout Trajectories was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 8 caption and object |
| Figure 9 | Purpose: The Figure 9 caption identifies a qualitative example or visualization centered on text, Figure, Successful, rollout, under, four-turn, budget., agent.; result: The caption makes a qualitative claim about text, Figure, Successful, rollout, under, four-turn; no plotted value is inferred from pixels.; caveat: The caption under Appendix G Visualization of AdaTurn Rollout Trajectories was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 9 caption and object |
| Figure 10 | Purpose: The Figure 10 caption identifies a paper-specific visual object centered on under, budget., light, Figure, Successful, rollout, eight-turn, agent.; result: The caption makes a qualitative claim about under, budget., light, Figure, Successful, rollout; no plotted value is inferred from pixels.; caveat: The caption under Appendix G Visualization of AdaTurn Rollout Trajectories was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 10 caption and object |
| Figure 11 | Purpose: The Figure 11 caption identifies a architecture or pipeline schematic centered on budget., text, Figure, Successful, rollout, under, eight-turn, agent.; result: The caption makes a qualitative claim about budget., text, Figure, Successful, rollout, under; no plotted value is inferred from pixels.; caveat: The caption under Appendix G Visualization of AdaTurn Rollout Trajectories was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 11 caption and object |
| Figure 12 | Purpose: The Figure 12 caption identifies a qualitative example or visualization centered on budget., person, target, Figure, Failure, case, under, four-turn.; result: The caption makes a qualitative claim about budget., person, target, Figure, Failure, case; no plotted value is inferred from pixels.; caveat: The caption under Appendix H Failure Analysis was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.14547, Figure 12 caption and object |
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
