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

Reviewer inference: the durable mechanism is the source-defined change centered on Type, across, tasks, and reasoning, rather than the paper's brand name. This interpretation predicts that a matched intervention on Type changes STOP; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to 3 Methodology: Super Token for Pruning, Robustness across Tasks and Model Scales, B.2 Model-Specific Construction Pipeline. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

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

**Formal object 1 at 2.1 Problem Definition — Formula 1 under 2.1 Problem Definition is classified as a evaluation or scoring relation; adjacent prose centers on Theta, Consider, input, query, parallel, reasoning, and the expression links Theta..** `\Theta`
Variables: "Theta".
Sign/normalization/conditioning/surrogate audit: "Formula 1 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Theta; meanings remain tied to 2.1 Problem Definition.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition, formal object 1.

**Formal object 2 at 2.1 Problem Definition — Formula 2 under 2.1 Problem Definition is classified as a evaluation or scoring relation; adjacent prose centers on Theta, Consider, input, query, parallel, reasoning, and the expression links x..** `x`
Variables: "x".
Sign/normalization/conditioning/surrogate audit: "Formula 2 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x; meanings remain tied to 2.1 Problem Definition.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition, formal object 2.

**Formal object 3 at 2.1 Problem Definition — Formula 3 under 2.1 Problem Definition is classified as a evaluation or scoring relation; adjacent prose centers on Theta, Consider, input, query, parallel, reasoning, and the expression links N..** `N`
Variables: "N".
Sign/normalization/conditioning/surrogate audit: "Formula 3 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N; meanings remain tied to 2.1 Problem Definition.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition, formal object 3.

**Formal object 4 at 2.1 Problem Definition — Formula 4 under 2.1 Problem Definition is classified as a evaluation or scoring relation; adjacent prose centers on Theta, Consider, input, query, parallel, reasoning, and the expression links T, tau, i, N..** `T=\{\tau_{i}\}_{i=1}^{N}`
Variables: "T, tau, i, N".
Sign/normalization/conditioning/surrogate audit: "Formula 4 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T, tau, i, N; meanings remain tied to 2.1 Problem Definition.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition, formal object 4.

**Formal object 5 at 2.1 Problem Definition — Formula 5 under 2.1 Problem Definition is classified as a evaluation or scoring relation; adjacent prose centers on Theta, Consider, input, query, parallel, reasoning, and the expression links tau, i, sim, P_{\Theta}, x..** `\tau_{i}\sim P_{\Theta}(x)`
Variables: "tau, i, sim, P_{\\Theta}, x".
Sign/normalization/conditioning/surrogate audit: "Formula 5 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tau, i, sim, P_{\\Theta}, x; meanings remain tied to 2.1 Problem Definition.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition, formal object 5.

**Formal object 6 at 2.1 Problem Definition — Formula 6 under 2.1 Problem Definition is classified as a evaluation or scoring relation; adjacent prose centers on Theta, Consider, input, query, parallel, reasoning, and the expression links hat, y..** `\hat{y}`
Variables: "hat, y".
Sign/normalization/conditioning/surrogate audit: "Formula 6 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, y; meanings remain tied to 2.1 Problem Definition.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition, formal object 6.

**Formal object 7 at 2.1 Problem Definition — Formula 7 under 2.1 Problem Definition is classified as a evaluation or scoring relation; adjacent prose centers on trajectories, Theta, generating, cost, Consider, input, and the expression links hat, y, tau, i, N..** `\hat{y}=\text{vote}(\{\tau_{i}\}_{i=1}^{N}).`
Variables: "hat, y, tau, i, N".
Sign/normalization/conditioning/surrogate audit: "Formula 7 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, y, tau, i, N; meanings remain tied to 2.1 Problem Definition.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition, formal object 7.

**Formal object 8 at 2.1 Problem Definition — Formula 8 under 2.1 Problem Definition is classified as a paper-defined mathematical relation; adjacent prose centers on trajectories, cost, However, generating, complete, incurs, and the expression links C, propto, N..** `C\propto N`
Variables: "C, propto, N".
Sign/normalization/conditioning/surrogate audit: "Formula 8 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C, propto, N; meanings remain tied to 2.1 Problem Definition.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 2.1 Problem Definition, formal object 8.

**Formal object 9 at The Path Pruning Formulation — Formula 9 under The Path Pruning Formulation is classified as a evaluation or scoring relation; adjacent prose centers on prefix, pruning, Formally, define, checkpoint, length, and the expression links L_{\text{prefix}}..** `L_{\text{prefix}}`
Variables: "L_{\\text{prefix}}".
Sign/normalization/conditioning/surrogate audit: "Formula 9 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{prefix}}; meanings remain tied to The Path Pruning Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation, formal object 9.

**Formal object 10 at The Path Pruning Formulation — Formula 10 under The Path Pruning Formulation is classified as a evaluation or scoring relation; adjacent prose centers on prefix, pruning, Formally, define, checkpoint, length, and the expression links mathcal, P, p_{i}\}, i, N..** `\mathcal{P}=\{p_{i}\}_{i=1}^{N}`
Variables: "mathcal, P, p_{i}\\}, i, N".
Sign/normalization/conditioning/surrogate audit: "Formula 10 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, P, p_{i}\\}, i, N; meanings remain tied to The Path Pruning Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation, formal object 10.

**Formal object 11 at The Path Pruning Formulation — Formula 11 under The Path Pruning Formulation is classified as a evaluation or scoring relation; adjacent prose centers on prefix, pruning, Formally, define, checkpoint, length, and the expression links S..** `S`
Variables: "S".
Sign/normalization/conditioning/surrogate audit: "Formula 11 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S; meanings remain tied to The Path Pruning Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation, formal object 11.

**Formal object 12 at The Path Pruning Formulation — Formula 12 under The Path Pruning Formulation is classified as a evaluation or scoring relation; adjacent prose centers on prefix, where, pruning, signal, Formally, define, and the expression links s_{i}, S, p_{i}\mid, x, Theta..** `s_{i}=S(p_{i}\mid x,\Theta),`
Variables: "s_{i}, S, p_{i}\\mid, x, Theta".
Sign/normalization/conditioning/surrogate audit: "Formula 12 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{i}, S, p_{i}\\mid, x, Theta; meanings remain tied to The Path Pruning Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation, formal object 12.

**Formal object 13 at The Path Pruning Formulation — Formula 13 under The Path Pruning Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on where, denotes, pruning, signal., Based, signals, and the expression links s_{i}\in..** `s_{i}\in[0,1]`
Variables: "s_{i}\\in".
Sign/normalization/conditioning/surrogate audit: "Formula 13 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{i}\\in; meanings remain tied to The Path Pruning Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation, formal object 13.

**Formal object 14 at The Path Pruning Formulation — Formula 14 under The Path Pruning Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on where, denotes, pruning, signal., Based, signals, and the expression links k..** `k`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 14 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to The Path Pruning Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation, formal object 14.

**Formal object 15 at The Path Pruning Formulation — Formula 15 under The Path Pruning Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on where, denotes, pruning, signal., Based, signals, and the expression links k, ll, N..** `k\ll N`
Variables: "k, ll, N".
Sign/normalization/conditioning/surrogate audit: "Formula 15 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k, ll, N; meanings remain tied to The Path Pruning Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation, formal object 15.

**Formal object 16 at The Path Pruning Formulation — Formula 16 under The Path Pruning Formulation is classified as a optimization objective or loss; adjacent prose centers on pruned, where, pruning, design, denotes, signal., and the expression links hat, y, p_{i}, s_{i}\in\{s, j, k..** `\hat{y}_{\text{pruned}}=\text{vote}(\{\text{finish}(p_{i})\mid s_{i}\in\{s_{j}\}_{j=1}^{k}\}).`
Variables: "hat, y, p_{i}, s_{i}\\in\\{s, j, k".
Sign/normalization/conditioning/surrogate audit: "Formula 16 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, y, p_{i}, s_{i}\\in\\{s, j, k; meanings remain tied to The Path Pruning Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation, formal object 16.

**Formal object 17 at The Path Pruning Formulation — Formula 17 under The Path Pruning Formulation is classified as a optimization objective or loss; adjacent prose centers on design, pruned, objective, path, pruning, maximizes, and the expression links hat, y..** `\hat{y}_{\text{pruned}}`
Variables: "hat, y".
Sign/normalization/conditioning/surrogate audit: "Formula 17 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, y; meanings remain tied to The Path Pruning Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, The Path Pruning Formulation, formal object 17.

**Formal object 18 at Components — Formula 18 under Components is classified as a probabilistic or expectation relation; adjacent prose centers on Token, STOP, LoRA, Theta, text, augment, and the expression links theta..** `\theta_{\text{LoRA}}`
Variables: "theta".
Sign/normalization/conditioning/surrogate audit: "Formula 18 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: theta; meanings remain tied to Components.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Components, formal object 18.

**Formal object 19 at Components — Formula 19 under Components is classified as a probabilistic or expectation relation; adjacent prose centers on Token, STOP, LoRA, Theta, text, augment, and the expression links W_{\text{cls}}..** `W_{\text{cls}}`
Variables: "W_{\\text{cls}}".
Sign/normalization/conditioning/surrogate audit: "Formula 19 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W_{\\text{cls}}; meanings remain tied to Components.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Components, formal object 19.

**Formal object 20 at Training: Learn to Use Internal Information — Formula 20 under Training: Learn to Use Internal Information is classified as a optimization objective or loss; adjacent prose centers on training, model, prefix, soft, process, goal, and the expression links p_{i}..** `p_{i}`
Variables: "p_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 20 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p_{i}; meanings remain tied to Training: Learn to Use Internal Information.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Training: Learn to Use Internal Information, formal object 20.

**Formal object 21 at Training: Learn to Use Internal Information — Formula 21 under Training: Learn to Use Internal Information is classified as a optimization objective or loss; adjacent prose centers on training, model, prefix, soft, process, goal, and the expression links s, i, in..** `s^{mc}_{i}\in[0,1]`
Variables: "s, i, in".
Sign/normalization/conditioning/surrogate audit: "Formula 21 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s, i, in; meanings remain tied to Training: Learn to Use Internal Information.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Training: Learn to Use Internal Information, formal object 21.

**Formal object 22 at Training: Learn to Use Internal Information — Formula 22 under Training: Learn to Use Internal Information is classified as a optimization objective or loss; adjacent prose centers on training, model, prefix, soft, process, goal, and the expression links mathcal, C, p_{i}}, p_{i}, Theta..** `\mathcal{C}_{p_{i}}=\text{LRM}(p_{i};\Theta)`
Variables: "mathcal, C, p_{i}}, p_{i}, Theta".
Sign/normalization/conditioning/surrogate audit: "Formula 22 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, p_{i}}, p_{i}, Theta; meanings remain tied to Training: Learn to Use Internal Information.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Training: Learn to Use Internal Information, formal object 22.

**Formal object 23 at Training: Learn to Use Internal Information — Formula 23 under Training: Learn to Use Internal Information is classified as a optimization objective or loss; adjacent prose centers on training, model, prefix, soft, process, goal, and the expression links T_{s}..** `T_{s}`
Variables: "T_{s}".
Sign/normalization/conditioning/surrogate audit: "Formula 23 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T_{s}; meanings remain tied to Training: Learn to Use Internal Information.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Training: Learn to Use Internal Information, formal object 23.

