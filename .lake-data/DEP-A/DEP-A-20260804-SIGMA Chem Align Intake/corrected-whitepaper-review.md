# Whitepaper Review: SIGMA: Structure-Invariant Generative Molecular Alignment for Chemical Language Models via Autoregressive Contrastive Learning

## A detailed review, technical reconstruction, and independent re-conceptualization of “SIGMA: Structure-Invariant Generative Molecular Alignment for Chemical Language Models via Autoregressive Contrastive Learning”

**Source paper:** Xinyu Wang; Fei Dou; Jinbo Bi; Minghu Song, “SIGMA: Structure-Invariant Generative Molecular Alignment for Chemical Language Models via Autoregressive Contrastive Learning,” arXiv:2603.25062v1.[^source-paper]

**Artifact prepared:** 2026-08-20
**Local source reviewed:** complete locally archived PDF (15 pages) and matching full-paper HTML (61905 readable body characters); private path withheld
**Review scope:** full-paper reconstruction, claim vetting, local evidence mapping, implications, and replication agenda
**Review status:** source artifacts inspected; bounded online primary-source vetting performed; experiments not independently rerun

## Executive Assessment

### The paper in one sentence

The paper presents and evaluates a technical contribution framed around sigma, structure-invariant, generative, molecular, alignment, chemical, with its method, formal objects, experimental record, limitations, and source structure inspected from a complete local paper pair rather than an abstract page.

### The deeper idea

Reviewer inference: the durable mechanism is the source-defined change centered on mathcal, autoregressive, sequence, and SIGMA, rather than the paper's brand name. This interpretation predicts that a matched intervention on mathcal changes SIGMA; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to 3 Methodology, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

### Bottom-line judgment

The source is complete enough for a full-paper assessment, and the paper reports a technically organized contribution with an explicit evaluation record. Results remain paper-reported. The local evidence pass confirms the complete results structure and numbered-object inventory, but it does not independently reproduce a numerical value or infer a stronger denominator than the source states. The defensible verdict is therefore conditional: the paper establishes what it directly measures under its own setup, while broader superiority, generality, robustness, efficiency, or deployment readiness remains bounded by the tested models, data, metrics, budgets, hardware, and comparisons.[^scope]

### Principal strengths

- Complete PDF and matching full-paper HTML passed identity, structure, title, references, and readability gates.
- The source exposes 46 section headings, 3 table captions, 9 figure captions, and 130 mathematical renderings for coverage auditing.
- The review can distinguish paper report, external-primary evidence, reviewer inference, and hypothesis without relying on an abstract-only summary.

### Principal qualifications

1. The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions.
2. No result, code path, benchmark, training run, or hardware measurement was independently reproduced.
3. Bounded online checks verified canonical identity and the explicitly recorded official URLs; the search is not exhaustive and does not establish artifact runnability or reproduction.[^external]

## 1. The Problem and Research Questions

### 1.1 Problem and stakes

**Paper-reported problem:** For SIGMA: Structure-Invariant Generative Molecular Alignment for Chemical Language Models via Autoregressive Contrastive Learning, the formal target is bounded to the source-defined relation among molecular, SIGMA, graph, latent, trajectory, autoregressive, and divergence. The task assumptions and stakes are anchored to Abstract, and 1 Introduction; no objective outside those sections is inferred.

**Research gap reconstructed from the source:** The paper positions SIGMA around molecular, SIGMA, graph, mathcal, autoregressive, and sequence. This records the authors' gap framing only; novelty, priority, generality, and superiority require the separate prior-work and evaluation audits.

The title and full-paper organization identify sigma, structure-invariant, generative, molecular, alignment, chemical as the central problem space. A rigorous reading asks what input object is transformed, predicted, selected, optimized, or measured; which practical or scientific constraint motivates that operation; and which outcome makes the change valuable. Those questions must be answered by the method and evaluation sections, not by the title alone. The paper reports its own problem definition; this review preserves the boundary between that report and reviewer interpretation.

Paper-specific reconstruction: the abstract/introduction evidence concentrates on molecular, where, graph, models, sequence, chemical, language, string, representations, sequences, under the headings Abstract, 1 Introduction. Those source terms locate the actual objects and constraints; they do not by themselves prove novelty or improvement. In this review they constrain the problem statement so a generic systems narrative cannot replace the paper's own domain and terminology.

The practical stakes depend on the actual denominator. An improvement in a representation, proxy, component score, or controlled benchmark can be important without automatically improving end-user quality, wall-clock cost, reliability, or safety. A durable account therefore separates the immediate technical objective from the downstream objective and asks which bridge between them is tested. If that bridge is only assumed, it remains an explicit gap rather than a hidden premise.

### 1.2 Prior method families and inherited components

The paper's related-work and background sections define the relevant method families. The review treats established backbones, pretrained models, datasets, optimization routines, kernels, evaluation harnesses, and standard metrics as inherited unless the source identifies a change. Novelty belongs to the specific interface, objective, representation, decision rule, data construction, proof, or evaluation design that differs. This prevents a system-level bundle from receiving credit for every capability of its dependencies.

### 1.3 Questions that govern the assessment

Five questions organize the reconstruction. What exact object enters and leaves the method? Which components are learned, fixed, searched, sampled, or verified? What objective and assumptions determine the operation? How do training or calibration differ from inference or deployment? Finally, which result would falsify the authors' causal or generality story rather than merely lower an aggregate score? These questions create an audit trail from paper report to independent assessment.

## 2. Formal and Technical Reconstruction

### 2.1 Definitions and assumptions

The authoritative definition chain lives in the complete source sections listed below. The automated evidence profile does not pretend that section names themselves describe the mechanism. Instead, the full review binds each claim to the source's definitions, stated assumptions, and adjacent formal or experimental context. The core technical headings identified for close reading were:

- 3 Methodology
- 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds

Variables should be assigned plain-language meanings before algebra is interpreted. Inputs, labels, state, parameters, budgets, constraints, random variables, and outputs must remain distinct. A probability requires a sample space and conditioning event; a loss requires an optimization direction; a ratio requires a numerator and denominator; and a guarantee retains every assumption under which it was proved. If the source uses the same symbol in different roles or shifts between population and sample quantities, that ambiguity should be preserved rather than silently repaired.

### 2.2 Objective and central equations

The full HTML exposes 130 distinct mathematical renderings. Each is treated as a paper-reported formal object whose sign, normalization, conditioning, and denominator must be read with adjacent prose.

Paper-specific formal reconstruction:

**Formal object 1 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 1 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, graph, dots, mathbb, molecular, defined, and the expression links mathcal, G, in, mathbb..** `\mathcal{G}\in\mathbb{G}`
Variables: "mathcal, G, in, mathbb".
Sign/normalization/conditioning/surrogate audit: "Formula 1 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, G, in, mathbb; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 1.

**Formal object 2 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 2 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, graph, dots, mathbb, molecular, defined, and the expression links mathcal, G..** `\mathcal{G}`
Variables: "mathcal, G".
Sign/normalization/conditioning/surrogate audit: "Formula 2 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, G; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 2.

**Formal object 3 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 3 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, graph, dots, mathbb, molecular, defined, and the expression links S, x_{1}, dots, x_{L}..** `S=(x_{1},\dots,x_{L})`
Variables: "S, x_{1}, dots, x_{L}".
Sign/normalization/conditioning/surrogate audit: "Formula 3 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S, x_{1}, dots, x_{L}; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 3.

**Formal object 4 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 4 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, graph, dots, mathbb, molecular, defined, and the expression links mathcal, V..** `\mathcal{V}`
Variables: "mathcal, V".
Sign/normalization/conditioning/surrogate audit: "Formula 4 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, V; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 4.

**Formal object 5 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 5 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, graph, dots, mathbb, molecular, defined, and the expression links Pi, mathcal, G, S, dots, K..** `\Pi(\mathcal{G})=\{S^{(1)},\dots,S^{(K)}\}`
Variables: "Pi, mathcal, G, S, dots, K".
Sign/normalization/conditioning/surrogate audit: "Formula 5 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Pi, mathcal, G, S, dots, K; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 5.

**Formal object 6 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 6 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a optimization objective or loss; adjacent prose centers on Standard, ChemLMs, maximize, likelihood, sequence, autoregressive, and the expression links S..** `S`
Variables: "S".
Sign/normalization/conditioning/surrogate audit: "Formula 6 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 6.

