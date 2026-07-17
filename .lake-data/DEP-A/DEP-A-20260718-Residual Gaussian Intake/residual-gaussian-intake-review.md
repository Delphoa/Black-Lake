# Spectral Routing without Violating the Forward Model

## a whitepaper-grade archival intake review of the Residual Gaussian DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian`
**Source commit:** `2a010d716ea8d56b8d64a2d58641675dbdeb857a`
**Paired task indicator:** `BL-DEPPAIR-20260718-21965BB8`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-07-18
**Review scope:** complete two-file repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is a paper-centered DEP-E review of Residual Gaussian Splatting for Ultra Sparse-View CBCT Reconstruction, arXiv:2604.27552v1. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

Residual Gaussian Splatting offers a coherent representation-allocation strategy: wavelet energy routes capacity toward fine structure, while supervision stays in the physically compatible nonnegative projection domain and a staged schedule prevents the broad branch from consuming the detail residual. The source-reported fidelity gains support this mechanism on simulated sparse-view data, but not clinical readiness, hallucination control, robustness to acquisition mismatch, or reproducibility from the current README-only code release.

The primary object under review is the complete paper-centered DEP-E record. The source record documents prior complete-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- Residual Gaussian Splatting offers a coherent representation-allocation strategy: wavelet energy routes capacity toward fine structure, while supervision stays in the physically compatible nonnegative projection domain and a staged schedule prevents the broad branch from consuming the detail residual. The source-reported fidelity gains support this mechanism on simulated sparse-view data, but not clinical readiness, hallucination control, robustness to acquisition mismatch, or reproducibility from the current README-only code release.
- A single-level wavelet transform decomposes each projection. FDK of the low-frequency component initializes broad base Gaussians that anchor global attenuation.
- Absolute directional wavelet energy creates a nonnegative saliency map. Backprojection places smaller detail Gaussians where fine structure is likely, using wavelets for capacity routing rather than signed target values.
- Both branches ultimately fit raw measured projections. The detail branch receives the residual left after the base response, preserving the nonnegative Beer-Lambert-compatible field rather than attempting impossible signed attenuation.

### Principal qualifications

1. A detail branch can reconstruct plausible high-frequency structure unsupported by measurements when geometry, noise, scatter, motion, or detector response are misspecified.
2. PSNR and SSIM can miss task-relevant anatomy and do not establish diagnostic preservation or clinical safety.
3. Ablations are not matched for final primitive count, memory, time, or compute, so capacity and schedule can confound causal interpretation.
4. The official repository's README-only state prevents independent inspection of projector, density control, data processing, splits, and exact baselines.

## 1. Problem framing and research question

Ultra sparse-view cone-beam CT is underdetermined. Analytical reconstruction produces streaks, while learned or explicit neural representations can smooth away fine anatomy. The paper diagnoses frequency-dependent optimization in a 3D Gaussian attenuation field and proposes separate base and detail branches. The archival review must distinguish a useful mechanism from clinical claims, preserve the simulated-versus-acquired evidence boundary, and keep projection consistency from being mistaken for diagnostic truth under model mismatch.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

A single-level wavelet transform decomposes each projection. FDK of the low-frequency component initializes broad base Gaussians that anchor global attenuation.

### 2.2 Stage 2

Absolute directional wavelet energy creates a nonnegative saliency map. Backprojection places smaller detail Gaussians where fine structure is likely, using wavelets for capacity routing rather than signed target values.

### 2.3 Stage 3

Both branches ultimately fit raw measured projections. The detail branch receives the residual left after the base response, preserving the nonnegative Beer-Lambert-compatible field rather than attempting impossible signed attenuation.

### 2.4 Stage 4

