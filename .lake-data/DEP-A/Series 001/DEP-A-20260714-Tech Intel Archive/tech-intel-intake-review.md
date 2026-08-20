# Control Surfaces for Persistent Agent Systems

## A whitepaper-grade archival intake review of the Tech Intel Agent Systems Review bundle

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260708-Tech Intel Review`
**Source commit:** `a1ffd4737ce95c14f3a15251ee4fbba4403108a5`
**Paired task indicator:** `BL-DEPPAIR-20260714-8BCA1848`
**Direction:** `DEP-E -> DEP-A`
**Artifact prepared:** 2026-07-14
**Review scope:** complete repository-record review of two tracked Markdown files; canonical-record checks for the ten central publications; independent re-conceptualization and replication planning
**Reproduction boundary:** no paper experiment was rerun, no code was executed, and no result was independently reproduced
**One-way provenance:** source action was review-only; the DEP-E was not modified; no files were moved or copied; this DEP-A contains newly generated derived data

---

## Executive assessment

### The record in one sentence

The selected DEP-E is a broad technical-intelligence bundle that uses ten recent research reports to map reliability problems in persistent, tool-using, multi-model, and domain-embedded AI systems.

### The deeper idea

The durable contribution is not a leaderboard of ten papers. It is an implicit control architecture. Memory consolidation controls what persists after context disappears; semantic stopping controls whether an iterative process should continue; tool-description security controls what instructions enter through interfaces; co-failure analysis controls whether diversity claims survive correlated errors; causal process supervision controls whether a correct answer arose from a defensible route; and grounding controls whether high-stakes outputs remain attached to evidence. Read together, these are interfaces at which an agent system can accept, reject, retain, forget, or escalate information.

### Bottom-line judgment

The complete repository record is a useful orientation artifact with strong provenance and unusually explicit access limits. It is not a substitute for ten paper reviews. Its quantitative statements were inherited from an earlier generated findings artifact and were not table-checked in the DEP-E; the source manuscript says so repeatedly. This archival intake therefore preserves the bundle's strongest value—its cross-paper systems map—while lowering confidence on paper-level metrics, novelty, and reproduction. The record is whitepaper-worthy as a review of a scholarly source bundle because its inventory, evidence boundary, and downstream research questions can be reconstructed completely.

### Principal strengths

- The README and manuscript agree on source identity, scope, and non-redistribution.
- Ten findings are organized around a coherent reliability problem rather than an arbitrary topic list.
- The source distinguishes repository synthesis, arXiv metadata, and unperformed full-paper validation.
- The bundle generates practical review questions without requiring operationalization of security-sensitive work.

### Principal qualifications

1. The source record inspected metadata and abstracts rather than complete papers, appendices, code, and datasets.
2. Reported numbers are DEP-E-reported claims; this review does not upgrade them into independently verified results.
3. Breadth creates useful links but weakens mechanism-level comparison because tasks, metrics, and evidence standards differ.

## 1. Source identity, integrity, and complete inventory

The repository object contains exactly two tracked files. `README.md` supplies the class, date, subject, two-item inventory, public context, explanation of relevance, and final attribution block. `tech-intel-agent-systems-review.md` supplies YAML metadata followed by source and evidence ledgers, an executive and detailed synthesis, claim table, methodology, scope, observations, strengths and weaknesses, proposed improvements, three exercises, an MVP concept, related reading, source references, selection record, and validation notes.

Both files were readable from beginning to end. Their internal relationship is consistent: the README describes the manuscript as a first-pass research artifact for a former Black-Lake-Data daily findings DEP, and the manuscript identifies that same upstream record. The cited core identifiers are ten arXiv records: 2606.26806, 2606.27027, 2606.26933, 2606.27288, 2606.26071, 2606.27154, 2606.27009, 2606.26874, 2606.26758, and 2606.25889.[^bundle] An eleventh record, 2606.25870, is explicitly labeled a related seed rather than one of the ten ranked findings.

The source-integrity strength is candor. The manuscript labels its status “mixed,” assigns medium confidence, and states that full PDFs and repositories were not downloaded during its run. It calls arXiv pages “metadata/abstract” evidence and refuses to present its own metric list as reproduction. That access statement is crucial: the primary object reviewed here is the complete DEP-E bundle, while directly inspected external evidence in this intake is limited to canonical public records and, where available, their exposed metadata. No claim in this document should be read as an independent complete-paper judgment about all ten works.

The source record ends cleanly, includes all references it invokes, and has no unaccounted tracked attachment. It contains no equation, numbered source-paper table, or source-paper figure. Its own tables are organizational ledgers: source metadata, evidence, claims, potential improvements, related reading, and references. Consequently, the coverage obligation is to account for those bundle tables and every topical section, not to invent figure-by-figure coverage for papers that were not included.

## 2. The problem and research question

The bundle asks a practical question: once AI systems keep state, call tools, loop over partial results, combine multiple models, and enter consequential domains, what evidence is needed to decide that their behavior is reliable? Classic model evaluation often treats one prompt and one answer as the unit. The selected findings instead foreground persistence and composition. Errors can enter through a memory write, a tool description, an ensemble's shared blind spot, an unsupported diagnostic step, or a generated medical statement. A final accuracy score can conceal each route.

The manuscript's own taxonomy has four clusters. First, EVAF and semantic early stopping concern persistence and iteration. Second, ShareLock, Chai, and model forensics concern hostile or concerning behavior. Third, co-failure ceilings and OpenRCA concern evaluation structure. Fourth, TAVR-VLM, EGG, and the quantum-annealing report extend the frame into clinical grounding, systems optimization, and scientific computation. That grouping is supported by the source files; the stronger claim that all ten instantiate one control theory is reviewer inference.

## 3. Technical and evidentiary reconstruction

### 3.1 Evidence layers

The DEP-E itself uses three practically distinct evidence layers. Its local README and generated manuscript establish provenance and what the upstream synthesis said. Canonical arXiv pages establish that named research records exist and expose titles, authors, versions, and abstracts. Reviewer synthesis connects the records into a systems map. These layers must not collapse.

For memory, the source reports an EVAF-like selective parametric consolidation proposal and interprets “memory depth” as recall after ordinary context is unloaded. That distinction matters because retrieval access and parametric retention are different mechanisms. The DEP-E does not contain a full experimental specification, so any numerical advantage remains a report about what the upstream artifact said.

For tool security, ShareLock is represented as a threshold poisoning threat in which fragments distributed across descriptions become harmful only when composed. Chai is represented as agentic discovery of cryptographic misuse across formats and dependencies. The reliable inference is that interface metadata and dependency graphs are review surfaces. The record does not provide exploit procedures, and this archival intake does not derive any.

For multi-model evaluation, the co-failure work is represented as placing a ceiling on routing, voting, or mixture gains when all candidate models fail together. This yields a simple systems lesson: mean diversity is less informative than the probability mass in the shared failure tail. The exact experimental population of 67 frontier models is a source-reported scope, not an independently audited sample here.[^cofailure]

For process evidence, OpenRCA is represented as moving from outcome labels to causal process supervision. Model forensics similarly distinguishes observed concerning behavior from the stronger diagnosis of misalignment. Both support a common audit rule: conclusions and causes require separate evidence fields. A correct root-cause label does not prove a sound diagnostic trajectory, just as a suspicious output does not prove one latent objective.

For stopping, the semantic early-stopping record frames iterative RAG or agent loops as controlled processes rather than fixed-depth chains. A controller should measure marginal semantic or quality change and terminate when another iteration is unlikely to improve the accepted result. Without a full paper audit, the threshold, evaluator, and dataset remain unverified, but the control pattern is coherent.

For high-stakes grounding, TAVR-VLM is reported as risk-conditioned causal grounding for medical report generation. The source appropriately warns that any hallucination reduction or clinical metric requires full-paper and dataset scrutiny. The defensible bundle-level implication is narrower: a medical generator needs evidence-linked statements, calibrated uncertainty, and rejection paths.

EGG is presented as expert-guided, stage-aware GPU-kernel generation. Its inclusion demonstrates that an agent can be part of a measurable optimization loop, but no speedup is accepted here without hardware, workload, baseline, and validation context. The quantum-annealing report is similarly preserved as a scientific-computation frontier example. Its hardware scale is not evidence that its physical interpretation or general advantage has been reproduced by this review.[^quantum]

### 3.2 Information flow

The reconstructed bundle pipeline is: daily discovery selects recent records; an upstream findings artifact summarizes claims and relevance; the DEP-E manuscript checks repository provenance and canonical identifiers; it groups the findings; and it proposes deeper review queues. The pipeline's output is therefore a map and backlog. It does not transform abstracts into full experimental audits.

This distinction resolves an apparent tension. The manuscript is detailed, yet its primary evidence depth is limited. Detail can improve traceability without increasing source authority. The correct archival action is to preserve both: the rich conceptual graph and the explicit ceiling on confidence.

## 4. Experimental design and quantitative audit

No unified experiment exists across the bundle. Each paper has a different task, dataset, denominator, and unit of analysis. The DEP-E mentions attack success, token reduction, AUROC, speedup, co-failure, hallucination, and qubit count, but does not reproduce the tables that define those quantities. Cross-paper averaging would be meaningless.

The audit result is therefore procedural. A future deep review must record, for each quantitative claim: the exact paper version; table, figure, or appendix location; dataset and split; baseline provenance; model and training budget; aggregation unit; confidence interval or seed count; and whether the metric is conditioned on success. Security metrics need an explicit threat model and authorization boundary. Medical metrics need cohort construction, label source, clinical relevance, and subgroup behavior. Systems speedups need workload, hardware, batch size, compilation and warm-up semantics. Quantum results need hardware topology, calibration, embedding overhead, comparator, and physical interpretation.

Because none of those audits were performed by the DEP-E, the bundle's numbers are “promising but limited” evidence at best. This is not a defect hidden by the source; it is one of the source's stated next actions.

## 5. Results: what the complete record establishes

The record establishes five durable facts. First, its ten core source identifiers and one related seed are traceable. Second, the repository provenance and selection context are explicit. Third, the topics form a plausible reliability map spanning memory, interfaces, correlated failure, process traces, grounding, optimization, and scientific verification. Fourth, the original review did not perform full-paper or reproduction work. Fifth, the bundle contains a concrete backlog for doing so.

Where this artifact says that a paper reports a result, the wording identifies a DEP-E-reported source claim rather than an independently confirmed experiment.

The record does not establish the comparative superiority, generality, or deployment readiness of any named method. It also does not show that the ten mechanisms compose safely in one system. Those stronger statements would require task-specific evidence and integration testing.

## 6. Ablations and causal evidence

There are no bundle-level ablations. The DEP-E reports that individual papers contain evaluations, but it does not preserve enough primary detail to decide whether one component caused a gain. This absence suggests a cross-cutting replication design.

For memory, ablate retrieval availability and parametric consolidation separately, then test after context unloading. For loop control, compare fixed iteration counts, semantic-delta stopping, and an oracle stopping rule under a common token budget. For tool security, compare isolated descriptions, threshold combinations, and a sanitized registry in a benign authorized harness. For ensembles, condition gains on the all-model failure subset rather than only total accuracy. For process supervision, score final outcomes and causal trace correctness independently. For grounded generation, remove or corrupt evidence links and measure whether the system abstains. These are reviewer-proposed tests, not experiments reported as completed.

## 7. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| The DEP-E is a ten-finding agent-systems research bundle. | Both tracked files and their inventory. | Strongly supported. | Describes the repository object, not all upstream source material. |
| Persistent-agent reliability spans memory, loops, tools, ensembles, and grounding. | Topic distribution and source synthesis. | Supported as a useful taxonomy. | Reviewer grouping; not a formal completeness claim. |
| The cited works report quantitative improvements or risks. | DEP-E manuscript summaries and canonical records. | Promising but limited. | Numbers were not table-checked or reproduced in the source bundle. |
| Tool metadata is a meaningful security surface. | ShareLock and Chai summaries. | Supported as a defensive systems inference. | Threat prevalence and mitigation efficacy remain unverified. |
| Co-failure limits ensemble gains. | Source-reported co-failure framing. | Mechanistically plausible and testable. | Scope depends on model set, task distribution, and routing policy. |
| Process supervision gives evidence beyond final-answer accuracy. | OpenRCA and model-forensics synthesis. | Strong design principle. | Requires valid causal annotations and trace metrics. |
| The bundle supports deployment decisions. | Proposed implementations and controls. | Not established. | It supports review planning, not production certification. |

## 8. External primary-source context

Canonical public records confirm the identities around which the bundle is organized. EVAF, ShareLock, Chai, the co-failure paper, Model Forensics, OpenRCA 2.0, semantic early stopping, TAVR-VLM, EGG, and the false-vacuum report each have public arXiv locators.[^memory][^security][^process] Those records are primary publication locators. In this intake they were used to maintain identity and context, not to claim complete coverage of ten full texts.

The external context also reinforces the bundle's heterogeneity. Computer-security discovery, language-agent memory, clinical report generation, GPU kernels, and quantum simulation do not share an evaluation protocol. Their commonality is architectural: each places a learned component inside a larger process whose interfaces and validation determine whether the result is usable.

Code and reproducibility are unresolved at bundle level. The source says repositories, dependencies, checkpoints, and datasets were not audited. “Artifact available,” “artifact inspectable,” “artifact runnable,” and “result reproducible” must remain separate states.

## 9. Independent re-conceptualization: the evidence-gated state machine

Remove the paper names and the bundle becomes an evidence-gated state machine. A system receives observations through prompts, memories, tools, and domain data. It proposes a state update or action. A gate evaluates provenance, novelty, risk, agreement, and causal support. The gate may accept the update, quarantine it, request another iteration, forget it, or escalate to a human or deterministic validator.

This interpretation explains why the ten records fit together better than their domains suggest. Selective consolidation governs the write transition. Semantic early stopping governs the loop transition. Threshold poisoning governs adversarial composition at the input transition. Co-failure governs whether parallel proposals provide actual redundancy. Process supervision governs the justification transition. Medical grounding governs acceptance in a high-cost domain. Kernel and scientific tasks illustrate output transitions with deterministic or physical validators.

**Boundary of the analogy:** not every model exposes a clean state, not every claim has a deterministic validator, and a state-machine description can conceal social, clinical, or physical uncertainty. The interpretation is a design aid, not a theorem.

The transferable principle is: persist or act only when the evidence appropriate to that transition is archived. A memory write needs source and conflict metadata. A tool call needs manifest provenance. An ensemble decision needs dependence diagnostics. A diagnosis needs causal trace evidence. A scientific output needs domain validation.

## 10. Research notes, caveats, and failure modes

The largest failure mode is authority laundering: a generated daily finding becomes a polished manuscript and is later quoted as though the underlying experiment was independently verified. The DEP-E resists this by stating its boundary, and this DEP-A preserves that resistance.

A second failure mode is metric collision. Attack success, clinical quality, token savings, speed, and scientific scale can all sound like “improvement,” but they have incompatible denominators. A durable research graph should attach metric schemas to edges rather than ranking results by verbal intensity.

A third is interface blindness. A model may be safe in isolation yet unsafe when descriptions compose, when memory persists, or when router candidates share a blind spot. Component certification is therefore insufficient for an agent system.

A fourth is validation asymmetry. Kernel outputs may be compiled and benchmarked; cryptographic findings can be tested in authorized code; causal diagnoses may have partial labels; medical statements may require expert review; quantum interpretations may remain contested. One universal acceptance gate would either be too permissive or unusably strict.

A fifth is temporal drift. These sources were recent when the bundle was created. Versions, code, and peer-review status may change. The immutable source commit makes the archival judgment reproducible, while a correction DEP-A should be created for a materially changed state.

## 11. Implications

### Scientific implications

Agent research should report where state resides, how it is updated, which dependencies can jointly fail, and what evidence distinguishes mechanism from correlation. Evaluation sets should include persistent and compositional failures, not only single-turn scores.

### System-design implications

An agent platform benefits from typed ledgers for memory writes, tool manifests, loop decisions, model votes, causal traces, and validators. These are not verbose logs for their own sake; they are the minimum evidence needed to diagnose a composite failure.

### Deployment and governance implications

Appropriate use of the bundle is research triage, threat-model development, and experiment planning. Poor use includes medical deployment, security claims, or scientific conclusions derived from the summary alone. Required safeguards are source version pinning, prompt-injection isolation, per-transition evidence capture, domain-specific validators, abstention routes, and human review for high-impact decisions.

## 12. Falsifiable hypotheses

### Hypothesis 1: transition evidence predicts failures better than final confidence

**Proposition:** an agent reliability model using memory-write provenance, tool-manifest changes, stopping deltas, and vote dependence will predict downstream failure better than a model using final-answer confidence alone.
**Motivating evidence:** the bundle repeatedly places risk in process interfaces.
**Predicted observation:** transition features improve calibrated failure detection on persistent, tool-using tasks.
**Falsifying observation:** final confidence matches or exceeds performance after controlling for data volume and model capacity.
**Minimum test:** a preregistered evaluation with common train/test splits and process-level labels.

### Hypothesis 2: shared-failure auditing changes ensemble selection

**Proposition:** selecting models to minimize joint failure yields better worst-case outcomes than selecting by individual accuracy.
**Predicted observation:** a lower-average-accuracy set can outperform a top-accuracy set on the all-model failure tail.
**Falsifier:** shared-failure optimization produces no benefit across multiple task families.
**Minimum test:** compare selection policies with fixed model count and inference cost.

### Hypothesis 3: evidence-aware stopping dominates fixed depth under a budget

**Proposition:** a stopping policy using semantic change plus validator status improves quality per token.
**Predicted observation:** fewer redundant iterations with no loss in accepted-result quality.
**Falsifier:** the controller systematically stops before recoverable improvements or adds evaluator cost without savings.
**Minimum test:** common tasks, seeds, token budgets, and an oracle upper bound.

## 13. Replication and falsification agenda

The first priority is a claim-trace matrix for the ten central records. Each row should name paper version, claim, exact location, metric definition, experimental unit, code state, and reviewer verdict. This alone could correct summary drift without running experiments.

Second, select one source from each control surface: memory, tool security, co-failure, process supervision, stopping, grounding, optimization, and scientific validation. Inspect complete papers and appendices, then assess official code at a pinned commit. Do not treat a repository README as a successful run.

Third, build a small authorized composite harness. It should include a memory write/read cycle, a benign multi-tool manifest, a two-model router, an iterative task, and deterministic validators. Introduce one fault at a time, archive transition evidence, and measure whether gates localize it. Security experiments must remain defensive and synthetic.

Fourth, normalize reporting. Use common-instance metrics for model combinations; include failures rather than excluding them; report hardware and total pipeline time; separate inference, evaluator, and validator cost; and publish confidence intervals across data and training seeds.

The success criterion is not “reproduce every headline.” It is to know which conclusions survive precise source tracing and controlled tests. Falsifying evidence should be preserved alongside positive results.

## 14. Durable restatement

> The Tech Intel Agent Systems Review is best preserved as a map of evidence gates in composite AI systems. It identifies where reliability can fail—memory, loops, tool metadata, correlated model errors, causal traces, domain grounding, optimization, and scientific validation—but it does not independently validate the experiments behind its ten source summaries.

What should endure is the discipline encoded by the bundle: keep provenance and mechanism separate from promotional claims; treat interfaces as first-class risk surfaces; and require evidence appropriate to each state transition before persistence or action.

## 15. Coverage ledger

| Source item | Coverage | Material result | Caveat |
|---|---|---|---|
| README front matter, tags, and context | Complete | Establishes class, date, upstream identity, and public-safe purpose. | Upstream Black-Lake-Data files are referenced, not present. |
| README contents and summaries | Complete | Confirms exactly two tracked files and their roles. | No source documents are deposited. |
| README insights | Complete | Frames the ten findings as agent-systems reliability. | This is synthesis, not experimental proof. |
| README Attribution Block | Complete | Accounts for ten core records plus one future seed. | URLs establish provenance, not full-paper access. |
| Manuscript YAML and Source Metadata table | Complete | Records mixed status and metadata/abstract access. | Several statuses are historical to the source run. |
| Evidence Ledger and Executive/Detailed Summary | Complete | Separates repository evidence from paper locators and groups themes. | Quantitative details remain unverified. |
| Claims, methodology, scope, observations | Complete | Makes uncertainty and reviewer stance explicit. | No experiment execution. |
| Considerations, strengths, weaknesses, improvements | Complete | Provides a balanced research backlog. | Priorities are judgment calls. |
| Implementations, exercises, MVP | Complete | Converts themes into review tooling concepts. | Proposals are not deployed systems. |
| Related Reading, Source References, Appendix | Complete | Traces identifiers and selection provenance. | One related seed was not deeply reviewed. |
| Source-paper tables, figures, equations | Not materially applicable to the repository bundle | The DEP-E contains none of those primary-paper objects. | Complete paper audits are future work. |

## 16. Source and evidence notes

### Primary reviewed artifact

The complete primary object was the two-file DEP-E repository record at the exact source commit. All tracked text was read. The source record's upstream daily findings files and local paper copies were not uploaded into this DEP-A.

### External primary sources

- https://arxiv.org/abs/2606.26806
- https://arxiv.org/abs/2606.27027
- https://arxiv.org/abs/2606.26933
- https://arxiv.org/abs/2606.27288
- https://arxiv.org/abs/2606.26071
- https://arxiv.org/abs/2606.27154
- https://arxiv.org/abs/2606.27009
- https://arxiv.org/abs/2606.26874
- https://arxiv.org/abs/2606.26758
- https://arxiv.org/abs/2606.25889

### Evidence boundary

Repository claims are labeled as DEP-E-reported when they originate in the source synthesis. Canonical publication records were directly inspected as identity and context evidence. This is not ten independent full-paper reviews. Code was not executed, experiments were not rerun, and results were not independently reproduced. Reviewer inference appears in the control-surface model and hypotheses; proposals are explicitly falsifiable.

## Footnotes

[^bundle]: Immutable source record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260708-Tech%20Intel%20Review
[^memory]: Canonical memory and stopping records: https://arxiv.org/abs/2606.26806 and https://arxiv.org/abs/2606.27009
[^security]: Canonical tool-security and cryptographic-discovery records: https://arxiv.org/abs/2606.27027 and https://arxiv.org/abs/2606.26933
[^cofailure]: Canonical co-failure record: https://arxiv.org/abs/2606.27288
[^process]: Canonical model-forensics and process-supervision records: https://arxiv.org/abs/2606.26071 and https://arxiv.org/abs/2606.27154
[^quantum]: Canonical false-vacuum quantum-annealing record: https://arxiv.org/abs/2606.25889
