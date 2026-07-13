# State as an Auditable Control Surface

## Whitepaper-grade archival intake review of the complete `DEP-E-20260708-Agent State Review` repository record

**Artifact prepared:** 2026-07-14  
**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260708-Agent State Review`  
**Source commit:** `e4dbe1a71bdef28ee7c38b7d6e8ecec707890b73`  
**Paired task indicator:** `BL-DEPPAIR-20260714-C83F1D29`  
**Direction:** `DEP-E -> DEP-A`  
**Provenance action:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes  
**Review scope:** complete repository-record reconstruction, claim vetting, external primary-record checks, independent re-conceptualization, failure analysis, and replication agenda  
**Reproduction boundary:** every tracked file in the source DEP-E was read in full; canonical public records were checked for the ten named papers; no paper experiment, code repository, dataset, or benchmark was rerun; most paper-level evidence remains abstract-level or source-DEP-reported

---

## Executive assessment

### The record in one sentence

This DEP-E is a structured synthesis arguing that persistent or latent state—code history, evidence selections, monitor calibration, parameter localization, reusable adapters, deployment models, object memory, durable storage, and activation subspaces—should be reviewed as an explicit object rather than treated as invisible infrastructure.

### The deeper idea

The durable mechanism is **state externalization under an evidence contract**. A system becomes more reviewable when the information that affects future behavior is given an owner, lifetime, representation, update rule, and verification method. The source record develops that theme across ten research threads, with its strongest treatment reserved for persistent coding-agent control, recursive evidence replay, and online safety monitoring. The remaining threads are used as cross-domain evidence that similar review questions recur at model, agent, and infrastructure layers.

### Bottom-line judgment

As a repository artifact, the DEP-E is coherent, useful, and unusually transparent about its evidence limits. It does not provide ten full-paper reviews and should not be read as one. Its strongest contribution is taxonomic and operational: it turns “state” from a vague metaphor into a review target with concrete examples of storage, replay, calibration, localization, and durability. Its principal weakness is evidentiary asymmetry. ReContext receives method and results treatment, while seven other papers are summarized primarily from canonical abstracts and project pages. The synthesis therefore supports a research program and an audit design more strongly than it supports general empirical conclusions.

The current canonical record for *Distributed Attacks in Persistent-State AI Control* is version 2, revised after the source DEP-E’s v1-oriented review state. That does not invalidate the DEP-E, but it means the public record has evolved and any paper-level quantitative reuse should cite the current version directly.[^persistent]

### Principal strengths

- The README and main artifact expose their source inventory, access depth, uncertainty, reproduction boundary, and public-safety constraints.
- The synthesis is mechanism-oriented: link tracking, evidence replay, risk-calibrated alarms, parameter localization, and durable interfaces are connected through observable state rather than topic similarity alone.
- The record separates source claims, reviewer interpretation, and proposed implementation ideas more consistently than a conventional narrative digest.
- It preserves defensive boundaries around coding-agent attacks and avoids claiming code execution or experimental reproduction.

### Principal qualifications

1. The primary object reviewed here is the complete DEP-E repository record, not ten complete scholarly papers.
2. The bundle’s cross-domain “state as a review object” thesis is a reviewer synthesis, not a conclusion jointly established by the cited authors.
3. Several quantitative statements are reported through abstracts or the source DEP-E’s earlier inspection and have not been independently reconstructed from complete papers in this intake.
4. A repository-level synthesis can reveal shared control structure, but it cannot by itself establish that monitoring, replay, unlearning, storage, and interpretability share a single causal theory.

---

## 1. The problem and research question

### 1.1 What the DEP-E is actually solving

The immediate task was to transform a prior Black-Lake-Data technology-intelligence package into a durable research artifact. The source DEP-E does more than restate that package. It asks what kind of evidence future reviewers need when AI behavior depends on information that persists across time, contexts, parameters, or physical systems.

The practical problem is that many evaluations observe only a final output. A coding-agent monitor may inspect a single diff while missing suspicious dependencies accumulated across pull requests. A long-context model may receive relevant evidence but fail to use it. An unlearning method may suppress a memorized string at the output while leaving the responsible parameters recoverable. A deployment planner may choose hardware without an explicit model of latency and power. A world model may lose object identity when an entity exits and re-enters view. These are not identical failures, but each involves hidden state whose representation and lifecycle determine what can be checked.

### 1.2 Central research question

The record’s implicit question is: **What is the minimum sufficient state representation that permits reliable control, retrospective audit, and bounded retention without merely accumulating more raw history?**

That question has four parts:

1. What state exists and who or what updates it?
2. Which evidence should be retained, replayed, localized, or discarded?
3. What monitor or validator can test the state transition?
4. What provenance allows a later reviewer to distinguish observed evidence from synthesized interpretation?

### 1.3 Why longer raw history is not the answer

The source DEP-E repeatedly contrasts structured state with undifferentiated accumulation. A larger diff window is not equivalent to a link tracker. A 128K context window is not equivalent to effective evidence use. More output-only tests are not equivalent to parameter-localized evidence. A larger operational log is not automatically a better audit trail. The record’s strongest design claim is therefore not “retain everything,” but “retain enough structure to make consequential transitions inspectable.”

---

## 2. Source integrity and complete inventory

### 2.1 Repository source state

The reviewed source is the tracked directory at commit `e4dbe1a71bdef28ee7c38b7d6e8ecec707890b73`. It contains exactly two files:

1. `README.md` — manifest, classification tags, two-item inventory, item summary, relevance synthesis, and final Attribution Block.
2. `agent_state_review.md` — a schema-complete research artifact with front matter, 13-source metadata table, 11-entry evidence ledger, narrative synthesis, five-claim assessment table, methodology, scope limits, research observations, implementation proposals, exercises, an MVP concept, related reading, source references, and process appendix.

Both files were read from beginning to end. No tracked source file was missing. The README’s inventory matches the actual source directory. The Attribution Block is final and includes the originating Black-Lake-Data manifest and findings artifact, ten arXiv records, two implementation repositories, and one project page.

### 2.2 Integrity of the main artifact

The main artifact identifies its evidence as mixed and assigns confidence levels rather than presenting every citation as equally inspected. It states that the selected DEP manifest and findings artifact were read, that ReContext received the deepest expansion, that persistent-state control and online monitoring received selected HTML inspection, and that other paper claims are primarily abstract-level. This internal labeling is an important positive integrity signal.

There are two qualifications. First, a few statements use broad phrases such as “future agent review will need” where the record is making a reviewer inference rather than reporting a demonstrated necessity. Second, the source access dates freeze a 2026-07-08 view, while at least one canonical record has since advanced from v1 to v2. The source DEP-E remains a valid record of its own state, but downstream readers need the source commit and canonical version distinction preserved.

### 2.3 Directly inspected primary evidence

For this archival intake, canonical arXiv records were checked for all ten named publications. Those records confirm titles, authors, submission state, subject classifications, and abstract-level claims. The ReContext record confirms a training-free evidence-replay method tested on eight 128K-context datasets across three backbones and links public code.[^recontext] The Online Safety Monitoring record confirms a thresholded external-verifier design calibrated by risk control and evaluated on mathematical reasoning and red-team datasets.[^monitor] The LACUNA record confirms a testbed with synthetic PII injected into predefined parameters of 1B and 7B OLMo-based models.[^lacuna]

These checks improve metadata and scope confidence. They do not convert the composite DEP-E into ten complete paper reviews. No publication row is added to the DEP-A publication index for this artifact because no paper in the composite source was fully re-reviewed from its complete primary text during this intake.

---

## 3. Formal and technical reconstruction

### 3.1 A common state model

The ten research threads can be expressed through a shared but deliberately abstract model. Let a system at step (t) have latent or persisted state (S_t), new observation (O_t), update operator (U), decision policy (D), and validator (V):

\[
S_{t+1} = U(S_t, O_t), \qquad A_t = D(S_t, O_t), \qquad q_t = V(S_t, O_t, A_t).
\]

This equation is a reviewer construction, not an equation from the source DEP-E. Its purpose is to expose the recurring questions. What belongs in (S_t)? Can (U) be audited? Does (V) see enough history? Is (q_t) calibrated? What happens when state is compressed, erased, or reconstituted?

### 3.2 Persistent coding-agent control

The source DEP-E reports that iterative coding work creates a sequential control surface because changes can be distributed across pull requests. Its key distinction is between monitors that consume more raw diff history and monitors that construct relationships across changes. The current v2 canonical abstract reports 20 task variations across CLI and Flask families, multiple attack-agent backends, high evasion under tested conditions, and a stateful link tracker that improves detection of gradual buildup. The paper reports that a four-monitor ensemble reduces gradual-attack evasion from 93% under the weakest standard diff monitor to 47%.[^persistent]

Those figures are paper-reported, not independently reproduced here. The generalizable point is narrower: a monitor that represents cross-step dependencies can expose patterns that remain diffuse in a larger but unstructured history. The source DEP-E appropriately keeps attack detail conceptual and defensive.

### 3.3 Evidence replay for long context

ReContext treats the original context as a memory store and the question as a retrieval cue. The source DEP-E describes a pipeline that derives model-internal relevance, selects candidate evidence tokens, materializes copied spans from the original prompt, recursively replays the evidence pool near the question, and generates while retaining the full context. The canonical record describes the method as training-free and explicitly distinguishes evidence organization from answer generation.[^recontext]

The design is significant because it avoids two common collapses: it does not equate context capacity with context use, and it does not replace the original source with a free-form summary. The copied-span constraint gives a reviewer a more concrete provenance surface. The remaining risk is selection error: replay can emphasize the wrong evidence, omit counterevidence, or create position effects that look like improved reasoning.

### 3.4 Online monitor state

Online Safety Monitoring adds calibration state. A verifier produces a scalar or ordered signal, a calibration process chooses a threshold, and the deployed monitor raises an alarm when the score crosses that boundary. The source DEP-E distinguishes false-alarm rate, detection power, and delay, and notes an expectation-versus-high-probability control distinction. This is a strong operational complement to link tracking: the monitor needs both a state representation and a defensible decision rule.

The DEP-E does not establish that one risk-control calibration will remain valid under model, prompt, or deployment drift. Its own deployment recommendations—versioned metadata, explicit targets, reviewer paths, and recalibration—are therefore necessary caveats rather than optional polish.

### 3.5 Parameter, artifact, and infrastructure state

The remaining sources expand the state model:

- LACUNA localizes synthetic memorization to predefined parameter regions, making parameter state testable rather than inferring erasure from outputs alone.[^lacuna]
- Program-as-Weights treats a compiled adapter as a reusable local program, moving repeated execution into a durable learned artifact.[^paw]
- Dual-channel debate records public and off-the-record responses, making audience-conditioned divergence observable rather than latent in a single channel.[^dual]
- WattGPU creates a predictive planning artifact from public model and GPU metadata; its canonical abstract reports leave-one-GPU-out and leave-one-LLM-out evaluation over 42 models and eight GPUs.[^wattgpu]
- WorldDirector uses persistent dynamic object memory to maintain identity across occlusion and viewpoint changes.[^world]
- FlintKV provides durable linearizability, snapshots, iterators, and atomic batches for NVM-backed storage.[^flint]
- RFM-AGOP targets fast extraction of multidimensional refusal subspaces, turning activation structure into an inspectable artifact.[^rfm]

These sources do not jointly prove one unified theory of state. They show that state representations repeatedly become the locus of performance, safety, and auditability.

---

## 4. Architecture and operational pipeline

### 4.1 Reviewer-derived control pipeline

A durable implementation inspired by the DEP-E would use six stages:

1. **Observe:** collect authorized events, evidence spans, verifier scores, and source identifiers.
2. **Materialize state:** convert raw history into typed records such as dependency links, evidence selections, calibration versions, or parameter-localization masks.
3. **Validate transition:** run deterministic checks where possible and calibrated monitors where uncertainty remains.
4. **Act or escalate:** permit, block, request review, or retain full state based on explicit policy.
5. **Persist provenance:** store the source locator, state version, decision rule, and evidence boundary.
6. **Expire or correct:** apply retention limits and correction records without silently rewriting prior provenance.

### 4.2 Guarantee boundary

Nothing in the source DEP-E provides a universal guarantee that structured state will detect covert behavior, recover all relevant evidence, erase memorized information, predict unseen hardware, or expose every refusal feature. Some source threads provide empirical improvements under tested conditions; some provide testbeds; some provide system mechanisms. The reviewer-derived pipeline is therefore a governance proposal, not a proved architecture.

### 4.3 Resource and privacy boundary

State construction can itself be expensive or intrusive. Cross-session links may retain sensitive code context. Evidence replay may preserve personal or confidential spans. Monitor calibration requires representative data. Parameter-localization tests can overfit synthetic insertion mechanisms. A responsible system needs minimum-necessary retention, secret filtering, access controls, deletion/correction semantics, and explicit uncertainty.

---

## 5. Re-conceptualization

### 5.1 State externalization under an evidence contract

The primary re-conceptualization is that these systems **externalize consequential state into a contract that specifies what was observed, how it was transformed, and what decision it supported**. The contract can be a link graph, replay pool, calibration threshold, localization mask, adapter, predictor, object-memory record, storage snapshot, or subspace basis.

The mapping explains why raw scale is insufficient: more tokens, diffs, parameters, or logs do not automatically improve control. Reviewability emerges when state has explicit semantics and provenance.

**Boundary of the analogy:** A link tracker, an adapter, and an NVM snapshot have radically different failure modes and mathematical properties. Calling all of them evidence contracts does not make them interchangeable or equally reliable.

### 5.2 Proposal–validator–ledger

A second interpretation is a three-part architecture:

- a **proposal** selects or updates state;
- a **validator** tests the proposal against rules, evidence, or calibrated risk;
- a **ledger** preserves enough provenance to reconstruct the choice.

ReContext proposes evidence spans; answer generation and citation checks can validate their use; a replay ledger can preserve the spans. A coding agent proposes changes; tests and monitors validate them; a cross-PR ledger preserves dependencies. An unlearning method proposes parameter changes; localization and resurfacing tests validate them; a correction record preserves scope.

**Boundary of the analogy:** Some cited systems do not implement all three parts, and a ledger cannot compensate for a weak validator or biased proposal mechanism.

### 5.3 Transferable design principle

Prefer the smallest typed state that preserves counterevidence, supports independent validation, and can be corrected without erasing history. This principle is a reviewer inference. It should be tested against task performance, audit reconstruction, privacy exposure, and storage cost rather than accepted as a slogan.

---

## 6. Experimental design and evidence reconstructed

### 6.1 Bundle-level design

The DEP-E itself is not an experiment. It is a mixed-evidence synthesis built from two repository artifacts and ten scholarly threads. Its methodology records source access, inclusion, exclusions, confidence, and a reproducibility boundary. The evidence table distinguishes repository package evidence, full/selected HTML inspection, abstracts, repositories, and project pages.

### 6.2 Quantitative evidence audit

The artifact reports a limited set of notable numbers: ReContext’s eight datasets, 128K context, three model backbones, and mean accuracy movement; persistent-state monitor comparisons; LACUNA model scales; and individual systems claims from abstracts. Because denominators, confidence intervals, complete baseline configurations, and table locations are not preserved for every thread, those numbers should be treated as signposts to primary sources rather than a normalized benchmark comparison.

### 6.3 Baseline and metric limits

No common baseline spans all ten papers. “State” is not a shared metric. Detection evasion, QA accuracy, unlearning precision, prediction error, throughput, identity persistence, and ablation performance answer different questions. The DEP-E is strongest when it compares architecture roles, not metric magnitudes.

### 6.4 Runtime and statistical status

The source record did not execute code. It does not report independent training seeds, confidence intervals, hardware-normalized reruns, or significance tests across the combined bundle. Repository availability for ReContext and WattGPU establishes artifact availability and partial inspectability only. It does not establish that their results are reproducible.

---

## 7. Results: what the record supports

### 7.1 Strongly supported at repository-record level

The source DEP-E contains a complete, internally linked argument that state should be made explicit for audit. Every file is inventoried; source depth is disclosed; claims map to evidence identifiers; implementation suggestions are separated from observed results; and limitations are repeated in the scope and weakness sections. That conclusion is strongly supported because it concerns the artifact’s own structure and content.

### 7.2 Supported under source-reported conditions

The more technical propositions—link trackers can help with distributed buildup, evidence replay can improve long-context use, calibrated threshold monitors can be competitive, and localization matters for unlearning—are supported under the conditions reported by their respective sources. They should not be generalized to arbitrary agents, organizations, domains, or safety regimes.

### 7.3 Promising but limited synthesis

The cross-domain claim that one state-ledger architecture could serve coding agents, long-context reasoning, unlearning, and infrastructure is promising but limited. The common control vocabulary is useful, but evidence of transfer is absent. A successful ledger for source spans may fail for parameter state; a storage guarantee may say nothing about semantic correctness.

---

## 8. Ablations and causal evidence

### 8.1 Repository-level ablations

Not materially applicable: the DEP-E is a synthesis and contains no controlled ablation of its own thesis. Its suggested comparison—larger raw history versus compact structured state—comes from source-reported experiments, principally the persistent-state monitor and ReContext threads.

### 8.2 Alternative explanations

Reported gains attributed to state structure may instead arise from extra compute, improved prompting, task-specific inductive bias, model familiarity, or evaluator coupling. For example, replayed evidence changes token position as well as evidence salience. A link tracker adds a representation and potentially a different monitoring budget. Parameter-localization success in a synthetic injection testbed may not transfer to naturally acquired memorization.

### 8.3 Randomness and statistics

The composite record does not supply enough common statistical detail to estimate effect stability across sources. Any future implementation should separate data-generation seeds, model-training seeds, inference seeds, monitor calibration samples, and human-review variance.

---

## 9. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| Persistent state creates a sequential coding-agent control surface. | DEP-E synthesis plus current canonical persistent-state abstract. | Supported under tested conditions. | Twenty reported task variations and named model/monitor configurations do not establish enterprise-wide generality. |
| Larger context alone does not guarantee effective evidence use. | ReContext canonical record and source DEP-E method reconstruction. | Strongly supported as a problem statement; method benefit is supported under tested conditions. | The intake did not rerun the eight-dataset evaluation. |
| Runtime safety alarms should expose risk and false-alarm trade-offs. | Online Safety Monitoring canonical record and DEP-E calibration discussion. | Supported and operationally well motivated. | Calibration may drift; a threshold does not guarantee safe deployment. |
| Output-level unlearning evaluation can miss residual parameter state. | LACUNA canonical abstract and source DEP-E synthesis. | Supported as the testbed’s motivation; broader prevalence remains unresolved. | Synthetic parameter injection is intentionally controlled and may not model natural memorization. |
| State is becoming a first-class review object across AI systems. | Ten-source repository synthesis. | Useful reviewer inference. | Cross-domain recurrence is not a shared causal theory. |
| A signed state ledger is the next practical agent-safety primitive. | Source DEP-E observation and implementation proposals. | Speculative but falsifiable. | No ledger implementation or comparative evaluation exists in the source record. |

---

## 10. External primary-source context

The external checks sharpen three boundaries. First, the persistent-state paper’s canonical record now points to v2, so quantitative citations should not silently retain the source DEP-E’s earlier version framing.[^persistent] Second, ReContext explicitly claims training-free inference without external memory or context pruning, narrowing the mechanism beyond generic retrieval augmentation.[^recontext] Third, the abstract-level records for LACUNA, Program-as-Weights, WattGPU, WorldDirector, FlintKV, and RFM-AGOP support the metadata and high-level mechanisms repeated by the DEP-E, but they do not justify full-method or full-experiment claims in this artifact.

Code status is mixed. The source DEP-E inspected ReContext and WattGPU repositories at README or inventory level, but did not execute them. This intake did not upgrade either to “runnable” or “result reproducible.” For the other source threads, repository availability was not systematically re-audited. External context therefore increases provenance confidence more than reproduction confidence.

---

## 11. Research notes and critical considerations

### 11.1 Internal consistency

The README and main artifact are consistent about file inventory, source collection policy, and the evidence boundary. The main artifact’s source metadata identifies 13 source records because it includes the selected DEP files, papers, repositories, and a project page. Its Evidence Ledger consolidates these into 11 evidence entries. The claims table is traceable to those entries.

The principal temporal inconsistency is external: the persistent-state canonical paper advanced to v2 after the source record’s v1 snapshot. This is a versioning issue, not evidence that the source DEP-E was modified.

### 11.2 Metric and baseline concerns

The artifact’s reported metrics are not harmonized and should not be aggregated. Abstract-level percentages lack the full denominators and uncertainty needed for cross-source comparison. “Better,” “fast,” “durable,” and “persistent” have source-specific definitions.

### 11.3 Unsupported or overbroad claims

The DEP-E occasionally moves from “these sources suggest” to “future systems will need.” The evidence supports a plausible design agenda, not inevitability. It also uses infrastructure examples as thematic support for agent-state governance; that mapping is insightful but inferential.

### 11.4 Failure modes

- Structured state can omit the evidence that would reverse a decision.
- Replay can amplify spurious or adversarially selected spans.
- Cross-session ledgers can become privacy and secret-retention liabilities.
- Calibrated monitors can fail after distribution or model changes.
- Localization can be precise only with respect to a synthetic insertion mechanism.
- Durable artifacts can preserve stale assumptions with high confidence.
- Activation subspaces can be model- and prompt-specific.
- A ledger can create false assurance when validators are weak.

---

## 12. Potential implications

### 12.1 Scientific implications

Evaluation should measure the quality of state representations, not only terminal outputs. Useful dimensions include sufficiency, counterevidence retention, update stability, calibration, reconstructability, and privacy exposure.

### 12.2 System-design implications

Agent platforms should separate raw event capture from typed audit state. A typed record can preserve source identifiers, cross-step dependencies, monitor versions, and validation results while applying stricter retention to raw content. This separation also makes correction possible without rewriting history.

### 12.3 Governance implications

High-impact uses need an explicit acceptance policy: which state is authoritative, which validators are deterministic, which scores are calibrated, when human review is required, and how stale state is invalidated. “More memory” should not be treated as a safety feature without retention and access controls.

---

## 13. New hypotheses

These are reviewer hypotheses, not established findings.

### Hypothesis 1: Typed state beats equivalent raw-history budgets

**Proposition:** At a fixed token and compute budget, a typed dependency/evidence ledger will improve reviewer reconstruction and monitor recall more than an equally sized raw-history window.  
**Motivating evidence:** Link tracking and evidence replay both add structure rather than only more history.  
**Predicted observation:** Reviewers identify cross-step dependencies faster and miss fewer planted relationships.  
**Falsifying observation:** Raw history matches or exceeds typed state after controlling for compute, model, and reviewer time.  
**Minimum test:** Synthetic multi-step coding and long-document tasks with matched storage and inference budgets.

### Hypothesis 2: Counterevidence retention is the key ledger variable

**Proposition:** State summaries that preserve disconfirming evidence will reduce confident audit errors more than summaries optimized only for relevance.  
**Motivating evidence:** Evidence replay and monitor compression can overemphasize selected signals.  
**Predicted observation:** A counterevidence-aware ledger lowers unsupported approvals without a disproportionate rise in false alarms.  
**Falsifying observation:** Counterevidence fields add cost but do not improve calibrated decision quality.  
**Minimum test:** Paired state summaries with and without explicit counterevidence slots on adversarially constructed review tasks.

### Hypothesis 3: Shared provenance improves control-layer composability

**Proposition:** Loop stopping, evidence replay, action gating, and long-term retention will be easier to debug when they emit one common provenance schema.  
**Motivating evidence:** The DEP-E shows similar state questions across otherwise separate systems.  
**Predicted observation:** Failure attribution requires fewer bespoke joins and produces fewer contradictory decisions.  
**Falsifying observation:** A shared schema obscures domain-specific semantics and reduces diagnostic precision.  
**Minimum test:** Implement two controllers with a common ledger and compare replay/debug time against controller-specific logs.

---

## 14. Deployment and governance considerations

### 14.1 Appropriate use

The synthesis is appropriate for designing research prototypes, defensive audit schemas, evidence-replay evaluations, and review checklists. It is not sufficient authority for production safety enforcement or privacy compliance.

### 14.2 Poor fit and failure modes

It is a poor fit when state cannot be collected lawfully, when a task needs exact raw evidence rather than a derived trace, when validators are uncalibrated, or when retention risk exceeds audit benefit.

### 14.3 Required safeguards

1. Preserve public-safe source identifiers and state/version provenance.
2. Redact secrets and minimize retained raw content before persistence.
3. Record validator limitations, calibration data, and fallback behavior.
4. Keep correction records append-only; do not silently overwrite prior decisions.
5. Route uncertain or high-impact cases to independent review.

---

## 15. Replication and falsification agenda

### 15.1 Highest-priority unresolved result

Test whether a structured cross-step ledger improves detection and reconstruction under a matched information budget. Archive the task generator, monitor prompts, state schema, calibration split, complete event history, and reviewer decisions. Success requires improved recall or reconstruction time without unacceptable false alarms or privacy leakage. Failure to beat raw history would falsify the strongest architectural implication.

### 15.2 Reproduce the evidence-replay thread

Retrieve the exact ReContext version and repository commit, verify dependency and dataset instructions, run a small public task, and archive selected spans alongside final answers. Separate artifact availability, inspectability, runnability, and result reproduction.

### 15.3 Normalize evaluation

For each controller, report storage bytes, inference tokens, wall-clock latency, compute hardware, verifier calls, false alarms, missed events, and audit reconstruction success. Avoid comparing percentages whose denominators differ.

### 15.4 Test the proposed mechanism directly

Measure whether gains arise from typed relationships, token repositioning, extra compute, or reviewer attention. Use ablations that preserve one factor at a time.

### 15.5 Test realistic shifts and alternatives

Evaluate changed repositories, model upgrades, prompt changes, longer task horizons, and privacy-constrained retention. Compare typed ledgers with raw windows, retrieval summaries, graph representations, and event-sourced traces.

---

## 16. Durable restatement

> The complete DEP-E record supports a durable but bounded conclusion: consequential AI state becomes governable only when it is represented with enough structure and provenance to be independently checked. The record demonstrates this idea as a synthesis across coding-agent persistence, evidence replay, calibrated monitoring, parameter localization, reusable learned artifacts, deployment prediction, dynamic object memory, durable storage, and activation subspaces. It does not demonstrate one universal state architecture, and it does not reproduce the cited experiments.

What should be remembered is the control question, not a product slogan: for every stateful system, identify what persists, how it changes, what validates the change, what counterevidence is retained, and what later reviewer can reconstruct the decision.

---

## Appendix A. Complete source-record coverage ledger

| Source item | Material accounted for | Evidence depth | Intake disposition |
|---|---|---|---|
| `README.md` | Title, six tags, two-file inventory, item summary, relevance synthesis, final Attribution Block, all listed source locators | Complete file read | Fully covered |
| `agent_state_review.md` front matter | Identity, generated date, source status, confidence, safety scope, distribution notes | Complete file read | Fully covered |
| Source Metadata table | 13 source records and access-depth labels | Complete file read plus canonical-record checks | Fully covered |
| Evidence Ledger | 11 evidence entries, confidence, and limitations | Complete file read | Fully covered |
| Executive and Detailed Summaries | Problem; persistent monitoring; evidence replay; parameter/artifact/infrastructure state; conclusion | Complete file read | Fully covered |
| Key Claims table | Five claims and confidence judgments | Complete file read and recalibrated here | Fully covered |
| Methodology and scope | Discovery, inclusion, exclusions, evidence handling, assumptions, reproducibility and safety boundaries | Complete file read | Fully covered |
| Observations through Weaknesses | State thesis, tensions, strengths, abstract-level evidence limits | Complete file read | Fully covered |
| Improvements and implementations | Five improvements; three implementation concepts | Complete file read | Covered as proposals, not results |
| Exercises and MVP | Exactly three exercises; StateTrace Review concept | Complete file read | Covered as proposals, not deployed artifacts |
| Related Research and Source References | Twelve related items; eighteen source references | Complete file read; canonical records checked | Covered with mixed evidence boundary |
| Appendix | Prior selection counts, eligibility process, and validation checklist | Complete file read | Process history preserved, not treated as current-run counts |

The source DEP-E contains multiple Markdown tables but no embedded figures, numbered equations, algorithms, or code blocks. The equation in this archival review is a reviewer abstraction and is not attributed to the source DEP-E.

---

## Appendix B. Source and evidence notes

### Primary reviewed artifact

Complete tracked repository record `.lake-data/DEP-E/DEP-E-20260708-Agent State Review` at commit `e4dbe1a71bdef28ee7c38b7d6e8ecec707890b73`: two UTF-8 Markdown files, both readable and read in full.

### External primary sources

- https://arxiv.org/abs/2607.02514
- https://arxiv.org/abs/2607.02509
- https://arxiv.org/abs/2607.02510
- https://arxiv.org/abs/2607.02513
- https://arxiv.org/abs/2607.02512
- https://arxiv.org/abs/2607.02507
- https://arxiv.org/abs/2607.02391
- https://arxiv.org/abs/2607.02517
- https://arxiv.org/abs/2607.02401
- https://arxiv.org/abs/2607.02396

### Evidence boundary

The complete repository record was inspected. Canonical arXiv metadata and abstracts were checked for all ten papers. Selected source-record claims about ReContext, persistent-state control, and online monitoring were reconstructed, but the complete primary papers were not all read in this intake. Repositories were not cloned or executed. Experiments, datasets, notebooks, and code were not rerun. Source documents were not uploaded. Paper-level claims are labeled as canonical-abstract-confirmed, source-DEP-reported, reviewer inference, or hypothesis.

### One-way provenance

This is newly generated derived data. The source DEP-E was reviewed in place. Direction is `DEP-E -> DEP-A`. Source action was review-only. Source DEP modified: no. Files moved: no. Existing files copied into DEP-A: no. This artifact does not reclassify, supersede, transfer, or mutate the source record.

---

## Footnotes

[^persistent]: Josh Hills, Ida Caspary, and Asa Cooper Stickland, “Distributed Attacks in Persistent-State AI Control,” current canonical arXiv record, version 2: https://arxiv.org/abs/2607.02514

[^recontext]: Yanjun Zhao et al., “ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning,” arXiv:2607.02509v1: https://arxiv.org/abs/2607.02509

[^monitor]: Mona Schirmer et al., “Online Safety Monitoring for LLMs,” arXiv:2607.02510v1: https://arxiv.org/abs/2607.02510

[^lacuna]: Matteo Boglioni et al., “LACUNA: A Testbed for Evaluating Localization Precision for LLM Unlearning,” arXiv:2607.02513v1: https://arxiv.org/abs/2607.02513

[^paw]: Wentao Zhang et al., “Program-as-Weights: A Programming Paradigm for Fuzzy Functions,” arXiv:2607.02512v1: https://arxiv.org/abs/2607.02512

[^dual]: Arman Ghaffarizadeh et al., “What LLM Agents Say When No One Is Watching,” arXiv:2607.02507v1: https://arxiv.org/abs/2607.02507

[^wattgpu]: Mauricio Fadel Argerich, Jonathan Fürst, and Marta Patiño-Martínez, “WattGPU,” arXiv:2607.02391v1: https://arxiv.org/abs/2607.02391

[^world]: Hanlin Wang et al., “WorldDirector,” arXiv:2607.02517v1: https://arxiv.org/abs/2607.02517

[^flint]: Sergey Egorov et al., “FlintKV,” arXiv:2607.02401v1: https://arxiv.org/abs/2607.02401

[^rfm]: Thomas Winninger, “Fast Multi-dimensional Refusal Subspaces via RFM-AGOP,” arXiv:2607.02396v1: https://arxiv.org/abs/2607.02396
