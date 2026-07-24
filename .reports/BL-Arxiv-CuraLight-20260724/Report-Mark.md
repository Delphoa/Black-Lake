# Report-Mark: CuraLight

## Source Metadata

- `Full title`: *CuraLight: Debate-Guided Data Curation for LLM-Centered Traffic Signal Control*.
- `Authors`: Qing Guo, Xinhang Li, Junyu Chen, Zheng Guo, Shengzhe Xu, Lin Zhang, Lei Li.
- `Version`: arXiv:2604.05663v2, dated 2026-04-13 in the inspected paper.
- `Persistent identifiers`: https://doi.org/10.48550/arXiv.2604.05663.
- `Primary sources`: https://arxiv.org/abs/2604.05663, https://arxiv.org/pdf/2604.05663, and https://arxiv.org/html/2604.05663.
- `Official code cited by the paper`: https://anonymous.4open.science/r/CuralightCode-6437/.
- `Source state`: verified complete private PDF plus verified complete private full-paper HTML; metadata HTML collected; all source files withheld.

## Research Notes

CuraLight addresses heterogeneous traffic signal control in which intersections expose different lane, movement, phase, and green-duration choices. It combines a reinforcement-learning assistant, an LLM decision layer, and multi-agent deliberation. A pressure-based policy proposes a phase; diffusion sampling and a distributional critic propose and score green durations. Those references, predicted rollouts, and traffic history become guidance for an LLM controller rather than a direct replacement for it.

The central contribution is data curation rather than only policy architecture. An RL critic assigns priority to LLM decisions. A defender LLM argues for each candidate, a consensus LLM compares candidates through a hidden auxiliary field, and a combined RL-plus-LLM score selects positive and negative trajectories. The resulting curriculum trains Gemma-3-12B-it with LoRA using weighted cross-entropy and unlikelihood objectives.

The reported evidence covers seven SUMO traces spanning Jinan, Hangzhou, and Yizhuang. Networks range from 17 to 177 intersections, and traffic demand ranges from 2,150 to 10,500 vehicles per half-hour. The paper evaluates average travel time, average queue length, and average waiting time. Its headline author-reported averages are improvements of 5.34%, 5.14%, and 7.02% on those metrics. On HZ2, CuraLight reduces travel time from UniTSA's 277.57 seconds to 262.14 seconds and waiting time from 134.52 to 118.80 seconds. JN2 exposes a tradeoff: CuraLight has the lowest queue length, 13.06 metres versus 15.74, while not leading travel or waiting time.

Transfer evidence is promising but bounded. A controller trained on HZ2 is evaluated without adaptation on the 177-intersection Yizhuang network. On YZ1 it reports 11.04% lower travel time and 19.86% lower waiting time than UniTSA, with slightly worse queue length. The within-scenario demand transfer reports a smaller travel-time increase for CuraLight than UniTSA. These comparisons support further transfer testing, not general zero-shot robustness.

The ablation evidence separates imitation from deliberation. On HZ2, the base Gemma model reports 315.42/39.78/165.25 for travel time, queue length, and waiting time; imitation reports 275.35/30.48/136.98; the complete system reports 262.14/25.03/118.80. The paper characterizes the average reductions as about 19.3% for imitation and 28.5% for full deliberation relative to the base model.

The main limitations are evaluation and governance. The work is simulation-only, reports no visible repeated-seed uncertainty or significance tests, and leaves important prompt, judge, mixture-weight, dataset-size, and training-schedule details incomplete. Textual rationales and debate transcripts are useful evidence surfaces, but they are not automatically faithful explanations. The consensus field is deliberately hidden from direct quotation, making retention and audit policy especially important.

A bounded inspection of the cited code found concrete training entry points, SUMO maps, traffic configurations, and hybrid diffusion parameters. It did not establish an environment lock, complete setup guide, fixed evaluation protocol, or reproduced result. The code therefore improves inspectability without yet completing independent reproducibility.

