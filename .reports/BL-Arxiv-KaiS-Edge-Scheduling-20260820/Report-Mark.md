# Report-Mark: KaiS Edge Scheduling

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Tailored Learning-Based Scheduling for Kubernetes-Oriented Edge-Cloud System* |
| Authors | Yiwen Han; Shihao Shen; Xiaofei Wang; Shiqiang Wang; Victor C. M. Leung |
| arXiv | `2101.06582v1`; submitted 2021-01-17; `cs.DC` with `cs.AI` cross-listing |
| arXiv DOI | `10.48550/arXiv.2101.06582` |
| Published record | IEEE INFOCOM 2021, pages 1-10 |
| Published DOI | `10.1109/INFOCOM42981.2021.9488701` |
| Primary sources | https://arxiv.org/abs/2101.06582 ; https://arxiv.org/html/2101.06582 ; https://arxiv.org/pdf/2101.06582 |
| Source integrity | Complete PDF and official full-paper HTML verified after bounded repair; metadata HTML retained as metadata only; source package unavailable under the exact-surface broker policy |
| Official code context | https://github.com/XiaofeiTJU/KaiS at commit `35d3514ba4b59d68e64772aeba870327a54ccead`; Apache-2.0 adjusted simulator demo |
| Review date | 2026-08-20 |

## Concise Research Notes

KaiS separates Kubernetes-oriented edge-cloud scheduling into two control loops. Coordinated multi-agent actor-critic (`cMMAC`) places a local actor at each edge access point for rapid request dispatch while using a centralized critic during training. A policy-context filter removes resource-invalid destinations from the changing action space. Graph policy gradient (`GPG`) encodes node, access-point, and cluster state with hierarchical GNN aggregation, selects a small number of high-value nodes, and adds/deletes at most one service replica per selected node.

The default paper configuration dispatches every 0.25 seconds and orchestrates every 100 slots, or 25 seconds, with `H = 2` nodes selected for scaling. This time-scale split is the paper's strongest transferable idea: fast routing stays near request arrival, while expensive replica movement occurs less frequently and in bounded steps.

The experiment modifies Alibaba workload traces into 30 service types and generated delay requirements. Five GCP k3s clusters each contain one master and eight edge nodes; a 15-VM Kubernetes cluster supplies cloud capacity. A request generator replaces real end devices, and Linux Traffic Control shapes cloud-edge links. Over 50 clipped arrival sequences, the authors report 14.3% higher throughput and 34.7% lower scheduling cost than the closest baselines.

Other reported results support the decomposition but remain environment-specific: decentralized dispatch completes in roughly 10 ms, centralized orchestration is almost nine times slower, a high-variability sequence yields 3.6% higher average throughput, and plain state stacking loses 1.3% in the smaller setting versus 5.4% in a 100-edge-node setting. No raw curves, seed schedule, confidence intervals, exact trace-transform manifest, or production failure study was available.

The official repository is useful but not a reproduction receipt. Its README says it is a handcrafted simulator with adjusted algorithms and potentially different results. Its pinned `main.py` uses six valid nodes, twelve task types, a 0.5-second slot, and a 1,000-slot orchestration cycle, all materially different from the paper's default. The repository uses TensorFlow 1.14 and contains no test directory or CI workflow in the inspected tree. Code and experiments were not executed.

## Evidence and Attribution

| ID | Evidence | Supports | Reviewer qualification |
|---|---|---|---|
| E1 | arXiv v1 metadata, arXiv DOI, and INFOCOM DOI | Identity, five-author byline, dates, venue, subjects, and canonical locators | Bibliographic evidence does not validate technical claims. |
| E2 | Complete ten-page PDF and official full-paper HTML | Scheduling model, cMMAC, context filtering, GNN encoding, GPG, two-time-scale controller, implementation, experiments, results, and references | Complete primary evidence; no result was independently reproduced. |
| E3 | Sections IV-V and Figures 6-12 | GCP/k3s topology, modified Alibaba traces, baselines, slot/frame sweeps, throughput, delay, cost, and scale claims | Author-reported; raw data, seeds, intervals, and full repetition protocol are absent. |
| E4 | Official KaiS repository at pinned commit | Simulator structure, dependencies, algorithm modules, sample data, and explicit reproduction disclaimer | Adjusted simulator context only; not evidence of deployed-prototype equivalence. |
| E5 | Private source-integrity records | Preserved PDF hash, PDF header/trailer/page state, official HTML body/structure, metadata size, zero partials | Verification evidence remains local and is summarized without private paths. |
| E6 | Cross-repository selection/dedup records | 75,967 PDFs, 75,964 units, 4,904 used IDs, 73,846 eligible units, accepted index 53,128, zero reselections | Conservative used-ID extraction may over-exclude cited works but preserves uniformity over the eligible array. |
| E7 | Exactly three inspected Black Lake entries | Device/cloud transfer, edge/cloud partition, and CTDE MARL implementation relationships | Reviewer synthesis; no related entry validates KaiS's empirical claims. |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md`
   - Relevance: both works split computation across constrained edge devices and a more capable cloud. The related manuscript shows why architectural compression or delegation is not enough: bytes, precision, latency, privacy, compatibility, failure, and fallback must be measured separately.
   - Source basis: inspected source metadata, device-encoder/cloud-decoder mechanism, ImageNet evidence, communication-claim gap, deployment considerations, and reviewer controls.
