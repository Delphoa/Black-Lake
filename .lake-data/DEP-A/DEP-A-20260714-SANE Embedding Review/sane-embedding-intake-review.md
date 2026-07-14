# Locality-Guided Attributed Network Embedding

## A complete-paper review and independent re-conceptualization of SANE

**Source paper:** Weiyi Liu, Zhining Liu, Toyotaro Suzumura, and Guangmin Hu, arXiv:1804.07152v2.[^paper]
**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260709-SANE Embeddings`[^dep]
**Source commit:** `a1ffd4737ce95c14f3a15251ee4fbba4403108a5`
**Paired task indicator:** `BL-DEPPAIR-20260714-FB034839`
**Direction:** `DEP-E -> DEP-A`
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file DEP-E review plus complete authorized primary-paper inspection
**Reproduction boundary:** paper and repository record inspected; no code was executed, no experiment was rerun, and no result was independently reproduced
**One-way provenance:** review-only; source DEP modified: no; files moved: no; files copied: no; new derived DEP-A data generated: yes

---

## Executive assessment

SANE aligns local attribute-neighborhood reconstruction with topology embeddings so a node representation reflects both what a node is and how it is connected, while avoiding the global eigendecompositions that constrained earlier attributed-network methods.

The paper-level narrative is sufficiently complete to reconstruct the mechanism, evaluation, reported results, qualifications, and open replication work. The source record is also internally consistent with the primary paper. The major archival risk is not missing description; it is claim inflation. Source-reported metrics are observations within the authors' protocol, not universal performance facts. This review therefore separates paper-reported claims, directly inspected evidence, reviewer inference, and hypotheses.

The bottom-line judgment is constructive. The work has a legible causal story, a meaningful evaluation surface, and a reusable design pattern. Its evidence supports the mechanism under the studied conditions. It does not establish production safety, broad domain transfer, or independent reproducibility. Those boundaries are preserved rather than treated as deficiencies to be silently repaired.

## 1. Problem framing and research question

Topology-only embeddings can ignore descriptive attributes, while attribute-only representations ignore relational structure. Earlier joint methods often manipulate global matrices. SANE asks whether local neighborhoods and stochastic optimization can recover useful joint embeddings with better scaling.

The question is important because the system under study sits between an underlying process and an operational decision. A useful method must do more than improve one average: it must define what information is represented, how that representation is trained or constructed, what decisions consume it, and where error can propagate. The review uses that chain as its organizing unit.

The source DEP-E is the archival object, while the complete paper is direct primary evidence for paper-level statements. The DEP-E's earlier synthesis is not treated as an independent replication. Where the two agree, confidence increases that the record faithfully represents the source; it does not convert author results into independently verified facts.

## 2. Source identity, integrity, and complete inventory

The repository record contains exactly `README.md` and its named manuscript. Both were read from beginning to end. The README supplies public context, inventory, insights, and a final attribution block. The manuscript supplies metadata, evidence ledger, detailed summary, claims, methods, constraints, observations, implementations, reading, references, and run notes.

The canonical record identifies **Scalable attribute-aware network embedding with locality**, by Weiyi Liu, Zhining Liu, Toyotaro Suzumura, and Guangmin Hu, as arXiv:1804.07152v2. The complete authorized article was inspected at https://arxiv.org/pdf/1804.07152. The persistent identifier is https://doi.org/10.48550/arXiv.1804.07152.[^doi]

The complete nine-page paper, equations, algorithm sketch, dataset and result tables, parameter-sensitivity and scalability figures, conclusion, future work, and references were directly inspected. Both DEP-E files were read completely.

No source document was uploaded or copied into this DEP-A. The public files are a new review and a new manifest. This protects both the one-way classification relationship and the ability to audit which language originated in this intake.

## 3. Technical reconstruction of the method

SANE uses node2vec-style topology contexts and locally linear embedding in attribute space. Each node is reconstructed from its K nearest attribute neighbors, yielding local weights. The optimization encourages topology embeddings to preserve those local attribute relationships. Negative sampling and stochastic updates replace global eigendecomposition. The learned vector is therefore a negotiated representation between explicit links and attribute-local structure.

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

The paper evaluates node classification on Cora, BlogCatalog, Flickr, and PPI using logistic regression and five-fold cross-validation with 80% training labels per fold. It compares LLE, node2vec, LANE, AANE, and MultiView. The joint dimension is reported as 96. Scalability is studied on synthetic Barabasi-Albert graphs up to 100,000 nodes.

The design is broad enough to test the central proposal, but not broad enough to support unconstrained transfer. Dataset or simulator coverage, baseline selection, evaluation sample size, and metric choice define the claim domain. The absence of a real-world deployment or independently rerun artifact is material when operational language is considered.

A sound reading asks four questions for every reported comparison: Was the information budget matched? Was the tuning budget matched? Were preprocessing and evaluation identical? Was uncertainty measured? The paper answers these to different degrees. Where uncertainty is not reported, point estimates should not be interpreted as stable rankings.

## 5. Results and quantitative audit

Reported F1 values are 0.83 on Cora, 0.91 on BlogCatalog, 0.72 on Flickr, and 0.77 on PPI. The paper reports gains over node2vec of 5.1%, 40%, 71.4%, and 11.6%, respectively. It reports roughly linear scaling and about ten seconds for the C++ joint-representation step at 100,000 nodes, with roughly twenty minutes total processing dominated by preprocessing.

These are paper-reported claims directly observed in the complete article. They were transcribed and checked for direction, but not recomputed. A quantitative result is strongest when denominator, sample construction, baseline, and metric direction are all visible. It becomes weaker when transported to a different device, domain, data distribution, or operational threshold.

The review does not average unlike metrics or turn multiple tables into one synthetic score. A method can improve one structural metric while trading another quality dimension. Such tradeoffs are scientifically useful because they reveal the objective surface. The archival artifact retains them rather than selecting only favorable values.

### 5.1 Statistical and operational limits

Point estimates do not expose variance across training, sampling, or initialization unless the paper reports it. Operational readiness would additionally require latency distribution, memory, energy, failure recovery, calibration, and out-of-distribution monitoring appropriate to the domain. None is inferred from an average simulation or benchmark result.

### 5.2 Negative and mixed evidence

Mixed outcomes are part of the contribution. They indicate where the proposed causal story is incomplete, where a baseline has an advantage, or where a design choice optimizes one metric at the expense of another. This review uses those cases to design falsification tests rather than dismiss them as noise.

## 6. Ablations and causal evidence

Parameter sensitivity covers embedding dimension, alignment strength, and K. Dataset-dependent optima show that the joint objective is not self-tuning. The paper's baseline comparison also isolates topology-only and attribute-only views, but it does not provide a modern component ablation with matched compute, multiple graph seeds, or contemporary GNN baselines.

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

For archival systems, SANE is better treated as a relation-proposal mechanism than an authority. Explicit citation edges, shared identifiers, and reviewer judgments should remain separate from embedding-near proposals. A useful source graph can combine topology and attributes while requiring provenance evidence before an inferred edge becomes public fact.

This framing is deliberately independent of the paper's marketing language. It asks what state exists, who or what consumes it, what evidence can falsify the claimed benefit, and which assumptions break the analogy. The re-conceptualization is a reviewer proposal, not an author claim.

A useful boundary follows: transferring an architectural pattern does not transfer thresholds, safety guarantees, learned parameters, or empirical rankings. Every new domain needs its own data, failure taxonomy, baseline, and governance.

## 11. Research notes and caveats

### 1. Critical note

The 2018 baseline set does not establish present-day state of the art against modern graph neural networks or graph transformers. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 2. Critical note

Flickr results show that joint alignment is not uniformly best, making dataset structure and tuning material. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 3. Critical note

Label information used by LANE complicates direct comparison because it receives extra supervision. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 4. Critical note

The code was described as available by contacting authors; no runnable official repository was validated in this intake. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.

### 5. Critical note

Locality improves computational tractability but may miss long-range dependencies important to source graphs. This is material because it changes either causal interpretation, portability, or the maximum safe claim. The note is a reviewer assessment, not a statement that the authors ignored the issue entirely.


These notes reduce overclaiming while preserving the work's value. A whitepaper-grade archive should make it easy for a future reviewer to see both why a mechanism matters and what would invalidate it.

## 12. Implications

1. **Store explicit and inferred graph edges as different types with different evidence requirements.** This implication concerns evidence and system design; it is not a claim of reproduced capability.
2. **Use embedding locality to rank review candidates, never as a citation substitute.** This implication concerns evidence and system design; it is not a claim of reproduced capability.
3. **Audit disagreement among topology, attributes, embeddings, and reviewer-approved relations.** This implication concerns evidence and system design; it is not a claim of reproduced capability.
4. **Benchmark incremental updates because archival graphs evolve continuously.** This implication concerns evidence and system design; it is not a claim of reproduced capability.

The research implication is to move from headline metrics toward mechanism-specific evidence. The operational implication is to retain enough state and provenance to diagnose failures. The archival implication is to bind every restatement to source version and reproduction status.

## 13. Falsifiable hypotheses

### Hypothesis 1

**Proposition:** Selective alignment will outperform uniform alignment when attribute and topology neighborhoods disagree.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.

### Hypothesis 2

**Proposition:** Provenance-gated edge admission will reduce false related-entry links with only a modest recall loss.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.

### Hypothesis 3

**Proposition:** Incremental local updates will approximate full recomputation when new nodes affect bounded neighborhoods.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.

### Hypothesis 4

**Proposition:** Modern graph baselines will reduce SANE's classification advantage while preserving its interpretability and scaling value.

**Prediction:** a controlled study varying the named factor while holding data, compute, and scoring fixed will produce a directional difference.

**Falsifier:** the difference vanishes across representative seeds and fixtures, or a simpler confound fully explains it.

**Minimum test:** preregister the comparison, preserve configuration and negative cases, and report uncertainty rather than a single best run.


## 14. Replication and falsification agenda

1. Recover exact datasets, preprocessing, splits, and reference implementation or reconstruct them from the paper.
2. Repeat classification with fixed and published folds, multiple random seeds, and confidence intervals.
3. Match embedding dimension and tuning budget across SANE, node2vec, attribute-only, and modern GNN baselines.
4. Reproduce the 100,000-node timing with preprocessing and memory separately reported.
5. Inject controlled topology and attribute noise to measure when alignment helps or harms.

Execution should proceed from the smallest discriminating test to broader comparison. The objective is not to reproduce only the best number; it is to determine which mechanism, assumption, and failure boundary create the observed result.

A credible report should label exact reproduction, approximate reproduction, extension, and failed attempt separately. Failed reproduction does not automatically refute a paper, but unexplained divergence is evidence that configuration or hidden dependencies matter.

## 15. Durable restatement

### Review protocol and decision rule

The archival decision follows a conservative rule. A statement enters the durable restatement only when its mechanism is visible in the complete paper, its evidence type is named, and its scope can be expressed without borrowing confidence from an uninspected artifact. Numerical rankings remain paper-reported claims even when the table was directly read.[^claims] Reviewer proposals are allowed only when they include a falsifier or a concrete replication step. This prevents an attractive interpretation from becoming indistinguishable from an observed result.

The same rule applies to repository provenance. The paired task indicator binds this newly generated artifact to one source path and one immutable source state.[^pair] It does not declare ownership of the source, move a document, or collapse the DEP-E and DEP-A classes. A later correction should create another pair tied to the changed source commit so that readers can compare states without overwriting the earlier review.

For future use, the most important acceptance test is explanatory: a reviewer should be able to identify the input evidence, the transformation or decision mechanism, the metric, the strongest counterexample, and the reproduction gap without consulting private run data. If any of those elements is missing, the artifact can still guide discovery, but it should not be used to justify a high-consequence decision. This standard keeps the review useful when software, datasets, and benchmark rankings age.


> SANE's lasting idea is that scalable joint representation can be built from local agreements between graph structure and attributes. For provenance-sensitive archives, those agreements should propose relationships, while explicit evidence decides which relationships become authoritative.

This is the claim that should survive metric drift and ecosystem change. It preserves the mechanism and evidence limit without freezing a provisional ranking into an archival fact. It also keeps proposing a graph relationship separate from admitting that relationship as evidence-backed archival knowledge. That distinction remains important even when a newer embedding method replaces SANE.

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

- Canonical record: https://arxiv.org/abs/1804.07152v2
- Complete authorized paper: https://arxiv.org/pdf/1804.07152
- Persistent identifier: https://doi.org/10.48550/arXiv.1804.07152
- Immutable DEP-E record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-SANE%20Embeddings

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

[^paper]: Canonical record and complete paper: https://arxiv.org/abs/1804.07152v2 and https://arxiv.org/pdf/1804.07152
[^dep]: Immutable source record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-SANE%20Embeddings
[^doi]: Persistent identifier: https://doi.org/10.48550/arXiv.1804.07152
[^boundary]: Reproduction boundary: no code was executed and no reported result was independently reproduced.
[^claims]: Paper-reported claims were checked against the complete primary article but were not recomputed.
[^pair]: Paired task indicator `BL-DEPPAIR-20260714-FB034839` records the one-way `DEP-E -> DEP-A` relationship.
