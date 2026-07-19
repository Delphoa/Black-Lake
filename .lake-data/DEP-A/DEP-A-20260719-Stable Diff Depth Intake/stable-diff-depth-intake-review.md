# Synthetic Condition Expansion Needs a Geometry Gate

## a whitepaper-grade archival intake review of the Stable Diffusion Depth DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth`
**Source commit:** `859396e38a37cf27e69dcef090c2b55851a1667f`
**Paired task indicator:** `BL-DEPPAIR-20260719-6D82E3CF`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-07-19
**Review scope:** complete two-file repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is a paper-centered DEP-E review of Stealing Stable Diffusion Prior for Robust Monocular Depth Estimation, arXiv:2403.05056v1, with project and repository availability evidence. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

The source's durable strategy is offline condition expansion followed by robustness distillation: a large generative pipeline proposes night and rain appearances, while a smaller DINOv2-DPT student learns from a day-clear teacher. That strategy is credible only with an independent geometry-preservation gate, resolved reliability-mask semantics, repeated factorial evidence, and real-domain calibration; none is established strongly enough for autonomous-driving readiness.

The primary object under review is the complete paper-centered DEP-E record. This run reopened canonical full-text locators and directly checked source identity and central claims, but it did not conduct a new page-by-page independent full-paper review. Paper-level details therefore remain explicitly attributed to the DEP-E and the paper authors.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- The source's durable strategy is offline condition expansion followed by robustness distillation: a large generative pipeline proposes night and rain appearances, while a smaller DINOv2-DPT student learns from a day-clear teacher. That strategy is credible only with an independent geometry-preservation gate, resolved reliability-mask semantics, repeated factorial evidence, and real-domain calibration; none is established strongly enough for autonomous-driving readiness.
- GDT uses BLIP-2 captions, MiDaS plus PatchFusion depth, Stable Diffusion 1.5, ControlNet, IP-Adapter, condition text, image prompts, and noise to propose night or rain variants. The controls intend to preserve content, style, and geometry but do not quantify corpus-wide geometric fidelity.
- A day-clear teacher and a DINOv2 ViT-base plus DPT student share the depth task. The teacher predicts pseudo-depth on original frames while the student sees original or translated frames; PoseNet supplies self-supervised reconstruction structure.
- Semantic loss aligns DINOv2 features across source and translation. The teacher reliability mask is intended to retain pixels where teacher photometric error is lower, but the printed Iverson inequality and multiplication appear to select teacher-worse pixels unless one symbol, inequality, or complement is reversed.

### Principal qualifications

1. Generated night or rain images can alter objects, edges, reflections, camera geometry, or depth while still looking plausible.
2. The teacher-mask equation/prose conflict can invert which pixels receive distillation and cannot be resolved without executable implementation evidence.
3. Single-run cumulative ablations, median scaling, two datasets, and selected qualitative panels limit causal, metric-scale, and generalization claims.
4. Autonomous use needs uncertainty, calibration, temporal consistency, fixed-denominator failure rates, target-device latency, abstention, and downstream control validation.

## 1. Problem framing and research question

Self-supervised monocular depth depends on photometric consistency, which darkness and weather violate. The paper uses Stable Diffusion controls to generate adverse appearances from day-clear frames and transfers pseudo-depth into a student. The archival task is to separate the generator, architecture, pseudo-label, and loss contributions, preserve metric non-dominance across datasets, and treat an equation/prose conflict and incomplete release as material findings.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

GDT uses BLIP-2 captions, MiDaS plus PatchFusion depth, Stable Diffusion 1.5, ControlNet, IP-Adapter, condition text, image prompts, and noise to propose night or rain variants. The controls intend to preserve content, style, and geometry but do not quantify corpus-wide geometric fidelity.

### 2.2 Stage 2

A day-clear teacher and a DINOv2 ViT-base plus DPT student share the depth task. The teacher predicts pseudo-depth on original frames while the student sees original or translated frames; PoseNet supplies self-supervised reconstruction structure.

### 2.3 Stage 3

Semantic loss aligns DINOv2 features across source and translation. The teacher reliability mask is intended to retain pixels where teacher photometric error is lower, but the printed Iverson inequality and multiplication appear to select teacher-worse pixels unless one symbol, inequality, or complement is reversed.

### 2.4 Stage 4

