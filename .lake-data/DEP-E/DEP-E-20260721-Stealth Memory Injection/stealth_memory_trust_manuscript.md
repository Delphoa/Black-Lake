---
title: "Stealth Memory Trust - DEP-E"
generated_at: "2026-07-21T00:00:00Z"
artifact_type: "DEP research artifact"
primary_subject: "A defensive, source-grounded review of stealthy cross-session memory injection in persistent personal agents."
source_status: "Complete PDF, full-paper HTML, abstract HTML, and source archive verified locally; source payloads withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-21"
temporal_cutoff: "2026-07-21"
primary_url: "https://arxiv.org/abs/2607.05189v1"
stable_identifier: "arXiv:2607.05189v1"
confidence_summary: "High for accurately reporting the complete paper; medium for generality because experiments were author-run, code and data were not publicly linked, and no results were independently reproduced."
safety_scope: "Defensive architecture, evaluation, provenance, authorization, monitoring, and incident response; operational attack payloads omitted"
distribution_notes: "No PDF, HTML, TeX source, extracted text, prompt payload, credential, private trace, or local path is redistributed."
---

# Stealth Memory Trust - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL | Access Date | Status |
|---|---|---|---|---|---|---|---|
| S1 | *When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents* | Primary paper metadata | arXiv abstract record | arXiv:2607.05189v1 | https://arxiv.org/abs/2607.05189v1 | 2026-07-21 | Inspected |
| S2 | Same paper | Complete primary paper | PDF, 25 pages | arXiv:2607.05189v1 | https://arxiv.org/pdf/2607.05189v1 | 2026-07-21 | Verified and inspected locally |
| S3 | Same paper | Structured full text | arXiv HTML | arXiv:2607.05189v1 | https://arxiv.org/html/2607.05189v1 | 2026-07-21 | Verified and inspected locally |
| S4 | Same paper | Source-level consistency check | arXiv source archive | arXiv:2607.05189v1 | https://arxiv.org/e-print/2607.05189v1 | 2026-07-21 | Verified and inspected locally |
| S5 | *Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses* | Related primary research | arXiv paper | arXiv:2607.05029v1 | https://arxiv.org/abs/2607.05029v1 | 2026-07-21 | Metadata and related DEP inspected |
| S6 | *Defense effectiveness across architectural layers: a mechanistic evaluation of persistent memory attacks on stateful LLM agents* | Related primary research | arXiv paper | arXiv:2605.08442 | https://arxiv.org/abs/2605.08442 | 2026-07-21 | Metadata and related DEP inspected |
| S7 | OpenClaw | Referenced agent runtime | Official GitHub repository | repository state at access time | https://github.com/openclaw/openclaw | 2026-07-21 | Public repository inspected; code not executed |
| S8 | Hermes Agent | Referenced agent runtime | Official GitHub repository | repository state at access time | https://github.com/NousResearch/hermes-agent | 2026-07-21 | Public repository inspected; code not executed |
| S9 | NanoClaw | Referenced agent runtime | Official GitHub repository | repository state at access time | https://github.com/qwibitai/nanoclaw | 2026-07-21 | Public repository inspected; code not executed |
| S10 | Black Lake repository rules and three related DEP records | Deposition and synthesis context | Repository Markdown | fetched `main` at review time | Repository-relative paths in this artifact | 2026-07-21 | Inspected |

The paper lists Yechao Zhang, Shiqian Zhao, Jiawen Zhang, Jie Zhang, Gelei Deng, Xiaogeng Liu, Chaowei Xiao, and Tianwei Zhang. It was submitted on 2026-07-06 in `cs.CR` with `cs.AI` cross-listing. The DOI is https://doi.org/10.48550/arXiv.2607.05189. The arXiv comments say "25 pages, 8 figures," while the complete document and source expose Figures 1 through 10; this metadata inconsistency is recorded rather than silently normalized.

## Evidence Ledger

