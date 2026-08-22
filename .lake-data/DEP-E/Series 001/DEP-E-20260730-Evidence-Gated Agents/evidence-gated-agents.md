---
title: "Evidence-Gated Agents - DEP-E"
generated_at: "2026-07-30T00:03:00Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of ten studies on evidence, controls, evaluation, and expert gates for agentic systems."
source_status: "mixed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-30"
temporal_cutoff: "2026-07-30"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260730-Tech%20Intel%200102"
stable_identifier: "DEP-20260730-Tech Intel 0102"
confidence_summary: "High for directly reported paper methods and metrics; medium for implementation readiness because no code, datasets, models, benchmarks, clusters, clinical workflows, or quantum experiments were executed."
safety_scope: "Defensive, evaluation-only, and research-planning use."
distribution_notes: "Public sources retain their own licenses; repository inspection does not imply redistribution permission or independent replication."
---

# Evidence-Gated Agents - DEP-E

## Source Metadata

This artifact expands `Black-Lake-Data/.lake-data/DEP-20260730-Tech Intel 0102` through direct inspection of its two Markdown records, all ten cited primary papers, and the official implementation repositories that could be identified and opened. External papers and repositories were inspected by public URL; they were not copied into this DEP.

| ID | Source | Role | Type | Identifier / Version | URL / Repository-Relative Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Black-Lake-Data DEP README | Primary intake | Markdown | `DEP-20260730-Tech Intel 0102` | `Black-Lake-Data/.lake-data/DEP-20260730-Tech Intel 0102/README.md` | Repository content; attribution retained | 2026-07-30 | Inspected |
| S2 | Daily Research Findings | Primary intake | Markdown | 2026-07-30 0102 | `Black-Lake-Data/.lake-data/DEP-20260730-Tech Intel 0102/daily_research_findings_2026-07-30_0102.md` | Repository content; attribution retained | 2026-07-30 | Inspected |
| S3 | *MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents* — Shuyue Wei, Chang Liu, Zimu Zhou, Yongxin Tong, Lizhen Cui | Primary paper | arXiv HTML | arXiv:2607.25992v1 | https://arxiv.org/abs/2607.25992 | License visible from arXiv record | 2026-07-30 | Full HTML inspected |
| S4 | MemLens | Official implementation | GitHub repository | Current public default branch at access | https://github.com/LIUHA1ZHU/MemLens | MIT license visible | 2026-07-30 | Repository structure and README inspected; not executed |
| S5 | *Towards an Agent Operating System - Lessons from Classical and Cloud OS* — Gosia Steinder, Hubertus Franke | Primary paper | arXiv PDF | arXiv:2607.25076v1 | https://arxiv.org/abs/2607.25076 | License visible from arXiv record | 2026-07-30 | Full PDF inspected |
| S6 | rossoctl | Near-primary prototype | GitHub repository | Current public default branch at access | https://github.com/rossoctl/rossoctl | Apache-2.0 license visible | 2026-07-30 | README and repository structure inspected; not executed |
| S7 | *Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation* — Stefan Krsteski, Charlotte Meyer, Guillaume Allegre, Tony O'Halloran, Alexandre Sallinen | Primary paper | arXiv HTML | arXiv:2607.25891v1 | https://arxiv.org/abs/2607.25891 | CC BY 4.0 visible | 2026-07-30 | Full HTML inspected |
| S8 | Messier artifact locator | Official artifact link | Repository snapshot | Paper-linked locator | https://anonymous.4open.science/r/messier-d3 | Usage terms not inspected | 2026-07-30 | Inaccessible during review |
| S9 | *Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?* — Farooq Shaikh | Primary paper | arXiv HTML | arXiv:2607.25995v1 | https://arxiv.org/abs/2607.25995 | License visible from arXiv record | 2026-07-30 | Full HTML inspected |
| S10 | VulnCare | Official benchmark implementation | GitHub repository | Current public default branch at access | https://github.com/dynatrace-research/vulncare | Apache-2.0; intentionally vulnerable test environment | 2026-07-30 | README and repository structure inspected; not executed |
| S11 | KuTIE artifacts | Official experiment artifact | GitHub repository | Current public default branch at access | https://github.com/dynatrace-research/kutie-artifacts | Source-available; repository states all rights reserved | 2026-07-30 | README, test layout, and results layout inspected; not executed |
| S12 | *Distributing Security Controls Through Harness Engineering* — William Robert Gore | Primary paper | arXiv PDF | arXiv:2607.25890v1 | https://arxiv.org/abs/2607.25890 | CC license visible from arXiv record | 2026-07-30 | Full PDF inspected |
| S13 | shard-demo | Official demonstration | GitHub repository | Current public default branch at access | https://github.com/wrgore/shard-demo | Demonstration status; current README limits enforcement claims | 2026-07-30 | README and repository structure inspected; not executed |
| S14 | agent-security-lab | Official evaluation harness | GitHub repository | Current public default branch at access | https://github.com/wrgore/agent-security-lab | MIT license; benign prompts and synthetic credentials noted | 2026-07-30 | README, tests, and result-data layout inspected; not executed |
| S15 | *Reinforcement Learning for Code Optimization* — Pierre Chambon, Kunhao Zheng, Juliette Decugis, Benoit Sagot, Gabriel Synnaeve | Primary paper | arXiv PDF | arXiv:2607.25970v1 | https://arxiv.org/abs/2607.25970 | CC license visible from arXiv record | 2026-07-30 | Full PDF inspected |
| S16 | BigOBench | Related benchmark substrate | GitHub repository | Current public default branch at access | https://github.com/facebookresearch/BigOBench | License visible in repository; not the paper's implementation | 2026-07-30 | README inspected; not executed |
| S17 | *Evaluating Multi-Turn Multimodal Diagnostic Reasoning on Challenging Real-World Clinical Cases* — Rui Yang, Weihao Xuan, Yi Lin, et al. | Primary paper | arXiv HTML | arXiv:2607.25933v1 | https://arxiv.org/abs/2607.25933 | License visible from arXiv record | 2026-07-30 | Full HTML inspected |
| S18 | ClinMM repository locator | Official implementation link | GitHub repository | Paper-linked locator | https://github.com/ruiyang-medinfo/ClinMM | Terms not inspected | 2026-07-30 | Discovered but inaccessible during review |
| S19 | *Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?* — Abhishek Pillai, Samir Kumar Nayak, Yuan Chen | Primary paper | arXiv PDF | arXiv:2607.26041v1 | https://arxiv.org/abs/2607.26041 | License visible from arXiv record | 2026-07-30 | Full PDF inspected |
| S20 | Desktop-Delta Bench repository locator | Official implementation link | GitHub repository | Paper-linked locator | https://github.com/abhipi/DDB | Terms unavailable | 2026-07-30 | Returned not found during review |
| S21 | *OmniQEC: discovering practical quantum error-correcting codes by an AI scientist* — Ge Yan, Shanchuan Li, Pengyue Ma, Qixin Zhang, Pingchuan Ma, Jianping Wang, Min-Hsiu Hsieh, Yuxuan Du | Primary paper | arXiv HTML | arXiv:2607.25865v1 | https://arxiv.org/abs/2607.25865 | CC BY 4.0 visible | 2026-07-30 | Full HTML inspected |
| S22 | *Lowering the implementation barrier of neutral-atom quantum computing with agentic workflows* — Constantin Dalyac, Alexandre Dauphin, Loïc Henriet, Christophe Jurczak | Primary paper | arXiv HTML | arXiv:2607.25834v1 | https://arxiv.org/abs/2607.25834 | CC BY 4.0 visible | 2026-07-30 | Full HTML inspected |
| S23 | pasqal-cloud | Related official SDK | GitHub repository | Current public default branch at access | https://github.com/pasqal-io/pasqal-cloud | Apache-2.0 license visible; not a paper workflow release | 2026-07-30 | README and repository structure inspected; not executed |

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S2 | Primary intake | Selected DEP inventory, ten source links, initial synthesis, and collection note | Scope and provenance | High | Intake contains summaries, not independent validation |
| E2 | S3-S4 | Primary paper plus official repo | Memory hierarchy, Shapley-style value proxy, retention workflow, EduMemBench description, visible system components | Memory should be evaluated as governed data | High | No independent run; quantitative result tables were not recovered from the inspected HTML |
| E3 | S5-S6 | Primary conceptual paper plus prototype | Thirteen proposed agent-OS primitives, eight research tasks, and prototype positioning | Portable agent abstractions remain an open systems problem | High | Proposal is not a completed standard; prototype does not validate all semantics |
| E4 | S7-S8 | Primary paper plus artifact locator | Corpus dimensions, IRT comparisons, aggregation analysis, domain limitations | Evaluation records can be reusable evidence infrastructure | High | Linked artifact was inaccessible; upstream benchmark quality is assumed by the paper |
| E5 | S9-S11 | Primary paper plus official artifacts | 248-trial design, topology-aware/blind comparison, scoring method, benchmark manifests and result layout | Runtime context materially changes remediation success in the studied setting | High | Synthetic cluster; exact-value scoring is a proxy; artifacts were not executed |
| E6 | S12-S14 | Primary paper plus official repos | Four configurations, 23 tests, raw/adjusted scores, current demo behavior | Harness controls can be distributed, but release-state claims need version checks | High | Four controls studied and three implemented; current demo README differs from paper enforcement wording |
| E7 | S15-S16 | Primary paper plus related repo | DMC-Optim, correctness/speed gates, calibrated timing, strict pass@1 and human-comparison results | Optimization RL requires measurement and reward gates | High | Narrow Python competitive-programming scope; paper-specific code release not identified |
| E8 | S17-S18 | Primary paper plus repository locator | 1,089 cases, 3,760 images, 15 MLLMs, accuracy/reasoning measures, failure taxonomy | High-stakes evaluation needs progressive evidence and explicit escalation | High | Challenging published cases are not routine prevalence; repo inaccessible; no clinical validation performed |
| E9 | S19-S20 | Primary paper plus repository locator | 2,013 instances, ordering/action tasks, decoys, context effects, exact-match and F1 results | Transition verification is a distinct computer-use capability | High | Offline Linux benchmark with five action families; repository unavailable |
| E10 | S21 | Primary paper | Slow-fast search, qLDPC families, budgets, decoder-based circuit evaluation, reported logical-error results | Proxy search needs circuit-level correction | High | Simulation and tool evidence only; no hardware validation or code release identified |
| E11 | S22-S23 | Primary paper plus related SDK | Structured experiment specification, emulator gates, two QPUs, three cases, expert-caught failures, 633-paper screening | Expert validation remains essential before physical execution | High | Paper workflow code not identified; no experiment independently reproduced |
| E12 | E2-E11 | Reviewer synthesis | Cross-source comparison of memory, platform, benchmark, security, optimization, medical, GUI, and quantum evidence | Evidence gates are a reusable systems pattern | Medium | Cross-domain generalization is reviewer interpretation, not a shared causal result |