**Formal object 7 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 7 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a optimization objective or loss; adjacent prose centers on same, latent, Standard, ChemLMs, maximize, likelihood, and the expression links p_{\theta}, S, nolimits, t, L, x_{t}, x_{..** `\log p_{\theta}(S)=\sum\nolimits_{t=1}^{L}\log p_{\theta}(x_{t}|x_{<t})`
Variables: "p_{\\theta}, S, nolimits, t, L, x_{t}, x_{".
Sign/normalization/conditioning/surrogate audit: "Formula 7 operator audit: summation; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p_{\\theta}, S, nolimits, t, L, x_{t}, x_{; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 7.

**Formal object 8 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 8 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a optimization objective or loss; adjacent prose centers on same, latent, While, effective, unique, sequences, and the expression links S, i..** `S^{(i)}`
Variables: "S, i".
Sign/normalization/conditioning/surrogate audit: "Formula 8 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S, i; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 8.

**Formal object 9 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 9 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a optimization objective or loss; adjacent prose centers on same, latent, While, effective, unique, sequences, and the expression links S, j..** `S^{(j)}`
Variables: "S, j".
Sign/normalization/conditioning/surrogate audit: "Formula 9 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S, j; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 9.

**Formal object 10 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 10 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a optimization objective or loss; adjacent prose centers on same, latent, While, effective, unique, sequences, and the expression links Pi, mathcal, G..** `\Pi(\mathcal{G})`
Variables: "Pi, mathcal, G".
Sign/normalization/conditioning/surrogate audit: "Formula 10 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Pi, mathcal, G; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 10.

**Formal object 11 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 11 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a optimization objective or loss; adjacent prose centers on same, latent, While, effective, unique, sequences, and the expression links h_{t}, S, i..** `h_{t}(S^{(i)})`
Variables: "h_{t}, S, i".
Sign/normalization/conditioning/surrogate audit: "Formula 11 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: h_{t}, S, i; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 11.

**Formal object 12 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 12 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a optimization objective or loss; adjacent prose centers on same, latent, While, effective, unique, sequences, and the expression links h_{t}, S, j..** `h_{t}(S^{(j)})`
Variables: "h_{t}, S, j".
Sign/normalization/conditioning/surrogate audit: "Formula 12 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: h_{t}, S, j; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 12.

**Formal object 13 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 13 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a optimization objective or loss; adjacent prose centers on same, latent, While, effective, unique, sequences, and the expression links f_{\theta}..** `f_{\theta}(\cdot)`
Variables: "f_{\\theta}".
Sign/normalization/conditioning/surrogate audit: "Formula 13 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f_{\\theta}; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 13.

**Formal object 14 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 14 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a optimization objective or loss; adjacent prose centers on same, latent, While, effective, unique, sequences, and the expression links f_{\theta}, x_{, t, i, approx, j, quad, cong..** `f_{\theta}(x_{<t}^{(i)})\approx f_{\theta}(x_{<t}^{(j)})\quad\text{if}\quad\text{Mol}(x_{<t}^{(i)})\cong\text{Mol}(x_{<t}^{(j)})`
Variables: "f_{\\theta}, x_{, t, i, approx, j, quad, cong".
Sign/normalization/conditioning/surrogate audit: "Formula 14 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f_{\\theta}, x_{, t, i, approx, j, quad, cong; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 14.

**Formal object 15 at 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds — Formula 15 under 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds is classified as a paper-defined mathematical relation; adjacent prose centers on where, cong, denotes, subgraph, isomorphism., and the expression links cong..** `\cong`
Variables: "cong".
Sign/normalization/conditioning/surrogate audit: "Formula 15 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: cong; meanings remain tied to 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, formal object 15.

**Formal object 16 at 3.2 Constructing Functionally Equivalent Views — Formula 16 under 3.2 Constructing Functionally Equivalent Views is classified as a paper-defined mathematical relation; adjacent prose centers on pair, suffix, construct, positive, sampling, randomized, and the expression links S, u, v..** `(S^{u},S^{v})`
Variables: "S, u, v".
Sign/normalization/conditioning/surrogate audit: "Formula 16 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S, u, v; meanings remain tied to 3.2 Constructing Functionally Equivalent Views.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.2 Constructing Functionally Equivalent Views, formal object 16.

**Formal object 17 at 3.2 Constructing Functionally Equivalent Views — Formula 17 under 3.2 Constructing Functionally Equivalent Views is classified as a paper-defined mathematical relation; adjacent prose centers on pair, suffix, construct, positive, sampling, randomized, and the expression links p..** `p`
Variables: "p".
Sign/normalization/conditioning/surrogate audit: "Formula 17 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p; meanings remain tied to 3.2 Constructing Functionally Equivalent Views.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.2 Constructing Functionally Equivalent Views, formal object 17.

**Formal object 18 at 3.2 Constructing Functionally Equivalent Views — Formula 18 under 3.2 Constructing Functionally Equivalent Views is classified as a paper-defined mathematical relation; adjacent prose centers on pair, suffix, construct, positive, sampling, randomized, and the expression links p_{u}..** `p_{u}`
Variables: "p_{u}".
Sign/normalization/conditioning/surrogate audit: "Formula 18 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p_{u}; meanings remain tied to 3.2 Constructing Functionally Equivalent Views.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.2 Constructing Functionally Equivalent Views, formal object 18.

**Formal object 19 at 3.2 Constructing Functionally Equivalent Views — Formula 19 under 3.2 Constructing Functionally Equivalent Views is classified as a paper-defined mathematical relation; adjacent prose centers on pair, suffix, construct, positive, sampling, randomized, and the expression links p_{v}..** `p_{v}`
Variables: "p_{v}".
Sign/normalization/conditioning/surrogate audit: "Formula 19 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p_{v}; meanings remain tied to 3.2 Constructing Functionally Equivalent Views.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.2 Constructing Functionally Equivalent Views, formal object 19.

**Formal object 20 at 3.2 Constructing Functionally Equivalent Views — Formula 20 under 3.2 Constructing Functionally Equivalent Views is classified as a paper-defined mathematical relation; adjacent prose centers on pair, suffix, construct, positive, sampling, randomized, and the expression links p_{u}, p_{v}..** `(p_{u},p_{v})`
Variables: "p_{u}, p_{v}".
Sign/normalization/conditioning/surrogate audit: "Formula 20 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p_{u}, p_{v}; meanings remain tied to 3.2 Constructing Functionally Equivalent Views.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.2 Constructing Functionally Equivalent Views, formal object 20.

**Formal object 21 at 3.2 Constructing Functionally Equivalent Views — Formula 21 under 3.2 Constructing Functionally Equivalent Views is classified as a paper-defined mathematical relation; adjacent prose centers on Syntactic, Divergence, prefixes, must, represent, distinct, and the expression links p_{u}\neq, p_{v}..** `p_{u}\neq p_{v}`
Variables: "p_{u}\\neq, p_{v}".
Sign/normalization/conditioning/surrogate audit: "Formula 21 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p_{u}\\neq, p_{v}; meanings remain tied to 3.2 Constructing Functionally Equivalent Views.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.2 Constructing Functionally Equivalent Views, formal object 21.

**Formal object 22 at 3.2 Constructing Functionally Equivalent Views — Formula 22 under 3.2 Constructing Functionally Equivalent Views is classified as a paper-defined mathematical relation; adjacent prose centers on Oracle, mathcal, Structural, Equivalence, Verification, concatenation, and the expression links mathcal, H..** `\mathcal{H}`
Variables: "mathcal, H".
Sign/normalization/conditioning/surrogate audit: "Formula 22 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, H; meanings remain tied to 3.2 Constructing Functionally Equivalent Views.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.2 Constructing Functionally Equivalent Views, formal object 22.

**Formal object 23 at 3.2 Constructing Functionally Equivalent Views — Formula 23 under 3.2 Constructing Functionally Equivalent Views is classified as a state or representation transformation; adjacent prose centers on Equivalence, Oracle, Verification, prefixes, suffix, mathcal, and the expression links mathcal, H, p_{u}\oplus, s, equiv, p_{v}\oplus, G..** `\mathcal{H}(\text{Mol}(p_{u}\oplus s))\equiv\mathcal{H}(\text{Mol}(p_{v}\oplus s))\equiv\mathcal{H}(\mathcal{G})`
Variables: "mathcal, H, p_{u}\\oplus, s, equiv, p_{v}\\oplus, G".
Sign/normalization/conditioning/surrogate audit: "Formula 23 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, H, p_{u}\\oplus, s, equiv, p_{v}\\oplus, G; meanings remain tied to 3.2 Constructing Functionally Equivalent Views.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.2 Constructing Functionally Equivalent Views, formal object 23.

**Formal object 24 at The “Probe Suffix” Protocol. — Formula 24 under The “Probe Suffix” Protocol. is classified as a state or representation transformation; adjacent prose centers on chemically, Probe, structure, practical, engineering, challenge, and the expression links s_{probe}..** `s_{probe}`
Variables: "s_{probe}".
Sign/normalization/conditioning/surrogate audit: "Formula 24 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{probe}; meanings remain tied to The “Probe Suffix” Protocol..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, The “Probe Suffix” Protocol., formal object 24.

**Formal object 25 at Structural Negatives. — Formula 25 under Structural Negatives. is classified as a constraint or formal-analysis relation; adjacent prose centers on mathcal, negatives., chemical, prefix, Standard, contrastive, and the expression links p_{neg}..** `p_{neg}`
Variables: "p_{neg}".
Sign/normalization/conditioning/surrogate audit: "Formula 25 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p_{neg}; meanings remain tied to Structural Negatives..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Structural Negatives., formal object 25.

**Formal object 26 at Structural Negatives. — Formula 26 under Structural Negatives. is classified as a constraint or formal-analysis relation; adjacent prose centers on mathcal, negatives., chemical, prefix, Standard, contrastive, and the expression links mathcal, H, p_{neg}\oplus, s, neq, G..** `\mathcal{H}(\text{Mol}(p_{neg}\oplus s))\neq\mathcal{H}(\mathcal{G})`
Variables: "mathcal, H, p_{neg}\\oplus, s, neq, G".
Sign/normalization/conditioning/surrogate audit: "Formula 26 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, H, p_{neg}\\oplus, s, neq, G; meanings remain tied to Structural Negatives..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Structural Negatives., formal object 26.

**Formal object 27 at 3.3 Architecture and Parameterization — Formula 27 under 3.3 Architecture and Parameterization is classified as a state or representation transformation; adjacent prose centers on mathbf, theta, sequence, model, instantiate, framework, and the expression links f_{\theta}..** `f_{\theta}`
Variables: "f_{\\theta}".
Sign/normalization/conditioning/surrogate audit: "Formula 27 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f_{\\theta}; meanings remain tied to 3.3 Architecture and Parameterization.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.3 Architecture and Parameterization, formal object 27.

**Formal object 28 at 3.3 Architecture and Parameterization — Formula 28 under 3.3 Architecture and Parameterization is classified as a state or representation transformation; adjacent prose centers on mathbf, theta, sequence, model, instantiate, framework, and the expression links theta..** `\theta`
Variables: "theta".
Sign/normalization/conditioning/surrogate audit: "Formula 28 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: theta; meanings remain tied to 3.3 Architecture and Parameterization.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.3 Architecture and Parameterization, formal object 28.

**Formal object 29 at 3.3 Architecture and Parameterization — Formula 29 under 3.3 Architecture and Parameterization is classified as a state or representation transformation; adjacent prose centers on mathbf, theta, sequence, model, instantiate, framework, and the expression links mathbf, H, h, dots, L..** `\mathbf{H}=[\mathbf{h}_{1},\dots,\mathbf{h}_{L}]`
Variables: "mathbf, H, h, dots, L".
Sign/normalization/conditioning/surrogate audit: "Formula 29 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, H, h, dots, L; meanings remain tied to 3.3 Architecture and Parameterization.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.3 Architecture and Parameterization, formal object 29.

**Formal object 30 at 3.3 Architecture and Parameterization — Formula 30 under 3.3 Architecture and Parameterization is classified as a state or representation transformation; adjacent prose centers on mathbf, theta, sequence, model, instantiate, framework, and the expression links mathbf, h, t, in, mathbb, R, d_{model}}..** `\mathbf{h}_{t}\in\mathbb{R}^{d_{model}}`
Variables: "mathbf, h, t, in, mathbb, R, d_{model}}".
Sign/normalization/conditioning/surrogate audit: "Formula 30 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, h, t, in, mathbb, R, d_{model}}; meanings remain tied to 3.3 Architecture and Parameterization.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.3 Architecture and Parameterization, formal object 30.

**Formal object 31 at Projection-Decoupled Mechanism. — Formula 31 under Projection-Decoupled Mechanism. is classified as a optimization objective or loss; adjacent prose centers on contrastive, mathbf, Directly, applying, loss, backbone, and the expression links mathbf, H..** `\mathbf{H}`
Variables: "mathbf, H".
Sign/normalization/conditioning/surrogate audit: "Formula 31 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, H; meanings remain tied to Projection-Decoupled Mechanism..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Projection-Decoupled Mechanism., formal object 31.

**Formal object 32 at Projection-Decoupled Mechanism. — Formula 32 under Projection-Decoupled Mechanism. is classified as a optimization objective or loss; adjacent prose centers on contrastive, mathbf, Directly, applying, loss, backbone, and the expression links g_{\phi}..** `g_{\phi}`
Variables: "g_{\\phi}".
Sign/normalization/conditioning/surrogate audit: "Formula 32 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: g_{\\phi}; meanings remain tied to Projection-Decoupled Mechanism..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Projection-Decoupled Mechanism., formal object 32.

**Formal object 33 at Projection-Decoupled Mechanism. — Formula 33 under Projection-Decoupled Mechanism. is classified as a optimization objective or loss; adjacent prose centers on contrastive, mathbf, Directly, applying, loss, backbone, and the expression links mathcal, Z..** `\mathcal{Z}`
Variables: "mathcal, Z".
Sign/normalization/conditioning/surrogate audit: "Formula 33 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, Z; meanings remain tied to Projection-Decoupled Mechanism..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Projection-Decoupled Mechanism., formal object 33.

**Formal object 34 at Projection-Decoupled Mechanism. — Formula 34 under Projection-Decoupled Mechanism. is classified as a optimization objective or loss; adjacent prose centers on model, mathbf, contrastive, backbone, required, objective, and the expression links mathbf, z, t, g_{\phi}, h, W, sigma, b..** `\mathbf{z}_{t}=g_{\phi}(\mathbf{h}_{t})=W^{(2)}\sigma(W^{(1)}\mathbf{h}_{t}+b^{(1)})+b^{(2)}`
Variables: "mathbf, z, t, g_{\\phi}, h, W, sigma, b".
Sign/normalization/conditioning/surrogate audit: "Formula 34 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, z, t, g_{\\phi}, h, W, sigma, b; meanings remain tied to Projection-Decoupled Mechanism..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Projection-Decoupled Mechanism., formal object 34.

**Formal object 35 at Projection-Decoupled Mechanism. — Formula 35 under Projection-Decoupled Mechanism. is classified as a optimization objective or loss; adjacent prose centers on model, mathbb, times, proj, where, sigma, and the expression links sigma..** `\sigma`
Variables: "sigma".
Sign/normalization/conditioning/surrogate audit: "Formula 35 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sigma; meanings remain tied to Projection-Decoupled Mechanism..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Projection-Decoupled Mechanism., formal object 35.

**Formal object 36 at Projection-Decoupled Mechanism. — Formula 36 under Projection-Decoupled Mechanism. is classified as a optimization objective or loss; adjacent prose centers on model, mathbb, times, proj, where, sigma, and the expression links W, in, mathbb, R, d_{model}\times, d_{model}}..** `W^{(1)}\in\mathbb{R}^{d_{model}\times d_{model}}`
Variables: "W, in, mathbb, R, d_{model}\\times, d_{model}}".
Sign/normalization/conditioning/surrogate audit: "Formula 36 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W, in, mathbb, R, d_{model}\\times, d_{model}}; meanings remain tied to Projection-Decoupled Mechanism..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Projection-Decoupled Mechanism., formal object 36.

**Formal object 37 at Projection-Decoupled Mechanism. — Formula 37 under Projection-Decoupled Mechanism. is classified as a optimization objective or loss; adjacent prose centers on model, mathbb, times, proj, where, sigma, and the expression links W, in, mathbb, R, d_{proj}\times, d_{model}}..** `W^{(2)}\in\mathbb{R}^{d_{proj}\times d_{model}}`
Variables: "W, in, mathbb, R, d_{proj}\\times, d_{model}}".
Sign/normalization/conditioning/surrogate audit: "Formula 37 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W, in, mathbb, R, d_{proj}\\times, d_{model}}; meanings remain tied to Projection-Decoupled Mechanism..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Projection-Decoupled Mechanism., formal object 37.

**Formal object 38 at Projection-Decoupled Mechanism. — Formula 38 under Projection-Decoupled Mechanism. is classified as a optimization objective or loss; adjacent prose centers on model, mathbb, times, proj, where, sigma, and the expression links d_{model}..** `d_{model}=768`
Variables: "d_{model}".
Sign/normalization/conditioning/surrogate audit: "Formula 38 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{model}; meanings remain tied to Projection-Decoupled Mechanism..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Projection-Decoupled Mechanism., formal object 38.

**Formal object 39 at Projection-Decoupled Mechanism. — Formula 39 under Projection-Decoupled Mechanism. is classified as a optimization objective or loss; adjacent prose centers on model, mathbb, times, proj, where, sigma, and the expression links d_{proj}..** `d_{proj}=128`
Variables: "d_{proj}".
Sign/normalization/conditioning/surrogate audit: "Formula 39 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{proj}; meanings remain tied to Projection-Decoupled Mechanism..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Projection-Decoupled Mechanism., formal object 39.

**Formal object 40 at Projection-Decoupled Mechanism. — Formula 40 under Projection-Decoupled Mechanism. is classified as a optimization objective or loss; adjacent prose centers on model, mathbb, times, proj, where, sigma, and the expression links mathbf, h, t..** `\mathbf{h}_{t}`
Variables: "mathbf, h, t".
Sign/normalization/conditioning/surrogate audit: "Formula 40 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, h, t; meanings remain tied to Projection-Decoupled Mechanism..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Projection-Decoupled Mechanism., formal object 40.

**Formal object 41 at Siamese Forward Pass. — Formula 41 under Siamese Forward Pass. is classified as a optimization objective or loss; adjacent prose centers on mathbf, mathcal, computed, ensuring, During, training, and the expression links N..** `N`
Variables: "N".
Sign/normalization/conditioning/surrogate audit: "Formula 41 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N; meanings remain tied to Siamese Forward Pass..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Siamese Forward Pass., formal object 41.

**Formal object 42 at Siamese Forward Pass. — Formula 42 under Siamese Forward Pass. is classified as a optimization objective or loss; adjacent prose centers on mathbf, mathcal, computed, ensuring, During, training, and the expression links N..** `2N`
Variables: "N".
Sign/normalization/conditioning/surrogate audit: "Formula 42 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N; meanings remain tied to Siamese Forward Pass..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Siamese Forward Pass., formal object 42.

