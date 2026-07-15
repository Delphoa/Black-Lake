# Alternating Fourier and Image-Domain Adaptive Filters

## a whitepaper-grade archival intake review of the AFIDAF Vision Filters DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters`
**Source commit:** `84175d48e5ef802d8ed0fcef7373d4bd7717a294`
**Paired task indicator:** `BL-DEPPAIR-20260716-152E7D47`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-07-16
**Review scope:** complete two-file repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is AFIDAF: Alternating Fourier and Image Domain Adaptive Filters as an Efficient Alternative to Attention in ViTs, arXiv:2407.12217v2. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

AFIDAF decomposes token mixing across complementary domains: large-kernel image-space filtering captures local and high-frequency structure, while Fourier-domain channel mixing supplies global low-frequency reach. The paper's evidence supports a useful lightweight backbone tradeoff, but not a cost-free replacement for attention.

The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- AFIDAF decomposes token mixing across complementary domains: large-kernel image-space filtering captures local and high-frequency structure, while Fourier-domain channel mixing supplies global low-frequency reach. The paper's evidence supports a useful lightweight backbone tradeoff, but not a cost-free replacement for attention.
- The AFF path applies a Fourier transform, a channel-wise nonlinear mask, and an inverse transform. Because the implemented mask is constant across frequency locations for a channel, its adaptivity is more limited than a fully frequency-local filter.
- The image-domain path uses grouped, shuffled large-kernel approximations with multiplicative spatial modulation to capture edges, corners, textures, and broader receptive fields.
- Alternation makes the two paths complementary rather than concurrent attention heads: image-space filtering resolves spatially localized structure, and Fourier mixing propagates global context through channel interactions.

### Principal qualifications

1. Fourier transforms and large kernels can have hardware-dependent latency and memory behavior that FLOPs do not capture.
2. The ablation compares closely related architectures but does not isolate every grouping, shuffle, kernel, and training choice.
3. Small downstream differences may be within unreported training variance.
4. Without code and checkpoints, reproduction requires reconstructing details from prose and tables.

## 1. Problem framing and research question

The work begins from a discrepancy between the theoretical adaptive Fourier filter described by AFFNet and the practical channel-wise mask visible in code. A purely channel-wise frequency operation has global reach but limited spatial selectivity. A purely image-domain large-kernel operation captures local structure but may not cheaply express long-range interactions. AFIDAF asks whether alternating the two can recover a better local/global balance while staying in the lightweight regime.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

The AFF path applies a Fourier transform, a channel-wise nonlinear mask, and an inverse transform. Because the implemented mask is constant across frequency locations for a channel, its adaptivity is more limited than a fully frequency-local filter.

### 2.2 Stage 2

The image-domain path uses grouped, shuffled large-kernel approximations with multiplicative spatial modulation to capture edges, corners, textures, and broader receptive fields.

### 2.3 Stage 3

Alternation makes the two paths complementary rather than concurrent attention heads: image-space filtering resolves spatially localized structure, and Fourier mixing propagates global context through channel interactions.

### 2.4 Stage 4

The HAFIDAF variant hybridizes the approach with additional blocks. The architecture's practical merit depends on parameter/FLOP budgets, memory movement, transform kernels, and downstream head choices, not parameter count alone.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `afidaf_vision_filters_manuscript.md metadata and evidence`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `84175d48e5ef802d8ed0fcef7373d4bd7717a294`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

AFIDAF can be understood as a spectral-spatial operator split. Rather than asking one mixer to be simultaneously local, global, adaptive, and inexpensive, the design assigns different frequency regimes to different inductive biases and alternates them. The transferable lesson is to split an expensive universal operator into bounded operators whose failure modes are measurable, then test whether their composition preserves the desired response across spatial frequency, resolution, and downstream task.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

On ImageNet-1K, the paper reports AFIDAF at 80.9 percent top-1 with 6.5 million parameters and 1.5 GFLOPs; AFIDAF-T reports 77.6 percent with 3.0 million parameters and 0.8 GFLOPs. The same table reports AFFNet at 79.8 and IDAF at 80.3, supporting the alternating-domain contribution in that configuration.