## Executive Summary

The ten studies converge on a practical systems thesis: capable agents need evidence gates at the boundaries where context becomes memory, intent becomes an action, a proxy becomes a score, or a generated plan becomes a physical or high-stakes intervention. The sources cover value-aware agent memory, an agent operating-system proposal, reusable evaluation records, context-aware Kubernetes remediation, coding-agent harness security, reinforcement learning for faster code, multimodal medical evaluation, desktop transition understanding, quantum error-correction search, and neutral-atom experiment preparation.

The strongest directly supported results are bounded to their own settings. KuTIE reports that topology context raised topology-dependent patch correctness from 11.1% to 78.0% across 248 trials [E5]. Reinforcement learning with calibrated execution-time rewards raised strict top-50% pass@1 from 18.0% to 31.3% for Qwen 2.5 7B and from 30.7% to 50.4% for CWM 32B [E7]. Desktop-Delta Bench remains unsaturated at 65.1% and 65.7% best exact-match rates for non-decoy and decoy ordering [E9]. ClinMM-Bench reports that even its best evaluated model produced completely correct diagnoses in only 33.88% of cases [E8]. In neutral-atom experiments, expert review caught both an inadequate observable and a plausible but incorrect hardware diagnosis [E11].

Reviewer interpretation: these are not ten demonstrations of one universal architecture. They are ten independent signals that agent reliability improves when a system separates fast generation from slower evidence, preserves the evidence trace, and routes unresolved disagreement to a bounded reviewer. Confidence is high in the reported designs and source-grounded metrics, but only medium in implementation readiness because the review did not execute any code, datasets, models, clusters, clinical workflows, benchmarks, simulators, or quantum hardware.

