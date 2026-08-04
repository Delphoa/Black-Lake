---
title: "Evidence-Bound Systems - DEP-E"
generated_at: "2026-08-04T00:02:51Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of ten systems that bind agent, model, scientific, medical, and serving decisions to explicit evidence or state boundaries."
source_status: "URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-04"
temporal_cutoff: "2026-08-04"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260718-Tech%20Intel%201304/README.md"
stable_identifier: "DEP-20260718-Tech Intel 1304; DEP-E-20260804-Evidence-Bound Systems"
confidence_summary: "Medium-high for source characterization; lower for generalization because no reported experiment was independently reproduced."
safety_scope: "defensive, evaluation-oriented, privacy-preserving, and non-clinical"
distribution_notes: "Public derived review; source papers and repositories retain their own licenses and terms."
---

# Evidence-Bound Systems - DEP-E

## Source Metadata

| ID | Source | Authors / organization | Role | Identifier / Version | URL | Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Selected DEP README | Delphoa-Labs | Primary source-package manifest | DEP-20260718-Tech Intel 1304 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260718-Tech%20Intel%201304/README.md | Public repository text | 2026-08-04 | Inspected |
| S2 | Daily Research Findings | Delphoa-Labs | Source synthesis and ten-item inventory | 2026-07-18 record | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260718-Tech%20Intel%201304/daily_research_findings_2026-07-18_1304.md | Public repository text; source-reported claims were rechecked | 2026-08-04 | Inspected |
| S3 | Proof-or-Stop | Jek Huang; Jeffery Hsia; Jiayi Sun; Freddie Shi; Wei Huang; Ian H. White | Primary paper | arXiv:2607.14890v1 | https://arxiv.org/abs/2607.14890 | CC BY-NC-SA 4.0 shown on full-text record | 2026-08-04 | Full HTML inspected |
| S4 | Transcoders for Investigating Deception | Darius Lim; Nathan Leow; Xin Wei Chia | Primary paper | arXiv:2607.14791v1 | https://arxiv.org/abs/2607.14791 | CC BY 4.0 shown on full-text record | 2026-08-04 | Full HTML inspected |
| S5 | SMC-ES | Riccardo Curcio; Toni Mancini; Enrico Tronci | Primary paper | arXiv:2607.15003v1 | https://arxiv.org/abs/2607.15003 | Usage governed by source record | 2026-08-04 | Full HTML inspected |
| S6 | SmartRAG | Zhihan Jiang; Meng Li; Shenghao Liu; Keran Li; Ruiben Zhou; Wei Wang; Xianjun Deng; Shuai Wang; Haipeng Dai | Primary paper | arXiv:2607.14661v2 | https://arxiv.org/abs/2607.14661 | CC BY 4.0 shown on full-text record | 2026-08-04 | Full HTML inspected |
| S7 | TopoAgent | Mingze Xu; Yinghui Li; Jiayi Kuang; Zhanhui Kang; Di Yin; Ying Shen; Xing Sun; Yuxing Han | Primary paper | arXiv:2607.14658v1 | https://arxiv.org/abs/2607.14658 | Usage governed by source record | 2026-08-04 | Full HTML inspected |
| S8 | Alipay-PIBench | Shiyu Ying; Xuejie Cao; Yingfan Ma; Yuanhao Dong; Wenyu Chen; Bowen Song; Lin Zhu | Primary benchmark paper | arXiv:2607.14573v3 | https://arxiv.org/abs/2607.14573 | CC BY 4.0 shown on full-text record | 2026-08-04 | Full HTML inspected; current canonical version checked |
| S9 | AutoSynthesis | Moein Taherinezhad; Sebastian Maier; Gerardo Vitagliano; Francesco Pierri; Stefan Feuerriegel | Primary paper | arXiv:2607.15247v1 | https://arxiv.org/abs/2607.15247 | Usage governed by source record | 2026-08-04 | Full HTML inspected |
| S10 | Demographically-Conditioned Synthetic Medical Images | Mahmoud Ibrahim; Bart Elen; Chang Sun; Gokhan Ertaylan; Michel Dumontier | Primary paper | arXiv:2607.14984v1 | https://arxiv.org/abs/2607.14984 | COVID-19 e-print; not clinical evidence | 2026-08-04 | Complete 17-page PDF text inspected |
| S11 | Seer | Qicheng Zhao; Qi Sun; Zheyu Yan | Primary systems paper | arXiv:2607.14557v1; ACM MM 2026 acceptance stated by source | https://arxiv.org/abs/2607.14557 | CC BY 4.0 shown on full-text record | 2026-08-04 | Full HTML inspected |
| S12 | CEDI | Yijiang Li; Huiqi Zou; Bingyang Wang; Ziang Xiao | Primary evaluation paper | arXiv:2607.14499v1 | https://arxiv.org/abs/2607.14499 | CC BY 4.0 shown on full-text record | 2026-08-04 | Full HTML inspected |

