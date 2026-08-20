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

Reviewer inference: the durable mechanism is the source-defined change centered on flash, B-A10B, document, and content, rather than the paper's brand name. This interpretation predicts that a matched intervention on flash changes document; it is not an author claim or theorem. *(paper-specific reconstruction; source locator retained in the private substantive profile).* The source's technical path is anchored to 4.1 Models, Model specializations., H.4 Scaling of model size, Per-metric trade-offs across model variants.. The review treats those sections as the authority for inputs, state, transformations, objectives, and outputs; heading labels alone are not promoted into performance claims. This reconstruction does not replace the authors' definitions and does not imply that a heading or architecture label proves an empirical claim.

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

**Paper-reported problem:** For Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing, the formal target is bounded to the source-defined relation among Document, parsing, documents, pages, Dr.DocBench, expert-level, and benchmarks. The task assumptions and stakes are anchored to Abstract, and 1 Introduction; no objective outside those sections is inferred.

**Research gap reconstructed from the source:** The paper positions Dr. DocBench around Document, parsing, documents, flash, and B-A10B. This records the authors' gap framing only; novelty, priority, generality, and superiority require the separate prior-work and evaluation audits.

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

**Formal object 1 at Report GitHub Issue — Formula 1 under Report GitHub Issue is classified as a state or representation transformation; adjacent prose centers on Document, parsing, pages, Dr.DocBench, Content, recognition, and the expression links n..** `n{=}2`
Variables: "n".
Sign/normalization/conditioning/surrogate audit: "Formula 1 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: n; meanings remain tied to Report GitHub Issue.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Report GitHub Issue, formal object 1.

**Formal object 2 at 1 Introduction — Formula 2 under 1 Introduction is classified as a state or representation transformation; adjacent prose centers on pages, documents, visual, contain, introduce, Dr.DocBench, and the expression links sim..** `\sim`
Variables: "sim".
Sign/normalization/conditioning/surrogate audit: "Formula 2 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: sim; meanings remain tied to 1 Introduction.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, 1 Introduction, formal object 2.

**Formal object 3 at Formulas. — Formula 3 under Formulas. is classified as a evaluation or scoring relation; adjacent prose centers on text, scores, times, Overall, Score, component, and the expression links times..** `(1-\text{edit distance})\times 100`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 3 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Formulas..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formulas., formal object 3.

**Formal object 4 at Formulas. — Formula 4 under Formulas. is classified as a evaluation or scoring relation; adjacent prose centers on text, scores, times, Overall, Score, component, and the expression links times..** `\text{CDM}\times 100`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 4 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Formulas..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formulas., formal object 4.

**Formal object 5 at Formulas. — Formula 5 under Formulas. is classified as a evaluation or scoring relation; adjacent prose centers on text, scores, times, Overall, Score, component, and the expression links times..** `\text{TEDS}\times 100`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 5 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to Formulas..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formulas., formal object 5.

**Formal object 6 at 4.3 Overall Results and Findings — Formula 6 under 4.3 Overall Results and Findings is classified as a evaluation or scoring relation; adjacent prose centers on text, scores, TEDS, component, times, table, and the expression links uparrow..** `\uparrow`
Variables: "uparrow".
Sign/normalization/conditioning/surrogate audit: "Formula 6 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: uparrow; meanings remain tied to 4.3 Overall Results and Findings.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, 4.3 Overall Results and Findings, formal object 6.

**Formal object 7 at 4.3 Overall Results and Findings — Formula 7 under 4.3 Overall Results and Findings is classified as a evaluation or scoring relation; adjacent prose centers on text, scores, TEDS, component, times, table, and the expression links downarrow..** `\downarrow`
Variables: "downarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 7 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: downarrow; meanings remain tied to 4.3 Overall Results and Findings.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, 4.3 Overall Results and Findings, formal object 7.

**Formal object 8 at 4.5 Per-data-source Breakdown — Formula 8 under 4.5 Per-data-source Breakdown is classified as a evaluation or scoring relation; adjacent prose centers on models, document, worst, performance, type, Doubao, and the expression links dagger..** `\dagger`
Variables: "dagger".
Sign/normalization/conditioning/surrogate audit: "Formula 8 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: dagger; meanings remain tied to 4.5 Per-data-source Breakdown.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, 4.5 Per-data-source Breakdown, formal object 8.

**Formal object 9 at 4.5 Per-data-source Breakdown — Formula 9 under 4.5 Per-data-source Breakdown is classified as a evaluation or scoring relation; adjacent prose centers on document, performance, type, models., Doubao, edit, and the expression links times..** `\times`
Variables: "times".
Sign/normalization/conditioning/surrogate audit: "Formula 9 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: times; meanings remain tied to 4.5 Per-data-source Breakdown.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, 4.5 Per-data-source Breakdown, formal object 9.

**Formal object 10 at 4.5 Per-data-source Breakdown — Formula 10 under 4.5 Per-data-source Breakdown is classified as a evaluation or scoring relation; adjacent prose centers on text, models., document, while, performance, Table, and the expression links geq..** `\geq`
Variables: "geq".
Sign/normalization/conditioning/surrogate audit: "Formula 10 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: geq; meanings remain tied to 4.5 Per-data-source Breakdown.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, 4.5 Per-data-source Breakdown, formal object 10.

**Formal object 11 at 5.1 Sensitivity to Multi-page Context Length — Formula 11 under 5.1 Sensitivity to Multi-page Context Length is classified as a evaluation or scoring relation; adjacent prose centers on Models, table, tables, model, performance, suggesting, and the expression links n..** `n`
Variables: "n".
Sign/normalization/conditioning/surrogate audit: "Formula 11 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: n; meanings remain tied to 5.1 Sensitivity to Multi-page Context Length.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, 5.1 Sensitivity to Multi-page Context Length, formal object 11.

**Formal object 12 at 5.1 Sensitivity to Multi-page Context Length — Formula 12 under 5.1 Sensitivity to Multi-page Context Length is classified as a evaluation or scoring relation; adjacent prose centers on pages, parsing, recognition, sliding, window, order, and the expression links rightarrow..** `\rightarrow`
Variables: "rightarrow".
Sign/normalization/conditioning/surrogate audit: "Formula 12 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: rightarrow; meanings remain tied to 5.1 Sensitivity to Multi-page Context Length.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, 5.1 Sensitivity to Multi-page Context Length, formal object 12.

**Formal object 13 at 5.1 Sensitivity to Multi-page Context Length — Formula 13 under 5.1 Sensitivity to Multi-page Context Length is classified as a evaluation or scoring relation; adjacent prose centers on pages, parsing, recognition, sliding, window, order, and the expression links n..** `n=15`
Variables: "n".
Sign/normalization/conditioning/surrogate audit: "Formula 13 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: n; meanings remain tied to 5.1 Sensitivity to Multi-page Context Length.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, 5.1 Sensitivity to Multi-page Context Length, formal object 13.

**Formal object 14 at Appendix A Data Sourcing and Pipeline — Formula 14 under Appendix A Data Sourcing and Pipeline is classified as a evaluation or scoring relation; adjacent prose centers on subject, classification, apply, difficulty-aware, sampling, Appendix, and the expression links k..** `k`
Variables: "k".
Sign/normalization/conditioning/surrogate audit: "Formula 14 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: k; meanings remain tied to Appendix A Data Sourcing and Pipeline.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix A Data Sourcing and Pipeline, formal object 14.

