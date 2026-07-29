---
title: "Evidence-Gated Systems - DEP-E"
generated_at: "2026-07-27"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of ten works on recoverable long-context memory, selective agent-memory updates, prompt-injection evaluation, layered agent security, agent governance, clinical evidence evaluation, medical visual-token selection, and verified quantum preprocessing."
source_status: "Repository files, canonical public records, full papers, prior DEP artifacts, and official implementation surfaces inspected; no external source file deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-27"
temporal_cutoff: "2026-07-27"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/c6cee063d86e6144c69890ba197f84d5a972c3c6/.lake-data/DEP-20260702-Tech%20Intel%200103"
stable_identifier: "DEP-20260702-Tech Intel 0103"
confidence_summary: "High for bibliographic identity and the claims directly reported in the inspected papers; medium for cross-paper synthesis; low for independent reproducibility because no code, model, dataset, benchmark, clinical workflow, or quantum experiment was executed."
safety_scope: "Defensive security evaluation, evidence governance, clinical-evaluation research, and non-operational quantum-software analysis"
distribution_notes: "No source files are redistributed. Repository-relative provenance, immutable public links, and date-only or UTC-only run provenance are used."
---

# Evidence-Gated Systems - DEP-E

## Source Metadata

The primary research object is the two-file source bundle `Black-Lake-Data/.lake-data/DEP-20260702-Tech Intel 0103` at source commit `c6cee063d86e6144c69890ba197f84d5a972c3c6`. Its `README.md` and `daily_research_findings_2026-07-02_0103.md` were inspected in full. The bundle identifies ten arXiv papers spanning AI memory and serving, agent security and governance, medical evaluation and visual reasoning, and quantum compilation and preprocessing.

Two older DEP-A artifacts were found for papers in this source bundle: the SeKV review and the Janus review. No same-family source `.reports` entry, Black-Lake `.logs` entry, or Report-Mark existed for the selected DEP. Because prior DEP Class material did exist, this pass applied the iterative-expansion rule. A cryptographic random draw over four accessible supporting items selected `Black-Lake/.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/README.md`. That artifact and its full companion review were inspected, and the new comparison between recoverable SeKV memory and irreversible CompressKV eviction is carried into `Related Research and Reading`.

| ID | Work / producing organization | Platform and date | Identifier / version | URL / repository-relative path | Access and usage notes | Access date | Status |
|---|---|---|---|---|---|---|---|
| S0 | `DEP-20260702-Tech Intel 0103`; Black-Lake-Data | GitHub; deposited 2026-07-02 | Commit `c6cee063d86e6144c69890ba197f84d5a972c3c6` | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/c6cee063d86e6144c69890ba197f84d5a972c3c6/.lake-data/DEP-20260702-Tech%20Intel%200103 | Both Markdown files inspected; original local-time text treated only as evidence and not reproduced as run provenance | 2026-07-27 | Complete source bundle inspected |
| S1 | *SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference*; Amirhossein Abaskohi, Giuseppe Carenini, Peter West, Yuhang He | arXiv; submitted 2026-06-30 | arXiv:2606.31145v1 | https://arxiv.org/abs/2606.31145v1 | Canonical record and full paper inspected; official implementation README inspected at commit `6569d111d3ace5c7c1ad596bf36962a99cd7e94b` | 2026-07-27 | Primary paper and implementation surface inspected |
| S2 | *The Past Is Prologue: A Plug-in Controller for Selective Updates in Sequentially Evolving LLM Memory*; Zihan Chen, Songwei Dong, Chengshuai Shi, Peng Wang, Song Wang, Cong Shen, Jundong Li | arXiv; submitted 2026-06-30 | arXiv:2606.31121v1 | https://arxiv.org/abs/2606.31121v1 | Canonical record and full paper inspected; no official implementation link was identified in the paper | 2026-07-27 | Primary paper inspected |
| S3 | *Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense*; Mitchell Hermon, Rahul Gupta, Weitong Ruan, Ekraam Sabir, Haohan Wang | arXiv / ICML 2026; submitted 2026-06-29 | arXiv:2606.30783v1 | https://arxiv.org/abs/2606.30783v1 | Canonical record and full paper inspected; security content summarized defensively without operational attack instructions | 2026-07-27 | Primary paper inspected |
| S4 | *Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming*; Yong Yang, Xing Zheng, Huiyu Wu, et al. | arXiv; submitted 2026-06-30 | arXiv:2606.31227v1 | https://arxiv.org/abs/2606.31227v1 | Canonical record and full report inspected; official implementation README inspected at commit `51d0584360aea91ec24eaa996cf02372f54dc185` | 2026-07-27 | Primary report and implementation surface inspected |
| S5 | *Governance Gaps in Agent Interoperability Protocols: What MCP, A2A, and ACP Cannot Express*; Richard Kang, Yudho Diponegoro | arXiv; submitted 2026-06-30 | arXiv:2606.31498v1 | https://arxiv.org/abs/2606.31498v1 | Canonical record and full paper inspected; protocol findings are a June 2026 specification snapshot | 2026-07-27 | Primary paper inspected |
| S6 | *AtomiMed: Hierarchical Atomic Fact-Checking for Universal Clinical-Aware Medical Report Evaluation*; Yuan Wang, Wanxing Chang, Songtao Jiang, et al. | arXiv; submitted 2026-06-30 | arXiv:2606.31292v1 | https://arxiv.org/abs/2606.31292v1 | Canonical record and full paper inspected; official repository README inspected at commit `3149cbf4ef77ddb3c6cbd3532b73e35280c031b6` | 2026-07-27 | Primary paper and partial implementation surface inspected |
| S7 | *Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning*; Kaitao Chen, Weiqian Zhao, Jiamin Wu, et al. | arXiv / ICML 2026; submitted 2026-06-30 | arXiv:2606.31599v1 | https://arxiv.org/abs/2606.31599v1 | Canonical record and full paper inspected; official repository README inspected at commit `b129fcba9742f947d2f0d3fb3cf906c2916377cd` | 2026-07-27 | Primary paper inspected; public code surface minimal |
| S8 | *Context-Verified, Error-Budget-Aware Decomposition Selection for Toffoli Networks*; Karol Bartkiewicz, Patrycja Tulewicz | arXiv; submitted 2026-06-30 | arXiv:2606.31791v1 | https://arxiv.org/abs/2606.31791v1 | Canonical record and full paper inspected; official implementation README inspected at commit `f39807eb9f42feed81fd05744f4cbc983ca4bd83` | 2026-07-27 | Primary paper and implementation surface inspected |
| S9 | *Automatic quantum function parallelization and memory management in Qrisp*; Raphael Seidel | arXiv; submitted 2026-06-30; paper notes original IWQC 2024 publication | arXiv:2606.31837v1 | https://arxiv.org/abs/2606.31837v1 | Canonical record and full paper inspected; Qrisp README inspected at commit `1c70e7ef7b1f23443a7cb98b1ed5d2e8615a7070` | 2026-07-27 | Primary paper and current framework surface inspected |
| S10 | *An efficient Pauli decomposition algorithm for structured matrices*; Daniel J. Spencer, Kishor Bharti, Alexey V. Gorshkov | arXiv; submitted 2026-06-30 | arXiv:2606.31952v1 | https://arxiv.org/abs/2606.31952v1 | Canonical record and full paper inspected; paper release tag and README inspected at commit `65b2b95d06ca5fdc08895a1eae2c197221ce71f7` | 2026-07-27 | Primary paper and paper-release implementation surface inspected |
| P1 | SeKV DEP-A review | Black-Lake; deposited 2026-07-14 | `DEP-A-20260714-SeKV Resolution` | `Black-Lake/.lake-data/DEP-A/DEP-A-20260714-SeKV Resolution/` | Older full-paper review; used to detect prior DEP Class processing and enumerate supporting items | 2026-07-27 | Inspected |
| P2 | Janus DEP-A review | Black-Lake; deposited 2026-07-16 | `DEP-A-20260716-The Past Is Prologue` | `Black-Lake/.lake-data/DEP-A/DEP-A-20260716-The Past Is Prologue/` | Older full-paper review; used to detect prior DEP Class processing | 2026-07-27 | Inspected |
| X1 | CompressKV Semantic Heads DEP-A review | Black-Lake; deposited 2026-07-14 | `DEP-A-20260714-CompressKV Semantic Heads` | `Black-Lake/.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/` | Randomly selected expansion item; full README and whitepaper review inspected | 2026-07-27 | New supporting thread in this pass |

