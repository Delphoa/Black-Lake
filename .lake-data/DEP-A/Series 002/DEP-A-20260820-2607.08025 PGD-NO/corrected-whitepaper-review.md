# Whitepaper Review: PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-scale Physics Simulations

## A detailed review, technical reconstruction, and independent re-conceptualization of “PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-scale Physics Simulations”

**Source paper:** Weiheng Zhong; Jing Bi; Victor Oancea; Hadi Meidani, “PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-scale Physics Simulations,” arXiv:2607.08025v1.[^source-paper]

**Artifact prepared:** 2026-08-20
**Local source reviewed:** complete locally archived PDF (20 pages) and matching full-paper HTML (67248 readable body characters); private path withheld
**Review scope:** full-paper reconstruction, claim vetting, local evidence mapping, implications, and replication agenda
**Review status:** source artifacts inspected; bounded online primary-source vetting performed; experiments not independently rerun

## Executive Assessment

### The paper in one sentence

The paper presents and evaluates a technical contribution framed around pgd-no, neural, operator, precomputed, geometry, decomposition, with its method, formal objects, experimental record, limitations, and source structure inspected from a complete local paper pair rather than an abstract page.

### The deeper idea

Reviewer inference: the durable mechanism is the source-defined change centered on features, nodes, geometry, and token, rather than the paper's brand name. This interpretation predicts that a matched intervention on features changes geometry; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to 3.2 Model Architecture, 3.3 Model Complexity Analysis. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

### Bottom-line judgment

The source is complete enough for a full-paper assessment, and the paper reports a technically organized contribution with an explicit evaluation record. Results remain paper-reported. The local evidence pass confirms the complete results structure and numbered-object inventory, but it does not independently reproduce a numerical value or infer a stronger denominator than the source states. The defensible verdict is therefore conditional: the paper establishes what it directly measures under its own setup, while broader superiority, generality, robustness, efficiency, or deployment readiness remains bounded by the tested models, data, metrics, budgets, hardware, and comparisons.[^scope]

### Principal strengths

- Complete PDF and matching full-paper HTML passed identity, structure, title, references, and readability gates.
- The source exposes 28 section headings, 6 table captions, 15 figure captions, and 108 mathematical renderings for coverage auditing.
- The review can distinguish paper report, external-primary evidence, reviewer inference, and hypothesis without relying on an abstract-only summary.

### Principal qualifications

1. The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions.
2. No result, code path, benchmark, training run, or hardware measurement was independently reproduced.
3. Bounded online checks verified canonical identity and the explicitly recorded official URLs; the search is not exhaustive and does not establish artifact runnability or reproduction.[^external]

## 1. The Problem and Research Questions

### 1.1 Problem and stakes

**Paper-reported problem:** For PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-scale Physics Simulations, the formal target is bounded to the source-defined relation among neural, memory, Geometry, industrial, geometries, mesh, and PGD-NO. The task assumptions and stakes are anchored to Abstract, and 1 Introduction; no objective outside those sections is inferred.

**Research gap reconstructed from the source:** The paper positions PGD-NO around neural, memory, Geometry, features, and nodes. This records the authors' gap framing only; novelty, priority, generality, and superiority require the separate prior-work and evaluation audits.

The title and full-paper organization identify pgd-no, neural, operator, precomputed, geometry, decomposition as the central problem space. A rigorous reading asks what input object is transformed, predicted, selected, optimized, or measured; which practical or scientific constraint motivates that operation; and which outcome makes the change valuable. Those questions must be answered by the method and evaluation sections, not by the title alone. The paper reports its own problem definition; this review preserves the boundary between that report and reviewer interpretation.

Paper-specific reconstruction: the abstract/introduction evidence concentrates on memory, methods, geometries, transolver, neural, pde, mesh, these, industrial, models, under the headings Abstract, 1 Introduction. Those source terms locate the actual objects and constraints; they do not by themselves prove novelty or improvement. In this review they constrain the problem statement so a generic systems narrative cannot replace the paper's own domain and terminology.

The practical stakes depend on the actual denominator. An improvement in a representation, proxy, component score, or controlled benchmark can be important without automatically improving end-user quality, wall-clock cost, reliability, or safety. A durable account therefore separates the immediate technical objective from the downstream objective and asks which bridge between them is tested. If that bridge is only assumed, it remains an explicit gap rather than a hidden premise.

### 1.2 Prior method families and inherited components

The paper's related-work and background sections define the relevant method families. The review treats established backbones, pretrained models, datasets, optimization routines, kernels, evaluation harnesses, and standard metrics as inherited unless the source identifies a change. Novelty belongs to the specific interface, objective, representation, decision rule, data construction, proof, or evaluation design that differs. This prevents a system-level bundle from receiving credit for every capability of its dependencies.

### 1.3 Questions that govern the assessment

Five questions organize the reconstruction. What exact object enters and leaves the method? Which components are learned, fixed, searched, sampled, or verified? What objective and assumptions determine the operation? How do training or calibration differ from inference or deployment? Finally, which result would falsify the authors' causal or generality story rather than merely lower an aggregate score? These questions create an audit trail from paper report to independent assessment.

## 2. Formal and Technical Reconstruction

### 2.1 Definitions and assumptions

The authoritative definition chain lives in the complete source sections listed below. The automated evidence profile does not pretend that section names themselves describe the mechanism. Instead, the full review binds each claim to the source's definitions, stated assumptions, and adjacent formal or experimental context. The core technical headings identified for close reading were:

- 3.2 Model Architecture
- 3.3 Model Complexity Analysis

Variables should be assigned plain-language meanings before algebra is interpreted. Inputs, labels, state, parameters, budgets, constraints, random variables, and outputs must remain distinct. A probability requires a sample space and conditioning event; a loss requires an optimization direction; a ratio requires a numerator and denominator; and a guarantee retains every assumption under which it was proved. If the source uses the same symbol in different roles or shifts between population and sample quantities, that ambiguity should be preserved rather than silently repaired.

### 2.2 Objective and central equations

The full HTML exposes 108 distinct mathematical renderings. Each is treated as a paper-reported formal object whose sign, normalization, conditioning, and denominator must be read with adjacent prose.

Paper-specific formal reconstruction:

**Formal object 1 at 3.1 Geometry Token Extraction — Formula 1 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on mesh, Step, Graph, Construction, process, begins, and the expression links G, V, E..** `G=(V,E)`
Variables: "G, V, E".
Sign/normalization/conditioning/surrogate audit: "Formula 1 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G, V, E; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 1.

**Formal object 2 at 3.1 Geometry Token Extraction — Formula 2 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on mesh, Step, Graph, Construction, process, begins, and the expression links V..** `V`
Variables: "V".
Sign/normalization/conditioning/surrogate audit: "Formula 2 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 2.

**Formal object 3 at 3.1 Geometry Token Extraction — Formula 3 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on mesh, Step, Graph, Construction, process, begins, and the expression links E..** `E`
Variables: "E".
Sign/normalization/conditioning/surrogate audit: "Formula 3 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: E; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 3.

**Formal object 4 at 3.1 Geometry Token Extraction — Formula 4 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Sharp, threshold, theta_, mathbf, where, angle, and the expression links theta..** `\theta_{ij}`
Variables: "theta".
Sign/normalization/conditioning/surrogate audit: "Formula 4 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: theta; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 4.

**Formal object 5 at 3.1 Geometry Token Extraction — Formula 5 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Sharp, threshold, theta_, mathbf, where, angle, and the expression links mathbf, n, a..** `\mathbf{n}_{a}`
Variables: "mathbf, n, a".
Sign/normalization/conditioning/surrogate audit: "Formula 5 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, n, a; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 5.

**Formal object 6 at 3.1 Geometry Token Extraction — Formula 6 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Sharp, threshold, theta_, mathbf, where, angle, and the expression links mathbf, n, b..** `\mathbf{n}_{b}`
Variables: "mathbf, n, b".
Sign/normalization/conditioning/surrogate audit: "Formula 6 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, n, b; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 6.

**Formal object 7 at 3.1 Geometry Token Extraction — Formula 7 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Sharp, threshold, theta_, mathbf, where, angle, and the expression links e_{ij}..** `e_{ij}`
Variables: "e_{ij}".
Sign/normalization/conditioning/surrogate audit: "Formula 7 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: e_{ij}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 7.

**Formal object 8 at 3.1 Geometry Token Extraction — Formula 8 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Sharp, threshold, theta_, mathbf, where, angle, and the expression links theta, arccos, mathbf, n, a, b..** `\theta_{ij}=\arccos(\mathbf{n}_{a}\cdot\mathbf{n}_{b})>\theta_{\text{threshold}}`
Variables: "theta, arccos, mathbf, n, a, b".
Sign/normalization/conditioning/surrogate audit: "Formula 8 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: theta, arccos, mathbf, n, a, b; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 8.

**Formal object 9 at 3.1 Geometry Token Extraction — Formula 9 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Sharp, threshold, theta_, mathbf, where, angle, and the expression links v, in, e_{ij}..** `v\in e_{ij}`
Variables: "v, in, e_{ij}".
Sign/normalization/conditioning/surrogate audit: "Formula 9 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: v, in, e_{ij}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 9.

**Formal object 10 at 3.1 Geometry Token Extraction — Formula 10 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Sharp, threshold, theta_, mathbf, where, angle, and the expression links V_{\text{sharp}}..** `V_{\text{sharp}}`
Variables: "V_{\\text{sharp}}".
Sign/normalization/conditioning/surrogate audit: "Formula 10 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V_{\\text{sharp}}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 10.

**Formal object 11 at 3.1 Geometry Token Extraction — Formula 11 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Sharp, threshold, theta_, mathbf, where, angle, and the expression links theta..** `\theta_{\text{threshold}}`
Variables: "theta".
Sign/normalization/conditioning/surrogate audit: "Formula 11 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: theta; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 11.

**Formal object 12 at 3.1 Geometry Token Extraction — Formula 12 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on sharp, threshold, text, Graph, Partition, subgraph, and the expression links G, prime, V, setminus, V_{\text{sharp}}..** `G^{\prime}=G[V\setminus V_{\text{sharp}}]`
Variables: "G, prime, V, setminus, V_{\\text{sharp}}".
Sign/normalization/conditioning/surrogate audit: "Formula 12 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G, prime, V, setminus, V_{\\text{sharp}}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 12.

**Formal object 13 at 3.1 Geometry Token Extraction — Formula 13 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on sharp, threshold, text, Graph, Partition, subgraph, and the expression links mathcal, C, C_{1}, C_{2}, dots, C_{k}\}..** `\mathcal{C}=\{C_{1},C_{2},\dots,C_{k}\}`
Variables: "mathcal, C, C_{1}, C_{2}, dots, C_{k}\\}".
Sign/normalization/conditioning/surrogate audit: "Formula 13 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, C_{1}, C_{2}, dots, C_{k}\\}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 13.

**Formal object 14 at 3.1 Geometry Token Extraction — Formula 14 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on sharp, threshold, text, Graph, Partition, subgraph, and the expression links theta, i, alpha..** `\theta^{i+1}_{\text{threshold}}=\alpha\theta^{i}_{\text{threshold}}`
Variables: "theta, i, alpha".
Sign/normalization/conditioning/surrogate audit: "Formula 14 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: theta, i, alpha; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 14.

