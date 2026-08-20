---
title: "KaiS Edge Scheduling - DEP-E"
generated_at: "2026-08-20 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of KaiS, a two-time-scale learning framework for request dispatch and service orchestration in Kubernetes-oriented edge-cloud systems."
source_status: "verified complete PDF and official full-paper HTML; metadata and private verification records retained locally; source package unavailable"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-20"
temporal_cutoff: "arXiv:2101.06582v1, IEEE INFOCOM 2021 identity, and official KaiS repository state inspected through 2026-08-20"
primary_url: "https://arxiv.org/abs/2101.06582"
stable_identifier: "arXiv:2101.06582v1; DOI 10.1109/INFOCOM42981.2021.9488701"
confidence_summary: "High for source identity, architecture, setup, and printed results; medium for causal interpretation; low for modern production readiness and independent reproducibility."
safety_scope: "offline scheduling research, simulation, shadow evaluation, and authorized test clusters only"
distribution_notes: "Generated Markdown and public URLs only; original source documents, metadata, receipts, caches, and private verification material remain local."
---

# KaiS Edge Scheduling - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | *Tailored Learning-Based Scheduling for Kubernetes-Oriented Edge-Cloud System* | Primary paper | PDF and official full-paper HTML | arXiv:2101.06582v1; ten pages | https://arxiv.org/abs/2101.06582 | arXiv non-exclusive distribution license; private copies withheld | 2026-08-20 | Complete and inspected |
| S2 | arXiv PDF and HTML | Primary technical evidence | PDF/HTML | arXiv:2101.06582v1 | https://arxiv.org/pdf/2101.06582 ; https://arxiv.org/html/2101.06582 | Public reading locators; no source file redistributed | 2026-08-20 | Inspected |
| S3 | arXiv-issued DOI | Persistent identity | DOI | 10.48550/arXiv.2101.06582 | https://doi.org/10.48550/arXiv.2101.06582 | DataCite/arXiv identity | 2026-08-20 | Verified |
| S4 | IEEE INFOCOM record | Published identity | DOI | 10.1109/INFOCOM42981.2021.9488701 | https://doi.org/10.1109/INFOCOM42981.2021.9488701 | Publisher locator; technical claims remain grounded in the inspected paper | 2026-08-20 | Verified |
| S5 | KaiS | Paper-linked implementation context | GitHub repository | commit `35d3514ba4b59d68e64772aeba870327a54ccead` | https://github.com/XiaofeiTJU/KaiS | Apache-2.0; adjusted simulator demo, not a reproduction receipt for the deployed prototype | 2026-08-20 | README, tree, dependencies, and key code paths inspected |
| S6 | Alibaba Cluster Trace Program | Workload provenance | Public repository | paper/repository locator | https://github.com/alibaba/clusterdata | Paper modifies trace fields to generate requests and delay requirements | 2026-08-20 | Locator inspected through paper and KaiS README |
| S7 | Black Lake repository rules | Filing authority | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md ; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Governs class, contents, index, attribution, source withholding, and commit convention | 2026-08-20 | Fetched and read |
| S8 | Black-Lake-Data repository rules | Companion dedup authority | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Used for cross-repository duplicate validation | 2026-08-20 | Fetched and read |
| S9 | Three related Black Lake entries | Conceptual context | DEP-A/DEP-E Markdown | repository-relative paths | See `## Related Research and Reading` | Processed research context; no claims transferred to KaiS | 2026-08-20 | Inspected |

The paper authors are Yiwen Han, Shihao Shen, Xiaofei Wang, Shiqiang Wang, and Victor C. M. Leung. The arXiv record shows one version submitted on 2021-01-17 under Distributed, Parallel, and Cluster Computing (`cs.DC`) with an Artificial Intelligence (`cs.AI`) cross-list. The paper is identified as an IEEE INFOCOM 2021 work.