No paper PDF, TeX archive, repository checkout, model, dataset, benchmark payload, clinical record, or quantum execution trace is deposited with this artifact. Temporary paper copies used for full-text inspection are outside the deposit and are removed after validation.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E0 | S0 | Primary source bundle | Complete README, inventory, synthesis, attribution block, and ten ranked findings | Selection boundary, source inventory, and original relevance framing | High | The bundle summarizes research; it is not independent validation |
| E1 | S1 | Primary paper and official code surface | Hierarchical spans, GPU summaries, CPU low-rank bases, trained zoom-in, five backbones, four long-context benchmarks, GSM8K, runtime table, memory scaling, ablations, and limitations | Recoverable multi-resolution cache can improve the tested memory-quality trade-off | High for reported results | No independent rerun; host-transfer and adversarial activation costs remain workload-dependent |
| E2 | S2 | Primary paper and prior DEP review | Memory Momentum Trigger, hybrid coverage/boundary/fresh evaluation set, six datasets, two backbones, two memory updaters, ablations, costs, and limitations | Candidate memory updates can be gated instead of automatically deployed | High for reported experiments | Prompt-based external memory only; no long-horizon interactive or non-stationary environment |
| E3 | S3 | Primary paper | Behaviorally separable benchmark construction, 1,168 examples, 48 configurations, Wilson intervals, agentic extension, preference-tuning appendix, and limitations | Security metrics can hide task-fidelity loss caused by suppression | High | Fixed probes; binary cost abstraction; benchmark behavior is not a deployment-wide safety guarantee |
| E4 | S4 | Primary technical report and official repository | Four evidence classes and layers, infrastructure rule corpus, MCP/skill auditors, black-box agent testing, jailbreak harness, SkillTrustBench, current repository README | Security assessment should match the evidence type required by each layer | Medium-high | Several scope and uniqueness claims are author comparisons; only the skill scanner has a detailed public benchmark in the paper |
| E5 | S5 | Primary specification analysis | Six governance dimensions, Supported/Partial/Absent criteria, five protocol snapshots, gap matrix, extension analysis, and limitations | Current coordination protocols did not natively encode a complete governance layer at the reviewed snapshot | Medium-high | Time-sensitive June 2026 snapshot; partial classifications are judgment-based; taxonomy reflects a bounded theoretical tradition |
| E6 | S6 | Primary medical-evaluation paper and repository | Atomic Clinical Facts, bidirectional cross-verification, more than 178K verified QA pairs, four reader-study benchmarks, 80-case pairwise study, correlation and ranking tables, repository availability | Atomic, traceable fact checks can align better with expert report-evaluation judgments than holistic metrics in tested settings | Medium-high | LLM evaluator dependence, one radiologist for the pairwise gold standard, inference cost, and incomplete public repository |
| E7 | S7 | Primary medical-VLM paper and repository | Dual-stream GRPO, IoU/format/accuracy rewards, cross-feedback sequencing, 18,222 training instances, seven benchmarks, three model settings, token-retention and timing tables, ablations, and limitations | Grounding-guided token selection can improve tested VQA accuracy while reducing visual-token work | Medium-high | Standard-resolution study; no clinical deployment validation; public repository contains only a minimal placeholder README |
| E8 | S8 | Primary quantum-compilation paper and official code surface | Context-conditioned admission, exact/QCEC verification, safety ablation, 12-circuit and 20-circuit suites, noise-model estimates, verification crossover, and repository reproduction map | Aggressive context-dependent optimization can be guarded by per-instance correctness checks | High for reported software experiments | Workload-dependent gains; estimated rather than hardware-measured infidelity; bounded-approximate branch remains inert |
| E9 | S9 | Primary quantum-programming paper and current framework surface | Permeability theorem, DAG construction, Kahn/Flex-Sort transformations, MaxCut parallelization, complexity discussion, memory-management example, and limitations | Semantic commutation information can guide equivalent circuit reorderings for depth and qubit lifetime | Medium-high | Memory benchmark sets lack deallocation metadata; optimal peak-qubit use is not guaranteed; favorable MaxCut results may not generalize |
| E10 | S10 | Primary theory/algorithm paper and paper-release code | Sparse query model, randomized support discovery, sparse Walsh-Hadamard decoding, theorems, synthetic experiments to n=30, PennyLane crossover, and failure boundaries | Exact Pauli decomposition is polynomial under explicit sparsity and query-access promises | High for stated theorem and inspected experiments | Not generic; memory may remain exponential; incorrect sparsity bounds can escape detection; experiments are synthetic |
| E11 | P1, P2 | Prior Black-Lake DEP-A artifacts | Full-paper reviews, source maps, availability notes, and linked supporting items | Prior-processing detection and expansion-candidate inventory | Medium-high | Prior reviews are derivative evidence and not substitutes for the primary papers |
| E12 | X1 | Randomly selected prior DEP-A artifact | CompressKV method reconstruction, head-selection evidence, equal-budget concerns, irreversible-eviction limits, and direct SeKV comparison | New comparison of irreversible semantic retention and recoverable multi-resolution memory | Medium-high | No new CompressKV experiment was run; this artifact expands the research thread rather than independently reproducing it |
| E13 | Official repositories | Primary implementation surfaces | Immutable README snapshots for SeKV, AI-Infra-Guard, MRGEvalKit, ViToS, TopToffoli, Qrisp, and sparse Pauli decomposition | Public availability and reproducibility boundary | High for observed README state | Repository presence does not establish that code reproduces every paper result |

