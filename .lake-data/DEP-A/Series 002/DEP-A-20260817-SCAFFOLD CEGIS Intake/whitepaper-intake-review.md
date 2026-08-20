# Monotone Security Gates for Iterative Code Refinement

## a whitepaper-grade archival intake review of DEP-E-20260816-SCAFFOLD-CEGIS Preventing

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260816-SCAFFOLD-CEGIS Preventing`
**Source commit:** `81b588d864e26b3ed63be7d1c7e947940bb4a3c3`
**Paired task indicator:** `BL-DEPPAIR-20260817-1511C5CB`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-08-17
**Review scope:** complete tracked repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is the complete DEP-E record centered on SCAFFOLD-CEGIS: Preventing Latent Security Degradation in LLM-Driven Iterative Code Refinement (arXiv:2603.08520), plus the complete 12-page canonical paper. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

SCAFFOLD-CEGIS turns iterative LLM repair into a gated counterexample loop: candidate changes must preserve semantic anchors and pass correctness, safety-monotonicity, diff-budget, and anchor-integrity checks. The reported reduction in latent security degradation is substantial on 24 tasks, but the gate's operational monotonicity is not a formal guarantee over all vulnerabilities, languages, or tool blind spots.

The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- SCAFFOLD-CEGIS turns iterative LLM repair into a gated counterexample loop: candidate changes must preserve semantic anchors and pass correctness, safety-monotonicity, diff-budget, and anchor-integrity checks. The reported reduction in latent security degradation is substantial on 24 tasks, but the gate's operational monotonicity is not a formal guarantee over all vulnerabilities, languages, or tool blind spots.
- Semantic anchors encode security-critical invariants extracted from the initial task and retained across proposed patches. Anchor survival guards against deletion or semantic erosion of protections that tests may not exercise.
- A four-layer gate checks functional correctness, measured safety monotonicity, a bounded diff budget, and anchor integrity before accepting a refinement.
- Counterexamples from failed gates are assimilated into the next prompt, forming a CEGIS-style loop in which the model proposes and the verification scaffold rejects unsafe candidates.

### Principal qualifications

1. The benchmark is small and synthetic relative to production repositories, build systems, dependency graphs, and organizational threat models.
2. Static analyzers and LLM reviewers share blind spots; a patch can be monotone under observed checks while worsening an unmeasured vulnerability.
3. Diff budgets may reject necessary refactors or encourage superficially small patches that preserve unsafe architecture.
4. The term guarantee can be overread: the evidence is empirical acceptance monotonicity, not a proof of semantic security for arbitrary code.

## 1. Problem framing and research question

An LLM can fix the visible defect in one refinement round while silently removing a security check or introducing a new weakness. Ordinary pass/fail evaluation rewards the immediate fix and may miss this latent degradation across iterations.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

Semantic anchors encode security-critical invariants extracted from the initial task and retained across proposed patches. Anchor survival guards against deletion or semantic erosion of protections that tests may not exercise.

### 2.2 Stage 2

A four-layer gate checks functional correctness, measured safety monotonicity, a bounded diff budget, and anchor integrity before accepting a refinement.

### 2.3 Stage 3

Counterexamples from failed gates are assimilated into the next prompt, forming a CEGIS-style loop in which the model proposes and the verification scaffold rejects unsafe candidates.

### 2.4 Stage 4

Four agent configurations are evaluated across 24 Python and Java tasks in six scenarios. Static-analysis and LLM-review components extend detection coverage but also define the observable security boundary.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `scaffold_cegis_preventing_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `81b588d864e26b3ed63be7d1c7e947940bb4a3c3`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

SCAFFOLD-CEGIS is a transactional write protocol for code agents. The proposed diff is an uncommitted transaction, anchors are invariants, verification stages are constraints, and only a passing candidate commits. The analogy motivates audit logs and rollback, but cannot make incomplete security predicates complete.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

The paper reports latent security degradation falling from 20.8 percent in the ungated condition to 2.1 percent with the full framework, while measured safety monotonicity reaches 100 percent.

### 7.2 Evidence unit 2