### 7.2 Evidence unit 2

For COCO detection with SSD, the reported AFIDAF row reaches 30.2 mAP versus 28.4 for AFFNet, while the tiny variants differ by only 0.1 mAP. This shows that scale and task matter and that a headline claim should not erase small-effect rows.

### 7.3 Evidence unit 3

For PASCAL VOC segmentation, AFIDAF reports 81.6 mIoU, IDAF 81.1, and AFFNet 80.5. The result supports downstream usefulness under the stated pretraining/fine-tuning pipeline, not a universal advantage over modern attention backbones.

### 7.4 Evidence unit 4

The paper does not provide an official code release, repeated seeds, confidence intervals, or full device-level latency/energy evidence in the inspected canonical record. Parameter and FLOP comparisons therefore remain proxies for realized deployment cost.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| Alternating image and Fourier filtering improves ImageNet accuracy over either compared single-domain variant. | Table 1: 80.9 versus 80.3 IDAF and 79.8 AFFNet. | Supported for the reported training recipe; no repeated-run uncertainty. |
| AFIDAF improves dense prediction. | COCO and VOC tables. | Supported under the stated SSD and segmentation settings; effect size varies. |
| AFIDAF is an efficient alternative to attention. | Parameter and FLOP comparisons with lightweight backbones. | Promising but incomplete without matched latency, memory, energy, and kernel evidence. |
| The mechanism captures local/high-frequency and global/low-frequency information. | Operator construction and domain interpretation. | Mechanistically plausible; feature attribution is not fully isolated by the experiments. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2407.12217](https://arxiv.org/abs/2407.12217) — Canonical metadata and version record.
- [https://arxiv.org/html/2407.12217](https://arxiv.org/html/2407.12217) — Complete paper rendering inspected for method, experiments, tables, and limitations.
- [https://arxiv.org/pdf/2407.12217](https://arxiv.org/pdf/2407.12217) — Canonical complete-paper locator; not deposited.
- [https://doi.org/10.48550/arXiv.2407.12217](https://doi.org/10.48550/arXiv.2407.12217) — Persistent arXiv-issued DOI.

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

**Proposition:** If domain complementarity is causal, selectively suppressing high spatial frequencies should reduce the marginal value of the image-domain path more than the Fourier path.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** If the efficiency claim transfers, AFIDAF should preserve its Pareto position under matched compiler, batch, resolution, and device measurements rather than FLOPs alone.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** If alternation is more important than added capacity, a capacity-matched concurrent or repeated-single-domain control should underperform across multiple seeds.

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

> AFIDAF decomposes token mixing across complementary domains: large-kernel image-space filtering captures local and high-frequency structure, while Fourier-domain channel mixing supplies global low-frequency reach. The paper's evidence supports a useful lightweight backbone tradeoff, but not a cost-free replacement for attention.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | classification, inventory, paper identity, source policy, attribution | fully read |
| `afidaf_vision_filters_manuscript.md metadata and evidence` | canonical v2 record, method and tables | fully read; paper report and reviewer inference separated |
| `Introduction and related work` | attention-free lightweight token mixing and AFFNet gap | problem and novelty boundaries assessed |
| `Equations 1-3 and Figures 1-2` | theoretical AFF, implemented channel mask, AFIDAF block | technical reconstruction; no code execution |
| `Table 1` | ImageNet comparisons and IDAF/AFFNet ablation | all material rows interpreted with budget caveats |
| `Tables 2-3` | COCO detection and VOC segmentation | downstream effects and small-row differences preserved |
| `training settings and conclusions` | pretraining, fine-tuning, limitations, future localization | reproducibility and cost boundary assessed |
| `source proposals and appendices` | implementations, exercises, public source inventory | reviewer proposals labeled |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260716-152E7D47` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/84175d48e5ef802d8ed0fcef7373d4bd7717a294
[^primary-one]: Primary public source: https://arxiv.org/abs/2407.12217
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/html/2407.12217
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