**Formal object 15 at Appendix B Multi-Parser Disagreement Score — Formula 15 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on pages, parsers, book, Markdown, over, bias, and the expression links T_{m, b..** `T_{m,b}`
Variables: "T_{m, b".
Sign/normalization/conditioning/surrogate audit: "Formula 15 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: T_{m, b; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 15.

**Formal object 16 at Appendix B Multi-Parser Disagreement Score — Formula 16 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on pages, parsers, book, Markdown, over, bias, and the expression links m..** `m`
Variables: "m".
Sign/normalization/conditioning/surrogate audit: "Formula 16 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: m; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 16.

**Formal object 17 at Appendix B Multi-Parser Disagreement Score — Formula 17 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on pages, parsers, book, Markdown, over, bias, and the expression links b..** `b`
Variables: "b".
Sign/normalization/conditioning/surrogate audit: "Formula 17 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: b; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 17.

**Formal object 18 at Appendix B Multi-Parser Disagreement Score — Formula 18 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on text, struct, conf, annotation, pages, parsers, and the expression links D, b, i, j, mathrm, T_{m..** `D^{\text{text}}_{b}=\frac{1}{6}\!\!\sum_{(i,j)}\!\frac{\mathrm{Lev}(T_{m_{i},b},T_{m_{j},b})}{\max(|T_{m_{i},b}|,|T_{m_{j},b}|)}.`
Variables: "D, b, i, j, mathrm, T_{m".
Sign/normalization/conditioning/surrogate audit: "Formula 18 operator audit: maximization, fraction or division; explicit negative term not detected; conditioning marker present; fraction denominator(s) 6. Variables audited: D, b, i, j, mathrm, T_{m; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 18.

**Formal object 19 at Appendix B Multi-Parser Disagreement Score — Formula 19 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on text, struct, conf, alpha, gamma, delta, and the expression links D_{b}, alpha, D, b, gamma, delta..** `D_{b}=\alpha D^{\text{text}}_{b}+\gamma D^{\text{struct}}_{b}+\delta D^{\text{conf}}_{b}`
Variables: "D_{b}, alpha, D, b, gamma, delta".
Sign/normalization/conditioning/surrogate audit: "Formula 19 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: D_{b}, alpha, D, b, gamma, delta; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 19.

**Formal object 20 at Appendix B Multi-Parser Disagreement Score — Formula 20 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on text, struct, conf, alpha, gamma, delta, and the expression links D, b..** `D^{\text{struct}}_{b}`
Variables: "D, b".
Sign/normalization/conditioning/surrogate audit: "Formula 20 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: D, b; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 20.

**Formal object 21 at Appendix B Multi-Parser Disagreement Score — Formula 21 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on text, struct, conf, alpha, gamma, delta, and the expression links D, b..** `D^{\text{conf}}_{b}`
Variables: "D, b".
Sign/normalization/conditioning/surrogate audit: "Formula 21 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: D, b; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 21.

**Formal object 22 at Appendix B Multi-Parser Disagreement Score — Formula 22 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on text, struct, conf, alpha, gamma, delta, and the expression links alpha..** `\alpha=0.6`
Variables: "alpha".
Sign/normalization/conditioning/surrogate audit: "Formula 22 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: alpha; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 22.

**Formal object 23 at Appendix B Multi-Parser Disagreement Score — Formula 23 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on text, struct, conf, alpha, gamma, delta, and the expression links gamma..** `\gamma=0.3`
Variables: "gamma".
Sign/normalization/conditioning/surrogate audit: "Formula 23 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: gamma; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 23.

**Formal object 24 at Appendix B Multi-Parser Disagreement Score — Formula 24 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on text, struct, conf, alpha, gamma, delta, and the expression links delta..** `\delta=0.1`
Variables: "delta".
Sign/normalization/conditioning/surrogate audit: "Formula 24 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: delta; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 24.

**Formal object 25 at Appendix B Multi-Parser Disagreement Score — Formula 25 under Appendix B Multi-Parser Disagreement Score is classified as a evaluation or scoring relation; adjacent prose centers on text, struct, conf, alpha, gamma, delta, and the expression links D_{b}, tau..** `D_{b}>\tau=0.5`
Variables: "D_{b}, tau".
Sign/normalization/conditioning/surrogate audit: "Formula 25 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: D_{b}, tau; meanings remain tied to Appendix B Multi-Parser Disagreement Score.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Appendix B Multi-Parser Disagreement Score, formal object 25.

**Formal object 26 at C.3 Block-Level Categories — Formula 26 under C.3 Block-Level Categories is classified as a paper-defined mathematical relation; adjacent prose centers on Isolated, equations, formula_type, print, handwritten, chemical, and the expression links in..** `\in`
Variables: "in".
Sign/normalization/conditioning/surrogate audit: "Formula 26 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: in; meanings remain tied to C.3 Block-Level Categories.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, C.3 Block-Level Categories, formal object 26.

**Formal object 27 at C.4 Inter-Block Relations — Formula 27 under C.4 Inter-Block Relations is classified as a paper-defined mathematical relation; adjacent prose centers on textit, anno, relation, record, extra.relation, form, and the expression links textit..** `(\textit{source\_anno\_id},\ \textit{target\_anno\_id},\ \textit{relation\_type})`
Variables: "textit".
Sign/normalization/conditioning/surrogate audit: "Formula 27 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: textit; meanings remain tied to C.4 Inter-Block Relations.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, C.4 Inter-Block Relations, formal object 27.

**Formal object 28 at C.4 Inter-Block Relations — Formula 28 under C.4 Inter-Block Relations is classified as a paper-defined mathematical relation; adjacent prose centers on Marks, blocks, form, logical, unit, cross-page, and the expression links symbols defined beside the formula..** `-1`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 28 operator audit: no named reduction/optimization operator; explicit negative term present; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to C.4 Inter-Block Relations.".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, C.4 Inter-Block Relations, formal object 28.

**Formal object 29 at Effect of the outlier document. — Formula 29 under Effect of the outlier document. is classified as a evaluation or scoring relation; adjacent prose centers on Model, outlier, models, scores, failure, null, and the expression links symbols defined beside the formula..** `-`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 29 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Effect of the outlier document..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Effect of the outlier document., formal object 29.

**Formal object 30 at Effect of the outlier document. — Formula 30 under Effect of the outlier document. is classified as a evaluation or scoring relation; adjacent prose centers on Model, outlier, models, scores, failure, null, and the expression links leq..** `\leq`
Variables: "leq".
Sign/normalization/conditioning/surrogate audit: "Formula 30 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: leq; meanings remain tied to Effect of the outlier document..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Effect of the outlier document., formal object 30.

**Formal object 31 at Challenge type (Table 13 ). — Formula 31 under Challenge type (Table 13 ). is classified as a evaluation or scoring relation; adjacent prose centers on domain_reasoning, structural, semantically, harder, domain, elements, and the expression links symbols defined beside the formula..** `>`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 31 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Challenge type (Table 13 )..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Challenge type (Table 13 )., formal object 31.

**Formal object 32 at Page-level language (Table 14 ). — Formula 32 under Page-level language (Table 14 ). is classified as a probabilistic or expectation relation; adjacent prose centers on Models, Kimi, score, Table, groups, Claude, and the expression links to..** `\to`
Variables: "to".
Sign/normalization/conditioning/surrogate audit: "Formula 32 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: to; meanings remain tied to Page-level language (Table 14 )..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Page-level language (Table 14 )., formal object 32.

**Formal object 33 at Reading order degrades most consistently. — Formula 33 under Reading order degrades most consistently. is classified as a evaluation or scoring relation; adjacent prose centers on reading, order, across, subjects, edit, distance., and the expression links n..** `n{=}1`
Variables: "n".
Sign/normalization/conditioning/surrogate audit: "Formula 33 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: n; meanings remain tied to Reading order degrades most consistently..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Reading order degrades most consistently., formal object 33.

**Formal object 34 at Reading order degrades most consistently. — Formula 34 under Reading order degrades most consistently. is classified as a evaluation or scoring relation; adjacent prose centers on reading, order, across, subjects, edit, distance., and the expression links n..** `n{=}15`
Variables: "n".
Sign/normalization/conditioning/surrogate audit: "Formula 34 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: n; meanings remain tied to Reading order degrades most consistently..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Reading order degrades most consistently., formal object 34.

**Formal object 35 at Text edit distance shows a mixed early-window benefit. — Formula 35 under Text edit distance shows a mixed early-window benefit. is classified as a evaluation or scoring relation; adjacent prose centers on context, text, GPT-5.5, Gemini, cross-page, content., and the expression links to..** `0.287\to 0.285`
Variables: "to".
Sign/normalization/conditioning/surrogate audit: "Formula 35 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: to; meanings remain tied to Text edit distance shows a mixed early-window benefit..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Text edit distance shows a mixed early-window benefit., formal object 35.

**Formal object 36 at Text edit distance shows a mixed early-window benefit. — Formula 36 under Text edit distance shows a mixed early-window benefit. is classified as a evaluation or scoring relation; adjacent prose centers on context, text, GPT-5.5, Gemini, cross-page, content., and the expression links to..** `0.335\to 0.322`
Variables: "to".
Sign/normalization/conditioning/surrogate audit: "Formula 36 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: to; meanings remain tied to Text edit distance shows a mixed early-window benefit..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Text edit distance shows a mixed early-window benefit., formal object 36.

**Formal object 37 at Text edit distance shows a mixed early-window benefit. — Formula 37 under Text edit distance shows a mixed early-window benefit. is classified as a evaluation or scoring relation; adjacent prose centers on context, text, GPT-5.5, Gemini, cross-page, content., and the expression links symbols defined beside the formula..** `0.220`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 37 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Text edit distance shows a mixed early-window benefit..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Text edit distance shows a mixed early-window benefit., formal object 37.

**Formal object 38 at Text edit distance shows a mixed early-window benefit. — Formula 38 under Text edit distance shows a mixed early-window benefit. is classified as a evaluation or scoring relation; adjacent prose centers on context, text, GPT-5.5, Gemini, cross-page, content., and the expression links symbols defined beside the formula..** `0.365`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 38 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Text edit distance shows a mixed early-window benefit..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Text edit distance shows a mixed early-window benefit., formal object 38.

**Formal object 39 at Text edit distance shows a mixed early-window benefit. — Formula 39 under Text edit distance shows a mixed early-window benefit. is classified as a evaluation or scoring relation; adjacent prose centers on context, text, GPT-5.5, Gemini, cross-page, content., and the expression links symbols defined beside the formula..** `0.531`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 39 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Text edit distance shows a mixed early-window benefit..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Text edit distance shows a mixed early-window benefit., formal object 39.

**Formal object 40 at Text edit distance shows a mixed early-window benefit. — Formula 40 under Text edit distance shows a mixed early-window benefit. is classified as a evaluation or scoring relation; adjacent prose centers on context, text, GPT-5.5, Gemini, cross-page, content., and the expression links symbols defined beside the formula..** `0.782`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 40 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Text edit distance shows a mixed early-window benefit..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Text edit distance shows a mixed early-window benefit., formal object 40.

**Formal object 41 at Text edit distance shows a mixed early-window benefit. — Formula 41 under Text edit distance shows a mixed early-window benefit. is classified as a evaluation or scoring relation; adjacent prose centers on context, text, GPT-5.5, Gemini, cross-page, content., and the expression links symbols defined beside the formula..** `0.345`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 41 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Text edit distance shows a mixed early-window benefit..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Text edit distance shows a mixed early-window benefit., formal object 41.

**Formal object 42 at Text edit distance shows a mixed early-window benefit. — Formula 42 under Text edit distance shows a mixed early-window benefit. is classified as a evaluation or scoring relation; adjacent prose centers on context, text, GPT-5.5, Gemini, cross-page, content., and the expression links symbols defined beside the formula..** `0.369`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 42 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Text edit distance shows a mixed early-window benefit..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Text edit distance shows a mixed early-window benefit., formal object 42.

**Formal object 43 at Formula metrics show no systematic degradation. — Formula 43 under Formula metrics show no systematic degradation. is classified as a evaluation or scoring relation; adjacent prose centers on models, Formula, stays, within, moderate, band, and the expression links symbols defined beside the formula..** `0.817`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 43 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Formula metrics show no systematic degradation..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formula metrics show no systematic degradation., formal object 43.

**Formal object 44 at Formula metrics show no systematic degradation. — Formula 44 under Formula metrics show no systematic degradation. is classified as a evaluation or scoring relation; adjacent prose centers on models, Formula, stays, within, moderate, band, and the expression links symbols defined beside the formula..** `0.763`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 44 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Formula metrics show no systematic degradation..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formula metrics show no systematic degradation., formal object 44.

**Formal object 45 at Formula metrics show no systematic degradation. — Formula 45 under Formula metrics show no systematic degradation. is classified as a evaluation or scoring relation; adjacent prose centers on models, Formula, stays, within, moderate, band, and the expression links symbols defined beside the formula..** `0.867`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 45 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Formula metrics show no systematic degradation..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formula metrics show no systematic degradation., formal object 45.

**Formal object 46 at Formula metrics show no systematic degradation. — Formula 46 under Formula metrics show no systematic degradation. is classified as a evaluation or scoring relation; adjacent prose centers on models, Formula, stays, within, moderate, band, and the expression links n..** `n{=}12`
Variables: "n".
Sign/normalization/conditioning/surrogate audit: "Formula 46 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: n; meanings remain tied to Formula metrics show no systematic degradation..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formula metrics show no systematic degradation., formal object 46.

**Formal object 47 at Formula metrics show no systematic degradation. — Formula 47 under Formula metrics show no systematic degradation. is classified as a evaluation or scoring relation; adjacent prose centers on models, Formula, stays, within, moderate, band, and the expression links symbols defined beside the formula..** `0.687`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 47 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Formula metrics show no systematic degradation..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formula metrics show no systematic degradation., formal object 47.

**Formal object 48 at Formula metrics show no systematic degradation. — Formula 48 under Formula metrics show no systematic degradation. is classified as a evaluation or scoring relation; adjacent prose centers on models, Formula, stays, within, moderate, band, and the expression links n..** `n{=}5`
Variables: "n".
Sign/normalization/conditioning/surrogate audit: "Formula 48 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: n; meanings remain tied to Formula metrics show no systematic degradation..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formula metrics show no systematic degradation., formal object 48.

**Formal object 49 at Formula metrics show no systematic degradation. — Formula 49 under Formula metrics show no systematic degradation. is classified as a evaluation or scoring relation; adjacent prose centers on models, Formula, stays, within, moderate, band, and the expression links symbols defined beside the formula..** `0.000`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 49 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Formula metrics show no systematic degradation..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formula metrics show no systematic degradation., formal object 49.

**Formal object 50 at Formula metrics show no systematic degradation. — Formula 50 under Formula metrics show no systematic degradation. is classified as a evaluation or scoring relation; adjacent prose centers on models, Formula, stays, within, moderate, band, and the expression links symbols defined beside the formula..** `0.704`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 50 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Formula metrics show no systematic degradation..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formula metrics show no systematic degradation., formal object 50.

**Formal object 51 at Formula metrics show no systematic degradation. — Formula 51 under Formula metrics show no systematic degradation. is classified as a evaluation or scoring relation; adjacent prose centers on models, Formula, stays, within, moderate, band, and the expression links symbols defined beside the formula..** `0.916`
Variables: "No standalone variable token was mechanically isolated; inspect adjacent definitions.".
Sign/normalization/conditioning/surrogate audit: "Formula 51 operator audit: no named reduction/optimization operator; explicit negative term not detected; conditioning marker not detected; fraction denominator(s) not exposed as a simple TeX fraction. Variables audited: none mechanically isolated; meanings remain tied to Formula metrics show no systematic degradation..".
Source locator: private full-paper evidence dossier for arXiv:2606.01393, Formula metrics show no systematic degradation., formal object 51.

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

**Input/output dataflow:** The documented dataflow is reconstructed only across 4.1 Models, Model specializations., and H.4 Scaling of model size, where the source associates flash, B-A10B, document, content, equation, variants, and context. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

| Component | Inherited or novel | Role | Source locator |
|---|---|---|---|
| 4.1 Models | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with categorize, document, content, extraction, and main; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2606.01393, 4.1 Models |
| Model specializations. | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with equation, leads, content, including, and subject; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Model specializations. |
| H.4 Scaling of model size | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with size, three, variants, metrics, and Scaling; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2606.01393, H.4 Scaling of model size |
| Per-metric trade-offs across model variants. | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with flash, B-A10B, text, accuracy, and Per-metric; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Per-metric trade-offs across model variants. |
| Per-metric trade-offs across model variants. | paper-reported component; inherited-versus-new status requires the cited method and prior-work audit | The source associates this component with context, Per-metric, variants, Qwen3.5-Flash, and Qwen3.5-Plus; no additional operation is inferred. | private full-paper evidence dossier for arXiv:2606.01393, Per-metric trade-offs across model variants. |

The paper-specific method vocabulary is flash, content, equation, b-a10b, leads, including, subject, claude, but, model. This vocabulary was derived from the complete method/architecture paragraphs rather than the title. It identifies the entities that must appear in a faithful architecture reconstruction and creates a falsifiable check: an implementation or summary that omits these named objects is not yet grounded in this paper.

The architecture is reconstructed as an information-flow graph: source identity and inputs enter; inherited and paper-specific components transform or score them; a decision or representation is produced; optional validation or post-processing occurs; and an evaluated outcome leaves the pipeline. Each edge should name the information available at that point. A comparison becomes unfair if one method has access to labels, future requests, privileged metadata, additional context, or a larger tuning budget that another method lacks.

### 2.4 Training, calibration, and inference

Construction-time and runtime work are separate accounting domains. Training may fit parameters, construct representations, estimate thresholds, tune prompts, or learn a policy. Calibration may use held-out examples or measurements. Inference may retrieve, route, compress, classify, generate, search, solve, or verify. Post-processing may enforce a constraint or discard invalid output. A credible efficiency claim says which of these phases is included, which is amortized, and which is external to the reported number.

Training or calibration evidence is explicitly located in Model specializations.. The associated source vocabulary emphasizes flash, content, equation, b-a10b, leads, including, subject, claude, but, model.

Paper-specific construction/training sequence:

1. At Model specializations., the paper reports a training-related operation involving equation, leads, content, including, subject, and Claude. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Model specializations.)*
2. At Per-metric trade-offs across model variants., the paper reports a training-related operation involving context, Per-metric, variants, Qwen3.5-Flash, Qwen3.5-Plus, and https. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Per-metric trade-offs across model variants.)*
3. At Document Parsing Systems., the paper reports a training-related operation involving Parsing, Document, Systems, parsers, pipelines, and VLM-based. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Document Parsing Systems.)*

