# Coupled Educational State as an Auditable Control System

## A whitepaper-grade archival intake review of the CogEvo-Edu DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260714-CogEvo Edu Agents`  
**Source commit:** `398f692812550135476e8d560be1d2a01fa2982e`  
**Paired task indicator:** `BL-DEPPAIR-20260715-87750E15`  
**Direction:** `DEP-E -> DEP-A`  
**Review date:** 2026-07-15  
**Review scope:** complete two-file repository record, canonical paper identity and full-paper structure, technical reconstruction, claim vetting, external context, re-conceptualization, and replication planning  
**Provenance boundary:** source action was review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes  
**Reproduction boundary:** the paper, benchmark, and software were not independently rerun or reproduced.

---

## Executive assessment

The reviewed DEP-E record is a coherent, public-safe research package containing an inventory README and a long analytical manuscript about CogEvo-Edu, an educational multi-agent architecture organized around student-state consolidation, knowledge-base lifecycle control, and meta-level teaching orchestration. Both tracked files were read in full. The record supplies explicit source identities, a layered evidence ledger, the reported DSP-EduBench comparison, limitations, proposed implementations, and a source-locality statement. Its strongest archival value is not the headline benchmark score. It is the recognition that memory, retrieval, and orchestration form one coupled stateful system whose errors can reinforce one another over time.

The canonical arXiv record and complete HTML article were inspected directly. They confirm a six-section paper with related work, three method layers, benchmark construction, an evaluation protocol, one comparative table, three figures, and a conclusion.[^paper] Direct inspection supports the architecture and Table I values. It also reveals the evidence constraint that dominates this review: the evaluation relies on simulated learner profiles and an LLM-as-a-Judge ensemble, while the paper does not expose enough benchmark instances, run counts, judge prompts, agreement statistics, or longitudinal learner outcomes to establish educational effectiveness.

The most durable interpretation is **auditable coupled state adaptation**. CogEvo-Edu is not merely a collection of agents. It is a controller whose policy reads a mutable learner model and a mutable knowledge store, then changes both short-horizon actions and long-horizon parameters. That makes lineage, rollback, protected evidence, and calibration central design requirements. The source record already identifies this tension: the system calls its profile self-correcting while allowing knowledge to be physically deleted. Correction requires evidence; irreversible forgetting can destroy it.

Bottom line: the DEP-E record is technically rich and internally careful, and the underlying paper offers a plausible systems thesis. The reported 5.32-to-9.23 score change is a useful within-benchmark signal, not proof of improved learning. Whitepaper-grade archival status is justified when the artifact is treated as a complete review of the repository record with a verified paper boundary, rather than as an independently reproduced educational result.

### Principal strengths

- The three-layer decomposition makes state, retrieval, and control interfaces visible enough to audit.
- The DEP-E manuscript labels paper reports, reviewer interpretations, and recommendations separately.
- Exact values from the only comparative table are preserved with appropriate non-reproduction caveats.
- Privacy, profile correction, evidence retention, destructive forgetting, and controller-update risks are treated as first-class research issues.
- The source-locality policy is explicit: the public record contains derived Markdown and public URLs, not downloaded source documents.

### Principal qualifications

1. DSP-EduBench appears to be a constructed, simulated environment without a released package or documented independent validation.
2. The five configurations are not a complete factorial ablation, so component interactions and causal attribution remain unresolved.
3. LLM-judge scores are response-quality measurements, not mastery, retention, transfer, motivation, equity, or classroom utility.
4. The outer-loop controller is described at the objective level more clearly than at a reproducible algorithmic level.
5. Persistent student state can become sensitive profiling data and requires governance beyond ordinary chat history handling.

---

## 1. The problem and research question

The practical problem is long-horizon tutoring under bounded context. A tutor must remember what a learner understands, retrieve the right evidence for the present misconception, select an instructional strategy, and update its beliefs when new interactions contradict old ones. Static retrieval treats the course corpus as fixed. A sliding dialogue summary treats learner state as prose without a strong evidence model. A monolithic tutor asks one model to diagnose, teach, retrieve, and decide when to change course.

CogEvo-Edu asks whether these functions should evolve together. The Cognitive Perception Layer (CPL) turns recent interactions into structured learner features with confidence. The Knowledge Evolution Layer (KEL) scores knowledge chunks using use, recency, and neighborhood density, then keeps, compresses, or removes them. The Meta-Control Layer (MCL) chooses specialist roles, teaching modes, difficulty, and retrieval settings, while a slower outer loop is intended to update policy and memory/lifecycle hyperparameters.