**Formal object 24 at Training: Learn to Use Internal Information — Formula 24 under Training: Learn to Use Internal Information is classified as a optimization objective or loss; adjacent prose centers on training, model, prefix, soft, process, goal, and the expression links h_{i}..** `h_{i}`
Variables: "h_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 24 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: h_{i}; meanings remain tied to Training: Learn to Use Internal Information.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Training: Learn to Use Internal Information, formal object 24.

**Formal object 25 at Training: Learn to Use Internal Information — Formula 25 under Training: Learn to Use Internal Information is classified as a optimization objective or loss; adjacent prose centers on text, Theta, training, model, prefix, soft, and the expression links mathcal, L, s_{i}^{mc}\log\sigma, W_{cls}h, i, s_{i}^{mc}, sigma..** `\begin{array}[]{ll}\mathcal{L}=&-[s_{i}^{mc}\log\sigma(W_{cls}h_{i})\\ &+(1-s_{i}^{mc})\log(1-\sigma(W_{cls}h_{i}))],\end{array}`
Variables: "mathcal, L, s_{i}^{mc}\\log\\sigma, W_{cls}h, i, s_{i}^{mc}, sigma".
Sign/normalization/conditioning/surrogate audit: "Formula 25 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, L, s_{i}^{mc}\\log\\sigma, W_{cls}h, i, s_{i}^{mc}, sigma; meanings remain tied to Training: Learn to Use Internal Information.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Training: Learn to Use Internal Information, formal object 25.

**Formal object 26 at Training: Learn to Use Internal Information — Formula 26 under Training: Learn to Use Internal Information is classified as a paper-defined mathematical relation; adjacent prose centers on LoRA, text, Theta, where, mathcal, and the expression links h_{i}, T_{s}\mid\mathcal{C}, p_{i}}, Theta, theta..** `h_{i}=\text{LRM}(T_{s}\mid\mathcal{C}_{p_{i}};\Theta,\theta_{\text{LoRA}})_{-1}`
Variables: "h_{i}, T_{s}\\mid\\mathcal{C}, p_{i}}, Theta, theta".
Sign/normalization/conditioning/surrogate audit: "Formula 26 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: h_{i}, T_{s}\\mid\\mathcal{C}, p_{i}}, Theta, theta; meanings remain tied to Training: Learn to Use Internal Information.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Training: Learn to Use Internal Information, formal object 26.

**Formal object 27 at Training Cost — Formula 27 under Training Cost is classified as a paper-defined mathematical relation; adjacent prose centers on cost, during, STOP, Constructing, supervision, requires, and the expression links s, i..** `s^{mc}_{i}`
Variables: "s, i".
Sign/normalization/conditioning/surrogate audit: "Formula 27 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s, i; meanings remain tied to Training Cost.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Training Cost, formal object 27.

**Formal object 28 at Training Cost — Formula 28 under Training Cost is classified as a paper-defined mathematical relation; adjacent prose centers on cost, during, STOP, Constructing, supervision, requires, and the expression links K..** `K=32`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 28 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to Training Cost.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Training Cost, formal object 28.

**Formal object 29 at Inference: “Launch-Check-Resume” — Formula 29 under Inference: “Launch-Check-Resume” is classified as a evaluation or scoring relation; adjacent prose centers on prefixes, Stage, Resume, rank, scores, apply, and the expression links uparrow..** `\uparrow`
Variables: "uparrow".
Sign/normalization/conditioning/surrogate audit: "Formula 29 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: uparrow; meanings remain tied to Inference: “Launch-Check-Resume”.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Inference: “Launch-Check-Resume”, formal object 29.

**Formal object 30 at Inference: “Launch-Check-Resume” — Formula 30 under Inference: “Launch-Check-Resume” is classified as a evaluation or scoring relation; adjacent prose centers on prefixes, Stage, Resume, rank, scores, apply, and the expression links downarrow..** `\downarrow`
Variables: "downarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 30 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: downarrow; meanings remain tied to Inference: “Launch-Check-Resume”.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Inference: “Launch-Check-Resume”, formal object 30.

**Formal object 31 at Standardized protocol. — Formula 31 under Standardized protocol. is classified as a evaluation or scoring relation; adjacent prose centers on paths., ensure, fair, comparison, establish, standardized, and the expression links symbols defined beside the formula..** `64`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 31 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Standardized protocol..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Standardized protocol., formal object 31.

