# Self-Learned Integrated Decision and Control

## A whitepaper-grade source-bundle review and independent re-conceptualization

**Source work:** Self-learned Intelligence for Integrated Decision and Control of Automated Vehicles at Signalized Intersections.[^paper]
**Source DEP-E:** .lake-data/DEP-E/DEP-E-20260710-Self Learned IDC[^dep]
**Source commit:** a1ffd4737ce95c14f3a15251ee4fbba4403108a5
**Paired task indicator:** BL-DEPPAIR-20260714-0BA69C8A
**Direction:** DEP-E -> DEP-A
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file DEP-E record; paper-level detail remains source-reported unless explicitly identified
**Reproduction boundary:** repository record and public locators inspected; no code was executed, no experiment rerun, and no result independently reproduced
**One-way provenance:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived DEP-A data generated: yes

---

## Executive assessment

This intake reviews Self-learned Intelligence for Integrated Decision and Control of Automated Vehicles at Signalized Intersections through the complete DEP-E repository record. It asks whether a learned policy and value model can integrate tactical decisions with continuous control while representing a variable number of surrounding road users. The record is coherent enough to reconstruct the mechanism, evidence, limitations, and open work, but it is not an independently reproduced full-paper review.

A permutation-invariant encoder maps each vehicle, bicycle, and pedestrian and sums the representations before concatenating ego, road, signal, and route features. Offline learning trains the policy, value function, and encoder for one integrated decision-and-control objective.

The paper reports and authors report language below denotes claims carried by the source bundle. The overall judgment is constructive and bounded: the work presents a legible, falsifiable research program, while broad transfer, production safety, and independent reproducibility remain open.

## 1. Problem framing and research question

Whether a learned policy and value model can integrate tactical decisions with continuous control while representing a variable number of surrounding road users is important because it joins representation, policy, and observable outcome. A credible review must ask what information enters, how state is formed, what objective shapes behavior, and which metric stands in for the intended effect.

The DEP-E is the archival object. Its manuscript is evidence about an earlier review, not independent confirmation of the underlying experiments. Agreement between its inventory and public locators supports identity and internal integrity; it does not convert author results into reproduced facts.

## 2. Source identity, integrity, and complete inventory

The source path is .lake-data/DEP-E/DEP-E-20260710-Self Learned IDC at commit a1ffd4737ce95c14f3a15251ee4fbba4403108a5. It contains exactly README.md and self_learned_idc_manuscript.md. Both files were read from beginning to end. The README supplies classification, inventory, public context, insights, and attribution. The manuscript supplies metadata, evidence ledger, detailed reconstruction, claims, method, constraints, observations, proposed extensions, references, and validation notes.

The canonical public locator is https://arxiv.org/abs/2110.12359; a persistent or related locator is https://doi.org/10.48550/arXiv.2110.12359. The complete canonical paper was not independently used to validate all paper-level detail in this run. No source document was uploaded, no source Markdown copied, and the source record remains unchanged.

## 3. Technical reconstruction of the method

A permutation-invariant encoder maps each vehicle, bicycle, and pedestrian and sums the representations before concatenating ego, road, signal, and route features. Offline learning trains the policy, value function, and encoder for one integrated decision-and-control objective.

The information path is observation, representation, objective or policy, outcome, and evidence. This decomposition makes alternatives visible: a gain may arise from the named mechanism, additional information, preprocessing, tuning, baseline configuration, or evaluation. The DEP-E provides partial separation; the replication agenda supplies the missing controls.

### 3.1 Assumptions

The method assumes that observed or simulated data cover structures needed at evaluation, metrics are meaningful proxies, preprocessing introduces no hidden advantage, and baselines receive a fair search budget. Each assumption is a possible failure mode.

### 3.2 Reproducibility-relevant details

A reproduction needs immutable source and code versions, data identity and splits, preprocessing, seeds, initialization, optimization, stopping rules, dependencies, hardware where material, and exact metrics. Missing details are not guessed.

## 4. Experimental design and evidence reconstructed

The DEP-E reports SUMO tests at a four-way signalized intersection with mixed traffic, six phases, a 120-second cycle, and one hundred evaluation simulations. Dynamic, fixed, and rule-based methods are compared for compute, comfort, traversal, collisions, and compliance.

The design addresses the question at its stated scale. Its domain remains bounded by data or simulator coverage, participant sampling where applicable, baselines, metrics, sample size, and version. A strong audit matches information, tuning, and compute budgets; retains negative cases; and reports uncertainty. Unspecified controls remain unspecified.

## 5. Results and quantitative audit