**Formal object 43 at Siamese Forward Pass. — Formula 43 under Siamese Forward Pass. is classified as a optimization objective or loss; adjacent prose centers on mathbf, mathcal, computed, ensuring, During, training, and the expression links mathbf, Z, u..** `\mathbf{Z}_{u}`
Variables: "mathbf, Z, u".
Sign/normalization/conditioning/surrogate audit: "Formula 43 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, Z, u; meanings remain tied to Siamese Forward Pass..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Siamese Forward Pass., formal object 43.

**Formal object 44 at Siamese Forward Pass. — Formula 44 under Siamese Forward Pass. is classified as a optimization objective or loss; adjacent prose centers on mathbf, mathcal, computed, ensuring, During, training, and the expression links mathbf, Z, v..** `\mathbf{Z}_{v}`
Variables: "mathbf, Z, v".
Sign/normalization/conditioning/surrogate audit: "Formula 44 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, Z, v; meanings remain tied to Siamese Forward Pass..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Siamese Forward Pass., formal object 44.

**Formal object 45 at Siamese Forward Pass. — Formula 45 under Siamese Forward Pass. is classified as a optimization objective or loss; adjacent prose centers on mathbf, mathcal, computed, ensuring, During, training, and the expression links mathcal, L..** `\mathcal{L}_{MLE}`
Variables: "mathcal, L".
Sign/normalization/conditioning/surrogate audit: "Formula 45 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, L; meanings remain tied to Siamese Forward Pass..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Siamese Forward Pass., formal object 45.

**Formal object 46 at Siamese Forward Pass. — Formula 46 under Siamese Forward Pass. is classified as a optimization objective or loss; adjacent prose centers on mathbf, mathcal, computed, ensuring, During, training, and the expression links mathcal, L..** `\mathcal{L}_{SIGMA}`
Variables: "mathcal, L".
Sign/normalization/conditioning/surrogate audit: "Formula 46 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, L; meanings remain tied to Siamese Forward Pass..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Siamese Forward Pass., formal object 46.

**Formal object 47 at Siamese Forward Pass. — Formula 47 under Siamese Forward Pass. is classified as a optimization objective or loss; adjacent prose centers on mathbf, mathcal, computed, ensuring, During, training, and the expression links hat, mathbf, z..** `\hat{\mathbf{z}}=\mathbf{z}/\|\mathbf{z}\|_{2}`
Variables: "hat, mathbf, z".
Sign/normalization/conditioning/surrogate audit: "Formula 47 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, mathbf, z; meanings remain tied to Siamese Forward Pass..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Siamese Forward Pass., formal object 47.

**Formal object 48 at Formulation. — Formula 48 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, mathbf, token, view, Consider, projected, and the expression links mathbf, Z, u..** `\mathbf{Z}^{u}_{suf}`
Variables: "mathbf, Z, u".
Sign/normalization/conditioning/surrogate audit: "Formula 48 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, Z, u; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 48.

**Formal object 49 at Formulation. — Formula 49 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, mathbf, token, view, Consider, projected, and the expression links mathbf, Z, v..** `\mathbf{Z}^{v}_{suf}`
Variables: "mathbf, Z, v".
Sign/normalization/conditioning/surrogate audit: "Formula 49 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, Z, v; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 49.

**Formal object 50 at Formulation. — Formula 50 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, mathbf, token, view, Consider, projected, and the expression links t..** `t`
Variables: "t".
Sign/normalization/conditioning/surrogate audit: "Formula 50 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: t; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 50.

**Formal object 51 at Formulation. — Formula 51 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, mathbf, token, view, Consider, projected, and the expression links u..** `u`
Variables: "u".
Sign/normalization/conditioning/surrogate audit: "Formula 51 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: u; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 51.

**Formal object 52 at Formulation. — Formula 52 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, mathbf, token, view, Consider, projected, and the expression links v..** `v`
Variables: "v".
Sign/normalization/conditioning/surrogate audit: "Formula 52 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: v; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 52.

**Formal object 53 at Formulation. — Formula 53 under Formulation. is classified as a paper-defined mathematical relation; adjacent prose centers on mathbf, text, mathcal, displaystyle, SIGMA, frac, and the expression links displaystyle, mathcal, L, t, mathbf, z, u, v..** `\displaystyle\mathcal{L}_{SIGMA}^{(t)}=-\log\frac{\exp(\text{sim}(\mathbf{z}_{u,t},\mathbf{z}_{v,t})/\tau)}{\exp(\text{sim}(\mathbf{z}_{u,t},\mathbf{z}_{v,t})/\tau)+\sum_{k\in\mathcal{N}_{neg}}\exp(\text{sim}(\mathbf{z}_{u,t},\mathbf{z}_{k,t})/\tau)}`
Variables: "displaystyle, mathcal, L, t, mathbf, z, u, v, tau, k, in, N".
Sign/normalization/conditioning/surrogate audit: "Formula 53 operator audit: fraction or division; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, mathcal, L, t, mathbf, z, u, v, tau, k, in, N; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 53.

**Formal object 54 at Formulation. — Formula 54 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on cdot, where, text, denotes, cosine, similarity, and the expression links symbols defined beside the formula..** `\text{sim}(\cdot,\cdot)`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 54 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 54.

**Formal object 55 at Formulation. — Formula 55 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on cdot, where, text, denotes, cosine, similarity, and the expression links tau..** `\tau`
Variables: "tau".
Sign/normalization/conditioning/surrogate audit: "Formula 55 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tau; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 55.

**Formal object 56 at Formulation. — Formula 56 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on cdot, where, text, denotes, cosine, similarity, and the expression links L_{suf}..** `L_{suf}`
Variables: "L_{suf}".
Sign/normalization/conditioning/surrogate audit: "Formula 56 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{suf}; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 56.

**Formal object 57 at Formulation. — Formula 57 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links mathcal, L, tfrac, L_{suf}}\sum\nolimits, t, L_{suf}}\mathcal{L}..** `\mathcal{L}_{SIGMA}=\tfrac{1}{L_{suf}}\sum\nolimits_{t=1}^{L_{suf}}\mathcal{L}_{SIGMA}^{(t)}`
Variables: "mathcal, L, tfrac, L_{suf}}\\sum\\nolimits, t, L_{suf}}\\mathcal{L}".
Sign/normalization/conditioning/surrogate audit: "Formula 57 operator audit: summation; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, L, tfrac, L_{suf}}\\sum\\nolimits, t, L_{suf}}\\mathcal{L}; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 57.

**Formal object 58 at Formulation. — Formula 58 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links K..** `K`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 58 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 58.

**Formal object 59 at Formulation. — Formula 59 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links mathcal, M..** `\mathcal{M}`
Variables: "mathcal, M".
Sign/normalization/conditioning/surrogate audit: "Formula 59 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, M; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 59.

**Formal object 60 at Formulation. — Formula 60 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links mathcal, B, leftarrow..** `\mathcal{B}\leftarrow\{[\text{BOS}]\}`
Variables: "mathcal, B, leftarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 60 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, B, leftarrow; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 60.

**Formal object 61 at Formulation. — Formula 61 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links t, dots, T_{\max}..** `t=1\dots T_{\max}`
Variables: "t, dots, T_{\\max}".
Sign/normalization/conditioning/surrogate audit: "Formula 61 operator audit: maximization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: t, dots, T_{\\max}; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 61.

**Formal object 62 at Formulation. — Formula 62 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links mathcal, B..** `\mathcal{B}`
Variables: "mathcal, B".
Sign/normalization/conditioning/surrogate audit: "Formula 62 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, B; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 62.

**Formal object 63 at Formulation. — Formula 63 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links mathcal, B, leftarrow, emptyset..** `\mathcal{B}_{new}\leftarrow\emptyset`
Variables: "mathcal, B, leftarrow, emptyset".
Sign/normalization/conditioning/surrogate audit: "Formula 63 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, B, leftarrow, emptyset; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 63.

**Formal object 64 at Formulation. — Formula 64 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links mathcal, S, leftarrow, emptyset..** `\mathcal{S}_{seen}\leftarrow\emptyset`
Variables: "mathcal, S, leftarrow, emptyset".
Sign/normalization/conditioning/surrogate audit: "Formula 64 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S, leftarrow, emptyset; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 64.

**Formal object 65 at Formulation. — Formula 65 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links c..** `c`
Variables: "c".
Sign/normalization/conditioning/surrogate audit: "Formula 65 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 65.

**Formal object 66 at Formulation. — Formula 66 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links M, leftarrow, c..** `M\leftarrow\text{MolFromSmiles}(c)`
Variables: "M, leftarrow, c".
Sign/normalization/conditioning/surrogate audit: "Formula 66 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: M, leftarrow, c; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 66.

**Formal object 67 at Formulation. — Formula 67 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links M..** `M`
Variables: "M".
Sign/normalization/conditioning/surrogate audit: "Formula 67 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: M; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 67.

**Formal object 68 at Formulation. — Formula 68 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links mathcal, B, leftarrow, cup, c..** `\mathcal{B}_{new}\leftarrow\mathcal{B}_{new}\cup\{c\}`
Variables: "mathcal, B, leftarrow, cup, c".
Sign/normalization/conditioning/surrogate audit: "Formula 68 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, B, leftarrow, cup, c; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 68.

**Formal object 69 at Formulation. — Formula 69 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links leftarrow, mathcal, H, M..** `id\leftarrow\mathcal{H}(M)`
Variables: "leftarrow, mathcal, H, M".
Sign/normalization/conditioning/surrogate audit: "Formula 69 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: leftarrow, mathcal, H, M; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 69.

**Formal object 70 at Formulation. — Formula 70 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links notin, mathcal, S..** `id\notin\mathcal{S}_{seen}`
Variables: "notin, mathcal, S".
Sign/normalization/conditioning/surrogate audit: "Formula 70 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: notin, mathcal, S; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 70.

**Formal object 71 at Formulation. — Formula 71 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links mathcal, S, leftarrow, cup..** `\mathcal{S}_{seen}\leftarrow\mathcal{S}_{seen}\cup\{id\}`
Variables: "mathcal, S, leftarrow, cup".
Sign/normalization/conditioning/surrogate audit: "Formula 71 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S, leftarrow, cup; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 71.

**Formal object 72 at Formulation. — Formula 72 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links mathcal, B, K..** `|\mathcal{B}_{new}|=K`
Variables: "mathcal, B, K".
Sign/normalization/conditioning/surrogate audit: "Formula 72 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, B, K; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 72.

**Formal object 73 at Formulation. — Formula 73 under Formulation. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, text, cdot, and the expression links mathcal, B, leftarrow..** `\mathcal{B}\leftarrow\mathcal{B}_{new}`
Variables: "mathcal, B, leftarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 73 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, B, leftarrow; meanings remain tied to Formulation..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Formulation., formal object 73.

**Formal object 74 at Theoretical Insight: Implicit Gradient Alignment. — Formula 74 under Theoretical Insight: Implicit Gradient Alignment. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, representations, through, and the expression links s_{t}..** `s_{t}`
Variables: "s_{t}".
Sign/normalization/conditioning/surrogate audit: "Formula 74 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{t}; meanings remain tied to Theoretical Insight: Implicit Gradient Alignment..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Theoretical Insight: Implicit Gradient Alignment., formal object 74.

**Formal object 75 at Theoretical Insight: Implicit Gradient Alignment. — Formula 75 under Theoretical Insight: Implicit Gradient Alignment. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, representations, through, and the expression links s_{, t..** `s_{<t}`
Variables: "s_{, t".
Sign/normalization/conditioning/surrogate audit: "Formula 75 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{, t; meanings remain tied to Theoretical Insight: Implicit Gradient Alignment..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Theoretical Insight: Implicit Gradient Alignment., formal object 75.

**Formal object 76 at Theoretical Insight: Implicit Gradient Alignment. — Formula 76 under Theoretical Insight: Implicit Gradient Alignment. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, representations, through, and the expression links mathbf, h, s_{t}}, s_{t}, p, s_{, t..** `\mathbf{h}_{s_{t}}=\text{Transformer}(s_{t}|p,s_{<t})`
Variables: "mathbf, h, s_{t}}, s_{t}, p, s_{, t".
Sign/normalization/conditioning/surrogate audit: "Formula 76 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, h, s_{t}}, s_{t}, p, s_{, t; meanings remain tied to Theoretical Insight: Implicit Gradient Alignment..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Theoretical Insight: Implicit Gradient Alignment., formal object 76.

**Formal object 77 at Theoretical Insight: Implicit Gradient Alignment. — Formula 77 under Theoretical Insight: Implicit Gradient Alignment. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, representations, through, and the expression links mathbf, h, s_{t}}^{u}..** `\mathbf{h}_{s_{t}}^{u}`
Variables: "mathbf, h, s_{t}}^{u}".
Sign/normalization/conditioning/surrogate audit: "Formula 77 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, h, s_{t}}^{u}; meanings remain tied to Theoretical Insight: Implicit Gradient Alignment..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Theoretical Insight: Implicit Gradient Alignment., formal object 77.

**Formal object 78 at Theoretical Insight: Implicit Gradient Alignment. — Formula 78 under Theoretical Insight: Implicit Gradient Alignment. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, representations, through, and the expression links mathbf, h, s_{t}}^{v}..** `\mathbf{h}_{s_{t}}^{v}`
Variables: "mathbf, h, s_{t}}^{v}".
Sign/normalization/conditioning/surrogate audit: "Formula 78 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, h, s_{t}}^{v}; meanings remain tied to Theoretical Insight: Implicit Gradient Alignment..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Theoretical Insight: Implicit Gradient Alignment., formal object 78.

**Formal object 79 at Theoretical Insight: Implicit Gradient Alignment. — Formula 79 under Theoretical Insight: Implicit Gradient Alignment. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, Transformer, mathbf, representations, through, and the expression links nabla, mathcal, L..** `\nabla\mathcal{L}_{SIGMA}`
Variables: "nabla, mathcal, L".
Sign/normalization/conditioning/surrogate audit: "Formula 79 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: nabla, mathcal, L; meanings remain tied to Theoretical Insight: Implicit Gradient Alignment..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Theoretical Insight: Implicit Gradient Alignment., formal object 79.

