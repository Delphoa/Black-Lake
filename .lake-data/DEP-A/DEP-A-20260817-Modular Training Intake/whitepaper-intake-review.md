# Module-Selective Training Through Tangent Spectra

## a whitepaper-grade archival intake review of DEP-E-20260816-Train Faster Perform

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260816-Train Faster Perform`
**Source commit:** `81b588d864e26b3ed63be7d1c7e947940bb4a3c3`
**Paired task indicator:** `BL-DEPPAIR-20260817-C33A5129`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-08-17
**Review scope:** complete tracked repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is the complete DEP-E record centered on Train Faster, Perform Better: Modular Adaptive Training in Over-Parameterized Models (arXiv:2405.07527), plus the complete 19-page canonical paper. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

Modular Adaptive Training uses module-wise neural tangent information to update only modules whose estimated contribution clears a dynamic threshold. The paper reports substantial compute reductions on BERT, Switch Transformer, and VGG16 while preserving or improving selected metrics, but the estimator overhead, threshold sensitivity, and overparameterized-theory assumptions limit any universal efficiency guarantee.

The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- Modular Adaptive Training uses module-wise neural tangent information to update only modules whose estimated contribution clears a dynamic threshold. The paper reports substantial compute reductions on BERT, Switch Transformer, and VGG16 while preserving or improving selected metrics, but the estimator overhead, threshold sensitivity, and overparameterized-theory assumptions limit any universal efficiency guarantee.
- A modular neural tangent kernel decomposes training dynamics by network component. Principal eigenvalue estimates serve as proxies for each module's current contribution to optimization.
- A dynamic threshold selects active modules; only those above the criterion receive updates while the others remain frozen for that interval.
- The selection is recomputed during training, allowing modules to re-enter rather than imposing one static pruning mask. Average activation frequency is therefore distinct from permanent parameter removal.

### Principal qualifications

1. PFLOP accounting may omit wall-clock synchronization, eigenvalue estimation, data movement, and hardware underutilization caused by dynamic module selection.
2. Theoretical convergence conditions for overparameterized or locally linearized models may not predict practical nonconvex training behavior.
3. Threshold schedules add hyperparameters and can preferentially starve modules whose contribution appears late or is poorly estimated.
4. Three model-task families do not establish benefits for long-context, multimodal, reinforcement-learning, or distributed production training.

## 1. Problem framing and research question

Large networks contain modules whose marginal contribution changes through training, yet ordinary optimization updates all trainable weights every step. The paper asks whether a module-level spectral signal can allocate compute dynamically without sacrificing convergence or final performance.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

A modular neural tangent kernel decomposes training dynamics by network component. Principal eigenvalue estimates serve as proxies for each module's current contribution to optimization.

### 2.2 Stage 2

A dynamic threshold selects active modules; only those above the criterion receive updates while the others remain frozen for that interval.

### 2.3 Stage 3

The selection is recomputed during training, allowing modules to re-enter rather than imposing one static pruning mask. Average activation frequency is therefore distinct from permanent parameter removal.

### 2.4 Stage 4

Theory analyzes convergence in an overparameterized regime, while experiments apply the procedure to BERT on WikiText-2, Switch Transformer on WikiText-103, and VGG16 on CIFAR-10.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `train_faster_perform_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `81b588d864e26b3ed63be7d1c7e947940bb4a3c3`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

MAT is a compute scheduler whose sensor is local tangent-spectrum energy. The right assurance question is whether that sensor predicts counterfactual loss reduction per unit of real hardware cost. This reframing requires calibrating spectral estimates against skipped-update regret, not only reporting end metrics and theoretical bounds.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

For BERT, the convergence table reports 16.50 PFLOPs for MAT versus 28.70 for the standard BERT baseline, with test log perplexity 4.27 versus 4.41.

### 7.2 Evidence unit 2

For VGG16, the paper reports convergence at 9.03 PFLOPs versus 17.14, with test accuracy 93.86 percent versus 93.77 percent.

### 7.3 Evidence unit 3

The Switch Transformer study reports lower validation perplexity at compared budgets and a 10.4-percent improvement in test perplexity under the paper's stated comparison.

### 7.4 Evidence unit 4

