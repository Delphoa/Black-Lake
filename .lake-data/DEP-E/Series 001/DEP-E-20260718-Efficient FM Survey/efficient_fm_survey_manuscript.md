---
title: "Efficient FM Survey - DEP-E"
generated_at: "2026-07-18 (date-only public marker)"
artifact_type: "DEP research artifact and survey paper report"
primary_subject: "Source-grounded review of a lifecycle taxonomy for resource-efficient language, vision, diffusion, and multimodal foundation models."
source_status: "verified local source bundle plus public URLs; original source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-18"
temporal_cutoff: "arXiv v2 revised 2024-09-23; public companion and DEP context inspected through 2026-07-18"
primary_url: "https://arxiv.org/abs/2401.08092"
stable_identifier: "arXiv:2401.08092v2; DOI:10.48550/arXiv.2401.08092"
confidence_summary: "High for paper identity, scope, taxonomy, and source transcription; medium for synthesis; low for independent validation of surveyed third-party metrics."
safety_scope: "public scholarly review, bounded ML-systems planning, and non-sensitive synthetic evaluation"
distribution_notes: "Public URLs and repository-relative paths only; PDF, HTML, metadata, source package, caches, extracted source text, and private execution context withheld."
---

# Efficient FM Survey - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Reference | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *A Survey of Resource-efficient LLM and Multimodal Foundation Models* | Primary paper | arXiv metadata, full HTML, and PDF | arXiv:2401.08092v2; DOI:10.48550/arXiv.2401.08092 | https://arxiv.org/abs/2401.08092; https://arxiv.org/html/2401.08092; https://arxiv.org/pdf/2401.08092 | arXiv exposes a license locator; evidence use only; no source document redistributed. | 2026-07-18 | Full text and 65-page PDF inspected |
| S2 | Efficient Foundation Model Survey | Official companion | GitHub README and curated paper/figure list | `UbiquitousLearning/Efficient_Foundation_Model_Survey`, default branch | https://github.com/UbiquitousLearning/Efficient_Foundation_Model_Survey | Official companion context; repository was read, not executed or redistributed. | 2026-07-18 | README inspected |
| S3 | Private arXiv archive paper unit | Selection and source integrity | Local PDF, full-paper HTML, metadata HTML, source package, README, attribution, summary, verification report | arXiv:2401.08092v2 | Location withheld; public locators in S1 | Private local evidence; all original source artifacts withheld. | 2026-07-18 | Repaired from partial to verified complete |
| S4 | KDFlow LLM Distill - DEP-E | Related DEP entry | Markdown manuscript and README | DEP-E-20260712-KDFlow LLM Distill | `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` | Processed Black Lake artifact; primary basis arXiv:2603.01875v2 and official implementation. | 2026-07-18 | Inspected |
| S5 | CompressKV Semantic Heads - DEP-A | Related DEP entry | Markdown whitepaper review and README | DEP-A-20260714-CompressKV Semantic Heads | `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/2606.24467-whitepaper-review.md` | Processed Black Lake artifact; primary basis arXiv:2606.24467v1 and official implementation. | 2026-07-18 | Inspected |
| S6 | llama.cpp Runtime - DEP-E | Related DEP entry | Markdown manuscript and README | DEP-E-20260712-LlamaCpp-Runtime | `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md` | Processed Black Lake artifact; primary basis official llama.cpp release and linked commit. | 2026-07-18 | Inspected |
| S7 | Black Lake repository standards | Repository authority | Live README and `.lake-data` class/index rules | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Process evidence only. | 2026-07-18 | Live files fetched and read |
| S8 | Black-Lake-Data repository standard | Related-repository authority | Live README | Live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Used for related-repository layout and dedup authority, not paper claims. | 2026-07-18 | Live file fetched and read |

Paper metadata:

- `Full title`: A Survey of Resource-efficient LLM and Multimodal Foundation Models.
- `Authors`: Mengwei Xu, Wangsong Yin, Dongqi Cai, Rongjie Yi, Daliang Xu, Qipeng Wang, Bingyang Wu, Yihao Zhao, Chen Yang, Shihe Wang, Qiyang Zhang, Zhenyan Lu, Li Zhang, Shangguang Wang, Yuanchun Li, Yunxin Liu, Xin Jin, and Xuanzhe Liu.
- `Dates`: v1 submitted 2024-01-16; v2 revised 2024-09-23.
- `Subjects`: Machine Learning; Artificial Intelligence; Distributed, Parallel, and Cluster Computing.
- `Paper extent`: 65 pages in the inspected v2 PDF.
- `Stated scope`: Algorithm and system innovations for physical resources such as compute, memory, storage, and bandwidth; hardware design, training data as a resource, and privacy as a resource are excluded from the core review scope.
- `Companion`: The official repository preserves figures and a maintained paper list organized by the survey taxonomy.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 arXiv metadata | Primary metadata | Title, complete authorship, dates, version, DOI, subjects, license/source links. | Stable source identity. | High | Metadata alone does not validate survey claims. |
| E2 | S1 full-paper HTML, Sections 1-6 | Primary full text | Scope, selection rationales, taxonomy, mechanisms, reported examples, conclusions, and future directions. | Central paper reconstruction. | High for transcription | Most quantitative claims summarize other works and were not traced to every cited primary paper. |
| E3 | S1 PDF | Primary rendered paper | Page count, organization figure, section hierarchy, tables/figures, and text-layer consistency. | Layout and structure cross-check. | High for observed layout/text | Several visual screenshot requests failed; no chart was digitized. |
| E4 | S2 official companion | Near-primary repository | Scope statement, taxonomy-aligned paper list, figures, and active-maintenance claim. | Companion availability and taxonomy persistence. | High | A curated list is not a systematic-search ledger or benchmark. |
| E5 | S4 | Related DEP and primary-source synthesis | Teacher/student workload asymmetry, hidden-state transfer, Ray/SGLang/FSDP2 design, author-reported speed and quality evidence, limitations. | Distillation bridge. | Medium-high | KDFlow experiments were not rerun. |
| E6 | S5 | Related DEP and primary-source synthesis | Semantic retrieval-head cache control, error-aware layer allocation, LongBench/NIAH evidence, systems and recoverability limits. | KV-cache bridge. | Medium-high | CompressKV experiments were not rerun; overlapping paper lineage is not independent corroboration. |
| E7 | S6 | Related DEP and official release evidence | Cross-platform runtime inventory and a quantization correction for an MoE-with-MTP boundary. | Deployment/runtime bridge. | High for release/commit facts | Assets were not built or tested; no performance claim is supported. |
| E8 | S3, S7, S8, public dedup pointer, automation memory | Process and private verification | Random selection, dedup pass, source repair, integrity metrics, publication/index rules, source-withholding rule. | Methodological and repository compliance. | High | Private paths and exact execution details intentionally withheld. |

## Executive Summary

The reviewed work is a broad lifecycle survey of resource-efficient foundation models. Its central organizing contribution is to separate interventions at three levels. Architecture changes alter the model's compute graph, for example through efficient attention, dynamic execution, diffusion-specific designs, or vision-transformer variants. Algorithm changes intervene during pre-training, fine-tuning, inference, or model compression. System changes govern distributed training, federated execution, cloud serving, and edge deployment. This separation gives researchers and engineers a shared map for techniques that otherwise use incompatible metrics and assumptions.

The paper's evidence is strongest as taxonomy and technical synthesis, not as a new empirical result. It compiles mechanisms, source-reported measurements, tables, and figures across many works, but does not normalize them under one hardware/workload envelope or provide a formal systematic-review protocol. The authors state that they prioritize top-tier CS conferences, manually include selected high-impact arXiv work, and focus mainly on post-2020 literature. They exclude hardware design and narrow the resource definition to physical quantities such as compute, memory, storage, and bandwidth. These choices make the artifact tractable but leave important boundaries around data efficiency, privacy, governance, and rapid post-2024 changes.

The three related DEP entries turn the survey into an end-to-end implementation story. KDFlow specializes the teacher-inference and student-training workloads and reduces cross-process transfer. CompressKV uses functionally selected attention heads and layer sensitivity to control which context remains in the KV cache. llama.cpp Runtime exposes the final compatibility layer where quantization, kernels, release packaging, and platform differences determine whether an optimization can be used. Reviewer interpretation: the practical unit of efficiency is therefore a versioned resource contract spanning model, state, runtime, workload, and hardware—not a technique name or isolated speedup.

Confidence is high for paper identity, scope, taxonomy, and accurate reconstruction of inspected text. Confidence is medium for the cross-DEP synthesis because it combines separate systems not evaluated together. Confidence is low for independent validity of third-party metrics reported in the survey; those experiments were not reproduced and most cited primary papers were not individually re-audited in this run.

## Detailed Summary

### Problem Context

Foundation models unify many tasks and modalities, but scale shifts the engineering bottleneck from model accuracy alone to resource acquisition and management. Training requires accelerator time, memory, communication, checkpoints, and energy. Autoregressive inference adds a growing KV cache, sequential decoding, request scheduling, and latency constraints. Multimodal systems introduce modality encoders, high-resolution inputs, and larger activation footprints. Edge deployment adds hard memory, I/O, power, and privacy boundaries.

The survey treats resource efficiency as an interdisciplinary problem across machine learning, language/vision/speech, networking, cloud systems, and edge computing. That stance matters because an algorithmic saving can move work elsewhere. Quantization may reduce parameter memory but add dequantization kernels or compatibility risk. Offloading may fit a model but increase I/O and latency. Sparse execution may save FLOPs while introducing routing and load-balancing costs. A useful survey must therefore organize both algorithms and systems.

