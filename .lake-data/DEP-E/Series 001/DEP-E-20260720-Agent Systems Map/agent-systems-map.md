---
title: "Agent Systems Map - DEP-E"
generated_at: "2026-07-20T00:01:48Z"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of ten papers on state placement, observability, verified memory, governance, and physical validity in agentic AI systems."
source_status: "URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-20"
temporal_cutoff: "2026-07-20"
primary_url: "https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260715-Tech%20Intel%200102"
stable_identifier: "DEP-20260715-Tech Intel 0102"
confidence_summary: "Medium-high for the cross-paper synthesis; eight full HTML papers and four official repositories were inspected, while two papers were limited to canonical metadata and abstracts."
safety_scope: "Defensive, evaluation-oriented, privacy-preserving, and authorized testing only"
distribution_notes: "Public URLs and repository-relative provenance only; no paper, dataset, model, or source archive is redistributed."
---

# Agent Systems Map - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Selected DEP README | Primary repository artifact | Markdown | `DEP-20260715-Tech Intel 0102` | `Black-Lake-Data/.lake-data/DEP-20260715-Tech Intel 0102/README.md` | Public repository record | 2026-07-20 | Inspected in full |
| S2 | Daily Research Findings | Primary repository artifact | Markdown | 2026-07-15 intake | `Black-Lake-Data/.lake-data/DEP-20260715-Tech Intel 0102/daily_research_findings_2026-07-15_0102.md` | Public repository record | 2026-07-20 | Inspected in full |
| S3 | AAFLOW+ | Primary paper | arXiv HTML | arXiv:2607.10987v1 | https://arxiv.org/abs/2607.10987 | CC BY 4.0 shown by arXiv HTML | 2026-07-20 | Metadata, method, evaluation, limitations, and appendix evidence inspected |
| S4 | MemExchange | Primary paper | arXiv metadata/abstract | arXiv:2607.11579v2 | https://arxiv.org/abs/2607.11579v2 | License link exposed by arXiv; terms not independently interpreted | 2026-07-20 | Canonical metadata and abstract inspected; full HTML unavailable |
| S5 | HCRMap | Primary paper | arXiv HTML | arXiv:2607.11586v1 | https://arxiv.org/abs/2607.11586 | arXiv perpetual non-exclusive license | 2026-07-20 | Method, simulator setup, results, and conclusion inspected |
| S6 | GPU-Tile-Sim | Primary paper | arXiv HTML | arXiv:2607.11262v1 | https://arxiv.org/abs/2607.11262 | arXiv perpetual non-exclusive license | 2026-07-20 | Method, evaluation, ablations, and case studies inspected |
| S7 | Local Monitors and Compositional Harm | Primary paper | arXiv HTML | arXiv:2607.11751v1 | https://arxiv.org/abs/2607.11751 | CC BY 4.0 shown by arXiv HTML | 2026-07-20 | Theory, evaluation scope, results, and limitations inspected |
| S8 | Agent Hacks Agent | Primary paper | arXiv HTML | arXiv:2607.11698v1 | https://arxiv.org/abs/2607.11698 | arXiv perpetual non-exclusive license | 2026-07-20 | Method, held-out evaluation, ablations, and implementation references inspected |
| S9 | Distributional-RL Risk Audit | Primary paper | arXiv HTML | arXiv:2607.11607v1 | https://arxiv.org/abs/2607.11607 | CC BY 4.0 shown by arXiv HTML | 2026-07-20 | Audit method, results, repairs, limitations, and statistics inspected |
| S10 | ToolAtlas | Primary paper | arXiv HTML | arXiv:2607.11126v1 | https://arxiv.org/abs/2607.11126 | CC BY-NC-SA 4.0 shown by arXiv HTML | 2026-07-20 | Method, benchmark tables, transfer results, limitations, and ethics inspected |
| S11 | NVAITC AI Scientist | Primary paper | arXiv HTML | arXiv:2607.11084v1 | https://arxiv.org/abs/2607.11084 | arXiv perpetual non-exclusive license | 2026-07-20 | Architecture, GWAS workflow, governance, results, and limitations inspected |
| S12 | CatRetriever | Primary paper | arXiv metadata/abstract | arXiv:2607.11712v1 | https://arxiv.org/abs/2607.11712 | License link exposed by arXiv; terms not independently interpreted | 2026-07-20 | Canonical metadata and abstract inspected; full HTML unavailable |
| S13 | AAFLOW repository | Official implementation | GitHub repository | `main`, unpinned snapshot | https://github.com/arupcsedu/AAFLOW | MIT license shown by repository | 2026-07-20 | README, layout, stateful module, smoke test, and benchmark references inspected |
| S14 | Observability Boundary repository | Official project repository | GitHub repository | `main`, unpinned snapshot | https://github.com/yibo-hu-lab/observability-boundary | MIT license shown by repository | 2026-07-20 | README inspected; reproduction package stated as not yet public |
| S15 | AHA repository | Official implementation | GitHub repository | `main`, unpinned snapshot | https://github.com/henrymao2004/Auto-research-red-teaming | MIT license; authorized research warning | 2026-07-20 | README, safety warning, quick start, dry run, docs, tests, and license inspected |
| S16 | ToolAtlas repository | Official implementation | GitHub repository | `main`, unpinned snapshot | https://github.com/PuppyKnightUniversity/ToolAtlas | MIT license shown by repository | 2026-07-20 | README, included task suite, memory graph, install, and evaluation paths inspected |

