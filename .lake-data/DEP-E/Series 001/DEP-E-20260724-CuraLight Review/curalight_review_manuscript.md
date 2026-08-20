---
title: "CuraLight Review - DEP-E"
generated_at: "2026-07-24 (public-safe date marker)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of debate-guided data curation for LLM-centered traffic signal control."
source_status: "verified private PDF and full-paper HTML; public URLs only in deposit"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-24"
temporal_cutoff: "arXiv v2 and paper-cited code repository; sources checked through the public date marker"
primary_url: "https://arxiv.org/abs/2604.05663"
stable_identifier: "arXiv:2604.05663v2; DOI 10.48550/arXiv.2604.05663"
confidence_summary: "High for identity and source transcription; medium for comparative interpretation and code inspectability; low for independent reproducibility and road-deployment readiness."
safety_scope: "offline simulation, traffic-policy auditing, research replication, and human-supervised prototyping"
distribution_notes: "Source files remain private and local; generated public-safe Markdown only."
---

# CuraLight Review - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | CuraLight arXiv record | Primary metadata | HTML | arXiv:2604.05663v2 | https://arxiv.org/abs/2604.05663 | Public metadata and license link; metadata alone is not the paper | 2026-07-24 | Inspected |
| S2 | CuraLight complete paper | Primary artifact | PDF and full-paper HTML | v2; six pages | https://arxiv.org/pdf/2604.05663; https://arxiv.org/html/2604.05663 | Verified private copies inspected and withheld | 2026-07-24 | Fully inspected, rendered, and integrity-verified |
| S3 | Paper-cited CuraLight code | Implementation evidence | Source repository | CuralightCode-6437 | https://anonymous.4open.science/r/CuralightCode-6437/ | Public anonymous repository cited by the paper | 2026-07-24 | Bounded file and configuration inspection; not executed |
| S4 | Self Learned IDC DEP | Related Black Lake artifact | Markdown | DEP-E-20260710 | `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` | Repository context only | 2026-07-24 | Full manuscript inspected |
| S5 | OViP Preference DEP | Related Black Lake artifact | Markdown | DEP-E-20260714 | `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` | Repository context only | 2026-07-24 | Full manuscript inspected |
| S6 | Agent State Review DEP | Related Black Lake artifact | Markdown | DEP-E-20260708 | `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` | Repository context; underlying source is abstract-level | 2026-07-24 | Manuscript inspected with source-depth caveat |
| S7 | Selection, dedup, and integrity evidence | Processing evidence | Public-safe summary | 75,324 final eligible units | This manuscript, Methodology and Appendix | No private path or exact execution timestamp | 2026-07-24 | Generated and validated |

Paper metadata:

- `Title`: *CuraLight: Debate-Guided Data Curation for LLM-Centered Traffic Signal Control*.
- `Authors`: Qing Guo, Xinhang Li, Junyu Chen, Zheng Guo, Shengzhe Xu, Lin Zhang, Lei Li.
- `Version`: arXiv:2604.05663v2; the inspected PDF is dated 2026-04-13.
- `Identifier`: DOI 10.48550/arXiv.2604.05663.
- `Source files deposited`: none; no `.source/` directory.
- `Venue status`: no publisher venue was confirmed from the inspected primary sources.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, identifier, version history, subjects, DOI | Bibliographic identity | High | Metadata alone cannot validate method or results |
| E2 | S2, problem and method sections | Primary full text | Heterogeneous intersection model; phase and duration actions; pressure policy; diffusion duration candidates; distributional critic | RL-guided decision architecture | High for transcription | Mathematical behavior was not independently rederived or executed |
| E3 | S2, deliberation and training sections | Primary full text | RL priority labels; defender and consensus roles; positive/negative trajectories; weighted cross-entropy and unlikelihood; Gemma-3-12B-it with LoRA | Data-curation and fine-tuning mechanism | High for transcription | Exact prompts, judge snapshots, coefficients, and corpus sizes are incomplete |
| E4 | S2, experiment tables | Primary tables | Seven SUMO traces; Jinan, Hangzhou, Yizhuang networks; ATT, AQL, AWT; baseline comparisons | Main performance claims | High for reporting | Author-reported; repeated seeds, uncertainty, and significance tests not visible |
| E5 | S2, transfer tables | Primary tables and prose | HZ2-to-Yizhuang no-adaptation transfer and within-scenario demand transfer | Transfer claim | Medium-high | Limited cities, traces, and perturbation types |
| E6 | S2, ablation table | Primary table | Base Gemma, imitation, and full deliberation results on HZ2 | Incremental contribution of curation and debate | High for reporting | One scenario does not isolate every component or judge bias |
| E7 | S2, resource disclosure | Primary prose | CPU/GPU, token lengths, throughput, memory, LoRA backbone | Compute and deployment context | High for transcription | End-to-end latency and cost under real controller deadlines are not established |
| E8 | S3 | Public implementation | Training entry point, SUMO integration, scenario assets, hybrid-diffusion configuration | Code inspectability | Medium-high | No environment lock or successful independent run |
| E9 | S4-S6 | Related DEP artifacts | Heterogeneous topology, preference loops, and hidden-state governance | Cross-DEP synthesis | Medium | Related artifacts do not validate CuraLight |
| E10 | S7 | Process evidence | Corrected fixed-pool draw, dedup scans, archive repair, verification, public-output checks | Selection and integrity | High | Depends on repository and archive state at the public date marker |