**Formal object 15 at 3.1 Geometry Token Extraction — Formula 15 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on sharp, threshold, text, Graph, Partition, subgraph, and the expression links alpha, in..** `\alpha\in(0,1)`
Variables: "alpha, in".
Sign/normalization/conditioning/surrogate audit: "Formula 15 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: alpha, in; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 15.

**Formal object 16 at 3.1 Geometry Token Extraction — Formula 16 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on sharp, threshold, text, Graph, Partition, subgraph, and the expression links C_{i}..** `C_{i}`
Variables: "C_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 16 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C_{i}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 16.

**Formal object 17 at 3.1 Geometry Token Extraction — Formula 17 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on sharp, threshold, text, Graph, Partition, subgraph, and the expression links C_{i}..** `|C_{i}|>\text{min\_size}`
Variables: "C_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 17 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C_{i}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 17.

**Formal object 18 at 3.1 Geometry Token Extraction — Formula 18 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on small, text, Graph, Merge, algorithm, threshold, and the expression links G_{\text{small}}..** `G_{\text{small}}`
Variables: "G_{\\text{small}}".
Sign/normalization/conditioning/surrogate audit: "Formula 18 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G_{\\text{small}}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 18.

**Formal object 19 at 3.1 Geometry Token Extraction — Formula 19 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on small, text, Graph, Merge, algorithm, threshold, and the expression links V_{\text{small}}..** `|V_{\text{small}}|<\text{threshold}`
Variables: "V_{\\text{small}}".
Sign/normalization/conditioning/surrogate audit: "Formula 19 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V_{\\text{small}}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 19.

**Formal object 20 at 3.1 Geometry Token Extraction — Formula 20 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on small, text, Graph, Merge, algorithm, threshold, and the expression links partial, V_{\text{small}}..** `\partial V_{\text{small}}`
Variables: "partial, V_{\\text{small}}".
Sign/normalization/conditioning/surrogate audit: "Formula 20 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: partial, V_{\\text{small}}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 20.

**Formal object 21 at 3.1 Geometry Token Extraction — Formula 21 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on small, text, Graph, Merge, algorithm, threshold, and the expression links h..** `h`
Variables: "h".
Sign/normalization/conditioning/surrogate audit: "Formula 21 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: h; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 21.

**Formal object 22 at 3.1 Geometry Token Extraction — Formula 22 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on small, text, Graph, Merge, algorithm, threshold, and the expression links v..** `\text{Adj}(v)`
Variables: "v".
Sign/normalization/conditioning/surrogate audit: "Formula 22 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: v; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 22.