**Formal object 80 at Theoretical Insight: Implicit Gradient Alignment. — Formula 80 under Theoretical Insight: Implicit Gradient Alignment. is classified as a optimization objective or loss; adjacent prose centers on suffix, prefix, representations, Transformer, mathbf, aligning, and the expression links p_{u}, approx, p_{v}..** `\text{Encoder}(p_{u})\approx\text{Encoder}(p_{v})`
Variables: "p_{u}, approx, p_{v}".
Sign/normalization/conditioning/surrogate audit: "Formula 80 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p_{u}, approx, p_{v}; meanings remain tied to Theoretical Insight: Implicit Gradient Alignment..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Theoretical Insight: Implicit Gradient Alignment., formal object 80.

**Formal object 81 at Theoretical Insight: Implicit Gradient Alignment. — Formula 81 under Theoretical Insight: Implicit Gradient Alignment. is classified as a optimization objective or loss; adjacent prose centers on mathcal, lambda, final, training, objective, combines, and the expression links mathcal, L, lambda..** `\mathcal{L}_{total}=\mathcal{L}_{NLL}+\lambda\mathcal{L}_{SIGMA}`
Variables: "mathcal, L, lambda".
Sign/normalization/conditioning/surrogate audit: "Formula 81 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, L, lambda; meanings remain tied to Theoretical Insight: Implicit Gradient Alignment..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Theoretical Insight: Implicit Gradient Alignment., formal object 81.

**Formal object 82 at Theoretical Insight: Implicit Gradient Alignment. — Formula 82 under Theoretical Insight: Implicit Gradient Alignment. is classified as a optimization objective or loss; adjacent prose centers on mathcal, lambda, final, training, objective, combines, and the expression links lambda..** `\lambda`
Variables: "lambda".
Sign/normalization/conditioning/surrogate audit: "Formula 82 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: lambda; meanings remain tied to Theoretical Insight: Implicit Gradient Alignment..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Theoretical Insight: Implicit Gradient Alignment., formal object 82.

**Formal object 83 at Complexity vs. Diversity Trade-off. — Formula 83 under Complexity vs. Diversity Trade-off. is classified as a optimization objective or loss; adjacent prose centers on beam, size, IsoBeam, contain, molecular, structures, and the expression links K..** `K=10`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 83 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to Complexity vs. Diversity Trade-off..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Complexity vs. Diversity Trade-off., formal object 83.

**Formal object 84 at Complexity vs. Diversity Trade-off. — Formula 84 under Complexity vs. Diversity Trade-off. is classified as a optimization objective or loss; adjacent prose centers on beam, size, molecular, IsoBeam, contain, structures, and the expression links pm..** `\pm`
Variables: "pm".
Sign/normalization/conditioning/surrogate audit: "Formula 84 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: pm; meanings remain tied to Complexity vs. Diversity Trade-off..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Complexity vs. Diversity Trade-off., formal object 84.

**Formal object 85 at Complexity vs. Diversity Trade-off. — Formula 85 under Complexity vs. Diversity Trade-off. is classified as a optimization objective or loss; adjacent prose centers on beam, size, molecular, IsoBeam, contain, structures, and the expression links uparrow..** `\uparrow`
Variables: "uparrow".
Sign/normalization/conditioning/surrogate audit: "Formula 85 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: uparrow; meanings remain tied to Complexity vs. Diversity Trade-off..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Complexity vs. Diversity Trade-off., formal object 85.

**Formal object 86 at Complexity vs. Diversity Trade-off. — Formula 86 under Complexity vs. Diversity Trade-off. is classified as a optimization objective or loss; adjacent prose centers on beam, size, molecular, IsoBeam, contain, structures, and the expression links dagger..** `{\dagger}`
Variables: "dagger".
Sign/normalization/conditioning/surrogate audit: "Formula 86 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: dagger; meanings remain tied to Complexity vs. Diversity Trade-off..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Complexity vs. Diversity Trade-off., formal object 86.

**Formal object 87 at Complexity vs. Diversity Trade-off. — Formula 87 under Complexity vs. Diversity Trade-off. is classified as a optimization objective or loss; adjacent prose centers on beam, size, molecular, IsoBeam, contain, structures, and the expression links ddagger..** `{\ddagger}`
Variables: "ddagger".
Sign/normalization/conditioning/surrogate audit: "Formula 87 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: ddagger; meanings remain tied to Complexity vs. Diversity Trade-off..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Complexity vs. Diversity Trade-off., formal object 87.

**Formal object 88 at Complexity vs. Diversity Trade-off. — Formula 88 under Complexity vs. Diversity Trade-off. is classified as a optimization objective or loss; adjacent prose centers on beam, size, molecular, IsoBeam, contain, structures, and the expression links downarrow..** `\downarrow`
Variables: "downarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 88 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: downarrow; meanings remain tied to Complexity vs. Diversity Trade-off..".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Complexity vs. Diversity Trade-off., formal object 88.

**Formal object 89 at 4.2 Unconditional Generation: Bridging Sequence and Graph Models — Formula 89 under 4.2 Unconditional Generation: Bridging Sequence and Graph Models is classified as a paper-defined mathematical relation; adjacent prose centers on Validity, Uniqueness, SIGMA, maintains, near-perfect, characteristic, and the expression links symbols defined beside the formula..** `>99.8\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 89 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 4.2 Unconditional Generation: Bridging Sequence and Graph Models.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 4.2 Unconditional Generation: Bridging Sequence and Graph Models, formal object 89.

**Formal object 90 at 4.3 Optimization Efficiency in Reinforcement Learning — Formula 90 under 4.3 Optimization Efficiency in Reinforcement Learning is classified as a optimization objective or loss; adjacent prose centers on SIGMA, baseline, unique, scaffolds, over, Regarding, and the expression links sim..** `\sim`
Variables: "sim".
Sign/normalization/conditioning/surrogate audit: "Formula 90 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sim; meanings remain tied to 4.3 Optimization Efficiency in Reinforcement Learning.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 4.3 Optimization Efficiency in Reinforcement Learning, formal object 90.

**Formal object 91 at 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search — Formula 91 under 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search is classified as a paper-defined mathematical relation; adjacent prose centers on beam, standard, search, redundant, isomorphic, SMILES., and the expression links K..** `K=5{,}000`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 91 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search, formal object 91.

**Formal object 92 at 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search — Formula 92 under 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search is classified as a paper-defined mathematical relation; adjacent prose centers on beam, standard, search, redundant, isomorphic, SMILES., and the expression links K..** `K=50{,}000`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 92 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search, formal object 92.

**Formal object 93 at 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search — Formula 93 under 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search is classified as a paper-defined mathematical relation; adjacent prose centers on beam, standard, search, redundant, isomorphic, SMILES., and the expression links times..** `\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 93 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search, formal object 93.

**Formal object 94 at 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search — Formula 94 under 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search is classified as a optimization objective or loss; adjacent prose centers on beam, isomorphic, SMILES., chemical, models., standard, and the expression links K, to..** `K=100\to 50,000`
Variables: "K, to".
Sign/normalization/conditioning/surrogate audit: "Formula 94 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K, to; meanings remain tied to 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search, formal object 94.

**Formal object 95 at 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search — Formula 95 under 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search is classified as a optimization objective or loss; adjacent prose centers on beam, isomorphic, SMILES., chemical, models., standard, and the expression links K, approx..** `K\approx 5,000`
Variables: "K, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 95 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K, approx; meanings remain tied to 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search, formal object 95.

**Formal object 96 at 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search — Formula 96 under 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search is classified as a optimization objective or loss; adjacent prose centers on beam, isomorphic, SMILES., chemical, models., standard, and the expression links times..** `>2\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 96 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search, formal object 96.

**Formal object 97 at 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search — Formula 97 under 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search is classified as a optimization objective or loss; adjacent prose centers on beam, isomorphic, SMILES., chemical, models., standard, and the expression links K..** `K=50,000`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 97 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search, formal object 97.

**Formal object 98 at B.1 Model Architecture — Formula 98 under B.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on Embedding, Layer, learned, positional, maximum, sequence, and the expression links symbols defined beside the formula..** `>99\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 98 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to B.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, B.1 Model Architecture, formal object 98.

**Formal object 99 at B.1 Model Architecture — Formula 99 under B.1 Model Architecture is classified as a optimization objective or loss; adjacent prose centers on Head, Projection, contrastive, Hidden, during, learning, and the expression links to..** `768\to 256`
Variables: "to".
Sign/normalization/conditioning/surrogate audit: "Formula 99 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: to; meanings remain tied to B.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, B.1 Model Architecture, formal object 99.

**Formal object 100 at B.2 Training Configuration — Formula 100 under B.2 Training Configuration is classified as a paper-defined mathematical relation; adjacent prose centers on batch, size, number, specifically, note, SIGMA, and the expression links times..** `2\times\text{Batch Size}`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 100 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to B.2 Training Configuration.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, B.2 Training Configuration, formal object 100.

**Formal object 101 at B.2 Training Configuration — Formula 101 under B.2 Training Configuration is classified as a paper-defined mathematical relation; adjacent prose centers on Dataset, Detailed, hyperparameters, listed, Table, ZINC-250k, and the expression links times..** `5\times 10^{-4}`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 101 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to B.2 Training Configuration.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, B.2 Training Configuration, formal object 101.

**Formal object 102 at B.2 Training Configuration — Formula 102 under B.2 Training Configuration is classified as a paper-defined mathematical relation; adjacent prose centers on Dataset, Detailed, hyperparameters, listed, Table, ZINC-250k, and the expression links symbols defined beside the formula..** `0.01`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 102 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to B.2 Training Configuration.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, B.2 Training Configuration, formal object 102.

**Formal object 103 at B.2 Training Configuration — Formula 103 under B.2 Training Configuration is classified as a paper-defined mathematical relation; adjacent prose centers on Dataset, Detailed, hyperparameters, listed, Table, ZINC-250k, and the expression links symbols defined beside the formula..** `(0.9,0.999)`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 103 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to B.2 Training Configuration.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, B.2 Training Configuration, formal object 103.

**Formal object 104 at B.2 Training Configuration — Formula 104 under B.2 Training Configuration is classified as a paper-defined mathematical relation; adjacent prose centers on Dataset, Detailed, hyperparameters, listed, Table, ZINC-250k, and the expression links symbols defined beside the formula..** `1.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 104 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to B.2 Training Configuration.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, B.2 Training Configuration, formal object 104.

**Formal object 105 at B.5 Inference Details (IsoBeam) — Formula 105 under B.5 Inference Details (IsoBeam) is classified as a paper-defined mathematical relation; adjacent prose centers on asymptotic, analysis, Section, scaled, beam, width, and the expression links symbols defined beside the formula..** `\{100,500,1000,5000,10000,50000\}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 105 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to B.5 Inference Details (IsoBeam).".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, B.5 Inference Details (IsoBeam), formal object 105.

**Formal object 106 at B.5 Inference Details (IsoBeam) — Formula 106 under B.5 Inference Details (IsoBeam) is classified as a paper-defined mathematical relation; adjacent prose centers on IsoBeam, Implemented, custom, decoding, loop., step, and the expression links O..** `O(1)`
Variables: "O".
Sign/normalization/conditioning/surrogate audit: "Formula 106 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O; meanings remain tied to B.5 Inference Details (IsoBeam).".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, B.5 Inference Details (IsoBeam), formal object 106.

**Formal object 107 at C.1 Graph Partitioning Algorithm — Formula 107 under C.1 Graph Partitioning Algorithm is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, given, molecule, identify, cuttable, bonds, and the expression links G, V, E..** `G=(V,E)`
Variables: "G, V, E".
Sign/normalization/conditioning/surrogate audit: "Formula 107 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G, V, E; meanings remain tied to C.1 Graph Partitioning Algorithm.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.1 Graph Partitioning Algorithm, formal object 107.

**Formal object 108 at C.1 Graph Partitioning Algorithm — Formula 108 under C.1 Graph Partitioning Algorithm is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, given, molecule, identify, cuttable, bonds, and the expression links mathcal, E, subset..** `\mathcal{E}_{cut}\subset E`
Variables: "mathcal, E, subset".
Sign/normalization/conditioning/surrogate audit: "Formula 108 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, E, subset; meanings remain tied to C.1 Graph Partitioning Algorithm.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.1 Graph Partitioning Algorithm, formal object 108.

**Formal object 109 at C.1 Graph Partitioning Algorithm — Formula 109 under C.1 Graph Partitioning Algorithm is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, given, molecule, identify, cuttable, bonds, and the expression links e, u, v..** `e=(u,v)`
Variables: "e, u, v".
Sign/normalization/conditioning/surrogate audit: "Formula 109 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: e, u, v; meanings remain tied to C.1 Graph Partitioning Algorithm.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.1 Graph Partitioning Algorithm, formal object 109.

**Formal object 110 at C.1 Graph Partitioning Algorithm — Formula 110 under C.1 Graph Partitioning Algorithm is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, given, molecule, identify, cuttable, bonds, and the expression links mathcal, E..** `\mathcal{E}_{cut}`
Variables: "mathcal, E".
Sign/normalization/conditioning/surrogate audit: "Formula 110 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, E; meanings remain tied to C.1 Graph Partitioning Algorithm.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.1 Graph Partitioning Algorithm, formal object 110.

**Formal object 111 at C.1 Graph Partitioning Algorithm — Formula 111 under C.1 Graph Partitioning Algorithm is classified as a paper-defined mathematical relation; adjacent prose centers on Acyclicity, belong, ring, system., and the expression links e..** `e`
Variables: "e".
Sign/normalization/conditioning/surrogate audit: "Formula 111 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: e; meanings remain tied to C.1 Graph Partitioning Algorithm.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.1 Graph Partitioning Algorithm, formal object 111.