## Detailed Summary

### Memory as governed evidence

MemLens treats individual memories as managed data objects. It builds hierarchical memory units, estimates their marginal value with a Shapley-style sampling approximation, applies value-aware retention, and exposes retrieval, response, latency, and token behavior in an interactive system [E2]. The important architectural move is not merely “long-term memory”; it is a measurable retention policy whose decisions can be inspected. The paper's evidence supports a design direction, while independent performance replication remains open.

### Stable abstractions for agent platforms

*Towards an Agent Operating System* maps classical and cloud operating-system lessons into thirteen candidate primitives: lifecycle management, orchestration, skills, mediated tools, context, agent-to-agent communication, memory, identity and authorization, guardrails, failure handling, checkpoint/saga behavior, trajectory observability, and an AI-aware proxy [E3]. The paper explicitly presents these as a proposal and research agenda rather than a complete standard. Its eight open tasks make semantic precision, failure behavior, information flow, supply-chain risk, context eviction, and evaluation first-class research problems.

### Evaluation records instead of leaderboard snapshots

Messier standardizes 957,253 execution records from 30 benchmarks, 714 agents, 11,891 tasks, and 74,205 verifiers [E4]. Its 1PL item-response model correlates with a matched external capability index at 0.81 overall, 0.77 for programming, and 0.84 for mathematics; 1PL and 2PL rankings correlate at 0.98. The contribution is a reusable record layer that makes aggregation rules and verifier behavior inspectable. Its limits matter: the corpus is concentrated in English-language technical and professional tasks, inherits source-benchmark quality, and could not be checked against the linked artifact during this review.

### Runtime context as a security control input

KuTIE builds a live graph from Istio calls, Trivy posture findings, and service-account bindings, then supplies that topology to a model generating Kubernetes patches [E5]. The VulnCare evaluation spans 36 deployments, four namespaces, 31 findings, seven dependency classes, four models, and 248 deterministic trials. The aware condition solved 78 of 100 topology-dependent cases versus 11 of 99 in the blind condition; a topology-independent control showed no difference. The paper also exposes a measurement caveat: exact expected-value scoring can reject a healthy but over-permissive patch, so “correctness” is a deterministic proxy rather than full operational fitness.

### Harness security and release-state verification

SHarD evaluates OS sandboxing, skill scanning, and tool restriction through a 23-test suite across four agent configurations [E6]. Reported adjusted scores are 100% for the secured commercial comparison, 75% for the Codex comparison, and 100% for SHarD; raw scores are 87.0%, 69.6%, and 78.3%. The paper's harness architecture is a useful distribution pattern, but its current public demo README says a missing sandbox produces a warning and that enforced relaunch belongs to a planned/full version. That differs from wording in the paper describing relaunch and enforcement. The defensible conclusion is version-sensitive: the evaluated concept supports harness-distributed controls, while current public-main behavior must be checked before relying on enforcement.

### Performance optimization needs calibrated gates

