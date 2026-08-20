# Whitepaper Review: Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty

## A detailed review, technical reconstruction, and independent re-conceptualization of “Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty”

**Source paper:** Tianjue Lin; Jianan Zhou; Jieyi Bi; Yaoxin Wu; Wen Song; Zhiguang Cao; Jie Zhang, “Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty,” arXiv:2605.14494v1.[^source-paper]

**Artifact prepared:** 2026-08-20
**Local source reviewed:** complete locally archived PDF (25 pages) and matching full-paper HTML (90565 readable body characters); private path withheld
**Review scope:** full-paper reconstruction, claim vetting, local evidence mapping, implications, and replication agenda
**Review status:** source artifacts inspected; bounded online primary-source vetting performed; experiments not independently rerun

## Executive Assessment

### The paper in one sentence

The paper presents and evaluates a technical contribution framed around learning, scenario, reduction, two-stage, robust, optimization, with its method, formal objects, experimental record, limitations, and source structure inspected from a complete local paper pair rather than an abstract page.

### The deeper idea

Reviewer inference: the durable mechanism is the source-defined change centered on scenario, instance, embeddings, and mathbf, rather than the paper's brand name. This interpretation predicts that a matched intervention on scenario changes scenario; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to 4 Methodology, 4.2.1 Model Architecture. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

### Bottom-line judgment

The source is complete enough for a full-paper assessment, and the paper reports a technically organized contribution with an explicit evaluation record. Results remain paper-reported. The local evidence pass confirms the complete results structure and numbered-object inventory, but it does not independently reproduce a numerical value or infer a stronger denominator than the source states. The defensible verdict is therefore conditional: the paper establishes what it directly measures under its own setup, while broader superiority, generality, robustness, efficiency, or deployment readiness remains bounded by the tested models, data, metrics, budgets, hardware, and comparisons.[^scope]

### Principal strengths

- Complete PDF and matching full-paper HTML passed identity, structure, title, references, and readability gates.
- The source exposes 61 section headings, 23 table captions, 8 figure captions, and 371 mathematical renderings for coverage auditing.
- The review can distinguish paper report, external-primary evidence, reviewer inference, and hypothesis without relying on an abstract-only summary.

### Principal qualifications

1. The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions.
2. No result, code path, benchmark, training run, or hardware measurement was independently reproduced.
3. Bounded online checks verified canonical identity and the explicitly recorded official URLs; the search is not exhaustive and does not establish artifact runnability or reproduction.[^external]

## 1. The Problem and Research Questions

### 1.1 Problem and stakes

**Paper-reported problem:** For Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty, the formal target is bounded to the source-defined relation among Scenario, uncertainty, PRISE, NeurPRISE, scenarios, objective, and reduction. The task assumptions and stakes are anchored to Abstract, and 1 Introduction; no objective outside those sections is inferred.

**Research gap reconstructed from the source:** The paper positions Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty around Scenario, uncertainty, PRISE, instance, and embeddings. This records the authors' gap framing only; novelty, priority, generality, and superiority require the separate prior-work and evaluation audits.

The title and full-paper organization identify learning, scenario, reduction, two-stage, robust, optimization as the central problem space. A rigorous reading asks what input object is transformed, predicted, selected, optimized, or measured; which practical or scientific constraint motivates that operation; and which outcome makes the change valuable. Those questions must be answered by the method and evaluation sections, not by the title alone. The paper reports its own problem definition; this review preserves the boundary between that report and reviewer interpretation.

Paper-specific reconstruction: the abstract/introduction evidence concentrates on scenario, uncertainty, set, prise, scenarios, optimization, discrete, often, reduction, robust, under the headings Abstract, 1 Introduction. Those source terms locate the actual objects and constraints; they do not by themselves prove novelty or improvement. In this review they constrain the problem statement so a generic systems narrative cannot replace the paper's own domain and terminology.

The practical stakes depend on the actual denominator. An improvement in a representation, proxy, component score, or controlled benchmark can be important without automatically improving end-user quality, wall-clock cost, reliability, or safety. A durable account therefore separates the immediate technical objective from the downstream objective and asks which bridge between them is tested. If that bridge is only assumed, it remains an explicit gap rather than a hidden premise.

### 1.2 Prior method families and inherited components

The paper's related-work and background sections define the relevant method families. The review treats established backbones, pretrained models, datasets, optimization routines, kernels, evaluation harnesses, and standard metrics as inherited unless the source identifies a change. Novelty belongs to the specific interface, objective, representation, decision rule, data construction, proof, or evaluation design that differs. This prevents a system-level bundle from receiving credit for every capability of its dependencies.

### 1.3 Questions that govern the assessment

Five questions organize the reconstruction. What exact object enters and leaves the method? Which components are learned, fixed, searched, sampled, or verified? What objective and assumptions determine the operation? How do training or calibration differ from inference or deployment? Finally, which result would falsify the authors' causal or generality story rather than merely lower an aggregate score? These questions create an audit trail from paper report to independent assessment.

## 2. Formal and Technical Reconstruction

### 2.1 Definitions and assumptions

The authoritative definition chain lives in the complete source sections listed below. The automated evidence profile does not pretend that section names themselves describe the mechanism. Instead, the full review binds each claim to the source's definitions, stated assumptions, and adjacent formal or experimental context. The core technical headings identified for close reading were:

- 4 Methodology
- 4.2.1 Model Architecture

Variables should be assigned plain-language meanings before algebra is interpreted. Inputs, labels, state, parameters, budgets, constraints, random variables, and outputs must remain distinct. A probability requires a sample space and conditioning event; a loss requires an optimization direction; a ratio requires a numerator and denominator; and a guarantee retains every assumption under which it was proved. If the source uses the same symbol in different roles or shifts between population and sample quantities, that ambiguity should be preserved rather than silently repaired.

### 2.2 Objective and central equations

The full HTML exposes 371 distinct mathematical renderings. Each is treated as a paper-reported formal object whose sign, normalization, conditioning, and denominator must be read with adjacent prose.

Paper-specific formal reconstruction:

**Formal object 1 at Abstract — Formula 1 under Abstract is classified as a optimization objective or loss; adjacent prose centers on Scenario, PRISE, NeurPRISE, scenarios, times, uncertainty, and the expression links symbols defined beside the formula..** `7`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 1 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Abstract.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Abstract, formal object 1.

**Formal object 2 at Abstract — Formula 2 under Abstract is classified as a optimization objective or loss; adjacent prose centers on Scenario, PRISE, NeurPRISE, scenarios, times, uncertainty, and the expression links times..** `200\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 2 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Abstract.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Abstract, formal object 2.

**Formal object 3 at Abstract — Formula 3 under Abstract is classified as a optimization objective or loss; adjacent prose centers on Scenario, PRISE, NeurPRISE, scenarios, times, uncertainty, and the expression links times..** `5\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 3 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Abstract.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Abstract, formal object 3.