No local source paths are published because no paper, repository, dataset, model, or benchmark payload was collected for deposition.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Source manifest | Package boundary, inventory, attribution, and no-source-file status | Provenance and selected source identity | High | Manifest is not independent evidence for paper results |
| E2 | S2 | Source synthesis | Ranked summaries and original source roles | Discovery and continuity | Medium | Generated synthesis; claims required primary-source checking |
| E3 | S3 | Primary paper and released-artifact locator | Formal claim-admission model, 10/10 mechanism suite, 18 tamper classes, 9,240-cell ablation, threats to validity | Evidence-gated lifecycle control | High for reported study; medium for transfer | One model family, 24 ablation tasks, self-hosted corpus, local-key trust boundary |
| E4 | S4 | Primary paper | Qwen3-4B, 100-prompt dataset, 112 manually identified features, steering and null-group tests | Internal feature evidence for a narrow deception behavior | Medium | One model and transcoder set; manual feature selection; fixed steering strength |
| E5 | S5 | Primary paper | SMC certificate definition, MuJoCo and Safety Gymnasium design, distributed scaling results | Probabilistic policy assurance under sampled scenarios | Medium-high | Simulation only; heavy compute and communication overhead; code pending acceptance |
| E6 | S6 | Primary paper | MRGraph provenance, hybrid retrieval, two-phone deployment, four QA benchmarks, component ablations | Structured local memory under device constraints | Medium-high | LLM judge, heuristic planner, cloud-prepared LoRA and preprocessing, device-specific results |
| E7 | S7 | Primary paper | DAG isolation, atomic fission, six-model and seven-benchmark evaluation, ablation | Structured task state for multimodal science reasoning | Medium | Benchmark-only scientific correctness; no prospective discovery validation; no explicit limitations section |
| E8 | S8 | Primary benchmark paper and official repo locator | Nine projects, 18 tasks, six models, paired skill condition, multiple evaluator modes | Domain-specific executable evaluation | Medium-high | Alipay-specific tasks and agent configuration; LLM-assisted rubric component |
| E9 | S9 | Primary paper | Full meta-analysis workflow, audit traces, retrieval and effect-size comparison with expert reviews | Auditable evidence synthesis | Medium-high | Limited benchmark meta-analyses; only 71.4% study recovery in the main comparison; access and contamination risks |
| E10 | S10 | Primary paper PDF | Patient-disjoint partitions, 22 regimes, five seeds/cohorts, schedule comparison, subgroup proxy analysis | Synthetic-data fairness audit hypothesis | Medium | Single generator and dataset; no privacy audit; not clinical evidence; cross-classifier validity open |
| E11 | S11 | Primary systems paper | Step-0 sparsity boundary, hybrid routing, three model families, nine benchmarks, latency and boundary-error analyses | Output-suffix truncation for DMLLM serving | Medium-high | Architecture-specific; up to 3.8% over-truncation on inspected tasks; broader transfer untested |
| E12 | S12 | Primary evaluation paper and official repo locator | Dynamic examiner, scene-graph grader, human annotation, repeated-run stability, multi-model hallucination results | Context-dependent multimodal evaluation | Medium-high | Ground-truth scene-graph dependence; examiner/grader backbone dependence; transcript-level scoring |

## Executive Summary

The ten primary works do not form one empirical field, but they converge on a useful engineering pattern: consequential outputs become safer or more useful when a system makes the relevant state, evidence, or boundary explicit before it acts. Proof-or-Stop binds lifecycle claims to fresh source-state evidence; SMC-ES binds policy deployment claims to statistical verification; and Alipay-PIBench binds coding-agent success to executable payment and business-state checks. SmartRAG and TopoAgent structure memory and task context so that downstream reasoning receives selected, provenance-aware state rather than an undifferentiated history. AutoSynthesis and CEDI turn research synthesis and multimodal evaluation into inspectable, staged interactions. Seer acts on a measured semantic boundary instead of processing a fixed padded window. These are source-supported mechanisms within their own studies, not evidence that one architecture has been validated across all domains (E3-E12).

The strongest result is therefore a reviewer interpretation, not a new empirical claim: a reusable assurance stack should separate actors from claims, claims from admissible evidence, and evidence from the state transition it authorizes. The papers also show why this separation is incomplete without boundary tests. Proof-or-Stop cannot prove semantic correctness; SMC-ES certificates inherit a scenario distribution; internal deception features may not generalize beyond Qwen3-4B; graph memory can retrieve peripheral evidence; synthetic medical proxies retain distribution and privacy questions; and CEDI depends on its examiner, grader, and scene graphs. Confidence is medium-high that the source set supports this cross-domain design heuristic, but low that any reported metric transfers unchanged to a new deployment.

## Detailed Summary

### Claim admission and assurance

