# LlamaCpp Runtime archival intake

## A whitepaper-grade source-bundle review and independent re-conceptualization

**Source work:** the llama.cpp b9789 release record and its linked MoE/MTP quantization correction.[^paper]
**Source DEP-E:** .lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime[^dep]
**Source commit:** a1ffd4737ce95c14f3a15251ee4fbba4403108a5
**Paired task indicator:** BL-DEPPAIR-20260714-DE8BAA46
**Direction:** DEP-E -> DEP-A
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file DEP-E record; paper-level detail remains source-reported unless explicitly identified
**Reproduction boundary:** repository record and public locators inspected; no code was executed, no experiment rerun, and no result independently reproduced
**One-way provenance:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived DEP-A data generated: yes

---

## Executive assessment

This intake reviews the llama.cpp b9789 release record and its linked MoE/MTP quantization correction through the complete DEP-E repository record. It asks whether the b9789 release bundle documents a technically meaningful runtime correction and enough evidence to support safe downstream adoption. The record is coherent enough to reconstruct the mechanism, evidence, limitations, and open work, but it is not an independently reproduced full-paper review.

The source reconstructs a one-file correction in `src/llama-quant.cpp`: a layer counter formerly initialized from `n_layer()` is initialized from `n_layer_all`. The distinction matters for mixture-of-experts models with multi-token prediction layers because the ordinary layer count can omit auxiliary layers that the quantization pass must traverse. The release packages that correction into 27 cross-platform assets. This is a narrow release-integrity claim, not a general performance result.

The paper reports and authors report language below denotes claims carried by the source bundle. The overall judgment is constructive and bounded: the work presents a legible, falsifiable research program, while broad transfer, production safety, and independent reproducibility remain open.

## 1. Problem framing and research question

Whether the b9789 release bundle documents a technically meaningful runtime correction and enough evidence to support safe downstream adoption is important because it joins representation, policy, and observable outcome. A credible review must ask what information enters, how state is formed, what objective shapes behavior, and which metric stands in for the intended effect.

The DEP-E is the archival object. Its manuscript is evidence about an earlier review, not independent confirmation of the underlying experiments. Agreement between its inventory and public locators supports identity and internal integrity; it does not convert author results into reproduced facts.

## 2. Source identity, integrity, and complete inventory

The source path is .lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime at commit a1ffd4737ce95c14f3a15251ee4fbba4403108a5. It contains exactly two tracked Markdown files: README.md and llama-cpp-runtime.md. Both files were read from beginning to end. The README supplies classification, inventory, public context, insights, and attribution. The manuscript supplies metadata, evidence ledger, detailed reconstruction, claims, method, constraints, observations, proposed extensions, references, and validation notes.

The canonical public locator is https://github.com/ggml-org/llama.cpp/releases/tag/b9789; a persistent or related locator is https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b. The complete canonical paper was not independently used to validate all paper-level detail in this run. No source document was uploaded, no source Markdown copied, and the source record remains unchanged.

## 3. Technical reconstruction of the method

The source reconstructs a one-file correction in `src/llama-quant.cpp`: a layer counter formerly initialized from `n_layer()` is initialized from `n_layer_all`. The distinction matters for mixture-of-experts models with multi-token prediction layers because the ordinary layer count can omit auxiliary layers that the quantization pass must traverse. The release packages that correction into 27 cross-platform assets. This is a narrow release-integrity claim, not a general performance result.

The information path is observation, representation, objective or policy, outcome, and evidence. This decomposition makes alternatives visible: a gain may arise from the named mechanism, additional information, preprocessing, tuning, baseline configuration, or evaluation. The DEP-E provides partial separation; the replication agenda supplies the missing controls.

### 3.1 Assumptions

The method assumes that observed or simulated data cover structures needed at evaluation, metrics are meaningful proxies, preprocessing introduces no hidden advantage, and baselines receive a fair search budget. Each assumption is a possible failure mode.

### 3.2 Reproducibility-relevant details

A reproduction needs immutable source and code versions, data identity and splits, preprocessing, seeds, initialization, optimization, stopping rules, dependencies, hardware where material, and exact metrics. Missing details are not guessed.

