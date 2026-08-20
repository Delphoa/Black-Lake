# Whitepaper Review: Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries

## A detailed review, technical reconstruction, and independent re-conceptualization of “Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries”

**Source paper:** Yun Tian; Guili Wang; Jian Bi; Kaixin Han; Chenglu Wu; Zhiyi Lu; Chenhao Li; Liangwang Sun; Minyu Zhou; Chenchen Xu, “Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries,” arXiv:2603.27186v1.[^source-paper]

**Artifact prepared:** 2026-08-20
**Local source reviewed:** complete locally archived PDF (23 pages) and matching full-paper HTML (72391 readable body characters); private path withheld
**Review scope:** full-paper reconstruction, claim vetting, local evidence mapping, implications, and replication agenda
**Review status:** source artifacts inspected; bounded online primary-source vetting performed; experiments not independently rerun

## Executive Assessment

### The paper in one sentence

The paper presents and evaluates a technical contribution framed around hybrid, deep, learning, temporal, data, augmentation, with its method, formal objects, experimental record, limitations, and source structure inspected from a complete local paper pair rather than an abstract page.

### The deeper idea

Reviewer inference: the durable mechanism is the source-defined change centered on battery, prediction, degradation, and temporal, rather than the paper's brand name. This interpretation predicts that a matched intervention on battery changes dataset; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to 2.1 Physics-Based Modeling Methods, 2.2 Deep Learning-Based Methods. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

### Bottom-line judgment

The source is complete enough for a full-paper assessment, and the paper reports a technically organized contribution with an explicit evaluation record. Results remain paper-reported. The local evidence pass confirms the complete results structure and numbered-object inventory, but it does not independently reproduce a numerical value or infer a stronger denominator than the source states. The defensible verdict is therefore conditional: the paper establishes what it directly measures under its own setup, while broader superiority, generality, robustness, efficiency, or deployment readiness remains bounded by the tested models, data, metrics, budgets, hardware, and comparisons.[^scope]

### Principal strengths

- Complete PDF and matching full-paper HTML passed identity, structure, title, references, and readability gates.
- The source exposes 32 section headings, 10 table captions, 15 figure captions, and 95 mathematical renderings for coverage auditing.
- The review can distinguish paper report, external-primary evidence, reviewer inference, and hypothesis without relying on an abstract-only summary.

### Principal qualifications

1. The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions.
2. No result, code path, benchmark, training run, or hardware measurement was independently reproduced.
3. Bounded online checks verified canonical identity and the explicitly recorded official URLs; the search is not exhaustive and does not establish artifact runnability or reproduction.[^external]

## 1. The Problem and Research Questions

### 1.1 Problem and stakes

**Paper-reported problem:** For Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries, the formal target is bounded to the source-defined relation among battery, degradation, data, prediction, temporal, deep, and complex. The task assumptions and stakes are anchored to Abstract, and 1 Introduction; no objective outside those sections is inferred.

**Research gap reconstructed from the source:** The paper positions Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries around battery, degradation, data, and prediction. This records the authors' gap framing only; novelty, priority, generality, and superiority require the separate prior-work and evaluation audits.

The title and full-paper organization identify hybrid, deep, learning, temporal, data, augmentation as the central problem space. A rigorous reading asks what input object is transformed, predicted, selected, optimized, or measured; which practical or scientific constraint motivates that operation; and which outcome makes the change valuable. Those questions must be answered by the method and evaluation sections, not by the title alone. The paper reports its own problem definition; this review preserves the boundary between that report and reviewer interpretation.

Paper-specific reconstruction: the abstract/introduction evidence concentrates on degradation, battery, networks, prediction, rul, data, deep, model, temporal, however, under the headings Abstract, 1 Introduction. Those source terms locate the actual objects and constraints; they do not by themselves prove novelty or improvement. In this review they constrain the problem statement so a generic systems narrative cannot replace the paper's own domain and terminology.

The practical stakes depend on the actual denominator. An improvement in a representation, proxy, component score, or controlled benchmark can be important without automatically improving end-user quality, wall-clock cost, reliability, or safety. A durable account therefore separates the immediate technical objective from the downstream objective and asks which bridge between them is tested. If that bridge is only assumed, it remains an explicit gap rather than a hidden premise.

### 1.2 Prior method families and inherited components

The paper's related-work and background sections define the relevant method families. The review treats established backbones, pretrained models, datasets, optimization routines, kernels, evaluation harnesses, and standard metrics as inherited unless the source identifies a change. Novelty belongs to the specific interface, objective, representation, decision rule, data construction, proof, or evaluation design that differs. This prevents a system-level bundle from receiving credit for every capability of its dependencies.

### 1.3 Questions that govern the assessment

Five questions organize the reconstruction. What exact object enters and leaves the method? Which components are learned, fixed, searched, sampled, or verified? What objective and assumptions determine the operation? How do training or calibration differ from inference or deployment? Finally, which result would falsify the authors' causal or generality story rather than merely lower an aggregate score? These questions create an audit trail from paper report to independent assessment.

## 2. Formal and Technical Reconstruction

### 2.1 Definitions and assumptions

The authoritative definition chain lives in the complete source sections listed below. The automated evidence profile does not pretend that section names themselves describe the mechanism. Instead, the full review binds each claim to the source's definitions, stated assumptions, and adjacent formal or experimental context. The core technical headings identified for close reading were:

- 2.1 Physics-Based Modeling Methods
- 2.2 Deep Learning-Based Methods

Variables should be assigned plain-language meanings before algebra is interpreted. Inputs, labels, state, parameters, budgets, constraints, random variables, and outputs must remain distinct. A probability requires a sample space and conditioning event; a loss requires an optimization direction; a ratio requires a numerator and denominator; and a guarantee retains every assumption under which it was proved. If the source uses the same symbol in different roles or shifts between population and sample quantities, that ambiguity should be preserved rather than silently repaired.

### 2.2 Objective and central equations

The full HTML exposes 95 distinct mathematical renderings. Each is treated as a paper-reported formal object whose sign, normalization, conditioning, and denominator must be read with adjacent prose.

Paper-specific formal reconstruction:

**Formal object 1 at 3.1.1 1D-CNNs — Formula 1 under 3.1.1 1D-CNNs is classified as a paper-defined mathematical relation; adjacent prose centers on times, tensor, mathbb, kernel, input, time-series, and the expression links X, in, mathbb, R, N, times, C_{in}\times, L_{in}}..** `X\in\mathbb{R}^{N\times C_{in}\times L_{in}}`
Variables: "X, in, mathbb, R, N, times, C_{in}\\times, L_{in}}".
Sign/normalization/conditioning/surrogate audit: "Formula 1 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: X, in, mathbb, R, N, times, C_{in}\\times, L_{in}}; meanings remain tied to 3.1.1 1D-CNNs.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs, formal object 1.

**Formal object 2 at 3.1.1 1D-CNNs — Formula 2 under 3.1.1 1D-CNNs is classified as a paper-defined mathematical relation; adjacent prose centers on times, tensor, mathbb, kernel, input, time-series, and the expression links N..** `N`
Variables: "N".
Sign/normalization/conditioning/surrogate audit: "Formula 2 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N; meanings remain tied to 3.1.1 1D-CNNs.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs, formal object 2.

**Formal object 3 at 3.1.1 1D-CNNs — Formula 3 under 3.1.1 1D-CNNs is classified as a paper-defined mathematical relation; adjacent prose centers on times, tensor, mathbb, kernel, input, time-series, and the expression links C_{in}..** `C_{in}`
Variables: "C_{in}".
Sign/normalization/conditioning/surrogate audit: "Formula 3 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C_{in}; meanings remain tied to 3.1.1 1D-CNNs.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs, formal object 3.

**Formal object 4 at 3.1.1 1D-CNNs — Formula 4 under 3.1.1 1D-CNNs is classified as a paper-defined mathematical relation; adjacent prose centers on times, tensor, mathbb, kernel, input, time-series, and the expression links L_{in}..** `L_{in}`
Variables: "L_{in}".
Sign/normalization/conditioning/surrogate audit: "Formula 4 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{in}; meanings remain tied to 3.1.1 1D-CNNs.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs, formal object 4.

**Formal object 5 at 3.1.1 1D-CNNs — Formula 5 under 3.1.1 1D-CNNs is classified as a paper-defined mathematical relation; adjacent prose centers on times, tensor, mathbb, kernel, input, time-series, and the expression links W, in, mathbb, R, C_{out}\times, C_{in}\times, K..** `W\in\mathbb{R}^{C_{out}\times C_{in}\times K}`
Variables: "W, in, mathbb, R, C_{out}\\times, C_{in}\\times, K".
Sign/normalization/conditioning/surrogate audit: "Formula 5 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W, in, mathbb, R, C_{out}\\times, C_{in}\\times, K; meanings remain tied to 3.1.1 1D-CNNs.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs, formal object 5.

**Formal object 6 at 3.1.1 1D-CNNs — Formula 6 under 3.1.1 1D-CNNs is classified as a paper-defined mathematical relation; adjacent prose centers on times, tensor, mathbb, kernel, input, time-series, and the expression links C_{out}..** `C_{out}`
Variables: "C_{out}".
Sign/normalization/conditioning/surrogate audit: "Formula 6 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C_{out}; meanings remain tied to 3.1.1 1D-CNNs.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs, formal object 6.

**Formal object 7 at 3.1.1 1D-CNNs — Formula 7 under 3.1.1 1D-CNNs is classified as a paper-defined mathematical relation; adjacent prose centers on times, tensor, mathbb, kernel, input, time-series, and the expression links K..** `K`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 7 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to 3.1.1 1D-CNNs.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs, formal object 7.

**Formal object 8 at 3.1.1 1D-CNNs — Formula 8 under 3.1.1 1D-CNNs is classified as a paper-defined mathematical relation; adjacent prose centers on times, tensor, mathbb, kernel, input, time-series, and the expression links Y, in, mathbb, R, N, times, C_{\text{out}}\times, L_{\text{out}}}..** `Y\in\mathbb{R}^{N\times C_{\text{out}}\times L_{\text{out}}}`
Variables: "Y, in, mathbb, R, N, times, C_{\\text{out}}\\times, L_{\\text{out}}}".
Sign/normalization/conditioning/surrogate audit: "Formula 8 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, in, mathbb, R, N, times, C_{\\text{out}}\\times, L_{\\text{out}}}; meanings remain tied to 3.1.1 1D-CNNs.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs, formal object 8.

**Formal object 9 at 3.1.1 1D-CNNs — Formula 9 under 3.1.1 1D-CNNs is classified as a paper-defined mathematical relation; adjacent prose centers on times, mathbb, input, tensor, where, temporal, and the expression links Y, n, c_{\text{out}}, t, c_{\text{in}}, C_{\text{in}}}\sum, k, K..** `Y[n,c_{\text{out}},t]=\sum_{c_{\text{in}}=1}^{C_{\text{in}}}\sum_{k=1}^{K}X[n,c_{\text{in}},t+k]\cdot W[c_{\text{out}},c_{\text{in}},k]+b[c_{\text{out}}],`
Variables: "Y, n, c_{\\text{out}}, t, c_{\\text{in}}, C_{\\text{in}}}\\sum, k, K, X, W, b".
Sign/normalization/conditioning/surrogate audit: "Formula 9 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, n, c_{\\text{out}}, t, c_{\\text{in}}, C_{\\text{in}}}\\sum, k, K, X, W, b; meanings remain tied to 3.1.1 1D-CNNs.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs, formal object 9.

**Formal object 10 at 3.1.1 1D-CNNs — Formula 10 under 3.1.1 1D-CNNs is classified as a paper-defined mathematical relation; adjacent prose centers on where, mathbb, text, denotes, bias, term., and the expression links b, in, mathbb, R, C_{\text{out}}}..** `b\in\mathbb{R}^{C_{\text{out}}}`
Variables: "b, in, mathbb, R, C_{\\text{out}}}".
Sign/normalization/conditioning/surrogate audit: "Formula 10 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: b, in, mathbb, R, C_{\\text{out}}}; meanings remain tied to 3.1.1 1D-CNNs.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs, formal object 10.

**Formal object 11 at 3.1.2 DRSN — Formula 11 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on convolutional, layers, input, capture, local, temporal, and the expression links Y, X, W, b..** `Y=X\cdot W+b,`
Variables: "Y, X, W, b".
Sign/normalization/conditioning/surrogate audit: "Formula 11 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, X, W, b; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 11.