| ID | Evidence | Supports | Confidence | Limits |
|---|---|---|---|---|
| E1 | S1-S4, complete version-matched source bundle | Identity, section coverage, equations, tables, figures, appendices, limitations, ethics, and disclosures | High for source reporting | The study is a preprint and was not independently replicated |
| E2 | Sections II-IV and Figures 1-2 | Cross-session threat model, WhisperBench construction, MemGhost proxy design, and training flow | Medium-high | Operational payload details are intentionally omitted from this artifact |
| E3 | Table I and associated discussion | Main model-specific injection, stealth, execution, and end-to-end rates | Medium-high | Author-run controlled cases; no confidence intervals or multi-seed uncertainty reported |
| E4 | Tables II-V | Runtime transfer, proxy correlation, defense evasion, and adaptive visibility results | Medium | Model endpoints, agent versions, rubrics, and evaluator behavior may change |
| E5 | Tables VI-VII and Appendices A-G | Hyperparameters, benchmark cases, scoring rubrics, examples, and implementation detail | Medium-high | No public code or dataset link was found on the paper record as of the access date |
| E6 | S5-S6 and related DEP records | Comparison with forged-reasoning attacks, layered defenses, provenance, and memory forensics | Medium | Conceptual relation does not establish empirical equivalence |
| E7 | S7-S9 | Existence and public framing of referenced agent runtimes | Medium-high | Runtime code and historical versions used by the paper were not audited or executed |
| E8 | Source-text consistency audit | Metric wording ambiguity, unfinished limitation sentence, grammar defect, and figure-count mismatch | High for textual observation | Editorial defects do not by themselves invalidate the experimental results |

## Executive Summary

The paper studies a persistent-agent security failure in which a single malicious email causes an agent to write attacker-influenced memory, suppress visible evidence of that write, and act on the retained state in a later session. The authors introduce WhisperBench, a 108-case benchmark spanning five risk categories, and MemGhost, an attacker-policy training method that replaces expensive end-to-end victim interaction with an environment proxy and an objective proxy. Fifty-two cases are used for training and 56 are held out for evaluation.

The central systems insight is stronger than a conventional prompt-injection observation. The harmful state transition can occur at ingestion, while the consequence appears only after the original conversation context has disappeared. A user who sees a normal email summary may therefore lack the evidence needed to understand why a later action changed. This creates a gap between content safety, memory integrity, interface transparency, and action authorization.

The paper reports high attack rates in several tested configurations. For example, in the held-out background setting, MemGhost reports 87.5% end-to-end success against GPT-5.4, 91.1% against Grok 4.1, and 75.0% against DeepSeek v4 Flash. Foreground interaction often reduces stealth or end-to-end success, but the effect varies sharply by model. On MiniMax M2.5, foreground injection remains 98.2% while stealth falls to 21.4%, illustrating why component metrics must be read together rather than reduced to injection alone.

The evidence supports a credible controlled vulnerability class, not a prevalence estimate for production systems. The benchmark uses simulated profiles and controlled mail infrastructure; results are endpoint-, model-, rubric-, and date-conditioned; query-based baselines use a 20-case subset while the principal methods use 56 held-out cases; and no main confidence intervals, independent seeds, real-user study, or public artifact link is presented. The paper also contains an ambiguity in how execution success is described, although the active equations and table values support an all-run interpretation.

The defensive conclusion is that persistent memory needs its own trust architecture. Untrusted messages should not acquire durable authority merely because a model summarized them. Every memory write should carry provenance, origin trust, policy scope, visibility, expiration, and review state. Retrieval and action should enforce those labels. High-impact actions should require corroboration independent of the memory that proposes them, and user-visible receipts should make durable state changes inspectable and reversible.

## Detailed Summary

### Threat Model

The attacker can send one email to a user whose personal agent reads mail and maintains persistent memory. The attacker does not need access to model weights, hidden prompts, or the memory database. The desired sequence is: induce a memory write during the malicious-email session, avoid an obvious user-facing indication, and later influence behavior when the relevant memory is retrieved. The paper distinguishes background processing, where the agent handles mail without immediate user dialogue, from foreground processing, where a user interacts with the agent and may receive more visible evidence.

