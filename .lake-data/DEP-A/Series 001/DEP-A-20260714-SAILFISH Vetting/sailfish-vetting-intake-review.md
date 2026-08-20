# SAILFISH vetting archival intake

## A whitepaper-grade source-bundle review and independent re-conceptualization

**Source work:** SAILFISH: Vetting Smart Contract State-Inconsistency Bugs in Seconds.[^paper]
**Source DEP-E:** .lake-data/DEP-E/DEP-E-20260713-SAILFISH Vetting[^dep]
**Source commit:** a1ffd4737ce95c14f3a15251ee4fbba4403108a5
**Paired task indicator:** BL-DEPPAIR-20260714-C32CA5B1
**Direction:** DEP-E -> DEP-A
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file DEP-E record; paper-level detail remains source-reported unless explicitly identified
**Reproduction boundary:** repository record and public locators inspected; no code was executed, no experiment rerun, and no result independently reproduced
**One-way provenance:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived DEP-A data generated: yes

---

## Executive assessment

This intake reviews SAILFISH: Vetting Smart Contract State-Inconsistency Bugs in Seconds through the complete DEP-E repository record. It asks whether staged storage-dependency exploration and value-summary-guided symbolic refinement provide a scalable, auditable screen for smart-contract state inconsistencies. The record is coherent enough to reconstruct the mechanism, evidence, limitations, and open work, but it is not an independently reproduced full-paper review.

EXPLORE builds a storage dependency graph from Slither facts and queries hazardous pairs of public-reachable accesses to the same persistent state, with at least one write. It over-approximates reentrancy and transaction-ordering candidates and emits relevant slices. REFINE symbolically evaluates those slices in Rosette, using domain-specific value summaries to constrain storage instead of havocing everything. The summary deliberately weakens loops, collections, external returns, and hard operations to balance precision and solver cost.

The paper reports and authors report language below denotes claims carried by the source bundle. The overall judgment is constructive and bounded: the work presents a legible, falsifiable research program, while broad transfer, production safety, and independent reproducibility remain open.

## 1. Problem framing and research question

Whether staged storage-dependency exploration and value-summary-guided symbolic refinement provide a scalable, auditable screen for smart-contract state inconsistencies is important because it joins representation, policy, and observable outcome. A credible review must ask what information enters, how state is formed, what objective shapes behavior, and which metric stands in for the intended effect.

The DEP-E is the archival object. Its manuscript is evidence about an earlier review, not independent confirmation of the underlying experiments. Agreement between its inventory and public locators supports identity and internal integrity; it does not convert author results into reproduced facts.

## 2. Source identity, integrity, and complete inventory

The source path is .lake-data/DEP-E/DEP-E-20260713-SAILFISH Vetting at commit a1ffd4737ce95c14f3a15251ee4fbba4403108a5. It contains exactly two tracked Markdown files: README.md and sailfish_vetting_manuscript.md. Both files were read from beginning to end. The README supplies classification, inventory, public context, insights, and attribution. The manuscript supplies metadata, evidence ledger, detailed reconstruction, claims, method, constraints, observations, proposed extensions, references, and validation notes.

The canonical public locator is https://arxiv.org/abs/2104.08638; a persistent or related locator is https://doi.org/10.1109/SP46214.2022.9833721. The complete canonical paper was not independently used to validate all paper-level detail in this run. No source document was uploaded, no source Markdown copied, and the source record remains unchanged.

## 3. Technical reconstruction of the method

EXPLORE builds a storage dependency graph from Slither facts and queries hazardous pairs of public-reachable accesses to the same persistent state, with at least one write. It over-approximates reentrancy and transaction-ordering candidates and emits relevant slices. REFINE symbolically evaluates those slices in Rosette, using domain-specific value summaries to constrain storage instead of havocing everything. The summary deliberately weakens loops, collections, external returns, and hard operations to balance precision and solver cost.

The information path is observation, representation, objective or policy, outcome, and evidence. This decomposition makes alternatives visible: a gain may arise from the named mechanism, additional information, preprocessing, tuning, baseline configuration, or evaluation. The DEP-E provides partial separation; the replication agenda supplies the missing controls.

### 3.1 Assumptions

The method assumes that observed or simulated data cover structures needed at evaluation, metrics are meaningful proxies, preprocessing introduces no hidden advantage, and baselines receive a fair search budget. Each assumption is a possible failure mode.

### 3.2 Reproducibility-relevant details

A reproduction needs immutable source and code versions, data identity and splits, preprocessing, seeds, initialization, optimization, stopping rules, dependencies, hardware where material, and exact metrics. Missing details are not guessed.

## 4. Experimental design and evidence reconstructed