**Formal object 32 at Standardized protocol. — Formula 32 under Standardized protocol. is classified as a evaluation or scoring relation; adjacent prose centers on paths., ensure, fair, comparison, establish, standardized, and the expression links symbols defined beside the formula..** `8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 32 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Standardized protocol..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Standardized protocol., formal object 32.

**Formal object 33 at Evaluation metrics. — Formula 33 under Evaluation metrics. is classified as a evaluation or scoring relation; adjacent prose centers on pruning, average, accuracy, baseline, report, metrics, and the expression links m..** `m`
Variables: "m".
Sign/normalization/conditioning/surrogate audit: "Formula 33 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: m; meanings remain tied to Evaluation metrics..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Evaluation metrics., formal object 33.

**Formal object 34 at Evaluation metrics. — Formula 34 under Evaluation metrics. is classified as a evaluation or scoring relation; adjacent prose centers on pruning, average, accuracy, baseline, report, metrics, and the expression links Delta..** `\Delta`
Variables: "Delta".
Sign/normalization/conditioning/surrogate audit: "Formula 34 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta; meanings remain tied to Evaluation metrics..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Evaluation metrics., formal object 34.

**Formal object 35 at Evaluation metrics. — Formula 35 under Evaluation metrics. is classified as a evaluation or scoring relation; adjacent prose centers on pruning, average, accuracy, baseline, report, metrics, and the expression links Delta, times..** `\Delta=\frac{\text{Tokens}_{\text{original}}-\text{Tokens}_{\text{pruned}}}{\text{Tokens}_{\text{original}}}\times 100\%.`
Variables: "Delta, times".
Sign/normalization/conditioning/surrogate audit: "Formula 35 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta, times; meanings remain tied to Evaluation metrics..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Evaluation metrics., formal object 35.

**Formal object 36 at 4.2 On the Scalability of Pruning — Formula 36 under 4.2 On the Scalability of Pruning is classified as a paper-defined mathematical relation; adjacent prose centers on compute, validating, effectiveness, practical, parallel, inference, and the expression links gamma, M, N..** `\gamma=M/N=1/2`
Variables: "gamma, M, N".
Sign/normalization/conditioning/surrogate audit: "Formula 36 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, M, N; meanings remain tied to 4.2 On the Scalability of Pruning.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 4.2 On the Scalability of Pruning, formal object 36.

**Formal object 37 at 5.1 Determining the Optimal remaining ratios — Formula 37 under 5.1 Determining the Optimal remaining ratios is classified as a optimization objective or loss; adjacent prose centers on prefix, text, task, gamma, optimal, length, and the expression links gamma..** `\gamma`
Variables: "gamma".
Sign/normalization/conditioning/surrogate audit: "Formula 37 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma; meanings remain tied to 5.1 Determining the Optimal remaining ratios.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 5.1 Determining the Optimal remaining ratios, formal object 37.

**Formal object 38 at 5.1 Determining the Optimal remaining ratios — Formula 38 under 5.1 Determining the Optimal remaining ratios is classified as a optimization objective or loss; adjacent prose centers on prefix, text, task, gamma, optimal, length, and the expression links gamma, f, C, L_{\text{prefix}}, L_{\text{task}}..** `\gamma=f(C,L_{\text{prefix}},L_{\text{task}})`
Variables: "gamma, f, C, L_{\\text{prefix}}, L_{\\text{task}}".
Sign/normalization/conditioning/surrogate audit: "Formula 38 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, f, C, L_{\\text{prefix}}, L_{\\text{task}}; meanings remain tied to 5.1 Determining the Optimal remaining ratios.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 5.1 Determining the Optimal remaining ratios, formal object 38.

**Formal object 39 at 5.1 Determining the Optimal remaining ratios — Formula 39 under 5.1 Determining the Optimal remaining ratios is classified as a optimization objective or loss; adjacent prose centers on prefix, text, task, gamma, optimal, length, and the expression links C..** `C`
Variables: "C".
Sign/normalization/conditioning/surrogate audit: "Formula 39 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C; meanings remain tied to 5.1 Determining the Optimal remaining ratios.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 5.1 Determining the Optimal remaining ratios, formal object 39.

**Formal object 40 at 5.1 Determining the Optimal remaining ratios — Formula 40 under 5.1 Determining the Optimal remaining ratios is classified as a optimization objective or loss; adjacent prose centers on prefix, text, task, gamma, optimal, length, and the expression links L_{\text{task}}..** `L_{\text{task}}`
Variables: "L_{\\text{task}}".
Sign/normalization/conditioning/surrogate audit: "Formula 40 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{task}}; meanings remain tied to 5.1 Determining the Optimal remaining ratios.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 5.1 Determining the Optimal remaining ratios, formal object 40.

**Formal object 41 at 5.1 Determining the Optimal remaining ratios — Formula 41 under 5.1 Determining the Optimal remaining ratios is classified as a optimization objective or loss; adjacent prose centers on prefix, text, gamma, task, optimal, length, and the expression links underset, f, C, L_{\text{prefix}}, L_{\text{task}}, gamma..** `\underset{f}{\arg\max}\text{ Accuracy}(C,L_{\text{prefix}},L_{\text{task}},\gamma),`
Variables: "underset, f, C, L_{\\text{prefix}}, L_{\\text{task}}, gamma".
Sign/normalization/conditioning/surrogate audit: "Formula 41 operator audit: maximization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: underset, f, C, L_{\\text{prefix}}, L_{\\text{task}}, gamma; meanings remain tied to 5.1 Determining the Optimal remaining ratios.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 5.1 Determining the Optimal remaining ratios, formal object 41.

**Formal object 42 at 5.1 Determining the Optimal remaining ratios — Formula 42 under 5.1 Determining the Optimal remaining ratios is classified as a paper-defined mathematical relation; adjacent prose centers on gamma, where, determines, proportion, paths, retained., and the expression links f..** `f`
Variables: "f".
Sign/normalization/conditioning/surrogate audit: "Formula 42 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f; meanings remain tied to 5.1 Determining the Optimal remaining ratios.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, 5.1 Determining the Optimal remaining ratios, formal object 42.

**Formal object 43 at Consistent Empirical Trends across Various Settings — Formula 43 under Consistent Empirical Trends across Various Settings is classified as a evaluation or scoring relation; adjacent prose centers on prefix, gamma, text, compute, derive, conduct, and the expression links symbols defined beside the formula..** `1/32`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 43 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Consistent Empirical Trends across Various Settings.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Consistent Empirical Trends across Various Settings, formal object 43.

**Formal object 44 at Consistent Empirical Trends across Various Settings — Formula 44 under Consistent Empirical Trends across Various Settings is classified as a evaluation or scoring relation; adjacent prose centers on prefix, gamma, text, compute, derive, conduct, and the expression links symbols defined beside the formula..** `1/2`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 44 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Consistent Empirical Trends across Various Settings.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Consistent Empirical Trends across Various Settings, formal object 44.

**Formal object 45 at Formalizing Empirical Findings — Formula 45 under Formalizing Empirical Findings is classified as a paper-defined mathematical relation; adjacent prose centers on approx, empirical, model, formulation, Building, insights, and the expression links gamma, f, C, L_{\text{prefix}}, L_{\text{task}}, b, L_{\text{prefix}}^{c}}{L, d..** `\gamma^{-1}=f(C,L_{\text{prefix}},L_{\text{task}})=aC^{b}\frac{L_{\text{prefix}}^{c}}{L_{\text{task}}^{d}}.`
Variables: "gamma, f, C, L_{\\text{prefix}}, L_{\\text{task}}, b, L_{\\text{prefix}}^{c}}{L, d".
Sign/normalization/conditioning/surrogate audit: "Formula 45 operator audit: fraction or division; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, f, C, L_{\\text{prefix}}, L_{\\text{task}}, b, L_{\\text{prefix}}^{c}}{L, d; meanings remain tied to Formalizing Empirical Findings.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings, formal object 45.

**Formal object 46 at Formalizing Empirical Findings — Formula 46 under Formalizing Empirical Findings is classified as a paper-defined mathematical relation; adjacent prose centers on approx, empirical, formulation, input, variables, normalized, and the expression links a, approx, times..** `a\approx 1.17\times 10^{4}`
Variables: "a, approx, times".
Sign/normalization/conditioning/surrogate audit: "Formula 46 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: a, approx, times; meanings remain tied to Formalizing Empirical Findings.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings, formal object 46.

**Formal object 47 at Formalizing Empirical Findings — Formula 47 under Formalizing Empirical Findings is classified as a paper-defined mathematical relation; adjacent prose centers on approx, empirical, formulation, input, variables, normalized, and the expression links b, approx..** `b\approx 0.46`
Variables: "b, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 47 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: b, approx; meanings remain tied to Formalizing Empirical Findings.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings, formal object 47.

**Formal object 48 at Formalizing Empirical Findings — Formula 48 under Formalizing Empirical Findings is classified as a paper-defined mathematical relation; adjacent prose centers on approx, empirical, formulation, input, variables, normalized, and the expression links c, approx..** `c\approx 0.40`
Variables: "c, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 48 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c, approx; meanings remain tied to Formalizing Empirical Findings.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings, formal object 48.

**Formal object 49 at Formalizing Empirical Findings — Formula 49 under Formalizing Empirical Findings is classified as a paper-defined mathematical relation; adjacent prose centers on approx, empirical, formulation, input, variables, normalized, and the expression links d, approx..** `d\approx 4.55`
Variables: "d, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 49 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d, approx; meanings remain tied to Formalizing Empirical Findings.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings, formal object 49.

**Formal object 50 at Applying the Empirical Guideline — Formula 50 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on text, task, approx, prefix, gamma, optimal, and the expression links L_{\text{task}}\approx..** `L_{\text{task}}\approx 8{,}650`
Variables: "L_{\\text{task}}\\approx".
Sign/normalization/conditioning/surrogate audit: "Formula 50 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{task}}\\approx; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 50.

**Formal object 51 at Applying the Empirical Guideline — Formula 51 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on text, task, approx, prefix, gamma, optimal, and the expression links L_{\text{prefix}}..** `L_{\text{prefix}}=2{,}048`
Variables: "L_{\\text{prefix}}".
Sign/normalization/conditioning/surrogate audit: "Formula 51 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{prefix}}; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 51.

**Formal object 52 at Applying the Empirical Guideline — Formula 52 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on text, task, approx, prefix, gamma, optimal, and the expression links C, k..** `C=158\text{k}`
Variables: "C, k".
Sign/normalization/conditioning/surrogate audit: "Formula 52 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C, k; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 52.

**Formal object 53 at Applying the Empirical Guideline — Formula 53 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on text, task, approx, prefix, gamma, optimal, and the expression links gamma, approx..** `\gamma^{-1}\approx 9.63`
Variables: "gamma, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 53 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, approx; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 53.

**Formal object 54 at Applying the Empirical Guideline — Formula 54 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on text, task, approx, prefix, gamma, optimal, and the expression links gamma, approx..** `\gamma\approx 10\%`
Variables: "gamma, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 54 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, approx; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 54.

**Formal object 55 at Applying the Empirical Guideline — Formula 55 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on text, task, approx, prefix, gamma, optimal, and the expression links L_{\text{task}}\approx, k..** `L_{\text{task}}\approx 12\text{k}`
Variables: "L_{\\text{task}}\\approx, k".
Sign/normalization/conditioning/surrogate audit: "Formula 55 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{task}}\\approx, k; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 55.

**Formal object 56 at Applying the Empirical Guideline — Formula 56 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on text, task, approx, prefix, gamma, optimal, and the expression links L_{\text{prefix}}, k..** `L_{\text{prefix}}=3\text{k}`
Variables: "L_{\\text{prefix}}, k".
Sign/normalization/conditioning/surrogate audit: "Formula 56 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{prefix}}, k; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 56.

**Formal object 57 at Applying the Empirical Guideline — Formula 57 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on text, task, approx, prefix, gamma, optimal, and the expression links C, k..** `C=275\text{k}`
Variables: "C, k".
Sign/normalization/conditioning/surrogate audit: "Formula 57 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C, k; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 57.

**Formal object 58 at Applying the Empirical Guideline — Formula 58 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on text, task, approx, prefix, gamma, optimal, and the expression links gamma, approx..** `\gamma^{-1}\approx 3.36`
Variables: "gamma, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 58 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, approx; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 58.

**Formal object 59 at Applying the Empirical Guideline — Formula 59 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on predictions, consistent, empirical, observations, indicating, scaling, and the expression links L_{\text{prefix}}..** `L_{\text{prefix}}=512`
Variables: "L_{\\text{prefix}}".
Sign/normalization/conditioning/surrogate audit: "Formula 59 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{prefix}}; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 59.

**Formal object 60 at Applying the Empirical Guideline — Formula 60 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on predictions, consistent, empirical, observations, indicating, scaling, and the expression links L_{\text{prefix}}..** `L_{\text{prefix}}=1024`
Variables: "L_{\\text{prefix}}".
Sign/normalization/conditioning/surrogate audit: "Formula 60 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{prefix}}; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 60.

**Formal object 61 at Applying the Empirical Guideline — Formula 61 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on predictions, consistent, empirical, observations, indicating, scaling, and the expression links L_{\text{prefix}}..** `L_{\text{prefix}}=2048`
Variables: "L_{\\text{prefix}}".
Sign/normalization/conditioning/surrogate audit: "Formula 61 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{prefix}}; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 61.

**Formal object 62 at Applying the Empirical Guideline — Formula 62 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on predictions, consistent, empirical, observations, indicating, scaling, and the expression links L_{\text{prefix}}..** `L_{\text{prefix}}=4096`
Variables: "L_{\\text{prefix}}".
Sign/normalization/conditioning/surrogate audit: "Formula 62 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{prefix}}; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 62.

**Formal object 63 at Applying the Empirical Guideline — Formula 63 under Applying the Empirical Guideline is classified as a paper-defined mathematical relation; adjacent prose centers on predictions, consistent, empirical, observations, indicating, scaling, and the expression links gamma..** `\gamma^{-1}`
Variables: "gamma".
Sign/normalization/conditioning/surrogate audit: "Formula 63 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma; meanings remain tied to Applying the Empirical Guideline.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Applying the Empirical Guideline, formal object 63.

**Formal object 64 at Ablation: Quality of the Supervision Signal — Formula 64 under Ablation: Quality of the Supervision Signal is classified as a constraint or formal-analysis relation; adjacent prose centers on soft, labels, STOP, supervision, improves, uses, and the expression links s..** `s^{mc}`
Variables: "s".
Sign/normalization/conditioning/surrogate audit: "Formula 64 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s; meanings remain tied to Ablation: Quality of the Supervision Signal.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Ablation: Quality of the Supervision Signal, formal object 64.

**Formal object 65 at Ablation: Quality of the Supervision Signal — Formula 65 under Ablation: Quality of the Supervision Signal is classified as a constraint or formal-analysis relation; adjacent prose centers on soft, labels, STOP, supervision, improves, uses, and the expression links K..** `K=1`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 65 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to Ablation: Quality of the Supervision Signal.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Ablation: Quality of the Supervision Signal, formal object 65.

**Formal object 66 at Ablation: Sensitivity to Design Choices — Formula 66 under Ablation: Sensitivity to Design Choices is classified as a paper-defined mathematical relation; adjacent prose centers on further, STOP, tokens, Table, performance, capacity, and the expression links r..** `r=128`
Variables: "r".
Sign/normalization/conditioning/surrogate audit: "Formula 66 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: r; meanings remain tied to Ablation: Sensitivity to Design Choices.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Ablation: Sensitivity to Design Choices, formal object 66.

**Formal object 67 at Findings 5 . — Formula 67 under Findings 5 . is classified as a optimization objective or loss; adjacent prose centers on STOP, Type, latency, single, overhead, robust, and the expression links symbols defined beside the formula..** `|`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 67 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Findings 5 ..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Findings 5 ., formal object 67.

**Formal object 68 at Analysis: Computational Overhead — Formula 68 under Analysis: Computational Overhead is classified as a optimization objective or loss; adjacent prose centers on Type, latency, single, overhead, STOP, quantify, and the expression links symbols defined beside the formula..** `2,048`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 68 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Analysis: Computational Overhead.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Analysis: Computational Overhead, formal object 68.

**Formal object 69 at Analysis: Generalization to Non-Math/STEM Tasks — Formula 69 under Analysis: Generalization to Non-Math/STEM Tasks is classified as a evaluation or scoring relation; adjacent prose centers on reasoning, STOP, evaluate, assess, whether, captures, and the expression links leq..** `\leq 4`
Variables: "leq".
Sign/normalization/conditioning/surrogate audit: "Formula 69 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: leq; meanings remain tied to Analysis: Generalization to Non-Math/STEM Tasks.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Analysis: Generalization to Non-Math/STEM Tasks, formal object 69.

**Formal object 70 at Analysis: Generalization to Tool Use — Formula 70 under Analysis: Generalization to Tool Use is classified as a evaluation or scoring relation; adjacent prose centers on STOP, baseline, competition, problems, under, reasoning, and the expression links rightarrow..** `\rightarrow`
Variables: "rightarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 70 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: rightarrow; meanings remain tied to Analysis: Generalization to Tool Use.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Analysis: Generalization to Tool Use, formal object 70.

**Formal object 71 at Limitations. — Formula 71 under Limitations. is classified as a evaluation or scoring relation; adjacent prose centers on models, Verification, Extreme, Scales, current, evaluation, and the expression links N..** `N=64`
Variables: "N".
Sign/normalization/conditioning/surrogate audit: "Formula 71 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N; meanings remain tied to Limitations..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Limitations., formal object 71.

**Formal object 72 at Limitations. — Formula 72 under Limitations. is classified as a evaluation or scoring relation; adjacent prose centers on models, Verification, Extreme, Scales, current, evaluation, and the expression links N, geq..** `N\geq 1000`
Variables: "N, geq".
Sign/normalization/conditioning/surrogate audit: "Formula 72 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N, geq; meanings remain tied to Limitations..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Limitations., formal object 72.

**Formal object 73 at Future Directions. — Formula 73 under Future Directions. is classified as a optimization objective or loss; adjacent prose centers on Progressive, Multi-Stage, Pruning, natural, extension, apply, and the expression links to..** `64\to 32\to 16`
Variables: "to".
Sign/normalization/conditioning/surrogate audit: "Formula 73 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: to; meanings remain tied to Future Directions..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Future Directions., formal object 73.

**Formal object 74 at Difficulty Stratification (Filtering). — Formula 74 under Difficulty Stratification (Filtering). is classified as a constraint or formal-analysis relation; adjacent prose centers on problems, model, samples, correct, answers, Before, and the expression links N..** `N=32`
Variables: "N".
Sign/normalization/conditioning/surrogate audit: "Formula 74 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N; meanings remain tied to Difficulty Stratification (Filtering)..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Difficulty Stratification (Filtering)., formal object 74.

**Formal object 75 at Difficulty Stratification (Filtering). — Formula 75 under Difficulty Stratification (Filtering). is classified as a constraint or formal-analysis relation; adjacent prose centers on problems, model, samples, correct, answers, Before, and the expression links symbols defined beside the formula..** `>28`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 75 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Difficulty Stratification (Filtering)..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Difficulty Stratification (Filtering)., formal object 75.

**Formal object 76 at Difficulty Stratification (Filtering). — Formula 76 under Difficulty Stratification (Filtering). is classified as a constraint or formal-analysis relation; adjacent prose centers on problems, model, samples, correct, answers, Before, and the expression links symbols defined beside the formula..** `<4`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 76 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Difficulty Stratification (Filtering)..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Difficulty Stratification (Filtering)., formal object 76.

**Formal object 77 at Prefix Generation. — Formula 77 under Prefix Generation. is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, retained, problems, generate, forms, part, and the expression links p..** `p`
Variables: "p".
Sign/normalization/conditioning/surrogate audit: "Formula 77 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p; meanings remain tied to Prefix Generation..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Prefix Generation., formal object 77.

**Formal object 78 at Potential Estimation via MC Rollouts. — Formula 78 under Potential Estimation via MC Rollouts. is classified as a paper-defined mathematical relation; adjacent prose centers on prime, estimate, potential, prefix, generate, continuations, and the expression links symbols defined beside the formula..** `0.6`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 78 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Potential Estimation via MC Rollouts..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Potential Estimation via MC Rollouts., formal object 78.

**Formal object 79 at Potential Estimation via MC Rollouts. — Formula 79 under Potential Estimation via MC Rollouts. is classified as a paper-defined mathematical relation; adjacent prose centers on prime, estimate, potential, prefix, generate, continuations, and the expression links tau, prime, ldots, K..** `\{\tau^{\prime}_{1},\tau^{\prime}_{2},\ldots,\tau^{\prime}_{K}\}`
Variables: "tau, prime, ldots, K".
Sign/normalization/conditioning/surrogate audit: "Formula 79 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tau, prime, ldots, K; meanings remain tied to Potential Estimation via MC Rollouts..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Potential Estimation via MC Rollouts., formal object 79.

**Formal object 80 at MC Score Calculation. — Formula 80 under MC Score Calculation. is classified as a probabilistic or expectation relation; adjacent prose centers on evaluate, response, correctness, correct, otherwise, MC-estimated, and the expression links s, K, j, tau, prime..** `s^{mc}=\frac{1}{K}\sum_{j=1}^{K}\text{is\_correct}(\tau^{\prime}_{j}).`
Variables: "s, K, j, tau, prime".
Sign/normalization/conditioning/surrogate audit: "Formula 80 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) K. Variables audited: s, K, j, tau, prime; meanings remain tied to MC Score Calculation..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, MC Score Calculation., formal object 80.

**Formal object 81 at MC Score Calculation. — Formula 81 under MC Score Calculation. is classified as a evaluation or scoring relation; adjacent prose centers on resulting, label, provides, fine-grained, probabilistic, target, and the expression links s, in..** `s^{mc}\in[0.0,1.0]`
Variables: "s, in".
Sign/normalization/conditioning/surrogate audit: "Formula 81 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s, in; meanings remain tied to MC Score Calculation..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, MC Score Calculation., formal object 81.

**Formal object 82 at Data Statistics and Insights. — Formula 82 under Data Statistics and Insights. is classified as a constraint or formal-analysis relation; adjacent prose centers on model, training, larger, Table, summarizes, composition, and the expression links symbols defined beside the formula..** `>28/32`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 82 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Data Statistics and Insights..".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, Data Statistics and Insights., formal object 82.

**Formal object 83 at B.3 Training Cost Details — Formula 83 under B.3 Training Cost Details is classified as a paper-defined mathematical relation; adjacent prose centers on costs, data, construction, training, provide, correspond, and the expression links times..** `\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 83 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to B.3 Training Cost Details.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, B.3 Training Cost Details, formal object 83.