This is a black-box and delayed-effect threat. The victim agent is evaluated through observable interactions, while the attack policy learns to produce email content that survives the full memory pipeline. This artifact intentionally omits the paper's concrete attack messages and any reusable construction recipe. The research value lies in the state-transition model and defensive measurements.

### WhisperBench

WhisperBench contains 108 cases divided across five risk categories and two broad memory types: facts and preferences. Each case defines an injection scenario and a later trigger scenario. The authors allocate 52 cases to training and 56 to held-out evaluation. They use a real IMAP/SMTP workflow through controlled mail infrastructure so the agent interacts through an authentic email skill rather than a simplified text-only function call.

The benchmark is useful because it separates four outcomes: injection success rate (ISR), stealth success rate (SSR), execution success rate (ESR), and end-to-end success rate (E2E). This decomposition exposes failure modes such as successful writing without later execution, or successful execution accompanied by obvious visible evidence. It also prevents a system from appearing secure merely because one stage happens to fail.

The benchmark remains synthetic and bounded. The profiles and accounts are simulated, the messages are controlled, and the evaluated horizon is short. It does not measure long-term memory decay, consolidation across weeks, multi-agent propagation, multi-tenant leakage, multimedia mail, or the effects of enterprise mail gateways and sender-authentication controls.

### MemGhost Mechanism

MemGhost trains an attacker policy without requiring every optimization step to invoke the target personal agent. An environment proxy estimates whether generated content will produce the intended memory-relevant behavior. An objective proxy estimates injection, stealth, and downstream trace objectives. The paper combines supervised fine-tuning with group-relative policy optimization (GRPO), using reward terms for successful injection, low visible disclosure, and trace evidence associated with later execution.

The formal optimization can be understood as constrained policy search. Given a benchmark case and a candidate message, the policy seeks a high expected task reward while retaining natural correspondence behavior and avoiding user-visible disclosure. The proxy objective decomposes that reward into measurable stage outcomes. This is not a proof that the proxy equals victim-agent behavior; the paper therefore reports correlations between proxy rewards and end metrics.

The reported proxy correlations are substantial: the injection reward and execution success have Pearson correlation 0.872; the stealth reward and stealth success have Pearson 0.785; and the trace reward and end-to-end success have Pearson 0.839. Rank and directional measures are also positive. These numbers support the proxies as useful optimization signals in the tested setting, but they do not establish calibration on unseen agent families or future model versions.

### Training Configuration

The attacker policy uses a Qwen 4B model. Supervised fine-tuning uses LoRA rank 16 with scaling 32 for three epochs, batch size 2, gradient accumulation 8, AdamW at learning rate `2e-4`, warmup ratio 0.1, and weight decay 0.01. Reinforcement learning increases LoRA rank to 64 with scaling 128, yielding about 132 million trainable parameters. The first curriculum stage runs for 30 iterations with AdamW at `5e-6`, KL coefficient 0.01, entropy coefficient 0.05, group size 8, sampling temperature 1.2, maximum completion length 2,048, hard-buffer size 50, and 30% replay.

DeepSeek-V3.2 is used in seed search and GPT-5.4-mini serves as a shadow agent. Query-based search baselines are allocated 50 iterations. These details are adequate to outline the training regime, but hardware, wall-clock cost, complete random-seed policy, and independently executable configuration are not available from a linked public repository.

### Main Results

Table I reports MemGhost against six victim-model configurations in background and foreground use. In background mode, end-to-end success is 87.5% for GPT-5.4, 71.4% for Claude Sonnet 4.6, 80.4% for Claude Sonnet 4.5, 78.6% for MiniMax M2.5, 91.1% for Grok 4.1, and 75.0% for DeepSeek v4 Flash. Foreground end-to-end success is 75.0%, 48.2%, 71.4%, 21.4%, 76.8%, and 42.9%, respectively.

The component rates matter. MiniMax M2.5 foreground mode reports 98.2% ISR but only 21.4% SSR and E2E, indicating that the agent often writes the state but exposes evidence. Claude Sonnet 4.6 has lower injection rates than several peers in both modes. These are comparative observations within the tested harness; they are not stable rankings of vendors or products.

