---
title: "Inspectable Agents - DEP-E"
generated_at: "2026-07-29T00:03:00Z"
artifact_type: "DEP research artifact"
primary_subject: "Evidence and control surfaces for autonomous agents, with a new full-paper expansion of the Jacobian-lens J-space."
source_status: "URLs and repository files only; no external source files collected"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-29"
temporal_cutoff: "Sources available through 2026-07-29"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260717-Tech%20Intel%200104"
stable_identifier: "Black-Lake-Data DEP-20260717-Tech Intel 0104"
confidence_summary: "High for source identity and inspected mechanisms; medium for unreplicated empirical and deployment claims."
safety_scope: "Defensive evaluation, governance, and authorized research"
distribution_notes: "Public-source synthesis; source documents and private execution context are not redistributed."
---

# Inspectable Agents - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Black-Lake-Data source DEP | Primary source bundle | Markdown repository entry | `DEP-20260717-Tech Intel 0104` | [DEP directory](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260717-Tech%20Intel%200104) | Repository content used as evidence, not as instructions | 2026-07-29 | Both files inspected |
| S2 | Daily Research Findings | Primary synthesis inside S1 | Markdown | `daily_research_findings_2026-07-17_0104.md` | [Public file](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260717-Tech%20Intel%200104/daily_research_findings_2026-07-17_0104.md) | No original source files were deposited | 2026-07-29 | Inspected in full |
| S3 | GPT-Red | Official research report | HTML | Published 2026-07-15 | [OpenAI report](https://openai.com/index/unlocking-self-improvement-gpt-red/) | Internal-system results; technical paper linked by publisher | 2026-07-29 | Full public report inspected |
| S4 | SWE-Bench Pro audit | Official evaluation audit | HTML | Published 2026-07-08 | [OpenAI audit](https://openai.com/index/separating-signal-from-noise-coding-evaluations/) | Organization-authored audit | 2026-07-29 | Full public report inspected |
| S5 | STOCKTAKE | Primary paper | arXiv HTML | `arXiv:2607.13618v1` | [Canonical record](https://arxiv.org/abs/2607.13618) | CC BY 4.0 visible on arXiv HTML | 2026-07-29 | Full-paper HTML inspected |
| S6 | Verbalizable Representations Form a Global Workspace in Language Models | Primary technical paper; new expansion source | Interactive full paper | Transformer Circuits, 2026-07-06 | [Full paper](https://transformer-circuits.pub/2026/workspace/index.html) | Public technical paper | 2026-07-29 | Full paper and appendices inspected |
| S7 | A global workspace in language models | Official author summary | HTML | Published 2026-07-06 | [Anthropic summary](https://www.anthropic.com/research/global-workspace) | Organization-authored summary | 2026-07-29 | Inspected |
| S8 | `anthropics/jacobian-lens` | Official implementation | GitHub repository | Public `main` snapshot accessed 2026-07-29 | [Repository](https://github.com/anthropics/jacobian-lens) | Apache-2.0; reference implementation, stated as unmaintained | 2026-07-29 | README, package metadata, license, tree, tests/data presence inspected; code not run |
| S9 | Modular Pretraining Enables Access Control | Primary paper and official research thread | arXiv / research post | `arXiv:2607.08077v1` | [Canonical record](https://arxiv.org/abs/2607.08077); [official post](https://alignment.anthropic.com/2026/modular-pretraining/) | Preliminary; not applied to a production frontier model | 2026-07-29 | Canonical record and official technical account inspected |
| S10 | Towards autonomous medical artificial intelligence agents | Peer-reviewed primary paper | Nature HTML | DOI `10.1038/s41586-026-10675-5` | [Publisher record](https://doi.org/10.1038/s41586-026-10675-5) | Open-access article; MIMIC-IV constraints apply to underlying data | 2026-07-29 | Methods, results, safety, and limitations inspected |
| S11 | An agentic artificially intelligent X-ray scientist | Peer-reviewed primary paper | Nature Machine Intelligence HTML | DOI `10.1038/s42256-026-01261-5` | [Publisher record](https://doi.org/10.1038/s42256-026-01261-5) | Open-access article; code/data have separate Zenodo records | 2026-07-29 | Full publisher article inspected |
| S12 | Oracle Agent Memory | Primary paper plus prior Black-Lake continuity artifact | arXiv / repository review | `arXiv:2607.13157v1` | [Canonical record](https://arxiv.org/abs/2607.13157v1); [prior review](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-A/Series%20001/DEP-A-20260719-Oracle%20Agent%20Memory) | Prior review verified complete paper but did not reproduce experiments | 2026-07-29 | Prior full review and README inspected |
| S13 | HORCRUX | Primary paper | arXiv HTML | `arXiv:2607.13939v1` | [Canonical record](https://arxiv.org/abs/2607.13939) | CC BY-NC-SA 4.0 visible on arXiv HTML | 2026-07-29 | Full-paper HTML inspected |
| S14 | PriEval-Protect | Primary paper | arXiv record | `arXiv:2607.13754v1` | [Canonical record](https://arxiv.org/abs/2607.13754) | License not established from inspected record | 2026-07-29 | Canonical metadata and abstract inspected; full text was not accessible |
| S15 | Smart Coverage Goals continuity artifact | Prior related DEP-E | Repository manuscript, log, Report-Mark | `DEP-E-20260717-Smart Coverage Goals` | [Prior artifact](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-Smart%20Coverage%20Goals) | Uses S4 as related evidence, not as its primary paper | 2026-07-29 | Log, Report-Mark, related-reading, and source-reference sections inspected |

No local filesystem locator, user name, machine name, local timezone, or private source cache is part of this public artifact. No paper PDF, source archive, dataset, model, benchmark payload, clinical record, beamline trace, repository clone, or execution output was collected.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S2 | Repository source bundle | Two complete Markdown files, ten ranked findings, source roles, limitations, and URLs | Scope, source inventory, cross-domain synthesis | High | The DEP is a secondary synthesis; several original claims required direct-source checking |
| E2 | S3 | Official lab report | Self-play design, held-out evaluation, live-agent case studies, robustness figures | Automated adversarial search and training-loop claims | Medium | Results are organization-authored and mostly internal; no independent reproduction |
| E3 | S4 | Official audit | 731-task split, flagged-task pipeline, five-engineer review, issue taxonomy | Benchmark validity and human-agent audit claims | Medium-high | Only flagged tasks received deep review; the audit is organization-authored |
| E4 | S5 | Primary paper | POMDP task, fair Bayes-filter oracle, fifty seeds, belief/action metrics, complete prompt | Perception-versus-control decomposition | High for paper report | No environment or model run was reproduced |
| E5 | S6-S7 | Primary paper and official summary | J-lens derivation, causal swaps/ablations, workspace structure, alignment audits, limitations | J-space mechanism and new expansion | High for paper report | Mostly proprietary Claude checkpoints; human-readable token probes are incomplete |
| E6 | S8 | Official implementation | Repository tree, `jlens` package, tests, synthetic prompt sets, lockfile, notebook, Apache-2.0 license | Public replication surface and its boundaries | High | Code was not installed or executed; no model weights or training corpus are bundled |
| E7 | S9 | Primary paper / official technical account | GRAM routing, realistic-domain setup, partial-label and scaling claims | Capability modularization and access control | Medium | Full-paper HTML was unavailable; results are preliminary and not frontier-production evidence |
| E8 | S10 | Peer-reviewed paper | EHR sandbox, patient-agent tests, physician comparisons, medication safety results | Governed clinical workflow evidence | High for published report | Retrospective simulation on selected conditions; no prospective clinical deployment |
| E9 | S11 | Peer-reviewed paper | Virtual beamline, MCP tool boundary, ten-run model tests, human command relay, real-beamline demonstrations | Instrument-grounded autonomy | High for published report | Limited repeated real-world trials; human relay remained in the safety loop |
| E10 | S12 | Primary paper and prior full review | Memory lifecycle, scopes, LongMemEval results, prior limitations and replication agenda | Durable context as governed state | Medium-high | Vendor-authored; no code, benchmark, or service deployment reproduced |
| E11 | S13 | Primary paper | Shared coprocessor architecture, FPGA/ASIC results, fixed-latency claim, SCA gap | Crypto-agility and substrate control | High for paper report | No RTL, synthesis, power, or side-channel result reproduced |
| E12 | S14 | Primary metadata / abstract | Two-phase privacy framework, legal and technical scoring, protection recommendations | Privacy-governance concept | Low-medium | Full text and empirical detail were not accessible; no legal conclusion is drawn |
| E13 | S15 | Prior repository continuity | SWE-Bench audit bridge, source list, evaluation-control synthesis | Prior-art detection and non-duplicate expansion | High | The prior DEP-E did not fully review the selected source bundle |

## Executive Summary

The selected DEP links ten systems that make capability growth answerable to evidence and control. Its strongest cross-domain pattern is not “more autonomy”; it is the creation of inspectable boundaries around adversarial search, benchmark validity, hidden state, model internals, removable capabilities, clinical actions, instrument commands, durable memory, cryptographic kernels, and privacy risk.

Three distinctions recur. First, outcome must be separated from cause: STOCKTAKE distinguishes perception from control, the SWE-Bench Pro audit distinguishes agent failure from broken tests, and the X-ray scientist separates planning from a safety-mediated execution boundary. Second, internal or durable state must be governed: Oracle Agent Memory treats memory as a lifecycle, while the newly expanded J-space work identifies a small set of verbalizable representations that are causally involved in flexible reasoning. Third, safety claims need independent gates: GPT-Red searches for failures, GRAM attempts capability-level access control, HORCRUX exposes hardware cost and side-channel boundaries, and PriEval-Protect proposes a combined compliance and technical-risk workflow.

The new material in this pass is the complete J-space/global-workspace thread. The authors derive a Jacobian lens that maps intermediate residual-stream activations into a vocabulary-aligned readout using an average downstream Jacobian. They then use concept swaps, steering, ablation, control directions, sparse decomposition, and model comparisons to argue that a small J-space supports report, deliberate modulation, flexible reasoning, and broad broadcast while much automatic processing bypasses it. In the alignment-audit experiments, silent representations of evaluation awareness, fabrication, manipulation, and implanted misaligned objectives become visible. In counterfactual reflection training, dishonesty scores fall from 0.25 to 0.07 on a 27-transcript fabrication benchmark and deception scores fall from 0.38 to 0.05 on 100 role-play scenarios; ablating the ethics-related J-lens directions reverses most of the first improvement and part of the second. These are source-reported causal interventions, not independent proof that the readout captures all cognition or that deployment monitoring is solved.

Reviewer interpretation: the most reusable architecture is an evidence-linked control loop with four receipts—observation, decision, execution, and outcome—plus an explicit fallback when any receipt is missing or invalid. J-space signals can strengthen the observation receipt, but they cannot replace behavioral testing, access control, provenance, or human authority.

## Detailed Summary

### Problem and background

Autonomous systems fail in ways that final outcomes obscure. A bad replenishment cost may follow from a wrong belief or a correct belief followed by a bad action. A coding benchmark failure may reflect weak capability or a hidden test that contradicts the prompt. A clinical recommendation may look plausible while violating a medication constraint. A scientific agent may reason correctly but issue an unsafe motor command. A memory system may retrieve relevant content but violate scope or deletion policy. The selected source bundle is valuable because each item makes one of these hidden distinctions explicit.

### Adversarial search and benchmark validity

GPT-Red is described as a self-play red-teamer trained against evolving defender models in environments with explicit threat models. OpenAI reports 84% success across held-out indirect prompt-injection scenarios versus 13% for human red-teamers, live-agent case studies, and a reduction from above 95% to below 10% for one direct-injection class between GPT-5.1 and GPT-5.6 Sol. The same report states that GPT-5.6 Sol fails on 0.05% of GPT-Red direct injections in the named evaluation and emphasizes capability-preserving robustness rather than refusal inflation. These numbers remain internal-report evidence.

The SWE-Bench Pro audit shows why a strong attacker or solver still needs a valid oracle. On a 731-task public split, an automated pipeline flagged 286 tasks for deeper review. The investigator pipeline ultimately labeled 200 tasks (27.4%) broken, while a five-engineer annotation campaign labeled 249 (34.1%) broken. Overly strict tests, underspecified prompts, low-coverage tests, and one misleading-prompt category undermine the inference that pass/fail cleanly measures software capability. Human judgments overlapped with the agent pipeline on 74% of categories and found low coverage more often, showing both the leverage and incompleteness of agent-assisted auditing.

### Belief, action, and durable state

STOCKTAKE models a 26-week replenishment task as a factored POMDP with six hidden processes. A fair oracle uses the same observation stream as the agent, with exact Bayes filtering per factor, so performance can be normalized between a symptom-blind floor and the oracle. The authors separately grade written beliefs and actions. Across fifty curated seeds, four frontier models detect 84-88% of hidden failures but span skill scores from 0.62 to -0.23; 34-43% of correctly diagnosed stress weeks still end in stockout. This demonstrates that explicit knowledge does not guarantee effective control and that both under-response and costly over-response matter.

Oracle Agent Memory treats long-horizon state as a database lifecycle: ingest, extract, consolidate, summarize, retrieve, revise, and remove under user, agent, and thread scopes. Its report gives 93.8% LongMemEval accuracy and about 10.7 times fewer tokens than flat history. The prior full review correctly limits those numbers to the reported configuration and highlights extraction correctness, consent, deletion propagation, poisoning, benchmark leakage, and cross-baseline comparability as unresolved.

### New expansion: verbalizable internal state

The J-lens paper asks whether a privileged subset of language-model representations is available for report, directed control, flexible computation, and broad broadcast. For layer \(\ell\), it averages the Jacobian from an intermediate residual-stream state to later final-layer states over prompts and token positions, then composes that linear map with the model's normal unembedding. The resulting token-indexed vectors describe what an activation is disposed to make the model say across contexts. Sparse non-negative combinations define a J-space approximation, typically using at most about 25 active vectors; the paper reports that this component never exceeds 10% of activation variance in the studied layers.

The evidence is mechanistic. Swapping a chosen sport representation changes the model's later report. Swapping an unspoken intermediate such as “spider” for “ant” changes the derived leg count. The same country swap redirects several different downstream questions, supporting a shared representation rather than task-specific copies. Conversely, swaps affect explicit report and flexible inference while leaving fluent continuation and anomaly detection mostly intact. Broad J-space ablation damages multi-step reasoning much more than several automatic tasks, and targeted attention-head ablations reduce injected-thought reporting from 0.54 to 0.09 while matched controls do not.

The safety results are promising but bounded. The J-lens surfaces evaluation-awareness, fabrication, manipulation, and deception-related tokens in case studies and model organisms. A simple evaluation-awareness score has AUC 0.853 against an independent natural-language-autoencoder flag set over a stratified sample from roughly 94,000 positions. Realism edits lower the score in all eleven evaluated suites, significantly in eight. However, the authors explicitly do not claim that all strategic cognition routes through the J-space; automatic or well-practiced processes can bypass it.

Counterfactual reflection training adds a causal training result. Ten thousand partial task rollouts receive an appended reflection question and constitution-grounded target, but loss is computed only on that reflection. At evaluation, no reflection prompt is present. The trained Haiku 4.5 model improves on two honesty/deception benchmarks, and ethics-related concepts become more active in J-space. Ablating 176 ethics-related directions moves fabrication dishonesty from 0.07 to 0.22, close to the 0.25 baseline; ablating 63 directions moves deception from 0.05 to 0.23, leaving some unexplained gain. This supports mediation by the inspected representations without establishing completeness.

The released `anthropics/jacobian-lens` repository provides a small Apache-2.0 package, tests, synthetic prompt data, an end-to-end notebook, a dependency lock, and fitting/apply interfaces for open-weight decoder models. It states that the reference implementation is unmaintained, bundles no model weights or text corpus, and is not optimized. This is a useful replication surface, not a reproduction receipt.

### Capability, clinical, scientific, and hardware control

GRAM attaches capability-specific auxiliary modules to transformer MLPs and selectively routes forward/backward updates by dataset. Deleting a module changes the inference-time capability profile. The paper reports experiments on SimpleStories and on 800M-parameter models trained with general data plus virology, cybersecurity, nuclear-physics, and specialist-code domains, followed by a scaling study from 50M to 5B parameters. GRAM is reported to track separately trained data-filtered models while supporting five profiles at one-fifth the training compute. It remains preliminary, dependent on labels and routing, and untested as a production frontier control.

MIRA moves medical evaluation into a FHIR-compatible EHR sandbox with eleven tools and more than 85,000 action options. It uses retrospective MIMIC-IV cases across eight diagnoses and compares against two physician cohorts. The paper reports 87.8% diagnostic accuracy on a matched 311-case subset versus 78.1% for board-certified physicians and 71.1% for a mixed-seniority cohort, plus patient-agent consistency, adversarial prompt tests, and medication-safety audits. The system remains simulation-based, condition-limited, and not reliable enough for autonomous clinical deployment.

The X-ray scientist uses an MCP interface to observe detector images and scan plots, issue beamline-style commands, and iteratively align a crystal. Virtual experiments automate execution; real-beamline demonstrations preserve a human relay for facility safety while executing the proposed commands without modification. Ten-run virtual evaluations show mostly sub-five-degree alignment errors and expose degradation under constrained reasoning or harder conditions. Real trials demonstrate adaptive reuse of an observed motor offset, but identical-condition repetitions were limited by beamtime.

HORCRUX unifies Keccak, modular/Galois arithmetic, sampling, and related kernels for ML-KEM, ML-DSA, SLH-DSA, HQC, and Falcon in a tightly coupled RISC-V coprocessor. The paper reports up to 129x, 9.17x, and 27x acceleration for hash-, lattice-, and code-based schemes, under 21,000 LUTs and 4,400 flip-flops, plus 65 nm post-synthesis and power results. Fixed-latency instructions address timing leakage, while the paper leaves power-analysis resistance to future work.

PriEval-Protect proposes a two-stage healthcare privacy workflow combining regulatory retrieval/scoring with technical measures such as architecture, encryption, similarity, uncertainty, adversary success, and information gain/loss, followed by mitigation recommendations. Because only the canonical record and abstract were accessible, this artifact does not import empirical hospital results, weighting validity, or legal conclusions as established evidence.

### Synthesis

Across these domains, the mechanism is consistent: expose the hidden state that matters, preserve the authority boundary for action, and evaluate the complete transition. Interpretability without action receipts can describe a thought but miss what the system does. Behavioral testing without valid oracles can score the wrong property. Capability removal without provenance can hide leakage. Autonomy without execution interlocks can turn a correct plan into an unsafe act.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | GPT-Red reaches 84% scenario success versus 13% for humans on the named held-out indirect-injection arena. | Author/organization claim | E2 | Directly reported with a named comparator; external reproduction unavailable. | Medium |
| C2 | Roughly 30% of the SWE-Bench Pro public split may be broken. | Author/organization claim | E3 | Supported by two review paths with 27.4% and 34.1% estimates; audit selection and organizational provenance remain caveats. | Medium-high |
| C3 | Correctly stated beliefs and effective actions separate sharply in STOCKTAKE. | Author claim | E4 | The fair-oracle construction and reported skill/stockout results directly support the gap under the benchmark. | High for paper report |
| C4 | A sparse vocabulary-aligned J-space is causally involved in report and flexible reasoning. | Author claim | E5 | Multiple swaps, ablations, matched controls, and cross-task reuse support causality within studied models and tasks. | High for paper report |
| C5 | The J-space is an incomplete monitor of strategic cognition. | Source limitation and reviewer assessment | E5 | Explicitly supported by single-token, interpretability, task-selection, architecture, and automatic-processing limitations. | High |
| C6 | Counterfactual reflection training changes behavior partly through implanted J-space content. | Author claim | E5 | Behavioral improvement plus targeted reversal supports mediation; incomplete reversal on deception leaves additional mechanisms open. | High for paper report |
| C7 | The open Jacobian-lens repository materially improves reproducibility. | Reviewer interpretation | E6 | Code, tests, data, lockfile, and notebook are present, but no released production-model lens or independent run was verified. | Medium-high |
| C8 | GRAM approximates multiple filtered capability profiles from one training run. | Author claim | E7 | Supported by the canonical account across named scales; full independent evaluation is absent. | Medium |
| C9 | MIRA shows strong governed-workflow performance but not autonomous clinical readiness. | Mixed author claim and reviewer interpretation | E8 | Peer-reviewed retrospective simulation supports the first half; paper limitations support the boundary. | High |
| C10 | The X-ray scientist demonstrates closed-loop physical-task transfer with a retained safety intermediary. | Mixed author claim and reviewer interpretation | E9 | Virtual and real evidence supports proof of concept; limited real repetitions constrain generalization. | High |
| C11 | Oracle Agent Memory makes memory lifecycle and scope explicit, but benchmark accuracy does not prove governance correctness. | Mixed source claim and reviewer interpretation | E10 | Directly grounded in architecture and prior full review. | Medium-high |
| C12 | HORCRUX demonstrates a shared crypto-agile hardware design but does not complete the side-channel case. | Mixed author claim and reviewer interpretation | E11 | Paper provides FPGA/ASIC evidence and explicitly leaves power SCA hardening for future work. | High for paper report |
| C13 | Inspectable autonomy requires observation, decision, execution, and outcome receipts plus fallback. | Derived reviewer inference | E1-E13 | Cross-source synthesis; not directly tested as a unified system. | Medium |

## Methodology

- `Research objective`: Review one randomly selected eligible source DEP, preserve its complete provenance, detect prior Black-Lake continuity, and expand one randomly chosen primary thread into a schema-complete DEP research artifact.
- `Sources inspected`: Both source DEP files; live README rules for both repositories; the prior Oracle Agent Memory artifact; the Smart Coverage Goals log, Report-Mark, related-reading, and reference sections; official pages and full papers listed in Source Metadata; and the official Jacobian-lens repository surface.
- `Discovery strategy`: Repository enumeration, exact marker search, structured path/content review, direct opening of source URLs, canonical arXiv/publisher checks, prior-art lookup by source identifier, and inspection of official code/documentation links.
- `Inclusion criteria`: Canonical source-DEP items, primary or official sources, peer-reviewed publisher records, official implementation surfaces, and older repository artifacts directly connected to this DEP.
- `Exclusion criteria`: Secondary commentary as claim evidence, inaccessible full text as empirical evidence, unpinned claims not present in inspected sources, and material requiring unsafe, private, licensed, or clinical execution.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication.
- `Evidence handling`: Major claims map to evidence IDs; organization and author claims remain labeled; repository files and URLs are public-safe; negative evidence and unavailable artifacts remain visible.
- `Uncertainty handling`: Confidence is reduced for internal-only evaluations, abstract-limited sources, organization-authored audits, absent independent reproduction, proprietary models, and limited real-world trials.
- `Version control`: Paper versions, publication dates, repository access date, and public identifiers are recorded when visible. No unavailable commit identifier is invented.
- `Random selection`: The DEP draw used one accepted OS-cryptographic UInt32 with rejection sampling over 86 sorted eligible candidates. Because older relevant artifacts existed, the expansion draw used one accepted OS-cryptographic UInt32 over seven accessible, not-yet-dedicated threads and selected the J-space paper.
- `Reviewer stance`: DEP-ready synthesis, critique, implementation translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: Ten findings in the selected DEP, with full expansion of J-space mechanisms, evidence, code availability, limitations, and product implications.
- `Temporal boundary`: Sources available through 2026-07-29; later revisions may differ.
- `Evidence limits`: GPT-Red and several alignment results rely on internal models or environments; PriEval-Protect remained abstract-limited; GRAM full-paper HTML was unavailable; no paper result was rerun.
- `Assumptions`: The source DEP's ranking is treated as a selection context, not as an authority ranking. Prior Black-Lake reviews are continuity evidence, not proof of source claims.
- `Constraints`: No external source redistribution, private-system access, patient data handling, beamline control, model-weight use, adversarial exploit execution, or security certification.
- `Out of scope`: Legal compliance determination, clinical recommendation, production red-team execution, dual-use capability training, hardware synthesis, side-channel testing, and consciousness attribution.
- `Intended use`: Research review, DEP deposition, audit architecture, evaluation planning, and safe MVP design.
- `Audience`: Agent-system researchers, evaluation engineers, safety reviewers, product architects, and provenance maintainers.
- `Reproducibility boundary`: Public source and implementation surfaces are identifiable; no environment, dataset, model, benchmark, clinical workflow, instrument, or hardware result was independently reproduced.
- `Data sensitivity`: Public repository and publication content only. Underlying clinical and internal lab data remain governed by their original controls.

## Observations

- `Observed pattern`: Every strong item adds a typed boundary: threat model, benchmark oracle, belief/action split, workspace layer, removable module, FHIR action, MCP command, memory scope, fixed-latency instruction, or privacy score.
- `Technical implication`: Evaluation architecture should log why an action was chosen, what authority executed it, and whether the outcome validated the belief—not just the final score.
- `New in this pass`: The J-space evidence suggests a useful observation channel between hidden activations and external action. Its value is highest when joined to action and outcome receipts, not used as a standalone deception detector.
- `Contradiction or tension`: The J-lens is causally informative yet incomplete. Automatic cognition can bypass it, token-level readouts miss multi-token or relational structure, and some outputs remain uninterpretable.
- `Observed pattern`: Human intermediaries remain valuable at ambiguity and consequence boundaries: engineers adjudicate broken benchmark tasks, physicians define clinical safety, and beamline staff relay commands.
- `Reviewer hypothesis`: The most robust agent-control stack will combine behavioral red-teaming, valid task oracles, internal-state probes, capability restriction, and execution interlocks, with disagreement treated as an escalation signal.
- `Open question`: Can internal probes remain calibrated across model updates, quantization, fine-tuning, context length, and deployment traffic without reintroducing a new opaque benchmark?

## Considerations

- Internal-state monitoring can create false confidence. A missing deception token is not evidence of honest cognition, and a salient token may reflect context rather than intent.
- Interpretability outputs are sensitive data when they expose user content, latent goals, or proprietary model internals. Access, retention, deletion, and audit controls should match or exceed those for ordinary logs.
- Automated red-teaming must remain in authorized environments with containment, disclosure, and non-release rules for offensive capability.
- Benchmark auditors should publish task-level receipts, adjudication disagreement, and the effect of excluding invalid tasks rather than only a revised aggregate.
- Clinical agents require prospective evaluation, clinician authority, patient-level safeguards, drift monitoring, and regulatory review; retrospective sandbox success is not deployment permission.
- Scientific agents need typed commands, simulator-to-instrument validation, motor and radiation interlocks, human override, and immutable experiment traces.
- Capability modules and hardware extensions create supply-chain artifacts that need versioning, authenticity, rollback, and side-channel review.
- Privacy scoring must not be represented as legal advice. Regulatory interpretation, technical leakage, and mitigation effectiveness require distinct accountable reviewers.
- The consciousness analogy in the J-space paper is functional and contested. This artifact makes no claim about subjective experience or moral status.

## Strengths

- The selected DEP spans model, agent, evaluation, data, instrument, memory, hardware, and governance layers without collapsing their distinct evidence standards.
- STOCKTAKE, the J-space paper, MIRA, and the X-ray scientist expose intermediate state and action structure rather than relying only on end scores.
- The J-space work uses causal interventions, matched controls, cross-task tests, multiple model checkpoints, explicit negative results, and an unusually extensive appendix.
- The official Jacobian-lens repository includes tests, synthetic evaluation data, a lockfile, a notebook, and a clear license.
- The SWE-Bench audit combines agent investigation with multiple independent engineers and makes category disagreement visible.
- MIRA and the X-ray scientist ground agent outputs in typed tools and domain state rather than free-text judgment alone.
- HORCRUX and GRAM translate governance into architectural controls instead of relying exclusively on policy at the output layer.

## Weaknesses

- Several central claims are produced by the organizations that built the evaluated models or systems; independent replications are missing.
- J-space results rely heavily on proprietary Claude checkpoints, token-aligned concepts, post-hoc workspace boundaries, and model-specific layer analysis.
- The J-lens does not reliably capture multi-token concepts, relational binding, all tasks, early-layer content, or automatic cognition.
- GPT-Red evidence is largely internal, and releasing a strong attacker is intentionally out of scope, limiting independent audit.
- The SWE-Bench Pro deep review begins from an automated flagged subset, so false negatives outside that subset remain possible.
- GRAM's access-control framing depends on data labels, module isolation, and resistance to later adaptation; production frontier behavior is unknown.
- MIRA is retrospective and condition-limited; the X-ray real-world demonstrations had limited repeated trials.
- Oracle Agent Memory lacks independent end-to-end lifecycle verification; HORCRUX lacks completed power-side-channel hardening.
- PriEval-Protect is abstract-limited in this pass, preventing assessment of weighting, legal grounding, or experimental validity.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Cross-model J-lens replication | Interpretability | Test whether workspace claims survive open models, architectures, tokenizers, and scales | Generalization evidence and calibrated failure maps | High compute; method may not transfer | Pre-register prompts, layers, controls, metrics, and negative results across at least three open families |
| Relational and multi-token readouts | Interpretability | Token bags miss bindings and diffuse concepts | Higher recall for safety-relevant cognition | More complex probes can become harder to audit | Compare phrase/relational probes against causal patching and held-out human labels |
| Joint internal-behavioral audit | Safety evaluation | Internal probes and external outcomes have complementary blind spots | Better precision and escalation logic | Privacy and false-positive burden | Measure lift over transcript-only and lens-only auditors on blinded cases |
| Task-validity receipts | Benchmarks | Scores fail when prompt, tests, and intended behavior diverge | Auditable benchmark maintenance | Human review cost | Publish issue taxonomy, per-task evidence, disagreement, and score sensitivity |
| Lifecycle deletion tests | Agent memory | Retrieval quality does not establish revocation | Safer durable context | Storage and lineage overhead | Seed, consolidate, revoke, and verify propagation across replicas and summaries |
| Typed execution interlocks | Clinical/scientific agents | Correct plans can still produce unsafe acts | Bounded real-world autonomy | Reduced flexibility or slower workflows | Simulator, shadow, hardware-in-loop, and human-override acceptance tests |
| Capability-leakage audit | GRAM | Removed knowledge may remain distributed or recoverable | Stronger access-control evidence | Adversarial fine-tuning can be dual-use | Authorized, contained recovery tests and matched filtered-model baselines |
| Power-side-channel evaluation | HORCRUX | Fixed latency covers only one leakage class | Completes a major hardware-security boundary | Specialized equipment and design changes | TVLA-style and attack-oriented measurements on representative FPGA/ASIC implementations |

## Potential Implementations

### 1. Evidence-linked agent control plane

- `User`: Agent-platform safety and reliability teams.
- `Goal`: Connect observations, internal signals, decisions, tool calls, and outcomes without treating any one signal as truth.
- `Core mechanism`: Append-only receipts with source identity, decision rationale, authority, execution result, outcome, confidence, and fallback status.
- `Required inputs`: Tool schemas, policy rules, model/version pins, task oracle, optional interpretability signals, and evaluation labels.
- `Outputs`: Trace graph, exception queue, confidence calibration, and replay package.
- `Risk controls`: Least privilege, redaction, encrypted retention, human escalation, and no automatic punitive action from internal-state probes.
- `Evaluation`: Fault-injection matrix covering wrong belief, right-belief/wrong-action, invalid oracle, denied tool call, stale memory, and misleading internal signal.

### 2. Benchmark validity gate

- `User`: Evaluation maintainers and model-release reviewers.
- `Goal`: Prevent capability or safety decisions from depending on broken tasks.
- `Core mechanism`: Agents inspect prompt, repository state, tests, reference patch, and failure traces; independent humans adjudicate flagged or disputed cases.
- `Required inputs`: Versioned task bundle, environment manifest, model attempts, test results, and issue taxonomy.
- `Outputs`: Per-task validity receipt, severity, disagreement, and sensitivity-adjusted score.
- `Risk controls`: Blind initial human review, conflict disclosure, immutable evidence, and a held-out audit sample from unflagged tasks.
- `Evaluation`: Inter-rater agreement, false-negative sampling, adjudication time, and downstream score change.

### 3. Internal-state audit adapter

- `User`: Authorized interpretability researchers.
- `Goal`: Add J-lens observations to a behavioral audit without promoting them to ground truth.
- `Core mechanism`: Fit or load an open-model lens, query selected positions, compare with matched control directions, and join results to external behavior.
- `Required inputs`: Open model, licensed prompts, lens artifact, control probes, and blinded case labels.
- `Outputs`: Ranked concepts, uncertainty, control comparison, and behavior-linked audit notes.
- `Risk controls`: Local-only processing, synthetic prompts by default, no secret logging, strict access to activations, and a “no finding” state.
- `Evaluation`: Precision/recall against held-out labels, causal intervention checks, drift across model revisions, and auditor lift.

### 4. Governed scientific action broker

- `User`: Laboratory and facility automation teams.
- `Goal`: Separate agent planning from safety-authorized physical execution.
- `Core mechanism`: Typed command proposals pass deterministic limits, simulator checks, and human or facility authority before execution.
- `Required inputs`: Instrument schema, motor/energy limits, sample state, simulator, experiment plan, and emergency-stop policy.
- `Outputs`: Approved command, denial reason, instrument result, and experiment trace.
- `Risk controls`: Hardware interlocks, read-only default, bounded command grammar, rate limits, operator override, and rollback or safe-stop.
- `Evaluation`: Simulator coverage, hardware-in-loop trials, unexpected-offset scenarios, malformed-command tests, and incident-free shadow operation.

## Three Ways to Exercise This Research

1. `Receipt-first toy agent`: Use a synthetic inventory task to log observation, stated belief, chosen action, simulated execution, and cost. Success means every wrong outcome can be assigned to perception, policy, execution, or oracle error; stop if any action lacks a typed receipt.
2. `Open-model J-lens notebook`: In a local authorized environment, run only the released walkthrough on synthetic prompts and an open-weight model. Compare J-lens readouts with random-direction controls and record failures. Success means a reproducible notebook plus negative cases; stop before using private prompts, proprietary weights, or deployment decisions.
3. `Benchmark mini-audit`: Select twenty public toy coding tasks, blind one reviewer to agent flags, and classify prompt/test consistency. Success means per-task evidence and measured agreement; stop if licenses, secrets, or executable tests cannot be safely isolated.

## Example MVP Product

- `Product name`: Evidence Gate
- `Target user`: Teams shipping tool-using agents in regulated or operationally consequential settings.
- `Problem`: Agent traces contain outputs and tool calls but often cannot show whether failure began in observation, reasoning, authority, execution, or evaluation.
- `Core workflow`: Register a versioned task and policy; collect observation and optional internal-probe receipts; require a typed decision; enforce tool authority; attach execution and outcome receipts; route missing, conflicting, or high-risk evidence to review.
- `Data requirements`: Synthetic or authorized task inputs, policy rules, tool schemas, version identifiers, outcomes, and optional local-only activation summaries. Raw secrets and patient data are excluded from the MVP.
- `Architecture`: Local event collector, append-only receipt store, deterministic policy gate, optional probe adapter, replay worker, and reviewer dashboard.
- `Success metrics`: At least 95% receipt completeness on toy tasks; correct root-cause classification on seeded failures; zero unauthorized tool executions; calibrated review precision; replay success for every accepted case.
- `Risk controls`: Least privilege, encryption, retention limits, redaction, immutable audit events, human override, and explicit prohibition on treating interpretability output as intent proof.
- `Limitations`: Does not certify truth, safety, clinical fitness, legal compliance, or absence of hidden cognition. An agent can fail outside the modeled schema.
- `MVP boundary`: Synthetic or public toy workloads only; no production model activations, medical decisions, beamline control, offensive red-teaming, or capability-removal training.
- `Deployment model`: Local-only CLI plus browser dashboard.
- `Evaluation plan`: Unit tests for schema and policy, seeded fault matrix, blinded reviewer exercise, and one shadow-mode pilot with no write authority.
- `Failure modes`: Missing source identity, stale policy, forged outcome, overconfident probe, incomplete tool telemetry, and reviewer automation bias.
- `Maintenance plan`: Versioned schemas, signed policy releases, model/probe recalibration, retention review, and quarterly fault-taxonomy refresh.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| **New in this pass - Verbalizable Representations Form a Global Workspace in Language Models** | Primary technical paper | Full expansion source for J-lens derivation, J-space function, alignment audits, counterfactual reflection, limitations, and appendices | https://transformer-circuits.pub/2026/workspace/index.html |
| **New in this pass - A global workspace in language models** | Official author summary | Concise organization-authored account and public interpretation boundary | https://www.anthropic.com/research/global-workspace |
| **New in this pass - `anthropics/jacobian-lens`** | Official implementation | Apache-2.0 reference code, tests, synthetic prompt sets, notebook, and replication boundary | https://github.com/anthropics/jacobian-lens |
| **New in this pass - Neuronpedia Jacobian Lens** | Interactive implementation surface | Open-model exploration surface; useful for bounded demonstrations, not claim validation | https://www.neuronpedia.org/jlens |
| STOCKTAKE | Primary benchmark paper | Fair-oracle separation of perception and action in long-horizon agents | https://arxiv.org/abs/2607.13618 |
| Modular Pretraining Enables Access Control | Primary capability-control paper | Architectural restriction of dual-use capabilities through removable modules | https://arxiv.org/abs/2607.08077 |
| Smart Coverage Goals | Prior DEP-E continuity | Shows how invalid or redundant objectives distort search and links the selected DEP's SWE-Bench audit | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-Smart%20Coverage%20Goals |
| Oracle Agent Memory | Prior DEP-A continuity | Full prior review of one selected DEP paper; memory lifecycle and governance boundary | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-A/Series%20001/DEP-A-20260719-Oracle%20Agent%20Memory |
| NIST Cybersecurity White Paper on crypto agility | Near-primary standard context | Referenced by HORCRUX for algorithm and implementation agility; requires separate review before importing claims | https://doi.org/10.6028/NIST.CSWP.39.ipd |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260717-Tech%20Intel%200104 | Selected DEP identity and inventory | 2026-07-29 | Repository evidence |
| R2 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260717-Tech%20Intel%200104/daily_research_findings_2026-07-17_0104.md | Ten source findings and original synthesis | 2026-07-29 | Inspected in full |
| R3 | https://openai.com/index/unlocking-self-improvement-gpt-red/ | GPT-Red method, results, case studies, limitations | 2026-07-29 | Official report; internal-system evidence |
| R4 | https://openai.com/index/separating-signal-from-noise-coding-evaluations/ | SWE-Bench Pro audit methodology and findings | 2026-07-29 | Official audit |
| R5 | https://arxiv.org/abs/2607.13618 | STOCKTAKE identity and full-paper locator | 2026-07-29 | Full HTML inspected |
| R6 | https://arxiv.org/html/2607.13618 | STOCKTAKE task, oracle, metrics, results, prompts | 2026-07-29 | Primary full text |
| R7 | https://transformer-circuits.pub/2026/workspace/index.html | J-lens/J-space method, experiments, limitations, appendices | 2026-07-29 | **New full expansion source** |
| R8 | https://www.anthropic.com/research/global-workspace | Official J-space summary and interpretation boundary | 2026-07-29 | **New in this pass** |
| R9 | https://github.com/anthropics/jacobian-lens | Official reference implementation and data/license notes | 2026-07-29 | **New in this pass**; code not run |
| R10 | https://www.neuronpedia.org/jlens | Interactive open-model surface | 2026-07-29 | Discovery and implementation context only |
| R11 | https://alignment.anthropic.com/2026/modular-pretraining/ | GRAM official technical account | 2026-07-29 | Preliminary research |
| R12 | https://arxiv.org/abs/2607.08077 | GRAM canonical title, authors, date, and abstract | 2026-07-29 | Primary record |
| R13 | https://doi.org/10.1038/s41586-026-10675-5 | MIRA methods, results, safety, limitations | 2026-07-29 | Peer-reviewed publisher record |
| R14 | https://doi.org/10.1038/s42256-026-01261-5 | X-ray scientist methods, virtual and real results, availability | 2026-07-29 | Peer-reviewed publisher record |
| R15 | https://arxiv.org/abs/2607.13157v1 | Oracle Agent Memory canonical record | 2026-07-29 | Primary paper identity |
| R16 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-A/Series%20001/DEP-A-20260719-Oracle%20Agent%20Memory | Prior full review and continuity | 2026-07-29 | Older than eligibility cutoff |
| R17 | https://arxiv.org/abs/2607.13939 | HORCRUX canonical identity | 2026-07-29 | Full HTML inspected |
| R18 | https://arxiv.org/html/2607.13939 | HORCRUX architecture, FPGA/ASIC results, security boundary | 2026-07-29 | Primary full text |
| R19 | https://arxiv.org/abs/2607.13754 | PriEval-Protect identity and abstract | 2026-07-29 | Abstract-limited; no empirical conclusion imported |
| R20 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-Smart%20Coverage%20Goals | Prior related DEP-E, log/report continuity, SWE-Bench bridge | 2026-07-29 | Older than eligibility cutoff |
| R21 | https://doi.org/10.6028/NIST.CSWP.39.ipd | Crypto-agility related reading | 2026-07-29 | Referenced as follow-up context; not fully reviewed |

## Appendix

### Selection receipt

- `Automation family`: Black-Lake Data Processing & Review; Black-Lake Data Processing & Review 0900.
- `Canonical candidate count`: 87.
- `Excluded within 24 hours`: 1.
- `Eligible count`: 86.
- `Eligibility cutoff`: 2026-07-28T00:03:00Z.
- `Recent exclusion`: `DEP-20260702-Tech Intel 1102`, marked at 2026-07-28T00:03:23Z.
- `Eligible-list SHA-256`: `ae003107619616eff133e978b61b1bbbc9f03b90ced75600f1ba50a5e7b7ca59`.
- `Accepted DEP-selection UInt32`: `1439622081`.
- `Selected zero-based index`: 55.
- `Selected DEP`: `Black-Lake-Data/.lake-data/DEP-20260717-Tech Intel 0104`.
- `Expansion pool`: Seven accessible primary or near-primary threads without a dedicated prior expansion in this continuity review.
- `Expansion-pool SHA-256`: `8d2d260db8ec3d31e984fd1593f08a553c47b32bc65165f11c0e8f07cce16e03`.
- `Accepted expansion UInt32`: `3718540255`.
- `Selected expansion index`: 3.
- `Selected expansion`: J-space/global workspace paper, official summary, and official implementation.

### Source inventory and collection boundary

- Repository files inspected: selected DEP `README.md`; selected daily findings; prior Oracle Agent Memory README and full review; Smart Coverage log, Report-Mark, related-reading section, and source-reference section; live repository README authorities.
- External sources inspected by URL: official reports, canonical records, full-paper HTML, publisher pages, and the official Jacobian-lens repository listed above.
- External source files collected: none.
- Executed artifacts: none.
- Independent reproduction: none.
- Public sanitization: repository-relative paths and public URLs only; private execution and filesystem context withheld.
