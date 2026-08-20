---
title: "Memory Defense Layers - DEP-E"
generated_at: "2026-07-18T00:04:42Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-grounded review of architecture-layer defenses for persistent-memory attacks in stateful LLM agents."
source_status: "Public URLs and repository-relative source artifacts; no source payloads collected"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-18"
temporal_cutoff: "2026-07-18"
primary_url: "https://arxiv.org/abs/2605.08442"
stable_identifier: "arXiv:2605.08442v4"
confidence_summary: "Medium-high for accurately reporting the inspected paper and repository; lower for independent validity because experiments and released code were not executed."
safety_scope: "Defensive research, evaluation design, provenance controls, and authorized agent-runtime monitoring"
distribution_notes: "No paper PDF, TeX source, experiment log, model artifact, credential, private trace, or local execution context is redistributed."
---

# Memory Defense Layers - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | DEP-20260701-Tech Intel 0103 README | Selected source DEP manifest | Markdown | DEP-20260701-Tech Intel 0103 | Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/README.md | Repository artifact; no source payload copied. | 2026-07-18 | Inspected |
| S2 | Daily Research Findings - 2026-07-01 0103 | Selected source synthesis | Markdown | DEP-20260701-Tech Intel 0103 | Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/daily_research_findings_2026-07-01_0103.md | Repository-generated research artifact. | 2026-07-18 | Inspected |
| S3 | Prior processing report and Report-Mark | Prior same-family provenance | Markdown | 2026-07-11 pass; Report-Mark 001 | Black-Lake-Data/.reports/BL-DEP-20260701-Tech Intel 0103-20260711/README.md; Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/BL-DEP-Mark001 Report-Mark.md | Repository records; exact copied prior sections inspected. | 2026-07-18 | Inspected |
| S4 | Prior Memory Forensics DEP-E and log | Prior same-family research artifact | Markdown | DEP-E-20260711-Agent Memory Forensics | Black-Lake/.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md; Black-Lake/.logs/20260711-DEP-20260701-Tech Intel 0103-LOG.md | Prior review context, not independent experimental evidence. | 2026-07-18 | Inspected |
| S5 | Prior 2D-RC OTFS DEP-E and log | Earlier cross-DEP context | Markdown | DEP-E-20260709-2D-RC OTFS | Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md; Black-Lake/.logs/20260709-Arxiv-2D-RC-OTFS-LOG.md | Context explaining the earliest Black-Lake reference to the selected source DEP. | 2026-07-18 | Inspected |
| S6 | Defense effectiveness across architectural layers | Selected primary paper metadata | arXiv abstract | arXiv:2605.08442v4 | https://arxiv.org/abs/2605.08442 | arXiv links CC BY 4.0; version revised 2026-07-03. | 2026-07-18 | Inspected |
| S7 | Defense effectiveness across architectural layers | Selected primary paper full text | arXiv HTML | arXiv:2605.08442v4 | https://arxiv.org/html/2605.08442 | Full methods, results, discussion, limitations, ethics, and appendices inspected. | 2026-07-18 | Inspected |
| S8 | Stateful Agent Security Evaluation | Official implementation and evidence repository | GitHub repository | main branch at access time | https://github.com/junwenleong/stateful-agent-security-eval | MIT license shown; README, repository inventory, tests/configs/results presence, and no-release status inspected. Exact commit pin was not available from the inspected page. | 2026-07-18 | Repository overview and README inspected; code not executed |
| S9 | Forensic Trajectory Signatures for Agent Memory Poisoning Detection | Companion primary paper | arXiv abstract and HTML | arXiv:2606.30566v1 | https://arxiv.org/abs/2606.30566; https://arxiv.org/html/2606.30566 | CC BY 4.0; public v1 remained unchanged at access time. | 2026-07-18 | Metadata and full text re-inspected |
| S10 | Repository authorities | Deposition rules | Markdown | fetched default branches at review time | Black-Lake/README.md; Black-Lake/.lake-data/README.md; Black-Lake-Data/README.md | Governs DEP class, placement, publication index, manifest, log, attribution, and submission rules. | 2026-07-18 | Inspected after fetch |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S2 | Selected source DEP | Ten-source inventory, original companion-paper discovery, public locators, and source-bundle themes. | Selection provenance and relationship to agent memory, execution control, and communication security. | High for repository provenance; medium for research summaries | The source DEP summarizes papers and does not replace direct review. |
| E2 | S3-S4 | Prior same-family records | Earlier random expansion, evidence boundaries, prior claims about trace-only detection, and reviewer questions. | Iterative baseline and identification of unexpanded related sources. | High for provenance; medium for prior interpretation | Prior generated artifacts are not independent validation. |
| E3 | S5 | Prior cross-DEP records | Earlier conceptual link from the selected source DEP to state and communication review. | Historical context for prior-material detection. | High for repository provenance | OTFS findings do not support memory-security claims. |
| E4 | S6 | Primary arXiv metadata | Title, author, v4 revision, abstract claims, DOI, subjects, code link, and license. | Source identity and high-level claims. | High | Abstract-level evidence alone cannot validate experiments. |
| E5 | S7 | Primary full paper | Four-session attack design, six defenses across four layers, 5,040-run factorial, statistical procedure, primary results, ablations, frontier evaluation, limitations, and appendices. | Mechanism, reported metrics, validity boundaries, and implementation implications. | Medium-high for reporting source claims | Results were not reproduced; some equations and interval values are absent from HTML text extraction. |
| E6 | S7 | Primary full paper | Memory Sandbox bypasses, think-toggle crossover, RATG proof of concept, and Defense Attribution Validity Criterion. | Model/runtime interaction and reasons capability removal can change the attack path. | Medium | Full crossover is single-family; RATG reasoning-model efficacy has no supported claim. |
| E7 | S7 | Primary full paper | Loaded-corpus endpoint results and injection-versus-execution behavior. | Endpoint- and date-conditioned vendor/model observations and shared-memory persistence risk. | Medium | Hosted aliases can change; one pre-release model is included; results are not universal vendor guarantees. |
| E8 | S8 | Official repository | Public README, visible source/config/data/results/tests inventory, quick-start estimates, MIT license, and absence of releases. | Artifact availability and practical reproduction requirements. | Medium-high | Individual code paths, raw logs, and tests were not independently audited or run; no commit pin was recovered. |
| E9 | S9 | Companion primary paper | Public v1 threat model, 19-feature classifier, source-reported AUC values, negative-class definition, and explicit lack of true-benign baseline. | Trace-detection baseline and versioned evidence tension with S7. | High for public v1 contents | The selected paper's v4 discussion reports true-benign overlap not present in the public companion v1. |
| E10 | S10 | Repository policy | DEP-E class, index update, public-safe attribution, and commit conventions. | Artifact structure and submission validation. | High | Policy evidence does not support scientific claims. |