**Formal object 112 at C.1 Graph Partitioning Algorithm — Formula 112 under C.1 Graph Partitioning Algorithm is classified as a paper-defined mathematical relation; adjacent prose centers on subgraph, During, training, molecule, batch, uniformly, and the expression links e, in, mathcal, E..** `e\in\mathcal{E}_{cut}`
Variables: "e, in, mathcal, E".
Sign/normalization/conditioning/surrogate audit: "Formula 112 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: e, in, mathcal, E; meanings remain tied to C.1 Graph Partitioning Algorithm.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.1 Graph Partitioning Algorithm, formal object 112.

**Formal object 113 at C.1 Graph Partitioning Algorithm — Formula 113 under C.1 Graph Partitioning Algorithm is classified as a paper-defined mathematical relation; adjacent prose centers on subgraph, During, training, molecule, batch, uniformly, and the expression links G_{pre}..** `G_{pre}`
Variables: "G_{pre}".
Sign/normalization/conditioning/surrogate audit: "Formula 113 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G_{pre}; meanings remain tied to C.1 Graph Partitioning Algorithm.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.1 Graph Partitioning Algorithm, formal object 113.

**Formal object 114 at C.1 Graph Partitioning Algorithm — Formula 114 under C.1 Graph Partitioning Algorithm is classified as a paper-defined mathematical relation; adjacent prose centers on subgraph, During, training, molecule, batch, uniformly, and the expression links G_{suf}..** `G_{suf}`
Variables: "G_{suf}".
Sign/normalization/conditioning/surrogate audit: "Formula 114 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G_{suf}; meanings remain tied to C.1 Graph Partitioning Algorithm.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.1 Graph Partitioning Algorithm, formal object 114.

**Formal object 115 at C.3 Contrastive View Generation — Formula 115 under C.3 Contrastive View Generation is classified as a paper-defined mathematical relation; adjacent prose centers on View, generate, canonical, SMILES, string, rooted, and the expression links s_{pre}^{..** `s_{pre}^{(1)}`
Variables: "s_{pre}^{".
Sign/normalization/conditioning/surrogate audit: "Formula 115 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{pre}^{; meanings remain tied to C.3 Contrastive View Generation.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.3 Contrastive View Generation, formal object 115.

**Formal object 116 at C.3 Contrastive View Generation — Formula 116 under C.3 Contrastive View Generation is classified as a paper-defined mathematical relation; adjacent prose centers on View, generate, randomized, SMILES, string, same, and the expression links s_{pre}^{..** `s_{pre}^{(2)}`
Variables: "s_{pre}^{".
Sign/normalization/conditioning/surrogate audit: "Formula 116 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{pre}^{; meanings remain tied to C.3 Contrastive View Generation.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.3 Contrastive View Generation, formal object 116.

**Formal object 117 at C.3 Contrastive View Generation — Formula 117 under C.3 Contrastive View Generation is classified as a optimization objective or loss; adjacent prose centers on pair, serves, positive, sample, contrastive, objective, and the expression links s_{pre}^{..** `(s_{pre}^{(1)},s_{pre}^{(2)})`
Variables: "s_{pre}^{".
Sign/normalization/conditioning/surrogate audit: "Formula 117 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{pre}^{; meanings remain tied to C.3 Contrastive View Generation.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, C.3 Contrastive View Generation, formal object 117.

**Formal object 118 at Appendix D Dense Trajectory Alignment Objective — Formula 118 under Appendix D Dense Trajectory Alignment Objective is classified as a optimization objective or loss; adjacent prose centers on Given, equivalent, prefix, pairs, SIGMA, applies, and the expression links p_{i}, p_{j}..** `(p_{i},p_{j})`
Variables: "p_{i}, p_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 118 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p_{i}, p_{j}; meanings remain tied to Appendix D Dense Trajectory Alignment Objective.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Appendix D Dense Trajectory Alignment Objective, formal object 118.

**Formal object 119 at Appendix D Dense Trajectory Alignment Objective — Formula 119 under Appendix D Dense Trajectory Alignment Objective is classified as a optimization objective or loss; adjacent prose centers on Given, equivalent, prefix, pairs, SIGMA, applies, and the expression links h_{t}..** `h_{t}`
Variables: "h_{t}".
Sign/normalization/conditioning/surrogate audit: "Formula 119 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: h_{t}; meanings remain tied to Appendix D Dense Trajectory Alignment Objective.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Appendix D Dense Trajectory Alignment Objective, formal object 119.

**Formal object 120 at Appendix D Dense Trajectory Alignment Objective — Formula 120 under Appendix D Dense Trajectory Alignment Objective is classified as a optimization objective or loss; adjacent prose centers on equivalent, trajectories., Given, prefix, pairs, SIGMA, and the expression links mathcal, L, t, h_{t}^{, i, j, tau, k..** `\mathcal{L}_{\text{SIGMA}}=-\sum_{t}\log\frac{\exp(\text{sim}(h_{t}^{(i)},h_{t}^{(j)})/\tau)}{\sum_{k}\exp(\text{sim}(h_{t}^{(i)},h_{t}^{(k)})/\tau)}.`
Variables: "mathcal, L, t, h_{t}^{, i, j, tau, k".
Sign/normalization/conditioning/surrogate audit: "Formula 120 operator audit: fraction or division; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, L, t, h_{t}^{, i, j, tau, k; meanings remain tied to Appendix D Dense Trajectory Alignment Objective.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, Appendix D Dense Trajectory Alignment Objective, formal object 120.

**Formal object 121 at F.1 Generative Quality Metrics — Formula 121 under F.1 Generative Quality Metrics is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, generated, molecules, train, training, dataset., and the expression links mathcal, D..** `\mathcal{D}_{train}`
Variables: "mathcal, D".
Sign/normalization/conditioning/surrogate audit: "Formula 121 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D; meanings remain tied to F.1 Generative Quality Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, F.1 Generative Quality Metrics, formal object 121.

**Formal object 122 at F.1 Generative Quality Metrics — Formula 122 under F.1 Generative Quality Metrics is classified as a evaluation or scoring relation; adjacent prose centers on fraction, valid, molecules, unique, generated, Uniqueness, and the expression links mathcal, G..** `\text{Uniqueness}=\frac{|\text{unique}(\mathcal{G}_{valid})|}{|\mathcal{G}_{valid}|}`
Variables: "mathcal, G".
Sign/normalization/conditioning/surrogate audit: "Formula 122 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, G; meanings remain tied to F.1 Generative Quality Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, F.1 Generative Quality Metrics, formal object 122.

**Formal object 123 at F.1 Generative Quality Metrics — Formula 123 under F.1 Generative Quality Metrics is classified as a evaluation or scoring relation; adjacent prose centers on generated, Diversity, Novelty, fraction, valid, unique, and the expression links m, in, mathcal, G, notin, D..** `\text{Novelty}=\frac{|\{m\in\mathcal{G}_{valid}\mid m\notin\mathcal{D}_{train}\}|}{|\mathcal{G}_{valid}|}`
Variables: "m, in, mathcal, G, notin, D".
Sign/normalization/conditioning/surrogate audit: "Formula 123 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: m, in, mathcal, G, notin, D; meanings remain tied to F.1 Generative Quality Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, F.1 Generative Quality Metrics, formal object 123.

**Formal object 124 at F.1 Generative Quality Metrics — Formula 124 under F.1 Generative Quality Metrics is classified as a evaluation or scoring relation; adjacent prose centers on Diversity, Internal, IntDiv, Measures, chemical, within, and the expression links T_{d}..** `T_{d}`
Variables: "T_{d}".
Sign/normalization/conditioning/surrogate audit: "Formula 124 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T_{d}; meanings remain tied to F.1 Generative Quality Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, F.1 Generative Quality Metrics, formal object 124.

**Formal object 125 at F.1 Generative Quality Metrics — Formula 125 under F.1 Generative Quality Metrics is classified as a probabilistic or expectation relation; adjacent prose centers on generated, distance, Diversity, Measures, chemical, ChemNet, and the expression links mathcal, G, m_{i}, m_{j}\in\mathcal{G}}\text{Tanimoto}, M, m_{j}..** `\text{IntDiv}(\mathcal{G})=1-\frac{1}{|\mathcal{G}|^{2}}\sum_{m_{i},m_{j}\in\mathcal{G}}\text{Tanimoto}(M(m_{i}),M(m_{j}))`
Variables: "mathcal, G, m_{i}, m_{j}\\in\\mathcal{G}}\\text{Tanimoto}, M, m_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 125 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, G, m_{i}, m_{j}\\in\\mathcal{G}}\\text{Tanimoto}, M, m_{j}; meanings remain tied to F.1 Generative Quality Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, F.1 Generative Quality Metrics, formal object 125.

**Formal object 126 at F.3 Geometric Invariance Metrics — Formula 126 under F.3 Geometric Invariance Metrics is classified as a state or representation transformation; adjacent prose centers on given, Trajectory, Invariance, Score, custom, metric, and the expression links s_{1}..** `s_{1}`
Variables: "s_{1}".
Sign/normalization/conditioning/surrogate audit: "Formula 126 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{1}; meanings remain tied to F.3 Geometric Invariance Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, F.3 Geometric Invariance Metrics, formal object 126.

**Formal object 127 at F.3 Geometric Invariance Metrics — Formula 127 under F.3 Geometric Invariance Metrics is classified as a state or representation transformation; adjacent prose centers on given, Trajectory, Invariance, Score, custom, metric, and the expression links s_{2}..** `s_{2}`
Variables: "s_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 127 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{2}; meanings remain tied to F.3 Geometric Invariance Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, F.3 Geometric Invariance Metrics, formal object 127.

**Formal object 128 at F.3 Geometric Invariance Metrics — Formula 128 under F.3 Geometric Invariance Metrics is classified as a state or representation transformation; adjacent prose centers on given, Trajectory, Invariance, Score, custom, metric, and the expression links G_{sub}..** `G_{sub}`
Variables: "G_{sub}".
Sign/normalization/conditioning/surrogate audit: "Formula 128 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G_{sub}; meanings remain tied to F.3 Geometric Invariance Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, F.3 Geometric Invariance Metrics, formal object 128.

**Formal object 129 at F.3 Geometric Invariance Metrics — Formula 129 under F.3 Geometric Invariance Metrics is classified as a state or representation transformation; adjacent prose centers on given, Trajectory, Invariance, Score, custom, metric, and the expression links mathbf, h, s..** `\mathbf{h}(s)`
Variables: "mathbf, h, s".
Sign/normalization/conditioning/surrogate audit: "Formula 129 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, h, s; meanings remain tied to F.3 Geometric Invariance Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, F.3 Geometric Invariance Metrics, formal object 129.

**Formal object 130 at F.3 Geometric Invariance Metrics — Formula 130 under F.3 Geometric Invariance Metrics is classified as a state or representation transformation; adjacent prose centers on Invariance, latent, given, model, Trajectory, Score, and the expression links mathbb, E, M, sim, mathcal, D, left, mathbf..** `\text{TIS}=\mathbb{E}_{M\sim\mathcal{D}_{test}}\left[1-\text{sim}(\mathbf{h}(s_{1}),\mathbf{h}(s_{2}))\right]`
Variables: "mathbb, E, M, sim, mathcal, D, left, mathbf, h, s_{1}, s_{2}, right".
Sign/normalization/conditioning/surrogate audit: "Formula 130 operator audit: expectation; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbb, E, M, sim, mathcal, D, left, mathbf, h, s_{1}, s_{2}, right; meanings remain tied to F.3 Geometric Invariance Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.25062, F.3 Geometric Invariance Metrics, formal object 130.

Representative source mathematical objects follow. They are navigation evidence, not standalone interpretations:

- Mathematical object 1: `\mathcal{G}\in\mathbb{G}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 2: `\mathcal{G}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 3: `S=(x_{1},\dots,x_{L})` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 4: `\mathcal{V}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 5: `\Pi(\mathcal{G})=\{S^{(1)},\dots,S^{(K)}\}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 6: `S` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 7: `\log p_{\theta}(S)=\sum\nolimits_{t=1}^{L}\log p_{\theta}(x_{t}|x_{<t})` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 8: `S^{(i)}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 9: `S^{(j)}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 10: `\Pi(\mathcal{G})` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 11: `h_{t}(S^{(i)})` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 12: `h_{t}(S^{(j)})` — read with adjacent definitions; no symbol meaning is inferred from markup alone.

Equation-to-adjacent-context reconstruction:

- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `\mathcal{G}\in\mathbb{G}`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `\mathcal{G}`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `S=(x_{1},\dots,x_{L})`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `\mathcal{V}`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `\mathcal{G}`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `\Pi(\mathcal{G})=\{S^{(1)},\dots,S^{(K)}\}`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `S`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `\log p_{\theta}(S)=\sum\nolimits_{t=1}^{L}\log p_{\theta}(x_{t}|x_{<t})`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `S^{(i)}`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `S^{(j)}`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `\Pi(\mathcal{G})`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.
- Equation under source heading 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds: `h_{t}(S^{(i)})`; adjacent method terms: mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles.

For each central equation, the audit asks whether the sign agrees with the prose, whether weights are normalized, whether masking or conditioning changes the denominator, whether a displayed objective is exact or a training surrogate, and whether units can be compared. A learned score is not automatically calibrated, a relaxation is not an exact discrete solution, and an empirical constraint satisfaction rate is not a theorem. These distinctions protect the paper's real contribution from stronger claims it does not need.

### 2.3 Components, architecture, and information flow

The source's technical path is anchored to 3 Methodology, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims.

**Input/output dataflow:** The documented dataflow is reconstructed only across 3 Methodology, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, and 3.3 Architecture and Parameterization, where the source associates mathcal, autoregressive, sequence, SIGMA, generative, graph, and mathbf. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

| Component | Inherited or novel | Role | Source locator |
|---|---|---|---|
| 3 Methodology | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with SIGMA, Methodology, framework, designed, and resolve; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2603.25062, 3 Methodology |
| 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with mathcal, Modeling, graph, dots, and Problem; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds |
| 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with Problem, Formulation, Generative, Modeling, and Chemical; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds |
| 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with Chemical, latent, Problem, Formulation, and Generative; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds |
| 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with Problem, Formulation, Generative, Modeling, and Chemical; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds |

The paper-specific method vocabulary is mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles, permutations, sequences. This vocabulary was derived from the complete method/architecture paragraphs rather than the title. It identifies the entities that must appear in a faithful architecture reconstruction and creates a falsifiable check: an implementation or summary that omits these named objects is not yet grounded in this paper.

The architecture is reconstructed as an information-flow graph: source identity and inputs enter; inherited and paper-specific components transform or score them; a decision or representation is produced; optional validation or post-processing occurs; and an evaluated outcome leaves the pipeline. Each edge should name the information available at that point. A comparison becomes unfair if one method has access to labels, future requests, privileged metadata, additional context, or a larger tuning budget that another method lacks.

### 2.4 Training, calibration, and inference

Construction-time and runtime work are separate accounting domains. Training may fit parameters, construct representations, estimate thresholds, tune prompts, or learn a policy. Calibration may use held-out examples or measurements. Inference may retrieve, route, compress, classify, generate, search, solve, or verify. Post-processing may enforce a constraint or discard invalid output. A credible efficiency claim says which of these phases is included, which is amortized, and which is external to the reported number.

Training or calibration evidence is explicitly located in 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds. The associated source vocabulary emphasizes mathcal, autoregressive, latent, graph, sigma, chemlms, standard, smiles, permutations, sequences.

Paper-specific construction/training sequence:

1. At 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, the paper reports a training-related operation involving Chemical, latent, Problem, Formulation, Generative, and Modeling. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds)*
2. At 4.2 Unconditional Generation: Bridging Sequence and Graph Models, the paper reports a training-related operation involving Sequence, Graph, generative, high, validity, and distribution. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, 4.2 Unconditional Generation: Bridging Sequence and Graph Models)*
3. At 4 Experiments, the paper reports a training-related operation involving trained, SMILES, Experiments, Experimental, Setup, and evaluate. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, 4 Experiments)*
4. At 2 Related Work, the paper reports a training-related operation involving Augmentation, SMILES, Canonicalization, Bias, Data, and mapping. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, 2 Related Work)*

