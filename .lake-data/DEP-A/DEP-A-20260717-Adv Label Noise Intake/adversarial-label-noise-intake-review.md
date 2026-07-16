# Soft-Target Rectification for Robust Overfitting

## a whitepaper-grade archival intake review of the Adversarial Label Noise DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260716-Adversarial Label Noise`
**Source commit:** `695f4473ebb1174f78bd9a027184a7fb8bf2847e`
**Paired task indicator:** `BL-DEPPAIR-20260717-8302F064`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-07-17
**Review scope:** complete two-file repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is a paper-centered DEP-E review of Label Noise in Adversarial Training: A Novel Perspective to Study Robust Overfitting, arXiv:2110.03135v4. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

The record's most defensible contribution is a target-correction view of robust overfitting: adversarial perturbation can make inherited one-hot labels a poor distributional target, and a robust teacher can reduce the best-to-last robustness gap, but global calibration and an existential theorem do not recover an unknown per-example semantic truth.

The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- The record's most defensible contribution is a target-correction view of robust overfitting: adversarial perturbation can make inherited one-hot labels a poor distributional target, and a robust teacher can reduce the best-to-last robustness gap, but global calibration and an existential theorem do not recover an unknown per-example semantic truth.
- A standard adversarial-training loop generates bounded adversarial examples but continues to optimize against inherited clean one-hot targets. The paper models the unobserved true distribution for an adversarial example as potentially different, so training sees a distribution mismatch rather than ordinary annotation noise alone.
- KD-AT-Auto trains a separate robust self-teacher. Correctly classified adversarial examples use the teacher distribution after temperature scaling; misclassified examples interpolate that distribution with the inherited one-hot target. Adversarial validation likelihood selects global temperature and interpolation parameters.
- The reported total-variation results are existence statements. Under the paper's cases and assumptions, a temperature or interpolation weight can improve mismatch to an unknown distribution. They do not identify that distribution, guarantee that global validation parameters improve every example, or establish semantic preservation.

### Principal qualifications

1. The central true-label distribution is latent, making the causal interpretation indirect.
2. A robust teacher can transfer its own calibration and threat-model errors into the target distribution.
3. Global validation parameters are not sample-wise optima despite the existence results.
4. Robust accuracy against selected attacks does not establish semantic, open-world, or adaptive robustness.

## 1. Problem framing and research question

Conventional adversarial training perturbs the input while retaining the clean example's label. The source DEP-E reconstructs the paper's proposal that the appropriate label distribution may shift after perturbation, creating implicit label noise that appears as robust overfitting and long-horizon epoch-wise double descent. The archival problem is to preserve the distinction between an observed gap reduction, a latent-label causal account, and the stronger claim that corrected targets equal human semantic labels.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

A standard adversarial-training loop generates bounded adversarial examples but continues to optimize against inherited clean one-hot targets. The paper models the unobserved true distribution for an adversarial example as potentially different, so training sees a distribution mismatch rather than ordinary annotation noise alone.

### 2.2 Stage 2

KD-AT-Auto trains a separate robust self-teacher. Correctly classified adversarial examples use the teacher distribution after temperature scaling; misclassified examples interpolate that distribution with the inherited one-hot target. Adversarial validation likelihood selects global temperature and interpolation parameters.

### 2.3 Stage 3

The reported total-variation results are existence statements. Under the paper's cases and assumptions, a temperature or interpolation weight can improve mismatch to an unknown distribution. They do not identify that distribution, guarantee that global validation parameters improve every example, or establish semantic preservation.

### 2.4 Stage 4