The core research question is therefore broader than “does multi-agent tutoring score well?” It is: **can a coupled controller maintain useful learner state and knowledge under finite resources while adapting teaching behavior without accumulating opaque or irreversible errors?** The paper tests the response-quality part of that question. It does not yet test the full safety, privacy, correction, or longitudinal-learning burden.

Prior method families include conventional intelligent tutoring with explicit skill models, static RAG, long-context or summarized conversational memory, general agent-memory systems, and heuristic multi-agent tutoring. The paper’s gap is the absence of a single adaptation loop spanning learner representation, knowledge lifecycle, and teaching orchestration. That gap is plausible, although the novelty claim should remain scoped: each ingredient has predecessors; the contribution is their particular coupling and evaluation inside one DSP tutoring prototype.

---

## 2. Technical reconstruction

### 2.1 State and interfaces

CPL maintains a short-term store of recent question-answer turns and a long-term set of structured features. A feature has a key, a value, and a confidence. Once the short-term window reaches a trigger, a model extracts candidate features and compares them with existing entries. Agreement increases confidence toward one; contradiction decreases confidence in proportion to its current value. The update shape is interpretable, but the meaning of “agreement,” “contradiction,” identity continuity, and evidence sufficiency is delegated to semantic processing that the paper does not operationally specify.

KEL assigns each knowledge chunk a weighted score. The score combines normalized interaction frequency, exponential decay since last use, and an average similarity to nearby chunks as a semantic-density proxy. Two thresholds create active, compressed, and deleted tiers. This is a resource-allocation heuristic, not a proof of optimal storage. Frequency favors commonly requested material; recency penalizes dormant material; density favors material that resembles its neighborhood. Rare prerequisites, minority learning paths, contradictory evidence, and novel but important material may score poorly for reasons unrelated to educational value.

MCL observes the structured learner profile, active knowledge subset, and current task. Its action comprises a lead specialist, teaching strategy, difficulty, and retrieval configuration. The inner loop selects actions per turn. The outer loop is described as maximizing expected learning gain across students and sessions while updating policy parameters and CPL/KEL hyperparameters. The source names mastery improvement, disappearance of error patterns, and retention as long-horizon signals, but it does not provide an executable update schedule, estimator, optimizer, data partition, or release gate.

### 2.2 Information flow

The architecture forms a feedback cycle:

1. interaction events enter short-term memory;
2. consolidation proposes and updates learner features;
3. learner state and task context influence retrieval and agent routing;
4. retrieved material and teaching actions produce a response;
5. judged outcomes inform future state and, conceptually, the slower controller;
6. usage signals alter knowledge scores and can eventually compress or remove evidence.

This cycle is the central mechanism. Errors are not isolated. A false learner feature can select the wrong strategy. That strategy can generate interactions that appear to confirm the feature. Retrieval choices can increase the usage score of favored material while starving alternatives. A judge-trained outer loop can then optimize the feedback pattern rather than genuine learning.

### 2.3 Guarantee boundary

No mathematical guarantee establishes accurate learner-state recovery, optimal retention, safe deletion, policy convergence, or learning improvement. The confidence update and value function are exact formulas once their inputs exist, but the semantic labels and weights are model- and configuration-dependent. The only deterministic protections suggested by the source DEP are reviewer proposals: typed state contracts, evidence identifiers, protected anchors, recoverable cold pages, versioned policies, and rollback. Those are not reported features of the paper’s evaluated system.

---

## 3. Source inventory and integrity assessment

The source record contains exactly two tracked files. `README.md` defines the DEP-E identity, tags, inventory, source-withholding policy, related records, and attribution. `cogevo_edu_agents_manuscript.md` supplies metadata, an eight-source evidence ledger, a technical summary, benchmark values, claims, methodology, constraints, observations, product ideas, source references, selection and integrity notes, and a final validation checklist. No `.source` directory or source document appears in the repository record.

The inventory is complete and consistent with `git ls-files` at the source commit. The README’s final section is an Attribution Block. Canonical locators include the arXiv abstract, full-paper HTML, PDF, source package, and related DOI. Repository-relative references point to three inspected Black Lake records. The manuscript’s internal source separation is generally strong: paper evidence is distinguished from related-DEP context, and related records are not treated as validation of CogEvo-Edu.

