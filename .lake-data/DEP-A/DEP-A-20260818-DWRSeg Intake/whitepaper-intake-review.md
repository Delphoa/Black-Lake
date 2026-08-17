# DWRSeg as Staged Receptive-Field Allocation

## a whitepaper-grade archival intake review of DEP-E-20260817-DWRSeg Rethinking

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260817-DWRSeg Rethinking`
**Source commit:** `904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff`
**Paired task indicator:** `BL-DEPPAIR-20260818-DD484F83`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-08-18
**Review scope:** complete tracked repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is the complete DEP-E record centered on Wei et al., DWRSeg: Rethinking Efficient Acquisition of Multi-scale Contextual Information for Real-time Semantic Segmentation (arXiv:2212.01173), plus the complete 10-page canonical paper. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

DWRSeg's core contribution is a staged receptive-field allocation rule: first form compact regional features, then apply stage-specific depth-wise dilated filtering for semantic residuals. Cityscapes and CamVid results support an attractive speed-accuracy-size operating point on a GTX 1080 Ti, but hand-tuned receptive fields, single-hardware FPS, and dated comparison conditions prevent a universal real-time or state-of-the-art conclusion.

The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- DWRSeg's core contribution is a staged receptive-field allocation rule: first form compact regional features, then apply stage-specific depth-wise dilated filtering for semantic residuals. Cityscapes and CamVid results support an attractive speed-accuracy-size operating point on a GTX 1080 Ti, but hand-tuned receptive fields, single-hardware FPS, and dated comparison conditions prevent a universal real-time or state-of-the-art conclusion.
- Region residualization first compresses and transforms the input into concise region-form feature maps. Semantic residualization then uses parallel depth-wise dilated convolutions as morphological filters over those intermediate maps.
- The Dilation-wise Residual module serves higher stages, where larger semantic receptive fields are useful. The Simple Inverted Residual module removes the multi-branch dilation machinery in lower stages, where smaller context and cheaper processing are preferred.
- Dilation rates, branch channel allocation, and expansion ratios are stage specific. A desired-receptive-field experiment examines learned branch weights, but this tuning also makes the final architecture partly empirical.

### Principal qualifications

1. FPS is measured on one older GPU and depends on framework, input resolution, batch size, warm-up, and kernel implementation.
2. Architecture and receptive-field hyperparameters were carefully tuned on the target setting, creating selection risk not captured by final tables.
3. Cityscapes and CamVid are road-scene datasets; weather, geography, sensor, class, and temporal shifts remain untested in this paper.
4. mIoU and throughput do not expose rare-class misses, calibration, boundary quality, or safety-critical object latency.

## 1. Problem framing and research question

Real-time segmentation architectures often apply several dilated depth-wise convolutions directly to one feature map. The paper argues that this single-step pattern mixes region formation and semantic filtering, making receptive-field selection inefficient. It seeks a lightweight encoder-decoder that separates those roles and changes receptive fields with network depth.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

Region residualization first compresses and transforms the input into concise region-form feature maps. Semantic residualization then uses parallel depth-wise dilated convolutions as morphological filters over those intermediate maps.

### 2.2 Stage 2

The Dilation-wise Residual module serves higher stages, where larger semantic receptive fields are useful. The Simple Inverted Residual module removes the multi-branch dilation machinery in lower stages, where smaller context and cheaper processing are preferred.

### 2.3 Stage 3

Dilation rates, branch channel allocation, and expansion ratios are stage specific. A desired-receptive-field experiment examines learned branch weights, but this tuning also makes the final architecture partly empirical.

### 2.4 Stage 4

A simple encoder-decoder and FCN-like head combine stage outputs. DWRSeg-B and DWRSeg-L trade parameter count and compute against accuracy and FPS without pretraining or multiscale test-time evaluation in the reported comparison.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `dwrseg_rethinking_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

DWRSeg is a budgeted context allocator: cheap local region formation precedes selective semantic widening, and later stages receive more context because their features can use it. This predicts that learned effective receptive fields should track stage depth and object scale; if equalized receptive fields perform the same, the two-stage causal story is incomplete.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

On Cityscapes at half resolution, DWRSeg-B50 reports 72.7% mIoU, 319.5 FPS, and 2.54M parameters; DWRSeg-L50 reports 73.1%, 256.2 FPS, and 3.53M parameters on one GTX 1080 Ti.

### 7.2 Evidence unit 2

At 0.75 input ratio, DWRSeg-B75 reports 75.6% mIoU at 151.7 FPS and DWRSeg-L75 reports 76.3% at 123.4 FPS. Resolution therefore remains a major coordinate of the speed-accuracy claim.

### 7.3 Evidence unit 3

On CamVid, the starred DWRSeg-B and -L variants report 76.5%/237.2 FPS and 77.5%/189.2 FPS, respectively, compared with the paper's listed baselines under its protocol.

### 7.4 Evidence unit 4

