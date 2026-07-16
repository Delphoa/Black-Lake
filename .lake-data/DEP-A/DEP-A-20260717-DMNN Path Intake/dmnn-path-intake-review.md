# Conditional Width and Depth Through Gated Paths

## a whitepaper-grade archival intake review of the DMNN Conditional Paths DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths`
**Source commit:** `695f4473ebb1174f78bd9a027184a7fb8bf2847e`
**Paired task indicator:** `BL-DEPPAIR-20260717-AE70F5FC`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-07-17
**Review scope:** complete two-file repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is a paper-centered DEP-E review of Dynamic Multi-path Neural Network, arXiv:1902.10949v3. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

DMNN demonstrates that gated sub-block routes can vary effective width and depth and improve the reported accuracy-FLOP frontier, but arithmetic sparsity is only a proposal for systems efficiency until batching, compiler, memory, latency, energy, route stability, and fallback behavior are measured end to end.

The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- DMNN demonstrates that gated sub-block routes can vary effective width and depth and improve the reported accuracy-FLOP frontier, but arithmetic sparsity is only a proposal for systems efficiency until batching, compiler, memory, latency, energy, route stability, and fallback behavior are measured end to end.
- Residual and MobileNet blocks are divided into N candidate sub-block paths. A gate vector chooses a subset for each input, changing effective width and allowing entire transformed blocks to become inactive, thereby changing depth as well.
- The controller combines a current feature summary with prior controller state. Category-supervised signals during training encourage semantically informed routing and are removed at inference, while the recurrent state lets earlier decisions influence later paths.
- Training combines classification, controller/category supervision, and a resource penalty that targets an average execution rate. The rate is a differentiable training control over estimated active arithmetic, not a service-level guarantee.

### Principal qualifications

1. Dynamic branches can fragment accelerator batches and erase FLOP savings.
2. Controller overhead excludes memory, synchronization, compilation, and rare-route costs.
3. Category-supervised routing may not transfer to new taxonomies or unlabeled domains.
4. Missing code, repeated seeds, and route traces prevent independent verification and stability analysis.

## 1. Problem framing and research question

Static convolutional networks spend similar nominal compute on easy and difficult inputs, while coarse dynamic networks skip whole blocks and vary depth only. DMNN partitions transformed blocks into candidate paths and uses a recurrent, category-informed controller to activate subsets. The evidence question is whether lower active FLOPs translate into realized device efficiency without hidden accuracy, batching, or route-instability costs.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

Residual and MobileNet blocks are divided into N candidate sub-block paths. A gate vector chooses a subset for each input, changing effective width and allowing entire transformed blocks to become inactive, thereby changing depth as well.

### 2.2 Stage 2

The controller combines a current feature summary with prior controller state. Category-supervised signals during training encourage semantically informed routing and are removed at inference, while the recurrent state lets earlier decisions influence later paths.

### 2.3 Stage 3

Training combines classification, controller/category supervision, and a resource penalty that targets an average execution rate. The rate is a differentiable training control over estimated active arithmetic, not a service-level guarantee.

### 2.4 Stage 4