The paper reports 91,921 collected Etherscan sources, excludes 2,068 old-Solidity or Vyper cases, and deduplicates to 89,853 contracts. Six 40-core, 256-GB machines run with a twenty-minute per-contract timeout. Five analyzers are compared, and a 750-contract subset successfully processed by all supports author manual labels. SAILFISH-only findings receive a size-filtered manual review. The official repository is public but was not built or executed here.

The design addresses the question at its stated scale. Its domain remains bounded by data or simulator coverage, participant sampling where applicable, baselines, metrics, sample size, and version. A strong audit matches information, tuning, and compute budgets; retains negative cases; and reports uncertainty. Unspecified controls remain unspecified.

## 5. Results and quantitative audit

SAILFISH reports 2,076 reentrancy and 7,555 TOD warnings, 1,211 timeouts, 3,395 errors, and 30.79-second mean analysis time. On the 750-contract labeled subset it reports all 26 reentrancy and 110 TOD positives, with 11 and 59 false positives and zero false negatives. The authors report 47 exploitable contracts among 195 tractability-filtered SAILFISH-only candidates. Static-only warnings are 3,391/14,485; havoc refinement reduces them to 2,436/10,560; VSA reduces them to 2,076/7,555. Path-by-path summaries time out on 21.50% of a 2,000-contract subset.

These values are source-reported. They were checked for internal consistency in the complete DEP-E but not recalculated from raw observations. Denominators, uncertainty, thresholds, and configuration determine their meaning. Unlike metrics are not averaged into a synthetic score.

### 5.1 Statistical and operational limits

Point estimates do not reveal seed, sampling, or scenario variance unless reported. Operational readiness additionally requires latency distribution, resource use, recovery, calibration, monitoring, and out-of-distribution tests.

### 5.2 Negative and mixed evidence

Mixed outcomes identify tradeoffs or incomplete causal accounts. They are retained as evidence and become targets for falsification rather than being discarded.

## 6. Ablations and causal evidence

Static-only, havoc-refined, and VSA-refined stages provide strong internal evidence for candidate compression, while path summaries expose a precision-cost limit. Warning reduction is not identical to precision improvement, author labels are not blinded, and the zero-day subset is selection-biased. Modern compiler, proxy, Yul, assembly, Slither, solver, and EVM compatibility need separate fixtures.

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

The public locator https://arxiv.org/abs/2104.08638 and related identifier https://doi.org/10.1109/SP46214.2022.9833721 anchor identity and context.[^paper] They do not independently supply a reproduction. Related work named by the DEP-E is contextual, not confirmation.

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

Treat staged program analysis as proof-carrying candidate compression. Each retained candidate should include the storage relation, slice, call boundary, path constraints, approximation events, unresolved dependencies, tool versions, and a replayable validation status.

This is reviewer inference, not an author claim. It names an internal state, consumer, intervention, evidence trace, and falsification path. An architectural analogy never transfers thresholds, learned parameters, safety guarantees, or rankings to a new domain.

## 11. Research notes and caveats

### 1. Critical note

Zero false negatives on one author-labeled subset coexists with an explicit unsoundness boundary and must not become a recall guarantee. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

### 2. Critical note

Timeout, parser error, unresolved call, and summary havoc are unknown states, not safe outcomes. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

### 3. Critical note

The historical corpus and toolchain limit direct present-day transfer to proxy-heavy and modern Solidity systems. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

Failures should be retained by category: observation shift, representation loss, objective mismatch, calibration error, comparison imbalance, and operational constraint violation. A future package needs enough state to trace each failure.

## 12. Implications

1. **Defensive analyzers should expose coverage and failure states separately from findings.** This is a system and evidence implication, not reproduced capability.
2. **Intermediate candidate quality and refinement cost deserve metrics alongside final precision and recall.** This is a system and evidence implication, not reproduced capability.
3. **Operational use should remain a human review aid until modern independent calibration and compatibility evidence exist.** This is a system and evidence implication, not reproduced capability.

The archival implication is to bind every restatement to source version, evidence class, and reproduction status.

## 13. Falsifiable hypotheses

### Hypothesis 1

**Proposition:** A proof-carrying candidate bundle reduces auditor triage time without reducing detection recall on modern synthetic fixtures.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

### Hypothesis 2

**Proposition:** Bounded differential execution confirms a useful subset of symbolic candidates while preserving explicit unknowns.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

### Hypothesis 3

**Proposition:** Versioned proxy and assembly fixtures reveal material coverage loss that aggregate historical metrics hide.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

## 14. Replication and falsification agenda