Task completion for the full configuration is reported at 77.14 percent, exposing a real availability and productivity cost rather than claiming costless safety.

### 7.3 Evidence unit 3

Fix success is reported to rise from about 20 percent toward 52.71 percent under the scaffold. The exact interpretation depends on task, attempt, and gate denominators.

### 7.4 Evidence unit 4

Ablations attribute the monotonicity result directly to the acceptance gate and show semantic anchors catching cases beyond the static analyzer. This is evidence about the instrumented threat surface, not exhaustive security.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| A gate with persistent security anchors sharply reduces observed latent degradation during iterative repair. | A 24-task comparison and ablations report 20.8-to-2.1-percent degradation reduction and 100-percent measured monotonicity. | Supported on the instrumented benchmark; external validity remains limited. |
| The framework guarantees security-preserving refinement. | Acceptance is defined by tests, analyzers, LLM review, anchors, and diff constraints rather than formal program semantics. | Rejected as a universal guarantee; valid only relative to the measured predicates. |
| The gate has no material completion cost. | The full system reports 77.14-percent task completion and can reject candidates for security or budget reasons. | Rejected; safety and completion must be reported jointly. |
| This intake reproduced the benchmark. | The full PDF was reviewed, but no agent, analyzer, repository, or task execution occurred. | Rejected. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2603.08520](https://arxiv.org/abs/2603.08520) — Canonical arXiv identity and version record.
- [https://arxiv.org/pdf/2603.08520](https://arxiv.org/pdf/2603.08520) — Complete canonical paper inspected; no source document uploaded.
- [https://doi.org/10.48550/arXiv.2603.08520](https://doi.org/10.48550/arXiv.2603.08520) — Persistent arXiv DOI.

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

**Proposition:** Repository-derived semantic anchors will reduce real-world regression escapes more than prompt-only security reminders at equal model cost.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Diversifying gate implementations across symbolic and learned detectors will reduce correlated blind spots more than adding retries to one detector.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** Risk-adaptive diff budgets will recover completion rate without increasing measured latent degradation relative to one fixed budget.

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

> SCAFFOLD-CEGIS turns iterative LLM repair into a gated counterexample loop: candidate changes must preserve semantic anchors and pass correctness, safety-monotonicity, diff-budget, and anchor-integrity checks. The reported reduction in latent security degradation is substantial on 24 tasks, but the gate's operational monotonicity is not a formal guarantee over all vulnerabilities, languages, or tool blind spots.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | complete manifest and attribution boundary | read from beginning to end; headings, tables, claims, URLs, limitations, proposals, and attribution accounted for |
| `scaffold_cegis_preventing_manuscript.md` | complete substantive artifact with 2177 words | read from beginning to end; headings, tables, claims, URLs, limitations, proposals, and attribution accounted for |
| `arXiv:2603.08520 complete canonical PDF` | SCAFFOLD-CEGIS: Preventing Latent Security Degradation in LLM-Driven Iterative Code Refinement; 12 pages, 8372 extracted words, 0 table-caption candidates, 1 figure-caption candidates | every PDF page inspected and structurally inventoried; abstract, method, quantitative results, captions, limitations, appendices, and references checked; no experiment, proof, code, data, model, or benchmark rerun |
| `source metadata and evidence ledger` | identity, version, evidence roles, confidence, access status, and limitations | reconstructed with source DEP report, directly inspected primary evidence, reviewer inference, and proposals kept distinct |
| `method, equations, tables, figures, and appendices` | technical dataflow, objectives, evaluation coordinates, ablations, quantitative results, captions, and supplementary boundaries | material units accounted for in private maps; exact claims remain source-reported unless explicitly assessed |
| `limitations, proposals, references, and attribution` | failure modes, transfer limits, implementation ideas, reproduction boundary, public locators, and source-locality policy | limitations retained; proposals treated as hypotheses; source documents remained outside the public repository |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260817-1511C5CB` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260816-SCAFFOLD-CEGIS%20Preventing
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/81b588d864e26b3ed63be7d1c7e947940bb4a3c3
[^primary-one]: Primary public source: https://arxiv.org/abs/2603.08520
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/pdf/2603.08520
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