Source-integrity status is `complete`. The byte-identical pre-existing PDF is 1,257,418 bytes, begins with `%PDF-1.5`, contains ten unencrypted pages, and has a trailing `%%EOF`. The official full-paper HTML is 323,128 bytes and passed the private verifier with 69,580 stripped body characters, a document marker, 69 heading/section markers, and six paper-structure terms. Metadata HTML is 43,406 bytes. No partial file remained. The source-package route redirected outside the exact-surface broker policy and was recorded unavailable; that does not invalidate the complete PDF-plus-HTML gate.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S4 | Primary paper and bibliographic records | title, authors, dates, venue, abstract, identifiers, complete paper | Identity, scope, chronology, and paper-level claims | High | Bibliographic records do not independently validate empirical results |
| E2 | S1/S2, Sections II-III, Algorithms/Figures 2-5 | Primary method evidence | scheduling objective, cMMAC, policy-context filtering, hierarchical GNN encoding, stepwise GPG orchestration | Mechanism and architecture reconstruction | High for transcription | No independent derivation, training, or execution |
| E3 | S1/S2, Sections IV-V, Figures 6-12 | Primary systems/empirical evidence | GCP/k3s topology, modified Alibaba traces, baselines, slot/frame settings, throughput, delay, cost, and scale results | Experimental claims and operational setting | High for transcription; medium for effectiveness | Figures do not expose raw data, seeds, intervals, or full repetition protocol |
| E4 | S5 | Official code context | README disclaimer, repository tree, pinned dependencies, `main.py`, cMMAC/GPG modules, simulator environment | Availability and reproduction boundary | High for inspected repository state | Repository explicitly adjusts the system and algorithms; code was not executed |
| E5 | S6 | Workload provenance | public trace program cited by paper/repository | Origin of request-generation input | Medium-high | KaiS modifies task types and timing fields; exact preprocessing manifest is absent |
| E6 | S9 | Related DEP evidence | device/cloud split, edge/cloud inference partition, CTDE MARL controls | Concept bridges and implementation framing | Medium-high | Related entries do not validate KaiS results |
| E7 | Selection and dedup records | Process evidence | PDF enumeration, parent-unit grouping, used-ID exclusion, uniform draw, exact identity scans | Eligibility and zero-reselection result | High | Conservative ID extraction can over-exclude cited papers but does not bias the uniform eligible draw |
| E8 | Private integrity records | Verification evidence | byte counts, hashes, PDF header/trailer, page/encryption state, HTML structure, partial inventory | Complete-source gate | High | Private paths and files are deliberately withheld |

## Executive Summary

KaiS addresses a coupled edge-cloud control problem that Kubernetes and lightweight edge variants did not natively solve in the paper's setting: each access point must quickly dispatch arriving requests to an eligible edge node or the cloud, while a slower controller decides where service replicas should be added or removed. The authors split those decisions by locality and cadence rather than forcing one global policy to act everywhere at the same frequency.

For dispatch, coordinated multi-agent actor-critic (`cMMAC`) places an actor at every edge access point and trains against a centralized critic. A policy-context filter removes currently invalid destinations from a changing action space. For orchestration, graph policy gradient (`GPG`) encodes edge nodes, access points, and the whole cluster with hierarchical GNN aggregation, selects a small set of high-value nodes, and chooses one add/delete/no-op scaling action per selected node. The default paper configuration uses 0.25-second dispatch slots, 100-slot/25-second orchestration frames, and `H = 2` selected nodes.

The evaluation uses modified Alibaba workload traces, five geographically separated Google Cloud k3s clusters with eight edge nodes each, and a 15-VM Kubernetes cloud cluster. The paper reports that, over 50 clipped request-arrival sequences, KaiS produces 14.3% higher throughput and 34.7% lower scheduling cost than the closest compared baselines. Other reported findings include dispatch in roughly 10 ms, about nine-times-greater delay for centralized service orchestration, 3.6% higher average throughput under a high-variability pattern sequence, and a GNN advantage that grows from 1.3% in the smaller topology to 5.4% in a 100-edge-node topology.

These are meaningful prototype results, not a modern production certificate. Requests are generated rather than sent by real end devices; delay requirements are derived by scaling trace timestamps; scheduling cost focuses mainly on normalized network transfer; and no raw traces, confidence intervals, seed schedule, tail-SLO analysis, or failure-recovery study is supplied. The paper-linked repository is useful but explicitly calls itself a handcrafted simulator with adjusted algorithms. Its pinned TensorFlow 1.14 stack and 0.5-second demo slot differ from the paper's 0.25-second default. Code and experiments were not executed for this review.

## Detailed Summary

### Problem and objective

The target system contains multiple edge access points, heterogeneous edge nodes, and a cloud cluster. Service requests arrive at access points with service types and delay requirements. A request is successful when it is processed within its delay bound. KaiS seeks to maximize long-term throughput: the fraction of arriving requests completed within those bounds over continuing system operation.

The control surface has two interdependent parts. Request dispatch selects an execution destination for each newly scheduled request. Service orchestration places and scales containerized service replicas so future dispatch actions have feasible low-delay destinations. Treating either part alone can strand resources or send requests toward unavailable services.

### Coordinated decentralized dispatch

Each edge access point is an actor in a cooperative Markov game. Its local observation includes the current request, its local dispatch queue, nearby edge-node queues and resources, topology size, and measured cloud latency. The centralized critic receives broader edge/cloud state during training. This centralized-training/decentralized-execution arrangement lets decisions occur near request arrival while using global learning signals to reduce nonstationarity.

The dispatch action space changes as resources and service availability change. KaiS's policy-context filtering retains only currently valid destinations before sampling the action. All actors share a reward that penalizes delay violations and resource imbalance. The design is valuable because it makes feasibility part of policy evaluation rather than expecting a fixed-dimensional action head to learn every invalid state implicitly.

### Hierarchical GNN state encoding