Table II evaluates transfer across OpenClaw, NanoClaw, Hermes, and Mem0-backed variants using GPT-5.4. Background E2E ranges from 80.4% to 87.5%; foreground E2E ranges from 48.2% to 80.4%. The results support transfer across several memory implementations, although all rows share one underlying model family and the paper does not establish equivalence among runtime versions or default configurations.

Table IV reports high false-negative rates for several defenses in the tested setup: 91.59% for DataSentinel; 49.07% ISR and 98.15% SSR false-negative rates for Meta-SecAlign; and 93.46% for AgentDoG on OpenClaw versus 40.38% on the Claude Code SDK. These outcomes are useful stress tests, not universal measurements of those systems. Defender thresholds, versions, and deployment context determine practical performance.

Table V evaluates an adaptive visibility condition. Foreground end-to-end success drops to 23.2% for Claude Sonnet 4.6, 19.6% for Claude Sonnet 4.5, 3.6% for Hermes with GPT-5.4, and 1.8% for OpenClaw with GPT-5.4. This suggests that preserving or increasing user-visible evidence can materially disrupt a stealth objective. It does not prove that transparency alone prevents a memory write or later misuse.

### Metric and Baseline Qualification

The paper's source contains conflicting prose around execution success. One passage describes ESR as measured only among successful injections, while the active metric definition and reported table relationships are consistent with an all-run denominator. E2E is the intersection of injection, stealth, and execution. A replication should publish raw per-case outcomes and both conditional and unconditional rates to remove the ambiguity.

The query-based baselines are evaluated on a fixed 20-case subset, whereas MemGhost and handcrafted methods are evaluated on 56 held-out cases. Raw percentages therefore do not have identical sampling denominators. Fair comparison requires either evaluating every method on the same 56 cases or presenting paired results on the shared 20-case subset with uncertainty intervals.

### Reproducibility and Editorial Audit

The complete document includes seven tables and ten numbered figures. The arXiv comment states eight figures, which does not match the inspected v1 paper. The source also contains an unfinished sentence in the limitations section: "While our evaluation in this paper covers the authentic agent workflow, we do not xxx." A research-question sentence has a grammatical defect. These are editorial quality issues, not direct refutations of the experiments, but they reduce confidence that the v1 manuscript completed a final consistency pass.

No official code, benchmark, dataset, model checkpoint, or experiment repository was linked from the arXiv record or paper as of 2026-07-21. The authors state that the benchmark and dataset will be released. Experiments and source code were not rerun for this review.

## Key Claims and Evidence

| Claim | Direct evidence | Assessment | Boundary |
|---|---|---|---|
| One malicious email can create covert, persistent influence across sessions | End-to-end controlled workflow, held-out cases, Table I | Supported for the tested harness | Not a production prevalence estimate |
| MemGhost transfers across models and runtimes | Tables I-II | Supported across the listed configurations | Endpoint and version conditioned; one common model in runtime transfer table |
| Proxy rewards track victim outcomes | Table III correlations | Supported as association | Correlation is not proxy calibration or causal identification |
| Existing defenses miss many tested attacks | Table IV | Supported for reported configurations | Threshold, version, and implementation details limit generality |
| Foreground visibility can reduce stealth | Tables I and V | Supported, with large model-specific variation | Visibility does not necessarily prevent writing or retrieval |
| The benchmark captures persistent personal-agent risk | 108 cases, real mail protocol, delayed trigger design | Credible controlled benchmark | Synthetic users, short horizons, single-user text-email scope |

## Methodology

The review used the canonical arXiv v1 metadata, a complete 25-page PDF, full-paper HTML, and the source archive. File integrity and version alignment were checked before analysis. PDF text, HTML text, and source text were extracted into a private cache; the body, references, appendices, all seven tables, Figures 1-10, equations, ethics statement, and AI-use disclosure were inspected. Selected rendered pages were visually reviewed to verify architecture diagrams, benchmark flow, equations, tables, and examples.