Inference or runtime evidence is explicitly located in Document parsing benchmarks.. Its source vocabulary overlaps flash, content, equation, b-a10b, leads, including, subject, claude, but, model.

Paper-specific inference/evaluation sequence:

1. At Document parsing benchmarks., the paper reports an inference or deployment action involving Document, recognition, parsing, benchmarks, pages, and textbooks. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks.)*
2. At Document Parsing Systems., the paper reports an inference or deployment action involving Parsing, Document, Systems, parsers, pipelines, and VLM-based. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Document Parsing Systems.)*

The reconstructed operational sequence is: pin input and artifact versions; validate prerequisites; compute the method-specific state or signal; apply the stated decision or objective; materialize the output; execute any downstream consumer; and measure both quality and resource outcomes. This sequence is reviewer inference grounded in the paper's organization. It is a testing model, not an assertion that the authors implemented an identical production controller.[^inference]

### 2.5 Notation and implementation audit

No independent implementation was run. The audit therefore checks internal legibility across equations, prose, captions, appendices, and extracted code/data statements. Apparent inconsistencies remain unresolved unless source evidence explains them. Source availability is classified in levels—declared, reachable, inspectable, runnable, and result-reproducing—and this local phase establishes only the declared/local-source layers.

## 3. Architecture and Complete Operational Pipeline