No original paper, PDF, source archive, dataset, model, benchmark output, or repository clone was collected for deposition. Public provenance is limited to the repository-relative source DEP paths and canonical URLs above.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S2 | Repository artifacts | Complete DEP inventory, ten ranked findings, source URLs, and original synthesis | Scope of the selected source bundle and its initial claims | High | The findings document is a prior synthesis, not independent validation |
| E2 | S3, S13 | Full paper and official repository | Stateful operators, compatibility constraints, 4-16 node A100 setup, shared-prefix workload, reported TTFT/compute/memory/throughput results, limitations, and runnable stateful module | KV state as an explicit distributed runtime object | High for inspected claims; medium for reproducibility | No experiment was rerun and the repository snapshot was not commit-pinned |
| E3 | S4 | Canonical metadata and abstract | Utility-based memory allocation, one-sided RDMA MTC protocol, Memcached implementation, up to 100 CloudLab servers, and reported 2.3x/13%/63% results | Cross-node memory trading as a resource-placement mechanism | Medium | Full text was unavailable; methods and caveats beyond the abstract were not inspected |
| E4 | S5 | Full paper | Masked Double DQN residency control, deterministic fast mapping, LEGOSim configuration, recorded router traces, eight MoE models, and geometric-mean latency comparisons | Pressure-aware expert residency across hierarchical memory | High for reported simulator evidence | Evaluation is simulator-based and no hardware reproduction was performed |
| E5 | S6 | Full paper | Warp-level tile graphs, TileLang frontend, A100/H100 kernel suites, end-to-end Llama-3-8B results, ablations, and preliminary Blackwell extension | Dependency structure as a useful performance-modeling abstraction | High for inspected experiments | No simulator code or measurements were executed in this pass |
| E6 | S7, S14 | Full paper and official repository | Local-indistinguishability bound, controlled locality sweep, 0.874 mean AUROC marker-free monitor, decoded-view ceiling, scope limits, and release status | Representation and composition boundaries in runtime safety | High for paper claims; high for repository release status | Public repository says the reproduction package is not yet released; harmful payload details are not operationalized here |
| E7 | S8, S15 | Full paper and official repository | Falsifiable discovery loop, VCG schema, frozen held-out protocol, 47.0% versus 32.8% ASR, ablations, dry run, sandbox and authorization controls | Reusable, auditable vulnerability knowledge for defensive red-teaming | High for inspected claims | Only three scenarios and selected production-agent configurations were evaluated; no attacks were run in this pass |
| E8 | S9 | Full paper | Excess-Wasserstein screening, snapshot-restart Monte Carlo, permutation/bootstrapping/FDR harness, 33 MinAtar runs, 40-95% refutation, positive controls, repair failures, and limitations | Validation must target decision-relevant claims, not proxy confidence | High for inspected evidence | Snapshot-restart access is required and broader calibrated variants remain untested |
| E9 | S10, S16 | Full paper and official repository | Three-layer provider-side memory, execution-verified probing, two MCP benchmarks/eight services, transfer results, lifecycle limits, poisoning risk, and public filesystem artifact | Verified provider-side tool knowledge as shared infrastructure | High for inspected claims | Public repository is a compact artifact and does not by itself reproduce every paper table |
| E10 | S11 | Full paper | Governed broker/Kubeflow architecture, 286,422-person GWAS, aggregate-only boundary, phenotype discordance, PLINK2 workflow, replicated loci, DILI AUC, and limitations | Governance and human reconciliation as part of the research system | High for reported case-study evidence | Single institution; replication rather than novel loci; no participant-level data or analysis outputs were inspected |
| E11 | S12 | Canonical metadata and abstract | Contrastive slab-to-bulk retrieval, R@1 above 91%, R@3 above 98%, and adsorption-energy-targeted discovery pipeline | Physical-parent retrieval as a validity boundary for generated surfaces | Medium | Full text, dataset splits, code, and experimental details were not inspected |

## Executive Summary

The ten-paper source bundle is best read as a map of boundaries that agentic systems must make explicit. Four papers move hidden runtime assumptions into managed objects: AAFLOW+ externalizes KV state, MemExchange reallocates stranded memory by marginal utility, HCRMap controls expert residency across hierarchical memory, and GPU-Tile-Sim represents kernel execution through dependency graphs rather than instruction streams (E2-E5). Together they suggest that agent performance increasingly depends on state placement, movement cost, compatibility, and resource pressure, not only model quality.

Four other papers expose evidence and control boundaries. Local monitors can be information-theoretically blind when harm exists only after composition; AHA stores falsifiable mechanisms rather than one-off payloads; the distributional-RL audit shows that confident risk heads can be decision-irrelevant artifacts; and ToolAtlas moves execution-verified tool knowledge to the provider boundary (E6-E9). The reviewer inference is that durable agent knowledge should be versioned, testable, and attached to the component that owns the relevant behavior.

The final two papers extend the same logic into governed science. NAIS separates agent reasoning from protected-data execution and relies on human-directed phenotype reconciliation, while CatRetriever adds a bulk-structure validity constraint to surface generation (E10-E11). Their domains differ, but both reject unconstrained generation as sufficient evidence. Overall confidence is medium-high for this cross-paper synthesis: eight full HTML papers and four official repositories were inspected, while MemExchange and CatRetriever remain abstract-level evidence only; no code, data, hardware, biomedical analysis, or material-discovery result was independently reproduced.

## Detailed Summary

### State and resource plane

AAFLOW+ treats a model's KV cache as a structured distributed state object with model, tokenizer, position, lineage, placement, and ownership metadata. Operators materialize, transfer, fork, resume, restrict composition, and evict state, while compatibility failures fall back to recomputation. The evaluated workload is specifically a shared-prefix multi-agent topology on 4-16 A100 nodes, not independent stateless chat. The paper reports up to 50.2x lower time to first token, up to 7.63x lower multi-agent compute cost at 16-agent scale, 1.72-6.10x lower peak KV memory, and more than 7.74x higher throughput. Its own limitations narrow the claim to controlled, synthetic, deterministic prompts, short outputs, unconstrained memory, and non-production cluster experiments (E2).