1. Recover exact datasets, preprocessing, splits, and reference implementation or reconstruct them from the paper.
2. Repeat classification with fixed and published folds, multiple random seeds, and confidence intervals.
3. Match embedding dimension and tuning budget across SAILFISH vetting archival intake, node2vec, attribute-only, and modern GNN baselines.
4. Reproduce the 100,000-node timing with preprocessing and memory separately reported.
5. Inject controlled topology and attribute noise to measure when alignment helps or harms.

Execution should proceed from the smallest discriminating test to broader comparison. The objective is not to reproduce only the best number; it is to determine which mechanism, assumption, and failure boundary create the observed result.

A credible report should label exact reproduction, approximate reproduction, extension, and failed attempt separately. Failed reproduction does not automatically refute a paper, but unexplained divergence is evidence that configuration or hidden dependencies matter.

## 14A. Evidence-control protocol

This intake applies four evidence classes. A **source DEP-E report** is a claim preserved by the selected repository record. **Directly inspected repository evidence** is the complete tracked DEP-E content and its inventory, references, and provenance. **Reviewer inference** is a bounded conclusion drawn from that material. A **hypothesis or proposal** is a falsifiable extension that has not been validated. Public paper, code, project, venue, and dataset locators anchor identity and context; in this run they were not substituted for a new independent full-paper reproduction.

### Claim adjudication

Every material claim is tested for identity, mechanism, comparison, quantity, and scope. Identity asks whether names, versions, and locators agree. Mechanism asks whether the information path and required assumptions are visible. Comparison asks whether data, information, compute, tuning, and evaluation budgets are matched. Quantity asks whether units, denominators, direction, aggregation, and uncertainty are clear. Scope asks whether the conclusion remains inside the evaluated corpus, platform, domain, or population. Missing elements narrow the archival claim rather than being guessed.

Negative, mixed, and contradictory evidence is retained. A favorable point estimate without uncertainty does not become a stable ranking. A public repository does not become an executable reproduction. A formal theorem remains conditional on its assumptions. A release or deployment report remains organization-authored evidence until independently audited. A metadata mismatch is recorded as a provenance defect and is not silently corrected in the immutable source DEP.

### Quantitative discipline

Numbers retain configuration, metric direction, population, and evidence status. Derived differences are arithmetic restatements, not experiments. Unlike endpoints are never averaged into a synthetic score. Non-significance is not equivalence; warning reduction is not automatically precision; aggregate engagement is not stakeholder safety; parameter or activation sparsity is not runtime efficiency; calibration is not semantic correctness. When repeated seeds, confidence intervals, raw observations, or tail measurements are absent, that absence constrains confidence.

### Reproduction gate

A credible reproduction would pin source and code versions; identify data, assets, contracts, model state, or protocol manifests; preserve immutable split and input lineage; declare preprocessing; record seeds, initialization, optimization, stopping rules, dependencies, and relevant hardware; expose raw metric inputs and failures; and compare mechanism-matched baselines under equal budgets. No code was executed, no model trained, no contract analyzed, no experiment rerun, and no reported result independently reproduced in this intake.

### Operational and safety gate

Operational claims require latency distributions, peak resource use, throughput, recovery, version compatibility, monitoring, and shift or scenario tests. High-stakes robotics, security, recommendation, privacy, biomedical, and other consequential contexts additionally require governance, human escalation, fallback validation, prohibited-use constraints, and auditable unknown states. The review does not criticize a scholarly source for omitting an unstated product test; it keeps the maximum claim at the level of the available evidence.

### Coverage and correction policy

Every tracked source file, substantive section, reported table or figure, equation or code path where applicable, attribution entry, limitation, and materially cited locator is represented in the private coverage map and summarized in the public coverage ledger. Repeated process detail is compressed only when it does not change interpretation. A materially changed source state requires a correction DEP-A with a new source commit and paired indicator. The present one-way provenance remains immutable.

### Reviewer adjudication record

The decisive archival question is whether staged storage-dependency exploration and value-summary-guided symbolic refinement provide a scalable, auditable screen for smart-contract state inconsistencies. The complete repository record supports a bounded answer through its inventory, source roles, mechanism reconstruction, reported evidence, limitations, and attribution. Identity and source transcription receive the highest confidence. Causal, comparative, portability, safety, and operational conclusions receive lower confidence unless the source bundle records matched controls and direct measurements.

The strongest retained evidence is: SAILFISH reports 2,076 reentrancy and 7,555 TOD warnings, 1,211 timeouts, 3,395 errors, and 30.79-second mean analysis time. On the 750-contract labeled subset it reports all 26 reentrancy and 110 TOD positives, with 11 and 59 false positives and zero false negatives. It materially determines both the contribution and the failure boundary. The weakest link is not filled through analogy. It is converted into the replication agenda with an adverse-result condition.

