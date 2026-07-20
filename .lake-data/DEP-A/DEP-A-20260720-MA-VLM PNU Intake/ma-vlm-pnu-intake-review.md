# Disagreement Is Evidence, Not an Automatic Label

## a whitepaper-grade archival intake review of the MA-VLM PNU Moderation DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260719-MA-VLM PNU Moderation`
**Source commit:** `5211c0ea55952389dc988c2a37444aefcaadda67`
**Paired task indicator:** `BL-DEPPAIR-20260720-7713085A`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-07-20
**Review scope:** complete two-file repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is a paper-centered DEP-E review of Multi-Agent VLMs Guided Self-Training with PNU Loss, arXiv:2511.13759v1. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

The reusable mechanism is not the anthropomorphic multi-agent framing but an explicit three-state evidence model: human labels, bounded soft consensus, and unresolved disagreement. That structure can improve low-label self-training, yet two role prompts from one VLM are correlated judges, and aggregate Macro-F1 cannot establish fairness or authorize moderation consequences.

The primary object under review is the complete paper-centered DEP-E record. This run reopened canonical primary locators and directly checked source identity, version, and central claims, but it did not conduct a new page-by-page independent full-paper review. Paper-level details remain attributed to the DEP-E and the paper authors, and no result is represented as independently reproduced.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- The reusable mechanism is not the anthropomorphic multi-agent framing but an explicit three-state evidence model: human labels, bounded soft consensus, and unresolved disagreement. That structure can improve low-label self-training, yet two role prompts from one VLM are correlated judges, and aggregate Macro-F1 cannot establish fairness or authorize moderation consequences.
- A CLIP-Large classifier starts from n human labels and ranks the unlabeled pool. The top k=500 predictions enter a VLM review stage each round, while a development gate accepts or reverts the update.
- Strict moderator and lenient user personas exchange rationales and revise decisions. Agreement among classifier and both personas becomes Agreed-Unknown with soft targets 0.67 or 0.33; conflict becomes Disagreed-Unknown rather than a forced class.
- The PNU objective combines human PN risk, soft PN risk from consensus, and PU or NU risk from contested samples through dataset-specific gamma. The positive prior is fixed at 0.5, matching balanced working sets but not necessarily live prevalence.

### Principal qualifications

1. Two personas from one model family share training data, policy, and cultural blind spots; rationale exchange can manufacture consensus rather than independent evidence.
2. Balanced datasets, binary mappings, fixed class prior, and global gamma hide live prevalence and subgroup uncertainty.
3. Repeated accept/revert decisions against one development set can overfit the entire self-training trajectory.
4. Moderation errors have asymmetric harms; aggregate Macro-F1 omits subgroup false positives, appeals, reviewer well-being, and cultural validity.

## 1. Problem framing and research question

Offensive-content labels are scarce, culturally contingent, multimodal, and asymmetric in harm. The selected work trains a small CLIP classifier, asks strict-moderator and lenient-user personas of one frozen VLM to review high-confidence unlabeled items, promotes three-way agreement to soft pseudo-labels, and routes disagreement into a PNU objective. The archival task is to preserve reported gains while auditing correlated supervision, development gating, prevalence shift, fairness, and cost.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

A CLIP-Large classifier starts from n human labels and ranks the unlabeled pool. The top k=500 predictions enter a VLM review stage each round, while a development gate accepts or reverts the update.

### 2.2 Stage 2

Strict moderator and lenient user personas exchange rationales and revise decisions. Agreement among classifier and both personas becomes Agreed-Unknown with soft targets 0.67 or 0.33; conflict becomes Disagreed-Unknown rather than a forced class.

### 2.3 Stage 3

The PNU objective combines human PN risk, soft PN risk from consensus, and PU or NU risk from contested samples through dataset-specific gamma. The positive prior is fixed at 0.5, matching balanced working sets but not necessarily live prevalence.

### 2.4 Stage 4