## Executive Summary

The ten works share a mechanism more precise than “optimization”: each makes a consequential change to memory, behavior, evaluation, governance, or a compiled representation, and the strongest designs ask for evidence before accepting that change. SeKV reconstructs relevant detail instead of permanently evicting every compressed token. Janus tests suspicious memory updates before deployment. SecFid makes both successful defense and fidelity loss observable. AI-Infra-Guard assigns different evidence procedures to different attack-surface layers. The protocol study asks whether governance primitives are encoded rather than merely transportable. AtomiMed decomposes clinical reports into auditable facts. ViToS grounds token pruning in spatial evidence. The Toffoli compiler refuses cheap substitutions until equivalence is certified. Qrisp uses a proved commutation property to justify reordering. The sparse Pauli algorithm succeeds only under explicit access and sparsity promises.

These are not demonstrations of one unified architecture. They come from unrelated tasks, metrics, and assurance regimes. The shared statement is therefore a reviewer interpretation: **resource-saving or capability-enhancing changes should be treated as candidates whose admission depends on evidence appropriate to their failure mode**. Some gates are learned and empirical, some deterministic, some statistical, and some formal. Conflating them would erase the most important distinction in the source set.

Three results make the practical case. First, SeKV reports the best compressed result in all 20 benchmark-model comparisons at a 10% GPU-resident KV budget, a 5.9% average gain over SentenceKV, and GPU memory of 34.9 GB rather than FullKV's 74.8 GB at 128K on the named setup (E1). Second, Janus improves the two tested base memory updaters by 2.7 to 4.6 average points across two backbones, while its own cost sweep shows that more replay is not automatically better (E2). Third, the Toffoli safety ablation finds that ungated substitutions corrupt 6 of 12 circuits, whereas the per-instance verification gate reports 0 errors and retains most of the available two-qubit-gate reduction (E8).

The safety and governance papers show why acceptance metrics must expose costs and evidence classes. SecFid's most secure configurations reach 99.3% security but only 71.0%-73.9% fidelity, while the highest-fidelity model reaches 96.5% fidelity at 47.8% security (E3). AI-Infra-Guard separates signature, semantic, behavioral, and statistical evidence rather than applying one detector everywhere (E4). The protocol paper finds no complete native governance layer in its June 2026 snapshot; that finding must remain version-bound because protocols evolve rapidly (E5).

The medical and quantum works add a second discipline: the evidence gate must match what failure means. AtomiMed's atomic facts support per-finding audit rather than a single opaque score; ViToS's grounding reward ties pruning to a spatially supervised task but does not establish clinical safety. The Toffoli verifier proves equivalence for accepted rewrites; Qrisp proves a commutation condition but uses heuristic topological ordering; sparse Pauli decomposition provides a formal high-probability guarantee only under a declared promise model. “Evidence-gated” therefore does not mean “guaranteed.” It means the system records the candidate, the gate, the evidence class, the fallback, and the residual uncertainty.

New in this pass: the randomly selected CompressKV artifact sharpens the SeKV analysis. CompressKV uses calibrated semantic retrieval heads and irreversible token retention; SeKV keeps summaries and low-rank bases that can be expanded later. The two methods change the failure model, not merely the cache size. No inspected source supplies a head-to-head comparison at equal actual bytes, equal host bandwidth, equal prefill cost, and equal tail latency, so this manuscript treats recoverability as a testable design axis rather than a demonstrated winner.

## Detailed Summary

### Recoverable long-context memory

SeKV segments a prefetched context into entropy-guided semantic spans. Each span retains routing information on GPU and a low-rank basis on CPU. A small trained module selects spans for zoom-in during decoding, reconstructing approximate token-level key/value detail and mixing compressed and expanded entries in one attention distribution. The base language model stays frozen; the added trainable parameters are reported as fewer than 0.05%.

The evaluation covers LongBench, RULER, InfiniteBench, NIAH, and a many-shot GSM8K setting across five backbones. At a 10% GPU-resident KV budget, SeKV is the best compressed method in all 20 benchmark-model cells of the main table. The paper reports an average 5.9% improvement over SentenceKV, with especially strong gains on retrieval-heavy tasks. On Qwen2.5-14B-Instruct, GPU memory grows from 31.2 GB at 8K to 34.9 GB at 128K, while FullKV grows from 36.0 GB to 74.8 GB. Runtime is not uniformly best: StreamingLLM is faster but substantially less accurate, and CPU-resident reconstruction exposes SeKV to host-bandwidth and activation-pattern costs.

The ablations support the claimed mechanism. Removing SVD reconstruction lowers NIAH from 91.17 to 83.47, and removing trained zoom-in lowers it to 85.96. Noisy span boundaries, dense tables, code, unusual formatting, slow transfers, or adversarially broad span activation remain open failure modes. “Recoverable” also needs calibration: low-rank SVD bases approximate the original cache and are not a lossless copy.

### Selective deployment of evolving memory

Janus wraps an existing prompt-based memory updater. After each task, the updater proposes a candidate memory. A Memory Momentum Trigger compares the candidate update direction with recent memory evolution. If the trigger fires, Janus compares old and new memories on a bounded set containing representative coverage tasks, prior boundary cases where memory changed behavior, and fresh tasks since the preceding trigger. It deploys the better-scoring state; otherwise it accepts the candidate directly.

Across MATH500, GPQA Diamond, two MMLU-Pro subsets, APIBench-HF, and HumanEval, the paper evaluates Qwen3-8B and DeepSeek-V4-Flash with DC-RS and ExpeL memory updaters. DC-RS plus Janus moves from 79.5 to 83.2 average on Qwen and from 76.7 to 81.3 on DeepSeek. ExpeL plus Janus moves from 78.3 to 81.5 and from 79.6 to 82.3. Trigger and support-set ablations indicate that the timing and composition of validation matter. The default GPQA setting reports 173 triggers, a 72.4% trigger rate, and an estimated 4,325 evaluation units; larger support sets cost more without improving accuracy in that sweep.

Janus does not reject every untriggered change, prove future utility, or cover learned weight/policy updates. Its validation proxy can itself be stale or noisy, and the authors explicitly leave long-horizon interactive, multi-agent, and non-stationary settings open. The transferable design is an admission controller with a logged fallback, not the claim that one trigger solves memory safety.

### Security measured as both protection and retained utility

SecFid constructs tasks where three behaviors have distinguishable outputs: executing an injected instruction, processing the same span as task data, and suppressing it. Translation and editing make omission visible by requiring preservation of the full input. Extraction and counting make omission visible by placing task-relevant entities inside the untrusted span. Security is one minus execution rate; fidelity is one minus ignored rate; strict safe processing additionally requires processing without execution.