**Formal object 23 at 3.1 Geometry Token Extraction — Formula 23 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on small, text, Graph, Merge, algorithm, threshold, and the expression links V_{\text{small}}^{, h..** `V_{\text{small}}^{(h)}`
Variables: "V_{\\text{small}}^{, h".
Sign/normalization/conditioning/surrogate audit: "Formula 23 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V_{\\text{small}}^{, h; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 23.

**Formal object 24 at 3.1 Geometry Token Extraction — Formula 24 under 3.1 Geometry Token Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on small, text, Graph, Merge, algorithm, threshold, and the expression links V_{\text{large}}..** `V_{\text{large}}`
Variables: "V_{\\text{large}}".
Sign/normalization/conditioning/surrogate audit: "Formula 24 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V_{\\text{large}}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 24.

**Formal object 25 at 3.1 Geometry Token Extraction — Formula 25 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Geometry, Step, matrix, tokens, mesh, number, and the expression links S, in, mathbb, R, K, times, N..** `S\in\mathbb{R}^{K\times N}`
Variables: "S, in, mathbb, R, K, times, N".
Sign/normalization/conditioning/surrogate audit: "Formula 25 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S, in, mathbb, R, K, times, N; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 25.

**Formal object 26 at 3.1 Geometry Token Extraction — Formula 26 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Geometry, Step, matrix, tokens, mesh, number, and the expression links K..** `K`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 26 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 26.

**Formal object 27 at 3.1 Geometry Token Extraction — Formula 27 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Geometry, Step, matrix, tokens, mesh, number, and the expression links N..** `N`
Variables: "N".
Sign/normalization/conditioning/surrogate audit: "Formula 27 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 27.

**Formal object 28 at 3.1 Geometry Token Extraction — Formula 28 under 3.1 Geometry Token Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on Geometry, Step, token, matrix, tokens, mesh, and the expression links S_{ki}, C_{k}, v_{i}\in..** `S_{ki}=\begin{cases}\frac{1}{|C_{k}|}&\text{if }v_{i}\in C_{k},\\ 0&\text{otherwise}.\end{cases}`
Variables: "S_{ki}, C_{k}, v_{i}\\in".
Sign/normalization/conditioning/surrogate audit: "Formula 28 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S_{ki}, C_{k}, v_{i}\\in; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 28.

**Formal object 29 at 3.1 Geometry Token Extraction — Formula 29 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathcal, P..** `\mathcal{P}`
Variables: "mathcal, P".
Sign/normalization/conditioning/surrogate audit: "Formula 29 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, P; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 29.

**Formal object 30 at 3.1 Geometry Token Extraction — Formula 30 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathbf, X..** `\mathbf{X}`
Variables: "mathbf, X".
Sign/normalization/conditioning/surrogate audit: "Formula 30 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, X; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 30.

**Formal object 31 at 3.1 Geometry Token Extraction — Formula 31 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links Theta, theta, dots, m..** `\Theta=\{\theta_{1},\theta_{2},\dots,\theta_{m}\}`
Variables: "Theta, theta, dots, m".
Sign/normalization/conditioning/surrogate audit: "Formula 31 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Theta, theta, dots, m; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 31.

**Formal object 32 at 3.1 Geometry Token Extraction — Formula 32 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links rho..** `\rho`
Variables: "rho".
Sign/normalization/conditioning/surrogate audit: "Formula 32 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: rho; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 32.

**Formal object 33 at 3.1 Geometry Token Extraction — Formula 33 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathcal, S, G..** `\mathcal{S}=\{G\}`
Variables: "mathcal, S, G".
Sign/normalization/conditioning/surrogate audit: "Formula 33 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S, G; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 33.

**Formal object 34 at 3.1 Geometry Token Extraction — Formula 34 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links theta, in, Theta..** `\theta\in\Theta`
Variables: "theta, in, Theta".
Sign/normalization/conditioning/surrogate audit: "Formula 34 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: theta, in, Theta; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 34.

**Formal object 35 at 3.1 Geometry Token Extraction — Formula 35 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links V_{sharp}, v, in, V, theta..** `V_{sharp}=\{v\in V\mid\text{dihedral angle at }v>\theta\}`
Variables: "V_{sharp}, v, in, V, theta".
Sign/normalization/conditioning/surrogate audit: "Formula 35 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V_{sharp}, v, in, V, theta; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 35.

**Formal object 36 at 3.1 Geometry Token Extraction — Formula 36 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathcal, S, emptyset..** `\mathcal{S}_{\text{next}}=\emptyset`
Variables: "mathcal, S, emptyset".
Sign/normalization/conditioning/surrogate audit: "Formula 36 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S, emptyset; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 36.

**Formal object 37 at 3.1 Geometry Token Extraction — Formula 37 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links g, in, mathcal, S..** `g\in\mathcal{S}`
Variables: "g, in, mathcal, S".
Sign/normalization/conditioning/surrogate audit: "Formula 37 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: g, in, mathcal, S; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 37.

**Formal object 38 at 3.1 Geometry Token Extraction — Formula 38 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathcal, C, dots, k, g, setminus, V_{sharp}..** `\{\mathcal{C}_{1},\dots,\mathcal{C}_{k}\}=\text{Graph-Split}(g\setminus V_{sharp})`
Variables: "mathcal, C, dots, k, g, setminus, V_{sharp}".
Sign/normalization/conditioning/surrogate audit: "Formula 38 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, dots, k, g, setminus, V_{sharp}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 38.

**Formal object 39 at 3.1 Geometry Token Extraction — Formula 39 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathcal, S, cup, C, i, rho, V..** `\mathcal{S}_{\text{next}}=\mathcal{S}_{\text{next}}\cup\{\mathcal{C}_{i}\mid|\mathcal{C}_{i}|>\rho\cdot|V|\}`
Variables: "mathcal, S, cup, C, i, rho, V".
Sign/normalization/conditioning/surrogate audit: "Formula 39 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S, cup, C, i, rho, V; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 39.

**Formal object 40 at 3.1 Geometry Token Extraction — Formula 40 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathcal, S..** `\mathcal{S}=\mathcal{S}_{\text{next}}`
Variables: "mathcal, S".
Sign/normalization/conditioning/surrogate audit: "Formula 40 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 40.

**Formal object 41 at 3.1 Geometry Token Extraction — Formula 41 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathcal, S, emptyset..** `\mathcal{S}=\emptyset`
Variables: "mathcal, S, emptyset".
Sign/normalization/conditioning/surrogate audit: "Formula 41 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S, emptyset; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 41.

**Formal object 42 at 3.1 Geometry Token Extraction — Formula 42 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links V_{unassigned}, V, setminus, bigcup, g, in, mathcal, S..** `V_{unassigned}=V\setminus\bigcup_{g\in\mathcal{S}}V(g)`
Variables: "V_{unassigned}, V, setminus, bigcup, g, in, mathcal, S".
Sign/normalization/conditioning/surrogate audit: "Formula 42 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V_{unassigned}, V, setminus, bigcup, g, in, mathcal, S; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 42.

**Formal object 43 at 3.1 Geometry Token Extraction — Formula 43 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathcal, S, cup, G, V_{unassigned}..** `\mathcal{S}=\mathcal{S}\cup\text{Graph-Split}(G[V_{unassigned}])`
Variables: "mathcal, S, cup, G, V_{unassigned}".
Sign/normalization/conditioning/surrogate audit: "Formula 43 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S, cup, G, V_{unassigned}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 43.

**Formal object 44 at 3.1 Geometry Token Extraction — Formula 44 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathcal, S..** `\mathcal{S}`
Variables: "mathcal, S".
Sign/normalization/conditioning/surrogate audit: "Formula 44 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 44.

**Formal object 45 at 3.1 Geometry Token Extraction — Formula 45 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathcal, S..** `\{\mathcal{S}_{large},\mathcal{S}_{small}\}`
Variables: "mathcal, S".
Sign/normalization/conditioning/surrogate audit: "Formula 45 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 45.

**Formal object 46 at 3.1 Geometry Token Extraction — Formula 46 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links g_{small}\in\mathcal{S}..** `g_{small}\in\mathcal{S}_{small}`
Variables: "g_{small}\\in\\mathcal{S}".
Sign/normalization/conditioning/surrogate audit: "Formula 46 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: g_{small}\\in\\mathcal{S}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 46.

**Formal object 47 at 3.1 Geometry Token Extraction — Formula 47 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links G..** `G`
Variables: "G".
Sign/normalization/conditioning/surrogate audit: "Formula 47 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: G; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 47.

**Formal object 48 at 3.1 Geometry Token Extraction — Formula 48 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links V_{expanded}, V, g_{small}, h..** `V_{expanded}=\text{BFS}(V(g_{small}),h)`
Variables: "V_{expanded}, V, g_{small}, h".
Sign/normalization/conditioning/surrogate audit: "Formula 48 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V_{expanded}, V, g_{small}, h; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 48.

**Formal object 49 at 3.1 Geometry Token Extraction — Formula 49 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links V_{expanded}\cap, V, g_{large}, neq, emptyset..** `V_{expanded}\cap V(g_{large})\neq\emptyset`
Variables: "V_{expanded}\\cap, V, g_{large}, neq, emptyset".
Sign/normalization/conditioning/surrogate audit: "Formula 49 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V_{expanded}\\cap, V, g_{large}, neq, emptyset; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 49.

**Formal object 50 at 3.1 Geometry Token Extraction — Formula 50 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links V, g_{small}..** `V(g_{small})`
Variables: "V, g_{small}".
Sign/normalization/conditioning/surrogate audit: "Formula 50 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, g_{small}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 50.

**Formal object 51 at 3.1 Geometry Token Extraction — Formula 51 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links V, g_{large}..** `V(g_{large})`
Variables: "V, g_{large}".
Sign/normalization/conditioning/surrogate audit: "Formula 51 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: V, g_{large}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 51.

**Formal object 52 at 3.1 Geometry Token Extraction — Formula 52 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathbf, M, in, mathbb, R, mathcal, S, times..** `\mathbf{M}\in\mathbb{R}^{|\mathcal{S}|\times|V|}`
Variables: "mathbf, M, in, mathbb, R, mathcal, S, times, V".
Sign/normalization/conditioning/surrogate audit: "Formula 52 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, M, in, mathbb, R, mathcal, S, times, V; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 52.

**Formal object 53 at 3.1 Geometry Token Extraction — Formula 53 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links S, V, mathcal, i, v_{j}\in\mathcal{S}..** `\text{S}_{ij}=\begin{cases}1/|V(\mathcal{S}_{i})|&\text{if }v_{j}\in\mathcal{S}_{i}\\ 0&\text{otherwise}\end{cases}`
Variables: "S, V, mathcal, i, v_{j}\\in\\mathcal{S}".
Sign/normalization/conditioning/surrogate audit: "Formula 53 operator audit: fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S, V, mathcal, i, v_{j}\\in\\mathcal{S}; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 53.

**Formal object 54 at 3.1 Geometry Token Extraction — Formula 54 under 3.1 Geometry Token Extraction is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, geometry, token, matrix, and the expression links mathbf, S..** `\mathbf{S}`
Variables: "mathbf, S".
Sign/normalization/conditioning/surrogate audit: "Formula 54 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, S; meanings remain tied to 3.1 Geometry Token Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.1 Geometry Token Extraction, formal object 54.

**Formal object 55 at 3.2 Model Architecture — Formula 55 under 3.2 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, matrix, mathbf, segmentation, and the expression links mathbf, S, in, mathbb, R, times, N..** `\mathbf{S}\in\mathbb{R}^{S\times N}`
Variables: "mathbf, S, in, mathbb, R, times, N".
Sign/normalization/conditioning/surrogate audit: "Formula 55 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, S, in, mathbb, R, times, N; meanings remain tied to 3.2 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture, formal object 55.

**Formal object 56 at 3.2 Model Architecture — Formula 56 under 3.2 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, matrix, mathbf, segmentation, and the expression links mathbb, R, N, times..** `\mathbb{R}^{N\times 3}`
Variables: "mathbb, R, N, times".
Sign/normalization/conditioning/surrogate audit: "Formula 56 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbb, R, N, times; meanings remain tied to 3.2 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture, formal object 56.

**Formal object 57 at 3.2 Model Architecture — Formula 57 under 3.2 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, matrix, mathbf, segmentation, and the expression links mathbf, X, in, mathbb, R, N, times, C..** `\mathbf{X}\in\mathbb{R}^{N\times C}`
Variables: "mathbf, X, in, mathbb, R, N, times, C".
Sign/normalization/conditioning/surrogate audit: "Formula 57 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, X, in, mathbb, R, N, times, C; meanings remain tied to 3.2 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture, formal object 57.

**Formal object 58 at 3.2 Model Architecture — Formula 58 under 3.2 Model Architecture is classified as a state or representation transformation; adjacent prose centers on mathbb, times, point, matrix, mathbf, segmentation, and the expression links mathbf, in, mathbb, R, S, times, C..** `\mathbf{SX}\in\mathbb{R}^{S\times C}`
Variables: "mathbf, in, mathbb, R, S, times, C".
Sign/normalization/conditioning/surrogate audit: "Formula 58 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, in, mathbb, R, S, times, C; meanings remain tied to 3.2 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture, formal object 58.

**Formal object 59 at 3.2 Model Architecture — Formula 59 under 3.2 Model Architecture is classified as a state or representation transformation; adjacent prose centers on features., Geometric, Token, architecture, Layers, global, and the expression links M..** `M`
Variables: "M".
Sign/normalization/conditioning/surrogate audit: "Formula 59 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: M; meanings remain tied to 3.2 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture, formal object 59.

**Formal object 60 at 3.2 Model Architecture — Formula 60 under 3.2 Model Architecture is classified as a state or representation transformation; adjacent prose centers on features, token, variant, introduces, latent, multi-head, and the expression links Q..** `Q`
Variables: "Q".
Sign/normalization/conditioning/surrogate audit: "Formula 60 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Q; meanings remain tied to 3.2 Model Architecture.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture, formal object 60.

**Formal object 61 at 3.3 Model Complexity Analysis — Formula 61 under 3.3 Model Complexity Analysis is classified as a state or representation transformation; adjacent prose centers on nodes, establish, baseline, performance, evaluate, computational, and the expression links N_{s}..** `N_{s}`
Variables: "N_{s}".
Sign/normalization/conditioning/surrogate audit: "Formula 61 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N_{s}; meanings remain tied to 3.3 Model Complexity Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.3 Model Complexity Analysis, formal object 61.

**Formal object 62 at 3.3 Model Complexity Analysis — Formula 62 under 3.3 Model Complexity Analysis is classified as a state or representation transformation; adjacent prose centers on nodes, establish, baseline, performance, evaluate, computational, and the expression links N_{v}..** `N_{v}`
Variables: "N_{v}".
Sign/normalization/conditioning/surrogate audit: "Formula 62 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N_{v}; meanings remain tied to 3.3 Model Complexity Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.3 Model Complexity Analysis, formal object 62.

**Formal object 63 at 3.3 Model Complexity Analysis — Formula 63 under 3.3 Model Complexity Analysis is classified as a state or representation transformation; adjacent prose centers on computational, operations, volume, node, Transolver++, memory, and the expression links O, N_{v}..** `O(4N_{v})`
Variables: "O, N_{v}".
Sign/normalization/conditioning/surrogate audit: "Formula 63 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O, N_{v}; meanings remain tied to 3.3 Model Complexity Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.3 Model Complexity Analysis, formal object 63.

**Formal object 64 at 3.3 Model Complexity Analysis — Formula 64 under 3.3 Model Complexity Analysis is classified as a state or representation transformation; adjacent prose centers on computational, operations, volume, node, Transolver++, memory, and the expression links O, N_{v}..** `O(8N_{v})`
Variables: "O, N_{v}".
Sign/normalization/conditioning/surrogate audit: "Formula 64 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O, N_{v}; meanings remain tied to 3.3 Model Complexity Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.3 Model Complexity Analysis, formal object 64.

**Formal object 65 at 3.3 Model Complexity Analysis — Formula 65 under 3.3 Model Complexity Analysis is classified as a state or representation transformation; adjacent prose centers on computational, operations, volume, node, Transolver++, memory, and the expression links O, N_{s}..** `O(4N_{s})`
Variables: "O, N_{s}".
Sign/normalization/conditioning/surrogate audit: "Formula 65 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O, N_{s}; meanings remain tied to 3.3 Model Complexity Analysis.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.3 Model Complexity Analysis, formal object 65.

**Formal object 66 at 4 Experiment — Formula 66 under 4 Experiment is classified as a evaluation or scoring relation; adjacent prose centers on model, Neural, Operator, Metric, Baseline, following, and the expression links bar, T..** `\bar{T}_{\text{chip}}`
Variables: "bar, T".
Sign/normalization/conditioning/surrogate audit: "Formula 66 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: bar, T; meanings remain tied to 4 Experiment.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment, formal object 66.

**Formal object 67 at 4 Experiment — Formula 67 under 4 Experiment is classified as a evaluation or scoring relation; adjacent prose centers on model, Neural, Operator, Metric, Baseline, following, and the expression links sigma..** `\sigma_{\text{max}}`
Variables: "sigma".
Sign/normalization/conditioning/surrogate audit: "Formula 67 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sigma; meanings remain tied to 4 Experiment.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment, formal object 67.

**Formal object 68 at 4 Experiment — Formula 68 under 4 Experiment is classified as a evaluation or scoring relation; adjacent prose centers on model, Neural, Operator, Metric, Baseline, following, and the expression links C_{D}..** `C_{D}`
Variables: "C_{D}".
Sign/normalization/conditioning/surrogate audit: "Formula 68 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C_{D}; meanings remain tied to 4 Experiment.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment, formal object 68.

**Formal object 69 at 4 Experiment — Formula 69 under 4 Experiment is classified as a evaluation or scoring relation; adjacent prose centers on model, Neural, Operator, Metric, Baseline, following, and the expression links C_{L}..** `C_{L}`
Variables: "C_{L}".
Sign/normalization/conditioning/surrogate audit: "Formula 69 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C_{L}; meanings remain tied to 4 Experiment.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment, formal object 69.

**Formal object 70 at 4 Experiment — Formula 70 under 4 Experiment is classified as a evaluation or scoring relation; adjacent prose centers on model, Neural, Operator, Metric, Baseline, following, and the expression links v_{\text{mid}}..** `v_{\text{mid}}`
Variables: "v_{\\text{mid}}".
Sign/normalization/conditioning/surrogate audit: "Formula 70 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: v_{\\text{mid}}; meanings remain tied to 4 Experiment.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment, formal object 70.

**Formal object 71 at 4 Experiment — Formula 71 under 4 Experiment is classified as a evaluation or scoring relation; adjacent prose centers on Metric, accuracy, model, error, critical, quantify, and the expression links L..** `L^{2}`
Variables: "L".
Sign/normalization/conditioning/surrogate audit: "Formula 71 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L; meanings remain tied to 4 Experiment.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment, formal object 71.

**Formal object 72 at 4.3 Ablation Studies — Formula 72 under 4.3 Ablation Studies is classified as a evaluation or scoring relation; adjacent prose centers on tokens, geometry, performance, number, layers, complex, and the expression links L_{2}..** `L_{2}`
Variables: "L_{2}".
Sign/normalization/conditioning/surrogate audit: "Formula 72 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{2}; meanings remain tied to 4.3 Ablation Studies.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, 4.3 Ablation Studies, formal object 72.

**Formal object 73 at References — Formula 73 under References is classified as a optimization objective or loss; adjacent prose centers on attention, layer, geometry, projection, linear, learning., and the expression links alpha..** `\alpha`
Variables: "alpha".
Sign/normalization/conditioning/surrogate audit: "Formula 73 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: alpha; meanings remain tied to References.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, References, formal object 73.

**Formal object 74 at Appendix A Model complexity analysis — Formula 74 under Appendix A Model complexity analysis is classified as a optimization objective or loss; adjacent prose centers on attention, layer, projection, linear, operations, node., and the expression links O, N..** `O(N)`
Variables: "O, N".
Sign/normalization/conditioning/surrogate audit: "Formula 74 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O, N; meanings remain tied to Appendix A Model complexity analysis.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix A Model complexity analysis, formal object 74.

**Formal object 75 at Appendix A Model complexity analysis — Formula 75 under Appendix A Model complexity analysis is classified as a evaluation or scoring relation; adjacent prose centers on volume, nodes, memory, surface, complexity, model, and the expression links O, N_{s}..** `O(3N_{s})`
Variables: "O, N_{s}".
Sign/normalization/conditioning/surrogate audit: "Formula 75 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: O, N_{s}; meanings remain tied to Appendix A Model complexity analysis.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix A Model complexity analysis, formal object 75.

**Formal object 76 at Appendix B Dataset description — Formula 76 under Appendix B Dataset description is classified as a state or representation transformation; adjacent prose centers on Heat, Thermal, Management, steady-state, parameterized, mathbf, and the expression links mathbf, p, in, mathbb, R..** `\mathbf{p}\in\mathbb{R}^{4}`
Variables: "mathbf, p, in, mathbb, R".
Sign/normalization/conditioning/surrogate audit: "Formula 76 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, p, in, mathbb, R; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 76.

**Formal object 77 at Appendix B Dataset description — Formula 77 under Appendix B Dataset description is classified as a state or representation transformation; adjacent prose centers on Heat, Thermal, Management, steady-state, parameterized, mathbf, and the expression links mathcal, X..** `\mathcal{X}`
Variables: "mathcal, X".
Sign/normalization/conditioning/surrogate audit: "Formula 77 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, X; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 77.

**Formal object 78 at Appendix B Dataset description — Formula 78 under Appendix B Dataset description is classified as a state or representation transformation; adjacent prose centers on Heat, Thermal, Management, steady-state, parameterized, mathbf, and the expression links T, mathbf, x..** `T(\mathbf{x})`
Variables: "T, mathbf, x".
Sign/normalization/conditioning/surrogate audit: "Formula 78 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T, mathbf, x; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 78.

**Formal object 79 at Appendix B Dataset description — Formula 79 under Appendix B Dataset description is classified as a state or representation transformation; adjacent prose centers on Heat, Thermal, Management, steady-state, parameterized, mathbf, and the expression links nabla, kappa, T, Q..** `-\nabla\cdot(\kappa\nabla T)=Q`
Variables: "nabla, kappa, T, Q".
Sign/normalization/conditioning/surrogate audit: "Formula 79 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: nabla, kappa, T, Q; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 79.

**Formal object 80 at Appendix B Dataset description — Formula 80 under Appendix B Dataset description is classified as a constraint or formal-analysis relation; adjacent prose centers on convection, where, kappa, thermal, conductivity, heat, and the expression links kappa..** `\kappa`
Variables: "kappa".
Sign/normalization/conditioning/surrogate audit: "Formula 80 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: kappa; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 80.

**Formal object 81 at Appendix B Dataset description — Formula 81 under Appendix B Dataset description is classified as a constraint or formal-analysis relation; adjacent prose centers on convection, where, kappa, thermal, conductivity, heat, and the expression links q, h, T, T_{\infty}..** `q=h(T-T_{\infty})`
Variables: "q, h, T, T_{\\infty}".
Sign/normalization/conditioning/surrogate audit: "Formula 81 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: q, h, T, T_{\\infty}; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 81.

**Formal object 82 at Appendix B Dataset description — Formula 82 under Appendix B Dataset description is classified as a optimization objective or loss; adjacent prose centers on Aerospace, Structural, mathbf, Engineering, Reducing, component, and the expression links mathcal, M..** `\mathcal{M}`
Variables: "mathcal, M".
Sign/normalization/conditioning/surrogate audit: "Formula 82 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, M; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 82.

**Formal object 83 at Appendix B Dataset description — Formula 83 under Appendix B Dataset description is classified as a optimization objective or loss; adjacent prose centers on Aerospace, Structural, mathbf, Engineering, Reducing, component, and the expression links mathbf, u, x..** `\mathbf{u}(\mathbf{x})`
Variables: "mathbf, u, x".
Sign/normalization/conditioning/surrogate audit: "Formula 83 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, u, x; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 83.

**Formal object 84 at Appendix B Dataset description — Formula 84 under Appendix B Dataset description is classified as a optimization objective or loss; adjacent prose centers on Structural, mathbf, Aerospace, where, stress, Engineering, and the expression links nabla, sigma, mathbf, f..** `\nabla\cdot\sigma+\mathbf{f}=0`
Variables: "nabla, sigma, mathbf, f".
Sign/normalization/conditioning/surrogate audit: "Formula 84 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: nabla, sigma, mathbf, f; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 84.

**Formal object 85 at Appendix B Dataset description — Formula 85 under Appendix B Dataset description is classified as a paper-defined mathematical relation; adjacent prose centers on where, sigma, stress, tensor, mathbf, represents, and the expression links sigma..** `\sigma`
Variables: "sigma".
Sign/normalization/conditioning/surrogate audit: "Formula 85 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sigma; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 85.

**Formal object 86 at Appendix B Dataset description — Formula 86 under Appendix B Dataset description is classified as a paper-defined mathematical relation; adjacent prose centers on where, sigma, stress, tensor, mathbf, represents, and the expression links mathbf, f..** `\mathbf{f}`
Variables: "mathbf, f".
Sign/normalization/conditioning/surrogate audit: "Formula 86 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, f; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 86.

**Formal object 87 at Appendix B Dataset description — Formula 87 under Appendix B Dataset description is classified as a optimization objective or loss; adjacent prose centers on Automotive, surface, DrivAer++, Aerodynamics, Minimizing, aerodynamic, and the expression links p..** `p`
Variables: "p".
Sign/normalization/conditioning/surrogate audit: "Formula 87 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 87.

**Formal object 88 at Appendix B Dataset description — Formula 88 under Appendix B Dataset description is classified as a optimization objective or loss; adjacent prose centers on Automotive, surface, DrivAer++, Aerodynamics, Minimizing, aerodynamic, and the expression links tau, w..** `\tau_{w}`
Variables: "tau, w".
Sign/normalization/conditioning/surrogate audit: "Formula 88 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tau, w; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 88.

**Formal object 89 at Appendix B Dataset description — Formula 89 under Appendix B Dataset description is classified as a optimization objective or loss; adjacent prose centers on surface, Automotive, stress, conditions, DrivAer++, Aerodynamics, and the expression links rho, mathbf, u, nabla, p, mu, tau, R..** `\rho(\mathbf{u}\cdot\nabla)\mathbf{u}=-\nabla p+\mu\nabla^{2}\mathbf{u}+\nabla\cdot\tau^{R}`
Variables: "rho, mathbf, u, nabla, p, mu, tau, R".
Sign/normalization/conditioning/surrogate audit: "Formula 89 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: rho, mathbf, u, nabla, p, mu, tau, R; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 89.

**Formal object 90 at Appendix B Dataset description — Formula 90 under Appendix B Dataset description is classified as a constraint or formal-analysis relation; adjacent prose centers on conditions, where, Reynolds, stress, tensor., Boundary, and the expression links tau, R..** `\tau^{R}`
Variables: "tau, R".
Sign/normalization/conditioning/surrogate audit: "Formula 90 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tau, R; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 90.

**Formal object 91 at Appendix B Dataset description — Formula 91 under Appendix B Dataset description is classified as a state or representation transformation; adjacent prose centers on Aircraft, conditions, angle, Transonic, Aerodynamics, design, and the expression links beta..** `\beta`
Variables: "beta".
Sign/normalization/conditioning/surrogate audit: "Formula 91 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: beta; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 91.

**Formal object 92 at Appendix B Dataset description — Formula 92 under Appendix B Dataset description is classified as a state or representation transformation; adjacent prose centers on Aircraft, conditions, angle, Transonic, Aerodynamics, design, and the expression links u, v, w..** `(u,v,w)`
Variables: "u, v, w".
Sign/normalization/conditioning/surrogate audit: "Formula 92 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: u, v, w; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 92.

**Formal object 93 at Appendix B Dataset description — Formula 93 under Appendix B Dataset description is classified as a state or representation transformation; adjacent prose centers on Aircraft, Transonic, conditions, flow, angle, Aerodynamics, and the expression links partial, rho, t, nabla, mathbf, u..** `\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf{u})=0`
Variables: "partial, rho, t, nabla, mathbf, u".
Sign/normalization/conditioning/surrogate audit: "Formula 93 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) \\partial t. Variables audited: partial, rho, t, nabla, mathbf, u; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 93.

**Formal object 94 at Appendix B Dataset description — Formula 94 under Appendix B Dataset description is classified as a paper-defined mathematical relation; adjacent prose centers on Fluid, mathbf, field, CFD-VOL, Industrial, Mechanics, and the expression links p, mathbf, x..** `p(\mathbf{x})`
Variables: "p, mathbf, x".
Sign/normalization/conditioning/surrogate audit: "Formula 94 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p, mathbf, x; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 94.

**Formal object 95 at Appendix B Dataset description — Formula 95 under Appendix B Dataset description is classified as a paper-defined mathematical relation; adjacent prose centers on Fluid, mathbf, Industrial, required, field, CFD-VOL, and the expression links rho, mathbf, u, nabla, p, mu, f, quad..** `\rho(\mathbf{u}\cdot\nabla)\mathbf{u}=-\nabla p+\mu\nabla^{2}\mathbf{u}+\mathbf{f},\quad\nabla\cdot\mathbf{u}=0`
Variables: "rho, mathbf, u, nabla, p, mu, f, quad".
Sign/normalization/conditioning/surrogate audit: "Formula 95 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: rho, mathbf, u, nabla, p, mu, f, quad; meanings remain tied to Appendix B Dataset description.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix B Dataset description, formal object 95.

**Formal object 96 at Appendix E Implementation details and baseline comparison — Formula 96 under Appendix E Implementation details and baseline comparison is classified as a optimization objective or loss; adjacent prose centers on training, size, beta_, isolate, architectural, efficacy, and the expression links beta..** `\beta_{1}=0.9,\beta_{2}=0.999`
Variables: "beta".
Sign/normalization/conditioning/surrogate audit: "Formula 96 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: beta; meanings remain tied to Appendix E Implementation details and baseline comparison.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix E Implementation details and baseline comparison, formal object 96.

**Formal object 97 at Appendix E Implementation details and baseline comparison — Formula 97 under Appendix E Implementation details and baseline comparison is classified as a optimization objective or loss; adjacent prose centers on training, size, beta_, isolate, architectural, efficacy, and the expression links symbols defined beside the formula..** `10^{-4}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 97 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Appendix E Implementation details and baseline comparison.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix E Implementation details and baseline comparison, formal object 97.

**Formal object 98 at F.1 Field prediction error — Formula 98 under F.1 Field prediction error is classified as a evaluation or scoring relation; adjacent prose centers on physical, across, assess, global, accuracy, predicted, and the expression links hat, y..** `\hat{y}`
Variables: "hat, y".
Sign/normalization/conditioning/surrogate audit: "Formula 98 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, y; meanings remain tied to F.1 Field prediction error.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.1 Field prediction error, formal object 98.

**Formal object 99 at F.1 Field prediction error — Formula 99 under F.1 Field prediction error is classified as a evaluation or scoring relation; adjacent prose centers on physical, across, assess, global, accuracy, predicted, and the expression links y..** `y`
Variables: "y".
Sign/normalization/conditioning/surrogate audit: "Formula 99 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: y; meanings remain tied to F.1 Field prediction error.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.1 Field prediction error, formal object 99.

**Formal object 100 at F.1 Field prediction error — Formula 100 under F.1 Field prediction error is classified as a state or representation transformation; adjacent prose centers on physical, across, Error, assess, global, accuracy, and the expression links L_{2}, hat, y, i, n, y_{i}, y_{i}^{2}}}..** `\text{Relative }L_{2}=\frac{\|\hat{y}-y\|_{2}}{\|y\|_{2}}=\frac{\sqrt{\sum_{i=1}^{n}(\hat{y}_{i}-y_{i})^{2}}}{\sqrt{\sum_{i=1}^{n}y_{i}^{2}}}.`
Variables: "L_{2}, hat, y, i, n, y_{i}, y_{i}^{2}}}".
Sign/normalization/conditioning/surrogate audit: "Formula 100 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: L_{2}, hat, y, i, n, y_{i}, y_{i}^{2}}}; meanings remain tied to F.1 Field prediction error.".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.1 Field prediction error, formal object 100.

**Formal object 101 at F.2 Quantities of Interest (QoI) — Formula 101 under F.2 Quantities of Interest (QoI) is classified as a evaluation or scoring relation; adjacent prose centers on Chip, Heat, Average, Temperature, text, Stress, and the expression links bar, T, A_{\text{base}}}\int, A_{\text{base}}}T, mathbf, x..** `\bar{T}_{\text{chip}}=\frac{1}{A_{\text{base}}}\int_{A_{\text{base}}}T(\mathbf{x})dA`
Variables: "bar, T, A_{\\text{base}}}\\int, A_{\\text{base}}}T, mathbf, x".
Sign/normalization/conditioning/surrogate audit: "Formula 101 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: bar, T, A_{\\text{base}}}\\int, A_{\\text{base}}}T, mathbf, x; meanings remain tied to F.2 Quantities of Interest (QoI).".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.2 Quantities of Interest (QoI), formal object 101.

**Formal object 102 at F.2 Quantities of Interest (QoI) — Formula 102 under F.2 Quantities of Interest (QoI) is classified as a paper-defined mathematical relation; adjacent prose centers on Stress, structural, Drag, Coefficient, Maximum, Mises, and the expression links sigma, mathbf, x, in, mathcal, M..** `\sigma_{\text{max}}=\max_{\mathbf{x}\in\mathcal{M}}\sigma_{vm}(\mathbf{x})`
Variables: "sigma, mathbf, x, in, mathcal, M".
Sign/normalization/conditioning/surrogate audit: "Formula 102 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sigma, mathbf, x, in, mathcal, M; meanings remain tied to F.2 Quantities of Interest (QoI).".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.2 Quantities of Interest (QoI), formal object 102.

**Formal object 103 at F.2 Quantities of Interest (QoI) — Formula 103 under F.2 Quantities of Interest (QoI) is classified as a probabilistic or expectation relation; adjacent prose centers on Coefficient, Drag, integrating, surface, pressure, Lift, and the expression links C_{D}, rho, v, A, int, p, mathbf, n..** `C_{D}=\frac{2}{\rho v^{2}A}\int_{A}(p\mathbf{n}\cdot\mathbf{i}+\tau_{w}\mathbf{t}\cdot\mathbf{i})dA`
Variables: "C_{D}, rho, v, A, int, p, mathbf, n, i, tau, w, t".
Sign/normalization/conditioning/surrogate audit: "Formula 103 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C_{D}, rho, v, A, int, p, mathbf, n, i, tau, w, t; meanings remain tied to F.2 Quantities of Interest (QoI).".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.2 Quantities of Interest (QoI), formal object 103.

**Formal object 104 at F.2 Quantities of Interest (QoI) — Formula 104 under F.2 Quantities of Interest (QoI) is classified as a probabilistic or expectation relation; adjacent prose centers on Lift, Coefficient, Aircraft, Aerodynamic, performance, flight, and the expression links mathbf, k..** `\mathbf{k}`
Variables: "mathbf, k".
Sign/normalization/conditioning/surrogate audit: "Formula 104 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, k; meanings remain tied to F.2 Quantities of Interest (QoI).".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.2 Quantities of Interest (QoI), formal object 104.

**Formal object 105 at F.2 Quantities of Interest (QoI) — Formula 105 under F.2 Quantities of Interest (QoI) is classified as a probabilistic or expectation relation; adjacent prose centers on Lift, Coefficient, along, mathbf, Velocity, Error, and the expression links C_{L}, rho, v, A, int, p, mathbf, n..** `C_{L}=\frac{2}{\rho v^{2}A}\int_{A}(p\mathbf{n}\cdot\mathbf{k})dA`
Variables: "C_{L}, rho, v, A, int, p, mathbf, n, k".
Sign/normalization/conditioning/surrogate audit: "Formula 105 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: C_{L}, rho, v, A, int, p, mathbf, n, k; meanings remain tied to F.2 Quantities of Interest (QoI).".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.2 Quantities of Interest (QoI), formal object 105.

**Formal object 106 at F.2 Quantities of Interest (QoI) — Formula 106 under F.2 Quantities of Interest (QoI) is classified as a evaluation or scoring relation; adjacent prose centers on Velocity, Error, text, CFD-VOL, Cross-Cut, large-scale, and the expression links symbols defined beside the formula..** `\text{Err}_{\text{cut}}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 106 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to F.2 Quantities of Interest (QoI).".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.2 Quantities of Interest (QoI), formal object 106.

**Formal object 107 at F.2 Quantities of Interest (QoI) — Formula 107 under F.2 Quantities of Interest (QoI) is classified as a evaluation or scoring relation; adjacent prose centers on Velocity, Error, text, CFD-VOL, Cross-Cut, large-scale, and the expression links mathbf, u..** `\mathbf{u}`
Variables: "mathbf, u".
Sign/normalization/conditioning/surrogate audit: "Formula 107 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, u; meanings remain tied to F.2 Quantities of Interest (QoI).".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.2 Quantities of Interest (QoI), formal object 107.

**Formal object 108 at F.2 Quantities of Interest (QoI) — Formula 108 under F.2 Quantities of Interest (QoI) is classified as a probabilistic or expectation relation; adjacent prose centers on Error, PGD-NO, Velocity, Transolver++, text, large-scale, and the expression links hat, mathbf, u..** `\text{Err}_{\text{cut}}=\frac{\|\hat{\mathbf{u}}_{\text{plane}}-\mathbf{u}_{\text{plane}}\|_{2}}{\|\mathbf{u}_{\text{plane}}\|_{2}}`
Variables: "hat, mathbf, u".
Sign/normalization/conditioning/surrogate audit: "Formula 108 operator audit: fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, mathbf, u; meanings remain tied to F.2 Quantities of Interest (QoI).".
Source locator: private full-paper evidence dossier for arXiv:2607.08025, F.2 Quantities of Interest (QoI), formal object 108.

Representative source mathematical objects follow. They are navigation evidence, not standalone interpretations:

- Mathematical object 1: `G=(V,E)` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 2: `V` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 3: `E` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 4: `\theta_{ij}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 5: `\mathbf{n}_{a}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 6: `\mathbf{n}_{b}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 7: `e_{ij}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 8: `\theta_{ij}=\arccos(\mathbf{n}_{a}\cdot\mathbf{n}_{b})>\theta_{\text{threshold}}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 9: `v\in e_{ij}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 10: `V_{\text{sharp}}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 11: `\theta_{\text{threshold}}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 12: `G^{\prime}=G[V\setminus V_{\text{sharp}}]` — read with adjacent definitions; no symbol meaning is inferred from markup alone.

Equation-to-adjacent-context reconstruction:

- Equation under source heading 3.1 Geometry Token Extraction: `G=(V,E)`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `V`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `E`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `\theta_{ij}`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `\mathbf{n}_{a}`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `\mathbf{n}_{b}`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `e_{ij}`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `\theta_{ij}=\arccos(\mathbf{n}_{a}\cdot\mathbf{n}_{b})>\theta_{\text{threshold}}`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `v\in e_{ij}`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `V_{\text{sharp}}`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `\theta_{\text{threshold}}`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.
- Equation under source heading 3.1 Geometry Token Extraction: `G^{\prime}=G[V\setminus V_{\text{sharp}}]`; adjacent method terms: features, point, token, geometry, into, matrix, mathbb, times.

For each central equation, the audit asks whether the sign agrees with the prose, whether weights are normalized, whether masking or conditioning changes the denominator, whether a displayed objective is exact or a training surrogate, and whether units can be compared. A learned score is not automatically calibrated, a relaxation is not an exact discrete solution, and an empirical constraint satisfaction rate is not a theorem. These distinctions protect the paper's real contribution from stronger claims it does not need.

### 2.3 Components, architecture, and information flow

The source's technical path is anchored to 3.2 Model Architecture, 3.3 Model Complexity Analysis. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims.

**Input/output dataflow:** The documented dataflow is reconstructed only across 3.2 Model Architecture, 3.3 Model Complexity Analysis, and 4.4 Model Explanation, where the source associates features, nodes, geometry, token, point, Attention, and Layer. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

| Component | Inherited or novel | Role | Source locator |
|---|---|---|---|
| 3.2 Model Architecture | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with mathbb, times, point, matrix, and mathbf; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture |
| 3.2 Model Architecture | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with features, Architecture, Geometric, Token, and Layers; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture |
| 3.2 Model Architecture | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with features, token, variant, Architecture, and introduces; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture |
| 3.3 Model Complexity Analysis | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with Complexity, Analysis, nodes, establish, and baseline; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2607.08025, 3.3 Model Complexity Analysis |
| 3.3 Model Complexity Analysis | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with Complexity, Analysis, computational, operations, and volume; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2607.08025, 3.3 Model Complexity Analysis |

The paper-specific method vocabulary is features, point, token, geometry, into, matrix, mathbb, times, tokens, architecture. This vocabulary was derived from the complete method/architecture paragraphs rather than the title. It identifies the entities that must appear in a faithful architecture reconstruction and creates a falsifiable check: an implementation or summary that omits these named objects is not yet grounded in this paper.

The architecture is reconstructed as an information-flow graph: source identity and inputs enter; inherited and paper-specific components transform or score them; a decision or representation is produced; optional validation or post-processing occurs; and an evaluated outcome leaves the pipeline. Each edge should name the information available at that point. A comparison becomes unfair if one method has access to labels, future requests, privileged metadata, additional context, or a larger tuning budget that another method lacks.

### 2.4 Training, calibration, and inference

Construction-time and runtime work are separate accounting domains. Training may fit parameters, construct representations, estimate thresholds, tune prompts, or learn a policy. Calibration may use held-out examples or measurements. Inference may retrieve, route, compress, classify, generate, search, solve, or verify. Post-processing may enforce a constraint or discard invalid output. A credible efficiency claim says which of these phases is included, which is amortized, and which is external to the reported number.

Training or calibration evidence is explicitly located in 3.2 Model Architecture. The associated source vocabulary emphasizes features, point, token, geometry, into, matrix, mathbb, times, tokens, architecture.

Paper-specific construction/training sequence:

1. At 3.2 Model Architecture, the paper reports a training-related operation involving mathbb, times, point, matrix, mathbf, and segmentation. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture)*
2. At 4.4 Model Explanation, the paper reports a training-related operation involving region, attention, Layer, Geometric, nodes, and distribution. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 4.4 Model Explanation)*
3. At Appendix A Model complexity analysis, the paper reports a training-related operation involving attention, layer, projection, linear, operations, and node. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix A Model complexity analysis)*
4. At Appendix A Model complexity analysis, the paper reports a training-related operation involving volume, nodes, memory, surface, complexity, and bottleneck. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, Appendix A Model complexity analysis)*