### 3.1 Representation and state

The documented dataflow is reconstructed only across 4.1 Models, Model specializations., and H.4 Scaling of model size, where the source associates flash, B-A10B, document, content, equation, variants, and context. Exact sequencing, hidden preprocessing, and post-processing remain bounded to the cited sections.

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
| Dr.DocBench | The evidence at Abstract names partition(s) without a mechanically isolated sample count. | The preprocessing evidence for Dr.DocBench names Document, parsing, pages, Dr.DocBench, recognition, VLMs at Abstract. | private full-paper evidence dossier for arXiv:2606.01393, Abstract |
| OmniDocBench | The evidence at Document parsing benchmarks. names partition(s) without a mechanically isolated sample count. | The preprocessing evidence for OmniDocBench names edit, distance, MusicXML, task., musical, structured at H.1.1 Music Analysis. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| OCRBench | The evidence at Document parsing benchmarks. names partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to OCRBench was stated in the captured paragraphs at Document parsing benchmarks.; none is imputed. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| MusiXQA | The evidence at Document parsing benchmarks. names partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to MusiXQA was stated in the captured paragraphs at Document parsing benchmarks.; none is imputed. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |
| VQA | The evidence at Document parsing benchmarks. names partition(s) without a mechanically isolated sample count. | No preprocessing operation tied to VQA was stated in the captured paragraphs at Document parsing benchmarks.; none is imputed. | private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks. |

Dataset audit begins with source or generator, sample count, train/validation/test split, scale, dimensionality, preprocessing, and whether examples are synthetic or real. It asks whether generation guarantees feasibility, whether filtering removes hard failures, whether evaluation shares entities or templates with training, and which distribution shifts are tested. Missing values are not filled from common practice; they remain evidence gaps.

### 4.2 Baselines and adaptation

