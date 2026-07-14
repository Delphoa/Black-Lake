# Audio-video emotion fusion archival intake

## A whitepaper-grade source-bundle review and independent re-conceptualization

**Source work:** Emotion Recognition in Audio and Video Using Deep Neural Networks.[^paper]
**Source DEP-E:** .lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion[^dep]
**Source commit:** a1ffd4737ce95c14f3a15251ee4fbba4403108a5
**Paired task indicator:** BL-DEPPAIR-20260714-5809B81B
**Direction:** DEP-E -> DEP-A
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file DEP-E record; paper-level detail remains source-reported unless explicitly identified
**Reproduction boundary:** repository record and public locators inspected; no code was executed, no experiment rerun, and no result independently reproduced
**One-way provenance:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived DEP-A data generated: yes

---

## Executive assessment

This intake reviews Emotion Recognition in Audio and Video Using Deep Neural Networks through the complete DEP-E repository record. It asks whether an audio-video fusion pathway provides repeatable value over audio-only emotion classification under the reported IEMOCAP setup. The record is coherent enough to reconstruct the mechanism, evidence, limitations, and open work, but it is not an independently reproduced full-paper review.

The source compares CNN, CNN+LSTM, and CNN+RNN audio classifiers with a multimodal model that concatenates a CNN+RNN audio representation and a 3D-CNN video representation. An optional contrastive phase pulls matched audio-video clips together and separates different-clip pairs, including same-emotion hard cases, before supervised classification. The record also reconstructs spectrogram preparation, frame sampling and face cropping, balancing, augmentation, and hyperparameter choices.

The paper reports and authors report language below denotes claims carried by the source bundle. The overall judgment is constructive and bounded: the work presents a legible, falsifiable research program, while broad transfer, production safety, and independent reproducibility remain open.

## 1. Problem framing and research question

Whether an audio-video fusion pathway provides repeatable value over audio-only emotion classification under the reported IEMOCAP setup is important because it joins representation, policy, and observable outcome. A credible review must ask what information enters, how state is formed, what objective shapes behavior, and which metric stands in for the intended effect.

The DEP-E is the archival object. Its manuscript is evidence about an earlier review, not independent confirmation of the underlying experiments. Agreement between its inventory and public locators supports identity and internal integrity; it does not convert author results into reproduced facts.

## 2. Source identity, integrity, and complete inventory

The source path is .lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion at commit a1ffd4737ce95c14f3a15251ee4fbba4403108a5. It contains exactly two tracked Markdown files: README.md and av_emotion_fusion_manuscript.md. Both files were read from beginning to end. The README supplies classification, inventory, public context, insights, and attribution. The manuscript supplies metadata, evidence ledger, detailed reconstruction, claims, method, constraints, observations, proposed extensions, references, and validation notes.

The canonical public locator is https://arxiv.org/abs/2006.08129; a persistent or related locator is https://github.com/julieeF/CS231N-Project. The complete canonical paper was not independently used to validate all paper-level detail in this run. No source document was uploaded, no source Markdown copied, and the source record remains unchanged.

## 3. Technical reconstruction of the method

The source compares CNN, CNN+LSTM, and CNN+RNN audio classifiers with a multimodal model that concatenates a CNN+RNN audio representation and a 3D-CNN video representation. An optional contrastive phase pulls matched audio-video clips together and separates different-clip pairs, including same-emotion hard cases, before supervised classification. The record also reconstructs spectrogram preparation, frame sampling and face cropping, balancing, augmentation, and hyperparameter choices.

The information path is observation, representation, objective or policy, outcome, and evidence. This decomposition makes alternatives visible: a gain may arise from the named mechanism, additional information, preprocessing, tuning, baseline configuration, or evaluation. The DEP-E provides partial separation; the replication agenda supplies the missing controls.

### 3.1 Assumptions

The method assumes that observed or simulated data cover structures needed at evaluation, metrics are meaningful proxies, preprocessing introduces no hidden advantage, and baselines receive a fair search budget. Each assumption is a possible failure mode.

### 3.2 Reproducibility-relevant details

A reproduction needs immutable source and code versions, data identity and splits, preprocessing, seeds, initialization, optimization, stopping rules, dependencies, hardware where material, and exact metrics. Missing details are not guessed.

## 4. Experimental design and evidence reconstructed

The paper uses four IEMOCAP labels and also a three-label task that removes happiness. Reported class counts are balanced by repetition or reduction, but the relationship among 1,600-per-class counts, 400 validation examples per class, and an 80/20 split is ambiguous. The review identifies possible lineage leakage, no speaker-disjoint repeated folds, no uncertainty intervals, no calibration, no video-only baseline in the central table, and no reproduction.