Proof-or-Stop provides the most explicit control semantics. Actor output is treated as a claim; a transition advances only when evidence is fresh, complete, integrity-checked, produced by an authorized actor, execution-attested when necessary, relevant to the claim, and accepted by the gate. In its reported implementation, source-state hashes and receipt identities reject stale or altered evidence. The paper reports 10/10 unattended-loop contract scenarios with zero false-DONE, rejection of 18 tamper classes with zero false accepts, and a powered comparison where a compute-budgeted naive loop amplified 31 of 1,800 visible-pass/hidden-fail cells while the gated loop amplified 2 of 1,800. The near-compute review-only condition amplified 14 of 1,800, supporting the narrower mechanism claim that enforcing review as a transition gate differs from merely receiving reviewer advice. The source explicitly limits the result to one model family, 24 ablation tasks, and a self-hosted corpus (E3).

SMC-ES applies an analogous discipline to learned control. It combines evolutionary strategies with statistical model checking so that, given allowable violation probability epsilon and confidence parameter delta, the produced policy has a certificate that violations occur with probability at most epsilon with confidence at least 1-delta under the sampled scenario model. The evaluation spans standard MuJoCo, SafetyVelocity tasks with rewards that conflict with velocity limits, and noise-augmented variants. The paper reports verified zero-violation policies competitive with selected safe-DRL baselines, but the guarantee is statistical, simulation-bound, and specification-dependent. Scaling SafetyHalfCheetahVelocity from 128 to 1,024 CPU cores reduced time from 4.05 to 1.02 hours with diminishing efficiency, and the authors leave sim-to-real evaluation and communication optimization for future work (E5).

Alipay-PIBench turns payment integration into a layered evidence problem. Nine product-specific projects create 18 Basic and Advanced tasks. Rubrics combine static, unit, integration, end-to-end, and LLM-assisted checks, exposing differences between source-level structure, executable workflows, and payment-domain correctness. Six coding-agent models achieved mean rubric pass rates from 68.58% to 91.37% with the payment skill; the paired skill condition improved mean performance by 10.31 percentage points, with gains in 101 of 108 model-product-scenario comparisons. The benchmark's deeper value is not a universal model ranking but its controlled separation of transaction state, business state, idempotence, notification authenticity, and refund boundaries (E8).

### Inspectable internal and external state

The transcoder study asks whether internal feature circuits can provide earlier evidence of a narrowly defined deceptive behavior: withholding a secret when instructed. On 100 templated prompts with Qwen3-4B and pre-trained per-layer transcoders, researchers manually traced 112 features and found the ten most frequent across 55%-95% of prompts. Negative steering of the top ten converted all tested deceptive prompts to non-deceptive outputs; a two-feature pair involving secrets/confidentiality and obscuring information also outperformed control pairs. This supports causal influence in the tested setup, not a universal deception detector. Manual selection, one model, one transcoder set, and fixed alpha 5 keep confidence moderate (E4).

SmartRAG makes external state explicit through Perception, Memory, Focus, and Thinking. EvoNER adds entity types through reserved labels and teacher-distilled updates; MRGraph stores entity-paragraph links and source pointers; hybrid graph, lexical, and dense retrieval assembles bounded evidence; the LLM is reserved for labeling, planning, and answer synthesis. On two OnePlus phones, compact Q6_K backbones were tested across four QA benchmarks. With Qwen3-1.7B, SmartRAG reported correctness/F1 of 66.68/54.84 on Natural Questions and 63.93/51.27 on HotpotQA; removing MRGraph reduced the ablation's token-F1 from 0.5484 to 0.4151. The evaluation still uses an LLM judge and cloud-prepared data and LoRA steps, and retrieval-conditioned prefilling dominates latency (E6).

TopoAgent structures a scientific task as visually grounded atoms in a dependency DAG, passes only prerequisite state downstream, and splits failed nodes through adaptive atomic fission. Across six multimodal models and mathematics, physics, and chemistry benchmarks, the source reports a 66.3% global average versus 58.1% for LangChain and 62.0% for AutoGen. Removing DAG planning reduced the average by 1.4 points; disabling fission reduced it by 0.6 points. These results support benchmark-level context isolation and recovery, but the source does not demonstrate prospective scientific discovery, laboratory validity, or independent reproduction (E7).

### Auditable research, fairness, and evaluation

AutoSynthesis maps a natural-language research question into protocol design, search, screening, full-text eligibility, statistical extraction, validation, standardized effect sizes, random-effects meta-analysis, heterogeneity and bias analyses, and a PRISMA-aligned report with traces. In the persuasive-LLM case it retrieved 28 records, retained 19 full-text-eligible studies, and included eight studies with 20 effect sizes. Its pooled estimate was Hedges' g=0.143 with 95% CI [0.059, 0.226], while the main comparison recovered 71.4% of the human review's studies and differed by 0.12 Hedges' g. The paper positions the system as a checking and update aid, not a substitute for expert protocol and interpretation, and identifies retrieval/full-text access as the largest discrepancy source (E9).