*Reinforcement Learning for Code Optimization* separates correctness, optimization eligibility, and quality in the reward path and uses a calibrated timing sandbox plus an offline simulator to choose training configurations [E7]. Reported gains preserve pure-correctness performance while improving strict speed-aware pass rates. On LiveCodeBench, CWM 32B wins up to 83% of median-sample speed comparisons against standard RLVR. Against fastest correct human submissions, models reach roughly half the rate of complexity-class improvement, 14% versus 28%. Timing noise, sparse rewards, judge disagreement, and a single-file Python competitive-programming scope limit direct production claims.

### Clinical benchmarks as escalation evidence

ClinMM-Bench uses progressive multimodal disclosure across 1,089 challenging cases, 3,760 images, eight specialties, and an average of 5.45 turns [E8]. It evaluates 15 multimodal models at diagnostic and reasoning levels. GPT-5-medium leads the reported aggregate at 1.140 yet is completely correct in 33.88% of cases; Qwen3-VL-32B is the only evaluated open model above 10% complete correctness, at 11.20%. The authors identify information synthesis, knowledge mapping, perception, premature closure, and visual hallucination failures. This is evaluation evidence, not a clinical deployment endorsement or medical advice.

### GUI state transitions as a missing verification layer

Desktop-Delta Bench isolates action-caused visual change with 463 three-frame ordering cases, including 105 decoys, and 1,550 single-action cases across about 15 Linux applications and 50 domains [E9]. Task context improves decoy identification by 6.9 percentage points while reducing non-decoy exact match by 2.2 points, and models often copy the presented order. The benchmark shows that task success and single-frame grounding can conceal state-transition errors. It does not cover long-horizon execution, non-Linux environments, or the full diversity of GUI actions.

### Slow-fast evidence for quantum design

OmniQEC coordinates code generation, cheap code-level screening, syndrome-circuit synthesis, and decoder-based circuit evaluation across four qLDPC families, three language-model backends, fourteen physical-qubit budgets, and repeated seeds [E10]. The fast proxy guides exploration, while the slow circuit-level loop corrects proxy misranking. Reported codes beat selected bivariate-bicycle references under complete implementation budgets, with the best logical-error-rate improvement ranging from 29.23 times at physical error 0.002 to 1.66 times at 0.01 in one sweep. These are simulation-grounded results, not physical-hardware demonstrations.

### Expert gates before quantum execution

The neutral-atom workflow converts papers or patents into structured experiment specifications, performs noiseless and noise-aware emulation, and then routes campaigns to two cloud QPUs with human validation [E11]. Three case studies reached overnight campaigns, but experts corrected an inadequate observable in one case and a plausible false hardware diagnosis in another. A second agent considered 633 papers: 107 were unreadable and 526 classified, of which 258 were judged compatible with current QPUs, including 225 direct and 33 adaptation cases. The workflow demonstrates access compression while simultaneously documenting why an expert gate cannot yet be removed.

### Cross-source synthesis

Across these domains, four recurring control-plane objects emerge [E12]:

1. **A typed artifact**: memory record, benchmark record, patch, trajectory delta, experiment specification, or code candidate.
2. **A cheap evidence stage**: retrieval, topology extraction, proxy scoring, action inference, or noiseless emulation.
3. **A slower adjudication stage**: verifier aggregation, exact checks, circuit decoding, noise-aware simulation, or expert review.
4. **A durable trace**: value scores, runtime graph, verifier result, test transcript, benchmark item, or campaign record.

This synthesis is an implementation hypothesis, not a claim that the papers establish one shared causal law.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Memory retention can be made value-aware and inspectable. | Author claim | E2 | Architecture is directly documented; independent efficiency/quality replication remains open. | Medium |
| C2 | Agent platforms need stable abstractions with explicit semantics. | Author thesis | E3 | Strong systems framing, but the thirteen primitives are proposals rather than standards. | High |
| C3 | Standardized verifier-level records enable cross-benchmark capability analysis. | Author claim | E4 | Corpus scale and correlations support the analytical value; inaccessible artifact blocks independent checking. | Medium |
| C4 | Runtime topology improved Kubernetes patch correctness in VulnCare. | Author empirical claim | E5 | Strong within-study effect with a control; synthetic setting and exact-value proxy limit generalization. | High |
| C5 | Harness engineering can distribute agent controls. | Author empirical claim | E6 | Test evidence supports the prototype pattern; current public demo enforcement differs from paper wording. | Medium |
| C6 | Calibrated timing and gated rewards make code-optimization RL learnable. | Author empirical claim | E7 | Multiple baselines and exact metrics support the claim in the studied Python benchmark. | High |
| C7 | Multi-turn multimodal models remain unreliable on challenging clinical cases. | Author empirical claim | E8 | Large benchmark and failure taxonomy are direct; case distribution is not routine clinical prevalence. | High |
| C8 | Desktop transition reasoning is not saturated by current computer-use models. | Author empirical claim | E9 | Direct benchmark evidence; offline, Linux-only scope. | High |
| C9 | Slow-fast evaluation can improve practical QEC search. | Author empirical claim | E10 | Physically informed simulation supports search quality, not hardware performance. | High |
| C10 | Expert review remains necessary in agent-prepared QPU experiments. | Author observation and reviewer interpretation | E11 | Two concrete expert-caught failures directly support the need for review in these cases. | High |
| C11 | Evidence gates are a reusable architecture for reliable agents. | Reviewer interpretation | E12 | Consistent cross-domain pattern, but not jointly evaluated by the sources. | Medium |