The orchestration state is larger and structurally variable. KaiS first embeds every edge node from resource, queue, deployment, and network information. It then aggregates edge-node embeddings into an access-point summary and access-point summaries into a cluster representation. Separate neural transformations are used at the node, access-point, and cluster levels.

This hierarchy is intended to reduce dependence on a fixed node ordering and fixed topology size. The paper's complex comparison uses ten k3s masters managing between three and fifteen edge nodes each, for 100 edge nodes total. In that setting, plain state stacking is reported to lose 5.4% scheduling performance relative to GNN encoding, compared with a 1.3% loss in the default smaller topology.

### Stepwise service orchestration

Rather than emitting a joint action across every service and node, GPG first scores nodes and selects `H` high-value nodes. For each selected node it chooses among `2W + 1` actions: no change, add one replica of a service, or delete one replica of a service. Resource-invalid actions become no-ops. This decomposition reduces combinatorial action growth and bounds the number of changes in a frame.

The frame reward decreases with total queued work, linking replica placement to backlog reduction. A policy-gradient update learns the hierarchical encoders, the node-ranking policy, and the service-scaling policy. The default `H = 2` is an operating-point choice: larger values offer little reported throughput improvement while increasing scheduling cost.

### Two-time-scale Kubernetes integration

The implementation design uses Kubernetes in the cloud and k3s at the edge, with Docker-hosted services. State monitors read system information and `/proc` data, latency probes report network state, and local cMMAC services choose dispatch actions. GNN encoding services exist across edge, access-point, and cloud levels; the cloud GPG service merges embeddings and calls k3s API servers through a Kubernetes client.

Dispatch occurs every 0.25 seconds in the paper. Orchestration occurs every 100 slots, or 25 seconds. The separation respects different control latencies: request routing must react quickly, while replica changes are heavier and can destabilize a cluster if performed too often. Deletion is delayed until a service is idle.

### Experimental setup

The paper modifies Alibaba workload traces into 30 service classes. Task type becomes service type, and a scaled start/end interval becomes the delay requirement. A request generator sends traffic randomly to k3s masters instead of using physical end devices.

The default edge side uses five GCP regions. Each region has one k3s master and eight k3s edge nodes. Masters use 2 vCPU, 4 GB memory, and 0.3 TB disk; edge nodes use 1-2 vCPU, 2-4 GB memory, and 0.3 TB disk. The cloud uses fifteen VMs, each with 4 vCPU, 16 GB memory, and 1 TB disk. Linux Traffic Control shapes cloud-edge bandwidth and delay. Thirty services with different CPU/memory profiles are handcrafted and stored as Docker images.

The reported baselines include Greedy dispatch, native Kubernetes Horizontal Pod Autoscaler orchestration, GSP-SS joint scheduling with advance request-rate knowledge, and Firmament dispatch. The paper also combines KaiS components with simple alternatives to study cMMAC and GPG separately.

### Results and interpretation

Four arrival patterns are constructed, with 20 sequences per pattern: periodic CPU fluctuation, periodic memory fluctuation, a higher-frequency variant, and raw stochastic arrivals. KaiS reportedly converges under all four; the stochastic case requires at least 1.2 times more frames, and the final gap across patterns is within 4.5%.

Decentralized dispatch completes in around 10 ms in the paper's setup, while centralized service orchestration takes almost nine times as long. A centralized-dispatch comparison also performs worse because observations and decisions cross the network before a request can be routed.

The selected default of 0.25-second slots, 25-second frames, and two orchestrated nodes balances reaction and control overhead in the authors' sweeps. Slots of 0.1 seconds produce adjacent observations that are too similar for effective learning; 0.5-second slots react too slowly. Increasing the orchestration set beyond two nodes adds cost with little benefit.

Under a long sequence that switches between arrival patterns, KaiS is reported to outperform the closest combination baseline by 3.6% average throughput. Under the final comparison over 50 clipped sequences, the reported headline improvement is 14.3% higher throughput with 34.7% lower scheduling cost. These values are author-reported and tied to the stated emulator, trace transformation, baseline implementations, normalization, and control settings.

### Official repository boundary

The paper-linked KaiS repository contains cMMAC and GPG modules, a simple edge-cloud environment, two large sample CSV files, and a `main.py` runner. The pinned requirements are NumPy 1.18.5, TensorFlow 1.14.0, and Matplotlib 3.0.3. Its README says the cluster system was extracted into a handcrafted simulator, algorithms were adjusted, and results may not exactly match the practical system.