MemExchange operates one layer lower. It estimates tenants' miss-ratio curves, derives marginal utility, and reallocates idle cache capacity across nodes through an application-layer protocol using one-sided RDMA without remote CPU involvement. The v2 arXiv record reports an implementation in Memcached, deployments up to 100 CloudLab servers, up to 2.3x lower remote-access overhead than TCP designs, 13% greater rack-scale memory utilization, and up to 63% lower miss rate for constrained tenants. The selected DEP used the earlier title *MemExchange: Cloud-Scale Memory Trading*; the canonical v2 record now uses *Utility-Driven Distributed Memory Reallocation for Multi-Tenant Datacenters*. Because full text was unavailable, the manuscript does not infer allocator stability, workload coverage, or operational failure modes beyond the abstract (E3).

HCRMap turns MoE hotness into a two-timescale residency problem. A masked Double DQN chooses at most one legal promotion, demotion, retention, or eviction per decision window, and a deterministic mapper assigns token groups among published replicas using queue, path, bank, and tier pressure. Evaluation replays recorded router outputs for eight MoE configurations in LEGOSim on a modeled 3.5D substrate with 16 compute chiplets, four I/O-memory chiplets, stacked SRAM, HBM, and DDR5 tiers. It reports geometric-mean end-to-end latency reductions of 43.6%/43.0% over Hydra, 34.5%/33.1% over MoEntwine, and 46.7%/46.0% over PIMoE for prefill/decode. These are internally comparative simulator results, not measured chiplet hardware outcomes (E4).

GPU-Tile-Sim argues that modern fused LLM kernels are governed by dependency and overlap structure. Its frontend extracts warp-level tile graphs from TileLang IR, and its backend schedules ready operations against throughput-oriented compute, memory, and network abstractions. Across A100/H100 GEMM and attention tests, reported MAPE ranges from 1.22% to 8.71%; end-to-end Llama-3-8B inference on H100 has 8.71% average MAPE, while decode-only configurations average 7.06%. Ablations raise error sharply when cross-warp synchronization or ordering constraints are removed, supporting the mechanism rather than only the headline accuracy. The Blackwell validation remains preliminary (E5).

### Evidence, monitoring, and reusable knowledge

The distributed-backdoor paper formalizes an observability boundary: a monitor restricted to a local view cannot separate attack from benign traffic beyond the information present in that view. Its experiments distinguish splitting from local benignness, show a marker-free assembled-code detector at 0.874 mean AUROC across held-out encodings, and use a decoded-view gate as a diagnostic ceiling that blocks every tested attack when given the encoding family. The claim is not that this ceiling is deployable. The paper explicitly leaves longer horizons, adaptive attackers, covert natural-language reassembly, and non-code harms open. The official repository additionally states that the CPU reproduction package will be released later and is currently available only from the authors (E6).

AHA addresses a different red-team failure: discovery systems often retain payloads or scores but not falsifiable explanations. Its loop commits to a hypothesis and falsifier before building a scenario-valid attack, runs the attack in a sandboxed victim harness, reflects on the trajectory, and promotes evidence-bearing concepts into a Vulnerability Concept Graph. Under a frozen single-shot held-out protocol across Claude Code, Codex, three scenarios, and three victim models, AHA reports 47.0% attack success versus 32.8% for the strongest frozen discovery baseline, a 14.2-point advantage. The official repository includes a dry run, tests, scenario contracts, and explicit instructions to use the harness only on owned or authorized systems (E7).

The distributional-RL audit asks whether a learned return distribution supports the risk trade-offs a user would act on. It screens with an excess-Wasserstein measure, obtains environment ground truth through snapshot-restart Monte Carlo, and uses per-state permutation nulls, bootstrap refutation, and false-discovery-rate control. Across QR-DQN, C51, and IQN on 33 MinAtar runs, 40-95% of the strongest claims are refuted at 95% confidence, while positive controls confirm 96-100% of injected real claims. Risk training and ensembles do not eliminate the pattern; recalibration passes only by nullifying claims. The key transfer is methodological: any high-confidence agent score used for safety or resource decisions needs a decision-level falsification target (E8).

ToolAtlas places reusable knowledge at the provider boundary. It builds linked trace, capability, and strategy graphs from verified task executions and active exploration of tool affordances and failure boundaries, then traverses the graph to produce task-conditioned guidance. Across two MCP benchmarks spanning eight services, it reports gains up to 21.61% in pass@1 and 18.61% in pass@4, plus transfer across environments and agent frameworks. The paper also identifies the operational debt: stored knowledge must be reverified as APIs, permissions, and schemas change, and graph construction from untrusted traces creates a poisoning risk. The public repository supplies a compact filesystem benchmark path rather than evidence that every paper result is independently reproducible from the repository alone (E9).

### Governance and physical validity

NAIS separates agent planning from governed execution near protected biomedical data. The agent submits approved actions through brokered interfaces; PLINK2 and related pipelines execute inside institutional infrastructure; only aggregate artifacts return. In the 286,422-person hypertension case study, an early lab-threshold phenotype disagreed with the expert ICD/medication definition for 3,950 subjects. Human review and a medication audit caused a directed rerun, after which the workflow reproduced established loci including FGF5, ATP2B1, CNNM2, FTO, and GRB14. A secondary 390-compound DILI study reports AUC 0.842. The paper treats governance and scientist oversight as system components, while acknowledging a single-institution setting, replication rather than novel discovery, qualitative locus inspection, and insufficient clinical validation scale (E10).