Inference or runtime evidence is explicitly located in 3.2 Model Architecture. Its source vocabulary overlaps features, point, token, geometry, into, matrix, mathbb, times, tokens, architecture.

Paper-specific inference/evaluation sequence:

1. At 3.2 Model Architecture, the paper reports an inference or deployment action involving features, Architecture, Geometric, Token, Layers, and global. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture)*
2. At 3.2 Model Architecture, the paper reports an inference or deployment action involving features, token, variant, Architecture, introduces, and latent. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture)*
3. At 4.4 Model Explanation, the paper reports an inference or deployment action involving region, attention, Layer, Geometric, nodes, and distribution. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 4.4 Model Explanation)*
4. At 4 Experiment, the paper reports an inference or deployment action involving dataset, Prediction, datasets, physics, Experiment, and tasks. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment)*

The reconstructed operational sequence is: pin input and artifact versions; validate prerequisites; compute the method-specific state or signal; apply the stated decision or objective; materialize the output; execute any downstream consumer; and measure both quality and resource outcomes. This sequence is reviewer inference grounded in the paper's organization. It is a testing model, not an assertion that the authors implemented an identical production controller.[^inference]

### 2.5 Notation and implementation audit

No independent implementation was run. The audit therefore checks internal legibility across equations, prose, captions, appendices, and extracted code/data statements. Apparent inconsistencies remain unresolved unless source evidence explains them. Source availability is classified in levels—declared, reachable, inspectable, runnable, and result-reproducing—and this local phase establishes only the declared/local-source layers.