The medical-imaging paper separates synthetic data's training and evaluation roles. It uses 168,694 COVIDx-CT-3A slices from 1,718 patients with patient-disjoint partitions, a fine-tuned Stable Diffusion 2.1 generator, 22 DenseNet-121 regimes, and subgroup metrics over sex-age cells. Balanced synthetic pretraining followed by fine-tuning on 585 real slices reported mean/worst-cell MCC of 0.83/0.52 versus 0.78/0.17 for the full biased real baseline. At nearly fixed data, sequential pretraining improved worst-cell MCC by 0.367 +/- 0.040 over joint augmentation. For evaluation, a large synthetic cohort matched the well-powered real oracle's MCC and recall subgroup rankings at Spearman rho=1.00, but threshold-sensitive aggregate metrics drifted and the real test remained better in well-sampled cells. The source itself restricts the result to one generator and one dataset and calls for membership-inference and nearest-neighbor privacy analysis. It is not clinical evidence (E10).

CEDI evaluates visual models through an examiner, an evaluatee, and a grader over graph-guided multi-turn interactions. A scene-graph grader compares transcript-derived and ground-truth structures, while human annotations provide a reference for hallucination judgments. Across multiple models and datasets, CEDI elicited more hallucinations than caption, prompt-only, and binary-question baselines; the study reports that errors accumulate through self-reinforcing dialogue and that premise-rejection and refusal questions are especially difficult. Repeated-run scene-graph metrics had standard deviations below 1% of their means. Dependence on scene graphs, GPT-4o as the default examiner, and model-based parsing/grading make this an evaluation instrument that itself requires calibration (E12).

### Computation boundary

Seer observes a sparsity jump and plateau in early-layer text-side MLP activations at the first denoising step of diffusion multimodal LLMs, then truncates the predicted redundant suffix once. A hybrid static, packed-variable, and eager router tries to preserve CUDA-graph efficiency across mixed lengths. Across three model variants and nine benchmarks, the paper reports up to 30.9x throughput improvement in a named InfoVQA setting while accuracy rose from 15.11 to 15.29, and 10.5x on a MathVista setting with a 1.31% relative accuracy decrease. Boundary mean absolute error ranged from 0.40 to 1.18 on three reported datasets, with 0.8%-3.8% over-truncation. The mechanism is promising but architecture- and workload-specific (E11).

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Fresh, state-bound evidence gates reduced hidden-failure amplification in the reported software-agent ablation. | Source claim | E3 | Supported within the powered, one-family study; not semantic correctness or broad deployment proof. | High within scope |
| C2 | SMC-ES produces statistical safety certificates for synthesized policies under its scenario and specification model. | Source claim | E5 | The certificate is meaningful but distribution-, simulator-, and property-bound. | Medium-high |
| C3 | Internal transcoder features causally influenced the tested secret-withholding behavior. | Source claim | E4 | Steering supports causal influence, while manual feature discovery and one-model scope limit detector claims. | Medium |
| C4 | Explicit structured memory, dependency state, and dynamic interaction can expose or reduce context failures. | Reviewer synthesis | E6, E7, E12 | Supported as a pattern across separate benchmarks; no shared task or causal comparison exists. | Medium |
| C5 | Multi-method payment evaluation localizes failures that a single code or execution check can miss. | Source-supported interpretation | E8 | Strong within the Alipay project set; generalization to other payment ecosystems is untested. | Medium-high |
| C6 | Automated evidence synthesis can approximate selected expert meta-analyses while remaining retrieval-limited. | Source claim | E9 | Supported by reported comparisons; 71.4% study recovery makes human review essential. | Medium-high |
| C7 | Balanced synthetic pretraining and synthetic subgroup auditing improved the reported fairness results. | Source claim | E10 | Strong study-specific results, but one dataset/generator and missing privacy evaluation prevent clinical or general claims. | Medium |
| C8 | Step-0 sparsity can guide efficient one-shot suffix truncation in tested DMLLMs. | Source claim | E11 | Supported across tested models/benchmarks; premature truncation and architecture transfer remain open. | Medium-high |
| C9 | Evidence-bound state transitions form a reusable cross-domain design heuristic. | Reviewer inference | E3-E12 | Useful conceptual synthesis, not independently benchmarked as one architecture. | Medium |

## Methodology

- `Research objective`: Determine what the selected ten-source package supports about explicit evidence, state, evaluation, and computation boundaries, and preserve it as a DEP-ready manuscript.
- `Sources inspected`: The selected DEP README and findings file; canonical arXiv records for all ten works; full experimental HTML for nine papers; the complete 17-page PDF text for the medical-imaging paper; source-reported official implementation locators where visible.
- `Discovery strategy`: Repository-first inspection, exact identifier matching, canonical arXiv record checks, full-text section inspection, results/limitations tracing, and code-availability checks. No general secondary-source search informed technical claims.
- `Inclusion criteria`: All ten ranked findings in the selected DEP and official repositories explicitly linked by their papers.
- `Exclusion criteria`: Background citations were excluded from substantive review; aggregator claims, commentary, and sources not inspected were not used as evidence.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication-oriented synthesis.
- `Evidence handling`: Each major statement is mapped to an evidence-ledger item; source claims, reviewer interpretations, and inference are labeled separately.
- `Uncertainty handling`: Simulation, benchmark, single-model, missing-code, privacy, and clinical limits are retained beside the relevant claims.
- `Extraction process`: Tables, methods, ablations, conclusions, availability statements, and limitation sections were inspected. The medical PDF's textual tables and figure captions were checked; no local source file was retained.
- `Version control`: Current arXiv version histories were checked on 2026-08-04. Alipay-PIBench is recorded as v3 and SmartRAG as v2; the remaining records were v1.
- `Reviewer stance`: Initial source-first synthesis, critique, implementation translation, and replication planning. No prior direct artifact existed for this DEP, so no supporting-thread expansion draw was performed.