**Formal object 4 at Abstract — Formula 4 under Abstract is classified as a optimization objective or loss; adjacent prose centers on Scenario, PRISE, NeurPRISE, scenarios, times, uncertainty, and the expression links times..** `4\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 4 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Abstract.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Abstract, formal object 4.

**Formal object 5 at 1 Introduction — Formula 5 under 1 Introduction is classified as a optimization objective or loss; adjacent prose centers on uncertainty, reduction, scenario, problem, while, Traditional, and the expression links k..** `k`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 5 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 1 Introduction.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 1 Introduction, formal object 5.

**Formal object 6 at 1 Introduction — Formula 6 under 1 Introduction is classified as a optimization objective or loss; adjacent prose centers on scenario, PRISE, objective., scenarios, SEquential, yields, and the expression links symbols defined beside the formula..** `2`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 6 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 1 Introduction.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 1 Introduction, formal object 6.

**Formal object 7 at 1 Introduction — Formula 7 under 1 Introduction is classified as a optimization objective or loss; adjacent prose centers on scenario, PRISE, objective., scenarios, SEquential, yields, and the expression links times..** `7{\times}`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 7 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to 1 Introduction.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 1 Introduction, formal object 7.

**Formal object 8 at 3 Preliminaries — Formula 8 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on focus, linear, two-stage, robust, optimization, over, and the expression links Xi, xi, dots, S..** `\Xi=\{\xi_{1},\dots,\xi_{S}\}`
Variables: "Xi, xi, dots, S".
Sign/normalization/conditioning/surrogate audit: "Formula 8 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Xi, xi, dots, S; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 8.

**Formal object 9 at 3 Preliminaries — Formula 9 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on focus, linear, two-stage, robust, optimization, over, and the expression links S..** `S`
Variables: "S".
Sign/normalization/conditioning/surrogate audit: "Formula 9 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 9.

**Formal object 10 at 3 Preliminaries — Formula 10 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links displaystyle, x, in, X..** `\displaystyle\min_{x\in X}`
Variables: "displaystyle, x, in, X".
Sign/normalization/conditioning/surrogate audit: "Formula 10 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, x, in, X; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 10.

**Formal object 11 at 3 Preliminaries — Formula 11 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links displaystyle, c, top, x, xi, in, Xi, y..** `\displaystyle c^{\top}x+\max_{\xi\in\Xi}\min_{y\in F(x,\xi)}b_{\xi}^{\top}y,`
Variables: "displaystyle, c, top, x, xi, in, Xi, y, F, b_{\\xi}^{\\top}y".
Sign/normalization/conditioning/surrogate audit: "Formula 11 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, c, top, x, xi, in, Xi, y, F, b_{\\xi}^{\\top}y; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 11.

**Formal object 12 at 3 Preliminaries — Formula 12 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links displaystyle, geq, d..** `\displaystyle Ax\geq d,`
Variables: "displaystyle, geq, d".
Sign/normalization/conditioning/surrogate audit: "Formula 12 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, geq, d; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 12.

**Formal object 13 at 3 Preliminaries — Formula 13 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links x, in, mathbb, R, n..** `x\in\mathbb{R}^{n}`
Variables: "x, in, mathbb, R, n".
Sign/normalization/conditioning/surrogate audit: "Formula 13 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x, in, mathbb, R, n; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 13.

**Formal object 14 at 3 Preliminaries — Formula 14 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links y, in, mathbb, R, m..** `y\in\mathbb{R}^{m}`
Variables: "y, in, mathbb, R, m".
Sign/normalization/conditioning/surrogate audit: "Formula 14 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y, in, mathbb, R, m; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 14.

**Formal object 15 at 3 Preliminaries — Formula 15 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links c, in, mathbb, R, n..** `c\in\mathbb{R}^{n}`
Variables: "c, in, mathbb, R, n".
Sign/normalization/conditioning/surrogate audit: "Formula 15 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c, in, mathbb, R, n; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 15.

**Formal object 16 at 3 Preliminaries — Formula 16 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links b_{\xi}\in\mathbb{R}^{m}..** `b_{\xi}\in\mathbb{R}^{m}`
Variables: "b_{\\xi}\\in\\mathbb{R}^{m}".
Sign/normalization/conditioning/surrogate audit: "Formula 16 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: b_{\\xi}\\in\\mathbb{R}^{m}; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 16.

**Formal object 17 at 3 Preliminaries — Formula 17 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links F, x, xi, y, in, Y, geq, h..** `F(x,\xi)=\{y\in Y:Gy\geq h-Ex-M\xi\}`
Variables: "F, x, xi, y, in, Y, geq, h, M".
Sign/normalization/conditioning/surrogate audit: "Formula 17 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: F, x, xi, y, in, Y, geq, h, M; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 17.

**Formal object 18 at 3 Preliminaries — Formula 18 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links X, subseteq, mathbb, Z, n..** `X\subseteq\mathbb{Z}^{n}_{+}`
Variables: "X, subseteq, mathbb, Z, n".
Sign/normalization/conditioning/surrogate audit: "Formula 18 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: X, subseteq, mathbb, Z, n; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 18.

**Formal object 19 at 3 Preliminaries — Formula 19 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links Y, subseteq, mathbb, Z, m..** `Y\subseteq\mathbb{Z}^{m}_{+}`
Variables: "Y, subseteq, mathbb, Z, m".
Sign/normalization/conditioning/surrogate audit: "Formula 19 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, subseteq, mathbb, Z, m; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 19.

**Formal object 20 at 3 Preliminaries — Formula 20 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links mathbb, R, m..** `\mathbb{R}^{m}_{+}`
Variables: "mathbb, R, m".
Sign/normalization/conditioning/surrogate audit: "Formula 20 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbb, R, m; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 20.

**Formal object 21 at 3 Preliminaries — Formula 21 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links F, x, xi, neq, emptyset..** `F(x,\xi)\neq\emptyset`
Variables: "F, x, xi, neq, emptyset".
Sign/normalization/conditioning/surrogate audit: "Formula 21 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: F, x, xi, neq, emptyset; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 21.

**Formal object 22 at 3 Preliminaries — Formula 22 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links x..** `x`
Variables: "x".
Sign/normalization/conditioning/surrogate audit: "Formula 22 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 22.

**Formal object 23 at 3 Preliminaries — Formula 23 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links xi, in, Xi..** `\xi\in\Xi`
Variables: "xi, in, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 23 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, in, Xi; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 23.

**Formal object 24 at 3 Preliminaries — Formula 24 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links A, in, mathbb, R, p, times, n..** `A\in\mathbb{R}^{p\times n}`
Variables: "A, in, mathbb, R, p, times, n".
Sign/normalization/conditioning/surrogate audit: "Formula 24 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: A, in, mathbb, R, p, times, n; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 24.

**Formal object 25 at 3 Preliminaries — Formula 25 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links d, in, mathbb, R, p..** `d\in\mathbb{R}^{p}`
Variables: "d, in, mathbb, R, p".
Sign/normalization/conditioning/surrogate audit: "Formula 25 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d, in, mathbb, R, p; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 25.

**Formal object 26 at 3 Preliminaries — Formula 26 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links G, in, mathbb, R, r, times, m..** `G\in\mathbb{R}^{r\times m}`
Variables: "G, in, mathbb, R, r, times, m".
Sign/normalization/conditioning/surrogate audit: "Formula 26 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G, in, mathbb, R, r, times, m; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 26.

**Formal object 27 at 3 Preliminaries — Formula 27 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links h, in, mathbb, R, r..** `h\in\mathbb{R}^{r}`
Variables: "h, in, mathbb, R, r".
Sign/normalization/conditioning/surrogate audit: "Formula 27 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: h, in, mathbb, R, r; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 27.

**Formal object 28 at 3 Preliminaries — Formula 28 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links E, in, mathbb, R, r, times, n..** `E\in\mathbb{R}^{r\times n}`
Variables: "E, in, mathbb, R, r, times, n".
Sign/normalization/conditioning/surrogate audit: "Formula 28 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: E, in, mathbb, R, r, times, n; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 28.

**Formal object 29 at 3 Preliminaries — Formula 29 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, times, recourse, decisions, feasible, integer, and the expression links M, in, mathbb, R, r, times, q..** `M\in\mathbb{R}^{r\times q}`
Variables: "M, in, mathbb, R, r, times, q".
Sign/normalization/conditioning/surrogate audit: "Formula 29 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: M, in, mathbb, R, r, times, q; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 29.

**Formal object 30 at 3 Preliminaries — Formula 30 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on denote, cost, first-stage, decision, Core, Notation., and the expression links Q, x, xi, y, in, F, b_{\xi}^{\top}y..** `Q(x,\xi):=\min_{y\in F(x,\xi)}b_{\xi}^{\top}y`
Variables: "Q, x, xi, y, in, F, b_{\\xi}^{\\top}y".
Sign/normalization/conditioning/surrogate audit: "Formula 30 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Q, x, xi, y, in, F, b_{\\xi}^{\\top}y; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 30.

**Formal object 31 at 3 Preliminaries — Formula 31 under 3 Preliminaries is classified as a paper-defined mathematical relation; adjacent prose centers on denote, cost, first-stage, decision, Core, Notation., and the expression links xi..** `\xi`
Variables: "xi".
Sign/normalization/conditioning/surrogate audit: "Formula 31 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 31.

**Formal object 32 at 3 Preliminaries — Formula 32 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on denote, cost, first-stage, decision, scenario, Core, and the expression links Z, x, c, top, xi, in, Xi, Q..** `Z(x):=c^{\top}x+\max_{\xi\in\Xi}Q(x,\xi).`
Variables: "Z, x, c, top, xi, in, Xi, Q".
Sign/normalization/conditioning/surrogate audit: "Formula 32 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Z, x, c, top, xi, in, Xi, Q; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 32.

**Formal object 33 at 3 Preliminaries — Formula 33 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on scenario, subset, subseteq, define, restricted-scenario, objective, and the expression links R, subseteq, Xi..** `R\subseteq\Xi`
Variables: "R, subseteq, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 33 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, subseteq, Xi; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 33.

**Formal object 34 at 3 Preliminaries — Formula 34 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on scenario, subset, subseteq, define, restricted-scenario, objective, and the expression links V, R..** `V(R)`
Variables: "V, R".
Sign/normalization/conditioning/surrogate audit: "Formula 34 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 34.

**Formal object 35 at 3 Preliminaries — Formula 35 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on value, scenario, objective, full-scenario, evaluate, reduced, and the expression links V, R, x, in, X, left, c, top..** `V(R)\;:=\;\min_{x\in X}\left[c^{\top}x\,+\,\max_{\xi\in R}\,Q(x,\xi)\right],`
Variables: "V, R, x, in, X, left, c, top, xi, Q, right".
Sign/normalization/conditioning/surrogate audit: "Formula 35 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R, x, in, X, left, c, top, xi, Q, right; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 35.

**Formal object 36 at 3 Preliminaries — Formula 36 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on value, full-scenario, objective, evaluate, scenario, reduced, and the expression links V, emptyset..** `V(\emptyset):=0`
Variables: "V, emptyset".
Sign/normalization/conditioning/surrogate audit: "Formula 36 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, emptyset; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 36.

**Formal object 37 at 3 Preliminaries — Formula 37 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on value, full-scenario, objective, evaluate, scenario, reduced, and the expression links V, Xi..** `V(\Xi)`
Variables: "V, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 37 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, Xi; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 37.

**Formal object 38 at 3 Preliminaries — Formula 38 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on value, full-scenario, objective, evaluate, scenario, reduced, and the expression links R, k..** `R=R^{(k)}`
Variables: "R, k".
Sign/normalization/conditioning/surrogate audit: "Formula 38 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, k; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 38.

**Formal object 39 at 3 Preliminaries — Formula 39 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on value, full-scenario, objective, evaluate, scenario, reduced, and the expression links R, k..** `|R^{(k)}|=k`
Variables: "R, k".
Sign/normalization/conditioning/surrogate audit: "Formula 39 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, k; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 39.

**Formal object 40 at 3 Preliminaries — Formula 40 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on value, full-scenario, objective, evaluate, scenario, reduced, and the expression links V, R, k..** `V(R^{(k)})`
Variables: "V, R, k".
Sign/normalization/conditioning/surrogate audit: "Formula 40 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R, k; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 40.

**Formal object 41 at 3 Preliminaries — Formula 41 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on value, full-scenario, objective, evaluate, scenario, reduced, and the expression links R, k..** `R^{(k)}`
Variables: "R, k".
Sign/normalization/conditioning/surrogate audit: "Formula 41 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, k; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 41.

**Formal object 42 at 3 Preliminaries — Formula 42 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on value, full-scenario, objective, evaluate, scenario, reduced, and the expression links x, k, star..** `x^{(k)\star}`
Variables: "x, k, star".
Sign/normalization/conditioning/surrogate audit: "Formula 42 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x, k, star; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 42.

**Formal object 43 at 3 Preliminaries — Formula 43 under 3 Preliminaries is classified as a optimization objective or loss; adjacent prose centers on value, full-scenario, star, problem, regret, objective, and the expression links mathrm, R, k, Z, x, star, V, Xi..** `\mathrm{Regret}(R^{(k)})\;=\;\frac{Z(x^{(k)\star})\;-\;V(\Xi)}{V(\Xi)}\times 100.`
Variables: "mathrm, R, k, Z, x, star, V, Xi, times".
Sign/normalization/conditioning/surrogate audit: "Formula 43 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm, R, k, Z, x, star, V, Xi, times; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 43.

**Formal object 44 at 3 Preliminaries — Formula 44 under 3 Preliminaries is classified as a probabilistic or expectation relation; adjacent prose centers on Regret, problem., Since, mathrm, equality, only, and the expression links V, Xi, x, in, X, Z..** `V(\Xi)=\min_{x\in X}Z(x)`
Variables: "V, Xi, x, in, X, Z".
Sign/normalization/conditioning/surrogate audit: "Formula 44 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, Xi, x, in, X, Z; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 44.

**Formal object 45 at 3 Preliminaries — Formula 45 under 3 Preliminaries is classified as a probabilistic or expectation relation; adjacent prose centers on Regret, problem., Since, mathrm, equality, only, and the expression links mathrm, R, k, geq..** `\mathrm{Regret}(R^{(k)})\geq 0`
Variables: "mathrm, R, k, geq".
Sign/normalization/conditioning/surrogate audit: "Formula 45 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm, R, k, geq; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 45.

**Formal object 46 at 3 Preliminaries — Formula 46 under 3 Preliminaries is classified as a probabilistic or expectation relation; adjacent prose centers on Regret, problem., Since, mathrm, equality, only, and the expression links Xi..** `|\Xi|`
Variables: "Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 46 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Xi; meanings remain tied to 3 Preliminaries.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries, formal object 46.

**Formal object 47 at 4.1 PRISE — Formula 47 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, reduced, scenario, candidate, constructs, subseteq, and the expression links t..** `t`
Variables: "t".
Sign/normalization/conditioning/surrogate audit: "Formula 47 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: t; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 47.

**Formal object 48 at 4.1 PRISE — Formula 48 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, reduced, scenario, candidate, constructs, subseteq, and the expression links R_{t}..** `R_{t}`
Variables: "R_{t}".
Sign/normalization/conditioning/surrogate audit: "Formula 48 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R_{t}; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 48.

**Formal object 49 at 4.1 PRISE — Formula 49 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, reduced, scenario, candidate, constructs, subseteq, and the expression links R_{0}, emptyset..** `R_{0}=\emptyset`
Variables: "R_{0}, emptyset".
Sign/normalization/conditioning/surrogate audit: "Formula 49 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R_{0}, emptyset; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 49.

**Formal object 50 at 4.1 PRISE — Formula 50 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, reduced, scenario, candidate, constructs, subseteq, and the expression links xi, j, in, Xi, setminus, R_{t}..** `\xi_{j}\in\Xi\setminus R_{t}`
Variables: "xi, j, in, Xi, setminus, R_{t}".
Sign/normalization/conditioning/surrogate audit: "Formula 50 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, j, in, Xi, setminus, R_{t}; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 50.

**Formal object 51 at 4.1 PRISE — Formula 51 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, reduced, scenario, candidate, constructs, subseteq, and the expression links R_{t}\cup\{\xi, j..** `R_{t}\cup\{\xi_{j}\}`
Variables: "R_{t}\\cup\\{\\xi, j".
Sign/normalization/conditioning/surrogate audit: "Formula 51 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R_{t}\\cup\\{\\xi, j; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 51.

**Formal object 52 at 4.1 PRISE — Formula 52 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, marginal, objective, candidate, and the expression links xi, t, mathrm, in, j, Xi, setminus, R_{t}}V..** `\xi_{t}^{\mathrm{PRISE}}\in\arg\max_{\xi_{j}\in\Xi\setminus R_{t}}V(R_{t}\cup\{\xi_{j}\}).`
Variables: "xi, t, mathrm, in, j, Xi, setminus, R_{t}}V, R_{t}\\cup\\{\\xi".
Sign/normalization/conditioning/surrogate audit: "Formula 52 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, t, mathrm, in, j, Xi, setminus, R_{t}}V, R_{t}\\cup\\{\\xi; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 52.

**Formal object 53 at 4.1 PRISE — Formula 53 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, marginal, reduced, objective, full, and the expression links V, R_{t}\cup\{\xi, j, R_{t}..** `V(R_{t}\cup\{\xi_{j}\})-V(R_{t})`
Variables: "V, R_{t}\\cup\\{\\xi, j, R_{t}".
Sign/normalization/conditioning/surrogate audit: "Formula 53 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R_{t}\\cup\\{\\xi, j, R_{t}; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 53.

**Formal object 54 at 4.1 PRISE — Formula 54 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, marginal, reduced, objective, full, and the expression links V, R_{t}\cup\{\xi, j..** `V(R_{t}\cup\{\xi_{j}\})`
Variables: "V, R_{t}\\cup\\{\\xi, j".
Sign/normalization/conditioning/surrogate audit: "Formula 54 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R_{t}\\cup\\{\\xi, j; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 54.

**Formal object 55 at 4.1 PRISE — Formula 55 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links Xi, xi, dots, S..** `\Xi{=}\{\xi_{1},\dots,\xi_{S}\}`
Variables: "Xi, xi, dots, S".
Sign/normalization/conditioning/surrogate audit: "Formula 55 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Xi, xi, dots, S; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 55.

**Formal object 56 at 4.1 PRISE — Formula 56 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links S, Xi..** `S{=}|\Xi|`
Variables: "S, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 56 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S, Xi; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 56.

**Formal object 57 at 4.1 PRISE — Formula 57 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links epsilon, geq..** `\epsilon{\geq}0`
Variables: "epsilon, geq".
Sign/normalization/conditioning/surrogate audit: "Formula 57 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: epsilon, geq; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 57.

**Formal object 58 at 4.1 PRISE — Formula 58 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links hat, k..** `\hat{k}`
Variables: "hat, k".
Sign/normalization/conditioning/surrogate audit: "Formula 58 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, k; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 58.

**Formal object 59 at 4.1 PRISE — Formula 59 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links R..** `R`
Variables: "R".
Sign/normalization/conditioning/surrogate audit: "Formula 59 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 59.

**Formal object 60 at 4.1 PRISE — Formula 60 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links mathcal, D..** `\mathcal{D}`
Variables: "mathcal, D".
Sign/normalization/conditioning/surrogate audit: "Formula 60 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 60.

**Formal object 61 at 4.1 PRISE — Formula 61 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links R, leftarrow, emptyset..** `R\leftarrow\emptyset`
Variables: "R, leftarrow, emptyset".
Sign/normalization/conditioning/surrogate audit: "Formula 61 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, leftarrow, emptyset; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 61.

**Formal object 62 at 4.1 PRISE — Formula 62 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links mathcal, D, leftarrow, emptyset..** `\mathcal{D}\leftarrow\emptyset`
Variables: "mathcal, D, leftarrow, emptyset".
Sign/normalization/conditioning/surrogate audit: "Formula 62 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D, leftarrow, emptyset; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 62.

**Formal object 63 at 4.1 PRISE — Formula 63 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links v_{\mathrm{prev}}\leftarrow..** `v_{\mathrm{prev}}\leftarrow 0`
Variables: "v_{\\mathrm{prev}}\\leftarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 63 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: v_{\\mathrm{prev}}\\leftarrow; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 63.

**Formal object 64 at 4.1 PRISE — Formula 64 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links R, K..** `|R|<K`
Variables: "R, K".
Sign/normalization/conditioning/surrogate audit: "Formula 64 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, K; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 64.

**Formal object 65 at 4.1 PRISE — Formula 65 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links xi, j, in, Xi, setminus, R..** `\xi_{j}\in\Xi\setminus R`
Variables: "xi, j, in, Xi, setminus, R".
Sign/normalization/conditioning/surrogate audit: "Formula 65 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, j, in, Xi, setminus, R; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 65.

**Formal object 66 at 4.1 PRISE — Formula 66 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links mathrm, xi, j, leftarrow, V, R, cup..** `\mathrm{score}(\xi_{j})\leftarrow V(R\cup\{\xi_{j}\})`
Variables: "mathrm, xi, j, leftarrow, V, R, cup".
Sign/normalization/conditioning/surrogate audit: "Formula 66 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm, xi, j, leftarrow, V, R, cup; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 66.

**Formal object 67 at 4.1 PRISE — Formula 67 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links xi, star, leftarrow..** `\xi^{\star}\leftarrow`
Variables: "xi, star, leftarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 67 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, star, leftarrow; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 67.

**Formal object 68 at 4.1 PRISE — Formula 68 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links Delta, leftarrow, mathrm, xi, star, v_{\mathrm{prev}}..** `\Delta\leftarrow\mathrm{score}(\xi^{\star})-v_{\mathrm{prev}}`
Variables: "Delta, leftarrow, mathrm, xi, star, v_{\\mathrm{prev}}".
Sign/normalization/conditioning/surrogate audit: "Formula 68 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta, leftarrow, mathrm, xi, star, v_{\\mathrm{prev}}; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 68.

**Formal object 69 at 4.1 PRISE — Formula 69 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links Delta, leq, epsilon..** `\Delta\leq\epsilon`
Variables: "Delta, leq, epsilon".
Sign/normalization/conditioning/surrogate audit: "Formula 69 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta, leq, epsilon; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 69.

**Formal object 70 at 4.1 PRISE — Formula 70 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links R, xi, star, Delta..** `(R,\xi^{\star},\Delta)`
Variables: "R, xi, star, Delta".
Sign/normalization/conditioning/surrogate audit: "Formula 70 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, xi, star, Delta; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 70.

**Formal object 71 at 4.1 PRISE — Formula 71 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links xi, star..** `\xi^{\star}`
Variables: "xi, star".
Sign/normalization/conditioning/surrogate audit: "Formula 71 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, star; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 71.

**Formal object 72 at 4.1 PRISE — Formula 72 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links R, leftarrow, cup, xi, star..** `R\leftarrow R\cup\{\xi^{\star}\}`
Variables: "R, leftarrow, cup, xi, star".
Sign/normalization/conditioning/surrogate audit: "Formula 72 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, leftarrow, cup, xi, star; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 72.

**Formal object 73 at 4.1 PRISE — Formula 73 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links v_{\mathrm{prev}}\leftarrow\mathrm{score}, xi, star..** `v_{\mathrm{prev}}\leftarrow\mathrm{score}(\xi^{\star})`
Variables: "v_{\\mathrm{prev}}\\leftarrow\\mathrm{score}, xi, star".
Sign/normalization/conditioning/surrogate audit: "Formula 73 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: v_{\\mathrm{prev}}\\leftarrow\\mathrm{score}, xi, star; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 73.

**Formal object 74 at 4.1 PRISE — Formula 74 under 4.1 PRISE is classified as a optimization objective or loss; adjacent prose centers on PRISE, scenario, reduced, selection, marginal, objective, and the expression links hat, k, leftarrow, R..** `\hat{k}\leftarrow|R|`
Variables: "hat, k, leftarrow, R".
Sign/normalization/conditioning/surrogate audit: "Formula 74 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, k, leftarrow, R; meanings remain tied to 4.1 PRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.1 PRISE, formal object 74.

**Formal object 75 at 4.2 NeurPRISE — Formula 75 under 4.2 NeurPRISE is classified as a paper-defined mathematical relation; adjacent prose centers on PRISE, NeurPRISE, selection, scenario, While, produces, and the expression links mathcal, O, K, Xi..** `\mathcal{O}(K{\cdot}|\Xi|)`
Variables: "mathcal, O, K, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 75 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, O, K, Xi; meanings remain tied to 4.2 NeurPRISE.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2 NeurPRISE, formal object 75.

**Formal object 76 at 4.2.1 Model Architecture — Formula 76 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on graph, scenario, bipartite, Encoder., model, standard, and the expression links xi, j, in, Xi..** `\xi_{j}\in\Xi`
Variables: "xi, j, in, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 76 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, j, in, Xi; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 76.

**Formal object 77 at 4.2.1 Model Architecture — Formula 77 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on graph, scenario, bipartite, Encoder., model, standard, and the expression links G_{j}..** `G_{j}`
Variables: "G_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 77 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G_{j}; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 77.

**Formal object 78 at 4.2.1 Model Architecture — Formula 78 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on graph, scenario, bipartite, Encoder., model, standard, and the expression links d_{s}..** `d_{s}`
Variables: "d_{s}".
Sign/normalization/conditioning/surrogate audit: "Formula 78 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{s}; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 78.

**Formal object 79 at 4.2.1 Model Architecture — Formula 79 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on scenario, graph, embeddings, Encoder., bipartite, model, and the expression links mathbf, h, j, mathrm, left, phi, G_{j}, right..** `\mathbf{h}_{j}=\mathrm{Pool}\left(\mathrm{GNN}_{\phi}(G_{j})\right)\in\mathbb{R}^{d_{s}}.`
Variables: "mathbf, h, j, mathrm, left, phi, G_{j}, right, in, mathbb, R, d_{s}}".
Sign/normalization/conditioning/surrogate audit: "Formula 79 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, h, j, mathrm, left, phi, G_{j}, right, in, mathbb, R, d_{s}}; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 79.

**Formal object 80 at 4.2.1 Model Architecture — Formula 80 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on embeddings, Decoder., instance, context, capture, inter-scenario, and the expression links mathbf, Z, mathrm, h, Xi, in, mathbb, R..** `\mathbf{Z}_{\mathrm{sce}}=\mathrm{TransformerEnc}(\mathbf{h}_{1:|\Xi|})\in\mathbb{R}^{|\Xi|\times d_{s}}.`
Variables: "mathbf, Z, mathrm, h, Xi, in, mathbb, R, times, d_{s}}".
Sign/normalization/conditioning/surrogate audit: "Formula 80 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, Z, mathrm, h, Xi, in, mathbb, R, times, d_{s}}; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 80.

**Formal object 81 at 4.2.1 Model Architecture — Formula 81 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on Decoder., instance, context, mathbf, mathrm, scenarios, and the expression links mathbf, z, mathrm, Xi, j, h, in, mathbb..** `\mathbf{z}_{\mathrm{inst}}=\frac{1}{|\Xi|}\sum_{j=1}^{|\Xi|}\mathbf{h}_{j}\;\in\;\mathbb{R}^{d_{s}}.`
Variables: "mathbf, z, mathrm, Xi, j, h, in, mathbb, R, d_{s}}".
Sign/normalization/conditioning/surrogate audit: "Formula 81 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) |\\Xi|. Variables audited: mathbf, z, mathrm, Xi, j, h, in, mathbb, R, d_{s}}; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 81.

**Formal object 82 at 4.2.1 Model Architecture — Formula 82 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbf, mathrm, inst, times, representing, serves, and the expression links mathbf, z, mathrm..** `\mathbf{z}_{\mathrm{inst}}`
Variables: "mathbf, z, mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 82 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, z, mathrm; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 82.

**Formal object 83 at 4.2.1 Model Architecture — Formula 83 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbf, mathrm, inst, times, representing, serves, and the expression links times, d_{s}..** `[1\times d_{s}]`
Variables: "times, d_{s}".
Sign/normalization/conditioning/surrogate audit: "Formula 83 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times, d_{s}; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 83.

**Formal object 84 at 4.2.1 Model Architecture — Formula 84 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbf, mathrm, inst, times, representing, serves, and the expression links Q..** `Q`
Variables: "Q".
Sign/normalization/conditioning/surrogate audit: "Formula 84 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Q; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 84.

**Formal object 85 at 4.2.1 Model Architecture — Formula 85 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbf, mathrm, inst, times, representing, serves, and the expression links mathbf, Z, mathrm..** `\mathbf{Z}_{\mathrm{sce}}`
Variables: "mathbf, Z, mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 85 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, Z, mathrm; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 85.

**Formal object 86 at 4.2.1 Model Architecture — Formula 86 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbf, mathrm, inst, times, representing, serves, and the expression links Xi, times, d_{s}..** `[|\Xi|\times d_{s}]`
Variables: "Xi, times, d_{s}".
Sign/normalization/conditioning/surrogate audit: "Formula 86 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Xi, times, d_{s}; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 86.

**Formal object 87 at 4.2.1 Model Architecture — Formula 87 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbf, mathrm, inst, times, representing, serves, and the expression links mathbf, K, mathrm..** `\mathbf{K}_{\mathrm{attn}}`
Variables: "mathbf, K, mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 87 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, K, mathrm; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 87.

**Formal object 88 at 4.2.1 Model Architecture — Formula 88 under 4.2.1 Model Architecture is classified as a evaluation or scoring relation; adjacent prose centers on head, inputs, projected, parallel, heads, dimension, and the expression links H..** `H`
Variables: "H".
Sign/normalization/conditioning/surrogate audit: "Formula 88 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: H; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 88.

**Formal object 89 at 4.2.1 Model Architecture — Formula 89 under 4.2.1 Model Architecture is classified as a evaluation or scoring relation; adjacent prose centers on head, inputs, projected, parallel, heads, dimension, and the expression links d_{k}..** `d_{k}`
Variables: "d_{k}".
Sign/normalization/conditioning/surrogate audit: "Formula 89 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{k}; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 89.

**Formal object 90 at 4.2.1 Model Architecture — Formula 90 under 4.2.1 Model Architecture is classified as a evaluation or scoring relation; adjacent prose centers on head, inputs, projected, parallel, heads, dimension, and the expression links h, in, dots, H..** `h\in\{1,\dots,H\}`
Variables: "h, in, dots, H".
Sign/normalization/conditioning/surrogate audit: "Formula 90 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: h, in, dots, H; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 90.

**Formal object 91 at 4.2.1 Model Architecture — Formula 91 under 4.2.1 Model Architecture is classified as a evaluation or scoring relation; adjacent prose centers on head, inputs, projected, parallel, heads, dimension, and the expression links j..** `j`
Variables: "j".
Sign/normalization/conditioning/surrogate audit: "Formula 91 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: j; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 91.

**Formal object 92 at 4.2.1 Model Architecture — Formula 92 under 4.2.1 Model Architecture is classified as a evaluation or scoring relation; adjacent prose centers on head, scenario, mathbf, inputs, projected, parallel, and the expression links s_{h, j, mathbf, z, mathrm, W, h, Q..** `s_{h,j}=\frac{(\mathbf{z}_{\mathrm{inst}}\mathbf{W}_{h}^{Q})\cdot(\mathbf{Z}_{\mathrm{sce},j}\mathbf{W}_{h}^{K})}{\sqrt{d_{k}}}\in\mathbb{R},`
Variables: "s_{h, j, mathbf, z, mathrm, W, h, Q, Z, K, d_{k}}}\\in\\mathbb{R}".
Sign/normalization/conditioning/surrogate audit: "Formula 92 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{h, j, mathbf, z, mathrm, W, h, Q, Z, K, d_{k}}}\\in\\mathbb{R}; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 92.

**Formal object 93 at 4.2.1 Model Architecture — Formula 93 under 4.2.1 Model Architecture is classified as a evaluation or scoring relation; adjacent prose centers on mathbf, scenario, where, learnable, projection, matrices., and the expression links mathbf, W, h, Q, K..** `\mathbf{W}_{h}^{Q},\mathbf{W}_{h}^{K}`
Variables: "mathbf, W, h, Q, K".
Sign/normalization/conditioning/surrogate audit: "Formula 93 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, W, h, Q, K; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 93.

**Formal object 94 at 4.2.1 Model Architecture — Formula 94 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on scenario, where, mathbf, importance, scores, mathbb, and the expression links z_{j}, mathrm, left, s_{1, j, dots, s_{H, right..** `z_{j}=\mathrm{MLP}\!\left([s_{1,j},\,\dots,\,s_{H,j}]\right),\quad j\in\{1,\dots,|\Xi|\},`
Variables: "z_{j}, mathrm, left, s_{1, j, dots, s_{H, right, quad, in, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 94 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: z_{j}, mathrm, left, s_{1, j, dots, s_{H, right, quad, in, Xi; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 94.

**Formal object 95 at 4.2.1 Model Architecture — Formula 95 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbb, single, NeurPRISE, where, maps, hidden, and the expression links mathbb, R, H, to..** `\mathbb{R}^{H}\to\mathbb{R}`
Variables: "mathbb, R, H, to".
Sign/normalization/conditioning/surrogate audit: "Formula 95 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbb, R, H, to; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 95.

**Formal object 96 at 4.2.1 Model Architecture — Formula 96 under 4.2.1 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbb, single, NeurPRISE, where, maps, hidden, and the expression links z_{j}\}, j, Xi..** `\{z_{j}\}_{j=1}^{|\Xi|}`
Variables: "z_{j}\\}, j, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 96 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: z_{j}\\}, j, Xi; meanings remain tied to 4.2.1 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture, formal object 96.

**Formal object 97 at 4.2.2 Loss Function — Formula 97 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on scenario, gain, score, selected, Delta_, target, and the expression links xi, j_{t}}..** `\xi_{j_{t}}`
Variables: "xi, j_{t}}".
Sign/normalization/conditioning/surrogate audit: "Formula 97 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, j_{t}}; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 97.

**Formal object 98 at 4.2.2 Loss Function — Formula 98 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on scenario, gain, score, selected, Delta_, target, and the expression links Delta, t, V, R_{t}\cup\{\xi, j_{t}}\}, R_{t}..** `\Delta_{t}=V(R_{t}\cup\{\xi_{j_{t}}\})-V(R_{t})`
Variables: "Delta, t, V, R_{t}\\cup\\{\\xi, j_{t}}\\}, R_{t}".
Sign/normalization/conditioning/surrogate audit: "Formula 98 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta, t, V, R_{t}\\cup\\{\\xi, j_{t}}\\}, R_{t}; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 98.

**Formal object 99 at 4.2.2 Loss Function — Formula 99 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on scenario, gain, score, selected, Delta_, target, and the expression links g, in, mathbb, R, Xi..** `g\in\mathbb{R}^{|\Xi|}`
Variables: "g, in, mathbb, R, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 99 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: g, in, mathbb, R, Xi; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 99.

**Formal object 100 at 4.2.2 Loss Function — Formula 100 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on scenario, gain, score, selected, Delta_, target, and the expression links g_{j}, Delta, t..** `g_{j}=\Delta_{t}`
Variables: "g_{j}, Delta, t".
Sign/normalization/conditioning/surrogate audit: "Formula 100 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: g_{j}, Delta, t; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 100.

**Formal object 101 at 4.2.2 Loss Function — Formula 101 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on scenario, gain, score, selected, Delta_, target, and the expression links g_{j}..** `g_{j}=0`
Variables: "g_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 101 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: g_{j}; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 101.

**Formal object 102 at 4.2.2 Loss Function — Formula 102 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on scenario, gain, target, one-shot, score, selected, and the expression links y_{j}, g_{j}..** `y_{j}=\log(1+g_{j}).`
Variables: "y_{j}, g_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 102 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{j}, g_{j}; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 102.

**Formal object 103 at 4.2.2 Loss Function — Formula 103 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on distribution, convert, compressed, gains, soft, target, and the expression links P..** `P`
Variables: "P".
Sign/normalization/conditioning/surrogate audit: "Formula 103 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: P; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 103.

**Formal object 104 at 4.2.2 Loss Function — Formula 104 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on distribution, convert, compressed, gains, soft, target, and the expression links hat, P..** `\hat{P}`
Variables: "hat, P".
Sign/normalization/conditioning/surrogate audit: "Formula 104 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, P; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 104.

**Formal object 105 at 4.2.2 Loss Function — Formula 105 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on distribution, convert, compressed, gains, soft, target, and the expression links z_{j}..** `z_{j}`
Variables: "z_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 105 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: z_{j}; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 105.

**Formal object 106 at 4.2.2 Loss Function — Formula 106 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on target, distribution, scenarios, convert, compressed, gains, and the expression links P_{j}, y_{j}, tau, ell, Xi, y_{\ell}, qquad, hat..** `P_{j}=\frac{\exp(y_{j}/\tau)}{\sum_{\ell=1}^{|\Xi|}\exp(y_{\ell}/\tau)},\qquad\hat{P}_{j}=\frac{\exp(z_{j})}{\sum_{\ell=1}^{|\Xi|}\exp(z_{\ell})},`
Variables: "P_{j}, y_{j}, tau, ell, Xi, y_{\\ell}, qquad, hat, P, j, z_{j}, z_{\\ell}".
Sign/normalization/conditioning/surrogate audit: "Formula 106 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: P_{j}, y_{j}, tau, ell, Xi, y_{\\ell}, qquad, hat, P, j, z_{j}, z_{\\ell}; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 106.

**Formal object 107 at 4.2.2 Loss Function — Formula 107 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on where, temperature, flattens, target, ensuring, unselected, and the expression links tau..** `\tau`
Variables: "tau".
Sign/normalization/conditioning/surrogate audit: "Formula 107 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tau; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 107.

**Formal object 108 at 4.2.2 Loss Function — Formula 108 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on scenarios, where, temperature, flattens, target, ensuring, and the expression links mathcal, L, theta, D_{\mathrm{KL}}\, left, P, hat, right..** `\mathcal{L}(\theta)=D_{\mathrm{KL}}\!\left(P\,\|\,\hat{P}\right).`
Variables: "mathcal, L, theta, D_{\\mathrm{KL}}\\, left, P, hat, right".
Sign/normalization/conditioning/surrogate audit: "Formula 108 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, L, theta, D_{\\mathrm{KL}}\\, left, P, hat, right; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 108.

**Formal object 109 at 4.2.2 Loss Function — Formula 109 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on scenarios., NeurPRISE, produces, single, forward, pass, and the expression links k, leq, K..** `k\leq K`
Variables: "k, leq, K".
Sign/normalization/conditioning/surrogate audit: "Formula 109 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k, leq, K; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 109.

**Formal object 110 at 4.2.2 Loss Function — Formula 110 under 4.2.2 Loss Function is classified as a optimization objective or loss; adjacent prose centers on SWKL, loss., refer, objective, Score-Weighted, forward, and the expression links D_{\mathrm{KL}}, P, hat..** `D_{\mathrm{KL}}(P\|\hat{P})`
Variables: "D_{\\mathrm{KL}}, P, hat".
Sign/normalization/conditioning/surrogate audit: "Formula 110 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: D_{\\mathrm{KL}}, P, hat; meanings remain tied to 4.2.2 Loss Function.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.2 Loss Function, formal object 110.

**Formal object 111 at 5 Experiments — Formula 111 under 5 Experiments is classified as a optimization objective or loss; adjacent prose centers on Gurobi, experiments, conducted, server, EPYC, Core, and the expression links symbols defined beside the formula..** `10^{-4}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 111 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5 Experiments.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, formal object 111.

**Formal object 112 at 5 Experiments — Formula 112 under 5 Experiments is classified as a constraint or formal-analysis relation; adjacent prose centers on evaluate, problem, minimum-cost, items, uncertain, costs, and the expression links n..** `n`
Variables: "n".
Sign/normalization/conditioning/surrogate audit: "Formula 112 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: n; meanings remain tied to 5 Experiments.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, formal object 112.

**Formal object 113 at 5 Experiments — Formula 113 under 5 Experiments is classified as a paper-defined mathematical relation; adjacent prose centers on instances, Uniform, Instance, Generation., generate, small, and the expression links mathrm..** `\mathrm{Uniform}[1,100]`
Variables: "mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 113 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm; meanings remain tied to 5 Experiments.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, formal object 113.

**Formal object 114 at 5 Experiments — Formula 114 under 5 Experiments is classified as a optimization objective or loss; adjacent prose centers on Training., validation, instances, test, report, results, and the expression links operatorname, k..** `\operatorname{top\text{-}k}`
Variables: "operatorname, k".
Sign/normalization/conditioning/surrogate audit: "Formula 114 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: operatorname, k; meanings remain tied to 5 Experiments.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, formal object 114.

**Formal object 115 at 5 Experiments — Formula 115 under 5 Experiments is classified as a optimization objective or loss; adjacent prose centers on NeurPRISE, methods., scenarios, Baselines., PRISE, across, and the expression links k..** `k=1`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 115 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 5 Experiments.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, formal object 115.

**Formal object 116 at 5 Experiments — Formula 116 under 5 Experiments is classified as a optimization objective or loss; adjacent prose centers on NeurPRISE, methods., scenarios, Baselines., PRISE, across, and the expression links k..** `k=2`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 116 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 5 Experiments.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, formal object 116.

**Formal object 117 at 5 Experiments — Formula 117 under 5 Experiments is classified as a optimization objective or loss; adjacent prose centers on NeurPRISE, methods., scenarios, Baselines., PRISE, across, and the expression links k..** `k=4`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 117 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 5 Experiments.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, formal object 117.

**Formal object 118 at 5 Experiments — Formula 118 under 5 Experiments is classified as a optimization objective or loss; adjacent prose centers on NeurPRISE, methods., scenarios, Baselines., PRISE, across, and the expression links k..** `k=6`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 118 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 5 Experiments.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, formal object 118.

**Formal object 119 at 5 Experiments — Formula 119 under 5 Experiments is classified as a optimization objective or loss; adjacent prose centers on NeurPRISE, methods., scenarios, Baselines., PRISE, across, and the expression links downarrow..** `\downarrow`
Variables: "downarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 119 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: downarrow; meanings remain tied to 5 Experiments.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, formal object 119.

**Formal object 120 at 5.1 Comparison Analysis — Formula 120 under 5.1 Comparison Analysis is classified as a evaluation or scoring relation; adjacent prose centers on NeurPRISE, across, methods, regret, PRISE, achieves, and the expression links k, in..** `k\in\{1,2,4,6\}`
Variables: "k, in".
Sign/normalization/conditioning/surrogate audit: "Formula 120 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k, in; meanings remain tied to 5.1 Comparison Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.1 Comparison Analysis, formal object 120.

**Formal object 121 at 5.1 Comparison Analysis — Formula 121 under 5.1 Comparison Analysis is classified as a evaluation or scoring relation; adjacent prose centers on NeurPRISE, across, methods, regret, PRISE, achieves, and the expression links k..** `k{=}1`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 121 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 5.1 Comparison Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.1 Comparison Analysis, formal object 121.