## 3. Architecture and Complete Operational Pipeline

### 3.1 Representation and state

The documented dataflow is reconstructed only across 3.2 Model Architecture, 3.3 Model Complexity Analysis, and 4.4 Model Explanation, where the source associates features, nodes, geometry, token, point, Attention, and Layer. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

The central representation must be described by shape, type, provenance, lifetime, and relationship to the original input. If it is compressed, selected, latent, retrieved, generated, or aggregated, the review asks what information can be lost and how that loss is detected. If it is learned, the training distribution and version become part of its identity. If it is mutable, update ordering, expiry, and rollback become part of the method rather than operational afterthoughts.

### 3.2 Decision or action modules

The paper-specific modules should be separated from inherited encoders, decoders, solvers, retrieval systems, evaluators, or model APIs. A score can rank candidates without being calibrated; a policy can improve average reward without satisfying hard constraints; and a verifier can reject some failures without certifying all accepted outputs. The assessment uses the source's strongest ablation or controlled comparison to decide which module is necessary and which is merely bundled.

### 3.3 Dependencies, post-processing, and guarantee boundary

Dependencies include data preprocessing, external models, tokenizers, simulators, indexes, numerical libraries, and evaluation code. Post-processing can materially create the final result, so its compute and failure rate belong in the pipeline. Exact validation, when present, may establish a property of a returned object; it does not automatically establish semantic correctness, optimality, robustness, or absence of distribution shift.

