# Conformal Evidence Envelopes for LLM Judging

## a whitepaper-grade archival intake review of the Judge Conformal DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260716-Judge Conformal`
**Source commit:** `695f4473ebb1174f78bd9a027184a7fb8bf2847e`
**Paired task indicator:** `BL-DEPPAIR-20260717-60D5570C`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-07-17
**Review scope:** complete two-file repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is a paper-centered DEP-E review of Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction, arXiv:2509.18658v1. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

The work is best understood as an evaluation-evidence envelope: token-logit features and held-out human ratings support split-conformal intervals whose coverage is conditional on exchangeability, while width, slice support, calibration age, judge/prompt identity, label quality, and review capacity determine whether those intervals are operationally useful.

The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- The work is best understood as an evaluation-evidence envelope: token-logit features and held-out human ratings support split-conformal intervals whose coverage is conditional on exchangeability, while width, slice support, calibration age, judge/prompt identity, label quality, and review capacity determine whether those intervals are operationally useful.
- A judge response is located at its rating token, and logits for numerical and verbal label variants become features for regression-style or ordinal conformal predictors.
- A disjoint calibration set yields nonconformity scores and a finite-sample quantile at target miscoverage alpha. Exchangeability and fixed pipeline identity are operational prerequisites.
- The discrete boundary transformation aligns continuous endpoints with legal rating labels and is reported to provide non-decreasing coverage under its construction. Expansion can increase width and review demand.

### Principal qualifications

1. Model, prompt, rubric, task, language, or annotator drift can invalidate exchangeability and stale intervals.
2. Marginal coverage can hide subgroup undercoverage and reproduce systematic human-label bias.
3. Wider intervals can improve coverage while overwhelming review capacity or enabling selective automation.
4. Tokenization, rating-position detection, logit access, and equivalent-token aggregation are brittle versioned dependencies.

## 1. Problem framing and research question

Point ratings from an LLM judge hide prompt sensitivity, model error, annotation disagreement, and decoding variability. The source reconstructs a single-pass logit-based conformal workflow for ordinal ratings, a boundary adjustment for legal labels, midpoint scoring, and reprompting. The archival task is to preserve conditional marginal validity without turning it into a claim of semantic correctness, subgroup fairness, or production durability.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

A judge response is located at its rating token, and logits for numerical and verbal label variants become features for regression-style or ordinal conformal predictors.

### 2.2 Stage 2

A disjoint calibration set yields nonconformity scores and a finite-sample quantile at target miscoverage alpha. Exchangeability and fixed pipeline identity are operational prerequisites.

### 2.3 Stage 3

The discrete boundary transformation aligns continuous endpoints with legal rating labels and is reported to provide non-decreasing coverage under its construction. Expansion can increase width and review demand.

### 2.4 Stage 4

Interval midpoints are evaluated as alternative scores, while interval-informed reprompting tests whether the judge changes a discrepant integer rating. The latter is prompt behavior, not part of the coverage guarantee.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `llm_judge_conformal_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `695f4473ebb1174f78bd9a027184a7fb8bf2847e`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

Build a judge evidence registry, not a confidence badge. Every interval carries its calibration split, support, target and observed coverage, width, method, judge/prompt/rubric versions, slice checks, shift state, and invalidation rules. Decisions route through allow, human review, or recalibrate states; a version mismatch fails closed, and label-quality or fairness audits can veto otherwise valid marginal coverage.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

The DEP-E describes SummEval with 1,600 and DialSumm with 1,400 cases, four approximately 200-example ROSCOE subsets, three judge models, two frameworks, nine conformal methods, 50/50 calibration-test splits, and 30 seeds.

### 7.2 Evidence unit 2

Boundary adjustment reportedly improves coverage broadly; one cited LVD e-SNLI configuration moves from 85.96% to 95.53%. Several settings still under-cover, so adjustment is not a universal 90% certificate.

### 7.3 Evidence unit 3

A highlighted GPT-4o-mini SummEval fluency example reports R2CCP midpoint MSE falling from 3.907 to 0.443, an 88.7% reduction. A midpoint remains a heuristic point summary, not a probability mean.

### 7.4 Evidence unit 4

Reprompting often reinforces the original rating rather than correcting it. The source repository is substantive but was not run; dependency locks, dataset reconstruction, API versions, license, and deterministic table regeneration remain unverified.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| Split conformal intervals can be formed from one judge pass and held-out labels. | DEP-E equations, experiment design, and code inventory. | Supported conditionally on exchangeability and stable feature extraction. |
| Boundary adjustment never reduces coverage. | Source Theorem 1 under the specified transformation. | Supported as source-reported theorem; not independently formalized. |
| Adjusted intervals guarantee production correctness. | No production shift or semantic correctness guarantee. | Not established. |
| Midpoint or reprompting fixes judge error. | Midpoint tables and reprompt analysis. | Midpoints are task-level heuristics; reprompting is unreliable. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2509.18658v1](https://arxiv.org/abs/2509.18658v1) — Canonical title, authors, version, and abstract checked in this run.
- [https://arxiv.org/html/2509.18658](https://arxiv.org/html/2509.18658) — Official full-paper locator used by the source DEP-E; not reopened page by page here.
- [https://github.com/BruceSheng1202/Analyzing_Uncertainty_of_LLM-as-a-Judge](https://github.com/BruceSheng1202/Analyzing_Uncertainty_of_LLM-as-a-Judge) — Official implementation surface pinned by the source DEP-E; not executed and no visible license was re-established here.
- [https://doi.org/10.48550/arXiv.2509.18658](https://doi.org/10.48550/arXiv.2509.18658) — Persistent arXiv DOI.

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

**Proposition:** A version-mismatch release gate will prevent more stale-evidence decisions than interval-informed reprompting because it acts on calibration validity rather than model persuasion.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Conditional slice evaluation will reveal undercoverage hidden by acceptable marginal coverage on low-support reasoning tasks.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** Nested method selection, calibration, and final test splits will reduce apparent coverage-width advantages compared with selecting methods on shared evaluation evidence.

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

> The work is best understood as an evaluation-evidence envelope: token-logit features and held-out human ratings support split-conformal intervals whose coverage is conditional on exchangeability, while width, slice support, calibration age, judge/prompt identity, label quality, and review capacity determine whether those intervals are operationally useful.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | classification, inventory, public-safe source handling, summary, relevance, and attribution | read from beginning to end |
| `llm_judge_conformal_manuscript.md` | metadata, evidence ledger, conformal construction, boundary theorem, datasets, tables, midpoint, reprompting, code, ethics, proposals, references, and appendix | read from beginning to end; paper-level claims remain DEP-E-reported |
| `Sections 3 and Appendix A.1` | logit features, split conformal, discrete adjustment, theorem and proof | method reconstructed; proof not independently formalized |
| `Section 4 and Tables 1-2` | dataset/model/method grid, coverage and width before/after adjustment | representative results and residual undercoverage retained |
| `midpoint results` | MSE, MAE, correlation, and highlighted fluency case | heuristic semantics preserved |
| `reprompting and calibration-size analyses` | judge resistance and support-size effects | routing interpretation separated from theorem |
| `official repository inventory` | predictors, scripts, notebooks, examples, pinned commit, missing visible license | inventory only; no execution or copying |
| `limitations and ethics` | exchangeability, drift, annotation bias, review capacity, consequential-use boundary | governance failures foregrounded |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260717-60D5570C` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Judge%20Conformal
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/695f4473ebb1174f78bd9a027184a7fb8bf2847e
[^primary-one]: Primary public source: https://arxiv.org/abs/2509.18658v1
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/html/2509.18658
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
