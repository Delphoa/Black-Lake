# Conditional Identifiability of Learned Representations

## a whitepaper-grade archival intake review of the Contravariance Study DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260716-Contravariance Study`
**Source commit:** `695f4473ebb1174f78bd9a027184a7fb8bf2847e`
**Paired task indicator:** `BL-DEPPAIR-20260717-EB2C6EC4`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-07-17
**Review scope:** complete two-file repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is an iterative DEP-E expansion centered on Contravariance Theory: Strong Alignment for Minimal Solutions to Hard Tasks, arXiv:2607.08561v1. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

Contravariance is a conditional identifiability program: task-visible nonlinear signatures can collapse weak affine equivalence into native-axis alignment and propagate it upstream, but only when hardness, usedness, minimality, compactness, and regularity assumptions hold; it is not evidence that arbitrary trained networks or brains inevitably share coordinates.

The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- Contravariance is a conditional identifiability program: task-visible nonlinear signatures can collapse weak affine equivalence into native-axis alignment and propagate it upstream, but only when hardness, usedness, minimality, compactness, and regularity assumptions hold; it is not evidence that arbitrary trained networks or brains inevitably share coordinates.
- A task-used ReLU axis leaves a kink and a task-used Softplus axis leaves curvature. If representations are weakly aligned on both sides of such a nonlinearity, these task-visible signatures restrict arbitrary mixing and can identify axes up to the permitted permutation and scaling symmetries.
- The layer-specific used-axis budget m_l(epsilon) defines how many nonlinear axes are necessary to meet a loss tolerance. The exact theorem lower-bounds the strongly aligned fraction by this required budget relative to width, making task hardness an operational variable rather than a benchmark label.
- An asymptotic result moves from exact equality to shrinking adjacent-layer weak-alignment errors on compact comparison families. Approximate strong alignment follows only with the stated constants and comparison-family restrictions.

### Principal qualifications

1. Theorem assumptions may be difficult or impossible to estimate reliably in modern networks and biological recordings.
2. Genericity in parameter space can be mistaken for probability under a training algorithm.
3. Alignment maps can overfit finite stimuli and create apparent equivalence without held-out validation.
4. Architecture-specific gauges, width mismatch, unused axes, and duplicate features can invalidate naive coordinate matching.

## 1. Problem framing and research question

The record expands a previously abstract-only research thread asking when coarse representational similarity implies stronger coordinate-level correspondence. The paper formalizes weak alignment with injective affine maps and strong alignment with activation-compatible native-axis matches. The archival task is to retain the exact theorem conditions, distinguish genericity from trained-parameter probability, and turn the claims into empirical assumption checks rather than slogans about convergence.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

A task-used ReLU axis leaves a kink and a task-used Softplus axis leaves curvature. If representations are weakly aligned on both sides of such a nonlinearity, these task-visible signatures restrict arbitrary mixing and can identify axes up to the permitted permutation and scaling symmetries.

### 2.2 Stage 2

The layer-specific used-axis budget m_l(epsilon) defines how many nonlinear axes are necessary to meet a loss tolerance. The exact theorem lower-bounds the strongly aligned fraction by this required budget relative to width, making task hardness an operational variable rather than a benchmark label.

### 2.3 Stage 3

An asymptotic result moves from exact equality to shrinking adjacent-layer weak-alignment errors on compact comparison families. Approximate strong alignment follows only with the stated constants and comparison-family restrictions.

### 2.4 Stage 4

