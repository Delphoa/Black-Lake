# Abstract-State Safety Analysis for AI-CPS

## A complete-paper review and independent re-conceptualization of Mosaic

**Source paper:** Xuan Xie, Jiayang Song, Zhehua Zhou, Fuyuan Zhang, and Lei Ma, arXiv:2305.03882v1.[^paper]
**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260709-Mosaic Safety`[^dep]
**Source commit:** `a1ffd4737ce95c14f3a15251ee4fbba4403108a5`
**Paired task indicator:** `BL-DEPPAIR-20260714-97E22888`
**Direction:** `DEP-E -> DEP-A`
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file DEP-E review plus complete authorized primary-paper inspection
**Reproduction boundary:** paper and repository record inspected; no code was executed, no experiment was rerun, and no result was independently reproduced
**One-way provenance:** review-only; source DEP modified: no; files moved: no; files copied: no; new derived DEP-A data generated: yes

---

## Executive assessment

Mosaic learns a compact Markov decision process from AI-controlled cyber-physical traces, then uses probabilistic model checking both to switch controllers online and to guide falsification offline. Its durable contribution is the separation of learned behavior, explicit monitor state, query, intervention, and retained evidence.

The paper-level narrative is sufficiently complete to reconstruct the mechanism, evaluation, reported results, qualifications, and open replication work. The source record is also internally consistent with the primary paper. The major archival risk is not missing description; it is claim inflation. Source-reported metrics are observations within the authors' protocol, not universal performance facts. This review therefore separates paper-reported claims, directly inspected evidence, reviewer inference, and hypotheses.

The bottom-line judgment is constructive. The work has a legible causal story, a meaningful evaluation surface, and a reusable design pattern. Its evidence supports the mechanism under the studied conditions. It does not establish production safety, broad domain transfer, or independent reproducibility. Those boundaries are preserved rather than treated as deficiencies to be silently repaired.

## 1. Problem framing and research question

Learning-based controllers can improve control objectives while making behavior harder to explain and less amenable to conventional safety analysis. Mosaic asks whether simulation traces can support an abstract behavioral model useful for both runtime monitoring and counterexample search.

The question is important because the system under study sits between an underlying process and an operational decision. A useful method must do more than improve one average: it must define what information is represented, how that representation is trained or constructed, what decisions consume it, and where error can propagate. The review uses that chain as its organizing unit.

The source DEP-E is the archival object, while the complete paper is direct primary evidence for paper-level statements. The DEP-E's earlier synthesis is not treated as an independent replication. Where the two agree, confidence increases that the record faithfully represents the source; it does not convert author results into independently verified facts.

## 2. Source identity, integrity, and complete inventory

The repository record contains exactly `README.md` and its named manuscript. Both were read from beginning to end. The README supplies public context, inventory, insights, and a final attribution block. The manuscript supplies metadata, evidence ledger, detailed summary, claims, methods, constraints, observations, implementations, reading, references, and run notes.

The canonical record identifies **Mosaic: Model-based Safety Analysis Framework for AI-enabled Cyber-Physical Systems**, by Xuan Xie, Jiayang Song, Zhehua Zhou, Fuyuan Zhang, and Lei Ma, as arXiv:2305.03882v1. The complete authorized article was inspected at https://arxiv.org/pdf/2305.03882. The persistent identifier is https://doi.org/10.48550/arXiv.2305.03882.[^doi]

The complete 11-page paper, its algorithms, result tables, workflow and monitor/falsification figures, threats to validity, related work, and conclusion were directly inspected. The repository README and manuscript were also read completely.

No source document was uploaded or copied into this DEP-A. The public files are a new review and a new manifest. This protects both the one-way classification relationship and the ability to audit which language originated in this intake.

## 3. Technical reconstruction of the method

The paper frames the AI-CPS as a Moore machine whose outputs are robustness values for safety specifications. It abstracts sampled behavior into an MDP with state, action, transition, and label abstractions. Where robustness variance makes an abstract state too coarse, a refinement step uses an SVM boundary. Online monitoring poses a bounded-reachability PCTL query and switches to a traditional controller when estimated risk crosses a threshold. Offline falsification seeds candidates globally, queries the abstract model, and applies local optimization to promising regions.

The method can be analyzed as a five-stage information path:

1. **Observation:** raw or simulated information is collected under a defined protocol.
2. **Representation:** the method converts observations into an internal state or embedding.
3. **Objective:** training or optimization makes that representation useful for a target.
4. **Decision:** a downstream decoder, monitor, classifier, or generator produces an outcome.
5. **Evidence:** evaluation compares the outcome with baselines and retains traces needed to interpret failure.

This decomposition exposes the main causal dependencies. A reported gain can arise from the representation, data, objective, baseline configuration, or evaluation metric. The paper's own design and ablations provide partial separation; the replication agenda below adds the missing controls.

### 3.1 Assumptions

The method assumes that training or sampled evidence covers the structures needed at evaluation; that chosen metrics are meaningful proxies; that preprocessing does not introduce untracked advantages; and that baseline implementations are adequate. These assumptions are normal for empirical work, but they should be explicit because each defines a failure mode.

### 3.2 Reproducibility-relevant details

A reproduction needs immutable source version, dataset identity and split, preprocessing, random seeds, model or controller initialization, optimization settings, stopping rules, hardware/software versions where relevant, and exact metric implementations. The paper provides many conceptual and numerical details; missing executable artifacts remain a boundary rather than an invitation to guess.

## 4. Experimental design and evidence reconstructed

Three simulated systems are used: adaptive cruise control, abstract fuel control, and an exothermic chemical reactor. Nine AI controllers span DNN and reinforcement-learning variants. The paper reports 20,000 traces for each abstract model, 1,000 random traces for labeling precision, 100 signals for monitor evaluation, and 30 trials per falsification approach. PRISM performs probabilistic model checking; MATLAB/Simulink supplies plants; Breach is a falsification baseline.

The design is broad enough to test the central proposal, but not broad enough to support unconstrained transfer. Dataset or simulator coverage, baseline selection, evaluation sample size, and metric choice define the claim domain. The absence of a real-world deployment or independently rerun artifact is material when operational language is considered.

A sound reading asks four questions for every reported comparison: Was the information budget matched? Was the tuning budget matched? Were preprocessing and evaluation identical? Was uncertainty measured? The paper answers these to different degrees. Where uncertainty is not reported, point estimates should not be interpreted as stable rankings.

## 5. Results and quantitative audit

The authors report 92.22% average abstract-model labeling preciseness. They report that Mosaic has the best falsification performance in 13 of 16 problems and is strictly better in nine. Average safety-query time is 0.1032 seconds versus 35.7501 seconds average simulation time. Online switching improves safety and performance in several settings, but abstract-fuel-control cases show the danger of a weaker fallback controller.

These are paper-reported claims directly observed in the complete article. They were transcribed and checked for direction, but not recomputed. A quantitative result is strongest when denominator, sample construction, baseline, and metric direction are all visible. It becomes weaker when transported to a different device, domain, data distribution, or operational threshold.

The review does not average unlike metrics or turn multiple tables into one synthetic score. A method can improve one structural metric while trading another quality dimension. Such tradeoffs are scientifically useful because they reveal the objective surface. The archival artifact retains them rather than selecting only favorable values.

### 5.1 Statistical and operational limits

Point estimates do not expose variance across training, sampling, or initialization unless the paper reports it. Operational readiness would additionally require latency distribution, memory, energy, failure recovery, calibration, and out-of-distribution monitoring appropriate to the domain. None is inferred from an average simulation or benchmark result.

### 5.2 Negative and mixed evidence

Mixed outcomes are part of the contribution. They indicate where the proposed causal story is incomplete, where a baseline has an advantage, or where a design choice optimizes one metric at the expense of another. This review uses those cases to design falsification tests rather than dismiss them as noise.

## 6. Ablations and causal evidence

The Mosaic-rand variant removes model-checking-informed queueing and therefore acts as the most direct mechanism ablation. Random search and Breach provide additional comparisons. The evidence supports the value of guided prioritization in many tested settings, but not universal dominance. Missing ablations include model-refinement alternatives, query-threshold sweeps, state-feature sensitivity, and matched fallback quality.

An ablation supports a causal claim only when the comparison changes the intended component and holds material alternatives fixed. Training budget, parameter count, preprocessing, data, and evaluation should remain matched. When they do not, the result can still be informative but is associative rather than isolating.

A stronger follow-on should also evaluate interaction effects. Components that look weak alone may be necessary in combination; components that help one metric may harm another. Multiple seeds and uncertainty intervals are essential when optimization or sampling is stochastic.

## 7. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper addresses a real representation-to-decision problem. | Problem statement, method, and evaluation in the complete article. | Strongly supported. | Importance does not establish the proposed solution's universality. |
| The proposed mechanism is implemented as described. | Equations, algorithms, architecture, and experiment setup. | Supported as a paper report. | Code execution was not independently inspected here. |
| Reported metrics improve under the tested protocol. | Primary result tables and accompanying text. | Supported for the stated comparisons. | Not independently reproduced; uncertainty and portability vary. |
| Ablations support the named components. | Component and design comparisons in the complete article. | Partially to strongly supported depending on control quality. | Interactions and matched-budget checks remain important. |
| The result generalizes to production. | No direct deployment evidence in this intake. | Not established. | Requires target-domain, operational, and governance evidence. |
| The DEP-E faithfully identifies the work. | Complete repository inventory compared with canonical record. | Supported. | Earlier generated synthesis is not independent validation. |
| The DEP-A transfers or supersedes the DEP-E. | One-way pair metadata and new authorship. | False. | Review-only; no source file moved, copied, or modified. |

## 8. External primary-source context

The canonical paper and DOI anchor title, authorship, version, and public source. The complete article supplies direct evidence for methods and reported experiments.[^paper] Related DEP entries in the source manuscript are contextual only; they do not validate this paper's results.

The work should be situated by mechanism rather than by a broad label. Its novelty lies in the particular representation, objective, or decision linkage reconstructed above. Neighboring methods may pursue the same outcome with different information assumptions. A fair future comparison should disclose those assumptions instead of treating every baseline as interchangeable.

External pages, repositories, and papers were treated as evidence only. None was followed as an instruction, and none expanded the authorized mutation scope.

## 9. Code and reproducibility status

No experiment or code path was run. The paper's source availability and any locator mentioned by the DEP-E are evidence about access, not execution. Reproducibility status is therefore **source-inspected, not reproduced**.

A durable reproduction package would include:

- canonical code commit and license;
- environment and dependency lock;
- data manifest, licensing, split hashes, and preprocessing;
- full configuration, seeds, and hardware details;
- machine-readable result tables and expected tolerances;
- negative cases, timeouts, and known unsupported configurations;
- a narrative explaining deviations from the article.

Without this package, the right archival statement is not “irreproducible”; it is “reproduction remains open.”

## 10. Independent re-conceptualization

Mosaic is best understood as an evidence compiler. Continuous trajectories are compressed into reviewable state; a formal query translates state into a risk signal; policy converts risk into intervention; and the ledger preserves what happened. This pattern can transfer to other agentic systems only at the level of architecture, not by carrying over the paper's thresholds or safety guarantees.

This framing is deliberately independent of the paper's marketing language. It asks what state exists, who or what consumes it, what evidence can falsify the claimed benefit, and which assumptions break the analogy. The re-conceptualization is a reviewer proposal, not an author claim.

A useful boundary follows: transferring an architectural pattern does not transfer thresholds, safety guarantees, learned parameters, or empirical rankings. Every new domain needs its own data, failure taxonomy, baseline, and governance.

## 11. Research notes and caveats

### 1. Critical note

Fallback quality is part of the safety case; switching cannot be assumed safer merely because the alternate controller is traditional. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 2. Critical note

An abstract model can make behavior inspectable while still omitting rare states and distribution shift. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 3. Critical note

The reported query overhead is relative to simulation and cannot be generalized to a real-time plant without end-to-end timing. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 4. Critical note

Falsification finds counterexamples; it does not prove safety when none are found. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 5. Critical note

The draft source contains placeholder conference metadata, so bibliographic claims should rely on the canonical arXiv record. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.


These notes reduce overclaiming while preserving the work's value. A whitepaper-grade archive should make it easy for a future reviewer to see both why a mechanism matters and what would invalidate it.

## 12. Implications

1. **Preserve state, query, action, fallback, and outcome as separate fields in safety ledgers.** This implication concerns evidence and system design; it is not a claim of reproduced capability.
2. **Require fallback-controller evaluation before enabling automated switching.** This implication concerns evidence and system design; it is not a claim of reproduced capability.
3. **Use model-guided search to prioritize authorized simulation tests, while preserving unguided baselines.** This implication concerns evidence and system design; it is not a claim of reproduced capability.
4. **Treat formal queries as versioned policy artifacts with owners and review history.** This implication concerns evidence and system design; it is not a claim of reproduced capability.

The research implication is to move from headline metrics toward mechanism-specific evidence. The operational implication is to retain enough state and provenance to diagnose failures. The archival implication is to bind every restatement to source version and reproduction status.

## 13. Falsifiable hypotheses

### Hypothesis 1

**Proposition:** Monitor benefit will correlate more strongly with fallback quality than with abstract-model precision once precision passes a minimum threshold.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.

### Hypothesis 2

**Proposition:** Uncertainty-aware states will reduce unsafe false negatives compared with deterministic labels at the same state budget.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.

### Hypothesis 3

**Proposition:** Guided falsification advantage will shrink when unsafe regions are broad and increase when they are narrow but structurally connected.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.

### Hypothesis 4

**Proposition:** A provenance-complete monitor ledger will reduce review time without increasing false assurance.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.


## 14. Replication and falsification agenda

1. Rebuild one benchmark with fixed versions of MATLAB/Simulink, PRISM, Breach, controller checkpoints, seeds, and safety specifications.
2. Recompute the labeling-precision table and publish confusion by abstract state rather than only the average.
3. Sweep query horizon and probability threshold while measuring false alarms, missed violations, performance, and switching latency.
4. Evaluate fallback-only, AI-only, and switched systems under identical disturbances.
5. Repeat falsification trials with preregistered budgets and confidence intervals; retain failures and timeouts.

Execution should proceed from the smallest discriminating test to broader comparison. The objective is not to reproduce only the best number; it is to determine which mechanism, assumption, and failure boundary create the observed result.

A credible report should label exact reproduction, approximate reproduction, extension, and failed attempt separately. Failed reproduction does not automatically refute a paper, but unexplained divergence is evidence that configuration or hidden dependencies matter.

## 15. Durable restatement

### Review protocol and decision rule

The archival decision follows a conservative rule. A statement enters the durable restatement only when its mechanism is visible in the complete paper, its evidence type is named, and its scope can be expressed without borrowing confidence from an uninspected artifact. Numerical rankings remain paper-reported claims even when the table was directly read.[^claims] Reviewer proposals are allowed only when they include a falsifier or a concrete replication step. This prevents an attractive interpretation from becoming indistinguishable from an observed result.

The same rule applies to repository provenance. The paired task indicator binds this newly generated artifact to one source path and one immutable source state.[^pair] It does not declare ownership of the source, move a document, or collapse the DEP-E and DEP-A classes. A later correction should create another pair tied to the changed source commit so that readers can compare states without overwriting the earlier review.

For future use, the most important acceptance test is explanatory: a reviewer should be able to identify the input evidence, the transformation or decision mechanism, the metric, the strongest counterexample, and the reproduction gap without consulting private run data. If any of those elements is missing, the artifact can still guide discovery, but it should not be used to justify a high-consequence decision. This standard keeps the review useful when software, datasets, and benchmark rankings age.


> Mosaic shows that learned controller behavior can be converted into an explicit probabilistic state model that supports monitoring and test prioritization. The reported simulations are promising, but safety depends on abstraction coverage, query choice, fallback competence, and reproduction.

This is the claim that should survive metric drift and ecosystem change. It preserves the mechanism and evidence limit without freezing a provisional ranking into an archival fact.

## Appendix A. Coverage ledger

| Paper or DEP element | Coverage | Assessment |
|---|---|---|
| DEP-E README | Read completely; inventory, context, links, and attribution checked. | Direct repository evidence. |
| DEP-E manuscript | Read completely; every section and source role accounted for. | Generated source report, not independent replication. |
| Title, authors, version, DOI | Checked against canonical record. | High-confidence identity. |
| Abstract and introduction | Reconstructed in problem framing. | Direct primary evidence. |
| Related work | Used to bound novelty and comparison class. | Context, not validation. |
| Method, equations, and algorithms | Reconstructed by information flow and assumptions. | Direct primary evidence; not executed. |
| Tables and quantitative results | Major values and tradeoffs audited. | Paper-reported claims. |
| Figures | Roles and qualitative claims accounted for. | Visual evidence not independently measured. |
| Ablations | Component and design evidence evaluated. | Causal strength depends on controls. |
| Limitations and threats | Integrated into notes and evidence boundary. | Direct and reviewer-added qualifications. |
| Conclusion and future work | Compared with durable restatement and agenda. | No stronger claim imported. |
| References | Read as the paper's context map. | Background works not re-reviewed by default. |

## Appendix B. Source and evidence notes

### Primary sources

- Canonical record: https://arxiv.org/abs/2305.03882
- Complete authorized paper: https://arxiv.org/pdf/2305.03882
- Persistent identifier: https://doi.org/10.48550/arXiv.2305.03882
- Immutable DEP-E record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-Mosaic%20Safety

### Evidence boundary

The complete paper and complete selected DEP-E record were directly inspected. Paper-reported claims are labeled as such. Reviewer inference appears in assessment, re-conceptualization, implications, caveats, and hypotheses. No result was independently reproduced.[^boundary]

### Provenance facts

- Source action: review-only.
- Source DEP modified: no.
- Files moved: no.
- Existing files copied into DEP-A: no.
- New derived data generated: yes.
- Intake and deposition become complete only with validation and repository submission.

## Footnotes

[^paper]: Canonical record and complete paper: https://arxiv.org/abs/2305.03882 and https://arxiv.org/pdf/2305.03882
[^dep]: Immutable source record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-Mosaic%20Safety
[^doi]: Persistent identifier: https://doi.org/10.48550/arXiv.2305.03882
[^boundary]: Reproduction boundary: no code was executed and no reported result was independently reproduced.
[^claims]: Paper-reported claims were checked against the complete primary article but were not recomputed.
[^pair]: Paired task indicator `BL-DEPPAIR-20260714-97E22888` records the one-way `DEP-E -> DEP-A` relationship.