**Formal object 122 at 5.1 Comparison Analysis — Formula 122 under 5.1 Comparison Analysis is classified as a evaluation or scoring relation; adjacent prose centers on NeurPRISE, across, methods, regret, PRISE, achieves, and the expression links k, geq..** `k{\geq}2`
Variables: "k, geq".
Sign/normalization/conditioning/surrogate audit: "Formula 122 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k, geq; meanings remain tied to 5.1 Comparison Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.1 Comparison Analysis, formal object 122.

**Formal object 123 at 5.1 Comparison Analysis — Formula 123 under 5.1 Comparison Analysis is classified as a evaluation or scoring relation; adjacent prose centers on NeurPRISE, across, methods, regret, PRISE, achieves, and the expression links k..** `k{=}2`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 123 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 5.1 Comparison Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.1 Comparison Analysis, formal object 123.

**Formal object 124 at 5.1 Comparison Analysis — Formula 124 under 5.1 Comparison Analysis is classified as a evaluation or scoring relation; adjacent prose centers on NeurPRISE, across, methods, regret, PRISE, achieves, and the expression links k, geq..** `k{\geq}4`
Variables: "k, geq".
Sign/normalization/conditioning/surrogate audit: "Formula 124 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k, geq; meanings remain tied to 5.1 Comparison Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.1 Comparison Analysis, formal object 124.

**Formal object 125 at 5.2 Flexibility and Scalability — Formula 125 under 5.2 Flexibility and Scalability is classified as a constraint or formal-analysis relation; adjacent prose centers on scenario, runtime, without, budget, When, tolerance, and the expression links symbols defined beside the formula..** `7\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 125 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5.2 Flexibility and Scalability.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.2 Flexibility and Scalability, formal object 125.

**Formal object 126 at 5.2 Flexibility and Scalability — Formula 126 under 5.2 Flexibility and Scalability is classified as a constraint or formal-analysis relation; adjacent prose centers on scenario, runtime, without, budget, When, tolerance, and the expression links times..** `2\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 126 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to 5.2 Flexibility and Scalability.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.2 Flexibility and Scalability, formal object 126.

**Formal object 127 at 5.2 Flexibility and Scalability — Formula 127 under 5.2 Flexibility and Scalability is classified as a constraint or formal-analysis relation; adjacent prose centers on scenario, runtime, without, budget, When, tolerance, and the expression links symbols defined beside the formula..** `25\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 127 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5.2 Flexibility and Scalability.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.2 Flexibility and Scalability, formal object 127.

**Formal object 128 at 5.2 Flexibility and Scalability — Formula 128 under 5.2 Flexibility and Scalability is classified as a constraint or formal-analysis relation; adjacent prose centers on scenario, runtime, without, budget, When, tolerance, and the expression links symbols defined beside the formula..** `3.4\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 128 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5.2 Flexibility and Scalability.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.2 Flexibility and Scalability, formal object 128.

**Formal object 129 at 5.2 Flexibility and Scalability — Formula 129 under 5.2 Flexibility and Scalability is classified as a optimization objective or loss; adjacent prose centers on scenarios, Sub-linear, runtime, scaling, scenario, count., and the expression links times..** `1.7\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 129 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to 5.2 Flexibility and Scalability.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.2 Flexibility and Scalability, formal object 129.

**Formal object 130 at 5.3 Generalization — Formula 130 under 5.3 Generalization is classified as a state or representation transformation; adjacent prose centers on Scenario, across, NeurPRISE, count, times, demonstrate, and the expression links s..** `s{=}50`
Variables: "s".
Sign/normalization/conditioning/surrogate audit: "Formula 130 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 130.

**Formal object 131 at 5.3 Generalization — Formula 131 under 5.3 Generalization is classified as a state or representation transformation; adjacent prose centers on Scenario, across, NeurPRISE, count, times, demonstrate, and the expression links s..** `s{=}100,200`
Variables: "s".
Sign/normalization/conditioning/surrogate audit: "Formula 131 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 131.

**Formal object 132 at 5.3 Generalization — Formula 132 under 5.3 Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on NeurPRISE, Scenario, across, generalizes, text, scenarios., and the expression links k..** `k{=}4`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 132 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 132.

**Formal object 133 at 5.3 Generalization — Formula 133 under 5.3 Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on NeurPRISE, Scenario, across, generalizes, text, scenarios., and the expression links k..** `k{=}6`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 133 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 133.

**Formal object 134 at 5.3 Generalization — Formula 134 under 5.3 Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on NeurPRISE, Scenario, across, generalizes, text, scenarios., and the expression links symbols defined beside the formula..** `100,200`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 134 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 134.

**Formal object 135 at 5.3 Generalization — Formula 135 under 5.3 Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on NeurPRISE, Scenario, across, generalizes, text, scenarios., and the expression links S..** `S{=}100`
Variables: "S".
Sign/normalization/conditioning/surrogate audit: "Formula 135 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 135.

**Formal object 136 at 5.3 Generalization — Formula 136 under 5.3 Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on NeurPRISE, Scenario, across, generalizes, text, scenarios., and the expression links S..** `S{=}200`
Variables: "S".
Sign/normalization/conditioning/surrogate audit: "Formula 136 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 136.

**Formal object 137 at 5.3 Generalization — Formula 137 under 5.3 Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on NeurPRISE, Scenario, across, generalizes, text, scenarios., and the expression links k..** `k{=}8`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 137 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 137.

**Formal object 138 at 5.3 Generalization — Formula 138 under 5.3 Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on NeurPRISE, Scenario, across, generalizes, text, scenarios., and the expression links k..** `k{=}16`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 138 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 138.

**Formal object 139 at 5.3 Generalization — Formula 139 under 5.3 Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on NeurPRISE, text, Distribution, generalizes, distributions, across, and the expression links symbols defined beside the formula..** `{}_{\text{uni}}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 139 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 139.

**Formal object 140 at 5.3 Generalization — Formula 140 under 5.3 Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on NeurPRISE, text, Distribution, generalizes, distributions, across, and the expression links symbols defined beside the formula..** `{}_{\text{norm}}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 140 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 140.

**Formal object 141 at 5.3 Generalization — Formula 141 under 5.3 Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on NeurPRISE, text, Distribution, generalizes, distributions, across, and the expression links symbols defined beside the formula..** `{}_{\text{mm}}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 141 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5.3 Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.3 Generalization, formal object 141.

**Formal object 142 at Appendix A Notation — Formula 142 under Appendix A Notation is classified as a paper-defined mathematical relation; adjacent prose centers on quick, reference, summarize, main, symbols, used, and the expression links V..** `V`
Variables: "V".
Sign/normalization/conditioning/surrogate audit: "Formula 142 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 142.

**Formal object 143 at Appendix A Notation — Formula 143 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links x, in, X..** `x\in X`
Variables: "x, in, X".
Sign/normalization/conditioning/surrogate audit: "Formula 143 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x, in, X; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 143.

**Formal object 144 at Appendix A Notation — Formula 144 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links y, in, F, x, xi..** `y\in F(x,\xi)`
Variables: "y, in, F, x, xi".
Sign/normalization/conditioning/surrogate audit: "Formula 144 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y, in, F, x, xi; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 144.

**Formal object 145 at Appendix A Notation — Formula 145 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links Xi, S..** `|\Xi|=S`
Variables: "Xi, S".
Sign/normalization/conditioning/surrogate audit: "Formula 145 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Xi, S; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 145.

**Formal object 146 at Appendix A Notation — Formula 146 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links c, b_{\xi}..** `c,\ b_{\xi}`
Variables: "c, b_{\\xi}".
Sign/normalization/conditioning/surrogate audit: "Formula 146 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c, b_{\\xi}; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 146.

**Formal object 147 at Appendix A Notation — Formula 147 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links Q, x, xi..** `Q(x,\xi)`
Variables: "Q, x, xi".
Sign/normalization/conditioning/surrogate audit: "Formula 147 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Q, x, xi; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 147.

**Formal object 148 at Appendix A Notation — Formula 148 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links y, in, F, x, xi, b_{\xi}^{\top}y..** `\min_{y\in F(x,\xi)}b_{\xi}^{\top}y`
Variables: "y, in, F, x, xi, b_{\\xi}^{\\top}y".
Sign/normalization/conditioning/surrogate audit: "Formula 148 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y, in, F, x, xi, b_{\\xi}^{\\top}y; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 148.

**Formal object 149 at Appendix A Notation — Formula 149 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links x, in, X, bigl, c, top, xi, R..** `\min_{x\in X}\bigl[c^{\top}x+\max_{\xi\in R}Q(x,\xi)\bigr]`
Variables: "x, in, X, bigl, c, top, xi, R, Q, bigr".
Sign/normalization/conditioning/surrogate audit: "Formula 149 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x, in, X, bigl, c, top, xi, R, Q, bigr; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 149.

**Formal object 150 at Appendix A Notation — Formula 150 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links Z, x..** `Z(x)`
Variables: "Z, x".
Sign/normalization/conditioning/surrogate audit: "Formula 150 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Z, x; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 150.

**Formal object 151 at Appendix A Notation — Formula 151 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links c, top, x, xi, in, Xi, Q..** `c^{\top}x+\max_{\xi\in\Xi}Q(x,\xi)`
Variables: "c, top, x, xi, in, Xi, Q".
Sign/normalization/conditioning/surrogate audit: "Formula 151 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c, top, x, xi, in, Xi, Q; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 151.

**Formal object 152 at Appendix A Notation — Formula 152 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links mathrm, R, k..** `\mathrm{Regret}(R^{(k)})`
Variables: "mathrm, R, k".
Sign/normalization/conditioning/surrogate audit: "Formula 152 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm, R, k; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 152.

**Formal object 153 at Appendix A Notation — Formula 153 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links left, Z, x, k, star, V, Xi, right..** `\left(Z(x^{(k)\star})-V(\Xi)\right)/V(\Xi)\times 100`
Variables: "left, Z, x, k, star, V, Xi, right, times".
Sign/normalization/conditioning/surrogate audit: "Formula 153 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: left, Z, x, k, star, V, Xi, right, times; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 153.

**Formal object 154 at Appendix A Notation — Formula 154 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links R..** `|R|`
Variables: "R".
Sign/normalization/conditioning/surrogate audit: "Formula 154 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 154.

**Formal object 155 at Appendix A Notation — Formula 155 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links V, Xi, R, k, leq..** `(V(\Xi){-}V(R^{(k)}))/V(\Xi)\leq 1\%`
Variables: "V, Xi, R, k, leq".
Sign/normalization/conditioning/surrogate audit: "Formula 155 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, Xi, R, k, leq; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 155.

**Formal object 156 at Appendix A Notation — Formula 156 under Appendix A Notation is classified as a optimization objective or loss; adjacent prose centers on defined, quick, reference, summarize, main, symbols, and the expression links Delta, t..** `\Delta_{t}`
Variables: "Delta, t".
Sign/normalization/conditioning/surrogate audit: "Formula 156 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta, t; meanings remain tied to Appendix A Notation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Appendix A Notation, formal object 156.

**Formal object 157 at Proposition 1 (Monotonicity under set inclusion) . — Formula 157 under Proposition 1 (Monotonicity under set inclusion) . is classified as a optimization objective or loss; adjacent prose centers on subseteq, prime, objective, values, satisfy, and the expression links R, subseteq, prime, Xi..** `R\subseteq R^{\prime}\subseteq\Xi`
Variables: "R, subseteq, prime, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 157 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, subseteq, prime, Xi; meanings remain tied to Proposition 1 (Monotonicity under set inclusion) ..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proposition 1 (Monotonicity under set inclusion) ., formal object 157.

**Formal object 158 at Proposition 1 (Monotonicity under set inclusion) . — Formula 158 under Proposition 1 (Monotonicity under set inclusion) . is classified as a optimization objective or loss; adjacent prose centers on subseteq, prime, objective, values, satisfy, Consequently, and the expression links V, R, leq, prime, Xi..** `V(R)\;\leq\;V(R^{\prime})\;\leq\;V(\Xi).`
Variables: "V, R, leq, prime, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 158 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R, leq, prime, Xi; meanings remain tied to Proposition 1 (Monotonicity under set inclusion) ..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proposition 1 (Monotonicity under set inclusion) ., formal object 158.

**Formal object 159 at Proposition 1 (Monotonicity under set inclusion) . — Formula 159 under Proposition 1 (Monotonicity under set inclusion) . is classified as a paper-defined mathematical relation; adjacent prose centers on subseteq, Consequently, nested, sequence, PRISE, construction, and the expression links R, k, geq..** `\{R^{(k)}\}_{k\geq 1}`
Variables: "R, k, geq".
Sign/normalization/conditioning/surrogate audit: "Formula 159 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, k, geq; meanings remain tied to Proposition 1 (Monotonicity under set inclusion) ..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proposition 1 (Monotonicity under set inclusion) ., formal object 159.

**Formal object 160 at Proposition 1 (Monotonicity under set inclusion) . — Formula 160 under Proposition 1 (Monotonicity under set inclusion) . is classified as a paper-defined mathematical relation; adjacent prose centers on subseteq, Consequently, nested, sequence, PRISE, construction, and the expression links R, k, subseteq, Xi..** `R^{(k)}\subseteq R^{(k+1)}\subseteq\Xi`
Variables: "R, k, subseteq, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 160 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, k, subseteq, Xi; meanings remain tied to Proposition 1 (Monotonicity under set inclusion) ..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proposition 1 (Monotonicity under set inclusion) ., formal object 160.

**Formal object 161 at Proposition 1 (Monotonicity under set inclusion) . — Formula 161 under Proposition 1 (Monotonicity under set inclusion) . is classified as a paper-defined mathematical relation; adjacent prose centers on subseteq, Consequently, nested, sequence, PRISE, construction, and the expression links V, R, k, geq..** `\{V(R^{(k)})\}_{k\geq 1}`
Variables: "V, R, k, geq".
Sign/normalization/conditioning/surrogate audit: "Formula 161 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R, k, geq; meanings remain tied to Proposition 1 (Monotonicity under set inclusion) ..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proposition 1 (Monotonicity under set inclusion) ., formal object 161.

**Formal object 162 at Proposition 1 (Monotonicity under set inclusion) . — Formula 162 under Proposition 1 (Monotonicity under set inclusion) . is classified as a paper-defined mathematical relation; adjacent prose centers on subseteq, Consequently, nested, sequence, PRISE, construction, and the expression links V, Xi, R, k..** `V(\Xi)-V(R^{(k)})`
Variables: "V, Xi, R, k".
Sign/normalization/conditioning/surrogate audit: "Formula 162 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, Xi, R, k; meanings remain tied to Proposition 1 (Monotonicity under set inclusion) ..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proposition 1 (Monotonicity under set inclusion) ., formal object 162.

**Formal object 163 at Proof. — Formula 163 under Proof. is classified as a constraint or formal-analysis relation; adjacent prose centers on Since, subseteq, prime, pointwise, monotonicity, maximum, and the expression links R, subseteq, prime..** `R\subseteq R^{\prime}`
Variables: "R, subseteq, prime".
Sign/normalization/conditioning/surrogate audit: "Formula 163 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, subseteq, prime; meanings remain tied to Proof..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proof., formal object 163.

**Formal object 164 at Proof. — Formula 164 under Proof. is classified as a constraint or formal-analysis relation; adjacent prose centers on Since, subseteq, prime, pointwise, monotonicity, maximum, and the expression links xi, in, R, Q, x, leq, prime..** `\max_{\xi\in R}Q(x,\xi)\;\leq\;\max_{\xi\in R^{\prime}}Q(x,\xi).`
Variables: "xi, in, R, Q, x, leq, prime".
Sign/normalization/conditioning/surrogate audit: "Formula 164 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, in, R, Q, x, leq, prime; meanings remain tied to Proof..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proof., formal object 164.

**Formal object 165 at Proof. — Formula 165 under Proof. is classified as a constraint or formal-analysis relation; adjacent prose centers on Adding, both, sides, taking, minimum, over, and the expression links c, top, x..** `c^{\top}x`
Variables: "c, top, x".
Sign/normalization/conditioning/surrogate audit: "Formula 165 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c, top, x; meanings remain tied to Proof..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proof., formal object 165.

**Formal object 166 at Proof. — Formula 166 under Proof. is classified as a constraint or formal-analysis relation; adjacent prose centers on inequality, prime, subseteq, Adding, both, sides, and the expression links V, R, x, in, X, left, c, top..** `V(R)\;=\;\min_{x\in X}\!\left[c^{\top}x+\max_{\xi\in R}Q(x,\xi)\right]\;\leq\;\min_{x\in X}\!\left[c^{\top}x+\max_{\xi\in R^{\prime}}Q(x,\xi)\right]\;=\;V(R^{\prime}).`
Variables: "V, R, x, in, X, left, c, top, xi, Q, right, leq, prime".
Sign/normalization/conditioning/surrogate audit: "Formula 166 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R, x, in, X, left, c, top, xi, Q, right, leq, prime; meanings remain tied to Proof..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proof., formal object 166.

**Formal object 167 at Proof. — Formula 167 under Proof. is classified as a constraint or formal-analysis relation; adjacent prose centers on prime, subseteq, Applying, same, argument, gives, and the expression links R, prime, subseteq, Xi..** `R^{\prime}\subseteq\Xi`
Variables: "R, prime, subseteq, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 167 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, prime, subseteq, Xi; meanings remain tied to Proof..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proof., formal object 167.

**Formal object 168 at Proof. — Formula 168 under Proof. is classified as a constraint or formal-analysis relation; adjacent prose centers on prime, subseteq, Applying, same, argument, gives, and the expression links V, R, prime, leq, Xi..** `V(R^{\prime})\leq V(\Xi)`
Variables: "V, R, prime, leq, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 168 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R, prime, leq, Xi; meanings remain tied to Proof..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proof., formal object 168.

**Formal object 169 at Proof. — Formula 169 under Proof. is classified as a constraint or formal-analysis relation; adjacent prose centers on prime, subseteq, Applying, same, argument, gives, and the expression links R, k..** `\{R^{(k)}\}`
Variables: "R, k".
Sign/normalization/conditioning/surrogate audit: "Formula 169 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, k; meanings remain tied to Proof..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proof., formal object 169.

**Formal object 170 at Proof. — Formula 170 under Proof. is classified as a constraint or formal-analysis relation; adjacent prose centers on prime, subseteq, Applying, same, argument, gives, and the expression links R, k, subseteq..** `R^{(k)}\subseteq R^{(k+1)}`
Variables: "R, k, subseteq".
Sign/normalization/conditioning/surrogate audit: "Formula 170 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, k, subseteq; meanings remain tied to Proof..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proof., formal object 170.

**Formal object 171 at Proof. — Formula 171 under Proof. is classified as a constraint or formal-analysis relation; adjacent prose centers on prime, subseteq, Applying, same, argument, gives, and the expression links V, R, k, leq..** `V(R^{(k)})\leq V(R^{(k+1)})`
Variables: "V, R, k, leq".
Sign/normalization/conditioning/surrogate audit: "Formula 171 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R, k, leq; meanings remain tied to Proof..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Proof., formal object 171.

**Formal object 172 at Remark 1 (Non-submodularity of V V ) . — Formula 172 under Remark 1 (Non-submodularity of V V ) . is classified as a paper-defined mathematical relation; adjacent prose centers on function, submodular, adding, Although, PRISE, empirically, and the expression links g..** `g`
Variables: "g".
Sign/normalization/conditioning/surrogate audit: "Formula 172 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: g; meanings remain tied to Remark 1 (Non-submodularity of V V ) ..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Remark 1 (Non-submodularity of V V ) ., formal object 172.

**Formal object 173 at Remark 1 (Non-submodularity of V V ) . — Formula 173 under Remark 1 (Non-submodularity of V V ) . is classified as a paper-defined mathematical relation; adjacent prose centers on function, submodular, adding, Although, PRISE, empirically, and the expression links g, S, cup, e, geq, T..** `g(S\cup\{e\})-g(S)\geq g(T\cup\{e\})-g(T)`
Variables: "g, S, cup, e, geq, T".
Sign/normalization/conditioning/surrogate audit: "Formula 173 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: g, S, cup, e, geq, T; meanings remain tied to Remark 1 (Non-submodularity of V V ) ..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Remark 1 (Non-submodularity of V V ) ., formal object 173.

**Formal object 174 at Remark 1 (Non-submodularity of V V ) . — Formula 174 under Remark 1 (Non-submodularity of V V ) . is classified as a paper-defined mathematical relation; adjacent prose centers on function, submodular, adding, Although, PRISE, empirically, and the expression links S, subseteq, T..** `S\subseteq T`
Variables: "S, subseteq, T".
Sign/normalization/conditioning/surrogate audit: "Formula 174 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S, subseteq, T; meanings remain tied to Remark 1 (Non-submodularity of V V ) ..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Remark 1 (Non-submodularity of V V ) ., formal object 174.

**Formal object 175 at Remark 1 (Non-submodularity of V V ) . — Formula 175 under Remark 1 (Non-submodularity of V V ) . is classified as a paper-defined mathematical relation; adjacent prose centers on function, submodular, adding, Although, PRISE, empirically, and the expression links e, notin, T..** `e\notin T`
Variables: "e, notin, T".
Sign/normalization/conditioning/surrogate audit: "Formula 175 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: e, notin, T; meanings remain tied to Remark 1 (Non-submodularity of V V ) ..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Remark 1 (Non-submodularity of V V ) ., formal object 175.

**Formal object 176 at Counterexample. — Formula 176 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on three, first-stage, Consider, instance, feasible, decisions, and the expression links X, a, b, c..** `X=\{a,b,c\}`
Variables: "X, a, b, c".
Sign/normalization/conditioning/surrogate audit: "Formula 176 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: X, a, b, c; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 176.

**Formal object 177 at Counterexample. — Formula 177 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on three, first-stage, Consider, instance, feasible, decisions, and the expression links s_{1}, s_{2}, s_{3}\}..** `\{s_{1},s_{2},s_{3}\}`
Variables: "s_{1}, s_{2}, s_{3}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 177 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{1}, s_{2}, s_{3}\\}; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 177.

**Formal object 178 at Counterexample. — Formula 178 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on three, first-stage, Consider, instance, feasible, decisions, and the expression links f, x, xi, c, top, Q..** `f(x,\xi):=c^{\top}x+Q(x,\xi)`
Variables: "f, x, xi, c, top, Q".
Sign/normalization/conditioning/surrogate audit: "Formula 178 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f, x, xi, c, top, Q; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 178.

**Formal object 179 at Counterexample. — Formula 179 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, three, first-stage, decisions, decision, under, and the expression links f, x, s..** `f(x,s)`
Variables: "f, x, s".
Sign/normalization/conditioning/surrogate audit: "Formula 179 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f, x, s; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 179.

**Formal object 180 at Counterexample. — Formula 180 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, three, first-stage, decisions, decision, under, and the expression links s_{1}..** `s_{1}`
Variables: "s_{1}".
Sign/normalization/conditioning/surrogate audit: "Formula 180 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{1}; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 180.

**Formal object 181 at Counterexample. — Formula 181 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, three, first-stage, decisions, decision, under, and the expression links s_{2}..** `s_{2}`
Variables: "s_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 181 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{2}; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 181.

**Formal object 182 at Counterexample. — Formula 182 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, three, first-stage, decisions, decision, under, and the expression links s_{3}..** `s_{3}`
Variables: "s_{3}".
Sign/normalization/conditioning/surrogate audit: "Formula 182 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{3}; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 182.

**Formal object 183 at Counterexample. — Formula 183 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, three, first-stage, decisions, decision, under, and the expression links a..** `a`
Variables: "a".
Sign/normalization/conditioning/surrogate audit: "Formula 183 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: a; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 183.

**Formal object 184 at Counterexample. — Formula 184 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, three, first-stage, decisions, decision, under, and the expression links b..** `b`
Variables: "b".
Sign/normalization/conditioning/surrogate audit: "Formula 184 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: b; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 184.

**Formal object 185 at Counterexample. — Formula 185 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, three, first-stage, decisions, decision, under, and the expression links c..** `c`
Variables: "c".
Sign/normalization/conditioning/surrogate audit: "Formula 185 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 185.

**Formal object 186 at Counterexample. — Formula 186 under Counterexample. is classified as a paper-defined mathematical relation; adjacent prose centers on compute, subsets, and the expression links V, R, x, in, a, b, c, s..** `V(R)=\min_{x\in\{a,b,c\}}\max_{s\in R}f(x,s)`
Variables: "V, R, x, in, a, b, c, s, f".
Sign/normalization/conditioning/surrogate audit: "Formula 186 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, R, x, in, a, b, c, s, f; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 186.

**Formal object 187 at Counterexample. — Formula 187 under Counterexample. is classified as a optimization objective or loss; adjacent prose centers on compute, subsets, PRISE, Algorithm, greedily, selects, and the expression links s, f, a..** `\max_{s}f(a,s)`
Variables: "s, f, a".
Sign/normalization/conditioning/surrogate audit: "Formula 187 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s, f, a; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 187.