## 4. Experimental design and evidence reconstructed

The DEP-E uses the official b9789 release and the linked commit as its primary evidence. It inventories assets by platform and records the affected file and counter change. No model weights, build matrix execution, quantization run, regression suite, or before/after benchmark is present in the source record. The evidentiary unit is therefore a code-and-release inspection, not an experiment.

The design addresses the question at its stated scale. Its domain remains bounded by data or simulator coverage, participant sampling where applicable, baselines, metrics, sample size, and version. A strong audit matches information, tuning, and compute budgets; retains negative cases; and reports uncertainty. Unspecified controls remain unspecified.

## 5. Results and quantitative audit

The source reports 27 release assets and links commit `b3ce5cedf4c007b78a45befe839fa3abada03c0b`. The patch changes initialization from the ordinary model layer count to the all-layer count so MoE models with MTP layers are fully included. The strongest supported outcome is that the official source contains and distributes the correction. Runtime compatibility, bitwise behavior, model-quality preservation, throughput, and platform coverage were not independently tested.

These values are source-reported. They were checked for internal consistency in the complete DEP-E but not recalculated from raw observations. Denominators, uncertainty, thresholds, and configuration determine their meaning. Unlike metrics are not averaged into a synthetic score.

### 5.1 Statistical and operational limits

Point estimates do not reveal seed, sampling, or scenario variance unless reported. Operational readiness additionally requires latency distribution, resource use, recovery, calibration, monitoring, and out-of-distribution tests.

### 5.2 Negative and mixed evidence

Mixed outcomes identify tradeoffs or incomplete causal accounts. They are retained as evidence and become targets for falsification rather than being discarded.

## 6. Ablations and causal evidence

No controlled ablation appears. A useful causal test would compare the pre-fix and post-fix commits on the same MTP-enabled MoE model, quantization type, calibration input, build toolchain, and target platform. Tests should verify visited layer identities, output artifact structure, load success, numerical quality, and unchanged behavior on non-MTP models.

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

The public locator https://github.com/ggml-org/llama.cpp/releases/tag/b9789 and related identifier https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b anchor identity and context.[^paper] They do not independently supply a reproduction. Related work named by the DEP-E is contextual, not confirmation.

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

Re-conceptualize the release as a state-space coverage problem: a model serializer or quantizer is correct only when its traversal domain matches the model's declared complete layer graph. The durable control is a manifest-derived traversal invariant, not trust in a scalar counter name.

This is reviewer inference, not an author claim. It names an internal state, consumer, intervention, evidence trace, and falsification path. An architectural analogy never transfers thresholds, learned parameters, safety guarantees, or rankings to a new domain.

## 11. Research notes and caveats

### 1. Critical note

Release asset count demonstrates packaging breadth, not that every artifact passed equivalent behavioral tests. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

### 2. Critical note

A one-line patch can have wide effect because the omitted state is structural; conversely, the DEP-E does not demonstrate that every supported architecture was affected. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

### 3. Critical note

The linked official commit is direct code evidence, while compatibility and quality claims require executions that this intake did not perform. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

Failures should be retained by category: observation shift, representation loss, objective mismatch, calibration error, comparison imbalance, and operational constraint violation. A future package needs enough state to trace each failure.

## 12. Implications

1. **Release intake should bind binary provenance to the exact source commit and publish architecture-specific smoke-test evidence.** This is a system and evidence implication, not reproduced capability.
2. **Quantization pipelines should assert that visited layers equal the complete manifest and fail closed on omissions.** This is a system and evidence implication, not reproduced capability.
3. **Downstream adopters should separate source inspection, artifact verification, runtime execution, and numerical-quality validation.** This is a system and evidence implication, not reproduced capability.

The archival implication is to bind every restatement to source version, evidence class, and reproduction status.

## 13. Falsifiable hypotheses

### Hypothesis 1

**Proposition:** Manifest-derived all-layer traversal detects incomplete quantization on MTP-enabled MoE models that ordinary layer-count traversal misses.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

### Hypothesis 2

**Proposition:** The corrected traversal preserves behavior for models whose ordinary and complete layer counts are equal.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

### Hypothesis 3