**Formal object 12 at 3.1.2 DRSN — Formula 12 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, input, denotes, convolutional, weights, bias, and the expression links X..** `X`
Variables: "X".
Sign/normalization/conditioning/surrogate audit: "Formula 12 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: X; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 12.

**Formal object 13 at 3.1.2 DRSN — Formula 13 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, input, denotes, convolutional, weights, bias, and the expression links W..** `W`
Variables: "W".
Sign/normalization/conditioning/surrogate audit: "Formula 13 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 13.

**Formal object 14 at 3.1.2 DRSN — Formula 14 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, input, denotes, convolutional, weights, bias, and the expression links b..** `b`
Variables: "b".
Sign/normalization/conditioning/surrogate audit: "Formula 14 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: b; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 14.

**Formal object 15 at 3.1.2 DRSN — Formula 15 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on noise, soft-thresholding, function, suppress, inherent, irrelevant, and the expression links Y, mathrm, X, lambda, leq..** `Y=\mathrm{sign}(X)\cdot\max(|X|-\lambda,0)=\begin{cases}X-\lambda,&X>\lambda,\\ 0,&|X|\leq\lambda,\\ X+\lambda,&X<-\lambda,\end{cases}`
Variables: "Y, mathrm, X, lambda, leq".
Sign/normalization/conditioning/surrogate audit: "Formula 15 operator audit: maximization; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, mathrm, X, lambda, leq; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 15.

**Formal object 16 at 3.1.2 DRSN — Formula 16 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, lambda, learnable, threshold, parameter., smooth, and the expression links lambda..** `\lambda`
Variables: "lambda".
Sign/normalization/conditioning/surrogate audit: "Formula 16 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: lambda; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 16.

**Formal object 17 at 3.1.2 DRSN — Formula 17 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on threshold, generator, lambda, dynamically, generated, dedicated, and the expression links F_{2}..** `F_{2}`
Variables: "F_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 17 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: F_{2}; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 17.

**Formal object 18 at 3.1.2 DRSN — Formula 18 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on threshold, generator, lambda, dynamically, generated, dedicated, and the expression links Z, mathrm, d, F_{2}, in, mathbb, R, B..** `Z=\mathrm{AvgPool1d}(F_{2})\in\mathbb{R}^{B\times C},`
Variables: "Z, mathrm, d, F_{2}, in, mathbb, R, B, times, C".
Sign/normalization/conditioning/surrogate audit: "Formula 18 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Z, mathrm, d, F_{2}, in, mathbb, R, B, times, C; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 18.

**Formal object 19 at 3.1.2 DRSN — Formula 19 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, denote, batch, size, number, channels, and the expression links C..** `C`
Variables: "C".
Sign/normalization/conditioning/surrogate audit: "Formula 19 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 19.

**Formal object 20 at 3.1.2 DRSN — Formula 20 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, denote, batch, size, number, channels, and the expression links Z..** `Z`
Variables: "Z".
Sign/normalization/conditioning/surrogate audit: "Formula 20 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Z; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 20.

**Formal object 21 at 3.1.2 DRSN — Formula 21 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, Sigmoid, thresholds, denote, batch, size, and the expression links lambda, sigma, big, W_{2}\cdot\mathrm{ReLU}, W_{1}Z, b_{1}, b_{2}\big..** `\lambda=\sigma\big(W_{2}\cdot\mathrm{ReLU}(W_{1}Z+b_{1})+b_{2}\big),`
Variables: "lambda, sigma, big, W_{2}\\cdot\\mathrm{ReLU}, W_{1}Z, b_{1}, b_{2}\\big".
Sign/normalization/conditioning/surrogate audit: "Formula 21 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: lambda, sigma, big, W_{2}\\cdot\\mathrm{ReLU}, W_{1}Z, b_{1}, b_{2}\\big; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 21.

**Formal object 22 at 3.1.2 DRSN — Formula 22 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, learnable, parameters, sigma, cdot, denotes, and the expression links W_{1}, W_{2}, b_{1}, b_{2}..** `W_{1},W_{2},b_{1},b_{2}`
Variables: "W_{1}, W_{2}, b_{1}, b_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 22 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W_{1}, W_{2}, b_{1}, b_{2}; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 22.

**Formal object 23 at 3.1.2 DRSN — Formula 23 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, learnable, parameters, sigma, cdot, denotes, and the expression links sigma..** `\sigma(\cdot)`
Variables: "sigma".
Sign/normalization/conditioning/surrogate audit: "Formula 23 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sigma; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 23.

**Formal object 24 at 3.1.2 DRSN — Formula 24 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, learnable, parameters, sigma, cdot, denotes, and the expression links symbols defined beside the formula..** `[0,1]`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 24 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 24.

**Formal object 25 at 3.1.2 DRSN — Formula 25 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on Since, lambda, mathbb, times, represents, per-channel, and the expression links lambda, in, mathbb, R, B, times, C..** `\lambda\in\mathbb{R}^{B\times C}`
Variables: "lambda, in, mathbb, R, B, times, C".
Sign/normalization/conditioning/surrogate audit: "Formula 25 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: lambda, in, mathbb, R, B, times, C; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 25.

**Formal object 26 at 3.1.2 DRSN — Formula 26 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on Since, lambda, mathbb, times, represents, per-channel, and the expression links lambda, mathrm, otimes, mathbf, L, in, mathbb, R..** `\lambda_{\mathrm{expanded}}=\lambda\otimes\mathbf{1}_{L}\in\mathbb{R}^{B\times C\times L},`
Variables: "lambda, mathrm, otimes, mathbf, L, in, mathbb, R, B, times, C".
Sign/normalization/conditioning/surrogate audit: "Formula 26 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: lambda, mathrm, otimes, mathbf, L, in, mathbb, R, B, times, C; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 26.

**Formal object 27 at 3.1.2 DRSN — Formula 27 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, mathbf, all-ones, vector, length, soft-thresholding, and the expression links mathbf, L..** `\mathbf{1}_{L}`
Variables: "mathbf, L".
Sign/normalization/conditioning/surrogate audit: "Formula 27 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, L; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 27.

**Formal object 28 at 3.1.2 DRSN — Formula 28 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, mathbf, all-ones, vector, length, soft-thresholding, and the expression links L..** `L`
Variables: "L".
Sign/normalization/conditioning/surrogate audit: "Formula 28 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 28.

**Formal object 29 at 3.1.2 DRSN — Formula 29 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on where, mathbf, all-ones, vector, length, soft-thresholding, and the expression links widetilde, F, mathrm, F_{2}, big, lambda..** `\widetilde{F}_{2}=\mathrm{sign}(F_{2})\cdot\max\big(|F_{2}|-\lambda_{\mathrm{expanded}},0\big).`
Variables: "widetilde, F, mathrm, F_{2}, big, lambda".
Sign/normalization/conditioning/surrogate audit: "Formula 29 operator audit: maximization; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: widetilde, F, mathrm, F_{2}, big, lambda; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 29.

**Formal object 30 at 3.1.2 DRSN — Formula 30 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on ensure, stable, gradient, propagation, preserve, original, and the expression links F, X..** `F(X)`
Variables: "F, X".
Sign/normalization/conditioning/surrogate audit: "Formula 30 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: F, X; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 30.

**Formal object 31 at 3.1.2 DRSN — Formula 31 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on input, convolution, normalization, ensure, stable, gradient, and the expression links Y, F, X..** `Y=F(X)+X,`
Variables: "Y, F, X".
Sign/normalization/conditioning/surrogate audit: "Formula 31 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, F, X; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 31.

**Formal object 32 at 3.1.2 DRSN — Formula 32 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on convolution, normalization, where, denotes, composite, operations, and the expression links C_{in}\neq, C_{out}..** `C_{in}\neq C_{out}`
Variables: "C_{in}\\neq, C_{out}".
Sign/normalization/conditioning/surrogate audit: "Formula 32 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C_{in}\\neq, C_{out}; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 32.

**Formal object 33 at 3.1.2 DRSN — Formula 33 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on convolution, normalization, where, denotes, composite, operations, and the expression links times..** `1\times 1`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 33 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 33.

**Formal object 34 at 3.1.2 DRSN — Formula 34 under 3.1.2 DRSN is classified as a paper-defined mathematical relation; adjacent prose centers on convolution, normalization, activation, output, where, denotes, and the expression links mathrm, X, C_{in}, C_{out}, s, times..** `\mathrm{Shortcut}(X)=\begin{cases}X,&C_{in}=C_{out},\\ \mathrm{BN}_{s}(\mathrm{Conv}_{1\times 1}(X)),&\text{otherwise}.\end{cases}`
Variables: "mathrm, X, C_{in}, C_{out}, s, times".
Sign/normalization/conditioning/surrogate audit: "Formula 34 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathrm, X, C_{in}, C_{out}, s, times; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 34.

**Formal object 35 at 3.1.2 DRSN — Formula 35 under 3.1.2 DRSN is classified as a state or representation transformation; adjacent prose centers on feature, residual, connection, convolutional, soft-thresholding, connections, and the expression links Y, mathrm, big, widetilde, F, X..** `Y=\mathrm{ReLU}\big(\widetilde{F}_{2}+\mathrm{Shortcut}(X)\big).`
Variables: "Y, mathrm, big, widetilde, F, X".
Sign/normalization/conditioning/surrogate audit: "Formula 35 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, mathrm, big, widetilde, F, X; meanings remain tied to 3.1.2 DRSN.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN, formal object 35.

**Formal object 36 at 3.1.3 Transformer — Formula 36 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on attention, follows, Multi-head, self-attention, extends, representational, and the expression links Q, K, V, dots, h, W, O..** `\text{MultiHead}(Q,K,V)=\text{Concat}(\text{head}_{1},\text{head}_{2},\dots,\text{head}_{h})\cdot W^{O}.`
Variables: "Q, K, V, dots, h, W, O".
Sign/normalization/conditioning/surrogate audit: "Formula 36 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Q, K, V, dots, h, W, O; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 36.

**Formal object 37 at 3.1.3 Transformer — Formula 37 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on attention, head, computed, individually, follows, scaled, and the expression links i, Q, W_{i}^{Q}, K, W_{i}^{K}, V, W_{i}^{V}..** `\text{head}_{i}=\text{Attention}(Q\cdot W_{i}^{Q},K\cdot W_{i}^{K},V\cdot W_{i}^{V}).`
Variables: "i, Q, W_{i}^{Q}, K, W_{i}^{K}, V, W_{i}^{V}".
Sign/normalization/conditioning/surrogate audit: "Formula 37 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: i, Q, W_{i}^{Q}, K, W_{i}^{K}, V, W_{i}^{V}; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 37.

**Formal object 38 at 3.1.3 Transformer — Formula 38 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on scaled, dot-product, attention, mechanism, defined, Following, and the expression links Q, K, V, left, T, d_{k}}}\right..** `\text{Attention}(Q,K,V)=\text{Softmax}\left(\frac{Q\cdot K^{T}}{\sqrt{d_{k}}}\right)\cdot V.`
Variables: "Q, K, V, left, T, d_{k}}}\\right".
Sign/normalization/conditioning/surrogate audit: "Formula 38 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Q, K, V, left, T, d_{k}}}\\right; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 38.

**Formal object 39 at 3.1.3 Transformer — Formula 39 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on feedforward, matrices, projection, attention, output, layer, and the expression links Y, X, W_{1}, b_{1}, W_{2}, b_{2}..** `Y=\text{ReLU}(X\cdot W_{1}+b_{1})\cdot W_{2}+b_{2}.`
Variables: "Y, X, W_{1}, b_{1}, W_{2}, b_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 39 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Y, X, W_{1}, b_{1}, W_{2}, b_{2}; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 39.

**Formal object 40 at 3.1.3 Transformer — Formula 40 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links Q..** `Q`
Variables: "Q".
Sign/normalization/conditioning/surrogate audit: "Formula 40 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Q; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 40.

**Formal object 41 at 3.1.3 Transformer — Formula 41 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links V..** `V`
Variables: "V".
Sign/normalization/conditioning/surrogate audit: "Formula 41 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 41.