A base-only warm-up followed by joint optimization with low-frequency consistency enforces a division of labor. Adaptive density control changes capacity during training, so primitive trajectories and matched compute are necessary for causal attribution.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `residual_gaussian_cbct_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `2a010d716ea8d56b8d64a2d58641675dbdeb857a`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The primary object under review is the complete paper-centered DEP-E record. The source record documents prior complete-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

The transferable mechanism is constraint-compatible spectral routing. A transform may reveal where model capacity should be placed even when its signed coefficients are incompatible with the physical output space. The route is valid only if final supervision remains in the measurement domain and if a residual audit can distinguish supported detail from forward-model-consistent invention.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

Across six source-reported AAPM volumes, RGS has the best average PSNR/SSIM at 20, 40, and 60 simulated views: 34.68/0.909, 37.59/0.954, and 38.97/0.975 respectively.

### 7.2 Evidence unit 2

The aggregate margin over 3DGR is largest at 20 views and narrows by 60 views. Individual-volume SSIM exceptions remain, so the evidence supports aggregate improvement rather than universal dominance.

### 7.3 Evidence unit 3

The source reports a 40-view wavelet-prior ablation loss of 1.36 dB and 0.015 SSIM and a curriculum ablation loss of 2.97 dB and 0.031 SSIM on different three-volume subsets.

### 7.4 Evidence unit 4

A 40-projection rhinoceros-beetle acquisition provides qualitative feasibility only. No ground truth, uncertainty, repeated seeds, compute ledger, robustness sweep, clinical endpoint, or usable implementation release was established.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| Standard projection-optimized 3DGS leaves persistent high-frequency error. | DEP-E reconstruction of Figure 3 and spectral curves. | Supported for the displayed configuration; universality is not established. |
| Nonnegative saliency plus raw residual fitting resolves the signed-wavelet mismatch. | Equations and algorithm as reconstructed by the DEP-E. | Strongly supported as a coherent method design under the stated forward model. |
| RGS is best on average at 20, 40, and 60 views. | Source-reported Table I. | Supported for six simulated volumes and tested baselines; individual metric exceptions remain. |
| The method is clinically ready and code-reproducible. | Qualitative beetle evidence and README-only repository. | Not established. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2604.27552](https://arxiv.org/abs/2604.27552) — Canonical title, authors, version, abstract, subject, DOI, and full-text locators checked in this run.
- [https://doi.org/10.48550/arXiv.2604.27552](https://doi.org/10.48550/arXiv.2604.27552) — Persistent arXiv DOI.
- [https://github.com/yqx7150/RGS](https://github.com/yqx7150/RGS) — Paper-declared implementation repository; the source DEP-E recorded a README-only state.

### Associated DEP records

- `.lake-data/DEP-A/DEP-A-20260714-Hypercomplex MRI` — verified related DEP-A; it does not replace or complete this pair.
- `.lake-data/DEP-A/DEP-A-20260716-AFIDAF Filters Intake` — verified related DEP-A; it does not replace or complete this pair.
- `.lake-data/DEP-A/DEP-A-20260714-Clothed Avatar Review` — verified related DEP-A; it does not replace or complete this pair.

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

**Proposition:** At matched total primitive trajectories and compute, the curriculum will retain more of the reported gain than wavelet initialization, indicating branch competition is the dominant mechanism.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Projection-model perturbations will cause detail-branch error to rise faster than global PSNR reveals, especially for calibration, scatter, and motion mismatch.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** Bandwise residual and local boundary metrics will detect clinically relevant degradation missed by aggregate PSNR/SSIM on deliberately blurred or hallucinated synthetic structures.

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

> Residual Gaussian Splatting offers a coherent representation-allocation strategy: wavelet energy routes capacity toward fine structure, while supervision stays in the physically compatible nonnegative projection domain and a staged schedule prevents the broad branch from consuming the detail residual. The source-reported fidelity gains support this mechanism on simulated sparse-view data, but not clinical readiness, hallucination control, robustness to acquisition mismatch, or reproducibility from the current README-only code release.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | inventory, method summary, evidence boundary, related DEP bridges, and final attribution | read from beginning to end |
| `residual_gaussian_cbct_manuscript.md` | metadata, evidence, equations, algorithm, experiments, claims, limitations, tools, and appendices | read from beginning to end; paper-level results remain DEP-E-reported |
| `Figure 3 and motivation` | spectral bias, frequency error, and boundary-localized residual | mechanism evidence retained without universalizing |
| `Equations 1-17 and Algorithm 1` | forward model, wavelet energy, dual fields, residual loss, and curriculum | sign and physical compatibility reconstructed |
| `Table I and Figure 5` | six-volume AAPM 20/40/60-view PSNR/SSIM and visuals | aggregate and per-volume exceptions retained |
| `Tables II-III and Figures 6-8` | wavelet and curriculum ablations | subset and matched-cost limits retained |
| `Figure 9 and repository status` | qualitative beetle acquisition and README-only code release | feasibility separated from accuracy/reproduction |
| `source-integrity and no-upload appendix` | complete paper, rendered pages, source archive, no private/public source files | process evidence checked |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The primary object under review is the complete paper-centered DEP-E record. The source record documents prior complete-paper inspection, while this run directly inspected the complete repository bundle and canonical metadata rather than reopening every page of the external paper. Paper-level results are therefore explicitly treated as DEP-E-reported claims. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260718-21965BB8` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260717-Residual%20Gaussian
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/2a010d716ea8d56b8d64a2d58641675dbdeb857a
[^primary-one]: Primary public source: https://arxiv.org/abs/2604.27552
[^primary-two]: Additional complete or canonical source locator: https://doi.org/10.48550/arXiv.2604.27552
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
