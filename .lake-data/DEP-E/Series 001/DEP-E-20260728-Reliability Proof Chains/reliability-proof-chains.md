---
title: "Reliability Proof Chains - DEP-E"
artifact_type: "DEP research artifact"
source_dep: "Black-Lake-Data/.lake-data/DEP-20260702-Tech Intel 1102"
source_repository: "https://github.com/Delphoa-Labs/Black-Lake-Data"
output_repository: "https://github.com/Delphoa/Black-Lake"
generated_at: "2026-07-28T00:03:23Z"
source_access_date: "2026-07-28"
temporal_cutoff: "2026-07-28"
review_status: "source-first review complete; independent reproduction not performed"
expansion_source: "Chai, arXiv:2606.26933"
---

# Reliability Proof Chains - DEP-E

## Source Metadata

- **Primary source package:** `Black-Lake-Data/.lake-data/DEP-20260702-Tech Intel 1102`
- **Primary source files inspected:** `README.md`; `daily_research_findings_2026-07-02_1102.md`
- **Primary source snapshot:** [Black-Lake-Data source DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260702-Tech%20Intel%201102)
- **Source package role:** discovery record and preliminary synthesis for ten research papers.
- **Canonical works reviewed:** ProtoPilot, ACE, AxDafny, Antaeus, KidnapRAG, Xiaomi-GUI-0, FARS, MARS, Evo-PI, and the global transverse-field Ising universality paper.
- **New supporting work reviewed:** Chai.
- **Prior Black-Lake context inspected:** [BEAGLE Learner](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260710-BEAGLE%20Learner) and [SAILFISH Vetting](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-SAILFISH%20Vetting).
- **Access date:** 2026-07-28.
- **Version note:** canonical arXiv records and the fullest accessible primary paper representations were used. Several records have revisions newer than the source package's preliminary capture, so current-version facts are tied to their canonical records.
- **Collection status:** no external source file is deposited with this artifact. Public paper records, full-paper HTML where available, one full paper PDF for Chai, and one full paper PDF for Xiaomi-GUI-0 were inspected. Repository code was not executed.

## Evidence Ledger