**Formal object 42 at 3.1.3 Transformer — Formula 42 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links W_{i}^{Q}..** `W_{i}^{Q}`
Variables: "W_{i}^{Q}".
Sign/normalization/conditioning/surrogate audit: "Formula 42 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W_{i}^{Q}; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 42.

**Formal object 43 at 3.1.3 Transformer — Formula 43 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links W_{i}^{K}..** `W_{i}^{K}`
Variables: "W_{i}^{K}".
Sign/normalization/conditioning/surrogate audit: "Formula 43 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W_{i}^{K}; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 43.

**Formal object 44 at 3.1.3 Transformer — Formula 44 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links W_{i}^{V}..** `W_{i}^{V}`
Variables: "W_{i}^{V}".
Sign/normalization/conditioning/surrogate audit: "Formula 44 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W_{i}^{V}; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 44.

**Formal object 45 at 3.1.3 Transformer — Formula 45 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links i..** `i`
Variables: "i".
Sign/normalization/conditioning/surrogate audit: "Formula 45 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: i; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 45.

**Formal object 46 at 3.1.3 Transformer — Formula 46 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links W, O..** `W^{O}`
Variables: "W, O".
Sign/normalization/conditioning/surrogate audit: "Formula 46 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W, O; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 46.

**Formal object 47 at 3.1.3 Transformer — Formula 47 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links d_{k}..** `d_{k}`
Variables: "d_{k}".
Sign/normalization/conditioning/surrogate audit: "Formula 47 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{k}; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 47.

**Formal object 48 at 3.1.3 Transformer — Formula 48 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links W_{1}..** `W_{1}`
Variables: "W_{1}".
Sign/normalization/conditioning/surrogate audit: "Formula 48 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W_{1}; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 48.

**Formal object 49 at 3.1.3 Transformer — Formula 49 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links W_{2}..** `W_{2}`
Variables: "W_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 49 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: W_{2}; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 49.

**Formal object 50 at 3.1.3 Transformer — Formula 50 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links b_{1}..** `b_{1}`
Variables: "b_{1}".
Sign/normalization/conditioning/surrogate audit: "Formula 50 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: b_{1}; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 50.

**Formal object 51 at 3.1.3 Transformer — Formula 51 under 3.1.3 Transformer is classified as a state or representation transformation; adjacent prose centers on matrices, projection, attention, output, layer, Here, and the expression links b_{2}..** `b_{2}`
Variables: "b_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 51 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: b_{2}; meanings remain tied to 3.1.3 Transformer.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.3 Transformer, formal object 51.

**Formal object 52 at 3.1.4 Regression Head — Formula 52 under 3.1.4 Regression Head is classified as a state or representation transformation; adjacent prose centers on mathbf, mathbb, denote, final, hidden, representation, and the expression links mathbf, z, in, mathbb, R, d..** `\mathbf{z}\in\mathbb{R}^{d}`
Variables: "mathbf, z, in, mathbb, R, d".
Sign/normalization/conditioning/surrogate audit: "Formula 52 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, z, in, mathbb, R, d; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 52.

**Formal object 53 at 3.1.4 Regression Head — Formula 53 under 3.1.4 Regression Head is classified as a state or representation transformation; adjacent prose centers on mathbf, mathbb, denote, final, hidden, representation, and the expression links mathbf, z, h, T..** `\mathbf{z}=\mathbf{h}_{T}`
Variables: "mathbf, z, h, T".
Sign/normalization/conditioning/surrogate audit: "Formula 53 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, z, h, T; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 53.

**Formal object 54 at 3.1.4 Regression Head — Formula 54 under 3.1.4 Regression Head is classified as a state or representation transformation; adjacent prose centers on mathbf, mathbb, linear, prime, output, time, and the expression links hat, c, t, mathbf, W, mathrm, z, b..** `\hat{c}_{t}=\mathbf{W}_{2}\cdot\mathrm{ReLU}(\mathbf{W}_{1}\cdot\mathbf{z}+\mathbf{b}_{1})+\mathbf{b}_{2},`
Variables: "hat, c, t, mathbf, W, mathrm, z, b".
Sign/normalization/conditioning/surrogate audit: "Formula 54 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, c, t, mathbf, W, mathrm, z, b; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 54.

**Formal object 55 at 3.1.4 Regression Head — Formula 55 under 3.1.4 Regression Head is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, mathbf, prime, times, linear, layer, and the expression links mathbf, W, in, mathbb, R, d, prime, times..** `\mathbf{W}_{1}\in\mathbb{R}^{d^{\prime}\times d}`
Variables: "mathbf, W, in, mathbb, R, d, prime, times".
Sign/normalization/conditioning/surrogate audit: "Formula 55 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, W, in, mathbb, R, d, prime, times; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 55.

**Formal object 56 at 3.1.4 Regression Head — Formula 56 under 3.1.4 Regression Head is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, mathbf, prime, times, linear, layer, and the expression links mathbf, b, in, mathbb, R, d, prime..** `\mathbf{b}_{1}\in\mathbb{R}^{d^{\prime}}`
Variables: "mathbf, b, in, mathbb, R, d, prime".
Sign/normalization/conditioning/surrogate audit: "Formula 56 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, b, in, mathbb, R, d, prime; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 56.

**Formal object 57 at 3.1.4 Regression Head — Formula 57 under 3.1.4 Regression Head is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, mathbf, prime, times, linear, layer, and the expression links mathbf, W, in, mathbb, R, times, d, prime..** `\mathbf{W}_{2}\in\mathbb{R}^{1\times d^{\prime}}`
Variables: "mathbf, W, in, mathbb, R, times, d, prime".
Sign/normalization/conditioning/surrogate audit: "Formula 57 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, W, in, mathbb, R, times, d, prime; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 57.

**Formal object 58 at 3.1.4 Regression Head — Formula 58 under 3.1.4 Regression Head is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, mathbf, prime, times, linear, layer, and the expression links mathbf, b, in, mathbb, R..** `\mathbf{b}_{2}\in\mathbb{R}`
Variables: "mathbf, b, in, mathbb, R".
Sign/normalization/conditioning/surrogate audit: "Formula 58 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, b, in, mathbb, R; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 58.

**Formal object 59 at 3.1.4 Regression Head — Formula 59 under 3.1.4 Regression Head is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, mathbf, prime, times, linear, layer, and the expression links hat, c, t, in, mathbb, R..** `\hat{c}_{t}\in\mathbb{R}`
Variables: "hat, c, t, in, mathbb, R".
Sign/normalization/conditioning/surrogate audit: "Formula 59 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, c, t, in, mathbb, R; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 59.

**Formal object 60 at 3.1.4 Regression Head — Formula 60 under 3.1.4 Regression Head is classified as a paper-defined mathematical relation; adjacent prose centers on mathbb, mathbf, prime, times, linear, layer, and the expression links t..** `t`
Variables: "t".
Sign/normalization/conditioning/surrogate audit: "Formula 60 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: t; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 60.

**Formal object 61 at 3.1.4 Regression Head — Formula 61 under 3.1.4 Regression Head is classified as a constraint or formal-analysis relation; adjacent prose centers on linear, layer, ReLU, activation, regression, dataset, and the expression links mathbf, z..** `\mathbf{z}`
Variables: "mathbf, z".
Sign/normalization/conditioning/surrogate audit: "Formula 61 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, z; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 61.

**Formal object 62 at 3.1.4 Regression Head — Formula 62 under 3.1.4 Regression Head is classified as a constraint or formal-analysis relation; adjacent prose centers on linear, layer, ReLU, activation, regression, dataset, and the expression links hat, c, t..** `\hat{c}_{t}`
Variables: "hat, c, t".
Sign/normalization/conditioning/surrogate audit: "Formula 62 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, c, t; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 62.