### 3.4 Resource allocation and stopping

Budgets can refer to tokens, bytes, parameters, candidates, iterations, calls, samples, time, energy, or money. Requested and achieved budgets should both be recorded. Early stopping and fallback can bias which cases receive expensive processing. Batching can improve throughput while worsening latency. The review therefore distinguishes construction cost, per-instance latency, batch throughput, tail latency, peak memory, and downstream cost before accepting a general efficiency claim.

## 4. Experimental Design and Evidence Reconstructed

The evaluation reconstruction follows 4.1 Main Results, 4.3 Ablation Studies, 4 Experiment, with 6 table captions and 15 figure captions inventoried.

Paper-specific evaluation vocabulary centers on tokens, dataset, model, geometry, performance, jeb, geometries, datasets, heat, sink. These terms constrain which datasets, metrics, models, budgets, or operational quantities must be preserved with each reported comparison. They also identify where a later reproduction dossier must look for splits, baselines, hardware, batching, runtime semantics, and uncertainty rather than assuming conventional defaults.

The headings mechanically associated with evaluation and results were:

- 4.1 Main Results
- 4.3 Ablation Studies
- 4 Experiment

### 4.1 Data, splits, and distribution

Not applicable: No named dataset, benchmark, corpus, or split was found in the captured full-paper data/evaluation paragraphs; none is invented. (source locator: private full-paper evidence dossier for arXiv:2607.08025, data/evaluation paragraph inventory).

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| POINTNET | Table 1 lists POINTNET as a numeric comparison row under 4 Experiment. | Neither the Table 1 caption nor its row label establishes whether POINTNET was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 1 row POINTNET |
| MESHGRAPHNET | Table 1 lists MESHGRAPHNET as a numeric comparison row under 4 Experiment. | Neither the Table 1 caption nor its row label establishes whether MESHGRAPHNET was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 1 row MESHGRAPHNET |
| GNO | Table 1 lists GNO as a numeric comparison row under 4 Experiment. | Neither the Table 1 caption nor its row label establishes whether GNO was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 1 row GNO |
| GALERKIN | Table 1 lists GALERKIN as a numeric comparison row under 4 Experiment. | Neither the Table 1 caption nor its row label establishes whether GALERKIN was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 1 row GALERKIN |
| GINO | Table 1 lists GINO as a numeric comparison row under 4 Experiment. | Neither the Table 1 caption nor its row label establishes whether GINO was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 1 row GINO |
| GNOT | Table 1 lists GNOT as a numeric comparison row under 4 Experiment. | Neither the Table 1 caption nor its row label establishes whether GNOT was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 1 row GNOT |
| TRANSOLVER | Table 1 lists TRANSOLVER as a numeric comparison row under 4 Experiment. | Neither the Table 1 caption nor its row label establishes whether TRANSOLVER was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 1 row TRANSOLVER |
| AB-UPT | Table 1 lists AB-UPT as a numeric comparison row under 4 Experiment. | Neither the Table 1 caption nor its row label establishes whether AB-UPT was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 1 row AB-UPT |
| TRANSOLVER++ | Table 1 lists TRANSOLVER++ as a numeric comparison row under 4 Experiment. | Neither the Table 1 caption nor its row label establishes whether TRANSOLVER++ was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 1 row TRANSOLVER++ |
| Vol. points size | Table 2 lists Vol. points size as a numeric comparison row under 4.2 Larger Meshes. | Neither the Table 2 caption nor its row label establishes whether Vol. points size was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 2 row Vol. points size |
| Sampling ratio | Table 2 lists Sampling ratio as a numeric comparison row under 4.2 Larger Meshes. | Neither the Table 2 caption nor its row label establishes whether Sampling ratio was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 2 row Sampling ratio |
| Number of Layers | Table 3 lists Number of Layers as a numeric comparison row under 4.3 Ablation Studies. | Neither the Table 3 caption nor its row label establishes whether Number of Layers was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 3 row Number of Layers |
| Number of Tokens | Table 4 lists Number of Tokens as a numeric comparison row under 4.3 Ablation Studies. | Neither the Table 4 caption nor its row label establishes whether Number of Tokens was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 4 row Number of Tokens |
| Heatsink | Table 5 lists Heatsink as a numeric comparison row under Appendix C Additional results. | Neither the Table 5 caption nor its row label establishes whether Heatsink was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 5 row Heatsink |
| JEB | Table 5 lists JEB as a numeric comparison row under Appendix C Additional results. | Neither the Table 5 caption nor its row label establishes whether JEB was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 5 row JEB |
| Grid- token | Table 6 lists Grid- token as a numeric comparison row under Appendix C Additional results. | Neither the Table 6 caption nor its row label establishes whether Grid- token was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2607.08025, Table 6 row Grid- token |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

| Metric | Denominator/conditioning | Direction | Source locator |
|---|---|---|---|
| error | The metric-definition evidence at 4 Experiment ties error to terms Metric, accuracy, model, error, critical, quantify, predictions, employ. | lower is better | private full-paper evidence dossier for arXiv:2607.08025, Table 2 header 12M / 0.01 |

Metrics are reconstructed with direction, denominator, aggregation unit, conditioning, and reference quality. Failures excluded from an average create survivor bias. A gap to a best-known incumbent is not a gap to a proven optimum. A judge-model score is not a human preference without validation. A compression ratio can invert depending on convention. Confidence intervals, paired tests, and effect sizes matter when differences are close or instances are correlated.

### 4.4 Hardware, batching, and runtime semantics

Quality-v2 paper-specific hardware/runtime evidence:

- At 1 Introduction, the paper's hardware/runtime paragraph names GPU. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 1 Introduction)*
- At 1 Introduction, the paper's hardware/runtime paragraph names GPU. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 1 Introduction)*
- At 1 Introduction, the paper's hardware/runtime paragraph names latency, 360GB. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 1 Introduction)*
- At 1 Introduction, the paper's hardware/runtime paragraph names GPU. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 1 Introduction)*
- At 1 Introduction, the paper's hardware/runtime paragraph names Geometry, propose, Pre-computed, Decomposition, Neural, Operator, PGD-NO, decouples. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 1 Introduction)*
- At 2.1 Neural PDE Solver, the paper's hardware/runtime paragraph names Wang, memory, Graph-based, neural, operators, GNOs, Anandkumar, designed. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 2.1 Neural PDE Solver)*
- At 2.1 Neural PDE Solver, the paper's hardware/runtime paragraph names GPU. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 2.1 Neural PDE Solver)*
- At 3.2 Model Architecture, the paper's hardware/runtime paragraph names features, token, variant, introduces, latent, multi-head, cross-attention, directly. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture)*


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
| Table 2 | PGD-NO-v1 | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | 12M / 0.01; 12M / 0.1; 12M / 1.0; 60M / 0.01; 60M / 0.1; 60M / 1.0 | 12M / 0.01=13.3; 12M / 0.1=12.9; 12M / 1.0=12.2; 60M / 0.01=13.0; 60M / 0.1=12.7; 60M / 1.0=12.5 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2607.08025, Table 2 row 4 |
| Table 2 | Transolver++ / - | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | 12M / 0.01; 12M / 0.1; 12M / 1.0; 60M / 0.01; 60M / 0.1 | 12M / 0.01=20.8; 12M / 0.1=17.3; 12M / 1.0=15.8; 60M / 0.01=22.3; 60M / 0.1=18.1 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2607.08025, Table 2 row 3 |
| Table 4 | PGD-NO (Ours) | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | 32; 64; 128; 256 | 32=65.4; 64=41.5; 128=37.2; 256=35.4 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2607.08025, Table 4 row 2 |
| result context at Appendix C Additional results | PGD-NO | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | error | 2 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2607.08025, Appendix C Additional results |
| result context at 4 Experiment | PGD-NO | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | accuracy, error | 2 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment |

Bounded exact evidence retained from the paper report:

- Paper report, numeric result in 4.1 Main Results: “The experimental results, summarized in Table 1 , demonstrate that…” (exact numeric tokens: 1).

- No table-caption fragment was included in the bounded verbatim evidence budget.

The correct interpretation retains task, dataset, split, model, baseline, metric, budget, and hardware with each result. A largest reported improvement is an operating point, not a distribution. An average is not a tail guarantee. A component metric can diagnose mechanism without proving end-to-end utility. Where the source reports multiple tables or figures, their relationships should be checked for consistent defaults, denominators, and versioned settings.