## Executive Summary

This iterative DEP-E expands `DEP-20260701-Tech Intel 0103` through a second random draw from the two unexpanded primary or near-primary items preserved by its prior manuscript. The draw selected *Defense effectiveness across architectural layers: a mechanistic evaluation of persistent memory attacks on stateful LLM agents* (arXiv:2605.08442v4), the companion study underlying the source DEP's earlier memory-forensics review.

The selected paper reports a 5,040-run factorial across nine open-source models, six defenses plus an undefended baseline, and matched attack/no-attack arms. Its central source claim is architectural: input defenses cannot observe a payload introduced through RAG; the tested retrieval classifiers observe it but do not distinguish the compliance-framed document at their tested operating points; prompt hardening often fails at execution; and tool-layer recall removal is the only tested defense that strongly interrupts the primary path. The aggregate reported attack-success rates are 88.6% for no defense, 88.9% for each of four input/retrieval defenses, 77.8% for prompt hardening, and 11.1% for Memory Sandbox, with 100% binary task-completion rate in the no-attack arms.

The paper also supplies its own reasons not to turn those figures into a universal deployment rule. Memory Sandbox is bypassed through alternative retrieval on multiple provider/model stacks; a full reasoning-mode crossover is shown only within one model family; a content-layer defense called RATG reaches 0% reported attack success for three reproducible mechanical models but has no supported reasoning-model efficacy claim; and several attractive results are excluded because baselines or pre-activation behavior do not reproduce. Frontier results are explicitly endpoint- and date-conditioned.

The strongest reviewer conclusion is therefore a design constraint, not a product claim: persistent memory should carry provenance and authority metadata, recall should be privileged, and high-impact actions should be gated against provenance-bearing state. Trace-only classifiers can remain useful forensic signals, but the selected paper's v4 discussion reports true-benign score overlap that is not represented in the still-public companion v1. This unresolved version tension lowers confidence in a universal trace-blocking interpretation and strengthens the case for provenance-aware policy enforcement plus evaluation-validity gates.

## Detailed Summary

### Iterative Research Object

The source DEP contains ten primary research findings spanning memory, multi-agent security, policy, model hubs, entity binding, execution control, medical agents, vision-language tools, and quantum authentication. A 2026-07-11 same-family pass randomly selected arXiv:2606.30566 and generated the prior `Memory Forensics - DEP-E` artifact. That manuscript preserved two unexpanded primary or near-primary items: the companion defense paper and an execution-control neighbor. This pass randomly selected the companion defense paper and inspected its current v4 full text and public implementation repository.

### Threat Model and Authority Boundary

The selected paper evaluates a delayed-trigger attack in a simulated enterprise agent. A RAG-retrieved document is framed as an internal compliance rule, stored during an injection session, retained through two unrelated sessions, and recalled during a later email task. Conversation history is isolated between sessions; persistent state is the intended bridge. Injection and attack success are measured separately so that storage-stage and execution-stage effects are not conflated.

The research object is security-sensitive, but this artifact does not reproduce or operationalize the attack. Its useful mechanism is the authority boundary: retrieved text becomes durable state and later influences a privileged action. A defense that cannot observe the relevant state transition or mediate the action cannot be credited merely because its classifier is strong in another location.

### Six Defenses Across Four Layers

The factorial compares Minimizer and Sanitizer at the input layer, RAG Sanitizer and a small RAG LLM Judge at retrieval, Prompt Hardening at instruction, and Memory Sandbox at the memory-tool layer. The input defenses never receive the retrieved malicious document. The tested retrieval defenses receive it but do not flag the compliance-framed content. Prompt Hardening reduces aggregate attack success but provides no protection for seven of nine reported models. Memory Sandbox removes explicit recall and reduces aggregate attack success to 11.1%, driven by blocking for eight of nine local models in the primary factorial.