**Formal object 188 at Counterexample. — Formula 188 under Counterexample. is classified as a optimization objective or loss; adjacent prose centers on compute, subsets, PRISE, Algorithm, greedily, selects, and the expression links s, f, b..** `\max_{s}f(b,s)`
Variables: "s, f, b".
Sign/normalization/conditioning/surrogate audit: "Formula 188 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s, f, b; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 188.

**Formal object 189 at Counterexample. — Formula 189 under Counterexample. is classified as a optimization objective or loss; adjacent prose centers on compute, subsets, PRISE, Algorithm, greedily, selects, and the expression links s, f, c..** `\max_{s}f(c,s)`
Variables: "s, f, c".
Sign/normalization/conditioning/surrogate audit: "Formula 189 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s, f, c; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 189.

**Formal object 190 at Counterexample. — Formula 190 under Counterexample. is classified as a optimization objective or loss; adjacent prose centers on compute, subsets, PRISE, Algorithm, greedily, selects, and the expression links s_{1}\}..** `\{s_{1}\}`
Variables: "s_{1}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 190 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{1}\\}; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 190.

**Formal object 191 at Counterexample. — Formula 191 under Counterexample. is classified as a optimization objective or loss; adjacent prose centers on compute, subsets, PRISE, Algorithm, greedily, selects, and the expression links s_{2}\}..** `\{s_{2}\}`
Variables: "s_{2}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 191 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{2}\\}; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 191.

**Formal object 192 at Counterexample. — Formula 192 under Counterexample. is classified as a optimization objective or loss; adjacent prose centers on compute, subsets, PRISE, Algorithm, greedily, selects, and the expression links s_{3}\}..** `\{s_{3}\}`
Variables: "s_{3}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 192 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{3}\\}; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 192.

**Formal object 193 at Counterexample. — Formula 193 under Counterexample. is classified as a optimization objective or loss; adjacent prose centers on compute, subsets, PRISE, Algorithm, greedily, selects, and the expression links s_{1}, s_{2}\}..** `\{s_{1},s_{2}\}`
Variables: "s_{1}, s_{2}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 193 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{1}, s_{2}\\}; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 193.

**Formal object 194 at Counterexample. — Formula 194 under Counterexample. is classified as a optimization objective or loss; adjacent prose centers on compute, subsets, PRISE, Algorithm, greedily, selects, and the expression links s_{1}, s_{3}\}..** `\{s_{1},s_{3}\}`
Variables: "s_{1}, s_{3}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 194 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{1}, s_{3}\\}; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 194.

**Formal object 195 at Counterexample. — Formula 195 under Counterexample. is classified as a optimization objective or loss; adjacent prose centers on compute, subsets, PRISE, Algorithm, greedily, selects, and the expression links s_{2}, s_{3}\}..** `\{s_{2},s_{3}\}`
Variables: "s_{2}, s_{3}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 195 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{2}, s_{3}\\}; meanings remain tied to Counterexample..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Counterexample., formal object 195.

**Formal object 196 at PRISE trace on this instance. — Formula 196 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, varnothing, Evaluate, Select, highest, Gain, and the expression links R_{0}, varnothing..** `R_{0}=\varnothing`
Variables: "R_{0}, varnothing".
Sign/normalization/conditioning/surrogate audit: "Formula 196 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R_{0}, varnothing; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 196.

**Formal object 197 at PRISE trace on this instance. — Formula 197 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, varnothing, Evaluate, Select, highest, Gain, and the expression links V, s_{1}\}..** `V(\{s_{1}\}){=}1`
Variables: "V, s_{1}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 197 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, s_{1}\\}; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 197.

**Formal object 198 at PRISE trace on this instance. — Formula 198 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, varnothing, Evaluate, Select, highest, Gain, and the expression links V, s_{2}\}..** `V(\{s_{2}\}){=}1`
Variables: "V, s_{2}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 198 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, s_{2}\\}; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 198.

**Formal object 199 at PRISE trace on this instance. — Formula 199 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, varnothing, Evaluate, Select, highest, Gain, and the expression links V, s_{3}\}..** `V(\{s_{3}\}){=}5`
Variables: "V, s_{3}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 199 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, s_{3}\\}; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 199.

**Formal object 200 at PRISE trace on this instance. — Formula 200 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, varnothing, Evaluate, Select, highest, Gain, and the expression links Delta..** `\Delta_{0}=5`
Variables: "Delta".
Sign/normalization/conditioning/surrogate audit: "Formula 200 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 200.

**Formal object 201 at PRISE trace on this instance. — Formula 201 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, Evaluate, Select, Gain, Delta_, and the expression links R_{1}, s_{3}\}..** `R_{1}=\{s_{3}\}`
Variables: "R_{1}, s_{3}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 201 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R_{1}, s_{3}\\}; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 201.

**Formal object 202 at PRISE trace on this instance. — Formula 202 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, Evaluate, Select, Gain, Delta_, and the expression links V, s_{3}, s_{1}\}..** `V(\{s_{3},s_{1}\}){=}6`
Variables: "V, s_{3}, s_{1}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 202 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, s_{3}, s_{1}\\}; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 202.

**Formal object 203 at PRISE trace on this instance. — Formula 203 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, Evaluate, Select, Gain, Delta_, and the expression links V, s_{3}, s_{2}\}..** `V(\{s_{3},s_{2}\}){=}5`
Variables: "V, s_{3}, s_{2}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 203 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, s_{3}, s_{2}\\}; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 203.

**Formal object 204 at PRISE trace on this instance. — Formula 204 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, Evaluate, Select, Gain, Delta_, and the expression links Delta..** `\Delta_{1}=6-5=1`
Variables: "Delta".
Sign/normalization/conditioning/surrogate audit: "Formula 204 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 204.

**Formal object 205 at PRISE trace on this instance. — Formula 205 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, Evaluate, Select, Gain, Delta_, and the expression links R_{2}, s_{3}, s_{1}\}..** `R_{2}=\{s_{3},s_{1}\}`
Variables: "R_{2}, s_{3}, s_{1}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 205 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R_{2}, s_{3}, s_{1}\\}; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 205.

**Formal object 206 at PRISE trace on this instance. — Formula 206 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, Evaluate, Select, Gain, Delta_, and the expression links V, s_{3}, s_{1}, s_{2}\}..** `V(\{s_{3},s_{1},s_{2}\}){=}8`
Variables: "V, s_{3}, s_{1}, s_{2}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 206 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, s_{3}, s_{1}, s_{2}\\}; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 206.

**Formal object 207 at PRISE trace on this instance. — Formula 207 under PRISE trace on this instance. is classified as a paper-defined mathematical relation; adjacent prose centers on Step, Evaluate, Select, Gain, Delta_, and the expression links Delta..** `\Delta_{2}=8-6=2`
Variables: "Delta".
Sign/normalization/conditioning/surrogate audit: "Formula 207 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 207.

**Formal object 208 at PRISE trace on this instance. — Formula 208 under PRISE trace on this instance. is classified as a optimization objective or loss; adjacent prose centers on gains, Delta_, Note, marginal, strictly, positive, and the expression links Delta..** `\Delta_{1}=1<2=\Delta_{2}`
Variables: "Delta".
Sign/normalization/conditioning/surrogate audit: "Formula 208 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 208.

**Formal object 209 at PRISE trace on this instance. — Formula 209 under PRISE trace on this instance. is classified as a optimization objective or loss; adjacent prose centers on gains, Delta_, Note, marginal, strictly, positive, and the expression links V, s_{1}, s_{2}, s_{3}\}..** `V(\{s_{1},s_{2},s_{3}\})=8`
Variables: "V, s_{1}, s_{2}, s_{3}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 209 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, s_{1}, s_{2}, s_{3}\\}; meanings remain tied to PRISE trace on this instance..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, PRISE trace on this instance., formal object 209.

**Formal object 210 at Submodularity violation. — Formula 210 under Submodularity violation. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, Delta, decision, under, switch, marginal, and the expression links Delta, s_{3}\}, s_{2}..** `\Delta(\{s_{3}\},s_{2})=0`
Variables: "Delta, s_{3}\\}, s_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 210 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta, s_{3}\\}, s_{2}; meanings remain tied to Submodularity violation..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Submodularity violation., formal object 210.

**Formal object 211 at Submodularity violation. — Formula 211 under Submodularity violation. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, Delta, decision, under, switch, marginal, and the expression links Delta, s_{3}, s_{1}\}, s_{2}..** `\Delta(\{s_{3},s_{1}\},s_{2})=2`
Variables: "Delta, s_{3}, s_{1}\\}, s_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 211 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta, s_{3}, s_{1}\\}, s_{2}; meanings remain tied to Submodularity violation..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Submodularity violation., formal object 211.

**Formal object 212 at Submodularity violation. — Formula 212 under Submodularity violation. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, Delta, decision, under, switch, marginal, and the expression links s_{3}\}\subset\{s, s_{1}\}..** `\{s_{3}\}\subset\{s_{3},s_{1}\}`
Variables: "s_{3}\\}\\subset\\{s, s_{1}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 212 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: s_{3}\\}\\subset\\{s, s_{1}\\}; meanings remain tied to Submodularity violation..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Submodularity violation., formal object 212.

**Formal object 213 at Submodularity violation. — Formula 213 under Submodularity violation. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, Delta, decision, under, switch, marginal, and the expression links V, s_{3}\}..** `V(\{s_{3}\})=5`
Variables: "V, s_{3}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 213 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, s_{3}\\}; meanings remain tied to Submodularity violation..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Submodularity violation., formal object 213.

**Formal object 214 at Submodularity violation. — Formula 214 under Submodularity violation. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, Delta, decision, under, switch, marginal, and the expression links V, s_{3}, s_{2}\}..** `V(\{s_{3},s_{2}\})=5`
Variables: "V, s_{3}, s_{2}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 214 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, s_{3}, s_{2}\\}; meanings remain tied to Submodularity violation..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Submodularity violation., formal object 214.

**Formal object 215 at B.2 PRISE Compression Budget and Convergence Comparison — Formula 215 under B.2 PRISE Compression Budget and Convergence Comparison is classified as a optimization objective or loss; adjacent prose centers on compression, method, define, budget, minimum, number, and the expression links hat, k, bigl, V, Xi, R, leq, bigr..** `\hat{k}\;=\;\min\bigl\{k:(V(\Xi)-V(R^{(k)}))/V(\Xi)\leq 1\%\bigr\}.`
Variables: "hat, k, bigl, V, Xi, R, leq, bigr".
Sign/normalization/conditioning/surrogate audit: "Formula 215 operator audit: minimization, fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, k, bigl, V, Xi, R, leq, bigr; meanings remain tied to B.2 PRISE Compression Budget and Convergence Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, B.2 PRISE Compression Budget and Convergence Comparison, formal object 215.

**Formal object 216 at B.2 PRISE Compression Budget and Convergence Comparison — Formula 216 under B.2 PRISE Compression Budget and Convergence Comparison is classified as a evaluation or scoring relation; adjacent prose centers on analysis, metric, Table, distinct, PRISE, internal, and the expression links epsilon..** `\epsilon`
Variables: "epsilon".
Sign/normalization/conditioning/surrogate audit: "Formula 216 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: epsilon; meanings remain tied to B.2 PRISE Compression Budget and Convergence Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, B.2 PRISE Compression Budget and Convergence Comparison, formal object 216.

**Formal object 217 at B.2 PRISE Compression Budget and Convergence Comparison — Formula 217 under B.2 PRISE Compression Budget and Convergence Comparison is classified as a evaluation or scoring relation; adjacent prose centers on analysis, metric, Table, distinct, PRISE, internal, and the expression links hat, k, Xi..** `\hat{k}/|\Xi|`
Variables: "hat, k, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 217 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, k, Xi; meanings remain tied to B.2 PRISE Compression Budget and Convergence Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, B.2 PRISE Compression Budget and Convergence Comparison, formal object 217.

**Formal object 218 at B.2 PRISE Compression Budget and Convergence Comparison — Formula 218 under B.2 PRISE Compression Budget and Convergence Comparison is classified as a optimization objective or loss; adjacent prose centers on PRISE, labeling, scenario, instances, Section, cost, and the expression links downarrow..** `\,\downarrow`
Variables: "downarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 218 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: downarrow; meanings remain tied to B.2 PRISE Compression Budget and Convergence Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, B.2 PRISE Compression Budget and Convergence Comparison, formal object 218.

**Formal object 219 at B.2 PRISE Compression Budget and Convergence Comparison — Formula 219 under B.2 PRISE Compression Budget and Convergence Comparison is classified as a optimization objective or loss; adjacent prose centers on PRISE, labeling, scenario, instances, Section, cost, and the expression links hat, k, Xi, leq..** `\hat{k}/|\Xi|\leq`
Variables: "hat, k, Xi, leq".
Sign/normalization/conditioning/surrogate audit: "Formula 219 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, k, Xi, leq; meanings remain tied to B.2 PRISE Compression Budget and Convergence Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, B.2 PRISE Compression Budget and Convergence Comparison, formal object 219.

**Formal object 220 at B.2 PRISE Compression Budget and Convergence Comparison — Formula 220 under B.2 PRISE Compression Budget and Convergence Comparison is classified as a optimization objective or loss; adjacent prose centers on PRISE, labeling, scenario, instances, Section, cost, and the expression links uparrow..** `\uparrow`
Variables: "uparrow".
Sign/normalization/conditioning/surrogate audit: "Formula 220 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: uparrow; meanings remain tied to B.2 PRISE Compression Budget and Convergence Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, B.2 PRISE Compression Budget and Convergence Comparison, formal object 220.

**Formal object 221 at Labeling cost. — Formula 221 under Labeling cost. is classified as a paper-defined mathematical relation; adjacent prose centers on PRISE, labeling, cost, wall-clock, instances, Section, and the expression links O, hat, k, S..** `O(\hat{k}{\cdot}S)`
Variables: "O, hat, k, S".
Sign/normalization/conditioning/surrogate audit: "Formula 221 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O, hat, k, S; meanings remain tied to Labeling cost..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Labeling cost., formal object 221.

**Formal object 222 at Labeling cost. — Formula 222 under Labeling cost. is classified as a paper-defined mathematical relation; adjacent prose centers on PRISE, labeling, cost, wall-clock, instances, Section, and the expression links approx..** `{\approx}`
Variables: "approx".
Sign/normalization/conditioning/surrogate audit: "Formula 222 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: approx; meanings remain tied to Labeling cost..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Labeling cost., formal object 222.

**Formal object 223 at B.3 Connection to Column-and-Constraint Generation — Formula 223 under B.3 Connection to Column-and-Constraint Generation is classified as a constraint or formal-analysis relation; adjacent prose centers on widehat, solution, star, solves, restricted, master, and the expression links V, widehat, R..** `V(\widehat{R})`
Variables: "V, widehat, R".
Sign/normalization/conditioning/surrogate audit: "Formula 223 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, widehat, R; meanings remain tied to B.3 Connection to Column-and-Constraint Generation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, B.3 Connection to Column-and-Constraint Generation, formal object 223.

**Formal object 224 at B.3 Connection to Column-and-Constraint Generation — Formula 224 under B.3 Connection to Column-and-Constraint Generation is classified as a constraint or formal-analysis relation; adjacent prose centers on widehat, solution, star, solves, restricted, master, and the expression links x, star, widehat, R..** `x^{\star}(\widehat{R})`
Variables: "x, star, widehat, R".
Sign/normalization/conditioning/surrogate audit: "Formula 224 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x, star, widehat, R; meanings remain tied to B.3 Connection to Column-and-Constraint Generation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, B.3 Connection to Column-and-Constraint Generation, formal object 224.

**Formal object 225 at B.3 Connection to Column-and-Constraint Generation — Formula 225 under B.3 Connection to Column-and-Constraint Generation is classified as a constraint or formal-analysis relation; adjacent prose centers on widehat, solution, star, solves, restricted, master, and the expression links xi, mathrm, in, Xi, Q, x, star, widehat..** `\xi^{\mathrm{CCG}}\in\arg\max_{\xi\in\Xi}Q(x^{\star}(\widehat{R}),\xi)`
Variables: "xi, mathrm, in, Xi, Q, x, star, widehat, R".
Sign/normalization/conditioning/surrogate audit: "Formula 225 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, mathrm, in, Xi, Q, x, star, widehat, R; meanings remain tied to B.3 Connection to Column-and-Constraint Generation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, B.3 Connection to Column-and-Constraint Generation, formal object 225.

**Formal object 226 at C.1 Deterministic-Equivalent MILP Reformulation — Formula 226 under C.1 Deterministic-Equivalent MILP Reformulation is classified as a constraint or formal-analysis relation; adjacent prose centers on scenario, MILP, recourse, reduced, deterministic-equivalent, reformulation, and the expression links displaystyle, x, eta, y, s..** `\displaystyle\min_{x,\,\eta,\,\{y^{(s)}\}}`
Variables: "displaystyle, x, eta, y, s".
Sign/normalization/conditioning/surrogate audit: "Formula 226 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, x, eta, y, s; meanings remain tied to C.1 Deterministic-Equivalent MILP Reformulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, C.1 Deterministic-Equivalent MILP Reformulation, formal object 226.

**Formal object 227 at C.1 Deterministic-Equivalent MILP Reformulation — Formula 227 under C.1 Deterministic-Equivalent MILP Reformulation is classified as a constraint or formal-analysis relation; adjacent prose centers on scenario, MILP, recourse, reduced, deterministic-equivalent, reformulation, and the expression links displaystyle, c, top, x, eta..** `\displaystyle c^{\top}x+\eta`
Variables: "displaystyle, c, top, x, eta".
Sign/normalization/conditioning/surrogate audit: "Formula 227 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, c, top, x, eta; meanings remain tied to C.1 Deterministic-Equivalent MILP Reformulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, C.1 Deterministic-Equivalent MILP Reformulation, formal object 227.