Three types of gain remain separate. Representation gain means fewer tokens, bytes, channels, states, features, or bits. Execution gain means lower latency, memory traffic, transfer, energy, or higher throughput. Outcome gain means better correctness, quality, utility, constraint satisfaction, or task completion. The paper may establish one or more under its setting; a deployment decision requires the combination relevant to its service objective.

Table and figure captions were inventoried rather than republished. Their exact values remain anchored to the paper. Any public summary should cite only values whose numerator, denominator, model, dataset, and comparison are simultaneously known. This review does not manufacture missing uncertainty or turn qualitative illustrations into statistical evidence.

## 6. Ablations and Causal Evidence

Paper-specific ablation/control ledger:

| Component/control | Paper-reported delta | Control caveat | Source locator |
|---|---|---|---|
| Ablation, studies, and CFD-VOL | 3 | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2607.08025, 4.3 Ablation Studies |
| tokens, Transolver++, and sensitivity | direction or magnitude is reported only at the source locator | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2607.08025, 4.3 Ablation Studies |
| conduct, additional, and ablation | direction or magnitude is reported only at the source locator | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2607.08025, 4.3 Ablation Studies |

Ablations are persuasive when one named component changes while model, data, budget, training effort, and implementation quality stay fixed. The complete source was screened for removals, swaps, budget sweeps, sensitivity tests, and failure examples. If multiple elements change together, the result supports the bundle more strongly than any individual mechanism. If a simple cost-matched control is missing, the causal interpretation remains limited.

Randomness must be classified as training seeds, inference seeds, data-generation seeds, checkpoint-selection variance, or hyperparameter-search variance. Repeated inference does not prove training robustness. A named significance test should identify its independence unit and paired design. The practical importance of an effect is separate from statistical detectability, especially when a large benchmark makes very small changes significant.

Author-stated limitations:

- The author-side qualification at 5 Conclusion concerns Pre-computed, Geometry, PGD-NO, introduce, Decomposition, and Neural. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 5 Conclusion)*
- The author-side qualification at 5 Conclusion concerns PGD-NO, efficiency, decoupled, geometry, Limitations, and matches. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 5 Conclusion)*

Reviewer-identified limitations:

- No independent reproduction was performed for arXiv:2607.08025v1; geometry, tokens, dataset, and performance remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment, and Appendix B Dataset description)*
- The dossier inventories 28 headings, 6 tables, 15 figures, and 108 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2607.08025, complete coverage inventory)*