CatRetriever applies a comparable constraint to materials generation. Surface-only catalyst models can omit the parent bulk structure needed to reason about formation energy, symmetry, surface energy, and synthesizability. CatRetriever aligns slab and bulk embeddings and reports R@1 above 91% and R@3 above 98% on both in-distribution and holdout sets, then combines retrieval with search-space expansion and adsorption-energy analysis. This supports the existence of a useful slab-to-bulk retrieval signal, but abstract-only inspection cannot establish split construction, leakage controls, structure diversity, or experimental synthesis validity (E11).

### Cross-paper mechanism

Across the bundle, the shared mechanism is boundary elevation: internal state becomes a schedulable object; cross-agent harm becomes an assembled representation; tool experience becomes provider-owned memory; risk confidence becomes a claim requiring ground truth; protected data become broker-governed execution; and generated surfaces become candidates requiring a physical parent. The reviewer interpretation is that reliable agent systems should expose five fields for every durable decision: object identity, compatibility or validity predicate, provenance, refresh or invalidation rule, and a falsifiable outcome measure.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Shared-prefix agent workflows can avoid redundant prefill by transferring compatible KV state. | Author claim | E2 | Supported in the paper's controlled cluster and cost-model setting; production and heterogeneous-model transfer remain open. | Medium-high |
| C2 | Utility-guided RDMA memory exchange improves rack-scale cache utilization and constrained-tenant miss rate. | Author claim | E3 | Quantitative claims are present in canonical v2 metadata, but full method and limitations were unavailable. | Medium |
| C3 | Pressure-aware expert residency materially lowers simulated MoE latency across eight models. | Author claim | E4 | Strong within one shared simulator and trace setup; hardware generalization is untested here. | High for simulation, low for hardware deployment |
| C4 | Tile dependency graphs model optimized LLM kernels more accurately than coarser baselines across the tested A100/H100 workloads. | Author claim | E5 | Multiple workloads and mechanism ablations support the claim; Blackwell evidence is preliminary. | High |
| C5 | A local monitor can be fundamentally blind when attack and benign fragments are indistinguishable in its observation view. | Theoretical and empirical author claim | E6 | The bound is representation-relative and the experiments make that boundary visible; deployable representation discovery is unresolved. | High |
| C6 | Falsifier-bearing vulnerability concepts transfer better than frozen payload-oriented discovery artifacts in the evaluated agent scenarios. | Author claim | E7 | Held-out frozen evaluation and ablations support reuse; scenario/model breadth is still narrow. | Medium-high |
| C7 | Distributional-RL heads can express confident risk trade-offs that fail environment-ground-truth audits. | Author claim | E8 | Strong statistical harness and positive controls support the result within evaluated algorithms and games. | High |
| C8 | Execution-verified provider-side memory can improve tool use across agents and environments. | Author claim | E9 | Benchmark and ablation evidence supports the mechanism; lifecycle governance and poisoning remain open. | Medium-high |
| C9 | Governance and scientist reconciliation are enabling components of agentic biomedical research, not external review after execution. | Reviewer interpretation | E10 | The phenotype disagreement and brokered workflow support this interpretation in one institution. | Medium-high |
| C10 | Across these domains, reliability improves when hidden assumptions are converted into explicit, versioned, testable boundary objects. | Derived inference | E2-E11 | Coherent across the source bundle, but not a directly tested unified theory. | Medium |

## Methodology

- `Research objective`: Determine what the selected ten-paper DEP says about the engineering boundaries needed for reliable agentic systems, while preserving paper-specific evidence and uncertainty.
- `Sources inspected`: Both selected DEP files; canonical arXiv records for all ten papers; full arXiv HTML for AAFLOW+, HCRMap, GPU-Tile-Sim, Local Monitors, AHA, the distributional-RL audit, ToolAtlas, and NAIS; canonical metadata and abstracts for MemExchange and CatRetriever; and the official AAFLOW, observability-boundary, AHA, and ToolAtlas repositories.
- `Discovery strategy`: Repository-first inventory, exact arXiv identifier resolution, full-HTML inspection of methods/results/limitations where available, and official implementation-repository inspection for links exposed by papers.
- `Inclusion criteria`: Sources had to be a selected DEP artifact, canonical paper record, full paper, or author-linked implementation directly supporting one of the ten findings.
- `Exclusion criteria`: Secondary commentary, search-result summaries, inaccessible full text, unverified mirrors, and related papers not needed to test the bundle's main synthesis were excluded from evidence claims.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety and ethics, product research, and replication-oriented review.
- `Evidence handling`: Author claims remain labeled as claims; quantitative results retain evaluation context; abstract-only evidence is marked medium confidence; reviewer synthesis is separated from source claims.
- `Uncertainty handling`: Missing full text, unpinned repository snapshots, absent public reproduction packages, simulator-only results, and unperformed reproductions are explicit in the ledger and conclusions.
- `Extraction process`: Repository Markdown and web-rendered paper sections, tables, appendices, and official README material were inspected. No PDF was downloaded, no source archive was collected, and no code or benchmark was executed.
- `Version control`: Paper versions are pinned to arXiv identifiers; repository observations are unpinned access snapshots dated 2026-07-20.
- `Reviewer stance`: DEP-ready cross-paper synthesis, critical review, safe implementation translation, and replication backlog.

## Scope, Constraints, and Assumptions

