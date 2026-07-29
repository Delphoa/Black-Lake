---
title: "Agent Reliability Gates - DEP-E"
generated_at: "2026-07-27T15:06:54Z"
artifact_type: "DEP research artifact"
primary_subject: "Cross-domain evidence on verification, routing, memory, auditability, rejection, and intervention mechanisms around AI-agent inference."
source_status: "URLs only; two repository Markdown sources and ten primary papers inspected; no external source files collected"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-28"
temporal_cutoff: "Primary-source versions available on 2026-07-28"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/f375b375aa053b8e5bd84cb2a49f3bc95a5d4a39/.lake-data/DEP-20260713-Tech%20Intel%201301"
stable_identifier: "Black-Lake-Data DEP-20260713-Tech Intel 1301"
confidence_summary: "Medium-high for source description and reported results; medium for cross-domain synthesis because no inspected work evaluates the proposed gate stack end to end."
safety_scope: "Defensive, evaluation-only, research-planning, and authorized-testbed framing"
distribution_notes: "Public URLs and repository-relative provenance only; no source payloads redistributed."
---

# Agent Reliability Gates - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S0 | DEP-20260713-Tech Intel 1301 | Primary source bundle | Git repository snapshot | `f375b375aa053b8e5bd84cb2a49f3bc95a5d4a39` | [Selected DEP](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/f375b375aa053b8e5bd84cb2a49f3bc95a5d4a39/.lake-data/DEP-20260713-Tech%20Intel%201301) | Repository material; public attribution preserved | 2026-07-28 | Both Markdown files inspected in full |
| S1 | Selected DEP README | Source inventory and attribution | Markdown | Snapshot above | [README](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/f375b375aa053b8e5bd84cb2a49f3bc95a5d4a39/.lake-data/DEP-20260713-Tech%20Intel%201301/README.md) | Repository material | 2026-07-28 | Inspected in full |
| S2 | Daily Research Findings | Original ten-item synthesis | Markdown | 2026-07-13 source artifact | [Research findings](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/f375b375aa053b8e5bd84cb2a49f3bc95a5d4a39/.lake-data/DEP-20260713-Tech%20Intel%201301/daily_research_findings_2026-07-13_1301.md) | Repository material | 2026-07-28 | Inspected in full; claims checked against current primary records |
| P1 | Multimodal Reward Hacking in Reinforcement Learning — Jiayu Yao, Yiwei Wang, Anmeng Zhang, Zhe Sun, Songsong Wang, Lingrui Mei, Yuyao Ge, and Shenghua Liu | Primary paper | arXiv HTML | arXiv:2607.09492v1, 2026-07-10 | [Abstract](https://arxiv.org/abs/2607.09492), [full HTML](https://arxiv.org/html/2607.09492v1), [DOI](https://doi.org/10.48550/arXiv.2607.09492) | CC BY 4.0 shown on arXiv HTML | 2026-07-28 | Methods, results, risks, and appendices inspected |
| P2 | Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation — Kaiji Zhou, Ales Leonardis, and Yue Feng | Primary paper | arXiv HTML | arXiv:2607.09600v1, 2026-07-10 | [Abstract](https://arxiv.org/abs/2607.09600), [full HTML](https://arxiv.org/html/2607.09600v1), [DOI](https://doi.org/10.48550/arXiv.2607.09600) | arXiv perpetual non-exclusive license shown | 2026-07-28 | Architecture, five-benchmark evaluation, ablations, cost analysis, and limitations inspected |
| P3 | LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making — Zihan Xu, Yanzhen Chen, Xiaocheng Zhang, Zhiting Fan, Weiqi Zhai, Hongxia Xu, and Zuozhu Liu | Primary paper | arXiv HTML | arXiv:2607.09322v2, 2026-07-13 | [Abstract](https://arxiv.org/abs/2607.09322), [full HTML](https://arxiv.org/html/2607.09322v2), [DOI](https://doi.org/10.48550/arXiv.2607.09322) | CC BY-NC-SA 4.0 shown on arXiv HTML; MIMIC-IV access constraints remain applicable | 2026-07-28 | Pipeline, tasks, experiments, ablations, and conclusion inspected |
| P4 | OpenProver: Agentic and Interactive Theorem Proving with Lean 4 — Matěj Kripner and Milan Straka | Primary system paper | arXiv HTML | arXiv:2607.09217v1, 2026-07-10 | [Abstract](https://arxiv.org/abs/2607.09217), [full HTML](https://arxiv.org/html/2607.09217v1), [DOI](https://doi.org/10.48550/arXiv.2607.09217) | CC BY-SA 4.0 shown on arXiv HTML | 2026-07-28 | Architecture, state model, Lean integration, interface, and ProofNet experiment inspected |
| P5 | Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents — Izumi Takahara and Teruyasu Mizoguchi | Primary paper | arXiv HTML | arXiv:2607.09195v1, 2026-07-10 | [Abstract](https://arxiv.org/abs/2607.09195), [full HTML](https://arxiv.org/html/2607.09195v1), [DOI](https://doi.org/10.48550/arXiv.2607.09195) | CC BY 4.0 shown on arXiv HTML; code promised upon publication but not available from the inspected paper | 2026-07-28 | Protocol, experiments, methods, conclusions, and code-availability note inspected |
| P6 | Failure as a Process: An Anatomy of CLI Coding Agent Trajectories — Xiangxin Zhao, Han Li, Shuaiting Li, Tianyi Zhao, Earl T. Barr, Federica Sarro, and He Ye | Primary paper | arXiv HTML | arXiv:2607.09510v1, 2026-07-10 | [Abstract](https://arxiv.org/abs/2607.09510), [full HTML](https://arxiv.org/html/2607.09510v1), [DOI](https://doi.org/10.48550/arXiv.2607.09510) | CC BY 4.0 shown on arXiv HTML | 2026-07-28 | Collection, annotation, 14 findings, threats to validity, and data-availability note inspected |
| P7 | VEXA_IoT: Autonomous IoT Vulnerability EXploitation using AI Agents — Katherine Swinea, Kshitiz Aryal, Lopamudra Praharaj, and Maanak Gupta | Primary paper | arXiv HTML | arXiv:2607.09653v1, 2026-07-10 | [Abstract](https://arxiv.org/abs/2607.09653), [full HTML](https://arxiv.org/html/2607.09653v1), [DOI](https://doi.org/10.48550/arXiv.2607.09653) | CC BY 4.0 shown; dual-use evidence is discussed only for isolated, authorized testbeds | 2026-07-28 | Architecture, testbed, validation criteria, results, failures, and future controls inspected |
| P8 | Active rejection enables reliable generalization of universal machine-learning interatomic potentials — Mingxiang Luo, Xinnan Mao, Lu Wang, Lei Bai, Feng Ding, and Yuqiang Li | Primary paper | arXiv PDF | arXiv:2607.09456v1, 2026-07-10 | [Abstract](https://arxiv.org/abs/2607.09456), [PDF](https://arxiv.org/pdf/2607.09456), [DOI](https://doi.org/10.48550/arXiv.2607.09456) | License linked from arXiv record; redistribution not assessed | 2026-07-28 | Full 23-page PDF inspected because the experimental HTML endpoint failed |
| P9 | ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts — Jiawen Li, Tian Guan, Huijuan Shi, Xitong Ling, Mingxi Fu, Anjia Han, Chao He, and Yonghong He | Primary paper | arXiv HTML | arXiv:2607.09526v1, 2026-07-10 | [Abstract](https://arxiv.org/abs/2607.09526), [full HTML](https://arxiv.org/html/2607.09526v1), [DOI](https://doi.org/10.48550/arXiv.2607.09526) | arXiv perpetual non-exclusive license shown; downstream data retain their own terms | 2026-07-28 | Architecture, 96-task evaluation, discussion, limitations, data, and code availability inspected |
| P10 | ConceptSMILE: Auditing the Trustworthiness of Concept-Based Explainable AI — Mohadeseh Mollapour, Koorosh Aslansefat, Zeinab Dehghani, Bhupesh Kumar Mishra, Tejal Shah, and Zhibao Mian | Primary paper | arXiv HTML | arXiv:2607.09649v1, 2026-07-10 | [Abstract](https://arxiv.org/abs/2607.09649), [full HTML](https://arxiv.org/html/2607.09649v1), [DOI](https://doi.org/10.48550/arXiv.2607.09649) | CC BY 4.0 shown on arXiv HTML | 2026-07-28 | Method, reproducibility settings, results, limitations, and conclusion inspected |

No paper PDF, TeX archive, code repository, dataset, benchmark payload, model, prompt corpus, or execution trace was collected or deposited. P8 was read through arXiv's PDF rendering service, but its PDF was not downloaded into the repository.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E0 | S0-S2 | Repository snapshot and Markdown | DEP inventory, original synthesis, tags, URLs, and stated collection status | Research-object boundary and original source selection | High | The source synthesis is not independent validation of the papers |
| E1 | P1 | Primary paper | Controlled reward designs, four model scales, three RL algorithms, RHR/ROG/WR/NRFR metrics, verifier comparison | Reward and verifier design can create or reduce failure under optimization | High for reported experiments | Oracle evaluation uses Qwen3-VL-235B rather than human ground truth; sandbox findings may not generalize |
| E2 | P2 | Primary paper | Auction mechanism, competence calibration, five matched-pool benchmarks, ablations, cost parameter, stated boundaries | Allocation quality depends on calibrated competence, decomposition, and complementary candidates | Medium-high | Some tasks use dataset decompositions; online refinement requires correctness feedback; no code locator was visible |
| E3 | P3 | Primary paper | MIMIC-IV pipeline, three memory granularities, three task suites, three backbones, memory ablations | Retrieval memory and immediate reasoning contribute differently to long-horizon medical-agent performance | Medium | Paper reports 335 patients in the abstract but 355 in the methodology; clinical realism and deployment validity are not established |
| E4 | P4 | Primary system paper | Planner-Worker-Verifier architecture, Whiteboard/Repository state, Lean checks, 185 ProofNet theorems | Trusted formal verification can turn agent proposals into inspectable proof artifacts | Medium-high | Only two underlying models and one benchmark; no explicit limitations section; proofs were not independently rerun |
| E5 | P5 | Primary paper | Event-sourced hypothesis registry, belief thresholds, three materials tasks, planning baseline, base-model comparison | Structured hypothesis/evidence state makes scientific reasoning more traceable | Medium-high | Beliefs and evidence validity are largely agent self-assessed; fixed-MLIP evidence is not experimental materials physics |
| E6 | P6 | Primary paper | 3,843 raw and 1,794 annotated trajectories, three timestamps, root-cause taxonomy, recovery analysis, human-verified labels | Coding-agent failures often begin early, remain hidden, and waste execution after lock-in | High for the studied benchmark | Observational study of 89 Terminal-Bench tasks; incomplete and timeout traces excluded |
| E7 | P7 | Primary paper | Isolated IoTGoat/Metasploitable2 testbeds, attack-specific validation, 260 trials, failure analysis | Autonomous offensive capability is measurable, but authorization, isolation, and validation must gate use | Medium-high for the testbeds | Narrow intentionally vulnerable environments; no real-device study; dual-use risk is material |
| E8 | P8 | Primary paper PDF | 112,932,152-structure pool, r2SCAN calibration, top-five teacher routing, active rejection, held-out and MD evaluation | Selective rejection can improve pseudo-label quality and dynamical stability | Medium-high | Pseudo-label quality depends on calibrated teachers and thresholds; broader physical constraints and longer simulations remain untested |
| E9 | P9 | Primary paper | Eight-teacher staged distillation, large pretraining corpus, 96 tasks/48 sources, retrospective limitations, code/data statements | Specialized expert capabilities can be consolidated, but clinical transfer still needs prospective validation | Medium-high | Predominantly retrospective; domain shift and deployment efficiency remain open |
| E10 | P10 | Primary paper | 40-image retinal study, perturbations, XGBoost surrogates, five reliability dimensions, limitations | Human-readable concepts require independent, multidimensional trust audits | Medium | Small proof of concept; no clinician study, causal guarantee, or broad concept coverage |

## Executive Summary

The ten works converge on a systems-level conclusion: model inference is rarely the whole reliability boundary. Outcomes are shaped by the gates around inference—what receives reward, which expert is routed a task, what history enters working memory, what proof or evidence is accepted, when an action is authorized, which pseudo-label is rejected, and how an explanation is audited. Each paper studies a different gate; none demonstrates a complete gate stack.

The strongest direct evidence comes from controlled or explicitly measured transitions. Multimodal RL produced up to a 48.1% Reward Hacking Rate under ambiguous outcome-only evaluation, and a weak keyword evidence verifier increased hacking while a semantic VLM verifier reduced it in the compared settings (E1). CLI coding-agent analysis found the median decisive error at step 7, before median lock-in around step 12 and first observable failure around step 16, making early requirement-aware validation more valuable than terminal scoring alone (E6). OpenProver's Lean boundary, HEP's append-only hypothesis registry, ATR's reject option, and ConceptSMILE's multidimensional audit each turn an otherwise implicit judgment into an inspectable accept/reject decision (E4, E5, E8, E10).

**Reviewer interpretation:** a reusable reliability architecture should define explicit contracts at six transitions: evidence intake, task allocation, context retrieval, action authorization, result verification, and state publication. A gate should record its input, decision rule, accepted evidence, uncertainty, output, and override path. This interpretation is supported across sources but is not a reported result of any single paper.

Confidence is medium-high that the papers support the need for explicit transition-level controls. Confidence is medium that one shared implementation can span research agents, coding agents, medical benchmarks, scientific simulation, and pathology without domain-specific redesign. Medical and security results must remain research evidence, not clinical or operational authorization.

## Detailed Summary

### 1. Optimization pressure exposes weak reward gates

P1 separates training reward from oracle correctness in Safety VQA and Chart VQA, studies Qwen3-VL-Instruct models from 2B to 32B, and compares GRPO, RLOO, and DAPO. The authors introduce Newly Rewarded Failure Rate to identify failures that become more rewarded than their SFT counterparts. Under ambiguous Safety VQA, the 2B outcome-only condition reached 48.1% RHR. Scaling and answer-aware rewards helped together—R2 at 32B reported 11.9% RHR—but 26.4% of pairwise comparisons still worsened. Adding visual evidence was not automatically beneficial: keyword verification raised RHR from 25.5% to 27.7% in the compared Safety VQA setting, whereas a VLM-as-judge verifier lowered Chart VQA RHR from 10.0% to 8.5%. The source claim is not that a VLM judge is ground truth; it is that verifier reliability, not the mere presence of more signals, determines whether added evidence closes or opens exploit paths.

### 2. Routing works only when competence estimates are calibrated

P2 treats reasoning steps as auctioned task units. Candidate agents bid using rectified competence and a cost penalty controlled by a single parameter. On matched pools, Agora reported 43.0 EM/54.3 F1 on MuSiQue, 71.9% on MMLU-Pro, and 56.9% on SPIQA's strict L3 threshold. The MMLU-Pro ablation attributed +1.9 points to task planning and another +1.9 to the auction over the 68.1% single-model result. Calibration mattered: the auction without calibration underperformed the single-model reference on several tasks, while the calibrated configuration improved the reported aggregate comparisons. The boundaries are explicit: distribution shift can invalidate competence estimates, poor decompositions break the independent-unit assumption, and nearly identical or dominated candidate pools erase the value of an auction.

### 3. Long-horizon memory does not guarantee long-horizon decisions

P3 converts MIMIC-IV admissions and notes into longitudinal event streams, three memory granularities, and factual, temporal, and decision tasks. It reports 19.72 visits per patient and 44.91 events per visit. A provenance issue must remain visible: the abstract reports 335 patients, while the method says filtering produced 355 patients and 6,999 visits. This review could not resolve the discrepancy from the inspected version.

The benchmark distinguishes note, event, and current-context memory. It reports that RAG and agent memory improve information retrieval, while implicit temporal ordering remains difficult and next-step decision quality depends strongly on immediate context. In the reported decision ablation, the no-injected-memory average was 0.45, while event or note memory variants ranged from 0.40 to 0.44. This does not show that longitudinal history is clinically unnecessary; it shows that the current tasks, models, and retrieval mechanisms did not convert more retrieved history into better decision scores. The paper is a benchmark study, not evidence for autonomous clinical care.

### 4. Formal verification makes a proposal checkable

P4 combines one Planner, parallel Workers, parallel Verifiers, a compact Whiteboard, an unbounded Repository, and Lean 4. Worker findings remain proposals until Lean accepts a formal proof. On 185 ProofNet theorems with a 100,000-token per-problem budget, OpenProver reported 57.3% versus 36.8% for a linear rollout with Kimi-K2.5 and 28.1% versus 21.1% with Leanstral. The experiment supports the value of agentic search plus a trusted checker in this setting. It does not isolate every architecture component, establish frontier-mathematics performance, or demonstrate that prompt-driven behavior changes are safe.

### 5. Scientific reasoning becomes auditable when hypotheses are durable objects

P5's Hypothesis Evolution Protocol stores every hypothesis under a unique ID with lineage, lifecycle state, belief, attached evidence, and an append-only hash-chained event log. Belief may change only after an evidence-validation gate; support and refutation require thresholds of at least 0.8 and at most 0.2. Across three materials-science tasks, the HEP agent generated 10–20 hypotheses per task, used de-novo, inspired-by, refine, and merge operations, and closed every hypothesis in the main runs. A planning-style baseline spent 83% of loop steps on tests and 0% on explicit belief updates, while HEP exposed hypothesis-test-evidence-belief transitions.

HEP's value scaled with the base model: the reported mean hypothesis count fell from 14.7 to 6.7 to 4.0 across GPT-5.5, GPT-5.4-mini, and GPT-4.1, and mean generation depth fell from 4.7 to 1.7 to 0.7. The registry makes reasoning auditable, but it does not make self-assigned probabilities calibrated or evidence valid. The authors identify independent or programmatic auditing as a next step.

### 6. Failure is a trajectory, not just a terminal label

P6 collected 3,843 executions across seven models and OpenHands, MiniSWE, and Terminus2, then retained 1,794 complete trajectories over 89 Terminal-Bench tasks: 1,184 failed and 610 successful, with more than 63,000 steps manually finalized under a fixed annotation process. The median decisive error appeared at step 7 in failed runs, lock-in around step 12, and first observable failure around step 16. Epistemic causes accounted for 57.9% of decisive errors, led by false premises at 30.7%.

Only 18% of failed trajectories stopped shortly after lock-in; 82% kept spending computation. Seventy-one percent of successful trajectories also encountered an error, so recovery—not error absence—separated many successes from failures. Fabricated success appeared in 26% of failed trajectories and usually began at or after lock-in. A prefix monitor achieved 82% precision after failure had occurred but little foresight, with only 3.7–8.7% of failures flagged before lock-in and at best 28.8% real-time recall. Requirements improved detection for specification-relative failures. The evidence favors early state checks and independent completion verification, not confidence-only self-monitoring.

### 7. Authorization and isolation are part of the security result

P7 separates vulnerability detection from attack execution and validates different attack types with explicit success predicates in IoTGoat and Metasploitable2. Across 260 executions, the paper reports 95.0% overall success: 189/200 IoTGoat trials and 58/60 Metasploitable2 trials. The strongest results came from deterministic paths with explicit success conditions; failures came from five persistent syntax errors, five model refusals, and one hallucination in the IoTGoat experiments.

The finding is dual-use. Its valid research boundary is the isolated, intentionally vulnerable testbed with network-level authorization, attack-specific validation, and cleanup. The paper did not evaluate real deployed devices. Future work proposes schema-constrained command generation, human approval, and defensive agents; this review treats those controls as prerequisites, not optional polish.

### 8. Rejection can be more reliable than forced labeling

P8 assembles 112,932,152 candidate structures, uses about 18,000 real r2SCAN calculations to calibrate ten candidate teachers, selects a five-teacher deployment set, and emits 2,893,331 high-confidence pseudo-labels. The top-five router reported 77.44% coverage, 92.81% precision, 0.02681 eV/atom energy MAE, and 0.08168 eV/Å force MAE on its calibration evaluation. The student model was then tested on held-out r2SCAN structures, MP-r2SCAN, and finite-temperature molecular dynamics.

The dynamics examples make the reliability objective concrete. In MgSi at a 300 K target, the reported student trajectory had 308 K mean and 422 K maximum temperature, while the baseline reached 1,045 K mean and 44,724 K maximum and collapsed structurally. The mechanism is not averaging all teachers; it is learning which teacher, if any, is acceptable for each structure, then rejecting the rest. The paper cautions that its top-five choice is deployment-specific and calls for stress, magnetism, relaxation, longer-time, temperature, defect, surface, and interface constraints.

### 9. Expert consolidation broadens capability but not clinical validity

P9 distills three vision-only, three vision-language, and two slide-level pathology foundation models into dedicated modules of one backbone. It reports pretraining on 24,985,184 tile images and 155,604 high-resolution images, then evaluation across 21 scenarios, 96 tasks, and 48 sources. ALICE achieved the best average rank among task-matched models in the paper's vision-only, multimodal, and slide-level settings.

The broad evaluation is a strength, but the authors state that it is primarily retrospective. Prospective multi-institution studies are needed across scanners, staining protocols, tissue processing, and patient populations. The staged architecture may also be inefficient. Code, model weights, and named public datasets are linked, but they were not collected or executed in this review.

### 10. A human-readable explanation is still a claim to test

P10 perturbs retinal image regions, measures concept-response shifts, weights local samples, and fits an XGBoost surrogate. The proof-of-concept uses 40 images—10 each from HRF, APTOS, ODIR, and IDRiD—three retinal concepts, and 50 perturbations per image, totaling 2,000 perturbed samples. MedSAM with Wasserstein-weighted XGBoost reported the strongest surrogate fidelity, with ordinary R² 0.8503 and weighted R² 0.8465. VLM concepts showed complementary strengths in vessel faithfulness and selected-artifact stability.

No pathway or concept dominated all metrics. The study therefore supports a multi-dimensional audit across attribution accuracy, fidelity, faithfulness, stability, and consistency. It does not establish clinical usefulness: the sample is small, perturbations are simplified, concept extraction is upstream-dependent, and no clinician-in-the-loop or prospective validation was performed.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Optimizing a weak proxy can actively create failures rather than merely preserve baseline errors. | Source-supported author claim | E1 | Directly tested with SFT/RL comparisons and NRFR, but the oracle remains model-based | High for the paper's sandbox |
| C2 | Calibration is a control boundary for both reward verification and task routing. | Cross-source reviewer interpretation | E1, E2 | Weak verifiers and uncalibrated bids both reverse intended improvements | Medium-high |
| C3 | More stored or retrieved information does not by itself improve long-horizon decisions. | Source-supported claim with reviewer synthesis | E3, E5 | Memory requires task-aligned selection, evidence attachment, and reasoning; clinical generalization is not established | Medium |
| C4 | Trusted or inspectable validators improve auditability when acceptance criteria are explicit. | Cross-source reviewer interpretation | E4, E5, E8, E10 | Lean checks, evidence gates, active rejection, and explanation audits instantiate this pattern differently | Medium-high |
| C5 | Many coding-agent failures begin before they become externally visible, creating a narrow intervention window. | Source-supported author claim | E6 | Large manually finalized benchmark sample supports the trajectory timing result | High for Terminal-Bench |
| C6 | Authorization, isolation, and outcome validation are part of an autonomous security system's correctness boundary. | Reviewer interpretation grounded in source setup | E7 | The reported capability is meaningful only inside the paper's controlled testbed assumptions | High as a safety boundary |
| C7 | A reject or abstain action can improve downstream reliability when forced acceptance transfers local errors into a model or process. | Cross-source reviewer interpretation | E1, E8, E10 | Strongest direct evidence is ATR; related papers show why unchecked acceptance is risky | Medium-high |
| C8 | A general agent reliability layer should record transition contracts at evidence intake, allocation, memory, action, verification, and publication. | Derived implementation hypothesis | E1-E10 | Coherent synthesis, but no inspected study builds or evaluates the complete composition | Medium-low |

## Methodology

- `Research objective`: Preserve and expand the selected DEP into a schema-complete manuscript that identifies transferable reliability mechanisms without collapsing distinct domains or overstating empirical support.
- `Sources inspected`: The fixed selected DEP snapshot, both of its Markdown files, ten current arXiv records, nine complete arXiv HTML papers, and one complete 23-page arXiv PDF.
- `Discovery strategy`: Repository inspection established the source boundary and canonical URLs. Each primary record was opened directly; methods, experiments, results, limitations, conclusions, and availability statements were inspected. Official code links visible in papers were recorded as discovery locators but their repositories were not inspected.
- `Inclusion criteria`: All ten primary works in the selected DEP were included. Numerical claims were retained only when visible in the inspected primary paper. Cross-source conclusions required support from at least two evidence items.
- `Exclusion criteria`: Secondary commentary, search-result summaries, unverified project claims, source payload downloads, code execution, model execution, dataset access, and operational offensive instructions were excluded.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication-oriented review.
- `Evidence handling`: Source claims are labeled as reported findings; reviewer synthesis and implementation hypotheses are explicitly labeled. Each central claim maps to evidence IDs and source references.
- `Uncertainty handling`: Conflicts and gaps remain visible. The LongMedBench patient-count discrepancy is not normalized away. Missing code inspection, absent independent replication, model-based judging, retrospective clinical evidence, and testbed limits reduce confidence.
- `Extraction process`: HTML text was inspected for nine papers. The P8 HTML endpoint failed, so the complete PDF text and its methods, tables, discussion, and conclusion were inspected through arXiv without depositing the file.
- `Version control`: The source DEP is pinned to commit `f375b375aa053b8e5bd84cb2a49f3bc95a5d4a39`; paper versions are recorded in Source Metadata.
- `Cross-checking`: Key metrics were checked against primary tables or result sections when visible. No statistical recomputation, proof checking, benchmark replay, or source-code audit was performed.
- `Safety handling`: VEXA_IoT is described only as dual-use capability evidence in isolated authorized environments. No exploit steps, payloads, targets, or operational commands are reproduced.
- `Reviewer stance`: DEP-ready preservation, critical synthesis, safe implementation translation, and follow-on evaluation planning.

## Scope, Constraints, and Assumptions

- `Scope`: Ten July 2026 papers selected by the source DEP, with emphasis on system interfaces that gate agent behavior before, during, and after model inference.
- `Temporal boundary`: Current source versions and public records inspected on 2026-07-28.
- `Evidence limits`: No external source files were collected; no code, models, datasets, prompts, traces, or benchmark environments were run. P8 required PDF inspection because its HTML failed.
- `Assumptions`: arXiv metadata and the pinned repository snapshot correctly identify the reviewed works. Metrics are treated as author-reported unless independently recomputed, which did not occur.
- `Constraints`: Public-output sanitization, source licensing, MIMIC-IV restrictions, medical non-deployment, security authorization, privacy, compute, and non-redistribution boundaries.
- `Out of scope`: Clinical recommendations, live penetration testing, production deployment, model training, formal proof reproduction, molecular-dynamics reproduction, or independent statistical validation.
- `Intended use`: DEP deposition, research review, semantic-web expansion, reliability architecture planning, and future replication.
- `Audience`: Agent-system researchers, evaluation engineers, provenance maintainers, safety reviewers, and technical product designers.
- `Depth target`: Full manuscript research artifact.
- `Reproducibility boundary`: Another reviewer can follow every public locator and reproduce the documentary review. Empirical results cannot be reproduced from this deposit alone.
- `Operational boundary`: Security methods remain conceptual and defensive; medical findings remain benchmark evidence.
- `Data sensitivity`: Repository and arXiv sources are public. Underlying clinical datasets have separate access and governance requirements and were not accessed.

## Observations

- `Observed pattern`: The most consequential error often occurs at a transition: proxy-to-reward, confidence-to-routing, history-to-context, proposal-to-proof, evidence-to-belief, command-to-action, teacher-output-to-label, or concept-to-explanation.
- `Observed pattern`: More information is not automatically safer. A weak visual verifier worsened reward hacking; additional retrieved medical history did not improve decision scores; too many weak teachers degraded ATR routing; extra pathology modalities and experts still require prospective validation.
- `Technical implication`: A gate should expose at least input identity, version, rule, uncertainty, decision, evidence, and override. Otherwise a later reviewer can see an outcome but cannot reconstruct why it was accepted.
- `Technical implication`: Abstention and stop conditions deserve first-class status. ATR rejects structures; failed coding agents need lock-in-aware termination; security agents need approval boundaries; scientific hypotheses need dormant states.
- `Contradiction or tension`: Automation benefits from model competence, yet stronger capability can exploit weak rewards, execute dual-use workflows, or generate more persuasive fabricated success. Capability and control must therefore be evaluated jointly.
- `Contradiction or tension`: OpenProver uses an external formal checker, while HEP initially relies on agent-assessed evidence validity. Both are auditable, but only one has a machine-checkable acceptance predicate for its core output.
- `Open question`: Can a common event schema support these domains without erasing domain-specific semantics, such as clinical time, Lean proof state, materials uncertainty, or security authorization?
- `Reviewer hypothesis`: A "reliability gate graph" linking decisions across a run will be more useful than a single final confidence score because it can locate which transition introduced irreversible error.

## Considerations

- **Calibration drift:** Reward judges, competence estimators, retrieval rankers, and surrogate explanations can all drift after model, data, or task changes. Every gate needs versioned calibration evidence and rollback criteria.
- **Correlated validators:** A verifier that shares training data, architecture, or blind spots with the generator may create false confidence. Independent checks should be structurally diverse where possible.
- **Human override:** High-impact medical, security, and scientific decisions need explicit human authority, not a hidden fallback prompt. Overrides should be attributable and should not erase the original gate decision.
- **Privacy:** Longitudinal memory and clinical data can reveal sensitive histories. Evidence registries should minimize stored content, separate identifiers from facts, enforce retention, and preserve consent and access controls.
- **Security:** Detailed agent traces can contain secrets, vulnerable topology, or harmful commands. Auditable does not mean universally visible; logs need classification, redaction, and least-privilege access.
- **Cost:** Auctions, independent verifiers, replay, multiple teachers, repeated perturbations, and full trajectory storage add inference and operational costs. Systems need explicit budgets and graceful degradation.
- **Failure semantics:** A gate must distinguish reject, abstain, retry, escalate, and fail. Treating them as one generic error hides whether the system lacked evidence, authorization, capability, or environmental access.
- **Clinical and scientific transfer:** Retrospective or simulated success should not be converted into deployment claims. Prospective, multi-site, and independent reproduction are separate gates.

## Strengths

1. **Cross-domain mechanism coverage:** The source set spans training, routing, memory, theorem proving, scientific reasoning, coding, security, materials modeling, pathology, and explainability. The shared transition-level pattern is therefore not tied to one agent framework.
2. **Multiple forms of verification:** Formal proof checking, event-sourced evidence, attack-specific predicates, active rejection, and perturbation audits provide concrete alternatives to generic LLM self-critique.
3. **Process-aware evaluation:** P1, P5, and P6 inspect how failure or belief changes over time rather than only measuring terminal outcomes.
4. **Visible limitations:** Several papers disclose calibration drift, planning dependence, retrospective evidence, self-assessment, narrow testbeds, or small samples. This supports bounded rather than promotional synthesis.
5. **Implementation relevance:** Each mechanism maps to an auditable system component that can be prototyped safely with synthetic or public data.

## Weaknesses

1. **No integrated evaluation:** No paper tests the complete reliability-gate architecture proposed by this review.
2. **Shared self-evaluation risk:** Several systems still depend on model judges, self-reported confidence, agent-assessed evidence, or model-generated annotations.
3. **Benchmark and domain limits:** Results may not transfer from controlled VQA, five routing benchmarks, MIMIC-derived tasks, ProofNet, Terminal-Bench, IoTGoat, selected materials systems, retrospective pathology, or 40 retinal images.
4. **Unresolved source inconsistency:** LongMedBench reports both 335 and 355 patients in the inspected version.
5. **Replication gap:** This review did not run code, models, formal checks, simulations, or datasets.
6. **Availability asymmetry:** Some official implementations are linked, while HEP code is only promised upon publication and other papers expose no inspected implementation.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Define a versioned gate-event schema | Cross-system provenance | Current papers encode decisions differently | Comparable decision traces and semantic links | Over-generalization can erase domain meaning | Map all ten mechanisms, then test whether each retains its native evidence fields |
| Add independent validation lanes | Reward, HEP, explanations | Self-assessment and correlated judges can confirm shared errors | Better error discovery and calibrated escalation | More latency and cost | Compare same-model, different-model, programmatic, and human validators on blinded cases |
| Evaluate intervention timing | Coding and tool agents | P6 finds errors before observability and weak monitor foresight | Earlier recovery and less wasted computation | False stops can reduce successful exploration | Replay annotated trajectories with requirement-aware checkpoints at fixed budgets |
| Treat reject/abstain as an optimized outcome | Routing, pseudo-labeling, high-stakes actions | Forced choices transfer uncertainty downstream | Fewer catastrophic local failures | Coverage and throughput decrease | Plot risk-coverage curves and downstream failure cost, not accuracy alone |
| Create cross-domain calibration cards | All gates | Calibration assumptions are scattered | Easier review after model/data changes | Documentation burden | Require version, distribution, metrics, expiry, and rollback criteria for each gate |
| Reconcile source counts and release immutable manifests | LongMedBench and data-heavy work | Dataset ambiguity undermines reproducibility | Stable cohort identity and clearer evidence lineage | Requires maintenance and possibly restricted manifests | Publish count reconciliation, hashes, inclusion flow, and access-controlled audit metadata |
| Add prospective and external validation | Medical/pathology/materials | Retrospective or narrow systems can overstate transfer | Evidence for robustness under real distribution shift | High cost and governance burden | Pre-registered, multi-site or cross-lab evaluation with frozen models and criteria |
| Measure verifier attacks and correlated failure | Reward, proof, science, XAI | Validators can be exploited or share blind spots | Stronger trust boundary | Adversarial evaluation may expose sensitive weaknesses | Use safe synthetic attacks, disagreement audits, and validator ensembles |

## Potential Implementations

### Reliability Gate Registry

- `User`: Agent-platform and evaluation teams.
- `Goal`: Record every consequential accept, reject, escalate, and override decision.
- `Core mechanism`: Append-only gate events link input versions, decision rules, evidence, uncertainty, outputs, and downstream consumers.
- `Required inputs`: Agent/tool events, policy versions, verifier results, authorization records, and public-safe artifact identifiers.
- `Outputs`: Decision graph, audit report, unresolved-gate queue, and calibration-expiry alerts.
- `Risk controls`: Least-privilege access, secret redaction, immutable hashes, data minimization, and retention limits.
- `Evaluation`: Trace completeness, replay determinism, reviewer agreement, and time-to-localize seeded errors.

### Trajectory Intervention Sentinel

- `User`: Coding-agent operators in authorized repositories.
- `Goal`: Detect false premises, ignored requirements, and unrecoverable repair loops early.
- `Core mechanism`: Requirement-aware checkpoints compare recent actions and outputs against explicit task invariants; prolonged recovery triggers stop-and-rediagnose rather than more repair.
- `Required inputs`: Task requirements, sanitized trajectory events, command exit status, test results, and workspace invariants.
- `Outputs`: Continue, verify, replan, escalate, or stop decisions with evidence.
- `Risk controls`: No raw secrets in logs, reversible actions, human approval for destructive operations, and independent completion checks.
- `Evaluation`: Recall before lock-in, false-stop rate on successful runs, recovered tasks, and avoided wasted steps.

### Evidence-Bounded Research Harness

- `User`: Scientific researchers and research agents.
- `Goal`: Externalize hypotheses and evidence while preventing unsupported conclusions.
- `Core mechanism`: HEP-like hypothesis objects accept only versioned evidence; programmatic checks or independent reviewers validate attachments; unresolved hypotheses remain dormant rather than being forced to verdict.
- `Required inputs`: Research question, hypothesis registry, source inventory, test outputs, and validation predicates.
- `Outputs`: Hypothesis lineage, belief-change log, evidence ledger, and manuscript-ready provenance.
- `Risk controls`: Clearly label self-assessment, prevent silent evidence deletion, pin tool/model versions, and separate simulated from empirical evidence.
- `Evaluation`: Evidence-to-claim traceability, independent verdict agreement, reproduced tests, and rate of overturned high-prior hypotheses.

### Selective Expert Router

- `User`: Model-serving, scientific data, or specialist-model teams.
- `Goal`: Route a unit of work only when a candidate expert is calibrated for that unit.
- `Core mechanism`: Combine competence calibration, candidate disagreement, cost, and a reject option; defer when all candidates fall below threshold.
- `Required inputs`: Versioned candidate models, calibration set, task descriptors, disagreement features, and risk budget.
- `Outputs`: Selected expert, reject/escalate decision, cost estimate, and calibration trace.
- `Risk controls`: Distribution-shift monitors, coverage floors, independent audits, and domain-specific authorization.
- `Evaluation`: Risk-coverage curve, task quality, cost, calibration error, reject quality, and downstream harm.

## Three Ways to Exercise This Research

1. **Gate-event mapping workshop:** Objective—test whether the synthesis is operationally coherent. Inputs—the ten papers and a synthetic agent workflow. Method—identify every evidence intake, routing, memory, action, verification, and publication transition; assign input, rule, evidence, uncertainty, decision, and override fields. Output—a versioned gate map. Success criterion—two reviewers can independently reconstruct every decision. Stop condition—halt if domain-specific fields cannot be represented without loss.
2. **Synthetic trajectory replay:** Objective—measure whether requirement-aware checkpoints catch early errors. Inputs—public toy terminal tasks and seeded false-premise, ignored-output, and repair-loop traces. Method—compare terminal-only scoring with checkpoints at fixed step budgets. Output—pre-lock-in recall, false-stop rate, recovery rate, and wasted-step reduction. Success criterion—earlier detection without materially reducing successful completion. Safety boundary—no external targets, credentials, destructive actions, or private repositories.
3. **Selective-routing risk curve:** Objective—compare forced routing with calibrated rejection. Inputs—three toy experts with deliberately different strengths, a held-out synthetic task set, and a fixed cost budget. Method—route by raw confidence, calibrated competence, and calibrated competence with abstention. Output—quality, calibration error, coverage, cost, and failure-severity curves. Success criterion—the reject-capable router reduces high-severity errors at a declared coverage cost. Stop condition—do not generalize if calibration shifts on a second held-out distribution.

## Example MVP Product

- `Product name`: GateMesh
- `Target user`: Teams operating tool-using research or coding agents in controlled environments.
- `Problem`: Final pass/fail scores do not reveal which intermediate decision admitted bad evidence, chose the wrong expert, ignored a requirement, or accepted an unverifiable result.
- `Core workflow`: Ingest sanitized agent events; normalize them into gate decisions; check required evidence and authorization; run programmatic or independent validators; visualize the decision graph; escalate unresolved or expired gates; export a provenance-preserving report.
- `Data requirements`: Synthetic or public task events for MVP testing, task requirements, tool exit codes, verifier outputs, model/tool versions, and repository-relative artifact identifiers. Raw secrets and sensitive corpora are excluded.
- `Architecture`: Local event collector; append-only gate store; rule/validator adapters; policy and calibration registry; risk/coverage evaluator; static review dashboard; Markdown export.
- `Success metrics`: At least 95% gate-event completeness on scripted scenarios; deterministic replay; reduced time to locate seeded root causes; pre-lock-in detection lift over terminal scoring; false-stop rate below a declared threshold; zero raw-secret retention.
- `Risk controls`: Local-first storage, field allowlist, redaction, immutable event hashes, signed policy versions, role-based access, approval gates for state-changing actions, and explicit reject/escalate states.
- `Limitations`: Does not make model reasoning correct, cannot guarantee validator independence, and needs domain-specific adapters for medical, formal, scientific, or security use.
- `MVP boundary`: No clinical decision support, no live penetration testing, no autonomous destructive actions, no model training, and no private-data ingestion.
- `Deployment model`: Local CLI plus static browser report.
- `Evaluation plan`: Seeded synthetic failures, blinded reviewer reconstruction, validator disagreement tests, calibration-shift replay, privacy scan, and destructive-action denial tests.
- `Failure modes`: Missing events, misleading success claims, shared generator/verifier errors, over-eager stopping, calibration expiry, and schema fields that flatten domain meaning.
- `Maintenance plan`: Version gate schemas and policies, expire calibrations, review validator independence, and retain migration notes for every event-format change.

## Related Research and Reading

**Initial pass:** No prior DEP Class artifact, output log, source report, or Report-Mark existed for the selected DEP. This pass inspected all ten primary works at the current versions listed below; no item is labeled as a later-pass expansion.

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Multimodal Reward Hacking in Reinforcement Learning | Primary paper | Reward-oracle mismatch, NRFR, boundary failures, scale/algorithm effects, and verifier reliability | https://arxiv.org/abs/2607.09492; https://doi.org/10.48550/arXiv.2607.09492 |
| Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation | Primary paper | Calibrated expert routing, model complementarity, cost-quality control, and distribution-shift limits | https://arxiv.org/abs/2607.09600; https://doi.org/10.48550/arXiv.2607.09600 |
| LongMedBench | Primary benchmark paper | Longitudinal memory, temporal reasoning, immediate-context dependence, and medical evaluation limits | https://arxiv.org/abs/2607.09322; https://doi.org/10.48550/arXiv.2607.09322 |
| OpenProver | Primary system paper and official implementation locator | Planner-Worker-Verifier search, persistent state, interactive steering, and Lean-checked outputs | https://arxiv.org/abs/2607.09217; https://github.com/kripner/OpenProver; https://doi.org/10.48550/arXiv.2607.09217 |
| Hypothesis Evolution Protocol | Primary paper | Append-only hypothesis lineage, evidence-gated belief updates, lifecycle states, and independent-auditor opportunity | https://arxiv.org/abs/2607.09195; https://doi.org/10.48550/arXiv.2607.09195 |
| Failure as a Process | Primary paper and official data/code locator | Early decisive errors, lock-in, delayed observability, recovery, fabricated success, and trajectory-aware monitoring | https://arxiv.org/abs/2607.09510; https://github.com/xz-Sean/cli_trajectory_analysis; https://doi.org/10.48550/arXiv.2607.09510 |
| VEXA_IoT | Primary dual-use paper | Controlled autonomous security testing, explicit validation predicates, failure modes, and approval requirements | https://arxiv.org/abs/2607.09653; https://doi.org/10.48550/arXiv.2607.09653 |
| Active rejection for universal interatomic potentials | Primary paper | Calibrated multi-teacher selection, reject option, traceable pseudo-labels, and dynamical robustness | https://arxiv.org/abs/2607.09456; https://doi.org/10.48550/arXiv.2607.09456 |
| ALICE pathology foundation model | Primary paper and official implementation locator | Multi-stage expert consolidation across morphology, language, and slide context; prospective-validation gap | https://arxiv.org/abs/2607.09526; https://github.com/WonderLandxD/ALICE; https://doi.org/10.48550/arXiv.2607.09526 |
| ConceptSMILE | Primary paper | Multidimensional auditing of concept explanations under perturbation | https://arxiv.org/abs/2607.09649; https://doi.org/10.48550/arXiv.2607.09649 |
| MLLM Reward Hacking repository | Official implementation locator | Code and experimental artifacts linked by P1; useful for a future pinned static audit | https://github.com/Theodyy/MLLM-Reward-Hacking |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R0 | [Selected source DEP at `f375b37`](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/f375b375aa053b8e5bd84cb2a49f3bc95a5d4a39/.lake-data/DEP-20260713-Tech%20Intel%201301) | Research boundary, inventory, source roles, and original synthesis | 2026-07-28 | Both Markdown files inspected in full |
| R1 | [Selected DEP README](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/f375b375aa053b8e5bd84cb2a49f3bc95a5d4a39/.lake-data/DEP-20260713-Tech%20Intel%201301/README.md) | Package contents, tags, attribution, and stated collection status | 2026-07-28 | Primary source-bundle metadata |
| R2 | [Daily research findings](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/f375b375aa053b8e5bd84cb2a49f3bc95a5d4a39/.lake-data/DEP-20260713-Tech%20Intel%201301/daily_research_findings_2026-07-13_1301.md) | Original ten findings and interpretations | 2026-07-28 | Inspected in full; claims checked against current papers |
| R3 | Jiayu Yao et al. [*Multimodal Reward Hacking in Reinforcement Learning*](https://arxiv.org/abs/2607.09492), arXiv:2607.09492v1, [full HTML](https://arxiv.org/html/2607.09492v1), [DOI](https://doi.org/10.48550/arXiv.2607.09492) | Experimental framework, reward designs, metrics, results, risks, and appendices | 2026-07-28 | Primary paper inspected beyond abstract |
| R4 | Kaiji Zhou, Ales Leonardis, and Yue Feng. [*Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation*](https://arxiv.org/abs/2607.09600), arXiv:2607.09600v1, [full HTML](https://arxiv.org/html/2607.09600v1), [DOI](https://doi.org/10.48550/arXiv.2607.09600) | Auction, calibration, benchmark protocol, ablations, cost, and limitations | 2026-07-28 | Primary paper inspected beyond abstract |
| R5 | Zihan Xu et al. [*LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making*](https://arxiv.org/abs/2607.09322), arXiv:2607.09322v2, [full HTML](https://arxiv.org/html/2607.09322v2), [DOI](https://doi.org/10.48550/arXiv.2607.09322) | Data pipeline, memory taxonomy, tasks, experiments, ablations, and conflicting cohort counts | 2026-07-28 | Primary paper inspected beyond abstract; not clinical guidance |
| R6 | Matěj Kripner and Milan Straka. [*OpenProver: Agentic and Interactive Theorem Proving with Lean 4*](https://arxiv.org/abs/2607.09217), arXiv:2607.09217v1, [full HTML](https://arxiv.org/html/2607.09217v1), [DOI](https://doi.org/10.48550/arXiv.2607.09217) | Architecture, persistent state, Lean integration, interface, and ProofNet results | 2026-07-28 | Primary paper inspected; proofs not independently checked |
| R7 | Izumi Takahara and Teruyasu Mizoguchi. [*Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents*](https://arxiv.org/abs/2607.09195), arXiv:2607.09195v1, [full HTML](https://arxiv.org/html/2607.09195v1), [DOI](https://doi.org/10.48550/arXiv.2607.09195) | Registry, lifecycle, evidence rules, experiments, base-model comparison, and limits | 2026-07-28 | Primary paper inspected; code not yet public per paper |
| R8 | Xiangxin Zhao et al. [*Failure as a Process: An Anatomy of CLI Coding Agent Trajectories*](https://arxiv.org/abs/2607.09510), arXiv:2607.09510v1, [full HTML](https://arxiv.org/html/2607.09510v1), [DOI](https://doi.org/10.48550/arXiv.2607.09510) | Collection, annotation, timing, root causes, recovery, monitoring, and validity threats | 2026-07-28 | Primary paper inspected beyond abstract |
| R9 | Katherine Swinea et al. [*VEXA_IoT: Autonomous IoT Vulnerability EXploitation using AI Agents*](https://arxiv.org/abs/2607.09653), arXiv:2607.09653v1, [full HTML](https://arxiv.org/html/2607.09653v1), [DOI](https://doi.org/10.48550/arXiv.2607.09653) | Isolated testbed, agent roles, success predicates, results, failures, and future controls | 2026-07-28 | Primary dual-use paper; evidence retained only for defensive, authorized evaluation |
| R10 | Mingxiang Luo et al. [*Active rejection enables reliable generalization of universal machine-learning interatomic potentials*](https://arxiv.org/abs/2607.09456), arXiv:2607.09456v1, [PDF](https://arxiv.org/pdf/2607.09456), [DOI](https://doi.org/10.48550/arXiv.2607.09456) | Candidate pool, routing, rejection, pseudo-labels, held-out tests, MD, and future physical constraints | 2026-07-28 | Complete PDF inspected; file not collected |
| R11 | Jiawen Li et al. [*ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts*](https://arxiv.org/abs/2607.09526), arXiv:2607.09526v1, [full HTML](https://arxiv.org/html/2607.09526v1), [DOI](https://doi.org/10.48550/arXiv.2607.09526) | Staged distillation, datasets, evaluations, retrospective limits, and availability statements | 2026-07-28 | Primary paper inspected beyond abstract; not clinical guidance |
| R12 | Mohadeseh Mollapour et al. [*ConceptSMILE: Auditing the Trustworthiness of Concept-Based Explainable AI*](https://arxiv.org/abs/2607.09649), arXiv:2607.09649v1, [full HTML](https://arxiv.org/html/2607.09649v1), [DOI](https://doi.org/10.48550/arXiv.2607.09649) | Perturbation framework, reproducibility settings, results, and limitations | 2026-07-28 | Primary paper inspected; small proof of concept |
| R13 | [MLLM Reward Hacking](https://github.com/Theodyy/MLLM-Reward-Hacking) | Official implementation locator linked by P1 | 2026-07-28 | Discovered in paper; repository not inspected or collected |
| R14 | [OpenProver](https://github.com/kripner/OpenProver) | Official implementation locator linked by P4 | 2026-07-28 | Discovered in paper; repository not inspected or collected |
| R15 | [CLI trajectory analysis](https://github.com/xz-Sean/cli_trajectory_analysis) | Official data/code locator linked by P6 | 2026-07-28 | Discovered in paper; repository not inspected or collected |
| R16 | [ALICE](https://github.com/WonderLandxD/ALICE) | Official code/model locator linked by P9 | 2026-07-28 | Discovered in paper; repository not inspected or collected |

No external PDF, TeX source, code repository, dataset, model, benchmark payload, prompt corpus, or execution trace was collected or deposited.

## Appendix

### Source Inventory

- Repository sources inspected: `Black-Lake-Data/.lake-data/DEP-20260713-Tech Intel 1301/README.md` and `Black-Lake-Data/.lake-data/DEP-20260713-Tech Intel 1301/daily_research_findings_2026-07-13_1301.md`.
- Primary papers inspected: ten.
- Full-text mode: nine arXiv HTML papers and one complete arXiv PDF.
- External source files collected: none.
- Code/model/data execution: none.

### Replication Checklist

- Pin the paper versions listed in Source Metadata.
- Reconcile the LongMedBench 335/355 cohort discrepancy before dataset-level reproduction.
- Review licenses and access terms before downloading any paper source, dataset, model, or code.
- Audit official repositories at immutable commits before executing code.
- Use isolated, no-egress environments for dual-use security evaluation.
- Reproduce one result per gate type with frozen inputs, metrics, seeds, and expected outputs.
- Compare same-model, independent-model, programmatic, and human validation where feasible.
- Report negative results, rejects, abstentions, and calibration failures alongside successes.