The code reinforces that warning: `main.py` says parameters may not be consistent with the actual system, uses six valid edge nodes, twelve task types, a 0.5-second slot, and a 1,000-slot orchestration cycle. The inspected tree has no test directory or continuous-integration workflow. The repository is therefore implementation context and a starting point for archaeology, not evidence that the paper's 40-edge-node GCP prototype or figures can be reproduced unchanged.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Separating fast local dispatch from slower global orchestration is an effective control decomposition. | Author method claim | E2/E3 | Mechanism is explicit and supported by timing/setting sweeps in the paper's environment. | Medium-high |
| C2 | cMMAC handles decentralized dispatch with dynamic feasible action spaces. | Author method claim | E2 | Centralized critic, local actors, and context filtering are directly described. | High for design; medium for general effectiveness |
| C3 | Hierarchical GNN encoding scales better than state stacking as topology complexity increases. | Author empirical claim | E3 | Reported loss grows from 1.3% to 5.4% for stacking; raw runs and intervals are unavailable. | Medium |
| C4 | KaiS improves average throughput by 14.3% and reduces scheduling cost by 34.7% against the closest baselines. | Author empirical claim | E3 | Direct paper statement over 50 clipped sequences; not reproduced and metric normalization is only partially specified. | Medium |
| C5 | KaiS adapts across request patterns and system scales. | Author generalization claim | E3 | Supported inside four constructed patterns and two topology settings; broader workloads and failure regimes remain untested. | Medium-low |
| C6 | The public repository enables paper reproduction. | Availability implication | E4 | Not established. It is an adjusted simulator with materially different settings and no reproducibility manifest. | Low |
| C7 | The design is production-ready for current Kubernetes edge fleets. | Deployment implication | E2-E5 | Not established; software age, telemetry, safety, rollback, multi-tenant security, tail SLOs, and operational failure handling require new evidence. | Low |
| C8 | A modern scheduler should retain the cadence/locality split but place learned policies behind constraint and rollback gates. | Reviewer interpretation | E2/E6 | Strong conceptual fit with the mechanism and related DEP controls; not tested by the paper. | Medium-high |

## Methodology

- `Research objective`: preserve a source-grounded account of KaiS's scheduling decomposition, learning mechanisms, Kubernetes integration, empirical evidence, limitations, and modern implementation relevance.
- `Sources inspected`: verified complete PDF and official full-paper HTML, metadata HTML, arXiv identity/license, INFOCOM DOI identity, paper-linked KaiS repository at a pinned commit, Alibaba trace locator, live repository rules, and exactly three related Black Lake entries.
- `Discovery strategy`: enumerated local PDFs with `rg --files -g "*.pdf"`, grouped each PDF parent as one unit, built a cross-repository used-paper index, drew uniformly with PowerShell `Get-Random`, verified identity from local/public metadata, repaired source integrity, then inspected the complete paper and official implementation context.
- `Inclusion criteria`: primary or near-primary sources that directly support identity, architecture, setup, metrics, code availability, filing authority, or a concrete edge/cloud and multi-agent relationship.
- `Exclusion criteria`: abstract-only text was excluded from technical conclusions; secondary search pages did not support major claims; local source material was excluded from public output; related DEP claims were not transferred to KaiS.
- `Analytical approach`: empirical, conceptual, comparative, implementation, systems/operations, product research, safety, and replication analysis.
- `Evidence handling`: paper statements are labeled as author claims; exact numbers remain attached to their experiment; negative evidence and repository differences are visible; reviewer recommendations are marked as interpretations.
- `Uncertainty handling`: missing raw results, seeds, error intervals, exact trace transformation, modern environment, tail-SLO evidence, and recovery tests remain explicit rather than inferred.
- `Random selection methodology`: 75,967 PDFs collapsed to 75,964 parent units. A conservative cross-repository index contained 4,904 distinct arXiv base IDs; 1,933 used-ID units and 185 identifier-incomplete units were withheld. One uniform draw selected zero-based eligible index 53,128 from 73,846 units.
- `Dedup/reselection validation`: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data `.lake-data`/`.reports` were checked by arXiv ID, arXiv DOI, published DOI, normalized title, and slug. The 24-hour cutoff date was 2026-08-19. Duplicate rejections: zero; reselections: zero.
- `Source-integrity handling`: the initial unit was partial because a valid PDF lacked full-paper HTML. A bounded broker-controlled repair preserved the PDF, collected official full-paper and metadata HTML, refreshed private provenance/summary/verification records, and recorded the source-package redirect as unavailable without blind retry.
- `Integrity verification`: PDF 1,257,418 bytes with valid header/trailer and ten unencrypted pages; HTML 323,128 bytes with 69,580 stripped characters, document structure, 69 headings, and six structural terms; metadata HTML 43,406 bytes; zero partials.
- `Extraction and visual handling`: all ten pages were text-extracted with `pypdf`; official HTML supplied searchable sections, equations, captions, and references. The canonical web PDF parser was used to cross-check page/figure/table placement. A local pixel-rendering runtime was unavailable, so no claim of exhaustive pixel-level figure inspection is made.
- `Version control`: paper pinned to arXiv v1; code pinned to commit `35d3514ba4b59d68e64772aeba870327a54ccead`; repository authorities read from refreshed default branches.
- `Reviewer stance`: paper report, critique, DEP-ready preservation, implementation brief, product translation, and replication planning.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv:2101.06582v1, its INFOCOM identity, complete paper evidence, official simulator repository, exactly three related DEP bridges, and bounded implementation implications.
- `Temporal boundary`: public sources and repository state available through 2026-08-20.
- `Evidence limits`: no experiment, training run, trace replay, Kubernetes deployment, repository build, or benchmark reproduction was performed. Raw plot data, seed schedule, confidence intervals, and exact request-generation manifest were not available.
- `Assumptions`: the inspected PDF/HTML correspond to arXiv v1; reported percentages use internally consistent denominators; the public repository's pinned state is the intended paper-linked demo.
- `Constraints`: no production cluster changes, cloud spending, private telemetry, unbounded training, or autonomous rollout is authorized. Examples use synthetic traces and policy simulation.
- `Out of scope`: certifying modern Kubernetes compatibility, proving convergence, reproducing the GCP environment, measuring production economics, or treating normalized scheduling cost as total cost of ownership.
- `Intended use`: research review, DEP deposition, replication planning, scheduler architecture review, and safe shadow-mode MVP design.
- `Audience`: distributed-systems researchers, Kubernetes platform engineers, edge-computing developers, reinforcement-learning researchers, and technical reviewers.
- `Reproducibility boundary`: readers can reconstruct the conceptual controller and inspect a related simulator, but cannot claim figure-level reproduction without a pinned trace transform, environment manifest, settings, seeds, and raw outputs.
- `Data sensitivity`: public research records only in this artifact; original sources and private archive records remain withheld.
- `Operational boundary`: learned actions are recommendations in authorized test environments until deterministic feasibility, safety, security, and rollback gates pass.