Claims were classified as paper-reported evidence, direct textual observation, or reviewer inference. Numeric claims were checked against the tables rather than copied from the abstract. The analysis compared metric wording with equations and table relationships, examined baseline denominators, and separated transfer evidence from claims of universal robustness. External checks were limited to official arXiv records and official runtime repositories. No experiments, model calls, code, or attack procedures were executed.

For safety, this artifact excludes concrete malicious messages, optimization prompts, trigger phrases, and payload-construction instructions. Defensive controls are described at an architectural level that supports evaluation and mitigation without making exploitation easier.

## Scope, Constraints, and Assumptions

- Scope is arXiv:2607.05189v1 as deposited on 2026-07-06 and accessed on 2026-07-21.
- The review assumes the paper's reported infrastructure and endpoint identities are accurate; runtime versions were not reconstructed.
- Results are treated as author-reported controlled evidence, not independently verified performance.
- The study covers post-delivery text email in single-agent, single-user scenarios; it does not test mail-gateway controls, multimodal content, multi-agent spread, multi-tenancy, or long-horizon memory evolution.
- Hosted models and agent repositories can change after the reported experiments.
- The absence of a linked public repository is a time-bounded observation, not proof that private artifacts do not exist.
- Concrete offensive artifacts are outside the distribution boundary.

## Observations

1. The attack depends on a policy error: untrusted communication is allowed to become durable state with future behavioral authority.
2. Injection, stealth, and execution are separable. A defense that improves one metric may leave another failure mode intact.
3. Foreground interaction is not uniformly protective, but user-visible evidence is an important control surface.
4. Transfer across memory implementations suggests that the problem is broader than one storage backend.
5. Proxy correlation supports scalable red-team training, while also creating a need to validate proxy drift against real victim behavior.
6. The benchmark's authentic mail protocol improves systems realism, but simulated identities and short horizons leave organizational and longitudinal effects unresolved.
7. The paper's strongest numerical claims need uncertainty estimates and paired baselines before small differences can be interpreted.
8. Editorial inconsistencies are visible enough that a corrected version should publish explicit metric denominators and a machine-readable result table.

## Considerations

Persistent memory should be modeled as a typed security object. A memory record needs origin, signer or channel, extraction method, confidence, intended scope, visibility, expiration, sensitivity, and action authority. A natural-language statement alone is not sufficient evidence for a privileged state transition.

Memory write policy and action policy must be independent. Even if a system stores untrusted information for search or forensic value, it need not permit that record to authorize purchases, account changes, communication, code execution, or preference mutation. Quarantine and read-only retrieval offer a more useful response than indiscriminate deletion.

Transparency is necessary but not sufficient. A user-facing receipt should show what was retained, why, from which source, and what it can influence. High-impact updates should require confirmation through a channel independent of the content proposing the change. Incident response must preserve the original message, extraction trace, memory diff, retrieval events, tool calls, and revocation history.

Evaluation should report conditional and unconditional metrics, paired per-case outcomes, confidence intervals, model and runtime versions, endpoint dates, and clean-task utility. Defenses should be tested against adaptive attackers and benign distribution shifts, with explicit false-positive costs.

## Strengths

- Introduces a clear cross-session threat model that distinguishes storage, visibility, retrieval, and later execution.
- Uses a real mail protocol and persistent-agent workflow rather than a single-turn text proxy.
- Provides a 108-case benchmark with held-out evaluation and multiple risk categories.
- Reports stage-specific metrics and model-specific results rather than only aggregate attack success.
- Tests multiple victim models, agent runtimes, memory backends, defenses, and an adaptive visibility condition.
- Publishes substantial training and rubric detail in appendices.
- States controlled-environment, ethics, and AI-assistance boundaries.

## Weaknesses

- No public code, dataset, checkpoint, or executable configuration is linked in v1.
- Main results lack confidence intervals, independent training seeds, and external replication.
- Query-based baseline denominators differ from the principal 56-case evaluation.
- ESR wording is internally ambiguous between conditional and all-run definitions.
- Production controls such as mail gateways, sender authentication, organizational policy, and multi-tenant isolation are out of scope.
- The evaluation horizon is too short to characterize decay, consolidation, or repeated exposure.
- Editorial defects include an unfinished limitations sentence and a figure-count mismatch.
- Defense comparisons may be sensitive to thresholds, versions, and implementation choices that are not fully normalized.