## Executive Summary

CuraLight is an LLM-centered traffic signal controller whose distinctive contribution is the curation loop around the model. A reinforcement-learning assistant produces structured phase and green-duration references. An LLM reasons over those references and traffic history. A defender-and-consensus ensemble then compares candidate decisions, combines its preference with an RL critic score, and constructs positive and negative trajectories for LoRA adaptation.

The paper reports favorable average travel time, queue length, and waiting time across seven SUMO traces. It also reports no-adaptation transfer from a 19-intersection Hangzhou scenario to two 177-intersection Yizhuang traces and an ablation in which imitation improves a base Gemma controller while full deliberation improves it further. These results support the idea that task-aligned data selection can matter as much as the LLM backbone.

The evidence boundary is substantial. All results are simulated. The inspected paper does not expose uncertainty intervals, significance tests, physical-controller safety tests, or a complete reproduction manifest. Several elements that determine the training distribution - prompts, judge identities, data counts, mixture coefficients, and exact schedules - remain underspecified. The paper-cited repository contains meaningful code and assets, but the bounded inspection did not establish a locked environment or regenerated results.

The practical lesson is to treat CuraLight as an evidence-producing research architecture, not a deployment-ready traffic controller. A responsible implementation would preserve RL and LLM scores separately, treat disagreement as uncertainty, validate every action against an intersection manifest, provide deterministic fallback, and retain an auditable decision receipt without presenting generated rationale as guaranteed causal explanation.

## Detailed Summary

### Problem and Setting

Traffic signal control is heterogeneous. One intersection may have different incoming lanes, legal movements, phase combinations, and allowable green durations from another. A controller that assumes a fixed observation or action shape can overfit to a single network or require costly retraining. CuraLight instead frames the LLM as a flexible decision layer that receives structured, topology-aware context.

The control target includes both phase choice and green duration. The road network is represented as a directed graph. State summaries cover current and historical traffic, and the prompt includes predicted consequences and reference actions. The controller is evaluated in SUMO rather than on physical infrastructure.

### RL Guidance

The phase reference follows a pressure-based principle: select a phase that relieves imbalance between incoming and outgoing movements. Green duration is handled through a hybrid diffusion assistant. History provides anchors; a diffusion model samples possible durations; a distributional critic evaluates them. This division is important because it keeps hard traffic-domain structure outside the language model while allowing the LLM to reconcile several signals.

The guidance layer does more than output a suggested action. It also contributes a predicted rollout, time-queue history, and a critic score used later in curation. The LLM therefore receives both a proposal and evidence about its likely consequence. The design is closer to tool-augmented decision making than to unconstrained text generation.

### Debate-Guided Curation

The curation loop first uses the RL critic to prioritize candidate LLM decisions. A defender model then argues for each candidate. A consensus model compares candidates through an auxiliary field that is not directly quoted into the final output. RL quality and LLM preference are mapped into a combined score with a mixture coefficient.