The design addresses the question at its stated scale. Its domain remains bounded by data or simulator coverage, participant sampling where applicable, baselines, metrics, sample size, and version. A strong audit matches information, tuning, and compute budgets; retains negative cases; and reports uncertainty. Unspecified controls remain unspecified.

## 5. Results and quantitative audit

Four-class accuracy is 52.23% for CNN, 39.77% for CNN+LSTM, 54.00% for CNN+RNN, and 51.94% for fused CNN+RNN+3DCNN. On sadness, anger, and neutral, audio-only reaches 70.25% and fusion 71.75%, a 1.50 percentage-point gain; on four classes fusion is 2.06 points worse. Noise cleanup and the chosen rotation/cropping augmentation do not help. Five contrastive pretraining epochs reportedly beat ten by 0.5 points. These are author-reported validation outcomes without repeated-run uncertainty.

These values are source-reported. They were checked for internal consistency in the complete DEP-E but not recalculated from raw observations. Denominators, uncertainty, thresholds, and configuration determine their meaning. Unlike metrics are not averaged into a synthetic score.

### 5.1 Statistical and operational limits

Point estimates do not reveal seed, sampling, or scenario variance unless reported. Operational readiness additionally requires latency distribution, resource use, recovery, calibration, monitoring, and out-of-distribution tests.

### 5.2 Negative and mixed evidence

Mixed outcomes identify tradeoffs or incomplete causal accounts. They are retained as evidence and become targets for falsification rather than being discarded.

## 6. Ablations and causal evidence

The source varies architecture, augmentation, denoising, label set, and contrastive duration, but does not isolate visual value with video-only, shuffled-pair, masked-stream, temporal-offset, or quality-gated controls. Removing happiness changes the task rather than repairing the same four-class classifier. A causal fusion test needs speaker-group splits and identical lineage across audio-only, video-only, and fused models.

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

The public locator https://arxiv.org/abs/2006.08129 and related identifier https://github.com/julieeF/CS231N-Project anchor identity and context.[^paper] They do not independently supply a reproduction. Related work named by the DEP-E is contextual, not confirmation.

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

Reframe multimodal prediction as conditional evidence routing. Audio and video should each expose quality and uncertainty signals; a gate should choose audio, video, fusion, or abstention per condition. The objective is not maximum aggregate fusion accuracy but reliable incremental evidence under corruption and disagreement.

This is reviewer inference, not an author claim. It names an internal state, consumer, intervention, evidence trace, and falsification path. An architectural analogy never transfers thresholds, learned parameters, safety guarantees, or rankings to a new domain.

## 11. Research notes and caveats

### 1. Critical note

Repeated oversampling increases count without adding speakers or recording conditions and can leak correlated descendants if splitting happens later. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

### 2. Critical note

Emotion labels are interpretive and sensitive; this evidence does not authorize consequential or covert inference. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

### 3. Critical note

The 1.50-point three-class gain is smaller than the unreported uncertainty and coexists with a four-class regression. This changes causal interpretation, portability, or the maximum safe claim. It is a reviewer assessment, not an assertion that the source authors ignored the issue.

Failures should be retained by category: observation shift, representation loss, objective mismatch, calibration error, comparison imbalance, and operational constraint violation. A future package needs enough state to trace each failure.

## 12. Implications

1. **Fusion should be released only after per-class, speaker-disjoint, corruption, and missing-modality tests.** This is a system and evidence implication, not reproduced capability.
2. **Raw audiovisual data and inferred affect labels require consent, minimal retention, and explicit prohibited-use controls.** This is a system and evidence implication, not reproduced capability.
3. **Calibration, abstention, and a unimodal fallback are separate requirements from classifier accuracy.** This is a system and evidence implication, not reproduced capability.

The archival implication is to bind every restatement to source version, evidence class, and reproduction status.

## 13. Falsifiable hypotheses

### Hypothesis 1

**Proposition:** A quality-gated mixture of unimodal experts outperforms unconditional concatenation under side-view video and corrupted audio.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

### Hypothesis 2

**Proposition:** Speaker-disjoint repeated folds reduce the apparent three-class fusion advantage relative to a random utterance split.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

### Hypothesis 3

**Proposition:** Tracked-face inputs improve visual contribution only on clips with adequate pose and temporal alignment, leaving an abstention region elsewhere.

**Falsification condition:** Under matched data, information, compute, tuning, and evaluation, the predicted effect is absent or reverses across independent seeds or scenario strata.

**Measurement:** Pre-register the primary endpoint, retain all runs, report uncertainty, and compare with the strongest mechanism-matched baseline.

## 14. Replication and falsification agenda