**Formal object 84 at B.3 Training Cost Details — Formula 84 under B.3 Training Cost Details is classified as a paper-defined mathematical relation; adjacent prose centers on costs, data, construction, training, provide, correspond, and the expression links times..** `2\times 10^{-5}`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 84 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to B.3 Training Cost Details.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, B.3 Training Cost Details, formal object 84.

**Formal object 85 at B.3 Training Cost Details — Formula 85 under B.3 Training Cost Details is classified as a paper-defined mathematical relation; adjacent prose centers on costs, data, construction, training, provide, correspond, and the expression links r..** `r`
Variables: "r".
Sign/normalization/conditioning/surrogate audit: "Formula 85 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: r; meanings remain tied to B.3 Training Cost Details.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, B.3 Training Cost Details, formal object 85.

**Formal object 86 at B.3 Training Cost Details — Formula 86 under B.3 Training Cost Details is classified as a paper-defined mathematical relation; adjacent prose centers on costs, data, construction, training, provide, correspond, and the expression links alpha..** `\alpha`
Variables: "alpha".
Sign/normalization/conditioning/surrogate audit: "Formula 86 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: alpha; meanings remain tied to B.3 Training Cost Details.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, B.3 Training Cost Details, formal object 86.

**Formal object 87 at C.1 Infrastructure and Sampling Configuration — Formula 87 under C.1 Infrastructure and Sampling Configuration is classified as a paper-defined mathematical relation; adjacent prose centers on models, Configuration., generation, tokens, Sampling, ensure, and the expression links symbols defined beside the formula..** `0.95`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 87 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to C.1 Infrastructure and Sampling Configuration.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, C.1 Infrastructure and Sampling Configuration, formal object 87.

**Formal object 88 at C.1 Infrastructure and Sampling Configuration — Formula 88 under C.1 Infrastructure and Sampling Configuration is classified as a paper-defined mathematical relation; adjacent prose centers on models, Configuration., generation, tokens, Sampling, ensure, and the expression links symbols defined beside the formula..** `40`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 88 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to C.1 Infrastructure and Sampling Configuration.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, C.1 Infrastructure and Sampling Configuration, formal object 88.

**Formal object 89 at C.1 Infrastructure and Sampling Configuration — Formula 89 under C.1 Infrastructure and Sampling Configuration is classified as a paper-defined mathematical relation; adjacent prose centers on models, Configuration., generation, tokens, Sampling, ensure, and the expression links symbols defined beside the formula..** `16{,}384`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 89 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to C.1 Infrastructure and Sampling Configuration.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, C.1 Infrastructure and Sampling Configuration, formal object 89.

**Formal object 90 at C.1 Infrastructure and Sampling Configuration — Formula 90 under C.1 Infrastructure and Sampling Configuration is classified as a paper-defined mathematical relation; adjacent prose centers on models, Configuration., generation, tokens, Sampling, ensure, and the expression links symbols defined beside the formula..** `32{,}768`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 90 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to C.1 Infrastructure and Sampling Configuration.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, C.1 Infrastructure and Sampling Configuration, formal object 90.

**Formal object 91 at D.1 Motivation and Setup — Formula 91 under D.1 Motivation and Setup is classified as a probabilistic or expectation relation; adjacent prose centers on Type, external, Model, quality, data., STOP, and the expression links symbols defined beside the formula..** `{}^{\text{retrain}}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 91 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to D.1 Motivation and Setup.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, D.1 Motivation and Setup, formal object 91.

**Formal object 92 at E.1 Empirical Observations on Optimal Retention — Formula 92 under E.1 Empirical Observations on Optimal Retention is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, study, optimal, retention, ratio, gamma, and the expression links gamma..** `\gamma^{*}`
Variables: "gamma".
Sign/normalization/conditioning/surrogate audit: "Formula 92 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 92.

**Formal object 93 at E.1 Empirical Observations on Optimal Retention — Formula 93 under E.1 Empirical Observations on Optimal Retention is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, gamma, text, increases., GPQA, optimal, and the expression links symbols defined beside the formula..** `1024`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 93 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 93.

**Formal object 94 at E.1 Empirical Observations on Optimal Retention — Formula 94 under E.1 Empirical Observations on Optimal Retention is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, gamma, text, increases., GPQA, optimal, and the expression links symbols defined beside the formula..** `1/8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 94 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 94.

**Formal object 95 at E.1 Empirical Observations on Optimal Retention — Formula 95 under E.1 Empirical Observations on Optimal Retention is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, gamma, text, increases., GPQA, optimal, and the expression links sim..** `\sim 24`
Variables: "sim".
Sign/normalization/conditioning/surrogate audit: "Formula 95 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sim; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 95.

**Formal object 96 at E.1 Empirical Observations on Optimal Retention — Formula 96 under E.1 Empirical Observations on Optimal Retention is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, gamma, text, increases., GPQA, optimal, and the expression links symbols defined beside the formula..** `195`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 96 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 96.

**Formal object 97 at E.1 Empirical Observations on Optimal Retention — Formula 97 under E.1 Empirical Observations on Optimal Retention is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, gamma, text, increases., GPQA, optimal, and the expression links gamma, approx..** `\gamma\approx 1/16`
Variables: "gamma, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 97 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, approx; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 97.

**Formal object 98 at E.1 Empirical Observations on Optimal Retention — Formula 98 under E.1 Empirical Observations on Optimal Retention is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, gamma, text, increases., GPQA, optimal, and the expression links gamma..** `\gamma=1/2`
Variables: "gamma".
Sign/normalization/conditioning/surrogate audit: "Formula 98 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 98.

**Formal object 99 at E.1 Empirical Observations on Optimal Retention — Formula 99 under E.1 Empirical Observations on Optimal Retention is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, gamma, text, increases., GPQA, optimal, and the expression links gamma, approx..** `\gamma\approx 1/28`
Variables: "gamma, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 99 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, approx; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 99.

**Formal object 100 at E.1 Empirical Observations on Optimal Retention — Formula 100 under E.1 Empirical Observations on Optimal Retention is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, Mathematical, AIME, gamma, Reasoning, higher, and the expression links gamma, approx..** `\gamma\approx 1/2`
Variables: "gamma, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 100 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, approx; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 100.

**Formal object 101 at E.1 Empirical Observations on Optimal Retention — Formula 101 under E.1 Empirical Observations on Optimal Retention is classified as a paper-defined mathematical relation; adjacent prose centers on prefix, Mathematical, AIME, gamma, Reasoning, higher, and the expression links gamma, approx..** `\gamma\approx 1/4`
Variables: "gamma, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 101 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, approx; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 101.

**Formal object 102 at E.1 Empirical Observations on Optimal Retention — Formula 102 under E.1 Empirical Observations on Optimal Retention is classified as a probabilistic or expectation relation; adjacent prose centers on prefix, text, longer, gamma, When, context, and the expression links gamma, in..** `\gamma\in[1/6,1/8]`
Variables: "gamma, in".
Sign/normalization/conditioning/surrogate audit: "Formula 102 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, in; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 102.