High-scoring and low-scoring decisions become positive and negative trajectories. The paper uses weighted cross-entropy for preferred behavior and unlikelihood training for rejected behavior. It describes a curriculum that admits higher-priority data before lower-priority examples. Gemma-3-12B-it is the reported backbone and LoRA is the adaptation mechanism.

This approach targets a familiar agent-training problem: raw trajectories contain decisions that are plausible in language but weak in domain outcome. Curation attempts to transform domain feedback into a trainable preference signal. Its weakness is circularity: an LLM judge and an RL critic may share blind spots, and the final learner can amplify whatever the selection system rewards.

### Evaluation Environment

The evaluation includes Jinan networks JN1, JN2, and JN3 with 17 intersections; Hangzhou HZ1 and HZ2 with 19 intersections; and Yizhuang YZ1 and YZ2 with 177 intersections. Reported demand ranges from 2,150 to 10,500 vehicles per half-hour.

The primary metrics are average travel time in seconds, average queue length in metres, and average waiting time in seconds. These metrics can conflict. A policy may reduce queues at a subset of intersections while increasing travel time elsewhere, so an aggregate claim needs a prespecified rule rather than post hoc metric selection.

The paper's hardware disclosure lists a dual-socket Intel Xeon Platinum 8457C system and one NVIDIA L20 with 48 GiB under CUDA 12.4. It reports an average batch size of 2.85, average input and output lengths of 960 and 356 tokens, throughput of 242 tokens per second, and peak GPU use around 44,200 MiB. These figures help bound training or evaluation cost, but they do not establish controller-loop latency under failure and fallback conditions.

### Main Results

The authors summarize average gains over the comparison set as approximately 5.34% for average travel time, 5.14% for average queue length, and 7.02% for average waiting time. The underlying tables matter more than the aggregate:

- On HZ2, UniTSA reports travel time 277.57 and waiting time 134.52, while CuraLight reports 262.14 and 118.80, reductions of about 5.56% and 11.69%.
- On JN2, CuraLight reports queue length 13.06 versus UniTSA's 15.74, about a 17.03% reduction, but it does not lead travel time or waiting time. This is evidence of a real metric tradeoff rather than uniform dominance.
- Across the seven traces, the direction of improvement is generally favorable, but without run-level dispersion the stability of the ranking cannot be assessed.

### Transfer and Ablation

For cross-network transfer, the HZ2-trained controller is evaluated without adaptation on Yizhuang. On YZ1, CuraLight reports 11.04% lower travel time and 19.86% lower waiting time than UniTSA, while queue length is slightly worse. The result is notable because the target network is much larger, but two traces within one additional city are not enough to establish broad topology invariance.

For demand transfer within HZ2, the paper reports that CuraLight's travel time increases by about 1.26%, compared with about 4.56% for UniTSA. This supports robustness to the tested demand shift, subject to the same missing uncertainty information.

The HZ2 ablation reports:

| Variant | ATT | AQL | AWT |
|---|---:|---:|---:|
| Gemma base | 315.42 | 39.78 | 165.25 |
| Imitation | 275.35 | 30.48 | 136.98 |
| Full CuraLight | 262.14 | 25.03 | 118.80 |

The paper describes average reductions of roughly 19.3% from imitation and 28.5% from full deliberation relative to the base. The table supports incremental value under HZ2, but it does not isolate judge choice, critic calibration, hidden consensus, negative training, or curriculum order one at a time.

### Implementation Inspectability

The paper-cited code repository contains training entry points, `HDA` components, SUMO integration, maps, traffic configurations, logs, and fine-tuning material. A training entry point invokes the hybrid-diffusion trainer. The inspected configuration includes 1,000 training episodes, 1 evaluation episode, 1,800 steps, duration bounds from 5 to 40, hidden width 256, phase embedding 64, learning rate `3e-4`, soft-update coefficient `5e-3`, batch size 128, replay capacity 10,000, eight diffusion steps, and latent width 8.

Those details make the mechanism more inspectable. The repository's minimal top-level documentation, missing environment lock, unclear seed protocol, and lack of a verified table-regeneration workflow prevent a stronger reproducibility conclusion. This review did not install or execute the repository.

## Key Claims and Evidence