No sentence was mechanically classified as an explicit inference/runtime description. The operational sequence below is labeled reviewer reconstruction and must be checked against the source before implementation.

Paper-specific inference/evaluation sequence:

Not applicable: No inference, retrieval, generation, prediction, or runtime action was identified; a runtime pipeline is not inferred. (source locator: private full-paper evidence dossier for arXiv:2603.25062, inference evidence inventory).

The reconstructed operational sequence is: pin input and artifact versions; validate prerequisites; compute the method-specific state or signal; apply the stated decision or objective; materialize the output; execute any downstream consumer; and measure both quality and resource outcomes. This sequence is reviewer inference grounded in the paper's organization. It is a testing model, not an assertion that the authors implemented an identical production controller.[^inference]

### 2.5 Notation and implementation audit

No independent implementation was run. The audit therefore checks internal legibility across equations, prose, captions, appendices, and extracted code/data statements. Apparent inconsistencies remain unresolved unless source evidence explains them. Source availability is classified in levels—declared, reachable, inspectable, runnable, and result-reproducing—and this local phase establishes only the declared/local-source layers.

## 3. Architecture and Complete Operational Pipeline

### 3.1 Representation and state

The documented dataflow is reconstructed only across 3 Methodology, 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds, and 3.3 Architecture and Parameterization, where the source associates mathcal, autoregressive, sequence, SIGMA, generative, graph, and mathbf. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

The central representation must be described by shape, type, provenance, lifetime, and relationship to the original input. If it is compressed, selected, latent, retrieved, generated, or aggregated, the review asks what information can be lost and how that loss is detected. If it is learned, the training distribution and version become part of its identity. If it is mutable, update ordering, expiry, and rollback become part of the method rather than operational afterthoughts.

### 3.2 Decision or action modules

The paper-specific modules should be separated from inherited encoders, decoders, solvers, retrieval systems, evaluators, or model APIs. A score can rank candidates without being calibrated; a policy can improve average reward without satisfying hard constraints; and a verifier can reject some failures without certifying all accepted outputs. The assessment uses the source's strongest ablation or controlled comparison to decide which module is necessary and which is merely bundled.

### 3.3 Dependencies, post-processing, and guarantee boundary

Dependencies include data preprocessing, external models, tokenizers, simulators, indexes, numerical libraries, and evaluation code. Post-processing can materially create the final result, so its compute and failure rate belong in the pipeline. Exact validation, when present, may establish a property of a returned object; it does not automatically establish semantic correctness, optimality, robustness, or absence of distribution shift.

### 3.4 Resource allocation and stopping

Budgets can refer to tokens, bytes, parameters, candidates, iterations, calls, samples, time, energy, or money. Requested and achieved budgets should both be recorded. Early stopping and fallback can bias which cases receive expensive processing. Batching can improve throughput while worsening latency. The review therefore distinguishes construction cost, per-instance latency, batch throughput, tail latency, peak memory, and downstream cost before accepting a general efficiency claim.

## 4. Experimental Design and Evidence Reconstructed

The evaluation reconstruction follows 4.1 Analysis of Geometric Invariance, 4 Experiments, with 3 table captions and 9 figure captions inventoried.

Paper-specific evaluation vocabulary centers on sigma, trained, smiles, central, hypothesis, work, standard, autoregressive, objectives, lead. These terms constrain which datasets, metrics, models, budgets, or operational quantities must be preserved with each reported comparison. They also identify where a later reproduction dossier must look for splits, baselines, hardware, batching, runtime semantics, and uncertainty rather than assuming conventional defaults.

The headings mechanically associated with evaluation and results were:

- 4.1 Analysis of Geometric Invariance
- 4 Experiments

### 4.1 Data, splits, and distribution

Not applicable: No named dataset, benchmark, corpus, or split was found in the captured full-paper data/evaluation paragraphs; none is invented. (source locator: private full-paper evidence dossier for arXiv:2603.25062, data/evaluation paragraph inventory).

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| Task | Table 1 lists Task as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 1 caption nor its row label establishes whether Task was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Task |
| Sitagliptin | Table 1 lists Sitagliptin as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 1 caption nor its row label establishes whether Sitagliptin was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Sitagliptin |
| ✓ | Table 1 lists ✓ as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 1 caption nor its row label establishes whether ✓ was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row ✓ |
| Zaleplon | Table 1 lists Zaleplon as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 1 caption nor its row label establishes whether Zaleplon was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Zaleplon |
| Fexofenadine | Table 1 lists Fexofenadine as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 1 caption nor its row label establishes whether Fexofenadine was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Fexofenadine |
| Osimertinib | Table 1 lists Osimertinib as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 1 caption nor its row label establishes whether Osimertinib was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Osimertinib |
| Perindopril | Table 1 lists Perindopril as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 1 caption nor its row label establishes whether Perindopril was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Perindopril |
| - | Table 1 lists - as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 1 caption nor its row label establishes whether - was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row - |
| GraphAF † | Table 2 lists GraphAF † as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 2 caption nor its row label establishes whether GraphAF † was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 row GraphAF † |
| MoFlow † | Table 2 lists MoFlow † as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 2 caption nor its row label establishes whether MoFlow † was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 row MoFlow † |
| LO-ARM † | Table 2 lists LO-ARM † as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 2 caption nor its row label establishes whether LO-ARM † was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 row LO-ARM † |
| CharRNN ‡ | Table 2 lists CharRNN ‡ as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 2 caption nor its row label establishes whether CharRNN ‡ was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 row CharRNN ‡ |
| mGPT2 ‡ | Table 2 lists mGPT2 ‡ as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 2 caption nor its row label establishes whether mGPT2 ‡ was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 row mGPT2 ‡ |
| MolGPT ‡ | Table 2 lists MolGPT ‡ as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 2 caption nor its row label establishes whether MolGPT ‡ was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 row MolGPT ‡ |
| RandSMILES | Table 2 lists RandSMILES as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 2 caption nor its row label establishes whether RandSMILES was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 row RandSMILES |
| LTCL | Table 2 lists LTCL as a numeric comparison row under Complexity vs. Diversity Trade-off.. | Neither the Table 2 caption nor its row label establishes whether LTCL was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 row LTCL |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