The benchmark contains 1,168 examples and evaluates 48 configurations drawn from 15 base-model settings, reasoning variants, and four defense families. The reported frontier is stark. Llama 3.3 70B reaches 96.5% fidelity but 47.8% security. SECALIGN variants reach 99.3% security with 71.0% or 73.9% fidelity. Wilson intervals and per-configuration paired analyses make the descriptive trade-off more informative than a single attack-success number.

A small appendix experiment trains one SECALIGN 8B starting point with a preference ordering that favors processed over ignored over executed responses. On the held-out edit task, processed responses rise from 43.2% to 80.6%, ignored responses fall from 53.5% to 16.8%, and execution remains below 1%. This is promising but bounded to one starting model, one preference construction, and one held-out transfer task. Fixed probes and a binary process/filter cost abstraction do not cover adaptive attacks or richer actions such as clarification, sandboxing, reduced privilege, or human review.

### Layer-matched security evidence

AI-Infra-Guard organizes the agent attack surface into infrastructure, protocol/tool, runtime behavior, and model layers. Its main theoretical contribution is an evidence ladder: signature evidence for known exposed components, semantic evidence for code and metadata, behavioral evidence for runtime interactions, and statistical evidence for model robustness. The implementation maps these to deterministic rules, LLM-driven MCP and skill auditing, bounded black-box agent red teaming, and large attack-operator evaluation.

At the paper snapshot, the report describes more than 75 AI components, more than 1,400 vulnerability rules, 26 or more attack operators, and sixteen jailbreak datasets containing about 7,248 prompts. SkillTrustBench distills 5,520 cases from 62,652 skills across nine threat categories. With the audit specification held fixed, the reported loose F1 ranges from 0.9566 to 0.9848 across nine base models, and false-positive rate ranges from 0.0120 to 0.1867. This benchmark supports the skill-scanner evaluation, not every module in the framework.

The official repository had evolved by the access date: its README at the verified commit reports release v4.5.0 with 130 components and 1,888 rules. That is a current implementation observation, not a retroactive correction to the paper. The framework also relies on LLM judgments, operator libraries, plugin trust, target authorization, and continuous corpus maintenance. This manuscript does not reproduce attack payloads or provide operational exploitation guidance.

### Coordination protocols versus governance semantics

The governance paper defines six requirements: membership, deliberation, voting, dissent preservation, human escalation, and audit/replay. It classifies MCP v1.1, A2A v1.0.1, ACP, ANP, and ERC-8004 as Supported, Partial, or Absent based on what the specification natively encodes, not what an application can transport in an opaque message.

The gap matrix gives MCP, A2A, ACP, ANP, and ERC-8004 coverage scores of 1/12, 1/12, 2/12, 0/12, and 2/12. Voting, dissent preservation, and human escalation are absent in all five classifications. ACP receives partial deliberation for structured bilateral negotiation, MCP receives partial audit for sessions and structured tool responses, and ERC-8004 receives partial audit for its blockchain history. The authors argue that transport and implementation logs do not provide interoperable governance semantics.

This is a time-bound, interpretive specification analysis. The authors explicitly note rapid protocol evolution, judgment in “Partial” classifications, a taxonomy rooted in Western organizational theory, and a deliberate exclusion of application-layer capabilities. The paper's estimate that extensions could narrow the gap in six to twelve months is a forecast, not measured fact. A durable use of the matrix is as a review checklist with pinned protocol versions.

### Atomic medical-report evaluation

AtomiMed decomposes reference and generated radiology reports into disease-level and attribute-level Atomic Clinical Facts, then performs bidirectional evidence-based question answering. It reports precision, recall, and F1 at both levels and retains the question-level disagreements as an audit trace. OmniMRG-Bench spans X-ray, CT, MRI, and ultrasound, nine anatomical systems, six attribute categories, and more than 178,000 expert-verified QA pairs.

Four radiologist-annotated benchmarks support correlation analysis. The paper reports a Spearman correlation of 0.806 on ReXVal, slightly above GREEN's 0.798. A separate pairwise study samples 20 cases from each of four modalities, compares ten model outputs per case, and uses one board-certified radiologist's rankings as the gold standard. AtomiMed reaches 95.71% pairwise accuracy and Kendall's tau of 0.9807 on X-ray, 84.33% accuracy on CT, 68.19% on MRI, and 49.86% on ultrasound.

Those figures do not make AtomiMed a clinical decision system. They evaluate generated reports against expert judgments. The metric still depends on automated extraction and evidence reading, incurs model-inference cost, and uses one radiologist for the pairwise gold standard. Its official repository advertises installation and evaluation scripts but also says the detailed repository is “coming soon,” limiting independent reconstruction of the full reported pipeline at the inspected commit.

### Grounded visual-token selection

ViToS trains one medical vision-language policy in two sequential branches. A localization branch outputs a bounding box and receives format, IoU, and downstream accuracy signals. A token-sparse branch retains foreground visual tokens, fuses background information into them, and reasons over the resulting sequence. Cross-feedback connects the branches, but gradients are separated: localization is trained first and frozen before sparse reasoning is optimized.

The study uses 18,222 VQA instances with bounding boxes, eight H200 GPUs for eight hours, and seven public medical benchmarks. On Lingshu-7B, combined dual-stream RL and grounded token pruning moves the average from 63.68 to 68.95; on HuatuoGPT-Vision-7B it moves from 56.81 to 59.17; on Lingshu-32B it moves from 66.46 to 70.21. The average token retention is 77%. A timing table reports ViToS completing its inference comparison in 11 minutes for 7B and 53 minutes for 32B, versus 47-54 and 171-202 minutes for the tested pruning baselines under the paper's setup.

The method remains an evaluation study, not clinical validation. It uses standard-resolution images, binary answer rewards, generated/revalidated training data, and model-specific adaptations for some baselines. Pruning-only ablations can fail badly when localization is wrong, especially on multi-region and spatial tasks; token fusion reduces but does not eliminate this dependence. The official repository at the verified commit contains only a title-level placeholder README despite the paper's code-availability statement.

### Correctness-gated quantum optimization

The Toffoli compiler chooses among exact, relative-phase, and approximate decompositions using a two-qubit-infidelity objective. Context-dependent candidates are admitted only when a per-instance equivalence obligation passes. Small windows use exhaustive checking; larger cases use a decision-diagram backend. A failed candidate falls back to the cheapest certified alternative.

The safety ablation is more important than the headline speedup. The authors report 66 non-equivalent standalone rewrites in an audited optimizer library. Both count-greedy substitution and the authors' structural analysis with the verification gate disabled corrupt 6 of 12 circuits. The gated pass reports 0 errors and reduces the primary suite from the exact-only baseline to 170 two-qubit gates and estimated infidelity 1.736, corresponding to 39.5% and 36.7% reductions. On a broader 20-circuit, 12-24-qubit suite, the aggregate two-qubit-gate reduction is 15.6%, demonstrating workload dependence.

The hardware figures are estimates under published error rates, not executions on those devices. The bounded-approximate regime is inert under the current set-based reachability analysis. Exhaustive verification scales exponentially with local window width, and the practical result relies on small local obligations or decision diagrams. The public repository maps scripts to figures and tables, but no reproduction was run in this review.