- `Scope`: The ten primary works and directly linked official repositories contained in or discovered from `DEP-20260715-Tech Intel 0102`.
- `Temporal boundary`: Public sources inspected through 2026-07-20.
- `Evidence limits`: MemExchange and CatRetriever were abstract-only; repository snapshots were not commit-pinned; the observability reproduction package was not publicly released; no external dataset, model, hardware trace, biomedical output, or materials structure was inspected.
- `Assumptions`: Canonical arXiv HTML accurately represents the cited paper version, and official repository READMEs accurately describe their current public contents.
- `Constraints`: Public-output sanitization, redistribution limits, privacy, biomedical governance, and defensive-only handling of red-team material.
- `Out of scope`: Reproducing experiments, executing attacks, accessing participant-level data, validating chiplet hardware, synthesizing catalysts, benchmarking production MCP servers, or making clinical or materials deployment claims.
- `Intended use`: DEP deposition, architecture review, research prioritization, evaluation design, and provenance-preserving follow-on work.
- `Audience`: Agent-system researchers, infrastructure engineers, safety evaluators, tool providers, governance reviewers, and AI-for-science teams.
- `Reproducibility boundary`: Some public code paths exist, but this run establishes inspectability and research questions rather than reproduction.
- `Data sensitivity`: Public paper and repository metadata only; biomedical participant data remain outside the evidence set.

## Observations

- `Observed pattern`: State is becoming portable and explicit at several levels: KV blocks, rack memory, expert replicas, tile dependencies, tool capability graphs, and research run state.
- `Observed pattern`: The strongest safety papers do not merely add classifiers; they change the object being evaluated, from fragments to assemblies, payloads to falsifiable mechanisms, and risk-head confidence to environment-grounded decisions.
- `Technical implication`: Compatibility metadata and invalidation rules are as important as storage. AAFLOW+ requires model/position/lineage compatibility, ToolAtlas needs re-verification as APIs change, and NAIS uses run IDs and governed artifacts to survive failed pipelines.
- `Contradiction or tension`: Several works report large improvements in controlled settings while acknowledging incomplete deployment evidence. HCRMap is simulator-only; AAFLOW+ uses synthetic deterministic prompts; CatRetriever does not establish synthesis; NAIS is one institution.
- `Contradiction or tension`: Public code availability is uneven. AAFLOW, AHA, and ToolAtlas expose runnable material, while the observability repository states that its reproduction package is not yet public.
- `Open question`: Can one boundary ledger represent state compatibility, provenance, refresh conditions, safety observations, and outcome tests across runtime, tool, and research systems without becoming an unmaintainable control plane?
- `Reviewer hypothesis`: Reliability gains will depend less on retaining more context than on assigning each durable claim to an owner that can verify, invalidate, and audit it.

## Considerations

- Resource-plane improvements can create new privacy and governance surfaces because KV state, expert replicas, and tool memories may encode sensitive or stale information.
- Cross-agent safety must inspect composition and effects, but full-trace collection can itself expose secrets. Derived representations should be minimal, access-controlled, and purpose-bound.
- Provider-side memory needs signed provenance, permission-aware partitioning, expiry, and poison-resistant verification before it can serve heterogeneous agents safely.
- AHA is dual-use. Any implementation must remain inside owned or explicitly authorized targets, isolate victims, block external side effects, retain evidence for defensive review, and avoid publishing operational payloads.
- Decision-level audits require a trustworthy ground-truth interface. Where snapshot-restart, physical validation, or expert adjudication is unavailable, the system should surface uncertainty rather than convert a proxy into authority.
- Biomedical and materials results require domain governance. An agent can coordinate a workflow, but phenotype definitions, participant protections, lead-variant claims, synthesis feasibility, and experimental confirmation remain expert responsibilities.
- Repository implementations are moving targets. Future review should pin commits, licenses, environment manifests, expected outputs, and benchmark data before making reproducibility claims.

## Strengths

- The bundle connects infrastructure, safety, evaluation, tools, governance, and science through concrete mechanisms rather than generic agent rhetoric.
- Multiple papers include mechanism-revealing ablations or controls: GPU-Tile-Sim removes dependency classes, the RL audit injects positive controls, AHA removes loop components, and the monitor paper varies the observation view.
- The works often expose boundary conditions instead of hiding them: AAFLOW+ narrows its workload, ToolAtlas names refresh and poisoning risks, NAIS documents phenotype disagreement, and the RL audit records its own failed audit designs.
- Four official repositories add inspectable implementation context, including smoke tests, scenario contracts, safety warnings, public task suites, and explicit release gaps.
- The source DEP preserves a coherent, high-value intake set with direct canonical locators and no unverified redistribution.

## Weaknesses

- Two of ten primary papers could be assessed only through canonical abstracts, limiting methodological confidence.
- Several large reported improvements are tightly bound to synthetic, simulated, benchmark, or single-institution settings.
- Repository observations are unpinned, and public availability does not guarantee that paper results are reproducible.
- The selected bundle spans heterogeneous domains, so the unifying boundary thesis is reviewer synthesis rather than a shared experimental hypothesis.
- No independent execution, statistical recomputation, hardware measurement, biomedical reanalysis, or physical validation was performed.
- Safety-monitor and red-team results center on selected code-like and benchmark attack families; non-code compositional harm and adaptive deployment adversaries remain open.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish commit-pinned replication manifests | All public implementations | Current repository snapshots are mutable | Auditable linkage between paper claims and runnable artifacts | Maintenance and storage burden | Recreate one headline table from a tagged release and signed manifest |
| Add invalidation and deletion tests | KV/tool/provider memory | Reuse without revocation can preserve stale or sensitive state | Safer long-lived memory and clearer ownership | Lower cache hit rate; more recomputation | Create/update/delete fixtures with provenance and rollback checks |
| Evaluate composed representations under privacy budgets | Runtime safety | Full traces may detect more while leaking more | Measured safety/privacy trade-off | Possible missed attacks or excess collection | Compare local, assembly, derived, and decoded views on synthetic authorized traces |
| Cross-validate simulator claims on hardware | HCRMap and GPU-Tile-Sim | Simulation accuracy and policy benefit are distinct claims | Stronger deployment confidence | Hardware access and instrumentation cost | Pre-register workloads and compare latency, energy, and ranking stability |
| Extend decision-level audits beyond RL | Agent confidence and tool memory | Proxy scores can look calibrated while failing action-relevant truth | General falsification discipline | Requires domain-specific ground truth | Audit tool confidence, safety scores, and scheduler predictions against outcomes |
| Multi-institution and prospective governance trials | NAIS | Single-site retrospective replication limits generality | Evidence for portable governance architecture | Legal, privacy, and coordination cost | Federated protocol with site-local execution and aggregate reporting |
| Add synthesis and novelty validation | CatRetriever | Retrieval accuracy does not prove useful new catalysts | Stronger scientific utility claim | Expensive simulation and lab work | Deduplicated holdouts, DFT screening, synthesis triage, and experimental follow-up |