| ID | Source and locator | Evidence inspected | Source claim or observation | Reviewer assessment | Limits |
|---|---|---|---|---|---|
| E1 | [ProtoPilot, arXiv:2606.31763](https://arxiv.org/abs/2606.31763) | Canonical record and full paper | Converts natural-language experimental objectives into executable protocols; current revision reports 294 tasks from 98 protocols, an 89.5% overall protocol-to-code gate-pass rate, and four wet-lab workflows with confirmed products. | Strong example of staged translation plus executable and physical validation. | Task set, instruments, and assays remain bounded; dry-wet iteration is future work. |
| E2 | [ACE, arXiv:2606.31564](https://arxiv.org/abs/2606.31564) | Canonical record and full paper | Assigns each trajectory step to raw retention, abstraction, or removal while preserving lossless recoverability; reports gains on several long-horizon agent benchmarks. | Preserving reversible state is a reliability mechanism because later reviewers can recover details that an abstraction omitted. | Gains are not uniform across every metric; orchestration and model calls add cost. |
| E3 | [AxDafny, arXiv:2606.32007](https://arxiv.org/abs/2606.32007) | Canonical record and full paper | Uses verifier feedback to repair Dafny code and proofs; reports 725/782 on DafnyBench and 56.4% on the 250-task LCB-Pro-Dafny benchmark. | Executable proof checking creates a stronger gate than model self-assessment, while benchmark curation still needs human review. | Formal verification proves encoded properties, not all runtime, deployment, or specification properties. |
| E4 | [Antaeus, arXiv:2607.01138](https://arxiv.org/abs/2607.01138) | Canonical record and full paper | Stages repository prioritization, local context augmentation, structured sink/safety-condition reasoning, and comparative peer validation; detects and explains 15 logic vulnerabilities across 28 repositories. | Separating candidate generation from comparative validation reduces dependence on a single agent pass. | Evaluated only on selected C/C++ logic-vulnerability classes; no official code locator was identified in the inspected primary record. |
| E5 | [KidnapRAG, arXiv:2607.00422](https://arxiv.org/abs/2607.00422) and [official code](https://github.com/chanwoochoi316/KidnapRAG) | Canonical record, full paper, and official repository surface | A black-box Bait, Chain-Link, and Mal-Instruction sequence can drag reasoning through retrievable malicious documents in ReAct and WebThinker settings. | Reliability gates must verify provenance and instruction authority before retrieved text is admitted into the reasoning state. | The attack assumes exposed retrieval/reasoning signals and the ability to publish retrievable documents; experimental scope does not establish universal attack success. |
| E6 | [Xiaomi-GUI-0, arXiv:2606.31410](https://arxiv.org/abs/2606.31410) and [project page](https://seerray-lab.github.io/Xiaomi-GUI-0/) | Canonical record and visually inspected 40-page paper | Combines real-device closed-loop data, error-driven refinement, supervised training, step-level reinforcement learning, and agentic reinforcement learning; reports 72.0% success on 100 RealMobile tasks and 78.9 on AndroidWorld. | Real-device replay and explicit stops before consequential transactions are important gates, but average task success is not a complete safety measure. | RealMobile is in-house, live applications drift, and some comparisons rely on proprietary systems. |
| E7 | [FARS, arXiv:2606.31651](https://arxiv.org/abs/2606.31651) | Canonical record and full paper | Reports 166 generated papers across 67 topics, 417 agent hours, 21.6 billion tokens, and roughly USD 186,000 total cost; reviews show substantial integrity and quality failures. | Scale and throughput do not substitute for evidence quality. Multi-reviewer disagreement and integrity flags should block automatic release. | The study evaluates one autonomous research setup and its review process; quality measures remain partly judgment-based. |
| E8 | [MARS, arXiv:2606.31876](https://arxiv.org/abs/2606.31876) | Canonical record and full paper | Transfers text-derived refusal directions to multimodal models, uses neutral-image recentering, a ReLU gate, adaptive trust regions, and layer selection; reports large refusal improvements on video jailbreaks. | Internal activation interventions require utility, over-refusal, and distribution-shift gates in addition to safety averages. | Assumes a usable refusal direction; centering is a linear approximation; residual over-refusal remains. |
| E9 | [Evo-PI, arXiv:2606.31800](https://arxiv.org/abs/2606.31800) and [official code](https://github.com/zhengxianda/Evo_PI) | Canonical record, full paper, and official repository surface | Evolves a principle bank using a frozen judge and reinforcement learning for medical visual question answering; reports gains across eight benchmarks and several backbones. | The evolving principles are inspectable intermediates, but a frozen judge can propagate its own blind spots. | Judge quality, compute overhead, rare medical conditions, and non-clinical evaluation limit deployment claims. |
| E10 | [Werner, arXiv:2607.01227](https://arxiv.org/abs/2607.01227) | Canonical record and full paper | Constructively relates a gate-model computation to a global, nonmonotonic, time-dependent transverse-field Ising evolution with polynomial overhead. | A constructive reduction is itself a proof chain: assumptions and transformations are explicit enough to inspect. | Polynomial exponents are impractically large; the nonmonotonic schedule may not be available on all hardware; classical hardness is conditional. |
| E11 | [Chai, arXiv:2606.26933](https://arxiv.org/abs/2606.26933) | Canonical record and full 17-page paper | Differentially tests equivalent X.509, JWT, and SAML objects across 47 libraries in eight languages, then uses agents for discrepancy interpretation and downstream impact analysis. | **New in this pass.** Chai turns independent implementations into comparative oracles and makes disagreement a trigger for targeted investigation. | Coverage is empirical rather than exhaustive; each library needed two to five hours of manual preparation; downstream exploitability still needs confirmation. |
| E12 | Source DEP files | README and findings document | Provides the original ten-paper inventory, preliminary summaries, and early cross-paper interpretations. | Useful discovery and provenance layer, but revised canonical records control when facts differ. | Not a substitute for primary-paper inspection. |
| E13 | Prior Black-Lake artifacts | BEAGLE Learner and SAILFISH Vetting manuscripts, READMEs, and logs | Prior passes developed simulation and security-vetting threads connected to the selected source DEP. | Establishes continuity and supplies the candidate pool from which Chai was randomly selected for expansion. | These are reviewer artifacts, not primary evidence for the eleven papers. |

## Executive Summary

The reviewed evidence supports a practical thesis: trustworthy agentic systems need proof chains, not merely better prompts or stronger base models. A proof chain is a sequence of evidence-bearing transformations in which each important intermediate state is preserved, checked by a validator with a distinct failure mode, and linked to the decision it supports. The validator may be a formal verifier, a deterministic differential test, a real-device replay, a wet-lab gate, a peer agent, a human reviewer, or an explicit safety stop. What matters is that the gate produces inspectable evidence rather than another unsupported assertion.

The eleven papers do not collectively prove that one universal architecture solves reliability. They do show recurring mechanisms. ProtoPilot validates translated scientific procedures before and during execution. ACE preserves raw trajectory state behind abstractions. AxDafny closes the loop around a formal verifier. Antaeus separates repository triage from structured validation. KidnapRAG demonstrates that untrusted retrieved text can hijack multi-step reasoning. Xiaomi-GUI-0 uses real-device feedback and refuses to cross consequential transaction boundaries. FARS demonstrates that large autonomous output can still fail integrity review. MARS adds activation-level safety gates but retains over-refusal risk. Evo-PI externalizes evolving principles while remaining dependent on judge quality. The Ising construction makes assumptions and transformations explicit. Chai, newly expanded here, uses independent implementations as comparative oracles and carries discrepancies into downstream audits.

The main reviewer inference is that these mechanisms should be composed into an evidence graph. Claims should identify their source artifacts, transformations, validators, rejected alternatives, uncertainty, and release decision. An agent should not be able to erase an inconvenient intermediate result, silently replace raw evidence with a summary, or promote a discrepancy into a vulnerability claim without a separate impact check. A modest evidence-gate ledger can implement this pattern without pretending to deliver mathematical proof for every domain.

## Detailed Summary

### From fluent output to inspectable state

Agent pipelines often compress their history into prose. ACE shows a more disciplined alternative: route each trajectory step into raw retention, abstraction, or removal while keeping the process reversible. The reported GAIA improvements—38.8 to 42.4 with GPT-4.1 and 46.1 to 52.7 with Gemini—support the narrower claim that active context management can improve long-horizon performance in the evaluated settings. They do not establish that every metric improves, and they do not remove the cost of maintaining and querying a richer memory hierarchy.

ProtoPilot and Evo-PI also externalize important intermediate state. ProtoPilot represents protocol steps, resolves missing information, and subjects outputs to rule-based, reviewer, simulation, and physical gates. Evo-PI maintains a principle bank that changes over training rather than leaving the entire decision policy latent. In both cases the artifact between input and action is available for inspection. The reliability opportunity is to preserve those intermediates with versions and explicit validator outcomes.

### Independent gates and executable checks

AxDafny provides the clearest executable gate. Candidate repairs are checked by Dafny's verifier, so a model cannot certify its own proof. The 92.7% DafnyBench result and 56.4% LCB-Pro-Dafny result indicate strong performance in the tested environments, but the meaning of success is bounded by the specification. A verified implementation can still satisfy the wrong property or fail in an unmodeled deployment condition.

Chai uses a different form of executable independence. Its mutation program builds semantically equivalent security objects, serializes the same bytes, and supplies them to multiple independently maintained libraries. A discrepancy is deterministic evidence of inconsistent behavior. Agents then interpret the discrepancy and search reverse dependencies to evaluate downstream consequences. In X.509 testing, Chai reports 147 differentials from 1,500 certificates at USD 52.5, compared with 73 from roughly 500,000 certificates at approximately USD 560 for MLCerts. These are source-reported experimental comparisons, not independent cost audits; CPU fuzzing cost is excluded from the cited comparison.

Antaeus adds another variant: a staged security workflow that prioritizes repositories, augments local context, frames candidate issues around sinks and safety conditions, and uses comparative peer validation. Chai and Antaeus therefore complement one another. Chai creates deterministic cross-implementation discrepancies; Antaeus structures repository-specific reasoning and peer comparison. Neither paper establishes that an agent's initial security finding is automatically exploitable.

### Trust boundaries and adversarial evidence

KidnapRAG is a direct warning against treating retrieved content as evidence merely because a search system returned it. The Bait, Chain-Link, and Mal-Instruction sequence is designed to pull a reasoning agent through a chain of attacker-controlled documents. The evaluated attack requires observable retrieval or reasoning cues and the ability to publish content that can be retrieved. Within that scope, it demonstrates that provenance is not a cosmetic citation field: it is an execution boundary.

A proof-chain system should therefore label every artifact with origin, authority, acquisition method, and permitted role. Retrieved prose may inform a hypothesis, but it should not acquire the authority to modify tool policy or approve an action. Independent retrieval, canonical-record checks, content hashing, and instruction/data separation can reduce the chance that a poisoned document becomes an implicit controller.

### Embodied, scientific, and safety validation

Xiaomi-GUI-0 and ProtoPilot operate closer to physical consequences. Xiaomi-GUI-0 trains and evaluates a mobile agent using real devices, sandboxes, and an error-driven data flywheel. Its RealMobile benchmark contains 100 tasks across 14 live applications, with 57% requiring multiple applications. The reported 72.0% success and 85.8% progress are useful capability measures, while the paper's decision to stop before real transactions is a separate safety constraint. The weakest category results—43.8% for Safety and Reflection and 66.7% for Memory—also caution against using the average as the release gate.

ProtoPilot reports 294 tasks derived from 98 protocols, an 89.5% overall protocol-to-code gate-pass rate, and four wet-lab workflows with confirmed products. Physical confirmation strengthens the evidence chain, but four workflows cannot establish general laboratory reliability.

MARS intervenes in model activations rather than task planning. Its text-derived refusal direction, neutral-image recentering, ReLU gate, adaptive trust region, and layer selection improve refusal rates in the tested multimodal settings; the paper reports video-jailbreak refusal improvements of 59.4 percentage points for Qwen3-VL, 52 for Qwen3.5, and 40.4 for Molmo2. Those gains must be paired with utility and over-refusal checks because a system that refuses safe work is not reliably aligned with user intent.

### Scale, review, and the danger of aggregate success

FARS is the strongest counterexample to equating scale with validity. The system produced 166 papers across 67 topics using 417 agent hours, 21.6 billion tokens, and roughly USD 186,000. Yet 16.7% of reviews raised formal integrity flags, and 44% of papers with free-text reviews had at least one integrity failure. Only two of 95 papers with at least two reviewers reached the highest review level. The source evidence indicates that throughput can increase faster than trustworthy evaluation capacity.

This reinforces a cross-paper rule: release gates should examine distributions, disagreement, and failure classes, not only averages. Xiaomi-GUI-0's category spread, ACE's nonuniform metrics, FARS's reviewer disagreement, and Chai's distinction between library discrepancy and downstream impact all show why a single aggregate score is insufficient.

### Constructive transformations as audit trails

Werner's transverse-field Ising result belongs to a different technical domain, but its methodological relevance is direct. The paper constructs a polynomial equivalence between a gate-model computation and a globally controlled, nonmonotonic transverse-field Ising evolution. Each assumption and transformation can be audited. The result remains subject to impractically large polynomial exponents, conditional hardness assumptions, and hardware constraints. This is a useful model for honest proof chains: explicit transformation does not erase feasibility limits.

## Key Claims and Evidence

1. **Claim: preservation of raw intermediate state improves auditability.**
   - **Source evidence:** ACE retains recoverable raw trajectory steps behind abstractions; ProtoPilot, Evo-PI, and the Ising construction externalize important intermediate representations.
   - **Reviewer interpretation:** a later validator cannot challenge evidence that has been irreversibly summarized away.
   - **Boundary:** the sources do not provide a universal cost-optimal retention policy.

2. **Claim: validators should fail differently from the generators they check.**
   - **Source evidence:** AxDafny uses a formal verifier; Chai compares independent libraries; ProtoPilot uses rule, reviewer, simulation, and physical checks; Antaeus uses comparative peer validation.
   - **Reviewer interpretation:** independence reduces correlated self-approval, although shared specifications and shared training data can still correlate failures.
   - **Boundary:** independence is contextual and must be measured rather than assumed.

3. **Claim: provenance is an operational security control.**
   - **Source evidence:** KidnapRAG's attack relies on attacker-published retrievable documents that shape subsequent reasoning.
   - **Reviewer interpretation:** retrieval results require authority labels and instruction isolation before entering an agent's execution context.
   - **Boundary:** the tested attack assumptions do not establish success against every retrieval architecture.

4. **Claim: aggregate success metrics are insufficient release gates.**
   - **Source evidence:** FARS combines high throughput with integrity failures; Xiaomi-GUI-0 has substantial category variance; ACE's gains vary by metric; Chai separates detected discrepancies from confirmed impact.
   - **Reviewer interpretation:** releases should be blocked on critical failure classes and unresolved disagreement even when averages improve.
   - **Boundary:** thresholds are domain-specific and cannot be inferred from these papers alone.

5. **Claim: deterministic replay is a high-value bridge between agents and conventional testing.**
   - **Source evidence:** Chai deterministically constructs equivalent objects and reproduces cross-library divergence; AxDafny checks candidate repairs against an executable verifier; Xiaomi-GUI-0 uses real-device closed-loop feedback.
   - **Reviewer interpretation:** an agent is most useful when it can attach a replayable artifact to a hypothesis.
   - **Boundary:** deterministic reproduction of a discrepancy does not prove security severity or generality.

6. **Claim: safety gates require utility checks.**
   - **Source evidence:** MARS discusses residual safe over-refusal; Xiaomi-GUI-0 separates task success from safety/reflection; Evo-PI depends on a judge whose quality bounds the learned principles.
   - **Reviewer interpretation:** a system that blocks all actions can score well on a narrow harm metric while failing its intended purpose.
   - **Boundary:** the evidence does not define one cross-domain utility-safety frontier.

## Methodology

- **Review design:** source-first, qualitative comparative review with claim-level evidence tracking.
- **Primary evidence:** canonical arXiv records and full papers for the ten works in the source DEP plus Chai; official project or code surfaces for KidnapRAG, Xiaomi-GUI-0, and Evo-PI.
- **Secondary evidence:** the source DEP's README and findings document and the prior BEAGLE Learner and SAILFISH Vetting artifacts.
- **Selection method:** one eligible DEP was sampled from the sorted canonical source set using an operating-system cryptographic UInt32 and rejection sampling. Because prior output material referenced the selected DEP, four accessible related-source candidates were sorted and independently sampled by the same method; Chai was selected.
- **Extraction method:** bibliographic identity, method, benchmark scope, quantitative results, stated limitations, and evidence form were recorded. Claims were compared across the source package and current canonical paper versions.
- **Synthesis method:** mechanisms were grouped by their role in a reliability proof chain: state preservation, provenance, independent validation, deterministic replay, disagreement handling, and consequential-action gating.
- **Validation performed:** heading/schema checks, title-contract checks, source-reference checks, exact-section extraction checks, repository-rule checks, and public-output disclosure scans.
- **Validation not performed:** no code execution, benchmark reproduction, laboratory protocol execution, mobile-agent run, medical evaluation, vulnerability reproduction, library differential test, or quantum simulation.

## Scope, Constraints, and Assumptions

- **Scope:** agentic reliability mechanisms represented by eleven papers connected to one Black-Lake source DEP and its prior related artifacts.
- **Temporal boundary:** evidence available and inspected through 2026-07-28.
- **Evidence boundary:** source-reported results remain source claims unless explicitly labeled as reviewer interpretation or inference.
- **Repository boundary:** no external source payload is deposited; only the manuscript, companion metadata, index update, and run log are public artifacts.
- **Version assumption:** current canonical paper revisions control quantitative facts; any observed difference from a preliminary source record must be retained as provenance rather than silently normalized.
- **Independence assumption:** formal verifiers, independent libraries, peer agents, humans, devices, and physical experiments have distinct but not necessarily uncorrelated failure modes.
- **Generalization constraint:** results from bounded benchmarks, languages, libraries, applications, laboratory procedures, and hardware models do not establish universal performance.
- **Security constraint:** vulnerability discrepancies and attack demonstrations require contextual impact validation before production severity is assigned.
- **Clinical constraint:** Evo-PI is treated as research evidence, not clinical guidance or approval.
- **Cost constraint:** reported token, dollar, device, and compute costs are not normalized across papers.

## Observations

- The most credible workflows attach a machine-checkable or physically observable artifact to the agent's claim.
- Reversibility appears in multiple forms: ACE can recover raw steps, Chai can replay identical bytes, AxDafny can rerun a verifier, and ProtoPilot can trace a protocol step through gates.
- Validator diversity matters more than validator count. Three model judges trained on similar data may provide less independence than one deterministic checker.
- Revision drift is itself a provenance issue. Several papers were revised after the source DEP's initial capture, so the review records current canonical versions.
- The papers frequently report average performance while operational decisions depend on tails, disagreement, and critical failure categories.
- Chai's downstream audit is important because it prevents the first discrepancy from becoming an inflated security conclusion.
- KidnapRAG shifts provenance from documentation into the threat model: an unauthenticated document can act like an instruction channel.
- FARS reveals a scaling asymmetry: generation capacity can grow faster than reviewer capacity.

## Considerations

- Store rejected, superseded, and inconclusive outcomes, not only the evidence that supported release.
- Define gate ownership and override authority before deployment; otherwise an agent may route around a failing check.
- Separate semantic equivalence from byte equivalence and application impact when adopting Chai-like differential tests.
- Pin source versions and validator versions so that later metric changes can be explained.
- Track evaluator independence explicitly, including shared models, prompts, data, specifications, and institutional incentives.
- Design evidence retention around risk: lossless state for consequential decisions, bounded abstraction for routine work, and documented expiration for transient context.
- Treat official code availability as an inspectability signal, not as proof of reproducibility.
- Budget human review where disagreement or real-world consequence is highest rather than distributing it uniformly.

## Strengths

- The evidence set spans formal, deterministic, empirical, adversarial, physical, human-review, and theoretical validation.
- Multiple papers expose intermediate artifacts that can be integrated into a common evidence ledger.
- Chai provides a concrete, newly inspected pattern for converting independent implementations into comparative oracles.
- KidnapRAG supplies an adversarial counterweight to optimistic retrieval and memory designs.
- FARS makes evaluation failure visible at a scale large enough to challenge throughput-centered narratives.
- The synthesis preserves revision status, source limitations, and non-reproduced status instead of collapsing them into a single confidence score.

## Weaknesses

- No experiment or code path was independently reproduced.
- The papers use heterogeneous tasks and metrics, so cross-paper quantitative comparison would be misleading.
- Several evaluations depend on in-house benchmarks, proprietary models, costly infrastructure, or specialized hardware.
- Some primary records lack a clearly identified official implementation surface.
- The proposed proof-chain pattern is a reviewer synthesis, not a controlled comparison evaluated by the eleven papers.
- Validator independence is argued structurally but not measured with a shared experimental protocol.

## Potential Improvements

- Reproduce one bounded workflow from each validator class: formal, differential, device, human, and physical.
- Define a common evidence-envelope schema with artifact hashes, source authority, validator identity, uncertainty, and override history.
- Measure correlated failures by swapping generators and validators across model families and institutions.
- Add tail-risk and critical-category thresholds beside aggregate benchmark metrics.
- Evaluate the operational cost of lossless state retention and determine when reversible compression is worth its latency.
- Extend Chai-like differential testing from parser acceptance into semantic outputs, error handling, and downstream policy decisions.
- Add retrieval provenance checks and instruction/data isolation to long-horizon memory benchmarks.
- Require a reproducibility capsule for claims used in release decisions, while keeping nonredistributable source material outside the public artifact.

## Potential Implementations

- **Evidence-gate ledger:** append-only records linking claims to artifacts, validators, decisions, and overrides.
- **Differential validation service:** deterministic object builders that submit identical inputs to independent implementations and produce replay bundles.
- **Verifier adapter layer:** a common interface for formal checkers, test suites, schema validators, policy gates, and human approval.
- **Provenance firewall:** labels retrieved content by origin and prevents evidence text from becoming executable instruction authority.
- **Disagreement router:** escalates critical disagreement to an independent validator and retains all competing outputs.
- **Release scorecard:** reports average performance, tail performance, critical failures, abstentions, and unresolved evidence gaps separately.
- **Revision monitor:** detects changes to canonical sources and opens a review task when a cited metric or limitation changes.

## Three Ways to Exercise This Research

1. **Reproduce a deterministic gate.** Select two security libraries supported by Chai, pin versions, generate one semantically equivalent object, record identical serialized bytes, replay the case, and distinguish parser disagreement from downstream impact. Stop before exploit development unless separately authorized.
2. **Build a provenance-aware agent trace.** Run a bounded retrieval task in a sandbox, label each retrieved document by source and authority, block embedded instructions, preserve raw and abstracted memory, and compare the result with an unguarded trace.
3. **Audit a release decision.** Take one published benchmark table from the evidence set, reconstruct its aggregate and category-level gates, add explicit critical-failure thresholds, and document whether the release decision changes.

## Example MVP Product

- **Name:** ProofChain Ledger
- **Problem:** agent teams can produce plausible outputs without preserving enough evidence to reproduce, challenge, or safely approve them.
- **Primary users:** agent-platform engineers, security reviewers, research leads, and release managers.
- **Core workflow:** an agent submits a claim with source artifacts; the ledger records immutable provenance; one or more independent validators run; disagreements are routed for review; an authorized owner accepts, rejects, or defers the claim.
- **Minimum data model:** claim ID, artifact locator and digest, source authority, transformation history, validator and version, result, confidence or uncertainty, disagreement status, release decision, owner, and override reason.
- **Minimum gates:** source availability, artifact digest, instruction/data boundary check, domain validator, critical-failure check, and human approval for consequential actions.
- **User interface:** claim queue, evidence graph, replay action, validator comparison, unresolved-disagreement view, and release summary.
- **Success measures:** replay rate, provenance completeness, disagreement resolution time, critical false-approval rate, override frequency, and evidence-retention cost.
- **Security posture:** append-only audit history, least-privilege validators, untrusted-content isolation, signed decision records, and no automatic execution from retrieved prose.
- **Initial boundary:** one repository, Markdown and JSON evidence envelopes, two deterministic validators, and manual release approval.
- **Explicit non-goals:** universal truth scoring, automatic vulnerability severity assignment, clinical decision support, autonomous laboratory operation, or proof of every real-world property.
- **Evaluation plan:** seed known passing, failing, conflicting, stale, and poisoned evidence cases; verify deterministic replay; measure validator correlation; and require reviewers to recover the basis for every release decision.

## Related Research and Reading

- **New in this pass — Chai:** Corban Villa, Sohee Kim, Austin Chu, Alon Shakevsky, and Raluca Ada Popa, “Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities,” [arXiv:2606.26933](https://arxiv.org/abs/2606.26933). Chai supplies the expanded supporting thread: deterministic object construction, cross-library comparison, agent interpretation, reverse-dependency search, and targeted downstream audit. It is most useful here as an implementation pattern for an independent evidence gate, while its empirical coverage and manual preparation burden remain explicit limitations.
- **BEAGLE Learner:** the prior [BEAGLE Learner artifact](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260710-BEAGLE%20Learner) develops simulation-oriented learning and trajectory evidence connected to ACE. It motivates retaining raw execution histories for later validation.
- **SAILFISH Vetting:** the prior [SAILFISH Vetting artifact](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-SAILFISH%20Vetting) develops state-consistency and library-vetting concerns connected to Antaeus. Chai extends that thread with deterministic cross-library differentials.
- **KidnapRAG code:** the [official KidnapRAG repository](https://github.com/chanwoochoi316/KidnapRAG) exposes attack workflows for ReAct and WebThinker and can support a bounded provenance-firewall exercise without treating the repository as authority over local execution policy.
- **Xiaomi-GUI-0 project page:** the [official project page](https://seerray-lab.github.io/Xiaomi-GUI-0/) supplements the paper's description of real-device GUI-agent training and evaluation.
- **Evo-PI code:** the [official Evo-PI repository](https://github.com/zhengxianda/Evo_PI) provides an inspectable implementation surface for evolving principle banks; the code was not executed in this review.

## Source References

1. Yankai Jiang, Weiting Tang, Haoran Sun, et al. “A Self-Evolving Agentic System for Automated Generation and Execution of Biological Protocols.” [arXiv:2606.31763](https://arxiv.org/abs/2606.31763).
2. Ning Liao, Zihao Long, Xiaoxing Wang, et al. “ACE: Pluggable Adaptive Context Elasticizer across Agents.” [arXiv:2606.31564](https://arxiv.org/abs/2606.31564).
3. Benjamin Breen, Austin Letson, Borja Requena Pozo, and Leopoldo Sarra. “AxDafny: Agentic Verified Code Generation in Dafny.” [arXiv:2606.32007](https://arxiv.org/abs/2606.32007).
4. Michele Armillotta, Nicolò Romandini, Rebecca Montanari, and Lorenzo Cavallaro. “Antaeus: Hunting Repository-Level Logic Vulnerabilities via Context-Grounded LLM Reasoning.” [arXiv:2607.01138](https://arxiv.org/abs/2607.01138).
5. Chanwoo Choi, Euntae Kim, Kyuho Lee, et al. “KidnapRAG: A Black-Box Attack for Hijacking Reasoning in Agentic Retrieval-Augmented Generation Systems.” [arXiv:2607.00422](https://arxiv.org/abs/2607.00422).
6. Wanxia Cao, Chengzhen Duan, Pei Fu, et al. “Xiaomi-GUI-0 Technical Report.” [arXiv:2606.31410](https://arxiv.org/abs/2606.31410).
7. Qiong Tang, Tianxiang Sun, Xiangkun Hu, et al. “FARS: A Fully Automated Research System Deployed at Scale.” [arXiv:2606.31651](https://arxiv.org/abs/2606.31651).
8. Moreno D'Incà, Nicu Sebe, and Massimiliano Mancini. “Harnessing Textual Refusal Directions for Multimodal Safety.” [arXiv:2606.31876](https://arxiv.org/abs/2606.31876).
9. Xianda Zheng, Huan Gao, Meng-Fen Chiang, Michael Witbrock, Kaiqi Zhao, and Shangyang Li. “Evo-PI: Aligning Medical Reasoning via Evolving Principle-Guided Supervision.” [arXiv:2606.31800](https://arxiv.org/abs/2606.31800).
10. Matthias Werner. “Polynomial equivalence of the global transverse-field Ising model and the gate model of quantum computation.” [arXiv:2607.01227](https://arxiv.org/abs/2607.01227).
11. **New in this pass:** Corban Villa, Sohee Kim, Austin Chu, Alon Shakevsky, and Raluca Ada Popa. “Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities.” [arXiv:2606.26933](https://arxiv.org/abs/2606.26933).
12. Delphoa-Labs. [Black-Lake-Data source DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260702-Tech%20Intel%201102), accessed 2026-07-28.

## Appendix

### A. Selection Provenance

- Canonical source candidates: 85.
- Excluded by same-family markers within the 24-hour window: 2.
- Eligible candidates: 83.
- Eligibility cutoff: 2026-07-27T00:03:23Z.
- Sorted eligible-list SHA-256: `2fada5b3095f5f54325c39f4ae2a472d802e79b4f9f4d312752deb7a5b6203ec`.
- Accepted cryptographic UInt32: `1720101562`.
- Selected zero-based index: 17.
- Selected DEP: `DEP-20260702-Tech Intel 1102`.
- Recent exclusions: `DEP-20260702-Tech Intel 0103` and `DEP-20260713-Tech Intel 1301`.

### B. Expansion Selection Provenance

- Accessible related-source candidates: 4.
- Candidate-list SHA-256: `b8a29cd6a2a5154005ea375804a945a3ada1d0aa6920b58b76023e9005df9e6b`.
- Accepted cryptographic UInt32: `484186745`.
- Selected zero-based index: 1.
- Selected supporting source: Chai, arXiv:2606.26933.

### C. Reproduction Boundary

The review verifies public source identity, paper content, internal consistency, and artifact schema. It does not verify the papers' experimental results independently. No source payload is redistributed. A future reproduction should pin versions, preserve raw inputs and outputs, record resource usage, and distinguish successful replay from confirmation of the broader claim.