## Scope, Constraints, and Assumptions

- `Scope`: One selected source DEP and the ten primary records it identifies.
- `Temporal boundary`: Sources accessible through 2026-08-04; later revisions may change results or availability.
- `Evidence limits`: No code, model, dataset, benchmark payload, experiment log, device, controller, clinical workflow, or repository implementation was executed. Repository links were inspected only as source-reported availability surfaces.
- `Assumptions`: The selected DEP's inventory is a discovery aid, while canonical records and full texts control technical attribution.
- `Constraints`: Public-source review only; no private data, credentials, payment environment, patient data, or safety-critical control system was accessed.
- `Out of scope`: Clinical guidance, production safety certification, offensive deception manipulation, live payment transactions, and claims of independent reproducibility.
- `Intended use`: DEP deposition, design review, research backlog, defensive evaluation planning, and provenance-preserving follow-on synthesis.
- `Audience`: Researchers, agent-platform engineers, evaluation designers, ML systems engineers, and governance reviewers.
- `Reproducibility boundary`: Literature assertions can be traced; empirical claims cannot be reproduced from this manuscript alone.
- `Data sensitivity`: Public metadata and papers only. Medical and personal-memory implications are discussed conceptually with privacy-preserving boundaries.

## Observations

- `Observed pattern`: The most credible systems separate a proposal from the condition that authorizes action: agent claim versus gate, candidate policy versus certificate, code change versus domain checks, retrieved item versus provenance, and predicted suffix versus measured boundary.
- `Technical implication`: Evidence identity needs both content and context. A hash without an authorized producer or accepted outcome is incomplete; a metric without its scenario distribution or threshold is equally incomplete.
- `Contradiction or tension`: More structure can add overhead or new failure modes. Proof-or-Stop adds token and control cost, SMC-ES adds distributed verification cost, graph retrieval can surface peripheral evidence, and dynamic evaluators inherit examiner/grader bias.
- `Observed pattern`: Static success often hides state-dependent failure. This appears in hidden tests, multi-turn hallucinations, asynchronous payment flows, subgroup cells, and fixed-length serving.
- `Open question`: Which minimal boundary schema transfers across domains without erasing domain-specific semantics?
- `Reviewer hypothesis`: A small common envelope—artifact identity, state version, claim, evidence locator, producer, evaluator, threshold, decision, expiry, and unresolved limitations—could support cross-domain audit without pretending that evidence types are interchangeable.

## Considerations

- Assurance labels must state the trust model. Local-key integrity, statistical confidence, benchmark accuracy, and clinical validity are different claims.
- Provenance-aware memory still contains sensitive personal context. On-device storage reduces exposure but does not remove access control, retention, poisoning, deletion, or backup risks.
- Internal-feature monitoring can create false confidence and dual-use risk. Defensive use should require distribution-shift tests, human review, and output-level corroboration.
- Medical synthetic data needs generator-fidelity, privacy, subgroup, threshold, and site-shift validation. Synthetic performance must not be presented as clinical effectiveness.
- Payment evaluation should use sandboxed, synthetic transactions and deterministic test doubles. Real credentials and funds are outside this artifact's scope.
- Automated meta-analysis should expose search coverage, inaccessible full texts, extraction confidence, and expert overrides rather than only a pooled estimate.
- Dynamic evaluation must audit the evaluator. Examiner prompts, grader versions, scene-graph quality, and repeated-run stability belong in the evidence package.
- Efficiency boundaries need a fail-open/fail-closed choice. Over-truncation should be detectable, bounded, and reversible when answer integrity matters more than throughput.

## Strengths

- The source set spans mechanism tests, ablations, benchmarks, statistical synthesis, device measurements, and a full medical subgroup study, allowing a richer comparison than abstract-only review.
- Several papers publish explicit boundary conditions instead of treating them as footnotes: Proof-or-Stop separates operational proof from semantic correctness; AutoSynthesis preserves expert judgment; and the medical paper distinguishes rank detection from absolute calibration.
- Component ablations in Proof-or-Stop, SmartRAG, TopoAgent, Alipay-PIBench, and Seer help connect observed improvements to mechanisms rather than only reporting end scores.
- Multiple works make evidence inspectable through receipts, provenance links, audit traces, scene graphs, rubrics, or repository artifacts.
- The cross-domain synthesis yields concrete design questions while keeping source-specific metrics and caveats separate.