Direct canonical inspection confirmed title, five authors, v1 status, submission date, categories, related DOI, full-text links, and the article structure.[^record] The complete HTML contains the method, benchmark description, Table I, three figure references, and conclusion. This run did not download or redistribute the paper. The DEP-E reports prior local PDF, HTML, and TeX integrity checks; those private bytes were not available inside the repository record and are therefore treated as DEP-E process claims, not re-performed file-integrity evidence.

The record has no obvious local path, username, machine name, credential, or private timestamp leak. It does contain public date markers and repository-relative paths, which are appropriate. The source object is complete for the present review: every tracked file was read beginning to end, and each material claim or limitation is represented in the coverage ledger below.

---

## 4. Architecture and operational pipeline

From a systems perspective, CPL should be treated as an evidence-backed state reducer, KEL as a tiering policy, and MCL as a policy router. The paper’s terminology can obscure that these components have different failure semantics. CPL errors are classification and consolidation errors. KEL errors are ranking, compression, and deletion errors. MCL errors are decisions under uncertain state. Their monitors and rollback mechanisms should differ.

A robust implementation would preserve raw event references separately from derived learner features, attach policy and model versions to every update, and prevent one consolidation pass from overwriting the only contradictory evidence. KEL should initially demote data to a recoverable tier rather than delete it. MCL policy updates should occur offline against frozen evaluation sets and should not automatically rewrite memory thresholds. A public-facing tutor should expose correction paths and data-retention controls to the learner or institution.

The paper describes soft orchestration among explanation, diagnosis, question-generation, and knowledge-reconstruction roles. The architecture does not require those roles to be separate models; they may be prompts or policies over one backbone. This distinction matters for attribution. The benchmark keeps Qwen3-14B as the instructional backbone, so observed gains may come from structured prompting, state visibility, retrieval changes, or controller logic rather than agent plurality itself.

---

## 5. Independent re-conceptualization

### 5.1 Evidence-bearing adaptive control

Reviewer inference: CogEvo-Edu is best understood as an adaptive controller over two mutable stores. The learner model is a belief state; the knowledge store is a resource pool; the teaching action is a control signal; and judged interaction outcomes are feedback. This mapping clarifies why observability and provenance matter. If the controller cannot observe true learning and instead observes model-judge preferences, it may optimize a proxy.

The analogy breaks because learners are not stationary plants, teaching actions change motivation and trust, and ethical rights constrain what state may be retained. A control formulation cannot justify invasive profiling or irreversible forgetting. It is useful only as a way to expose feedback, state uncertainty, and update timing.

### 5.2 Learned handoff with recoverable memory

The three layers also resemble a learned handoff system: short-term events are handed into persistent features; knowledge is handed between active and compressed tiers; tasks are handed among teaching roles. Every handoff should include evidence, confidence, version, and reversal semantics. This predicts that systems with reversible, evidence-bearing handoffs will recover from injected false learner features faster than confidence-only systems.

### 5.3 Transferable principle

The transferable principle is not “use more agents.” It is **couple adaptation while decoupling evidence and rollback**. Components may share state and objectives, but each state transition must remain independently inspectable and reversible. This principle applies to support agents, clinical decision support, personalized search, and operations assistants, with domain-specific privacy and authorization constraints.

---

## 6. Experimental design and evidence reconstructed

DSP-EduBench combines heterogeneous DSP resources, simulated learner profiles, and long-range scripts involving conceptual discrimination, fault diagnosis, and code debugging. Ground truth reportedly includes solutions, key-point checklists, and an ideal teaching strategy. The instructional backbone is Qwen3-14B across five configurations. GLM-4.5, DeepSeek-V3.1, and Qwen3-max independently score each turn from one to ten on factual correctness, contextual relevance, memory consistency, personalization alignment, knowledge guidance, and strategy flexibility.

The five settings are: plain LLM, static RAG, simple memory, a single agent with CPL and KEL but fixed teaching control, and the full CogEvo-Edu architecture. This design gives useful directional comparisons. Static RAG isolates some retrieval effect; simple memory isolates a lightweight state mechanism; the single-agent setting exposes the effect of adding meta-control and specialist routing to CPL/KEL.