The paper characterizes this as a layer-placement result first and a classifier result second. That distinction is partly structural and partly empirical. Blind input filters cannot see a RAG payload by construction. Retrieval-filter failure is bounded to the tested corpus, small training set, and 1.5B/7B judges; the paper explicitly declines to claim that no larger or better-trained retrieval defense could work.

### Experimental and Statistical Design

The primary factorial covers nine models, seven conditions, two attack arms, and 40 runs per cell, totaling 5,040 runs. It uses fresh SQLite state per run, fixed model/runtime settings within the reported experiment, deterministic outcome tagging, and 115 pre-specified comparisons, with 108 active after undefined baselines are removed. Confidence intervals use BCa bootstrap unless a degenerate binary vector requires Wilson intervals; Holm-Bonferroni correction controls the active comparison family.

The paper is unusually explicit about power and negative evidence. Its design resolves the observed near-zero or greater-than-77-percentage-point effects but is not powered for modest 10-20-point changes. Defenses are tested independently rather than stacked, and the benign task-completion measure does not assess latency or output quality.

### Capability Removal, Bypass, and Double Dissociation

Memory Sandbox is not uniformly safe. The paper reports alternative RAG retrieval when recall is unavailable on Mistral, Z.AI, and OpenAI models served through a separate stack, as well as re-injection during an intervening session. It also reports a perfect crossover in a Qwen-3-32B think-toggle ablation: schema removal and null-return variants yield opposite outcomes depending on whether reasoning mode is enabled. The full crossover is bounded to that family, while one alternative-retrieval arm is reproduced more broadly.

This supports a narrower inference: removing a capability can alter the information path and task-completion strategy, so a safety evaluation must inspect the entire resulting action path. It does not support the broad claim that reasoning models are inherently more or less safe; the paper documents divergent behavior even among reasoning-capable systems.

### Content-Layer Gating and Validity Criteria

RATG retains the recall tool but sanitizes recalled routing directives and unauthorized addresses before the content reaches the model. The source reports 100% to 0% attack-success changes for three mechanical models whose baselines reproduce. It withholds a reasoning-model efficacy claim because baseline vulnerability or pre-activation equivalence fails.

The resulting Defense Attribution Validity Criterion is one of the paper's most reusable contributions. A defense effect requires both a reproducible vulnerable baseline across independent runtime loads and behaviorally identical defended/undefended arms before the defense activates. A complementary Retrieval-Fidelity Criterion requires a RAG-security evaluation to make the relevant document retrievable through the actual tested channel. The authors apply the latter criterion to reject their own initial 0/210 empty-corpus frontier result as a threat-model artifact.

### Frontier and Shared-Memory Findings

The loaded-corpus evaluation covers 21 hosted models across three providers and reports sharply different storage and execution behavior. The most conspicuous figures include 95% attack success for a pre-release Gemini 3.1 Pro Preview endpoint, a non-monotonic GPT sequence with 22.5% for GPT-5.1 versus 5% for GPT-5, and 0% execution for several later models despite near-universal rule storage. Anthropic models in the tested endpoints predominantly block earlier, at injection or storage.

These are author-reported, endpoint- and date-conditioned observations, not stable vendor ratings. The transferable issue is the injection-execution split. A model that refuses execution can still leave adversarial durable state for a later model or agent. The paper argues compositionally that a shared plain-text store without writer identity or derivation lineage cannot tell a downstream reader whether a fact came from a user, a retrieved document, itself, or another agent. The end-to-end cross-model write/read attack is not run, so the supply-chain claim remains a structurally supported inference rather than a directly demonstrated experiment.

### Reproducibility and Released Artifacts

The paper documents ten evaluation artifacts and a separate daemon-state degradation issue. Tool return text, schema composition, context settings, daemon lifecycle, and effective served configuration can alter whether a model emits a tool call. Some apparently safe results were excluded after baseline behavior failed to reproduce. The paper recommends process restarts and verification of effective runtime parameters, not merely intended configuration.

The public repository exposes source, attack/defense modules, configurations, data, results, tests, analysis scripts, a canonical-number verifier, Docker assets, and an MIT license. Its README estimates a full local factorial at roughly 8.5 days on the published single-GPU setup and lists large model/runtime requirements. This pass inspected the repository overview and README only. It did not clone the repository, inspect every code path, run tests, reproduce tables, or verify raw logs, so code presence raises reproducibility potential rather than proving reproduction.

### Versioned Tension With the Prior Companion Review

The public companion arXiv v1 reports high cross-validation AUC on poisoned attack-arm sessions and explicitly states that its negative class excludes unpoisoned true-benign sessions. The selected paper's later v4 discussion says benign memory-grounded actions produce nearly indistinguishable mean detector scores (0.974 versus 0.971) and that some safety-conscious models yield 95-100% false positives. Those later claims are not visible in the still-public companion v1 inspected on 2026-07-18.