## Evidence and Attribution

| ID | Evidence | Supports | Boundary |
|---|---|---|---|
| E1 | Official arXiv metadata record | Identity, authors, version history, subjects, DOI | Metadata does not validate methods or results |
| E2 | Verified six-page PDF and official full-paper HTML | Architecture, equations, tables, figures, results, limitations | Author-reported and not independently reproduced |
| E3 | Sections on RL guidance and deliberative curation | Pressure policy, diffusion durations, distributional critic, defender/consensus roles, preference construction | Exact prompts, model snapshots, and all coefficients are incomplete |
| E4 | Main comparison tables | Seven SUMO traces, three traffic metrics, baseline comparisons | No raw runs, confidence intervals, significance tests, or physical deployment |
| E5 | Transfer and ablation tables | Cross-network transfer, demand transfer, imitation and deliberation contributions | Limited geography, traces, and scenario perturbations |
| E6 | Resource and implementation disclosures | Gemma-3-12B-it, LoRA, dual-socket CPU, NVIDIA L20, throughput and memory | Hardware disclosure does not establish reproducibility or deployment latency |
| E7 | Bounded inspection of the paper-cited code repository | Training entry point, hybrid-diffusion configuration, maps, SUMO integration | No independent installation, training, or benchmark reproduction |
| E8 | Related Black Lake DEP manuscripts | Heterogeneous traffic control, preference curation, hidden agent state | Related artifacts contextualize but do not validate CuraLight |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` - direct domain overlap in SUMO traffic control, heterogeneous intersection state/action spaces, transfer, and simulation-to-deployment boundaries. Source basis: its inspected full manuscript and evidence ledger.
2. `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - method overlap in failure-guided data curation, dual preference signals, LoRA adaptation, and governance of judge-generated training data. Source basis: its inspected full manuscript and evidence ledger.
3. `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` - conceptual overlap in public versus hidden multi-agent state, debate evidence, and runtime auditability. Source basis: its inspected manuscript; the underlying Agent Laboratory source is abstract-level, so this bridge is treated as conceptual rather than validating evidence.

## Synthesis Note

### Concept Bridge

CuraLight can be read as a layered evidence-control system. Self Learned IDC supplies the domain lesson that a controller must normalize heterogeneous traffic topology without erasing operational constraints. OViP Preference shows how a generator and judge can create an evolving training distribution while also introducing feedback-loop risk. Agent State Review makes the hidden-state issue explicit: public decisions, private deliberation, critic scores, and retained evidence need distinct governance even when they belong to one agent workflow.

### Potential Implementations

1. **Offline intersection-policy audit bench**: replay public or synthetic SUMO scenarios, preserve every candidate action and critic score, and compare safety, latency, and traffic metrics before any deployment claim.
2. **Disagreement-aware curation service**: store RL and LLM scores separately, calibrate them on held-out scenarios, and route systematic disagreement to abstention or expert review.
3. **Topology-normalized controller adapter**: convert varying intersection graphs into a versioned schema while retaining lane, movement, phase, and duration constraints for traceable policy inputs.

### Deeper Relationship Observations

1. CuraLight and OViP both improve a learner by changing which examples receive weight; their largest hidden risk is not model capacity but self-reinforcing selection bias in the curator.
2. The diffusion critic and LLM consensus model are distinct evaluators of the same action space, so their disagreement is a potentially valuable uncertainty signal rather than noise to average away.
3. CuraLight's hidden consensus field resembles private agent state: concealing it may reduce imitation leakage, but it also creates a provenance obligation for authorized audit and incident reconstruction.

### Conceptual Similarities

1. Like Self Learned IDC, CuraLight targets variable traffic topology and uses SUMO evidence while leaving the physical-road transfer gap open.
2. Like OViP Preference, CuraLight turns evaluator judgments into a curriculum and therefore needs model, prompt, sample, and selection-policy versioning.
3. Like Agent State Review, CuraLight separates externally visible output from internal deliberation and needs explicit rules for retention, access, and faithful explanation.