The design does not fully isolate all three components. A factorial experiment would evaluate CPL, KEL, and MCL individually and in every combination while holding prompts, retrieval budget, context size, model calls, and judge exposure constant. The reported setup also lacks visible sample counts, run counts, generation seeds, judge agreement, confidence intervals, human validation, or pre-registration. Because scores are averaged over turns and judges, the independence unit and variance are unclear.

Dataset construction may create leakage or circularity if simulated profiles, ideal strategies, tutor prompts, and judge rubrics share assumptions. No direct evidence of leakage is reported, but the absence of a released benchmark prevents auditing it. Simulated profiles are useful for controlled failure injection; they do not establish performance with real learners.

---

## 7. Results and quantitative audit

The complete paper and DEP-E both report the same Table I values. The plain LLM averages 5.32; static RAG 5.97; simple memory 6.45; the single-agent CPL/KEL setting 6.42; and the full system 9.23. The full system’s six scores are 9.3, 9.1, 9.5, 9.2, 8.9, and 9.4. Every reported dimension exceeds the corresponding baseline values.[^table]

The pattern is informative. Static RAG most clearly lifts factual correctness. Simple memory most clearly lifts memory consistency and personalization. The single-agent setting raises factual and contextual scores but has the lowest strategy-flexibility result among the non-plain systems. The full system then rises sharply across all dimensions. This is consistent with an interaction effect among structured state, knowledge selection, and adaptive teaching control.

It is not sufficient to conclude causality. The full configuration may have more prompt structure, calls, routing opportunities, or generated context. Judge models may reward visible personalization language and strategy switching. No cost-normalized comparison is supplied. An average of ordinal one-to-ten judgments is convenient but should not be treated as an interval-scale measurement of educational gain.

No runtime, token cost, storage growth, consolidation error, retrieval precision, profile accuracy, or deletion-recovery result is reported in the central table. The paper’s claim that the method avoids increased inference overhead is therefore not quantitatively established. The review classifies the result as **promising but limited: strongly favorable within the constructed judge benchmark, unverified for real learning and operational cost**.

---

## 8. Ablations and causal evidence

The baseline suite is an architectural comparison, not a full ablation. Static RAG, simple memory, and the single-agent variant change multiple mechanisms relative to one another. There is no CPL-only, KEL-only, MCL-only, frozen-profile, no-deletion, or no-outer-loop condition. There is no sweep over confidence learning rate, time decay, semantic-density weight, thresholds, retrieval scope, or profile consolidation cadence.

The absence of repeated training or inference seeds is material because the benchmark involves generative tutors and generative judges. Averaging three judge models reduces dependence on a single judge but does not measure shared bias or disagreement. An agreement matrix, calibration set, human reference, and turn-level bootstrap would clarify uncertainty.

The highest-value causal test is a fixed-backbone factorial ablation with the same model-call and token budget. Another is to inject known false learner features and measure correction time, downstream strategy error, and evidence retention. A third is to compare physical deletion, compressed summaries, and recoverable cold storage under rare-query evaluation. These tests would directly challenge the reviewer’s mechanism thesis.

---

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| Retrieval, learner memory, and teaching control should evolve together. | The architecture couples CPL, KEL, and MCL, and the full configuration has the best reported table values. | Supported as a systems hypothesis under the tested benchmark. | The comparison does not isolate every interaction or prove transfer to real learners. |
| CPL creates self-correcting learner profiles. | A confidence update responds differently to agreement and contradiction. | Promising but not established. | Semantic contradiction detection, identity, evidence lineage, and correction accuracy are not evaluated. |
| KEL achieves an optimal storage-coverage balance. | A weighted score and two thresholds determine active, compressed, and deleted tiers. | Overstated. | No optimality proof or exhaustive storage-quality frontier is shown. |
| CogEvo-Edu raises the overall score from 5.32 to 9.23. | Table I in the complete paper and DEP-E record. | Strongly supported as an author-reported benchmark result. | Not independently reproduced; sample size and uncertainty are absent. |
| The system improves all six evaluated indicators. | Each full-system cell exceeds each comparator cell. | Supported under the reported judge protocol. | Indicators are LLM judgments, not direct learning outcomes. |
| Multi-agent orchestration causes the gain. | Full system exceeds the fixed single-agent setting. | Unresolved. | Other policy, prompting, call-budget, and outer-loop differences may contribute. |
| The design reduces retrieval piling and catastrophic forgetting. | KEL and CPL are explicitly designed for those problems. | Not established empirically as separate outcomes. | No retrieval precision, forgetting curve, or profile-correction metric is reported. |
| The system is ready for educational deployment. | No deployment study is reported. | Not established. | Privacy, consent, human oversight, fairness, retention, and efficacy require dedicated evidence. |