The evidence therefore supports a versioned conflict, not a silent reconciliation. Trace patterns remain potentially useful for forensic attribution under explicit logging assumptions, but a production blocking claim needs the missing true-benign protocol, versioned data, and independently reproducible thresholds.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Defense effectiveness is strongly constrained by whether the defense observes the payload/provenance or mediates the memory-to-action path. | Author claim with structural and empirical components | E4-E6 | Structural for blind input placement; empirical and setup-bounded for retrieval classifiers, prompts, and tool variants. | High for the placement principle; medium for generalization |
| C2 | The primary factorial reports 88.6% no-defense ASR, 88.9% for four input/retrieval defenses, 77.8% for prompt hardening, and 11.1% for Memory Sandbox. | Author empirical result | E5 | Directly present in the full paper; not independently reproduced. | High for accurate reporting; low for independent validity |
| C3 | No tested memory-schema sandbox is uniformly safe across the evaluated reasoning modes and model behaviors. | Author claim | E6 | Supported by one full single-family crossover plus broader reproduction of an alternative-retrieval bypass; not a universal reasoning-model law. | Medium |
| C4 | A defense effect should require baseline reproduction and pre-activation equivalence, while RAG evaluation requires a faithful loaded corpus. | Author methodological contribution | E5-E6 | Strong, auditable evaluation criteria that the paper applies to exclude its own misleading results. | High |
| C5 | Shared memory without provenance can preserve dormant adversarial state across model or agent boundaries. | Author compositional inference | E7 | Mechanistically plausible and supported by separate write/execution results, but the end-to-end cross-model chain was not executed. | Medium |
| C6 | The selected paper and companion v1 do not currently present a consistent public account of true-benign trace separability. | Reviewer observation | E5, E9 | Direct versioned tension: v4 reports near-overlap/high false positives; public companion v1 states no true-benign baseline. | High |
| C7 | Repository availability improves auditability but does not establish reproducibility until code, configurations, logs, and outputs are pinned and executed. | Reviewer interpretation | E8 | The repository exposes substantial artifacts, but this pass did not run them and recovered no exact commit pin. | High |

## Methodology

- `Research objective`: Expand an older eligible source DEP through one randomly selected unexpanded research thread and produce a schema-complete, provenance-preserving DEP research artifact.
- `Sources inspected`: The selected DEP README and findings; its prior report and Report-Mark; the latest same-family log, DEP README, and full manuscript; the earlier 2D-RC log and manuscript referenced by the prior report; arXiv metadata and full HTML for arXiv:2605.08442v4; the official GitHub repository overview/README; current arXiv metadata and full HTML for companion arXiv:2606.30566v1; and fetched repository authorities.
- `Discovery strategy`: Enumerated 60 canonical source DEP directories; scanned same-family `.reports`, `.logs`, Report-Marks, and prior markers across both repositories; used PowerShell `Get-Random` over the eligible sorted set; then used a second PowerShell `Get-Random` draw over the two unexpanded primary/near-primary items preserved in the prior manuscript.
- `Inclusion criteria`: Direct primary sources, official implementation material, repository provenance, prior same-family context, and sources necessary to explain an evidence conflict.
- `Exclusion criteria`: Attack execution, code cloning/execution, PDF/TeX download, model or dataset download, hosted endpoint testing, raw-log collection, and unrelated source-DEP findings beyond context.
- `Analytical approach`: Empirical reporting, conceptual mechanism review, comparative defense analysis, implementation planning, safety/ethics, replication review, product research, and DEP provenance.
- `Evidence handling`: Author claims remain labeled as source claims; numerical results are tied to the inspected paper; reviewer interpretations and version conflicts are explicit; repository policy is separated from research evidence.
- `Uncertainty handling`: Unreproduced experiments, unavailable exact commit pin, endpoint drift, HTML rendering gaps, single-family ablations, proof-of-concept scope, and conflicting public versions remain visible.
- `Extraction process`: Repository Markdown was inspected directly; public arXiv and GitHub pages were inspected as HTML; no external source file was collected.
- `Version control`: The primary paper is pinned to public arXiv v4 and the companion to public arXiv v1; the GitHub source is identified as main at access time without an invented commit SHA.
- `Reviewer stance`: Defensive manuscript review, replication-readiness critique, implementation translation, and source-preserving iterative DEP expansion.

## Scope, Constraints, and Assumptions

- `Scope`: Architecture-layer defenses, evaluation validity, provenance risk, and their relationship to the selected source DEP's earlier trace-detection artifact.
- `Temporal boundary`: Public sources and fetched repository authorities were inspected on 2026-07-18; model and hosted-endpoint results can change after that date.
- `Evidence limits`: Experiments, code, tests, raw logs, configurations, model endpoints, and statistical analyses were not independently executed. Some mathematical symbols and intervals are missing in HTML extraction.
- `Assumptions`: The public arXiv HTML corresponds to the named versions; repository-relative paths remain stable enough for follow-on review; official repository README claims describe the visible main-branch inventory at access time.
- `Constraints`: Defensive-only discussion; synthetic or authorized examples; no credentials, private traces, restricted data, local absolute paths, machine identifiers, local timezone labels, or source payload redistribution.
- `Out of scope`: Reproducing the attack, ranking vendors generally, asserting production safety, independently validating reported ASR figures, or shipping an autonomous blocker.
- `Intended use`: Black-Lake deposition, defensive architecture review, evaluation planning, provenance-system design, and follow-on replication.
- `Audience`: Agent-platform engineers, security researchers, evaluation operators, provenance-system designers, and future Black-Lake reviewers.
- `Reproducibility boundary`: A reviewer can retrieve the paper and repository and inspect the named artifacts, but exact reproduction requires pinned code, large model/runtime resources, hosted API access for some arms, and environment controls not exercised here.
- `Operational boundary`: Mechanisms may be analyzed to improve defenses, but this artifact does not provide an operational attack recipe or payload.
- `Data sensitivity`: Public research and repository artifacts only.