Ablations on Cityscapes vary multiscale structure, branch ratios, expansion, module placement, point-wise convolution, repetitions, and dilation offsets. Several alternatives remain close in FPS, so the evidence supports the complete design but does not isolate one uniquely necessary component.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| Two-step regional then semantic filtering improves the real-time segmentation tradeoff. | Ablations, branch-weight analysis, and benchmark results favor the complete DWRSeg designs. | Supported under the reported training, resolutions, and GTX 1080 Ti runtime protocol. |
| DWRSeg is unconditionally state of the art. | The comparison is tied to selected contemporaneous methods, hardware, resolution, and evaluation choices. | Not established beyond the table's coordinates. |
| The receptive-field analysis proves the proposed morphology mechanism. | Branch distributions and ablations are consistent with the explanation but are not a direct causal measurement of semantic morphology. | Promising interpretation, not proof. |
| This intake reproduced segmentation or FPS. | No dataset, model, training, inference, or timing run was executed. | Rejected. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/2212.01173](https://arxiv.org/abs/2212.01173) — Canonical arXiv identity and version record.
- [https://arxiv.org/pdf/2212.01173](https://arxiv.org/pdf/2212.01173) — Complete canonical paper inspected page by page; no source document uploaded.
- [https://doi.org/10.48550/arXiv.2212.01173](https://doi.org/10.48550/arXiv.2212.01173) — Persistent primary-source identifier.

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

**Proposition:** Stage-wise measured effective receptive fields will predict class-scale accuracy better than nominal dilation rates alone.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Kernel- and hardware-normalized benchmarking will preserve DWRSeg's parameter advantage but reduce the reported FPS separation from optimized baselines.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** Rare and thin classes will benefit less from aggressive regional compression than large amorphous classes, revealing a class-specific context tradeoff.

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

> DWRSeg's core contribution is a staged receptive-field allocation rule: first form compact regional features, then apply stage-specific depth-wise dilated filtering for semantic residuals. Cityscapes and CamVid results support an attractive speed-accuracy-size operating point on a GTX 1080 Ti, but hand-tuned receptive fields, single-hardware FPS, and dated comparison conditions prevent a universal real-time or state-of-the-art conclusion.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | complete manifest and attribution boundary | read from beginning to end; every heading, table row, claim, limitation, proposal, URL, related-record reference, and attribution entry accounted for |
| `dwrseg_rethinking_manuscript.md` | complete substantive DEP-E artifact with 2102 words | read from beginning to end; every heading, table row, claim, limitation, proposal, URL, related-record reference, and attribution entry accounted for |
| `arXiv:2212.01173 complete canonical PDF` | DWRSeg: Rethinking Efficient Acquisition of Multi-scale Contextual Information for Real-time Semantic Segmentation; 10 pages and 7830 extracted words | PDF header and terminal marker passed; every page inspected; complete body, equations, tables, figures, limitations, appendices where present, acknowledgments, and references accounted for; no experiment or code rerun |
| `canonical PDF page 1` | 914 extracted words; labels: Figure 1 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 2` | 866 extracted words; labels: Fig. 2, Figure 2, Figure 1 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 3` | 765 extracted words; labels: Figure 3, Figure 4a, Table 1 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 4` | 623 extracted words; labels: Figure 3, Figure 5 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 5` | 681 extracted words; labels: Figure 4, Figure 5, Figure 6a, Figure 3, Figure 6b, Table 1 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 6` | 955 extracted words; labels: Figure 6, Figure 7, Figure 8 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 7` | 1152 extracted words; labels: Figure 7, Figure 8, Table 2, Table 3 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 8` | 783 extracted words; labels: Table 2, Table 4, Table 3 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 9` | 906 extracted words | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 10` | 185 extracted words | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `Table 1. Detailed DWRSeg architecture. R, C and B denote the` | numbered table and its surrounding protocol/results | values interpreted only with dataset, metric, baseline, denominator, and runtime/uncertainty qualifications |
| `Table 2 Expt. I illustrates the results of a ’single recep-` | numbered table and its surrounding protocol/results | values interpreted only with dataset, metric, baseline, denominator, and runtime/uncertainty qualifications |
| `Table 2. Ablation experiments on the network structure design` | numbered table and its surrounding protocol/results | values interpreted only with dataset, metric, baseline, denominator, and runtime/uncertainty qualifications |
| `Table 3. Comparisons with other state-of-the-art methods on` | numbered table and its surrounding protocol/results | values interpreted only with dataset, metric, baseline, denominator, and runtime/uncertainty qualifications |
| `Table 4. Comparisons with other state-of-the-art methods on` | numbered table and its surrounding protocol/results | values interpreted only with dataset, metric, baseline, denominator, and runtime/uncertainty qualifications |
| `Figure 1. Speed-accuracy performance comparison on the` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 2. (a) presents the typical structure for drawing multi-scale` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 3. Illustration of the entire network structure. The structure is relatively simple; it is a typical encoder-decoder setup. The encoder` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 4. Illustration of the structure of a 3-branch DWR module` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 5. Illustration of the visualized heatmaps of feature maps` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 6. Illustration of the structure of the stem block and Seg-` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 6a. Two adjustments are made to the stem block pre-` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 7. The designed mod-` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `Figure 8. Illustration of the probability mass function (PMF) and cumulative distribution function (CDF)` | numbered figure and its surrounding argument | visual or architectural claim checked against prose; qualitative evidence not upgraded into a quantitative or causal guarantee |
| `central equations and algorithms` | 9 equation-number candidates plus all displayed/inline mathematical definitions | variables, signs, objectives, constraints, and guarantee boundaries reconstructed; extraction ambiguity preserved rather than guessed |
| `appendix, references, disclosures, and final page` | appendix detected: True; references detected: True | supplementary settings, failure examples, source lineage, acknowledgments, and end-of-document integrity checked |
| `private evidence-layer map` | source DEP-E report; directly inspected primary evidence; reviewer inference; hypothesis/proposal | all public claims assigned to one evidence layer; no reproduction or source-copy claim |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260818-DD484F83` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260817-DWRSeg%20Rethinking
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff
[^primary-one]: Primary public source: https://arxiv.org/abs/2212.01173
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/pdf/2212.01173
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