---

## 10. External primary-source context

The official arXiv record identifies v1, the five authors, artificial-intelligence and multi-agent categories, the complete HTML/PDF/source links, and a related 2026 DOI.[^record] The complete HTML is concise and contains only one quantitative comparison table. No official code or DSP-EduBench repository is linked from the record as of this review. Absence of a release is evidence about reproducibility, not evidence that no private implementation exists.

The DEP-E relates CogEvo-Edu to three repository records. Agent State Review motivates replayable persistent state and monitoring. Agent Memory Forensics motivates trace-level defenses around long-lived memory. CompressKV motivates calibration and recovery for semantic retention under resource limits. These are relevant analytical neighbors, but they are processed Black Lake artifacts, not independent replications of CogEvo-Edu.

Primary educational-AI context in the paper includes conventional tutoring models, RAG, agent memory, multi-agent frameworks, and LLM-as-a-Judge evaluation. This review does not claim priority over those lines. The architecture’s novelty is best described as a particular coupled control formulation for DSP tutoring rather than the first use of memory, retrieval, agents, or learner models.

---

## 11. Research notes and critical considerations

The strongest internal tension is evidence destruction. A learner profile can be corrected only if conflicting interactions remain traceable. KEL can physically delete chunks based partly on use and density. A chunk judged low-value today may be needed to explain a historical profile update tomorrow. Production designs should separate active retrieval tiering from legal retention and audit evidence.

Confidence is not probability unless calibrated. CPL’s scalar confidence is updated by a fixed learning rate, but no empirical mapping to correctness is provided. Downstream agents may over-trust a high number. The state schema should include evidence count, recency, contradiction count, protected status, and uncertainty source instead of a single confidence field.

The outer loop is a governance boundary. Updating memory thresholds and teaching policy from judged trajectories can create silent distribution shifts. Changes should be versioned, evaluated offline, reviewed, and rolled out with canaries. Learners should not unknowingly become experiments for autonomous parameter changes.

The benchmark’s LLM judges share the broad model ecosystem with the instructional system. Ensemble diversity is useful, but correlated preferences can survive averaging. Human educators and actual learners are needed for construct validity. Delayed retention, transfer, misconception correction, and student agency are more decision-relevant than response polish alone.

Profile content may include abilities, preferences, repeated errors, and inferred traits. These can become sensitive educational records. Minimum viable governance includes purpose limitation, consent, minimization, access control, correction rights, retention periods, encryption, and separation from identity wherever possible.

---

## 12. Potential implications

Scientifically, the paper suggests that state, retrieval, and policy evaluations should be designed jointly. A memory benchmark that ignores downstream action cannot reveal whether a remembered fact improves teaching. A retrieval benchmark that ignores learner-state uncertainty cannot reveal whether the right material was selected for the wrong reason.

For system design, the useful abstraction is a typed state contract shared across components. Each teaching action should cite the learner-state version, knowledge snapshot, policy version, and evidence IDs used. This makes counterfactual review possible: an investigator can ask whether a different state or protected chunk would have changed the action.

For deployment, recoverability should precede optimization. Cold paging is safer than deletion; offline policy tuning is safer than continuous self-modification; synthetic profiles are safer than early experimentation on real learners. The artifact does not justify classroom automation, but it does justify building better evaluation infrastructure.

For governance, the coupling creates joint accountability. A harmful recommendation cannot be attributed only to the final model if memory consolidation, retrieval tiering, and controller updates shaped the decision. Audit logs must cross component boundaries without exposing raw learner content in public reports.

---

## 13. Falsifiable hypotheses

### Hypothesis 1: evidence-linked profiles correct faster

**Proposition:** A profile schema that preserves supporting and contradicting event IDs will recover from injected false features faster than confidence-only consolidation.  
**Motivating evidence:** The source uses confidence momentum but does not retain explicit lineage in the formal feature representation.  
**Predicted observation:** Evidence-linked systems will require fewer corrective turns and produce fewer strategy errors after contradiction.  
**Falsifier:** No improvement in correction latency or downstream decisions at equal model and token budgets.  
**Minimum test:** Synthetic learner scripts with known feature reversals, blinded scoring, and immutable event logs.