### Claim: task-aligned curation improves the LLM controller

The HZ2 ablation is direct supporting evidence: imitation improves all three metrics over the base Gemma model, and the full deliberative system improves them again. Confidence is medium-high for the reported comparison and low for generalization beyond the tested setup. A stronger test would hold compute, number of training examples, and model updates constant while varying only curation.

### Claim: the controller handles heterogeneous road networks

Evidence includes training on a 19-intersection Hangzhou trace and no-adaptation evaluation on two 177-intersection Yizhuang traces. The favorable travel and waiting results support transfer to the inspected target. The slightly worse queue result and narrow set of geographies show why the claim should remain bounded.

### Claim: RL guidance and LLM deliberation are complementary

The architecture uses an RL proposal and critic rather than asking the LLM to discover traffic dynamics unaided. The ablation from imitation to full deliberation is consistent with complementary value. It does not prove that the defender and consensus roles are necessary, because the paper does not expose a full factorial component analysis.

### Claim: debate improves interpretability

Defender rationales and consensus comparisons create inspectable text around decisions. That is procedural transparency. It is not evidence that the rationale faithfully represents the internal cause of the action, nor that the hidden auxiliary field is free of unsupported assertions. Interpretability should therefore be described as an auditable evidence surface, not a causal explanation guarantee.

## Methodology

### Selection

The private archive was enumerated with `rg --files -g "*.pdf"`. Each unique PDF parent directory was one paper unit. Identifiers were derived from filenames, folder names, and nearby metadata, with arXiv IDs preferred. The enumeration found 75,780 PDFs in 75,777 units.

Repository surfaces and automation memory supplied 673 observed normalized identifiers. At the unit level, 268 prior-identifier matches were excluded. A further 185 units lacked a usable normalized identifier and were withheld from the draw. The sorted fixed eligible pool therefore contained 75,324 units.

PowerShell `Get-Random` selected zero-based eligible index 12,989, yielding arXiv:2604.05663. A preliminary diagnostic draw was discarded before paper review because it used incomplete identifier derivation. The corrected full-pool draw was uniform and required zero duplicate reselections.

### Deduplication

The accepted unit was checked by arXiv ID, DOI, normalized title, and slug across Black Lake `.logs`, `.reports`, `.lake-data`, automation memory, and relevant Black-Lake-Data records. It was also checked for an owning DEP and a same-paper marker within the preceding 24 hours. One author inventory row in the related data repository was metadata, not an owning DEP. No prior Arxiv DEP artifact or recent same-paper marker was found.

### Source Integrity

The unit initially contained a valid 7,295,610-byte PDF but lacked full-paper HTML, so it was classified partial and synthesis stopped. The valid PDF was preserved. A paced archive repair collected official full-paper HTML and metadata HTML, retained no partial downloads, and updated private provenance, machine-readable summary, and verification records.

The final PDF exceeds 10 KB, begins with `%PDF-`, ends with `%%EOF`, and parses as six pages. Full-paper HTML is 188,114 bytes with 34,193 body characters after script/style removal, a full-document marker, 46 heading or section markers, and six paper-structure terms. The final source state is complete. The optional source package was unavailable because its redirect was rejected by the archive broker; that is not part of the PDF-plus-full-paper-HTML gate.

### Review and Synthesis

All six PDF pages were rendered and visually inspected. Official full-paper HTML was cross-checked for sections, tables, and structure. The public metadata record and paper-cited code repository were inspected separately. Claims in this manuscript distinguish author-reported evidence, repository observations, reviewer inference, and unverified gaps.

Exactly three Black Lake entries were selected for concrete overlap:

1. Self Learned IDC for heterogeneous, simulation-based traffic control.
2. OViP Preference for evaluator-driven curation and feedback-loop governance.
3. Agent State Review for public-versus-hidden deliberation state and auditability.

## Scope, Constraints, and Assumptions