## Potential Improvements

1. Release WhisperBench, exact splits, evaluator rubrics, endpoint snapshots, model checkpoints, and executable configurations under a clear license.
2. Evaluate all methods on the same held-out cases and publish paired outcome files, confidence intervals, and multiple training seeds.
3. Define ISR, SSR, ESR, and E2E with both equations and explicit denominators; report conditional and unconditional variants.
4. Add benign-memory and legitimate-preference-update controls to quantify false positives and user friction.
5. Extend evaluation to weeks-long memory evolution, consolidation, contradiction resolution, and revocation.
6. Test multi-agent, multi-user, multi-tenant, and multimodal propagation.
7. Evaluate upstream sender authentication, mail scanning, provenance signatures, memory quarantine, and action-level authorization together.
8. Freeze runtime and model versions in reproducible containers and archive complete, privacy-safe event traces.
9. Correct the unfinished limitation, grammar, and figure metadata in a revised manuscript.

## Potential Implementations

### Provenance-Bearing Memory Gateway

Place a deterministic gateway between content ingestion and durable memory. The gateway records source identity, channel authentication, extractor version, confidence, policy scope, expiration, and whether user confirmation occurred. Untrusted correspondence defaults to a quarantined evidence class with no action authority.

### Memory Diff Receipt

After every session, produce a compact, user-visible diff of proposed persistent changes. The receipt supports approve, restrict, expire, or reject operations. Approval is cryptographically bound to the exact normalized record so later rewriting cannot inherit prior consent.

### Independent Action Authorization

At tool invocation, calculate required capabilities and inspect every retrieved memory that influenced the plan. High-impact actions fail closed if their supporting state is untrusted, expired, contradicted, or outside scope. Confirmation must arrive through an independent UI or policy service rather than through the same email content.

### Forensic Memory Ledger

Use an append-only event ledger linking source message hash, extraction decision, memory record, retrieval events, model/runtime version, tool calls, and revocation. This supports incident reconstruction and enables defenders to measure whether a suspicious record actually influenced an action.

## Three Ways to Exercise This Research

1. **Reproduce the measurement model:** implement a harmless synthetic benchmark with paired benign and adversarially labeled messages, then report per-case ISR, SSR, ESR, and E2E under explicit denominators and uncertainty intervals.
2. **Test authority separation:** allow untrusted records to be searchable but deny them action authority; measure task utility, false positives, and whether later actions require independently verified evidence.
3. **Run a longitudinal revocation drill:** inject benign conflicting preferences into a test profile, exercise retrieval over several weeks of simulated sessions, and verify that receipts, expiration, contradiction handling, and revocation are complete and auditable.

## Example MVP Product

**Memory Trust Gateway** is a sidecar for personal-agent runtimes. It intercepts proposed memory writes and emits a signed record with provenance, scope, confidence, expiration, and authority. A policy engine assigns one of four states: rejected, quarantined/searchable, user-approved/read-only, or action-authorizing. A small review UI presents memory diffs and permits revocation. Tool calls receive an evidence bundle listing the memories that influenced the plan; sensitive actions require an independently confirmed record.

The MVP can be evaluated without offensive payloads. A test suite generates ordinary correspondence, contradictory updates, unauthenticated claims, and user-approved changes. Success criteria are zero unauthorized action-authorizing writes, complete provenance for every retained record, deterministic revocation, bounded false-positive cost, and an auditable link from each sensitive action to approved evidence.

## Related Research and Reading