## Observations

- `Observed pattern`: KaiS's most durable design choice is two-time-scale decomposition, not any single neural architecture. It aligns decision cadence with actuation cost.
- `Observed pattern`: policy-context filtering and invalid-action-to-no-op handling anticipate modern action masking and admission-control patterns.
- `Observed pattern`: the GNN benefit grows with topology complexity, supporting structural encoding as a scale tool rather than a universal accuracy boost.
- `Evidence tension`: the headline cost reduction measures mainly network effects around dispatch and image pulling, not policy compute, telemetry collection, model synchronization, or total cloud cost.
- `Evidence tension`: the public simulator uses different slot, node, task, and orchestration settings, so repository availability should not be conflated with paper reproducibility.
- `Technical implication`: a modern controller should treat the learned policy as a proposal generator whose action is projected through Kubernetes resource, disruption, placement, and security policies.
- `Open question`: how does the scheduler behave under access-point failure, partition, stale state, cold-image pulls, image registry failure, nonstationary service mixes, and adversarial telemetry?
- `Open question`: do throughput gains survive when fairness, P95/P99 latency, energy, carbon, replica churn, and SLO violation cost are optimized jointly?
- `Reviewer hypothesis`: offline learning plus shadow evaluation and conservative rollout can preserve KaiS's decomposition while avoiding online exploration on production traffic.

## Considerations

### Control safety and Kubernetes semantics

Replica changes interact with PodDisruptionBudgets, affinity/anti-affinity, quotas, topology-spread constraints, storage locality, image availability, and rollout state. A learned scaling action must never bypass these controls. Invalid actions should be rejected with an auditable reason, and repeated invalid proposals should lower policy authority.

### Observability and state freshness

The policy depends on queue, resource, deployment, and network measurements gathered across regions. Every observation needs a timestamp, schema version, source identity, and staleness budget. A local actor should fall back when the observation or model version is stale, and the global orchestrator should abstain during partial topology views.

### Reward and stakeholder effects

Throughput can improve while a minority service, region, or user experiences starvation. Reward design should include per-service SLOs, fairness, churn, energy, registry traffic, and disruption. Aggregate success rates must be accompanied by service-level and tail distributions.

### Security and multi-tenancy

Telemetry and learned models cross trust boundaries. A deployment needs authenticated observations, least-privilege Kubernetes credentials, tenant isolation, signed model versions, replay protection, anomaly detection, and change receipts. The paper does not evaluate malicious or compromised actors.

### Software lifecycle

TensorFlow 1.14, Python 3.6, Ubuntu 16.04, and older Kubernetes APIs are not a current deployment baseline. A reimplementation should reproduce the algorithmic behavior in a maintained stack before adding features, with equivalence tests against saved synthetic trajectories rather than silently porting behavior.

## Strengths

- Decomposes a genuinely coupled scheduling problem by decision locality and time scale.
- Makes dynamic dispatch feasibility explicit through policy-context filtering.
- Uses centralized training and decentralized execution to keep dispatch near request arrival.
- Uses hierarchical GNN aggregation to represent variable edge topology.
- Reduces orchestration action complexity through node selection and bounded per-node scaling.
- Connects algorithms to a concrete Kubernetes/k3s component design rather than stopping at simulation equations.
- Evaluates multiple request patterns, topology scales, time-scale settings, and baseline combinations.
- Provides an Apache-2.0 paper-linked simulator that exposes algorithm modules and sample data, even though it is not a faithful reproduction package.