### Scope and Review Boundary

The authors define four important boundaries. First, algorithm and system innovations are in scope, while hardware design is excluded. Second, “resource” is limited mainly to physical compute, memory, storage, and bandwidth; training data and privacy are excluded as resource categories. Third, the paper favors work from top-tier CS conferences and manually chosen arXiv papers. Fourth, it focuses mainly on post-2020 literature because the field changes quickly.

These boundaries are transparent but not neutral. Venue preference can underrepresent industrial reports, negative results, non-CS venues, and efficient methods from smaller research communities. Manual arXiv selection adds expert judgment without a reproducible screening record. Excluding privacy as a resource makes the taxonomy cleaner, yet the conclusion later identifies practical privacy-preserving foundation models as a major future direction. The survey is therefore best read as an expert technical map, not an exhaustive or statistically controlled evidence review.

### Foundation-Model Baseline

Before presenting efficiency methods, the paper reviews language, vision, diffusion, and multimodal foundation-model pipelines. For language models, token embeddings, attention, feed-forward blocks, encoder/decoder variants, autoregressive decoding, and the KV cache create the baseline cost structure. For vision transformers, image patches become tokens and attention cost grows with token count. Diffusion models repeat denoising steps, and multimodal models combine encoders or align representations across modalities.

The baseline makes resource accounting modality-dependent. A long-context LLM may be memory-bound on KV state; a diffusion model may be dominated by repeated sampling; a ViT may be dominated by high-resolution token counts; a multimodal model may carry both modality-specific encoders and a large language backbone. The survey's categories are shared, but the operational bottleneck is workload-specific.

### Resource-Efficient Architectures

The architecture layer contains four branches. Efficient attention includes sparse patterns, approximation, and attention-free alternatives that seek lower time or memory complexity. Dynamic neural networks include mixture-of-experts routing and early exit, spending computation conditionally. Diffusion-specific optimization reduces sampling cost, moves generation into latent space, or changes network structure. ViT-specific designs alter tokens, attention, convolutional structure, or mobile-oriented blocks.

The common mechanism is selective computation: change the graph so every input does not exercise every component at full precision and full length. The risk is that theoretical complexity and realized latency diverge. Sparse or approximate operations need supported kernels; dynamic routing needs balanced expert placement; early exits require calibrated confidence; architecture changes often require retraining. Architecture-level claims therefore need compiler, kernel, and workload evidence in addition to FLOP counts.

### Resource-Efficient Algorithms

The algorithm layer follows the model lifecycle. Pre-training methods reduce data, search architectures, use progressive curricula, or adopt lower precision. Fine-tuning methods add small trainable modules, select a subset of parameters, or reparameterize updates through low-rank adapters. Inference methods accelerate decoding, compress/filter inputs, manage the KV cache, or extend context with recurrence/windowing. Model compression includes pruning, knowledge distillation, quantization, and low-rank decomposition.

This layer includes several important transfer choices. Distillation transfers behavior from a larger teacher into a smaller student. Pruning decides which parameters, heads, layers, tokens, or activations are dispensable. Quantization changes representation precision for weights, activations, and sometimes cached states. Low-rank methods factorize matrices or constrain updates. Prompt and context compression alter the input representation; speculative decoding changes the generation schedule; KV-cache policies change retained history.

The survey reports many technique-specific gains, but cross-paper comparison is fragile. “Compression ratio” may refer to parameters, bits, tokens, activations, or cache positions. “Speedup” may refer to kernel time, iteration time, tokens per second, or end-to-end latency. Quality may be measured on different tasks, prompts, or judges. Reviewer interpretation: every result needs its denominator and operational envelope before it can be composed with another result.

### Resource-Efficient Systems

The system layer covers distributed training, federated learning, cloud serving, and edge serving. Distributed-training work manages parallelism, communication, checkpointing, heterogeneous devices, storage, failures, and mixture-of-experts placement. Federated work reduces communication or local training cost and introduces parameter-efficient or gradient-free methods for resource-constrained clients.

Cloud serving must handle autoregressive prefill/decode phases, variable request lengths, batching, scheduling, parallelism, offloading, and memory management. The paper highlights KV caching as both a computation saving and a large memory consumer. It groups serving optimizations into computation, memory, and emerging platform categories. Edge serving adds cloud-edge collaboration, expert/parameter loading, memory walls, I/O optimization, mobile kernels, and the possibility of an LLM exposed as an operating-system service.

System techniques often move rather than remove cost. Offloading trades accelerator memory for host memory, storage, and transfer. Batching trades latency against throughput. Unified paging reduces fragmentation but adds memory-management machinery. Edge-cloud collaboration may lower device compute while adding network dependence and privacy exposure. A system-level evaluation must track transferred resources rather than reporting only the relieved bottleneck.

### Future Directions