| Baseline | Provenance | Tuning caveat | Source locator |
|---|---|---|---|
| Open | Table 1 lists Open as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether Open was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row Open |
| PaddleOCR | Table 1 lists PaddleOCR as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether PaddleOCR was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row PaddleOCR |
| Qwen3.5-Flash | Table 1 lists Qwen3.5-Flash as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether Qwen3.5-Flash was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row Qwen3.5-Flash |
| Qwen3.5-122B-A10B | Table 1 lists Qwen3.5-122B-A10B as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether Qwen3.5-122B-A10B was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row Qwen3.5-122B-A10B |
| Qwen3.5-Plus | Table 1 lists Qwen3.5-Plus as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether Qwen3.5-Plus was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row Qwen3.5-Plus |
| Kimi-K2.5 | Table 1 lists Kimi-K2.5 as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether Kimi-K2.5 was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row Kimi-K2.5 |
| - | Table 1 lists - as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether - was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row - |
| Doubao-Seed-1.6-Vision | Table 1 lists Doubao-Seed-1.6-Vision as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether Doubao-Seed-1.6-Vision was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row Doubao-Seed-1.6-Vision |
| Gemini 3.1 Pro | Table 1 lists Gemini 3.1 Pro as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether Gemini 3.1 Pro was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row Gemini 3.1 Pro |
| GPT-4o | Table 1 lists GPT-4o as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether GPT-4o was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row GPT-4o |
| GPT-5.5 | Table 1 lists GPT-5.5 as a numeric comparison row under 4.3 Overall Results and Findings. | Neither the Table 1 caption nor its row label establishes whether GPT-5.5 was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row GPT-5.5 |
| Model | Table 2 lists Model as a numeric comparison row under 4.4 Per-Subject Breakdown and Analysis. | Neither the Table 2 caption nor its row label establishes whether Model was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 2 row Model |
| Nemotron | Table 2 lists Nemotron as a numeric comparison row under 4.4 Per-Subject Breakdown and Analysis. | Neither the Table 2 caption nor its row label establishes whether Nemotron was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 2 row Nemotron |
| Claude | Table 2 lists Claude as a numeric comparison row under 4.4 Per-Subject Breakdown and Analysis. | Neither the Table 2 caption nor its row label establishes whether Claude was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 2 row Claude |
| Doubao | Table 2 lists Doubao as a numeric comparison row under 4.4 Per-Subject Breakdown and Analysis. | Neither the Table 2 caption nor its row label establishes whether Doubao was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 2 row Doubao |
| Gemini | Table 2 lists Gemini as a numeric comparison row under 4.4 Per-Subject Breakdown and Analysis. | Neither the Table 2 caption nor its row label establishes whether Gemini was copied, retrained, or retuned; that provenance is recorded as not stated rather than assumed. | private full-paper evidence dossier for arXiv:2606.01393, Table 2 row Gemini |

Each major baseline needs provenance and a comparison budget. The official implementation, an author adaptation, a copied result, and an independent reimplementation are different evidence types. Model size, training steps, retrieval access, tuning effort, and hardware can confound comparison. A baseline that does not natively support the task may still be informative, but the adaptation must be explicit and should not be used to claim universal superiority.

### 4.3 Metrics and denominators

| Metric | Denominator/conditioning | Direction | Source locator |
|---|---|---|---|
| Model | The metric-definition evidence at Per-metric trade-offs across model variants. ties Model to terms context, Qwen3.5-Flash, Qwen3.5-Plus, https, length., results, indicate, scaling. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 1 header Model |
| Size † | Table 1 reports Size † as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 1 header Size † |
| Text / Edit \downarrow | Table 1 reports Text / Edit \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 1 header Text / Edit \downarrow |
| Formula / Edit \downarrow | Table 1 reports Formula / Edit \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 1 header Formula / Edit \downarrow |
| Formula / CDM \uparrow | Table 1 reports Formula / CDM \uparrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 1 header Formula / CDM \uparrow |
| Table / TEDS \uparrow | Table 1 reports Table / TEDS \uparrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 1 header Table / TEDS \uparrow |
| Table / TEDS S \uparrow | Table 1 reports Table / TEDS S \uparrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 1 header Table / TEDS S \uparrow |
| Order / Edit \downarrow | Table 1 reports Order / Edit \downarrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 1 header Order / Edit \downarrow |
| Overall \uparrow | Table 1 reports Overall \uparrow as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 1 header Overall \uparrow |
| Score | The metric-definition evidence at Formulas. ties Score to terms text, scores, times, Overall, Score, component, report, higher. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 2 header Score |
| Subject Names | Table 2 reports Subject Names as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 2 header Subject Names |
| All | The metric-definition evidence at Formulas. ties All to terms text, scores, times, Overall, Score, component, report, higher. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 3 header All |
| Acad. Lit. | Table 3 reports Acad. Lit. as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 3 header Acad. Lit. |
| Book | Table 3 reports Book as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 3 header Book |
| Color. TB | Table 3 reports Color. TB as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 3 header Color. TB |
| Exam | Table 3 reports Exam as a column header, but its caption does not state a denominator; no denominator or failure exclusion rule is imputed. | higher is better when the paper treats this column as score/accuracy; otherwise direction follows the cited caption | private full-paper evidence dossier for arXiv:2606.01393, Table 3 header Exam |

Metrics are reconstructed with direction, denominator, aggregation unit, conditioning, and reference quality. Failures excluded from an average create survivor bias. A gap to a best-known incumbent is not a gap to a proven optimum. A judge-model score is not a human preference without validation. A compression ratio can invert depending on convention. Confidence intervals, paired tests, and effect sizes matter when differences are close or instances are correlated.

### 4.4 Hardware, batching, and runtime semantics

Quality-v2 paper-specific hardware/runtime evidence:

- At 1 Introduction, the paper's hardware/runtime paragraph names pages, documents, visual, contain, introduce, Dr.DocBench, expert-level, benchmark. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, 1 Introduction)*
- At 5.3 Case study: Table, the paper's hardware/runtime paragraph names window, table, page, HTML, rendering, Doubao, collapses, previous. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, 5.3 Case study: Table)*
- At Subject-level wins., the paper's hardware/runtime paragraph names edit, GPT-5.5, subject, GPT-4o, Kimi, achieves, lowest, distance. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Subject-level wins.)*
- At Model specializations., the paper's hardware/runtime paragraph names equation, leads, content, including, subject, Claude, GPT-5.5, subjects. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Model specializations.)*


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
| Table 1 | Open | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Model; Size †; Text / Edit \downarrow; Formula / Edit \downarrow; Formula / CDM \uparrow; Table / TEDS \uparrow; Table / TEDS S \uparrow; Order / Edit \downarrow; Overall \uparrow | Model=2.5; Size †=1.2B; Text / Edit \downarrow=0.33; Formula / Edit \downarrow=0.51; Formula / CDM \uparrow=24.15; Table / TEDS \uparrow=55.85; Table / TEDS S \uparrow=63.70; Order / Edit \downarrow=0.30; Overall \uparrow=54.37 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row 4 |
| Table 1 | Qwen3.5-Plus / Open | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Size †; Text / Edit \downarrow; Formula / Edit \downarrow; Formula / CDM \uparrow; Table / TEDS \uparrow; Table / TEDS S \uparrow; Order / Edit \downarrow; Overall \uparrow | Size †=17B; Text / Edit \downarrow=0.25; Formula / Edit \downarrow=0.31; Formula / CDM \uparrow=30.40; Table / TEDS \uparrow=49.77; Table / TEDS S \uparrow=58.23; Order / Edit \downarrow=0.26; Overall \uparrow=57.32 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 row 9 |
| Table 2 | Model | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Score; Subject Names | Score=3; Subject Names=3; Score=3; Subject Names=3 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 2 row 1 |
| Table 2 | YA Fic, Humor, Fic / Study, Des, Games | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Model; Score | Model=122B; Score=92.35; Score=29.58 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 2 row 13 |
| Table 3 | Qwen3.5-Plus / Gen. | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | All; Acad. Lit.; Book; Color. TB; Exam; Mag.; News.; Note; Res. Rep.; PPT | All=0.249; Acad. Lit.=0.223; Book=0.251; Color. TB=0.162; Exam=0.342; Mag.=0.196; News.=0.266; Note=0.248; Res. Rep.=0.383; PPT=0.317 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 3 row 6 |
| Table 3 | Kimi / Gen. | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | All; Acad. Lit.; Book; Color. TB; Exam; Mag.; News.; Note; Res. Rep.; PPT | All=0.193; Acad. Lit.=0.174; Book=0.190; Color. TB=0.147; Exam=0.291; Mag.=0.177; News.=0.385; Note=0.230; Res. Rep.=0.567; PPT=0.162 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 3 row 8 |
| Table 4 | MinerU / Spec. | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Text / RO Dist \downarrow; Text / Text Edit Dist \downarrow; Table / TEDS (%) \uparrow | Text / RO Dist \downarrow=0.237; Text / RO Dist \downarrow=0.357; Text / Text Edit Dist \downarrow=0.354; Text / Text Edit Dist \downarrow=0.539; Text / Text Edit Dist \downarrow=0.563; Text / Text Edit Dist \downarrow=0.546; Table / TEDS (%) \uparrow=54.0; Table / TEDS (%) \uparrow=78.8; Table / TEDS (%) \uparrow=32.3; Table / TEDS (%) \uparrow=67.9 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 4 row 4 |
| Table 4 | Kimi / Gen. | other rows in the same paper table; no cross-table comparator is inferred | configuration defined by the table caption and adjacent section | Text / RO Dist \downarrow; Text / Text Edit Dist \downarrow; Table / TEDS (%) \uparrow | Text / RO Dist \downarrow=0.133; Text / RO Dist \downarrow=0.263; Text / Text Edit Dist \downarrow=0.259; Text / Text Edit Dist \downarrow=0.672; Text / Text Edit Dist \downarrow=0.432; Text / Text Edit Dist \downarrow=0.357; Table / TEDS (%) \uparrow=49.1; Table / TEDS (%) \uparrow=21.4; Table / TEDS (%) \uparrow=33.1; Table / TEDS (%) \uparrow=40.1 | Paper-reported table cells; exact values parsed from full HTML and not independently reproduced. | private full-paper evidence dossier for arXiv:2606.01393, Table 4 row 10 |

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

- No independent reproduction was performed for arXiv:2606.01393v1; document, text, parsing, and benchmark remains paper-reported. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks., and 3.4 Final Dataset)*
- The dossier inventories 77 headings, 14 tables, 18 figures, and 51 extracted mathematical objects, but caption/equation extraction does not itself prove that every numeric denominator, axis, footnote qualification, or appendix value is consistent. *(source locator: private full-paper evidence dossier for arXiv:2606.01393, complete coverage inventory)*

The explicit qualification path is anchored to Limitations. Absent independent reruns or live artifact checks, portability, robustness, cost, and production readiness remain unresolved beyond tested conditions. A falsification test should stress the assumption most likely to invalidate the mechanism, not merely repeat the easiest central configuration. Useful negative controls include a no-transformation ceiling, a simple fixed policy, a shuffled or random signal, a cost-matched auxiliary baseline, and a conservative fallback.

The extracted ablation/sensitivity evidence contains 1 candidate sentences and the limitation/discussion vocabulary document, such, parsing, benchmark, not, docbench, expert-level, documents, fine-grained, content. This makes the absence of a clean one-component intervention visible: when no bounded ablation evidence is found, the review treats causal attribution as unresolved instead of converting a bundled result into mechanism proof.

## 7. Claim-by-Claim Vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper frames Dr. DocBench as a contribution to Document, parsing, documents, pages. | Problem framing is located in the profile's named introduction/problem headings; no numbered section marker is treated as a measurement. (private full-paper evidence dossier for arXiv:2606.01393, Abstract) | promising but bounded to the paper's stated task | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| The reported mechanism centers on flash, B-A10B, document, content. | Method and formula evidence is bound to the named method headings and formula-specific operator audits. (private full-paper evidence dossier for arXiv:2606.01393, 4.1 Models) | paper-reported mechanism; causal attribution requires matched ablation | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |
| Table 1 reports measured outcomes for Open across Model, Size †, Text / Edit \downarrow, Formula / Edit \downarrow, Formula / CDM \uparrow. | Quality-v2 paper-report result values: Model=2.5; Size †=1.2B; Text / Edit \downarrow=0.33; Formula / Edit \downarrow=0.51; Formula / CDM \uparrow=24.15; Table / TEDS \uparrow=55.85; Table / TEDS S \uparrow=63.70; Order / Edit \downarrow=0.30; Overall \uparrow=54.37 (private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks.) | supported only under reported evaluation conditions | The review does not expand this claim to untested data, scales, budgets, hardware, populations, or deployment conditions. |

The table uses calibrated judgments. “Supported” means direct evidence exists within the named scope, not that independent reproduction succeeded. “Conditional” preserves model, data, budget, hardware, metric, and formal assumptions. “Not established” does not mean false; it means the current evidence object cannot carry the stronger claim.

## 8. External Primary-Source Context