**Formal object 103 at E.1 Empirical Observations on Optimal Retention — Formula 103 under E.1 Empirical Observations on Optimal Retention is classified as a optimization objective or loss; adjacent prose centers on Scaling, Interaction, Across, compute, budget, optimal, and the expression links L_{prefix}..** `L_{prefix}=2048`
Variables: "L_{prefix}".
Sign/normalization/conditioning/surrogate audit: "Formula 103 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{prefix}; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 103.

**Formal object 104 at E.1 Empirical Observations on Optimal Retention — Formula 104 under E.1 Empirical Observations on Optimal Retention is classified as a optimization objective or loss; adjacent prose centers on Scaling, Interaction, Across, compute, budget, optimal, and the expression links L_{prefix}..** `L_{prefix}=4096`
Variables: "L_{prefix}".
Sign/normalization/conditioning/surrogate audit: "Formula 104 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{prefix}; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 104.

**Formal object 105 at E.1 Empirical Observations on Optimal Retention — Formula 105 under E.1 Empirical Observations on Optimal Retention is classified as a optimization objective or loss; adjacent prose centers on Scaling, Interaction, Across, compute, budget, optimal, and the expression links L_{prefix}..** `L_{prefix}=512`
Variables: "L_{prefix}".
Sign/normalization/conditioning/surrogate audit: "Formula 105 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{prefix}; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 105.

**Formal object 106 at E.1 Empirical Observations on Optimal Retention — Formula 106 under E.1 Empirical Observations on Optimal Retention is classified as a optimization objective or loss; adjacent prose centers on Scaling, Interaction, Across, compute, budget, optimal, and the expression links L_{prefix}..** `L_{prefix}=1024`
Variables: "L_{prefix}".
Sign/normalization/conditioning/surrogate audit: "Formula 106 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{prefix}; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 106.

**Formal object 107 at E.1 Empirical Observations on Optimal Retention — Formula 107 under E.1 Empirical Observations on Optimal Retention is classified as a optimization objective or loss; adjacent prose centers on Scaling, Interaction, Across, compute, budget, optimal, and the expression links L_{\text{task}}\approx..** `L_{\text{task}}\approx 11{,}950`
Variables: "L_{\\text{task}}\\approx".
Sign/normalization/conditioning/surrogate audit: "Formula 107 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{\\text{task}}\\approx; meanings remain tied to E.1 Empirical Observations on Optimal Retention.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.1 Empirical Observations on Optimal Retention, formal object 107.

**Formal object 108 at E.2 Recommended Retention Guidelines — Formula 108 under E.2 Recommended Retention Guidelines is classified as a paper-defined mathematical relation; adjacent prose centers on task, length, prefix, tables, intended, primarily, and the expression links L_{task}..** `L_{task}`
Variables: "L_{task}".
Sign/normalization/conditioning/surrogate audit: "Formula 108 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{task}; meanings remain tied to E.2 Recommended Retention Guidelines.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.2 Recommended Retention Guidelines, formal object 108.

**Formal object 109 at E.2 Recommended Retention Guidelines — Formula 109 under E.2 Recommended Retention Guidelines is classified as a paper-defined mathematical relation; adjacent prose centers on task, length, prefix, tables, intended, primarily, and the expression links L_{prefix}..** `L_{prefix}`
Variables: "L_{prefix}".
Sign/normalization/conditioning/surrogate audit: "Formula 109 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{prefix}; meanings remain tied to E.2 Recommended Retention Guidelines.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.2 Recommended Retention Guidelines, formal object 109.

**Formal object 110 at E.2 Recommended Retention Guidelines — Formula 110 under E.2 Recommended Retention Guidelines is classified as a paper-defined mathematical relation; adjacent prose centers on tasks, task, approx, Tables, report, recommended, and the expression links L_{task}\approx..** `L_{task}\approx 8{,}650`
Variables: "L_{task}\\approx".
Sign/normalization/conditioning/surrogate audit: "Formula 110 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{task}\\approx; meanings remain tied to E.2 Recommended Retention Guidelines.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.2 Recommended Retention Guidelines, formal object 110.

**Formal object 111 at E.2 Recommended Retention Guidelines — Formula 111 under E.2 Recommended Retention Guidelines is classified as a paper-defined mathematical relation; adjacent prose centers on tasks, task, approx, Tables, report, recommended, and the expression links L_{task}\approx..** `L_{task}\approx 11{,}950`
Variables: "L_{task}\\approx".
Sign/normalization/conditioning/surrogate audit: "Formula 111 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{task}\\approx; meanings remain tied to E.2 Recommended Retention Guidelines.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, E.2 Recommended Retention Guidelines, formal object 111.

**Formal object 112 at F.1 Metric Definitions — Formula 112 under F.1 Metric Definitions is classified as a evaluation or scoring relation; adjacent prose centers on Time, Generation, text, wall-clock, required, autoregressive, and the expression links T_{\text{gen}}..** `T_{\text{gen}}`
Variables: "T_{\\text{gen}}".
Sign/normalization/conditioning/surrogate audit: "Formula 112 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T_{\\text{gen}}; meanings remain tied to F.1 Metric Definitions.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, F.1 Metric Definitions, formal object 112.

**Formal object 113 at F.1 Metric Definitions — Formula 113 under F.1 Metric Definitions is classified as a evaluation or scoring relation; adjacent prose centers on verify, Verification, Latency, text, explicit, computation, and the expression links T_{\text{verify}}..** `T_{\text{verify}}`
Variables: "T_{\\text{verify}}".
Sign/normalization/conditioning/surrogate audit: "Formula 113 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T_{\\text{verify}}; meanings remain tied to F.1 Metric Definitions.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, F.1 Metric Definitions, formal object 113.

