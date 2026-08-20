# Prompts as Continual Task Memory

## a whitepaper-grade archival intake review of DEP-E-20260811-Parameterizing Context

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260811-Parameterizing Context`
**Source commit:** `6eede1198f50fd9d9644b48cdb44ae43412247b0`
**Paired task indicator:** `BL-DEPPAIR-20260812-6857A8B5`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-08-12
**Review scope:** complete tracked repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is the complete DEP-E record centered on arXiv:2310.04801v1, Parameterizing Context: Unleashing the Power of Parameter-Efficient Fine-Tuning and In-Context Tuning for Continual Table Semantic Parsing, accepted at NeurIPS 2023. Every tracked Markdown file was read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

The paper converts temporary demonstrations into task-specific prompt parameters: an in-context teacher supplies a richer output distribution, a parameter-efficient student distills it, and frozen backbone weights isolate new tasks from old ones. This is a strong memory-allocation design for continual parsing, but separate prompts shift forgetting risk into routing, storage, teacher bias, and schema drift rather than eliminating it universally.

The primary object under review is the complete DEP-E record. Every tracked source file was read and the canonical public record and availability of the complete authorized paper were checked. This run did not perform a fresh page-by-page independent full-paper review. Detailed paper claims remain attributed to the DEP-E and paper authors; no result is represented as independently reproduced.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- The paper converts temporary demonstrations into task-specific prompt parameters: an in-context teacher supplies a richer output distribution, a parameter-efficient student distills it, and frozen backbone weights isolate new tasks from old ones. This is a strong memory-allocation design for continual parsing, but separate prompts shift forgetting risk into routing, storage, teacher bias, and schema drift rather than eliminating it universally.
- The pretrained backbone remains frozen while small prompt parameters are learned per task, preventing direct overwrite of earlier task prompts.
- An in-context teacher conditions on a few demonstrations and exposes an output distribution that carries more information than one hard SQL label.
- A student learns that distribution through the task-adaptive PEFT framework, compressing demonstration context into prompt parameters so examples need not be stored at inference.

### Principal qualifications

1. Task identity may be unavailable or ambiguous at inference, turning routing into the new catastrophic-failure boundary.
2. Teacher mistakes and spurious demonstrations can be compressed permanently into prompt parameters.
3. A growing prompt bank accumulates storage, retrieval, versioning, and compatibility costs across many tasks.
4. Schema and distribution changes can invalidate a prompt even when the frozen backbone prevents numerical forgetting.

## 1. Problem framing and research question

Continual table semantic parsing presents few examples for each new schema and asks one system to translate language into SQL without forgetting earlier tasks. Full fine-tuning overfits and overwrites shared parameters; replay stores examples; in-context learning retains a recurring context and inference cost. The paper asks whether context can be compressed into small task-specific parameters.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

The pretrained backbone remains frozen while small prompt parameters are learned per task, preventing direct overwrite of earlier task prompts.

### 2.2 Stage 2

An in-context teacher conditions on a few demonstrations and exposes an output distribution that carries more information than one hard SQL label.

### 2.3 Stage 3

A student learns that distribution through the task-adaptive PEFT framework, compressing demonstration context into prompt parameters so examples need not be stored at inference.

### 2.4 Stage 4

The design depends on correct task or schema routing, stable tokenizer and backbone behavior, teacher quality, executable SQL evaluation, and storage/version control for the prompt bank.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains `README.md` and tracked substantive artifact(s), including `parameterizing_context_manuscript.md`. The private coverage map records the complete tracked inventory. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact set supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `6eede1198f50fd9d9644b48cdb44ae43412247b0`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The primary object under review is the complete DEP-E record. Every tracked source file was read and the canonical public record and availability of the complete authorized paper were checked. This run did not perform a fresh page-by-page independent full-paper review. Detailed paper claims remain attributed to the DEP-E and paper authors; no result is represented as independently reproduced. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

The durable mechanism is context compilation: use expensive, example-rich inference as a teacher, distill its task context into a small addressable state object, and keep shared capability frozen. The analogy fails if parameter isolation is called complete lifelong learning or if a prompt vector is treated as privacy-safe merely because raw examples were discarded.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

The paper reports superiority over few-shot and continual-learning baselines on two benchmarks across multiple metrics; exact tables were not recomputed in this intake.

### 7.2 Evidence unit 2

Freezing the backbone and assigning separate task prompts supports the narrow claim of avoiding parameter-overwrite forgetting for already learned prompts.

### 7.3 Evidence unit 3

Removing stored demonstrations reduces replay-data retention, but it does not prove that prompts contain no sensitive or reconstructable task information.

### 7.4 Evidence unit 4

No table schema, SQL query, benchmark split, teacher prompt, output distribution, PEFT module, replay baseline, execution metric, code, or seed was rerun.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| The record identifies a concrete mechanism rather than only a topic. | The pretrained backbone remains frozen while small prompt parameters are learned per task, preventing direct overwrite of earlier task prompts. | Supported as a source-grounded reconstruction; implementation fidelity was not independently reproduced. |
| The reported evidence supports the mechanism in its evaluated setting. | The paper reports superiority over few-shot and continual-learning baselines on two benchmarks across multiple metrics; exact tables were not recomputed in this intake. | Supported under the source's stated data, configuration, metric, and comparator boundaries. |
| The source establishes unrestricted generalization or production readiness. | The inspected record supplies no universal deployment proof. | Not established; preserved assumptions, limitations, and untested shifts bound the conclusion. |
| The reviewer-derived interpretation can be tested independently. | The durable mechanism is context compilation: use expensive, example-rich inference as a teacher, distill its task context into a small addressable state object, and keep shared capability frozen. The analogy fails if parameter isolation is called complete lifelong learning or if a prompt vector is treated as privacy-safe merely because raw examples were discarded. | Promising as a falsifiable synthesis, not an author claim or theorem. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2310.04801](https://arxiv.org/abs/2310.04801) — Canonical or primary public locator inspected or preserved by the source; no source document deposited.
- [https://arxiv.org/html/2310.04801](https://arxiv.org/html/2310.04801) — Canonical or primary public locator inspected or preserved by the source; no source document deposited.
- [https://arxiv.org/pdf/2310.04801](https://arxiv.org/pdf/2310.04801) — Canonical or primary public locator inspected or preserved by the source; no source document deposited.
- [https://doi.org/10.48550/arXiv.2310.04801](https://doi.org/10.48550/arXiv.2310.04801) — Canonical or primary public locator inspected or preserved by the source; no source document deposited.
- [https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-RandLoRA%20Full-rank](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260728-RandLoRA%20Full-rank) — Canonical or primary public locator inspected or preserved by the source; no source document deposited.
- [https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260801-Vector-ICL%20In-context](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260801-Vector-ICL%20In-context) — Canonical or primary public locator inspected or preserved by the source; no source document deposited.

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

**Proposition:** Routing errors will dominate forgetting metrics once task identity must be inferred rather than supplied.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Prompt-bank consolidation with explicit interference tests will reduce storage while preserving accuracy until semantically overlapping schemas are merged too aggressively.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** Teacher-disagreement filtering will improve continual robustness more than increasing the number of unvetted in-context demonstrations.

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

> The paper converts temporary demonstrations into task-specific prompt parameters: an in-context teacher supplies a richer output distribution, a parameter-efficient student distills it, and frozen backbone weights isolate new tasks from old ones. This is a strong memory-allocation design for continual parsing, but separate prompts shift forgetting risk into routing, storage, teacher bias, and schema drift rather than eliminating it universally.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | classification, complete inventory, public-safe context, relevance, links, and final attribution | read from beginning to end; links and inventory accounted for |
| `parameterizing_context_manuscript.md` | complete tracked DEP-E artifact with 2185 words | read from beginning to end; headings accounted for: # Parameterizing Context - DEP-E; ## Source Metadata; ## Evidence Ledger; ## Executive Summary; ## Detailed Summary; ### Problem and background; ### Method and mechanism; ### Evidence and results; ### Limitations and conclusion; ## Key Claims and Evidence; ## Methodology; ## Scope, Constraints, and Assumptions; ## Observations; ## Considerations; ## Strengths; ## Weaknesses; ## Potential Improvements; ## Potential Implementations; ## Three Ways to Exercise This Research; ## Example MVP Product; ## Related Research and Reading; ## Source References; ## Appendix |
| `source identity and evidence ledger` | canonical identities, versions, evidence types, confidence, implementation state, and limitations | all preserved rows and public locators accounted for |
| `technical and evidentiary reconstruction` | problem, mechanism, architecture, evaluation, claims, and conclusions | all source headings included in the private coverage map |
| `quantitative and visual evidence` | tables, figures, equations, algorithms, and reported values across 2520 source words | numbers retain source setting and reproduction boundary |
| `critical considerations` | assumptions, limitations, failure modes, unsupported implications, and negative evidence | unfavorable evidence retained |
| `proposals and research agenda` | implementation ideas, governance implications, and falsifiable tests | reviewer proposals remain separate from findings |
| `references and attribution` | public locators across every tracked file | provenance retained; no source document uploaded |

The coverage ledger accounts for every tracked source file and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The primary object under review is the complete DEP-E record. Every tracked source file was read and the canonical public record and availability of the complete authorized paper were checked. This run did not perform a fresh page-by-page independent full-paper review. Detailed paper claims remain attributed to the DEP-E and paper authors; no result is represented as independently reproduced. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260812-6857A8B5` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260811-Parameterizing%20Context
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/6eede1198f50fd9d9644b48cdb44ae43412247b0
[^primary-one]: Primary public source: https://arxiv.org/abs/2310.04801
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/html/2310.04801
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