1. [FARMA Reasoning Poison](../../DEP-A/DEP-A-20260717-FARMA%20Reasoning%20Poison/README.md) examines forged reasoning that enters agent memory and motivates provenance-aware quarantine before retained rationales can authorize behavior.
2. [Memory Defense Layers](../DEP-E-20260718-Memory%20Defense%20Layers/README.md) compares controls at input, retrieval, prompt, and tool layers and emphasizes that defense attribution requires pre-activation equivalence.
3. [Agent Memory Forensics](../DEP-E-20260711-Agent%20Memory%20Forensics/README.md) focuses on trajectory signatures and evidence needed to investigate persistent-memory poisoning.
4. The official [OpenClaw repository](https://github.com/openclaw/openclaw), [Hermes Agent repository](https://github.com/NousResearch/hermes-agent), and [NanoClaw repository](https://github.com/qwibitai/nanoclaw) provide current public context for three runtime families discussed by the paper; they do not by themselves reproduce the reported configurations.

## Source References

1. Yechao Zhang, Shiqian Zhao, Jiawen Zhang, Jie Zhang, Gelei Deng, Xiaogeng Liu, Chaowei Xiao, and Tianwei Zhang. *When Claws Remember but Do Not Tell: Stealthy Memory Injection in Persistent Personal Agents*. arXiv:2607.05189v1, 2026. https://arxiv.org/abs/2607.05189v1
2. Complete PDF for arXiv:2607.05189v1. https://arxiv.org/pdf/2607.05189v1
3. Full-paper HTML for arXiv:2607.05189v1. https://arxiv.org/html/2607.05189v1
4. DOI record. https://doi.org/10.48550/arXiv.2607.05189
5. Neeraj Karamchandani, Piyush Nagasubramaniam, Sencun Zhu, and Dinghao Wu. *Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses*. arXiv:2607.05029v1. https://arxiv.org/abs/2607.05029v1
6. *Defense effectiveness across architectural layers: a mechanistic evaluation of persistent memory attacks on stateful LLM agents*. arXiv:2605.08442. https://arxiv.org/abs/2605.08442

## Appendix

### Coverage Record

- Main sections I-VIII were inspected: introduction; system and threat model; WhisperBench; MemGhost; experiments; related work; limitations; conclusion.
- Appendices A-G were inspected, including benchmark details, hyperparameters, rubrics, examples, ethics, and AI-use disclosure.
- Tables I-VII were inspected. Their roles are main attack results, runtime transfer, proxy correlation, defense evasion, adaptive visibility, training details, and evaluation rubrics/examples.
- Figures 1-10 were inspected in the document/source inventory. They cover system architecture, benchmark and method flow, performance and training analyses, and qualitative examples.
- Central equations for the attacker objective, proxy objective, reward decomposition, supervised fine-tuning, entropy regularization, and GRPO were inspected.

### Integrity Record

- PDF SHA-256: `c40f26c2bc0513144e3d629a376f5ca849a5a1b762bc606c31a07fa89f6b9174`.
- Full-paper HTML SHA-256: `3cdc3c4ccf13ab0842b0c9a67bcc3180ec809a9994a4c8b20b9cc25e76dceb6b`.
- Abstract HTML SHA-256: `6bc8e256ffead499ed59b091eda25b3a4f52067de456dd51509d91975c6843f5`.
- Source archive SHA-256: `03d179cd53e813c6f90ad2d56b9a6b76b7f76405c433f5e0f750c197a65f49eb`.
- All four source artifacts remained local. No partial download markers were present.

### Evidence Conflicts and Open Questions

1. ESR prose alternates between a successful-injection condition and an all-run denominator; equations and active table relationships indicate all-run reporting.
2. The arXiv comment says eight figures, while the inspected document contains ten numbered figures.
3. The limitations source contains an unfinished `xxx` sentence.
4. It is unknown how results change under long-horizon consolidation, multiple attackers, organizational mail controls, multi-agent sharing, or stricter action authorization.
5. No public code or benchmark link was found as of 2026-07-21, so exact reproduction remains blocked.

### Validation Checklist

- Complete source gate: passed.
- Version alignment: passed for arXiv v1 metadata, PDF, HTML, and source.
- Full-paper coverage: passed.
- Defensive safety boundary: passed; no attack payload or construction procedure included.
- Exactly three exercise paths: passed.
- Exactly three related DEP entries: passed.
- Experiments rerun: no.
- Public source files uploaded: zero.