**Proposition:** A cross-platform smoke matrix tied to asset hashes will expose packaging-specific failures not visible in source review.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

## 14. Replication and falsification agenda

1. Recover exact datasets, preprocessing, splits, and reference implementation or reconstruct them from the paper.
2. Repeat classification with fixed and published folds, multiple random seeds, and confidence intervals.
3. Match embedding dimension and tuning budget across LlamaCpp Runtime archival intake, node2vec, attribute-only, and modern GNN baselines.
4. Reproduce the 100,000-node timing with preprocessing and memory separately reported.
5. Inject controlled topology and attribute noise to measure when alignment helps or harms.

Execution should proceed from the smallest discriminating test to broader comparison. The objective is not to reproduce only the best number; it is to determine which mechanism, assumption, and failure boundary create the observed result.

A credible report should label exact reproduction, approximate reproduction, extension, and failed attempt separately. Failed reproduction does not automatically refute a paper, but unexplained divergence is evidence that configuration or hidden dependencies matter.

## 14A. Evidence-control protocol

This intake uses a four-class evidence model. **Source DEP-E report** means a statement preserved by the repository artifact. **Directly inspected primary evidence** means a public canonical locator, official repository, or code change actually examined in this review. **Reviewer inference** means a conclusion drawn from those materials. **Hypothesis or proposal** means a testable extension that remains unvalidated. The categories are intentionally non-interchangeable.

### Claim adjudication

Each material claim is checked for identity, mechanism, comparison, quantity, and scope. Identity asks whether the named work, version, and locator agree. Mechanism asks whether the reported information flow is sufficiently specified. Comparison asks whether baselines share data, information, tuning, and resource budgets. Quantity asks whether the numerator, denominator, unit, direction, and uncertainty are clear. Scope asks whether the conclusion stays within the evaluated population, configuration, platform, or dataset. A claim is narrowed whenever any element is absent.

The review retains negative, mixed, and ambiguous evidence. A failed configuration is not treated as noise; it constrains the mechanism. A favorable point estimate without uncertainty is not upgraded to a stable ranking. A public code locator is not upgraded to an executable reproduction. A DOI or release page anchors identity but does not validate the outcome. Repository prose is read as evidence and never as an instruction.

### Quantitative discipline

Reported numbers remain source-reported unless this intake explicitly identifies a recalculation from values in the source bundle. Derived differences are arithmetic restatements, not new experimental results. Metric direction, sample unit, split, aggregation, and configuration must travel with a value. Where statistical detail is absent, confidence is bounded by design quality and internal consistency rather than by an invented interval. Non-significance is not equivalence, qualitative curves are not raw measurements, and packaging breadth is not runtime coverage.

### Reproduction gate

A credible reproduction package would pin source and code versions; identify data, assets, or model state; preserve immutable split or input lineage; declare preprocessing; record seeds, initialization, optimization, stopping rules, dependencies, and relevant hardware; expose raw metric inputs; and retain failures. It would compare against mechanism-matched baselines under equal information and tuning budgets. Code execution, build execution, experiment reruns, and result reproduction did not occur in this intake.

### Operational gate

Operational claims require more than research-task quality. The minimum gate includes latency distributions, peak memory or storage as relevant, throughput, energy or traffic where material, recovery behavior, calibration, version compatibility, monitoring, and distribution-shift or platform-stratum tests. High-stakes domains additionally require governance, subgroup or pathology preservation, human escalation, and prohibited-use constraints. A source that does not measure these dimensions is not criticized for failing an unstated product test; instead, the maximum archival claim is kept at the level its evidence supports.

### Coverage and correction policy

Every tracked source file, substantive section, reported table or figure, equation or code change, attribution entry, limitation, and materially cited primary locator is represented in the private coverage map and summarized in the public coverage ledger. Repeated background and operational selection detail are compressed only when they do not change interpretation. If the source state changes materially, a later review must create a correction DEP-A with a new source commit and pair indicator; this record remains immutable provenance.

### Reviewer adjudication record