Evaluation measures robust best accuracy, robust last accuracy, and their gap across datasets, architectures, training methods, and attacks. The mechanism is most directly supported when the last-epoch value rises and the gap closes without a corresponding collapse in clean or peak robustness.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `adversarial_label_noise_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `695f4473ebb1174f78bd9a027184a7fb8bf2847e`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

The durable mechanism is a guarded target-repair loop. The system does not merely smooth labels; it asks whether the inherited supervision remains credible after the input transformation, then uses an auxiliary model to propose a distributional correction subject to held-out calibration. The analogy breaks where the auxiliary model is treated as an oracle. A transferable design must retain uncertainty, provenance, and an abstention path whenever the transformed example's semantic class is genuinely ambiguous.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

The DEP-E transcribes CIFAR-10 robust best/last accuracy of 47.35/41.42 for ordinary adversarial training and 49.05/48.80 for KD-AT-Auto, reducing the reported gap from 5.93 to 0.25 percentage points. This is an author-reported table result, not a rerun.

### 7.2 Evidence unit 2

For CIFAR-100 the reported gap contracts from 5.04 to 0.12 points, and for Tiny-ImageNet from 1.80 to -0.10. A negative table gap means the recorded last value slightly exceeds the selected best column under that convention; it is not evidence of a negative error rate.

### 7.3 Evidence unit 3

Extension tables described by the record report similar gap reductions for VGG-19, TRADES, PGD-1000, Square, RayS, and SVHN. Breadth strengthens the within-paper pattern, but the source lacks repeated-seed intervals and an official implementation for independent verification.

### 7.4 Evidence unit 4

The strongest unresolved issue is semantic validity. The unknown label distribution is never directly observed, the teacher can inherit attack- and dataset-specific bias, and validation can tune to one threat model. Gap reduction therefore supports mitigation within tested coordinates rather than recovered ground truth.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| KD-AT-Auto reduces robust best-to-last gaps. | DEP-E reconstruction of Tables 1-5 across datasets, architectures, methods, and attacks. | Supported under reported conditions; not independently reproduced. |
| Implicit label noise causes robust overfitting. | Long-run double-descent observations and the distribution-mismatch formalization. | Plausible mechanism, but the latent true distribution is not directly observed. |
| The theory recovers correct adversarial labels. | Existence of improving temperature or interpolation choices. | Not established; existence and global validation do not provide per-example ground truth. |
| The method adds no meaningful operational cost. | No manual per-run tuning is claimed. | Overstated unless robust-teacher training and adversarial validation are included. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2110.03135v4](https://arxiv.org/abs/2110.03135v4) — Canonical title, authors, version, abstract, and submission history checked in this run.
- [https://arxiv.org/pdf/2110.03135](https://arxiv.org/pdf/2110.03135) — Canonical complete-paper locator used by the source DEP-E; document bytes were not downloaded in this run.
- [https://arxiv.org/html/2110.03135](https://arxiv.org/html/2110.03135) — Official full-paper rendering locator used by the source DEP-E.
- [https://proceedings.neurips.cc/paper_files/paper/2022/hash/6fe6a2ba2594521d15af3b1f2162d79c-Abstract-Conference.html](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6fe6a2ba2594521d15af3b1f2162d79c-Abstract-Conference.html) — Official NeurIPS 2022 publication record.
- [https://doi.org/10.48550/arXiv.2110.03135](https://doi.org/10.48550/arXiv.2110.03135) — Persistent arXiv DOI.

### Associated DEP records

- `.lake-data/DEP-A/DEP-A-20260714-PAC Confidence` — verified related DEP-A; it does not replace or complete this pair.
- `.lake-data/DEP-A/DEP-A-20260716-AFIDAF Filters Intake` — verified related DEP-A; it does not replace or complete this pair.

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

**Proposition:** If distribution mismatch drives the reported gap, independently annotated ambiguous perturbations should show larger teacher-target divergence and larger benefit from rectification than clearly label-preserving perturbations.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** If the correction generalizes rather than overfits one threat model, parameters calibrated on one attack family should preserve gap reduction on unseen adaptive and black-box attacks.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** If teacher quality is causal, an ensemble with measured disagreement should outperform a single teacher mainly on examples where the teacher is calibrated and semantically consistent.

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

> The record's most defensible contribution is a target-correction view of robust overfitting: adversarial perturbation can make inherited one-hot labels a poor distributional target, and a robust teacher can reduce the best-to-last robustness gap, but global calibration and an existential theorem do not recover an unknown per-example semantic truth.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | classification, inventory, quantitative synopsis, related records, and final attribution | fully read; source-document withholding and public context confirmed |
| `adversarial_label_noise_manuscript.md` | metadata, evidence ledger, method, theorems, tables, limitations, proposals, references, and appendix | fully read from beginning to end; all paper-level results remain DEP-E-reported |
| `problem and hypothesis sections` | implicit distribution mismatch and epoch-wise double descent | causal interpretation separated from observation |
| `KD-AT-Auto method` | teacher, temperature, interpolation, validation selection, outer objective | technical flow and global-parameter boundary reconstructed |
| `Theorems 5.1-5.2` | existence of total-variation improvement | existence distinguished from identification and universal guarantee |
| `Tables 1-5` | CIFAR, Tiny-ImageNet, SVHN, architecture, method, and attack results | material values and no-seed caveat retained |
| `limitations and availability` | teacher dependence, calibration, cost, semantic ambiguity, missing code | negative evidence preserved |
| `proposals and exercises` | semantic audit, transfer tests, compute ledger, replication | reviewer proposals labeled as proposals |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260717-8302F064` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Adversarial%20Label%20Noise
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/695f4473ebb1174f78bd9a027184a7fb8bf2847e
[^primary-one]: Primary public source: https://arxiv.org/abs/2110.03135v4
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/pdf/2110.03135
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