## Observations

- `Observed pattern`: The paper's strongest result is a map from state authority to action authority; classifier performance is secondary to where trust is decided.
- `Observed pattern`: The authors reject their own clean-looking results when retrieval fidelity, baseline reproduction, or pre-activation identity fails. This is unusually valuable negative evidence.
- `Contradiction or tension`: Public arXiv v1 of the companion lacks a true-benign baseline, while the selected paper's later v4 discussion reports true-benign score overlap and very high false positives. The underlying protocol/version is not public in the inspected companion.
- `Technical implication`: Durable agent memory needs writer identity, source lineage, policy scope, expiry, and read-time authorization; plain key-value state is insufficient for cross-agent trust.
- `Technical implication`: Tool schemas, return messages, daemon state, model version, and effective configuration must be first-class evaluation variables.
- `Reviewer hypothesis`: A defense stack combining provenance-bearing writes, content-aware recall policy, action authorization, and trace forensics should be evaluated compositionally, because isolated single-layer success can move rather than remove a harmful pathway.
- `Open question`: Can the released repository reproduce the current v4 tables from a pinned clean environment, including the true-benign trajectory result attributed to the companion work?

## Considerations

Persistent-memory evaluation is dual-use because it studies how harmful instructions survive and influence later actions. Follow-on work should remain synthetic or authorized, isolate external effects, and emphasize detection, provenance, and policy enforcement. Published logs and datasets should be checked for credentials, private content, and live endpoints before reuse.

The frontier-model observations are time-sensitive and should not become permanent vendor ratings. Hosted aliases, provider updates, gateways, tool implementations, and prompt/runtime changes can alter results. Evaluation records should preserve requested and effective model identifiers, endpoint/provider, date, tool schema hash, prompt/configuration hash, and environment manifest.

Trace-only monitoring reduces content exposure but does not eliminate privacy risk. Operation names, timing, and correlations can reveal business workflows. A production evidence ledger needs field minimization, access control, retention limits, and explicit purpose boundaries.

Blocking should not be based on the selected paper's or companion's headline metrics alone. The source set supports defense-in-depth, version-pinned evaluation, and human-reviewed escalation more strongly than an autonomous universal classifier.

## Strengths

- The paper evaluates multiple defense layers against one controlled mechanism rather than comparing unrelated benchmark scores.
- Injection, execution, and benign task completion are separated, exposing dormant-state risk that outcome-only monitoring misses.
- Pre-specified comparisons, multiplicity control, and explicit power limits improve interpretability of the primary factorial.
- The authors document evaluation artifacts, fragile baselines, and excluded results rather than smoothing them into a single success narrative.
- The retrieval-fidelity and defense-attribution criteria are reusable beyond this specific attack class.
- The official repository exposes configs, results, tests, analysis scripts, and canonical-number verification under a permissive license.
- The selected source DEP and prior Report-Mark provide a clear provenance chain from daily discovery to iterative full-paper review.

## Weaknesses

- The core experiment uses one simulated enterprise stack, one primary malicious document, one trigger framing, and lightweight retrieval classifiers.
- Several prominent reasoning and frontier observations are single-family, environment-conditioned, endpoint-conditioned, or pre-release.
- The primary design is not powered for moderate defense effects and does not test combined defense stacks.
- BTCR measures task attempt, not quality, latency, recipient correctness, or broader utility.
- The shared-memory supply-chain claim is compositional; the cross-model write/read chain is not executed end to end.
- Repository presence does not substitute for a pinned independent reproduction; this pass did not run code or audit raw logs.
- The selected paper's v4 benign-trajectory claim and the public companion v1 evidence base are not publicly reconciled.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Pin a reproducible release | Reproducibility | Main-branch state can move and no release is published. | Stable linkage among paper v4, code, configs, logs, and canonical figures. | Packaging and maintenance effort. | Rebuild every reported table from a signed tag and clean manifest. |
| Publish the true-benign companion protocol | Evidence consistency | The v4 benign-overlap claim is absent from companion v1. | Resolves a central deployment-boundary conflict. | Additional dataset governance and revision work. | Add versioned benign tasks, labels, thresholds, and companion revision. |
| Run provenance-bearing shared-memory tests | Compositional security | The cross-model supply-chain path is argued but not executed end to end. | Direct evidence for writer/reader lineage controls. | Requires careful synthetic, authorized multi-model design. | Compare plain state, signed lineage, scoped capability, and deny-path audit. |
| Evaluate defense stacks | External validity | Single-layer controls can shift pathways. | Shows whether provenance, recall filtering, action gates, and forensics complement or interfere. | Larger factorial and interaction complexity. | Pre-register compositional arms and preserve pre-activation equivalence. |
| Expand retrieval-framing diversity | Generalization | One compliance document cannot characterize semantic masking broadly. | Better bounds on classifier and provenance behavior. | More source design and human review. | Use benign/malicious synthetic policy families with held-out framings. |
| Capture effective environment manifests | Evaluation integrity | Intended model/runtime configuration can differ from served behavior. | Faster diagnosis of non-reproducible baselines. | Operational instrumentation burden. | Store hashed schemas, prompts, endpoints, model identifiers, process state, and health checks per arm. |

## Potential Implementations