## Methodology

- **Research objective:** Determine what the selected source DEP supports about evidence, control, and validation mechanisms for agentic systems, then preserve the result as a schema-complete DEP research artifact.
- **Sources inspected:** The selected DEP README and findings file; ten cited primary arXiv papers; official or near-primary public repositories for MemLens, rossoctl, VulnCare, KuTIE artifacts, SHarD, the agent security lab, BigOBench, and Pasqal's cloud SDK; and three paper-linked repository locators that were inaccessible.
- **Discovery strategy:** Source-first inspection of the selected DEP, followed by direct arXiv HTML/PDF review, paper-link tracing, and official repository README/structure inspection.
- **Inclusion criteria:** Every primary paper cited by the selected DEP was included. Repositories were included only when linked by the paper or clearly maintained as an official implementation, artifact, prototype, benchmark substrate, or SDK.
- **Exclusion criteria:** Secondary commentary, search-result snippets, unverified mirrors, and sources merely cited inside the papers were excluded. BigOBench and pasqal-cloud are labeled related rather than treated as paper implementations.
- **Analytical approach:** Mixed mechanistic, comparative, implementation, and safety review. Quantitative claims are kept within the experimental settings reported by each source.
- **Evidence handling:** Every substantive claim maps to S- and E-identifiers. Author claims, direct observations, reviewer interpretations, and cross-source inferences are labeled separately.
- **Uncertainty handling:** Inaccessible repositories, missing code releases, version mismatches, proxy-measure limitations, and non-replication are retained rather than silently resolved.
- **Extraction process:** Full paper HTML or PDF was inspected for methods, tables, numerical results, limitations, artifact links, and licensing cues. Repository inspection covered visible READMEs, licenses, and directory structure.
- **Version control:** Papers are pinned to arXiv v1 records. Repository observations describe the public default branch as accessed on 2026-07-30; no commit hashes were invented or asserted.
- **Cross-checking:** Intake metrics were checked against primary paper text. Repository claims were checked against current public README and structure where accessible.
- **Safety handling:** Kubernetes material is framed as defensive research; intentionally vulnerable artifacts were not executed. Clinical material is evaluation-only. Quantum claims distinguish simulation from physical execution.
- **Reviewer stance:** DEP-ready source preservation, critical synthesis, and bounded product translation.

## Scope, Constraints, and Assumptions

- **Scope:** Ten papers and their directly identifiable official artifacts from `DEP-20260730-Tech Intel 0102`.
- **Temporal boundary:** Public sources available through 2026-07-30.
- **Evidence limits:** Messier's linked artifact, ClinMM's repository, and Desktop-Delta Bench's repository were inaccessible. Paper-specific code releases were not identified for the code-optimization RL or OmniQEC studies. No MemLens result table was recovered from the inspected HTML.
- **Assumptions:** An official repository's current default-branch README is evidence of current public behavior, not necessarily the exact revision evaluated by a paper.
- **Constraints:** No external paper or repository content was redistributed. License boundaries remain source-specific. Security, medical, and quantum sources require bounded interpretation.
- **Out of scope:** Independent replication, clinical diagnosis, production security remediation, exploit development, model training, benchmark execution, cluster deployment, quantum simulation, or QPU execution.
- **Intended use:** DEP deposition, architecture review, research planning, evaluation design, and safe product ideation.
- **Audience:** Agent-platform engineers, evaluation researchers, security reviewers, research-tool designers, and DEP maintainers.
- **Depth target:** Full manuscript report with implementation-oriented synthesis.
- **Reproducibility boundary:** Metadata, methods, metrics, and public artifact locations are reproducible from the listed URLs; empirical findings were not independently reproduced.
- **Operational boundary:** The artifact may describe security and high-stakes workflows but does not provide operational instructions for exploiting systems, practicing medicine, or operating quantum hardware.
- **Data sensitivity:** Public research papers and public repositories; intentionally vulnerable cluster fixtures and synthetic credentials were not copied or executed.

## Observations

1. The highest-value evidence is often about a gate failing. Expert-caught quantum errors, clinical hallucinations, GUI decoys, proxy misranking, and topology-blind patches reveal where an architecture needs intervention.
2. Context is not uniformly beneficial. It improved KuTIE's topology-dependent patches and Desktop-Delta decoy identification, yet Desktop-Delta task context reduced non-decoy exact match. Context should be measured per decision, not treated as an unconditional gain.
3. The measurement layer can dominate the apparent result. Exact patch scoring, timing sandboxes, verifier aggregation, diagnostic judges, and circuit proxies each define what “better” means.
4. Artifact availability is uneven. Some papers provide well-organized repositories and raw results; others provide inaccessible locators or no identifiable code. Availability should be an explicit readiness dimension.
5. Version state can invalidate operational claims. SHarD's current public README and paper differ on automatic sandbox enforcement, demonstrating why paper conclusions must not be projected onto an unpinned default branch.
6. The Agent OS proposal supplies useful nouns, while the other nine studies supply candidate semantics: what a memory value means, how a verifier record composes, what a guardrail observes, and when a trajectory needs escalation.