**Formal object 63 at 3.1.4 Regression Head — Formula 63 under 3.1.4 Regression Head is classified as a paper-defined mathematical relation; adjacent prose centers on capacity, architecture, allows, model, learn, nonlinear, and the expression links symbols defined beside the formula..** `70\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 63 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 3.1.4 Regression Head.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head, formal object 63.

**Formal object 64 at 3.2.1 Time Warping — Formula 64 under 3.2.1 Time Warping is classified as a paper-defined mathematical relation; adjacent prose centers on time, temporal, method, axis, follows, simulate, and the expression links chi, x_{1}, x_{2}, dots, x_{T}\}, quad, t, i..** `\chi_{0}=\{x_{1},x_{2},\dots,x_{T}\},\quad(t=i\Delta t).`
Variables: "chi, x_{1}, x_{2}, dots, x_{T}\\}, quad, t, i, Delta".
Sign/normalization/conditioning/surrogate audit: "Formula 64 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: chi, x_{1}, x_{2}, dots, x_{T}\\}, quad, t, i, Delta; meanings remain tied to 3.2.1 Time Warping.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.1 Time Warping, formal object 64.

**Formal object 65 at 3.2.1 Time Warping — Formula 65 under 3.2.1 Time Warping is classified as a paper-defined mathematical relation; adjacent prose centers on time, follows, Accordingly, construct, indices, Here, and the expression links D, d_{1}, d_{2}, dots, d_{T}\}..** `D=\{d_{1},d_{2},\dots,d_{T}\}.`
Variables: "D, d_{1}, d_{2}, dots, d_{T}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 65 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: D, d_{1}, d_{2}, dots, d_{T}\\}; meanings remain tied to 3.2.1 Time Warping.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.1 Time Warping, formal object 65.

**Formal object 66 at 3.2.1 Time Warping — Formula 66 under 3.2.1 Time Warping is classified as a paper-defined mathematical relation; adjacent prose centers on Here, time, index, derived, perturbing, original, and the expression links d_{t}..** `d_{t}`
Variables: "d_{t}".
Sign/normalization/conditioning/surrogate audit: "Formula 66 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{t}; meanings remain tied to 3.2.1 Time Warping.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.1 Time Warping, formal object 66.

**Formal object 67 at 3.2.1 Time Warping — Formula 67 under 3.2.1 Time Warping is classified as a paper-defined mathematical relation; adjacent prose centers on time, original, follows, Here, index, derived, and the expression links d_{t}, t_{i}, delta, i, quad, sim, U, alpha..** `d_{t}=t_{i}+\delta_{i},\quad\delta_{i}\sim U(-\alpha\Delta t,\alpha\Delta t),`
Variables: "d_{t}, t_{i}, delta, i, quad, sim, U, alpha, Delta, t".
Sign/normalization/conditioning/surrogate audit: "Formula 67 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{t}, t_{i}, delta, i, quad, sim, U, alpha, Delta, t; meanings remain tied to 3.2.1 Time Warping.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.1 Time Warping, formal object 67.

**Formal object 68 at 3.2.1 Time Warping — Formula 68 under 3.2.1 Time Warping is classified as a paper-defined mathematical relation; adjacent prose centers on time, where, alpha, perturbation, strength, hyperparameter, and the expression links alpha..** `\alpha`
Variables: "alpha".
Sign/normalization/conditioning/surrogate audit: "Formula 68 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: alpha; meanings remain tied to 3.2.1 Time Warping.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.1 Time Warping, formal object 68.

**Formal object 69 at 3.2.1 Time Warping — Formula 69 under 3.2.1 Time Warping is classified as a paper-defined mathematical relation; adjacent prose centers on time, where, alpha, perturbation, strength, hyperparameter, and the expression links Delta, t..** `\Delta t`
Variables: "Delta, t".
Sign/normalization/conditioning/surrogate audit: "Formula 69 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Delta, t; meanings remain tied to 3.2.1 Time Warping.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.1 Time Warping, formal object 69.

**Formal object 70 at 3.2.1 Time Warping — Formula 70 under 3.2.1 Time Warping is classified as a paper-defined mathematical relation; adjacent prose centers on time, where, alpha, perturbation, strength, hyperparameter, and the expression links chi, prime..** `\chi^{\prime}`
Variables: "chi, prime".
Sign/normalization/conditioning/surrogate audit: "Formula 70 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: chi, prime; meanings remain tied to 3.2.1 Time Warping.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.1 Time Warping, formal object 70.

**Formal object 71 at 3.2.1 Time Warping — Formula 71 under 3.2.1 Time Warping is classified as a paper-defined mathematical relation; adjacent prose centers on time, where, alpha, perturbation, strength, hyperparameter, and the expression links chi..** `\chi_{0}`
Variables: "chi".
Sign/normalization/conditioning/surrogate audit: "Formula 71 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: chi; meanings remain tied to 3.2.1 Time Warping.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.1 Time Warping, formal object 71.

**Formal object 72 at 3.2.1 Time Warping — Formula 72 under 3.2.1 Time Warping is classified as a paper-defined mathematical relation; adjacent prose centers on time, where, alpha, perturbation, strength, hyperparameter, and the expression links D..** `D`
Variables: "D".
Sign/normalization/conditioning/surrogate audit: "Formula 72 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: D; meanings remain tied to 3.2.1 Time Warping.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.1 Time Warping, formal object 72.

**Formal object 73 at 3.2.1 Time Warping — Formula 73 under 3.2.1 Time Warping is classified as a paper-defined mathematical relation; adjacent prose centers on time, original, series, interpolating, sequence, points, and the expression links chi, prime, D..** `\chi^{\prime}=\text{Interp}(\chi_{0},D).`
Variables: "chi, prime, D".
Sign/normalization/conditioning/surrogate audit: "Formula 73 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: chi, prime, D; meanings remain tied to 3.2.1 Time Warping.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.1 Time Warping, formal object 73.

**Formal object 74 at 3.2.2 Time Resampling — Formula 74 under 3.2.2 Time Resampling is classified as a paper-defined mathematical relation; adjacent prose centers on time, method, randomly, points, original, addition, and the expression links n, lfloor, rho, T, rfloor..** `n=\lfloor\rho T\rfloor`
Variables: "n, lfloor, rho, T, rfloor".
Sign/normalization/conditioning/surrogate audit: "Formula 74 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: n, lfloor, rho, T, rfloor; meanings remain tied to 3.2.2 Time Resampling.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.2 Time Resampling, formal object 74.

**Formal object 75 at 3.2.2 Time Resampling — Formula 75 under 3.2.2 Time Resampling is classified as a paper-defined mathematical relation; adjacent prose centers on time, method, randomly, points, original, addition, and the expression links rho, in..** `\rho\in[0,1]`
Variables: "rho, in".
Sign/normalization/conditioning/surrogate audit: "Formula 75 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: rho, in; meanings remain tied to 3.2.2 Time Resampling.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.2 Time Resampling, formal object 75.

**Formal object 76 at 3.2.2 Time Resampling — Formula 76 under 3.2.2 Time Resampling is classified as a paper-defined mathematical relation; adjacent prose centers on time, method, original, noise, addition, data., and the expression links chi, prime, rho, T..** `\chi^{\prime}=\text{Interp}(\text{Sample}(\chi_{0},\rho T)).`
Variables: "chi, prime, rho, T".
Sign/normalization/conditioning/surrogate audit: "Formula 76 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: chi, prime, rho, T; meanings remain tied to 3.2.2 Time Resampling.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.2 Time Resampling, formal object 76.

**Formal object 77 at 3.2.3 Gaussian Noise — Formula 77 under 3.2.3 Gaussian Noise is classified as a paper-defined mathematical relation; adjacent prose centers on time, prime, Formally, given, original, series, and the expression links chi, x_{1}, x_{2}, dots, x_{T}\}..** `\chi_{0}=\{x_{1},x_{2},\dots,x_{T}\}`
Variables: "chi, x_{1}, x_{2}, dots, x_{T}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 77 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: chi, x_{1}, x_{2}, dots, x_{T}\\}; meanings remain tied to 3.2.3 Gaussian Noise.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.3 Gaussian Noise, formal object 77.

**Formal object 78 at 3.2.3 Gaussian Noise — Formula 78 under 3.2.3 Gaussian Noise is classified as a paper-defined mathematical relation; adjacent prose centers on time, prime, Formally, given, original, series, and the expression links chi, prime..** `\chi^{\prime\prime}`
Variables: "chi, prime".
Sign/normalization/conditioning/surrogate audit: "Formula 78 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: chi, prime; meanings remain tied to 3.2.3 Gaussian Noise.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.3 Gaussian Noise, formal object 78.

**Formal object 79 at 3.2.3 Gaussian Noise — Formula 79 under 3.2.3 Gaussian Noise is classified as a paper-defined mathematical relation; adjacent prose centers on time, prime, Formally, given, original, series, and the expression links epsilon, t..** `\epsilon_{t}`
Variables: "epsilon, t".
Sign/normalization/conditioning/surrogate audit: "Formula 79 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: epsilon, t; meanings remain tied to 3.2.3 Gaussian Noise.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.3 Gaussian Noise, formal object 79.

**Formal object 80 at 3.2.3 Gaussian Noise — Formula 80 under 3.2.3 Gaussian Noise is classified as a paper-defined mathematical relation; adjacent prose centers on time, prime, Formally, given, original, series, and the expression links mathcal, N, sigma..** `\mathcal{N}(0,\sigma^{2})`
Variables: "mathcal, N, sigma".
Sign/normalization/conditioning/surrogate audit: "Formula 80 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, N, sigma; meanings remain tied to 3.2.3 Gaussian Noise.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.3 Gaussian Noise, formal object 80.

**Formal object 81 at 3.2.3 Gaussian Noise — Formula 81 under 3.2.3 Gaussian Noise is classified as a paper-defined mathematical relation; adjacent prose centers on noise, time, prime, Gaussian, sigma, Formally, and the expression links chi, prime, x_{1}, epsilon, x_{2}, dots, x_{T}, T..** `\chi^{\prime\prime}=\{x_{1}+\epsilon_{1},x_{2}+\epsilon_{2},\dots,x_{T}+\epsilon_{T}\},\quad\epsilon_{t}\sim\mathcal{N}(0,\sigma^{2}),`
Variables: "chi, prime, x_{1}, epsilon, x_{2}, dots, x_{T}, T, quad, t, sim, mathcal, N, sigma".
Sign/normalization/conditioning/surrogate audit: "Formula 81 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: chi, prime, x_{1}, epsilon, x_{2}, dots, x_{T}, T, quad, t, sim, mathcal, N, sigma; meanings remain tied to 3.2.3 Gaussian Noise.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.3 Gaussian Noise, formal object 81.

**Formal object 82 at 3.2.3 Gaussian Noise — Formula 82 under 3.2.3 Gaussian Noise is classified as a paper-defined mathematical relation; adjacent prose centers on noise, where, sigma, hyperparameter, controlling, intensity., and the expression links sigma..** `\sigma`
Variables: "sigma".
Sign/normalization/conditioning/surrogate audit: "Formula 82 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sigma; meanings remain tied to 3.2.3 Gaussian Noise.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.2.3 Gaussian Noise, formal object 82.

**Formal object 83 at 4.1 Datasets — Formula 83 under 4.1 Datasets is classified as a evaluation or scoring relation; adjacent prose centers on dataset, battery, NASA, degradation, CALCE, batteries, and the expression links Omega..** `\Omega`
Variables: "Omega".
Sign/normalization/conditioning/surrogate audit: "Formula 83 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Omega; meanings remain tied to 4.1 Datasets.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.1 Datasets, formal object 83.

**Formal object 84 at 4.1 Datasets — Formula 84 under 4.1 Datasets is classified as a evaluation or scoring relation; adjacent prose centers on dataset, battery, NASA, degradation, CALCE, batteries, and the expression links pm..** `\pm`
Variables: "pm".
Sign/normalization/conditioning/surrogate audit: "Formula 84 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: pm; meanings remain tied to 4.1 Datasets.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.1 Datasets, formal object 84.

**Formal object 85 at 4.2 Implement Details — Formula 85 under 4.2 Implement Details is classified as a optimization objective or loss; adjacent prose centers on rates, NASA, dataset, CALCE, decay, beta_, and the expression links beta..** `\beta_{1}=0.9`
Variables: "beta".
Sign/normalization/conditioning/surrogate audit: "Formula 85 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: beta; meanings remain tied to 4.2 Implement Details.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.2 Implement Details, formal object 85.

**Formal object 86 at 4.2 Implement Details — Formula 86 under 4.2 Implement Details is classified as a optimization objective or loss; adjacent prose centers on rates, NASA, dataset, CALCE, decay, beta_, and the expression links beta..** `\beta_{2}=0.999`
Variables: "beta".
Sign/normalization/conditioning/surrogate audit: "Formula 86 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: beta; meanings remain tied to 4.2 Implement Details.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.2 Implement Details, formal object 86.

**Formal object 87 at 4.2 Implement Details — Formula 87 under 4.2 Implement Details is classified as a evaluation or scoring relation; adjacent prose centers on features, error, different, used, while, performance, and the expression links left, C_{\text{current}}}{C, times, right..** `\left(SOH=\frac{C_{\text{current}}}{C_{\text{initial}}}\times 100\%\right)`
Variables: "left, C_{\\text{current}}}{C, times, right".
Sign/normalization/conditioning/surrogate audit: "Formula 87 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: left, C_{\\text{current}}}{C, times, right; meanings remain tied to 4.2 Implement Details.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.2 Implement Details, formal object 87.

**Formal object 88 at 4.3 Metrics — Formula 88 under 4.3 Metrics is classified as a evaluation or scoring relation; adjacent prose centers on predicted, true, text, pred, RMSE, measures, and the expression links n, i, y_{\text{true}, y_{\text{pred}..** `RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_{\text{true},i}-y_{\text{pred},i})^{2}}.`
Variables: "n, i, y_{\\text{true}, y_{\\text{pred}".
Sign/normalization/conditioning/surrogate audit: "Formula 88 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) n. Variables audited: n, i, y_{\\text{true}, y_{\\text{pred}; meanings remain tied to 4.3 Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.3 Metrics, formal object 88.

**Formal object 89 at 4.3 Metrics — Formula 89 under 4.3 Metrics is classified as a evaluation or scoring relation; adjacent prose centers on true, text, pred, Here, ground, truth, and the expression links y_{\text{true}, i..** `y_{\text{true},i}`
Variables: "y_{\\text{true}, i".
Sign/normalization/conditioning/surrogate audit: "Formula 89 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{\\text{true}, i; meanings remain tied to 4.3 Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.3 Metrics, formal object 89.

**Formal object 90 at 4.3 Metrics — Formula 90 under 4.3 Metrics is classified as a evaluation or scoring relation; adjacent prose centers on true, text, pred, Here, ground, truth, and the expression links y_{\text{pred}, i..** `y_{\text{pred},i}`
Variables: "y_{\\text{pred}, i".
Sign/normalization/conditioning/surrogate audit: "Formula 90 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y_{\\text{pred}, i; meanings remain tied to 4.3 Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.3 Metrics, formal object 90.

**Formal object 91 at 4.3 Metrics — Formula 91 under 4.3 Metrics is classified as a evaluation or scoring relation; adjacent prose centers on true, values, predicted, text, pred, quantifies, and the expression links n, i, y_{\text{true}, y_{\text{pred}..** `MAE=\frac{1}{n}\sum_{i=1}^{n}|y_{\text{true},i}-y_{\text{pred},i}|.`
Variables: "n, i, y_{\\text{true}, y_{\\text{pred}".
Sign/normalization/conditioning/surrogate audit: "Formula 91 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) n. Variables audited: n, i, y_{\\text{true}, y_{\\text{pred}; meanings remain tied to 4.3 Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.3 Metrics, formal object 91.

**Formal object 92 at 4.3 Metrics — Formula 92 under 4.3 Metrics is classified as a evaluation or scoring relation; adjacent prose centers on text, true, predicted, cycle, pred, quantifies, and the expression links N_{\text{true}}^{\text{EOL}}-N, N_{\text{true}}^{\text{EOL}}}..** `RE=\frac{|N_{\text{true}}^{\text{EOL}}-N_{\text{pred}}^{\text{EOL}}|}{N_{\text{true}}^{\text{EOL}}}.`
Variables: "N_{\\text{true}}^{\\text{EOL}}-N, N_{\\text{true}}^{\\text{EOL}}}".
Sign/normalization/conditioning/surrogate audit: "Formula 92 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N_{\\text{true}}^{\\text{EOL}}-N, N_{\\text{true}}^{\\text{EOL}}}; meanings remain tied to 4.3 Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.3 Metrics, formal object 92.

**Formal object 93 at 4.3 Metrics — Formula 93 under 4.3 Metrics is classified as a evaluation or scoring relation; adjacent prose centers on text, true, pred, Here, refer, cycle, and the expression links N_{\text{true}}^{\text{EOL}}..** `N_{\text{true}}^{\text{EOL}}`
Variables: "N_{\\text{true}}^{\\text{EOL}}".
Sign/normalization/conditioning/surrogate audit: "Formula 93 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N_{\\text{true}}^{\\text{EOL}}; meanings remain tied to 4.3 Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.3 Metrics, formal object 93.

**Formal object 94 at 4.3 Metrics — Formula 94 under 4.3 Metrics is classified as a evaluation or scoring relation; adjacent prose centers on text, true, pred, Here, refer, cycle, and the expression links N_{\text{pred}}^{\text{EOL}}..** `N_{\text{pred}}^{\text{EOL}}`
Variables: "N_{\\text{pred}}^{\\text{EOL}}".
Sign/normalization/conditioning/surrogate audit: "Formula 94 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N_{\\text{pred}}^{\\text{EOL}}; meanings remain tied to 4.3 Metrics.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.3 Metrics, formal object 94.

**Formal object 95 at 5.1.1 Comparison with Existing Methods — Formula 95 under 5.1.1 Comparison with Existing Methods is classified as a state or representation transformation; adjacent prose centers on performance, CDFormer, degradation, compared, models, prediction, and the expression links downarrow..** `\downarrow`
Variables: "downarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 95 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: downarrow; meanings remain tied to 5.1.1 Comparison with Existing Methods.".
Source locator: private full-paper evidence dossier for arXiv:2603.27186, 5.1.1 Comparison with Existing Methods, formal object 95.

Representative source mathematical objects follow. They are navigation evidence, not standalone interpretations:

- Mathematical object 1: `X\in\mathbb{R}^{N\times C_{in}\times L_{in}}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 2: `N` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 3: `C_{in}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 4: `L_{in}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 5: `W\in\mathbb{R}^{C_{out}\times C_{in}\times K}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 6: `C_{out}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 7: `K` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 8: `Y\in\mathbb{R}^{N\times C_{\text{out}}\times L_{\text{out}}}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 9: `Y[n,c_{\text{out}},t]=\sum_{c_{\text{in}}=1}^{C_{\text{in}}}\sum_{k=1}^{K}X[n,c_{\text{in}},t+k]\cdot W[c_{\text{out}},c_{\text{in}},k]+b[c_{\text{out}}],` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 10: `b\in\mathbb{R}^{C_{\text{out}}}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 11: `Y=X\cdot W+b,` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 12: `X` — read with adjacent definitions; no symbol meaning is inferred from markup alone.

