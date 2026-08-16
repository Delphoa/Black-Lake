# EEG Foundation Models Across Clinical Tasks

## a whitepaper-grade archival intake review of DEP-E-20260816-EEGFormer Towards

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260816-EEGFormer Towards`
**Source commit:** `81b588d864e26b3ed63be7d1c7e947940bb4a3c3`
**Paired task indicator:** `BL-DEPPAIR-20260817-BF896D98`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-08-17
**Review scope:** complete tracked repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is the complete DEP-E record centered on EEGFormer: Towards Transferable and Interpretable Large-Scale EEG Foundation Model (arXiv:2401.10278), plus the complete six-page canonical paper. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

EEGFormer presents a vector-quantized, self-supervised EEG representation model pretrained on a reported 1.7 TB corpus and evaluated across abnormality, artifact, slowing, and seizure tasks. The evidence supports useful in-domain transfer and interpretable code activations, but short-format reporting, task-dependent gains, and limited external validation leave clinical portability and safety unresolved.

The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- EEGFormer presents a vector-quantized, self-supervised EEG representation model pretrained on a reported 1.7 TB corpus and evaluated across abnormality, artifact, slowing, and seizure tasks. The evidence supports useful in-domain transfer and interpretable code activations, but short-format reporting, task-dependent gains, and limited external validation leave clinical portability and safety unresolved.
- A convolutional frontend converts multichannel EEG windows into temporal features, and a vector-quantization module maps them to discrete latent codes. Masked prediction over those codes supplies the self-supervised learning signal.
- Transformer context layers learn longer-range dependencies from the discretized sequence. Downstream evaluation separates linear probing, training from scratch, and full fine-tuning so representation reuse can be compared with supervised baselines.
- The pretraining collection is reported at 1.7 TB. Scale is an input to the claim, but corpus composition, exclusions, patient overlap controls, and data governance remain material audit questions beyond byte count.

### Principal qualifications

1. Patient, institution, montage, or recording overlap can inflate transfer estimates unless split provenance is demonstrably isolated.
2. Macro metrics can obscure class prevalence, calibration, operating thresholds, false-alarm burden, and subgroup performance needed in clinical use.
3. Discrete-code saliency may be stable and recognizable without being faithful to the model's decision or sufficient for neurologist action.
4. External neonatal transfer is valuable but too narrow to establish portability across devices, ages, pathologies, and clinical workflows.

## 1. Problem framing and research question

EEG datasets vary in montage, patient population, acquisition system, pathology, and label practice, while supervised task datasets are often small. The paper asks whether large-scale unlabeled pretraining can learn reusable temporal representations and whether discrete code activations can make those representations neurologically interpretable.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

A convolutional frontend converts multichannel EEG windows into temporal features, and a vector-quantization module maps them to discrete latent codes. Masked prediction over those codes supplies the self-supervised learning signal.

### 2.2 Stage 2

Transformer context layers learn longer-range dependencies from the discretized sequence. Downstream evaluation separates linear probing, training from scratch, and full fine-tuning so representation reuse can be compared with supervised baselines.

### 2.3 Stage 3

The pretraining collection is reported at 1.7 TB. Scale is an input to the claim, but corpus composition, exclusions, patient overlap controls, and data governance remain material audit questions beyond byte count.

### 2.4 Stage 4

The interpretability analysis maps code occurrence back to temporal and spatial EEG patterns, including activations near seizure regions. These correspondences are descriptive evidence, not validated clinical explanations.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `README.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `81b588d864e26b3ed63be7d1c7e947940bb4a3c3`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

EEGFormer can be viewed as a learned clinical signal vocabulary whose tokens are useful only when both their predictive transfer and their physiological meaning survive domain change. The vocabulary view suggests separate audits for token stability, decision contribution, and clinician interpretability rather than treating a visualized code as an explanation.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

The complete paper evaluates TUAB, TUAR, TUSL, and TUSZ tasks and includes an external neonatal transfer study. Results are reported with macro AUROC and macro AUPRC under several adaptation regimes.

### 7.2 Evidence unit 2

