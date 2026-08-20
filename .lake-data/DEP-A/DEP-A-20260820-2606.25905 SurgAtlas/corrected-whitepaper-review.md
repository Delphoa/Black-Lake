# Whitepaper Review: SurgAtlas: A Large-Scale Surgical Video-Language Dataset with 2,391 Hours of Open and Minimally Invasive Surgery

## A detailed review, technical reconstruction, and independent re-conceptualization of “SurgAtlas: A Large-Scale Surgical Video-Language Dataset with 2,391 Hours of Open and Minimally Invasive Surgery”

**Source paper:** Filippos Bellos; Andre S. Gala-Garza; Miaowei Wang; Alyssa M. Hardin; Ahmad M. Hider; Yayuan Li; Jing Bi; Susan Liang; Chenliang Xu; Donald S. Likosky; Jason J. Corso, “SurgAtlas: A Large-Scale Surgical Video-Language Dataset with 2,391 Hours of Open and Minimally Invasive Surgery,” arXiv:2606.25905v1.[^source-paper]

**Artifact prepared:** 2026-08-20
**Local source reviewed:** complete locally archived PDF (16 pages) and matching full-paper HTML (69530 readable body characters); private path withheld
**Review scope:** full-paper reconstruction, claim vetting, local evidence mapping, implications, and replication agenda
**Review status:** source artifacts inspected; bounded online primary-source vetting performed; experiments not independently rerun

## Executive Assessment

### The paper in one sentence

The paper presents and evaluates a technical contribution framed around surgatlas, large-scale, surgical, video-language, dataset, hours, with its method, formal objects, experimental record, limitations, and source structure inspected from a complete local paper pair rather than an abstract page.

### The deeper idea

Reviewer inference: the durable mechanism is the source-defined change centered on datasets, surgical, videos, and hierarchical, rather than the paper's brand name. This interpretation predicts that a matched intervention on datasets changes mathcal; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to Surgical vision–language datasets and models.. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

### Bottom-line judgment

The source is complete enough for a full-paper assessment, and the paper reports a technically organized contribution with an explicit evaluation record. Results remain paper-reported. The local evidence pass confirms the complete results structure and numbered-object inventory, but it does not independently reproduce a numerical value or infer a stronger denominator than the source states. The defensible verdict is therefore conditional: the paper establishes what it directly measures under its own setup, while broader superiority, generality, robustness, efficiency, or deployment readiness remains bounded by the tested models, data, metrics, budgets, hardware, and comparisons.[^scope]

### Principal strengths

- Complete PDF and matching full-paper HTML passed identity, structure, title, references, and readability gates.
- The source exposes 42 section headings, 6 table captions, 8 figure captions, and 269 mathematical renderings for coverage auditing.
- The review can distinguish paper report, external-primary evidence, reviewer inference, and hypothesis without relying on an abstract-only summary.

### Principal qualifications

1. The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions.
2. No result, code path, benchmark, training run, or hardware measurement was independently reproduced.
3. Bounded online checks verified canonical identity and the explicitly recorded official URLs; the search is not exhaustive and does not establish artifact runnability or reproduction.[^external]

## 1. The Problem and Research Questions

### 1.1 Problem and stakes

**Paper-reported problem:** For SurgAtlas: A Large-Scale Surgical Video-Language Dataset with 2,391 Hours of Open and Minimally Invasive Surgery, the formal target is bounded to the source-defined relation among surgical, videos, video, language, SurgAtlas, public, and open. The task assumptions and stakes are anchored to Abstract, and 1 Introduction; no objective outside those sections is inferred.

**Research gap reconstructed from the source:** The paper positions SurgAtlas around surgical, videos, video, and datasets. This records the authors' gap framing only; novelty, priority, generality, and superiority require the separate prior-work and evaluation audits.

The title and full-paper organization identify surgatlas, large-scale, surgical, video-language, dataset, hours as the central problem space. A rigorous reading asks what input object is transformed, predicted, selected, optimized, or measured; which practical or scientific constraint motivates that operation; and which outcome makes the change valuable. Those questions must be answered by the method and evaluation sections, not by the title alone. The paper reports its own problem definition; this review preserves the boundary between that report and reviewer interpretation.

Paper-specific reconstruction: the abstract/introduction evidence concentrates on surgical, videos, video, language, surgatlas, datasets, public, over, first, question, under the headings Abstract, 1 Introduction. Those source terms locate the actual objects and constraints; they do not by themselves prove novelty or improvement. In this review they constrain the problem statement so a generic systems narrative cannot replace the paper's own domain and terminology.

The practical stakes depend on the actual denominator. An improvement in a representation, proxy, component score, or controlled benchmark can be important without automatically improving end-user quality, wall-clock cost, reliability, or safety. A durable account therefore separates the immediate technical objective from the downstream objective and asks which bridge between them is tested. If that bridge is only assumed, it remains an explicit gap rather than a hidden premise.

### 1.2 Prior method families and inherited components

The paper's related-work and background sections define the relevant method families. The review treats established backbones, pretrained models, datasets, optimization routines, kernels, evaluation harnesses, and standard metrics as inherited unless the source identifies a change. Novelty belongs to the specific interface, objective, representation, decision rule, data construction, proof, or evaluation design that differs. This prevents a system-level bundle from receiving credit for every capability of its dependencies.

### 1.3 Questions that govern the assessment

Five questions organize the reconstruction. What exact object enters and leaves the method? Which components are learned, fixed, searched, sampled, or verified? What objective and assumptions determine the operation? How do training or calibration differ from inference or deployment? Finally, which result would falsify the authors' causal or generality story rather than merely lower an aggregate score? These questions create an audit trail from paper report to independent assessment.

## 2. Formal and Technical Reconstruction

### 2.1 Definitions and assumptions

The authoritative definition chain lives in the complete source sections listed below. The automated evidence profile does not pretend that section names themselves describe the mechanism. Instead, the full review binds each claim to the source's definitions, stated assumptions, and adjacent formal or experimental context. The core technical headings identified for close reading were:

- Surgical vision–language datasets and models.

Variables should be assigned plain-language meanings before algebra is interpreted. Inputs, labels, state, parameters, budgets, constraints, random variables, and outputs must remain distinct. A probability requires a sample space and conditioning event; a loss requires an optimization direction; a ratio requires a numerator and denominator; and a guarantee retains every assumption under which it was proved. If the source uses the same symbol in different roles or shifts between population and sample quantities, that ambiguity should be preserved rather than silently repaired.

### 2.2 Objective and central equations

The full HTML exposes 269 distinct mathematical renderings. Each is treated as a paper-reported formal object whose sign, normalization, conditioning, and denominator must be read with adjacent prose.

Paper-specific formal reconstruction:

**Formal object 1 at Abstract — Formula 1 under Abstract is classified as a state or representation transformation; adjacent prose centers on surgical, SurgAtlas, video, language, open, question, and the expression links symbols defined beside the formula..** `5{,}000`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 1 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Abstract.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Abstract, formal object 1.

**Formal object 2 at 1 Introduction — Formula 2 under 1 Introduction is classified as a constraint or formal-analysis relation; adjacent prose centers on public, datasets, supervision, what, operative, surgical, and the expression links Sigma..** `\Sigma`
Variables: "Sigma".
Sign/normalization/conditioning/surrogate audit: "Formula 2 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Sigma; meanings remain tied to 1 Introduction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 1 Introduction, formal object 2.

**Formal object 3 at 2 Related Work — Formula 3 under 2 Related Work is classified as a state or representation transformation; adjacent prose centers on videos, surgical, video, annotations, Tier, SurgAtlas, and the expression links symbols defined beside the formula..** `15{,}291`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 3 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 2 Related Work.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 2 Related Work, formal object 3.

**Formal object 4 at 2 Related Work — Formula 4 under 2 Related Work is classified as a state or representation transformation; adjacent prose centers on videos, surgical, video, annotations, Tier, SurgAtlas, and the expression links symbols defined beside the formula..** `2{,}391`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 4 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 2 Related Work.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 2 Related Work, formal object 4.

**Formal object 5 at 3.2 Dataset Construction Pipeline — Formula 5 under 3.2 Dataset Construction Pipeline is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, video, associated, sequence, signals, and the expression links mathcal, D, v_{i}, A, i, N..** `\mathcal{D}=\{(v_{i},\mathcal{A}_{i})\}_{i=1}^{N}`
Variables: "mathcal, D, v_{i}, A, i, N".
Sign/normalization/conditioning/surrogate audit: "Formula 5 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D, v_{i}, A, i, N; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 5.

**Formal object 6 at 3.2 Dataset Construction Pipeline — Formula 6 under 3.2 Dataset Construction Pipeline is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, video, associated, sequence, signals, and the expression links v_{i}..** `v_{i}`
Variables: "v_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 6 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: v_{i}; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 6.

**Formal object 7 at 3.2 Dataset Construction Pipeline — Formula 7 under 3.2 Dataset Construction Pipeline is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, video, associated, sequence, signals, and the expression links i..** `i`
Variables: "i".
Sign/normalization/conditioning/surrogate audit: "Formula 7 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: i; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 7.

**Formal object 8 at 3.2 Dataset Construction Pipeline — Formula 8 under 3.2 Dataset Construction Pipeline is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, video, associated, sequence, signals, and the expression links mathcal, A, i..** `\mathcal{A}_{i}`
Variables: "mathcal, A, i".
Sign/normalization/conditioning/surrogate audit: "Formula 8 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A, i; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 8.

**Formal object 9 at 3.2 Dataset Construction Pipeline — Formula 9 under 3.2 Dataset Construction Pipeline is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, video, associated, sequence, signals, and the expression links v_{i}, f_{i}^{1}, ldots, f_{i}^{T, i..** `v_{i}=(f_{i}^{1},\ldots,f_{i}^{T_{i}})`
Variables: "v_{i}, f_{i}^{1}, ldots, f_{i}^{T, i".
Sign/normalization/conditioning/surrogate audit: "Formula 9 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: v_{i}, f_{i}^{1}, ldots, f_{i}^{T, i; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 9.

**Formal object 10 at 3.2 Dataset Construction Pipeline — Formula 10 under 3.2 Dataset Construction Pipeline is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, video, associated, sequence, signals, and the expression links tau, v_{i}..** `\tau(v_{i})`
Variables: "tau, v_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 10 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tau, v_{i}; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 10.

**Formal object 11 at 3.2 Dataset Construction Pipeline — Formula 11 under 3.2 Dataset Construction Pipeline is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, video, associated, sequence, signals, and the expression links a_{i}..** `a_{i}`
Variables: "a_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 11 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: a_{i}; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 11.

**Formal object 12 at 3.2 Dataset Construction Pipeline — Formula 12 under 3.2 Dataset Construction Pipeline is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, video, associated, sequence, signals, and the expression links mathcal, O, i..** `\mathcal{O}_{i}`
Variables: "mathcal, O, i".
Sign/normalization/conditioning/surrogate audit: "Formula 12 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, O, i; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 12.

**Formal object 13 at 3.2 Dataset Construction Pipeline — Formula 13 under 3.2 Dataset Construction Pipeline is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, video, associated, sequence, signals, and the expression links m_{i}, i..** `m_{i}=(\text{title}_{i},\text{description}_{i},\text{channel}_{i})`
Variables: "m_{i}, i".
Sign/normalization/conditioning/surrogate audit: "Formula 13 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: m_{i}, i; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 13.

**Formal object 14 at 3.2 Dataset Construction Pipeline — Formula 14 under 3.2 Dataset Construction Pipeline is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, video, procedure, and the expression links symbols defined beside the formula..** `18{,}855`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 14 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 14.

**Formal object 15 at 3.2 Dataset Construction Pipeline — Formula 15 under 3.2 Dataset Construction Pipeline is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, video, procedure, and the expression links symbols defined beside the formula..** `9{,}109`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 15 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 15.

**Formal object 16 at 3.2 Dataset Construction Pipeline — Formula 16 under 3.2 Dataset Construction Pipeline is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, video, procedure, and the expression links symbols defined beside the formula..** `6{,}182`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 16 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 16.

**Formal object 17 at 3.2 Dataset Construction Pipeline — Formula 17 under 3.2 Dataset Construction Pipeline is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, video, procedure, and the expression links mathcal, A..** `\mathcal{A}^{\text{exp}}`
Variables: "mathcal, A".
Sign/normalization/conditioning/surrogate audit: "Formula 17 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A; meanings remain tied to 3.2 Dataset Construction Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2 Dataset Construction Pipeline, formal object 17.

**Formal object 18 at 3.2.1 Stage 1: Collection and Filtering — Formula 18 under 3.2.1 Stage 1: Collection and Filtering is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, procedure, sigma, and the expression links mathcal, P, p_{1}, ldots, p_{..** `\mathcal{P}=\{p_{1},\ldots,p_{|\mathcal{P}|}\}`
Variables: "mathcal, P, p_{1}, ldots, p_{".
Sign/normalization/conditioning/surrogate audit: "Formula 18 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, P, p_{1}, ldots, p_{; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 18.

**Formal object 19 at 3.2.1 Stage 1: Collection and Filtering — Formula 19 under 3.2.1 Stage 1: Collection and Filtering is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, procedure, sigma, and the expression links symbols defined beside the formula..** `18`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 19 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 19.

**Formal object 20 at 3.2.1 Stage 1: Collection and Filtering — Formula 20 under 3.2.1 Stage 1: Collection and Filtering is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, procedure, sigma, and the expression links p, in, mathcal, P..** `p\in\mathcal{P}`
Variables: "p, in, mathcal, P".
Sign/normalization/conditioning/surrogate audit: "Formula 20 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p, in, mathcal, P; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 20.

**Formal object 21 at 3.2.1 Stage 1: Collection and Filtering — Formula 21 under 3.2.1 Stage 1: Collection and Filtering is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, procedure, sigma, and the expression links mathcal, P..** `\mathcal{P}`
Variables: "mathcal, P".
Sign/normalization/conditioning/surrogate audit: "Formula 21 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, P; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 21.

**Formal object 22 at 3.2.1 Stage 1: Collection and Filtering — Formula 22 under 3.2.1 Stage 1: Collection and Filtering is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, procedure, sigma, and the expression links sigma, j, p, mathcal, T, cap, cup..** `\sigma(\text{title}_{j},p)=|\mathcal{T}(\text{title}_{j})\cap\mathcal{T}(p)|/|\mathcal{T}(\text{title}_{j})\cup\mathcal{T}(p)|`
Variables: "sigma, j, p, mathcal, T, cap, cup".
Sign/normalization/conditioning/surrogate audit: "Formula 22 operator audit: nonlinear normalization, fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sigma, j, p, mathcal, T, cap, cup; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 22.

**Formal object 23 at 3.2.1 Stage 1: Collection and Filtering — Formula 23 under 3.2.1 Stage 1: Collection and Filtering is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, procedure, sigma, and the expression links mathcal, T..** `\mathcal{T}(\cdot)`
Variables: "mathcal, T".
Sign/normalization/conditioning/surrogate audit: "Formula 23 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, T; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 23.

**Formal object 24 at 3.2.1 Stage 1: Collection and Filtering — Formula 24 under 3.2.1 Stage 1: Collection and Filtering is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, title, text, surgical, procedure, sigma, and the expression links p, in, mathcal, P, sigma, j, geq, theta..** `\max_{p\in\mathcal{P}}\sigma(\text{title}_{j},p)\geq\theta_{\sigma}`
Variables: "p, in, mathcal, P, sigma, j, geq, theta".
Sign/normalization/conditioning/surrogate audit: "Formula 24 operator audit: nonlinear normalization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p, in, mathcal, P, sigma, j, geq, theta; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 24.

**Formal object 25 at 3.2.1 Stage 1: Collection and Filtering — Formula 25 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links mathcal, C, v_{j}\}, j, N_{\text{init}}}..** `\mathcal{C}_{\text{init}}=\{v_{j}\}_{j=1}^{N_{\text{init}}}`
Variables: "mathcal, C, v_{j}\\}, j, N_{\\text{init}}}".
Sign/normalization/conditioning/surrogate audit: "Formula 25 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, v_{j}\\}, j, N_{\\text{init}}}; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 25.

**Formal object 26 at 3.2.1 Stage 1: Collection and Filtering — Formula 26 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links N_{\text{init}}..** `N_{\text{init}}=18{,}855`
Variables: "N_{\\text{init}}".
Sign/normalization/conditioning/surrogate audit: "Formula 26 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N_{\\text{init}}; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 26.