Modules are active for roughly 34 percent of epochs on average, and reported compute savings across settings range from 26.4 to 50.9 percent. Kernel estimation and selection overhead are acknowledged and must remain in total-cost accounting.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| Module-selective training can reduce reported compute while preserving or improving selected task metrics. | BERT, Switch Transformer, and VGG16 tables report lower PFLOPs and comparable or improved perplexity or accuracy. | Supported for the reported configurations; wall-clock and hardware generalization remain open. |
| Principal mNTK eigenvalues causally identify the modules worth updating. | Theory and empirical selection behavior motivate the proxy, but matched alternative schedulers and counterfactual module updates are limited. | Promising, not fully isolated as the causal explanation. |
| The method guarantees faster training for any overparameterized model. | The assumptions and overhead are setting dependent, and experiments cover three model-task families. | Rejected as universal. |
| This intake reproduced MAT. | The canonical PDF was read independently of the DEP-E excerpt, but no training, spectrum estimation, or cost measurement was run. | Rejected. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2405.07527](https://arxiv.org/abs/2405.07527) — Canonical arXiv identity and version record.
- [https://arxiv.org/pdf/2405.07527](https://arxiv.org/pdf/2405.07527) — Complete canonical paper inspected; no source document uploaded.
- [https://doi.org/10.48550/arXiv.2405.07527](https://doi.org/10.48550/arXiv.2405.07527) — Persistent arXiv DOI.

### Associated DEP records

- No associated DEP record was asserted beyond relationships verified in the selected source.

External context is used to verify identity, locate complete evidence, and clarify version or implementation status. It is not added to inflate the selected source's evidentiary weight. A related paper, code repository, or DEP can make a mechanism easier to understand without independently reproducing the result.


## 11. Research notes and critical considerations

The first audit obligation is identity. A durable review binds every conclusion to an immutable repository source state and to stable public source locators. Titles and short names are insufficient because papers change versions, code changes behavior, and composite records can be corrected without changing their topic. The source commit and paired task indicator are therefore evidence, not administrative decoration.

The second obligation is denominator integrity. Every reported metric needs its unit of analysis, included and excluded cases, aggregation rule, configuration-selection process, and failure policy. A result conditioned on successful parsing, feasible compilation, completed generation, or selected checkpoints describes that conditional population. It must not be silently presented as end-to-end performance.

The third obligation is coordinate matching. Model revision, data split, preprocessing, random seed, prompt, judge, optimizer, hardware, budget, and stopping rule define the coordinates of an empirical claim. Comparisons made in different coordinates may still be informative, but they are not controlled evidence of one component's causal contribution. This intake uses calibrated phrases such as “paper reports,” “DEP-E reports,” and “supported under tested conditions” to keep that distinction visible.

The fourth obligation is negative evidence. Missing code, absent seeds, unreconciled tables, ambiguous operators, unavailable raw traces, and lack of external validation are findings. They do not prove a method is wrong, but they limit the strength and reuse of its claims. A public archival artifact should preserve those limits rather than optimize for a favorable narrative.

Finally, reproducibility is a ladder: an artifact can be available, inspectable, runnable, result-reproducing, and independently replicated. This review establishes inspectability for the selected DEP-E and directly checked public evidence. It does not claim execution or reproduction. The experiments were not independently rerun or reproduced.

## 12. Potential implications and failure modes

For research intake, the practical unit should be a claim-evidence-condition tuple. A headline claim without its metric, denominator, and tested envelope is too weak for downstream automation. A condition without immutable source identity is too unstable for audit. The derived DEP-A therefore treats provenance, mechanism, evidence, and limitations as linked records.

For implementation, stage boundaries should be observable. Inputs, transformations, selected policies, outputs, validator results, and failures should be recorded without exposing sensitive data in public summaries. If a learned judge or heuristic influences data selection, its identity and disagreement should be logged separately from the target system's result.

For governance, high-impact uses need independent domain review. Passing a source-integrity validator or reproducing a benchmark does not certify security, clinical safety, legal compliance, fairness, privacy, or production readiness. The methodology provides auditability, observability, and traceable lineage only.

Common failure modes include distribution shift, silent exclusion of hard cases, leakage across splits, selection on the evaluation set, metric gaming, stale calibration, correlated evaluators, uncounted preprocessing cost, and deployment hardware that changes the resource tradeoff. Each requires an explicit falsifier and stop condition.


## 13. Falsifiable hypotheses

The following are reviewer inferences and proposals, not findings of the source:

### Hypothesis 1

**Proposition:** Measured skipped-update regret will correlate more strongly with principal mNTK eigenvalues than with gradient norm at equal estimator cost.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Hardware-aware thresholds based on wall-clock throughput will retain less theoretical compute savings but deliver larger realized speedups.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** Late-activating modules will account for most performance loss when the threshold schedule is made aggressively sparse.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

## 14. Deployment and governance considerations

Appropriate use begins with bounded offline research, explicit data rights, immutable configuration, and human approval. High-stakes or production uses require domain-specific validation, threat modeling, access control, privacy review, monitoring, rollback, and incident handling outside the scope of this archival intake.

Every promotion decision should retain raw metric components, slice outcomes, exclusions, uncertainty, and cost. Composite scores may summarize but must not hide a failed safety, quality, fairness, or resource floor. A learned evaluator should never be the sole authority for the system it trained or selected.

Public artifacts should contain stable source locators and public-safe evidence only. Private source files, caches, credentials, execution traces, user data, and machine-specific paths remain outside the repository. Corrections append new provenance rather than silently rewriting prior evidence.

## 15. Replication and falsification agenda

1. **Identity gate.** Pin paper version, code commit, dataset revision, model/checkpoint, prompts, preprocessing, dependency lock, hardware, and evaluation policy. Verify licenses separately for each artifact.
2. **Source conformance.** Reconstruct every equation, table definition, exclusion rule, and configuration from complete primary evidence. Unit-test ambiguous thresholds, operators, and sign conventions before running expensive work.
3. **Baseline reproduction.** Reproduce baseline outputs first. A proposed-method result is uninterpretable if the local baseline does not match the reported operating range.
4. **Matched comparison.** Equalize data access, tuning/search budget, compute, preprocessing, failure handling, and metric code. Preserve per-case outputs and selection logs.
5. **Uncertainty.** Use repeated seeds, patient/group-aware folds, or repeated scenarios as appropriate. Report intervals and effect distributions, not only selected point estimates.
6. **Negative controls.** Shuffle, invert, or remove the proposed signal while matching capacity. Test whether the named mechanism, rather than extra parameters or search, explains the result.
7. **Shift tests.** Evaluate neighboring models, datasets, devices, workloads, and temporal states. Declare the envelope in which calibration or configuration is valid.
8. **Failure accounting.** Count refusals, parse failures, infeasible cases, timeouts, out-of-memory states, and discarded samples. Report conditional and end-to-end metrics separately.
9. **Operational measurement.** Include preprocessing, calibration, service calls, data generation, storage, communication, synchronization, and retries in cost claims.
10. **Independent review.** Separate the team or evaluator that constructs evidence from the authority that approves deployment. Archive the final evidence card and stop decision.

The agenda is successful if it can disconfirm the mechanism. A rerun that reproduces only a headline average is insufficient when the causal signal, denominator, or resource boundary remains untested.

## 16. Durable restatement

> Modular Adaptive Training uses module-wise neural tangent information to update only modules whose estimated contribution clears a dynamic threshold. The paper reports substantial compute reductions on BERT, Switch Transformer, and VGG16 while preserving or improving selected metrics, but the estimator overhead, threshold sensitivity, and overparameterized-theory assumptions limit any universal efficiency guarantee.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | complete manifest and attribution boundary | read from beginning to end; headings, tables, claims, URLs, limitations, proposals, and attribution accounted for |
| `train_faster_perform_manuscript.md` | complete substantive artifact with 2212 words | read from beginning to end; headings, tables, claims, URLs, limitations, proposals, and attribution accounted for |
| `arXiv:2405.07527 complete canonical PDF` | Train Faster, Perform Better: Modular Adaptive Training in Over-Parameterized Models; 19 pages, 9608 extracted words, 10 table-caption candidates, 9 figure-caption candidates | every PDF page inspected and structurally inventoried; abstract, method, quantitative results, captions, limitations, appendices, and references checked; no experiment, proof, code, data, model, or benchmark rerun |
| `source metadata and evidence ledger` | identity, version, evidence roles, confidence, access status, and limitations | reconstructed with source DEP report, directly inspected primary evidence, reviewer inference, and proposals kept distinct |
| `method, equations, tables, figures, and appendices` | technical dataflow, objectives, evaluation coordinates, ablations, quantitative results, captions, and supplementary boundaries | material units accounted for in private maps; exact claims remain source-reported unless explicitly assessed |
| `limitations, proposals, references, and attribution` | failure modes, transfer limits, implementation ideas, reproduction boundary, public locators, and source-locality policy | limitations retained; proposals treated as hypotheses; source documents remained outside the public repository |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260817-C33A5129` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260816-Train%20Faster%20Perform
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/81b588d864e26b3ed63be7d1c7e947940bb4a3c3
[^primary-one]: Primary public source: https://arxiv.org/abs/2405.07527
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/pdf/2405.07527
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
