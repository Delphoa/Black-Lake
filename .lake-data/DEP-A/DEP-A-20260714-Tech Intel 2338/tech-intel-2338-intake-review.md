# Operational AI Evidence Across Evaluation, State, and Governance

## A whitepaper-grade archival intake review of the Tech Intel 2338 composite DEP-E

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260709-Tech Intel 2338`[^dep]
**Source commit:** `a1ffd4737ce95c14f3a15251ee4fbba4403108a5`
**Paired task indicator:** `BL-DEPPAIR-20260714-6DCB29E5`
**Direction:** `DEP-E -> DEP-A`
**Artifact prepared:** 2026-07-14
**Review scope:** complete two-file composite DEP-E review plus canonical public-record checks
**Reproduction boundary:** no external complete paper set was reviewed, no code was executed, and no reported result was independently reproduced
**One-way provenance:** review-only; source DEP modified: no; files moved: no; files copied: no; new derived DEP-A data generated: yes

---

## Executive assessment

Tech Intel 2338 is a ten-source technology-intelligence bundle whose most durable theme is operational AI. Its subjects range from deployment simulation and artifact-heavy science benchmarks through clinical agents, structured tool state, human code-review behavior, embodied security, low-precision training, quantum optimization, and quantum chemistry. They are not one scientific program, but they converge on a useful proposition: model capability becomes consequential only when it is embedded in workflows, state, tools, people, hardware, and domain governance.

The complete repository record is strong as a research map. It preserves source identity, access boundaries, confidence notes, evidence categories, and public links. It is not a substitute for ten complete-paper reviews. This intake therefore reconstructs the bundle itself and labels numerical statements as DEP-reported or abstract/page-reported claims. It makes no claim that the studies were independently reproduced or directly comparable.

The archival judgment is positive with a medium evidence grade. The bundle should be retained because it exposes dependencies that narrow benchmarks omit. The most valuable next steps are not broader summarization but targeted full-source reviews of Deployment Simulation, LedgerAgent, MIRA, the review-habituation study, and the robotics security systematization.

## 1. Problem framing and research question

The bundle raises one cross-cutting question: what evidence is required before an AI system can be trusted inside a real workflow? Static benchmark accuracy is insufficient when the system maintains state, calls tools, changes files or records, interacts with reviewers, operates under hardware constraints, or influences clinical and physical decisions.

This review asks three bounded questions. First, does the complete DEP-E consistently identify its source set and access level? Second, which cross-source patterns are supported without pretending the underlying protocols are comparable? Third, what falsifiable evaluation program can connect deployment realism, structured state, human review, physical-domain risk, and systems constraints?

The primary reviewed object is the two-file repository record. Public posts, article pages, and arXiv records were used as canonical evidence for identity and headline scope. Complete source documents were not uniformly inspected, so no publication is added to the DEP-A publications index for this composite intake.

## 2. Complete inventory and source integrity

The record contains `README.md` and `tech-intel-2338-research.md`. The README declares the DEP class, source context, two-item inventory, summary, relevance, and final attribution block. The manuscript supplies metadata, fourteen source records, an eight-row evidence ledger, executive and detailed synthesis, claims, methodology, constraints, observations, implementations, exactly three exercises, an MVP, reading, references, and run notes.

Both files were read from beginning to end. Every named external source is represented in the manuscript inventory and README attribution. The access boundary is repeatedly stated: repository files and public pages were inspected, but external PDFs, datasets, code repositories, supplements, and experiments were not collected or reproduced.

Source integrity is therefore high for package identity and medium for technical synthesis. The DEP manuscript is generated evidence about what an earlier review concluded. It does not become independent authority by being detailed. This new DEP-A uses original language, preserves uncertainty, and does not copy any source Markdown.

## 3. Technical reconstruction of the bundle

The ten findings can be organized into six operational planes.

### 3.1 Deployment-realism plane

Deployment Simulation and LifeSciBench move evaluation from isolated prompts toward trajectories, tools, artifacts, and expert rubrics. The general mechanism is environmental reconstruction: preserve enough of the workflow that failures appearing only under context, tool use, or artifact production become observable before release.

This plane asks whether an evaluation approximates the deployment distribution without exposing private data or causing real effects. It also asks which parts are simulated, which are replayed, and which are inaccessible to external reviewers.

### 3.2 Structured-state plane

LedgerAgent represents task state separately from language context and checks policy before environment-changing tool calls. UltraQuant addresses long-context serving through low-bit KV-cache representation. These are different technical layers, yet both make state explicit: one for governance and one for memory/throughput.

The cross-source insight is not that ledger state and KV cache are interchangeable. It is that long-running agents require state models at several layers, each with different integrity, privacy, and failure properties.

### 3.3 Human-governance plane

The code-review habituation study reports longitudinal changes in approval and comment behavior around agent-authored pull requests. Its importance is sociotechnical. A technically capable review workflow can weaken if repeated exposure changes scrutiny, workload, or reviewer expectations.

A durable governance system should measure reviewer behavior, not merely require that a human click approve. It should preserve escalation triggers, sampled deep review, and independent validation for high-risk changes.

### 3.4 High-stakes domain plane

MIRA and the robotics security/privacy systematization extend agent action into clinical records and embodied systems. Here, errors can affect health, privacy, or physical behavior. Source identity and abstract-level claims are useful for prioritization; deployment recommendations require complete methods, prospective validation, threat modeling, regulatory context, and domain review.

### 3.5 Numeric and hardware plane

UltraQuant and UFP4 make representation precision an operational variable. Cache format, quantization grid, kernel support, and hardware can alter latency, memory, stability, or bias. Model behavior cannot be separated from its numeric substrate when compression becomes aggressive.

### 3.6 Scientific-computing plane

The quantum-optimization and quantum-chemistry entries preserve adjacent evidence about algorithms, hardware, and scientific workloads. They belong in the same daily bundle historically, but their empirical claims should not be used to validate agent workflows. Their relevance is methodological: complex systems claims require exact problem definitions, hardware records, baselines, and reproducible artifacts.

## 4. Evaluation design and evidence reconstructed

A unified evaluation program should not collapse the six planes into one score. It should define a matrix whose rows are workflows and whose columns are capability, state integrity, tool correctness, human oversight, resource use, privacy, and recovery. Each cell should name its source and validation level.

The Deployment Simulation entry reportedly uses privacy-processed production conversation prefixes and discusses agentic tool simulation. LifeSciBench is described as artifact-heavy and expert-reviewed. MIRA is presented as a sandboxed EHR agent. LedgerAgent introduces a task-state ledger and policy gates. The review-habituation paper reports a longitudinal sample of repeat reviewers. These details suggest concrete evaluation dimensions, but their metrics remain source-reported in this intake.[^claims]

Information budgets must be matched. A system with private production prefixes, a proprietary tool simulator, or expert artifacts has access to evidence that an external reproduction may not. Unavailable materials should be recorded as dependencies rather than replaced with invented proxies.

## 5. Results and quantitative audit

The source DEP reports approximate scale figures for several findings: roughly 1.3 million de-identified conversations in Deployment Simulation context; 400 repeat reviewers and 11,429 reviews in the habituation study; and technical counts for cache, numeric, quantum, and chemistry work. These numbers were preserved as discovery evidence, not pooled or independently verified.

The authors report results within distinct protocols. A shift in pull-request approval cannot be compared numerically with a cache-memory ratio, clinical-agent outcome, or quantum active-space size. The defensible result is structural: operational AI evaluation increasingly depends on trajectories, artifacts, explicit state, human behavior, hardware, and domain-specific governance.

The bundle supports prioritization, not universal ranking. It provides no common dataset, baseline, metric, or uncertainty model across the ten sources. A downstream dashboard should resist displaying them as one leaderboard.

## 6. Ablations and quantitative/experimental audit

A unified ablation is not materially applicable because the DEP is composite. However, the bundle motivates targeted ablations:

- Deployment evaluation with live, replayed, and simulated tools under the same trajectory set.
- Agent execution with free-form context state versus a structured ledger and policy gate.
- Code review with repeated reviewers, rotating deep reviewers, and randomized independent checks.
- Cache and numeric compression at fixed model, workload, hardware, and quality threshold.
- Clinical and embodied workflows with and without constrained action, sandboxing, and escalation.

Every ablation should report both task success and failure containment. Improving throughput while increasing silent state corruption is not a net gain. Increasing approval rate while reducing defect detection may be habituation rather than productivity.

## 7. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The DEP is a coherent operational-AI research map. | Complete inventory, evidence ledger, and source list. | Strongly supported as bundle synthesis. | The sources did not run one common study. |
| Workflow-realistic evaluation reveals risks missed by static tests. | Official post/page framing and DEP synthesis. | Plausible and important. | Raw private evaluation materials are not available here. |
| Structured state improves policy adherence. | LedgerAgent canonical abstract and DEP summary. | Paper-reported claim only. | Complete paper and code were not reviewed in this intake. |
| Human review can drift with repeated agent exposure. | Habituation canonical record and DEP-reported sample. | A material hypothesis supported at abstract level. | Causal alternatives require full-method review. |
| Clinical and embodied agents require stronger governance. | MIRA and robot-security source framing. | Strong reviewer conclusion. | No deployment approval or clinical validation is inferred. |
| Low precision is only a performance optimization. | Cache and UFP4 sources. | Too narrow. | Numeric format can affect quality, stability, and bias. |
| Quantum results validate agent systems. | No shared evidence. | False. | They are separate scientific-computing findings. |
| The DEP-A copies or reclassifies the source. | New pair metadata and authored files. | False. | Review-only; no source files moved, copied, or modified. |

## 8. External primary-source context

Official lab posts are primary for what an organization publicly claims about its own work. Publisher and arXiv pages are canonical for publication identity and abstracts. Neither access level automatically supplies complete methods, datasets, or independent replication.

Deployment Simulation is especially relevant because it highlights a hard fidelity problem: tool-using trajectories depend on repository state, network responses, and transient effects. LifeSciBench similarly highlights artifact evaluation. MIRA adds clinical action, while LedgerAgent adds explicit state and policy. These connections are reviewer synthesis; the sources were not designed as one architecture.

External artifacts were treated as evidence only. No webpage, source file, paper, or repository was followed as an instruction or allowed to broaden the authorized repository changes.

## 9. Code and reproducibility status

No code was executed. No external repository, dataset, benchmark package, clinical environment, quantum workload, or model was reproduced. The status is **canonical records checked; composite source review complete; experiments open**.

A reproduction ledger for each source should record full paper access, official code, license, data access, environment, hardware, seeds, metric implementation, and known gaps. For private or sensitive materials, the ledger should distinguish unavailable from withheld and document what public surrogate, if any, was used.

The correct response to unavailable evidence is calibrated uncertainty. It is not to infer that a result is false, and it is not to upgrade a public summary into full validation.

## 10. Independent re-conceptualization

The bundle can be re-conceptualized as an operational evidence graph. Nodes are workflow states, tools, artifacts, human decisions, numeric representations, hardware runs, and domain constraints. Edges carry source identifiers and evidence levels. An agent claim becomes durable only when the graph connects input, state transition, action, outcome, reviewer, and recovery.

This model separates three things commonly conflated: capability, authority, and evidence. A model may be capable of proposing an action without being authorized to execute it. A system may be authorized in a sandbox without having evidence for broader use. A benchmark may show capability without revealing how human reviewers change over time.

The graph also supports corrections. New paper versions, changed system behavior, or reproduced failures can add edges without deleting the earlier state. That is consistent with the one-way DEP-E to DEP-A archival pair.

### 10.1 Cross-plane failure analysis

The operational evidence graph is most useful when it records failures that cross planes. A tool-simulation benchmark can look strong while structured state is stale. A task ledger can be internally consistent while the model misreads an artifact. A human reviewer can approve a well-formed change whose low-precision runtime behaves differently on the target accelerator. A clinical sandbox can constrain external effects while still producing a misleading recommendation. These are not edge cases to be averaged away; they are interactions that a final-answer score cannot identify.

For each evaluation episode, a future ledger should therefore preserve an input manifest, model and runtime identity, state snapshot, tool transcript, generated artifacts, policy decisions, human interventions, resource measurements, and outcome adjudication. Fields should be typed so a missing value is distinguishable from an intentionally withheld value. The record should also retain whether an assertion came from direct observation, a source report, an evaluator, or an automated judge.

### 10.2 Counterfactual evaluation

The bundle motivates counterfactual tests at three levels. At the workflow level, replay the same authorized task with a simulated tool failure, stale repository state, or incomplete artifact. At the governance level, vary whether a state-changing action requires policy approval and whether a second reviewer sees the original agent rationale. At the systems level, vary cache or numeric format while holding model, prompt, seed, hardware, and metric implementation fixed.

Counterfactuals help distinguish capability from robustness. If a result survives only under one clean environment, it is a demonstration rather than operational evidence. If a structured ledger improves outcomes only because it supplies more information, the comparison should match information budgets. If a reviewer approves more changes after repeated exposure, randomized deep review can test whether the trend reflects growing expertise, reduced scrutiny, or easier tasks.

### 10.3 Sensitive-domain acceptance boundary

MIRA and the embodied-security source make the consequence boundary explicit.[^deployment][^ledger] A system that reads or proposes actions in a sensitive domain needs a layered acceptance case: authorized data use, validated sandbox semantics, constrained actions, expert review, uncertainty handling, incident escalation, and prospective evaluation. A research benchmark can support one layer without satisfying the others.

The same discipline applies outside medicine. Agent-authored code can change production behavior; a robotics system can affect physical space; a quantum or scientific-computing claim can influence expensive experiments. The archive should never translate a source's existence into authorization. Its role is to make the remaining evidence requirements visible and to preserve which requirements were actually checked.

### 10.4 Minimum viable evidence packet

A practical follow-on can start with a small packet rather than a comprehensive platform. The packet should contain a task contract, source/version inventory, one normal fixture, one adversarial or failure fixture, exact execution configuration, result and artifact hashes, reviewer rubric, and a recovery note. Passing the normal fixture shows feasibility. Passing the failure fixture with an intelligible trace begins to show robustness. Neither alone establishes broad deployment readiness.

This packet also improves comparability across the ten sources. It does not force unlike metrics into one number; it requires each source thread to answer the same provenance questions. Over time, those packets can form the evidence graph proposed above and support corrections without erasing earlier findings.

## 11. Research notes and caveats

### 11.1 Evaluation realism can create privacy tension

More realistic prefixes, artifacts, and trajectories improve fidelity but can contain sensitive context. Privacy processing, access controls, retention, and auditability are part of the evaluation method, not post-processing details.

### 11.2 Structured state can centralize risk

A task ledger improves inspectability, yet becomes a high-value integrity target. It needs schema validation, provenance, append-only history where appropriate, and explicit conflict handling.

### 11.3 Human presence is not sufficient oversight

Approval statistics can improve while scrutiny declines. Oversight quality needs outcome measures such as defect escape, sampled reconstruction, and reviewer disagreement.

### 11.4 High-stakes domains need prospective evidence

Sandbox results in clinical or embodied settings cannot establish real-world safety. Domain experts, prospective protocols, incident response, and conservative action boundaries are required.

### 11.5 Numeric formats are behavioral dependencies

Cache and FP4 choices may change more than cost. Quality, rare-event behavior, calibration, and error propagation should be audited at the target workload.

### 11.6 Composite breadth limits depth

Ten sources create a valuable map but prevent complete methodological validation in one artifact. This review explicitly keeps that boundary.

## 12. Implications

1. **Agent evaluations should retain trajectories and artifacts.** Final-answer scoring cannot explain tool or state failures.
2. **State changes should pass explicit policy checks.** Context alone is a poor authority boundary.
3. **Review systems need anti-habituation controls.** Rotation, random deep checks, and independent tests can preserve scrutiny.
4. **Clinical and embodied claims require domain gates.** Sandbox and simulation results are preparation, not deployment proof.
5. **Systems configuration belongs in provenance.** Precision, cache, kernel, hardware, and driver can change behavior.
6. **Daily intelligence bundles should seed narrower reviews.** The bundle's value increases when its highest-risk nodes receive complete-source follow-up.

## 13. Falsifiable hypotheses

### Hypothesis 1

**Proposition:** trajectory-and-artifact evaluation will predict post-release agent failures better than final-answer benchmarks.
**Prediction:** failure categories observed in realistic simulations will correlate more strongly with authorized deployment incidents.
**Falsifier:** static benchmark scores predict the same incidents after controlling for model and task.
**Minimum test:** matched models and tasks, preregistered failure taxonomy, privacy-reviewed traces.

### Hypothesis 2

**Proposition:** a structured state ledger plus pre-action policy gate will reduce unauthorized or inconsistent tool effects.
**Prediction:** adversarial and conflicting-state fixtures produce fewer unsafe transitions.
**Falsifier:** outcomes are unchanged or failures migrate into the ledger parser.
**Minimum test:** authorized toy environment with complete transition logs.

### Hypothesis 3

**Proposition:** sampled independent review will counter reviewer habituation more effectively than mandatory approval alone.
**Prediction:** defect escape falls without unacceptable review delay.
**Falsifier:** sampled checks add cost but do not improve detection.
**Minimum test:** randomized review policy on synthetic or low-risk changes.

### Hypothesis 4

**Proposition:** low-precision and cache optimizations will alter rare-event task quality before average scores reveal degradation.
**Prediction:** tail-risk fixtures degrade at compression settings that preserve the mean.
**Falsifier:** tail and average behavior remain stable across formats and seeds.
**Minimum test:** fixed workload, hardware, versions, and error taxonomy.

## 14. Replication and falsification agenda

1. Deep-review Deployment Simulation's complete public paper, mapping each claimed deployment proxy to accessible evidence and fidelity limits.
2. Reconstruct LedgerAgent's state schema and policy boundary in an authorized toy tool environment.
3. Inspect the review-habituation study's full methods, causal controls, definitions, and effect uncertainty.
4. Build a MIRA evidence checklist covering data source, action sandbox, prospective validation, safety, and governance.
5. Reproduce one UltraQuant or UFP4 quality/resource curve with exact hardware and format definitions.
6. Keep quantum findings in a separate replication track with problem, circuit/hardware, baseline, and sampling provenance.
7. Publish failures, inaccessible materials, and non-comparable metrics rather than forcing one score.

The agenda prioritizes discriminating evidence over breadth. A completed item should update this graph through a new archival pair if the source state or conclusion materially changes.

## 15. Durable restatement

> Tech Intel 2338 is a provenance-preserving map of operational AI evidence. It shows why realistic trajectories, explicit state, human review, hardware representation, and domain governance must be evaluated together, while its individual performance claims remain at the access level of their underlying sources.

### Review decision rule

The durable claim excludes any statement that requires ten complete papers to have been reviewed. Numerical details remain source-reported unless a later artifact inspects the full source and recomputes or independently validates them.[^claims] The pair indicator binds this review to one immutable source state and does not supersede the DEP-E.[^pair]

## Appendix A. Coverage ledger

| Source element | Coverage | Evidence boundary |
|---|---|---|
| README | Context, inventory, summary, insights, and all attribution entries checked. | Direct repository evidence. |
| Manuscript metadata and evidence ledger | All fourteen sources and eight evidence groups accounted for. | Generated source report. |
| Executive and detailed summary | Reconstructed by six operational planes. | No source prose copied. |
| Key claims | Conservatively re-vetted. | Abstract/page-level unless stated otherwise. |
| Methodology and constraints | Integrated into evidence boundary. | Process provenance, not empirical proof. |
| Observations and considerations | Reframed as reviewer notes. | Reviewer inference labeled. |
| Implementations, exercises, and MVP | Converted to falsifiable hypotheses and agenda. | Proposals only. |
| Related reading and source references | Canonical identity and scope checked. | Complete source set not reviewed. |
| Appendix run notes | Accounted for as repository history. | Not technical validation. |
| Figures/equations | Not materially applicable to the composite DEP object. | None invented. |

## Appendix B. Source and evidence notes

| Source | Public locator |
|---|---|
| Source DEP-E | https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-Tech%20Intel%202338 |
| Deployment Simulation | https://openai.com/index/deployment-simulation/ |
| LifeSciBench | https://openai.com/index/introducing-life-sci-bench/ |
| MIRA article | https://www.nature.com/articles/s41586-026-10675-5 |
| LedgerAgent | https://arxiv.org/abs/2606.20529 |
| Robot security SoK | https://arxiv.org/abs/2606.16788 |
| UFP4 | https://arxiv.org/abs/2606.20381 |

### Evidence boundary

The complete selected DEP-E record is the primary reviewed object. Direct evidence includes its complete text and checked canonical public records. DEP-reported, page-reported, and paper-reported claims are identified. Reviewer inference is confined to synthesis, cautions, implications, hypotheses, and replication design. No result was independently reproduced.[^boundary]

### Provenance facts

- Source action: review-only.
- Source DEP modified: no.
- Files moved: no.
- Existing files copied into DEP-A: no.
- New derived data generated: yes.
- Intake and deposition become complete only with validation and repository submission.

## Footnotes

[^dep]: Immutable source record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-Tech%20Intel%202338
[^claims]: The authors report results under separate protocols; this composite intake did not recompute them.
[^boundary]: Reproduction boundary: no code, dataset, benchmark, external full-paper set, or experiment was independently reproduced.
[^pair]: Paired task indicator `BL-DEPPAIR-20260714-6DCB29E5` records the one-way relationship.
[^deployment]: Official Deployment Simulation post: https://openai.com/index/deployment-simulation/
[^ledger]: LedgerAgent canonical record: https://arxiv.org/abs/2606.20529