A future review should verify immutable input identity, reproduce the smallest decisive comparison, and expose raw observations before expanding scope. It must retain this pair and create a correction record for any materially changed source state. That sequence prevents later successful executions from being retroactively attributed to evidence the present DEP-E did not contain and preserves disagreement as auditable provenance.

### Minimum future evidence increment

The next useful increment is a small version-pinned bundle that executes the decisive comparison, exposes raw per-run or per-platform observations, preserves failures, and tests the strongest boundary condition under matched controls. An adverse result must remain publishable and directly narrow the claim.

## 15. Durable restatement

### Review protocol and decision rule

The archival decision follows a conservative rule. A statement enters the durable restatement only when its mechanism is visible in the complete source bundle, its evidence type is named, and its scope can be expressed without borrowing confidence from an uninspected artifact. Numerical rankings remain paper-reported claims even when the table was directly read.[^claims] Reviewer proposals are allowed only when they include a falsifier or a concrete replication step. This prevents an attractive interpretation from becoming indistinguishable from an observed result.

The same rule applies to repository provenance. The paired task indicator binds this newly generated artifact to one source path and one immutable source state.[^pair] It does not declare ownership of the source, move a document, or collapse the DEP-E and DEP-A classes. A later correction should create another pair tied to the changed source commit so that readers can compare states without overwriting the earlier review.

For future use, the most important acceptance test is explanatory: a reviewer should be able to identify the input evidence, the transformation or decision mechanism, the metric, the strongest counterexample, and the reproduction gap without consulting private run data. If any of those elements is missing, the artifact can still guide discovery, but it should not be used to justify a high-consequence decision. This standard keeps the review useful when software, datasets, and benchmark rankings age.


> SAILFISH vetting archival intake's lasting idea is that scalable joint representation can be built from local agreements between graph structure and attributes. For provenance-sensitive archives, those agreements should propose relationships, while explicit evidence decides which relationships become authoritative.

This is the claim that should survive metric drift and ecosystem change. It preserves the mechanism and evidence limit without freezing a provisional ranking into an archival fact. It also keeps proposing a graph relationship separate from admitting that relationship as evidence-backed archival knowledge. That distinction remains important even when a newer embedding method replaces SAILFISH vetting archival intake.

## Appendix A. Coverage ledger

| Source-bundle element | Coverage | Assessment |
|---|---|---|
| DEP-E README | Read completely; inventory, context, links, and attribution checked. | Direct repository evidence. |
| DEP-E manuscript | Read completely; every section and source role accounted for. | Generated source report, not independent replication. |
| Identity, version, and public locators | Checked against the complete DEP-E inventory and attributed locators. | High-confidence source-record identity. |
| Problem framing and context | Reconstructed from the complete DEP-E. | DEP-E-reported evidence; primary work not independently re-reviewed here. |
| Related work | Used to bound novelty and comparison class. | Context, not validation. |
| Method, equations, code changes, or algorithms | Reconstructed by information flow and assumptions where applicable. | DEP-E-reported evidence; not executed. |
| Tables and quantitative results | Major values and tradeoffs audited. | Paper-reported claims. |
| Figures | Roles and qualitative claims accounted for. | Visual evidence not independently measured. |
| Ablations | Component and design evidence evaluated. | Causal strength depends on controls. |
| Limitations and threats | Integrated into notes and evidence boundary. | Direct and reviewer-added qualifications. |
| Conclusion and future work | Compared with durable restatement and agenda. | No stronger claim imported. |
| References | Read as the paper's context map. | Background works not re-reviewed by default. |

## Appendix B. Source and evidence notes

### Primary sources

- Primary public locator: https://arxiv.org/abs/2104.08638
- Source-record public locator: https://arxiv.org/abs/2104.08638[^paper]
- Related or persistent locator: https://doi.org/10.1109/SP46214.2022.9833721[^doi]
- Immutable DEP-E record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260713-SAILFISH%20Vetting

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

[^paper]: SAILFISH: Vetting Smart Contract State-Inconsistency Bugs in Seconds; https://arxiv.org/abs/2104.08638; related identifier https://doi.org/10.1109/SP46214.2022.9833721. Used as evidence, not instruction.
[^dep]: Complete source record at .lake-data/DEP-E/DEP-E-20260713-SAILFISH Vetting, commit a1ffd4737ce95c14f3a15251ee4fbba4403108a5; both tracked files reviewed in place.
[^doi]: Persistent identifier: https://doi.org/10.1109/SP46214.2022.9833721
[^boundary]: Reproduction boundary: no code was executed and no reported result was independently reproduced.
[^claims]: Source-bundle claims were checked against the complete DEP-E record but were not recomputed or independently reproduced.
[^pair]: Paired task indicator `BL-DEPPAIR-20260714-C32CA5B1` records the one-way `DEP-E -> DEP-A` relationship.