## Considerations

- **Evaluator independence:** A gate should not rely only on the generator's own confidence or narrative. Use distinct evidence, tools, or reviewers when feasible.
- **Proxy drift:** Cheap proxies accelerate search but can misrank real outcomes. Store both proxy and adjudicated results so disagreement becomes a retraining and policy signal.
- **Context provenance:** Record which topology edge, memory unit, screenshot, verifier, image, or simulation result affected a decision.
- **Fail-closed boundaries:** Security changes, clinical-facing outputs, and physical experiments need explicit authorization and review states, not implied completion.
- **Version pinning:** Operational assertions about repositories require a commit, tag, or release. Default-branch inspection is a temporal observation only.
- **Human workload:** Expert gates can become bottlenecks. The system should prioritize ambiguous, high-impact, or proxy-disagreeing cases rather than requiring equal review of all outputs.
- **Licensing:** Source availability does not equal redistribution or modification permission. KuTIE's artifact repository, for example, states source availability without an open-source grant.
- **Medical safety:** ClinMM results characterize a benchmark; they do not establish safe clinical deployment or substitute for qualified care.

## Strengths

- Covers all ten primary sources rather than relying on the intake summaries.
- Preserves exact high-value metrics and experimental boundaries.
- Connects paper claims to current repository state where public artifacts were discoverable.
- Makes inaccessible sources and non-execution explicit.
- Surfaces a concrete paper/repository mismatch instead of flattening it.
- Produces a cross-domain architecture hypothesis while labeling it as reviewer interpretation.

## Weaknesses

- No empirical result was independently reproduced.
- Repository inspections were not pinned to reported commit hashes because exact evaluated revisions were not established.
- Three important linked artifacts were inaccessible.
- The ten-paper set was selected by the source DEP's daily research process, not by a systematic literature-review protocol.
- Cross-domain synthesis risks over-generalizing from benchmarks with different tasks, metrics, and maturity levels.
- Some quantitative result details depend on source-defined evaluators whose external validity is not established here.

## Potential Improvements

1. Pin every accessible implementation to a commit and archive machine-readable metadata without redistributing restricted source content.
2. Revisit the three inaccessible artifact locators and record whether availability, URL, or access policy changed.
3. Reproduce one bounded, low-risk result per domain, starting with published evaluation records rather than production systems.
4. Build a shared “gate card” that records input artifact, cheap proxy, adjudicator, disagreement, escalation, and final disposition.
5. Add a repository-state test for claims such as sandbox enforcement, code availability, and exact reproduction commands.
6. Evaluate evidence-gate cost: latency, expert minutes, false escalation, missed escalation, and incident severity avoided.
7. Separate benchmark correctness from operational fitness using multi-dimensional acceptance criteria.
8. Extend the evidence set with independent replications, standards work, and negative results.

## Potential Implementations

### Gate ledger

A small append-only service can store an agent action proposal, the context slice used, proxy scores, verifier outputs, reviewer decision, version pins, and final outcome. It should support provenance queries such as “which evidence authorized this action?” and “where did proxy and adjudicator disagree?”

### Context broker

Implement Agent-OS-style mediated context access with typed providers for memory, topology, GUI deltas, benchmark records, and experiment state. Each provider should return evidence objects with freshness, scope, and source identity rather than injecting unstructured text alone.

### Dual-loop evaluation

Use a fast screen for volume and a slow adjudicator for fidelity. Candidate examples are code-complexity proxies followed by calibrated execution, code-level QEC screening followed by circuit simulation, or noiseless emulation followed by noise-aware emulation and expert sign-off.

### Release-state verifier

For paper-linked software, automatically compare manuscript claims with the current README, license, releases, tests, and executable entry points. Report mismatch without assuming either source is universally authoritative.

### High-stakes escalation router

Route outputs to qualified reviewers based on consequence, uncertainty, novelty, evidence disagreement, and source freshness. Clinical, infrastructure-security, and physical-experiment actions should remain evaluation-only until explicitly authorized in an appropriate environment.

## Three Ways to Exercise This Research

### 1. Architecture tabletop

- **Objective:** Test whether an agent platform exposes the four recurring objects: typed artifact, fast evidence, slow adjudication, and durable trace.
- **Method:** Select one existing workflow, map every decision boundary, and identify its evidence source and escalation state.
- **Expected output:** A gate map with missing controls and provenance gaps.
- **Success criterion:** Every state-changing action has an identified evidence object, adjudicator, and accountable disposition.

### 2. Proxy-disagreement replay

- **Objective:** Measure how often a cheap proxy would approve a candidate that a slower evaluator rejects, or vice versa.
- **Method:** Replay a safe historical set through both stages, store paired scores, and classify disagreement causes.
- **Expected output:** A calibrated escalation policy and a ranked list of proxy failure modes.
- **Success criterion:** The team can state disagreement rate, impact-weighted miss rate, and review cost without deploying the candidate actions.

### 3. Repository-claim audit