1. `Provenance-Bearing Memory Gateway`
   - `User`: Agent-platform security engineer.
   - `Goal`: Prevent untrusted retrieved text from silently becoming high-authority durable state.
   - `Core mechanism`: Attach writer identity, source locator, derivation, policy scope, expiry, and authorization status to every memory write; enforce read-time and action-time policy over those fields.
   - `Required inputs`: Memory events, source classifications, principal identity, policy version, action capability, and approved resource identifiers.
   - `Outputs`: Accepted/rejected writes, scoped memory objects, deny-path audit records, and provenance-linked action decisions.
   - `Risk controls`: Default-deny authority elevation, signed metadata, least privilege, content minimization, retention controls, and human approval for high-impact actions.
   - `Evaluation`: Synthetic multi-session workflows with pre-registered benign and adversarial state transitions; no external actions.

2. `Defense Attribution Harness`
   - `User`: Safety evaluation operator.
   - `Goal`: Prevent false defense claims caused by retrieval mismatch, runtime drift, or pre-activation divergence.
   - `Core mechanism`: Compare baseline and defense arms before activation, verify loaded-corpus fidelity, pin effective manifests, and reject cells whose vulnerable baseline does not reproduce.
   - `Required inputs`: Versioned tasks, model/runtime manifests, event traces, activation boundary, expected baseline, and statistical plan.
   - `Outputs`: Validity report, excluded-cell ledger, effect estimates, and reproducibility gaps.
   - `Risk controls`: Synthetic data, isolated tools, no live recipients, safe fixtures, and explicit stop conditions.
   - `Evaluation`: Seeded toy experiments where injected confounds must be correctly detected and excluded.

3. `Trace-and-Provenance Review Queue`
   - `User`: Incident response and internal audit teams.
   - `Goal`: Combine trajectory signals with memory provenance and policy context without treating a trace score as proof.
   - `Core mechanism`: Create an evidence package linking ordered tool events, state lineage, model/runtime version, policy decisions, and reviewer disposition.
   - `Required inputs`: Redacted event metadata, provenance-bearing memory references, policy hashes, model identifier, and reviewer labels.
   - `Outputs`: Evidence ledger, confidence-bounded alert, unresolved-evidence list, and follow-up decision.
   - `Risk controls`: No raw secrets in exports, encrypted storage, role-based access, retention limits, threshold calibration, and human review.
   - `Evaluation`: Held-out benign synthetic workflows plus authorized incident-tabletop cases.

## Three Ways to Exercise This Research

1. `Map the authority path`: Objective: identify where untrusted text becomes durable state and where state becomes action. Inputs: a harmless synthetic agent workflow, tool schema, and policy. Method: draw the retrieval-write-recall-action path and label each provenance/authorization check. Output: a gap table. Success criterion: every authority change has an owner and evidence record. Stop condition: do not connect the exercise to real external actions.
2. `Test attribution validity`: Objective: rehearse the selected paper's retrieval-fidelity and pre-activation-equivalence criteria. Inputs: two synthetic experiment arms and an intentionally mismatched corpus or configuration. Method: compare pre-activation traces and effective manifests, then accept or reject the effect claim. Output: a validity decision with reasons. Success criterion: the planted confound is detected. Stop condition: stop if baseline vulnerability cannot be reproduced safely.
3. `Prototype provenance policy`: Objective: test whether memory metadata changes a later action decision. Inputs: synthetic facts with writer, source, scope, and expiry fields. Method: evaluate plain key-value, unsigned metadata, and signed/scoped metadata under a deterministic action policy. Output: allow/deny audit ledger. Success criterion: untrusted or expired state cannot authorize the high-impact toy action. Stop condition: use only synthetic principals, resources, and destinations.

## Example MVP Product