## Weaknesses

- No study was independently executed in this review, so all performance and reproducibility claims remain source-reported.
- The source set is heterogeneous; there is no common baseline, cost model, failure taxonomy, or external validation that tests the proposed cross-domain heuristic.
- Several results are narrow: one model/transcoder set for deception, one generator/dataset for medical fairness, Alipay-specific integrations, and selected DMLLM architectures for Seer.
- Some availability claims are incomplete at access time. SMC-ES states that its repository will be public upon acceptance; SmartRAG, TopoAgent, AutoSynthesis, and Seer do not expose a paper-specific repository in the inspected full text.
- Evaluation instruments introduce their own uncertainty: LLM judges, LLM-assisted rubrics, scene-graph parsing, examiner backbones, and manually identified internal features.
- Safety claims can be over-read. Statistical or mechanistic evidence is not equivalent to real-world safety certification, clinical validity, or semantic correctness.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish one common evidence-envelope schema with domain extensions | Cross-domain interoperability | Makes identity, freshness, producer, evaluator, threshold, and limitations comparable | Easier audit and replay | Oversimplification | Map all ten studies and record fields that cannot be normalized |
| Run external, equal-budget replications | Evidence quality | Most claims are author-run and configuration-specific | Better causal and transfer confidence | High compute and access cost | Pre-register tasks, seeds, budgets, and negative results |
| Add evaluator calibration artifacts | Benchmarks and audits | Judges and graders can be failure sources | More trustworthy metrics | Annotation cost | Human reference sets, inter-rater agreement, repeated runs, adversarial evaluator tests |
| Add privacy and deletion tests | SmartRAG and synthetic medical data | Local or synthetic data can still leak or persist | Safer deployment boundaries | May reduce utility | Membership inference, nearest-neighbor analysis, deletion verification, poisoned-memory recovery |
| Couple dynamic boundaries to reversible fallbacks | Seer and task decomposition | Prediction errors can truncate valid state or split tasks poorly | Safer adaptive execution | More latency | Confidence bands, retry paths, oracle comparison, worst-case tests |
| Release pinned implementations and complete artifacts | SMC-ES, SmartRAG, TopoAgent, AutoSynthesis, Seer | Source availability determines reproducibility | Stronger independent review | Maintenance burden | Immutable tag, environment image, fixtures, expected outputs, license manifest |

## Potential Implementations

### Evidence admission service

- `User`: Agent-platform and CI maintainers.
- `Goal`: Prevent stale or unsupported completion, review, test, and release claims.
- `Core mechanism`: A small policy engine accepts signed evidence envelopes bound to artifact state and evaluates domain-specific gates.
- `Required inputs`: Repository identity, state digest, claim type, producer identity, command/result receipt, reviewer record, policy version, and expiry.
- `Outputs`: Admit, repair, escalate, or stop decisions with an audit record.
- `Risk controls`: Least-privilege signers, replay protection, policy review, no secret-bearing logs, override audit, and fail-closed handling for high-consequence claims.
- `Evaluation`: Inject stale, forged, incomplete, wrong-scope, and adversarially plausible evidence in a synthetic repository.

### Context provenance workbench

- `User`: Researchers and local-assistant builders.
- `Goal`: Make retrieved memory and task dependencies inspectable before generation.
- `Core mechanism`: Store source-linked graph nodes, isolate task state by dependency, and expose the exact evidence bundle used for each response.
- `Required inputs`: Public or user-authorized documents, entity/relation extraction, task DAG, retrieval scores, and source pointers.
- `Outputs`: Bounded context package, dependency trace, answer, and unresolved-evidence list.
- `Risk controls`: Local-only default, encryption, retention limits, user deletion, poisoning detection, and no automatic high-impact action.
- `Evaluation`: Synthetic multi-hop questions with distractors, stale facts, poisoned nodes, missing dependencies, and deletion requests.

### Adaptive evaluation harness

- `User`: Model-evaluation and domain-safety teams.
- `Goal`: Reveal stateful failures missed by static prompts while measuring evaluator reliability.
- `Core mechanism`: Graph-guided multi-turn probes, domain-specific executable checks, and an evaluator evidence ledger.
- `Required inputs`: Synthetic task states, examiner policy, deterministic or human reference, grader versions, stop conditions, and thresholds.
- `Outputs`: Failure trajectories, grader agreement, coverage, state-transition errors, and reproducible fixtures.
- `Risk controls`: Sandboxed payment/control/medical simulations, no real credentials or patient data, bounded adversarial probes, and human review.
- `Evaluation`: Compare static versus dynamic detection at equal budget and report both model and evaluator error.

## Three Ways to Exercise This Research