- **Objective:** Detect gaps between a paper's implementation claims and the current public repository state.
- **Method:** Pin a paper and repository revision, inventory documented controls, tests, licenses, and entry points, and mark each claim supported, version-dependent, or unsupported.
- **Expected output:** A versioned readiness matrix.
- **Success criterion:** Operational claims are traceable to a commit or release, and mismatches have explicit follow-up owners.

## Example MVP Product

- **Name:** GateTrace
- **Target users:** Agent-platform engineers, evaluators, security reviewers, and research-operations teams.
- **Problem statement:** Agent systems can generate plausible actions without preserving the evidence, version state, proxy disagreement, or reviewer authorization that justified execution.
- **Value proposition:** GateTrace makes every consequential agent action reviewable as a compact evidence bundle before execution and auditable afterward.
- **Core workflow:** Ingest a proposed action and typed context; run a cheap domain-specific screen; invoke a slower independent evaluator when policy requires; route disagreements or high-impact cases to a reviewer; store the final decision and evidence trace.
- **Minimum features:** Typed evidence objects; source and version provenance; pluggable proxy and adjudicator adapters; policy-based escalation; append-only decision ledger; disagreement dashboard; sanitized export.
- **Inputs:** Agent proposal, source context, tool metadata, evaluator outputs, policy, source versions, and reviewer identity.
- **Outputs:** Decision state, evidence bundle, risk flags, adjudicator rationale, reviewer disposition, and public-safe audit record.
- **Non-goals:** Autonomous clinical diagnosis, live exploitation, unsupervised production patching, or direct QPU control.
- **Risks:** Evaluator correlation, misleading confidence scores, sensitive context retention, reviewer overload, proxy gaming, and false assurance from an incomplete trace.
- **Dependencies:** Identity and authorization, secure storage, versioned tool adapters, domain evaluators, and organization-specific policy.
- **Validation plan:** Start with non-production historical trajectories. Measure evidence completeness, proxy/adjudicator disagreement, escalation precision and recall against reviewer labels, review time, and export sanitization failures.
- **Success metrics:** At least 95% of sampled decisions have complete provenance; zero execution occurs without a required disposition; disagreement clusters are actionable; public exports pass sanitization; review time remains within an agreed budget.
- **Phased roadmap:** Phase 1 ledger and manual review; Phase 2 two safe evaluator adapters; Phase 3 replay analytics and policy simulation; Phase 4 limited authorized pilot with fail-closed execution.

## Related Research and Reading

All entries below are newly inspected in this initial pass.