- `Product name`: Memory Authority Ledger
- `Target user`: Teams operating multi-session, tool-using agents with shared or persistent memory.
- `Problem`: Plain durable state loses who wrote it, where it came from, what authority it carries, and whether it may justify a later action.
- `Core workflow`: Intercept memory writes, attach signed provenance and scope, validate recall against the active principal/purpose, require an explicit policy decision for high-impact actions, and export a redacted evidence ledger for review.
- `Data requirements`: Synthetic or authorized memory events; source and writer identifiers; policy versions; capability/resource identifiers; expiry; redacted action outcomes; evaluation labels.
- `Architecture`: Write gateway, provenance signer, scoped memory store, recall-policy service, action authorization gate, append-only audit ledger, and reviewer interface/exporter.
- `Success metrics`: Provenance completeness, unauthorized-write rejection, deny-path audit coverage, benign task completion, false-block rate on held-out safe workflows, reproducible manifest coverage, and zero sensitive-data leaks in exported ledgers.
- `Risk controls`: Default-deny authority changes, signed metadata, separation of duties, least-privilege capabilities, no raw secrets in public artifacts, retention limits, human override, and periodic policy/model regression tests.
- `Limitations`: The MVP cannot prove source truth, inspect hidden model state, or guarantee safety when tools bypass the gateway; provenance can be wrong if identity or ingestion controls are compromised.
- `MVP boundary`: Local or isolated authorized evaluation first; no autonomous blocking in production and no external side effects.
- `Deployment model`: Internal sidecar or gateway for a controlled agent runtime.
- `Evaluation plan`: Unit tests for policy rules, synthetic multi-session scenarios, manifest-drift tests, benign calibration, red-team review focused on provenance bypass, and independent reproduction from a tagged fixture set.
- `Failure modes`: Missing instrumentation, spoofed writer identity, stale policy, unsigned legacy state, gateway bypass, overblocking, alert fatigue, and unsupported inference from incomplete traces.
- `Maintenance plan`: Rotate signing keys, version schemas/policies, migrate or quarantine legacy state, re-evaluate after model/tool/runtime updates, and audit ledger access.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Defense effectiveness across architectural layers: a mechanistic evaluation of persistent memory attacks on stateful LLM agents | Primary paper | **Expanded in this pass:** v4 methods, factorial results, defense-layer mechanisms, validity criteria, frontier evaluation, limitations, ethics, and appendices were inspected. | https://arxiv.org/abs/2605.08442; https://arxiv.org/html/2605.08442; https://doi.org/10.48550/arXiv.2605.08442 |
| Stateful Agent Security Evaluation | Official implementation repository | **New in this pass:** repository README, source/config/data/results/tests inventory, reproduction requirements, MIT license, and no-release status were inspected; code was not executed. | https://github.com/junwenleong/stateful-agent-security-eval |
| Forensic Trajectory Signatures for Agent Memory Poisoning Detection | Companion primary paper | **Rechecked in this pass:** public v1 remains the prior trace-detection source and exposes the true-benign-baseline limitation that conflicts with the selected paper's later discussion. | https://arxiv.org/abs/2606.30566; https://arxiv.org/html/2606.30566; https://doi.org/10.48550/arXiv.2606.30566 |
| Memory Forensics - DEP-E | Prior same-family artifact | Preserved baseline for the earlier expansion of the companion trace-detection paper. | Black-Lake/.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md |
| Selected source DEP finding | Repository research artifact | Preserves the ten-source discovery bundle and the original relationship among memory, execution control, and agent security. | Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/daily_research_findings_2026-07-01_0103.md |
| From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes | Unexpanded neighboring primary source | Preserved from the prior manuscript as the remaining execution-authorization thread; not full-text reviewed in this pass. | https://arxiv.org/abs/2606.29073 |
| MemLineage: Lineage-guided enforcement for LLM agent memory | Related defense source discovered in selected paper | **New discovery in this pass:** provenance-bearing memory enforcement named as a related formal defense; not independently full-text reviewed. | https://arxiv.org/abs/2605.14421 |
| Certified defence against runtime memory poisoning in persistent LLM agent systems | Related defense source discovered in selected paper | **New discovery in this pass:** certified robustness direction named by the selected paper; not independently full-text reviewed. | https://arxiv.org/abs/2606.12703 |
| Trojan Hippo: Weaponizing agent memory for data exfiltration | Related adaptive-attack source discovered in selected paper | **New discovery in this pass:** adaptive comparison used by the paper to bound its fixed-framing results; not independently full-text reviewed. | https://arxiv.org/abs/2605.01970 |
| AgentDojo: A dynamic environment to evaluate attacks and defenses for LLM agents | Related benchmark | Prior single-session agent-security benchmark used by the selected paper to distinguish persistent-memory evaluation. | https://arxiv.org/abs/2406.13352 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/README.md | Selected DEP identity, inventory, summary, and original attribution. | 2026-07-18 | Repository file inspected. |
| R2 | Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/daily_research_findings_2026-07-01_0103.md | Ten-item source bundle, original companion-paper finding, and neighboring execution-control source. | 2026-07-18 | Repository file inspected. |
| R3 | Black-Lake-Data/.reports/BL-DEP-20260701-Tech Intel 0103-20260711/README.md | Prior selection record, supporting-document selection, source limits, and output linkage. | 2026-07-18 | Older than the eligibility cutoff; inspected before expansion. |
| R4 | Black-Lake-Data/.lake-data/DEP-20260701-Tech Intel 0103/BL-DEP-Mark001 Report-Mark.md | Exact prior Related Research and Reading and Source References sections. | 2026-07-18 | Latest prior Report-Mark inspected. |
| R5 | Black-Lake/.logs/20260711-DEP-20260701-Tech Intel 0103-LOG.md | Latest same-family log, prior questions/challenges, and evidence limits. | 2026-07-18 | Older than the cutoff; inspected. |
| R6 | Black-Lake/.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/README.md | Prior DEP manifest and attribution. | 2026-07-18 | Inspected. |
| R7 | Black-Lake/.lake-data/DEP-E/DEP-E-20260711-Agent Memory Forensics/memory-forensics.md | Prior full manuscript and two-item unexpanded primary/near-primary pool. | 2026-07-18 | Full artifact inspected. |
| R8 | Black-Lake/.logs/20260709-Arxiv-2D-RC-OTFS-LOG.md | Earlier cross-DEP reference involving the selected source DEP. | 2026-07-18 | Context only; inspected. |
| R9 | Black-Lake/.lake-data/DEP-E/DEP-E-20260709-2D-RC OTFS/2d_rc_otfs_manuscript.md | Earlier cross-DEP context and source linkage. | 2026-07-18 | Full artifact inspected; not evidence for memory-defense claims. |
| R10 | https://arxiv.org/abs/2605.08442 | Primary title, author, v4 revision, abstract claims, DOI, code link, subjects, and license. | 2026-07-18 | Canonical arXiv record. |
| R11 | https://arxiv.org/html/2605.08442 | Full method, results, statistics, defense mechanisms, frontier evaluation, limitations, ethics, code availability, references, and appendices. | 2026-07-18 | Primary full text inspected; some formulas/intervals omitted by HTML extraction. |
| R12 | https://doi.org/10.48550/arXiv.2605.08442 | Persistent identifier for the selected primary paper. | 2026-07-18 | Referenced from canonical arXiv metadata. |
| R13 | https://github.com/junwenleong/stateful-agent-security-eval | Official repository README, visible inventory, requirements, tests/config/results presence, MIT license, and release status. | 2026-07-18 | Repository overview inspected; code and logs not executed; exact commit pin unavailable from inspected page. |
| R14 | https://arxiv.org/abs/2606.30566 | Companion v1 metadata, abstract metrics, version status, DOI, and explicit companion link. | 2026-07-18 | Canonical public v1 rechecked. |
| R15 | https://arxiv.org/html/2606.30566 | Companion v1 method, 19 features, result tables, negative-class definition, and no-true-benign-baseline boundary. | 2026-07-18 | Full public v1 re-inspected for the version conflict. |
| R16 | https://doi.org/10.48550/arXiv.2606.30566 | Persistent identifier for the companion paper. | 2026-07-18 | Referenced from canonical arXiv metadata. |
| R17 | https://arxiv.org/abs/2605.14421 | MemLineage locator. | 2026-07-18 | Discovery-only related source; full text not reviewed. **New in this pass.** |
| R18 | https://arxiv.org/abs/2606.12703 | Certified memory-defense locator. | 2026-07-18 | Discovery-only related source; full text not reviewed. **New in this pass.** |
| R19 | https://arxiv.org/abs/2605.01970 | Trojan Hippo locator. | 2026-07-18 | Discovery-only related source; full text not reviewed. **New in this pass.** |
| R20 | https://arxiv.org/abs/2406.13352 | AgentDojo canonical arXiv locator. | 2026-07-18 | Related benchmark locator; not full-text reviewed in this pass. |
| R21 | Black-Lake/README.md | Root DEP class, README, attribution, log, and commit rules. | 2026-07-18 | Live default-branch authority inspected after fetch. |
| R22 | Black-Lake/.lake-data/README.md | DEP-E placement and publication-index maintenance rules. | 2026-07-18 | Live default-branch authority inspected after fetch. |
| R23 | Black-Lake-Data/README.md | Source DEP, report, and attribution expectations. | 2026-07-18 | Live default-branch authority inspected after fetch. |