The expensive Qwen-2.5-VL-72B teacher is training-time only; the deployed classifier is smaller. The full cost nevertheless includes repeated role calls, image processing, rationales, retries, iterations, development selection, and sensitive-content handling.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `ma_vlm_pnu_moderation_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `5211c0ea55952389dc988c2a37444aefcaadda67`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The primary object under review is the complete paper-centered DEP-E record. This run reopened canonical primary locators and directly checked source identity, version, and central claims, but it did not conduct a new page-by-page independent full-paper review. Paper-level details remain attributed to the DEP-E and the paper authors, and no result is represented as independently reproduced. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

Use an evidence-state machine rather than an agent vote. Each sample carries provenance, judge identities, calibrated agreement, disagreement reasons, human-label authority, and a maximum training weight. Consensus may influence offline learning; disagreement increases review priority; neither state triggers enforcement. This predicts that independent model or human diversity will be more valuable than extra role-play from one model.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

With 100 labels, combined self-training reports Macro-F1 72.68 on FHM, 73.49 on MAMI, 86.69 on HSOL, and 77.11 on Sentiment140, above supervised CLIP on all four tasks.

### 7.2 Evidence unit 2

The method does not dominate Qwen-7B: Qwen reports 76.06 on MAMI and 78.19 on Sentiment140 versus 73.49 and 77.11 for combined self-training. Teacher-only pseudo-labeling also underperforms classifier-only on some tasks.

### 7.3 Evidence unit 3

At 50 labels, combined self-training reports 71.27/71.40 on FHM/MAMI. At 250 labels it reports 72.97/74.79, below Qwen-7B's 75.88/76.18, suggesting its relative value is strongest under extreme scarcity.

### 7.4 Evidence unit 4

Dual-persona prompting reports MAMI 81.64 versus zero-shot 79.17, but FHM 74.62 versus 74.46. Gamma 0.0 is best on displayed FHM values and 0.1 on MAMI. Public code exists, but no run, dependency audit, fairness audit, or cost reproduction occurred here.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| Combined classifier and VLM evidence beats supervised CLIP at n=100 on four reported tasks. | Main Macro-F1 table. | Supported as reported; single-split and uncertainty limits remain. |
| Dual-persona review supplies independent social perspectives. | One base VLM with two role prompts and rationale exchange. | Not established as independence; the signals are correlated. |
| Disagreement contains useful training information. | PNU design and gamma ablations. | Promising and dataset dependent; FHM and MAMI prefer different settings. |
| The method is ready for automated moderation. | Benchmark metrics and public code. | Rejected without fairness, prevalence, calibration, human governance, cost, and live-outcome evidence. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2511.13759](https://arxiv.org/abs/2511.13759) — Canonical title, nine-author record, v1 date, AAAI-26 comment, DOI, license, and complete-text locators checked in this run.
- [https://arxiv.org/html/2511.13759](https://arxiv.org/html/2511.13759) — Authorized complete-paper locator reopened for primary context; no source document deposited.
- [https://github.com/Social-AI-Studio/MA-VLM](https://github.com/Social-AI-Studio/MA-VLM) — Official public implementation repository inspected as availability context; code was not executed.

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

**Proposition:** Independent model-family or blinded human judgments will improve consensus calibration more than reciprocal rationales between two roles of one VLM.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Nested holdouts will reduce the apparent benefit of the round-level revert gate relative to repeated selection on one development set.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** Per-sample bounded disagreement weights will outperform one dataset-level gamma on calibration and subgroup error while preserving Macro-F1.

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

> The reusable mechanism is not the anthropomorphic multi-agent framing but an explicit three-state evidence model: human labels, bounded soft consensus, and unresolved disagreement. That structure can improve low-label self-training, yet two role prompts from one VLM are correlated judges, and aggregate Macro-F1 cannot establish fairness or authorize moderation consequences.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | classification, inventory, summary, relationships, source policy, final attribution | read from beginning to end |
| `ma_vlm_pnu_moderation_manuscript.md` | metadata, evidence ledger, five-stage loop, PNU equations, datasets, tables, ablations, code context, governance, proposals, appendix | read from beginning to end; no content or code execution |
| `self-training loop` | ranking, top-k review, consensus/disagreement states, development revert | adaptive selection boundary retained |
| `dual-persona review` | moderator/user roles, rationale exchange, correlated-judge limitation | independence claim calibrated |
| `PNU objective` | soft targets, PU/NU risk, gamma and prior | dataset/prevalence sensitivity retained |
| `datasets and Tables 1-5` | FHM, MAMI, HSOL, Sentiment140, label counts, prompts, gamma | all material values and non-dominance accounted for |
| `official repository and reproducibility` | visible pipeline, demo data, no release/execution | availability separated from reproduction |
| `fairness, cost, implementations, exercises, references, integrity appendix` | human authority, sensitive data, evaluation agenda, no source upload | reviewer proposals labeled |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The primary object under review is the complete paper-centered DEP-E record. This run reopened canonical primary locators and directly checked source identity, version, and central claims, but it did not conduct a new page-by-page independent full-paper review. Paper-level details remain attributed to the DEP-E and the paper authors, and no result is represented as independently reproduced. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260720-7713085A` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-MA-VLM%20PNU%20Moderation
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/5211c0ea55952389dc988c2a37444aefcaadda67
[^primary-one]: Primary public source: https://arxiv.org/abs/2511.13759
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/html/2511.13759
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