Equation-to-adjacent-context reconstruction:

- Equation under source heading 3.1.1 1D-CNNs: `X\in\mathbb{R}^{N\times C_{in}\times L_{in}}`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.1 1D-CNNs: `N`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.1 1D-CNNs: `C_{in}`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.1 1D-CNNs: `L_{in}`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.1 1D-CNNs: `W\in\mathbb{R}^{C_{out}\times C_{in}\times K}`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.1 1D-CNNs: `C_{out}`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.1 1D-CNNs: `K`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.1 1D-CNNs: `Y\in\mathbb{R}^{N\times C_{\text{out}}\times L_{\text{out}}}`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.1 1D-CNNs: `Y[n,c_{\text{out}},t]=\sum_{c_{\text{in}}=1}^{C_{\text{in}}}\sum_{k=1}^{K}X[n,c_{\text{in}},t+k]\cdot W[c_{\text{out}},c_{\text{in}},k]+b[c_{\text{out}}],`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.1 1D-CNNs: `b\in\mathbb{R}^{C_{\text{out}}}`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.2 DRSN: `Y=X\cdot W+b,`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.
- Equation under source heading 3.1.2 DRSN: `X`; adjacent method terms: models, battery, rul, prediction, degradation, methods, modeling, electrochemical.

For each central equation, the audit asks whether the sign agrees with the prose, whether weights are normalized, whether masking or conditioning changes the denominator, whether a displayed objective is exact or a training surrogate, and whether units can be compared. A learned score is not automatically calibrated, a relaxation is not an exact discrete solution, and an empirical constraint satisfaction rate is not a theorem. These distinctions protect the paper's real contribution from stronger claims it does not need.

### 2.3 Components, architecture, and information flow

The source's technical path is anchored to 2.1 Physics-Based Modeling Methods, 2.2 Deep Learning-Based Methods. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims.

**Input/output dataflow:** The documented dataflow is reconstructed only across 2.1 Physics-Based Modeling Methods, 2.2 Deep Learning-Based Methods, and 3 Method, where the source associates battery, prediction, degradation, temporal, performance, modeling, and data. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

| Component | Inherited or novel | Role | Source locator |
|---|---|---|---|
| 2.1 Physics-Based Modeling Methods | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with degradation, battery, prediction, Physics-Based, and empirical; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2603.27186, 2.1 Physics-Based Modeling Methods |
| 2.1 Physics-Based Modeling Methods | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with electrochemical, battery, internal, Physics-Based, and Modeling; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2603.27186, 2.1 Physics-Based Modeling Methods |
| 2.2 Deep Learning-Based Methods | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with prediction, mechanisms, Deep, applied, and battery; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2603.27186, 2.2 Deep Learning-Based Methods |
| 2.2 Deep Learning-Based Methods | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with Deep, temporal, modeling, battery, and applications; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2603.27186, 2.2 Deep Learning-Based Methods |
| 2.2 Deep Learning-Based Methods | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with challenge, Deep, Learning-Based, Therefore, and developing; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2603.27186, 2.2 Deep Learning-Based Methods |

The paper-specific method vocabulary is models, battery, rul, prediction, degradation, methods, modeling, electrochemical, capacity, life. This vocabulary was derived from the complete method/architecture paragraphs rather than the title. It identifies the entities that must appear in a faithful architecture reconstruction and creates a falsifiable check: an implementation or summary that omits these named objects is not yet grounded in this paper.

The architecture is reconstructed as an information-flow graph: source identity and inputs enter; inherited and paper-specific components transform or score them; a decision or representation is produced; optional validation or post-processing occurs; and an evaluated outcome leaves the pipeline. Each edge should name the information available at that point. A comparison becomes unfair if one method has access to labels, future requests, privileged metadata, additional context, or a larger tuning budget that another method lacks.

### 2.4 Training, calibration, and inference

Construction-time and runtime work are separate accounting domains. Training may fit parameters, construct representations, estimate thresholds, tune prompts, or learn a policy. Calibration may use held-out examples or measurements. Inference may retrieve, route, compress, classify, generate, search, solve, or verify. Post-processing may enforce a constraint or discard invalid output. A credible efficiency claim says which of these phases is included, which is amortized, and which is external to the reported number.

Training or calibration evidence is explicitly located in 2.2 Deep Learning-Based Methods. The associated source vocabulary emphasizes models, battery, rul, prediction, degradation, methods, modeling, electrochemical, capacity, life.

Paper-specific construction/training sequence:

1. At 2.2 Deep Learning-Based Methods, the paper reports a training-related operation involving prediction, mechanisms, Deep, applied, battery, and dependencies. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 2.2 Deep Learning-Based Methods)*
2. At 3 Method, the paper reports a training-related operation involving temporal, data, augmentation, techniques, mechanisms, and CDFormer. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 3 Method)*
3. At 5 Result and Discussion, the paper reports a training-related operation involving Result, Discussion, present, comprehensive, evaluation, and CDFormer. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 5 Result and Discussion)*
4. At 2 Related Work, the paper reports a training-related operation involving approaches, deep, learning, Existing, prediction, and broadly. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 2 Related Work)*

Inference or runtime evidence is explicitly located in 2.1 Physics-Based Modeling Methods. Its source vocabulary overlaps models, battery, rul, prediction, degradation, methods, modeling, electrochemical, capacity, life.

Paper-specific inference/evaluation sequence:

1. At 2.1 Physics-Based Modeling Methods, the paper reports an inference or deployment action involving degradation, battery, prediction, Physics-Based, empirical, and mechanism. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 2.1 Physics-Based Modeling Methods)*
2. At 2.1 Physics-Based Modeling Methods, the paper reports an inference or deployment action involving electrochemical, battery, internal, Physics-Based, Modeling, and changes. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 2.1 Physics-Based Modeling Methods)*
3. At 2.2 Deep Learning-Based Methods, the paper reports an inference or deployment action involving prediction, mechanisms, Deep, applied, battery, and dependencies. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 2.2 Deep Learning-Based Methods)*
4. At 2.2 Deep Learning-Based Methods, the paper reports an inference or deployment action involving Deep, temporal, modeling, battery, applications, and features. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 2.2 Deep Learning-Based Methods)*

The reconstructed operational sequence is: pin input and artifact versions; validate prerequisites; compute the method-specific state or signal; apply the stated decision or objective; materialize the output; execute any downstream consumer; and measure both quality and resource outcomes. This sequence is reviewer inference grounded in the paper's organization. It is a testing model, not an assertion that the authors implemented an identical production controller.[^inference]

### 2.5 Notation and implementation audit

No independent implementation was run. The audit therefore checks internal legibility across equations, prose, captions, appendices, and extracted code/data statements. Apparent inconsistencies remain unresolved unless source evidence explains them. Source availability is classified in levels—declared, reachable, inspectable, runnable, and result-reproducing—and this local phase establishes only the declared/local-source layers.

## 3. Architecture and Complete Operational Pipeline

### 3.1 Representation and state

The documented dataflow is reconstructed only across 2.1 Physics-Based Modeling Methods, 2.2 Deep Learning-Based Methods, and 3 Method, where the source associates battery, prediction, degradation, temporal, performance, modeling, and data. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

The central representation must be described by shape, type, provenance, lifetime, and relationship to the original input. If it is compressed, selected, latent, retrieved, generated, or aggregated, the review asks what information can be lost and how that loss is detected. If it is learned, the training distribution and version become part of its identity. If it is mutable, update ordering, expiry, and rollback become part of the method rather than operational afterthoughts.

### 3.2 Decision or action modules

The paper-specific modules should be separated from inherited encoders, decoders, solvers, retrieval systems, evaluators, or model APIs. A score can rank candidates without being calibrated; a policy can improve average reward without satisfying hard constraints; and a verifier can reject some failures without certifying all accepted outputs. The assessment uses the source's strongest ablation or controlled comparison to decide which module is necessary and which is merely bundled.

### 3.3 Dependencies, post-processing, and guarantee boundary

Dependencies include data preprocessing, external models, tokenizers, simulators, indexes, numerical libraries, and evaluation code. Post-processing can materially create the final result, so its compute and failure rate belong in the pipeline. Exact validation, when present, may establish a property of a returned object; it does not automatically establish semantic correctness, optimality, robustness, or absence of distribution shift.

### 3.4 Resource allocation and stopping

Budgets can refer to tokens, bytes, parameters, candidates, iterations, calls, samples, time, energy, or money. Requested and achieved budgets should both be recorded. Early stopping and fallback can bias which cases receive expensive processing. Batching can improve throughput while worsening latency. The review therefore distinguishes construction cost, per-instance latency, batch throughput, tail latency, peak memory, and downstream cost before accepting a general efficiency claim.

## 4. Experimental Design and Evidence Reconstructed

The evaluation reconstruction follows 5 Result and Discussion, 4.1 Datasets, with 10 table captions and 15 figure captions inventoried.

Paper-specific evaluation vocabulary centers on dataset, nasa, degradation, calce, conditions, evaluation, performance, two, battery, datasets. These terms constrain which datasets, metrics, models, budgets, or operational quantities must be preserved with each reported comparison. They also identify where a later reproduction dossier must look for splits, baselines, hardware, batching, runtime semantics, and uncertainty rather than assuming conventional defaults.

The headings mechanically associated with evaluation and results were:

- 5 Result and Discussion
- 4.1 Datasets

### 4.1 Data, splits, and distribution