## Weaknesses

- The request generator replaces physical end devices, and delay requirements are synthetically derived from trace timing.
- The GCP setup emulates geography and network behavior rather than demonstrating an uncontrolled real edge fleet.
- The paper does not expose raw traces, preprocessing, seeds, confidence intervals, error bars, or a complete repetition protocol.
- Scheduling cost is narrower than end-to-end operational cost and omits policy compute, state collection, synchronization, energy, and failure handling.
- Throughput is not broken down by service, region, fairness, or tail latency.
- No component ablation cleanly separates context filtering, centralized critic, GNN hierarchy, stepwise scheduling, and time-scale effects under matched tuning.
- The public repository's settings differ materially from the paper and include no tests or continuous-integration workflow.
- The software stack is obsolete for current production use and was not executed during this review.
- Failure, partition, stale-state, security, rollback, and multi-tenant scenarios are not evaluated.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release the exact trace transform, topology manifest, configs, seeds, raw curves, and result hashes | Reproducibility | Current paper and simulator cannot regenerate the reported environment unambiguously | Figure-level audit and reliable extension | Artifact maintenance and storage | Reproduce every figure from one pinned manifest in a clean environment |
| Build a maintained reference implementation with behavioral equivalence tests | Software lifecycle | TensorFlow 1.14/Python 3.6 and adjusted demo settings are obsolete | Safer research reuse and modern Kubernetes integration | Porting can change semantics | Replay fixed synthetic trajectories and compare action probabilities/rewards |
| Add factorial ablations for CTDE, context filtering, GNN levels, stepwise selection, and cadence | Causal evidence | Current gains bundle multiple choices | Identifies which mechanism causes each gain | More training and tuning runs | Multi-seed paired comparisons with confidence intervals |
| Measure per-service SLO, fairness, P95/P99 latency, churn, energy, registry traffic, and policy overhead | Objective validity | Throughput and normalized network cost hide operational harms | Deployable decision frontier | Larger telemetry and multi-objective design | Publish Pareto curves and hard-constraint violations |
| Stress partitions, stale telemetry, node loss, registry outage, burst shifts, and malicious observations | Reliability/security | Edge-cloud control is exposed to asynchronous and adversarial state | Evidence for fallback and authority limits | Complex fault harness | Deterministic fault injection with recovery-time and wrong-action metrics |
| Run shadow and canary evaluations behind deterministic Kubernetes policy projection | Deployment safety | Online exploration can disrupt production traffic | Reversible, evidence-gated adoption | Slower rollout and duplicate compute | Predeclare promotion thresholds and rollback triggers |

## Potential Implementations

1. **KaiS reproduction harness**
   - `User`: distributed-systems research team.
   - `Goal`: reproduce the original mechanism under a versioned synthetic topology and trace manifest.
   - `Core mechanism`: modular cMMAC, hierarchical GNN, and stepwise orchestration components with swappable baselines.
   - `Required inputs`: synthetic or public trace segments, topology schema, deterministic seeds, resource limits, and action masks.
   - `Outputs`: raw actions, rewards, throughput, cost, SLO distributions, and provenance hashes.
   - `Risk controls`: offline-only execution, bounded episodes, no cluster credentials, and automatic invalid-action rejection.
   - `Evaluation`: component ablations, multi-seed intervals, and exact manifest replay.

2. **Kubernetes shadow scheduler**
   - `User`: platform/SRE team with an authorized test cluster.
   - `Goal`: compare learned dispatch/scaling proposals with current scheduling decisions without actuating them.
   - `Core mechanism`: read-only telemetry adapter, policy inference, deterministic constraint projection, and decision-delta ledger.
   - `Required inputs`: sanitized metrics, topology, service catalog, SLOs, current scheduler decisions, and model version.
   - `Outputs`: counterfactual proposals, invalid-action reasons, expected benefit, and abstention status.
   - `Risk controls`: no write credentials, strict staleness budget, tenant redaction, signed policy artifact, and kill switch.
   - `Evaluation`: agreement, estimated regret, SLO risk, fairness, and proposal validity over replayed incidents.

3. **Two-cadence autoscaling controller**
   - `User`: edge-platform developer.
   - `Goal`: separate fast request routing from slower replica changes using explicit authority levels.
   - `Core mechanism`: local route scoring each short interval and global placement/scaling planning at a slower interval.
   - `Required inputs`: queue depth, resource headroom, network latency, image locality, rollout state, and disruption budgets.
   - `Outputs`: route recommendation, bounded scaling plan, projected constraints, and rollback receipt.
   - `Risk controls`: policy projection, no-op default, maximum change budget, cooldown, manual approval for high-impact actions, and deterministic fallback.
   - `Evaluation`: tail latency, throughput, churn, cost, recovery time, and constraint-violation rate.