**Formal object 114 at F.2 Quantitative Analysis — Formula 114 under F.2 Quantitative Analysis is classified as a paper-defined mathematical relation; adjacent prose centers on throughput, verification, latency, methods., generation., Table, and the expression links symbols defined beside the formula..** `<3\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 114 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to F.2 Quantitative Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2604.16029, F.2 Quantitative Analysis, formal object 114.

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
2. At B.1 Source Benchmarks and Decontamination, the paper reports a training-related operation involving AIME, Benchmarks, dataset, mathematical, Specifically, and GPQA. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, B.1 Source Benchmarks and Decontamination)*
3. At Appendix C Detailed Experimental Settings, the paper reports a training-related operation involving Experimental, Detailed, Settings, complete, details, and ensure. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Appendix C Detailed Experimental Settings)*
4. At C.2 Evaluation Protocol, the paper reports a training-related operation involving Evaluation, questions, training, Protocol, strictly, and adhered. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, C.2 Evaluation Protocol)*

Inference or runtime evidence is explicitly located in B.2 Model-Specific Construction Pipeline, Formalizing Empirical Findings. Its source vocabulary overlaps type, section, across, tasks, model, pruning, paradigm, but, all, scales.

Paper-specific inference/evaluation sequence:

1. At B.2 Model-Specific Construction Pipeline, the paper reports an inference or deployment action involving Model-Specific, Pipeline, Construction, Since, reasoning, and capabilities. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, B.2 Model-Specific Construction Pipeline)*
2. At D.1 Motivation and Setup, the paper reports an inference or deployment action involving Type, external, quality, data, STOP, and trained. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, D.1 Motivation and Setup)*
3. At Formalizing Empirical Findings, the paper reports an inference or deployment action involving Empirical, approx, Formalizing, Findings, formulation, and input. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Formalizing Empirical Findings)*
4. At 5.2 Ablations and Analysis, the paper reports an inference or deployment action involving Ablations, Analysis, validate, core, design, and choices. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, 5.2 Ablations and Analysis)*

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
| GPQA | The evidence at References names partition(s) without a mechanically isolated sample count. | The preprocessing evidence for GPQA names AIME, dataset, mathematical, Specifically, GPQA, constructed at B.1 Source Benchmarks and Decontamination. | private full-paper evidence dossier for arXiv:2604.16029, References |

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| DeepConf , AdaDec Think Just Enough | Table 1 lists DeepConf , AdaDec Think Just Enough as a numeric comparison row under 2.2 A Unified Taxonomy of Pruning Signal Generators. | Neither the Table 1 caption nor its row label establishes whether DeepConf , AdaDec Think Just Enough was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 1 row DeepConf , AdaDec Think Just Enough |
| Tokens ( \downarrow ) | Table 2 lists Tokens ( \downarrow ) as a numeric comparison row under Inference: “Launch-Check-Resume”. | Neither the Table 2 caption nor its row label establishes whether Tokens ( \downarrow ) was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 2 row Tokens ( \downarrow ) |
| AIME24 | Table 2 lists AIME24 as a numeric comparison row under Inference: “Launch-Check-Resume”. | Neither the Table 2 caption nor its row label establishes whether AIME24 was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 2 row AIME24 |
| AIME25 | Table 2 lists AIME25 as a numeric comparison row under Inference: “Launch-Check-Resume”. | Neither the Table 2 caption nor its row label establishes whether AIME25 was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 2 row AIME25 |
| BRUMO25 | Table 2 lists BRUMO25 as a numeric comparison row under Inference: “Launch-Check-Resume”. | Neither the Table 2 caption nor its row label establishes whether BRUMO25 was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 2 row BRUMO25 |
| HMMT25 | Table 2 lists HMMT25 as a numeric comparison row under Inference: “Launch-Check-Resume”. | Neither the Table 2 caption nor its row label establishes whether HMMT25 was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 2 row HMMT25 |
| GPQA-D | Table 2 lists GPQA-D as a numeric comparison row under Inference: “Launch-Check-Resume”. | Neither the Table 2 caption nor its row label establishes whether GPQA-D was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 2 row GPQA-D |
| Dataset | Table 3 lists Dataset as a numeric comparison row under Ablation: Quality of the Supervision Signal. | Neither the Table 3 caption nor its row label establishes whether Dataset was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 3 row Dataset |
| GPQA | Table 3 lists GPQA as a numeric comparison row under Ablation: Quality of the Supervision Signal. | Neither the Table 3 caption nor its row label establishes whether GPQA was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 3 row GPQA |
| STOP w/o Adapter | Table 4 lists STOP w/o Adapter as a numeric comparison row under Ablation: Necessity of Critique Adapter. | Neither the Table 4 caption nor its row label establishes whether STOP w/o Adapter was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 4 row STOP w/o Adapter |
| STOP | Table 4 lists STOP as a numeric comparison row under Ablation: Necessity of Critique Adapter. | Neither the Table 4 caption nor its row label establishes whether STOP was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 4 row STOP |
| # Tokens | Table 5 lists # Tokens as a numeric comparison row under Findings 5 .. | Neither the Table 5 caption nor its row label establishes whether # Tokens was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 5 row # Tokens |
| - | Table 5 lists - as a numeric comparison row under Findings 5 .. | Neither the Table 5 caption nor its row label establishes whether - was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 5 row - |
| Rank | Table 6 lists Rank as a numeric comparison row under Findings 5 .. | Neither the Table 6 caption nor its row label establishes whether Rank was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 6 row Rank |
| Type II | Table 7 lists Type II as a numeric comparison row under Analysis: Computational Overhead. | Neither the Table 7 caption nor its row label establishes whether Type II was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 7 row Type II |
| Type I | Table 7 lists Type I as a numeric comparison row under Analysis: Computational Overhead. | Neither the Table 7 caption nor its row label establishes whether Type I was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2604.16029, Table 7 row Type I |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

| Metric | Denominator/conditioning | Direction | Source locator |
|---|---|---|---|
| Model | The metric-definition evidence at Difficulty Stratification (Filtering). ties Model to terms problems, model, samples, correct, answers, Before, generating, prefixes. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header Model |
| No pruning (Baseline) / avg@64 ( \uparrow ) | Table 2 reports No pruning (Baseline) / avg@64 ( \uparrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header No pruning (Baseline) / avg@64 ( \uparrow ) |
| No pruning (Baseline) / Tokens ( \downarrow ) | Table 2 reports No pruning (Baseline) / Tokens ( \downarrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header No pruning (Baseline) / Tokens ( \downarrow ) |
| Type I / avg@8\|64 ( \uparrow ) | Table 2 reports Type I / avg@8\|64 ( \uparrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header Type I / avg@8\|64 ( \uparrow ) |
| Type I / Tokens (% \downarrow ) | Table 2 reports Type I / Tokens (% \downarrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header Type I / Tokens (% \downarrow ) |
| Type II / avg@8\|64 ( \uparrow ) | Table 2 reports Type II / avg@8\|64 ( \uparrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header Type II / avg@8\|64 ( \uparrow ) |
| Type II / Tokens (% \downarrow ) | Table 2 reports Type II / Tokens (% \downarrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header Type II / Tokens (% \downarrow ) |
| Type III / avg@8\|64 ( \uparrow ) | Table 2 reports Type III / avg@8\|64 ( \uparrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header Type III / avg@8\|64 ( \uparrow ) |
| Type III / Tokens (% \downarrow ) | Table 2 reports Type III / Tokens (% \downarrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header Type III / Tokens (% \downarrow ) |
| Type IV / avg@8\|64 ( \uparrow ) | Table 2 reports Type IV / avg@8\|64 ( \uparrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header Type IV / avg@8\|64 ( \uparrow ) |
| Type IV / Tokens (% \downarrow ) | Table 2 reports Type IV / Tokens (% \downarrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 2 header Type IV / Tokens (% \downarrow ) |
| No pruning (Baseline) / 73.73 | Table 8 reports No pruning (Baseline) / 73.73 as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 8 header No pruning (Baseline) / 73.73 |
| STOP / 77.23 | Table 8 reports STOP / 77.23 as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 8 header STOP / 77.23 |
| Full Paths (Baseline) / avg@8\|64 ( \uparrow ) | Table 13 reports Full Paths (Baseline) / avg@8\|64 ( \uparrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 13 header Full Paths (Baseline) / avg@8\|64 ( \uparrow ) |
| Full Paths (Baseline) / Tokens ( \downarrow ) | Table 13 reports Full Paths (Baseline) / Tokens ( \downarrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 13 header Full Paths (Baseline) / Tokens ( \downarrow ) |
| Type II {}^{\text{retrain}} / avg@8\|64 ( \uparrow ) | Table 13 reports Type II {}^{\text{retrain}} / avg@8\|64 ( \uparrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2604.16029, Table 13 header Type II {}^{\text{retrain}} / avg@8\|64 ( \uparrow ) |

Metrics are reconstructed with direction, denominator, aggregation unit, conditioning, and reference quality. Failures excluded from an average create survivor bias. A gap to a best-known incumbent is not a gap to a proven optimum. A judge-model score is not a human preference without validation. A compression ratio can invert depending on convention. Confidence intervals, paired tests, and effect sizes matter when differences are close or instances are correlated.

### 4.4 Hardware, batching, and runtime semantics

Quality-v2 paper-specific hardware/runtime evidence:

- At 3.1 Motivation for Type IV Pruning, the paper's hardware/runtime paragraph names latency. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, 3.1 Motivation for Type IV Pruning)*
- At Training: Learn to Use Internal Information, the paper's hardware/runtime paragraph names training, model, prefix, soft, process, goal, simple, teach. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Training: Learn to Use Internal Information)*
- At Performance Hierarchy across Four Types Pruning, the paper's hardware/runtime paragraph names Type, while, most, effectiveness, generators, states, significantly, both. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Performance Hierarchy across Four Types Pruning)*
- At 5.1 Determining the Optimal remaining ratios, the paper's hardware/runtime paragraph names latency. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, 5.1 Determining the Optimal remaining ratios)*
- At Analysis: Computational Overhead, the paper's hardware/runtime paragraph names latency, H100, GPU, throughput. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Analysis: Computational Overhead)*
- At Analysis: Generalization to Tool Use, the paper's hardware/runtime paragraph names H100, GPU. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Analysis: Generalization to Tool Use)*
- At B.3 Training Cost Details, the paper's hardware/runtime paragraph names costs, data, construction, correspond, one-time, process., Once, constructed. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, B.3 Training Cost Details)*
- At C.1 Infrastructure and Sampling Configuration, the paper's hardware/runtime paragraph names H100, 80GB. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, C.1 Infrastructure and Sampling Configuration)*


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
| Table 2 | AIME24 | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Model; No pruning (Baseline) / avg@64 ( \uparrow ); No pruning (Baseline) / Tokens ( \downarrow ); Type I / avg@8\|64 ( \uparrow ); Type I / Tokens (% \downarrow ); Type II / avg@8\|64 ( \uparrow ); Type II / Tokens (% \downarrow ); Type III / avg@8\|64 ( \uparrow ); Type III / Tokens (% \downarrow ); Type IV / avg@8\|64 ( \uparrow ); Type IV / Tokens (% \downarrow ) | Model=1.5B; No pruning (Baseline) / avg@64 ( \uparrow )=30.10; No pruning (Baseline) / Tokens ( \downarrow )=782.3k; Type I / avg@8\|64 ( \uparrow )=26.25; Type I / Tokens (% \downarrow )=218.3k; Type I / Tokens (% \downarrow )=-72.09%; Type II / avg@8\|64 ( \uparrow )=32.50; Type II / Tokens (% \downarrow )=325.9k; Type II / Tokens (% \downarrow )=-58.34%; Type III / avg@8\|64 ( \uparrow )=32.92; Type III / Tokens (% \downarrow )=210.6k; Type III / Tokens (% \downarrow )=-73.08%; Type IV / avg@8\|64 ( \uparrow )=37.92; Type IV / Tokens (% \downarrow )=204.3k; Type IV / Tokens (% \downarrow )=-73.88% | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 2 row 3 |
| Table 2 | AIME25 | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Model; No pruning (Baseline) / avg@64 ( \uparrow ); No pruning (Baseline) / Tokens ( \downarrow ); Type I / avg@8\|64 ( \uparrow ); Type I / Tokens (% \downarrow ); Type II / avg@8\|64 ( \uparrow ); Type II / Tokens (% \downarrow ); Type III / avg@8\|64 ( \uparrow ); Type III / Tokens (% \downarrow ); Type IV / avg@8\|64 ( \uparrow ); Type IV / Tokens (% \downarrow ) | Model=1.5B; No pruning (Baseline) / avg@64 ( \uparrow )=22.76; No pruning (Baseline) / Tokens ( \downarrow )=784.8k; Type I / avg@8\|64 ( \uparrow )=24.17; Type I / Tokens (% \downarrow )=214.7k; Type I / Tokens (% \downarrow )=-72.64%; Type II / avg@8\|64 ( \uparrow )=24.17; Type II / Tokens (% \downarrow )=325.0k; Type II / Tokens (% \downarrow )=-58.59%; Type III / avg@8\|64 ( \uparrow )=23.75; Type III / Tokens (% \downarrow )=208.7k; Type III / Tokens (% \downarrow )=-73.40%; Type IV / avg@8\|64 ( \uparrow )=26.67; Type IV / Tokens (% \downarrow )=206.6k; Type IV / Tokens (% \downarrow )=-73.68% | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 2 row 4 |
| Table 8 | Model / Gain | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | No pruning (Baseline) / 73.73; STOP / 77.23 | No pruning (Baseline) / 73.73=64; STOP / 77.23=8; STOP / 77.23=64 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 8 row 2 |
| Table 13 | AIME24 | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Model; Full Paths (Baseline) / avg@8\|64 ( \uparrow ); Full Paths (Baseline) / Tokens ( \downarrow ); Type II / avg@8\|64 ( \uparrow ); Type II / Tokens (% \downarrow ); Type II {}^{\text{retrain}} / avg@8\|64 ( \uparrow ); Type II {}^{\text{retrain}} / Tokens (% \downarrow ); Type IV / avg@8\|64 ( \uparrow ); Type IV / Tokens (% \downarrow ) | Model=1.5B; Full Paths (Baseline) / avg@8\|64 ( \uparrow )=30.10; Full Paths (Baseline) / Tokens ( \downarrow )=782.3k; Type II / avg@8\|64 ( \uparrow )=32.50; Type II / Tokens (% \downarrow )=325.9k; Type II / Tokens (% \downarrow )=-58.34%; Type II {}^{\text{retrain}} / avg@8\|64 ( \uparrow )=37.50; Type II {}^{\text{retrain}} / Tokens (% \downarrow )=318.2k; Type II {}^{\text{retrain}} / Tokens (% \downarrow )=-59.33%; Type IV / avg@8\|64 ( \uparrow )=37.92; Type IV / Tokens (% \downarrow )=204.3k; Type IV / Tokens (% \downarrow )=-73.88% | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 13 row 3 |
| Table 13 | AIME25 | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Model; Full Paths (Baseline) / avg@8\|64 ( \uparrow ); Full Paths (Baseline) / Tokens ( \downarrow ); Type II / avg@8\|64 ( \uparrow ); Type II / Tokens (% \downarrow ); Type II {}^{\text{retrain}} / avg@8\|64 ( \uparrow ); Type II {}^{\text{retrain}} / Tokens (% \downarrow ); Type IV / avg@8\|64 ( \uparrow ); Type IV / Tokens (% \downarrow ) | Model=1.5B; Full Paths (Baseline) / avg@8\|64 ( \uparrow )=22.76; Full Paths (Baseline) / Tokens ( \downarrow )=784.8k; Type II / avg@8\|64 ( \uparrow )=24.17; Type II / Tokens (% \downarrow )=325.0k; Type II / Tokens (% \downarrow )=-58.59%; Type II {}^{\text{retrain}} / avg@8\|64 ( \uparrow )=24.16; Type II {}^{\text{retrain}} / Tokens (% \downarrow )=323.2k; Type II {}^{\text{retrain}} / Tokens (% \downarrow )=-58.82%; Type IV / avg@8\|64 ( \uparrow )=26.67; Type IV / Tokens (% \downarrow )=206.6k; Type IV / Tokens (% \downarrow )=-73.68% | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2604.16029, Table 13 row 4 |
| result context at Ablation: Quality of the Supervision Signal | Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 46.67%, 53.33 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2604.16029, Ablation: Quality of the Supervision Signal |
| result context at Ablation: Necessity of Critique Adapter | Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 36.67%, 31.67% | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2604.16029, Ablation: Necessity of Critique Adapter |
| result context at D.2 Detailed Analysis | Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 1.5B, 8, 25, 26.67% | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2604.16029, D.2 Detailed Analysis |
| result context at D.2 Detailed Analysis | Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 32.50%, 7B, 24, 61.67% | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2604.16029, D.2 Detailed Analysis |

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
- The author-side qualification at Limitations. concerns pruning, fixed, Limitations, Structural, Flexibility, and focuses. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Limitations.)*

Reviewer-identified limitations:

- No independent reproduction was performed for arXiv:2604.16029v2; STOP, Type, pruning, and labels remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, Further Evaluation and Empirical Analysis, and Evaluation metrics.)*
- The dossier inventories 89 headings, 16 tables, 24 figures, and 114 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2604.16029, complete coverage inventory)*

The explicit qualification path is anchored to Limitations, Limitations., D.3 Discussion: The Advantage of Internal Signals. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 0 candidate sentences and the limitation/discussion vocabulary internal, stop, pruning, reasoning, type, research, potential, representations, prefix, external. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper frames Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning as a contribution to reasoning, Parallel, paths, STOP. | Problem framing is located in the profile's named introduction/problem headings; no numbered section marker is treated as a measurement. (private full-paper evidence dossier for arXiv:2604.16029, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| The reported mechanism centers on Type, across, tasks, reasoning. | Method and formula evidence is bound to the named method headings and formula-specific operator audits. (private full-paper evidence dossier for arXiv:2604.16029, 3 Methodology: Super Token for Pruning) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Table 2 reports measured outcomes for AIME24 across Model, No pruning (Baseline) / avg@64 ( \uparrow ), No pruning (Baseline) / Tokens ( \downarrow ), Type I / avg@8\|64 ( \uparrow ), Type I / Tokens (% \downarrow ). | Quality-v2 paper-report result values: 46.67%, 53.33, 36.67%, 31.67%, 1.5B, 8, 25, 26.67% (private full-paper evidence dossier for arXiv:2604.16029, Further Evaluation and Empirical Analysis) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2604.16029v2), [canonical PDF](https://arxiv.org/pdf/2604.16029v2), [canonical full-paper HTML](https://arxiv.org/html/2604.16029v2), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2604.16029). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2604.16029v2)*
- **Predecessor/prior work (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 1 Introduction; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2510.12164)*
- **Alternative or benchmark (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under B.1 Source Benchmarks and Decontamination; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://openreview.net/forum?id=Ti67584b98)*
- **Code/data (bounded_not_found):** The bounded verified-URL receipt contains no official code/data artifact for this paper; no access error was recorded, so this is not labeled blocked. *(evidence locator: bounded online-vetting receipt for arXiv:2604.16029)*

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

Reviewer inference: the durable mechanism is the source-defined change centered on Type, across, tasks, and reasoning, rather than the paper's brand name. This interpretation predicts that a matched intervention on Type changes STOP; it is not an author claim or theorem.

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

Substantive evidence boundary: The profile binds arXiv:2604.16029v2 to a complete local PDF and full-paper HTML, 89 headings, 16 tables, 24 figures, and 114 extracted mathematical objects, and 3 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

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

**Proposition:** Reviewer hypothesis: the source-linked Type operation is causally responsible for part of the reported STOP behavior.
**Predicted observation:** Removing or neutralizing Type under matched data and compute will measurably weaken STOP.
**Falsifying observation:** A competent matched control without Type preserves the same STOP distribution within uncertainty.
**Minimum test:** Run a paired, seed-controlled ablation at Further Evaluation and Empirical Analysis and archive per-instance outcomes and resource use.
**Evidence locator:** private full-paper evidence dossier for arXiv:2604.16029, 3 Methodology: Super Token for Pruning, and Robustness across Tasks and Model Scales

### Hypothesis 2: Boundary transfer for Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning

**Proposition:** Reviewer hypothesis: the relation between Type, and across and STOP, and Type weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2604.16029, Further Evaluation and Empirical Analysis, and Evaluation metrics.

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2604.16029, Further Evaluation and Empirical Analysis, and Evaluation metrics..
2. **Reproduce the end-to-end Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning path** Success: the source-defined Type, across, and tasks and STOP, and Type are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2604.16029, 3 Methodology: Super Token for Pruning, and Robustness across Tasks and Model Scales.
3. **Falsify the reviewer mechanism thesis for Type** Success: a matched intervention on Type predicts a corresponding change in STOP Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2604.16029, 3 Methodology: Super Token for Pruning, and Robustness across Tasks and Model Scales.

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning should be remembered as a tested relation between Type, across, and tasks and STOP, Type, and pruning under the configurations at Further Evaluation and Empirical Analysis, and Evaluation metrics., not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The Table 1 caption centers on Pruning, Methods., Desideratum, Table, Unified, Taxonomy, Path; its parsed headers include External Source, across 6 rows and 18 cells.; result: External Source / Internal Source=1; Learnable / (Desideratum 2 ) / Type II / DeepPrune , LaBoR ThinkPRM , MAV / Type IV=1; Learnable / (Desideratum 2 ) / Type II / DeepPrune , LaBoR ThinkPRM , MAV / Type IV=1; Learnable / (Desideratum 2 ) / Type II / DeepPrune , LaBoR ThinkPRM , MAV / Type IV=1; caveat: Interpret Table 1 with its spanning headers and caption under 2.2 A Unified Taxonomy of Pruning Signal Generators; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 1 caption and object |
| Table 2 | Purpose: The Table 2 caption centers on best, Table, Results, across, various, models, benchmarks.; its parsed headers include Model, Dataset, No pruning (Baseline), Type I, Type II, Type III, Type IV, across 22 rows and 241 cells.; result: Model=1.5B; No pruning (Baseline)=30.10; No pruning (Baseline)=782.3k; Type I=26.25; Type I=218.3k; Type I=-72.09%; Type II=32.50; Type II=325.9k; Type II=-58.34%; Type III=32.92; Type III=210.6k; Type III=-73.08%; Type IV=37.92; Type IV=204.3k; Type IV=-73.88%; caveat: Interpret Table 2 with its spanning headers and caption under Inference: “Launch-Check-Resume”; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 2 caption and object |
| Table 3 | Purpose: The Table 3 caption centers on labels, Table, Performance, comparison, between, hard, MC-estimated; its parsed headers include Dataset, Supervision Type, avg@8\|64 (%), Cons@N (%), AIME 24, Hard Labels ( K=1 ), Soft Labels ( K=32 ), across 5 rows and 18 cells.; result: column 1=32; column 2=36.67; column 3=53.33; caveat: Interpret Table 3 with its spanning headers and caption under Ablation: Quality of the Supervision Signal; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 3 caption and object |
| Table 4 | Purpose: The Table 4 caption centers on Table, Comparing, STOP, module, simple, linear, classifier; its parsed headers include Dataset, Configuration, avg@8\|64 (%), Cons@N (%), AIME 24, STOP w/o Adapter, STOP, across 5 rows and 18 cells.; result: column 3=8; column 3=64; caveat: Interpret Table 4 with its spanning headers and caption under Ablation: Necessity of Critique Adapter; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 4 caption and object |
| Table 5 | Purpose: The Table 5 caption centers on Table, Effect, number, STOP, tokens, DS-Qwen-2.5-1.5B, AIME; its parsed headers include # Tokens, avg@32 \| 256, 1, 6, 2, 7, across 6 rows and 24 cells.; result: column 1=1; column 2=30.10; column 3=6; column 4=37.71; caveat: Interpret Table 5 with its spanning headers and caption under Findings 5 .; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 5 caption and object |
| Table 6 | Purpose: The Table 6 caption centers on Table, Effect, LoRA, rank, DS-Qwen-2.5-1.5B, AIME; its parsed headers include Rank, Params (M), avg@8 \| 64, 32, 64, across 5 rows and 15 cells.; result: column 1=128; column 2=147.7; column 3=36.67; caveat: Interpret Table 6 with its spanning headers and caption under Findings 5 .; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 6 caption and object |
| Table 7 | Purpose: The Table 7 caption centers on Table, Inference, overhead, analysis., STOP, achieves, near-zero; its parsed headers include Pruning Paradigm, Latency / Check, Relative Overhead, Type II, Type I, across 4 rows and 12 cells.; result: Latency / Check=0.20 s; Relative Overhead=0.59%; caveat: Interpret Table 7 with its spanning headers and caption under Analysis: Computational Overhead; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 7 caption and object |
| Table 8 | Purpose: The Table 8 caption centers on Table, Generalization, ZebraLogic., STOP, robustly, generalizes, beyond; its parsed headers include Model, DS-Qwen-2.5-7B, across 3 rows and 10 cells.; result: Model=7B; No pruning (Baseline)=73.73; STOP=77.23; Gain=+3.50%; caveat: Interpret Table 8 with its spanning headers and caption under Analysis: Generalization to Non-Math/STEM Tasks; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 8 caption and object |
| Table 9 | Purpose: The Table 9 caption centers on Table, Results, AIMO3, competition, setting, tool, GPT-OSS-120B; its parsed headers include Method, Score, Baseline + Tool, STOP (24 \rightarrow 8), across 4 rows and 8 cells.; result: Method / Baseline + Tool=16; Method / Baseline + Tool=8; Score / 39=43; caveat: Interpret Table 9 with its spanning headers and caption under Analysis: Generalization to Tool Use; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 9 caption and object |
| Table 10 | Purpose: The Table 10 caption centers on data., Table, Statistics, model-specific, training, Prefixes, extracted; its parsed headers include Model, Math, Science, Total, DS-Qwen-2.5-1.5B, DS-Qwen-2.5-7B, across 5 rows and 20 cells.; result: Model=1.5B; Math=14,816; Science=8,448; Total=23,264; caveat: Interpret Table 10 with its spanning headers and caption under Difficulty Stratification (Filtering).; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 10 caption and object |
| Table 11 | Purpose: The Table 11 caption centers on Training, Cost, Table, Supervision, Construction., report, number; its parsed headers include Model, Math, Science, Total Training Pairs, 8 \times H100 Hours, DS-Qwen-2.5-1.5B, DS-Qwen-2.5-7B, across 5 rows and 25 cells.; result: Model=1.5B; Math=14,816; Science=8,448; Total Training Pairs=23,264; 8 \times H100 Hours=43.08; caveat: Interpret Table 11 with its spanning headers and caption under B.3 Training Cost Details; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 11 caption and object |
| Table 12 | Purpose: The Table 12 caption centers on Table, Training, hyperparameters, across, model, scales.; its parsed headers include Hyperparameter, Per-Device Batch Size, Gradient Accumulation, across 11 rows and 55 cells.; result: All Linear / AdamW / 2048 / bf16=2; All Linear / AdamW / 2048 / bf16=10; All Linear / AdamW / 2048 / bf16=-5; All Linear / AdamW / 2048 / bf16=2; All Linear / AdamW / 2048 / bf16=10; All Linear / AdamW / 2048 / bf16=-5; All Linear / AdamW / 2048 / bf16=2; All Linear / AdamW / 2048 / bf16=10; All Linear / AdamW / 2048 / bf16=-5; All Linear / AdamW / 2048 / bf16=2; All Linear / AdamW / 2048 / bf16=10; All Linear / AdamW / 2048 / bf16=-5; caveat: Interpret Table 12 with its spanning headers and caption under B.3 Training Cost Details; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 12 caption and object |
| Table 13 | Purpose: The Table 13 caption centers on Type, Data., Architecture, external, Table, Ablation, Study; its parsed headers include Model, Dataset, Full Paths (Baseline), Type II, Type II {}^{\text{retrain}}, Type IV, avg@8\|64 ( \uparrow ), across 22 rows and 198 cells.; result: Model=1.5B; Full Paths (Baseline)=30.10; Full Paths (Baseline)=782.3k; Type II=32.50; Type II=325.9k; Type II=-58.34%; Type II {}^{\text{retrain}}=37.50; Type II {}^{\text{retrain}}=318.2k; Type II {}^{\text{retrain}}=-59.33%; Type IV=37.92; Type IV=204.3k; Type IV=-73.88%; caveat: Interpret Table 13 with its spanning headers and caption under D.1 Motivation and Setup; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 13 caption and object |
| Table 14 | Purpose: The Table 14 caption centers on Table, GPQA, Science, Short-Horizon, Recommended, inverse, retention; its parsed headers include Prefix Length, ( L_{\text{prefix}} ), 512, across 7 rows and 62 cells.; result: Compute Budget C (Total Tokens)=140k; Compute Budget C (Total Tokens)=160k; Compute Budget C (Total Tokens)=180k; Compute Budget C (Total Tokens)=200k; Compute Budget C (Total Tokens)=220k; Compute Budget C (Total Tokens)=240k; Compute Budget C (Total Tokens)=260k; Compute Budget C (Total Tokens)=280k; Compute Budget C (Total Tokens)=300k; caveat: Interpret Table 14 with its spanning headers and caption under E.1 Empirical Observations on Optimal Retention; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 14 caption and object |
| Table 15 | Purpose: The Table 15 caption centers on Table, AIME, Math, Long-Horizon, Recommended, inverse, retention; its parsed headers include Prefix Length, ( L_{\text{prefix}} ), 1024, across 7 rows and 62 cells.; result: Compute Budget C (Total Tokens)=200k; Compute Budget C (Total Tokens)=250k; Compute Budget C (Total Tokens)=300k; Compute Budget C (Total Tokens)=350k; Compute Budget C (Total Tokens)=400k; Compute Budget C (Total Tokens)=450k; Compute Budget C (Total Tokens)=500k; Compute Budget C (Total Tokens)=550k; Compute Budget C (Total Tokens)=600k; caveat: Interpret Table 15 with its spanning headers and caption under E.1 Empirical Observations on Optimal Retention; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 15 caption and object |
| Table 16 | Purpose: The Table 16 caption centers on Throughput., cost, explicit, verification, drop, Table, Breakdown; its parsed headers include Method, Gen. Time (s), Verify Latency (s), Total Time (s), Throughput (tok/s), Throughput Drop ( \downarrow ), Explicit Verify Cost, across 5 rows and 35 cells.; result: Gen. Time (s)=40.64; Verify Latency (s)=0.38; Total Time (s)=41.02; Throughput (tok/s)=812.1; Throughput Drop ( \downarrow )=17.71%; Explicit Verify Cost=1.74%; caveat: Interpret Table 16 with its spanning headers and caption under F.2 Quantitative Analysis; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2604.16029, Table 16 caption and object |
| Figure 1 | Purpose: The Figure 1 caption identifies a paper-specific visual object centered on early., pruning, Figure, necessity, errors, often, lead, irreversible.; result: The caption makes a qualitative claim about early., pruning, Figure, necessity, errors, often; no plotted value is inferred from pixels.; caveat: The caption under 1 Introduction was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 1 caption and object |
| Figure 2 | Purpose: The Figure 2 caption identifies a paper-specific visual object centered on Figure, proposed, taxonomy, path, pruning..; result: The caption makes a qualitative claim about Figure, proposed, taxonomy, path, pruning.; no plotted value is inferred from pixels.; caveat: The caption under Contributions was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 2 caption and object |
| Figure 3 | Purpose: The Figure 3 caption identifies a paper-specific visual object centered on Figure, inference, process, comprises, three, stages, caching, initial.; result: The caption makes a qualitative claim about Figure, inference, process, comprises, three, stages; no plotted value is inferred from pixels.; caveat: The caption under 3.1 Motivation for Type IV Pruning was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 3 caption and object |
| Figure 4 | Purpose: The Figure 4 caption identifies a quantitative plot or comparison centered on Figure, Performance, compute, four, types, math, stem, benchmarks..; result: The caption makes a qualitative claim about Figure, Performance, compute, four, types, math; no plotted value is inferred from pixels.; caveat: The caption under Findings 2 . was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 4 caption and object |
| Figure 5 panel (a) | Purpose: The Figure 5 panel (a) caption identifies a paper-specific visual object centered on GPQA, text, prefix.; result: Caption-reported measured values: 512; caveat: The caption under Applying the Empirical Guideline was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 5 panel (a) caption and object |
| Figure 5 panel (b) | Purpose: The Figure 5 panel (b) caption identifies a paper-specific visual object centered on GPQA, text, prefix.; result: Caption-reported measured values: 1024; caveat: The caption under Applying the Empirical Guideline was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 5 panel (b) caption and object |
| Figure 5 panel (c) | Purpose: The Figure 5 panel (c) caption identifies a paper-specific visual object centered on AIME, text, prefix.; result: The caption makes a qualitative claim about AIME, text, prefix; no plotted value is inferred from pixels.; caveat: The caption under Applying the Empirical Guideline was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 5 panel (c) caption and object |
| Figure 5 panel (d) | Purpose: The Figure 5 panel (d) caption identifies a paper-specific visual object centered on AIME, text, prefix.; result: Caption-reported measured values: 4096; caveat: The caption under Applying the Empirical Guideline was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 5 panel (d) caption and object |
| Figure 5 | Purpose: The Figure 5 caption identifies a quantitative plot or comparison centered on prefix, Figure, Performance, comparison, under, different, retention, ratios.; result: The caption makes a qualitative claim about prefix, Figure, Performance, comparison, under, different; no plotted value is inferred from pixels.; caveat: The caption under Applying the Empirical Guideline was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 5 caption and object |
| Figure 6 | Purpose: The Figure 6 caption identifies a quantitative plot or comparison centered on ratio, Figure, Inverse, retention, gamma, compute-to-prefix, theoretical, curves.; result: Caption-reported measured values: -1; caveat: The caption under Applying the Empirical Guideline was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 6 caption and object |
| Figure 7 panel (a) | Purpose: The Figure 7 panel (a) caption identifies a paper-specific visual object centered on High-scoring, Path.; result: The caption makes a qualitative claim about High-scoring, Path; no plotted value is inferred from pixels.; caveat: The caption under Process-oriented Evaluation was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 7 panel (a) caption and object |
| Figure 7 panel (b) | Purpose: The Figure 7 panel (b) caption identifies a paper-specific visual object centered on Low-scoring, Path.; result: The caption makes a qualitative claim about Low-scoring, Path; no plotted value is inferred from pixels.; caveat: The caption under Process-oriented Evaluation was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 7 panel (b) caption and object |
| Figure 7 | Purpose: The Figure 7 caption identifies a paper-specific visual object centered on STOP, paths, Figure, Attention, Analysis, Decision-Making., High-scoring, prioritize.; result: The caption makes a qualitative claim about STOP, paths, Figure, Attention, Analysis, Decision-Making.; no plotted value is inferred from pixels.; caveat: The caption under Process-oriented Evaluation was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 7 caption and object |
| Figure 8 | Purpose: The Figure 8 caption identifies a paper-specific visual object centered on Figure, MC-based, construction, prefix, potential, supervision..; result: The caption makes a qualitative claim about Figure, MC-based, construction, prefix, potential, supervision.; no plotted value is inferred from pixels.; caveat: The caption under A.2 Path Pruning (Prefix Rejection) was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 8 caption and object |
| Figure 9 panel (a) | Purpose: The Figure 9 panel (a) caption identifies a paper-specific visual object centered on AIME, prefix, Optimal, gamma, shifts, aggressive, pruning, budget.; result: The caption makes a qualitative claim about AIME, prefix, Optimal, gamma, shifts, aggressive; no plotted value is inferred from pixels.; caveat: The caption under E.1 Empirical Observations on Optimal Retention was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 9 panel (a) caption and object |
| Figure 9 panel (b) | Purpose: The Figure 9 panel (b) caption identifies a paper-specific visual object centered on AIME, prefix, Longer, context, enables, stable, pruning, higher.; result: Caption-reported measured values: 4096; caveat: The caption under E.1 Empirical Observations on Optimal Retention was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 9 panel (b) caption and object |
| Figure 9 panel (c) | Purpose: The Figure 9 panel (c) caption identifies a paper-specific visual object centered on GPQA, prefix, Higher, compute, budgets, drive, aggressive, pruning..; result: Caption-reported measured values: 512; caveat: The caption under E.1 Empirical Observations on Optimal Retention was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 9 panel (c) caption and object |
| Figure 9 panel (d) | Purpose: The Figure 9 panel (d) caption identifies a paper-specific visual object centered on GPQA, prefix, Scaling, behavior, remains, consistent, longer, contexts..; result: Caption-reported measured values: 1024; caveat: The caption under E.1 Empirical Observations on Optimal Retention was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 9 panel (d) caption and object |
| Figure 9 | Purpose: The Figure 9 caption identifies a paper-specific visual object centered on Figure, Empirical, optimization, surfaces., Impact, retention, ratio, gamma.; result: The caption makes a qualitative claim about Figure, Empirical, optimization, surfaces., Impact, retention; no plotted value is inferred from pixels.; caveat: The caption under E.1 Empirical Observations on Optimal Retention was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 9 caption and object |
| Figure 10 panel (a) | Purpose: The Figure 10 panel (a) caption identifies a qualitative example or visualization centered on High-scoring, Case., module, focuses, logical, negation, cognitive, pivot.; result: The caption makes a qualitative claim about High-scoring, Case., module, focuses, logical, negation; no plotted value is inferred from pixels.; caveat: The caption under Appendix G Extended Attention Analysis was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 10 panel (a) caption and object |
| Figure 10 panel (b) | Purpose: The Figure 10 panel (b) caption identifies a qualitative example or visualization centered on Low-scoring, Case., Attention, concentrates, heavily, answer, option, itself.; result: The caption makes a qualitative claim about Low-scoring, Case., Attention, concentrates, heavily, answer; no plotted value is inferred from pixels.; caveat: The caption under Appendix G Extended Attention Analysis was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 10 panel (b) caption and object |
| Figure 10 panel (c) | Purpose: The Figure 10 panel (c) caption identifies a qualitative example or visualization centered on High-scoring, Case., Similar, module, attends, logical, marker, doesn.; result: The caption makes a qualitative claim about High-scoring, Case., Similar, module, attends, logical; no plotted value is inferred from pixels.; caveat: The caption under Appendix G Extended Attention Analysis was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 10 panel (c) caption and object |
| Figure 10 panel (d) | Purpose: The Figure 10 panel (d) caption identifies a qualitative example or visualization centered on Low-scoring, Case., module, demonstrates, premature, closure, fixating, terminal.; result: The caption makes a qualitative claim about Low-scoring, Case., module, demonstrates, premature, closure; no plotted value is inferred from pixels.; caveat: The caption under Appendix G Extended Attention Analysis was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 10 panel (d) caption and object |
| Figure 10 | Purpose: The Figure 10 caption identifies a qualitative example or visualization centered on STOP, paths, Figure, Extended, Visualization, Attention, Maps., While.; result: The caption makes a qualitative claim about STOP, paths, Figure, Extended, Visualization, Attention; no plotted value is inferred from pixels.; caveat: The caption under Appendix G Extended Attention Analysis was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2604.16029, Figure 10 caption and object |
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