## Potential Implementations

### 1. Stateful workflow compatibility service

- `User`: Multi-agent platform engineers.
- `Goal`: Decide whether to reuse, transfer, or recompute internal state.
- `Core mechanism`: A versioned registry stores model, tokenizer, position, lineage, placement, privacy class, expiry, and cost metadata for each state object.
- `Required inputs`: State descriptors, network/memory telemetry, reuse policy, and tenant authorization.
- `Outputs`: Reuse/transfer/recompute decision, provenance record, and deletion receipt.
- `Risk controls`: Tenant isolation, encryption, expiry, compatibility fail-closed, and auditable fallback.
- `Evaluation`: TTFT, throughput, contamination tests, invalidation success, and cost under shared-prefix synthetic workloads.

### 2. Composition-aware safety gate

- `User`: Agent runtime safety teams.
- `Goal`: Detect harms that appear only after multiple steps compose.
- `Core mechanism`: Build a minimal provenance graph and derived assembly representation before sensitive execution boundaries.
- `Required inputs`: Authorized tool-call metadata, artifact lineage, and a bounded set of candidate assemblies.
- `Outputs`: Allow, block, or require-review decision with evidence trace.
- `Risk controls`: Data minimization, no raw-secret logging, strict retention, human escalation, and non-operational test payloads.
- `Evaluation`: False-positive rate on benign collaboration, attack success on synthetic compositional tests, and privacy leakage budget.

### 3. Provider-side tool knowledge registry

- `User`: MCP and API providers.
- `Goal`: Share verified tool capabilities and failure boundaries across agents.
- `Core mechanism`: Signed capability, trace, and strategy nodes built from synthetic or provider-controlled tasks, each with version, permission scope, expiry, and verifier.
- `Required inputs`: Tool schema, test accounts, synthetic fixtures, verifiers, and change events.
- `Outputs`: Task-conditioned guidance and stale-node alerts.
- `Risk controls`: Trace trust levels, poisoning review, secret redaction, permission partitioning, and automatic invalidation on schema changes.
- `Evaluation`: pass@k, transfer, stale-guidance rate, verification cost, and cross-tenant leakage tests.

### 4. Decision-claim audit harness

- `User`: Evaluation and safety researchers.
- `Goal`: Test whether a model's confidence or risk signal supports the decisions made from it.
- `Core mechanism`: Rank decision-relevant claims, collect ground-truth rollouts or adjudications, calibrate per-item nulls, and control false discoveries.
- `Required inputs`: Frozen policy/model, restartable or replayable environment, action outcomes, and statistical plan.
- `Outputs`: Confirmed, refuted, unresolved, and untestable claim ledger.
- `Risk controls`: Pre-registered metrics, conservative refutation, uncertainty reporting, and no deployment authority from unvalidated proxies.
- `Evaluation`: Positive-control recovery, false-discovery rate, decision regret, and repeatability across seeds.

### 5. Governed research broker

- `User`: Institutional biomedical or materials-science teams.
- `Goal`: Let agents orchestrate approved workflows without direct access to restricted data or unvalidated physical claims.
- `Core mechanism`: Proposal review, human approval, brokered containers, immutable run IDs, aggregate-only outputs, and domain-specific validity gates.
- `Required inputs`: Approved protocol, institutional compute, domain pipelines, expert definitions, and audit policy.
- `Outputs`: Aggregate results, quality-control artifacts, provenance, and manuscript-ready evidence.
- `Risk controls`: Least privilege, site-local execution, ethics approval, consent enforcement, review checkpoints, and claims limited to validated outputs.
- `Evaluation`: Reproducibility, expert agreement, privacy incidents, rerun traceability, and prospective scientific validation.

## Three Ways to Exercise This Research

1. `Synthetic state-compatibility lab`: Objective: test reuse decisions without real user data. Inputs: a toy transformer-state descriptor set, synthetic network costs, and explicit compatibility rules. Method: simulate reuse, transfer, expiry, model-version mismatch, and deletion; compare against recomputation. Output: a decision ledger and cost curve. Success criterion: every incompatible or expired state fails closed while compatible reuse lowers modeled cost. Stop condition: any cross-tenant or deleted-state reuse.
2. `Composition-view benchmark`: Objective: measure what safety evidence appears at local, assembled, and derived-provenance views. Inputs: synthetic benign collaboration traces and non-operational compositional-harm fixtures. Method: score identical episodes under each view with fixed thresholds and a privacy budget. Output: AUROC/false-positive/privacy comparison. Success criterion: the composed view improves detection without exceeding the declared data budget. Stop condition: fixtures become operational, secrets enter traces, or retention exceeds policy.
3. `Tool-memory freshness drill`: Objective: test provider-side memory invalidation. Inputs: a local toy MCP service, synthetic tasks, signed capability nodes, and a controlled schema change. Method: build memory, evaluate a held-out split, mutate one permission or response schema, invalidate affected nodes, and rerun. Output: pass@k, stale-guidance rate, and refresh cost. Success criterion: stale guidance is blocked before use and refreshed nodes recover performance. Stop condition: credentials, external accounts, or production services are required.

## Example MVP Product