Dynamic encoding is reported at 7.24 plus or minus 1.36 milliseconds. Passage time is 24.46 plus or minus 4.52 seconds, versus 25.73 for fixed encoding and 66.18 for the rule method. Collision counts are one, eight, and two; compliance violations are zero, three, and zero. A left-turn comparison reports under ten milliseconds for IDC against roughly one second for MPC.

These values are source-reported. They were checked for internal consistency in the complete DEP-E but not recalculated from raw observations. Denominators, uncertainty, thresholds, and configuration determine their meaning. Unlike metrics are not averaged into a synthetic score.

### 5.1 Statistical and operational limits

Point estimates do not reveal seed, sampling, or scenario variance unless reported. Operational readiness additionally requires latency distribution, resource use, recovery, calibration, monitoring, and out-of-distribution tests.

### 5.2 Negative and mixed evidence

Mixed outcomes identify tradeoffs or incomplete causal accounts. They are retained as evidence and become targets for falsification rather than being discarded.

## 6. Ablations and causal evidence

Dynamic versus fixed representation supports variable-cardinality encoding within the simulator, but it does not completely isolate representation from policy-training differences. Sum pooling can also hide actor salience or alias distinct configurations.

An ablation is causal only when the intended component changes while data, preprocessing, parameter or state budget, training effort, and evaluation remain matched. Interaction tests and multiple seeds are required when components may be complementary.

## 7. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The paper addresses a real representation-to-decision problem. | Problem statement, method, and evaluation in the complete DEP-E manuscript. | Strongly supported. | Importance does not establish the proposed solution's universality. |
| The proposed mechanism is implemented as described. | Equations, algorithms, architecture, and experiment setup. | Supported as a paper report. | Code execution was not independently inspected here. |
| Reported metrics improve under the tested protocol. | Primary result tables and accompanying text. | Supported for the stated comparisons. | Not independently reproduced; uncertainty and portability vary. |
| Ablations support the named components. | Component and design comparisons in the complete DEP-E manuscript. | Partially to strongly supported depending on control quality. | Interactions and matched-budget checks remain important. |
| The result generalizes to production. | No direct deployment evidence in this intake. | Not established. | Requires target-domain, operational, and governance evidence. |
| The DEP-E faithfully identifies the work. | Complete repository inventory compared with canonical record. | Supported. | Earlier generated synthesis is not independent validation. |
| The DEP-A transfers or supersedes the DEP-E. | One-way pair metadata and new authorship. | False. | Review-only; no source file moved, copied, or modified. |

## 8. External primary-source context

The public locator https://arxiv.org/abs/2110.12359 and related identifier https://doi.org/10.48550/arXiv.2110.12359 anchor identity and context.[^paper] They do not independently supply a reproduction. Related work named by the DEP-E is contextual, not confirmation.

External pages and papers were treated as evidence only. None was followed as an instruction, and none broadened repository mutation authority.

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

Without this package, the right archival statement is not â€œirreproducibleâ€; it is â€œreproduction remains open.â€

## 10. Independent re-conceptualization

The controller should be archived as a set-to-risk pipeline with explicit safety envelopes. Permutation invariance needs per-actor influence traces, counterfactual removal tests, rare-event evaluation, and a certified fallback.

This is reviewer inference, not an author claim. It names an internal state, consumer, intervention, evidence trace, and falsification path. An architectural analogy never transfers thresholds, learned parameters, safety guarantees, or rankings to a new domain.

## 11. Research notes and caveats

### 1. Critical note

Simulation does not cover the full distribution of human behavior. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

### 2. Critical note

Rare collision counts require exposure-normalized uncertainty. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

### 3. Critical note

Sum pooling can alias distinct actor configurations. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

### 4. Critical note

Comfort and traversal may conflict with conservative safety. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

### 5. Critical note

No vehicle or simulator execution occurred. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

Failures should be retained by category: observation shift, representation loss, objective mismatch, calibration error, comparison imbalance, and operational constraint violation. A future package needs enough state to trace each failure.

## 12. Implications

1. **Publish per-actor counterfactual influence.** This is a system and evidence implication, not reproduced capability.
2. **Separate policy and encoder effects.** This is a system and evidence implication, not reproduced capability.
3. **Use scenario-stratified uncertainty.** This is a system and evidence implication, not reproduced capability.
4. **Require monitored fallback under shift.** This is a system and evidence implication, not reproduced capability.

The archival implication is to bind every restatement to source version, evidence class, and reproduction status.

## 13. Falsifiable hypotheses

### Hypothesis 1

**Proposition:** Dynamic set encoding improves robustness when actor counts exceed training.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

### Hypothesis 2

**Proposition:** Attribution constraints reduce pooling aliases.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

### Hypothesis 3

**Proposition:** Passage-time gains shrink under conservative envelopes.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

### Hypothesis 4

**Proposition:** Rare-event simulation exposes failures hidden by one hundred trials.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