- The review covers arXiv v2, its official public records, and a bounded inspection of the paper-cited code repository.
- Numeric results are transcribed from the authors' tables and were not independently reproduced.
- SUMO results are evidence about simulated traces, not direct evidence about physical intersections.
- The review assumes the arXiv PDF and HTML represent the same v2 paper; their identity and structure passed the local integrity checks.
- No claim is made that textual deliberation is causally faithful.
- No claim is made that a particular judge model is calibrated because its full identity and evaluation are incomplete.
- No source document, extracted source text, cache, render, receipt, or `.source/` directory is included in the deposit.
- Implementation proposals are limited to offline, synthetic, or human-supervised research settings.

## Observations

### The curator is part of the model

CuraLight's output quality depends on more than Gemma. The pressure heuristic, diffusion assistant, distributional critic, defender, consensus model, score mapping, curriculum, and negative-example objective jointly define the learning signal. Reproducing the backbone without this provenance would not reproduce the system.

### Disagreement can be evidence

The system combines RL and LLM judgments, but their raw difference can itself reveal uncertainty. A large gap may indicate an out-of-distribution traffic pattern, an LLM reasoning failure, a critic blind spot, or a score-calibration problem. Preserving the separate scores creates a more useful audit surface than only storing the final mixture.

### Metric tradeoffs should remain visible

JN2 shows that lower queue length need not coincide with the best travel or waiting time. A real controller would need explicit priorities, fairness constraints, emergency rules, and perhaps intersection-level tail metrics. A single average rank can conceal those policy choices.

### Hidden debate changes the governance problem

The consensus auxiliary field is intentionally hidden from direct quotation. That may prevent a downstream model from copying judge text, but it creates two evidence classes: what an operator sees and what the training pipeline uses. Retention, access, redaction, and incident reconstruction must be designed rather than assumed.

## Considerations

### Statistical evaluation

Future reports should include seeds, run counts, confidence intervals, paired tests, and raw per-run metrics. Traffic metrics are correlated and may have heavy tails; intersection-level and time-window distributions would be more informative than only network averages.

### Safety and fallback

An LLM-generated phase or duration must never bypass legal-movement constraints. A deployable controller needs a validated action schema, time budget, health checks, deterministic safe policy, conflict monitor, watchdog, operator override, and a path to revert without model availability.

### Feedback-loop governance

The same family of models can generate, defend, judge, and learn from trajectories. Versioned prompts, model identifiers, sampling settings, held-out judge audits, disagreement thresholds, and periodic human review are required to detect self-reinforcing errors.

### Reproducibility

Useful source release would include a locked environment, scenario manifests, preprocessing, seeds, prompts, judge snapshots, curation counts, mixture parameters, training schedules, checkpoints, and a script that regenerates each table. The existing code is a meaningful start but did not satisfy that end-to-end standard in this review.

### Deployment scope

Physical-road evidence should progress through offline replay, adversarial simulation, hardware-in-the-loop testing, shadow mode, controlled pilot, and monitored rollback. Cross-network simulation transfer is not a substitute for this sequence.

## Strengths

- Integrates topology-aware domain guidance rather than relying on unconstrained LLM action generation.
- Treats data quality and selection as first-class components of LLM controller training.
- Evaluates phase and green duration together across three cities and substantially different network sizes.
- Includes transfer and ablation evidence instead of only a single in-distribution benchmark.
- Discloses useful compute, throughput, memory, and paper-cited code information.
- Exposes multiple decision artifacts - proposals, critic scores, defender arguments, and consensus - that can support auditing if retained responsibly.

## Weaknesses

- Simulation-only evaluation leaves road safety, sensor noise, controller faults, and operator interaction untested.
- Missing dispersion and significance information prevents evaluation of ranking stability.
- Exact prompts, judge/model versions, data counts, important coefficients, seeds, and schedules are incomplete.
- The ablation does not fully isolate every curation and debate component.
- Transfer covers limited geographies and traces, and at least one target metric worsens.
- Textual rationales are treated as interpretability evidence without a direct faithfulness test.
- The paper-cited code lacks the documentation and environment lock needed for straightforward independent reproduction.

## Potential Improvements