- `Product name`: Boundary Ledger.
- `Target user`: Teams building multi-agent runtimes, MCP services, and governed research pipelines.
- `Problem`: Durable state and agent-generated claims are reused without consistent compatibility, provenance, invalidation, or outcome tests.
- `Core workflow`: Register a state or claim; attach owner, version, validity predicate, provenance, expiry, and verifier; evaluate it before reuse; record the decision and outcome; invalidate dependent entries when inputs change.
- `Data requirements`: Repository metadata, synthetic test results, tool schemas, state descriptors, and aggregate operational metrics. Raw prompts, secrets, participant-level data, and unrestricted traces are excluded.
- `Architecture`: Local-first CLI and SQLite ledger; signed JSON records; policy engine for compatibility and expiry; adapter interface for synthetic verifiers; optional read-only dashboard; no autonomous execution of external actions.
- `Success metrics`: 100% rejection of expired/deleted fixtures, zero cross-tenant test leakage, at least 95% dependency invalidation coverage, reproducible decision logs, and measurable reduction in stale guidance during synthetic drills.
- `Risk controls`: Least-privilege adapters, local-only default, redaction, immutable provenance, approval gates for sensitive domains, defensive-only fixtures, and explicit unsupported-state outcomes.
- `Limitations`: The MVP does not transfer real KV tensors, discover attacks, access protected data, validate catalysts, or prove that a verifier represents real-world truth.
- `MVP boundary`: Metadata and synthetic verification only; no production enforcement or automated remediation.
- `Deployment model`: Local CLI with an optional static report generator.
- `Evaluation plan`: Unit tests for versioning and invalidation, property tests for dependency closure, synthetic tenant-isolation tests, and reviewer inspection of every decision class.
- `Failure modes`: Incorrect ownership, incomplete dependency graphs, stale verifiers, overbroad collection, and false confidence from toy tests.
- `Maintenance plan`: Versioned schemas, signed migrations, verifier refresh dates, dependency health checks, and quarterly governance review.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| AAFLOW+ | Primary paper | **Reviewed in this pass:** distributed KV-state objects, shared-prefix evaluation, compatibility rules, and stated limitations. | https://arxiv.org/abs/2607.10987; https://doi.org/10.48550/arXiv.2607.10987 |
| MemExchange | Primary paper | **Reviewed in this pass at canonical abstract level:** utility-driven RDMA memory reallocation; v2 title differs from the selected DEP's initial title. | https://arxiv.org/abs/2607.11579v2; https://doi.org/10.48550/arXiv.2607.11579 |
| HCRMap | Primary paper | **Reviewed in this pass:** two-timescale expert residency, LEGOSim setup, eight-model comparisons, and simulator boundary. | https://arxiv.org/abs/2607.11586; https://doi.org/10.48550/arXiv.2607.11586 |
| GPU-Tile-Sim | Primary paper | **Reviewed in this pass:** dependency-graph mechanism, kernel and end-to-end accuracy, ablations, and preliminary Blackwell evidence. | https://arxiv.org/abs/2607.11262; https://doi.org/10.48550/arXiv.2607.11262 |
| When Local Monitors Miss Compositional Harm | Primary paper | **Reviewed in this pass:** observability bound, locality sweep, representation boundary, and non-deployable decoded-view ceiling. | https://arxiv.org/abs/2607.11751; https://doi.org/10.48550/arXiv.2607.11751 |
| Agent Hacks Agent | Primary paper | **Reviewed in this pass:** falsifiable discovery loop, Vulnerability Concept Graph, frozen held-out evaluation, and defensive sandbox boundary. | https://arxiv.org/abs/2607.11698; https://doi.org/10.48550/arXiv.2607.11698 |
| Auditing the Risk Claims of Distributional Reinforcement Learning | Primary paper | **Reviewed in this pass:** decision-level audit, statistical harness, refutation results, positive controls, and limitations. | https://arxiv.org/abs/2607.11607; https://doi.org/10.48550/arXiv.2607.11607 |
| ToolAtlas | Primary paper | **Reviewed in this pass:** provider-side memory graph, execution-verified probing, transfer results, lifecycle debt, and poisoning risk. | https://arxiv.org/abs/2607.11126; https://doi.org/10.48550/arXiv.2607.11126 |
| NVAITC AI Scientist | Primary paper | **Reviewed in this pass:** governed execution architecture, 286,422-person GWAS, phenotype reconciliation, replication scope, and single-site limits. | https://arxiv.org/abs/2607.11084; https://doi.org/10.48550/arXiv.2607.11084 |
| CatRetriever | Primary paper | **Reviewed in this pass at canonical abstract level:** slab-to-bulk validity boundary and reported retrieval metrics; synthesis validity remains untested here. | https://arxiv.org/abs/2607.11712; https://doi.org/10.48550/arXiv.2607.11712 |
| AAFLOW implementation | Official repository | Public stateful-agentic-algebra module, smoke test, benchmark references, and MIT license. | https://github.com/arupcsedu/AAFLOW |
| Observability Boundary project | Official repository | Public project record and release-status evidence; README says the reproduction package is not yet public. | https://github.com/yibo-hu-lab/observability-boundary |
| AHA implementation | Official repository | Runnable defensive harness, dry run, tests, scenario contracts, documentation, and explicit authorized-use warning. | https://github.com/henrymao2004/Auto-research-red-teaming |
| ToolAtlas implementation | Official repository | Compact public filesystem task suite and graph-memory evaluation path. | https://github.com/PuppyKnightUniversity/ToolAtlas |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | `Black-Lake-Data/.lake-data/DEP-20260715-Tech Intel 0102/README.md` | DEP identity, inventory, original synthesis, and ten canonical locators. | 2026-07-20 | Repository file inspected in full. |
| R2 | `Black-Lake-Data/.lake-data/DEP-20260715-Tech Intel 0102/daily_research_findings_2026-07-15_0102.md` | Ranked findings, source roles, reported metrics, and topical relationships. | 2026-07-20 | Repository file inspected in full. |
| R3 | https://arxiv.org/abs/2607.10987 | AAFLOW+ v1 metadata and full-paper locator. | 2026-07-20 | Full HTML inspected; no file collected. |
| R4 | https://arxiv.org/html/2607.10987 | AAFLOW+ method, setup, results, limitations, and appendices. | 2026-07-20 | Primary full text. |
| R5 | https://github.com/arupcsedu/AAFLOW | Stateful module, smoke test, benchmark paths, repository layout, and license. | 2026-07-20 | Official repository; snapshot not commit-pinned. |
| R6 | https://arxiv.org/abs/2607.11579v2 | MemExchange current title, authors, revision history, abstract method, deployment scale, and metrics. | 2026-07-20 | Canonical metadata/abstract only; full HTML unavailable. |
| R7 | https://arxiv.org/html/2607.11586 | HCRMap method, LEGOSim configuration, eight-model evaluation, and results. | 2026-07-20 | Primary full text; simulator claims not reproduced. |
| R8 | https://arxiv.org/html/2607.11262 | GPU-Tile-Sim method, kernel/end-to-end results, ablations, and case studies. | 2026-07-20 | Primary full text; no execution performed. |
| R9 | https://arxiv.org/html/2607.11751 | Observability theory, evaluation beds, results, scope, and open representation problem. | 2026-07-20 | Primary full text; harmful examples retained only at non-operational conceptual level. |
| R10 | https://github.com/yibo-hu-lab/observability-boundary | Project metadata, key findings, license, and public reproduction-package status. | 2026-07-20 | Official repository says package is not yet public. |
| R11 | https://arxiv.org/html/2607.11698 | AHA method, held-out frozen evaluation, ablations, results, and source-repository link. | 2026-07-20 | Primary full text. |
| R12 | https://github.com/henrymao2004/Auto-research-red-teaming | Public implementation, quick start, dry run, docs, tests, safety warning, and license. | 2026-07-20 | Official repository; no attacks executed. |
| R13 | https://arxiv.org/html/2607.11607 | Distributional-RL audit metric, statistical harness, results, controls, repairs, and limitations. | 2026-07-20 | Primary full text; no statistical recomputation. |
| R14 | https://arxiv.org/html/2607.11126 | ToolAtlas method, benchmark tables, transfer results, limitations, ethics, and poisoning concern. | 2026-07-20 | Primary full text. |
| R15 | https://github.com/PuppyKnightUniversity/ToolAtlas | Compact public artifact, filesystem tasks, memory components, install/evaluation paths, and license. | 2026-07-20 | Official repository; snapshot not commit-pinned. |
| R16 | https://arxiv.org/html/2607.11084 | NAIS architecture, governed execution, GWAS cohort, reconciliation, results, ethics context, and limitations. | 2026-07-20 | Primary full text; no protected data accessed. |
| R17 | https://arxiv.org/abs/2607.11712 | CatRetriever title, authors, abstract method, retrieval metrics, DOI, and subject metadata. | 2026-07-20 | Canonical metadata/abstract only; full HTML unavailable. |
| R18 | `Black-Lake/README.md` | DEP class, README, attribution, log, and commit requirements. | 2026-07-20 | Live default-branch authority inspected after fetch. |
| R19 | `Black-Lake/.lake-data/README.md` | DEP-E placement and publication-index maintenance rules. | 2026-07-20 | Live default-branch authority inspected after fetch. |
| R20 | `Black-Lake-Data/README.md` | Source DEP and attribution standard. | 2026-07-20 | Live default-branch authority inspected after fetch. |

