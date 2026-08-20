# Significant Paths as Degree-Calibrated Network Evidence

## a whitepaper-grade archival intake review of DEP-E-20260817-Predicting missing links

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260817-Predicting missing links`
**Source commit:** `904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff`
**Paired task indicator:** `BL-DEPPAIR-20260818-4E58E6FE`
**Direction:** `DEP-E -> DEP-A`
**Review date:** 2026-08-18
**Review scope:** complete tracked repository record; source-integrity assessment; technical and evidentiary reconstruction; claim vetting; independent re-conceptualization; failure analysis; replication agenda
**Provenance boundary:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes
**Reproduction boundary:** no experiment, model, dataset, service, benchmark, simulator, or repository code was executed; results were not independently reproduced.

---

## Executive assessment

The selected record is the complete DEP-E record centered on Zhu et al., Predicting missing links via significant paths (arXiv:1402.6225v3; EPL 106 18008), plus the complete six-page canonical paper. Both tracked Markdown files were read from beginning to end at the pinned source commit. The inventory, claims, evidence links, assumptions, limitations, quantitative material, implementation proposals, and final attribution were accounted for in a private coverage map before this public artifact was drafted.

The significant-path index modifies path-based link prediction by penalizing high-degree intermediate nodes, treating a path through specific low-degree nodes as stronger similarity evidence than one through hubs. Twelve-network AUC experiments support the heuristic against five contemporaneous baselines, but random edge hiding, dataset-level parameter selection, AUC aggregation, and static undirected topology limit claims about future temporal links or modern learned graph predictors.

The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated.

The source is valuable because it preserves more than a favorable abstract. It records methodological boundaries, negative evidence, related work, and proposals. The principal archival risk is confusing the DEP-E's careful synthesis with independent reproduction. This intake prevents that collapse by using four labels: **source DEP-E report**, **directly inspected primary evidence**, **reviewer inference**, and **hypothesis/proposal**.

Bottom line: this is a valid source record for derived intake. Its strongest claims are bounded to the displayed evidence and exact source state. Its most durable contribution is the mechanism reconstructed below, together with an explicit agenda for testing when that mechanism fails.

### Principal strengths

- The significant-path index modifies path-based link prediction by penalizing high-degree intermediate nodes, treating a path through specific low-degree nodes as stronger similarity evidence than one through hubs. Twelve-network AUC experiments support the heuristic against five contemporaneous baselines, but random edge hiding, dataset-level parameter selection, AUC aggregation, and static undirected topology limit claims about future temporal links or modern learned graph predictors.
- For each candidate node pair, the method enumerates short connecting paths. A path receives a significance weight based on the degrees of its intermediate nodes; negative beta penalizes paths that pass through high-degree hubs.
- Path-length weighting controls how evidence decays with additional hops. The significant-path score aggregates heterogeneous path contributions instead of treating every path of the same length as equally informative.
- Evaluation randomly withholds observed edges into a probe set and ranks all unobserved pairs using the training graph. AUC estimates how often a hidden edge outranks a truly unobserved pair.

### Principal qualifications

1. Random train/probe edge splits can leak future topology and do not model temporal emergence, node arrival, or changing degree distributions.
2. AUC weights all non-edge rankings and may hide top-k precision, calibration, class imbalance, or practical intervention costs.
3. Path enumeration and parameter tuning can become costly on large dense graphs, while dataset-level choices may overfit the benchmark collection.
4. The 2014 baseline set predates graph neural link predictors and current temporal, attributed, and inductive methods.

## 1. Problem framing and research question

Common-neighbor and local-path scores count topological evidence but can overvalue paths through hubs. The paper asks whether intermediate-node degree can quantify path significance so that structurally specific connections contribute more to a missing-link score.

The archival question is narrower than product adoption: what does the record establish, what remains author- or DEP-E-reported, and what evidence would change the conclusion? That framing prevents novelty, benchmark, and feasibility claims from being strengthened merely by appearing in a curated repository.

## 2. Formal and technical reconstruction

### 2.1 Stage 1

For each candidate node pair, the method enumerates short connecting paths. A path receives a significance weight based on the degrees of its intermediate nodes; negative beta penalizes paths that pass through high-degree hubs.

### 2.2 Stage 2

Path-length weighting controls how evidence decays with additional hops. The significant-path score aggregates heterogeneous path contributions instead of treating every path of the same length as equally informative.

### 2.3 Stage 3

Evaluation randomly withholds observed edges into a probe set and ranks all unobserved pairs using the training graph. AUC estimates how often a hidden edge outranks a truly unobserved pair.

### 2.4 Stage 4

The study compares common neighbors, Adamic-Adar, resource allocation, local path, bounded local path, and significant path across twelve networks, averaging ten independent train/probe splits.

### 2.5 Assumptions and invariants

The reconstruction preserves four invariants. First, source identity is immutable: conclusions are tied to the exact DEP-E path and commit. Second, evaluation coordinates remain attached to every number. Third, proposed mechanisms are separated from empirical outcomes. Fourth, a useful score or qualitative example does not imply deployment safety.

Where the source contains equations, the equations define relationships under named assumptions; they are not guarantees that an optimizer finds a global solution or that a learned model generalizes. Where the source contains architectural diagrams, the diagrams describe intended dataflow; they do not prove implementation fidelity. Where the source contains code observations, inspectability is distinguished from execution.

## 3. Complete inventory and source-integrity assessment

The source directory contains exactly `README.md` and `predicting_missing_links_manuscript.md`. The README supplies classification, an itemized inventory, public-safe context, relevance, source policy, and a final Attribution Block. The substantive artifact supplies metadata, evidence accounting, technical synthesis, claims, limitations, proposals, references, and appendices. No PDF, HTML, TeX/source archive, extracted text, dataset, cache, model, or private run evidence is contained in the source directory.

The tracked inventory matched the files available at `904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff`. This intake did not modify the source. No source file was moved, copied into DEP-A, renamed, deleted, reclassified, or used as a template. The review is new derived prose.

Completeness of a repository record is not the same as completeness of every external source. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Public locators are listed below so future reviewers can repeat or extend the evidence check.

## 4. Architecture and information flow

The record can be represented as a traceable flow: **source identity -> assumptions and inputs -> transformation or decision -> reported evidence -> limitations -> reviewer interpretation -> proposed test**. This ordering matters. If a claim loses its source identity or evaluation coordinate, it becomes unsuitable for automated reuse.

At an implementation boundary, record the immutable input identity, configuration, selected policy, intermediate decision evidence, execution result, outcome metrics, and failures. A final aggregate alone cannot distinguish invalid input, stale calibration, flawed decision logic, runtime drift, or downstream task failure.

For composite evidence, each underlying record remains an independent branch. Cross-record synthesis may identify a recurring mechanism, but it must not pool incomparable metrics or erase domain-specific assumptions. For paper-centered evidence, tables, figures, equations, and appendices belong to the same source unit and should not be selectively separated from limitations.

## 5. Independent re-conceptualization

Significant paths are a specificity-weighted evidence network: a hub is common context and therefore weak evidence, while a chain of rare intermediates behaves like a more diagnostic feature. The information-retrieval analogy predicts benefit when degree approximates background frequency and failure in disassortative or hub-mediated systems where hubs are genuinely causal.

This re-conceptualization is a reviewer inference, not an author claim. It is useful only if it produces tests that can fail. The corresponding tests appear in the hypothesis and replication sections. A metaphor that cannot be falsified should not guide promotion, safety, or resource-allocation decisions.

## 6. Experimental design and evidence reconstructed

The evaluation design is reconstructed from the complete DEP-E and, for paper-centered records, directly checked canonical evidence. It separates data construction, configuration selection, comparator choice, metrics, exclusions, and uncertainty. These are not clerical details: each can change the meaning of a reported improvement.

The source's evidence is strongest where the tested configuration, denominator, and result are explicit. It is weaker where values depend on a selected checkpoint, single split, one seed, unverified code path, learned judge, composite score, or scenario-specific simulator. The absence of independent reproduction is not filled with reviewer confidence.

Quantitative values below are source-reported. No plot was digitized, no table was recomputed from raw data, and no code was run. Internal consistency checks compare claims within the public record; they do not create new experimental results.

## 7. Results: what is reported and what it means

### 7.1 Evidence unit 1

Across twelve disparate networks, the paper reports the significant-path score as the strongest or near-strongest AUC method, with negative beta consistently favoring low-degree intermediates.

### 7.2 Evidence unit 2

Examples include USAir AUC 0.960 for significant paths versus 0.956 resource allocation and Yeast 0.847 versus 0.836 bounded local path and 0.780 local path; improvements vary materially by topology.

### 7.3 Evidence unit 3

Parameter curves show continuous sensitivity to beta, and the alpha/beta choices are part of the method's operating point rather than universal constants.

### 7.4 Evidence unit 4

Results average ten random edge divisions and report dispersion in parentheses. Random hiding measures reconstruction of a static network, not necessarily chronological prediction under graph evolution.

### 7.5 Aggregate interpretation

The evidence supports a bounded conclusion: the proposed or synthesized mechanism is credible enough to motivate replication and controlled implementation work. It does not support universal superiority, unrestricted deployment, or a claim that omitted conditions are benign. The safest archival phrasing is “supported under the reported conditions” with every material exception retained.

## 8. Ablations and causal evidence

Ablations are most informative when one intervention changes at a time while data, budget, training, implementation, and evaluation remain fixed. The selected record contains component comparisons, scenario contrasts, or cross-record contrasts that help assign mechanism. None removes the need for repeated runs, matched baselines, or negative controls.

The strongest falsifier is to destroy or invert the mechanism's proposed signal while preserving capacity and budget. If performance remains unchanged, the explanatory story is incomplete. The second is to equalize hidden costs and selection opportunities. If the advantage disappears after matching them, the result was a resource or search effect rather than the named mechanism.

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment |
|---|---|---|
| Degree-weighted path heterogeneity improves link reconstruction over five listed topological baselines. | Ten-split AUC results across twelve networks generally favor significant paths. | Supported for the paper's static undirected benchmarks and tuned parameters. |
| A negative beta is universally optimal. | Curves favor hub penalties on the tested networks, but topology and task semantics vary. | Not established beyond the benchmark family. |
| Random hidden-edge AUC proves future-link prediction. | The protocol reconstructs randomly removed edges from a static graph. | Rejected as a temporal generalization. |
| This intake reproduced the AUC table. | No graph dataset, split, path enumeration, parameter sweep, or metric was executed. | Rejected. |

The table's assessment column is intentionally calibrated. “Supported” means the source contains evidence consistent with the claim in its stated envelope. It does not mean the reviewer reran the work. “Promising” means the evidence is directionally useful but incomplete. “Not established” identifies an evidence gap, not a negative experimental result.

## 10. External primary-source context and associated records

### Directly inspected or canonical public sources

- [https://arxiv.org/abs/1402.6225](https://arxiv.org/abs/1402.6225) — Canonical arXiv identity and version record.
- [https://arxiv.org/pdf/1402.6225](https://arxiv.org/pdf/1402.6225) — Complete canonical paper inspected page by page; no source document uploaded.
- [https://doi.org/10.1209/0295-5075/106/18008](https://doi.org/10.1209/0295-5075/106/18008) — Persistent primary-source identifier.

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

**Proposition:** Degree weighting will help most when intermediate-node degree approximates inverse information content and will hurt in networks whose hubs mediate genuine link formation.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 2

**Proposition:** Temporal splits and top-k precision will reduce average gains relative to random-edge AUC while preserving benefits on low-clustering networks.

**Predicted observation:** the preregistered comparison changes in the stated direction under matched coordinates.

**Falsifying observation:** the effect disappears, reverses, or is explained by denominator, budget, leakage, or implementation differences.

**Minimum test:** use immutable source/configuration identities, repeated seeds or folds when stochastic, raw case-level outputs, uncertainty intervals, and a declared stop rule.

### Hypothesis 3

**Proposition:** Learning the path penalty from training-only topology with nested validation will outperform one global beta without benchmark leakage.

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

> The significant-path index modifies path-based link prediction by penalizing high-degree intermediate nodes, treating a path through specific low-degree nodes as stronger similarity evidence than one through hubs. Twelve-network AUC experiments support the heuristic against five contemporaneous baselines, but random edge hiding, dataset-level parameter selection, AUC aggregation, and static undirected topology limit claims about future temporal links or modern learned graph predictors.

The selected DEP-E is preserved as evidence, not copied or reclassified. This DEP-A adds a new archival interpretation tied to the exact source state. Its durable value lies in keeping mechanism, evidence, conditions, limitations, and falsifiers together.

## Appendix A. Complete coverage ledger

| Source item | Material covered | Treatment and boundary |
|---|---|---|
| `README.md` | complete manifest and attribution boundary | read from beginning to end; every heading, table row, claim, limitation, proposal, URL, related-record reference, and attribution entry accounted for |
| `predicting_missing_links_manuscript.md` | complete substantive DEP-E artifact with 2173 words | read from beginning to end; every heading, table row, claim, limitation, proposal, URL, related-record reference, and attribution entry accounted for |
| `arXiv:1402.6225 complete canonical PDF` | Predicting missing links via significant paths; 6 pages and 4705 extracted words | PDF header and terminal marker passed; every page inspected; complete body, equations, tables, figures, limitations, appendices where present, acknowledgments, and references accounted for; no experiment or code rerun |
| `canonical PDF page 1` | 876 extracted words | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 2` | 819 extracted words | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 3` | 867 extracted words; labels: FIG. 1, Figure 1, TABLE I, Table I | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 4` | 414 extracted words; labels: FIG. 2, Figure 2, Table II, Table 1 | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 5` | 889 extracted words; labels: TABLE II | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `canonical PDF page 6` | 840 extracted words | page read in full; narrative, mathematical notation, algorithms, diagrams, plots, tables, captions, footnotes, and qualifications retained at the evidence boundary |
| `central equations and algorithms` | 50 equation-number candidates plus all displayed/inline mathematical definitions | variables, signs, objectives, constraints, and guarantee boundaries reconstructed; extraction ambiguity preserved rather than guessed |
| `appendix, references, disclosures, and final page` | appendix detected: True; references detected: False | supplementary settings, failure examples, source lineage, acknowledgments, and end-of-document integrity checked |
| `private evidence-layer map` | source DEP-E report; directly inspected primary evidence; reviewer inference; hypothesis/proposal | all public claims assigned to one evidence layer; no reproduction or source-copy claim |

The coverage ledger accounts for both tracked source files and every section, table, figure, equation group, claim, limitation, attribution entry, and cited primary source that materially affects the record. Closely related units are grouped only when their evidentiary role is the same; no favorable table is treated as independent of its settings or limitations.

## Appendix B. Source and evidence notes

### Evidence boundary

The complete repository record was inspected at the pinned commit. The complete canonical paper was directly checked in addition to the complete DEP-E record. Paper-level claims below are attributed to the authors and remain unreplicated. Source-document bytes and private extraction material were not uploaded. Experiments, code, simulations, models, and datasets were not executed. Numerical claims remain author- or DEP-E-reported unless explicitly labeled reviewer inference.

### Provenance pair

`BL-DEPPAIR-20260818-4E58E6FE` records `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. DEP-A intake status and deposition status become complete only after the new package and matching rows in both review ledgers are atomically submitted and remotely verified.

## Footnotes

[^source-dep]: Complete source DEP-E record: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260817-Predicting%20missing%20links
[^source-state]: Exact source commit: https://github.com/Delphoa/Black-Lake/commit/904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff
[^primary-one]: Primary public source: https://arxiv.org/abs/1402.6225
[^primary-two]: Additional complete or canonical source locator: https://arxiv.org/pdf/1402.6225
[^repository]: Black Lake repository and live class policy: https://github.com/Delphoa/Black-Lake

The source DEP-E identity is preserved by its public repository locator,[^source-dep] exact source commit,[^source-state] and canonical primary record.[^primary-one] The evidence check also used the additional locator recorded above.[^primary-two] Repository policy was read from the live project before drafting.[^repository]