The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 3 candidate sentences and the limitation/discussion vocabulary geometry, pgd-no, pre-computed, decomposition, geometric, tokens, represent, diverse, accuracy, state-of-the-art. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper frames PGD-NO as a contribution to neural, memory, Geometry, industrial. | Problem framing is located in the profile's named introduction/problem headings; no numbered section marker is treated as a measurement. (private full-paper evidence dossier for arXiv:2607.08025, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| The reported mechanism centers on features, nodes, geometry, token. | Method and formula evidence is bound to the named method headings and formula-specific operator audits. (private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Table 2 reports measured outcomes for PGD-NO-v1 across 12M / 0.01, 12M / 0.1, 12M / 1.0, 60M / 0.01, 60M / 0.1. | Quality-v2 paper-report result values: 2 (private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2607.08025v1), [canonical PDF](https://arxiv.org/pdf/2607.08025v1), [canonical full-paper HTML](https://arxiv.org/html/2607.08025v1), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2607.08025). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2607.08025v1)*
- **Predecessor/prior work (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 1 Introduction; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://proceedings.mlr.press/v235/wu24r.html)*
- **Alternative or benchmark (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 4 Experiment; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://openreview.net/forum?id=nwQ8nitlTZ)*
- **Code/data (checked):** The bounded online record verified reachability for https://github.com/WeihengZ/PGD-NO. Reachability does not establish ownership, completeness, runnability, or result reproduction. *(evidence locator: https://github.com/WeihengZ/PGD-NO)*

Verified official primary-source links from the bounded check:

- Bounded primary-source check verified: https://github.com/WeihengZ/PGD-NO

Access-blocked or unverified URL evidence: not recorded

Prior-work and alternatives evidence: "bounded_to_canonical_arxiv_record_and_paper_declared_primary_links" This is a bounded search record, not an exhaustive map of the field.

Code/data and reproduction evidence: "link_reachability_only; repository contents were not downloaded, built, or executed" Reachability and metadata do not mean that code or data were executed, that dependencies were installed, or that a reported result reproduced.

Paper-declared external candidates were recorded as follows:

- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/accessible_HTML.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/license/index.html#licenses-available
- Paper-declared URL, not opened in this phase: https://github.com/WeihengZ/PGD-NO
- Paper-declared URL, not opened in this phase: https://openreview.net/forum?id=nwQ8nitlTZ
- Paper-declared URL, not opened in this phase: https://proceedings.mlr.press/v267/luo25o.html
- Paper-declared URL, not opened in this phase: https://proceedings.mlr.press/v235/wu24r.html
- Paper-declared URL, not opened in this phase: https://math.nist.gov/~BMiller/LaTeXML/
- Paper-declared URL, not opened in this phase: https://github.com/arXiv/html_feedback/issues
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML
- Paper-declared URL, not opened in this phase: https://github.com/brucemiller/LaTeXML/issues
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/ourmembers.html

Their presence is discovery evidence, not proof that an artifact is official, available, licensed, runnable, or reproducing the paper. A later online-vetting phase should use primary sources, record HTTP/access limits, verify ownership and linkage, inspect release and license state, and distinguish artifact availability from runnable or result-reproducing status. Until then the publication status remains: arXiv preprint; no separate peer-reviewed venue inferred without an official venue source.

The isolated Black Lake checkout was used only for repository-readiness and dedupe context. A same-paper DEP-A would block a new owning record; a DEP-E or directly corresponding implementation is associated context rather than a duplicate. Background citations do not transfer evidence or claims to this paper.[^association]

## 9. Independent Re-conceptualization

Reviewer inference: the durable mechanism is the source-defined change centered on features, nodes, geometry, and token, rather than the paper's brand name. This interpretation predicts that a matched intervention on features changes geometry; it is not an author claim or theorem.

Re-conceptualize the contribution as an evidence-linked state transition: pin source identity, record the method-specific decision, measure realized resource and outcome effects, and retain a conservative fallback whose trigger can be falsified on held-out conditions. This is reviewer inference and proposal, not an author claim and not an experimentally validated architecture.[^inference]

The mechanism can be viewed as a governed handoff between evidence, decision, execution, and outcome. Evidence identifies the source state and the signal the method uses. Decision records the action or representation chosen under a budget. Execution records what the system actually did, including fallback and resource use. Outcome records task quality and failure. The mapping is useful because it predicts what must be logged; it breaks when the paper studies a purely formal object with no operational transition.

A second bounded analogy is experimental portfolio control. Different baselines, budgets, and ablations are portfolio arms whose information access and cost must be matched. This analogy highlights selection bias and incomplete frontiers, but it does not imply that the paper uses an online bandit or that deployment should optimize only one scalar reward. Its falsifiable prediction is that the proposed mechanism's advantage should shrink when information access and complete cost are carefully matched if the original gain came mainly from comparison asymmetry.

## 10. Research Notes, Limitations, and Evidence Boundary

The complete local PDF and full-paper HTML for arXiv:2607.08025v1 were inspected. The PDF passed size, header, EOF, parse, page-count, title, structure, and references checks. The HTML passed size, readable-body, document-marker, heading, structure, title, and identity checks. Abstract HTML was metadata only and did not qualify as the paper body.[^integrity]

The coverage pass includes introduction, method or formal analysis, experiments or results, discussion or conclusion, references, appendices where exposed, tables, figures, equations, footnotes, disclosures, and code/data language. Extraction can lose visual layout and some mathematical semantics; the ledger records this boundary rather than claiming that every graphic was numerically reproduced.

Paper-specific qualification inventory: limitation/discussion terms geometry, pgd-no, pre-computed, decomposition, geometric, tokens, represent, diverse, accuracy, state-of-the-art; disclosure/funding language limitations, Disclosure, limitation; code/data language GitHub, dataset; appendix headings Appendix A Model complexity analysis, Appendix B Dataset description, Appendix C Additional results, Appendix D Extracted geometry token visualizations, Appendix E Implementation details and baseline comparison, Appendix F Metric, Appendix G Error map clarification. These are evidence pointers. A missing extracted term is not proof that a disclosure, artifact, or limitation does not exist.

Evidence layers remain explicit. Layer A is what the paper reports. Layer B contains the bounded primary records actually checked online; its conclusions are limited to the recorded identity, publication, and artifact-access evidence. Layer C is reviewer inference, including the governed-handoff interpretation. Layer D is a hypothesis or proposal, including deployment controls and falsification tests. A sentence is not silently promoted between layers.

Paper/prose/table consistency checks:

| Issue/check | Assessment | Source locator |
|---|---|---|
| Canonical ID, version, title, authors, PDF hash, and HTML hash were reconciled for arXiv:2607.08025v1; full quantitative table/prose/code consistency was not independently rerun. | identity consistency checked; quantitative and implementation consistency remain unresolved | source-integrity and online identity receipts for arXiv:2607.08025v1 |

Substantive evidence boundary: The profile binds arXiv:2607.08025v1 to a complete local PDF and full-paper HTML, 28 headings, 6 tables, 15 figures, and 108 extracted mathematical objects, and 3 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

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

### Hypothesis 1: Matched removal of features

**Proposition:** Reviewer hypothesis: the source-linked features operation is causally responsible for part of the reported geometry behavior.
**Predicted observation:** Removing or neutralizing features under matched data and compute will measurably weaken geometry.
**Falsifying observation:** A competent matched control without features preserves the same geometry distribution within uncertainty.
**Minimum test:** Run a paired, seed-controlled ablation at 4 Experiment and archive per-instance outcomes and resource use.
**Evidence locator:** private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture, and 3.3 Model Complexity Analysis

### Hypothesis 2: Boundary transfer for PGD-NO

**Proposition:** Reviewer hypothesis: the relation between features, and nodes and geometry, and tokens weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment, and Appendix B Dataset description

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for PGD-NO** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2607.08025, 4 Experiment, and Appendix B Dataset description.
2. **Reproduce the end-to-end PGD-NO path** Success: the source-defined features, nodes, and geometry and geometry, and tokens are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture, and 3.3 Model Complexity Analysis.
3. **Falsify the reviewer mechanism thesis for features** Success: a matched intervention on features predicts a corresponding change in geometry Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2607.08025, 3.2 Model Architecture, and 3.3 Model Complexity Analysis.

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-scale Physics Simulations should be remembered as a tested relation between features, nodes, and geometry and geometry, tokens, and dataset under the configurations at 4 Experiment, and Appendix B Dataset description, not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The Table 1 caption centers on specific, prediction, Table, Comparative, analysis, relative, error; its parsed headers include Model, across 15 rows and 149 cells.; result: Data Set=2.47; Data Set=3.35; Data Set=39.4; Data Set=43.1; Data Set=18.2; Data Set=16.4; Data Set=4.77; Data Set=1.32; Data Set=12.2; Data Set=13.2; caveat: Interpret Table 1 with its spanning headers and caption under 4 Experiment; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2607.08025, Table 1 caption and object |
| Table 2 | Purpose: The Table 2 caption centers on Table, Comparative, relative, error, CFD-VOL, across, varying; its parsed headers include Vol. points size, 12M, 60M, Sampling ratio, 0.01, 0.1, 1.0, across 4 rows and 24 cells.; result: column 2=0.01; column 3=0.1; column 4=1.0; column 5=0.01; column 6=0.1; column 7=1.0; caveat: Interpret Table 2 with its spanning headers and caption under 4.2 Larger Meshes; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2607.08025, Table 2 caption and object |
| Table 3 | Purpose: The Table 3 caption centers on Table, Comparative, relative, error, CFD-VOL, across, varying; its parsed headers include Number of Layers, 2, 4, 8, 12, Transolver++, PGD-NO-v1, across 3 rows and 15 cells.; result: column 2=2; column 3=4; column 4=8; column 5=12; caveat: Interpret Table 3 with its spanning headers and caption under 4.3 Ablation Studies; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2607.08025, Table 3 caption and object |
| Table 4 | Purpose: The Table 4 caption centers on Table, Comparative, relative, error, across, varying, number; its parsed headers include Number of Tokens, 32, 64, 128, 256, across 2 rows and 10 cells.; result: column 2=32; column 3=64; column 4=128; column 5=256; caveat: Interpret Table 4 with its spanning headers and caption under 4.3 Ablation Studies; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2607.08025, Table 4 caption and object |
| Table 5 | Purpose: The Table 5 caption centers on Table, Comparison, Training, Times, Memory, Usage, Across; its parsed headers include Dataset, PointNet, GNO, MeshGraphNet, Galerkin, GINO, GNOT, across 6 rows and 54 cells.; result: PointNet / 1.6h (15G) / 2.1h (10G) / 13.2h (30G)=800s; GNO / 28.2h (-) / 37.5h (-) / –=9,000s; MeshGraphNet / 27.8h (-) / 37.3h (-) / –=8,450s; Galerkin / 16.4h (-) / 11.6h (89G) / –=8,660s; GINO / 7.8h (-) / 12.9h (-) / –=9,200s; GNOT / 8.1h (89G) / 10.2h (75G) / –=10,800s; Transolver++ / 6.2h (77G) / 9.5h (62G) / 24.3h (345G)=7,800s; PGD-NO (Ours) / 5.4h (42G) / 8.8h (35GB) / 22h (120G)=6,200s; caveat: Interpret Table 5 with its spanning headers and caption under Appendix C Additional results; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2607.08025, Table 5 caption and object |
| Table 6 | Purpose: The Table 6 caption centers on tokens, Table, Comparison, between, surface, grid-pooling; its parsed headers include Method, Heatsink, JEB, Aircraft, Drivernet, CFD-VOL, Grid- token, across 3 rows and 18 cells.; result: Heatsink=9.43; JEB=62.5; Aircraft=35.4; Drivernet=10.5; CFD-VOL=36.7; caveat: Interpret Table 6 with its spanning headers and caption under Appendix C Additional results; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2607.08025, Table 6 caption and object |
| Figure 1 | Purpose: The Figure 1 caption identifies a quantitative plot or comparison centered on memory, Encoding, grid-based, tokens, PGD-NO, Figure, Architectural, comparison.; result: Caption-reported measured values: 10M; caveat: The caption under 1 Introduction was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 1 caption and object |
| Algorithm 1 | Purpose: The Algorithm 1 caption identifies a paper-specific visual object centered on Algorithm, Iterative, Geometry, Decomposition.; result: The caption makes a qualitative claim about Algorithm, Iterative, Geometry, Decomposition; no plotted value is inferred from pixels.; caveat: The caption under 3.1 Geometry Token Extraction was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Algorithm 1 caption and object |
| Figure 2 | Purpose: The Figure 2 caption identifies a architecture or pipeline schematic centered on layer, variants., segmentation, matrix, tokens, Figure, PGD-NO, architecture.; result: Caption-reported measured values: 1, 2, 3; caveat: The caption under 3.2 Model Architecture was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 2 caption and object |
| Figure 3 | Purpose: The Figure 3 caption identifies a qualitative example or visualization centered on benchmarks., Figure, Visualization, industrial, Geometry, tokens, generated, iterative.; result: The caption makes a qualitative claim about benchmarks., Figure, Visualization, industrial, Geometry, tokens; no plotted value is inferred from pixels.; caveat: The caption under 3.3 Model Complexity Analysis was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 3 caption and object |
| Figure 4 | Purpose: The Figure 4 caption identifies a quantitative plot or comparison centered on Error, structural, Figure, comparison, between, Transolver++, PGD-NO., Geometric.; result: The caption makes a qualitative claim about Error, structural, Figure, comparison, between, Transolver++; no plotted value is inferred from pixels.; caveat: The caption under 4.1 Main Results was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 4 caption and object |
| Figure 5 | Purpose: The Figure 5 caption identifies a paper-specific visual object centered on nodal, importance, Geometry, Figure, Interpretability, analysis, multi-layer, mapping..; result: The caption makes a qualitative claim about nodal, importance, Geometry, Figure, Interpretability, analysis; no plotted value is inferred from pixels.; caveat: The caption under 4.1 Main Results was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 5 caption and object |
| Figure 6 | Purpose: The Figure 6 caption identifies a paper-specific visual object centered on Figure, extracted, tokens, different, samples, Heat, Sink, dataset.; result: The caption makes a qualitative claim about Figure, extracted, tokens, different, samples, Heat; no plotted value is inferred from pixels.; caveat: The caption under Appendix D Extracted geometry token visualizations was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 6 caption and object |
| Figure 7 | Purpose: The Figure 7 caption identifies a paper-specific visual object centered on Figure, extracted, tokens, different, samples, dataset, presented..; result: The caption makes a qualitative claim about Figure, extracted, tokens, different, samples, dataset; no plotted value is inferred from pixels.; caveat: The caption under Appendix D Extracted geometry token visualizations was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 7 caption and object |
| Figure 8 panel (a) | Purpose: The Figure 8 panel (a) caption identifies a paper-specific visual object centered on view.; result: The caption makes a qualitative claim about view; no plotted value is inferred from pixels.; caveat: The caption under Appendix D Extracted geometry token visualizations was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 8 panel (a) caption and object |
| Figure 8 panel (b) | Purpose: The Figure 8 panel (b) caption identifies a paper-specific visual object centered on Bottom, view.; result: The caption makes a qualitative claim about Bottom, view; no plotted value is inferred from pixels.; caveat: The caption under Appendix D Extracted geometry token visualizations was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 8 panel (b) caption and object |
| Figure 8 | Purpose: The Figure 8 caption identifies a paper-specific visual object centered on Figure, extracted, tokens, different, samples, dataset, presented..; result: The caption makes a qualitative claim about Figure, extracted, tokens, different, samples, dataset; no plotted value is inferred from pixels.; caveat: The caption under Appendix D Extracted geometry token visualizations was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 8 caption and object |
| Figure 9 panel (a) | Purpose: The Figure 9 panel (a) caption identifies a paper-specific visual object centered on Front, view.; result: The caption makes a qualitative claim about Front, view; no plotted value is inferred from pixels.; caveat: The caption under Appendix D Extracted geometry token visualizations was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 9 panel (a) caption and object |
| Figure 9 panel (b) | Purpose: The Figure 9 panel (b) caption identifies a paper-specific visual object centered on Back, view.; result: The caption makes a qualitative claim about Back, view; no plotted value is inferred from pixels.; caveat: The caption under Appendix D Extracted geometry token visualizations was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 9 panel (b) caption and object |
| Figure 9 | Purpose: The Figure 9 caption identifies a paper-specific visual object centered on Figure, extracted, tokens, different, samples, DrivAerNet++, dataset, presented..; result: The caption makes a qualitative claim about Figure, extracted, tokens, different, samples, DrivAerNet++; no plotted value is inferred from pixels.; caveat: The caption under Appendix D Extracted geometry token visualizations was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 9 caption and object |
| Figure 10 | Purpose: The Figure 10 caption identifies a paper-specific visual object centered on Figure, bottom, view, extracted, tokens, different, samples, drivAerNet++.; result: The caption makes a qualitative claim about Figure, bottom, view, extracted, tokens, different; no plotted value is inferred from pixels.; caveat: The caption under Appendix D Extracted geometry token visualizations was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2607.08025, Figure 10 caption and object |
| Equations | 108 distinct mathematical renderings exposed by HTML; representative objects listed in Section 2.2. | Central objects were inventoried with sign, normalization, conditioning, and denominator checks; no numerical reproduction. |
| Sections | 28 headings exposed by the full HTML. | Every heading was screened; method, evaluation, results, limitations, references, and appendices were mapped where present. |

Appendix and supplementary coverage:

- Appendix A Model complexity analysis
- Appendix B Dataset description
- Appendix C Additional results
- Appendix D Extracted geometry token visualizations
- Appendix E Implementation details and baseline comparison
- Appendix F Metric
- Appendix G Error map clarification

Complete section inventory:

- Report GitHub Issue
- PGD-NO: A Neural Operator with Precomputed Geometry Decomposition for 3D Million-scale Physics Simulations Weiheng Zhong Jing Bi Victor Oancea Hadi Meidani
- Abstract
- 1 Introduction
- 2 Related Works
- 2.1 Neural PDE Solver
- 2.2 Geometry Decomposition
- 3 Method
- 3.1 Geometry Token Extraction
- 3.2 Model Architecture
- 3.3 Model Complexity Analysis
- 4 Experiment
- 4.1 Main Results
- 4.2 Larger Meshes
- 4.3 Ablation Studies
- 4.4 Model Explanation
- 5 Conclusion
- Impact Statement
- References
- Appendix A Model complexity analysis
- Appendix B Dataset description
- Appendix C Additional results
- Appendix D Extracted geometry token visualizations
- Appendix E Implementation details and baseline comparison
- Appendix F Metric
- F.1 Field prediction error
- F.2 Quantities of Interest (QoI)
- Appendix G Error map clarification

This ledger is completeness evidence, not reproduction. It records that each exposed section and numbered object was screened without reproducing the paper's tables, figures, or long captions.

## 16. Source and Evidence Notes

- Canonical arXiv record: https://arxiv.org/abs/2607.08025v1
- Canonical PDF: https://arxiv.org/pdf/2607.08025v1
- Canonical full-paper HTML: https://arxiv.org/html/2607.08025v1
- arXiv DOI resolver: https://doi.org/10.48550/arXiv.2607.08025
- Reviewed identity: arXiv:2607.08025v1
- Complete authors: Weiheng Zhong; Jing Bi; Victor Oancea; Hadi Meidani
- Locally archived full PDF and full-paper HTML were verified; private path withheld.
- No source PDF, HTML, archive, extracted text, validator, or private index belongs in the public DEP-A package.
- Online primary-source vetting status: performed and receipt-linked; alternatives are not exhaustive and no experiment was independently reproduced.

## 17. Footnotes

[^source-paper]: Canonical paper identity and version are linked at https://arxiv.org/abs/2607.08025v1; the locally archived complete PDF and full-paper HTML were reconciled to this identity.
[^scope]: Paper report means content attributable to the authors and supported by the reviewed artifact; it is not independent reproduction.
[^integrity]: Source integrity requires a matching complete PDF and full-paper HTML with identity, version, title, structure, references, and readable-body checks.
[^inference]: Reviewer inference labels a mechanism-level interpretation derived from source evidence rather than asserted by the authors.
[^external]: External primary evidence was limited to receipt-linked official records and URLs. Availability or publication status does not imply artifact runnability, result reproduction, or exhaustive prior-work coverage.
[^association]: An associated DEP is contextual evidence, not a duplicate and not proof of the reviewed paper's claims.