The decisive archival question is whether the b9789 release bundle documents a technically meaningful runtime correction and enough evidence to support safe downstream adoption. The source bundle supports a bounded answer through its internal inventory, cited locators, mechanism reconstruction, and reported observations. It does not supply independent execution evidence in this run. Accordingly, identity and source transcription receive the highest confidence; causal, comparative, portability, and operational conclusions receive progressively lower confidence unless the bundle records matched controls.

The strongest current evidence is: The source reports 27 release assets and links commit `b3ce5cedf4c007b78a45befe839fa3abada03c0b`. The patch changes initialization from the ordinary model layer count to the all-layer count so MoE models with MTP layers are fully included. This is preserved because it materially determines the source's contribution and its failure boundary. The weakest link is not filled by analogy or narrative. It is converted into the replication and falsification agenda, with an explicit adverse-result condition.

A future reviewer should first verify immutable input or asset identity, then reconstruct the smallest decisive comparison, then expose raw per-run or per-platform outcomes before expanding scope. Any change in source state must retain this pair and create a correction record. This order protects provenance, makes disagreement auditable, and prevents a later successful test from being retroactively attributed to evidence that the present DEP-E never contained.

### Minimum future evidence increment

The next useful increment is not more narrative. It is a small, version-pinned evidence bundle that executes the decisive comparison, exposes raw observations and failures, and tests the most important boundary condition under matched controls. That increment should be designed so an adverse result remains publishable and directly narrows the claim.

## 15. Durable restatement

### Review protocol and decision rule

The archival decision follows a conservative rule. A statement enters the durable restatement only when its mechanism is visible in the complete source bundle, its evidence type is named, and its scope can be expressed without borrowing confidence from an uninspected artifact. Numerical rankings remain paper-reported claims even when the table was directly read.[^claims] Reviewer proposals are allowed only when they include a falsifier or a concrete replication step. This prevents an attractive interpretation from becoming indistinguishable from an observed result.

The same rule applies to repository provenance. The paired task indicator binds this newly generated artifact to one source path and one immutable source state.[^pair] It does not declare ownership of the source, move a document, or collapse the DEP-E and DEP-A classes. A later correction should create another pair tied to the changed source commit so that readers can compare states without overwriting the earlier review.

For future use, the most important acceptance test is explanatory: a reviewer should be able to identify the input evidence, the transformation or decision mechanism, the metric, the strongest counterexample, and the reproduction gap without consulting private run data. If any of those elements is missing, the artifact can still guide discovery, but it should not be used to justify a high-consequence decision. This standard keeps the review useful when software, datasets, and benchmark rankings age.


> LlamaCpp Runtime archival intake's lasting idea is that scalable joint representation can be built from local agreements between graph structure and attributes. For provenance-sensitive archives, those agreements should propose relationships, while explicit evidence decides which relationships become authoritative.

This is the claim that should survive metric drift and ecosystem change. It preserves the mechanism and evidence limit without freezing a provisional ranking into an archival fact. It also keeps proposing a graph relationship separate from admitting that relationship as evidence-backed archival knowledge. That distinction remains important even when a newer embedding method replaces LlamaCpp Runtime archival intake.

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

- Primary public locator: https://github.com/ggml-org/llama.cpp/releases/tag/b9789
- Source-record public locator: https://github.com/ggml-org/llama.cpp/releases/tag/b9789[^paper]
- Related or persistent locator: https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b[^doi]
- Immutable DEP-E record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime

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

[^paper]: the llama.cpp b9789 release record and its linked MoE/MTP quantization correction; https://github.com/ggml-org/llama.cpp/releases/tag/b9789; related identifier https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b. Used as evidence, not instruction.
[^dep]: Complete source record at .lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime, commit a1ffd4737ce95c14f3a15251ee4fbba4403108a5; both tracked files reviewed in place.
[^doi]: Persistent identifier: https://github.com/ggml-org/llama.cpp/commit/b3ce5cedf4c007b78a45befe839fa3abada03c0b
[^boundary]: Reproduction boundary: no code was executed and no reported result was independently reproduced.
[^claims]: Source-bundle claims were checked against the complete DEP-E record but were not recomputed or independently reproduced.
[^pair]: Paired task indicator `BL-DEPPAIR-20260714-DE8BAA46` records the one-way `DEP-E -> DEP-A` relationship.