The cumulative ablation adds GDT/PatchFusion, teacher loss, DINOv2/DPT, and semantic loss. Because component order is fixed and seeds are not repeated, adjacent gains suggest mechanism but do not provide a factorial causal decomposition.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `stable_diffusion_depth_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `859396e38a37cf27e69dcef090c2b55851a1667f`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The primary object under review is the complete paper-centered DEP-E record. This run reopened canonical full-text locators and directly checked source identity and central claims, but it did not conduct a new page-by-page independent full-paper review. Paper-level details therefore remain explicitly attributed to the DEP-E and the paper authors. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

Treat the generator as a proposal engine and the student-training pipeline as a controlled acceptance process. Every generated pair must pass independent geometry, temporal, semantic, provenance, and condition-diversity gates before it can influence training; every rejected pair remains part of the denominator. This predicts that stricter gates will reduce synthetic volume but improve real adverse-condition calibration and failure visibility.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

On nuScenes, the student improves night absRel from 0.2103 to 0.1939 and rain absRel from 0.1718 to 0.1410 versus the teacher, while the teacher remains slightly better on night RMSE and day delta-1.

### 7.2 Evidence unit 2

On RobotCar, the student slightly improves day absRel and night delta-1, but the teacher remains better on night absRel, sqRel, and RMSE. Student superiority is therefore dataset- and metric-conditioned.

### 7.3 Evidence unit 3

The cumulative nuScenes ablation moves from 0.1513 absRel / 81.51 delta-1 to 0.1320 / 84.96, with the DINOv2-DPT swap producing the largest adjacent change. The first GDT substitution without PatchFusion is slightly worse than the GAN baseline.

### 7.4 Evidence unit 4

The official project repository evolved into UDE and presents method documentation and an MIT license, but the source-state audit found no executable code or weights at its pinned revision and the current page exposes no published release. This intake ran nothing.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| GDT preserves depth while diversifying adverse appearance. | Control streams and selected figures. | Promising but limited; geometry preservation is not measured across the generated corpus. |
| The student outperforms the teacher under challenging conditions. | nuScenes and RobotCar condition-specific tables. | Supported for selected nuScenes metrics; mixed on RobotCar and some nuScenes metrics. |
| Teacher loss filters unreliable pseudo-depth as printed. | Prose, Equations 5-6, and Iverson mask. | Unresolved; the printed inequality appears directionally inconsistent with the stated intent. |
| Code and weights make the work reproducible. | Official repository and current redirect. | Not established; release completeness and exact paper-to-code trace are insufficient, and nothing was run. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2403.05056](https://arxiv.org/abs/2403.05056) — Canonical title, three-author record, v1 date, subject, DOI, project and code locators checked in this run.
- [https://arxiv.org/pdf/2403.05056](https://arxiv.org/pdf/2403.05056) — Complete eighteen-page PDF reopened; mask equation, tables, figures, and cumulative ablation directly checked.
- [https://github.com/hitcslj/UDE](https://github.com/hitcslj/UDE) — Current official repository redirect and renamed framework inspected; README and license are visible, with no published release.

### Associated DEP records

- `.lake-data/DEP-A/DEP-A-20260717-UAV Localization Intake` — verified related DEP-A; it does not replace or complete this pair.
- `.lake-data/DEP-A/DEP-A-20260714-VideoWeave Geometry` — verified related DEP-A; it does not replace or complete this pair.
- `.lake-data/DEP-A/DEP-A-20260717-Stereo Lane Intake` — verified related DEP-A; it does not replace or complete this pair.

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

**Proposition:** An independent multi-view or stereo geometry gate will reject a nontrivial fraction of visually convincing GDT pairs and improve real night/rain calibration despite reducing training volume.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Unit-tested prose-consistent and printed mask variants will produce measurably different retained-pixel distributions and at least one result-table change.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** After repeated factorial ablations, DINOv2-DPT architecture will explain more of the aggregate gain than diffusion generation alone, while geometry-gated generation will explain more of adverse-condition robustness.

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

> The source's durable strategy is offline condition expansion followed by robustness distillation: a large generative pipeline proposes night and rain appearances, while a smaller DINOv2-DPT student learns from a day-clear teacher. That strategy is credible only with an independent geometry-preservation gate, resolved reliability-mask semantics, repeated factorial evidence, and real-domain calibration; none is established strongly enough for autonomous-driving readiness.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | classification, inventory, source policy, method summary, equation ambiguity, related records, and attribution | read from beginning to end |
| `stable_diffusion_depth_manuscript.md` | metadata, evidence ledger, GDT, teacher/student losses, experiments, tables, repository audit, proposals, and appendix | read from beginning to end; no source artifact executed |
| `GDT pipeline and Figure 3` | BLIP-2, MiDaS, PatchFusion, Stable Diffusion, ControlNet, IP-Adapter | component versions and geometry-assumption gaps retained |
| `teacher/student and Equations 4-7` | photometric reconstruction, mask, distillation, semantic alignment | mask-direction contradiction retained |
| `nuScenes and RobotCar tables` | day, night, rain metrics and median-scaling boundary | metric non-dominance retained |
| `Table 3 and Figures 5-6` | cumulative components and selected qualitative examples | order, seed, and selection limits retained |
| `official project and repository` | UDE redirect, renamed loss, README, MIT license, no published release | availability separated from reproduction |
| `source-integrity and replication appendix` | PDF/HTML/TeX verification, source withholding, no vehicle-control claim | negative evidence preserved |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The primary object under review is the complete paper-centered DEP-E record. This run reopened canonical full-text locators and directly checked source identity and central claims, but it did not conduct a new page-by-page independent full-paper review. Paper-level details therefore remain explicitly attributed to the DEP-E and the paper authors. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260719-6D82E3CF` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260718-Stable%20Diffusion%20Depth
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/859396e38a37cf27e69dcef090c2b55851a1667f
[^primary-one]: Primary public source: https://arxiv.org/abs/2403.05056
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/pdf/2403.05056
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