Realized efficiency depends on route distribution and runtime realization. Gate inference, mask materialization, kernel launch, memory traffic, synchronization, divergent batches, rare paths, and dense fallback can dominate even when mean FLOPs decline.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `dmnn_conditional_paths_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `695f4473ebb1174f78bd9a027184a7fb8bf2847e`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

DMNN is a per-input execution contract. The controller assigns a bounded compute plan, the network executes that plan, and telemetry must prove the plan saved the claimed resource without violating quality or latency. The analogy fails if the budget is measured only in FLOPs or if uncommon routes have no safe compiled realization. The transferable design principle is to optimize against a measured cost model and retain a dense fallback for unstable or unsupported routes.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

The source reports DMNN-50 with two paths and target 0.5 at 23.50 percent ImageNet top-1 error and 2.28G FLOPs, compared with the authors' ResNet-50 at 23.51 percent and 3.96G. The 57.6 percent FLOP ratio is an arithmetic estimate, not measured latency.

### 7.2 Evidence unit 2

A two-path DMNN-101 target-0.5 point reports 21.95 percent error at 4.21G versus the authors' ResNet-101 at 22.02 percent and 7.67G. A four-path DMNN-50 target-0.7 point reports better accuracy at higher active compute, showing the controller acts as adaptive capacity rather than pruning alone.

### 7.3 Evidence unit 3

The controller ablation reports 23.25 percent error for a baseline controller, 23.09 with previous state, 23.20 with category information, and 22.57 with both. This supports complementarity within one setup but lacks repeated-seed uncertainty and matched training-budget controls.

### 7.4 Evidence unit 4

MobileNetV2 and CIFAR-100 results extend the pattern, but the source found no official code, checkpoints, route traces, environment, device telemetry, or compiler analysis. Deployment-efficiency and reproducibility claims therefore remain open.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| DMNN varies effective width and depth per input. | Gated sub-block architecture and controller flow reconstructed by the DEP-E. | Directly supported as a method description; implementation not inspected. |
| DMNN-50 matches ResNet-50 at 57.6 percent of FLOPs. | Source-reported ImageNet table. | Supported as an author arithmetic/accuracy point, not a latency result. |
| Prior state and category information improve routing. | Single controller ablation table. | Promising component evidence without seed or budget controls. |
| DMNN is more efficient in deployment. | No matched device latency, memory, energy, throughput, or compiler study. | Not established. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/1902.10949v3](https://arxiv.org/abs/1902.10949v3) — Canonical metadata and abstract checked directly in this run.
- [https://arxiv.org/pdf/1902.10949](https://arxiv.org/pdf/1902.10949) — Canonical complete-paper locator used by the source DEP-E.
- [https://ar5iv.labs.arxiv.org/html/1902.10949](https://ar5iv.labs.arxiv.org/html/1902.10949) — Approved full-paper HTML fallback used by the source DEP-E.
- [https://doi.org/10.48550/arXiv.1902.10949](https://doi.org/10.48550/arXiv.1902.10949) — Persistent arXiv DOI.
- [https://github.com/Delphoa/Black-Lake](https://github.com/Delphoa/Black-Lake) — Repository containing the complete reviewed source record.

### Associated DEP records

- `.lake-data/DEP-A/DEP-A-20260716-AFIDAF Filters Intake` — verified related DEP-A; it does not replace or complete this pair.
- `.lake-data/DEP-A/DEP-A-20260714-HSD FTI-FDet` — verified related DEP-A; it does not replace or complete this pair.
- `.lake-data/DEP-A/DEP-A-20260714-SMES Expert Sparsity` — verified related DEP-A; it does not replace or complete this pair.

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

**Proposition:** If arithmetic sparsity survives system realization, common route signatures compiled as static graphs should reduce p95 latency and energy at matched accuracy across more than one device.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** If controller context is causal, removing previous state should increase route inconsistency across adjacent layers and reduce benefit most on ambiguous inputs.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** If category supervision generalizes, hierarchy-free training and unseen-class evaluation should preserve useful compute allocation rather than collapse to frequent training routes.

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

> DMNN demonstrates that gated sub-block routes can vary effective width and depth and improve the reported accuracy-FLOP frontier, but arithmetic sparsity is only a proposal for systems efficiency until batching, compiler, memory, latency, energy, route stability, and fallback behavior are measured end to end.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | inventory, quantitative synopsis, systems boundary, related records, attribution | fully read; source files withheld |
| `dmnn_conditional_paths_manuscript.md` | metadata, architecture, objectives, tables, ablations, limitations, proposals, appendix | fully read; paper results remain DEP-E-reported |
| `architecture` | sub-block paths, gates, recurrent state, category supervision | width/depth distinction and inference removal preserved |
| `training objective` | classification, category, and target execution-rate losses | rate distinguished from device SLO |
| `ImageNet table` | ResNet-50/101 and MobileNetV2 accuracy-FLOP points | parameters, FLOPs, and no-latency boundary retained |
| `CIFAR and controller ablation` | four-path result and prior-state/category comparisons | single-setting and no-seed limitations retained |
| `availability and runtime` | no official code, traces, telemetry, compiler evidence | negative evidence preserved |
| `proposed auditor` | route telemetry, compiled signatures, Pareto and shift tests | reviewer proposal labeled |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260717-AE70F5FC` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-DMNN%20Conditional%20Paths
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/695f4473ebb1174f78bd9a027184a7fb8bf2847e
[^primary-one]: Primary public source: https://arxiv.org/abs/1902.10949v3
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/pdf/1902.10949
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