## Appendix

### Selection record

- Automation family: `Black-Lake Data Processing & Review`; `Black-Lake Data Processing & Review 0900`.
- Fixed run timestamp: 2026-07-20T00:01:48Z.
- Eligibility cutoff: 2026-07-19T00:01:48Z.
- Canonical source candidates: 66.
- Family-marker Markdown files checked: 62 across source reports/Report-Marks and output logs/DEP artifacts.
- Excluded candidates: 1 (`DEP-20260628-Tech Intel 0102`), whose five linked same-family marker files were committed at 2026-07-19T00:04:48Z.
- Eligible candidates: 65.
- Final selection method: PowerShell `Get-Random` over the sorted corrected eligible list; eligible-list SHA-256 `2c1636cf0e21a639a301fd2ab69f0b62d119727b5e26f86900b4829e88f0ddd4`.
- Selected DEP: `DEP-20260715-Tech Intel 0102`.
- Audit note: an initial diagnostic draw was discarded before use because its eligibility-mapping probe failed; the final draw above was performed only after the corrected exclusion set was established.

### Source inventory

- Repository files inspected: two selected DEP files and three live repository authority files.
- Full paper HTML inspected: eight.
- Canonical metadata/abstract-only papers: two.
- Official implementation repositories inspected: four.
- Source files collected or deposited: none.

### Replication checklist

- [ ] Pin exact commits for AAFLOW, AHA, ToolAtlas, and the observability project.
- [ ] Reproduce one AAFLOW+ shared-prefix result with a public configuration and expected output.
- [ ] Reproduce one GPU-Tile-Sim kernel table and compare it against measured hardware.
- [ ] Obtain the public observability reproduction package after release and regenerate the headline detector table.
- [ ] Recompute one distributional-RL audit slice with positive and null controls.
- [ ] Run ToolAtlas only against a local toy MCP service and verify invalidation after a schema change.
- [ ] Keep NAIS and CatRetriever follow-up within approved institutional and scientific validation protocols.