- Publish a prespecified evaluation protocol with repeated seeds, run-level data, uncertainty intervals, paired tests, and multi-metric aggregation.
- Add incident, sensor-dropout, communication-loss, emergency-vehicle, pedestrian, and adversarial-prompt scenarios.
- Calibrate RL and LLM scores independently; report disagreement and add abstention rather than always averaging.
- Run factorial ablations for defender, consensus, negative training, curriculum order, mixture weight, and diffusion guidance.
- Release full provenance for prompts, model snapshots, trajectory counts, selection thresholds, manifests, seeds, and dependencies.
- Test explanation faithfulness by perturbing evidence, comparing stated reasons with causal action sensitivity, and measuring unsupported rationales.
- Measure end-to-end controller latency, deadline misses, fallback activations, and resource cost on hardware-in-the-loop infrastructure.

## Potential Implementations

### Offline Policy Audit Bench

Replay public or synthetic SUMO traces through a frozen controller. Save topology manifest, state hash, RL proposal, LLM candidate, separate critic scores, validated action, latency, fallback decision, and outcome metrics. Use the bench for regression and red-team testing, never for direct road control.

### Disagreement-Aware Curator

Build a curation service that calibrates RL and LLM judgments on held-out scenarios. Accept examples only when score provenance is complete and uncertainty is below threshold. Route large disagreement to an abstention pool for expert review instead of forcing a preference label.

### Topology Contract Adapter

Represent every intersection with a versioned schema for lanes, movements, phases, conflicts, duration bounds, and sensor validity. The LLM can reason over this normalized contract, while a deterministic validator rejects any action outside the manifest.

### Debate Evidence Store

Store candidate identifiers, public rationale, private auxiliary judgment, model and prompt versions, access class, and retention policy as separate fields. Authorized reviewers can reconstruct curation decisions without exposing infrastructure secrets or treating private reasoning as authoritative.

### Simulation Transfer Matrix

Evaluate train-city versus test-city combinations across network size, topology, demand, incidents, and sensor noise. Report all three traffic metrics plus tail behavior and failure rate, making negative transfer visible.

## Three Ways to Exercise This Research

1. **Reproduce the HZ2 ablation**: freeze one scenario manifest, training budget, seed set, and evaluation script; compare base Gemma, imitation, and full deliberation with run-level ATT, AQL, and AWT.
2. **Stress critic disagreement**: inject demand shocks, sensor dropouts, and altered phase constraints; measure whether RL-versus-LLM score gaps predict poor actions and whether abstention improves safety.
3. **Test topology transfer**: train on a small network, evaluate without adaptation across multiple larger public SUMO networks, and publish a full transfer matrix including negative results and deadline misses.

## Example MVP Product

### Name

CuraAudit

### Purpose

An offline workbench for auditing LLM-assisted traffic decisions against deterministic intersection constraints and separately calibrated RL and LLM critics.

### Primary User

A transportation-research engineer preparing a simulation study or reviewing a controller update before hardware-in-the-loop testing.

### Core Workflow

The user imports a public or synthetic SUMO scenario and a versioned intersection manifest. CuraAudit replays recorded states, obtains an RL reference and LLM candidate, validates the action, records critic disagreement, applies a safe fallback when needed, and produces a comparison report across traffic, latency, and failure metrics.

### Inputs

- SUMO network and route manifests with redistributable or synthetic data.
- Frozen controller and critic versions.
- Prompt template and public-safe model identifiers.
- Phase-conflict rules, duration bounds, latency budget, and fallback policy.
- Seed list and evaluation plan.

### Outputs

- Per-decision evidence receipts with state hashes rather than raw sensitive state.
- ATT, AQL, AWT, tail metrics, constraint violations, deadline misses, and fallback counts.
- RL-versus-LLM disagreement calibration plot and abstention analysis.
- Reproducible experiment manifest and human-readable review report.

### Guardrails

- Offline simulation only; no signal-controller or live road connection.
- Deterministic schema validation before every action.
- Fail closed on invalid phases, missing evidence, excessive disagreement, or deadline miss.
- Separate access controls for public rationale and private auxiliary judgments.
- No credentials, private infrastructure maps, or source documents in exported reports.
- Prominent statement that generated rationale is not guaranteed to be causally faithful.

### Evaluation Plan

Start with a fixed HZ2-like scenario and reproduce the three-stage ablation across at least five documented seeds. Add demand shocks, sensor dropouts, phase-manifest perturbations, and unavailable-model tests. Require zero accepted conflict violations, complete evidence receipts, deterministic fallback within the latency budget, and reported uncertainty for all traffic metrics. Then test transfer across several differently sized public networks.