### MVP Implementations With Code Mock-ups

1. **Critic Disagreement Gate**

```python
def gate_action(rl_score, llm_score, maximum_gap=0.25):
    gap = abs(rl_score - llm_score)
    return {"accept": gap <= maximum_gap, "gap": gap}
```

Keep the two evidence channels separate and fail closed when their calibrated scores diverge.

2. **Intersection Schema Adapter**

```python
def normalize_intersection(node_id, phases, duration_bounds):
    return {"node_id": node_id, "phases": list(phases),
            "duration_bounds": tuple(duration_bounds), "schema": "tsc-v1"}
```

Validate every phase and duration against the simulator manifest before prompting a model.

3. **Decision Evidence Receipt**

```python
def decision_receipt(action, rl_score, judge_id, prompt_version):
    return {"action": action, "rl_score": rl_score,
            "judge_id": judge_id, "prompt_version": prompt_version}
```

Record public-safe identifiers and scores without credentials, private prompts, or raw source documents.

### Developer Challenges

1. Reproducing the full system requires exact prompts, judge identities, score normalization, mixture weights, data volumes, seeds, and environment versions not established by the inspected package.
2. Real-time deliberation must respect controller deadlines while handling malformed outputs, unavailable models, unsafe phases, network failures, and deterministic fallback.
3. Evidence storage must preserve candidate decisions and critic disagreement without leaking sensitive infrastructure state or making unaudited hidden reasoning authoritative.

### Author Challenges

1. Report repeated seeds, uncertainty intervals, significance tests, incident stress tests, and a prespecified aggregation rule for competing traffic metrics.
2. Release a reproducible package with environment lock, prompts, judge/model versions, curation counts, coefficients, seeds, manifests, and scripted table regeneration.
3. Evaluate hardware-in-the-loop latency, fail-safe control, operator override, rationale faithfulness, and cross-city transfer before implying real-world readiness.

## Validation Notes

- Random selection: 75,780 PDFs collapsed to 75,777 units; 268 prior-identifier units and 185 identifier-incomplete units were excluded; final eligible pool 75,324; uniform final index 12,989; zero duplicate reselections after pool freeze.
- Selection correction: a preliminary diagnostic draw was discarded before review because identifier derivation was incomplete; the final fixed pool used filename, folder, and metadata identifiers.
- Dedup: arXiv ID, DOI, normalized title, slug, repository artifacts, automation memory, relevant Black-Lake-Data entries, and 24-hour markers were checked with no owning duplicate.
- Source integrity: initial partial unit repaired to complete; preserved PDF passes size/header/EOF and six-page parsing; full-paper HTML passes all size/body/marker/heading/structure checks; no partials remain.
- Review coverage: all six rendered PDF pages, official full-paper HTML, tables, figures, arXiv metadata, and bounded official-code inspection were reviewed.
- Public safety: output contains no private path, username, machine name, local timezone, exact execution timestamp, credential, or source file.
- Source-upload gate: generated Markdown only; no PDF, HTML, archive, cache, extracted source text, render, receipt, or `.source/` directory is allowed in the staged set.

## Attribution Block

- Source URL: https://arxiv.org/abs/2604.05663
  - Applies to: this report and the DEP-E manuscript.
  - Notes: canonical identity, authors, version history, public abstract, license link, and DOI.
- Source URL: https://arxiv.org/pdf/2604.05663
  - Applies to: this report and the DEP-E manuscript.
  - Notes: complete paper inspected from a verified private copy; source file withheld.
- Source URL: https://arxiv.org/html/2604.05663
  - Applies to: this report and the DEP-E manuscript.
  - Notes: verified full-paper HTML used for section and table cross-checking; source file withheld.
- Source URL: https://anonymous.4open.science/r/CuralightCode-6437/
  - Applies to: bounded implementation inspection.
  - Notes: repository cited by the paper; inspection does not claim successful reproduction.