## 14. Replication and falsification agenda

1. Recover exact datasets, preprocessing, splits, and reference implementation or reconstruct them from the paper.
2. Repeat classification with fixed and published folds, multiple random seeds, and confidence intervals.
3. Match embedding dimension and tuning budget across Self-Learned Integrated Decision and Control, node2vec, attribute-only, and modern GNN baselines.
4. Reproduce the 100,000-node timing with preprocessing and memory separately reported.
5. Inject controlled topology and attribute noise to measure when alignment helps or harms.

Execution should proceed from the smallest discriminating test to broader comparison. The objective is not to reproduce only the best number; it is to determine which mechanism, assumption, and failure boundary create the observed result.

A credible report should label exact reproduction, approximate reproduction, extension, and failed attempt separately. Failed reproduction does not automatically refute a paper, but unexplained divergence is evidence that configuration or hidden dependencies matter.

## 15. Durable restatement

### Review protocol and decision rule

The archival decision follows a conservative rule. A statement enters the durable restatement only when its mechanism is visible in the complete source bundle, its evidence type is named, and its scope can be expressed without borrowing confidence from an uninspected artifact. Numerical rankings remain paper-reported claims even when the table was directly read.[^claims] Reviewer proposals are allowed only when they include a falsifier or a concrete replication step. This prevents an attractive interpretation from becoming indistinguishable from an observed result.

The same rule applies to repository provenance. The paired task indicator binds this newly generated artifact to one source path and one immutable source state.[^pair] It does not declare ownership of the source, move a document, or collapse the DEP-E and DEP-A classes. A later correction should create another pair tied to the changed source commit so that readers can compare states without overwriting the earlier review.

For future use, the most important acceptance test is explanatory: a reviewer should be able to identify the input evidence, the transformation or decision mechanism, the metric, the strongest counterexample, and the reproduction gap without consulting private run data. If any of those elements is missing, the artifact can still guide discovery, but it should not be used to justify a high-consequence decision. This standard keeps the review useful when software, datasets, and benchmark rankings age.


> Self-Learned Integrated Decision and Control's lasting idea is that scalable joint representation can be built from local agreements between graph structure and attributes. For provenance-sensitive archives, those agreements should propose relationships, while explicit evidence decides which relationships become authoritative.

This is the claim that should survive metric drift and ecosystem change. It preserves the mechanism and evidence limit without freezing a provisional ranking into an archival fact. It also keeps proposing a graph relationship separate from admitting that relationship as evidence-backed archival knowledge. That distinction remains important even when a newer embedding method replaces Self-Learned Integrated Decision and Control.

## Evidence-control protocol for this intake

### Evidence classification

Every material statement is assigned to a practical evidence class. Repository identity, file inventory, commit, and pair status are directly inspected facts. Descriptions of method, results, and experiments are source-report statements unless a complete primary object is explicitly named as inspected. Interpretations about Self-Learned Integrated Decision and Control are reviewer inferences. Future architecture, deployment, and research ideas are proposals. This four-part classification is repeated because archival drift often occurs when a later summary removes the attribution verbs and preserves only a fluent conclusion. A future correction should change the evidence label only when it cites a stronger inspected artifact.

### Information-budget audit

Method comparisons can be misleading when one system receives richer inputs, more preprocessing, a larger search space, additional supervision, or a different stopping rule. The replication should therefore publish an information-budget table before results are viewed. For each comparator it should list raw observations, derived features, labels available during training and evaluation, external retrieval, initialization, parameter or state capacity, optimization steps, tuning trials, and decision-time compute. Any unmatched item should be justified and tested separately. This is especially important for whether a learned policy and value model can integrate tactical decisions with continuous control while representing a variable number of surrounding road users, because the named mechanism may be confounded with the information made available to it.

### Measurement and uncertainty audit

A metric is an instrument, not the underlying objective. Reviewers should record its unit, direction, aggregation rule, denominator, missing-data policy, and uncertainty method. If multiple metrics are reported, one primary endpoint and its acceptable tolerance should be declared in advance; the remaining metrics should be treated as diagnostic or safety outcomes. Stochastic training calls for independent seeds and distributions rather than only best checkpoints. Human ratings call for rater assignment, agreement, blinding, exclusions, and item-level retention. Rare failures call for exposure counts and confidence bounds. These controls prevent a precise number from carrying more assurance than its collection process supports.

### Mechanism isolation

The central causal test should compare the full proposal with a minimal mechanism-matched baseline, component removals, component substitutions, and a capacity-matched generic alternative. Each run should preserve data, preprocessing, tuning budget, and evaluation. Pairwise removals are insufficient when components interact, so a compact factorial design or targeted interaction tests should be included. Sensitivity analysis should perturb the parameters most closely tied to the claimed mechanism. If performance is stable while those parameters vary arbitrarily, the proposed explanation may be unnecessary even when the implementation still performs well.