1. `Synthetic claim-gate replay`: Objective—test whether state-bound evidence blocks false completion; inputs—a toy repository, five seeded defects, synthetic receipts, and a fixed gate policy; method—run valid, stale, forged, incomplete, and correct evidence cases; output—a decision ledger; success criterion—every invalid case stops while valid current evidence advances; stop condition—any credential, external repository, or unbounded command is requested.
2. `Provenance-aware context ablation`: Objective—measure whether source-linked graph state improves multi-hop answers; inputs—a small public document set with distractors and a gold answer graph; method—compare plain dense retrieval, graph-only retrieval, and hybrid bounded context under the same model and token budget; output—accuracy, citation precision, latency, and deletion/poisoning results; success criterion—improvement survives repeated seeds without provenance loss; stop condition—private or non-redistributable data enters the set.
3. `Dynamic evaluator calibration`: Objective—measure both model and examiner/grader error; inputs—synthetic images or diagrams with known scene graphs and scripted multi-turn traps; method—compare static, binary, and graph-guided probes with human reference labels; output—failure coverage, false-positive rate, inter-rater agreement, and repeated-run stability; success criterion—dynamic probing adds verified failures without unacceptable evaluator error; stop condition—the evaluator cannot distinguish unsupported prompts from ground truth.

## Example MVP Product

- `Product name`: Boundary Ledger
- `Target user`: Teams operating coding or research agents in controlled environments.
- `Problem`: Agent claims, retrieved context, evaluator verdicts, and execution results are often stored separately and can be stale, unverifiable, or consumed outside their scope.
- `Core workflow`: Register a work item; compute a public-safe artifact identity; accept structured evidence from tools and reviewers; evaluate a versioned gate; display admit/repair/escalate/stop; export a redacted audit bundle.
- `Data requirements`: Synthetic or public test fixtures, hashes, command exit metadata, policy identifiers, reviewer decisions, and source URLs. Secrets and raw sensitive content are excluded.
- `Architecture`: Local CLI and SQLite event store, deterministic gate evaluator, optional signed receipts, read-only dashboard, and export sanitizer. Domain extensions supply their own predicates without changing the core ledger.
- `Success metrics`: Zero false admissions across the seeded invalid-evidence suite; 100% replay determinism; complete provenance for every decision; median local decision latency below one second; zero sensitive-path findings in exported bundles.
- `Risk controls`: Local-only default, allowlisted commands, redaction before export, role-separated signers, append-only audit events, expiry checks, manual override with justification, and no automated production/clinical/payment action.
- `Limitations`: The MVP verifies evidence admission, not semantic correctness; it does not independently attest a compromised runner; and domain predicates require expert ownership.
- `MVP boundary`: One repository, synthetic fixtures, no cloud service, no real transactions, no patient data, and no autonomous merge.
- `Deployment model`: Local CLI plus read-only browser dashboard.
- `Evaluation plan`: Unit tests for gate predicates, property tests for replay and tamper resistance, seeded end-to-end fixtures, and a human review of false stops.
- `Failure modes`: Incorrect policy, authorized-but-compromised producer, missing domain evidence, hash exclusions that omit relevant state, and sanitizer failure.
- `Maintenance plan`: Version policies and schemas, rotate signing keys, retain migration tests, refresh fixtures quarterly, and audit exports before release.

## Related Research and Reading

### Primary records retained from the selected DEP

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| Proof-or-Stop | Evidence-gated agent lifecycle | Formalizes actor-output-as-claim and state-bound evidence admission. | https://arxiv.org/abs/2607.14890 |
| Transcoders for Investigating Deception | Mechanistic interpretability | Tests whether feature circuits provide internal evidence for a narrow behavior. | https://arxiv.org/abs/2607.14791 |
| SMC-ES | Statistical verification and control | Connects policy synthesis to explicit probability/confidence certificates. | https://arxiv.org/abs/2607.15003 |
| SmartRAG | On-device memory and retrieval | Preserves provenance in structured local memory under device constraints. | https://arxiv.org/abs/2607.14661 |
| TopoAgent | Scientific agent orchestration | Uses dependency graphs and adaptive task fission to isolate context and recover from tool limits. | https://arxiv.org/abs/2607.14658 |
| Alipay-PIBench | Coding-agent benchmark | Separates code structure, executable workflow, and payment-domain correctness. | https://arxiv.org/abs/2607.14573 |
| AutoSynthesis | Automated meta-analysis | Makes staged evidence synthesis and intermediate decisions auditable. | https://arxiv.org/abs/2607.15247 |
| Demographically-Conditioned Synthetic Medical Images | Medical-AI fairness research | Tests synthetic cohorts as representation priors and subgroup-audit proxies. | https://arxiv.org/abs/2607.14984 |
| Seer | Multimodal inference systems | Uses a measured semantic boundary to avoid redundant suffix computation. | https://arxiv.org/abs/2607.14557 |
| CEDI | Dynamic multimodal evaluation | Exposes context-dependent hallucinations through multi-turn graph-guided probing. | https://arxiv.org/abs/2607.14499 |

### Official implementations and reproduction surfaces