2. `.lake-data/DEP-A/DEP-A-20260719-Edge Cloud Split/2607.13093-whitepaper-review.md`
   - Relevance: both systems make a local/global cut to reduce latency and transfer. The related review turns that cut into an explicit latency-bandwidth-information boundary, clarifying which state KaiS actors must retain locally and which global context can be delayed or withheld.
   - Source basis: inspected architecture, endpoint/cloud roles, additive split, latency/downlink claims, privacy boundary, and shadow-rollout recommendations.
3. `.lake-data/DEP-E/DEP-E-20260722-SIM MARL Power/sim_marl_power_manuscript.md`
   - Relevance: both map distributed resource allocation to centralized-training/decentralized-execution MARL. The related manuscript reinforces that local execution does not erase training/synchronization cost and that learned proposals require feasibility projection, strong baselines, multi-seed evidence, and rollback.
   - Source basis: inspected NVR-MAPPO mechanism, CTDE state/action design, simulation results, missing ablations, constraint considerations, and implementation proposals.

## Synthesis Note

### Concept Bridge

KaiS can be reframed as a hierarchy of bounded decision contracts. A local dispatcher receives fresh, limited state and must choose one feasible destination within a tight deadline. A slower global controller receives richer graph state and may change only a small number of replicas. Device Tuning MTL and Edge Cloud Split explain the cost and information boundary of that local/global cut; SIM MARL Power explains why centralized training and decentralized execution still need constraint, synchronization, and evidence controls. Together they suggest a modern design in which learned policies rank options, while deterministic Kubernetes policy projects or rejects every action and records the decision.

### Potential Implementations

1. **Offline reproduction harness:** rebuild cMMAC/GPG as modular policies over a deterministic synthetic trace player, with fixed manifests, seeds, matched baselines, raw decisions, and confidence intervals.
2. **Read-only Kubernetes shadow scheduler:** consume sanitized test-cluster telemetry, generate dispatch/scaling proposals, project them through hard constraints, and compare them with native decisions without write access.
3. **Two-cadence guarded autoscaler:** keep fast route recommendations local and slower placement changes global, with no-op fallback, staleness limits, disruption budgets, signed model/config versions, and explicit rollback.

### Deeper Relationship Observations

1. Splitting a controller by locality also splits evidence. Local actors know freshness and immediate feasibility; the global controller knows broader capacity and coupling. A useful interface must expose uncertainty and staleness instead of pretending both sides share one current state.
2. Reducing action dimensionality moves complexity into selection policy and constraints. KaiS's `H`-node filter, Device Tuning's token pooling, and Edge Cloud Split's vocabulary partition all save work only when the discarded options or representation slices are provably irrelevant enough for the current objective.
3. CTDE does not eliminate central cost. KaiS and SIM MARL Power decentralize inference but still rely on global training state, synchronization, model distribution, and observation collection. Those flows belong in latency, bandwidth, privacy, and failure accounting.

### Conceptual Similarities

1. KaiS and Device Tuning MTL both place low-latency, task-specific computation near the device while retaining a shared higher-capacity stage in the cloud.
2. KaiS and Edge Cloud Split both trade global information for lower transfer and faster local decisions, making the boundary itself an optimization variable.
3. KaiS and SIM MARL Power both use local actors with broader centralized learning context to control a coupled resource system whose actions must remain feasible under changing constraints.

### MVP Implementations with Code Mock-Ups

1. **Constraint projection:** accept only bounded, resource-feasible synthetic scaling proposals.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class ScaleProposal:
    node: str
    service: str
    delta: int


def project(proposal: ScaleProposal, headroom: dict[str, int]) -> ScaleProposal:
    if proposal.delta not in {-1, 0, 1}:
        raise ValueError("delta must be -1, 0, or 1")
    if proposal.node not in headroom:
        return ScaleProposal(proposal.node, proposal.service, 0)
    if proposal.delta > headroom[proposal.node]:
        return ScaleProposal(proposal.node, proposal.service, 0)
    return proposal


assert project(ScaleProposal("edge-a", "svc-1", 1), {"edge-a": 0}).delta == 0
```

2. **Cadence contract:** verify that fast dispatch and slow orchestration remain bounded and commensurate.

```python
def validate_cadence(slot_s: float, frame_slots: int, max_frame_s: float) -> float:
    if slot_s <= 0 or frame_slots <= 0:
        raise ValueError("cadence values must be positive")
    frame_s = slot_s * frame_slots
    if frame_s > max_frame_s:
        raise ValueError("orchestration frame exceeds the approved bound")
    return frame_s


assert validate_cadence(0.25, 100, 30.0) == 25.0
```

3. **Experiment receipt gate:** require the fields needed to interpret a scheduler result.

```python
REQUIRED = {
    "trace_manifest",
    "topology_manifest",
    "policy_version",
    "seed",
    "throughput",
    "p99_latency_ms",
    "invalid_actions",
}