Exact and soft zippering theorems propagate terminal equivalence upstream under minimality and Jacobian regularity. The authors explicitly note that optimization may concentrate near exceptional sets and that modern architectures require branch- and gauge-aware treatment.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `contravariance-study.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `695f4473ebb1174f78bd9a027184a7fb8bf2847e`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

The paper can be recast as an observability theorem for nonlinear signatures. A hard task forces certain features to remain visible through the system; if two minimal solutions are already coarsely related, those visible signatures constrain the admissible coordinate changes. The abstraction fails when features are unused, duplicated, hidden behind gauge symmetries, or when optimization selects a degenerate solution. Its practical value is an assumption matrix and falsification protocol.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

The DEP-E reconstructs Definitions 1-5 and Theorems 1-4 from the complete 94-page v1 paper. These are formal conditional results; this run did not independently machine-check the proofs or compute architecture-specific constants.

### 7.2 Evidence unit 2

The exact weak-to-strong result connects adjacent weak equivalence and used nonlinear axes to a lower bound on native-axis correspondence. Its force depends on measuring usedness and a task-required budget, neither of which is supplied by model size alone.

### 7.3 Evidence unit 3

The zippering results provide a plausible explanation for hierarchical convergence, but application to trained networks requires minimality, regularity, and evidence that learning dynamics avoid degeneracies. Measure-zero language in ambient parameter space is insufficient by itself.

### 7.4 Evidence unit 4

Transformer implications are branch-specific: residual streams may exhibit weak affine similarity without privileged coordinates, while MLP hidden axes and gauge-invariant attention signatures are more plausible sites for strong alignment. The source presents this as a theory-guided empirical agenda.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| Weak alignment implies strong alignment for task-used axes. | Theorem 1 under adjacent-layer equivalence and usedness assumptions. | Strongly supported as a formal conditional statement; application must establish every assumption. |
| Terminal alignment zippers upstream. | Theorems 3-4 under minimality and regularity. | Supported within the formal setup; quantitative usefulness depends on constants and real-network fit. |
| Hard tasks make convergent evolution inevitable. | Abstract-level implication and genericity discussion. | Overstated outside the modeled assumptions and an optimization-aware parameter distribution. |
| Transformer branches should exhibit different alignment structure. | Architecture-specific discussion of residual, MLP, and attention symmetries. | Plausible prediction requiring branch-aware empirical tests. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2607.08561v1](https://arxiv.org/abs/2607.08561v1) — Canonical metadata and abstract checked directly in this run.
- [https://arxiv.org/pdf/2607.08561](https://arxiv.org/pdf/2607.08561) — Canonical 94-page complete-paper locator inspected by the source DEP-E.
- [https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260712-Tech%20Intel%201100](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260712-Tech%20Intel%201100) — Selected upstream DEP bundle.
- [https://github.com/Delphoa/Black-Lake/blob/db3a22b36676b872fbbcebc069916ac9878f93a3/.lake-data/DEP-E/DEP-E-20260713-Tech%20Intel%201100%20Review/tech-intel-1100-research.md](https://github.com/Delphoa/Black-Lake/blob/db3a22b36676b872fbbcebc069916ac9878f93a3/.lake-data/DEP-E/DEP-E-20260713-Tech%20Intel%201100%20Review/tech-intel-1100-research.md) — Prior abstract-boundary DEP-E artifact.
- [https://doi.org/10.48550/arXiv.2607.08561](https://doi.org/10.48550/arXiv.2607.08561) — Persistent arXiv DOI locator.

### Associated DEP records

- `.lake-data/DEP-A/DEP-A-20260714-Tech Intel 1100 Review` — verified related DEP-A; it does not replace or complete this pair.

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

**Proposition:** If the used-axis budget is the operative hardness variable, estimated strong alignment should increase with m_l(epsilon)/d_l across controlled tasks after matching architecture and training.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** If optimization avoids exceptional sets, duplicate-axis, vanishing-weight, and ill-conditioned-Jacobian diagnostics should become rarer as terminal alignment improves across seeds.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** If the transformer prediction is correct, held-out residual-stream affine alignment will exceed coordinate matching while MLP axes show the reverse pattern after gauge-aware controls.

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

> Contravariance is a conditional identifiability program: task-visible nonlinear signatures can collapse weak affine equivalence into native-axis alignment and propagate it upstream, but only when hardness, usedness, minimality, compactness, and regularity assumptions hold; it is not evidence that arbitrary trained networks or brains inevitably share coordinates.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | iterative source provenance, two-file inventory, prior boundary, and attribution | fully read; upstream DEP and prior manuscript links verified |
| `contravariance-study.md` | metadata, definitions, theorems, assumptions, applications, proposals, references, and appendix | fully read in two contiguous passes; paper-level content remains DEP-E-reported |
| `Definitions 1-5` | weak and strong alignment, usedness, hardness, comparison families | activation-specific symmetries retained |
| `Theorems 1-2` | exact and asymptotic weak-to-strong alignment | condition and constant boundaries preserved |
| `Theorems 3-4` | exact and soft upstream zippering | minimality and Jacobian regularity made explicit |
| `Sections 5-6` | transformers, RSA multiplicity, biology, future work | architectural extensions separated from proof |
| `prior provenance defect` | arXiv:2607.04595 source-identity mismatch | preserved without rewriting historical material |
| `implementation proposals` | condition probes, task-hardness estimator, branch-aware aligner | reviewer proposals labeled and bounded |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The primary object under review is the complete paper-centered DEP-E record. The source record documents prior full-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260717-EB2C6EC4` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Contravariance%20Study
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/695f4473ebb1174f78bd9a027184a7fb8bf2847e
[^primary-one]: Primary public source: https://arxiv.org/abs/2607.08561v1
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/pdf/2607.08561
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