### Semantic circuit reordering and memory lifetime

Qrisp's permeability DAG encodes when quantum operations commute because they are Z- or X-permeable on their shared qubits. The paper proves the relevant commutativity condition and enriches the graph with allocation, deallocation, and terminator nodes. Different topological sorts then target circuit depth or peak qubit lifetime.

For parallelization, an adapted Kahn algorithm chooses available nodes using dynamic qubit depth and gate timing. A MaxCut example reduces CNOT depth from 10 to 6; across sampled MaxCut circuits, the implementation is reported to improve over the second-best optimizer by about 33% except on the smallest case. The authors warn that MaxCut is especially favorable and broader algorithms may see more moderate gains.

For memory management, Flex-Sort tries to pull deallocations earlier and allocations later. The authors say it found optimal allocations on varied examples but is not always optimal. Standard benchmark suites lack deallocation information, so there is no comparable broad memory benchmark. Worst-case ordering analysis is \(O(|S||D|)\), mitigated in the implementation with parallel kernels. Qrisp is an active framework, but current repository availability is not evidence that this specific paper's every result remains reproduced at the current head.

### Promise-gated Pauli decomposition

The Pauli paper studies a promise problem. A \(2^n \times 2^n\) matrix must have support on \(k=\mathrm{poly}(n)\) Pauli strings and expose sparse row or column queries. The algorithm discovers active Pauli-X parts using random row queries, decodes unique Pauli-Z parts directly, and reduces degenerate slices to sparse Walsh-Hadamard recovery with certification.

Under those assumptions and a known upper bound on \(k\), the paper proves success probability at least \(1-\delta\), query complexity \(O(nk^2\log(k/\delta))\), and runtime \(O(n^2k^2\log(k/\delta))\) under its accounting. Synthetic experiments use five random matrices per \(n\) from 2 to 30 with \(k=2n\). The PennyLane comparison is faster at small \(n\); a crossover appears around \(n=10\), after which the new implementation is faster in the tested range. All reported random trials recovered the decomposition.

The promise is the gate. The method does not make generic dense decomposition efficient, memory can still be exponential, and an underestimated sparsity bound can produce an undetected wrong result. Random global checks can miss an exponentially sparse residual. The paper-release tag and README are public and pinned, but no benchmark was rerun here.

## Key Claims and Evidence

| Claim | Claim type | Evidence | Assessment |
|---|---|---|---|
| SeKV improves over the strongest tested semantic-compression baseline by 5.9% on average at the stated 10% KV budget | Source claim | E1, main benchmark table | Supported within the tested models, tasks, and budget; not a universal serving result |
| SeKV reduces GPU memory by 53.3% versus FullKV at 128K | Source claim | E1, memory-scaling figure and prose | Supported for the named Qwen2.5-14B setup; host memory and transfer costs remain outside the headline |
| Janus improves its two base memory updaters by 2.7-4.6 average points | Source claim | E2, main results | Supported across the six datasets and two backbones tested |
| Security-only prompt-injection evaluation can misclassify suppression as success | Source claim | E3, behaviorally separable construction and frontier | Strongly supported by the benchmark design; deployment cost weights still determine preferred action |
| Different agent layers require different evidence classes | Author framework plus reviewer endorsement | E4 | Coherent and useful; not proven as the only valid decomposition |
| No reviewed protocol natively encodes a complete governance layer | Source claim | E5, June 2026 gap matrix | Supported as a time-bound classification; must be re-audited as specifications change |
| AtomiMed aligns better with radiologist judgments than included metrics | Source claim | E6, correlation and pairwise tables | Supported in the reported studies; repository and expert-study boundaries limit reproduction |
| ViToS improves tested medical VQA averages while retaining 77% of visual tokens | Source claim | E7, main and pruning tables | Supported in the paper's setup; not evidence of clinical safety or deployment benefit |
| Ungated context-dependent Toffoli substitutions can silently corrupt circuits | Source claim | E8, safety ablation | Strongly supported by the reported verification experiment |
| Permeability can justify equivalent circuit reorderings | Source theorem and implementation claim | E9 | The commutation theorem supports correctness of permitted reorderings; heuristic optimization quality is not guaranteed |
| Sparse Pauli decomposition is polynomial under the stated promise model | Source theorem | E10 | Supported by the paper's theorem; invalid outside the explicit sparsity and query-access assumptions |
| Evidence-gated admission is the common design pattern across this source set | Reviewer interpretation | E1-E10 | Plausible synthesis, not a claim made or tested jointly by the authors |
| Recoverability is a distinct cache-design axis from semantic selection | Reviewer interpretation, new this pass | E1, E12 | Supported conceptually by SeKV versus CompressKV; no equal-resource head-to-head experiment was found |

## Methodology

1. **Repository-first boundary.** The live README files of both repositories were read before artifact construction. The selected source DEP's two files and complete attribution block were inspected at an immutable source commit.
2. **Eligibility and prior-artifact check.** Canonical source DEP directories were enumerated. Same-family `.reports`, `.logs`, Report-Marks, and prior markers were checked against the 24-hour cutoff. Exact references to the selected DEP in Black-Lake `.lake-data` identified two older DEP-A artifacts but no recent same-family marker.
3. **Primary-source inspection.** Canonical arXiv records and complete papers were inspected for all ten findings. Paper tables, equations, appendices, limitations, and code-availability statements were used where material to the claims.
4. **Implementation availability check.** Official repositories named by the papers were checked without executing their code. Public README state was inspected at verified commit identifiers. Repository availability is treated as inspectability, not reproduction.
5. **Iterative expansion.** Four accessible supporting items from the prior SeKV review were sorted and hashed. A cryptographic UInt32 draw selected the prior CompressKV DEP-A review. Its README and full manuscript were inspected, and a new recoverability comparison was added.
6. **Claim calibration.** Author claims, reviewer interpretation, and implementation hypotheses are separately labeled. Quantitative claims retain their denominator, model, benchmark, hardware, or promise conditions.
7. **Safety treatment.** Security papers were analyzed defensively. Operational exploit sequences, attack strings, and sensitive payload details were omitted.
8. **Public-output gate.** Generated artifacts are scanned for local paths, user or machine identifiers, local timezone labels, and local execution timestamps before submission. Source provenance is represented with repository-relative paths and immutable public URLs.

This process is a full-paper documentary review, not an experimental replication, code audit, clinical assessment, or formal proof check.

## Scope, Constraints, and Assumptions