def validate_receipt(receipt: dict[str, object]) -> None:
    missing = REQUIRED - receipt.keys()
    if missing:
        raise ValueError(f"missing receipt fields: {sorted(missing)}")
    if int(receipt["invalid_actions"]) != 0:
        raise ValueError("run proposed invalid actions")


validate_receipt({
    "trace_manifest": "synthetic-v1",
    "topology_manifest": "five-region-v1",
    "policy_version": "shadow-001",
    "seed": 7,
    "throughput": 0.91,
    "p99_latency_ms": 42.0,
    "invalid_actions": 0,
})
```

### Developer Challenges

1. **State and version coherence:** queue, resource, network, service, policy, and topology state arrive asynchronously; every decision must bind to a freshness budget and compatible schema/model version.
2. **Safe action integration:** learned route/scale proposals must coexist with quotas, disruption budgets, affinity, topology spread, image availability, rollout state, tenant boundaries, and deterministic fallback.
3. **Evidence-complete evaluation:** trace transforms, seeds, baselines, normalization, per-service SLOs, tail latency, fairness, churn, energy, policy overhead, fault injection, and rollback outcomes must remain joined in one auditable run receipt.

### Author Challenges

1. **Close the reproduction gap:** publish the exact GCP topology, Kubernetes/k3s versions, trace transformation, configurations, seeds, raw curves, and a code revision that matches the paper settings.
2. **Broaden the objective:** report per-service fairness, P95/P99 latency, energy, replica churn, registry traffic, policy compute, and complete cost boundaries rather than throughput and normalized network cost alone.
3. **Test operational failure:** evaluate partitions, stale or malicious telemetry, node/registry outages, model drift, unseen service mixes, invalid actions, and rollback in a modern maintained stack.

## Validation Notes

- Required enumeration used `rg --files -g "*.pdf"`; 75,967 PDFs collapsed to 75,964 parent units.
- The conservative used-paper index contained 4,904 arXiv base IDs. It excluded 1,933 used-ID units and withheld 185 identifier-incomplete units, leaving 73,846 eligible units.
- PowerShell `Get-Random` selected zero-based eligible index 53,128 on the first draw. Duplicate rejections and reselections were both zero.
- Exact arXiv ID, arXiv DOI, INFOCOM DOI, normalized title, and slug checks found no prior same-paper deposit. Public-safe cutoff date: 2026-08-19.
- Review paused when the unit was classified `partial`. A bounded repair preserved the byte-identical PDF, acquired official full-paper HTML and metadata HTML, updated private provenance/summary/verification records, and left zero partials.
- Complete-source gate: 1,257,418-byte PDF with valid header/trailer and ten unencrypted pages; 323,128-byte official HTML with 69,580 stripped characters, document structure, 69 headings, and six structure terms.
- The source package was unavailable after a redirect-policy rejection and was not blindly retried. PDF plus full-paper HTML satisfied the mandatory source gate.
- Paper, HTML, metadata, DOI identity, official repository, and exactly three related entries were inspected. Code and experiments were not run.
- The three Python mock-ups were designed for parser-only validation with standard-library imports.
- Original source files and private verification material remain local. No `.source/` directory was created, and no source file is authorized for GitHub or Slack upload.

## Attribution Block

- Source URL: https://arxiv.org/abs/2101.06582
  - Applies to: paper identity, authors, v1 date, abstract, subjects, license locator, and source links.
- Source URL: https://arxiv.org/html/2101.06582
  - Applies to: method, equations, implementation, experiments, results, conclusion, and references.
- Source URL: https://arxiv.org/pdf/2101.06582
  - Applies to: complete ten-page paper and layout/caption cross-check.
- Source URL: https://doi.org/10.48550/arXiv.2101.06582
  - Applies to: persistent arXiv identity.
- Source URL: https://doi.org/10.1109/INFOCOM42981.2021.9488701
  - Applies to: published IEEE INFOCOM 2021 identity.
- Source URL: https://github.com/XiaofeiTJU/KaiS
  - Applies to: official simulator README, code tree, dependency versions, and implementation/reproduction boundary; inspected at commit `35d3514ba4b59d68e64772aeba870327a54ccead`.
- Source URL: https://github.com/alibaba/clusterdata
  - Applies to: workload-trace provenance cited by the paper and simulator.
- Source file: `.lake-data/DEP-E/DEP-E-20260719-Device Tuning MTL/device_tuning_mtl_manuscript.md`
  - Applies to: device/cloud split, transfer measurement, and deployment-boundary relationship.
- Source file: `.lake-data/DEP-A/DEP-A-20260719-Edge Cloud Split/2607.13093-whitepaper-review.md`
  - Applies to: edge/cloud latency-bandwidth-information relationship.
- Source file: `.lake-data/DEP-E/DEP-E-20260722-SIM MARL Power/sim_marl_power_manuscript.md`
  - Applies to: CTDE MARL, constraint projection, simulation evidence, and rollback relationship.
- Source-handling note: original PDF, full-paper HTML, metadata HTML, acquisition receipts, provenance, verification records, extracted text, and other private archive material were withheld locally and were not uploaded.