### Deployment Boundary

The MVP stops at offline simulation reports. Hardware-in-the-loop, shadow operation, or physical deployment requires a separate safety case, transportation authority approval, secure infrastructure review, and monitored rollback plan.

### Why It Is Feasible

SUMO, structured intersection manifests, simple score calibration, and append-only evidence receipts are sufficient for a bounded prototype. The MVP does not require training a new foundation model or controlling real infrastructure.

## Related Research and Reading

### Black Lake DEP entries

- `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC/self_learned_idc_manuscript.md` - closest domain bridge for heterogeneous SUMO traffic control and the simulation-to-road boundary.
- `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md` - closest curation bridge for generator-judge feedback loops, preference evidence, and LoRA adaptation.
- `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md` - conceptual bridge for public, hidden, and runtime agent evidence; source-depth caveat retained.

### Paper context

- The CuraLight paper compares against LLMLight and UniTSA as traffic-controller baselines; their result rows are supporting context only and were not independently reviewed here.
- SUMO is the simulation substrate for all reported traffic evidence. Physical deployment behavior is outside this paper's evaluated scope.
- The paper-cited code repository is useful for mechanism inspection, but its existence does not substitute for a verified execution receipt.

## Source References

1. Qing Guo, Xinhang Li, Junyu Chen, Zheng Guo, Shengzhe Xu, Lin Zhang, and Lei Li. *CuraLight: Debate-Guided Data Curation for LLM-Centered Traffic Signal Control*. arXiv:2604.05663v2. https://arxiv.org/abs/2604.05663
2. Official arXiv PDF for arXiv:2604.05663. https://arxiv.org/pdf/2604.05663
3. Official arXiv full-paper HTML for arXiv:2604.05663. https://arxiv.org/html/2604.05663
4. Paper-cited CuraLight code repository. https://anonymous.4open.science/r/CuralightCode-6437/
5. DOI record for the arXiv work. https://doi.org/10.48550/arXiv.2604.05663

## Appendix

### Integrity Gate Summary

- Initial classification: partial because full-paper HTML was absent.
- Preserved PDF: 7,295,610 bytes; header and terminal marker valid; six parsed pages.
- Repaired full-paper HTML: 188,114 bytes; 34,193 body characters; full-document marker; 46 headings or sections; six structure terms.
- Metadata HTML: 43,015 bytes.
- Partials after repair: none.
- Final classification: complete and verified.
- Optional source package: not collected; PDF-plus-full-paper-HTML gate unaffected.

### Public-Output Allowlist

This deposit permits generated Markdown only: the Arxiv job log, Report-Mark, DEP README, manuscript, and publication index update. PDF, HTML, TeX/source archives, caches, extracted source text, renders, receipts, verification files, and `.source/` content are prohibited from staging and upload.

### Confidence Statement

Confidence is high for source identity, method transcription, tables, and local integrity. Confidence is medium for the interpretation that curation and debate jointly improve the controller because the ablation is limited. Confidence is low for independent reproducibility, statistical stability, rationale faithfulness, and physical-road readiness until stronger evidence is published.

## Attribution Block

- Source URL: https://arxiv.org/abs/2604.05663
  - Applies to: bibliographic identity, authors, version history, DOI, and public metadata.
  - Notes: `/abs/` is metadata only and was not treated as the full paper.
- Source URL: https://arxiv.org/pdf/2604.05663
  - Applies to: method, tables, figures, results, resource disclosures, and limitations.
  - Notes: complete PDF inspected from a verified private copy; source file withheld locally.
- Source URL: https://arxiv.org/html/2604.05663
  - Applies to: section, equation, and table cross-checking.
  - Notes: complete full-paper HTML inspected from a verified private copy; source file withheld locally.
- Source URL: https://anonymous.4open.science/r/CuralightCode-6437/
  - Applies to: bounded code, configuration, map, and entry-point observations.
  - Notes: no dependency installation, execution, or benchmark reproduction was claimed.
- Source file policy: no source file was uploaded, committed, copied into the DEP, or attached to Slack; no `.source/` directory was created.
