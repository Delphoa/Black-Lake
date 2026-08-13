---
title: "Evidence-Bound Agents - DEP-E"
generated_at: "2026-08-06T00:04:33Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of ten systems that bind agent behavior, evaluation, or generation to explicit evidence and deterministic constraints."
source_status: "URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-06"
temporal_cutoff: "2026-08-06"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260628-Tech%20Intel%201103"
stable_identifier: "DEP-20260628-Tech Intel 1103"
confidence_summary: "Medium-high for source-reported mechanisms and measurements; low for independent reproducibility because no code, data, models, or experiments were executed."
safety_scope: "defensive, evaluation-only, and non-clinical"
distribution_notes: "No original source files were collected or redistributed; only public URLs and derived analysis are deposited."
---

# Evidence-Bound Agents - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Source DEP README | Primary source package | Markdown | `DEP-20260628-Tech Intel 1103` | [Black-Lake-Data DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260628-Tech%20Intel%201103) | Repository-hosted source inventory and attribution record. | 2026-08-06 | Inspected in full. |
| S2 | Daily Research Findings | Primary source synthesis | Markdown | `daily_research_findings_2026-06-28_1103.md` | [Source findings](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260628-Tech%20Intel%201103/daily_research_findings_2026-06-28_1103.md) | Repository-hosted synthesis; claims were checked against the listed primary papers. | 2026-08-06 | Inspected in full. |
| S3 | *Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities*; Corban Villa, Sohee Kim, Austin Chu, Alon Shakevsky, Raluca Ada Popa | Primary paper | arXiv HTML | arXiv:2606.26933v1, 2026-06-25 | [arXiv](https://arxiv.org/abs/2606.26933) | CC BY 4.0 on the inspected arXiv HTML. | 2026-08-06 | Full HTML inspected. |
| S4 | *ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP*; Liwei Liu, Tianzhu Han, Zijian Liu, Zishu Dong, Na Ruan | Primary paper | arXiv HTML | arXiv:2606.27027v1, 2026-06-25 | [arXiv](https://arxiv.org/abs/2606.27027) | CC BY-NC-SA 4.0 on the inspected arXiv HTML. | 2026-08-06 | Full HTML inspected; security analysis kept defensive and non-operational. |
| S5 | *A Deterministic Control Plane for LLM Coding Agents*; Padmaraj Madatha | Primary paper | arXiv HTML | arXiv:2606.26924v1, 2026-06-25 | [arXiv](https://arxiv.org/abs/2606.26924) | arXiv perpetual non-exclusive license; companion artifact DOI listed by the source. | 2026-08-06 | Full HTML inspected. |
| S6 | *Memory Depth, Not Memory Access*; Haoliang Han | Primary paper | arXiv HTML | arXiv:2606.26806v1, 2026-06-25 | [arXiv](https://arxiv.org/abs/2606.26806) | arXiv perpetual non-exclusive license. | 2026-08-06 | Full HTML inspected. |
| S7 | *When Does Combining Language Models Help?*; Josef Chen | Primary paper | arXiv HTML | arXiv:2606.27288v1, 2026-06-25 | [arXiv](https://arxiv.org/abs/2606.27288) | CC BY 4.0 on the inspected arXiv HTML. | 2026-08-06 | Full HTML inspected. |
| S8 | *OpenRCA 2.0: From Outcome Labels to Causal Process Supervision*; Aoyang Fang, Yifan Yang, Jin'ao Shang, et al. | Primary paper | arXiv HTML | arXiv:2606.27154v2, 2026-06-30 | [arXiv](https://arxiv.org/abs/2606.27154) | CC BY-NC-SA 4.0 on the inspected arXiv HTML. | 2026-08-06 | Full HTML and appendix-level validity notes inspected. |
| S9 | *TAVR-VLM: Risk-Conditioned Causal Grounding for Hallucination-Resistant Report Generation*; Zhixiang Lu, Xiwei Liu, Sifan Song, Changkai Ji, Anh Nguyen, Jionglong Su, Imran Razzak, Jinfeng Wang | Primary paper | arXiv HTML | arXiv:2606.26874v1, 2026-06-25 | [arXiv](https://arxiv.org/abs/2606.26874) | arXiv perpetual non-exclusive license; medical claims are source-reported and not clinical guidance. | 2026-08-06 | Full HTML inspected. |
| S10 | *LithoDreamer: A Physics-Informed World Model for Multi-Stage Computational Lithography*; Yuqi Jiang, Yumeng Liu, Zimu Li, et al. | Primary paper | arXiv HTML | arXiv:2606.26713v1, 2026-06-25 | [arXiv](https://arxiv.org/abs/2606.26713) | CC BY-NC-ND 4.0 on the inspected arXiv HTML. | 2026-08-06 | Full HTML inspected. |
| S11 | *EGG: An Expert-Guided Agent Framework for Kernel Generation*; Yaochen Han, Ke Fan, Hongxu Jiang, Wanqi Xu, Weiyu Xie, Runhua Zhang, Chenhui Zhu, Yixiang Zhang | Primary paper | arXiv HTML | arXiv:2606.26758v1, 2026-06-25 | [arXiv](https://arxiv.org/abs/2606.26758) | arXiv perpetual non-exclusive license. | 2026-08-06 | Full HTML and appendix limitations inspected. |
| S12 | *Do Safety Guardrails Need to Reason? LeanGuard*; Dongbin Na | Primary paper | arXiv HTML | arXiv:2606.26686v1, 2026-06-25 | [arXiv](https://arxiv.org/abs/2606.26686) | arXiv perpetual non-exclusive license; paper links open-source code and models. | 2026-08-06 | Full HTML inspected; linked implementation was identified but not executed. |

No source files were collected. Repository-relative source paths and public URLs replace private execution paths.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Source DEP README | Inventory, source roles, tags, attribution block, and cross-item synthesis. | Source package identity and provenance boundary. | High | The README summarizes rather than independently validates the papers. |
| E2 | S2 | Source findings | Ten ranked findings, reported metrics, source links, and initial relevance claims. | Selection of the ten-paper research object and the original synthesis. | Medium | Generated synthesis; every material claim required primary-source cross-checking. |
| E3 | S3 | Primary paper | System design, 47-library/8-language evaluation, disclosure process, confirmed library findings, and downstream tracing caveats. | Evidence-backed vulnerability discovery can pair model search with deterministic differential signals. | High for paper contents; medium for generalization | Disclosure is ongoing; many downstream findings remain under investigation; CPU-bound baseline costs were not equalized. |
| E4 | S4 | Primary paper | Four-domain, 100-query evaluation across two MCP hosts and four models; attack-success, threshold, detector, and limitation results. | Independent tool vetting can miss cross-tool composition risk. | High for reported experiment; medium for deployment transfer | Mocked tool returns, manual prompt engineering, limited hosts/models, and real-world access controls constrain transfer. |
| E5 | S5 | Primary paper | 10,008-repository prevalence study, 237-definition conformance corpus, deterministic control mechanisms, and explicit non-causal limitations. | Agent configuration behaves like a supply-chain artifact and can be governed outside the model. | High for exact-duplicate finding; medium for other prevalence claims | Selection bias, incomplete fork metadata, fragile permission parser, and no developer-outcome study. |
| E6 | S6 | Primary paper | Synthetic loop-drift protocol, four-seed experiments, retrieval/consolidation comparison, actuation controls, and stale-memory limits. | Retrieval access and post-unload behavioral persistence are distinct memory functions. | Medium | Synthetic protocol, small backbones for the central result, weak paraphrase transfer, contamination, and unsolved forgetting. |
| E7 | S7 | Primary paper | 67-model/21-family measurements, co-failure bound, learned-router results, grading correction, cost record, and limitations. | Multi-model orchestration is bounded by common-mode failure and router realizability. | Medium-high for bounded-policy theorem; medium for empirical magnitude | Small all-wrong counts, benchmark and grading sensitivity, incomplete domain coverage, and no seed replication for some claims. |
| E8 | S8 | Primary paper | PAVE protocol, 500 instances across three systems and 27 fault types, 11-model evaluation, causal-path metrics, audit, and validity assumptions. | Outcome correctness can conceal unsupported diagnostic reasoning. | High for benchmark construction and reported evaluation | Requires controlled interventions, adequate dependency graphs, observable propagation, and representative baselines; transfer is bounded. |
| E9 | S9 | Primary paper | 1,482-patient multimodal cohort, patient-level split, R-CGA mechanism, comparative metrics, and ablations. | Domain-defined support constraints can reduce source-reported hallucination and improve grounding. | Medium | Single source paper, unclear external clinical validation, private cohort details, no deployment study, and no independent reproduction. |
| E10 | S10 | Primary paper | 280k training/20k in-domain/3k OOD samples, forward/inverse tasks, 28 nm cross-node test, metrics, and ablations. | Physics-informed latent constraints can stabilize a multi-stage world model in the tested lithography settings. | Medium-high for reported experiments | Industrial dataset access, commercial-simulator dependence, and external fab transfer were not independently examined. |
| E11 | S11 | Primary paper | KernelBench setup, four GPU platforms, staged multi-agent design, speedups, practical operators, ablations, and appendix limitations. | Expert-structured search can improve generated-kernel correctness and performance in the tested environment. | Medium-high | Hardware/software specificity, expert-prior bias, sequential local optima, token-budget dependence, and no independent run. |
| E12 | S12 | Primary paper | Same-base CoT ablation, 127,465-example corpus, three-seed evaluation, strict-FPR analysis, compute estimate, and limitations. | Reasoning traces are not automatically necessary for bounded moderation decisions. | High for same-base result; medium for broad deployment | Scope is standard moderation, not tool use or test-time reasoning; cross-architecture comparison is confounded. |

## Executive Summary

The ten works converge on a practical principle: an agentic system becomes more trustworthy when its decisions are bound to evidence or constraints that exist outside unconstrained language-model generation. In security, Chai uses deterministic cross-implementation disagreement as a validation signal, while ShareLock demonstrates why inspecting tools one at a time is insufficient when risk emerges only through composition [E3, E4]. In software governance, the deterministic control-plane study treats agent definitions as supply-chain objects and reports that 10.1% of tracked agent-configuration paths are exact duplicates across independent repositories after fork adjustment [E5].

The same pattern appears in memory and evaluation. Memory Depth separates retrieval of facts from durable post-unload behavior, but its strongest result remains a controlled synthetic mechanism study rather than a general memory solution [E6]. The co-failure work shows that routing, voting, and cascades cannot exceed the ceiling imposed when every member model fails on the same query; its 67-model measurement also shows that learned routing captured little of the available oracle gain in the tested pool [E7]. OpenRCA 2.0 makes reasoning auditable by scoring the causal path, not merely the final service label: across eleven evaluated models, exact root-cause-set recovery averaged 20.7%, while at least one correct service was named in 76.0% of cases and grounded in a verified path in 61.5% [E8].

Applied systems provide domain-specific variants of the same idea. TAVR-VLM constrains generated clinical entities through a risk-defined anatomical support and reports AUROC 0.896, CIDEr 0.936, hallucination rate 8.1%, and grounding mIoU 0.624 on its cohort [E9]. LithoDreamer constrains planning through stage-specific physics-informed latent spaces and reports in-domain EPE values of 1.58 nm, 0.96 nm, and 3.74 nm across mask, resist image, and ADI [E10]. EGG structures kernel search into expert-guided stages and reports 100% KernelBench correctness with 2.13x average speedup over PyTorch Eager in its setup [E11]. LeanGuard's controlled same-base comparison finds no moderation-accuracy benefit from chain-of-thought and shows a 395M encoder at 82.90 +/- 0.26 average F1, while explicitly limiting the claim to bounded moderation tasks [E12].

Reviewer interpretation: these papers do not establish one universal architecture. They form a reusable design test: identify the evidence boundary, encode it in deterministic checks or domain constraints, score the process as well as the outcome, and expose where the constraint stops being valid. Confidence is medium-high in this cross-source interpretation, but low in reproducibility because this review did not run source code, models, datasets, benchmarks, clinical workflows, fabrication simulators, or GPU experiments.

## Detailed Summary

### Problem Context

Modern agents operate through tools, persistent state, routing layers, generated code, and domain workflows. That expansion creates failure modes that outcome-only evaluation cannot reveal. A final answer can be correct for the wrong reason; a tool can look safe alone but become dangerous in combination; a memory system can recall a fact without preserving a goal; a generated kernel can compile without being fast; and a medical report can sound plausible without anatomical evidence. The source set addresses these problems by inserting checkable structure between model proposals and accepted outcomes.

### Security and Governance

Chai's mechanism begins with a deterministic discrepancy. An agent proposes protocol mutations, a builder produces reproducible test messages, and identical bytes are executed across implementations of X.509, JWT, or SAML. Disagreement supplies a signal that can be minimized, classified, reviewed, and traced into downstream dependency graphs. The evaluation spans 47 libraries and eight languages. The authors report two severe wolfSSL vulnerabilities confirmed and patched by maintainers, other library security bugs, and more than 100 downstream findings still under investigation. The important mechanism is not autonomous vulnerability prose; it is model-guided search coupled to a replayable differential oracle and human disclosure review [E3].

ShareLock tests the opposite boundary. It distributes an instruction across multiple tool descriptions using a threshold scheme, so isolated shares do not expose the composite payload. The evaluation uses 100 multi-step queries across travel, coding, finance, and office scenarios; Cherry Studio and Cline; and four model families. Average attack success is high in the tested settings, but the paper also notes mocked tool responses, manually engineered prompts, and possible failure under strict consent or access-control policies. Defensively, the result argues for graph-level inspection of tool bundles, runtime composition checks, least privilege, and user confirmation for sensitive actions [E4].

The deterministic control-plane paper shifts attention from tool payloads to the configuration layer. Its repository study analyzes 10,008 public repositories, 33,620 files, and 6,145 agent configurations. The strongest reported prevalence result is fork-adjusted exact duplication of 10.1% of tracked configuration paths, with 75.5% of raw clone pairs crossing organizational boundaries. Rel(AI)Build is offered as a reference architecture using content addressing, stamped lockfiles, hash-chained audit records, permission tiers, blocklists, phase gates, and compilation to seven IDE formats. Its 237-definition conformance corpus shows that injected violations trigger the intended detectors; the authors explicitly warn that these tests do not establish developer outcomes or field effectiveness [E5].

### Memory, Routing, and Process Evaluation

Memory Depth defines *memory access* as retrieving stored information and *memory depth* as preserving goal-conditioned behavioral tendencies after working context is unloaded. Its loop-drift protocol gives each of ten users 200 synthetic events with goals, distractors, transient requests, conflicts, contamination, and factual notes. Retrieval dominates shallow factual probes, while EVAF's selective LoRA writes improve goal persistence and post-unload recovery in the tested small-model settings. The paper is careful about its limits: paraphrase transfer is weak, contamination rises under strong actuation, the public boundary diagnostic is not statistically significant, and stale-memory deletion remains unsolved [E6].

The co-failure paper supplies a formal and empirical constraint for systems that choose among member-model answers. If every model is wrong on a fraction `beta` of queries, no router, vote, or cascade restricted to those answers can exceed accuracy `1 - beta`. Pairwise error correlation cannot identify this all-wrong tail. In a live pool of 67 models from 21 provider families, the paper reports populated co-failure tails on open-ended mathematics, limited counts in some domains, and a deployable router that captures essentially none of the oracle gain in the tested pool. The authors also document a grading bug they corrected before reporting results, a useful example of evaluation provenance affecting conclusions [E7].

OpenRCA 2.0 turns process evidence into the benchmark target. PAVE starts from a known fault injection and admits a causal edge only when structural rules, baseline-relative anomaly evidence, and temporal alignment agree. The dataset contains 500 evaluable instances across TrainTicket, OpenTelemetry Demo, and DeathStarBench Hotel Reservation, with 27 fault types and 7.5 causal edges per instance on average. Eleven frontier models average 20.7% exact root-cause-set recovery and 34.1% outcome F1; process metrics reveal when a correct service name lacks a verified propagation path. The paper's validity boundary is explicit: the method needs a controlled intervention, a sufficiently complete dependency graph, observable propagation, and a representative pre-injection baseline [E8].

### Domain-Constrained Generation and Optimization

TAVR-VLM uses a predicted procedural-risk state to create a global anatomical risk mask. A support projection then constrains token-level grounding to that mask while preventing the language loss from expanding the support. The source reports a 1,482-patient cohort with CT, echocardiography, biomarkers, risk labels, and clinician-authored reports; a patient-level 70/10/20 split; and expert regions for a test subset. The reported gains over Gemini-3 Pro are modest for AUROC and CIDEr but larger for hallucination and grounding. These are source-reported retrospective benchmark results, not evidence of clinical safety, prospective benefit, or regulatory readiness [E9].

LithoDreamer formulates lithography as an evolution from layout to mask, resist image, and after-development image. It learns stage-specific latent spaces, a policy over interventions, and a transition model. Training uses 280,000 samples from 36 process configurations at 55 nm, with 20,000 in-domain test samples, 3,000 same-node OOD samples, and a public 28 nm cross-node dataset. Strong ablations support the role of stage-specific latent directions and stochastic intervention modeling. Transfer to different industrial processes, manufacturing equipment, and yield outcomes remains unverified here [E10].

EGG decomposes GPU kernel optimization into algorithmic refinement and hardware-specific tuning, coordinated by code, profiling, and debugging agents through structured context. The main evaluation uses 250 KernelBench tasks, CUDA 13.0, PyTorch 2.9.1, Triton 3.5.1, an RTX 4090, and primarily GPT-5.1; appendices add three GPU platforms and another model. The paper reports 100% correctness, 87.6% `Fast_1`, and 2.13x average speedup over PyTorch Eager, with real-workload gains of 1.24x, 1.63x, and 1.08x on three TritonBench operators. Its limitations identify expert-prior bias and missed cross-stage interactions [E11].

LeanGuard asks whether moderation requires a generated chain of thought. It uses 127,465 public training examples and holds data, schedule, and base architecture fixed while removing the reasoning target. On Llama-3.2-1B, average F1 is 81.35 with CoT and 81.42 label-only; the 395M ModernBERT encoder reaches 82.90 +/- 0.26 across three seeds. At 1% false-positive rate, the source reports 44.8 true-positive rate for the encoder and 10.1 for the reasoning guard. The authors limit the conclusion to standard moderation and distinguish accuracy from the separate operational value of an auditable rationale [E12].

### Cross-Source Mechanism

Across the ten works, proposals remain probabilistic but acceptance becomes structured. Chai accepts reproducible discrepancies; the control plane accepts policy-conformant transitions; OpenRCA accepts causally verified edges; TAVR-VLM accepts token grounding inside risk support; LithoDreamer restricts transitions to learned physical directions; EGG accepts kernels that compile, pass correctness, and beat latency baselines; LeanGuard asks whether extra generated reasoning changes the decision at all. ShareLock and the co-failure analysis supply negative cases: independent checks and large model pools do not guarantee safety when failures compose.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Chai reports evaluation across 47 libraries and eight languages, confirmed severe library findings, and more than 100 downstream findings under investigation. | Source-reported empirical claim | E3 | The deterministic differential signal is directly described; downstream scope remains provisional. | Medium-high |
| C2 | ShareLock reports high attack success in its tested multi-tool environments, showing that isolated tool inspection can miss a composed payload. | Source-reported empirical claim | E4 | Strong within the synthetic setup; real-world transfer depends on host controls and human approval. | Medium |
| C3 | Fork-adjusted exact duplicates appear in 10.1% of tracked agent-configuration paths in the 10,008-repository corpus. | Source-reported measurement | E5 | This is the paper's strongest prevalence result; it is not causal evidence of compromise. | High |
| C4 | Retrieval and selective parametric consolidation serve different memory functions in the loop-drift protocol. | Source claim plus reviewer interpretation | E6 | Mechanistically useful, but the central evidence is synthetic and small-model. | Medium |
| C5 | All-model co-failure provides a ceiling for answer-selection policies, and pairwise correlation does not identify that ceiling. | Theoretical claim with empirical illustration | E7 | The bound is clear for the stated policy class; empirical tail estimates are sample-sensitive. | High for theorem; medium for magnitude |
| C6 | OpenRCA 2.0 reveals a measurable gap between naming a correct service and grounding it in a verified causal path. | Source-reported benchmark result | E8 | Strong evidence that outcome-only scoring hides process failures in the benchmark conditions. | High |
| C7 | TAVR-VLM reports AUROC 0.896, CIDEr 0.936, 8.1% hallucination rate, and grounding mIoU 0.624 on its cohort. | Source-reported empirical claim | E9 | Metrics are precise but not independently reproduced or prospectively validated. | Medium |
| C8 | LithoDreamer reports 1-4 nm in-domain EPE across three stages and OOD gains under the tested lithography distributions. | Source-reported empirical claim | E10 | Supported by tables and ablations; industrial generalization remains open. | Medium-high |
| C9 | EGG reports 100% correctness and 2.13x average speedup over PyTorch Eager in its KernelBench setup. | Source-reported empirical claim | E11 | Strong within pinned hardware/software; speed is environment-sensitive. | Medium-high |
| C10 | A same-base LeanGuard ablation finds no F1 gain from CoT for standard moderation. | Source-reported controlled result | E12 | The ablation isolates the training target; it does not settle tool-mediated or genuinely multi-step safety decisions. | High |
| C11 | Trustworthy agent systems should bind acceptance to evidence outside free-form generation and measure failure composition. | Reviewer interpretation | E3-E12 | Consistent across diverse systems, but it is a design synthesis rather than a directly tested universal law. | Medium-high |

## Methodology

- `Research objective`: Determine what the selected DEP's ten papers collectively show about evidence-bound, constrained, and process-auditable agentic systems, while preserving source provenance and limitations.
- `Sources inspected`: The complete source DEP README and findings Markdown, plus the complete official arXiv HTML for all ten cited papers, including methods, experiments, result tables, appendices, and limitation or validity sections where present.
- `Discovery strategy`: Started from repository-local DEP files, followed their canonical arXiv identifiers directly, inspected full official HTML, and followed only official artifact links needed to identify availability. No secondary news or commentary was used as evidence.
- `Inclusion criteria`: All ten findings in the selected DEP; primary or near-primary records; mechanism, experimental setup, quantitative results, ablations, and disclosed limitations relevant to the cross-source question.
- `Exclusion criteria`: Unsupported implications from the source synthesis, exploit-enabling operational detail, uninspected secondary commentary, and claims requiring execution of unavailable code, data, models, clinical systems, fabrication tools, or GPUs.
- `Analytical approach`: Conceptual, empirical, comparative, implementation, safety and ethics, product research, and replication analysis.
- `Evidence handling`: Source-synthesis claims were treated as hypotheses until checked against the paper. Major claims were mapped to evidence IDs; author claims, reviewer interpretation, and inference are labeled separately.
- `Uncertainty handling`: Missing replication, private or industrial data, synthetic setups, limited external validity, small tail counts, and inaccessible runtime artifacts are stated rather than inferred away.
- `Extraction process`: Read source Markdown, paper navigation, methods, main and appendix result tables, threats to validity, and implementation-availability statements. Metrics were transcribed from the inspected primary HTML and cross-checked against surrounding text.
- `Version control`: Paper versions were recorded from the inspected arXiv HTML; OpenRCA 2.0 was inspected at v2 and the other nine at v1. Repository sources are linked to the public default branch as accessed on 2026-08-06.
- `Safety handling`: Security papers are summarized for defensive architecture and evaluation. No payload construction, exploitation sequence, or target-specific procedure is reproduced. Medical content is non-clinical research review only.
- `Reviewer stance`: DEP-ready synthesis, critique, product translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: Ten papers listed by `DEP-20260628-Tech Intel 1103`, reviewed as a coherent evidence-bound agent-systems research object.
- `Temporal boundary`: Sources available and inspected through 2026-08-06; later paper revisions, code releases, corrections, and benchmark updates are outside this pass.
- `Evidence limits`: No PDF files, source packages, repositories, datasets, model weights, prompts, benchmarks, clinical records, simulators, or hardware experiments were downloaded or executed. Official HTML rendering omitted some math glyphs in Memory Depth, so this artifact avoids unsupported numeric cells from those omissions.
- `Assumptions`: Canonical arXiv HTML accurately represents the listed paper versions; source-reported measurements are transcribed faithfully but remain unverified until reproduced.
- `Constraints`: Public-only evidence; repository-safe provenance; no redistribution of source files; defensive treatment of dual-use security research; no clinical or fabrication decision support.
- `Out of scope`: Independent vulnerability validation, real MCP exploitation, medical diagnosis, fab-process validation, full benchmark reproduction, model training, GPU tuning, cost normalization across all systems, or deployment readiness certification.
- `Intended use`: Research review, DEP deposition, design guidance, evaluation planning, and a provenance-preserving seed for future expansion.
- `Audience`: Agent-platform engineers, research reviewers, evaluation designers, security engineers, ML-systems engineers, and product leads.
- `Reproducibility boundary`: The paper methods and public locators are preserved; none of the central empirical results were independently reproduced in this pass.
- `Data sensitivity`: Repository sources and papers are public. The TAVR cohort and industrial lithography data may contain restricted or proprietary material; no such data was accessed.

## Observations

- `Observed pattern`: The most credible systems do not ask an LLM to certify itself. They use replayable tests, hashes, state machines, causal annotations, support masks, physical constraints, or benchmark execution as independent evidence.
- `Observed pattern`: Process-level evidence repeatedly changes the interpretation of outcome success. OpenRCA exposes unsupported correct labels; Chai distinguishes model suggestions from confirmed disclosures; EGG requires both correctness and latency; LeanGuard tests whether the reasoning trace changes the verdict.
- `Technical implication`: Validation should be designed as a graph when risks compose. ShareLock's cross-tool payload and the co-failure tail both defeat local or pairwise summaries.
- `Technical implication`: Memory safety needs validity and deletion semantics, not only retrieval and writing. Memory Depth makes the missing stale-memory boundary explicit.
- `Contradiction or tension`: Deterministic control improves auditability but can encode incomplete policies. The control-plane blocklists detect constructed violations, while ShareLock shows that composition can evade isolated rules.
- `Contradiction or tension`: Domain constraints improve reported metrics but can transfer poorly. TAVR-VLM and LithoDreamer are strongest where their risk or physics priors match the data-generating process.
- `Open question`: What minimal evidence-receipt schema can cover tool calls, memory updates, causal diagnoses, generated code, and domain-grounded text without exposing sensitive content?
- `Reviewer hypothesis`: A practical agent platform should separate proposal, evidence collection, deterministic admission, and post-hoc audit into distinct interfaces rather than treating them as one model response.

## Considerations

- Evidence checks inherit their own failure modes. Hashes prove identity, not safety; causal rules can omit propagation mechanisms; support masks can encode biased or incomplete clinical labels; and benchmark tests can overfit a specific environment.
- Tool and configuration ecosystems require transitive provenance. Signing one file or approving one server is inadequate if combined behavior changes across versions or invocation sequences.
- Process telemetry can be sensitive. Audit records should store hashes, typed receipts, thresholds, and minimal summaries by default, with raw content access controlled and retained only when justified.
- Medical and industrial deployments need prospective validation, external sites or processes, human authority, rollback, and incident reporting. Source-reported benchmark gains do not establish operational benefit.
- GPU and model-routing economics are time-sensitive. Hardware, compilers, prices, provider models, and market churn can invalidate measured frontiers quickly.
- Defensive security research should preserve enough detail for authorized evaluation without publishing turnkey exploitation paths. This artifact therefore emphasizes threat models and controls, not attack reproduction.
- Human review remains a primary backstop when the evidence boundary is ambiguous, high impact, or outside the validated distribution.

## Strengths

- The source set spans security, governance, memory, evaluation, medicine, manufacturing, systems optimization, and moderation, making the cross-domain mechanism visible without relying on a single benchmark.
- Several works provide unusually explicit negative evidence: the control-plane paper distinguishes conformance from effectiveness; Memory Depth disclaims universal memory; the co-failure paper documents grading correction and small tails; OpenRCA states falsifiable input assumptions; LeanGuard separates accuracy from rationale value.
- Chai, OpenRCA, LithoDreamer, EGG, and LeanGuard expose concrete evaluation mechanisms rather than only architectural descriptions.
- The selected papers provide complementary threat directions: how to bind accepted behavior to evidence and how local validation fails under composition.
- Primary-source HTML, stable identifiers, versions, and license visibility support follow-on review without redistributing source files.

## Weaknesses

- All ten works are recent preprints in the inspected source set; peer-review status and later revisions were not independently established.
- This review did not execute any code or inspect underlying datasets, models, clinical records, fabrication tools, or hardware logs, so reproducibility confidence is necessarily limited.
- Cross-domain synthesis risks flattening important differences between security oracles, causal evaluation, physical priors, and performance benchmarks.
- Some results depend on synthetic or private data: ShareLock uses mocked responses; Memory Depth uses a synthetic protocol; TAVR-VLM uses a cohort not inspected here; LithoDreamer uses industrial data and a commercial simulator.
- Measured improvements are not directly comparable because tasks, baselines, budgets, models, and validation regimes differ.
- Implementation availability was identified only where explicitly linked; repositories were not pinned to commits or audited for completeness.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Standardize typed evidence receipts | Cross-system governance | Current evidence objects are domain-specific and difficult to compose. | Enables common audit, expiration, conflict, and provenance logic. | Schema ossification or leakage of sensitive metadata. | Test on synthetic tool, memory, RCA, kernel, and medical fixtures. |
| Add composition-aware policy tests | MCP and agent configurations | Local checks miss threshold and sequence-dependent behavior. | Detects cross-tool and cross-file emergent risk. | Combinatorial growth and false positives. | Generate bounded tool graphs with known benign and malicious compositions. |
| Couple outcome and process metrics | Agent evaluation | Outcome-only scores hide unsupported paths. | Rewards evidence-grounded decisions and exposes shortcut behavior. | Annotation and telemetry burden. | Compare rankings under outcome-only versus receipt-aware scoring. |
| Add validity, revocation, and conflict controls | Agent memory | Selective writing does not solve stale or contradictory memory. | Safer long-running behavior and auditable deletion. | Over-forgetting and governance complexity. | Use synthetic lifecycle tests with expiry, correction, and deletion requests. |
| Reproduce under frozen environments | Empirical claims | Reported gains may depend on versions, hardware, or private data. | Distinguishes mechanism from environment-specific performance. | Compute, access, license, and expertise costs. | Pin code, model, data, dependencies, hardware, seeds, and negative controls. |
| Validate constraints out of distribution | Medical and physical systems | Domain priors can fail when labels, equipment, or populations shift. | Better transfer and calibrated abstention. | Requires protected data and expert oversight. | External-site/process evaluation with pre-registered stop rules. |

## Potential Implementations

### Evidence Receipt Gateway

- `User`: Agent-platform and security teams.
- `Goal`: Prevent high-impact agent actions from being accepted without typed, independently checkable evidence.
- `Core mechanism`: Separate proposal from admission; require receipts such as test outcomes, content hashes, permission decisions, provenance pins, and human approvals.
- `Required inputs`: Proposed action, policy, target resource, test results, source identifiers, and risk tier.
- `Outputs`: Admit, reject, or escalate decision plus a minimal audit record.
- `Risk controls`: Least privilege, redaction, retention limits, signature verification, replay protection, and human override.
- `Evaluation`: Synthetic missing, stale, conflicting, forged, and cross-tool receipt cases.

### Composition-Aware Tool Auditor

- `User`: MCP host operators and plugin marketplaces.
- `Goal`: Detect risk that appears only when several tools, descriptions, or return values are combined.
- `Core mechanism`: Build a tool-invocation graph, analyze threshold and sequence conditions, sandbox dry runs, and require confirmation for sensitive edges.
- `Required inputs`: Versioned tool manifests, schemas, declared permissions, invocation traces, and host policy.
- `Outputs`: Composition-risk report, blocked edges, and review queue.
- `Risk controls`: Authorized test environment, no live credentials, bounded search, and conservative handling of uncertain findings.
- `Evaluation`: Public toy servers with seeded cross-tool conditions and benign controls.

### Process-Grounded Evaluation Harness

- `User`: Benchmark maintainers and agent developers.
- `Goal`: Score whether an agent's path is supported, not only whether its final answer is correct.
- `Core mechanism`: Attach typed evidence edges to each step and compute outcome, path reachability, evidence precision/recall, and unsupported-success rates.
- `Required inputs`: Task graph, allowed tools, ground-truth interventions or checkpoints, receipts, and final outputs.
- `Outputs`: Outcome score, process score, failure taxonomy, and replay bundle.
- `Risk controls`: Sensitive trace redaction, deterministic graders where possible, and uncertainty labels where causal ground truth is unavailable.
- `Evaluation`: RCA-style synthetic systems, code tasks with tests, and tool workflows with known dependencies.

### Memory Validity Ledger

- `User`: Builders of long-running assistants.
- `Goal`: Distinguish retrieved facts, behavioral preferences, temporary instructions, and revoked memories.
- `Core mechanism`: Store provenance, validity interval, supersession relation, confidence, and deletion state separately from content and parametric actuation.
- `Required inputs`: Event type, source, user authorization, expiry, conflicts, and consolidation proposal.
- `Outputs`: Retrieval set, actuation decision, conflict warning, and revocation receipt.
- `Risk controls`: Local-first storage, user inspection, hard deletion, no silent parametric writing, and bounded actuation.
- `Evaluation`: Synthetic users with conflicts, contamination, scheduled expiry, and post-unload probes.

### Constraint Adapter Registry

- `User`: Medical-AI, manufacturing, and ML-systems teams.
- `Goal`: Make domain constraints versioned, testable, and replaceable rather than implicit in prompts.
- `Core mechanism`: Register support masks, physical transition rules, compiler tests, latency thresholds, and abstention criteria as pinned adapters.
- `Required inputs`: Domain specification, validation dataset, constraint version, acceptance metrics, and expert sign-off.
- `Outputs`: Constraint verdicts, violation traces, calibration reports, and rollback artifacts.
- `Risk controls`: External validation, expert authority, versioned rollback, OOD detection, and prohibited autonomous deployment in high-stakes settings.
- `Evaluation`: Frozen in-domain, shifted, adversarial, and negative-control suites.

## Three Ways to Exercise This Research

1. `Receipt completeness lab`: Objective: test admission logic without sensitive systems. Inputs: synthetic action proposals and receipts with seeded missing, expired, conflicting, or forged fields. Method: run a deterministic validator and compare its decisions with the fixture truth. Output: confusion matrix and failure log. Success criterion: every seeded invalid receipt is rejected or escalated while benign controls pass. Stop condition: any validator path performs an external action or logs raw secrets.
2. `Composition-risk sandbox`: Objective: measure whether local tool checks miss graph-level behavior. Inputs: three to five toy tools, versioned descriptions, mocked returns, and a declared permission policy. Method: compare isolated inspection with bounded sequence-aware simulation. Output: a graph of locally benign but composition-sensitive paths. Success criterion: seeded cross-tool conditions are detected with documented false positives. Stop condition: any test requires real credentials, production services, or operational exploit payloads.
3. `Outcome-versus-process benchmark`: Objective: quantify unsupported success. Inputs: a small synthetic RCA or code workflow with known causal or test checkpoints. Method: score final answers and evidence paths separately, then compare system rankings. Output: outcome score, process score, and unsupported-success rate. Success criterion: the harness identifies intentionally correct answers with invalid paths. Stop condition: ground truth is ambiguous enough that path labels cannot be independently verified.

## Example MVP Product

- `Product name`: Evidence Gate
- `Target user`: Teams deploying tool-using coding, operations, research, or internal workflow agents.
- `Problem`: Agent actions are often admitted on persuasive output or final-task success without a checkable record of provenance, permissions, tests, and process evidence.
- `Core workflow`: The agent submits an action proposal and typed receipts; deterministic validators check identity, permission, freshness, test outcomes, and composition constraints; low-risk valid actions proceed; uncertain or high-impact actions enter human review; every decision produces a minimal audit receipt.
- `Data requirements`: Versioned policy, action schema, target identifiers, hashes, test results, tool manifests, approval records, and optional redacted process edges. Synthetic data is sufficient for the MVP.
- `Architecture`: Local policy engine; signed receipt store; plugin validators for hashes, tests, tool graphs, and process paths; decision API; redacted audit viewer; no model is allowed to override a deterministic reject.
- `Success metrics`: Invalid-receipt detection rate; benign false-positive rate; unsupported-success rate; percentage of high-impact actions with complete receipts; time to human decision; receipt replay success; zero sensitive-content leaks in audit logs.
- `Risk controls`: Least privilege, default deny for missing high-impact evidence, content minimization, encryption, retention limits, replay protection, human authority, rollback, and an explicit ban on autonomous clinical or security-critical deployment.
- `Limitations`: The gate can enforce only encoded policy; it cannot prove semantic safety, complete a missing threat model, validate private data it cannot access, or guarantee correctness under unknown composition.
- `MVP boundary`: Synthetic/local tool actions, file changes in a sandbox, and test receipts only; no production credentials, patient data, live infrastructure changes, or exploit validation.
- `Deployment model`: Local service or CI sidecar with a browser-based audit view.
- `Evaluation plan`: Unit tests for each validator, adversarial receipt fixtures, composition tests, offline replay, and reviewer usability sessions.
- `Failure modes`: Incomplete policies, stale constraint adapters, forged upstream evidence, overblocking, metadata leakage, and humans approving without reviewing evidence.
- `Maintenance plan`: Version policies and validators, expire old receipts, review false positives monthly, re-run composition fixtures on tool updates, and require independent approval for high-impact rule changes.

## Related Research and Reading

Pass status: All entries below are new in this initial processing pass; there was no prior direct DEP Class artifact, source report, output log, or Report-Mark for the selected DEP.

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| *Chai: Agentic Discovery of Cryptographic Misuse Vulnerabilities* | Primary paper | Deterministic differential evidence for agent-guided security discovery. | [arXiv:2606.26933](https://arxiv.org/abs/2606.26933) |
| *ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP* | Primary paper | Demonstrates composition risk that isolated tool checks can miss. | [arXiv:2606.27027](https://arxiv.org/abs/2606.27027) |
| *A Deterministic Control Plane for LLM Coding Agents* | Primary paper and companion artifact | Treats agent definitions as governed supply-chain objects. | [arXiv:2606.26924](https://arxiv.org/abs/2606.26924); [Zenodo](https://doi.org/10.5281/zenodo.20780913) |
| *Memory Depth, Not Memory Access* | Primary paper | Separates retrieval from durable post-unload behavioral actuation. | [arXiv:2606.26806](https://arxiv.org/abs/2606.26806) |
| *When Does Combining Language Models Help?* | Primary paper | Formalizes common-mode co-failure and router realizability limits. | [arXiv:2606.27288](https://arxiv.org/abs/2606.27288) |
| *OpenRCA 2.0* | Primary paper and benchmark | Provides causal-path annotations and process-level agent metrics. | [arXiv:2606.27154](https://arxiv.org/abs/2606.27154) |
| *TAVR-VLM* | Primary paper | Tests risk-defined anatomical support for grounded report generation. | [arXiv:2606.26874](https://arxiv.org/abs/2606.26874) |
| *LithoDreamer* | Primary paper | Applies physics-informed latent constraints to multi-stage planning. | [arXiv:2606.26713](https://arxiv.org/abs/2606.26713) |
| *EGG* | Primary paper | Uses expert-guided staged search plus executable correctness and latency evidence. | [arXiv:2606.26758](https://arxiv.org/abs/2606.26758) |
| *LeanGuard* | Primary paper and implementation | Controlled test of whether generated reasoning changes moderation performance. | [arXiv:2606.26686](https://arxiv.org/abs/2606.26686); [repository](https://github.com/ndb796/LeanGuard) |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | [Selected source DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260628-Tech%20Intel%201103) | Source inventory, original synthesis, and provenance boundary. | 2026-08-06 | Both repository Markdown files were inspected; no external source files were collected. |
| R2 | [Daily research findings](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260628-Tech%20Intel%201103/daily_research_findings_2026-06-28_1103.md) | Original ten-item ranking and reported relevance. | 2026-08-06 | Used as a locator and hypothesis source, not as sole evidence for paper claims. |
| R3 | [Chai, arXiv:2606.26933v1](https://arxiv.org/abs/2606.26933) | E3; differential testing, discrepancy tracing, evaluation, disclosure, and limitations. | 2026-08-06 | Full official arXiv HTML inspected; source file not collected. |
| R4 | [ShareLock, arXiv:2606.27027v1](https://arxiv.org/abs/2606.27027) | E4; threshold composition threat, evaluation, adaptive defenses, and limitations. | 2026-08-06 | Full official arXiv HTML inspected; defensive summary only. |
| R5 | [Deterministic Control Plane, arXiv:2606.26924v1](https://arxiv.org/abs/2606.26924) | E5; repository study, control architecture, conformance tests, and limitations. | 2026-08-06 | Full official arXiv HTML inspected. |
| R6 | [Companion artifact DOI](https://doi.org/10.5281/zenodo.20780913) | Availability locator reported by the control-plane source. | 2026-08-06 | Identified from the primary paper/source DEP; artifact contents were not downloaded or executed. |
| R7 | [Memory Depth, arXiv:2606.26806v1](https://arxiv.org/abs/2606.26806) | E6; loop-drift protocol, depth flip, controls, and limitations. | 2026-08-06 | Full official arXiv HTML inspected; some rendered math cells were blank. |
| R8 | [Co-Failure Ceiling, arXiv:2606.27288v1](https://arxiv.org/abs/2606.27288) | E7; theorem, 67-model measurement, router results, grading correction, and limitations. | 2026-08-06 | Full official arXiv HTML inspected. |
| R9 | [OpenRCA 2.0, arXiv:2606.27154v2](https://arxiv.org/abs/2606.27154) | E8; PAVE, dataset, process metrics, audit, and threats to validity. | 2026-08-06 | Full official arXiv HTML and appendix sections inspected. |
| R10 | [TAVR-VLM, arXiv:2606.26874v1](https://arxiv.org/abs/2606.26874) | E9; cohort, risk-conditioned grounding, metrics, and ablations. | 2026-08-06 | Full official arXiv HTML inspected; no patient data accessed. |
| R11 | [LithoDreamer, arXiv:2606.26713v1](https://arxiv.org/abs/2606.26713) | E10; datasets, physics-informed stages, metrics, OOD tests, and ablations. | 2026-08-06 | Full official arXiv HTML inspected; no industrial data or simulator accessed. |
| R12 | [EGG, arXiv:2606.26758v1](https://arxiv.org/abs/2606.26758) | E11; staged multi-agent method, KernelBench, hardware results, and limitations. | 2026-08-06 | Full official arXiv HTML and appendix limitations inspected; no GPU run performed. |
| R13 | [LeanGuard, arXiv:2606.26686v1](https://arxiv.org/abs/2606.26686) | E12; same-base ablation, robustness, strict-FPR result, and limitations. | 2026-08-06 | Full official arXiv HTML inspected. |
| R14 | [LeanGuard repository](https://github.com/ndb796/LeanGuard) | Public implementation locator stated by the paper. | 2026-08-06 | Availability identified; repository code and models were not cloned or executed. |
| R15 | [LeanGuard project page](https://ndb796.github.io/LeanGuard) | Official project-context locator stated by the paper. | 2026-08-06 | Identified but not used as evidence for metrics. |

## Appendix

### Source Inventory

- Collected source files: none.
- Repository source files inspected: `Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 1103/README.md` and `Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 1103/daily_research_findings_2026-06-28_1103.md`.
- External sources inspected: ten official arXiv HTML papers listed in `## Source References`.
- Implementations identified but not executed: the control-plane companion artifact and LeanGuard repository/project page.

### Replication Checklist

- [ ] Pin every paper revision, repository commit, dataset revision, model version, and dependency lockfile.
- [ ] Confirm licenses and access conditions before downloading or redistributing any dataset or model.
- [ ] Reproduce one bounded result at a time with source-reported and negative-control configurations.
- [ ] Preserve seeds, hardware, software, budgets, prompts, thresholds, grader versions, and raw failure counts.
- [ ] Separate deterministic conformance from field effectiveness and benchmark success from deployment readiness.
- [ ] For security research, use only authorized synthetic targets and coordinate disclosures.
- [ ] For medical or fabrication research, require domain-expert review and approved data governance.

### Review Boundary

This artifact is a source-grounded review and design synthesis. It is not a clinical recommendation, vulnerability disclosure, product certification, benchmark reproduction, or claim that any cited implementation is safe for deployment.