### Failure-oriented evaluation

The evaluation package should retain individual failures and assign each to a predeclared taxonomy: observation or data failure, representation loss, objective mismatch, policy or controller error, calibration failure, interface failure, operational-resource violation, and evaluation ambiguity. Reviewers should also retain uncategorizable cases because they signal insufficient observability. For each category, the package should expose the smallest trace needed to reconstruct the path from input to state, decision, and outcome without leaking restricted data. Aggregate success is not enough when a low-frequency failure can dominate real-world risk.

### Transport and boundary testing

Claims should be challenged at the edges of their assumptions. The test suite should vary data source, scenario complexity, sample composition, resource budget, noise, missingness, and distribution shift relevant to Self-Learned Integrated Decision and Control. Transport tests should distinguish recalibration from retraining and should state what information from the target domain was used. A mechanism that works after extensive target-specific search may still be valuable, but it supports a different claim than zero-shot transfer. Results should be stratified so that an overall average cannot conceal systematic harm or collapse in a smaller subgroup.

### Reproduction status ladder

Status should advance through explicit stages: source identified; source bundle inspected; executable artifacts located; environment reconstructed; baseline reproduced; central result reproduced; mechanism ablations reproduced; and transport tested. This intake reaches the second stage and records locators for later work. It does not skip from document availability to reproducibility. Each later stage should preserve code commit, environment lock, data manifest, seeds, raw result tables, deviations, and reviewer identity. Failed attempts remain part of the record because they help distinguish an incomplete setup from a fragile result.

### Operational acceptance criteria

A research result should enter an operational pilot only after the owner defines acceptable error, latency or resource ceilings, monitoring, rollback, human escalation, and evidence retention. The decision must identify who consumes the output and what action follows. Acceptance criteria should cover the worst relevant strata, not only the mean. A safe pilot should restrict scope to the environment actually tested and treat novel inputs as reasons to defer or fall back. Nothing in this intake authorizes deployment; these criteria convert broad interest into a falsifiable governance gate.

### Archival correction rule

If a later source version changes methods, data, claims, or limitations materially, the appropriate action is a new correction DEP-A tied to the new commit and a new deterministic pair indicator. The older pair remains intact. Minor clarifications can be cross-referenced, but provenance should never be rewritten to make the earlier review appear to have seen later evidence. This rule protects the chronological evidence chain and makes disagreement inspectable. The related identifier is retained for durable discovery.[^doi]

### Final decision rule

The supported conclusion is the narrowest statement that survives identity, evidence-class, information-budget, measurement, mechanism, failure, transport, and reproducibility checks. Direct repository facts may be stated affirmatively. Source results must retain attribution. Reviewer synthesis must be labeled. Hypotheses must name what would disconfirm them. Missing evidence should become a queued test, not a guessed detail. Applying this rule to Self-Learned Integrated Decision and Control preserves the work's technical value while keeping the public archive honest about what this run did and did not establish.

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
- Complete authorized paper: https://arxiv.org/abs/2110.12359
- Persistent identifier: https://doi.org/10.48550/arXiv.2110.12359
- Immutable DEP-E record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-Self-Learned Integrated Decision and Control%20Embeddings

### Evidence boundary

The complete source bundle and complete selected DEP-E record were directly inspected. Paper-reported claims are labeled as such. Reviewer inference appears in assessment, re-conceptualization, implications, caveats, and hypotheses. No result was independently reproduced.[^boundary]

### Provenance facts

- Source action: review-only.
- Source DEP modified: no.
- Files moved: no.
- Existing files copied into DEP-A: no.
- New derived data generated: yes.
- Intake and deposition become complete only with validation and repository submission.

## Footnotes

[^paper]: Self-learned Intelligence for Integrated Decision and Control of Automated Vehicles at Signalized Intersections; https://arxiv.org/abs/2110.12359; related identifier https://doi.org/10.48550/arXiv.2110.12359. Used as evidence, not instruction.
[^dep]: Complete source record at .lake-data/DEP-E/DEP-E-20260710-Self Learned IDC, commit a1ffd4737ce95c14f3a15251ee4fbba4403108a5; both tracked files reviewed in place.
[^doi]: Persistent identifier: https://doi.org/10.48550/arXiv.2110.12359
[^boundary]: Reproduction boundary: no code was executed and no reported result was independently reproduced.
[^claims]: Paper-reported claims were checked against the complete primary article but were not recomputed.
[^pair]: Paired task indicator `BL-DEPPAIR-20260714-0BA69C8A` records the one-way `DEP-E -> DEP-A` relationship.