- The temporal scope ends on 2026-07-27. Agent protocol and software-repository facts can change after that date.
- All ten canonical arXiv records were v1 at inspection.
- Quantitative results are author-reported unless explicitly labeled as a reviewer calculation.
- The source bundle's local-time strings are historical evidence only and are not republished as automation provenance.
- Clinical papers are evaluated as research on metrics and model behavior. Nothing in this artifact is clinical guidance.
- Quantum error rates and circuit-fidelity reductions are software estimates unless the paper explicitly reports hardware execution.
- “Recoverable” cache data may be approximate and still fail to restore evidence; it is not synonymous with lossless.
- “Verified” refers to the particular equivalence obligation and backend described by the source, not system-wide correctness.
- Public code was not executed, dependencies were not installed, and datasets or checkpoints were not downloaded.
- The cross-domain evidence-gate synthesis assumes that an admission decision, its evidence, and its fallback can be represented explicitly. Some learned systems may not expose those boundaries cleanly.

## Observations

1. **A gate is only meaningful when failure remains observable.** SecFid constructs separate outputs for execution, processing, and suppression. The Toffoli pass checks equivalence rather than assuming a rewrite is safe. Sparse Pauli decoding includes certifications but also documents residuals that random checks can miss.
2. **Resource compression changes the error model.** SeKV moves detail to an approximate recoverable tier; CompressKV irreversibly evicts positions; ViToS prunes and fuses visual tokens; Qrisp reuses execution qubits by changing lifetime order. Equal “retention ratio” does not imply equal recoverability or risk.
3. **More checking is not automatically better.** Janus can outperform always-triggered comparison in a noisy compact-evaluation setting. AI-Infra-Guard argues for the least expensive evidence class sufficient for a layer. Formal verification becomes expensive as obligations widen.
4. **Evidence schemas enable audit.** AtomiMed retains per-finding questions, the governance taxonomy names missing primitives, and the quantum papers make their promise or equivalence conditions explicit. An aggregate score alone cannot explain a rejected change.
5. **Availability claims need independent repository checks.** SeKV and TopToffoli expose substantial public surfaces. MRGEvalKit says details are coming soon, and ViToS exposes only a minimal README at the inspected head. A paper's “code available” statement does not establish a complete reproducibility package.
6. **Version identity is substantive evidence.** AI-Infra-Guard's current repository scope already exceeds its paper snapshot. Protocol governance claims are explicitly version-bound. Durable review should pin both paper and implementation identities.

## Considerations

- A production evidence gate should declare what it can prove, what it merely predicts, and when it falls back.
- Candidate changes should remain reversible until validation completes. When irreversible eviction or execution is unavoidable, the system should record the accepted risk.
- Metric selection must include lost utility, not only prevented failure. SecFid is the clearest example, but the principle also applies to cache quality, clinical false reassurance, and compiler conservatism.
- Learned gates require calibration-shift monitoring. SeKV span routing, Janus triggers, LLM security auditors, AtomiMed fact extraction, and ViToS localization can all drift outside their training or benchmark distributions.
- Formal gates still depend on model boundaries. A proof about a local circuit rewrite does not validate the hardware noise model, compiler pipeline, or application semantics around it.
- High-stakes domains need human authority and preserved dissent. The governance paper's missing primitives are relevant even when the underlying tool or model is technically correct.
- Reproduction should report rejected candidates and fallbacks, not just successful optimized outputs. Negative evidence is essential for evaluating gate selectivity.

## Strengths

- The source set contains several mechanism-level ablations rather than only headline accuracy.
- SeKV, Janus, SecFid, ViToS, and TopToffoli expose meaningful failure or component comparisons.
- The protocol paper and sparse Pauli paper state their classification or promise boundaries directly.
- AtomiMed and SecFid make otherwise hidden error categories observable.
- TopToffoli combines an aggressive optimization objective with an explicit correctness fallback.
- Multiple official repositories provide inspectable implementation or reproduction surfaces.
- The new CompressKV thread creates a concrete, falsifiable comparison axis: semantic selection versus recoverable representation.

## Weaknesses

- No single experiment spans the cross-domain evidence-gate architecture proposed by this review.
- Several results depend on author-designed benchmarks, models, judges, and repositories.
- AI-Infra-Guard's broad cross-layer claims are not backed by one uniform end-to-end benchmark.
- The governance matrix is time-sensitive and partly judgment-based.
- Medical studies do not establish prospective clinical utility, external safety, or workflow impact.
- SeKV's headline GPU savings omit the full CPU-memory and host-transfer accounting needed for deployment comparison.
- Janus validates only triggered updates and assumes a compact task set is a useful proxy for future behavior.
- Qrisp's memory optimization lacks a standard benchmark with deallocation semantics and is not always optimal.
- Sparse Pauli decomposition can retain exponential memory and relies on promises that may be difficult to validate.
- Public availability is uneven: two medical repositories are incomplete at their inspected heads.

## Potential Improvements

1. **Equal-resource cache study.** Compare FullKV, CompressKV, SeKV, eviction, quantization, and offload at equal GPU bytes, total host bytes, prefill latency, mean and p95 decode latency, energy, and task-level/tail quality.
2. **Reversible memory deployment.** Extend Janus-like update control with immutable candidate snapshots, explicit rollback, privacy filters, and non-stationary validation streams.
3. **Utility-aware security policies.** Evaluate clarification, sandboxing, read-only tool modes, provenance stripping, and human escalation alongside process/filter choices.
4. **Versioned governance conformance.** Build a public test suite that maps pinned MCP, A2A, ACP, ANP, and ERC-8004 schemas to machine-checkable G1-G6 criteria and preserves disagreements between reviewers.
5. **Clinical multi-reader replication.** Rebuild AtomiMed's pairwise gold standard with multiple radiologists, inter-rater uncertainty, calibration by modality, and prospective error-impact review.
6. **External medical evaluation.** Test ViToS on extreme-resolution, multi-region, longitudinal, and out-of-distribution studies with localization-failure reporting and no claim of clinical readiness.
7. **Compositional compiler assurance.** Verify how the Toffoli pass composes with routing, scheduling, error mitigation, and device calibration rather than treating the local rewrite in isolation.
8. **Promise diagnostics.** Add falsifiable pre-checks and adversarial residual tests for sparse Pauli inputs, with explicit “promise not established” outcomes.
9. **Artifact completeness labels.** Standardize repository badges for paper code, evaluation scripts, data manifests, checkpoints, licenses, and independently reproduced tables.

## Potential Implementations

### 1. Evidence Gate Ledger

Create a service that receives a candidate state change and a declared evidence contract. Contracts identify the evidence class, validator, budget, fallback, and expiry. A memory update might use replay tests; a repository tool change might use static and behavioral checks; a compiler rewrite might require equivalence. The service writes an append-only decision record containing accepted evidence, rejected candidates, and rollback pointers.

### 2. Recoverable Context Tier

Build a long-context serving prototype with three representations: active exact KV on GPU, compact routing summaries, and recoverable CPU or recomputable spans. Compare it with irreversible semantic eviction under equal total resource budgets. Log every zoom-in, failed retrieval, transfer stall, and evidence-position error.

### 3. Utility-Preserving Security Evaluator

