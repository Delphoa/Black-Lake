# Local AI as an Operational Evidence Stack

## A whitepaper-grade archival intake review of a composite DEP-E record

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260709-Local AI Stack`[^dep]
**Source commit:** `a1ffd4737ce95c14f3a15251ee4fbba4403108a5`
**Paired task indicator:** `BL-DEPPAIR-20260714-A29D9AC3`
**Direction:** `DEP-E -> DEP-A`
**Artifact prepared:** 2026-07-14
**Review scope:** complete repository-record review with external canonical-record checks
**Reproduction boundary:** no software was executed, no benchmark was rerun, and no reported result was independently reproduced
**One-way provenance:** review-only; source DEP modified: no; files moved: no; files copied: no; new derived DEP-A data generated: yes

---

## Executive assessment

Local AI is not a model-location decision. It is a coupled operational stack whose reliability depends on runtime packaging, accelerator support, tokenizer and adapter compatibility, memory policy, power and thermal constraints, data-local retrieval, persistent state, and tool authority.

This archival intake reviews the complete two-file DEP-E record as a composite evidence bundle about local and self-hosted AI. It does not present itself as a complete review of every paper or software release named by that bundle. The complete record is internally coherent as an evidence map. Its principal strength is breadth across layers that are often evaluated separately. Its principal weakness is that breadth can invite readers to flatten release announcements, abstracts, and generated synthesis into one confidence level. This intake therefore treats the DEP-E as the primary object, uses external pages only as evidence, and labels every stronger conclusion as reviewer inference.

The archival judgment is positive. The record is worth retaining because it makes a durable operational point and supplies traceable public references. Confidence is high in the repository inventory and provenance, medium in the cross-source synthesis, and low to medium in unverified performance or deployment implications. The proper use is prioritization and evaluation design.

## 1. Problem framing and research question

The practical question is not merely whether a model can run locally. It is whether a complete, versioned local system can deliver a target task under constraints on privacy, latency, energy, memory, correctness, maintainability, and authority. Model-centric comparisons hide the dependencies that decide real outcomes: serialization and quantization, tokenizer behavior, backend kernels, device support, cache placement, retrieval stores, persistent memory, tool permissions, and update cadence.

The review asks three bounded questions. First, what does the DEP-E record actually contain and at what evidence level? Second, which claims survive a conservative distinction among release-note evidence, abstract-level paper evidence, reviewer synthesis, and proposal? Third, how can the bundle be re-conceptualized into falsifiable evaluation work without implying that any system was reproduced?

This framing matters because “local” is a location property, not a quality guarantee. A local model can be stale, over-privileged, poorly evaluated, or exposed through logs and memory. Conversely, a carefully governed self-hosted system may offer useful data-control and latency properties. The record helps identify the decisions; it does not decide them automatically.

## 2. Complete inventory and source integrity

The record contains README.md and local-ai-research.md. The manuscript inventories official release pages for llama.cpp b9789, vLLM v0.23.0, Ollama v0.30.10, and Transformers v5.12.1, plus canonical arXiv records for FactoryLLM, an edge-device benchmark, OpenRad, an open-source-agent SAST study, Agent Memory, and a secure-agent survey.

The README is a manifest and attribution surface. The companion manuscript is a generated research artifact with source metadata, evidence ledger, executive synthesis, detailed summary, claims, methodology, limitations, implementation ideas, and an appendix. Both files were read completely. Their relationship is consistent: the README describes the manuscript and the manuscript accounts for the sources named in the attribution block.

The complete repository record was read from beginning to end. Direct external inspection in this intake was limited to canonical project-release and paper records; complete papers, binaries, code, datasets, and benchmarks were not executed or comprehensively audited. Accordingly, numerical paper statements remain DEP-reported or abstract-reported claims.

Integrity is strongest where the record reports its own limits. It repeatedly says that PDFs, binaries, datasets, and experiments were not collected or reproduced. That restraint is carried into this intake. No existing Markdown was copied into the DEP-A; this artifact restates the record in new language and preserves the one-way relationship.

## 3. Technical reconstruction of the evidence stack

The DEP organizes evidence into four layers. Runtime releases describe packaging and compatibility. Serving work describes memory movement and accelerator placement. Domain papers motivate local RAG, edge inference, medical curation, and security evaluation. Memory and secure-agent papers add persistent state, delegated authority, prompt injection, tool-mediated control flow, and state corruption.

A useful reconstruction separates six planes.

### 3.1 Artifact plane

Weights, tokenizer files, adapters, quantization formats, and build assets determine whether a nominal model can be loaded and interpreted. Version incompatibility at this plane can silently change output or prevent execution.

### 3.2 Runtime plane

Inference engines schedule kernels, manage batching, select backends, and expose APIs. Release notes provide primary evidence about intended support, but only executable fixtures establish behavior on a particular device and driver.

### 3.3 Memory plane

KV caches, retrieval indexes, agent memory, and logs decide how much context persists and how information is recalled. Memory is simultaneously a performance resource, a provenance surface, and a security boundary.

### 3.4 Domain plane

Industrial RAG, edge devices, medical curation, and static analysis have different loss functions. A generic language score cannot substitute for groundedness, power, expert verification, precision/recall, or false-positive cost.

### 3.5 Authority plane

Tool-using agents transform inference into action. Local execution does not reduce the need for least privilege, approval gates, state-change logs, and recovery procedures.

### 3.6 Evidence plane

Release notes, abstracts, complete papers, code, datasets, and reproduced results occupy different tiers. The DEP combines the first two tiers effectively but leaves most reproduction tiers open.

The architecture implied by the record is therefore not one application diagram but a dependency graph. Each edge should carry a version, evidence type, test status, and failure owner.

## 4. Evaluation design and evidence reconstructed

A rigorous evaluation would begin with a task contract: authorized inputs, expected outputs, refusal and escalation behavior, latency budget, energy or memory ceiling, and acceptable error. It would freeze the model and workload before changing the runtime or hardware. It would also record warm and cold starts, cache state, concurrency, precision, context length, and tool availability.

The record reports a broad release surface for llama.cpp, KV-cache offload and serving changes for vLLM, MLX support changes for Ollama, and PEFT/tokenizer fixes for Transformers. It also preserves abstract-level claims about FactoryLLM using 30 maintenance questions over roughly 600 pages, OpenRad screening 5,239 records and retaining 1,694 articles with expert review, and the SAST paper rejecting replacement of Bandit by the tested local agents. These are source claims, not reproduced results.

The quantitative statements are useful as discovery cues. The authors report them within separate papers and project contexts; they should not be pooled into a comparative score because they describe different tasks and were obtained under unrelated protocols. A figure about pages in a maintenance corpus cannot be compared with a count of screened medical papers or an SAST precision value. The defensible synthesis is structural: local systems need task-specific evidence and the infrastructure layer can change feasibility.

## 5. Results and what they support

The bundle supports four conclusions. First, local-AI tooling has a broad, fast-moving compatibility surface. Second, data-local applications are being explored in industrial, edge, medical-curation, and security contexts. Third, performance evidence is task-dependent and can be negative, as the SAST example illustrates. Fourth, memory and authority are first-class infrastructure for agents.

It does not support four stronger conclusions. It does not show that local deployment is always private; that any runtime is universally faster; that local models are clinically or industrially ready; or that an agent can safely replace a specialized tool. Those propositions require direct, matched evidence.

The distinction between feasibility and readiness is central. A release asset or paper abstract may show that a path exists. Readiness requires reproducibility, ongoing maintenance, monitoring, incident handling, and a measured fallback.

## 6. Ablations and quantitative audit

Not materially applicable as a unified experimental category. This is a composite source record, not one controlled experiment. The absence of cross-runtime, cross-hardware, or matched-workload comparisons is itself a major limitation. A defensible follow-on should hold models, prompts, precision, and data constant while varying runtime and hardware layers.

The most informative ablation matrix would vary one layer at a time: runtime with fixed model and hardware; quantization with fixed runtime; cache policy with fixed workload; retrieval and memory on/off with fixed questions; and tool permissions with fixed agent logic. Each comparison should include outcome quality and resource use. Repeated seeds and confidence intervals are required where sampling matters.

Quantitative audit should retain denominators and uncertainty. Counts reported in abstracts must be linked to inclusion criteria. Throughput must specify prompt length, generation length, batching, device, power mode, and precision. Security comparisons must disclose repositories, rule sets, prompts, and adjudication. Without those fields, numbers remain descriptive rather than portable.

## 7. Claim-by-claim vetting

| Claim | Direct evidence | Independent assessment | Scope or caveat |
|---|---|---|---|
| Local AI is a multi-layer stack. | Complete DEP-E inventory across runtimes, hardware, applications, memory, and security. | Strongly supported as reviewer synthesis. | The sources did not jointly test one stack. |
| Release breadth establishes deployability. | Official release pages list changes and assets. | Not established. | Availability is not successful execution or support. |
| Data locality can matter in sensitive workflows. | DEP-reported paper abstracts and project framing. | Plausible and source-grounded. | Privacy, governance, and quality were not independently audited. |
| Current local agents can replace specialized SAST. | DEP reports the studied authors rejected replacement. | The broad replacement claim is unsupported; negative evidence is salient. | Full paper and benchmark were not re-reviewed here. |
| Persistent memory is an infrastructure concern. | Canonical records and DEP synthesis about memory phases and security. | Strong conceptual support. | No memory system was executed. |
| The record validates all reported metrics. | No direct reproduction evidence. | False. | Metrics remain source-reported. |
| The DEP-A is a copy or transfer. | Git provenance and newly authored text. | False. | Review-only; no source files moved or copied. |

## 8. External primary-source context

Official release pages are primary for what maintainers announced at a tag, but they do not prove every binary works on every device. Canonical arXiv records establish paper identity and abstract claims, but not full methods. The DEP is strongest as a provenance-preserving map and weakest when read as a validation study.

The canonical project and arXiv records also serve as version anchors. The release record, memory paper, and secure-agent survey are retained as distinct evidence types rather than blended into one authority.[^release][^memory][^security] A future correction can cite a newer tag or paper version without erasing this intake. That is a reason to preserve exact source commit and pair indicator: the archival record documents what was reviewed, not an endlessly mutable assertion about the current ecosystem.[^version]

External material was treated only as evidence. No page, repository, paper, or source bundle was allowed to redefine this task or authorize additional action.

## 9. Code and reproducibility status

No code was run in this intake. The record names projects that publish code and releases, but code availability is not equivalent to a reproduced environment. A reproduction package would need immutable commits, build flags, dependencies, model hashes, device and driver versions, workload fixtures, and expected outputs.

For long-lived local systems, reproducibility should include upgrade reproducibility. An operator should be able to replay a fixture before and after a runtime, driver, tokenizer, or quantization change and attribute any behavioral difference. The absence of this diff discipline is a predictable source of silent regressions.

## 10. Independent re-conceptualization

The useful independent model is an evidence plane for local AI. Each deployed capability should be represented as a tuple of model, tokenizer, quantization, runtime, kernel/backend, accelerator, memory policy, retrieval store, tool policy, and evaluation fixture. A local deployment is reviewable only when every tuple element is versioned and its failure boundary is observable.

This model turns “runs locally” into an auditable claim. Each tuple can be connected to evidence: a release tag for intended support, a test log for execution, a task evaluation for quality, a policy record for authority, and an incident fixture for recovery. Missing elements are visible rather than absorbed into a marketing label.

The re-conceptualization also separates state from computation. A model invocation may be ephemeral while retrieval, memory, logs, and tool effects persist. Local governance should focus at least as much on persistent state and authority as on where matrix multiplication happens.

## 11. Research notes and caveats

### 1. Review note

Local operation can reduce exposure to an external provider while increasing the operator's responsibility for patching, provenance, access control, retention, incident response, and hardware behavior. This observation is a reviewer inference derived from the complete DEP-E bundle. It is not a claim that the named projects or papers jointly tested the proposition. The archival value comes from preserving the dependency and the uncertainty together: a downstream reader can see what must be checked before converting the observation into an operational decision.

### 2. Review note

A release tag is availability evidence, not reliability evidence. Asset matrices, build flags, and backends create a combinatorial support surface that requires fixture-based testing. This observation is a reviewer inference derived from the complete DEP-E bundle. It is not a claim that the named projects or papers jointly tested the proposition. The archival value comes from preserving the dependency and the uncertainty together: a downstream reader can see what must be checked before converting the observation into an operational decision.

### 3. Review note

Data locality does not guarantee data minimization. Persistent memory and RAG stores can accumulate sensitive context and become durable attack surfaces. This observation is a reviewer inference derived from the complete DEP-E bundle. It is not a claim that the named projects or papers jointly tested the proposition. The archival value comes from preserving the dependency and the uncertainty together: a downstream reader can see what must be checked before converting the observation into an operational decision.

### 4. Review note

Negative SAST evidence is especially valuable because it prevents privacy or openness from being mistaken for task competence. This observation is a reviewer inference derived from the complete DEP-E bundle. It is not a claim that the named projects or papers jointly tested the proposition. The archival value comes from preserving the dependency and the uncertainty together: a downstream reader can see what must be checked before converting the observation into an operational decision.

### 5. Review note

Medical and industrial examples must remain evaluation cases until governance, human review, data rights, and failure escalation are established. This observation is a reviewer inference derived from the complete DEP-E bundle. It is not a claim that the named projects or papers jointly tested the proposition. The archival value comes from preserving the dependency and the uncertainty together: a downstream reader can see what must be checked before converting the observation into an operational decision.


### Consolidated caveats

- No complete external paper was reviewed for this composite intake.
- No binary, model, code repository, benchmark, or dataset was downloaded into the public deposit.
- Release notes and abstracts were not independently reproduced.
- The DEP's original automation history is provenance context rather than technical evidence.
- Sensitive-domain examples do not authorize clinical, industrial, or security deployment.

These caveats are not procedural decoration. They define the maximum claim strength. The review can support an evaluation backlog and architectural model; it cannot support procurement, clinical use, replacement of security tools, or claims of reproduced performance.

## 12. Implications

1. **Implication 1.** Black-Lake can use the DEP as a source-thread index for deeper paper and code reviews. This follows at the level of research operations and evidence design; it does not grant deployment authority or establish comparative superiority.
2. **Implication 2.** Local-AI evaluations should report end-to-end latency, energy, memory, task quality, update cost, and failure recovery rather than tokens per second alone. This follows at the level of research operations and evidence design; it does not grant deployment authority or establish comparative superiority.
3. **Implication 3.** Stateful agents need explicit memory lineage and tool authorization even when every model call remains on premises. This follows at the level of research operations and evidence design; it does not grant deployment authority or establish comparative superiority.
4. **Implication 4.** Version pinning should extend beyond model weights to tokenizer, adapter, runtime commit, driver, kernel backend, and evaluation dataset. This follows at the level of research operations and evidence design; it does not grant deployment authority or establish comparative superiority.

A practical archival implication is that future DEP reviews should record a source-evidence matrix: canonical identifier, version, direct access level, code status, dataset status, reproduced status, and unresolved claims. That matrix would make bundle reviews comparable without pretending the underlying studies share one protocol.

## 13. Falsifiable hypotheses

### Hypothesis 1

**Proposition:** Configuration completeness will predict local-agent incident rate better than model size alone.

**Predicted observation:** a preregistered evaluation that varies the named factor while holding workload and scoring fixed should produce a directional, repeatable change.

**Falsifier:** the effect disappears across seeds and representative fixtures, or a simpler confound explains the result.

**Minimum test:** use public or authorized data, preserve exact versions, publish negative cases, and separate source reports from reviewer interpretation.

### Hypothesis 2

**Proposition:** Memory provenance controls will reduce persistent local-agent failures more than prompt-only defenses.

**Predicted observation:** a preregistered evaluation that varies the named factor while holding workload and scoring fixed should produce a directional, repeatable change.

**Falsifier:** the effect disappears across seeds and representative fixtures, or a simpler confound explains the result.

**Minimum test:** use public or authorized data, preserve exact versions, publish negative cases, and separate source reports from reviewer interpretation.

### Hypothesis 3

**Proposition:** Matched-workload comparisons will reveal that runtime/backend choice reverses model rankings on some edge devices.

**Predicted observation:** a preregistered evaluation that varies the named factor while holding workload and scoring fixed should produce a directional, repeatable change.

**Falsifier:** the effect disappears across seeds and representative fixtures, or a simpler confound explains the result.

**Minimum test:** use public or authorized data, preserve exact versions, publish negative cases, and separate source reports from reviewer interpretation.

### Hypothesis 4

**Proposition:** Negative task-specific baselines will remain more useful than general-agent scores for deciding replacement readiness.

**Predicted observation:** a preregistered evaluation that varies the named factor while holding workload and scoring fixed should produce a directional, repeatable change.

**Falsifier:** the effect disappears across seeds and representative fixtures, or a simpler confound explains the result.

**Minimum test:** use public or authorized data, preserve exact versions, publish negative cases, and separate source reports from reviewer interpretation.


## 14. Replication and falsification agenda

1. Freeze one public model and tokenizer, then run the same authorized prompt suite across two runtime backends with exact build and hardware manifests.
2. Reconstruct the FactoryLLM evaluation from the complete paper and any official code, using synthetic or authorized maintenance documents.
3. Rebuild the SAST comparison with a fixed repository corpus, Bandit configuration, local-agent prompts, and blinded false-positive review.
4. Create a memory-threat fixture that injects stale and conflicting records into an authorized toy agent and measures provenance-aware recovery.
5. Record all null results and configuration failures so release availability is not conflated with operational support.

The order is deliberate: establish a small, inspectable fixture before expanding to more models or devices. Every run should preserve negative and failed configurations. Reproduction should be considered successful only when an independent reviewer can reconstruct the environment and explain the scoring.

## 15. Durable restatement

> The record should be remembered as a map of the local-AI control plane: software release state, hardware placement, data locality, memory, tools, and governance jointly determine whether self-hosting is useful. It should not be remembered as proof that any named stack is secure, faster, cheaper, or ready for a sensitive domain.

The durable value is the dependency structure and evidence discipline. Specific release details will age; the need to bind capability claims to runtime, memory, authority, and task evidence will not.

## Appendix A. Coverage ledger

| Source element | Coverage in this review | Evidence boundary |
|---|---|---|
| DEP-E README | Inventory, context, attribution, limits, and relationship checked. | Directly inspected repository evidence. |
| Companion manuscript metadata | Identity, source list, access level, and confidence checked. | Directly inspected repository evidence. |
| Evidence ledger and claims | Reconstructed by layer and conservatively vetted. | Claims remain at their stated source level. |
| Detailed summaries | Accounted for in technical reconstruction and results. | No passage copied into the DEP-A. |
| Tables and quantitative claims | Major counts and evaluation categories audited. | Not recomputed or independently reproduced. |
| Implementation and MVP sections | Reframed as evidence-plane and replication work. | Proposals, not observed results. |
| Related research and source references | Canonical records checked for identity and scope. | Complete papers were not reviewed in this composite intake. |
| Appendix automation notes | Accounted for as provenance only. | Not treated as technical evidence. |
| Figures and equations | Not materially applicable to the composite repository object. | No new figures or equations invented. |

## Appendix B. Source and evidence notes

| Source | Public locator |
|---|---|
| Source DEP-E | https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-Local%20AI%20Stack |
| llama.cpp release | https://github.com/ggml-org/llama.cpp/releases/tag/b9789 |
| vLLM release | https://github.com/vllm-project/vllm/releases/tag/v0.23.0 |
| FactoryLLM record | https://arxiv.org/abs/2606.14119 |
| Agent Memory record | https://arxiv.org/abs/2606.06448 |
| Secure-agent survey record | https://arxiv.org/abs/2606.10749 |

### Evidence boundary

The complete selected DEP-E record is the primary reviewed object. Direct evidence means text or metadata inspected in that record or at the listed canonical pages. DEP-reported and paper-reported claims are labeled as such. Reviewer inference is confined to architecture, caveats, hypotheses, and evaluation design. No experiment was independently reproduced.[^boundary]

### Provenance facts

- Source action: review-only.
- Source DEP modified: no.
- Files moved: no.
- Existing files copied into DEP-A: no.
- New derived data generated: yes.
- Intake and deposition become complete only with validation and repository submission.

## Footnotes

[^dep]: Immutable source record: https://github.com/Delphoa/Black-Lake/tree/a1ffd4737ce95c14f3a15251ee4fbba4403108a5/.lake-data/DEP-E/DEP-E-20260709-Local%20AI%20Stack
[^version]: Official release pages and canonical paper records are version evidence, not proof of reproduced behavior.
[^boundary]: Reproduction boundary: no binary, code, benchmark, model, or experiment was run.
[^release]: llama.cpp release evidence: https://github.com/ggml-org/llama.cpp/releases/tag/b9789
[^memory]: Agent Memory canonical record: https://arxiv.org/abs/2606.06448
[^security]: Secure-agent survey canonical record: https://arxiv.org/abs/2606.10749