## Appendix

### Random Selection and Iteration Record

- Automation: Black-Lake Data Processing & Review 0900.
- Automation family: Black-Lake Data Processing & Review; Black-Lake Data Processing & Review 0900.
- Public run timestamp: 2026-07-18T00:04:42Z.
- Eligibility cutoff: 2026-07-17T00:04:42Z.
- Canonical source DEP candidates: 60.
- Same-family marker files checked: 44.
- Excluded inside the 24-hour window: 0.
- Eligible source DEPs: 60.
- Source DEP selection method: PowerShell `Get-Random` over sorted eligible canonical directory names.
- Selected source DEP: DEP-20260701-Tech Intel 0103.
- Prior same-family material: 2026-07-11 report, Report-Mark, log, DEP README, and full manuscript; all older than the cutoff.
- Expansion pool: two unexpanded primary or near-primary items preserved by the prior manuscript.
- Expansion method: PowerShell `Get-Random` over the sorted two-item pool.
- Selected expansion: arXiv:2605.08442, *Defense effectiveness across architectural layers: a mechanistic evaluation of persistent memory attacks on stateful LLM agents*.
- Accessibility: canonical arXiv metadata, complete experimental HTML, and the public official repository overview/README were accessible; no redraw was required.
- Source files collected: none.

### Source Inventory and Reproducibility Boundary

- Repository-relative Markdown inspected: selected DEP README and findings; prior report; prior Report-Mark; latest same-family log; prior Memory Forensics README/manuscript; earlier 2D-RC log/manuscript; repository authority READMEs.
- Public sources inspected: selected arXiv v4 metadata/full HTML, companion arXiv v1 metadata/full HTML, and official GitHub repository overview/README.
- Not collected or executed: PDFs, TeX sources, Git repository clone, experiment configs, raw logs, datasets, model weights, hosted endpoints, tests, or analysis scripts.
- Exact GitHub commit pin: not available from the inspected public page; no SHA was invented.
- Independent reproduction: not performed.

### Evidence Conflict Register

- Selected paper v4 states that true-benign memory-grounded behavior has mean trajectory scores close to malicious behavior and can create 95-100% false positives for some models.
- Public companion paper v1 states that its negative class is poisoned-but-defended sessions and contains no true-benign baseline.
- This artifact treats the mismatch as unresolved versioned evidence. A follow-on reviewer should locate a tagged dataset or companion revision before using the later figures operationally.

### Validation Checklist

- YAML title and H1 are identical, 29 characters, and include the DEP class identifier.
- All required manuscript headings are present in schema order.
- Evidence ledger and claim table separate source claims, reviewer interpretation, and unresolved conflict.
- Every evidence-ledger source is represented in Source References.
- Three Ways to Exercise This Research contains exactly three safe, bounded paths.
- Example MVP Product contains all required minimum fields and additional failure/maintenance fields.
- Related Research and Reading clearly marks new, rechecked, preserved, and discovery-only items.
- Public provenance uses repository-relative paths, public URLs, date-only values, and UTC-only timestamps.
- No external source payload was collected or deposited.