For TUAR, fine-tuning reports macro AUROC 0.852 plus or minus 0.004 and macro AUPRC 0.483 plus or minus 0.014. On TUSL, fine-tuning reports 0.679 plus or minus 0.013 and 0.389 plus or minus 0.003.

### 7.3 Evidence unit 3

Fine-tuning is not uniformly superior: the supervised TUSL macro AUROC shown in the table is 0.703, above the fine-tuned 0.679. That exception matters when interpreting 'transferable' as a comparative, task-bounded property.

### 7.4 Evidence unit 4

Longer pretraining generally improves downstream results in the displayed scaling analysis, and code examples localize seizure-related activity. Neither trend establishes prospective clinical benefit or causal explanation.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| Large-scale self-supervised pretraining yields reusable EEG representations across several downstream tasks. | Linear-probe and fine-tuning tables across four TUH tasks, plus a neonatal transfer experiment, provide comparative evidence. | Supported within the reported splits and adaptation protocols; gains are task dependent and not universal. |
| The model's discrete codes are clinically interpretable. | The paper visualizes code patterns and relates selected activations to seizure regions and EEG morphology. | Suggestive, not clinically validated; faithfulness, inter-rater agreement, and actionability remain open. |
| The results establish safe cross-hospital deployment. | The evaluation includes an external domain but does not provide prospective workflow, calibration, subgroup, or intervention evidence. | Not established. |
| This intake independently reproduced EEGFormer. | The complete source record and PDF were read, but no data, code, model, or EEG experiment was run. | Rejected. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2401.10278](https://arxiv.org/abs/2401.10278) — Canonical arXiv identity and version record.
- [https://arxiv.org/pdf/2401.10278](https://arxiv.org/pdf/2401.10278) — Complete canonical paper inspected; no source document uploaded.
- [https://doi.org/10.48550/arXiv.2401.10278](https://doi.org/10.48550/arXiv.2401.10278) — Persistent arXiv DOI.

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

**Proposition:** Codebook occupancy drift will predict downstream calibration loss across hospitals earlier than aggregate AUROC degradation.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Clinician-validated code semantics will transfer less reliably across montages than predictive performance unless montage normalization is explicit.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** A frozen encoder with site-specific calibration will outperform full fine-tuning on low-label external sites at matched governance cost.

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

> EEGFormer presents a vector-quantized, self-supervised EEG representation model pretrained on a reported 1.7 TB corpus and evaluated across abnormality, artifact, slowing, and seizure tasks. The evidence supports useful in-domain transfer and interpretable code activations, but short-format reporting, task-dependent gains, and limited external validation leave clinical portability and safety unresolved.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `eegformer_towards_manuscript.md` | complete substantive artifact with 2088 words | read from beginning to end; headings, tables, claims, URLs, limitations, proposals, and attribution accounted for |
| `README.md` | complete manifest and attribution boundary | read from beginning to end; headings, tables, claims, URLs, limitations, proposals, and attribution accounted for |
| `arXiv:2401.10278 complete canonical PDF` | EEGFormer: Towards Transferable and Interpretable Large-Scale EEG Foundation Model; 6 pages, 4235 extracted words, 2 table-caption candidates, 3 figure-caption candidates | every PDF page inspected and structurally inventoried; abstract, method, quantitative results, captions, limitations, appendices, and references checked; no experiment, proof, code, data, model, or benchmark rerun |
| `source metadata and evidence ledger` | identity, version, evidence roles, confidence, access status, and limitations | reconstructed with source DEP report, directly inspected primary evidence, reviewer inference, and proposals kept distinct |
| `method, equations, tables, figures, and appendices` | technical dataflow, objectives, evaluation coordinates, ablations, quantitative results, captions, and supplementary boundaries | material units accounted for in private maps; exact claims remain source-reported unless explicitly assessed |
| `limitations, proposals, references, and attribution` | failure modes, transfer limits, implementation ideas, reproduction boundary, public locators, and source-locality policy | limitations retained; proposals treated as hypotheses; source documents remained outside the public repository |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260817-BF896D98` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260816-EEGFormer%20Towards
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/81b588d864e26b3ed63be7d1c7e947940bb4a3c3
[^primary-one]: Primary public source: https://arxiv.org/abs/2401.10278
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/pdf/2401.10278
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