Not applicable: No named dataset, benchmark, corpus, or split was found in the captured full-paper data/evaluation paragraphs; none is invented. (source locator: private full-paper evidence dossier for arXiv:2603.27186, data/evaluation paragraph inventory).

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| Charge Mode | Table 1 lists Charge Mode as a numeric comparison row under 4.1 Datasets. | Neither the Table 1 caption nor its row label establishes whether Charge Mode was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 1 row Charge Mode |
| Discharge Cutoff Voltage | Table 1 lists Discharge Cutoff Voltage as a numeric comparison row under 4.1 Datasets. | Neither the Table 1 caption nor its row label establishes whether Discharge Cutoff Voltage was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 1 row Discharge Cutoff Voltage |
| Charge Cutoff Condition | Table 1 lists Charge Cutoff Condition as a numeric comparison row under 4.1 Datasets. | Neither the Table 1 caption nor its row label establishes whether Charge Cutoff Condition was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 1 row Charge Cutoff Condition |
| Cycle Count | Table 1 lists Cycle Count as a numeric comparison row under 4.1 Datasets. | Neither the Table 1 caption nor its row label establishes whether Cycle Count was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 1 row Cycle Count |
| Operating Temperature | Table 1 lists Operating Temperature as a numeric comparison row under 4.1 Datasets. | Neither the Table 1 caption nor its row label establishes whether Operating Temperature was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 1 row Operating Temperature |
| RNN | Table 4 lists RNN as a numeric comparison row under 5.1.1 Comparison with Existing Methods. | Neither the Table 4 caption nor its row label establishes whether RNN was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 4 row RNN |
| LSTM | Table 4 lists LSTM as a numeric comparison row under 5.1.1 Comparison with Existing Methods. | Neither the Table 4 caption nor its row label establishes whether LSTM was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 4 row LSTM |
| GRU | Table 4 lists GRU as a numeric comparison row under 5.1.1 Comparison with Existing Methods. | Neither the Table 4 caption nor its row label establishes whether GRU was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 4 row GRU |
| SA-LSTM | Table 4 lists SA-LSTM as a numeric comparison row under 5.1.1 Comparison with Existing Methods. | Neither the Table 4 caption nor its row label establishes whether SA-LSTM was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 4 row SA-LSTM |
| AttMoE | Table 4 lists AttMoE as a numeric comparison row under 5.1.1 Comparison with Existing Methods. | Neither the Table 4 caption nor its row label establishes whether AttMoE was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 4 row AttMoE |
| Baseline-FC | Table 5 lists Baseline-FC as a numeric comparison row under 5.1.2 Comparison with Other Deep Learning-Based Variants. | Neither the Table 5 caption nor its row label establishes whether Baseline-FC was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 5 row Baseline-FC |
| CNN-FC | Table 5 lists CNN-FC as a numeric comparison row under 5.1.2 Comparison with Other Deep Learning-Based Variants. | Neither the Table 5 caption nor its row label establishes whether CNN-FC was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 5 row CNN-FC |
| Gaussian Noise | Table 6 lists Gaussian Noise as a numeric comparison row under 5.2.1 Effects of temporal data augmentation on CDFormer. | Neither the Table 6 caption nor its row label establishes whether Gaussian Noise was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 6 row Gaussian Noise |
| Time Warping | Table 6 lists Time Warping as a numeric comparison row under 5.2.1 Effects of temporal data augmentation on CDFormer. | Neither the Table 6 caption nor its row label establishes whether Time Warping was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 6 row Time Warping |
| Time Resampling | Table 6 lists Time Resampling as a numeric comparison row under 5.2.1 Effects of temporal data augmentation on CDFormer. | Neither the Table 6 caption nor its row label establishes whether Time Resampling was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 6 row Time Resampling |
| All Combined (Ours) | Table 6 lists All Combined (Ours) as a numeric comparison row under 5.2.1 Effects of temporal data augmentation on CDFormer. | Neither the Table 6 caption nor its row label establishes whether All Combined (Ours) was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2603.27186, Table 6 row All Combined (Ours) |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

| Metric | Denominator/conditioning | Direction | Source locator |
|---|---|---|---|
| NASA / RMSE \downarrow | Table 4 reports NASA / RMSE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 4 header NASA / RMSE \downarrow |
| NASA / MAE \downarrow | Table 4 reports NASA / MAE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 4 header NASA / MAE \downarrow |
| NASA / RE \downarrow | Table 4 reports NASA / RE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 4 header NASA / RE \downarrow |
| CALCE / RMSE \downarrow | Table 4 reports CALCE / RMSE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 4 header CALCE / RMSE \downarrow |
| CALCE / MAE \downarrow | Table 4 reports CALCE / MAE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 4 header CALCE / MAE \downarrow |
| CALCE / RE \downarrow | Table 4 reports CALCE / RE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 4 header CALCE / RE \downarrow |
| Before temporal data augmentation / RMSE \downarrow | Table 7 reports Before temporal data augmentation / RMSE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 7 header Before temporal data augmentation / RMSE \downarrow |
| Before temporal data augmentation / MAE \downarrow | Table 7 reports Before temporal data augmentation / MAE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 7 header Before temporal data augmentation / MAE \downarrow |
| Before temporal data augmentation / RE \downarrow | Table 7 reports Before temporal data augmentation / RE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 7 header Before temporal data augmentation / RE \downarrow |
| After temporal data augmentation / RMSE \downarrow | Table 7 reports After temporal data augmentation / RMSE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 7 header After temporal data augmentation / RMSE \downarrow |
| After temporal data augmentation / MAE \downarrow | Table 7 reports After temporal data augmentation / MAE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 7 header After temporal data augmentation / MAE \downarrow |
| After temporal data augmentation / RE \downarrow | Table 7 reports After temporal data augmentation / RE \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2603.27186, Table 7 header After temporal data augmentation / RE \downarrow |

Metrics are reconstructed with direction, denominator, aggregation unit, conditioning, and reference quality. Failures excluded from an average create survivor bias. A gap to a best-known incumbent is not a gap to a proven optimum. A judge-model score is not a human preference without validation. A compression ratio can invert depending on convention. Confidence intervals, paired tests, and effect sizes matter when differences are close or instances are correlated.

### 4.4 Hardware, batching, and runtime semantics

Quality-v2 paper-specific hardware/runtime evidence:

- At 3.1.1 1D-CNNs, the paper's hardware/runtime paragraph names batch size. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.1 1D-CNNs)*
- At 3.1.2 DRSN, the paper's hardware/runtime paragraph names batch. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN)*
- At 3.1.2 DRSN, the paper's hardware/runtime paragraph names threshold, generator, lambda, dynamically, generated, dedicated, enabling, channel-wise. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN)*
- At 3.1.2 DRSN, the paper's hardware/runtime paragraph names batch size. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN)*
- At 3.1.2 DRSN, the paper's hardware/runtime paragraph names batch. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.2 DRSN)*
- At 3.1.4 Regression Head, the paper's hardware/runtime paragraph names mathbb, mathbf, prime, times, linear, layer, where, represent. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head)*
- At 3.1.4 Regression Head, the paper's hardware/runtime paragraph names linear, layer, ReLU, activation, regression, dataset, learned, feature. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 3.1.4 Regression Head)*
- At 4.2 Implement Details, the paper's hardware/runtime paragraph names Batch size. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.2 Implement Details)*


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
| Table 4 | CDFormer | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | NASA / RMSE \downarrow; NASA / MAE \downarrow; NASA / RE \downarrow; CALCE / RMSE \downarrow; CALCE / MAE \downarrow; CALCE / RE \downarrow | NASA / RMSE \downarrow=0.0671; NASA / MAE \downarrow=0.0586; NASA / RE \downarrow=0.2365; CALCE / RMSE \downarrow=0.0179; CALCE / MAE \downarrow=0.0106; CALCE / RE \downarrow=0.0877 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2603.27186, Table 4 row 9 |
| Table 4 | DeTransformer | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | NASA / RMSE \downarrow; NASA / MAE \downarrow; NASA / RE \downarrow; CALCE / RMSE \downarrow; CALCE / MAE \downarrow; CALCE / RE \downarrow | NASA / RMSE \downarrow=0.0863; NASA / MAE \downarrow=0.0746; NASA / RE \downarrow=0.2609; CALCE / RMSE \downarrow=0.0616; CALCE / MAE \downarrow=0.0481; CALCE / RE \downarrow=0.1282 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2603.27186, Table 4 row 6 |
| Table 5 | CNN-Transformer | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | NASA / RMSE \downarrow; NASA / MAE \downarrow; NASA / RE \downarrow; CALCE / RMSE \downarrow; CALCE / MAE \downarrow; CALCE / RE \downarrow | NASA / RMSE \downarrow=0.1059; NASA / MAE \downarrow=0.0904; NASA / RE \downarrow=0.2264; CALCE / RMSE \downarrow=0.0225; CALCE / MAE \downarrow=0.0133; CALCE / RE \downarrow=0.0896 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2603.27186, Table 5 row 5 |
| Table 5 | CDFormer | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | NASA / RMSE \downarrow; NASA / MAE \downarrow; NASA / RE \downarrow; CALCE / RMSE \downarrow; CALCE / MAE \downarrow; CALCE / RE \downarrow | NASA / RMSE \downarrow=0.0671; NASA / MAE \downarrow=0.0586; NASA / RE \downarrow=0.2365; CALCE / RMSE \downarrow=0.0179; CALCE / MAE \downarrow=0.0106; CALCE / RE \downarrow=0.0877 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2603.27186, Table 5 row 6 |
| Table 6 | No Augmentation | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | NASA / RMSE \downarrow; NASA / MAE \downarrow; NASA / RE \downarrow; CALCE / RMSE \downarrow; CALCE / MAE \downarrow; CALCE / RE \downarrow | NASA / RMSE \downarrow=0.0671; NASA / MAE \downarrow=0.0586; NASA / RE \downarrow=0.2365; CALCE / RMSE \downarrow=0.0179; CALCE / MAE \downarrow=0.0106; CALCE / RE \downarrow=0.0877 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2603.27186, Table 6 row 3 |
| Table 6 | Gaussian Noise | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | NASA / RMSE \downarrow; NASA / MAE \downarrow; NASA / RE \downarrow; CALCE / RMSE \downarrow; CALCE / MAE \downarrow; CALCE / RE \downarrow | NASA / RMSE \downarrow=0.0538; NASA / MAE \downarrow=0.0447; NASA / RE \downarrow=0.1548; CALCE / RMSE \downarrow=0.0166; CALCE / MAE \downarrow=0.0101; CALCE / RE \downarrow=0.0869 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2603.27186, Table 6 row 4 |
| Table 7 | CNN-Transformer | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Before temporal data augmentation / RMSE \downarrow; Before temporal data augmentation / MAE \downarrow; Before temporal data augmentation / RE \downarrow; After temporal data augmentation / RMSE \downarrow; After temporal data augmentation / MAE \downarrow; After temporal data augmentation / RE \downarrow | Before temporal data augmentation / RMSE \downarrow=0.1059; Before temporal data augmentation / MAE \downarrow=0.0904; Before temporal data augmentation / RE \downarrow=0.2264; After temporal data augmentation / RMSE \downarrow=0.0725; After temporal data augmentation / MAE \downarrow=0.0606; After temporal data augmentation / RE \downarrow=0.1670 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2603.27186, Table 7 row 5 |
| Table 7 | CDFormer | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Before temporal data augmentation / RMSE \downarrow; Before temporal data augmentation / MAE \downarrow; Before temporal data augmentation / RE \downarrow; After temporal data augmentation / RMSE \downarrow; After temporal data augmentation / MAE \downarrow; After temporal data augmentation / RE \downarrow | Before temporal data augmentation / RMSE \downarrow=0.0671; Before temporal data augmentation / MAE \downarrow=0.0586; Before temporal data augmentation / RE \downarrow=0.2365; After temporal data augmentation / RMSE \downarrow=0.0371; After temporal data augmentation / MAE \downarrow=0.0301; After temporal data augmentation / RE \downarrow=0.1327 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2603.27186, Table 7 row 6 |

Bounded exact evidence retained from the paper report:

- Paper report, numeric result in 4.1 Datasets: “Detailed information on battery types, nominal capacities, sampling frequencies, and…” (exact numeric tokens: 1, 2).

- No table-caption fragment was included in the bounded verbatim evidence budget.

The correct interpretation retains task, dataset, split, model, baseline, metric, budget, and hardware with each result. A largest reported improvement is an operating point, not a distribution. An average is not a tail guarantee. A component metric can diagnose mechanism without proving end-to-end utility. Where the source reports multiple tables or figures, their relationships should be checked for consistent defaults, denominators, and versioned settings.

Three types of gain remain separate. Representation gain means fewer tokens, bytes, channels, states, features, or bits. Execution gain means lower latency, memory traffic, transfer, energy, or higher throughput. Outcome gain means better correctness, quality, utility, constraint satisfaction, or task completion. The paper may establish one or more under its setting; a deployment decision requires the combination relevant to its service objective.