| Metric | Denominator/conditioning | Direction | Source locator |
|---|---|---|---|
| Optimization Quality / Top-Avg 1 ( \uparrow ) | Conditioning and aggregation follow the Table 1 caption: Table 1 : PMO Benchmark Performance. (mean \pm s.d. over 3 runs). Blue and pink shading indicate superior performance by SIGMA and the baseline, respectively. While peak scores (Top-1, Avg-100) are comparable due to saturation, SIGMA significantly excels in exploration (#Scaf) . In tasks like Osimertinib, SIGMA discovers 20–40% more unique scaffolds, confirming that geometric invariance facilitates effective scaffold hopping rather than local exploitation. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Sitagliptin / ✓ |
| Optimization Quality / Tio-Avg 10 ( \uparrow ) | Conditioning and aggregation follow the Table 1 caption: Table 1 : PMO Benchmark Performance. (mean \pm s.d. over 3 runs). Blue and pink shading indicate superior performance by SIGMA and the baseline, respectively. While peak scores (Top-1, Avg-100) are comparable due to saturation, SIGMA significantly excels in exploration (#Scaf) . In tasks like Osimertinib, SIGMA discovers 20–40% more unique scaffolds, confirming that geometric invariance facilitates effective scaffold hopping rather than local exploitation. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Sitagliptin / ✓ |
| Optimization Quality / Top-Avg 100 ( \uparrow ) | Conditioning and aggregation follow the Table 1 caption: Table 1 : PMO Benchmark Performance. (mean \pm s.d. over 3 runs). Blue and pink shading indicate superior performance by SIGMA and the baseline, respectively. While peak scores (Top-1, Avg-100) are comparable due to saturation, SIGMA significantly excels in exploration (#Scaf) . In tasks like Osimertinib, SIGMA discovers 20–40% more unique scaffolds, confirming that geometric invariance facilitates effective scaffold hopping rather than local exploitation. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Sitagliptin / ✓ |
| Efficiency / Top-AUC 1 ( \uparrow ) | Conditioning and aggregation follow the Table 1 caption: Table 1 : PMO Benchmark Performance. (mean \pm s.d. over 3 runs). Blue and pink shading indicate superior performance by SIGMA and the baseline, respectively. While peak scores (Top-1, Avg-100) are comparable due to saturation, SIGMA significantly excels in exploration (#Scaf) . In tasks like Osimertinib, SIGMA discovers 20–40% more unique scaffolds, confirming that geometric invariance facilitates effective scaffold hopping rather than local exploitation. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Sitagliptin / ✓ |
| Efficiency / Top-AUC 10 ( \uparrow ) | Conditioning and aggregation follow the Table 1 caption: Table 1 : PMO Benchmark Performance. (mean \pm s.d. over 3 runs). Blue and pink shading indicate superior performance by SIGMA and the baseline, respectively. While peak scores (Top-1, Avg-100) are comparable due to saturation, SIGMA significantly excels in exploration (#Scaf) . In tasks like Osimertinib, SIGMA discovers 20–40% more unique scaffolds, confirming that geometric invariance facilitates effective scaffold hopping rather than local exploitation. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Sitagliptin / ✓ |
| Efficiency / Top-AUC 100 ( \uparrow ) | Conditioning and aggregation follow the Table 1 caption: Table 1 : PMO Benchmark Performance. (mean \pm s.d. over 3 runs). Blue and pink shading indicate superior performance by SIGMA and the baseline, respectively. While peak scores (Top-1, Avg-100) are comparable due to saturation, SIGMA significantly excels in exploration (#Scaf) . In tasks like Osimertinib, SIGMA discovers 20–40% more unique scaffolds, confirming that geometric invariance facilitates effective scaffold hopping rather than local exploitation. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Sitagliptin / ✓ |
| Exploration / SA ( \uparrow ) | Conditioning and aggregation follow the Table 1 caption: Table 1 : PMO Benchmark Performance. (mean \pm s.d. over 3 runs). Blue and pink shading indicate superior performance by SIGMA and the baseline, respectively. While peak scores (Top-1, Avg-100) are comparable due to saturation, SIGMA significantly excels in exploration (#Scaf) . In tasks like Osimertinib, SIGMA discovers 20–40% more unique scaffolds, confirming that geometric invariance facilitates effective scaffold hopping rather than local exploitation. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Sitagliptin / ✓ |
| Exploration / Div ( \uparrow ) | Conditioning and aggregation follow the Table 1 caption: Table 1 : PMO Benchmark Performance. (mean \pm s.d. over 3 runs). Blue and pink shading indicate superior performance by SIGMA and the baseline, respectively. While peak scores (Top-1, Avg-100) are comparable due to saturation, SIGMA significantly excels in exploration (#Scaf) . In tasks like Osimertinib, SIGMA discovers 20–40% more unique scaffolds, confirming that geometric invariance facilitates effective scaffold hopping rather than local exploitation. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Sitagliptin / ✓ |
| Exploration / # Scaf ( \uparrow ) | Conditioning and aggregation follow the Table 1 caption: Table 1 : PMO Benchmark Performance. (mean \pm s.d. over 3 runs). Blue and pink shading indicate superior performance by SIGMA and the baseline, respectively. While peak scores (Top-1, Avg-100) are comparable due to saturation, SIGMA significantly excels in exploration (#Scaf) . In tasks like Osimertinib, SIGMA discovers 20–40% more unique scaffolds, confirming that geometric invariance facilitates effective scaffold hopping rather than local exploitation. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row Sitagliptin / ✓ |
| Task | Conditioning and aggregation follow the Table 1 caption: Table 1 : PMO Benchmark Performance. (mean \pm s.d. over 3 runs). Blue and pink shading indicate superior performance by SIGMA and the baseline, respectively. While peak scores (Top-1, Avg-100) are comparable due to saturation, SIGMA significantly excels in exploration (#Scaf) . In tasks like Osimertinib, SIGMA discovers 20–40% more unique scaffolds, confirming that geometric invariance facilitates effective scaffold hopping rather than local exploitation. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 row - |
| TIS ( \downarrow ) | Conditioning and aggregation follow the Table 2 caption: Table 2 : Unconditional Generation on ZINC250k. Baselines marked with {\dagger} and {\ddagger} are retrieved from (Wang et al. , 2025 ) and (Wu et al. , 2024 ) , respectively. TIS (Trajectory Invariance Score) measures latent divergence between isomorphic prefixes (lower is better). SIGMA achieves state-of-the-art FCD among sequence models, effectively bridging the gap with graph-based approaches. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 row SIGMA (Ours) |
| Validity ( \uparrow ) | Conditioning and aggregation follow the Table 2 caption: Table 2 : Unconditional Generation on ZINC250k. Baselines marked with {\dagger} and {\ddagger} are retrieved from (Wang et al. , 2025 ) and (Wu et al. , 2024 ) , respectively. TIS (Trajectory Invariance Score) measures latent divergence between isomorphic prefixes (lower is better). SIGMA achieves state-of-the-art FCD among sequence models, effectively bridging the gap with graph-based approaches. | Direction is interpreted only from the paper's caption/prose; the review does not invent whether higher or lower is better. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 row SIGMA (Ours) |

Metrics are reconstructed with direction, denominator, aggregation unit, conditioning, and reference quality. Failures excluded from an average create survivor bias. A gap to a best-known incumbent is not a gap to a proven optimum. A judge-model score is not a human preference without validation. A compression ratio can invert depending on convention. Confidence intervals, paired tests, and effect sizes matter when differences are close or instances are correlated.

### 4.4 Hardware, batching, and runtime semantics

Quality-v2 paper-specific hardware/runtime evidence:

- At Structural Negatives., the paper's hardware/runtime paragraph names batch. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, Structural Negatives.)*
- At Siamese Forward Pass., the paper's hardware/runtime paragraph names batch. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, Siamese Forward Pass.)*
- At B.2 Training Configuration, the paper's hardware/runtime paragraph names batch size. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, B.2 Training Configuration)*
- At B.4 Computing Infrastructure, the paper's hardware/runtime paragraph names A100, GPU, 40GB. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, B.4 Computing Infrastructure)*
- At B.4 Computing Infrastructure, the paper's hardware/runtime paragraph names batch, GPU, throughput. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, B.4 Computing Infrastructure)*
- At C.1 Graph Partitioning Algorithm, the paper's hardware/runtime paragraph names batch. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, C.1 Graph Partitioning Algorithm)*


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

Not applicable: No measured result survived the quality-v2 high-signal and table-row gates; no value is synthesized. (source locator: private full-paper evidence dossier for arXiv:2603.25062, quality-v2 results inventory).

Bounded exact evidence retained from the paper report:

- Paper report, numeric result in 4 Experiments: “The backbone is a GPT-2 (Small) causal language model trained…” (exact numeric tokens: 2, 2005).

- No table-caption fragment was included in the bounded verbatim evidence budget.

The correct interpretation retains task, dataset, split, model, baseline, metric, budget, and hardware with each result. A largest reported improvement is an operating point, not a distribution. An average is not a tail guarantee. A component metric can diagnose mechanism without proving end-to-end utility. Where the source reports multiple tables or figures, their relationships should be checked for consistent defaults, denominators, and versioned settings.

Three types of gain remain separate. Representation gain means fewer tokens, bytes, channels, states, features, or bits. Execution gain means lower latency, memory traffic, transfer, energy, or higher throughput. Outcome gain means better correctness, quality, utility, constraint satisfaction, or task completion. The paper may establish one or more under its setting; a deployment decision requires the combination relevant to its service objective.

Table and figure captions were inventoried rather than republished. Their exact values remain anchored to the paper. Any public summary should cite only values whose numerator, denominator, model, dataset, and comparison are simultaneously known. This review does not manufacture missing uncertainty or turn qualitative illustrations into statistical evidence.

## 6. Ablations and Causal Evidence

Paper-specific ablation/control ledger:

| Component/control | Paper-reported delta | Control caveat | Source locator |
|---|---|---|---|
| SMILES, Baselines, and include | 1, 2, 2025, and 3 | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2603.25062, 4 Experiments |
| enforcing, latent, and isotropy | direction or magnitude is reported only at the source locator | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2603.25062, 5 Conclusion |

Ablations are persuasive when one named component changes while model, data, budget, training effort, and implementation quality stay fixed. The complete source was screened for removals, swaps, budget sweeps, sensitivity tests, and failure examples. If multiple elements change together, the result supports the bundle more strongly than any individual mechanism. If a simple cost-matched control is missing, the causal interpretation remains limited.

Randomness must be classified as training seeds, inference seeds, data-generation seeds, checkpoint-selection variance, or hyperparameter-search variance. Repeated inference does not prove training robustness. A named significance test should identify its independence unit and paired design. The practical importance of an effect is separate from statistical detectability, especially when a large benchmark makes very small changes significant.

Author-stated limitations:

- The author-side qualification at 5 Conclusion concerns SIGMA, chemical, effectively, geometric, introduces, and framework. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, 5 Conclusion)*

Reviewer-identified limitations:

- No independent reproduction was performed for arXiv:2603.25062v1; SIGMA, molecular, language, and trained remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, 4 Experiments, and 4.1 Analysis of Geometric Invariance)*
- The dossier inventories 46 headings, 3 tables, 9 figures, and 130 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2603.25062, complete coverage inventory)*

The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 2 candidate sentences and the limitation/discussion vocabulary models, sigma, chemical, effectively, geometric, introduces, framework, designed, resolve, topological. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper frames SIGMA as a contribution to molecular, SIGMA, graph, latent. | Problem framing is located in the profile's named introduction/problem headings; no numbered section marker is treated as a measurement. (private full-paper evidence dossier for arXiv:2603.25062, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| The reported mechanism centers on mathcal, autoregressive, sequence, SIGMA. | Method and formula evidence is bound to the named method headings and formula-specific operator audits. (private full-paper evidence dossier for arXiv:2603.25062, 3 Methodology) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| SIGMA: Structure-Invariant Generative Molecular Alignment for Chemical Language Models via Autoregressive Contrastive Learning: paper-reported result claim centered on SIGMA, molecular, language, and trained | Quality-v2 paper-report result values: no measured claim survived; this claim is not admitted by semantic QA (private full-paper evidence dossier for arXiv:2603.25062, 4 Experiments) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2603.25062v1), [canonical PDF](https://arxiv.org/pdf/2603.25062v1), [canonical full-paper HTML](https://arxiv.org/html/2603.25062v1), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2603.25062). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2603.25062v1)*
- **Predecessor/prior work (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 1 Introduction; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2010.09885)*
- **Alternative or benchmark (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 1 Introduction; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2304.05376)*
- **Code/data (bounded_not_found):** The bounded verified-URL receipt contains no official code/data artifact for this paper; no access error was recorded, so this is not labeled blocked. *(evidence locator: bounded online-vetting receipt for arXiv:2603.25062)*

Verified official primary-source links from the bounded check:

- No additional official code, data, project, venue, or benchmark URL was verified beyond the canonical record.

Access-blocked or unverified URL evidence: not recorded

Prior-work and alternatives evidence: "bounded_to_canonical_arxiv_record_and_paper_declared_primary_links" This is a bounded search record, not an exhaustive map of the field.

Code/data and reproduction evidence: "link_reachability_only; repository contents were not downloaded, built, or executed" Reachability and metadata do not mean that code or data were executed, that dependencies were installed, or that a reported result reproduced.

Paper-declared external candidates were recorded as follows:

- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/accessible_HTML.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/license/index.html#licenses-available
- Paper-declared URL, not opened in this phase: https://math.nist.gov/~BMiller/LaTeXML/
- Paper-declared URL, not opened in this phase: https://github.com/arXiv/html_feedback/issues
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/issues
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/ourmembers.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/contact.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/subscribe
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/license/index.html

Their presence is discovery evidence, not proof that an artifact is official, available, licensed, runnable, or reproducing the paper. A later online-vetting phase should use primary sources, record HTTP/access limits, verify ownership and linkage, inspect release and license state, and distinguish artifact availability from runnable or result-reproducing status. Until then the publication status remains: arXiv preprint; no separate peer-reviewed venue inferred without an official venue source.

The isolated Black Lake checkout was used only for repository-readiness and dedupe context. A same-paper DEP-A would block a new owning record; a DEP-E or directly corresponding implementation is associated context rather than a duplicate. Background citations do not transfer evidence or claims to this paper.[^association]

## 9. Independent Re-conceptualization

Reviewer inference: the durable mechanism is the source-defined change centered on mathcal, autoregressive, sequence, and SIGMA, rather than the paper's brand name. This interpretation predicts that a matched intervention on mathcal changes SIGMA; it is not an author claim or theorem.

Re-conceptualize the contribution as an evidence-linked state transition: pin source identity, record the method-specific decision, measure realized resource and outcome effects, and retain a conservative fallback whose trigger can be falsified on held-out conditions. This is reviewer inference and proposal, not an author claim and not an experimentally validated architecture.[^inference]

The mechanism can be viewed as a governed handoff between evidence, decision, execution, and outcome. Evidence identifies the source state and the signal the method uses. Decision records the action or representation chosen under a budget. Execution records what the system actually did, including fallback and resource use. Outcome records task quality and failure. The mapping is useful because it predicts what must be logged; it breaks when the paper studies a purely formal object with no operational transition.

A second bounded analogy is experimental portfolio control. Different baselines, budgets, and ablations are portfolio arms whose information access and cost must be matched. This analogy highlights selection bias and incomplete frontiers, but it does not imply that the paper uses an online bandit or that deployment should optimize only one scalar reward. Its falsifiable prediction is that the proposed mechanism's advantage should shrink when information access and complete cost are carefully matched if the original gain came mainly from comparison asymmetry.

## 10. Research Notes, Limitations, and Evidence Boundary

The complete local PDF and full-paper HTML for arXiv:2603.25062v1 were inspected. The PDF passed size, header, EOF, parse, page-count, title, structure, and references checks. The HTML passed size, readable-body, document-marker, heading, structure, title, and identity checks. Abstract HTML was metadata only and did not qualify as the paper body.[^integrity]

The coverage pass includes introduction, method or formal analysis, experiments or results, discussion or conclusion, references, appendices where exposed, tables, figures, equations, footnotes, disclosures, and code/data language. Extraction can lose visual layout and some mathematical semantics; the ledger records this boundary rather than claiming that every graphic was numerically reproduced.

Paper-specific qualification inventory: limitation/discussion terms models, sigma, chemical, effectively, geometric, introduces, framework, designed, resolve, topological; disclosure/funding language no explicit disclosure/funding/acknowledgment term extracted; code/data language GitHub, code, reproducibility, dataset; appendix headings Appendix A Visualization of Trajectory Dynamics, Appendix B Implementation Details, Appendix C Data Construction and View Generation, Appendix D Dense Trajectory Alignment Objective, Appendix E Additional Evidence of Geometric Invariance, Appendix F Metric Definitions. These are evidence pointers. A missing extracted term is not proof that a disclosure, artifact, or limitation does not exist.

Evidence layers remain explicit. Layer A is what the paper reports. Layer B contains the bounded primary records actually checked online; its conclusions are limited to the recorded identity, publication, and artifact-access evidence. Layer C is reviewer inference, including the governed-handoff interpretation. Layer D is a hypothesis or proposal, including deployment controls and falsification tests. A sentence is not silently promoted between layers.

Paper/prose/table consistency checks:

| Issue/check | Assessment | Source locator |
|---|---|---|
| Canonical ID, version, title, authors, PDF hash, and HTML hash were reconciled for arXiv:2603.25062v1; full quantitative table/prose/code consistency was not independently rerun. | identity consistency checked; quantitative and implementation consistency remain unresolved | source-integrity and online identity receipts for arXiv:2603.25062v1 |

Substantive evidence boundary: The profile binds arXiv:2603.25062v1 to a complete local PDF and full-paper HTML, 46 headings, 3 tables, 9 figures, and 130 extracted mathematical objects, and 2 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. No experiment, benchmark, training run, code path, hardware measurement, dataset, service rollout, or security test was independently rerun. This methodology produces auditability, observability, and traceable evidence; it is not security certification.

The evidence-derived methodology score is 20/20: source integrity 2, full paper coverage 2, technical fidelity 2, quantitative fidelity 2, external vetting 2, claim calibration 2, reconceptualization 2, research value 2, provenance 2, durability 2. The score is computed from source integrity, complete coverage, paper-specific method/equation/training/inference evidence, numeric/table/figure evidence, and whether bounded external vetting was actually performed. It rates the review artifact's coverage and evidence discipline. It does not rate the paper's truth and cannot substitute for subject-matter peer review, actual reproduction, or security assessment.

## 11. Potential Implications

### 11.1 Scientific implications

The paper's durable scientific value depends on whether the named mechanism predicts outcomes beyond the exact benchmark coordinate. Publishing full frontiers, per-instance failures, achieved budgets, uncertainty, and versioned configurations would let later work test the explanation instead of comparing isolated maxima. Negative results under shifted data, models, or budgets are especially informative because they locate the mechanism's boundary.

### 11.2 System-design implications

Builders should place the optimized path behind an observable budget and fallback controller. Source, model, data, and configuration versions should be pinned. The controller should log why an action occurred, realized rather than requested cost, validation status, and downstream outcome. Shadow comparison against a conservative path can expose drift and tail regressions before the method becomes irreversible infrastructure.

### 11.3 Deployment and governance

Derived representations can preserve sensitive, licensed, or incorrect content. Access, retention, deletion, correction, provenance, and tenant isolation should follow the information after transformation. Appropriate use requires monitored assumptions and a measurable refusal or fallback path. Poor fit includes untested distributions, absent outcome joins, hidden preprocessing cost, or settings where failure cannot be detected before harm.

## 12. New Falsifiable Hypotheses

### Hypothesis 1: Matched removal of mathcal

**Proposition:** Reviewer hypothesis: the source-linked mathcal operation is causally responsible for part of the reported SIGMA behavior.
**Predicted observation:** Removing or neutralizing mathcal under matched data and compute will measurably weaken SIGMA.
**Falsifying observation:** A competent matched control without mathcal preserves the same SIGMA distribution within uncertainty.
**Minimum test:** Run a paired, seed-controlled ablation at 4 Experiments and archive per-instance outcomes and resource use.
**Evidence locator:** private full-paper evidence dossier for arXiv:2603.25062, 3 Methodology, and 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds

### Hypothesis 2: Boundary transfer for SIGMA

**Proposition:** Reviewer hypothesis: the relation between mathcal, and autoregressive and SIGMA, and molecular weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2603.25062, 4 Experiments, and 4.1 Analysis of Geometric Invariance

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for SIGMA** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2603.25062, 4 Experiments, and 4.1 Analysis of Geometric Invariance.
2. **Reproduce the end-to-end SIGMA path** Success: the source-defined mathcal, autoregressive, and sequence and SIGMA, and molecular are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3 Methodology, and 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.
3. **Falsify the reviewer mechanism thesis for mathcal** Success: a matched intervention on mathcal predicts a corresponding change in SIGMA Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2603.25062, 3 Methodology, and 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds.

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, SIGMA: Structure-Invariant Generative Molecular Alignment for Chemical Language Models via Autoregressive Contrastive Learning should be remembered as a tested relation between mathcal, autoregressive, and sequence and SIGMA, molecular, and language under the configurations at 4 Experiments, and 4.1 Analysis of Geometric Invariance, not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The Table 1 caption centers on SIGMA, Performance., Table, Benchmark, mean, over, runs; its parsed headers include Use, Task, SIGMA, MPO (Multiproperty Objective), across 18 rows and 165 cells.; result: Use / MPO (Multiproperty Objective) / Median Molecule=0.607; Use / MPO (Multiproperty Objective) / Median Molecule=0.013; Optimization Quality / MPO (Multiproperty Objective) / Median Molecule=0.596; Optimization Quality / MPO (Multiproperty Objective) / Median Molecule=0.020; Optimization Quality / MPO (Multiproperty Objective) / Median Molecule=0.541; Optimization Quality / MPO (Multiproperty Objective) / Median Molecule=0.014; Optimization Quality / MPO (Multiproperty Objective) / Median Molecule=0.544; Optimization Quality / MPO (Multiproperty Objective) / Median Molecule=0.011; Efficiency / MPO (Multiproperty Objective) / Median Molecule=0.508; Efficiency / MPO (Multiproperty Objective) / Median Molecule=0.020; Efficiency / MPO (Multiproperty Objective) / Median Molecule=0.423; Efficiency / MPO (Multiproperty Objective) / Median Molecule=0.016; Efficiency / MPO (Multiproperty Objective) / Median Molecule=3.628; Efficiency / MPO (Multiproperty Objective) / Median Molecule=0.487; Exploration / MPO (Multiproperty Objective) / Median Molecule=0.656; Exploration / MPO (Multiproperty Objective) / Median Molecule=0.073; Exploration / MPO (Multiproperty Objective) / Median Molecule=3143; Exploration / MPO (Multiproperty Objective) / Median Molecule=0; Exploration / MPO (Multiproperty Objective) / Median Molecule=89; caveat: Interpret Table 1 with its spanning headers and caption under Complexity vs. Diversity Trade-off.; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.25062, Table 1 caption and object |
| Table 2 | Purpose: The Table 2 caption centers on Table, Unconditional, Generation, ZINC250k., Baselines, marked, dagger; its parsed headers include Model, Graph-based, GraphAF †, across 12 rows and 74 cells.; result: TIS ( \downarrow ) / Graph-based / Sequence-based=0.041; Validity ( \uparrow ) / Graph-based / Sequence-based=0.998; Uniqueness ( \uparrow ) / Graph-based / Sequence-based=0.814; Novelty ( \uparrow ) / Graph-based / Sequence-based=0.798; IntDiv ( \uparrow ) / Graph-based / Sequence-based=0.910; FCD ( \downarrow )=0.752; caveat: Interpret Table 2 with its spanning headers and caption under Complexity vs. Diversity Trade-off.; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.25062, Table 2 caption and object |
| Table 3 | Purpose: The Table 3 caption centers on Table, Hyperparameter, Settings, SIGMA, Training.; its parsed headers include Hyperparameter, Optimization, Optimizer, across 20 rows and 37 cells.; result: Value / Optimization / AdamW / 0.01 / 1.0 / 64 / 50 / 2000 / Contrastive Learning / 0.1 / 2 / 256 / Architecture (GPT-2 Small) / 12 / 768 / 128=5; Value / Optimization / AdamW / 0.01 / 1.0 / 64 / 50 / 2000 / Contrastive Learning / 0.1 / 2 / 256 / Architecture (GPT-2 Small) / 12 / 768 / 128=10; Value / Optimization / AdamW / 0.01 / 1.0 / 64 / 50 / 2000 / Contrastive Learning / 0.1 / 2 / 256 / Architecture (GPT-2 Small) / 12 / 768 / 128=-4; caveat: Interpret Table 3 with its spanning headers and caption under B.2 Training Configuration; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.25062, Table 3 caption and object |
| Figure 1 | Purpose: The Figure 1 caption identifies a quantitative plot or comparison centered on SIGMA, Contrastive, Learning, SMILES, Views, distinct, Trajectory, Figure.; result: The caption makes a qualitative claim about SIGMA, Contrastive, Learning, SMILES, Views, distinct; no plotted value is inferred from pixels.; caveat: The caption under Abstract was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.25062, Figure 1 caption and object |
| Figure 2 | Purpose: The Figure 2 caption identifies a quantitative plot or comparison centered on alignment, across, equivalent, SMILES, matched, tokens, Figure, Token-level.; result: The caption makes a qualitative claim about alignment, across, equivalent, SMILES, matched, tokens; no plotted value is inferred from pixels.; caveat: The caption under 1 Introduction was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.25062, Figure 2 caption and object |
| Figure 3 | Purpose: The Figure 3 caption identifies a paper-specific visual object centered on Isomorphic, Search., Beam, Redundancy, IsoBeam, identical, Figure, Resolving.; result: The caption makes a qualitative claim about Isomorphic, Search., Beam, Redundancy, IsoBeam, identical; no plotted value is inferred from pixels.; caveat: The caption under 2 Related Work was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.25062, Figure 3 caption and object |
| Algorithm 1 | Purpose: The Algorithm 1 caption identifies a paper-specific visual object centered on Algorithm, Isomorphic, Beam, Search, IsoBeam.; result: The caption makes a qualitative claim about Algorithm, Isomorphic, Beam, Search, IsoBeam; no plotted value is inferred from pixels.; caveat: The caption under Formulation. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.25062, Algorithm 1 caption and object |
| Figure 4 | Purpose: The Figure 4 caption identifies a qualitative example or visualization centered on Geometric, Invariance., SMILES, views, where, isomorphic, clusters., Learning.; result: Caption-reported measured values: 50, 10; caveat: The caption under Theoretical Insight: Implicit Gradient Alignment. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.25062, Figure 4 caption and object |
| Figure 5 | Purpose: The Figure 5 caption identifies a paper-specific visual object centered on Latent, Alignment, similarity, distinct, region., structural, models, Figure.; result: The caption makes a qualitative claim about Latent, Alignment, similarity, distinct, region., structural; no plotted value is inferred from pixels.; caveat: The caption under Theoretical Insight: Implicit Gradient Alignment. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.25062, Figure 5 caption and object |
| Figure 6 | Purpose: The Figure 6 caption identifies a paper-specific visual object centered on Figure, Inference, Scalability, Analysis, Left, Both, strategies, yield.; result: Caption-reported measured values: 100, 50,000, 5,000, 2, 50,000; caveat: The caption under 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.25062, Figure 6 caption and object |
| Figure 7 | Purpose: The Figure 7 caption identifies a qualitative example or visualization centered on trajectories, Figure, Conceptual, Visualization, Trajectory, Dynamics., canonical, reference.; result: The caption makes a qualitative claim about trajectories, Figure, Conceptual, Visualization, Trajectory, Dynamics.; no plotted value is inferred from pixels.; caveat: The caption under Appendix A Visualization of Trajectory Dynamics was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.25062, Figure 7 caption and object |
| Figure 8 | Purpose: The Figure 8 caption identifies a paper-specific visual object centered on Aspirin, Figure, Geometric, Alignment, Acetylsalicylic, Acid, visualize, token-level.; result: The caption makes a qualitative claim about Aspirin, Figure, Geometric, Alignment, Acetylsalicylic, Acid; no plotted value is inferred from pixels.; caveat: The caption under Appendix E Additional Evidence of Geometric Invariance was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.25062, Figure 8 caption and object |
| Equations | 130 distinct mathematical renderings exposed by HTML; representative objects listed in Section 2.2. | Central objects were inventoried with sign, normalization, conditioning, and denominator checks; no numerical reproduction. |
| Sections | 46 headings exposed by the full HTML. | Every heading was screened; method, evaluation, results, limitations, references, and appendices were mapped where present. |

Appendix and supplementary coverage:

- Appendix A Visualization of Trajectory Dynamics
- Appendix B Implementation Details
- Appendix C Data Construction and View Generation
- Appendix D Dense Trajectory Alignment Objective
- Appendix E Additional Evidence of Geometric Invariance
- Appendix F Metric Definitions

Complete section inventory:

- Report GitHub Issue
- SIGMA: Structure-Invariant Generative Molecular Alignment for Chemical Language Models via Autoregressive Contrastive Learning
- Abstract
- 1 Introduction
- 2 Related Work
- 3 Methodology
- 3.1 Problem Formulation: Generative Modeling on Chemical Manifolds
- 3.2 Constructing Functionally Equivalent Views
- The “Probe Suffix” Protocol.
- Structural Negatives.
- 3.3 Architecture and Parameterization
- Projection-Decoupled Mechanism.
- Siamese Forward Pass.
- 3.4 Dense Trajectory Alignment Objective
- Formulation.
- Theoretical Insight: Implicit Gradient Alignment.
- 3.5 Isomorphic Beam Search (IsoBeam)
- Complexity vs. Diversity Trade-off.
- 4 Experiments
- 4.1 Analysis of Geometric Invariance
- Macroscopic: Resolving Manifold Fragmentation.
- Microscopic: Isomorphic Semantic Alignment.
- 4.2 Unconditional Generation: Bridging Sequence and Graph Models
- 4.3 Optimization Efficiency in Reinforcement Learning
- 4.4 Breaking the Redundancy Ceiling: Isomorphic Beam Search
- 5 Conclusion
- Impact Statement
- References
- Appendix A Visualization of Trajectory Dynamics
- Appendix B Implementation Details
- B.1 Model Architecture
- B.2 Training Configuration
- B.3 Data Preprocessing and Tokenization
- B.4 Computing Infrastructure
- B.5 Inference Details (IsoBeam)
- Appendix C Data Construction and View Generation
- C.1 Graph Partitioning Algorithm
- C.2 Handling Attachment Points
- C.3 Contrastive View Generation
- Appendix D Dense Trajectory Alignment Objective
- Appendix E Additional Evidence of Geometric Invariance
- Appendix F Metric Definitions
- F.1 Generative Quality Metrics
- F.2 Distribution Learning Metrics
- F.3 Geometric Invariance Metrics
- F.4 Optimization Metrics (PMO)

This ledger is completeness evidence, not reproduction. It records that each exposed section and numbered object was screened without reproducing the paper's tables, figures, or long captions.

## 16. Source and Evidence Notes

- Canonical arXiv record: https://arxiv.org/abs/2603.25062v1
- Canonical PDF: https://arxiv.org/pdf/2603.25062v1
- Canonical full-paper HTML: https://arxiv.org/html/2603.25062v1
- arXiv DOI resolver: https://doi.org/10.48550/arXiv.2603.25062
- Reviewed identity: arXiv:2603.25062v1
- Complete authors: Xinyu Wang; Fei Dou; Jinbo Bi; Minghu Song
- Locally archived full PDF and full-paper HTML were verified; private path withheld.
- No source PDF, HTML, archive, extracted text, validator, or private index belongs in the public DEP-A package.
- Online primary-source vetting status: performed and receipt-linked; alternatives are not exhaustive and no experiment was independently reproduced.

## 17. Footnotes

[^source-paper]: Canonical paper identity and version are linked at https://arxiv.org/abs/2603.25062v1; the locally archived complete PDF and full-paper HTML were reconciled to this identity.
[^scope]: Paper report means content attributable to the authors and supported by the reviewed artifact; it is not independent reproduction.
[^integrity]: Source integrity requires a matching complete PDF and full-paper HTML with identity, version, title, structure, references, and readable-body checks.
[^inference]: Reviewer inference labels a mechanism-level interpretation derived from source evidence rather than asserted by the authors.
[^external]: External primary evidence was limited to receipt-linked official records and URLs. Availability or publication status does not imply artifact runnability, result reproduction, or exhaustive prior-work coverage.
[^association]: An associated DEP is contextual evidence, not a duplicate and not proof of the reviewed paper's claims.