Extend an authorized prompt-injection test harness so that every test labels execution, faithful processing, suppression, refusal, clarification, and sandboxed completion. Policies are scored against deployment-specific loss matrices rather than one global attack-success rate. No exploit payload library is published by the evaluator.

### 4. Governance Envelope

Represent membership, deliberation turns, votes, dissent, escalation, and audit as a versioned envelope above an interoperability transport. Preserve protocol-specific adapters but validate governance events against a common schema. Each decision links to human authority and immutable evidence.

### 5. Verified Optimization Broker

Provide a compiler-agnostic API in which an optimizer proposes a transformation and a verifier returns a typed certificate or rejection. The broker records cost-model assumptions, certificate scope, tool versions, and fallback output. Quantum circuit rewrites are one application; database plans and code transformations are others.

## Three Ways to Exercise This Research

1. **Reproduce one bounded gate.** Select Janus's old-versus-new memory decision or the Toffoli equivalence gate, pin all dependencies, rerun a small public case, and publish accepted, rejected, and fallback outcomes.
2. **Run the recoverability comparison.** Evaluate SeKV and the newly expanded CompressKV thread on a matched long-context slice at equal GPU bytes and total end-to-end latency, reporting task-level and worst-decile failures rather than only an average.
3. **Audit one production decision flow.** Map an authorized agent workflow to signature, semantic, behavioral, statistical, and human evidence; record which gates exist, which are missing, and whether dissent and rollback survive the final action.

## Example MVP Product

**Name:** GateLedger

**User:** A team operating tool-using agents or automated optimization pipelines.

**Problem:** Candidate memory updates, tool actions, configuration changes, and optimized artifacts are often deployed without a durable record of why they were admitted or how to reverse them.

**Core workflow:**

1. A client submits a candidate change, immutable source identity, evidence contract, and rollback pointer.
2. GateLedger routes the candidate to a deterministic, semantic, behavioral, statistical, formal, or human validator.
3. The validator returns evidence, scope, confidence or certificate, and failure reasons.
4. Policy either accepts, rejects, escalates, or deploys in a reduced-privilege sandbox.
5. GateLedger writes an append-only decision record and monitors expiry or distribution shift.

**Minimum data model:** candidate ID; source/version; proposed effect; evidence class; validator/version; evaluation set; result; rejected alternatives; human decision; rollback location; expiry; downstream outcome.

**MVP boundary:** The product does not generate attacks, replace clinical review, certify entire software stacks, or claim formal assurance from statistical tests. It orchestrates existing authorized validators and preserves their scope.

**Success measures:** fraction of actions with complete provenance; rollback success rate; false accept and false reject rates by gate; utility retained after security controls; time to human escalation; expired decisions revalidated; rejected-candidate audit coverage.

**Failure tests:** stale evaluator, missing rollback, validator disagreement, unavailable evidence, out-of-distribution input, incomplete protocol version, unverifiable transformation, and a gate that improves average performance while worsening the worst-decile outcome.

## Related Research and Reading

### New in this pass: CompressKV and recoverability

The randomly selected expansion item is the existing Black-Lake DEP-A review `DEP-A-20260714-CompressKV Semantic Heads`, which analyzes *CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference* (arXiv:2606.24467v1) and its overlapping earlier lineage record arXiv:2508.02401.

CompressKV calibrates semantic retrieval heads offline, uses their attention to choose retained prompt positions, and allocates per-layer token budgets using compression error. Its reviewed evidence supports favorable tested memory-quality trade-offs, but the eviction is irreversible, several efficiency results are graph-only, calibration is answer-span-conditioned, and no formal recovery guarantee exists. SeKV instead retains a routing summary and low-rank basis for every span, then reconstructs selected detail. This changes the tail-failure question from “was the position retained?” to “was the span routed, transferred, and reconstructed well enough?”

No inspected source establishes which method is better under equal total resources. A fair experiment must hold constant GPU bytes, CPU bytes, host bandwidth, prefill cost, decode latency percentiles, model, prompt distribution, and task-level quality. It should include adversarially fragmented documents and repeated activation of distant spans. This comparison is newly added in this pass; it is a reviewer research proposal, not a result reported by either paper.

### Prior same-paper DEP artifacts

- `Black-Lake/.lake-data/DEP-A/DEP-A-20260714-SeKV Resolution/` contains a prior full-paper SeKV review and identified the supporting items used for the expansion draw.
- `Black-Lake/.lake-data/DEP-A/DEP-A-20260716-The Past Is Prologue/` contains a prior full-paper Janus review.
- These prior artifacts are older than the 24-hour cutoff. No associated source `.reports` entry, exact `.logs` entry, or Report-Mark existed for `DEP-20260702-Tech Intel 0103`.

### Adjacent primary and implementation surfaces

- Official SeKV implementation at verified commit `6569d111d3ace5c7c1ad596bf36962a99cd7e94b`: https://github.com/AmirAbaskohi/SeKV/tree/6569d111d3ace5c7c1ad596bf36962a99cd7e94b
- Official AI-Infra-Guard implementation at verified commit `51d0584360aea91ec24eaa996cf02372f54dc185`: https://github.com/Tencent/AI-Infra-Guard/tree/51d0584360aea91ec24eaa996cf02372f54dc185
- Official MRGEvalKit surface at verified commit `3149cbf4ef77ddb3c6cbd3532b73e35280c031b6`: https://github.com/Venn2336/MRGEvalkit/tree/3149cbf4ef77ddb3c6cbd3532b73e35280c031b6
- Official ViToS surface at verified commit `b129fcba9742f947d2f0d3fb3cf906c2916377cd`: https://github.com/JLINEkai/ViToS/tree/b129fcba9742f947d2f0d3fb3cf906c2916377cd
- Official TopToffoli implementation at verified commit `f39807eb9f42feed81fd05744f4cbc983ca4bd83`: https://github.com/barkol/toptoffoli/tree/f39807eb9f42feed81fd05744f4cbc983ca4bd83
- Qrisp framework at verified commit `1c70e7ef7b1f23443a7cb98b1ed5d2e8615a7070`: https://github.com/eclipse-qrisp/Qrisp/tree/1c70e7ef7b1f23443a7cb98b1ed5d2e8615a7070
- Sparse Pauli paper release at verified commit/tag `65b2b95d06ca5fdc08895a1eae2c197221ce71f7`: https://github.com/dspencer2596/sparse-pauli-decomposition/tree/65b2b95d06ca5fdc08895a1eae2c197221ce71f7

## Source References

### Source DEP

- Selected source DEP: https://github.com/Delphoa-Labs/Black-Lake-Data/tree/c6cee063d86e6144c69890ba197f84d5a972c3c6/.lake-data/DEP-20260702-Tech%20Intel%200103
- Source DEP README: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/c6cee063d86e6144c69890ba197f84d5a972c3c6/.lake-data/DEP-20260702-Tech%20Intel%200103/README.md
- Source findings document: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/c6cee063d86e6144c69890ba197f84d5a972c3c6/.lake-data/DEP-20260702-Tech%20Intel%200103/daily_research_findings_2026-07-02_0103.md