## Three Ways to Exercise This Research

1. **Deterministic trace replay:** Objective: test whether two-time-scale control improves a synthetic service fleet. Inputs: a public/synthetic trace, fixed topology, and seed. Method: replay the same arrivals through native, greedy, and KaiS-inspired policies. Output: per-request decisions and metric distributions. Success criterion: improvement survives multi-seed intervals without fairness or validity regressions. Stop condition: any unbounded queue, invalid action, or non-reproducible run. Safety boundary: offline simulator only.
2. **Topology-scaling ablation:** Objective: test the GNN claim separately from other policy changes. Inputs: graph topologies from small fixed clusters to 100 nodes. Method: hold reward, training budget, and policy size constant while comparing state stacking and hierarchical message passing. Output: quality/runtime frontier and topology-shift failures. Success criterion: a predeclared effect persists across seeds and topology families. Stop condition: tuning or input information differs between arms. Safety boundary: synthetic data and no live cluster.
3. **Read-only shadow trial:** Objective: measure proposal validity in an authorized test environment. Inputs: redacted metrics and current scheduler actions. Method: run inference with read-only credentials, project proposals through deterministic policy checks, and log counterfactual deltas. Output: signed decision receipts and abstention reasons. Success criterion: zero actuation, zero unauthorized data capture, and a sustained validity/SLO-risk threshold. Stop condition: stale state, permission drift, data-scope breach, or failed kill switch. Safety boundary: no write path to Kubernetes.

## Example MVP Product

- `Product name`: CadenceGuard Scheduler Lab.
- `Target user`: Kubernetes platform engineer or edge-computing researcher.
- `Problem`: learned scheduling ideas are difficult to evaluate safely because fast routing and slow orchestration are mixed, evidence is incomplete, and invalid actions can reach a live cluster.
- `Core workflow`: ingest a synthetic/replayed trace; validate topology and service manifests; run native/greedy/KaiS-inspired policies; project every learned proposal through hard constraints; compare throughput, SLO, fairness, churn, and cost; emit a signed experiment receipt.
- `Data requirements`: synthetic/public request traces, resource capacities, network-delay traces, service/image metadata, SLO definitions, and baseline decisions. No customer payloads are needed for the MVP.
- `Architecture`: local trace player; versioned state normalizer; fast dispatch policy; slower orchestration policy; deterministic feasibility projector; metric/evidence ledger; static comparison dashboard.
- `Success metrics`: 100% manifest completeness; deterministic replay for fixed seeds; zero executed invalid actions; complete per-service/tail metrics; reproducible baseline deltas; bounded runtime and storage.
- `Risk controls`: offline-by-default mode, no cluster credentials, read-only shadow adapter as an optional later stage, allowlisted metrics, staleness checks, signed model/config hashes, rate/change budgets, no-op fallback, and explicit human promotion gate.
- `Limitations`: it does not reproduce the original GCP prototype by itself, prove policy convergence, establish production savings, or authorize autonomous actuation.
- `MVP boundary`: synthetic/replayed workloads and recommendation output only; no online training or write access.
- `Deployment model`: local CLI plus static HTML report, optionally connected to a read-only test-cluster metrics endpoint.
- `Evaluation plan`: unit tests for manifests and constraint projection; golden trace replays; multi-seed baseline comparison; fault injection for stale/missing state; manual review of promotion criteria.
- `Failure modes`: reward/metric mismatch, stale telemetry, topology-schema drift, baseline leakage, invalid action masking, policy collapse, and misleading average metrics.
- `Maintenance plan`: versioned trace/topology schemas, locked dependencies, policy-card updates, regression corpus, and periodic Kubernetes API compatibility review.

## Related Research and Reading