**Formal object 228 at C.1 Deterministic-Equivalent MILP Reformulation — Formula 228 under C.1 Deterministic-Equivalent MILP Reformulation is classified as a constraint or formal-analysis relation; adjacent prose centers on scenario, MILP, recourse, reduced, deterministic-equivalent, reformulation, and the expression links displaystyle, eta, geq, b_{\xi, s, top, y, quad..** `\displaystyle\eta\geq b_{\xi_{s}}^{\top}y^{(s)},\quad\forall\xi_{s}\in\Xi,`
Variables: "displaystyle, eta, geq, b_{\\xi, s, top, y, quad, forall, xi, in, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 228 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, eta, geq, b_{\\xi, s, top, y, quad, forall, xi, in, Xi; meanings remain tied to C.1 Deterministic-Equivalent MILP Reformulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, C.1 Deterministic-Equivalent MILP Reformulation, formal object 228.

**Formal object 229 at C.1 Deterministic-Equivalent MILP Reformulation — Formula 229 under C.1 Deterministic-Equivalent MILP Reformulation is classified as a constraint or formal-analysis relation; adjacent prose centers on scenario, MILP, recourse, reduced, deterministic-equivalent, reformulation, and the expression links displaystyle, s, geq, h, M, xi, quad, forall..** `\displaystyle Gy^{(s)}\geq h-Ex-M\xi_{s},\quad\forall\xi_{s}\in\Xi,`
Variables: "displaystyle, s, geq, h, M, xi, quad, forall, in, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 229 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, s, geq, h, M, xi, quad, forall, in, Xi; meanings remain tied to C.1 Deterministic-Equivalent MILP Reformulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, C.1 Deterministic-Equivalent MILP Reformulation, formal object 229.

**Formal object 230 at C.1 Deterministic-Equivalent MILP Reformulation — Formula 230 under C.1 Deterministic-Equivalent MILP Reformulation is classified as a constraint or formal-analysis relation; adjacent prose centers on scenario, MILP, recourse, reduced, deterministic-equivalent, reformulation, and the expression links displaystyle, x, in, X, y, s, Y, eta..** `\displaystyle x\in X,\;y^{(s)}\in Y,\;\eta\in\mathbb{R},`
Variables: "displaystyle, x, in, X, y, s, Y, eta, mathbb, R".
Sign/normalization/conditioning/surrogate audit: "Formula 230 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, x, in, X, y, s, Y, eta, mathbb, R; meanings remain tied to C.1 Deterministic-Equivalent MILP Reformulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, C.1 Deterministic-Equivalent MILP Reformulation, formal object 230.

**Formal object 231 at C.1 Deterministic-Equivalent MILP Reformulation — Formula 231 under C.1 Deterministic-Equivalent MILP Reformulation is classified as a paper-defined mathematical relation; adjacent prose centers on scenario, reduced, where, recourse, decision, Given, and the expression links y, s..** `y^{(s)}`
Variables: "y, s".
Sign/normalization/conditioning/surrogate audit: "Formula 231 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y, s; meanings remain tied to C.1 Deterministic-Equivalent MILP Reformulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, C.1 Deterministic-Equivalent MILP Reformulation, formal object 231.

**Formal object 232 at C.1 Deterministic-Equivalent MILP Reformulation — Formula 232 under C.1 Deterministic-Equivalent MILP Reformulation is classified as a paper-defined mathematical relation; adjacent prose centers on scenario, reduced, where, recourse, decision, Given, and the expression links xi, s..** `\xi_{s}`
Variables: "xi, s".
Sign/normalization/conditioning/surrogate audit: "Formula 232 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: xi, s; meanings remain tied to C.1 Deterministic-Equivalent MILP Reformulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, C.1 Deterministic-Equivalent MILP Reformulation, formal object 232.

**Formal object 233 at C.1 Deterministic-Equivalent MILP Reformulation — Formula 233 under C.1 Deterministic-Equivalent MILP Reformulation is classified as a paper-defined mathematical relation; adjacent prose centers on scenario, reduced, where, recourse, decision, Given, and the expression links R, k, subseteq, Xi..** `R^{(k)}\subseteq\Xi`
Variables: "R, k, subseteq, Xi".
Sign/normalization/conditioning/surrogate audit: "Formula 233 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, k, subseteq, Xi; meanings remain tied to C.1 Deterministic-Equivalent MILP Reformulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, C.1 Deterministic-Equivalent MILP Reformulation, formal object 233.

**Formal object 234 at C.1 Deterministic-Equivalent MILP Reformulation — Formula 234 under C.1 Deterministic-Equivalent MILP Reformulation is classified as a paper-defined mathematical relation; adjacent prose centers on scenario, reduced, where, recourse, decision, Given, and the expression links R, k, ll, S..** `|R^{(k)}|=k\ll S`
Variables: "R, k, ll, S".
Sign/normalization/conditioning/surrogate audit: "Formula 234 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: R, k, ll, S; meanings remain tied to C.1 Deterministic-Equivalent MILP Reformulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, C.1 Deterministic-Equivalent MILP Reformulation, formal object 234.

**Formal object 235 at Selection Problem (SEL). — Formula 235 under Selection Problem (SEL). is classified as a optimization objective or loss; adjacent prose centers on selection, cost, decisions, costs, size, items, and the expression links lfloor, n, rfloor..** `\lfloor n/2\rfloor`
Variables: "lfloor, n, rfloor".
Sign/normalization/conditioning/surrogate audit: "Formula 235 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: lfloor, n, rfloor; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 235.

**Formal object 236 at Selection Problem (SEL). — Formula 236 under Selection Problem (SEL). is classified as a optimization objective or loss; adjacent prose centers on selection, cost, decisions, costs, size, items, and the expression links dots..** `\{1,\dots,100\}`
Variables: "dots".
Sign/normalization/conditioning/surrogate audit: "Formula 236 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: dots; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 236.

**Formal object 237 at Selection Problem (SEL). — Formula 237 under Selection Problem (SEL). is classified as a paper-defined mathematical relation; adjacent prose centers on scenario, cost, Given, items, dots, first-stage, and the expression links c_{i}..** `c_{i}`
Variables: "c_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 237 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c_{i}; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 237.

**Formal object 238 at Selection Problem (SEL). — Formula 238 under Selection Problem (SEL). is classified as a paper-defined mathematical relation; adjacent prose centers on scenario, cost, Given, items, dots, first-stage, and the expression links d_{i}^{, s..** `d_{i}^{(s)}`
Variables: "d_{i}^{, s".
Sign/normalization/conditioning/surrogate audit: "Formula 238 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{i}^{, s; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 238.

**Formal object 239 at Selection Problem (SEL). — Formula 239 under Selection Problem (SEL). is classified as a paper-defined mathematical relation; adjacent prose centers on scenario, cost, Given, items, dots, first-stage, and the expression links i..** `i`
Variables: "i".
Sign/normalization/conditioning/surrogate audit: "Formula 239 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: i; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 239.

**Formal object 240 at Selection Problem (SEL). — Formula 240 under Selection Problem (SEL). is classified as a probabilistic or expectation relation; adjacent prose centers on scenario, costs, Given, dots, first-stage, cost, and the expression links displaystyle, textstyle, i, n, c_{i}\, x_{i}, eta..** `\displaystyle\textstyle\sum_{i=1}^{n}c_{i}\,x_{i}+\eta`
Variables: "displaystyle, textstyle, i, n, c_{i}\\, x_{i}, eta".
Sign/normalization/conditioning/surrogate audit: "Formula 240 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, textstyle, i, n, c_{i}\\, x_{i}, eta; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 240.

**Formal object 241 at Selection Problem (SEL). — Formula 241 under Selection Problem (SEL). is classified as a probabilistic or expectation relation; adjacent prose centers on scenario, costs, Given, dots, first-stage, cost, and the expression links displaystyle, eta, geq, textstyle, i, n, d_{i}^{, s..** `\displaystyle\eta\geq\textstyle\sum_{i=1}^{n}d_{i}^{(s)}\,y_{i}^{(s)},`
Variables: "displaystyle, eta, geq, textstyle, i, n, d_{i}^{, s, y_{i}^{".
Sign/normalization/conditioning/surrogate audit: "Formula 241 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, eta, geq, textstyle, i, n, d_{i}^{, s, y_{i}^{; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 241.

**Formal object 242 at Selection Problem (SEL). — Formula 242 under Selection Problem (SEL). is classified as a probabilistic or expectation relation; adjacent prose centers on scenario, costs, Given, dots, first-stage, cost, and the expression links displaystyle, forall, s, in, S..** `\displaystyle\forall s\in[S],`
Variables: "displaystyle, forall, s, in, S".
Sign/normalization/conditioning/surrogate audit: "Formula 242 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, forall, s, in, S; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 242.

**Formal object 243 at Selection Problem (SEL). — Formula 243 under Selection Problem (SEL). is classified as a probabilistic or expectation relation; adjacent prose centers on scenario, costs, Given, dots, first-stage, cost, and the expression links displaystyle, textstyle, i, n, bigl, x_{i}, y_{i}^{, s..** `\displaystyle\textstyle\sum_{i=1}^{n}\bigl(x_{i}+y_{i}^{(s)}\bigr)=\lfloor n/2\rfloor,`
Variables: "displaystyle, textstyle, i, n, bigl, x_{i}, y_{i}^{, s, bigr, lfloor, rfloor".
Sign/normalization/conditioning/surrogate audit: "Formula 243 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, textstyle, i, n, bigl, x_{i}, y_{i}^{, s, bigr, lfloor, rfloor; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 243.

**Formal object 244 at Selection Problem (SEL). — Formula 244 under Selection Problem (SEL). is classified as a probabilistic or expectation relation; adjacent prose centers on scenario, costs, Given, dots, first-stage, cost, and the expression links displaystyle, x_{i}, y_{i}^{, s, leq..** `\displaystyle x_{i}+y_{i}^{(s)}\leq 1,`
Variables: "displaystyle, x_{i}, y_{i}^{, s, leq".
Sign/normalization/conditioning/surrogate audit: "Formula 244 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, x_{i}, y_{i}^{, s, leq; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 244.

**Formal object 245 at Selection Problem (SEL). — Formula 245 under Selection Problem (SEL). is classified as a probabilistic or expectation relation; adjacent prose centers on scenario, costs, Given, dots, first-stage, cost, and the expression links displaystyle, forall, i, in, n, s, S..** `\displaystyle\forall i\in[n],\;\forall s\in[S],`
Variables: "displaystyle, forall, i, in, n, s, S".
Sign/normalization/conditioning/surrogate audit: "Formula 245 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, forall, i, in, n, s, S; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 245.

**Formal object 246 at Selection Problem (SEL). — Formula 246 under Selection Problem (SEL). is classified as a probabilistic or expectation relation; adjacent prose centers on scenario, costs, Given, dots, first-stage, cost, and the expression links displaystyle, x_{i}, y_{i}^{, s, in..** `\displaystyle x_{i},\,y_{i}^{(s)}\in\{0,1\}.`
Variables: "displaystyle, x_{i}, y_{i}^{, s, in".
Sign/normalization/conditioning/surrogate audit: "Formula 246 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, x_{i}, y_{i}^{, s, in; meanings remain tied to Selection Problem (SEL)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL)., formal object 246.

**Formal object 247 at Vertex Cover (VC). — Formula 247 under Vertex Cover (VC). is classified as a probabilistic or expectation relation; adjacent prose centers on costs, nodes, edge., Given, graph, uncertain, and the expression links G, V, E..** `G=(V,E)`
Variables: "G, V, E".
Sign/normalization/conditioning/surrogate audit: "Formula 247 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G, V, E; meanings remain tied to Vertex Cover (VC)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Vertex Cover (VC)., formal object 247.

**Formal object 248 at Vertex Cover (VC). — Formula 248 under Vertex Cover (VC). is classified as a probabilistic or expectation relation; adjacent prose centers on costs, nodes, edge., Given, graph, uncertain, and the expression links n..** `10/n`
Variables: "n".
Sign/normalization/conditioning/surrogate audit: "Formula 248 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: n; meanings remain tied to Vertex Cover (VC)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Vertex Cover (VC)., formal object 248.

**Formal object 249 at Vertex Cover (VC). — Formula 249 under Vertex Cover (VC). is classified as a probabilistic or expectation relation; adjacent prose centers on costs, nodes, edge., Given, graph, uncertain, and the expression links approx..** `\approx 10`
Variables: "approx".
Sign/normalization/conditioning/surrogate audit: "Formula 249 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: approx; meanings remain tied to Vertex Cover (VC)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Vertex Cover (VC)., formal object 249.

**Formal object 250 at Vertex Cover (VC). — Formula 250 under Vertex Cover (VC). is classified as a constraint or formal-analysis relation; adjacent prose centers on costs, node, bipartite, graph, denotes, constraint, and the expression links displaystyle, textstyle, i, in, V, c_{i}\, x_{i}, eta..** `\displaystyle\textstyle\sum_{i\in V}c_{i}\,x_{i}+\eta`
Variables: "displaystyle, textstyle, i, in, V, c_{i}\\, x_{i}, eta".
Sign/normalization/conditioning/surrogate audit: "Formula 250 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, textstyle, i, in, V, c_{i}\\, x_{i}, eta; meanings remain tied to Vertex Cover (VC)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Vertex Cover (VC)., formal object 250.

**Formal object 251 at Vertex Cover (VC). — Formula 251 under Vertex Cover (VC). is classified as a constraint or formal-analysis relation; adjacent prose centers on costs, node, bipartite, graph, denotes, constraint, and the expression links displaystyle, eta, geq, textstyle, i, in, V, d_{i}^{..** `\displaystyle\eta\geq\textstyle\sum_{i\in V}d_{i}^{(s)}\,y_{i}^{(s)},`
Variables: "displaystyle, eta, geq, textstyle, i, in, V, d_{i}^{, s, y_{i}^{".
Sign/normalization/conditioning/surrogate audit: "Formula 251 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, eta, geq, textstyle, i, in, V, d_{i}^{, s, y_{i}^{; meanings remain tied to Vertex Cover (VC)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Vertex Cover (VC)., formal object 251.

**Formal object 252 at Vertex Cover (VC). — Formula 252 under Vertex Cover (VC). is classified as a constraint or formal-analysis relation; adjacent prose centers on costs, node, bipartite, graph, denotes, constraint, and the expression links displaystyle, x_{i}, y_{i}^{, s, x_{j}, y_{j}^{, geq..** `\displaystyle(x_{i}+y_{i}^{(s)})+(x_{j}+y_{j}^{(s)})\geq 1,`
Variables: "displaystyle, x_{i}, y_{i}^{, s, x_{j}, y_{j}^{, geq".
Sign/normalization/conditioning/surrogate audit: "Formula 252 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, x_{i}, y_{i}^{, s, x_{j}, y_{j}^{, geq; meanings remain tied to Vertex Cover (VC)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Vertex Cover (VC)., formal object 252.

**Formal object 253 at Vertex Cover (VC). — Formula 253 under Vertex Cover (VC). is classified as a constraint or formal-analysis relation; adjacent prose centers on costs, node, bipartite, graph, denotes, constraint, and the expression links displaystyle, forall, i, j, in, E, s, S..** `\displaystyle\forall(i,j)\in E,\;\forall s\in[S],`
Variables: "displaystyle, forall, i, j, in, E, s, S".
Sign/normalization/conditioning/surrogate audit: "Formula 253 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, forall, i, j, in, E, s, S; meanings remain tied to Vertex Cover (VC)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Vertex Cover (VC)., formal object 253.

**Formal object 254 at Vertex Cover (VC). — Formula 254 under Vertex Cover (VC). is classified as a constraint or formal-analysis relation; adjacent prose centers on costs, node, bipartite, graph, denotes, constraint, and the expression links displaystyle, y_{i}^{, s, leq, x_{i}..** `\displaystyle y_{i}^{(s)}\leq 1-x_{i},`
Variables: "displaystyle, y_{i}^{, s, leq, x_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 254 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, y_{i}^{, s, leq, x_{i}; meanings remain tied to Vertex Cover (VC)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Vertex Cover (VC)., formal object 254.

**Formal object 255 at Vertex Cover (VC). — Formula 255 under Vertex Cover (VC). is classified as a constraint or formal-analysis relation; adjacent prose centers on costs, node, bipartite, graph, denotes, constraint, and the expression links displaystyle, forall, i, in, V, s, S..** `\displaystyle\forall i\in V,\;\forall s\in[S],`
Variables: "displaystyle, forall, i, in, V, s, S".
Sign/normalization/conditioning/surrogate audit: "Formula 255 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, forall, i, in, V, s, S; meanings remain tied to Vertex Cover (VC)..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Vertex Cover (VC)., formal object 255.

**Formal object 256 at D.1.1 Bipartite Graph Representation — Formula 256 under D.1.1 Bipartite Graph Representation is classified as a state or representation transformation; adjacent prose centers on bipartite, graph, denotes, constraint, nodes, variable, and the expression links G_{j}, V_{c}\cup, V_{v}, E..** `G_{j}=(V_{c}\cup V_{v},E)`
Variables: "G_{j}, V_{c}\\cup, V_{v}, E".
Sign/normalization/conditioning/surrogate audit: "Formula 256 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G_{j}, V_{c}\\cup, V_{v}, E; meanings remain tied to D.1.1 Bipartite Graph Representation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.1 Bipartite Graph Representation, formal object 256.

**Formal object 257 at D.1.1 Bipartite Graph Representation — Formula 257 under D.1.1 Bipartite Graph Representation is classified as a state or representation transformation; adjacent prose centers on bipartite, graph, denotes, constraint, nodes, variable, and the expression links V_{c}..** `V_{c}`
Variables: "V_{c}".
Sign/normalization/conditioning/surrogate audit: "Formula 257 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V_{c}; meanings remain tied to D.1.1 Bipartite Graph Representation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.1 Bipartite Graph Representation, formal object 257.

**Formal object 258 at D.1.1 Bipartite Graph Representation — Formula 258 under D.1.1 Bipartite Graph Representation is classified as a state or representation transformation; adjacent prose centers on bipartite, graph, denotes, constraint, nodes, variable, and the expression links V_{v}..** `V_{v}`
Variables: "V_{v}".
Sign/normalization/conditioning/surrogate audit: "Formula 258 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V_{v}; meanings remain tied to D.1.1 Bipartite Graph Representation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.1 Bipartite Graph Representation, formal object 258.

**Formal object 259 at D.1.2 GINE Architecture — Formula 259 under D.1.2 GINE Architecture is classified as a state or representation transformation; adjacent prose centers on employ, Graph, Isomorphism, Network, edge, features, and the expression links ell..** `\ell`
Variables: "ell".
Sign/normalization/conditioning/surrogate audit: "Formula 259 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: ell; meanings remain tied to D.1.2 GINE Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.2 GINE Architecture, formal object 259.

**Formal object 260 at D.1.2 GINE Architecture — Formula 260 under D.1.2 GINE Architecture is classified as a state or representation transformation; adjacent prose centers on Graph, edge, GINE, node, mathbf, employ, and the expression links mathbf, g, i, ell, mathrm, left, epsilon, j..** `\mathbf{g}_{i}^{(\ell+1)}=\mathrm{MLP}^{(\ell)}\!\left((1+\epsilon^{(\ell)})\cdot\mathbf{g}_{i}^{(\ell)}+\sum_{j\in\mathcal{N}(i)}\mathrm{ReLU}\!\left(\mathbf{g}_{j}^{(\ell)}+\mathbf{e}_{ji}\right)\right),`
Variables: "mathbf, g, i, ell, mathrm, left, epsilon, j, in, mathcal, N, e, right".
Sign/normalization/conditioning/surrogate audit: "Formula 260 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, g, i, ell, mathrm, left, epsilon, j, in, mathcal, N, e, right; meanings remain tied to D.1.2 GINE Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.2 GINE Architecture, formal object 260.

**Formal object 261 at D.1.2 GINE Architecture — Formula 261 under D.1.2 GINE Architecture is classified as a state or representation transformation; adjacent prose centers on mathbf, where, edge, feature, constraint, coefficient, and the expression links mathbf, e..** `\mathbf{e}_{ji}`
Variables: "mathbf, e".
Sign/normalization/conditioning/surrogate audit: "Formula 261 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, e; meanings remain tied to D.1.2 GINE Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.2 GINE Architecture, formal object 261.

**Formal object 262 at D.1.2 GINE Architecture — Formula 262 under D.1.2 GINE Architecture is classified as a state or representation transformation; adjacent prose centers on mathbf, where, edge, feature, constraint, coefficient, and the expression links epsilon, ell..** `\epsilon^{(\ell)}`
Variables: "epsilon, ell".
Sign/normalization/conditioning/surrogate audit: "Formula 262 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: epsilon, ell; meanings remain tied to D.1.2 GINE Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.2 GINE Architecture, formal object 262.

**Formal object 263 at D.1.2 GINE Architecture — Formula 263 under D.1.2 GINE Architecture is classified as a state or representation transformation; adjacent prose centers on mathbf, where, edge, feature, constraint, coefficient, and the expression links mathbf, h, j, in, mathbb, R, d_{s}}..** `\mathbf{h}_{j}\in\mathbb{R}^{d_{s}}`
Variables: "mathbf, h, j, in, mathbb, R, d_{s}}".
Sign/normalization/conditioning/surrogate audit: "Formula 263 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, h, j, in, mathbb, R, d_{s}}; meanings remain tied to D.1.2 GINE Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.2 GINE Architecture, formal object 263.

**Formal object 264 at D.1.3 Problem-Specific Feature Engineering — Formula 264 under D.1.3 Problem-Specific Feature Engineering is classified as a optimization objective or loss; adjacent prose centers on constraint, edge, coefficient, node, features, include, and the expression links d_{\text{node}}..** `d_{\text{node}}`
Variables: "d_{\\text{node}}".
Sign/normalization/conditioning/surrogate audit: "Formula 264 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{\\text{node}}; meanings remain tied to D.1.3 Problem-Specific Feature Engineering.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.3 Problem-Specific Feature Engineering, formal object 264.

**Formal object 265 at D.1.3 Problem-Specific Feature Engineering — Formula 265 under D.1.3 Problem-Specific Feature Engineering is classified as a optimization objective or loss; adjacent prose centers on constraint, edge, coefficient, node, features, include, and the expression links d_{\text{edge}}..** `d_{\text{edge}}`
Variables: "d_{\\text{edge}}".
Sign/normalization/conditioning/surrogate audit: "Formula 265 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{\\text{edge}}; meanings remain tied to D.1.3 Problem-Specific Feature Engineering.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.3 Problem-Specific Feature Engineering, formal object 265.

**Formal object 266 at D.1.3 Problem-Specific Feature Engineering — Formula 266 under D.1.3 Problem-Specific Feature Engineering is classified as a optimization objective or loss; adjacent prose centers on constraint, edge, coefficient, node, features, include, and the expression links times..** `\times 4`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 266 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to D.1.3 Problem-Specific Feature Engineering.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, D.1.3 Problem-Specific Feature Engineering, formal object 266.

**Formal object 267 at Feature Engineering. — Formula 267 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links y..** `y`
Variables: "y".
Sign/normalization/conditioning/surrogate audit: "Formula 267 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 267.

**Formal object 268 at Feature Engineering. — Formula 268 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links eta..** `\eta`
Variables: "eta".
Sign/normalization/conditioning/surrogate audit: "Formula 268 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: eta; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 268.

**Formal object 269 at Feature Engineering. — Formula 269 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links G, s..** `G^{(s)}`
Variables: "G, s".
Sign/normalization/conditioning/surrogate audit: "Formula 269 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G, s; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 269.

**Formal object 270 at Feature Engineering. — Formula 270 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links x_{1}..** `x_{1}`
Variables: "x_{1}".
Sign/normalization/conditioning/surrogate audit: "Formula 270 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x_{1}; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 270.

**Formal object 271 at Feature Engineering. — Formula 271 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links x_{2}..** `x_{2}`
Variables: "x_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 271 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x_{2}; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 271.

**Formal object 272 at Feature Engineering. — Formula 272 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links vdots..** `\vdots`
Variables: "vdots".
Sign/normalization/conditioning/surrogate audit: "Formula 272 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: vdots; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 272.

**Formal object 273 at Feature Engineering. — Formula 273 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links x_{n}..** `x_{n}`
Variables: "x_{n}".
Sign/normalization/conditioning/surrogate audit: "Formula 273 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x_{n}; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 273.

**Formal object 274 at Feature Engineering. — Formula 274 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links y_{1}..** `y_{1}`
Variables: "y_{1}".
Sign/normalization/conditioning/surrogate audit: "Formula 274 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{1}; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 274.

**Formal object 275 at Feature Engineering. — Formula 275 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links y_{n}..** `y_{n}`
Variables: "y_{n}".
Sign/normalization/conditioning/surrogate audit: "Formula 275 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{n}; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 275.

**Formal object 276 at Feature Engineering. — Formula 276 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links mathrm, c_{i}..** `[\mathrm{type},\,c_{i},\,0]`
Variables: "mathrm, c_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 276 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm, c_{i}; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 276.

**Formal object 277 at Feature Engineering. — Formula 277 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links mathrm, d_{i}^{, s..** `[\mathrm{type},\,0,\,d_{i}^{(s)}]`
Variables: "mathrm, d_{i}^{, s".
Sign/normalization/conditioning/surrogate audit: "Formula 277 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm, d_{i}^{, s; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 277.

**Formal object 278 at Feature Engineering. — Formula 278 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links c_{1}..** `c_{1}`
Variables: "c_{1}".
Sign/normalization/conditioning/surrogate audit: "Formula 278 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c_{1}; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 278.

**Formal object 279 at Feature Engineering. — Formula 279 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links c_{2}..** `c_{2}`
Variables: "c_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 279 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c_{2}; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 279.

**Formal object 280 at Feature Engineering. — Formula 280 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links c_{m}..** `c_{m}`
Variables: "c_{m}".
Sign/normalization/conditioning/surrogate audit: "Formula 280 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c_{m}; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 280.

**Formal object 281 at Feature Engineering. — Formula 281 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links mathrm..** `[\mathrm{type},\,\mathrm{rhs},\,\mathrm{sim}]`
Variables: "mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 281 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 281.

**Formal object 282 at Feature Engineering. — Formula 282 under Feature Engineering. is classified as a optimization objective or loss; adjacent prose centers on features, include, Constraint, Variable, node, cost, and the expression links A_{ji}..** `A_{ji}`
Variables: "A_{ji}".
Sign/normalization/conditioning/surrogate audit: "Formula 282 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: A_{ji}; meanings remain tied to Feature Engineering..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Feature Engineering., formal object 282.

**Formal object 283 at Input normalization. — Formula 283 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, deterministic, first-stage, vector, scenario-dependent, second-stage, and the expression links D, d, dots, S..** `D=[d^{(1)},\dots,d^{(S)}]`
Variables: "D, d, dots, S".
Sign/normalization/conditioning/surrogate audit: "Formula 283 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: D, d, dots, S; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 283.

**Formal object 284 at Input normalization. — Formula 284 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, second-stage, costs, shared, denominator, deterministic, and the expression links d..** `d`
Variables: "d".
Sign/normalization/conditioning/surrogate audit: "Formula 284 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 284.

**Formal object 285 at Input normalization. — Formula 285 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, second-stage, costs, shared, denominator, deterministic, and the expression links H, to..** `H\to 4H\to 1`
Variables: "H, to".
Sign/normalization/conditioning/surrogate audit: "Formula 285 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: H, to; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 285.

**Formal object 286 at Input normalization. — Formula 286 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, second-stage, costs, shared, denominator, deterministic, and the expression links times..** `6\times 10^{-4}`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 286 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 286.

**Formal object 287 at Input normalization. — Formula 287 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, second-stage, costs, shared, denominator, deterministic, and the expression links symbols defined beside the formula..** `10^{-2}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 287 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 287.

**Formal object 288 at Input normalization. — Formula 288 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, second-stage, costs, shared, denominator, deterministic, and the expression links Delta..** `\log(1+\Delta)`
Variables: "Delta".
Sign/normalization/conditioning/surrogate audit: "Formula 288 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 288.

**Formal object 289 at Input normalization. — Formula 289 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on cost, second-stage, costs, shared, denominator, deterministic, and the expression links tilde, c, mathrm, D, infty, epsilon, qquad..** `\tilde{c}=\frac{c}{\|[c;\,\mathrm{vec}(D)]\|_{\infty}+\epsilon},\qquad\tilde{D}=\frac{D}{\|[c;\,\mathrm{vec}(D)]\|_{\infty}+\epsilon},`
Variables: "tilde, c, mathrm, D, infty, epsilon, qquad".
Sign/normalization/conditioning/surrogate audit: "Formula 289 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tilde, c, mathrm, D, infty, epsilon, qquad; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 289.

**Formal object 290 at Input normalization. — Formula 290 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on where, epsilon, avoids, division, zero., shared, and the expression links epsilon..** `\epsilon=10^{-8}`
Variables: "epsilon".
Sign/normalization/conditioning/surrogate audit: "Formula 290 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: epsilon; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 290.

**Formal object 291 at Motivation and setup. — Formula 291 under Motivation and setup. is classified as a probabilistic or expectation relation; adjacent prose centers on Uniform, mathrm, clip, sigma_, Normal., Per-node, and the expression links mu, v, sim, mathrm..** `\mu_{v}\sim\mathrm{Uniform}[25,75]`
Variables: "mu, v, sim, mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 291 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mu, v, sim, mathrm; meanings remain tied to Motivation and setup..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Motivation and setup., formal object 291.

**Formal object 292 at Motivation and setup. — Formula 292 under Motivation and setup. is classified as a probabilistic or expectation relation; adjacent prose centers on Uniform, mathrm, clip, sigma_, Normal., Per-node, and the expression links sigma, v, mathrm, mu..** `\sigma_{v}=\mathrm{clip}(0.15\,\mu_{v},\,3,\,15)`
Variables: "sigma, v, mathrm, mu".
Sign/normalization/conditioning/surrogate audit: "Formula 292 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sigma, v, mathrm, mu; meanings remain tied to Motivation and setup..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Motivation and setup., formal object 292.

**Formal object 293 at Motivation and setup. — Formula 293 under Motivation and setup. is classified as a probabilistic or expectation relation; adjacent prose centers on Uniform, mathrm, clip, sigma_, Normal., Per-node, and the expression links mathcal, N, mu, v, sigma..** `\mathcal{N}(\mu_{v},\sigma_{v})`
Variables: "mathcal, N, mu, v, sigma".
Sign/normalization/conditioning/surrogate audit: "Formula 293 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, N, mu, v, sigma; meanings remain tied to Motivation and setup..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Motivation and setup., formal object 293.

**Formal object 294 at Motivation and setup. — Formula 294 under Motivation and setup. is classified as a probabilistic or expectation relation; adjacent prose centers on Uniform, mathrm, clip, sigma_, Normal., Per-node, and the expression links symbols defined beside the formula..** `[1,100]`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 294 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Motivation and setup..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Motivation and setup., formal object 294.

**Formal object 295 at Motivation and setup. — Formula 295 under Motivation and setup. is classified as a paper-defined mathematical relation; adjacent prose centers on delta_, Uniform, mode, uniformly., Multimodal, Following, and the expression links K, sim, mathrm, dots..** `K\sim\mathrm{Uniform}\{3,\dots,8\}`
Variables: "K, sim, mathrm, dots".
Sign/normalization/conditioning/surrogate audit: "Formula 295 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K, sim, mathrm, dots; meanings remain tied to Motivation and setup..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Motivation and setup., formal object 295.

**Formal object 296 at Motivation and setup. — Formula 296 under Motivation and setup. is classified as a paper-defined mathematical relation; adjacent prose centers on delta_, Uniform, mode, uniformly., Multimodal, Following, and the expression links k, in, K..** `k\in[K]`
Variables: "k, in, K".
Sign/normalization/conditioning/surrogate audit: "Formula 296 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k, in, K; meanings remain tied to Motivation and setup..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Motivation and setup., formal object 296.

**Formal object 297 at Motivation and setup. — Formula 297 under Motivation and setup. is classified as a paper-defined mathematical relation; adjacent prose centers on delta_, Uniform, mode, uniformly., Multimodal, Following, and the expression links mu, k, in..** `\mu_{k}\in[25,75]`
Variables: "mu, k, in".
Sign/normalization/conditioning/surrogate audit: "Formula 297 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mu, k, in; meanings remain tied to Motivation and setup..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Motivation and setup., formal object 297.

**Formal object 298 at Motivation and setup. — Formula 298 under Motivation and setup. is classified as a paper-defined mathematical relation; adjacent prose centers on delta_, Uniform, mode, uniformly., Multimodal, Following, and the expression links delta, k, in..** `\delta_{k}\in[0.1,0.5]`
Variables: "delta, k, in".
Sign/normalization/conditioning/surrogate audit: "Formula 298 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: delta, k, in; meanings remain tied to Motivation and setup..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Motivation and setup., formal object 298.

**Formal object 299 at Motivation and setup. — Formula 299 under Motivation and setup. is classified as a paper-defined mathematical relation; adjacent prose centers on delta_, Uniform, mode, uniformly., Multimodal, Following, and the expression links delta, k, mu..** `[(1{-}\delta_{k})\mu_{k},\,(1{+}\delta_{k})\mu_{k}]`
Variables: "delta, k, mu".
Sign/normalization/conditioning/surrogate audit: "Formula 299 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: delta, k, mu; meanings remain tied to Motivation and setup..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Motivation and setup., formal object 299.

**Formal object 300 at E.1.2 Do We Need Target-Scale Training? — Formula 300 under E.1.2 Do We Need Target-Scale Training? is classified as a paper-defined mathematical relation; adjacent prose centers on training-set, model, advantage, instances, size, regret, and the expression links symbols defined beside the formula..** `2{,}000`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 300 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to E.1.2 Do We Need Target-Scale Training?.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.1.2 Do We Need Target-Scale Training?, formal object 300.

**Formal object 301 at E.1.2 Do We Need Target-Scale Training? — Formula 301 under E.1.2 Do We Need Target-Scale Training? is classified as a paper-defined mathematical relation; adjacent prose centers on training-set, model, advantage, instances, size, regret, and the expression links symbols defined beside the formula..** `400`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 301 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to E.1.2 Do We Need Target-Scale Training?.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.1.2 Do We Need Target-Scale Training?, formal object 301.

**Formal object 302 at E.1.2 Do We Need Target-Scale Training? — Formula 302 under E.1.2 Do We Need Target-Scale Training? is classified as a paper-defined mathematical relation; adjacent prose centers on training-set, model, advantage, instances, size, regret, and the expression links N, in..** `N\in\{500,1500,2500\}`
Variables: "N, in".
Sign/normalization/conditioning/surrogate audit: "Formula 302 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N, in; meanings remain tied to E.1.2 Do We Need Target-Scale Training?.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.1.2 Do We Need Target-Scale Training?, formal object 302.

**Formal object 303 at E.1.2 Do We Need Target-Scale Training? — Formula 303 under E.1.2 Do We Need Target-Scale Training? is classified as a paper-defined mathematical relation; adjacent prose centers on training-set, model, advantage, instances, size, regret, and the expression links N..** `N{=}1{,}500`
Variables: "N".
Sign/normalization/conditioning/surrogate audit: "Formula 303 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N; meanings remain tied to E.1.2 Do We Need Target-Scale Training?.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.1.2 Do We Need Target-Scale Training?, formal object 303.

**Formal object 304 at E.1.2 Do We Need Target-Scale Training? — Formula 304 under E.1.2 Do We Need Target-Scale Training? is classified as a paper-defined mathematical relation; adjacent prose centers on training-set, model, advantage, instances, size, regret, and the expression links N..** `N{=}500`
Variables: "N".
Sign/normalization/conditioning/surrogate audit: "Formula 304 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N; meanings remain tied to E.1.2 Do We Need Target-Scale Training?.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.1.2 Do We Need Target-Scale Training?, formal object 304.

**Formal object 305 at E.2 Seed Variance Analysis — Formula 305 under E.2 Seed Variance Analysis is classified as a paper-defined mathematical relation; adjacent prose centers on training, assess, sensitivity, stochasticity, train, default, and the expression links symbols defined beside the formula..** `\{1,2,3,4,42\}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 305 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to E.2 Seed Variance Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.2 Seed Variance Analysis, formal object 305.

**Formal object 306 at E.2 Seed Variance Analysis — Formula 306 under E.2 Seed Variance Analysis is classified as a paper-defined mathematical relation; adjacent prose centers on training, NeurPRISE, assess, sensitivity, stochasticity, train, and the expression links pm..** `\pm`
Variables: "pm".
Sign/normalization/conditioning/surrogate audit: "Formula 306 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: pm; meanings remain tied to E.2 Seed Variance Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.2 Seed Variance Analysis, formal object 306.

**Formal object 307 at E.3 Time-Budgeted Exact Solver Comparison — Formula 307 under E.3 Time-Budgeted Exact Solver Comparison is classified as a paper-defined mathematical relation; adjacent prose centers on NeurPRISE, time, budget, MILP, scenario, inference, and the expression links k, in..** `k\in\{4,6\}`
Variables: "k, in".
Sign/normalization/conditioning/surrogate audit: "Formula 307 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k, in; meanings remain tied to E.3 Time-Budgeted Exact Solver Comparison.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.3 Time-Budgeted Exact Solver Comparison, formal object 307.

**Formal object 308 at E.5 Scenario-Count Growth Control — Formula 308 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, runtime, scenario, MILP, solve, original, and the expression links times..** `1.0\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 308 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 308.

**Formal object 309 at E.5 Scenario-Count Growth Control — Formula 309 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, runtime, scenario, MILP, solve, original, and the expression links times..** `1.9\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 309 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 309.

**Formal object 310 at E.5 Scenario-Count Growth Control — Formula 310 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, runtime, scenario, MILP, solve, original, and the expression links times..** `1.2\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 310 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 310.

**Formal object 311 at E.5 Scenario-Count Growth Control — Formula 311 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, runtime, scenario, MILP, solve, original, and the expression links times..** `4.6\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 311 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 311.

**Formal object 312 at E.5 Scenario-Count Growth Control — Formula 312 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, runtime, scenario, MILP, solve, original, and the expression links times..** `1.5\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 312 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 312.

**Formal object 313 at E.5 Scenario-Count Growth Control — Formula 313 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, runtime, scenario, MILP, solve, original, and the expression links times..** `2.5\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 313 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 313.

**Formal object 314 at E.5 Scenario-Count Growth Control — Formula 314 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, runtime, scenario, MILP, solve, original, and the expression links times..** `1.1\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 314 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 314.

**Formal object 315 at E.5 Scenario-Count Growth Control — Formula 315 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, runtime, scenario, MILP, solve, original, and the expression links times..** `1.3\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 315 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 315.

**Formal object 316 at E.5 Scenario-Count Growth Control — Formula 316 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, runtime, scenario, MILP, solve, original, and the expression links times..** `5.0\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 316 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 316.

**Formal object 317 at E.5 Scenario-Count Growth Control — Formula 317 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, runtime, scenario, MILP, solve, original, and the expression links times..** `1.6\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 317 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 317.

**Formal object 318 at E.5 Scenario-Count Growth Control — Formula 318 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, times, only, original, scenario, count, and the expression links symbols defined beside the formula..** `1.1`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 318 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 318.

**Formal object 319 at E.5 Scenario-Count Growth Control — Formula 319 under E.5 Scenario-Count Growth Control is classified as a optimization objective or loss; adjacent prose centers on grows, times, only, original, scenario, count, and the expression links symbols defined beside the formula..** `1.6`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 319 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to E.5 Scenario-Count Growth Control.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, E.5 Scenario-Count Growth Control, formal object 319.

**Formal object 320 at G.1 Problem Formulation — Formula 320 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on CFLP, scenario, uncertainty, through, customer, constraint, and the expression links O..** `O(mn)`
Variables: "O".
Sign/normalization/conditioning/surrogate audit: "Formula 320 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 320.

**Formal object 321 at G.1 Problem Formulation — Formula 321 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on CFLP, scenario, uncertainty, through, customer, constraint, and the expression links O, m, n..** `O(m{+}n)`
Variables: "O, m, n".
Sign/normalization/conditioning/surrogate audit: "Formula 321 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O, m, n; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 321.

**Formal object 322 at G.1 Problem Formulation — Formula 322 under G.1 Problem Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on facilities, capacity, demand, scenario, costs, cost, and the expression links f_{j}\, in..** `f_{j}\!\in\![100,1000]`
Variables: "f_{j}\\, in".
Sign/normalization/conditioning/surrogate audit: "Formula 322 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f_{j}\\, in; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 322.

**Formal object 323 at G.1 Problem Formulation — Formula 323 under G.1 Problem Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on facilities, capacity, demand, scenario, costs, cost, and the expression links a_{j}\, in..** `a_{j}\!\in\![10,100]`
Variables: "a_{j}\\, in".
Sign/normalization/conditioning/surrogate audit: "Formula 323 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: a_{j}\\, in; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 323.

**Formal object 324 at G.1 Problem Formulation — Formula 324 under G.1 Problem Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on facilities, capacity, demand, scenario, costs, cost, and the expression links K_{j}\, in..** `K_{j}\!\in\![200,700]`
Variables: "K_{j}\\, in".
Sign/normalization/conditioning/surrogate audit: "Formula 324 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K_{j}\\, in; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 324.

**Formal object 325 at G.1 Problem Formulation — Formula 325 under G.1 Problem Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on facilities, capacity, demand, scenario, costs, cost, and the expression links c_{ij}\, in..** `c_{ij}\!\in\![1,1000]`
Variables: "c_{ij}\\, in".
Sign/normalization/conditioning/surrogate audit: "Formula 325 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c_{ij}\\, in; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 325.

**Formal object 326 at G.1 Problem Formulation — Formula 326 under G.1 Problem Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on facilities, capacity, demand, scenario, costs, cost, and the expression links d_{i}\, in..** `d_{i}\!\in\![10,500]`
Variables: "d_{i}\\, in".
Sign/normalization/conditioning/surrogate audit: "Formula 326 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{i}\\, in; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 326.

**Formal object 327 at G.1 Problem Formulation — Formula 327 under G.1 Problem Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on facilities, capacity, demand, scenario, costs, cost, and the expression links f_{j}..** `f_{j}`
Variables: "f_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 327 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f_{j}; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 327.

**Formal object 328 at G.1 Problem Formulation — Formula 328 under G.1 Problem Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on facilities, capacity, demand, scenario, costs, cost, and the expression links a_{j}..** `a_{j}`
Variables: "a_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 328 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: a_{j}; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 328.

**Formal object 329 at G.1 Problem Formulation — Formula 329 under G.1 Problem Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on facilities, capacity, demand, scenario, costs, cost, and the expression links K_{j}..** `K_{j}`
Variables: "K_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 329 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K_{j}; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 329.

**Formal object 330 at G.1 Problem Formulation — Formula 330 under G.1 Problem Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on facilities, capacity, demand, scenario, costs, cost, and the expression links c_{ij}..** `c_{ij}`
Variables: "c_{ij}".
Sign/normalization/conditioning/surrogate audit: "Formula 330 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c_{ij}; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 330.

**Formal object 331 at G.1 Problem Formulation — Formula 331 under G.1 Problem Formulation is classified as a paper-defined mathematical relation; adjacent prose centers on facilities, capacity, demand, scenario, costs, cost, and the expression links m..** `m`
Variables: "m".
Sign/normalization/conditioning/surrogate audit: "Formula 331 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: m; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 331.

**Formal object 332 at G.1 Problem Formulation — Formula 332 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on facilities, demand, capacity, CFLP, scenario, costs, and the expression links displaystyle, x, z, eta, y, s..** `\displaystyle\min_{x,\,z,\,\eta,\,\{y^{(s)}\}}`
Variables: "displaystyle, x, z, eta, y, s".
Sign/normalization/conditioning/surrogate audit: "Formula 332 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, x, z, eta, y, s; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 332.

**Formal object 333 at G.1 Problem Formulation — Formula 333 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on facilities, demand, capacity, CFLP, scenario, costs, and the expression links displaystyle, textstyle, j, m, f_{j}\, x_{j}, a_{j}\, z_{j}..** `\displaystyle\textstyle\sum_{j=1}^{m}f_{j}\,x_{j}+\textstyle\sum_{j=1}^{m}a_{j}\,z_{j}+\eta`
Variables: "displaystyle, textstyle, j, m, f_{j}\\, x_{j}, a_{j}\\, z_{j}, eta".
Sign/normalization/conditioning/surrogate audit: "Formula 333 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, textstyle, j, m, f_{j}\\, x_{j}, a_{j}\\, z_{j}, eta; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 333.

**Formal object 334 at G.1 Problem Formulation — Formula 334 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on facilities, demand, capacity, CFLP, scenario, costs, and the expression links displaystyle, eta, geq, textstyle, i, n, j, m..** `\displaystyle\eta\geq\textstyle\sum_{i=1}^{n}\sum_{j=1}^{m}c_{ij}\,y_{ij}^{(s)},`
Variables: "displaystyle, eta, geq, textstyle, i, n, j, m, c_{ij}\\, y_{ij}^{, s".
Sign/normalization/conditioning/surrogate audit: "Formula 334 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, eta, geq, textstyle, i, n, j, m, c_{ij}\\, y_{ij}^{, s; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 334.

**Formal object 335 at G.1 Problem Formulation — Formula 335 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on facilities, demand, capacity, CFLP, scenario, costs, and the expression links displaystyle, z_{j}\leq, K_{j}\, x_{j}..** `\displaystyle z_{j}\leq K_{j}\,x_{j},`
Variables: "displaystyle, z_{j}\\leq, K_{j}\\, x_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 335 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, z_{j}\\leq, K_{j}\\, x_{j}; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 335.

**Formal object 336 at G.1 Problem Formulation — Formula 336 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on facilities, demand, capacity, CFLP, scenario, costs, and the expression links displaystyle, forall, j, in, m..** `\displaystyle\forall j\in[m],`
Variables: "displaystyle, forall, j, in, m".
Sign/normalization/conditioning/surrogate audit: "Formula 336 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, forall, j, in, m; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 336.

**Formal object 337 at G.1 Problem Formulation — Formula 337 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on facilities, demand, capacity, CFLP, scenario, costs, and the expression links displaystyle, textstyle, i, n, y_{ij}^{, s, leq, z_{j}..** `\displaystyle\textstyle\sum_{i=1}^{n}y_{ij}^{(s)}\leq z_{j},`
Variables: "displaystyle, textstyle, i, n, y_{ij}^{, s, leq, z_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 337 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, textstyle, i, n, y_{ij}^{, s, leq, z_{j}; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 337.

**Formal object 338 at G.1 Problem Formulation — Formula 338 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on facilities, demand, capacity, CFLP, scenario, costs, and the expression links displaystyle, forall, j, in, m, s, S..** `\displaystyle\forall j\in[m],\;\forall s\in[S],`
Variables: "displaystyle, forall, j, in, m, s, S".
Sign/normalization/conditioning/surrogate audit: "Formula 338 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, forall, j, in, m, s, S; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 338.

**Formal object 339 at G.1 Problem Formulation — Formula 339 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on facilities, demand, capacity, CFLP, scenario, costs, and the expression links displaystyle, textstyle, j, m, y_{ij}^{, s, geq, d_{i}^{..** `\displaystyle\textstyle\sum_{j=1}^{m}y_{ij}^{(s)}\geq d_{i}^{(s)},`
Variables: "displaystyle, textstyle, j, m, y_{ij}^{, s, geq, d_{i}^{".
Sign/normalization/conditioning/surrogate audit: "Formula 339 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, textstyle, j, m, y_{ij}^{, s, geq, d_{i}^{; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 339.

**Formal object 340 at G.1 Problem Formulation — Formula 340 under G.1 Problem Formulation is classified as a optimization objective or loss; adjacent prose centers on facilities, demand, capacity, CFLP, scenario, costs, and the expression links displaystyle, y_{ij}^{, s, geq, z_{j}\geq, x_{j}\in\{0..** `\displaystyle y_{ij}^{(s)}\geq 0,\;z_{j}\geq 0,\;x_{j}\in\{0,1\}.`
Variables: "displaystyle, y_{ij}^{, s, geq, z_{j}\\geq, x_{j}\\in\\{0".
Sign/normalization/conditioning/surrogate audit: "Formula 340 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: displaystyle, y_{ij}^{, s, geq, z_{j}\\geq, x_{j}\\in\\{0; meanings remain tied to G.1 Problem Formulation.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.1 Problem Formulation, formal object 340.

**Formal object 341 at G.2 Encoding and Training — Formula 341 under G.2 Encoding and Training is classified as a state or representation transformation; adjacent prose centers on encoding, nodes, graph, facility, customer, scenario, and the expression links G, s..** `G^{(s)}_{\text{CFLP}}`
Variables: "G, s".
Sign/normalization/conditioning/surrogate audit: "Formula 341 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G, s; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 341.

**Formal object 342 at G.2 Encoding and Training — Formula 342 under G.2 Encoding and Training is classified as a state or representation transformation; adjacent prose centers on encoding, nodes, graph, facility, customer, scenario, and the expression links f_{1}..** `f_{1}`
Variables: "f_{1}".
Sign/normalization/conditioning/surrogate audit: "Formula 342 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f_{1}; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 342.

**Formal object 343 at G.2 Encoding and Training — Formula 343 under G.2 Encoding and Training is classified as a state or representation transformation; adjacent prose centers on encoding, nodes, graph, facility, customer, scenario, and the expression links f_{2}..** `f_{2}`
Variables: "f_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 343 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f_{2}; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 343.

**Formal object 344 at G.2 Encoding and Training — Formula 344 under G.2 Encoding and Training is classified as a state or representation transformation; adjacent prose centers on encoding, nodes, graph, facility, customer, scenario, and the expression links f_{m}..** `f_{m}`
Variables: "f_{m}".
Sign/normalization/conditioning/surrogate audit: "Formula 344 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f_{m}; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 344.

**Formal object 345 at G.2 Encoding and Training — Formula 345 under G.2 Encoding and Training is classified as a state or representation transformation; adjacent prose centers on encoding, nodes, graph, facility, customer, scenario, and the expression links f_{j}, a_{j}, K_{j}..** `[f_{j},\,a_{j},\,K_{j}]`
Variables: "f_{j}, a_{j}, K_{j}".
Sign/normalization/conditioning/surrogate audit: "Formula 345 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f_{j}, a_{j}, K_{j}; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 345.

**Formal object 346 at G.2 Encoding and Training — Formula 346 under G.2 Encoding and Training is classified as a state or representation transformation; adjacent prose centers on encoding, nodes, graph, facility, customer, scenario, and the expression links c_{n}..** `c_{n}`
Variables: "c_{n}".
Sign/normalization/conditioning/surrogate audit: "Formula 346 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c_{n}; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 346.

**Formal object 347 at G.2 Encoding and Training — Formula 347 under G.2 Encoding and Training is classified as a state or representation transformation; adjacent prose centers on encoding, nodes, graph, facility, customer, scenario, and the expression links d_{i}^{, s..** `[d_{i}^{(s)}]`
Variables: "d_{i}^{, s".
Sign/normalization/conditioning/surrogate audit: "Formula 347 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{i}^{, s; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 347.

**Formal object 348 at G.2 Encoding and Training — Formula 348 under G.2 Encoding and Training is classified as a state or representation transformation; adjacent prose centers on encoding, nodes, graph, facility, customer, scenario, and the expression links times..** `\times 2`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 348 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 348.

**Formal object 349 at G.2 Encoding and Training — Formula 349 under G.2 Encoding and Training is classified as a constraint or formal-analysis relation; adjacent prose centers on variable, encoding, nodes, CFLP, standard, constraint, and the expression links y_{ij}^{, s..** `y_{ij}^{(s)}`
Variables: "y_{ij}^{, s".
Sign/normalization/conditioning/surrogate audit: "Formula 349 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{ij}^{, s; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 349.

**Formal object 350 at G.2 Encoding and Training — Formula 350 under G.2 Encoding and Training is classified as a constraint or formal-analysis relation; adjacent prose centers on variable, encoding, nodes, CFLP, standard, constraint, and the expression links O, m, n..** `O(m+n)`
Variables: "O, m, n".
Sign/normalization/conditioning/surrogate audit: "Formula 350 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O, m, n; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 350.

**Formal object 351 at G.2 Encoding and Training — Formula 351 under G.2 Encoding and Training is classified as a state or representation transformation; adjacent prose centers on memory, regret, training, throughput., while, times, and the expression links times..** `2.7{\times}`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 351 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 351.

**Formal object 352 at G.2 Encoding and Training — Formula 352 under G.2 Encoding and Training is classified as a state or representation transformation; adjacent prose centers on memory, regret, training, throughput., while, times, and the expression links times..** `4{\times}`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 352 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to G.2 Encoding and Training.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.2 Encoding and Training, formal object 352.

**Formal object 353 at Training configuration. — Formula 353 under Training configuration. is classified as a paper-defined mathematical relation; adjacent prose centers on uses, scale, mathrm, times, problem, medium, and the expression links mathrm, times, B..** `\mathrm{lr}=6{\times}10^{-4}(B/32)`
Variables: "mathrm, times, B".
Sign/normalization/conditioning/surrogate audit: "Formula 353 operator audit: fraction or division; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm, times, B; meanings remain tied to Training configuration..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Training configuration., formal object 353.

**Formal object 354 at Training configuration. — Formula 354 under Training configuration. is classified as a paper-defined mathematical relation; adjacent prose centers on uses, scale, mathrm, times, problem, medium, and the expression links B..** `B{=}32`
Variables: "B".
Sign/normalization/conditioning/surrogate audit: "Formula 354 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: B; meanings remain tied to Training configuration..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Training configuration., formal object 354.

**Formal object 355 at Training configuration. — Formula 355 under Training configuration. is classified as a paper-defined mathematical relation; adjacent prose centers on uses, scale, mathrm, times, problem, medium, and the expression links B..** `B{=}24`
Variables: "B".
Sign/normalization/conditioning/surrogate audit: "Formula 355 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: B; meanings remain tied to Training configuration..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Training configuration., formal object 355.

**Formal object 356 at Training configuration. — Formula 356 under Training configuration. is classified as a paper-defined mathematical relation; adjacent prose centers on uses, scale, mathrm, times, problem, medium, and the expression links mathrm, times..** `\mathrm{lr}{=}4.5{\times}10^{-4}`
Variables: "mathrm, times".
Sign/normalization/conditioning/surrogate audit: "Formula 356 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm, times; meanings remain tied to Training configuration..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Training configuration., formal object 356.

**Formal object 357 at Training configuration. — Formula 357 under Training configuration. is classified as a paper-defined mathematical relation; adjacent prose centers on uses, scale, mathrm, times, problem, medium, and the expression links B..** `B{=}16`
Variables: "B".
Sign/normalization/conditioning/surrogate audit: "Formula 357 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: B; meanings remain tied to Training configuration..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Training configuration., formal object 357.

**Formal object 358 at Training configuration. — Formula 358 under Training configuration. is classified as a paper-defined mathematical relation; adjacent prose centers on uses, scale, mathrm, times, problem, medium, and the expression links mathrm, times..** `\mathrm{lr}{=}3{\times}10^{-4}`
Variables: "mathrm, times".
Sign/normalization/conditioning/surrogate audit: "Formula 358 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm, times; meanings remain tied to Training configuration..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Training configuration., formal object 358.

**Formal object 359 at Training configuration. — Formula 359 under Training configuration. is classified as a paper-defined mathematical relation; adjacent prose centers on uses, scale, mathrm, times, problem, medium, and the expression links B..** `B{=}8`
Variables: "B".
Sign/normalization/conditioning/surrogate audit: "Formula 359 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: B; meanings remain tied to Training configuration..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Training configuration., formal object 359.

**Formal object 360 at Input normalization. — Formula 360 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on group., normalized, costs, remaining, floating-point, features, and the expression links F_{g}..** `F_{g}`
Variables: "F_{g}".
Sign/normalization/conditioning/surrogate audit: "Formula 360 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: F_{g}; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 360.

**Formal object 361 at Input normalization. — Formula 361 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on group., features, normalized, costs, remaining, floating-point, and the expression links tilde, F, g, F_{g}}{\, F_{g}\, infty, epsilon..** `\tilde{F}_{g}=\frac{F_{g}}{\|F_{g}\|_{\infty}+\epsilon}.`
Variables: "tilde, F, g, F_{g}}{\\, F_{g}\\, infty, epsilon".
Sign/normalization/conditioning/surrogate audit: "Formula 361 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tilde, F, g, F_{g}}{\\, F_{g}\\, infty, epsilon; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 361.

**Formal object 362 at Input normalization. — Formula 362 under Input normalization. is classified as a paper-defined mathematical relation; adjacent prose centers on Since, features, non-negative, maps, group, without, and the expression links symbols defined beside the formula..** `[0,1]`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 362 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Input normalization..".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, Input normalization., formal object 362.

**Formal object 363 at G.3 Performance and Generalization — Formula 363 under G.3 Performance and Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on demand, larger, scenario, experiment, per-customer, Table, and the expression links S..** `S=100`
Variables: "S".
Sign/normalization/conditioning/surrogate audit: "Formula 363 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S; meanings remain tied to G.3 Performance and Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.3 Performance and Generalization, formal object 363.

**Formal object 364 at G.3 Performance and Generalization — Formula 364 under G.3 Performance and Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on demand, larger, scenario, experiment, per-customer, Table, and the expression links S..** `S=200`
Variables: "S".
Sign/normalization/conditioning/surrogate audit: "Formula 364 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S; meanings remain tied to G.3 Performance and Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.3 Performance and Generalization, formal object 364.

**Formal object 365 at G.3 Performance and Generalization — Formula 365 under G.3 Performance and Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on demand, larger, scenario, experiment, per-customer, Table, and the expression links mu, j, sim, mathrm..** `\mu_{j}\sim\mathrm{Uniform}[180,260]`
Variables: "mu, j, sim, mathrm".
Sign/normalization/conditioning/surrogate audit: "Formula 365 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mu, j, sim, mathrm; meanings remain tied to G.3 Performance and Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.3 Performance and Generalization, formal object 365.

**Formal object 366 at G.3 Performance and Generalization — Formula 366 under G.3 Performance and Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on demand, larger, scenario, experiment, per-customer, Table, and the expression links sigma, j, mathrm, mu..** `\sigma_{j}=\mathrm{clip}(0.08\,\mu_{j},\,12,\,22)`
Variables: "sigma, j, mathrm, mu".
Sign/normalization/conditioning/surrogate audit: "Formula 366 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sigma, j, mathrm, mu; meanings remain tied to G.3 Performance and Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.3 Performance and Generalization, formal object 366.

**Formal object 367 at G.3 Performance and Generalization — Formula 367 under G.3 Performance and Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on demand, larger, scenario, experiment, per-customer, Table, and the expression links symbols defined beside the formula..** `[10,500]`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 367 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to G.3 Performance and Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.3 Performance and Generalization, formal object 367.

**Formal object 368 at G.3 Performance and Generalization — Formula 368 under G.3 Performance and Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on demand, larger, scenario, experiment, per-customer, Table, and the expression links symbols defined beside the formula..** `[80,380]`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 368 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to G.3 Performance and Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.3 Performance and Generalization, formal object 368.

**Formal object 369 at G.3 Performance and Generalization — Formula 369 under G.3 Performance and Generalization is classified as a probabilistic or expectation relation; adjacent prose centers on demand, larger, scenario, experiment, per-customer, Table, and the expression links symbols defined beside the formula..** `[0.05,0.20]`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 369 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to G.3 Performance and Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.3 Performance and Generalization, formal object 369.

**Formal object 370 at G.3 Performance and Generalization — Formula 370 under G.3 Performance and Generalization is classified as a optimization objective or loss; adjacent prose centers on NeurPRISE, demand., under, scenario, Neur2RO, Table, and the expression links symbols defined beside the formula..** `{}_{\text{in}}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 370 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to G.3 Performance and Generalization.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.3 Performance and Generalization, formal object 370.

**Formal object 371 at G.4 Feasibility Analysis — Formula 371 under G.4 Feasibility Analysis is classified as a optimization objective or loss; adjacent prose centers on recourse, demand, scenarios, infeasibility, method, where, and the expression links approx, k, S..** `{\approx}k/S`
Variables: "approx, k, S".
Sign/normalization/conditioning/surrogate audit: "Formula 371 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: approx, k, S; meanings remain tied to G.4 Feasibility Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2605.14494, G.4 Feasibility Analysis, formal object 371.

Representative source mathematical objects follow. They are navigation evidence, not standalone interpretations:

- Mathematical object 1: `7` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 2: `200\times` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 3: `5\times` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 4: `4\times` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 5: `k` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 6: `2` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 7: `7{\times}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 8: `\Xi=\{\xi_{1},\dots,\xi_{S}\}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 9: `S` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 10: `\displaystyle\min_{x\in X}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 11: `\displaystyle c^{\top}x+\max_{\xi\in\Xi}\min_{y\in F(x,\xi)}b_{\xi}^{\top}y,` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 12: `\displaystyle Ax\geq d,` — read with adjacent definitions; no symbol meaning is inferred from markup alone.

Equation-to-adjacent-context reconstruction:

- Equation under source heading Abstract: `7`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading Abstract: `200\times`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading Abstract: `5\times`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading Abstract: `4\times`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading 1 Introduction: `k`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading 1 Introduction: `2`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading 1 Introduction: `7{\times}`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading 2 Related Work: `K`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading 2 Related Work: `K`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading 3 Preliminaries: `\Xi=\{\xi_{1},\dots,\xi_{S}\}`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading 3 Preliminaries: `S`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.
- Equation under source heading 3 Preliminaries: `\displaystyle\min_{x\in X}`; adjacent method terms: scenario, each, model, encoder, graph, embeddings, sequential, prise.

For each central equation, the audit asks whether the sign agrees with the prose, whether weights are normalized, whether masking or conditioning changes the denominator, whether a displayed objective is exact or a training surrogate, and whether units can be compared. A learned score is not automatically calibrated, a relaxation is not an exact discrete solution, and an empirical constraint satisfaction rate is not a theorem. These distinctions protect the paper's real contribution from stronger claims it does not need.

### 2.3 Components, architecture, and information flow

The source's technical path is anchored to 4 Methodology, 4.2.1 Model Architecture. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims.

**Input/output dataflow:** The documented dataflow is reconstructed only across 4 Methodology, and 4.2.1 Model Architecture, where the source associates scenario, instance, embeddings, mathbf, decoder, context, and encoder. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

| Component | Inherited or novel | Role | Source locator |
|---|---|---|---|
| 4 Methodology | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with SEquential, PRISE, Methodology, first, and introduce; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2605.14494, 4 Methodology |
| 4.2.1 Model Architecture | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with scenario, instance, Architecture, Given, and encoder; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture |
| 4.2.1 Model Architecture | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with graph, scenario, bipartite, Architecture, and Encoder; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture |
| 4.2.1 Model Architecture | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with embeddings, Architecture, capture, inter-scenario, and dependencies; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture |
| 4.2.1 Model Architecture | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with Decoder, instance, context, Architecture, and produces; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture |

The paper-specific method vocabulary is scenario, each, model, encoder, graph, embeddings, sequential, prise, then, given. This vocabulary was derived from the complete method/architecture paragraphs rather than the title. It identifies the entities that must appear in a faithful architecture reconstruction and creates a falsifiable check: an implementation or summary that omits these named objects is not yet grounded in this paper.

The architecture is reconstructed as an information-flow graph: source identity and inputs enter; inherited and paper-specific components transform or score them; a decision or representation is produced; optional validation or post-processing occurs; and an evaluated outcome leaves the pipeline. Each edge should name the information available at that point. A comparison becomes unfair if one method has access to labels, future requests, privileged metadata, additional context, or a larger tuning budget that another method lacks.

### 2.4 Training, calibration, and inference

Construction-time and runtime work are separate accounting domains. Training may fit parameters, construct representations, estimate thresholds, tune prompts, or learn a policy. Calibration may use held-out examples or measurements. Inference may retrieve, route, compress, classify, generate, search, solve, or verify. Post-processing may enforce a constraint or discard invalid output. A credible efficiency claim says which of these phases is included, which is amortized, and which is external to the reported number.

Training or calibration evidence is explicitly located in 4 Methodology. The associated source vocabulary emphasizes scenario, each, model, encoder, graph, embeddings, sequential, prise, then, given.

Paper-specific construction/training sequence:

1. At 4 Methodology, the paper reports a training-related operation involving SEquential, PRISE, Methodology, first, introduce, and PRoblem-drIven. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 4 Methodology)*
2. At 4.2.1 Model Architecture, the paper reports a training-related operation involving mathbf, scenario, Architecture, learnable, projection, and matrices. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture)*
3. At 5 Experiments, the paper reports a training-related operation involving Experiments, Gurobi, conducted, server, EPYC, and Core. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments)*
4. At 5 Experiments, the paper reports a training-related operation involving Training, validation, instances, test, Experiments, and instance. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments)*

Inference or runtime evidence is explicitly located in 4.2.1 Model Architecture, 5.1 Comparison Analysis, G.4 Feasibility Analysis. Its source vocabulary overlaps scenario, each, model, encoder, graph, embeddings, sequential, prise, then, given.

Paper-specific inference/evaluation sequence:

1. At 4.2.1 Model Architecture, the paper reports an inference or deployment action involving scenario, instance, Architecture, Given, encoder, and represents. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture)*
2. At 4.2.1 Model Architecture, the paper reports an inference or deployment action involving Decoder, instance, context, Architecture, produces, and per-scenario. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture)*
3. At 4.2.1 Model Architecture, the paper reports an inference or deployment action involving mathbf, mathrm, times, representing, serves, and Architecture. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 4.2.1 Model Architecture)*
4. At 5 Experiments, the paper reports an inference or deployment action involving instances, Experiments, Instance, Generation, generate, and small. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments)*

The reconstructed operational sequence is: pin input and artifact versions; validate prerequisites; compute the method-specific state or signal; apply the stated decision or objective; materialize the output; execute any downstream consumer; and measure both quality and resource outcomes. This sequence is reviewer inference grounded in the paper's organization. It is a testing model, not an assertion that the authors implemented an identical production controller.[^inference]

### 2.5 Notation and implementation audit

No independent implementation was run. The audit therefore checks internal legibility across equations, prose, captions, appendices, and extracted code/data statements. Apparent inconsistencies remain unresolved unless source evidence explains them. Source availability is classified in levels—declared, reachable, inspectable, runnable, and result-reproducing—and this local phase establishes only the declared/local-source layers.

## 3. Architecture and Complete Operational Pipeline

### 3.1 Representation and state

The documented dataflow is reconstructed only across 4 Methodology, and 4.2.1 Model Architecture, where the source associates scenario, instance, embeddings, mathbf, decoder, context, and encoder. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

The central representation must be described by shape, type, provenance, lifetime, and relationship to the original input. If it is compressed, selected, latent, retrieved, generated, or aggregated, the review asks what information can be lost and how that loss is detected. If it is learned, the training distribution and version become part of its identity. If it is mutable, update ordering, expiry, and rollback become part of the method rather than operational afterthoughts.

### 3.2 Decision or action modules

The paper-specific modules should be separated from inherited encoders, decoders, solvers, retrieval systems, evaluators, or model APIs. A score can rank candidates without being calibrated; a policy can improve average reward without satisfying hard constraints; and a verifier can reject some failures without certifying all accepted outputs. The assessment uses the source's strongest ablation or controlled comparison to decide which module is necessary and which is merely bundled.

### 3.3 Dependencies, post-processing, and guarantee boundary

Dependencies include data preprocessing, external models, tokenizers, simulators, indexes, numerical libraries, and evaluation code. Post-processing can materially create the final result, so its compute and failure rate belong in the pipeline. Exact validation, when present, may establish a property of a returned object; it does not automatically establish semantic correctness, optimality, robustness, or absence of distribution shift.

### 3.4 Resource allocation and stopping

Budgets can refer to tokens, bytes, parameters, candidates, iterations, calls, samples, time, energy, or money. Requested and achieved budgets should both be recorded. Early stopping and fallback can bias which cases receive expensive processing. Batching can improve throughput while worsening latency. The review therefore distinguishes construction cost, per-instance latency, batch throughput, tail latency, peak memory, and downstream cost before accepting a general efficiency claim.

## 4. Experimental Design and Evidence Reconstructed

The evaluation reconstruction follows 5.1 Comparison Analysis, E.2 Seed Variance Analysis, G.4 Feasibility Analysis, 5 Experiments, with 23 table captions and 8 figure captions inventoried.

Paper-specific evaluation vocabulary centers on instances, across, all, neurprise, where, scenarios, prise, training, regret, method. These terms constrain which datasets, metrics, models, budgets, or operational quantities must be preserved with each reported comparison. They also identify where a later reproduction dossier must look for splits, baselines, hardware, batching, runtime semantics, and uncertainty rather than assuming conventional defaults.

The headings mechanically associated with evaluation and results were:

- 5.1 Comparison Analysis
- E.2 Seed Variance Analysis
- G.4 Feasibility Analysis
- 5 Experiments

### 4.1 Data, splits, and distribution

Not applicable: No named dataset, benchmark, corpus, or split was found in the captured full-paper data/evaluation paragraphs; none is invented. (source locator: private full-paper evidence dossier for arXiv:2605.14494, data/evaluation paragraph inventory).

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| Prob. | Table 1 lists Prob. as a numeric comparison row under 5 Experiments. | Neither the Table 1 caption nor its row label establishes whether Prob. was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 row Prob. |
| SEL | Table 1 lists SEL as a numeric comparison row under 5 Experiments. | Neither the Table 1 caption nor its row label establishes whether SEL was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 row SEL |
| PRISE | Table 1 lists PRISE as a numeric comparison row under 5 Experiments. | Neither the Table 1 caption nor its row label establishes whether PRISE was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 row PRISE |
| Random | Table 1 lists Random as a numeric comparison row under 5 Experiments. | Neither the Table 1 caption nor its row label establishes whether Random was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 row Random |
| SOR | Table 1 lists SOR as a numeric comparison row under 5 Experiments. | Neither the Table 1 caption nor its row label establishes whether SOR was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 row SOR |
| K-means | Table 1 lists K-means as a numeric comparison row under 5 Experiments. | Neither the Table 1 caption nor its row label establishes whether K-means was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 row K-means |
| MaxSum | Table 1 lists MaxSum as a numeric comparison row under 5 Experiments. | Neither the Table 1 caption nor its row label establishes whether MaxSum was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 row MaxSum |
| Neur2RO | Table 1 lists Neur2RO as a numeric comparison row under 5 Experiments. | Neither the Table 1 caption nor its row label establishes whether Neur2RO was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 row Neur2RO |
| NeurPRISE | Table 1 lists NeurPRISE as a numeric comparison row under 5 Experiments. | Neither the Table 1 caption nor its row label establishes whether NeurPRISE was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 row NeurPRISE |
| VC | Table 1 lists VC as a numeric comparison row under 5 Experiments. | Neither the Table 1 caption nor its row label establishes whether VC was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 row VC |
| Large | Table 2 lists Large as a numeric comparison row under 5.1 Comparison Analysis. | Neither the Table 2 caption nor its row label establishes whether Large was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 2 row Large |
| Problem | Table 7 lists Problem as a numeric comparison row under B.2 PRISE Compression Budget and Convergence Comparison. | Neither the Table 7 caption nor its row label establishes whether Problem was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 7 row Problem |
| Avg | Table 12 lists Avg as a numeric comparison row under E.2 Seed Variance Analysis. | Neither the Table 12 caption nor its row label establishes whether Avg was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 12 row Avg |
| Medium | Table 13 lists Medium as a numeric comparison row under E.3 Time-Budgeted Exact Solver Comparison. | Neither the Table 13 caption nor its row label establishes whether Medium was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 13 row Medium |
| CFLP | Table 18 lists CFLP as a numeric comparison row under G.2 Encoding and Training. | Neither the Table 18 caption nor its row label establishes whether CFLP was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 18 row CFLP |
| CV | Table 19 lists CV as a numeric comparison row under G.2 Encoding and Training. | Neither the Table 19 caption nor its row label establishes whether CV was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2605.14494, Table 19 row CV |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

| Metric | Denominator/conditioning | Direction | Source locator |
|---|---|---|---|
| Problem | The metric-definition evidence at 3 Preliminaries ties Problem to terms value, full-scenario, objective, evaluate, scenario, reduced, star, convention. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 7 header Problem |
| \hat{k}/\|\Xi\| (%) \,\downarrow / Mean | Table 7 reports \hat{k}/\|\Xi\| (%) \,\downarrow / Mean as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 7 header \hat{k}/\|\Xi\| (%) \,\downarrow / Mean |
| \hat{k}/\|\Xi\| (%) \,\downarrow / Med. | Table 7 reports \hat{k}/\|\Xi\| (%) \,\downarrow / Med. as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 7 header \hat{k}/\|\Xi\| (%) \,\downarrow / Med. |
| % instances with \hat{k}/\|\Xi\|\leq \uparrow / 2% | Table 7 reports % instances with \hat{k}/\|\Xi\|\leq \uparrow / 2% as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 7 header % instances with \hat{k}/\|\Xi\|\leq \uparrow / 2% |
| % instances with \hat{k}/\|\Xi\|\leq \uparrow / 4% | Table 7 reports % instances with \hat{k}/\|\Xi\|\leq \uparrow / 4% as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 7 header % instances with \hat{k}/\|\Xi\|\leq \uparrow / 4% |
| % instances with \hat{k}/\|\Xi\|\leq \uparrow / 8% | Table 7 reports % instances with \hat{k}/\|\Xi\|\leq \uparrow / 8% as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 7 header % instances with \hat{k}/\|\Xi\|\leq \uparrow / 8% |
| % instances with \hat{k}/\|\Xi\|\leq \uparrow / 12% | Table 7 reports % instances with \hat{k}/\|\Xi\|\leq \uparrow / 12% as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 7 header % instances with \hat{k}/\|\Xi\|\leq \uparrow / 12% |
| N/C \,\downarrow / (%) | Table 7 reports N/C \,\downarrow / (%) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 7 header N/C \,\downarrow / (%) |
| Node Features | Table 8 reports Node Features as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 8 header Node Features |
| d_{\text{node}} | Table 8 reports d_{\text{node}} as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 8 header d_{\text{node}} |
| d_{\text{edge}} | Table 8 reports d_{\text{edge}} as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 8 header d_{\text{edge}} |
| Regret% ( \downarrow ) | Table 19 reports Regret% ( \downarrow ) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 19 header Regret% ( \downarrow ) |
| GPU (MB) | Table 19 reports GPU (MB) as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 19 header GPU (MB) |
| s/epoch | Table 19 reports s/epoch as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 19 header s/epoch |
| Batch | The metric-definition evidence at Training configuration. ties Batch to terms uses, scale, mathrm, times, problem, medium, large, batch. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2605.14494, Table 19 header Batch |

Metrics are reconstructed with direction, denominator, aggregation unit, conditioning, and reference quality. Failures excluded from an average create survivor bias. A gap to a best-known incumbent is not a gap to a proven optimum. A judge-model score is not a human preference without validation. A compression ratio can invert depending on convention. Confidence intervals, paired tests, and effect sizes matter when differences are close or instances are correlated.

### 4.4 Hardware, batching, and runtime semantics

Quality-v2 paper-specific hardware/runtime evidence:

- At 1 Introduction, the paper's hardware/runtime paragraph names uncertainty, discrete, sets, scenarios, solution, While, most, literature. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 1 Introduction)*
- At 3 Preliminaries, the paper's hardware/runtime paragraph names mathbb, times, recourse, decisions, feasible, integer, subseteq, where. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 3 Preliminaries)*
- At 5 Experiments, the paper's hardware/runtime paragraph names CPU, 48 GB. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments)*
- At 5.1 Comparison Analysis, the paper's hardware/runtime paragraph names runtime. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.1 Comparison Analysis)*
- At 5.2 Flexibility and Scalability, the paper's hardware/runtime paragraph names runtime. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.2 Flexibility and Scalability)*
- At 5.2 Flexibility and Scalability, the paper's hardware/runtime paragraph names runtime. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 5.2 Flexibility and Scalability)*
- At Labeling cost., the paper's hardware/runtime paragraph names PRISE, labeling, cost, wall-clock, instances, Section, training, small-scale. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, Labeling cost.)*
- At Selection Problem (SEL)., the paper's hardware/runtime paragraph names selection, cost, decisions, costs, size, items, uncertain, goal. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, Selection Problem (SEL).)*


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
| Table 7 | PRISE | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Problem; \hat{k}/\|\Xi\| (%) \,\downarrow / Mean; \hat{k}/\|\Xi\| (%) \,\downarrow / Med.; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 2%; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 4%; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 8%; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 12%; N/C \,\downarrow / (%) | Problem=20; Problem=50; \hat{k}/\|\Xi\| (%) \,\downarrow / Mean=4.2; \hat{k}/\|\Xi\| (%) \,\downarrow / Med.=4.0; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 2%=34.4; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 4%=79.6; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 8%=95.2; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 12%=96.4; N/C \,\downarrow / (%)=3.6 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2605.14494, Table 7 row 5 |
| Table 7 | PRISE | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Problem; \hat{k}/\|\Xi\| (%) \,\downarrow / Mean; \hat{k}/\|\Xi\| (%) \,\downarrow / Med.; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 2%; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 4%; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 8%; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 12%; N/C \,\downarrow / (%) | Problem=20; Problem=50; \hat{k}/\|\Xi\| (%) \,\downarrow / Mean=7.8; \hat{k}/\|\Xi\| (%) \,\downarrow / Med.=8.0; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 2%=1.2; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 4%=18.8; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 8%=71.6; % instances with \hat{k}/\|\Xi\|\leq \uparrow / 12%=91.6; N/C \,\downarrow / (%)=5.6 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2605.14494, Table 7 row 8 |
| Table 8 | SEL / constraint coeff. | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Node Features; d_{\text{node}}; d_{\text{edge}} | Node Features=4; d_{\text{node}}=8; d_{\text{edge}}=1 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2605.14494, Table 8 row 2 |
| Table 8 | VC / constraint coeff. | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Node Features; d_{\text{node}}; d_{\text{edge}} | Node Features=4; d_{\text{node}}=9; d_{\text{edge}}=1 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2605.14494, Table 8 row 3 |
| Table 18 | CFLP / transport cost c_{ij} | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Node Features; d_{\text{node}}; d_{\text{edge}} | Node Features=2; d_{\text{node}}=6; d_{\text{edge}}=1 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2605.14494, Table 18 row 2 |
| Table 19 | PS | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Regret% ( \downarrow ); GPU (MB); s/epoch; Batch | Regret% ( \downarrow )=0.10; GPU (MB)=3,973; s/epoch=43; Batch=32 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2605.14494, Table 19 row 3 |
| Table 19 | CV | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Regret% ( \downarrow ); GPU (MB); s/epoch; Batch | Regret% ( \downarrow )=0.12; GPU (MB)=3,648; s/epoch=114; Batch=8 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2605.14494, Table 19 row 2 |
| result context at 5.1 Comparison Analysis | Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 1, 2, 4, 6 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2605.14494, 5.1 Comparison Analysis |
| result context at 5.1 Comparison Analysis | Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 1, 2 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2605.14494, 5.1 Comparison Analysis |
| result context at 5.1 Comparison Analysis | Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 2, 4 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2605.14494, 5.1 Comparison Analysis |
| result context at G.4 Feasibility Analysis | Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 0%, 6 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2605.14494, G.4 Feasibility Analysis |

Bounded exact evidence retained from the paper report:

- Paper report, numeric result in 5.1 Comparison Analysis: “We evaluate methods across reduction budgets k ∈ { 1…” (exact numeric tokens: 1, 2, 4, 6, 1, 2, 4, 6).

- No table-caption fragment was included in the bounded verbatim evidence budget.

The correct interpretation retains task, dataset, split, model, baseline, metric, budget, and hardware with each result. A largest reported improvement is an operating point, not a distribution. An average is not a tail guarantee. A component metric can diagnose mechanism without proving end-to-end utility. Where the source reports multiple tables or figures, their relationships should be checked for consistent defaults, denominators, and versioned settings.

Three types of gain remain separate. Representation gain means fewer tokens, bytes, channels, states, features, or bits. Execution gain means lower latency, memory traffic, transfer, energy, or higher throughput. Outcome gain means better correctness, quality, utility, constraint satisfaction, or task completion. The paper may establish one or more under its setting; a deployment decision requires the combination relevant to its service objective.

Table and figure captions were inventoried rather than republished. Their exact values remain anchored to the paper. Any public summary should cite only values whose numerator, denominator, model, dataset, and comparison are simultaneously known. This review does not manufacture missing uncertainty or turn qualitative illustrations into statistical evidence.

## 6. Ablations and Causal Evidence

Paper-specific ablation/control ledger:

| Component/control | Paper-reported delta | Control caveat | Source locator |
|---|---|---|---|
| assess, sensitivity, and training | 1, 2, 3, 4, 42, and 12 | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2605.14494, E.2 Seed Variance Analysis |
| feasibility, NeurPRISE, and recovers | 0%, and 6 | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2605.14494, G.4 Feasibility Analysis |

Ablations are persuasive when one named component changes while model, data, budget, training effort, and implementation quality stay fixed. The complete source was screened for removals, swaps, budget sweeps, sensitivity tests, and failure examples. If multiple elements change together, the result supports the bundle more strongly than any individual mechanism. If a simple cost-matched control is missing, the causal interpretation remains limited.

Randomness must be classified as training seeds, inference seeds, data-generation seeds, checkpoint-selection variance, or hyperparameter-search variance. Repeated inference does not prove training robustness. A named significance test should identify its independence unit and paired design. The practical importance of an effect is separate from statistical detectability, especially when a large benchmark makes very small changes significant.

Author-stated limitations:

- The author-side qualification at 6 Conclusion concerns PRISE, NeurPRISE, propose, problem-driven, sequential, and lookahead. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 6 Conclusion)*

Reviewer-identified limitations:

- No independent reproduction was performed for arXiv:2605.14494v1; scenario, scenarios, Training, and NeurPRISE remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, and Motivation and setup.)*
- The dossier inventories 61 headings, 23 tables, 8 figures, and 371 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2605.14494, complete coverage inventory)*

The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 2 candidate sentences and the limitation/discussion vocabulary prise, neurprise, propose, problem-driven, sequential, lookahead, heuristic, scenario, reduction, gnn-transformer. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper frames Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty as a contribution to Scenario, uncertainty, PRISE, NeurPRISE. | Problem framing is located in the profile's named introduction/problem headings; no numbered section marker is treated as a measurement. (private full-paper evidence dossier for arXiv:2605.14494, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| The reported mechanism centers on scenario, instance, embeddings, mathbf. | Method and formula evidence is bound to the named method headings and formula-specific operator audits. (private full-paper evidence dossier for arXiv:2605.14494, 4 Methodology) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Table 7 reports measured outcomes for PRISE across Problem, \hat{k}/\|\Xi\| (%) \,\downarrow / Mean, \hat{k}/\|\Xi\| (%) \,\downarrow / Med., % instances with \hat{k}/\|\Xi\|\leq \uparrow / 2%, % instances with \hat{k}/\|\Xi\|\leq \uparrow / 4%. | Quality-v2 paper-report result values: 1, 2, 4, 6 (private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2605.14494v1), [canonical PDF](https://arxiv.org/pdf/2605.14494v1), [canonical full-paper HTML](https://arxiv.org/html/2605.14494v1), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2605.14494). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2605.14494v1)*
- **Predecessor/prior work (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 1 Introduction; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2410.08863)*
- **Alternative or benchmark (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 5 Experiments; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/1903.02428)*
- **Code/data (bounded_not_found):** The bounded verified-URL receipt contains no official code/data artifact for this paper; no access error was recorded, so this is not labeled blocked. *(evidence locator: bounded online-vetting receipt for arXiv:2605.14494)*

Verified official primary-source links from the bounded check:

- No additional official code, data, project, venue, or benchmark URL was verified beyond the canonical record.

Access-blocked or unverified URL evidence: not recorded

Prior-work and alternatives evidence: "bounded_to_canonical_arxiv_record_and_paper_declared_primary_links" This is a bounded search record, not an exhaustive map of the field.

Code/data and reproduction evidence: "link_reachability_only; repository contents were not downloaded, built, or executed" Reachability and metadata do not mean that code or data were executed, that dependencies were installed, or that a reported result reproduced.

Paper-declared external candidates were recorded as follows:

- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/accessible_HTML.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/license/index.html#licenses-available
- Paper-declared URL, not opened in this phase: https://openreview.net/forum?id=CKXul9iX77
- Paper-declared URL, not opened in this phase: https://docs.gurobi.com/projects/optimizer/en/12.0/
- Paper-declared URL, not opened in this phase: https://proceedings.mlr.press/v235/wu24ag.html
- Paper-declared URL, not opened in this phase: https://openreview.net/forum?id=ryGs6iA5Km
- Paper-declared URL, not opened in this phase: https://math.nist.gov/~BMiller/LaTeXML/
- Paper-declared URL, not opened in this phase: https://github.com/arXiv/html_feedback/issues
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/issues
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/ourmembers.html

Their presence is discovery evidence, not proof that an artifact is official, available, licensed, runnable, or reproducing the paper. A later online-vetting phase should use primary sources, record HTTP/access limits, verify ownership and linkage, inspect release and license state, and distinguish artifact availability from runnable or result-reproducing status. Until then the publication status remains: arXiv preprint; no separate peer-reviewed venue inferred without an official venue source.

The isolated Black Lake checkout was used only for repository-readiness and dedupe context. A same-paper DEP-A would block a new owning record; a DEP-E or directly corresponding implementation is associated context rather than a duplicate. Background citations do not transfer evidence or claims to this paper.[^association]

## 9. Independent Re-conceptualization

Reviewer inference: the durable mechanism is the source-defined change centered on scenario, instance, embeddings, and mathbf, rather than the paper's brand name. This interpretation predicts that a matched intervention on scenario changes scenario; it is not an author claim or theorem.

Re-conceptualize the contribution as an evidence-linked state transition: pin source identity, record the method-specific decision, measure realized resource and outcome effects, and retain a conservative fallback whose trigger can be falsified on held-out conditions. This is reviewer inference and proposal, not an author claim and not an experimentally validated architecture.[^inference]

The mechanism can be viewed as a governed handoff between evidence, decision, execution, and outcome. Evidence identifies the source state and the signal the method uses. Decision records the action or representation chosen under a budget. Execution records what the system actually did, including fallback and resource use. Outcome records task quality and failure. The mapping is useful because it predicts what must be logged; it breaks when the paper studies a purely formal object with no operational transition.

A second bounded analogy is experimental portfolio control. Different baselines, budgets, and ablations are portfolio arms whose information access and cost must be matched. This analogy highlights selection bias and incomplete frontiers, but it does not imply that the paper uses an online bandit or that deployment should optimize only one scalar reward. Its falsifiable prediction is that the proposed mechanism's advantage should shrink when information access and complete cost are carefully matched if the original gain came mainly from comparison asymmetry.

## 10. Research Notes, Limitations, and Evidence Boundary

The complete local PDF and full-paper HTML for arXiv:2605.14494v1 were inspected. The PDF passed size, header, EOF, parse, page-count, title, structure, and references checks. The HTML passed size, readable-body, document-marker, heading, structure, title, and identity checks. Abstract HTML was metadata only and did not qualify as the paper body.[^integrity]

The coverage pass includes introduction, method or formal analysis, experiments or results, discussion or conclusion, references, appendices where exposed, tables, figures, equations, footnotes, disclosures, and code/data language. Extraction can lose visual layout and some mathematical semantics; the ledger records this boundary rather than claiming that every graphic was numerically reproduced.

Paper-specific qualification inventory: limitation/discussion terms prise, neurprise, propose, problem-driven, sequential, lookahead, heuristic, scenario, reduction, gnn-transformer; disclosure/funding language limitations; code/data language GitHub, checkpoint, Code, dataset; appendix headings Appendix Contents, Appendix A Notation, Appendix B PRISE: Method Details, Appendix C Optimization Problems, Appendix D NeurPRISE Architecture and Training, Appendix E Additional Experimental Results, Appendix F Ablation Studies, Appendix G Extended Analysis for CFLP. These are evidence pointers. A missing extracted term is not proof that a disclosure, artifact, or limitation does not exist.

Evidence layers remain explicit. Layer A is what the paper reports. Layer B contains the bounded primary records actually checked online; its conclusions are limited to the recorded identity, publication, and artifact-access evidence. Layer C is reviewer inference, including the governed-handoff interpretation. Layer D is a hypothesis or proposal, including deployment controls and falsification tests. A sentence is not silently promoted between layers.

Paper/prose/table consistency checks:

| Issue/check | Assessment | Source locator |
|---|---|---|
| Canonical ID, version, title, authors, PDF hash, and HTML hash were reconciled for arXiv:2605.14494v1; full quantitative table/prose/code consistency was not independently rerun. | identity consistency checked; quantitative and implementation consistency remain unresolved | source-integrity and online identity receipts for arXiv:2605.14494v1 |

Substantive evidence boundary: The profile binds arXiv:2605.14494v1 to a complete local PDF and full-paper HTML, 61 headings, 23 tables, 8 figures, and 371 extracted mathematical objects, and 2 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

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

### Hypothesis 1: Matched removal of scenario

**Proposition:** Reviewer hypothesis: the source-linked scenario operation is causally responsible for part of the reported scenario behavior.
**Predicted observation:** Removing or neutralizing scenario under matched data and compute will measurably weaken scenario.
**Falsifying observation:** A competent matched control without scenario preserves the same scenario distribution within uncertainty.
**Minimum test:** Run a paired, seed-controlled ablation at 5 Experiments and archive per-instance outcomes and resource use.
**Evidence locator:** private full-paper evidence dossier for arXiv:2605.14494, 4 Methodology, and 4.2.1 Model Architecture

### Hypothesis 2: Boundary transfer for Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty

**Proposition:** Reviewer hypothesis: the relation between scenario, and instance and scenario, and scenarios weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, and Motivation and setup.

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2605.14494, 5 Experiments, and Motivation and setup..
2. **Reproduce the end-to-end Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty path** Success: the source-defined scenario, instance, and embeddings and scenario, and scenarios are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4 Methodology, and 4.2.1 Model Architecture.
3. **Falsify the reviewer mechanism thesis for scenario** Success: a matched intervention on scenario predicts a corresponding change in scenario Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2605.14494, 4 Methodology, and 4.2.1 Model Architecture.

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty should be remembered as a tested relation between scenario, instance, and embeddings and scenario, scenarios, and Training under the configurations at 5 Experiments, and Motivation and setup., not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The Table 1 caption centers on instances, Table, Performance, comparison, small-scale, test, dash; its parsed headers include Prob., Method, SEL, Exact, across 18 rows and 160 cells.; result: column 2=5.45; column 3=25.9; column 4=4.57; column 5=53.0; column 6=3.44; column 7=63.4; column 8=2.83; column 9=64.5; caveat: Interpret Table 1 with its spanning headers and caption under 5 Experiments; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 1 caption and object |
| Table 2 | Purpose: The Table 2 caption centers on Table, Medium-, large-scale, comparison, test, instances, notation; its parsed headers include Prob., Scale, Method, SEL, Med., Exact, across 30 rows and 273 cells.; result: column 2=4.38; column 3=1.6; column 4=4.12; column 5=1.6; column 6=2.19; column 7=1.9; column 8=1.76; column 9=3.0; caveat: Interpret Table 2 with its spanning headers and caption under 5.1 Comparison Analysis; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 2 caption and object |
| Table 3 | Purpose: The Table 3 caption centers on Table, Generalization, times, problem, size.; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 3 with its spanning headers and caption under 5.3 Generalization; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 3 caption and object |
| Table 4 | Purpose: The Table 4 caption centers on Table, Scenario, generalization; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 4 with its spanning headers and caption under 5.3 Generalization; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 4 caption and object |
| Table 5 | Purpose: The Table 5 caption centers on Table, Distribution, shift, Normal; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 5 with its spanning headers and caption under 5.3 Generalization; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 5 caption and object |
| Table 6 | Purpose: The Table 6 caption centers on Table, Distribution, shift; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 6 with its spanning headers and caption under 5.3 Generalization; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 6 caption and object |
| Table 7 | Purpose: The Table 7 caption centers on Table, Compression, ratio, budget, denotes, percentage, instances; its parsed headers include \hat{k}/\|\Xi\| (%) \,\downarrow, % instances with \hat{k}/\|\Xi\|\leq \uparrow, N/C \,\downarrow, Problem, Method, Mean, Med., across 8 rows and 64 cells.; result: column 2=4.2; \hat{k}/\|\Xi\| (%) \,\downarrow=4.0; \hat{k}/\|\Xi\| (%) \,\downarrow=34.4; % instances with \hat{k}/\|\Xi\|\leq \uparrow=79.6; % instances with \hat{k}/\|\Xi\|\leq \uparrow=95.2; % instances with \hat{k}/\|\Xi\|\leq \uparrow=96.4; % instances with \hat{k}/\|\Xi\|\leq \uparrow=3.6; caveat: Interpret Table 7 with its spanning headers and caption under B.2 PRISE Compression Budget and Convergence Comparison; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 7 caption and object |
| Table 8 | Purpose: The Table 8 caption centers on Table, Node, edge, features, used, encoder, problem; its parsed headers include Prob., Node Features, d_{\text{node}}, Edge Features, d_{\text{edge}}, across 3 rows and 15 cells.; result: Node Features=4; d_{\text{node}}=8; d_{\text{edge}}=1; caveat: Interpret Table 8 with its spanning headers and caption under D.1.3 Problem-Specific Feature Engineering; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 8 caption and object |
| Table 9 | Purpose: The Table 9 caption centers on Table, Default, NeurPRISE, hyperparameters.; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 9 with its spanning headers and caption under Input normalization.; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 9 caption and object |
| Table 10 | Purpose: The Table 10 caption centers on Table, Small-scale, versus, target-scale, training, comparison.; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 10 with its spanning headers and caption under E.1.2 Do We Need Target-Scale Training?; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 10 caption and object |
| Table 11 | Purpose: The Table 11 caption centers on Table, Effect, training-set, size, in-distribution, generalization, performance.; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 11 with its spanning headers and caption under E.1.2 Do We Need Target-Scale Training?; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 11 caption and object |
| Table 12 | Purpose: The Table 12 caption centers on Table, Seed, variance, analysis, NeurPRISE, across, five; its parsed headers include Prob., Seed, k{=}1 \downarrow, k{=}2 \downarrow, k{=}4 \downarrow, k{=}6 \downarrow, SEL, across 13 rows and 68 cells.; result: column 2=5.86; column 2=0.22; column 3=2.30; column 3=0.09; column 4=0.83; column 4=0.07; column 5=0.52; column 5=0.06; caveat: Interpret Table 12 with its spanning headers and caption under E.2 Seed Variance Analysis; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 12 caption and object |
| Table 13 | Purpose: The Table 13 caption centers on Table, Time-budgeted, comparison., Both, methods, receive, same; its parsed headers include Prob., Scale, k, Budget, Regret (%) \downarrow, NeurPRISE, Time-budgeted MILP, across 6 rows and 28 cells.; result: k=4; Budget=1 s; Regret (%) \downarrow / NeurPRISE=6.10; Regret (%) \downarrow / Time-budgeted MILP=16.43; caveat: Interpret Table 13 with its spanning headers and caption under E.3 Time-Budgeted Exact Solver Comparison; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 13 caption and object |
| Table 14 | Purpose: The Table 14 caption centers on Table, Medium, instances.; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 14 with its spanning headers and caption under E.5 Scenario-Count Growth Control; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 14 caption and object |
| Table 15 | Purpose: The Table 15 caption centers on Table, Large, instances.; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 15 with its spanning headers and caption under E.5 Scenario-Count Growth Control; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 15 caption and object |
| Table 16 | Purpose: The Table 16 caption centers on Table, Encoder-fusion, ablation, small, instances, averaged, over; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 16 with its spanning headers and caption under F.2 Loss Comparison; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 16 caption and object |
| Table 17 | Purpose: The Table 17 caption centers on Table, Loss-function, ablation.; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 17 with its spanning headers and caption under F.2 Loss Comparison; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 17 caption and object |
| Table 18 | Purpose: The Table 18 caption centers on Table, CFLP, graph, encoding, features.; its parsed headers include Prob., Node Features, d_{\text{node}}, Edge Features, d_{\text{edge}}, across 2 rows and 10 cells.; result: Node Features=2; d_{\text{node}}=6; d_{\text{edge}}=1; caveat: Interpret Table 18 with its spanning headers and caption under G.2 Encoding and Training; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 18 caption and object |
| Table 19 | Purpose: The Table 19 caption centers on Table, Encoding, ablation, CFLP, small, scale., Result; its parsed headers include Encoding, Regret% ( \downarrow ), GPU (MB), s/epoch, Batch, across 3 rows and 15 cells.; result: Regret% ( \downarrow )=0.10; GPU (MB)=3,973; s/epoch=43; Batch=32; caveat: Interpret Table 19 with its spanning headers and caption under G.2 Encoding and Training; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 19 caption and object |
| Table 20 | Purpose: The Table 20 caption centers on Table, CFLP, performance, across, three, scales, than; its parsed headers include Method, Exact, across 9 rows and 60 cells.; result: Small / Reg. \downarrow / —=0.15; Small / Time / —=28.3; Medium / Reg. \downarrow / —=0.1; Medium / Time / —=38.7; Large / Reg. \downarrow / —=0.1; Large / Time / —=42.5; caveat: Interpret Table 20 with its spanning headers and caption under G.3 Performance and Generalization; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 20 caption and object |
| Table 21 | Purpose: The Table 21 caption centers on Table, CFLP, generalization.; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 21 with its spanning headers and caption under G.3 Performance and Generalization; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 21 caption and object |
| Table 22 | Purpose: The Table 22 caption centers on Table, CFLP, distribution, shift; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 22 with its spanning headers and caption under G.3 Performance and Generalization; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 22 caption and object |
| Table 23 | Purpose: The Table 23 caption centers on Table, CFLP, infeasibility, rate; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 23 with its spanning headers and caption under G.4 Feasibility Analysis; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2605.14494, Table 23 caption and object |
| Figure 1 | Purpose: The Figure 1 caption identifies a architecture or pipeline schematic centered on Right, NeurPRISE, Figure, illustrative, overview, approach., Left, PRISE.; result: The caption makes a qualitative claim about Right, NeurPRISE, Figure, illustrative, overview, approach.; no plotted value is inferred from pixels.; caveat: The caption under 3 Preliminaries was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2605.14494, Figure 1 caption and object |
| Algorithm 1 | Purpose: The Algorithm 1 caption identifies a paper-specific visual object centered on Algorithm, PRISE.; result: The caption makes a qualitative claim about Algorithm, PRISE; no plotted value is inferred from pixels.; caveat: The caption under 4.1 PRISE was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2605.14494, Algorithm 1 caption and object |
| Figure 2 panel (a) | Purpose: The Figure 2 panel (a) caption identifies a paper-specific visual object centered on Mean, marginal, gain, across, iterations..; result: The caption makes a qualitative claim about Mean, marginal, gain, across, iterations.; no plotted value is inferred from pixels.; caveat: The caption under B.2 PRISE Compression Budget and Convergence Comparison was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2605.14494, Figure 2 panel (a) caption and object |
| Figure 2 panel (b) | Purpose: The Figure 2 panel (b) caption identifies a paper-specific visual object centered on Distribution, PRISE, stop, steps..; result: The caption makes a qualitative claim about Distribution, PRISE, stop, steps.; no plotted value is inferred from pixels.; caveat: The caption under B.2 PRISE Compression Budget and Convergence Comparison was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2605.14494, Figure 2 panel (b) caption and object |
| Figure 2 | Purpose: The Figure 2 caption identifies a paper-specific visual object centered on PRISE, Figure, Empirical, analysis, small-scale, instances., Marginal, gains.; result: The caption makes a qualitative claim about PRISE, Figure, Empirical, analysis, small-scale, instances.; no plotted value is inferred from pixels.; caveat: The caption under B.2 PRISE Compression Budget and Convergence Comparison was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2605.14494, Figure 2 caption and object |
| Figure 3 | Purpose: The Figure 3 caption identifies a paper-specific visual object centered on form, Figure, Constraint, variable, bipartite, graph, scenario, MILP.; result: The caption makes a qualitative claim about form, Figure, Constraint, variable, bipartite, graph; no plotted value is inferred from pixels.; caveat: The caption under Feature Engineering. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2605.14494, Figure 3 caption and object |
| Figure 4 | Purpose: The Figure 4 caption identifies a paper-specific visual object centered on Figure, Regret, total, solve, time, instances, different, tolerances..; result: Caption-reported measured values: 50 instances; caveat: The caption under E.4 Speed–Quality Tradeoff via Solver Tolerance was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2605.14494, Figure 4 caption and object |
| Figure 5 | Purpose: The Figure 5 caption identifies a paper-specific visual object centered on Figure, Problem-specific, graph, CFLP..; result: The caption makes a qualitative claim about Figure, Problem-specific, graph, CFLP.; no plotted value is inferred from pixels.; caveat: The caption under G.2 Encoding and Training was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2605.14494, Figure 5 caption and object |
| Equations | 371 distinct mathematical renderings exposed by HTML; representative objects listed in Section 2.2. | Central objects were inventoried with sign, normalization, conditioning, and denominator checks; no numerical reproduction. |
| Sections | 61 headings exposed by the full HTML. | Every heading was screened; method, evaluation, results, limitations, references, and appendices were mapped where present. |

Appendix and supplementary coverage:

- Appendix Contents
- Appendix A Notation
- Appendix B PRISE: Method Details
- Appendix C Optimization Problems
- Appendix D NeurPRISE Architecture and Training
- Appendix E Additional Experimental Results
- Appendix F Ablation Studies
- Appendix G Extended Analysis for CFLP

Complete section inventory:

- Report GitHub Issue
- Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty Tianjue Lin 1 Jianan Zhou 1 Jieyi Bi 1 Yaoxin Wu 2 Wen Song 3 Zhiguang Cao 4 Jie Zhang 1 1 Nanyang Technological University 2 Eindhoven University of Technology 3 Shandong University 4 Singapore Management University {tianjue002, jianan004, jieyi001}@e.ntu.edu.sg, y.wu2@tue.nl, wensong@email.sdu.edu.cn, zgcao@smu.edu.sg, zhangj@ntu.edu.sg Corresponding author.
- Abstract
- 1 Introduction
- 2 Related Work
- 3 Preliminaries
- 4 Methodology
- 4.1 PRISE
- 4.2 NeurPRISE
- 4.2.1 Model Architecture
- 4.2.2 Loss Function
- 5 Experiments
- 5.1 Comparison Analysis
- 5.2 Flexibility and Scalability
- 5.3 Generalization
- 6 Conclusion
- References
- Appendix Contents
- Appendix A Notation
- Appendix B PRISE: Method Details
- B.1 Monotonicity of the reduced-scenario objective value
- Proposition 1 (Monotonicity under set inclusion) .
- Proof.
- Remark 1 (Non-submodularity of V V ) .
- Counterexample.
- PRISE trace on this instance.
- Submodularity violation.
- B.2 PRISE Compression Budget and Convergence Comparison
- Labeling cost.
- B.3 Connection to Column-and-Constraint Generation
- Appendix C Optimization Problems
- C.1 Deterministic-Equivalent MILP Reformulation
- C.2 Problem Descriptions
- Selection Problem (SEL).
- Vertex Cover (VC).
- Appendix D NeurPRISE Architecture and Training
- D.1 Encoding
- D.1.1 Bipartite Graph Representation
- D.1.2 GINE Architecture
- D.1.3 Problem-Specific Feature Engineering
- Feature Engineering.
- D.2 Training Details
- Input normalization.
- Appendix E Additional Experimental Results
- E.1 Generalization
- E.1.1 Distribution Shift
- Motivation and setup.
- E.1.2 Do We Need Target-Scale Training?
- E.2 Seed Variance Analysis
- E.3 Time-Budgeted Exact Solver Comparison
- E.4 Speed–Quality Tradeoff via Solver Tolerance
- E.5 Scenario-Count Growth Control
- Appendix F Ablation Studies
- F.1 Encoding and Fusion Strategy
- F.2 Loss Comparison
- Appendix G Extended Analysis for CFLP
- G.1 Problem Formulation
- G.2 Encoding and Training
- Training configuration.
- G.3 Performance and Generalization
- G.4 Feasibility Analysis

This ledger is completeness evidence, not reproduction. It records that each exposed section and numbered object was screened without reproducing the paper's tables, figures, or long captions.

## 16. Source and Evidence Notes

- Canonical arXiv record: https://arxiv.org/abs/2605.14494v1
- Canonical PDF: https://arxiv.org/pdf/2605.14494v1
- Canonical full-paper HTML: https://arxiv.org/html/2605.14494v1
- arXiv DOI resolver: https://doi.org/10.48550/arXiv.2605.14494
- Reviewed identity: arXiv:2605.14494v1
- Complete authors: Tianjue Lin; Jianan Zhou; Jieyi Bi; Yaoxin Wu; Wen Song; Zhiguang Cao; Jie Zhang
- Locally archived full PDF and full-paper HTML were verified; private path withheld.
- No source PDF, HTML, archive, extracted text, validator, or private index belongs in the public DEP-A package.
- Online primary-source vetting status: performed and receipt-linked; alternatives are not exhaustive and no experiment was independently reproduced.

## 17. Footnotes

[^source-paper]: Canonical paper identity and version are linked at https://arxiv.org/abs/2605.14494v1; the locally archived complete PDF and full-paper HTML were reconciled to this identity.
[^scope]: Paper report means content attributable to the authors and supported by the reviewed artifact; it is not independent reproduction.
[^integrity]: Source integrity requires a matching complete PDF and full-paper HTML with identity, version, title, structure, references, and readable-body checks.
[^inference]: Reviewer inference labels a mechanism-level interpretation derived from source evidence rather than asserted by the authors.
[^external]: External primary evidence was limited to receipt-linked official records and URLs. Availability or publication status does not imply artifact runnability, result reproduction, or exhaustive prior-work coverage.
[^association]: An associated DEP is contextual evidence, not a duplicate and not proof of the reviewed paper's claims.