| Item | Type | Relevance | URL |
|---|---|---|---|
| Proof-or-Stop organization | Source-reported implementation and release artifacts | Reproduction entry point for gates, receipts, and ablation artifacts. | https://github.com/Proof-or-Stop |
| Circuit Tracer | Official tool used by the transcoder study | Provides the pre-trained Qwen3-4B transcoder and attribution tooling named by the paper. | https://github.com/decoderesearch/circuit-tracer |
| PIBench | Official benchmark repository | Source-reported code surface for Alipay-PIBench tasks and evaluation. | https://github.com/inclusionAI/PIBench |
| Synthetic Fairness | Author repository | Source-reported training and evaluation code for the medical paper; not executed here. | https://github.com/mahmoudibrahim98/synthetic-fairness |
| CEDI | Author repository | Source-reported implementation for dynamic multimodal evaluation; not executed here. | https://github.com/williamium3000/cedi |

This is an initial synthesis. All ten primary threads are new to this DEP-E pass; no prior direct artifact existed, so no iterative supporting-document draw was required.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260718-Tech%20Intel%201304/README.md | E1, source package identity and attribution | 2026-08-04 | Public repository path; no local path published |
| R2 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260718-Tech%20Intel%201304/daily_research_findings_2026-07-18_1304.md | E2, ten-item discovery inventory | 2026-08-04 | Source synthesis; primary claims independently checked |
| R3 | https://arxiv.org/abs/2607.14890 | E3, evidence-gated lifecycle control | 2026-08-04 | v1; complete HTML inspected |
| R4 | https://arxiv.org/abs/2607.14791 | E4, transcoder feature circuits | 2026-08-04 | v1; complete HTML inspected |
| R5 | https://arxiv.org/abs/2607.15003 | E5, statistical policy verification | 2026-08-04 | v1; complete HTML inspected; paper says code will be public upon acceptance |
| R6 | https://arxiv.org/abs/2607.14661 | E6, structured on-device memory | 2026-08-04 | v2; complete HTML inspected |
| R7 | https://arxiv.org/abs/2607.14658 | E7, topological scientific reasoning | 2026-08-04 | v1; complete HTML inspected |
| R8 | https://arxiv.org/abs/2607.14573 | E8, payment-integration benchmark | 2026-08-04 | v3 canonical record; full HTML and version history inspected |
| R9 | https://arxiv.org/abs/2607.15247 | E9, automated meta-analysis | 2026-08-04 | v1; complete HTML inspected |
| R10 | https://arxiv.org/abs/2607.14984 | E10, synthetic medical fairness | 2026-08-04 | v1; complete 17-page PDF text inspected; not clinical evidence |
| R11 | https://arxiv.org/abs/2607.14557 | E11, DMLLM suffix truncation | 2026-08-04 | v1; complete HTML inspected |
| R12 | https://arxiv.org/abs/2607.14499 | E12, dynamic multimodal evaluation | 2026-08-04 | v1; complete HTML inspected |
| R13 | https://github.com/Proof-or-Stop | E3 reproduction locator | 2026-08-04 | Source-reported official organization; code not executed |
| R14 | https://github.com/decoderesearch/circuit-tracer | E4 implementation dependency | 2026-08-04 | Repository named by paper; code not executed |
| R15 | https://github.com/inclusionAI/PIBench | E8 benchmark locator | 2026-08-04 | Source-reported official repository; not executed |
| R16 | https://github.com/mahmoudibrahim98/synthetic-fairness | E10 code locator | 2026-08-04 | Author repository named by paper; not executed |
| R17 | https://github.com/williamium3000/cedi | E12 code locator | 2026-08-04 | Author repository named by paper; not executed |

## Appendix

### Selection and eligibility record

- Automation family: `Black-Lake Data Processing & Review` and `Black-Lake Data Processing & Review 0900`.
- Fixed UTC run timestamp: `2026-08-04T00:02:51Z`.
- 24-hour cutoff: `2026-08-03T00:02:51Z`.
- Canonical candidate count: 104.
- Excluded recent-marker count: 2.
- Eligible count: 102.
- Excluded DEPs: `DEP-20260709-Tech Intel 1305` and `DEP-20260716-Tech Intel 1303`.
- Eligible-list SHA-256: `d6e97a65f2b5b979ab329b100421a01c4faafc89d2ef52cb20a4829e16e30c62`.
- Random method: OS-cryptographic UInt32 rejection sampling.
- Accepted UInt32: `2396016881`; attempt: 1; rejection limit: `4294967244`; zero-based index: 59.
- Selected DEP: `DEP-20260718-Tech Intel 1304`.

### Replication checklist

- [x] Source DEP README and findings inspected first.
- [x] Ten canonical arXiv records checked for title, authors, and version.
- [x] Nine complete HTML papers and one complete PDF text inspected.
- [x] Claims separated from reviewer interpretation.
- [ ] Code repositories pinned and executed.
- [ ] Datasets, models, benchmarks, devices, simulations, transactions, or clinical workflows reproduced.
- [ ] Cross-domain evidence-envelope hypothesis independently evaluated.

### Source inventory

No original source files were collected or deposited. Public URLs, versions, access dates, source roles, and availability limits are preserved above.