### Hypothesis 2: reversible tiering dominates deletion on tail needs

**Proposition:** Recoverable cold pages will match active-storage savings while reducing rare-query failure relative to physical deletion.  
**Motivating evidence:** KEL uses low frequency and low density as negative signals, both of which can characterize rare prerequisites.  
**Predicted observation:** Cold paging yields similar average quality and better tail recall, with bounded restoration latency.  
**Falsifier:** Deletion matches or exceeds tail quality and auditability under the same storage budget.  
**Minimum test:** Public toy curriculum, synthetic access histories, rare-need query set, and fixed storage limits.

### Hypothesis 3: routing accounts for less gain than state visibility

**Proposition:** Explicit typed state and retrieval controls explain more of the score gain than multiple named teaching agents.  
**Motivating evidence:** All configurations use one instructional backbone, and the comparison does not isolate role plurality.  
**Predicted observation:** A single-policy controller with the same state contract approaches the multi-agent score under equal calls.  
**Falsifier:** Multi-agent routing retains a large advantage after state, prompts, and compute are matched.  
**Minimum test:** Factorial ablation with token/call parity and identical judge protocol.

---

## 14. Deployment and governance considerations

Appropriate use is limited to research prototypes, synthetic learners, public curricula, and offline evaluation until real-learning and privacy evidence exists. Poor fit includes high-stakes placement, disability inference, disciplinary decisions, or unsupervised personalization where state errors could materially affect a learner.

Required safeguards include evidence-linked state, protected curriculum anchors, recoverable tiering, explicit consent and correction paths, privacy-minimized logs, offline controller updates, independent human evaluation, rollback, and rejection of actions when state uncertainty is high. A deterministic policy should prevent deletion of the only evidence supporting a learner feature. Public reports should expose aggregates and versions, not raw dialogue or identity data.

---

## 15. Replication and falsification agenda

The first priority is benchmark release or author-provided reconstruction material: DSP-EduBench instances, profile scripts, knowledge sources, prompts, configuration files, judge rubrics, run counts, seeds, and aggregation code. A clean-room team should reproduce Table I before altering the method. Every score should be accompanied by turn count, profile count, judge disagreement, and confidence intervals.

Second, run the full CPL/KEL/MCL factorial design with equal model calls, retrieval budget, context length, and prompt information. Report profile-feature precision, contradiction correction, retrieval precision/recall, storage, latency, strategy selection, and response quality separately. Preserve failed and excluded episodes.

Third, validate the proposed mechanism directly. Inject incorrect learner features, stale knowledge, misleading high-frequency chunks, rare prerequisites, and controller regressions. Measure propagation paths and recovery. A successful system should localize the faulty transition and restore a prior consistent snapshot.

Fourth, normalize evaluation with human educators and, only after governance approval, consented learner studies. Measure immediate correctness, delayed retention, transfer, misconception repair, user trust, correction burden, and subgroup performance. Judge models may remain an operational metric but should not be the sole release criterion.

Fifth, archive a public-safe evidence bundle: code/version identifiers, benchmark manifests, aggregate results, policy versions, model-call budgets, failure taxonomy, and privacy review. Raw learner interactions and proprietary course material should remain in authorized storage.

The highest-priority falsifier is a controlled result showing that the full-system advantage disappears under call/token parity or fails to predict human learning. Either outcome would narrow the contribution from educational effectiveness to benchmark-specific response orchestration.

---

## 16. Durable restatement

> CogEvo-Edu proposes a tutor whose learner model, knowledge store, and teaching policy adapt together. Its reported benchmark strongly favors the coupled configuration, but the evidence is a simulated DSP environment scored by model judges, not a reproduced learning study. The architecture’s durable value is the exposure of state and control interfaces; its durable risk is that errors, deletion, and proxy optimization can reinforce one another unless every transition carries evidence, versioning, and recovery.

The archival lesson is to preserve the source record as a careful systems hypothesis with exact reported numbers and explicit limits. Future work should test evidence-bearing profiles, reversible knowledge tiering, compute-matched orchestration, and human learning outcomes before making deployment claims.

---

## Appendix A. Complete coverage ledger