**Formal object 27 at 3.2.1 Stage 1: Collection and Filtering — Formula 27 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links Phi, circ..** `\Phi=\Phi_{\text{man}}\circ\Phi_{\text{LLM}}\circ\Phi_{\text{age}}`
Variables: "Phi, circ".
Sign/normalization/conditioning/surrogate audit: "Formula 27 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Phi, circ; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 27.

**Formal object 28 at 3.2.1 Stage 1: Collection and Filtering — Formula 28 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links Phi..** `\Phi_{\text{age}}`
Variables: "Phi".
Sign/normalization/conditioning/surrogate audit: "Formula 28 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Phi; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 28.

**Formal object 29 at 3.2.1 Stage 1: Collection and Filtering — Formula 29 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links Phi..** `\Phi_{\text{LLM}}`
Variables: "Phi".
Sign/normalization/conditioning/surrogate audit: "Formula 29 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Phi; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 29.

**Formal object 30 at 3.2.1 Stage 1: Collection and Filtering — Formula 30 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links phi, m_{j}\mapsto\{0..** `\phi_{\text{meta}}:m_{j}\mapsto\{0,1\}`
Variables: "phi, m_{j}\\mapsto\\{0".
Sign/normalization/conditioning/surrogate audit: "Formula 30 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: phi, m_{j}\\mapsto\\{0; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 30.

**Formal object 31 at 3.2.1 Stage 1: Collection and Filtering — Formula 31 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links j..** `(\text{title}_{j},\text{description}_{j})`
Variables: "j".
Sign/normalization/conditioning/surrogate audit: "Formula 31 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: j; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 31.

**Formal object 32 at 3.2.1 Stage 1: Collection and Filtering — Formula 32 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links Phi..** `\Phi_{\text{man}}`
Variables: "Phi".
Sign/normalization/conditioning/surrogate audit: "Formula 32 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Phi; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 32.

**Formal object 33 at 3.2.1 Stage 1: Collection and Filtering — Formula 33 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links mathcal, B, j, s_{j}^{, k, e_{j}^{..** `\mathcal{B}_{j}=\{(s_{j}^{(k)},e_{j}^{(k)})\}_{k}`
Variables: "mathcal, B, j, s_{j}^{, k, e_{j}^{".
Sign/normalization/conditioning/surrogate audit: "Formula 33 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, B, j, s_{j}^{, k, e_{j}^{; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 33.

**Formal object 34 at 3.2.1 Stage 1: Collection and Filtering — Formula 34 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links mathcal, C, Phi..** `\mathcal{C}=\Phi(\mathcal{C}_{\text{init}})`
Variables: "mathcal, C, Phi".
Sign/normalization/conditioning/surrogate audit: "Formula 34 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, Phi; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 34.

**Formal object 35 at 3.2.1 Stage 1: Collection and Filtering — Formula 35 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links mathcal, C, N..** `|\mathcal{C}|=N=15{,}291`
Variables: "mathcal, C, N".
Sign/normalization/conditioning/surrogate audit: "Formula 35 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, N; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 35.

**Formal object 36 at 3.2.1 Stage 1: Collection and Filtering — Formula 36 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links N_{\text{open}}..** `N_{\text{open}}=6{,}182`
Variables: "N_{\\text{open}}".
Sign/normalization/conditioning/surrogate audit: "Formula 36 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N_{\\text{open}}; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 36.

**Formal object 37 at 3.2.1 Stage 1: Collection and Filtering — Formula 37 under 3.2.1 Stage 1: Collection and Filtering is classified as a constraint or formal-analysis relation; adjacent prose centers on text, init, mathcal, content, operative, intraoperative, and the expression links N_{\text{MIS}}..** `N_{\text{MIS}}=9{,}109`
Variables: "N_{\\text{MIS}}".
Sign/normalization/conditioning/surrogate audit: "Formula 37 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N_{\\text{MIS}}; meanings remain tied to 3.2.1 Stage 1: Collection and Filtering.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering, formal object 37.

**Formal object 38 at 3.2.2 Stage 2: Tier Assignment — Formula 38 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links v_{i}\in\mathcal{C}..** `v_{i}\in\mathcal{C}`
Variables: "v_{i}\\in\\mathcal{C}".
Sign/normalization/conditioning/surrogate audit: "Formula 38 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: v_{i}\\in\\mathcal{C}; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 38.

**Formal object 39 at 3.2.2 Stage 2: Tier Assignment — Formula 39 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links mathbb, mathrm, v_{i}..** `\mathbb{1}_{\mathrm{narr}}(v_{i})`
Variables: "mathbb, mathrm, v_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 39 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbb, mathrm, v_{i}; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 39.

**Formal object 40 at 3.2.2 Stage 2: Tier Assignment — Formula 40 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links mathbb, mathrm, v_{i}..** `\mathbb{1}_{\mathrm{ocr}}(v_{i})`
Variables: "mathbb, mathrm, v_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 40 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbb, mathrm, v_{i}; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 40.

**Formal object 41 at 3.2.2 Stage 2: Tier Assignment — Formula 41 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links rho, mathcal, C, to..** `\rho:\mathcal{C}\to 2^{\{1,2,3\}}`
Variables: "rho, mathcal, C, to".
Sign/normalization/conditioning/surrogate audit: "Formula 41 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: rho, mathcal, C, to; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 41.

**Formal object 42 at 3.2.2 Stage 2: Tier Assignment — Formula 42 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links mathbb, mathrm, v_{i}..** `\mathbb{1}_{\mathrm{narr}}(v_{i})=1`
Variables: "mathbb, mathrm, v_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 42 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbb, mathrm, v_{i}; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 42.

**Formal object 43 at 3.2.2 Stage 2: Tier Assignment — Formula 43 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links mathbb, mathrm, v_{i}..** `\mathbb{1}_{\mathrm{ocr}}(v_{i})=1`
Variables: "mathbb, mathrm, v_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 43 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbb, mathrm, v_{i}; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 43.

**Formal object 44 at 3.2.2 Stage 2: Tier Assignment — Formula 44 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links mathcal, C, setminus, cup..** `\mathcal{C}\setminus(\mathcal{C}_{1}\cup\mathcal{C}_{2})`
Variables: "mathcal, C, setminus, cup".
Sign/normalization/conditioning/surrogate audit: "Formula 44 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, setminus, cup; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 44.

**Formal object 45 at 3.2.2 Stage 2: Tier Assignment — Formula 45 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links mathcal, C, approx..** `|\mathcal{C}_{1}|\approx 9{,}360`
Variables: "mathcal, C, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 45 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, approx; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 45.

**Formal object 46 at 3.2.2 Stage 2: Tier Assignment — Formula 46 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links mathcal, C, approx..** `|\mathcal{C}_{2}|\approx 4{,}460`
Variables: "mathcal, C, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 46 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, approx; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 46.

**Formal object 47 at 3.2.2 Stage 2: Tier Assignment — Formula 47 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links mathcal, C, approx..** `|\mathcal{C}_{3}|\approx 2{,}778`
Variables: "mathcal, C, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 47 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, approx; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 47.

**Formal object 48 at 3.2.2 Stage 2: Tier Assignment — Formula 48 under 3.2.2 Stage 2: Tier Assignment is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, Tier, narr, mathbb, mathrm, approx, and the expression links mathcal, C, cap, approx..** `|\mathcal{C}_{1}\cap\mathcal{C}_{2}|\approx 1{,}307`
Variables: "mathcal, C, cap, approx".
Sign/normalization/conditioning/surrogate audit: "Formula 48 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, cap, approx; meanings remain tied to 3.2.2 Stage 2: Tier Assignment.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.2 Stage 2: Tier Assignment, formal object 48.

**Formal object 49 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 49 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, step, every, produce, annotation, and the expression links mathcal, A, i..** `\mathcal{A}_{i}=\{\mathcal{A}_{i}^{\text{seg}},\mathcal{A}_{i}^{\text{step}},\mathcal{A}_{i}^{\text{vid}},\mathcal{A}_{i}^{\text{qa}}\}`
Variables: "mathcal, A, i".
Sign/normalization/conditioning/surrogate audit: "Formula 49 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A, i; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 49.

**Formal object 50 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 50 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on Whisper, mathcal, start, time, word, Tier, and the expression links mathcal, W, i, w_{i}^{, j, t_{i}^{, s, e..** `\mathcal{W}_{i}=\{(w_{i}^{(j)},t_{i}^{(j),s},t_{i}^{(j),e})\}_{j=1}^{J_{i}}`
Variables: "mathcal, W, i, w_{i}^{, j, t_{i}^{, s, e, J_{i}}".
Sign/normalization/conditioning/surrogate audit: "Formula 50 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, W, i, w_{i}^{, j, t_{i}^{, s, e, J_{i}}; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 50.

**Formal object 51 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 51 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on Whisper, mathcal, start, time, word, Tier, and the expression links mathcal, S, i, t_{i}^{, k, s, e, x_{i}^{..** `\mathcal{S}_{i}=\{(t_{i}^{(k),s},t_{i}^{(k),e},x_{i}^{(k)})\}_{k=1}^{K_{i}}`
Variables: "mathcal, S, i, t_{i}^{, k, s, e, x_{i}^{, K_{i}}".
Sign/normalization/conditioning/surrogate audit: "Formula 51 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, S, i, t_{i}^{, k, s, e, x_{i}^{, K_{i}}; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 51.

**Formal object 52 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 52 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on Whisper, mathcal, start, time, word, Tier, and the expression links x_{i}^{, k..** `x_{i}^{(k)}`
Variables: "x_{i}^{, k".
Sign/normalization/conditioning/surrogate audit: "Formula 52 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: x_{i}^{, k; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 52.

**Formal object 53 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 53 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, step, sentence, operator, sentences, and the expression links mathcal, R, x_{i}^{, k, mapsto, c_{i}^{..** `\mathcal{R}_{\text{LLM}}:x_{i}^{(k)}\mapsto c_{i}^{(k)}`
Variables: "mathcal, R, x_{i}^{, k, mapsto, c_{i}^{".
Sign/normalization/conditioning/surrogate audit: "Formula 53 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, R, x_{i}^{, k, mapsto, c_{i}^{; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 53.

**Formal object 54 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 54 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, step, sentence, operator, sentences, and the expression links t_{i}^{, k, s, e..** `[t_{i}^{(k),s},t_{i}^{(k),e}]`
Variables: "t_{i}^{, k, s, e".
Sign/normalization/conditioning/surrogate audit: "Formula 54 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: t_{i}^{, k, s, e; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 54.

**Formal object 55 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 55 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, step, sentence, operator, sentences, and the expression links g_{\text{rel}}, c_{i}^{, k, in..** `g_{\text{rel}}(c_{i}^{(k)})\in\{0,1\}`
Variables: "g_{\\text{rel}}, c_{i}^{, k, in".
Sign/normalization/conditioning/surrogate audit: "Formula 55 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: g_{\\text{rel}}, c_{i}^{, k, in; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 55.

**Formal object 56 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 56 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, step, sentence, operator, sentences, and the expression links mathcal, A, i, v_{i}, t_{i}^{, k, s, e..** `\mathcal{A}_{i}^{\text{seg}}=\{(v_{i}[t_{i}^{(k),s},t_{i}^{(k),e}],c_{i}^{(k)}):g_{\text{rel}}(c_{i}^{(k)})=1\}`
Variables: "mathcal, A, i, v_{i}, t_{i}^{, k, s, e, c_{i}^{, g_{\\text{rel}}".
Sign/normalization/conditioning/surrogate audit: "Formula 56 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A, i, v_{i}, t_{i}^{, k, s, e, c_{i}^{, g_{\\text{rel}}; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 56.

**Formal object 57 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 57 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, step, sentence, operator, sentences, and the expression links Psi..** `\Psi_{\text{LLM}}`
Variables: "Psi".
Sign/normalization/conditioning/surrogate audit: "Formula 57 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Psi; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 57.

**Formal object 58 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 58 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, step, sentence, operator, sentences, and the expression links t_{i}^{, k, s, e, c_{i}^{..** `\{(t_{i}^{(k),s},t_{i}^{(k),e},c_{i}^{(k)})\}_{k}`
Variables: "t_{i}^{, k, s, e, c_{i}^{".
Sign/normalization/conditioning/surrogate audit: "Formula 58 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: t_{i}^{, k, s, e, c_{i}^{; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 58.

**Formal object 59 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 59 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, step, sentence, operator, sentences, and the expression links m_{i}..** `m_{i}`
Variables: "m_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 59 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: m_{i}; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 59.

**Formal object 60 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 60 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, step, sentence, operator, sentences, and the expression links mathcal, A, i, v_{i}, t_{i}^{, alpha, s, beta..** `\mathcal{A}_{i}^{\text{step}}=\{(v_{i}[t_{i}^{(\alpha),s},t_{i}^{(\beta),e}],\mathcal{R}_{\text{LLM}}^{\text{step}}(c_{i}^{(\alpha:\beta)})):(\alpha,\beta)\in\Psi_{\text{LLM}}(\mathcal{S}_{i},m_{i})\}`
Variables: "mathcal, A, i, v_{i}, t_{i}^{, alpha, s, beta, e, R, c_{i}^{, in, Psi, S, m_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 60 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A, i, v_{i}, t_{i}^{, alpha, s, beta, e, R, c_{i}^{, in, Psi, S, m_{i}; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 60.

**Formal object 61 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 61 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, step, sentence, operator, sentences, and the expression links mathcal, R..** `\mathcal{R}_{\text{LLM}}^{\text{vid}}`
Variables: "mathcal, R".
Sign/normalization/conditioning/surrogate audit: "Formula 61 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, R; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 61.

**Formal object 62 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 62 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, step, sentence, operator, sentences, and the expression links mathcal, A, i, R, c_{i}^{, K_{i}, m_{i}..** `\mathcal{A}_{i}^{\text{vid}}=\mathcal{R}_{\text{LLM}}^{\text{vid}}(c_{i}^{(1:K_{i})},m_{i})`
Variables: "mathcal, A, i, R, c_{i}^{, K_{i}, m_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 62 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A, i, R, c_{i}^{, K_{i}, m_{i}; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 62.

**Formal object 63 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 63 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links mathcal, O, i, ell, k, t_{i}^{, s, e..** `\mathcal{O}_{i}^{\text{raw}}=\{(\ell_{i}^{(k)},t_{i}^{(k),s},t_{i}^{(k),e})\}_{k=1}^{L_{i}}`
Variables: "mathcal, O, i, ell, k, t_{i}^{, s, e, L_{i}}".
Sign/normalization/conditioning/surrogate audit: "Formula 63 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, O, i, ell, k, t_{i}^{, s, e, L_{i}}; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 63.

**Formal object 64 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 64 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links mathcal, R..** `\mathcal{R}_{\text{LLM}}^{\text{ocr}}`
Variables: "mathcal, R".
Sign/normalization/conditioning/surrogate audit: "Formula 64 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, R; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 64.

**Formal object 65 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 65 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links p_{i}..** `p_{i}`
Variables: "p_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 65 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: p_{i}; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 65.

**Formal object 66 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 66 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links Gamma..** `\Gamma`
Variables: "Gamma".
Sign/normalization/conditioning/surrogate audit: "Formula 66 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: Gamma; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 66.

**Formal object 67 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 67 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links mathcal, O, i, Gamma, big, R, p_{i}, tilde..** `\mathcal{O}_{i}=\Gamma\big(\mathcal{R}_{\text{LLM}}^{\text{ocr}}(\mathcal{O}_{i}^{\text{raw}}\mid p_{i})\big)=\{(\tilde{\ell}_{i}^{(k)},t_{i}^{(k),s},t_{i}^{(k),e})\}_{k}`
Variables: "mathcal, O, i, Gamma, big, R, p_{i}, tilde, ell, k, t_{i}^{, s, e".
Sign/normalization/conditioning/surrogate audit: "Formula 67 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, O, i, Gamma, big, R, p_{i}, tilde, ell, k, t_{i}^{, s, e; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 67.

**Formal object 68 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 68 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links mathcal, K, p, k_{1}^{p}, ldots, k_{M..** `\mathcal{K}(p)=(k_{1}^{p},\ldots,k_{M_{p}}^{p})`
Variables: "mathcal, K, p, k_{1}^{p}, ldots, k_{M".
Sign/normalization/conditioning/surrogate audit: "Formula 68 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, K, p, k_{1}^{p}, ldots, k_{M; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 68.

**Formal object 69 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 69 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links mathcal, R, p, mapsto, K..** `\mathcal{R}_{\text{LLM}}^{\text{kb}}:p\mapsto\mathcal{K}(p)`
Variables: "mathcal, R, p, mapsto, K".
Sign/normalization/conditioning/surrogate audit: "Formula 69 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, R, p, mapsto, K; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 69.

**Formal object 70 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 70 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links hat, ell, i, k, prime, in, mathcal, K..** `\hat{\ell}_{i}^{(k)}=\arg\max_{k^{\prime}\in\mathcal{K}(p_{i})}\text{sim}(\mathbf{e}(\tilde{\ell}_{i}^{(k)}),\mathbf{e}(k^{\prime}))`
Variables: "hat, ell, i, k, prime, in, mathcal, K, p_{i}, mathbf, e, tilde".
Sign/normalization/conditioning/surrogate audit: "Formula 70 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: hat, ell, i, k, prime, in, mathcal, K, p_{i}, mathbf, e, tilde; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 70.

**Formal object 71 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 71 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links geq, theta, s..** `\text{sim}\geq\theta_{s}`
Variables: "geq, theta, s".
Sign/normalization/conditioning/surrogate audit: "Formula 71 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: geq, theta, s; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 71.

**Formal object 72 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 72 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links mathbf, e..** `\mathbf{e}(\cdot)`
Variables: "mathbf, e".
Sign/normalization/conditioning/surrogate audit: "Formula 72 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, e; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 72.

**Formal object 73 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 73 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links d_{i}^{, k, mathcal, R, hat, ell, i, p_{i}..** `d_{i}^{(k)}=\mathcal{R}_{\text{LLM}}^{\text{exp}}(\hat{\ell}_{i}^{(k)}\mid p_{i})`
Variables: "d_{i}^{, k, mathcal, R, hat, ell, i, p_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 73 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: d_{i}^{, k, mathcal, R, hat, ell, i, p_{i}; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 73.

**Formal object 74 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 74 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a state or representation transformation; adjacent prose centers on text, mathcal, label, step, mathbf, procedural, and the expression links mathcal, A, i, v_{i}, t_{i}^{, k, s, e..** `\mathcal{A}_{i}^{\text{step}}=\{(v_{i}[t_{i}^{(k),s},t_{i}^{(k),e}],d_{i}^{(k)})\}_{k}`
Variables: "mathcal, A, i, v_{i}, t_{i}^{, k, s, e, d_{i}^{".
Sign/normalization/conditioning/surrogate audit: "Formula 74 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A, i, v_{i}, t_{i}^{, k, s, e, d_{i}^{; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 74.

**Formal object 75 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 75 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on text, meta, mathcal, Tier, metadata-only, videos, and the expression links mathcal, A, i, R, m_{i}..** `\mathcal{A}_{i}^{\text{vid}}=\mathcal{R}_{\text{LLM}}^{\text{meta}}(m_{i})`
Variables: "mathcal, A, i, R, m_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 75 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A, i, R, m_{i}; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 75.

**Formal object 76 at 3.2.3 Stage 3: Multigranular Annotation Extraction — Formula 76 under 3.2.3 Stage 3: Multigranular Annotation Extraction is classified as a paper-defined mathematical relation; adjacent prose centers on text, meta, mathcal, Tier, metadata-only, videos, and the expression links mathcal, R..** `\mathcal{R}_{\text{LLM}}^{\text{meta}}`
Variables: "mathcal, R".
Sign/normalization/conditioning/surrogate audit: "Formula 76 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, R; meanings remain tied to 3.2.3 Stage 3: Multigranular Annotation Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.3 Stage 3: Multigranular Annotation Extraction, formal object 76.

**Formal object 77 at 3.2.4 Stage 4: Procedure Window Extraction — Formula 77 under 3.2.4 Stage 4: Procedure Window Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, presentation-, operative, edge, flow, and the expression links mathbf, b, i, x_{i}, y_{i}, w_{i}, h_{i}..** `\mathbf{b}_{i}=(x_{i},y_{i},w_{i},h_{i})`
Variables: "mathbf, b, i, x_{i}, y_{i}, w_{i}, h_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 77 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, b, i, x_{i}, y_{i}, w_{i}, h_{i}; meanings remain tied to 3.2.4 Stage 4: Procedure Window Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.4 Stage 4: Procedure Window Extraction, formal object 77.

**Formal object 78 at 3.2.4 Stage 4: Procedure Window Extraction — Formula 78 under 3.2.4 Stage 4: Procedure Window Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, presentation-, operative, edge, flow, and the expression links f_{i}^{, tau, in, mathcal, T, s..** `\{f_{i}^{(\tau)}\}_{\tau\in\mathcal{T}_{s}}`
Variables: "f_{i}^{, tau, in, mathcal, T, s".
Sign/normalization/conditioning/surrogate audit: "Formula 78 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: f_{i}^{, tau, in, mathcal, T, s; meanings remain tied to 3.2.4 Stage 4: Procedure Window Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.4 Stage 4: Procedure Window Extraction, formal object 78.

**Formal object 79 at 3.2.4 Stage 4: Procedure Window Extraction — Formula 79 under 3.2.4 Stage 4: Procedure Window Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, presentation-, operative, edge, flow, and the expression links S_{i}, x, y, mathbb, E, tau, in, mathcal..** `S_{i}(x,y)=\mathbb{E}_{\tau\in\mathcal{T}_{s}}[\lambda_{1}\,S^{\text{sat}}_{i}(x,y;\tau)+\lambda_{2}\,S^{\text{edge}}_{i}(x,y;\tau)+\lambda_{3}\,S^{\text{flow}}_{i}(x,y;\tau)]`
Variables: "S_{i}, x, y, mathbb, E, tau, in, mathcal, T, s, lambda, S, i".
Sign/normalization/conditioning/surrogate audit: "Formula 79 operator audit: expectation; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S_{i}, x, y, mathbb, E, tau, in, mathcal, T, s, lambda, S, i; meanings remain tied to 3.2.4 Stage 4: Procedure Window Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.4 Stage 4: Procedure Window Extraction, formal object 79.

**Formal object 80 at 3.2.4 Stage 4: Procedure Window Extraction — Formula 80 under 3.2.4 Stage 4: Procedure Window Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, presentation-, operative, edge, flow, and the expression links mathbf, b, i, mathds, S_{i}\geq\tau, S, oplus, mathcal..** `\mathbf{b}_{i}=\text{bbox}(\text{LCC}(\mathds{1}[S_{i}\geq\tau_{S}]\oplus\mathcal{M}))`
Variables: "mathbf, b, i, mathds, S_{i}\\geq\\tau, S, oplus, mathcal, M".
Sign/normalization/conditioning/surrogate audit: "Formula 80 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathbf, b, i, mathds, S_{i}\\geq\\tau, S, oplus, mathcal, M; meanings remain tied to 3.2.4 Stage 4: Procedure Window Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.4 Stage 4: Procedure Window Extraction, formal object 80.

**Formal object 81 at 3.2.4 Stage 4: Procedure Window Extraction — Formula 81 under 3.2.4 Stage 4: Procedure Window Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, presentation-, operative, edge, flow, and the expression links oplus..** `\oplus`
Variables: "oplus".
Sign/normalization/conditioning/surrogate audit: "Formula 81 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: oplus; meanings remain tied to 3.2.4 Stage 4: Procedure Window Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.4 Stage 4: Procedure Window Extraction, formal object 81.

**Formal object 82 at 3.2.4 Stage 4: Procedure Window Extraction — Formula 82 under 3.2.4 Stage 4: Procedure Window Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, presentation-, operative, edge, flow, and the expression links mathcal, M..** `\mathcal{M}`
Variables: "mathcal, M".
Sign/normalization/conditioning/surrogate audit: "Formula 82 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, M; meanings remain tied to 3.2.4 Stage 4: Procedure Window Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.4 Stage 4: Procedure Window Extraction, formal object 82.

**Formal object 83 at 3.2.4 Stage 4: Procedure Window Extraction — Formula 83 under 3.2.4 Stage 4: Procedure Window Extraction is classified as a constraint or formal-analysis relation; adjacent prose centers on text, mathcal, presentation-, operative, edge, flow, and the expression links w_{i}, W_{i}, h_{i}, H_{i}, leq..** `\min(w_{i}/W_{i},h_{i}/H_{i})\leq 1-0.04`
Variables: "w_{i}, W_{i}, h_{i}, H_{i}, leq".
Sign/normalization/conditioning/surrogate audit: "Formula 83 operator audit: minimization, fraction or division; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: w_{i}, W_{i}, h_{i}, H_{i}, leq; meanings remain tied to 3.2.4 Stage 4: Procedure Window Extraction.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.4 Stage 4: Procedure Window Extraction, formal object 83.

**Formal object 84 at 3.2.5 Stage 5: Staged VQA Generation — Formula 84 under 3.2.5 Stage 5: Staged VQA Generation is classified as a state or representation transformation; adjacent prose centers on mathcal, action, state, operative, reasoning, categories, and the expression links mathcal, Y, y_{b}, y_{f}, y_{b}\in\mathcal{Y}, B, y_{f}\in\mathcal{Y}, F..** `\mathcal{Y}=\{(y_{b},y_{f}):y_{b}\in\mathcal{Y}_{B},\,y_{f}\in\mathcal{Y}_{F}(y_{b})\}`
Variables: "mathcal, Y, y_{b}, y_{f}, y_{b}\\in\\mathcal{Y}, B, y_{f}\\in\\mathcal{Y}, F".
Sign/normalization/conditioning/surrogate audit: "Formula 84 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, Y, y_{b}, y_{f}, y_{b}\\in\\mathcal{Y}, B, y_{f}\\in\\mathcal{Y}, F; meanings remain tied to 3.2.5 Stage 5: Staged VQA Generation.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.5 Stage 5: Staged VQA Generation, formal object 84.

**Formal object 85 at 3.2.5 Stage 5: Staged VQA Generation — Formula 85 under 3.2.5 Stage 5: Staged VQA Generation is classified as a state or representation transformation; adjacent prose centers on mathcal, action, state, operative, reasoning, categories, and the expression links mathcal, Y, B..** `|\mathcal{Y}_{B}|=5`
Variables: "mathcal, Y, B".
Sign/normalization/conditioning/surrogate audit: "Formula 85 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, Y, B; meanings remain tied to 3.2.5 Stage 5: Staged VQA Generation.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.5 Stage 5: Staged VQA Generation, formal object 85.

**Formal object 86 at 3.2.5 Stage 5: Staged VQA Generation — Formula 86 under 3.2.5 Stage 5: Staged VQA Generation is classified as a state or representation transformation; adjacent prose centers on mathcal, action, state, operative, reasoning, categories, and the expression links mathcal, Y, F..** `|\mathcal{Y}_{F}|=10`
Variables: "mathcal, Y, F".
Sign/normalization/conditioning/surrogate audit: "Formula 86 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker present; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, Y, F; meanings remain tied to 3.2.5 Stage 5: Staged VQA Generation.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.5 Stage 5: Staged VQA Generation, formal object 86.

**Formal object 87 at Pipeline. — Formula 87 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links v_{i}, t_{i}^{, k, s, e, c_{i}^{, in, mathcal..** `(v_{i}[t_{i}^{(k),s},t_{i}^{(k),e}],c_{i}^{(k)})\in\mathcal{A}_{i}^{\text{seg}}`
Variables: "v_{i}, t_{i}^{, k, s, e, c_{i}^{, in, mathcal, A, i".
Sign/normalization/conditioning/surrogate audit: "Formula 87 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: v_{i}, t_{i}^{, k, s, e, c_{i}^{, in, mathcal, A, i; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 87.

**Formal object 88 at Pipeline. — Formula 88 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links mathcal, C, i, k, c_{i}^{, w, m_{i}..** `\mathcal{C}_{i}^{(k)}=(c_{i}^{(k-w:k+w)},m_{i})`
Variables: "mathcal, C, i, k, c_{i}^{, w, m_{i}".
Sign/normalization/conditioning/surrogate audit: "Formula 88 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, C, i, k, c_{i}^{, w, m_{i}; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 88.

**Formal object 89 at Pipeline. — Formula 89 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links w..** `2w`
Variables: "w".
Sign/normalization/conditioning/surrogate audit: "Formula 89 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: w; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 89.

**Formal object 90 at Pipeline. — Formula 90 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links pi, i, k, mathcal, R, c_{i}^{, C..** `\pi_{i}^{(k)}=\mathcal{R}_{\text{plan}}(c_{i}^{(k)},\mathcal{C}_{i}^{(k)})`
Variables: "pi, i, k, mathcal, R, c_{i}^{, C".
Sign/normalization/conditioning/surrogate audit: "Formula 90 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: pi, i, k, mathcal, R, c_{i}^{, C; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 90.

**Formal object 91 at Pipeline. — Formula 91 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links pi, i, k, sigma, mathcal, E, Y..** `\pi_{i}^{(k)}=(\sigma_{i}^{(k)},\mathcal{E}_{i}^{(k)},\mathcal{Y}_{i}^{(k)})`
Variables: "pi, i, k, sigma, mathcal, E, Y".
Sign/normalization/conditioning/surrogate audit: "Formula 91 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: pi, i, k, sigma, mathcal, E, Y; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 91.

**Formal object 92 at Pipeline. — Formula 92 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links sigma, i, k..** `\sigma_{i}^{(k)}`
Variables: "sigma, i, k".
Sign/normalization/conditioning/surrogate audit: "Formula 92 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sigma, i, k; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 92.

**Formal object 93 at Pipeline. — Formula 93 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links mathcal, E, i, k..** `\mathcal{E}_{i}^{(k)}`
Variables: "mathcal, E, i, k".
Sign/normalization/conditioning/surrogate audit: "Formula 93 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, E, i, k; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 93.

**Formal object 94 at Pipeline. — Formula 94 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links mathcal, Y, i, k, subseteq..** `\mathcal{Y}_{i}^{(k)}\subseteq\mathcal{Y}`
Variables: "mathcal, Y, i, k, subseteq".
Sign/normalization/conditioning/surrogate audit: "Formula 94 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, Y, i, k, subseteq; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 94.

**Formal object 95 at Pipeline. — Formula 95 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links K_{\text{cat}}..** `K_{\text{cat}}`
Variables: "K_{\\text{cat}}".
Sign/normalization/conditioning/surrogate audit: "Formula 95 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K_{\\text{cat}}; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 95.

**Formal object 96 at Pipeline. — Formula 96 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links mathcal, Q, i, k, R, c_{i}^{, C, pi..** `\mathcal{Q}_{i}^{(k)}=\mathcal{R}_{\text{gen}}(c_{i}^{(k)},\mathcal{C}_{i}^{(k)},\pi_{i}^{(k)})=\{(q,a,y_{f},\texttt{evidence})\}`
Variables: "mathcal, Q, i, k, R, c_{i}^{, C, pi, q, a, y_{f}, texttt".
Sign/normalization/conditioning/surrogate audit: "Formula 96 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, Q, i, k, R, c_{i}^{, C, pi, q, a, y_{f}, texttt; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 96.

**Formal object 97 at Pipeline. — Formula 97 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links c_{i}^{, k, cup, mathcal, C, i..** `c_{i}^{(k)}\cup\mathcal{C}_{i}^{(k)}`
Variables: "c_{i}^{, k, cup, mathcal, C, i".
Sign/normalization/conditioning/surrogate audit: "Formula 97 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: c_{i}^{, k, cup, mathcal, C, i; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 97.

**Formal object 98 at Pipeline. — Formula 98 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links tilde, mathcal, Q, i, k, R, c_{i}^{, C..** `\tilde{\mathcal{Q}}_{i}^{(k)}=\mathcal{R}_{\text{judge}}(\mathcal{Q}_{i}^{(k)},c_{i}^{(k)},\mathcal{C}_{i}^{(k)})`
Variables: "tilde, mathcal, Q, i, k, R, c_{i}^{, C".
Sign/normalization/conditioning/surrogate audit: "Formula 98 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tilde, mathcal, Q, i, k, R, c_{i}^{, C; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 98.

**Formal object 99 at Pipeline. — Formula 99 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links gamma, g..** `\gamma_{g}`
Variables: "gamma, g".
Sign/normalization/conditioning/surrogate audit: "Formula 99 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, g; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 99.

**Formal object 100 at Pipeline. — Formula 100 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links gamma, t..** `\gamma_{t}`
Variables: "gamma, t".
Sign/normalization/conditioning/surrogate audit: "Formula 100 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, t; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 100.

**Formal object 101 at Pipeline. — Formula 101 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links gamma, a..** `\gamma_{a}`
Variables: "gamma, a".
Sign/normalization/conditioning/surrogate audit: "Formula 101 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, a; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 101.

**Formal object 102 at Pipeline. — Formula 102 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links gamma, n..** `\gamma_{n}`
Variables: "gamma, n".
Sign/normalization/conditioning/surrogate audit: "Formula 102 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, n; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 102.

**Formal object 103 at Pipeline. — Formula 103 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links gamma, h..** `\gamma_{h}`
Variables: "gamma, h".
Sign/normalization/conditioning/surrogate audit: "Formula 103 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, h; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 103.

**Formal object 104 at Pipeline. — Formula 104 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links ldots..** `\{1,\ldots,5\}`
Variables: "ldots".
Sign/normalization/conditioning/surrogate audit: "Formula 104 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: ldots; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 104.

**Formal object 105 at Pipeline. — Formula 105 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links gamma, g, t, a, n, h, geq, theta..** `\min(\gamma_{g},\gamma_{t},\gamma_{a},\gamma_{n},\gamma_{h})\geq\theta_{q}`
Variables: "gamma, g, t, a, n, h, geq, theta, q".
Sign/normalization/conditioning/surrogate audit: "Formula 105 operator audit: minimization; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma, g, t, a, n, h, geq, theta, q; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 105.

**Formal object 106 at Pipeline. — Formula 106 under Pipeline. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, gamma_, text, candidate, evidence, form, and the expression links mathcal, A, i, bigcup, k, tilde, Q..** `\mathcal{A}_{i}^{\text{qa}}=\bigcup_{k}\tilde{\mathcal{Q}}_{i}^{(k)}`
Variables: "mathcal, A, i, bigcup, k, tilde, Q".
Sign/normalization/conditioning/surrogate audit: "Formula 106 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A, i, bigcup, k, tilde, Q; meanings remain tied to Pipeline..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Pipeline., formal object 106.

**Formal object 107 at Question format. — Formula 107 under Question format. is classified as a evaluation or scoring relation; adjacent prose centers on open-ended, multiple-choice, pairs, accepted, pair, mathcal, and the expression links q, a, y_{f}, in, mathcal, A, i..** `(q,a,y_{f})\in\mathcal{A}_{i}^{\text{qa}}`
Variables: "q, a, y_{f}, in, mathcal, A, i".
Sign/normalization/conditioning/surrogate audit: "Formula 107 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: q, a, y_{f}, in, mathcal, A, i; meanings remain tied to Question format..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Question format., formal object 107.

**Formal object 108 at Question format. — Formula 108 under Question format. is classified as a evaluation or scoring relation; adjacent prose centers on open-ended, multiple-choice, pairs, accepted, pair, mathcal, and the expression links a..** `a`
Variables: "a".
Sign/normalization/conditioning/surrogate audit: "Formula 108 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: a; meanings remain tied to Question format..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Question format., formal object 108.

**Formal object 109 at Question format. — Formula 109 under Question format. is classified as a evaluation or scoring relation; adjacent prose centers on open-ended, multiple-choice, pairs, accepted, pair, mathcal, and the expression links o_{1}, o_{2}, o_{3}, o_{4}..** `(o_{1},o_{2},o_{3},o_{4})`
Variables: "o_{1}, o_{2}, o_{3}, o_{4}".
Sign/normalization/conditioning/surrogate audit: "Formula 109 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: o_{1}, o_{2}, o_{3}, o_{4}; meanings remain tied to Question format..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Question format., formal object 109.

**Formal object 110 at 3.2.6 Stage 6: Expert-Validated Evaluation Subset — Formula 110 under 3.2.6 Stage 6: Expert-Validated Evaluation Subset is classified as a probabilistic or expectation relation; adjacent prose centers on text, mathcal, subset, automatically, generated, supervision, and the expression links mathcal, A, i..** `\mathcal{A}_{i}^{\text{qa}}`
Variables: "mathcal, A, i".
Sign/normalization/conditioning/surrogate audit: "Formula 110 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A, i; meanings remain tied to 3.2.6 Stage 6: Expert-Validated Evaluation Subset.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.6 Stage 6: Expert-Validated Evaluation Subset, formal object 110.

**Formal object 111 at 3.2.6 Stage 6: Expert-Validated Evaluation Subset — Formula 111 under 3.2.6 Stage 6: Expert-Validated Evaluation Subset is classified as a probabilistic or expectation relation; adjacent prose centers on text, mathcal, subset, automatically, generated, supervision, and the expression links mathcal, A, subset, bigcup, i..** `\mathcal{A}^{\text{exp}}\subset\bigcup_{i}\mathcal{A}_{i}^{\text{qa}}`
Variables: "mathcal, A, subset, bigcup, i".
Sign/normalization/conditioning/surrogate audit: "Formula 111 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A, subset, bigcup, i; meanings remain tied to 3.2.6 Stage 6: Expert-Validated Evaluation Subset.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.6 Stage 6: Expert-Validated Evaluation Subset, formal object 111.

**Formal object 112 at 3.2.6 Stage 6: Expert-Validated Evaluation Subset — Formula 112 under 3.2.6 Stage 6: Expert-Validated Evaluation Subset is classified as a probabilistic or expectation relation; adjacent prose centers on text, mathcal, subset, automatically, generated, supervision, and the expression links N_{\text{rev}}..** `N_{\text{rev}}=2,960`
Variables: "N_{\\text{rev}}".
Sign/normalization/conditioning/surrogate audit: "Formula 112 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N_{\\text{rev}}; meanings remain tied to 3.2.6 Stage 6: Expert-Validated Evaluation Subset.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.6 Stage 6: Expert-Validated Evaluation Subset, formal object 112.

**Formal object 113 at 3.2.6 Stage 6: Expert-Validated Evaluation Subset — Formula 113 under 3.2.6 Stage 6: Expert-Validated Evaluation Subset is classified as a probabilistic or expectation relation; adjacent prose centers on text, mathcal, subset, automatically, generated, supervision, and the expression links symbols defined beside the formula..** `\{0,1\}`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 113 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 3.2.6 Stage 6: Expert-Validated Evaluation Subset.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.6 Stage 6: Expert-Validated Evaluation Subset, formal object 113.

**Formal object 114 at 3.2.7 Stage 7: Public Dataset Conversion — Formula 114 under 3.2.7 Stage 7: Public Dataset Conversion is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, splits, public, supervision, training, and the expression links mathcal, D, j..** `\mathcal{D}_{j}^{\text{pub}}`
Variables: "mathcal, D, j".
Sign/normalization/conditioning/surrogate audit: "Formula 114 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D, j; meanings remain tied to 3.2.7 Stage 7: Public Dataset Conversion.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.7 Stage 7: Public Dataset Conversion, formal object 114.

**Formal object 115 at 3.2.7 Stage 7: Public Dataset Conversion — Formula 115 under 3.2.7 Stage 7: Public Dataset Conversion is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, splits, public, supervision, training, and the expression links mathcal, T, j, f, y, mapsto, q, a..** `\mathcal{T}_{j}:(f,y)\mapsto(q,a)`
Variables: "mathcal, T, j, f, y, mapsto, q, a".
Sign/normalization/conditioning/surrogate audit: "Formula 115 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, T, j, f, y, mapsto, q, a; meanings remain tied to 3.2.7 Stage 7: Public Dataset Conversion.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.7 Stage 7: Public Dataset Conversion, formal object 115.

**Formal object 116 at 3.2.7 Stage 7: Public Dataset Conversion — Formula 116 under 3.2.7 Stage 7: Public Dataset Conversion is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, splits, public, supervision, training, and the expression links mathcal, D, bigcup, j, T..** `\mathcal{D}^{\text{IT}}=\bigcup_{j}\mathcal{T}_{j}(\mathcal{D}_{j}^{\text{pub,train}})`
Variables: "mathcal, D, bigcup, j, T".
Sign/normalization/conditioning/surrogate audit: "Formula 116 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D, bigcup, j, T; meanings remain tied to 3.2.7 Stage 7: Public Dataset Conversion.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.7 Stage 7: Public Dataset Conversion, formal object 116.

**Formal object 117 at Scale. — Formula 117 under Scale. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, videos, publicly, SurgAtlas, contains, mathcal, and the expression links N..** `N=15{,}291`
Variables: "N".
Sign/normalization/conditioning/surrogate audit: "Formula 117 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: N; meanings remain tied to Scale..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Scale., formal object 117.

**Formal object 118 at Scale. — Formula 118 under Scale. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, videos, publicly, SurgAtlas, contains, mathcal, and the expression links tau, mathcal, D..** `\tau(\mathcal{D})=2{,}391`
Variables: "tau, mathcal, D".
Sign/normalization/conditioning/surrogate audit: "Formula 118 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: tau, mathcal, D; meanings remain tied to Scale..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Scale., formal object 118.

**Formal object 119 at Scale. — Formula 119 under Scale. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, videos, publicly, SurgAtlas, contains, mathcal, and the expression links sim..** `\sim`
Variables: "sim".
Sign/normalization/conditioning/surrogate audit: "Formula 119 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sim; meanings remain tied to Scale..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Scale., formal object 119.

**Formal object 120 at Diversity. — Formula 120 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links S..** `S=18`
Variables: "S".
Sign/normalization/conditioning/surrogate audit: "Formula 120 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: S; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 120.

**Formal object 121 at Diversity. — Formula 121 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links symbols defined beside the formula..** `5000`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 121 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 121.

**Formal object 122 at Diversity. — Formula 122 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links symbols defined beside the formula..** `40.4\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 122 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 122.

**Formal object 123 at Diversity. — Formula 123 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links symbols defined beside the formula..** `4{,}913`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 123 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 123.

**Formal object 124 at Diversity. — Formula 124 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links symbols defined beside the formula..** `32.1\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 124 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 124.

**Formal object 125 at Diversity. — Formula 125 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links symbols defined beside the formula..** `3{,}051`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 125 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 125.

**Formal object 126 at Diversity. — Formula 126 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links symbols defined beside the formula..** `20.0\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 126 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 126.

**Formal object 127 at Diversity. — Formula 127 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links symbols defined beside the formula..** `122`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 127 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 127.

**Formal object 128 at Diversity. — Formula 128 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links symbols defined beside the formula..** `0.8\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 128 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 128.

**Formal object 129 at Diversity. — Formula 129 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links symbols defined beside the formula..** `1{,}023`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 129 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 129.

**Formal object 130 at Diversity. — Formula 130 under Diversity. is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, procedures, public, corpus, spans, specialties, and the expression links symbols defined beside the formula..** `6.7\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 130 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Diversity..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Diversity., formal object 130.

**Formal object 131 at Richness. — Formula 131 under Richness. is classified as a paper-defined mathematical relation; adjacent prose centers on video, four, levels, captions, reasoning, fine-grained, and the expression links K..** `300K`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 131 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to Richness..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Richness., formal object 131.

**Formal object 132 at Richness. — Formula 132 under Richness. is classified as a paper-defined mathematical relation; adjacent prose centers on video, four, levels, captions, reasoning, fine-grained, and the expression links K..** `81K`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 132 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to Richness..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Richness., formal object 132.

**Formal object 133 at Richness. — Formula 133 under Richness. is classified as a paper-defined mathematical relation; adjacent prose centers on video, four, levels, captions, reasoning, fine-grained, and the expression links K..** `12.2K`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 133 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to Richness..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Richness., formal object 133.

**Formal object 134 at Richness. — Formula 134 under Richness. is classified as a paper-defined mathematical relation; adjacent prose centers on video, four, levels, captions, reasoning, fine-grained, and the expression links K..** `400K`
Variables: "K".
Sign/normalization/conditioning/surrogate audit: "Formula 134 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: K; meanings remain tied to Richness..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Richness., formal object 134.

**Formal object 135 at Quality. — Formula 135 under Quality. is classified as a evaluation or scoring relation; adjacent prose centers on text, mathcal, surgical, content, pairs, quality, and the expression links mathcal, R..** `\mathcal{R}_{\text{LLM}}`
Variables: "mathcal, R".
Sign/normalization/conditioning/surrogate audit: "Formula 135 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, R; meanings remain tied to Quality..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Quality., formal object 135.

**Formal object 136 at Quality. — Formula 136 under Quality. is classified as a evaluation or scoring relation; adjacent prose centers on text, mathcal, surgical, content, pairs, quality, and the expression links mathcal, R..** `\mathcal{R}_{\text{judge}}`
Variables: "mathcal, R".
Sign/normalization/conditioning/surrogate audit: "Formula 136 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, R; meanings remain tied to Quality..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Quality., formal object 136.

**Formal object 137 at Quality. — Formula 137 under Quality. is classified as a evaluation or scoring relation; adjacent prose centers on text, mathcal, surgical, content, pairs, quality, and the expression links symbols defined beside the formula..** `7\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 137 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Quality..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Quality., formal object 137.

**Formal object 138 at 4.1 SurgAtlas-VLM: Aligning Qwen3-VL with SurgAtlas — Formula 138 under 4.1 SurgAtlas-VLM: Aligning Qwen3-VL with SurgAtlas is classified as a paper-defined mathematical relation; adjacent prose centers on supervision, stage, exploit, multigranular, mathcal, propose, and the expression links mathcal, D..** `\mathcal{D}`
Variables: "mathcal, D".
Sign/normalization/conditioning/surrogate audit: "Formula 138 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D; meanings remain tied to 4.1 SurgAtlas-VLM: Aligning Qwen3-VL with SurgAtlas.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 4.1 SurgAtlas-VLM: Aligning Qwen3-VL with SurgAtlas, formal object 138.

**Formal object 139 at Stage 1: Captioning pretraining. — Formula 139 under Stage 1: Captioning pretraining. is classified as a state or representation transformation; adjacent prose centers on text, mathcal, Step, projector, surgical, vision, and the expression links mathcal, D, bigcup, i, A, cup..** `\mathcal{D}_{\text{cap}}=\bigcup_{i}(\mathcal{A}_{i}^{\text{seg}}\cup\mathcal{A}_{i}^{\text{step}}\cup\mathcal{A}_{i}^{\text{vid}})`
Variables: "mathcal, D, bigcup, i, A, cup".
Sign/normalization/conditioning/surrogate audit: "Formula 139 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D, bigcup, i, A, cup; meanings remain tied to Stage 1: Captioning pretraining..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Stage 1: Captioning pretraining., formal object 139.

**Formal object 140 at Stage 1: Captioning pretraining. — Formula 140 under Stage 1: Captioning pretraining. is classified as a state or representation transformation; adjacent prose centers on text, mathcal, Step, projector, surgical, vision, and the expression links eta..** `\eta_{1}=10^{-4}`
Variables: "eta".
Sign/normalization/conditioning/surrogate audit: "Formula 140 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: eta; meanings remain tied to Stage 1: Captioning pretraining..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Stage 1: Captioning pretraining., formal object 140.

**Formal object 141 at Stage 1: Captioning pretraining. — Formula 141 under Stage 1: Captioning pretraining. is classified as a state or representation transformation; adjacent prose centers on text, mathcal, Step, projector, surgical, vision, and the expression links mathcal, D..** `\mathcal{D}_{\text{cap}}`
Variables: "mathcal, D".
Sign/normalization/conditioning/surrogate audit: "Formula 141 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D; meanings remain tied to Stage 1: Captioning pretraining..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Stage 1: Captioning pretraining., formal object 141.

**Formal object 142 at Stage 1: Captioning pretraining. — Formula 142 under Stage 1: Captioning pretraining. is classified as a state or representation transformation; adjacent prose centers on text, mathcal, Step, projector, surgical, vision, and the expression links eta, times..** `\eta_{2}=2\times 10^{-5}`
Variables: "eta, times".
Sign/normalization/conditioning/surrogate audit: "Formula 142 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: eta, times; meanings remain tied to Stage 1: Captioning pretraining..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Stage 1: Captioning pretraining., formal object 142.

**Formal object 143 at Stage 1: Captioning pretraining. — Formula 143 under Stage 1: Captioning pretraining. is classified as a state or representation transformation; adjacent prose centers on text, mathcal, Step, projector, surgical, vision, and the expression links mathcal, D, subset..** `\mathcal{D}_{\text{cap}}^{\text{clean}}\subset\mathcal{D}_{\text{cap}}`
Variables: "mathcal, D, subset".
Sign/normalization/conditioning/surrogate audit: "Formula 143 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D, subset; meanings remain tied to Stage 1: Captioning pretraining..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Stage 1: Captioning pretraining., formal object 143.

**Formal object 144 at Stage 1: Captioning pretraining. — Formula 144 under Stage 1: Captioning pretraining. is classified as a state or representation transformation; adjacent prose centers on text, mathcal, Step, projector, surgical, vision, and the expression links eta, times..** `\eta_{3}=5\times 10^{-6}`
Variables: "eta, times".
Sign/normalization/conditioning/surrogate audit: "Formula 144 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: eta, times; meanings remain tied to Stage 1: Captioning pretraining..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Stage 1: Captioning pretraining., formal object 144.

**Formal object 145 at Stage 1: Captioning pretraining. — Formula 145 under Stage 1: Captioning pretraining. is classified as a state or representation transformation; adjacent prose centers on text, mathcal, Step, projector, surgical, vision, and the expression links eta, v, times..** `\eta_{3}^{v}=2\times 10^{-6}`
Variables: "eta, v, times".
Sign/normalization/conditioning/surrogate audit: "Formula 145 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: eta, v, times; meanings remain tied to Stage 1: Captioning pretraining..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Stage 1: Captioning pretraining., formal object 145.

**Formal object 146 at Stage 2: Instruction tuning. — Formula 146 under Stage 2: Instruction tuning. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, Stage, inst, train, projector, and the expression links mathcal, D, bigcup, i, A, cup..** `\mathcal{D}_{\text{inst}}=\bigcup_{i}\mathcal{A}_{i}^{\text{qa}}\cup\mathcal{D}^{\text{IT}}`
Variables: "mathcal, D, bigcup, i, A, cup".
Sign/normalization/conditioning/surrogate audit: "Formula 146 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D, bigcup, i, A, cup; meanings remain tied to Stage 2: Instruction tuning..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Stage 2: Instruction tuning., formal object 146.

**Formal object 147 at Stage 2: Instruction tuning. — Formula 147 under Stage 2: Instruction tuning. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, Stage, inst, train, projector, and the expression links times..** `5\times 10^{-6}`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 147 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Stage 2: Instruction tuning..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Stage 2: Instruction tuning., formal object 147.

**Formal object 148 at Stage 2: Instruction tuning. — Formula 148 under Stage 2: Instruction tuning. is classified as a paper-defined mathematical relation; adjacent prose centers on mathcal, text, Stage, inst, train, projector, and the expression links mathcal, D..** `\mathcal{D}^{\text{IT}}`
Variables: "mathcal, D".
Sign/normalization/conditioning/surrogate audit: "Formula 148 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, D; meanings remain tied to Stage 2: Instruction tuning..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Stage 2: Instruction tuning., formal object 148.

**Formal object 149 at 4.2.1 Standard Surgical Benchmarks — Formula 149 under 4.2.1 Standard Surgical Benchmarks is classified as a evaluation or scoring relation; adjacent prose centers on recognition, Cholec80, HeiChole, MultiBypass140, evaluate, SurgAtlas-VLM, and the expression links symbols defined beside the formula..** `1`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 149 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 4.2.1 Standard Surgical Benchmarks.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 4.2.1 Standard Surgical Benchmarks, formal object 149.

**Formal object 150 at 4.2.1 Standard Surgical Benchmarks — Formula 150 under 4.2.1 Standard Surgical Benchmarks is classified as a evaluation or scoring relation; adjacent prose centers on recognition, Cholec80, HeiChole, MultiBypass140, evaluate, SurgAtlas-VLM, and the expression links symbols defined beside the formula..** `3`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 150 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 4.2.1 Standard Surgical Benchmarks.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 4.2.1 Standard Surgical Benchmarks, formal object 150.

**Formal object 151 at Phase and action recognition. — Formula 151 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, Table, recognition, and the expression links symbols defined beside the formula..** `+5.2`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 151 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 151.

**Formal object 152 at Phase and action recognition. — Formula 152 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, Table, recognition, and the expression links symbols defined beside the formula..** `+13.5`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 152 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 152.

**Formal object 153 at Phase and action recognition. — Formula 153 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, Table, recognition, and the expression links sim, times..** `\sim 9\times`
Variables: "sim, times".
Sign/normalization/conditioning/surrogate audit: "Formula 153 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sim, times; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 153.

**Formal object 154 at Phase and action recognition. — Formula 154 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `36.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 154 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 154.

**Formal object 155 at Phase and action recognition. — Formula 155 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `29.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 155 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 155.

**Formal object 156 at Phase and action recognition. — Formula 156 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `18.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 156 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 156.

**Formal object 157 at Phase and action recognition. — Formula 157 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `13.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 157 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 157.

**Formal object 158 at Phase and action recognition. — Formula 158 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `47.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 158 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 158.

**Formal object 159 at Phase and action recognition. — Formula 159 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `35.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 159 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 159.

**Formal object 160 at Phase and action recognition. — Formula 160 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `21.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 160 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 160.

**Formal object 161 at Phase and action recognition. — Formula 161 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `22.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 161 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 161.

**Formal object 162 at Phase and action recognition. — Formula 162 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `17.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 162 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 162.

**Formal object 163 at Phase and action recognition. — Formula 163 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `12.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 163 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 163.

**Formal object 164 at Phase and action recognition. — Formula 164 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `8.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 164 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 164.

**Formal object 165 at Phase and action recognition. — Formula 165 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `63.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 165 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 165.

**Formal object 166 at Phase and action recognition. — Formula 166 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `41.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 166 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 166.

**Formal object 167 at Phase and action recognition. — Formula 167 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `4.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 167 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 167.

**Formal object 168 at Phase and action recognition. — Formula 168 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `40.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 168 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 168.

**Formal object 169 at Phase and action recognition. — Formula 169 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `68.2`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 169 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 169.

**Formal object 170 at Phase and action recognition. — Formula 170 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `54.5`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 170 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 170.

**Formal object 171 at Phase and action recognition. — Formula 171 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `55.8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 171 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 171.

**Formal object 172 at Phase and action recognition. — Formula 172 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `23.9`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 172 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 172.

**Formal object 173 at Phase and action recognition. — Formula 173 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `15.2`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 173 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 173.

**Formal object 174 at Phase and action recognition. — Formula 174 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `30.5`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 174 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 174.

**Formal object 175 at Phase and action recognition. — Formula 175 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `16.7`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 175 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 175.

**Formal object 176 at Phase and action recognition. — Formula 176 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `26.2`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 176 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 176.

**Formal object 177 at Phase and action recognition. — Formula 177 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `36.4`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 177 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 177.

**Formal object 178 at Phase and action recognition. — Formula 178 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `31.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 178 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 178.

**Formal object 179 at Phase and action recognition. — Formula 179 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `33.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 179 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 179.

**Formal object 180 at Phase and action recognition. — Formula 180 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `38.9`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 180 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 180.

**Formal object 181 at Phase and action recognition. — Formula 181 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `36.8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 181 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 181.

**Formal object 182 at Phase and action recognition. — Formula 182 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `70.3`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 182 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 182.

**Formal object 183 at Phase and action recognition. — Formula 183 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `61.9`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 183 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 183.

**Formal object 184 at Phase and action recognition. — Formula 184 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `59.8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 184 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 184.

**Formal object 185 at Phase and action recognition. — Formula 185 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `76.4`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 185 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 185.

**Formal object 186 at Phase and action recognition. — Formula 186 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `70.8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 186 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 186.

**Formal object 187 at Phase and action recognition. — Formula 187 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `66.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 187 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 187.

**Formal object 188 at Phase and action recognition. — Formula 188 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `66.9`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 188 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 188.

**Formal object 189 at Phase and action recognition. — Formula 189 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `66.8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 189 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 189.

**Formal object 190 at Phase and action recognition. — Formula 190 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `73.5`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 190 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 190.

**Formal object 191 at Phase and action recognition. — Formula 191 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `2.4`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 191 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 191.

**Formal object 192 at Phase and action recognition. — Formula 192 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `2.6`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 192 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 192.

**Formal object 193 at Phase and action recognition. — Formula 193 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `2.5`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 193 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 193.

**Formal object 194 at Phase and action recognition. — Formula 194 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `4.8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 194 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 194.

**Formal object 195 at Phase and action recognition. — Formula 195 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `5.5`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 195 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 195.

**Formal object 196 at Phase and action recognition. — Formula 196 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `48.2`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 196 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 196.

**Formal object 197 at Phase and action recognition. — Formula 197 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `53.3`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 197 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 197.

**Formal object 198 at Phase and action recognition. — Formula 198 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `51.4`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 198 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 198.

**Formal object 199 at Phase and action recognition. — Formula 199 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `65.9`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 199 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 199.

**Formal object 200 at Phase and action recognition. — Formula 200 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `56.1`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 200 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 200.

**Formal object 201 at Phase and action recognition. — Formula 201 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `82.4`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 201 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 201.

**Formal object 202 at Phase and action recognition. — Formula 202 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `59.2`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 202 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 202.

**Formal object 203 at Phase and action recognition. — Formula 203 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `6.7`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 203 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 203.

**Formal object 204 at Phase and action recognition. — Formula 204 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `5.9`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 204 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 204.

**Formal object 205 at Phase and action recognition. — Formula 205 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `7.5`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 205 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 205.

**Formal object 206 at Phase and action recognition. — Formula 206 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `59.6`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 206 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 206.

**Formal object 207 at Phase and action recognition. — Formula 207 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `47.8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 207 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 207.

**Formal object 208 at Phase and action recognition. — Formula 208 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `63.9`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 208 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 208.

**Formal object 209 at Phase and action recognition. — Formula 209 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `67.1`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 209 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 209.

**Formal object 210 at Phase and action recognition. — Formula 210 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `76.9`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 210 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 210.

**Formal object 211 at Phase and action recognition. — Formula 211 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `75.3`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 211 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 211.

**Formal object 212 at Phase and action recognition. — Formula 212 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `72.9`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 212 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 212.

**Formal object 213 at Phase and action recognition. — Formula 213 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `76.6`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 213 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 213.

**Formal object 214 at Phase and action recognition. — Formula 214 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `76.1`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 214 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 214.

**Formal object 215 at Phase and action recognition. — Formula 215 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `83.1`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 215 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 215.

**Formal object 216 at Phase and action recognition. — Formula 216 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `70.6`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 216 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 216.

**Formal object 217 at Phase and action recognition. — Formula 217 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `77.7`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 217 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 217.

**Formal object 218 at Phase and action recognition. — Formula 218 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `77.1`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 218 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 218.

**Formal object 219 at Phase and action recognition. — Formula 219 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `82.9`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 219 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 219.

**Formal object 220 at Phase and action recognition. — Formula 220 under Phase and action recognition. is classified as a evaluation or scoring relation; adjacent prose centers on HeiChole, reports, phase, Cholec80, SurgAtlas-VLM, general-domain, and the expression links symbols defined beside the formula..** `73.0`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 220 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Phase and action recognition..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Phase and action recognition., formal object 220.

**Formal object 221 at Triplet recognition and CVS assessment. — Formula 221 under Triplet recognition and CVS assessment. is classified as a evaluation or scoring relation; adjacent prose centers on exceeding, triplet, accuracy, both, SurgVLM-72B, substantially, and the expression links symbols defined beside the formula..** `77.7\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 221 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Triplet recognition and CVS assessment..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Triplet recognition and CVS assessment., formal object 221.

**Formal object 222 at Triplet recognition and CVS assessment. — Formula 222 under Triplet recognition and CVS assessment. is classified as a evaluation or scoring relation; adjacent prose centers on exceeding, triplet, accuracy, both, SurgVLM-72B, substantially, and the expression links symbols defined beside the formula..** `76.9\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 222 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Triplet recognition and CVS assessment..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Triplet recognition and CVS assessment., formal object 222.

**Formal object 223 at Triplet recognition and CVS assessment. — Formula 223 under Triplet recognition and CVS assessment. is classified as a evaluation or scoring relation; adjacent prose centers on exceeding, triplet, accuracy, both, SurgVLM-72B, substantially, and the expression links symbols defined beside the formula..** `76.6\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 223 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Triplet recognition and CVS assessment..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Triplet recognition and CVS assessment., formal object 223.

**Formal object 224 at 4.2.2 SurgAtlas benchmarks. — Formula 224 under 4.2.2 SurgAtlas benchmarks. is classified as a evaluation or scoring relation; adjacent prose centers on SurgAtlas, mathcal, text, overall, broad, reasoning, and the expression links mathcal, A..** `\mathcal{A}^{\text{qa}}`
Variables: "mathcal, A".
Sign/normalization/conditioning/surrogate audit: "Formula 224 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: mathcal, A; meanings remain tied to 4.2.2 SurgAtlas benchmarks..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 4.2.2 SurgAtlas benchmarks., formal object 224.

**Formal object 225 at 4.2.2 SurgAtlas benchmarks. — Formula 225 under 4.2.2 SurgAtlas benchmarks. is classified as a evaluation or scoring relation; adjacent prose centers on SurgAtlas, mathcal, text, overall, broad, reasoning, and the expression links sim..** `\sim 10`
Variables: "sim".
Sign/normalization/conditioning/surrogate audit: "Formula 225 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sim; meanings remain tied to 4.2.2 SurgAtlas benchmarks..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 4.2.2 SurgAtlas benchmarks., formal object 225.

**Formal object 226 at 4.2.2 SurgAtlas benchmarks. — Formula 226 under 4.2.2 SurgAtlas benchmarks. is classified as a evaluation or scoring relation; adjacent prose centers on SurgAtlas, mathcal, text, overall, broad, reasoning, and the expression links times..** `30\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 226 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to 4.2.2 SurgAtlas benchmarks..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 4.2.2 SurgAtlas benchmarks., formal object 226.

**Formal object 227 at Open versus minimally invasive surgery. — Formula 227 under Open versus minimally invasive surgery. is classified as a evaluation or scoring relation; adjacent prose centers on open-surgery, Every, general-domain, baseline, GPT-5.1, SurgAtlas, and the expression links symbols defined beside the formula..** `-3.5`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 227 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Open versus minimally invasive surgery..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Open versus minimally invasive surgery., formal object 227.

**Formal object 228 at Open versus minimally invasive surgery. — Formula 228 under Open versus minimally invasive surgery. is classified as a evaluation or scoring relation; adjacent prose centers on open-surgery, Every, general-domain, baseline, GPT-5.1, SurgAtlas, and the expression links symbols defined beside the formula..** `-3.6`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 228 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Open versus minimally invasive surgery..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Open versus minimally invasive surgery., formal object 228.

**Formal object 229 at Cross-regime training ablation. — Formula 229 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `42.5\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 229 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 229.

**Formal object 230 at Cross-regime training ablation. — Formula 230 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `39.0\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 230 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 230.

**Formal object 231 at Cross-regime training ablation. — Formula 231 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `29.1\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 231 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 231.

**Formal object 232 at Cross-regime training ablation. — Formula 232 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `32.2\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 232 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 232.

**Formal object 233 at Cross-regime training ablation. — Formula 233 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `62.5\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 233 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 233.

**Formal object 234 at Cross-regime training ablation. — Formula 234 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `56.1\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 234 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 234.

**Formal object 235 at Cross-regime training ablation. — Formula 235 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `55.9\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 235 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 235.

**Formal object 236 at Cross-regime training ablation. — Formula 236 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `24.8\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 236 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 236.

**Formal object 237 at Cross-regime training ablation. — Formula 237 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `20`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 237 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 237.

**Formal object 238 at Cross-regime training ablation. — Formula 238 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 238 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 238.

**Formal object 239 at Cross-regime training ablation. — Formula 239 under Cross-regime training ablation. is classified as a probabilistic or expectation relation; adjacent prose centers on Open, surgical, only, open-surgery, operating-room, context, and the expression links symbols defined beside the formula..** `47.8\%`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 239 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Cross-regime training ablation..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation., formal object 239.

**Formal object 240 at 5 Conclusion — Formula 240 under 5 Conclusion is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, videos, SurgAtlas, across, surgery, pairs, and the expression links symbols defined beside the formula..** `300`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 240 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5 Conclusion.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 5 Conclusion, formal object 240.

**Formal object 241 at 5 Conclusion — Formula 241 under 5 Conclusion is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, videos, SurgAtlas, across, surgery, pairs, and the expression links symbols defined beside the formula..** `81`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 241 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5 Conclusion.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 5 Conclusion, formal object 241.

**Formal object 242 at 5 Conclusion — Formula 242 under 5 Conclusion is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, videos, SurgAtlas, across, surgery, pairs, and the expression links symbols defined beside the formula..** `12.2`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 242 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5 Conclusion.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 5 Conclusion, formal object 242.

**Formal object 243 at 5 Conclusion — Formula 243 under 5 Conclusion is classified as a paper-defined mathematical relation; adjacent prose centers on surgical, videos, SurgAtlas, across, surgery, pairs, and the expression links symbols defined beside the formula..** `400`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 243 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to 5 Conclusion.".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, 5 Conclusion, formal object 243.

**Formal object 244 at Specialty distribution. — Formula 244 under Specialty distribution. is classified as a probabilistic or expectation relation; adjacent prose centers on open, videos, National, Government, under, views, and the expression links sim..** `\sim 70\%`
Variables: "sim".
Sign/normalization/conditioning/surrogate audit: "Formula 244 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sim; meanings remain tied to Specialty distribution..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution., formal object 244.

**Formal object 245 at Specialty distribution. — Formula 245 under Specialty distribution. is classified as a probabilistic or expectation relation; adjacent prose centers on open, videos, specialties, minimally, invasive, corpus, and the expression links symbols defined beside the formula..** `739`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 245 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Specialty distribution..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution., formal object 245.

**Formal object 246 at Specialty distribution. — Formula 246 under Specialty distribution. is classified as a probabilistic or expectation relation; adjacent prose centers on open, videos, specialties, minimally, invasive, corpus, and the expression links symbols defined beside the formula..** `1{,}653`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 246 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Specialty distribution..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution., formal object 246.

**Formal object 247 at Specialty distribution. — Formula 247 under Specialty distribution. is classified as a probabilistic or expectation relation; adjacent prose centers on open, videos, specialties, minimally, invasive, corpus, and the expression links symbols defined beside the formula..** `2{,}928`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 247 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Specialty distribution..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution., formal object 247.

**Formal object 248 at Specialty distribution. — Formula 248 under Specialty distribution. is classified as a probabilistic or expectation relation; adjacent prose centers on open, videos, specialties, minimally, invasive, corpus, and the expression links symbols defined beside the formula..** `2{,}297`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 248 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Specialty distribution..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution., formal object 248.

**Formal object 249 at Specialty distribution. — Formula 249 under Specialty distribution. is classified as a probabilistic or expectation relation; adjacent prose centers on open, videos, specialties, minimally, invasive, corpus, and the expression links symbols defined beside the formula..** `2{,}093`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 249 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Specialty distribution..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution., formal object 249.

**Formal object 250 at Specialty distribution. — Formula 250 under Specialty distribution. is classified as a probabilistic or expectation relation; adjacent prose centers on open, videos, specialties, minimally, invasive, corpus, and the expression links symbols defined beside the formula..** `1{,}761`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 250 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Specialty distribution..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution., formal object 250.

**Formal object 251 at Specialty distribution. — Formula 251 under Specialty distribution. is classified as a probabilistic or expectation relation; adjacent prose centers on open, videos, specialties, minimally, invasive, corpus, and the expression links symbols defined beside the formula..** `1{,}627`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 251 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Specialty distribution..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution., formal object 251.

**Formal object 252 at Specialty distribution. — Formula 252 under Specialty distribution. is classified as a probabilistic or expectation relation; adjacent prose centers on open, videos, specialties, minimally, invasive, corpus, and the expression links symbols defined beside the formula..** `1{,}546`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 252 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Specialty distribution..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution., formal object 252.

**Formal object 253 at Specialty distribution. — Formula 253 under Specialty distribution. is classified as a probabilistic or expectation relation; adjacent prose centers on open, videos, specialties, minimally, invasive, corpus, and the expression links symbols defined beside the formula..** `1{,}382`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 253 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Specialty distribution..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution., formal object 253.

**Formal object 254 at Fine-grained results. — Formula 254 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `10`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 254 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 254.

**Formal object 255 at Fine-grained results. — Formula 255 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `+10.3`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 255 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 255.

**Formal object 256 at Fine-grained results. — Formula 256 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `+12.6`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 256 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 256.

**Formal object 257 at Fine-grained results. — Formula 257 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `+4.6`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 257 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 257.

**Formal object 258 at Fine-grained results. — Formula 258 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `+10.7`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 258 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 258.

**Formal object 259 at Fine-grained results. — Formula 259 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `48.4`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 259 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 259.

**Formal object 260 at Fine-grained results. — Formula 260 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `53.4`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 260 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 260.

**Formal object 261 at Fine-grained results. — Formula 261 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `45.5`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 261 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 261.

**Formal object 262 at Fine-grained results. — Formula 262 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `46.8`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 262 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 262.

**Formal object 263 at Fine-grained results. — Formula 263 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `41.7`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 263 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 263.

**Formal object 264 at Fine-grained results. — Formula 264 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `41.6`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 264 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 264.

**Formal object 265 at Fine-grained results. — Formula 265 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `39.4`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 265 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 265.

**Formal object 266 at Fine-grained results. — Formula 266 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links symbols defined beside the formula..** `32`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 266 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 266.

**Formal object 267 at Fine-grained results. — Formula 267 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links sim..** `\sim 13`
Variables: "sim".
Sign/normalization/conditioning/surrogate audit: "Formula 267 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sim; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 267.

**Formal object 268 at Fine-grained results. — Formula 268 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links times..** `4\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 268 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 268.

**Formal object 269 at Fine-grained results. — Formula 269 under Fine-grained results. is classified as a evaluation or scoring relation; adjacent prose centers on mathcal, text, categories, Table, split, both, and the expression links sim..** `\sim 5\%`
Variables: "sim".
Sign/normalization/conditioning/surrogate audit: "Formula 269 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sim; meanings remain tied to Fine-grained results..".
Source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results., formal object 269.

Representative source mathematical objects follow. They are navigation evidence, not standalone interpretations:

- Mathematical object 1: `5{,}000` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 2: `\Sigma` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 3: `15{,}291` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 4: `2{,}391` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 5: `\mathcal{D}=\{(v_{i},\mathcal{A}_{i})\}_{i=1}^{N}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 6: `v_{i}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 7: `i` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 8: `\mathcal{A}_{i}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 9: `v_{i}=(f_{i}^{1},\ldots,f_{i}^{T_{i}})` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 10: `\tau(v_{i})` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 11: `a_{i}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.
- Mathematical object 12: `\mathcal{O}_{i}` — read with adjacent definitions; no symbol meaning is inferred from markup alone.

Equation-to-adjacent-context reconstruction:

- Equation under source heading Abstract: `5{,}000`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading 1 Introduction: `\Sigma`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading 2 Related Work: `15{,}291`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading 2 Related Work: `2{,}391`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading Surgical vision–language datasets and models.: `\Sigma`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading 3.2 Dataset Construction Pipeline: `\mathcal{D}=\{(v_{i},\mathcal{A}_{i})\}_{i=1}^{N}`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading 3.2 Dataset Construction Pipeline: `v_{i}`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading 3.2 Dataset Construction Pipeline: `i`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading 3.2 Dataset Construction Pipeline: `\mathcal{A}_{i}`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading 3.2 Dataset Construction Pipeline: `v_{i}`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading 3.2 Dataset Construction Pipeline: `v_{i}=(f_{i}^{1},\ldots,f_{i}^{T_{i}})`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.
- Equation under source heading 3.2 Dataset Construction Pipeline: `\tau(v_{i})`; adjacent method terms: datasets, videos, hierarchical, supervision, narrated, into, scale, two.

For each central equation, the audit asks whether the sign agrees with the prose, whether weights are normalized, whether masking or conditioning changes the denominator, whether a displayed objective is exact or a training surrogate, and whether units can be compared. A learned score is not automatically calibrated, a relaxation is not an exact discrete solution, and an empirical constraint satisfaction rate is not a theorem. These distinctions protect the paper's real contribution from stronger claims it does not need.

### 2.3 Components, architecture, and information flow

The source's technical path is anchored to Surgical vision–language datasets and models.. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims.

**Input/output dataflow:** The documented dataflow is reconstructed only across Surgical vision–language datasets and models., where the source associates datasets, surgical, videos, hierarchical, supervision, narrated, and scale. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

| Component | Inherited or novel | Role | Source locator |
|---|---|---|---|
| Surgical vision–language datasets and models. | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with datasets, Surgical, language, videos, and hierarchical; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2606.25905, Surgical vision–language datasets and models. |

The paper-specific method vocabulary is datasets, videos, hierarchical, supervision, narrated, into, scale, two, main, directions. This vocabulary was derived from the complete method/architecture paragraphs rather than the title. It identifies the entities that must appear in a faithful architecture reconstruction and creates a falsifiable check: an implementation or summary that omits these named objects is not yet grounded in this paper.

The architecture is reconstructed as an information-flow graph: source identity and inputs enter; inherited and paper-specific components transform or score them; a decision or representation is produced; optional validation or post-processing occurs; and an evaluated outcome leaves the pipeline. Each edge should name the information available at that point. A comparison becomes unfair if one method has access to labels, future requests, privileged metadata, additional context, or a larger tuning budget that another method lacks.

### 2.4 Training, calibration, and inference

Construction-time and runtime work are separate accounting domains. Training may fit parameters, construct representations, estimate thresholds, tune prompts, or learn a policy. Calibration may use held-out examples or measurements. Inference may retrieve, route, compress, classify, generate, search, solve, or verify. Post-processing may enforce a constraint or discard invalid output. A credible efficiency claim says which of these phases is included, which is amortized, and which is external to the reported number.

No sentence was mechanically classified as an explicit training/calibration description. The review therefore does not invent optimizer, epoch, seed, or training-cost details; construction semantics remain anchored to the method sections.

Paper-specific construction/training sequence:

1. At 3.2.6 Stage 6: Expert-Validated Evaluation Subset, the paper reports a training-related operation involving text, mathcal, Subset, Stage, Evaluation, and automatically. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.6 Stage 6: Expert-Validated Evaluation Subset)*
2. At 3.2.7 Stage 7: Public Dataset Conversion, the paper reports a training-related operation involving mathcal, Public, text, splits, Dataset, and supervision. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.7 Stage 7: Public Dataset Conversion)*
3. At 4.2.2 SurgAtlas benchmarks., the paper reports a training-related operation involving SurgAtlas, mathcal, text, overall, broad, and reasoning. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, 4.2.2 SurgAtlas benchmarks.)*
4. At Cross-regime training ablation., the paper reports a training-related operation involving training, regime, partition, Cross-regime, ablation, and isolate. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation.)*

Inference or runtime evidence is explicitly located in Fine-grained results., 3.2.6 Stage 6: Expert-Validated Evaluation Subset. Its source vocabulary overlaps datasets, videos, hierarchical, supervision, narrated, into, scale, two, main, directions.

Paper-specific inference/evaluation sequence:

1. At 3.2.6 Stage 6: Expert-Validated Evaluation Subset, the paper reports an inference or deployment action involving text, mathcal, Subset, Stage, Evaluation, and automatically. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.6 Stage 6: Expert-Validated Evaluation Subset)*
2. At 4.2.1 Standard Surgical Benchmarks, the paper reports an inference or deployment action involving Surgical, Benchmarks, recognition, Cholec80, HeiChole, and MultiBypass140. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, 4.2.1 Standard Surgical Benchmarks)*
3. At Cross-regime training ablation., the paper reports an inference or deployment action involving Open, surgical, training, open-surgery, operating-room, and context. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation.)*
4. At Fine-grained results., the paper reports an inference or deployment action involving Fine-grained, mathcal, text, categories, split, and variants. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results.)*

The reconstructed operational sequence is: pin input and artifact versions; validate prerequisites; compute the method-specific state or signal; apply the stated decision or objective; materialize the output; execute any downstream consumer; and measure both quality and resource outcomes. This sequence is reviewer inference grounded in the paper's organization. It is a testing model, not an assertion that the authors implemented an identical production controller.[^inference]

### 2.5 Notation and implementation audit

No independent implementation was run. The audit therefore checks internal legibility across equations, prose, captions, appendices, and extracted code/data statements. Apparent inconsistencies remain unresolved unless source evidence explains them. Source availability is classified in levels—declared, reachable, inspectable, runnable, and result-reproducing—and this local phase establishes only the declared/local-source layers.

## 3. Architecture and Complete Operational Pipeline

### 3.1 Representation and state

The documented dataflow is reconstructed only across Surgical vision–language datasets and models., where the source associates datasets, surgical, videos, hierarchical, supervision, narrated, and scale. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

The central representation must be described by shape, type, provenance, lifetime, and relationship to the original input. If it is compressed, selected, latent, retrieved, generated, or aggregated, the review asks what information can be lost and how that loss is detected. If it is learned, the training distribution and version become part of its identity. If it is mutable, update ordering, expiry, and rollback become part of the method rather than operational afterthoughts.

### 3.2 Decision or action modules

The paper-specific modules should be separated from inherited encoders, decoders, solvers, retrieval systems, evaluators, or model APIs. A score can rank candidates without being calibrated; a policy can improve average reward without satisfying hard constraints; and a verifier can reject some failures without certifying all accepted outputs. The assessment uses the source's strongest ablation or controlled comparison to decide which module is necessary and which is merely bundled.

### 3.3 Dependencies, post-processing, and guarantee boundary

Dependencies include data preprocessing, external models, tokenizers, simulators, indexes, numerical libraries, and evaluation code. Post-processing can materially create the final result, so its compute and failure rate belong in the pipeline. Exact validation, when present, may establish a property of a returned object; it does not automatically establish semantic correctness, optimality, robustness, or absence of distribution shift.

### 3.4 Resource allocation and stopping

Budgets can refer to tokens, bytes, parameters, candidates, iterations, calls, samples, time, energy, or money. Requested and achieved budgets should both be recorded. Early stopping and fallback can bias which cases receive expensive processing. Batching can improve throughput while worsening latency. The review therefore distinguishes construction cost, per-instance latency, batch throughput, tail latency, peak memory, and downstream cost before accepting a general efficiency claim.

## 4. Experimental Design and Evidence Reconstructed

The evaluation reconstruction follows Cross-regime training ablation., Fine-grained results., Surgical video datasets., 3.2 Dataset Construction Pipeline, 3.2.6 Stage 6: Expert-Validated Evaluation Subset, 3.2.7 Stage 7: Public Dataset Conversion, with 6 table captions and 8 figure captions inventoried.

Paper-specific evaluation vocabulary centers on mathcal, text, exp, surgical, mis, only, open, both, each, supervision. These terms constrain which datasets, metrics, models, budgets, or operational quantities must be preserved with each reported comparison. They also identify where a later reproduction dossier must look for splits, baselines, hardware, batching, runtime semantics, and uncertainty rather than assuming conventional defaults.

The headings mechanically associated with evaluation and results were:

- Cross-regime training ablation.
- Fine-grained results.
- Surgical video datasets.
- 3.2 Dataset Construction Pipeline
- 3.2.6 Stage 6: Expert-Validated Evaluation Subset
- 3.2.7 Stage 7: Public Dataset Conversion

### 4.1 Data, splits, and distribution

| Dataset | Split | Preprocessing | Source locator |
|---|---|---|---|
| VQA | The evidence at Abstract names training, development partition(s) without a mechanically isolated sample count. | The preprocessing evidence for VQA names datasets, videos, hierarchical, supervision, narrated, scale at Surgical vision–language datasets and models.. | private full-paper evidence dossier for arXiv:2606.25905, Abstract |
| PitVQA | The evidence at 3.2.7 Stage 7: Public Dataset Conversion names training, train, test, held out partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to PitVQA was stated in the captured paragraphs at 3.2.7 Stage 7: Public Dataset Conversion; none is imputed. | private full-paper evidence dossier for arXiv:2606.25905, 3.2.7 Stage 7: Public Dataset Conversion |
| SurgBench | The evidence at References names partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to SurgBench was stated in the captured paragraphs at References; none is imputed. | private full-paper evidence dossier for arXiv:2606.25905, References |

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| GPT-5 | Table 3 lists GPT-5 as a numeric comparison row under Open versus minimally invasive surgery.. | Neither the Table 3 caption nor its row label establishes whether GPT-5 was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 3 row GPT-5 |
| GPT-5.1 | Table 3 lists GPT-5.1 as a numeric comparison row under Open versus minimally invasive surgery.. | Neither the Table 3 caption nor its row label establishes whether GPT-5.1 was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 3 row GPT-5.1 |
| Gemini 2.5 Pro | Table 3 lists Gemini 2.5 Pro as a numeric comparison row under Open versus minimally invasive surgery.. | Neither the Table 3 caption nor its row label establishes whether Gemini 2.5 Pro was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 3 row Gemini 2.5 Pro |
| Entity existence | Table 5 lists Entity existence as a numeric comparison row under Fine-grained results.. | Neither the Table 5 caption nor its row label establishes whether Entity existence was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row Entity existence |
| Entity state | Table 5 lists Entity state as a numeric comparison row under Fine-grained results.. | Neither the Table 5 caption nor its row label establishes whether Entity state was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row Entity state |
| Spatial relation | Table 5 lists Spatial relation as a numeric comparison row under Fine-grained results.. | Neither the Table 5 caption nor its row label establishes whether Spatial relation was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row Spatial relation |
| Instrument–tissue interaction | Table 5 lists Instrument–tissue interaction as a numeric comparison row under Fine-grained results.. | Neither the Table 5 caption nor its row label establishes whether Instrument–tissue interaction was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row Instrument–tissue interaction |
| Operative action | Table 5 lists Operative action as a numeric comparison row under Fine-grained results.. | Neither the Table 5 caption nor its row label establishes whether Operative action was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row Operative action |
| Maneuver rationale | Table 5 lists Maneuver rationale as a numeric comparison row under Fine-grained results.. | Neither the Table 5 caption nor its row label establishes whether Maneuver rationale was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row Maneuver rationale |
| Decision justification | Table 5 lists Decision justification as a numeric comparison row under Fine-grained results.. | Neither the Table 5 caption nor its row label establishes whether Decision justification was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row Decision justification |
| Procedural sequence | Table 5 lists Procedural sequence as a numeric comparison row under Fine-grained results.. | Neither the Table 5 caption nor its row label establishes whether Procedural sequence was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row Procedural sequence |
| Next-step prediction | Table 5 lists Next-step prediction as a numeric comparison row under Fine-grained results.. | Neither the Table 5 caption nor its row label establishes whether Next-step prediction was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row Next-step prediction |
| Risk anatomy identification | Table 5 lists Risk anatomy identification as a numeric comparison row under Fine-grained results.. | Neither the Table 5 caption nor its row label establishes whether Risk anatomy identification was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row Risk anatomy identification |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

| Metric | Denominator/conditioning | Direction | Source locator |
|---|---|---|---|
| accuracy | Table 3 reports accuracy as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.25905, Table 3 header Perception & ID / MIS / General-domain VLMs |

Metrics are reconstructed with direction, denominator, aggregation unit, conditioning, and reference quality. Failures excluded from an average create survivor bias. A gap to a best-known incumbent is not a gap to a proven optimum. A judge-model score is not a human preference without validation. A compression ratio can invert depending on convention. Confidence intervals, paired tests, and effect sizes matter when differences are close or instances are correlated.

### 4.4 Hardware, batching, and runtime semantics

Quality-v2 paper-specific hardware/runtime evidence:

- At Abstract, the paper's hardware/runtime paragraph names 391 hours. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, Abstract)*
- At 1 Introduction, the paper's hardware/runtime paragraph names 47 hours. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, 1 Introduction)*
- At 1 Introduction, the paper's hardware/runtime paragraph names 391 hours. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, 1 Introduction)*
- At Surgical vision–language datasets and models., the paper's hardware/runtime paragraph names datasets, videos, hierarchical, supervision, narrated, scale, main, directions. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, Surgical vision–language datasets and models.)*
- At 3.2.1 Stage 1: Collection and Filtering, the paper's hardware/runtime paragraph names mathcal, text, title, surgical, procedure, sigma, specialty, candidates. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, 3.2.1 Stage 1: Collection and Filtering)*
- At Scale., the paper's hardware/runtime paragraph names 391 hours. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, Scale.)*
- At 5 Conclusion, the paper's hardware/runtime paragraph names 391 hours. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, 5 Conclusion)*
- At Specialty distribution., the paper's hardware/runtime paragraph names 391 hours. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, Specialty distribution.)*


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
| Table 3 | SurgAtlas-VLM (SurgAtlas) | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Perception & ID / MIS / General-domain VLMs; Perception & ID / Open / General-domain VLMs; Action / state / MIS / General-domain VLMs; Action / state / Open / General-domain VLMs; Operative reas. / MIS / General-domain VLMs; Operative reas. / Open / General-domain VLMs; Temporal / pred. / MIS / General-domain VLMs; Temporal / pred. / Open / General-domain VLMs; Risk anatomy ID / MIS / General-domain VLMs; Risk anatomy ID / Open / General-domain VLMs; Overall / MIS / General-domain VLMs; Overall / Open / General-domain VLMs | Perception & ID / MIS / General-domain VLMs=42.3; Perception & ID / Open / General-domain VLMs=41.0; Action / state / MIS / General-domain VLMs=42.5; Action / state / Open / General-domain VLMs=34.5; Operative reas. / MIS / General-domain VLMs=37.3; Operative reas. / Open / General-domain VLMs=37.9; Temporal / pred. / MIS / General-domain VLMs=44.4; Temporal / pred. / Open / General-domain VLMs=40.0; Risk anatomy ID / MIS / General-domain VLMs=58.8; Risk anatomy ID / Open / General-domain VLMs=67.2; Overall / MIS / General-domain VLMs=42.5; Overall / Open / General-domain VLMs=39.0 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.25905, Table 3 row 10 |
| Table 3 | SurgAtlas-VLM ( + public) | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Perception & ID / MIS / General-domain VLMs; Perception & ID / Open / General-domain VLMs; Action / state / MIS / General-domain VLMs; Action / state / Open / General-domain VLMs; Operative reas. / MIS / General-domain VLMs; Operative reas. / Open / General-domain VLMs; Temporal / pred. / MIS / General-domain VLMs; Temporal / pred. / Open / General-domain VLMs; Risk anatomy ID / MIS / General-domain VLMs; Risk anatomy ID / Open / General-domain VLMs; Overall / MIS / General-domain VLMs; Overall / Open / General-domain VLMs | Perception & ID / MIS / General-domain VLMs=41.6; Perception & ID / Open / General-domain VLMs=39.4; Action / state / MIS / General-domain VLMs=42.7; Action / state / Open / General-domain VLMs=36.0; Operative reas. / MIS / General-domain VLMs=39.9; Operative reas. / Open / General-domain VLMs=38.5; Temporal / pred. / MIS / General-domain VLMs=46.5; Temporal / pred. / Open / General-domain VLMs=41.3; Risk anatomy ID / MIS / General-domain VLMs=58.8; Risk anatomy ID / Open / General-domain VLMs=68.9; Overall / MIS / General-domain VLMs=42.9; Overall / Open / General-domain VLMs=39.3 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.25905, Table 3 row 11 |
| Table 4 | SurgAtlas (Open only) | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | \mathcal{A}^{\text{exp}} / MIS; \mathcal{A}^{\text{exp}} / Open; EgoSurgery / (zero-shot) | \mathcal{A}^{\text{exp}} / MIS=32.2; \mathcal{A}^{\text{exp}} / Open=38.9; EgoSurgery / (zero-shot)=62.5 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.25905, Table 4 row 6 |
| Table 4 | SurgAtlas (combined) | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | \mathcal{A}^{\text{exp}} / MIS; \mathcal{A}^{\text{exp}} / Open; EgoSurgery / (zero-shot) | \mathcal{A}^{\text{exp}} / MIS=42.5; \mathcal{A}^{\text{exp}} / Open=39.0; EgoSurgery / (zero-shot)=56.1 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.25905, Table 4 row 7 |
| Table 5 | GPT-5.1 / SurgAtlas only / SurgAtlas + public | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | General-domain VLMs / MIS; General-domain VLMs / Open | General-domain VLMs / MIS=8B; General-domain VLMs / Open=8B; General-domain VLMs / MIS=32B; General-domain VLMs / Open=32B | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row 2 |
| Table 5 | Entity existence | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | General-domain VLMs / MIS; General-domain VLMs / Open; Surgical VLMs (ours) / MIS; Surgical VLMs (ours) / Open | General-domain VLMs / MIS=39.5; General-domain VLMs / Open=35.4; General-domain VLMs / MIS=24.0; General-domain VLMs / Open=24.8; General-domain VLMs / MIS=28.0; General-domain VLMs / Open=25.9; Surgical VLMs (ours) / MIS=49.8; Surgical VLMs (ours) / Open=48.0; Surgical VLMs (ours) / MIS=45.9; Surgical VLMs (ours) / Open=47.2 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 row 5 |
| Table 6 | Entity existence | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | General-domain VLMs / MIS; General-domain VLMs / Open; Surgical VLMs (ours) / MIS; Surgical VLMs (ours) / Open | General-domain VLMs / MIS=36.5; General-domain VLMs / Open=36.9; General-domain VLMs / MIS=34.5; General-domain VLMs / Open=35.9; General-domain VLMs / MIS=29.7; General-domain VLMs / Open=28.9; General-domain VLMs / MIS=26.5; General-domain VLMs / Open=18.5; General-domain VLMs / MIS=33.0; General-domain VLMs / Open=20.0; Surgical VLMs (ours) / MIS=46.0; Surgical VLMs (ours) / Open=47.7; Surgical VLMs (ours) / MIS=45.5; Surgical VLMs (ours) / Open=47.2 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.25905, Table 6 row 5 |
| Table 6 | Entity state | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | General-domain VLMs / MIS; General-domain VLMs / Open; Surgical VLMs (ours) / MIS; Surgical VLMs (ours) / Open | General-domain VLMs / MIS=47.1; General-domain VLMs / Open=36.0; General-domain VLMs / MIS=43.5; General-domain VLMs / Open=38.0; General-domain VLMs / MIS=35.3; General-domain VLMs / Open=25.7; General-domain VLMs / MIS=29.1; General-domain VLMs / Open=18.0; General-domain VLMs / MIS=34.9; General-domain VLMs / Open=27.0; Surgical VLMs (ours) / MIS=43.0; Surgical VLMs (ours) / Open=41.0; Surgical VLMs (ours) / MIS=44.2; Surgical VLMs (ours) / Open=33.0 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.25905, Table 6 row 6 |
| result context at Cross-regime training ablation. | SurgAtlas | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | accuracy | 10, 29.1, 32.2 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation. |
| result context at Cross-regime training ablation. | SurgAtlas | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 24.8, 20, 8 B, 47.8 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation. |
| result context at Fine-grained results. | SurgAtlas | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 32 B, 13, 4 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results. |
| result context at 4.2.2 SurgAtlas benchmarks. | SurgAtlas | comparison retained in the cited source sentence; not inferred | reported setting bound to the cited table row at the cited source locator | source-defined result measure | 42.9 | Paper-reported high-signal result sentence; citation years and numbered-object indices excluded. | private full-paper evidence dossier for arXiv:2606.25905, 4.2.2 SurgAtlas benchmarks. |

Bounded exact evidence retained from the paper report:

- Paper report, numeric result in Cross-regime training ablation.: “We isolate the contribution of each regime by training SurgAtlas…” (exact numeric tokens: 10, 4).

- No table-caption fragment was included in the bounded verbatim evidence budget.

The correct interpretation retains task, dataset, split, model, baseline, metric, budget, and hardware with each result. A largest reported improvement is an operating point, not a distribution. An average is not a tail guarantee. A component metric can diagnose mechanism without proving end-to-end utility. Where the source reports multiple tables or figures, their relationships should be checked for consistent defaults, denominators, and versioned settings.

Three types of gain remain separate. Representation gain means fewer tokens, bytes, channels, states, features, or bits. Execution gain means lower latency, memory traffic, transfer, energy, or higher throughput. Outcome gain means better correctness, quality, utility, constraint satisfaction, or task completion. The paper may establish one or more under its setting; a deployment decision requires the combination relevant to its service objective.

Table and figure captions were inventoried rather than republished. Their exact values remain anchored to the paper. Any public summary should cite only values whose numerator, denominator, model, dataset, and comparison are simultaneously known. This review does not manufacture missing uncertainty or turn qualitative illustrations into statistical evidence.

## 6. Ablations and Causal Evidence

Paper-specific ablation/control ledger:

| Component/control | Paper-reported delta | Control caveat | Source locator |
|---|---|---|---|
| Out-of-domain, open-only, and variant | direction or magnitude is reported only at the source locator | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation. |
| EgoSurgery-Phase, SurgAtlas-Open, and reaches | 62.5 | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2606.25905, Cross-regime training ablation. |
| Open, pattern, and observed | 8, 10, 10.3, +10.3, 12.6, +12.6, 5.1, 4.6, +4.6, 10.7, and +10.7 | This is a paper-reported ablation pointer; matched compute, retraining, interactions, and statistical uncertainty require direct audit. | private full-paper evidence dossier for arXiv:2606.25905, Fine-grained results. |

Ablations are persuasive when one named component changes while model, data, budget, training effort, and implementation quality stay fixed. The complete source was screened for removals, swaps, budget sweeps, sensitivity tests, and failure examples. If multiple elements change together, the result supports the bundle more strongly than any individual mechanism. If a simple cost-matched control is missing, the causal interpretation remains limited.

Randomness must be classified as training seeds, inference seeds, data-generation seeds, checkpoint-selection variance, or hyperparameter-search variance. Repeated inference does not prove training robustness. A named significance test should identify its independence unit and paired design. The practical importance of an effect is separate from statistical detectability, especially when a large benchmark makes very small changes significant.

Author-stated limitations:

- The author-side qualification at 5 Conclusion concerns surgical, videos, SurgAtlas, across, surgery, and pairs. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, 5 Conclusion)*

Reviewer-identified limitations:

- No independent reproduction was performed for arXiv:2606.25905v1; mathcal, text, surgical, and open remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, Surgical video datasets., and 3.2 Dataset Construction Pipeline)*
- The dossier inventories 42 headings, 6 tables, 8 figures, and 269 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2606.25905, complete coverage inventory)*

The explicit qualification path is anchored to the discussion, conclusion, appendix, and stated evidence boundary. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 3 candidate sentences and the limitation/discussion vocabulary surgical, videos, surgatlas, across, surgery, vqa, pairs, introduces, large-scale, video-language. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper frames SurgAtlas as a contribution to surgical, videos, video, language. | Problem framing is located in the profile's named introduction/problem headings; no numbered section marker is treated as a measurement. (private full-paper evidence dossier for arXiv:2606.25905, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| The reported mechanism centers on datasets, surgical, videos, hierarchical. | Method and formula evidence is bound to the named method headings and formula-specific operator audits. (private full-paper evidence dossier for arXiv:2606.25905, Surgical vision–language datasets and models.) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Table 3 reports measured outcomes for SurgAtlas-VLM (SurgAtlas) across Perception & ID / MIS / General-domain VLMs, Perception & ID / Open / General-domain VLMs, Action / state / MIS / General-domain VLMs, Action / state / Open / General-domain VLMs, Operative reas. / MIS / General-domain VLMs. | Quality-v2 paper-report result values: 10, 29.1, 32.2, 24.8, 20, 8 B, 47.8, 32 B, 13, 4 (private full-paper evidence dossier for arXiv:2606.25905, Surgical video datasets.) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2606.25905v1), [canonical PDF](https://arxiv.org/pdf/2606.25905v1), [canonical full-paper HTML](https://arxiv.org/html/2606.25905v1), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2606.25905). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2606.25905v1)*
- **Predecessor/prior work (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 1 Introduction; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2603.06570)*
- **Alternative or benchmark (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under Surgical video datasets.; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2401.00496)*
- **Code/data (bounded_not_found):** The bounded verified-URL receipt contains no official code/data artifact for this paper; no access error was recorded, so this is not labeled blocked. *(evidence locator: bounded online-vetting receipt for arXiv:2606.25905)*

Verified official primary-source links from the bounded check:

- Bounded primary-source check verified: https://dx.doi.org/10.1016/j.media.2025.103726
- Bounded primary-source check verified: https://dx.doi.org/10.1038/s41597-022-01719-2
- Bounded primary-source check verified: https://dx.doi.org/10.1038/s41597-024-03193-4

Access-blocked or unverified URL evidence: not recorded

Prior-work and alternatives evidence: "bounded_to_canonical_arxiv_record_and_paper_declared_primary_links" This is a bounded search record, not an exhaustive map of the field.

Code/data and reproduction evidence: "link_reachability_only; repository contents were not downloaded, built, or executed" Reachability and metadata do not mean that code or data were executed, that dependencies were installed, or that a reported result reproduced.

Paper-declared external candidates were recorded as follows:

- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/about/accessible_HTML.html
- Paper-declared URL, not opened in this phase: https://info.arxiv.org/help/license/index.html#licenses-available
- Paper-declared URL, not opened in this phase: https://www.ama-assn.org/practice-management/cpt
- Paper-declared URL, not opened in this phase: https://dx.doi.org/10.1016/j.media.2025.103726
- Paper-declared URL, not opened in this phase: https://dx.doi.org/10.1038/s41597-022-01719-2
- Paper-declared URL, not opened in this phase: https://dx.doi.org/10.1007/978-3-031-72089-5%5F18
- Paper-declared URL, not opened in this phase: https://dx.doi.org/10.1038/s41597-024-03193-4
- Paper-declared URL, not opened in this phase: https://dx.doi.org/10.1001/jamasurg.2023.6262
- Paper-declared URL, not opened in this phase: https://dx.doi.org/10.1007/978-3-031-72089-5%5F46
- Paper-declared URL, not opened in this phase: https://dx.doi.org/10.1007/s11548-024-03166-3
- Paper-declared URL, not opened in this phase: https://dx.doi.org/10.1145/3204949.3208127

Their presence is discovery evidence, not proof that an artifact is official, available, licensed, runnable, or reproducing the paper. A later online-vetting phase should use primary sources, record HTTP/access limits, verify ownership and linkage, inspect release and license state, and distinguish artifact availability from runnable or result-reproducing status. Until then the publication status remains: arXiv preprint; no separate peer-reviewed venue inferred without an official venue source.

The isolated Black Lake checkout was used only for repository-readiness and dedupe context. A same-paper DEP-A would block a new owning record; a DEP-E or directly corresponding implementation is associated context rather than a duplicate. Background citations do not transfer evidence or claims to this paper.[^association]

## 9. Independent Re-conceptualization

Reviewer inference: the durable mechanism is the source-defined change centered on datasets, surgical, videos, and hierarchical, rather than the paper's brand name. This interpretation predicts that a matched intervention on datasets changes mathcal; it is not an author claim or theorem.

Re-conceptualize the contribution as an evidence-linked state transition: pin source identity, record the method-specific decision, measure realized resource and outcome effects, and retain a conservative fallback whose trigger can be falsified on held-out conditions. This is reviewer inference and proposal, not an author claim and not an experimentally validated architecture.[^inference]

The mechanism can be viewed as a governed handoff between evidence, decision, execution, and outcome. Evidence identifies the source state and the signal the method uses. Decision records the action or representation chosen under a budget. Execution records what the system actually did, including fallback and resource use. Outcome records task quality and failure. The mapping is useful because it predicts what must be logged; it breaks when the paper studies a purely formal object with no operational transition.

A second bounded analogy is experimental portfolio control. Different baselines, budgets, and ablations are portfolio arms whose information access and cost must be matched. This analogy highlights selection bias and incomplete frontiers, but it does not imply that the paper uses an online bandit or that deployment should optimize only one scalar reward. Its falsifiable prediction is that the proposed mechanism's advantage should shrink when information access and complete cost are carefully matched if the original gain came mainly from comparison asymmetry.

## 10. Research Notes, Limitations, and Evidence Boundary

The complete local PDF and full-paper HTML for arXiv:2606.25905v1 were inspected. The PDF passed size, header, EOF, parse, page-count, title, structure, and references checks. The HTML passed size, readable-body, document-marker, heading, structure, title, and identity checks. Abstract HTML was metadata only and did not qualify as the paper body.[^integrity]

The coverage pass includes introduction, method or formal analysis, experiments or results, discussion or conclusion, references, appendices where exposed, tables, figures, equations, footnotes, disclosures, and code/data language. Extraction can lose visual layout and some mathematical semantics; the ledger records this boundary rather than claiming that every graphic was numerically reproduced.

Paper-specific qualification inventory: limitation/discussion terms surgical, videos, surgatlas, across, surgery, vqa, pairs, introduces, large-scale, video-language; disclosure/funding language limitations, limitation, Acknowledgments, Disclosure, Funding; code/data language Dataset, GitHub; appendix headings Appendix A Technical appendices and supplementary material. These are evidence pointers. A missing extracted term is not proof that a disclosure, artifact, or limitation does not exist.

Evidence layers remain explicit. Layer A is what the paper reports. Layer B contains the bounded primary records actually checked online; its conclusions are limited to the recorded identity, publication, and artifact-access evidence. Layer C is reviewer inference, including the governed-handoff interpretation. Layer D is a hypothesis or proposal, including deployment controls and falsification tests. A sentence is not silently promoted between layers.

Paper/prose/table consistency checks:

| Issue/check | Assessment | Source locator |
|---|---|---|
| Canonical ID, version, title, authors, PDF hash, and HTML hash were reconciled for arXiv:2606.25905v1; full quantitative table/prose/code consistency was not independently rerun. | identity consistency checked; quantitative and implementation consistency remain unresolved | source-integrity and online identity receipts for arXiv:2606.25905v1 |

Substantive evidence boundary: The profile binds arXiv:2606.25905v1 to a complete local PDF and full-paper HTML, 42 headings, 6 tables, 8 figures, and 269 extracted mathematical objects, and 5 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

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

### Hypothesis 1: Matched removal of datasets

**Proposition:** Reviewer hypothesis: the source-linked datasets operation is causally responsible for part of the reported mathcal behavior.
**Predicted observation:** Removing or neutralizing datasets under matched data and compute will measurably weaken mathcal.
**Falsifying observation:** A competent matched control without datasets preserves the same mathcal distribution within uncertainty.
**Minimum test:** Run a paired, seed-controlled ablation at Surgical video datasets. and archive per-instance outcomes and resource use.
**Evidence locator:** private full-paper evidence dossier for arXiv:2606.25905, Surgical vision–language datasets and models.

### Hypothesis 2: Boundary transfer for SurgAtlas

**Proposition:** Reviewer hypothesis: the relation between datasets, and surgical and mathcal, and text weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2606.25905, Surgical video datasets., and 3.2 Dataset Construction Pipeline

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for SurgAtlas** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2606.25905, Surgical video datasets., and 3.2 Dataset Construction Pipeline.
2. **Reproduce the end-to-end SurgAtlas path** Success: the source-defined datasets, surgical, and videos and mathcal, and text are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2606.25905, Surgical vision–language datasets and models..
3. **Falsify the reviewer mechanism thesis for datasets** Success: a matched intervention on datasets predicts a corresponding change in mathcal Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2606.25905, Surgical vision–language datasets and models..

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, SurgAtlas: A Large-Scale Surgical Video-Language Dataset with 2,391 Hours of Open and Minimally Invasive Surgery should be remembered as a tested relation between datasets, surgical, and videos and mathcal, text, and surgical under the configurations at Surgical video datasets., and 3.2 Dataset Construction Pipeline, not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The Table 1 caption centers on Table, Phase, action, recognition, benchmarks., Macro, across; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 1 with its spanning headers and caption under Phase and action recognition.; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.25905, Table 1 caption and object |
| Table 2 | Purpose: The Table 2 caption centers on Table, CholecT50, triplet, recognition, Endoscapes-CVS, criterion, accuracy.; its parsed headers include no explicit header text, across 0 rows and 0 cells.; result: no row with at least two measured cells survived the quality gate; caveat: Interpret Table 2 with its spanning headers and caption under Phase and action recognition.; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.25905, Table 2 caption and object |
| Table 3 | Purpose: The Table 3 caption centers on pairs, open, Table, results, expert-validated, subset, mathcal; its parsed headers include no explicit header text, across 11 rows and 113 cells.; result: column 2=34.0; column 3=36.5; column 4=39.9; column 5=32.5; column 6=49.2; column 7=51.2; column 8=38.7; column 9=34.8; column 10=45.1; column 11=67.2; column 12=39.2; column 13=37.6; caveat: Interpret Table 3 with its spanning headers and caption under Open versus minimally invasive surgery.; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.25905, Table 3 caption and object |
| Table 4 | Purpose: The Table 4 caption centers on partition, only, Table, Cross-regime, training, ablation., Accuracy; its parsed headers include no explicit header text, across 7 rows and 27 cells.; result: column 2=32.2; column 3=38.9; column 4=62.5; caveat: Interpret Table 4 with its spanning headers and caption under Cross-regime training ablation.; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.25905, Table 4 caption and object |
| Table 5 | Purpose: The Table 5 caption centers on Table, split, mathcal, text, reported, partition., results; its parsed headers include no explicit header text, across 19 rows and 146 cells.; result: column 2=39.5; column 3=35.4; column 4=24.0; column 5=24.8; column 6=28.0; column 7=25.9; column 8=49.8; column 9=48.0; column 10=45.9; column 11=47.2; caveat: Interpret Table 5 with its spanning headers and caption under Fine-grained results.; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.25905, Table 5 caption and object |
| Table 6 | Purpose: The Table 6 caption centers on partition., Table, results, expert-validated, subset, mathcal, text; its parsed headers include no explicit header text, across 19 rows and 196 cells.; result: column 2=36.5; column 3=36.9; column 4=34.5; column 5=35.9; column 6=29.7; column 7=28.9; column 8=26.5; column 9=18.5; column 10=33.0; column 11=20.0; column 12=46.0; column 13=47.7; column 14=45.5; column 15=47.2; caveat: Interpret Table 6 with its spanning headers and caption under Fine-grained results.; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.25905, Table 6 caption and object |
| Figure 1 | Purpose: The Figure 1 caption identifies a architecture or pipeline schematic centered on SurgAtlas., Figure, Visual, overview, Sampled, frames, organized, surgical.; result: The caption makes a qualitative claim about SurgAtlas., Figure, Visual, overview, Sampled, frames; no plotted value is inferred from pixels.; caveat: The caption under Abstract was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.25905, Figure 1 caption and object |
| Figure 2 | Purpose: The Figure 2 caption identifies a quantitative plot or comparison centered on surgical, restricted, Figure, Comparison, large-scale, video, datasets., Bubble.; result: Caption-reported measured values: 15, 291, 2, 391 hours; caveat: The caption under 2 Related Work was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.25905, Figure 2 caption and object |
| Figure 3 | Purpose: The Figure 3 caption identifies a architecture or pipeline schematic centered on text, alignment, Figure, Overview, SurgAtlas, construction, pipeline., YouTube.; result: Caption-reported measured values: 1, 18, 855, 15, 291, 9, 109, 6, 182, 2, 3, 4, 5, 6, 7; caveat: The caption under 3.2 Dataset Construction Pipeline was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.25905, Figure 3 caption and object |
| Figure 4 | Purpose: The Figure 4 caption identifies a paper-specific visual object centered on Macro, phase, action, benchmarks..; result: The caption makes a qualitative claim about Macro, phase, action, benchmarks.; no plotted value is inferred from pixels.; caveat: The caption under Phase and action recognition. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.25905, Figure 4 caption and object |
| Figure 5 | Purpose: The Figure 5 caption identifies a paper-specific visual object centered on Cholec80, detailed, metrics.; result: The caption makes a qualitative claim about Cholec80, detailed, metrics; no plotted value is inferred from pixels.; caveat: The caption under Phase and action recognition. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.25905, Figure 5 caption and object |
| Figure 6 | Purpose: The Figure 6 caption identifies a paper-specific visual object centered on CholecT50, Triplet.; result: The caption makes a qualitative claim about CholecT50, Triplet; no plotted value is inferred from pixels.; caveat: The caption under Phase and action recognition. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.25905, Figure 6 caption and object |
| Figure 7 | Purpose: The Figure 7 caption identifies a quantitative plot or comparison centered on Endoscapes-CVS, criterion, accuracy.; result: The caption makes a qualitative claim about Endoscapes-CVS, criterion, accuracy; no plotted value is inferred from pixels.; caveat: The caption under Phase and action recognition. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.25905, Figure 7 caption and object |
| Figure 4 | Purpose: The Figure 4 caption identifies a paper-specific visual object centered on specialties, total, open, surgery, Figure, Per-specialty, composition, SurgAtlas..; result: Caption-reported measured values: 18, 70; caveat: The caption under Specialty distribution. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.25905, Figure 4 caption and object |
| Equations | 269 distinct mathematical renderings exposed by HTML; representative objects listed in Section 2.2. | Central objects were inventoried with sign, normalization, conditioning, and denominator checks; no numerical reproduction. |
| Sections | 42 headings exposed by the full HTML. | Every heading was screened; method, evaluation, results, limitations, references, and appendices were mapped where present. |

Appendix and supplementary coverage:

- Appendix A Technical appendices and supplementary material

Complete section inventory:

- Report GitHub Issue
- SurgAtlas: A Large-Scale Surgical Video–Language Dataset with 2,391 Hours of Open and Minimally Invasive Surgery
- Abstract
- 1 Introduction
- 2 Related Work
- Surgical video datasets.
- Surgical vision–language datasets and models.
- 3 SurgAtlas Dataset
- 3.1 Overview
- 3.2 Dataset Construction Pipeline
- 3.2.1 Stage 1: Collection and Filtering
- 3.2.2 Stage 2: Tier Assignment
- 3.2.3 Stage 3: Multigranular Annotation Extraction
- 3.2.4 Stage 4: Procedure Window Extraction
- 3.2.5 Stage 5: Staged VQA Generation
- Pipeline.
- Question format.
- 3.2.6 Stage 6: Expert-Validated Evaluation Subset
- 3.2.7 Stage 7: Public Dataset Conversion
- 3.3 Dataset Analysis
- Scale.
- Diversity.
- Richness.
- Quality.
- 4 Experiments
- 4.1 SurgAtlas-VLM: Aligning Qwen3-VL with SurgAtlas
- Stage 1: Captioning pretraining.
- Stage 2: Instruction tuning.
- 4.2 Results
- 4.2.1 Standard Surgical Benchmarks
- Phase and action recognition.
- Triplet recognition and CVS assessment.
- 4.2.2 SurgAtlas benchmarks.
- Open versus minimally invasive surgery.
- 4.3 Ablation
- Cross-regime training ablation.
- 5 Conclusion
- Acknowledgments and Disclosure of Funding
- References
- Appendix A Technical appendices and supplementary material
- Specialty distribution.
- Fine-grained results.

This ledger is completeness evidence, not reproduction. It records that each exposed section and numbered object was screened without reproducing the paper's tables, figures, or long captions.

## 16. Source and Evidence Notes

- Canonical arXiv record: https://arxiv.org/abs/2606.25905v1
- Canonical PDF: https://arxiv.org/pdf/2606.25905v1
- Canonical full-paper HTML: https://arxiv.org/html/2606.25905v1
- arXiv DOI resolver: https://doi.org/10.48550/arXiv.2606.25905
- Reviewed identity: arXiv:2606.25905v1
- Complete authors: Filippos Bellos; Andre S. Gala-Garza; Miaowei Wang; Alyssa M. Hardin; Ahmad M. Hider; Yayuan Li; Jing Bi; Susan Liang; Chenliang Xu; Donald S. Likosky; Jason J. Corso
- Locally archived full PDF and full-paper HTML were verified; private path withheld.
- No source PDF, HTML, archive, extracted text, validator, or private index belongs in the public DEP-A package.
- Online primary-source vetting status: performed and receipt-linked; alternatives are not exhaustive and no experiment was independently reproduced.

## 17. Footnotes

[^source-paper]: Canonical paper identity and version are linked at https://arxiv.org/abs/2606.25905v1; the locally archived complete PDF and full-paper HTML were reconciled to this identity.
[^scope]: Paper report means content attributable to the authors and supported by the reviewed artifact; it is not independent reproduction.
[^integrity]: Source integrity requires a matching complete PDF and full-paper HTML with identity, version, title, structure, references, and readable-body checks.
[^inference]: Reviewer inference labels a mechanism-level interpretation derived from source evidence rather than asserted by the authors.
[^external]: External primary evidence was limited to receipt-linked official records and URLs. Availability or publication status does not imply artifact runnability, result reproduction, or exhaustive prior-work coverage.
[^association]: An associated DEP is contextual evidence, not a duplicate and not proof of the reviewed paper's claims.