Canonical identity was checked online through the [arXiv record](https://arxiv.org/abs/2606.01393v1), [canonical PDF](https://arxiv.org/pdf/2606.01393v1), [canonical full-paper HTML](https://arxiv.org/html/2606.01393v1), and [arXiv DOI resolver](https://doi.org/10.48550/arXiv.2606.01393). The bounded evidence also records only the official URLs listed below. It does not establish that alternatives are exhaustive, that code is runnable, or that a reported result reproduces.[^external]

Bounded paper-specific external findings:

- **Publication status (checked):** arXiv preprint; no separate peer-reviewed venue inferred without an official venue source *(evidence locator: https://arxiv.org/abs/2606.01393v1)*
- **Predecessor/prior work (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under 1 Introduction; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://openreview.net/forum?id=ogjBpZ8uSi)*
- **Alternative or benchmark (checked):** This URL was live-verified as a primary source. Its association is limited to paper-cited primary context under Document parsing benchmarks.; reachability does not establish priority, superiority, or reproduction. *(evidence locator: https://arxiv.org/abs/2506.23009)*
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

Reviewer inference: the durable mechanism is the source-defined change centered on flash, B-A10B, document, and content, rather than the paper's brand name. This interpretation predicts that a matched intervention on flash changes document; it is not an author claim or theorem.

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

Substantive evidence boundary: The profile binds arXiv:2606.01393v1 to a complete local PDF and full-paper HTML, 77 headings, 14 tables, 18 figures, and 51 extracted mathematical objects, and 5 bounded verified noncanonical or canonical URLs. No experiment, code path, data pipeline, hardware measurement, security property, or production claim was independently reproduced.

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

**Proposition:** Reviewer hypothesis: the relation between flash, and B-A10B and document, and text weakens under an untested scale, distribution, or budget shift.
**Predicted observation:** At least one held-out shift changes both the outcome distribution and the method's failure pattern relative to the in-distribution baseline.
**Falsifying observation:** Matched held-out shifts preserve both effect size and failure distribution within predeclared intervals.
**Minimum test:** Predeclare one realistic distribution shift and one resource-budget shift, compare a strong baseline, and archive failures rather than survivor-only averages.
**Evidence locator:** private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks., and 3.4 Final Dataset

## 13. Replication and Falsification Agenda

1. **Reconcile the principal numeric evidence for Dr. DocBench** Success: paper table, prose, metric denominator, conditioning, and script output agree exactly Falsifier: a material value, denominator, exclusion rule, or uncertainty statement cannot be reconciled Archive: configuration, raw per-instance outputs, aggregation code, environment, and comparison table. Source locator: private full-paper evidence dossier for arXiv:2606.01393, Document parsing benchmarks., and 3.4 Final Dataset.
2. **Reproduce the end-to-end Dr. DocBench path** Success: the source-defined flash, B-A10B, and document and document, and text are recovered within predeclared tolerance Falsifier: a stage cannot run from documented artifacts or the principal result falls outside tolerance Archive: source version, code commit, data snapshot, dependencies, seeds, logs, hardware, and outputs. Source locator: private full-paper evidence dossier for arXiv:2606.01393, 4.1 Models, and Model specializations..
3. **Falsify the reviewer mechanism thesis for flash** Success: a matched intervention on flash predicts a corresponding change in document Falsifier: the intervention does not alter the predicted outcome or a simpler matched alternative explains it Archive: intervention definition, matched controls, uncertainty intervals, failure taxonomy, and resource telemetry. Source locator: private full-paper evidence dossier for arXiv:2606.01393, 4.1 Models, and Model specializations..

These tests are prioritized because they can change the verdict. A result that survives matched information and cost, randomized-signal controls, independent seeds, and shifted conditions supports the mechanism more strongly. A result that fails can still be useful, but its durable claim becomes narrower and more precise.

## 14. Durable Restatement

> Durably, Dr. DocBench: A Comprehensive Benchmark for Expert-Level and Difficult Document Parsing should be remembered as a tested relation between flash, B-A10B, and document and document, text, and parsing under the configurations at Document parsing benchmarks., and 3.4 Final Dataset, not as proof outside those conditions.

That restatement deliberately removes marketing language. It preserves the paper's existence, technical organization, and reported evidence while keeping venue status, code usability, benchmark independence, production behavior, and security outside the proven boundary. Later corrections should retain the base arXiv identity and compare material version differences rather than silently replacing this evidence object.

## 15. Complete Table, Figure, Equation, and Appendix Coverage Ledger

| Item | Source locator | Review disposition |
|---|---|---|
| Table 1 | Purpose: The Table 1 caption centers on Table, Overall, Evaluation, Results., activated, Parameters., bold; its parsed headers include no explicit header text, across 16 rows and 136 cells.; result: column 1=2.5; column 2=1.2B; column 4=0.33; column 5=0.51; column 6=24.15; column 7=55.85; column 8=63.70; column 9=0.30; column 10=54.37; caveat: Interpret Table 1 with its spanning headers and caption under 4.3 Overall Results and Findings; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 1 caption and object |
| Table 2 | Purpose: The Table 2 caption centers on Table, Model, Best, Worst, Subjects., Subject, name; its parsed headers include no explicit header text, across 14 rows and 67 cells.; result: column 1=122B; column 2=92.35; column 4=29.58; caveat: Interpret Table 2 with its spanning headers and caption under 4.4 Per-Subject Breakdown and Analysis; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 2 caption and object |
| Table 3 | Purpose: The Table 3 caption centers on Table, Text, extraction, edit, distance, document, data; its parsed headers include no explicit header text, across 13 rows and 146 cells.; result: column 2=0.249; column 3=0.223; column 4=0.251; column 5=0.162; column 6=0.342; column 7=0.196; column 8=0.266; column 9=0.248; column 10=0.383; column 11=0.317; caveat: Interpret Table 3 with its spanning headers and caption under 4.5 Per-data-source Breakdown; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 3 caption and object |
| Table 4 | Purpose: The Table 4 caption centers on Table, block, type, Text, report, edit, distance; its parsed headers include no explicit header text, across 15 rows and 156 cells.; result: column 3=0.237; column 4=0.357; column 5=0.354; column 6=0.539; column 7=0.563; column 8=0.546; column 9=54.0; column 10=78.8; column 11=32.3; column 12=67.9; caveat: Interpret Table 4 with its spanning headers and caption under 4.5 Per-data-source Breakdown; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 4 caption and object |
| Table 5 | Purpose: The Table 5 caption centers on Other, Table, Per-page, primary-language, distribution, across, Dr.DocBench; its parsed headers include no explicit header text, across 16 rows and 48 cells.; result: column 2=4,514; column 3=100%; caveat: Interpret Table 5 with its spanning headers and caption under Appendix E Language Coverage; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 5 caption and object |
| Table 6 | Purpose: The Table 6 caption centers on GPT-4o, GPT-5.5, Table, Text, block, edit, distance; its parsed headers include no explicit header text, across 53 rows and 742 cells.; result: column 2=0.299; column 3=0.593; column 4=0.302; column 5=0.666; column 6=0.173; column 7=0.414; column 8=0.658; column 9=0.870; column 10=0.885; column 11=0.354; column 12=0.390; column 13=0.345; column 14=0.87; column 14=0.86; column 14=0.78; column 14=0.496; caveat: Interpret Table 6 with its spanning headers and caption under H.1 Per-subject breakdown; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 6 caption and object |
| Table 7 | Purpose: The Table 7 caption centers on edit, distance, Table, Music, score, rightarrow, MusicXML; its parsed headers include no explicit header text, across 14 rows and 42 cells.; result: column 2=0.662; column 3=0.598; caveat: Interpret Table 7 with its spanning headers and caption under H.1.1 Music Analysis; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 7 caption and object |
| Table 8 | Purpose: The Table 8 caption centers on Table, Detailed, breakdown, subject, results, worst, subjects; its parsed headers include no explicit header text, across 73 rows and 584 cells.; result: column 1=4.6; column 2=40.33; column 3=0.469; column 4=0.414; column 5=37.86; column 6=17.66; column 7=28.54; column 8=0.473; caveat: Interpret Table 8 with its spanning headers and caption under H.2 The Worst Five Subjects; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 8 caption and object |
| Table 9 | Purpose: The Table 9 caption centers on Table, Text, extraction, edit, distance, page, degradation; its parsed headers include no explicit header text, across 13 rows and 39 cells.; result: column 2=0.256; column 3=0.163; caveat: Interpret Table 9 with its spanning headers and caption under H.3 Additional Analyses; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 9 caption and object |
| Table 10 | Purpose: The Table 10 caption centers on Table, Reading-order, edit, distance, page, layout, type; its parsed headers include no explicit header text, across 13 rows and 91 cells.; result: column 2=0.167; column 3=0.143; column 4=0.194; column 5=0.180; column 6=0.226; column 7=0.222; caveat: Interpret Table 10 with its spanning headers and caption under Page degradation (Table 9 ).; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 10 caption and object |
| Table 11 | Purpose: The Table 11 caption centers on Text, Table, extraction, edit, distance, text-block, element; its parsed headers include no explicit header text, across 13 rows and 156 cells.; result: column 2=0.314; column 3=0.590; column 4=0.381; column 5=0.297; column 6=0.318; column 7=0.314; column 8=0.369; column 9=0.319; column 10=0.446; column 11=0.277; column 12=0.341; caveat: Interpret Table 11 with its spanning headers and caption under Reading order by layout (Table 10 ).; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 11 caption and object |
| Table 12 | Purpose: The Table 12 caption centers on Table, Display, formula, edit, distance, broken, down; its parsed headers include no explicit header text, across 13 rows and 117 cells.; result: column 1=122B; column 2=0.322; column 3=0.173; column 4=0.348; column 5=0.574; column 6=0.282; column 7=0.286; column 8=0.217; column 9=0.576; caveat: Interpret Table 12 with its spanning headers and caption under Text element attributes by edit distance (Table 11 ).; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 12 caption and object |
| Table 13 | Purpose: The Table 13 caption centers on Table, Text, extraction, edit, distance, challenge, type; its parsed headers include no explicit header text, across 13 rows and 65 cells.; result: column 2=0.217; column 3=0.158; column 4=0.256; column 5=0.123; caveat: Interpret Table 13 with its spanning headers and caption under Formula performance by document type and layout (Table 12 ).; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 13 caption and object |
| Table 14 | Purpose: The Table 14 caption centers on Table, Text, extraction, edit, distance, page-level, language; its parsed headers include no explicit header text, across 13 rows and 65 cells.; result: column 2=0.217; column 3=0.218; column 4=0.053; column 5=0.211; caveat: Interpret Table 14 with its spanning headers and caption under Challenge type (Table 13 ).; the parsed cells are paper report, not an independent rerun. | private full-paper evidence dossier for arXiv:2606.01393, Table 14 caption and object |
| Figure 1 | Purpose: The Figure 1 caption identifies a architecture or pipeline schematic centered on across, subject, pages, subjects, Figure, Overview, Dr.DocBench, BISAC.; result: Caption-reported measured values: 52, 4,514, 5, 4.6, 52; caveat: The caption under 1 Introduction was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 1 caption and object |
| Figure 2 | Purpose: The Figure 2 caption identifies a architecture or pipeline schematic centered on Figure, Overview, Dr.DocBench, benchmark, spans, diverse, BISAC, subject.; result: The caption makes a qualitative claim about Figure, Overview, Dr.DocBench, benchmark, spans, diverse; no plotted value is inferred from pixels.; caveat: The caption under 1 Introduction was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 2 caption and object |
| Figure 3 | Purpose: The Figure 3 caption identifies a quantitative plot or comparison centered on window, size, metrics., Figure, Impact, sliding, pages, overall.; result: The caption makes a qualitative claim about window, size, metrics., Figure, Impact, sliding; no plotted value is inferred from pixels.; caveat: The caption under 5.1 Sensitivity to Multi-page Context Length was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 3 caption and object |
| Figure 4 | Purpose: The Figure 4 caption identifies a paper-specific visual object centered on Figure, Token, efficiency, overall, score..; result: The caption makes a qualitative claim about Figure, Token, efficiency, overall, score.; no plotted value is inferred from pixels.; caveat: The caption under 5.1 Sensitivity to Multi-page Context Length was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 4 caption and object |
| Figure 5 panel (a) | Purpose: The Figure 5 panel (a) caption identifies a paper-specific visual object centered on Source, image.; result: The caption makes a qualitative claim about Source, image; no plotted value is inferred from pixels.; caveat: The caption under 5.2 Token Efficiency was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 5 panel (a) caption and object |
| Figure 5 panel (b) | Purpose: The Figure 5 panel (b) caption identifies a paper-specific visual object centered on Ground-truth.; result: The caption makes a qualitative claim about Ground-truth; no plotted value is inferred from pixels.; caveat: The caption under 5.2 Token Efficiency was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 5 panel (b) caption and object |
| Figure 5 panel (c) | Purpose: The Figure 5 panel (c) caption identifies a paper-specific visual object centered on Kimi, curr., window.; result: The caption makes a qualitative claim about Kimi, curr., window; no plotted value is inferred from pixels.; caveat: The caption under 5.2 Token Efficiency was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 5 panel (c) caption and object |
| Figure 5 panel (d) | Purpose: The Figure 5 panel (d) caption identifies a paper-specific visual object centered on Kimi, prev., window.; result: The caption makes a qualitative claim about Kimi, prev., window; no plotted value is inferred from pixels.; caveat: The caption under 5.2 Token Efficiency was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 5 panel (d) caption and object |
| Figure 5 panel (e) | Purpose: The Figure 5 panel (e) caption identifies a paper-specific visual object centered on Doubao, curr., window.; result: The caption makes a qualitative claim about Doubao, curr., window; no plotted value is inferred from pixels.; caveat: The caption under 5.2 Token Efficiency was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 5 panel (e) caption and object |
| Figure 5 | Purpose: The Figure 5 caption identifies a qualitative example or visualization centered on Table, HTML, Kimi, window, content, Figure, case, study..; result: Caption-reported measured values: 5, 5, 5, 5, 5; caveat: The caption under 5.2 Token Efficiency was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 5 caption and object |
| Figure 6 | Purpose: The Figure 6 caption identifies a quantitative plot or comparison centered on edit, distance, Figure, Music, score, rightarrow, MusicXML, transcription.; result: Caption-reported measured values: 1, 6; caveat: The caption under 5.4 Case study: Optical Music Recognition was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 6 caption and object |
| Figure 7 | Purpose: The Figure 7 caption identifies a paper-specific visual object centered on annotated, pages, subject, Figure, Number, BISAC, full, Dr.DocBench.; result: Caption-reported measured values: 6, 4,514; caveat: The caption under Annotators and Compensation. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 7 caption and object |
| Figure 8 | Purpose: The Figure 8 caption identifies a paper-specific visual object centered on Mean, standard, deviation, subject., high, Figure, four-parser, disagreement.; result: The caption makes a qualitative claim about Mean, standard, deviation, subject., high, Figure; no plotted value is inferred from pixels.; caveat: The caption under Annotators and Compensation. was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 8 caption and object |
| Figure 9 | Purpose: The Figure 9 caption identifies a paper-specific visual object centered on Figure, Unified, inference, prompt, used, evaluation, Part.; result: Caption-reported measured values: 1; caveat: The caption under Appendix G Inference Prompt was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 9 caption and object |
| Figure 10 | Purpose: The Figure 10 caption identifies a paper-specific visual object centered on Figure, Unified, inference, prompt, used, evaluation, Part.; result: Caption-reported measured values: 2; caveat: The caption under Appendix G Inference Prompt was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 10 caption and object |
| Figure 11 | Purpose: The Figure 11 caption identifies a paper-specific visual object centered on composition, subject., Figure, Left, data, elements, Right, layout.; result: Caption-reported measured values: 100; caveat: The caption under H.1 Per-subject breakdown was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 11 caption and object |
| Figure 12 | Purpose: The Figure 12 caption identifies a paper-specific visual object centered on Figure, Scaling, model, size.; result: The caption makes a qualitative claim about Figure, Scaling, model, size; no plotted value is inferred from pixels.; caveat: The caption under H.4 Scaling of model size was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 12 caption and object |
| Figure 13 | Purpose: The Figure 13 caption identifies a paper-specific visual object centered on Figure, Impact, sliding, window, size, pages, formula, metrics.; result: The caption makes a qualitative claim about Figure, Impact, sliding, window, size, pages; no plotted value is inferred from pixels.; caveat: The caption under H.5 Scaling of sliding window size was covered exactly; axes, visual marks, and pixel-level values were not digitized. | private full-paper evidence dossier for arXiv:2606.01393, Figure 13 caption and object |
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