| Source item | Material covered | Review treatment | Boundary |
|---|---|---|---|
| DEP-E `README.md` | identity, tags, inventory, relationships, source policy, Attribution Block | fully inspected and reconstructed in Sections 3 and 10 | repository metadata, not empirical evidence |
| Manuscript front matter and source metadata | paper version, authors, sources, access limits | Sections 3 and 10 | private source-file integrity is DEP-E-reported |
| Evidence ledger and executive summary | architecture, benchmark, related DEP roles | Executive assessment and Sections 2, 6, 7 | related records are contextual only |
| Detailed CPL discussion | short/long memory and confidence update | Sections 2, 4, 11 | semantic classifier behavior unverified |
| Detailed KEL discussion | frequency, decay, density, thresholds, compression/deletion | Sections 2, 5, 11 | optimality and safe deletion not established |
| Detailed MCL discussion | state, action, inner/outer loops | Sections 2 and 4 | outer-loop implementation incomplete |
| DSP-EduBench and Table I | profiles, scripts, judges, five configurations, six scores | Sections 6 through 8 | no independent reproduction or uncertainty |
| Claims, methodology, scope, observations | evidence calibration and review process | Sections 9 and 11 | random-selection history is background provenance |
| Improvements, implementations, MVP | reviewer proposals | Sections 12 through 15 | proposals are not paper results |
| Source references and local-integrity appendix | URLs, local withholding, completeness claims | Appendix B | no source files committed |
| Paper Figure 1 | three-layer architecture | Sections 2 and 4 | conceptual diagram; no quantitative evidence |
| Paper Figure 2 | LLM-as-a-Judge pipeline | Section 6 | protocol details remain incomplete |
| Paper Figure 3 | radar visualization of Table I | Section 7 | redundant visualization of reported table |
| Paper Table I | all five configuration rows and six dimensions | Section 7 and claim table | ordinal judge scores without intervals |
| Paper equations | CPL confidence, KEL value/density, MCL state/action/objective | Section 2 | explained qualitatively; not independently derived or executed |
| Paper conclusion and references | claimed implications and intellectual context | Sections 10 and 16 | references used for context, not independent validation |

No additional numbered tables, figures, algorithms, theorem statements, or appendices appear in the complete canonical HTML. The paper is concise; the DEP-E manuscript adds substantially more governance and implementation analysis than the paper itself.

---

## Appendix B. Source and evidence notes

### Primary reviewed artifact

The primary object was the complete repository record at `.lake-data/DEP-E/DEP-E-20260714-CogEvo Edu Agents` at source commit `398f692812550135476e8d560be1d2a01fa2982e`.[^dep][^provenance] Both tracked Markdown files were read in full. The source action was review-only. No source DEP file was modified, moved, copied, renamed, or reclassified.

### Directly inspected primary evidence

- https://arxiv.org/abs/2512.00331
- https://arxiv.org/html/2512.00331
- https://doi.org/10.48550/arXiv.2512.00331
- https://doi.org/10.1109/CSCWD68734.2026.11582082
- https://github.com/Delphoa/Black-Lake

### Evidence boundary

The complete DEP-E bundle and complete canonical HTML article were inspected. The paper was not downloaded into the repository. Private PDF, TeX, cache, and integrity records described by the DEP-E were not re-opened from this checkout. No benchmark data, code, model, judge prompt, or experiment was executed. Paper-level numerical claims are labeled as paper reports and were checked against the complete HTML where stated. Reviewer inference and hypotheses are explicitly marked. Independent reproduction was not performed.

### Provenance pair

Paired task indicator `BL-DEPPAIR-20260715-87750E15` records the one-way direction `DEP-E -> DEP-A`. Source action: review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. New derived data generated: yes. Intake status and deposition status become complete only when this artifact, its README, and both matching ledger rows are submitted atomically.

---

## Footnotes

[^paper]: Wu, Yefeng, et al., “CogEvo-Edu: Cognitive Evolution Educational Multi-Agent Collaborative System,” arXiv:2512.00331v1, complete HTML at https://arxiv.org/html/2512.00331.
[^record]: Canonical arXiv metadata and full-text links: https://arxiv.org/abs/2512.00331.
[^table]: Table I in the complete canonical HTML reports the five configurations and the 5.32, 5.97, 6.45, 6.42, and 9.23 averages: https://arxiv.org/html/2512.00331.
[^dep]: Source DEP-E record in the public repository: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-CogEvo%20Edu%20Agents.
[^provenance]: Source commit used for selection and provenance: https://github.com/Delphoa/Black-Lake/commit/398f692812550135476e8d560be1d2a01fa2982e.