1. Recover exact datasets, preprocessing, splits, and reference implementation or reconstruct them from the paper.
2. Repeat classification with fixed and published folds, multiple random seeds, and confidence intervals.
3. Match embedding dimension and tuning budget across Audio-video emotion fusion archival intake, node2vec, attribute-only, and modern GNN baselines.
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

The decisive archival question is whether an audio-video fusion pathway provides repeatable value over audio-only emotion classification under the reported IEMOCAP setup. The source bundle supports a bounded answer through its internal inventory, cited locators, mechanism reconstruction, and reported observations. It does not supply independent execution evidence in this run. Accordingly, identity and source transcription receive the highest confidence; causal, comparative, portability, and operational conclusions receive progressively lower confidence unless the bundle records matched controls.

The strongest current evidence is: Four-class accuracy is 52.23% for CNN, 39.77% for CNN+LSTM, 54.00% for CNN+RNN, and 51.94% for fused CNN+RNN+3DCNN. On sadness, anger, and neutral, audio-only reaches 70.25% and fusion 71.75%, a 1.50 percentage-point gain; on four classes fusion is 2.06 points worse. This is preserved because it materially determines the source's contribution and its failure boundary. The weakest link is not filled by analogy or narrative. It is converted into the replication and falsification agenda, with an explicit adverse-result condition.

A future reviewer should first verify immutable input or asset identity, then reconstruct the smallest decisive comparison, then expose raw per-run or per-platform outcomes before expanding scope. Any change in source state must retain this pair and create a correction record. This order protects provenance, makes disagreement auditable, and prevents a later successful test from being retroactively attributed to evidence that the present DEP-E never contained.

### Minimum future evidence increment

The next useful increment is not more narrative. It is a small, version-pinned evidence bundle that executes the decisive comparison, exposes raw observations and failures, and tests the most important boundary condition under matched controls. That increment should be designed so an adverse result remains publishable and directly narrows the claim.

## 15. Durable restatement

### Review protocol and decision rule

The archival decision follows a conservative rule. A statement enters the durable restatement only when its mechanism is visible in the complete source bundle, its evidence type is named, and its scope can be expressed without borrowing confidence from an uninspected artifact. Numerical rankings remain paper-reported claims even when the table was directly read.[^claims] Reviewer proposals are allowed only when they include a falsifier or a concrete replication step. This prevents an attractive interpretation from becoming indistinguishable from an observed result.

The same rule applies to repository provenance. The paired task indicator binds this newly generated artifact to one source path and one immutable source state.[^pair] It does not declare ownership of the source, move a document, or collapse the DEP-E and DEP-A classes. A later correction should create another pair tied to the changed source commit so that readers can compare states without overwriting the earlier review.

For future use, the most important acceptance test is explanatory: a reviewer should be able to identify the input evidence, the transformation or decision mechanism, the metric, the strongest counterexample, and the reproduction gap without consulting private run data. If any of those elements is missing, the artifact can still guide discovery, but it should not be used to justify a high-consequence decision. This standard keeps the review useful when software, datasets, and benchmark rankings age.


> Audio-video emotion fusion archival intake's lasting idea is that scalable joint representation can be built from local agreements between graph structure and attributes. For provenance-sensitive archives, those agreements should propose relationships, while explicit evidence decides which relationships become authoritative.

This is the claim that should survive metric drift and ecosystem change. It preserves the mechanism and evidence limit without freezing a provisional ranking into an archival fact. It also keeps proposing a graph relationship separate from admitting that relationship as evidence-backed archival knowledge. That distinction remains important even when a newer embedding method replaces Audio-video emotion fusion archival intake.

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

- Primary public locator: https://arxiv.org/abs/2006.08129
- Source-record public locator: https://arxiv.org/abs/2006.08129[^paper]
- Related or persistent locator: https://github.com/julieeF/CS231N-Project[^doi]
- Immutable DEP-E record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion

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

[^paper]: Emotion Recognition in Audio and Video Using Deep Neural Networks; https://arxiv.org/abs/2006.08129; related identifier https://github.com/julieeF/CS231N-Project. Used as evidence, not instruction.
[^dep]: Complete source record at .lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion, commit a1ffd4737ce95c14f3a15251ee4fbba4403108a5; both tracked files reviewed in place.
[^doi]: Persistent identifier: https://github.com/julieeF/CS231N-Project
[^boundary]: Reproduction boundary: no code was executed and no reported result was independently reproduced.
[^claims]: Source-bundle claims were checked against the complete DEP-E record but were not recomputed or independently reproduced.
[^pair]: Paired task indicator `BL-DEPPAIR-20260714-5809B81B` records the one-way `DEP-E -> DEP-A` relationship.