| Topic | Reading | Relationship | Review Status |
|---|---|---|---|
| Governed memory | [MemLens](https://arxiv.org/abs/2607.25992) and its [official implementation](https://github.com/LIUHA1ZHU/MemLens) | Treats retained context as a valued, inspectable data object. | Paper and repository inspected; implementation not executed |
| Platform semantics | [Towards an Agent Operating System](https://arxiv.org/abs/2607.25076) and [rossoctl](https://github.com/rossoctl/rossoctl) | Supplies candidate primitives for lifecycle, tools, context, memory, security, failure, and observability. | Paper and prototype repository inspected; prototype not executed |
| Evaluation infrastructure | [Messier](https://arxiv.org/abs/2607.25891) | Recasts benchmark outputs as reusable verifier-level records. | Paper inspected; linked artifact inaccessible |
| Topology-aware remediation | [KuTIE](https://arxiv.org/abs/2607.25995), [VulnCare](https://github.com/dynatrace-research/vulncare), and [KuTIE artifacts](https://github.com/dynatrace-research/kutie-artifacts) | Demonstrates a context gate for dependency-sensitive infrastructure changes. | Paper and repositories inspected; artifacts not executed |
| Harness controls | [SHarD](https://arxiv.org/abs/2607.25890), [shard-demo](https://github.com/wrgore/shard-demo), and [agent-security-lab](https://github.com/wrgore/agent-security-lab) | Tests distributed sandbox, skill-scan, and tool controls; exposes a paper/current-README enforcement mismatch. | Paper and repositories inspected; tests not executed |
| Performance evidence | [Reinforcement Learning for Code Optimization](https://arxiv.org/abs/2607.25970) and related [BigOBench](https://github.com/facebookresearch/BigOBench) | Shows why timing calibration, correctness gates, and slower execution evidence are necessary. | Paper inspected; related repository inspected; paper-specific code not identified |
| Clinical evaluation | [ClinMM-Bench](https://arxiv.org/abs/2607.25933) | Tests progressive multimodal evidence and catalogs diagnostic reasoning failures. | Paper inspected; repository locator inaccessible; evaluation-only |
| GUI verification | [Desktop-Delta Bench](https://arxiv.org/abs/2607.26041) | Isolates whether agents understand the action-caused state transition. | Paper inspected; repository locator returned not found |
| Quantum design | [OmniQEC](https://arxiv.org/abs/2607.25865) | Uses a fast code proxy and slower circuit-level adjudication in QEC search. | Paper inspected; no paper-specific repository identified |
| Quantum execution | [Neutral-atom agentic workflows](https://arxiv.org/abs/2607.25834) and related [pasqal-cloud SDK](https://github.com/pasqal-io/pasqal-cloud) | Demonstrates emulator and expert gates before physical campaigns. | Paper and related SDK inspected; no workflow code identified or executed |

## Source References

1. Black-Lake-Data. “DEP-20260730-Tech Intel 0102.” `Black-Lake-Data/.lake-data/DEP-20260730-Tech Intel 0102/README.md`. Accessed 2026-07-30. https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260730-Tech%20Intel%200102
2. Black-Lake-Data. “Daily Research Findings - 2026-07-30 0102.” `Black-Lake-Data/.lake-data/DEP-20260730-Tech Intel 0102/daily_research_findings_2026-07-30_0102.md`. Accessed 2026-07-30. https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260730-Tech%20Intel%200102/daily_research_findings_2026-07-30_0102.md
3. Wei, Shuyue; Liu, Chang; Zhou, Zimu; Tong, Yongxin; Cui, Lizhen. “MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents.” arXiv:2607.25992v1, 2026. https://arxiv.org/abs/2607.25992
4. MemLens official implementation. Accessed 2026-07-30. https://github.com/LIUHA1ZHU/MemLens
5. Steinder, Gosia; Franke, Hubertus. “Towards an Agent Operating System - Lessons from Classical and Cloud OS.” arXiv:2607.25076v1, 2026. https://arxiv.org/abs/2607.25076
6. rossoctl. Official prototype repository. Accessed 2026-07-30. https://github.com/rossoctl/rossoctl
7. Krsteski, Stefan; Meyer, Charlotte; Allegre, Guillaume; O'Halloran, Tony; Sallinen, Alexandre. “Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation.” arXiv:2607.25891v1, 2026. https://arxiv.org/abs/2607.25891
8. Messier paper-linked artifact locator. Accessed 2026-07-30; inaccessible. https://anonymous.4open.science/r/messier-d3
9. Shaikh, Farooq. “Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?” arXiv:2607.25995v1, 2026. https://arxiv.org/abs/2607.25995
10. VulnCare official benchmark repository. Accessed 2026-07-30. https://github.com/dynatrace-research/vulncare
11. KuTIE official experiment artifacts. Accessed 2026-07-30. https://github.com/dynatrace-research/kutie-artifacts
12. Gore, William Robert. “Distributing Security Controls Through Harness Engineering.” arXiv:2607.25890v1, 2026. https://arxiv.org/abs/2607.25890
13. SHarD demonstration repository. Accessed 2026-07-30. https://github.com/wrgore/shard-demo
14. Agent Security Lab repository. Accessed 2026-07-30. https://github.com/wrgore/agent-security-lab
15. Chambon, Pierre; Zheng, Kunhao; Decugis, Juliette; Sagot, Benoit; Synnaeve, Gabriel. “Reinforcement Learning for Code Optimization.” arXiv:2607.25970v1, 2026. https://arxiv.org/abs/2607.25970
16. BigOBench. Related benchmark substrate, not the paper's implementation. Accessed 2026-07-30. https://github.com/facebookresearch/BigOBench
17. Yang, Rui; Xuan, Weihao; Lin, Yi; et al. “Evaluating Multi-Turn Multimodal Diagnostic Reasoning on Challenging Real-World Clinical Cases.” arXiv:2607.25933v1, 2026. https://arxiv.org/abs/2607.25933
18. ClinMM paper-linked repository. Accessed 2026-07-30; inaccessible. https://github.com/ruiyang-medinfo/ClinMM
19. Pillai, Abhishek; Nayak, Samir Kumar; Chen, Yuan. “Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?” arXiv:2607.26041v1, 2026. https://arxiv.org/abs/2607.26041
20. Desktop-Delta Bench paper-linked repository. Accessed 2026-07-30; returned not found. https://github.com/abhipi/DDB
21. Yan, Ge; Li, Shanchuan; Ma, Pengyue; Zhang, Qixin; Ma, Pingchuan; Wang, Jianping; Hsieh, Min-Hsiu; Du, Yuxuan. “OmniQEC: discovering practical quantum error-correcting codes by an AI scientist.” arXiv:2607.25865v1, 2026. https://arxiv.org/abs/2607.25865
22. Dalyac, Constantin; Dauphin, Alexandre; Henriet, Loïc; Jurczak, Christophe. “Lowering the implementation barrier of neutral-atom quantum computing with agentic workflows.” arXiv:2607.25834v1, 2026. https://arxiv.org/abs/2607.25834
23. pasqal-cloud. Related official SDK, not a paper workflow release. Accessed 2026-07-30. https://github.com/pasqal-io/pasqal-cloud

## Appendix

### Validation and collection record

- No external source files, datasets, models, benchmark outputs, container images, or repository snapshots were added to this DEP.
- The two selected source DEP Markdown files were inspected through the source repository and are represented with repository-relative paths and public URLs.
- External evidence was inspected at public URLs only.
- No code, tests, benchmarks, models, clusters, clinical workflows, simulators, or QPUs were executed.
- The Messier artifact locator was inaccessible, the ClinMM repository could not be opened, and the Desktop-Delta Bench repository returned not found.
- Security examples remain defensive and non-operational; medical content remains evaluation-only; quantum performance claims distinguish simulation from hardware execution.

### Synthesis trace

The “evidence-gated agents” framing is a reviewer-generated abstraction based on E12. It should be tested as a design hypothesis. The sources do not jointly claim a shared architecture, and their reported metrics are not directly comparable across domains.