### Primary papers

1. Amirhossein Abaskohi, Giuseppe Carenini, Peter West, Yuhang He. *SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference*. arXiv:2606.31145v1. https://arxiv.org/abs/2606.31145v1 ; https://arxiv.org/pdf/2606.31145v1 ; https://doi.org/10.48550/arXiv.2606.31145
2. Zihan Chen, Songwei Dong, Chengshuai Shi, Peng Wang, Song Wang, Cong Shen, Jundong Li. *The Past Is Prologue: A Plug-in Controller for Selective Updates in Sequentially Evolving LLM Memory*. arXiv:2606.31121v1. https://arxiv.org/abs/2606.31121v1 ; https://arxiv.org/pdf/2606.31121v1 ; https://doi.org/10.48550/arXiv.2606.31121
3. Mitchell Hermon, Rahul Gupta, Weitong Ruan, Ekraam Sabir, Haohan Wang. *Security--Fidelity Tradeoffs: The Hidden Cost of Prompt Injection Defense*. arXiv:2606.30783v1; ICML 2026. https://arxiv.org/abs/2606.30783v1 ; https://arxiv.org/pdf/2606.30783v1 ; https://doi.org/10.48550/arXiv.2606.30783
4. Yong Yang, Xing Zheng, Huiyu Wu, Huangsheng Cheng, Xiaorong Shi, Jing Guo, Bo Yang, Yi Zhou, Xiangfan Wu, Zonghao Ying. *Securing the AI Agent: A Unified Framework for Multi-Layer Agent Red Teaming*. arXiv:2606.31227v1. https://arxiv.org/abs/2606.31227v1 ; https://arxiv.org/pdf/2606.31227v1 ; https://doi.org/10.48550/arXiv.2606.31227
5. Richard Kang, Yudho Diponegoro. *Governance Gaps in Agent Interoperability Protocols: What MCP, A2A, and ACP Cannot Express*. arXiv:2606.31498v1. https://arxiv.org/abs/2606.31498v1 ; https://arxiv.org/pdf/2606.31498v1 ; https://doi.org/10.48550/arXiv.2606.31498
6. Yuan Wang, Wanxing Chang, Songtao Jiang, Shujian Gao, Xiaotian Zhang, Ruifeng Yuan, Weiwei Cao, Bowen Shi, Ling Zhang, Zuozhu Liu, Jianpeng Zhang. *AtomiMed: Hierarchical Atomic Fact-Checking for Universal Clinical-Aware Medical Report Evaluation*. arXiv:2606.31292v1. https://arxiv.org/abs/2606.31292v1 ; https://arxiv.org/pdf/2606.31292v1 ; https://doi.org/10.48550/arXiv.2606.31292
7. Kaitao Chen, Weiqian Zhao, Jiamin Wu, Qihao Zheng, Shangquan Sun, Chunfeng Song, Xiaosong Wang, Mu Zhou, Mianxin Liu. *Token-Sparse Medical Multimodal Reasoning via Dual-Stream Reinforcement Learning*. arXiv:2606.31599v1; ICML 2026. https://arxiv.org/abs/2606.31599v1 ; https://arxiv.org/pdf/2606.31599v1 ; https://doi.org/10.48550/arXiv.2606.31599
8. Karol Bartkiewicz, Patrycja Tulewicz. *Context-Verified, Error-Budget-Aware Decomposition Selection for Toffoli Networks*. arXiv:2606.31791v1. https://arxiv.org/abs/2606.31791v1 ; https://arxiv.org/pdf/2606.31791v1 ; https://doi.org/10.48550/arXiv.2606.31791
9. Raphael Seidel. *Automatic quantum function parallelization and memory management in Qrisp*. arXiv:2606.31837v1. https://arxiv.org/abs/2606.31837v1 ; https://arxiv.org/pdf/2606.31837v1 ; https://doi.org/10.48550/arXiv.2606.31837
10. Daniel J. Spencer, Kishor Bharti, Alexey V. Gorshkov. *An efficient Pauli decomposition algorithm for structured matrices*. arXiv:2606.31952v1. https://arxiv.org/abs/2606.31952v1 ; https://arxiv.org/pdf/2606.31952v1 ; https://doi.org/10.48550/arXiv.2606.31952

### Expansion source

- `DEP-A-20260714-CompressKV Semantic Heads`: https://github.com/Delphoa/Black-Lake/tree/1fe5e87c4bd193533edd9bf12d3487b6ad236ead/.lake-data/DEP-A/DEP-A-20260714-CompressKV%20Semantic%20Heads
- CompressKV canonical record: https://arxiv.org/abs/2606.24467v1
- CompressKV PDF: https://arxiv.org/pdf/2606.24467v1
- CompressKV DOI: https://doi.org/10.48550/arXiv.2606.24467
- Earlier overlapping CompressKV lineage record: https://arxiv.org/abs/2508.02401
- Official CompressKV implementation: https://github.com/TUDa-HWAI/CompressKV

## Appendix

### A. Random selection record

- Eligibility cutoff: `2026-07-26T00:03:55Z`
- Canonical candidate count after the final source refresh: 85
- Excluded within the 24-hour window: 1
- Excluded DEP: `DEP-20260706-Tech Intel 1110`
- Recent exact markers: source `.reports`, source Report-Mark, and Black-Lake `.logs`, all carrying run timestamp `2026-07-26T15:07:38Z`
- Eligible count: 84
- Eligible-list SHA-256: `cd93bbf9a9caee9c8a43472564e7026e1d2c767f6c6e7766b85f388f4c83b041`
- Random method: operating-system cryptographic UInt32 with rejection sampling over the sorted eligible list
- Accepted UInt32: `1568308829`
- Successful zero-based index: 17
- Selected DEP: `DEP-20260702-Tech Intel 0103`
- Two earlier selection commands failed before a valid random result was produced: one used an unavailable API and emitted no random bytes; one failed at parse time. They did not constitute draws. The recorded selection is the valid draw performed after the final source refresh.

### B. Expansion selection record

- Prior same-paper DEP Class artifacts: 2
- Exact prior same-family report, log, or Report-Mark for the selected source DEP: none
- Accessible expansion candidates: 4
- Sorted candidate-list SHA-256: `64047e4a3f61b220162ef7137a0854cb9744a527013ee87f796c7e58d3d4cd04`
- Accepted UInt32: `634654884`
- Zero-based index: 0
- Selected supporting item: `Black-Lake/.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/README.md`
- Accessibility result: available; README and companion review inspected

### C. Validation gaps

- No source code was executed and no dependency was installed.
- No model, dataset, benchmark, checkpoint, clinical record, or quantum backend was accessed.
- No paper result, statistical table, formal proof, energy claim, memory profile, or hardware error rate was independently reproduced.
- Full papers were inspected, but the review does not redistribute those files.
- Security material was limited to defensive assessment and governance; operational exploit instructions were excluded.