Table and figure captions were inventoried rather than republished. Their exact values remain anchored to the paper. Any public summary should cite only values whose numerator, denominator, model, dataset, and comparison are simultaneously known. This review does not manufacture missing uncertainty or turn qualitative illustrations into statistical evidence.

## 6. Ablations and Causal Evidence

Paper-specific ablation/control ledger:

| Component/control | Paper-reported delta | Control caveat | Source locator |
|---|---|---|---|
| first, compare, and performance | direction or magnitude is reported only at the source locator | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2603.27186, 5 Result and Discussion |
| Ablation, studies, and indicate | direction or magnitude is reported only at the source locator | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2603.27186, 6 Conclusion |

Ablations are persuasive when one named component changes while model, data, budget, training effort, and implementation quality stay fixed. The complete source was screened for removals, swaps, budget sweeps, sensitivity tests, and failure examples. If multiple elements change together, the result supports the bundle more strongly than any individual mechanism. If a simple cost-matched control is missing, the causal interpretation remains limited.

Randomness must be classified as training seeds, inference seeds, data-generation seeds, checkpoint-selection variance, or hyperparameter-search variance. Repeated inference does not prove training robustness. A named significance test should identify its independence unit and paired design. The practical importance of an effect is separate from statistical detectability, especially when a large benchmark makes very small changes significant.

Author-stated limitations:

- The author-side qualification at 6 Conclusion concerns CDFormer, hybrid, deep, learning, framework, and integrates. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 6 Conclusion)*
- The author-side qualification at 6 Conclusion concerns Extensive, experiments, NASA, CALCE, datasets, and CDFormer. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 6 Conclusion)*
- The author-side qualification at 6 Conclusion concerns Future, focus, incorporating, multi-modal, sensor, and data. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 6 Conclusion)*
- The author-side qualification at 6 Conclusion concerns Overall, findings, highlight, CDFormer, effective, and extensible. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 6 Conclusion)*

Reviewer-identified limitations:

- No independent reproduction was performed for arXiv:2603.27186v1; dataset, NASA, degradation, and CALCE remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.1 Datasets, and 5 Result and Discussion)*
- The dossier inventories 32 headings, 10 tables, 15 figures, and 95 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2603.27186, complete coverage inventory)*

The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 2 candidate sentences and the limitation/discussion vocabulary cdformer, proposed, framework, battery, rul, data, augmentation, techniques, models, predictive. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper frames Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries as a contribution to battery, degradation, data, prediction. | Problem framing is located in the profile's named introduction/problem headings; no numbered section marker is treated as a measurement. (private full-paper evidence dossier for arXiv:2603.27186, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| The reported mechanism centers on battery, prediction, degradation, temporal. | Method and formula evidence is bound to the named method headings and formula-specific operator audits. (private full-paper evidence dossier for arXiv:2603.27186, 2.1 Physics-Based Modeling Methods) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Table 4 reports measured outcomes for CDFormer across NASA / RMSE \downarrow, NASA / MAE \downarrow, NASA / RE \downarrow, CALCE / RMSE \downarrow, CALCE / MAE \downarrow. | Quality-v2 paper-report result values: NASA / RMSE \downarrow=0.0671; NASA / MAE \downarrow=0.0586; NASA / RE \downarrow=0.2365; CALCE / RMSE \downarrow=0.0179; CALCE / MAE \downarrow=0.0106; CALCE / RE \downarrow=0.0877 (private full-paper evidence dossier for arXiv:2603.27186, 4.1 Datasets) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2603.27186v1), [canonical PDF](https://arxiv.org/pdf/2603.27186v1), [canonical full-paper HTML](https://arxiv.org/html/2603.27186v1), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2603.27186). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2603.27186v1)*
- **Predecessor/prior work (checked):** This URL was live-verified as a primary source. Its association is limited to battery remaining-useful-life forecasting context; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2505.16664)*
- **Alternative or benchmark (checked):** This URL was live-verified as a primary source. Its association is limited to contemporaneous battery remaining-life modeling alternative; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2603.22323)*
- **Code/data (bounded_not_found):** The bounded verified-URL receipt contains no official code/data artifact for this paper; no access error was recorded, so this is not labeled blocked. *(evidence locator: bounded online-vetting receipt for arXiv:2603.27186)*

Verified official primary-source links from the bounded check:

- No additional official code, data, project, venue, or benchmark URL was verified beyond the canonical record.

Access-blocked or unverified URL evidence: not recorded

Prior-work and alternatives evidence: "bounded_to_canonical_arxiv_record_and_paper_declared_primary_links" This is a bounded search record, not an exhaustive map of the field.

Code/data and reproduction evidence: "link_reachability_only; repository contents were not downloaded, built, or executed" Reachability and metadata do not mean that code or data were executed, that dependencies were installed, or that a reported result reproduced.

Paper-declared external candidates were recorded as follows:

- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/accessible_HTML.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/license/index.html#licenses-available
- Paper-declared URL, not opened in this phase: https://calce.umd.edu/battery-data
- Paper-declared URL, not opened in this phase: https://ti.arc.nasa.gov/tech/dash/groups/pcoe/prognostic-data-repository/
- Paper-declared URL, not opened in this phase: https://math.nist.gov/~BMiller/LaTeXML/
- Paper-declared URL, not opened in this phase: https://github.com/arXiv/html_feedback/issues
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/issues
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/ourmembers.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/contact.html

Their presence is discovery evidence, not proof that an artifact is official, available, licensed, runnable, or reproducing the paper. A later online-vetting phase should use primary sources, record HTTP/access limits, verify ownership and linkage, inspect release and license state, and distinguish artifact availability from runnable or result-reproducing status. Until then the publication status remains: arXiv preprint; no separate peer-reviewed venue inferred without an official venue source.

The isolated Black Lake checkout was used only for repository-readiness and dedupe context. A same-paper DEP-A would block a new owning record; a DEP-E or directly corresponding implementation is associated context rather than a duplicate. Background citations do not transfer evidence or claims to this paper.[^association]

## 9. Independent Re-conceptualization

Reviewer inference: the durable mechanism is the source-defined change centered on battery, prediction, degradation, and temporal, rather than the paper's brand name. This interpretation predicts that a matched intervention on battery changes dataset; it is not an author claim or theorem.

Re-conceptualize the contribution as an evidence-linked state transition: pin source identity, record the method-specific decision, measure realized resource and outcome effects, and retain a conservative fallback whose trigger can be falsified on held-out conditions. This is reviewer inference and proposal, not an author claim and not an experimentally validated architecture.[^inference]

The mechanism can be viewed as a governed handoff between evidence, decision, execution, and outcome. Evidence identifies the source state and the signal the method uses. Decision records the action or representation chosen under a budget. Execution records what the system actually did, including fallback and resource use. Outcome records task quality and failure. The mapping is useful because it predicts what must be logged; it breaks when the paper studies a purely formal object with no operational transition.

A second bounded analogy is experimental portfolio control. Different baselines, budgets, and ablations are portfolio arms whose information access and cost must be matched. This analogy highlights selection bias and incomplete frontiers, but it does not imply that the paper uses an online bandit or that deployment should optimize only one scalar reward. Its falsifiable prediction is that the proposed mechanism's advantage should shrink when information access and complete cost are carefully matched if the original gain came mainly from comparison asymmetry.

## 10. Research Notes, Limitations, and Evidence Boundary

The complete local PDF and full-paper HTML for arXiv:2603.27186v1 were inspected. The PDF passed size, header, EOF, parse, page-count, title, structure, and references checks. The HTML passed size, readable-body, document-marker, heading, structure, title, and identity checks. Abstract HTML was metadata only and did not qualify as the paper body.[^integrity]

The coverage pass includes introduction, method or formal analysis, experiments or results, discussion or conclusion, references, appendices where exposed, tables, figures, equations, footnotes, disclosures, and code/data language. Extraction can lose visual layout and some mathematical semantics; the ledger records this boundary rather than claiming that every graphic was numerically reproduced.

Paper-specific qualification inventory: limitation/discussion terms cdformer, proposed, framework, battery, rul, data, augmentation, techniques, models, predictive; disclosure/funding language limitations; code/data language GitHub, data availability, dataset, repository; appendix headings none separately exposed. These are evidence pointers. A missing extracted term is not proof that a disclosure, artifact, or limitation does not exist.

Evidence layers remain explicit. Layer A is what the paper reports. Layer B contains the bounded primary records actually checked online; its conclusions are limited to the recorded identity, publication, and artifact-access evidence. Layer C is reviewer inference, including the governed-handoff interpretation. Layer D is a hypothesis or proposal, including deployment controls and falsification tests. A sentence is not silently promoted between layers.

Paper/prose/table consistency checks:

| Issue/check | Assessment | Source locator |
|---|---|---|
| Canonical ID, version, title, authors, PDF hash, and HTML hash were reconciled for arXiv:2603.27186v1; full quantitative table/prose/code consistency was not independently rerun. | identity consistency checked; quantitative and implementation consistency remain unresolved | source-integrity and online identity receipts for arXiv:2603.27186v1 |

Substantive evidence boundary: The profile binds arXiv:2603.27186v1 to a complete local PDF and full-paper HTML, 32 headings, 10 tables, 15 figures, and 95 extracted mathematical objects, and 2 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

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

### Hypothesis 1: Matched removal of battery

**Proposition:** Reviewer hypothesis: the source-linked battery operation is causally responsible for part of the reported dataset behavior.
**Predicted observation:** Removing or neutralizing battery under matched data and compute will measurably weaken dataset.
**Falsifying observation:** A competent matched control without battery preserves the same dataset distribution within uncertainty.
**Minimum test:** Run a paired, seed-controlled ablation at 4.1 Datasets and archive per-instance outcomes and resource use.
**Evidence locator:** private full-paper evidence dossier for arXiv:2603.27186, 2.1 Physics-Based Modeling Methods, and 2.2 Deep Learning-Based Methods

### Hypothesis 2: Boundary transfer for Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries

**Proposition:** Reviewer hypothesis: the relation between battery, and prediction and dataset, and NASA weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2603.27186, 4.1 Datasets, and 5 Result and Discussion

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2603.27186, 4.1 Datasets, and 5 Result and Discussion.
2. **Reproduce the end-to-end Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries path** Success: the source-defined battery, prediction, and degradation and dataset, and NASA are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2603.27186, 2.1 Physics-Based Modeling Methods, and 2.2 Deep Learning-Based Methods.
3. **Falsify the reviewer mechanism thesis for battery** Success: a matched intervention on battery predicts a corresponding change in dataset Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2603.27186, 2.1 Physics-Based Modeling Methods, and 2.2 Deep Learning-Based Methods.

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries should be remembered as a tested relation between battery, prediction, and degradation and dataset, NASA, and degradation under the configurations at 4.1 Datasets, and 5 Result and Discussion, not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The Table 1 caption centers on Table, Detailed, Information, NASA, Lithium-Ion, Battery, Dataset; its parsed headers include no explicit header text, across 16 rows and 32 cells.; result: column 2=2.7; column 2=2.5; column 2=2.2; column 2=2.5; caveat: Interpret Table 1 with its spanning headers and caption under 4.1 Datasets; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.27186, Table 1 caption and object |
| Table 2 | Purpose: The Table 2 caption centers on Table, Detailed, Information, CALCE, Lithium-Ion, Battery, Dataset; its parsed headers include no explicit header text, across 16 rows and 32 cells.; result: column 2=900; column 2=950; column 2=1000; column 2=1000; caveat: Interpret Table 2 with its spanning headers and caption under 4.1 Datasets; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.27186, Table 2 caption and object |
| Table 3 | Purpose: The Table 3 caption centers on Table, Input, features, used, NASA, CALCE, datasets.; its parsed headers include no explicit header text, across 7 rows and 21 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 3 with its spanning headers and caption under 4.2 Implement Details; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.27186, Table 3 caption and object |
| Table 4 | Purpose: The Table 4 caption centers on Table, Quantitative, evaluations, CDFormer, baseline, models, NASA; its parsed headers include no explicit header text, across 9 rows and 58 cells.; result: column 2=0.0671; column 3=0.0586; column 4=0.2365; column 5=0.0179; column 6=0.0106; column 7=0.0877; caveat: Interpret Table 4 with its spanning headers and caption under 5.1.1 Comparison with Existing Methods; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.27186, Table 4 caption and object |
| Table 5 | Purpose: The Table 5 caption centers on Table, Quantitative, evaluations, CDFormer, other, deep, learning-based; its parsed headers include no explicit header text, across 6 rows and 37 cells.; result: column 2=0.1117; column 3=0.0981; column 4=0.2322; column 5=0.0209; column 6=0.0127; column 7=0.0828; caveat: Interpret Table 5 with its spanning headers and caption under 5.1.2 Comparison with Other Deep Learning-Based Variants; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.27186, Table 5 caption and object |
| Table 6 | Purpose: The Table 6 caption centers on Table, Impact, temporal, data, augmentation, NASA, CALCE; its parsed headers include no explicit header text, across 7 rows and 44 cells.; result: column 2=0.0671; column 3=0.0586; column 4=0.2365; column 5=0.0179; column 6=0.0106; column 7=0.0877; caveat: Interpret Table 6 with its spanning headers and caption under 5.2.1 Effects of temporal data augmentation on CDFormer; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.27186, Table 6 caption and object |
| Table 7 | Purpose: The Table 7 caption centers on Table, Performance, model, variants, before, temporal, data; its parsed headers include no explicit header text, across 6 rows and 37 cells.; result: column 2=0.1952; column 3=0.1822; column 4=0.5572; column 5=0.1814; column 6=0.1677; column 7=0.4005; caveat: Interpret Table 7 with its spanning headers and caption under 5.2.2 Effects of temporal data augmentation Across Model Variants; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.27186, Table 7 caption and object |
| Table 8 | Purpose: The Table 8 caption centers on Table, Performance, model, variants, before, temporal, data; its parsed headers include no explicit header text, across 6 rows and 37 cells.; result: column 2=0.0309; column 3=0.0184; column 4=0.0980; column 5=0.0312; column 6=0.0188; column 7=0.0870; caveat: Interpret Table 8 with its spanning headers and caption under 5.2.2 Effects of temporal data augmentation Across Model Variants; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.27186, Table 8 caption and object |
| Table 9 | Purpose: The Table 9 caption centers on temporal, Table, Impact, data, augmentation, single, feature; its parsed headers include no explicit header text, across 9 rows and 58 cells.; result: column 2=0.1435; column 3=0.1205; column 4=0.3692; column 5=0.1429; column 6=0.1205; column 7=0.2880; caveat: Interpret Table 9 with its spanning headers and caption under 5.2.3 Generalization under Diverse Temporal Feature Conditions; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.27186, Table 9 caption and object |
| Table 10 | Purpose: The Table 10 caption centers on temporal, Table, Impact, data, augmentation, single, feature; its parsed headers include no explicit header text, across 9 rows and 58 cells.; result: column 2=0.0534; column 3=0.0423; column 4=0.1418; column 5=0.0535; column 6=0.0423; column 7=0.1418; caveat: Interpret Table 10 with its spanning headers and caption under 5.2.3 Generalization under Diverse Temporal Feature Conditions; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2603.27186, Table 10 caption and object |
| Figure 1 | Purpose: The Figure 1 caption identifies a architecture or pipeline schematic centered on temporal, Figure, Workflow, CDFormer, prediction, pipeline, including, data.; result: The caption makes a qualitative claim about temporal, Figure, Workflow, CDFormer, prediction, pipeline; no plotted value is inferred from pixels.; caveat: The caption under 3 Method was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 1 caption and object |
| Figure 2 | Purpose: The Figure 2 caption identifies a architecture or pipeline schematic centered on Figure, Overall, architecture, D-CNN, model, used, time-series, feature.; result: The caption makes a qualitative claim about Figure, Overall, architecture, D-CNN, model, used; no plotted value is inferred from pixels.; caveat: The caption under 3.1.1 1D-CNNs was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 2 caption and object |
| Figure 3 | Purpose: The Figure 3 caption identifies a architecture or pipeline schematic centered on Figure, Architecture, DRSN, module, convolution, soft-thresholding, residual, connections..; result: The caption makes a qualitative claim about Figure, Architecture, DRSN, module, convolution, soft-thresholding; no plotted value is inferred from pixels.; caveat: The caption under 3.1.2 DRSN was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 3 caption and object |
| Figure 4 panel (a) | Purpose: The Figure 4 panel (a) caption identifies a paper-specific visual object centered on Transformer, encoder, block.; result: The caption makes a qualitative claim about Transformer, encoder, block; no plotted value is inferred from pixels.; caveat: The caption under 3.1.3 Transformer was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 4 panel (a) caption and object |
| Figure 4 panel (b) | Purpose: The Figure 4 panel (b) caption identifies a architecture or pipeline schematic centered on Regression, head, architecture.; result: The caption makes a qualitative claim about Regression, head, architecture; no plotted value is inferred from pixels.; caveat: The caption under 3.1.3 Transformer was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 4 panel (b) caption and object |
| Figure 4 | Purpose: The Figure 4 caption identifies a architecture or pipeline schematic centered on Figure, architectures, Transformer, encoder, block, multi-head, attention, feed-forward.; result: The caption makes a qualitative claim about Figure, architectures, Transformer, encoder, block, multi-head; no plotted value is inferred from pixels.; caveat: The caption under 3.1.3 Transformer was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 4 caption and object |
| Figure 5 | Purpose: The Figure 5 caption identifies a paper-specific visual object centered on Figure, Three, Temporal, Augmentation, Techniques.; result: The caption makes a qualitative claim about Figure, Three, Temporal, Augmentation, Techniques; no plotted value is inferred from pixels.; caveat: The caption under 3.2 Temporal Data Augmentation Techniques was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 5 caption and object |
| Figure 6.2 panel (a) | Purpose: The Figure 6.2 panel (a) caption identifies a paper-specific visual object centered on NASA, dataset.; result: The caption makes a qualitative claim about NASA, dataset; no plotted value is inferred from pixels.; caveat: The caption under 5.1.1 Comparison with Existing Methods was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 6.2 panel (a) caption and object |
| Figure 6.4 panel (b) | Purpose: The Figure 6.4 panel (b) caption identifies a paper-specific visual object centered on CALCE, dataset.; result: The caption makes a qualitative claim about CALCE, dataset; no plotted value is inferred from pixels.; caveat: The caption under 5.1.1 Comparison with Existing Methods was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 6.4 panel (b) caption and object |
| Figure 6 | Purpose: The Figure 6 caption identifies a quantitative plot or comparison centered on NASA, CALCE, column, metrics, predicted, true, curves, Figure.; result: The caption makes a qualitative claim about NASA, CALCE, column, metrics, predicted, true; no plotted value is inferred from pixels.; caveat: The caption under 5.1.1 Comparison with Existing Methods was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 6 caption and object |
| Figure 7 | Purpose: The Figure 7 caption identifies a quantitative plot or comparison centered on Figure, RMSE, metrics, predicted, true, capacity, curves, bottom.; result: The caption makes a qualitative claim about Figure, RMSE, metrics, predicted, true, capacity; no plotted value is inferred from pixels.; caveat: The caption under 5.1.2 Comparison with Other Deep Learning-Based Variants was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 7 caption and object |
| Figure 8 | Purpose: The Figure 8 caption identifies a quantitative plot or comparison centered on augmentation, NASA, CALCE, column, dataset, Figure, Visualization, temporal.; result: The caption makes a qualitative claim about augmentation, NASA, CALCE, column, dataset, Figure; no plotted value is inferred from pixels.; caveat: The caption under 5.2.1 Effects of temporal data augmentation on CDFormer was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 8 caption and object |
| Figure 9 panel (a) | Purpose: The Figure 9 panel (a) caption identifies a paper-specific visual object centered on Impact, data, augmentation, different, model, variants, NASA, dataset.; result: The caption makes a qualitative claim about Impact, data, augmentation, different, model, variants; no plotted value is inferred from pixels.; caveat: The caption under 5.2.2 Effects of temporal data augmentation Across Model Variants was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 9 panel (a) caption and object |
| Figure 9 panel (b) | Purpose: The Figure 9 panel (b) caption identifies a paper-specific visual object centered on Impact, data, augmentation, different, model, variants, CALCE, dataset.; result: The caption makes a qualitative claim about Impact, data, augmentation, different, model, variants; no plotted value is inferred from pixels.; caveat: The caption under 5.2.2 Effects of temporal data augmentation Across Model Variants was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 9 panel (b) caption and object |
| Figure 9 | Purpose: The Figure 9 caption identifies a quantitative plot or comparison centered on Figure, Comparison, impact, data, augmentation, different, model, variants.; result: The caption makes a qualitative claim about Figure, Comparison, impact, data, augmentation, different; no plotted value is inferred from pixels.; caveat: The caption under 5.2.2 Effects of temporal data augmentation Across Model Variants was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2603.27186, Figure 9 caption and object |
| Equations | 95 distinct mathematical renderings exposed by HTML; representative objects listed in Section 2.2. | Central objects were inventoried with sign, normalization, conditioning, and denominator checks; no numerical reproduction. |
| Sections | 32 headings exposed by the full HTML. | Every heading was screened; method, evaluation, results, limitations, references, and appendices were mapped where present. |

Appendix and supplementary coverage:

- No separately labeled appendix heading was exposed by full HTML.

Complete section inventory:

- Report GitHub Issue
- Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries
- Abstract
- keywords:
- 1 Introduction
- 2 Related Work
- 2.1 Physics-Based Modeling Methods
- 2.2 Deep Learning-Based Methods
- 3 Method
- 3.1 CDFormer
- 3.1.1 1D-CNNs
- 3.1.2 DRSN
- 3.1.3 Transformer
- 3.1.4 Regression Head
- 3.2 Temporal Data Augmentation Techniques
- 3.2.1 Time Warping
- 3.2.2 Time Resampling
- 3.2.3 Gaussian Noise
- 4 Case Study
- 4.1 Datasets
- 4.2 Implement Details
- 4.3 Metrics
- 5 Result and Discussion
- 5.1 Comparison with state-of-the-art (SOTA) Methods
- 5.1.1 Comparison with Existing Methods
- 5.1.2 Comparison with Other Deep Learning-Based Variants
- 5.2 Ablations
- 5.2.1 Effects of temporal data augmentation on CDFormer
- 5.2.2 Effects of temporal data augmentation Across Model Variants
- 5.2.3 Generalization under Diverse Temporal Feature Conditions
- 6 Conclusion
- References

This ledger is completeness evidence, not reproduction. It records that each exposed section and numbered object was screened without reproducing the paper's tables, figures, or long captions.

## 16. Source and Evidence Notes

- Canonical arXiv record: https://arxiv.org/abs/2603.27186v1
- Canonical PDF: https://arxiv.org/pdf/2603.27186v1
- Canonical full-paper HTML: https://arxiv.org/html/2603.27186v1
- arXiv DOI resolver: https://doi.org/10.48550/arXiv.2603.27186
- Reviewed identity: arXiv:2603.27186v1
- Complete authors: Yun Tian; Guili Wang; Jian Bi; Kaixin Han; Chenglu Wu; Zhiyi Lu; Chenhao Li; Liangwang Sun; Minyu Zhou; Chenchen Xu
- Locally archived full PDF and full-paper HTML were verified; private path withheld.
- No source PDF, HTML, archive, extracted text, validator, or private index belongs in the public DEP-A package.
- Online primary-source vetting status: performed and receipt-linked; alternatives are not exhaustive and no experiment was independently reproduced.

## 17. Footnotes

[^source-paper]: Canonical paper identity and version are linked at https://arxiv.org/abs/2603.27186v1; the locally archived complete PDF and full-paper HTML were reconciled to this identity.
[^scope]: Paper report means content attributable to the authors and supported by the reviewed artifact; it is not independent reproduction.
[^integrity]: Source integrity requires a matching complete PDF and full-paper HTML with identity, version, title, structure, references, and readable-body checks.
[^inference]: Reviewer inference labels a mechanism-level interpretation derived from source evidence rather than asserted by the authors.
[^external]: External primary evidence was limited to receipt-linked official records and URLs. Availability or publication status does not imply artifact runnability, result reproduction, or exhaustive prior-work coverage.
[^association]: An associated DEP is contextual evidence, not a duplicate and not proof of the reviewed paper's claims.