The paper identifies six forward directions: cloud-edge hybrid deployment; exploitation of model and activation sparsity; foundation models as a service; agents as holistic systems to optimize; practical privacy-preserving foundation models; and deeper understanding of scaling laws. These directions extend the taxonomy from individual models toward shared services and multi-model workflows.

The agent direction is especially relevant to downstream Black Lake work. An agent can call several models, retrieval systems, tools, and memory stores. Optimizing a standalone model may not optimize the workflow if coordination, repeated context, tool latency, or failure recovery dominates. The survey's lifecycle map therefore needs an orchestration layer for current agentic systems, even if that layer was only emerging at the paper's cutoff.

### Three-DEP Synthesis

KDFlow instantiates algorithm/system co-design. It recognizes that teacher inference and student training have different workloads, uses specialized engines, and transfers a compact representation instead of full logits. In the survey taxonomy, it spans knowledge distillation, distributed execution, communication, and serving-oriented inference engines.

CompressKV instantiates inference-memory control. It selects a small set of semantic retrieval heads offline, uses them to score prompt tokens, and allocates cache budgets to layers based on compression error. In the taxonomy, it spans input/KV compression, attention specialization, memory management, and long-context serving. Its irreversible eviction boundary also exposes a dimension the survey treats lightly: recovery after a resource-saving decision is wrong.

llama.cpp Runtime instantiates deployment reality. A release can publish many platform builds and carry a narrow quantization correction, yet package availability is not performance or correctness evidence. In the taxonomy, it spans quantization, edge/local serving, kernels, platform packaging, and compatibility. It reminds reviewers that efficient models and cache policies are only useful when the runtime implements them correctly for the target model and hardware.

Together, the entries form a pipeline: transfer knowledge into a smaller or more suitable model; control the retained inference state; execute through a pinned runtime. The pipeline should be accepted only when end-to-end quality, latency, memory, energy or cost proxy, compatibility, recoverability, and provenance pass jointly.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Resource-efficient foundation-model work can be organized across architectures, algorithms, and systems. | Author conceptual claim | E2, E3, E4 | The taxonomy is explicit, internally consistent, and useful for lifecycle review. | High |
| C2 | Architecture-level work includes efficient attention, dynamic networks, diffusion-specific optimization, and ViT-specific designs. | Author taxonomy claim | E2, E3 | Directly supported by Sections 3 and the organization figures. | High |
| C3 | Algorithm-level work spans pre-training, fine-tuning, inference, and compression; compression includes pruning, distillation, quantization, and low-rank decomposition. | Author taxonomy claim | E2, E3 | Directly supported by Section 4. | High |
| C4 | System-level efficiency spans distributed training, federated learning, cloud serving, and edge serving. | Author taxonomy claim | E2, E3 | Directly supported by Section 5. | High |
| C5 | Source-reported technique gains demonstrate a broad opportunity for resource savings. | Author synthesis claim | E2 | Plausible as a field summary, but metrics are heterogeneous and were not independently reproduced. | Medium for direction; low for portable magnitude |
| C6 | The survey's six future directions identify important unresolved system questions. | Author outlook | E2 | Useful agenda, not empirical validation. | Medium-high |
| C7 | KDFlow, CompressKV, and llama.cpp Runtime form an actionable distill-state-runtime bridge. | Reviewer interpretation | E5-E7 | Conceptually coherent; the combined stack has not been tested. | Medium |
| C8 | A versioned resource contract is a better implementation unit than a technique label. | Derived reviewer inference | E2, E5-E7 | Supported by differing denominators, boundaries, and runtime dependencies across sources. | Medium |
| C9 | The paper was eligible on the first random draw and had complete source evidence before synthesis. | Process claim | E8 | Dedup found no same-paper artifact; repair produced a verified complete local bundle. | High |

## Methodology