| Item | Type | Relevance | Repository-relative locator |
|---|---|---|---|
| Device Tuning MTL - DEP-E | Related DEP-E manuscript | Shows that splitting work across device and cloud requires direct transfer, latency, privacy, and failure measurements rather than architectural intuition. | `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` |
| Edge Cloud Split - DEP-A | Related DEP-A review | Makes the edge/cloud partition an explicit latency-bandwidth-information boundary and supplies a useful comparison for KaiS's local/global controller split. | `.lake-data/DEP-A/DEP-A-20260719-Edge Cloud Split/2607.13093-whitepaper-review.md` |
| SIM MARL Power - DEP-E | Related DEP-E manuscript | Provides a second CTDE MARL resource-allocation case and reinforces the need for constraint projection, strong baselines, multi-seed evidence, and rollback. | `.lake-data/DEP-E/DEP-E-20260722-SIM MARL Power/sim_marl_power_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2101.06582 | Identity, authors, v1 date, abstract, subjects, artifact links, license locator | 2026-08-20 | Canonical metadata; abstract not used alone for technical claims |
| R2 | https://arxiv.org/html/2101.06582 | Full method, equations, implementation, experiments, results, conclusion, references | 2026-08-20 | Official full-paper HTML; passed private full-document gate |
| R3 | https://arxiv.org/pdf/2101.06582 | Ten-page complete paper and layout/caption cross-check | 2026-08-20 | Original file withheld locally |
| R4 | https://doi.org/10.48550/arXiv.2101.06582 | Persistent arXiv identity | 2026-08-20 | arXiv-issued DOI |
| R5 | https://doi.org/10.1109/INFOCOM42981.2021.9488701 | IEEE INFOCOM 2021 published identity | 2026-08-20 | Publisher locator |
| R6 | https://github.com/XiaofeiTJU/KaiS | Official simulator README, code tree, dependencies, implementation boundary | 2026-08-20 | Inspected at commit `35d3514ba4b59d68e64772aeba870327a54ccead`; code not run |
| R7 | https://github.com/alibaba/clusterdata | Workload-trace program cited by paper/repository | 2026-08-20 | Exact KaiS preprocessing manifest unavailable |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public artifact, source-withholding, DEP, and commit rules | 2026-08-20 | Live filing authority |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP class container and publication-index requirements | 2026-08-20 | Live filing authority |
| R10 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository dedup scope | 2026-08-20 | Live repository authority |
| R11 | `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md` | Device/cloud split and measurement bridge | 2026-08-20 | Inspected processed artifact |
| R12 | `.lake-data/DEP-A/DEP-A-20260719-Edge Cloud Split/2607.13093-whitepaper-review.md` | Edge/cloud latency-bandwidth-information bridge | 2026-08-20 | Inspected processed artifact |
| R13 | `.lake-data/DEP-E/DEP-E-20260722-SIM MARL Power/sim_marl_power_manuscript.md` | CTDE MARL and constraint/rollback bridge | 2026-08-20 | Inspected processed artifact |

## Appendix

### Selection and dedup receipt

| Field | Value |
|---|---:|
| PDF candidates | 75,967 |
| Parent paper units | 75,964 |
| Conservatively observed used arXiv IDs | 4,904 |
| Units excluded by used ID | 1,933 |
| Identifier-incomplete units withheld | 185 |
| Eligible units | 73,846 |
| Selected zero-based eligible index | 53,128 |
| Duplicate rejections | 0 |
| Reselections | 0 |
| Public-safe 24-hour cutoff date | 2026-08-19 |

### Source-integrity receipt

- Initial classification: `partial` because full-paper HTML was absent.
- Final classification: `complete` after one bounded broker-controlled repair.
- PDF: preserved byte-for-byte; 1,257,418 bytes; valid header/trailer; ten pages; unencrypted.
- Full-paper HTML: official arXiv HTML; 323,128 bytes; 69,580 stripped body characters; document marker; 69 headings; six structure terms.
- Metadata HTML: 43,406 bytes; metadata only.
- TeX/source: unavailable after redirect-policy rejection; no blind retry.
- Partials: zero.
- Public source upload: none. No `.source/` directory exists.

### Replication checklist

- [ ] Pin the exact request-trace transformation and original data revision.
- [ ] Pin topology, service images, Kubernetes/k3s versions, network shaping, and hardware.
- [ ] Define every reward component, metric denominator, normalization, and cost boundary.
- [ ] Publish seeds, raw trajectories, model/config hashes, baselines, and uncertainty intervals.
- [ ] Separate cMMAC, context filtering, GNN hierarchy, stepwise actions, and cadence in ablations.
- [ ] Add partitions, stale state, node loss, registry failure, and adversarial telemetry tests.
- [ ] Report per-service fairness, P95/P99 latency, churn, energy, and constraint violations.
- [ ] Keep live actuation behind deterministic feasibility, canary, rollback, and human authority gates.

## Attribution Block

- Primary paper and metadata: https://arxiv.org/abs/2101.06582 ; https://arxiv.org/html/2101.06582 ; https://arxiv.org/pdf/2101.06582
- Persistent identities: https://doi.org/10.48550/arXiv.2101.06582 ; https://doi.org/10.1109/INFOCOM42981.2021.9488701
- Paper-linked code context: https://github.com/XiaofeiTJU/KaiS at commit `35d3514ba4b59d68e64772aeba870327a54ccead`
- Workload-trace context: https://github.com/alibaba/clusterdata
- Repository authorities: https://github.com/Delphoa/Black-Lake/blob/main/README.md ; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md ; https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
- Related processed artifacts: `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md`; `.lake-data/DEP-A/DEP-A-20260719-Edge Cloud Split/2607.13093-whitepaper-review.md`; `.lake-data/DEP-E/DEP-E-20260722-SIM MARL Power/sim_marl_power_manuscript.md`.
- Source-handling note: original PDF, full-paper HTML, metadata HTML, receipts, provenance, verification records, extracted text, and other private archive files were withheld locally and were not uploaded.