- `Research objective`: Randomly select one unused local arXiv paper, enforce a full-source integrity gate, review it source-first, connect it to exactly three concrete DEP entries, and produce a public-safe DEP-E manuscript.
- `Sources inspected`: Local archive README, PDF, repaired full-paper HTML, metadata HTML, source package inventory, attribution/summary/verification records; canonical arXiv metadata/HTML/PDF; official companion GitHub README; live Black Lake and Black-Lake-Data READMEs; Black Lake `.lake-data/README.md`; public dedup pointer; automation memory; and the README plus substantive artifact for each of the three related DEPs.
- `Discovery strategy`: Used `rg --files -g "*.pdf"` over the archive, treated each unique PDF parent as one paper unit, selected a uniform zero-based index with PowerShell `Get-Random`, derived the arXiv ID from the filename/README, and searched repositories plus memory by arXiv ID, DOI, normalized title, and slug.
- `Inclusion criteria`: Evidence had to identify the paper, expose full methods/taxonomy/conclusions, define repository rules, validate local source completeness, or provide concrete overlap in distillation, KV-cache control, or runtime deployment.
- `Exclusion criteria`: Excluded duplicate/same-paper artifacts, abstract-only evidence, incomplete or invalid paper documents, unrelated DEP entries, unverified quantitative generalization, private path disclosure, and source-file redistribution.
- `Analytical approach`: Conceptual, comparative, implementation, empirical-evidence critique, product research, replication planning, and provenance review.
- `Evidence handling`: Major claims map to evidence IDs. Paper claims, companion-repository observations, related-DEP findings, and reviewer inference are labeled separately. Source-reported metrics are not converted into reproduced results.
- `Uncertainty handling`: Search-protocol gaps, metric heterogeneity, temporal staleness, missing common benchmarks, non-reproduction, and combined-stack uncertainty remain explicit.
- `Extraction process`: The complete HTML supplied searchable full text; the 65-page PDF text layer and organization pages cross-checked structure. Local source integrity was verified before review. Several remote PDF screenshot requests failed, so no chart values were visually digitized.
- `Version control`: Paper pinned to arXiv:2401.08092v2. Official companion context was read from the current default branch and treated as maintained context, not as a version-pinned experiment.
- `Random selection`: 75,777 PDF candidates collapsed to 75,776 unique parent-directory paper units; uniform zero-based selected index 52,398.
- `Deduplication`: Scanned Black Lake `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, and live Black-Lake-Data context. Excluded count 0; duplicate/reselection count 0.
- `24-hour validation`: No same-paper ID, DOI, normalized title, archive-unit, or slug marker was found for the public-safe cutoff date 2026-07-17.
- `Source repair`: Initial state was `partial` because full-paper HTML was missing. The existing PDF was preserved after size/header/EOF validation; official full-paper HTML, metadata HTML, and source package were collected locally with bounded attempts. Final source state was `complete` with zero partials.
- `Reviewer stance`: Schema-complete DEP preservation, skeptical survey review, cross-layer systems synthesis, and bounded product/evaluation translation.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv v2 identity, stated literature-selection boundary, architecture/algorithm/system taxonomy, representative mechanisms, future directions, evidence limits, and synthesis with exactly three related DEP entries.
- `Temporal boundary`: Paper v2 revised 2024-09-23; official companion and repository context inspected through 2026-07-18.
- `Evidence limits`: Most cited papers, codebases, datasets, systems, and measurements were not individually re-audited. No experiment, model, benchmark, runtime asset, or related-DEP code was executed.
- `Assumptions`: Canonical arXiv HTML/PDF and official GitHub companion are authentic primary/near-primary sources; related DEP manuscripts accurately preserve their cited primary evidence subject to their stated limitations.
- `Constraints`: No local absolute path, username, machine identifier, local timezone, exact local execution timestamp, credential, source document, cache, or extracted source text may appear in public output.
- `Out of scope`: Updating the survey's bibliography through 2026, reproducing every quantitative claim, ranking all methods, certifying environmental benefit, validating privacy/legal compliance, or recommending production deployment.
- `Intended use`: Research review, DEP deposition, design-space mapping, evaluation planning, systems architecture review, and safe MVP ideation.
- `Audience`: ML researchers, model-compression engineers, inference/runtime teams, distributed-systems engineers, and Black Lake reviewers.
- `Depth target`: Full manuscript with claim/evidence separation and actionable cross-DEP synthesis.
- `Reproducibility boundary`: A follow-on reviewer can reconstruct the selection and source state from public markers and can use the manuscript to plan experiments, but cannot reproduce the survey's cited metrics from this DEP alone.
- `Operational boundary`: Implementation examples are synthetic, advisory, local/authorized, and approval-gated before costly model or hardware work.
- `Data sensitivity`: Public research metadata plus private local source artifacts; public output contains no private source location.

## Observations

- `Observed pattern`: The survey's three layers repeatedly exchange costs. Architecture changes need kernels; compression changes runtime representations; system offloading shifts memory pressure into communication or storage.
- `Taxonomy observation`: The map is strongest when categories are treated as intervention points rather than mutually exclusive method labels. A single technique can span several layers.
- `Evidence-quality observation`: Breadth is high, but common denominators are weak. Source-reported speedups and compression ratios cannot be compared safely without workload, hardware, quality, and measurement envelopes.
- `Temporal observation`: The official companion can keep the paper list alive, but a maintained list does not automatically revise the manuscript's synthesis, evidence quality, or taxonomy.
- `Cross-DEP observation`: KDFlow, CompressKV, and llama.cpp all specialize resources by role—workload role, attention/layer role, or platform/runtime role.
- `Risk observation`: Irreversible decisions are underrepresented in efficiency reporting. Evicted context, quantized behavior, and distilled capabilities need recovery or rollback evidence.
- `Open question`: Can a shared resource contract support comparable evaluations across training, inference state, and runtime without collapsing different objectives into one score?

## Considerations

Efficiency should be reported as a vector. At minimum, the vector should include task quality, latency distribution, throughput, peak and steady-state memory, transferred bytes, energy or a clearly labeled proxy, monetary cost, and failure/recovery behavior. The workload and hardware envelope must be versioned beside it. A single average hides whether a method moves cost from prefill to decode, GPU to CPU, memory to storage, or model quality to rare inputs.

Composition requires new tests. KDFlow can produce a smaller student, but the student may still have long-context cache pressure. CompressKV can reduce cache state, but the retained-evidence policy may interact with the student's learned attention. llama.cpp can run quantized models locally, but its kernels and formats may not implement the same cache controller or precision assumptions. The combined pipeline therefore needs factorial ablations and end-to-end tests, not multiplication of separate headline speedups.

Governance remains material. Dataset/model licenses, provenance, benchmark contamination, user-data privacy, secret-safe telemetry, release rollback, and dependency security can dominate adoption. The survey's physical-resource focus is defensible, but a product team should not treat privacy and governance as external to resource decisions. Local/edge execution can improve data locality while shifting patching, access control, and compatibility responsibility to the operator.

## Strengths

- Provides a clear lifecycle taxonomy spanning models, algorithms, and systems rather than equating efficiency with compression alone.
- Covers language, vision, diffusion, and multimodal foundation models in one conceptual frame.
- Defines scope and exclusions explicitly, including physical-resource focus and post-2020 emphasis.
- Connects algorithm mechanisms to distributed, cloud, and edge system concerns.
- Treats training, fine-tuning, inference, and deployment as one resource lifecycle.
- Preserves an official open companion repository with figures and a taxonomy-aligned paper list.
- Identifies forward directions that remain relevant to service and agent architectures.

## Weaknesses

- Does not present a reproducible systematic-review protocol, query set, screening ledger, or risk-of-bias assessment.
- Heterogeneous metrics and hardware/workload envelopes limit quantitative comparison across surveyed works.
- Source-reported claims are summarized at scale without independent reproduction or uniform evidence grading.
- Venue and manual-arXiv selection can introduce coverage and prestige bias.
- Core scope excludes hardware, training data, and privacy as resources, leaving cross-layer trade-offs incomplete.
- The September 2024 manuscript cutoff is stale for a fast-moving field; companion-list maintenance does not revise the paper's analysis automatically.
- Recovery, rollback, negative results, tail behavior, and operational failure cost receive less emphasis than positive resource savings.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish a versioned search and screening protocol | Review methodology | Manual selection is not reproducible. | Auditable coverage and update deltas. | Maintenance and review effort. | Re-run queries, publish inclusion/exclusion decisions, and measure inter-reviewer agreement. |
| Normalize result envelopes | Comparative evidence | Speedup and compression metrics use incompatible denominators. | Safer cross-paper comparison. | Primary papers may omit required fields. | Require model, workload, hardware, precision, baseline, quality, and measurement metadata for each row. |
| Add evidence-quality grades | Claims map | Breadth can hide weak or secondary support. | Readers can separate taxonomy from validated findings. | Judgment and calibration burden. | Dual-review a sample and disclose disagreements. |
| Add recovery and failure dimensions | Operational safety | Irreversible savings can create silent correctness loss. | Better production relevance. | New benchmarks and storage/runtime work. | Inject cache, quantization, scheduler, and checkpoint faults; measure recovery and quality. |
| Make agent orchestration first-class | Taxonomy update | Current agents coordinate multiple models, tools, memories, and services. | Captures workflow-level efficiency. | Category overlap. | Benchmark end-to-end agent tasks with per-component and orchestration telemetry. |
| Create living manuscript releases | Temporal maintenance | A paper list alone does not update synthesis. | Versioned current evidence map. | Editorial overhead. | Publish dated releases with added/removed claims and changed conclusions. |

## Potential Implementations

1. `Resource Contract Registry`
   - `User`: ML-systems reviewer and platform engineer.
   - `Goal`: Make efficiency claims comparable and auditable.
   - `Core mechanism`: Store a versioned tuple of model, adaptation, cache policy, runtime, workload, hardware, metric vector, and evidence level.
   - `Required inputs`: Public paper metadata, pinned configs, test records, and explicit budgets.
   - `Outputs`: Evidence matrix, comparison eligibility, Pareto frontier, and missing-field warnings.
   - `Risk controls`: No automatic production recommendation, provenance links, immutable raw results, and refusal on incompatible envelopes.
   - `Evaluation`: Reproduce comparison decisions from a frozen export and catch intentionally mismatched baselines.
2. `Adaptive Local Serving Planner`
   - `User`: Engineer deploying an authorized local foundation model.
   - `Goal`: Select student model, cache policy, quantization, and runtime build under resource constraints.
   - `Core mechanism`: Filter only verified combinations, estimate budgets, run a bounded synthetic smoke test, and report evidence gaps.
   - `Required inputs`: Approved models, platform inventory, memory/latency/quality limits, runtime manifest, and synthetic prompts.
   - `Outputs`: Candidate plan, verification matrix, risk register, and stop conditions.
   - `Risk controls`: No model/source download without approval, hard disk/compute budgets, checksum/version pins, and human release decision.
   - `Evaluation`: Prediction error versus controlled tests and false-confidence rate on unsupported combinations.
3. `Recoverable Context Service`
   - `User`: Long-context inference team.
   - `Goal`: Reduce hot KV memory without irreversible evidence loss.
   - `Core mechanism`: Use semantic relevance and layer sensitivity for hot-cache selection while preserving cold-tier provenance or recomputation pointers.
   - `Required inputs`: Model-specific calibration, prompt provenance, cache telemetry, confidence signals, and bounded cold storage.
   - `Outputs`: Hot cache, cold index, page-in events, quality/recovery telemetry, and audit trace.
   - `Risk controls`: Sensitive-data retention policy, encryption, bounded storage, deletion controls, and fallback to full context on low confidence.
   - `Evaluation`: Long-context quality, memory, p95 latency, page-in precision, and recovery after injected bad evictions.

## Three Ways to Exercise This Research

1. `Taxonomy-to-evidence audit`: Objective - test whether the survey map supports comparable claims; inputs - ten primary papers sampled across architecture, algorithm, and system categories; method - record model/workload/hardware/quality/resource denominators and evidence level; output - a gap matrix; success - every claim has a reproducible envelope or a visible missing-field status; stop - if primary records are inaccessible or license conditions are unclear.
2. `Synthetic cross-layer benchmark`: Objective - test composition without costly or restricted data; inputs - a small licensed teacher/student pair, synthetic prompts, a bounded cache controller, and a pinned local runtime; method - compare baseline, distillation-only, cache-only, runtime-only, and combined variants under fixed seeds; output - metric vectors and Pareto frontier; success - combined gains remain after quality and recovery gates; stop - on budget breach, numerical divergence, or unsupported runtime behavior.
3. `Failure-and-recovery drill`: Objective - make operational cost visible; inputs - synthetic long contexts and controlled fault injections; method - trigger bad eviction, quantization mismatch, runtime incompatibility, and interrupted execution; output - detection time, rollback/recovery outcome, quality loss, and resource overhead; success - every failure is detected and leaves an auditable terminal state; stop - if any test touches unapproved data, models, or production infrastructure.

## Example MVP Product

- `Product name`: FM Efficiency Evidence Board
- `Target user`: Research engineer or architecture review group comparing foundation-model efficiency options.
- `Problem`: Papers and releases report incompatible resource metrics, making apparent gains difficult to compose or validate.
- `Core workflow`: Import public claims and pinned local test records; require a complete resource contract; compare only compatible envelopes; display Pareto frontiers and evidence gaps; export a signed review artifact.
- `Data requirements`: Public paper/repository metadata, synthetic or authorized benchmark records, hardware/runtime manifests, and aggregate non-sensitive telemetry.
- `Architecture`: Local-first web or CLI application with a schema validator, immutable result store, comparison engine, provenance resolver, and read-only report renderer.
- `Success metrics`: Percentage of claims with complete envelopes; incompatible comparisons blocked; reproduction decisions matched by a second reviewer; time to identify the dominant bottleneck; zero private-path or raw-sensitive-data leaks.
- `Risk controls`: URL and checksum validation, least-privilege storage, public/private field separation, budget ceilings, no automatic downloads or deployment, and human approval for expensive tests.
- `Limitations`: Does not prove paper results, cannot normalize missing metrics, and may understate workload-specific effects not represented in the schema.
- `MVP boundary`: One paper at a time, three related implementations, synthetic benchmark records, and local-only use; no model hosting, training, or production scheduler.
- `Deployment model`: Local CLI plus static HTML/Markdown report export.
- `Evaluation plan`: Schema unit tests, mismatched-envelope regression cases, synthetic Pareto examples, redaction tests, and two-reviewer usability study.
- `Failure modes`: False comparability from missing metadata, stale runtime records, proxy metrics mistaken for direct energy, and incorrect provenance links.
- `Maintenance plan`: Versioned schemas, quarterly taxonomy review, dependency monitoring, and explicit migration notes when metrics or categories change.

## Related Research and Reading

### Related DEP Entries

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| KDFlow LLM Distill | Black Lake DEP-E manuscript | Instantiates knowledge distillation and distributed workload specialization, including teacher/student engine separation and communication reduction. | `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md`; arXiv:2603.01875v2 |
| CompressKV Semantic Heads | Black Lake DEP-A whitepaper review | Instantiates inference/KV-cache compression, semantic token retention, layer budgets, and recoverability limits. | `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/2606.24467-whitepaper-review.md`; arXiv:2606.24467v1 |
| llama.cpp Runtime | Black Lake DEP-E manuscript | Instantiates quantization/runtime packaging, platform compatibility, and the evidence gap between release inventory and validated execution. | `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md`; llama.cpp b9789 |

### Primary Companion Reading

- `Official survey companion`: https://github.com/UbiquitousLearning/Efficient_Foundation_Model_Survey — taxonomy-aligned paper and figure list maintained by the paper authors.
- `Canonical paper`: https://arxiv.org/abs/2401.08092 — stable metadata, complete authorship, version history, DOI, and full-text links.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2401.08092 | Paper identity, authors, dates, subjects, abstract, DOI, and source links. | 2026-07-18 | Canonical metadata; arXiv v2. |
| R2 | https://arxiv.org/html/2401.08092 | Full-text scope, taxonomy, mechanism summaries, conclusions, and future directions. | 2026-07-18 | Complete paper HTML, not abstract-only. |
| R3 | https://arxiv.org/pdf/2401.08092 | Rendered 65-page paper, figures/tables, and layout cross-check. | 2026-07-18 | Local verified copy withheld. |
| R4 | https://doi.org/10.48550/arXiv.2401.08092 | Persistent paper identity. | 2026-07-18 | arXiv-issued DOI. |
| R5 | https://github.com/UbiquitousLearning/Efficient_Foundation_Model_Survey | Official companion paper/figure list and scope statement. | 2026-07-18 | README inspected; code not executed. |
| R6 | `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/README.md` | Related DEP inventory and source attribution. | 2026-07-18 | Repository-relative processed artifact. |
| R7 | `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` | Distillation mechanism, results boundary, and system bridge. | 2026-07-18 | Primary basis https://arxiv.org/abs/2603.01875 and https://github.com/songmzhang/KDFlow. |
| R8 | `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/README.md` | Related DEP identity, overlap qualification, and source attribution. | 2026-07-18 | Repository-relative processed artifact. |
| R9 | `.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/2606.24467-whitepaper-review.md` | Semantic cache controller, reported evidence, and recovery boundary. | 2026-07-18 | Primary basis https://arxiv.org/abs/2606.24467 and https://github.com/TUDa-HWAI/CompressKV. |
| R10 | `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/README.md` | Related DEP inventory and source attribution. | 2026-07-18 | Repository-relative processed artifact. |
| R11 | `.lake-data/DEP-E/DEP-E-20260712-LlamaCpp-Runtime/llama-cpp-runtime.md` | Runtime release, quantization correction, and validation boundary. | 2026-07-18 | Primary basis https://github.com/ggml-org/llama.cpp/releases/tag/b9789 and linked commit. |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository paths, source-withholding, naming, attribution, log, and commit rules. | 2026-07-18 | Live default branch. |
| R13 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E class path and publication-index workflow. | 2026-07-18 | Live default branch. |
| R14 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository authority and dedup context. | 2026-07-18 | Live default branch. |
| R15 | Private archive source bundle | Random selection, source repair, integrity, and full-text review. | 2026-07-18 | Location withheld; no original source uploaded. |

## Appendix

### Random Selection and Eligibility Record

- Enumeration command family: `rg --files -g "*.pdf"`.
- PDF candidate count: 75,777.
- Unique parent-directory paper units: 75,776.
- Selection method: uniform PowerShell `Get-Random` over the unique-unit array.
- Selected zero-based index: 52,398.
- Selected stable paper ID: arXiv:2401.08092v2.
- Dedup/marker scans: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, and live Black-Lake-Data context.
- Excluded count: 0.
- Duplicate/reselection count: 0.
- Public-safe 24-hour cutoff marker: 2026-07-17.

### Source-Integrity Record

- Initial state: `partial`; PDF and metadata README present, full-paper HTML absent.
- Preserved PDF: 2,100,133 bytes; at least 10 KB; `%PDF-` header present; trailing `%%EOF` present.
- Repaired full-paper HTML: 966,294 bytes; 305,921 body characters; accepted document marker; 130 heading/section markers; seven paper-structure terms.
- Metadata HTML: present and non-empty.
- TeX/source package: downloaded locally.
- Partial/incomplete files after repair: zero.
- Final source state: `complete`; review gate `pass`.
- Public-source policy: no PDF, HTML, metadata page, TeX/source archive, cache, extracted text, or local source path deposited.

### Replication Checklist

- [ ] Pin arXiv:2401.08092v2 and the official companion commit used for any update.
- [ ] Define a reproducible search and screening protocol before claiming literature completeness.
- [ ] Sample primary papers across architecture, algorithm, and system categories and audit their reported denominators.
- [ ] Use a common resource-contract schema for model, workload, hardware, quality, latency, memory, energy/cost proxy, and recovery.
- [ ] Keep original source documents local unless a separate redistribution review explicitly authorizes deposition.
- [ ] Sanitize staged output and verify that only generated public-safe Markdown and approved index records are included.
