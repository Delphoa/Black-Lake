---
title: "Constrained Procedures - DEP-E"
generated_at: "2026-08-22T00:07:23Z"
artifact_type: "DEP research artifact"
primary_subject: "Evidence-grounded review of constrained procedure planning in instructional video, centered on CEFITO and expanded with the original Dual Dynamics Networks benchmark paper."
source_status: "URLs only; no source files collected"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-22"
temporal_cutoff: "2026-08-22"
primary_url: "https://arxiv.org/abs/2608.16457"
stable_identifier: "arXiv:2608.16457; DOI:10.1007/978-3-030-58621-8_20"
confidence_summary: "High for source identity and reported tables; medium for comparative interpretation; low for independent reproducibility because no code, data, or experiments were executed."
safety_scope: "research review, synthetic evaluation, and human-supervised planning support"
distribution_notes: "Derived review only; no paper PDFs, datasets, code, models, credentials, private data, or local execution details are redistributed."
---

# Constrained Procedures - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Repository-relative path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Contrastive Energy Fields for Inference-Time Procedure Planning in Instructional Videos | Primary research artifact | arXiv HTML and abstract record | arXiv:2608.16457v1, submitted 2026-08-17 | https://arxiv.org/abs/2608.16457; https://arxiv.org/html/2608.16457 | arXiv perpetual non-exclusive license shown on the HTML record; no source file redistributed | 2026-08-22 | Full HTML inspected |
| S2 | Procedure Planning in Instructional Videos | Newly inspected supporting research and direct baseline | ECCV 2020 paper, official PDF and landing page | DOI:10.1007/978-3-030-58621-8_20; arXiv:1907.01172 | https://doi.org/10.1007/978-3-030-58621-8_20; https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/1340_ECCV_2020_paper.php; https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123560324.pdf; https://arxiv.org/abs/1907.01172 | Official ECVA paper inspected by URL; no PDF collected or redistributed | 2026-08-22 | Complete 16-page paper text, tables, methods, results, and conclusion inspected; visual screenshot retrieval failed with a cache miss |
| S3 | Selected source DEP | Provenance record and deposited finding | Repository Markdown | DEP-20260819-Research Data 2234 D0396 | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260819-Research%20Data%202234%20D0396 | Repository evidence; source files not copied | 2026-08-22 | README, finding, and Report-Mark001 inspected |
| S4 | Prior Contrastive Energy DEP-E | Previous manuscript and attribution context | Repository Markdown | DEP-E-20260820-Contrastive-Energy-D0EE, Series 002 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260820-Contrastive-Energy-D0EE | Prior generated review, not independent evidence | 2026-08-22 | README and manuscript inspected |
| S5 | Prior review log and source report | Iteration and question history | Repository Markdown | 2026-08-20 processing pass | https://github.com/Delphoa/Black-Lake/blob/main/.logs/20260820-DEP-20260819-Research%20Data%202234%20D0396-LOG.md; https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.reports/Series/AA/AA/00/00/AA-AA00-0000/BL-DEP-20260819-Research%20Data%202234%20D0396-20260820 | Operational provenance only | 2026-08-22 | Inspected |

No external source file was collected. The CEFITO project locator at `https://visinf.github.io/cefito` was present in the paper but could not be opened through the available web surface, and no dedicated CEFITO code repository was verified. That locator is therefore discovery-only, not implementation evidence.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, arXiv abstract and Sections 1-3 | Primary preprint | Problem definition, action-conditioned predictor, triplet contrastive objective, mixed hard/easy negatives, and task-constrained inference | C1, C2 | High for described method; medium for efficacy | Author-reported v1 preprint; no code or execution inspected |
| E2 | S1, Tables 1-7 and Sections 4-5 | Primary preprint | CrossTask/COIN metrics, five-seed protocol, ablations, oracle classifier analysis, runtime scaling, and failed NIV experiment | C2, C3, C4 | High for table transcription; medium for generalization | Results were not recomputed; benchmark implementations were not audited |
| E3 | S2, Sections 1-3 | Peer-reviewed conference paper | Original task formulation, latent state/action mappings, forward dynamics, conjugate dynamics, and priority-queue planning | C1, C5 | High | 2020 method assumes a fixed horizon and supervised action segmentation |
| E4 | S2, Tables 1-2 and Sections 4-5 | Peer-reviewed conference paper | CrossTask scale, training setup, DDN baselines, low absolute success rates, walkthrough metrics, qualitative failure, and future work | C3, C5, C6 | High for reported results | No environment execution; exact-sequence success is only a proxy for executable plans |
| E5 | S3 | Repository provenance | Original deposited locator, source boundary, and prior Report-Mark sections | Provenance and iteration status | High for repository state | Generated finding contains a truncated abstract recap and is not independent validation |
| E6 | S4-S5 | Prior generated review and process records | Previous evidence gaps, unreviewed DOI pool, and next-review questions | Expansion selection and continuity | High for process history; low as scientific evidence | Prior manuscript was generic and did not substantively inspect DDN |

## Executive Summary

CEFITO reframes fixed-horizon procedure planning from direct sequence prediction into energy minimization over candidate action sequences. It learns a predictor that maps an initial state and candidate sequence toward a goal embedding, trains that representation with positive and mixed hard/easy negative sequences, and limits inference to actions associated with a predicted high-level task [E1]. On the authors' five-seed CrossTask protocol, CEFITO reports 39.62% success rate for horizon 3 and 24.76% for horizon 4, compared with 38.45% and 24.64% for ViterbiPlanNet. On COIN, the corresponding success-rate margins over ViterbiPlanNet are only 0.12 and 0.33 percentage points [E2]. These are benchmark improvements, not evidence that the produced plans are physically executable.

This pass adds a complete review of the randomly selected supporting source, Chang et al.'s ECCV 2020 paper *Procedure Planning in Instructional Videos*. That work introduced the task and Dual Dynamics Networks (DDN): a latent forward dynamics model paired with a conjugate dynamics model that predicts applicable actions [E3]. DDN's original CrossTask success rates were 12.18% at horizon 3 and 5.97% at horizon 4, despite outperforming its contemporaneous baselines; the authors explicitly noted low absolute exact-sequence success and reported a visual failure caused by missing the cue that a tool was already in hand [E4].

Reviewer interpretation: DDN and CEFITO share a durable insight—planning improves when the action space is structured by task and state constraints instead of treating all actions as equally plausible. CEFITO modernizes the mechanism and raises closed-benchmark scores, but it does not remove the underlying dependency on a predefined action vocabulary, known horizon, task classification, and sufficient same-task training density. Its own evidence shows exponential search growth, roughly one-order-of-magnitude slowdown versus PDPP at horizon 5 and two orders at horizon 6, and suboptimal performance on the 150-video NIV benchmark [E2]. Confidence is therefore high that constrained action reasoning is useful under the evaluated protocols, medium that the specific CEFITO design is robust across CrossTask and COIN, and low for open-world, long-horizon, or embodied deployment without independent reproduction.

## Detailed Summary

### Problem and lineage

Both papers define procedure planning as selecting a fixed-length action sequence that connects a visual start observation to a visual goal. DDN introduced this benchmark formulation for instructional videos and learned a plannable latent state/action space from CrossTask. CEFITO retains the start/goal/horizon setup but asks whether a learned energy can score complete candidate sequences while a task constraint removes irrelevant actions [E1, E3]. The expansion therefore traces a direct lineage rather than a loose thematic similarity: CEFITO cites DDN as the originating paper and evaluates DDN in its CrossTask comparison.

### DDN: dual latent dynamics

DDN maps an observation `o` to a latent state `x=f(o)` and an action `a` to a latent action `g(a)`. Its forward model predicts the next latent state from the current state and action. Its conjugate model uses the current or predicted state plus action history to predict which action is applicable next. The two are jointly optimized with `L = alpha * L_T + L_P`, intended to prevent trivial latent mappings and inject the relationship between state transitions and action preconditions [E3].

At inference, DDN encodes the start and goal, samples candidate applicable actions from the conjugate model, advances states with the forward model, and retains a bounded priority queue ordered by latent distance to the goal. This is a learned, beam-like search over discrete actions. The same learned states are also evaluated in walkthrough planning by ordering intermediate clips between fixed endpoints [E3, E4].

The DDN evaluation adapts 2,750 CrossTask videos (212 hours, 18 tasks, 105 action classes) with manually annotated temporal boundaries and action labels. It uses a 70/30 train/test split, 3,200-dimensional precomputed visual/audio features, 128-dimensional state and action embeddings, 200 training epochs, and one GTX 1080 Ti. The paper says full supervision is required and leaves unlabeled-video use to future work [E4].

For horizon 3, DDN reports 12.18% exact-sequence success, 31.29% action accuracy, and 47.48% mIoU; at horizon 4 it reports 5.97%, 27.10%, and 48.46%. UPN, the closest listed latent-planning baseline, reports 2.89% and 1.19% success at those horizons. Removing the conjugate dynamics collapses exact-sequence success below 0.01%, while removing the forward model yields 1.55% and 0.65%, supporting the authors' claim that both components matter in their setup [E4]. For walkthrough planning, full DDN reports pairwise accuracy of 86.81% at horizon 3 and 81.21% at horizon 4, above Causal InfoGAN's 71.55% and 68.41% [E4].

### CEFITO: contrastive energy and constrained search

CEFITO encodes start and goal frames, then learns a predictor `P_theta` whose output for the start plus an action sequence should be close to the goal embedding for a correct sequence and farther away for incorrect ones. Its triplet-style objective uses an adaptive margin. Negatives mix same-task sequences with changed order or composition (hard negatives) and sequences from other tasks (easy negatives), providing both local ordering and task-level discrimination [E1].

At inference, a task classifier predicts the high-level task. The candidate action vocabulary is reduced to the subset observed for that task in training, and the selected sequence minimizes distance between the predictor output and the goal embedding. This omits irrelevant actions explicitly but makes classifier quality a hard dependency: the paper states that an incorrect task prediction always yields a wrong sequence [E1, E2].

CEFITO evaluates CrossTask (2,750 videos, 18 tasks, 105 actions) and COIN (11,827 videos, 180 tasks, 778 actions). It trains five seeds and reports means with 90% confidence intervals. Metrics are exact-sequence success rate, stepwise mean accuracy, and element-wise mean IoU [E2]. On CrossTask at horizon 3, it reports 39.62±0.24 SR, 64.12±0.31 mAcc, and 84.29±0.21 mIoU. At horizon 4 it reports 24.76±0.43, 57.53±0.37, and 81.58±0.25. The corresponding ViterbiPlanNet results are 38.45±0.32 and 24.64±0.30 SR, so the strict-metric margin is meaningful but small [E2].

On COIN, CEFITO reports 34.11 SR at horizon 3 and 24.25 at horizon 4 versus ViterbiPlanNet's 33.99 and 23.92. The authors attribute the smaller gain to COIN's wider 180-task distribution, which supplies fewer examples per task and weakens intra-task negative sampling [E2]. The training ablation is more diagnostic: a plain regression baseline scores 13.65 SR at CrossTask horizon 3; adding triplet contrastive loss raises it to 37.58, the adaptive margin to 38.74, and auxiliary regularization to 39.62. This supports the contrastive-training mechanism within the authors' implementation [E2].

### Boundary evidence

CEFITO's task classifier scores above 90% on CrossTask but 79.42% on COIN; the authors say classifier mistakes cause wrong sequence predictions in about 20% of COIN validation examples. Ground-truth task labels improve COIN horizon-3 SR from 34.11 to 38.33 and horizon-4 SR from 24.25 to 29.51 [E2]. Constraint quality is therefore part of the planner, not a detachable preprocessing detail.

Search complexity grows exponentially with horizon. The paper reports comparable inference time to feed-forward and diffusion approaches through horizon 4, approximately ten-times PDPP runtime at horizon 5, and approximately one-hundred-times at horizon 6. Its failed NIV experiment is also important negative evidence: CEFITO records 22.46 SR at horizon 3 and 19.67 at horizon 4, below ViterbiPlanNet's 32.37 and 27.54. The authors suspect contrastive learning collapses because NIV has only 150 videos, far less than CrossTask or COIN [E2].

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Procedure planning benefits from representing action applicability and task structure rather than treating every discrete action as equally plausible. | Cross-paper author claim and reviewer synthesis | E1, E3 | Supported within both papers' fixed-horizon benchmark settings; not established for open action spaces. | Medium-high |
| C2 | CEFITO's contrastive predictor plus task-constrained optimization improves the reported CrossTask and COIN metrics. | Author claim / benchmark result | E1, E2 | Tables support best reported means under the unified protocol, but strict-success margins over the strongest baseline are small. | High for transcription; medium for broader significance |
| C3 | Closed-benchmark accuracy does not establish executable real-world plans. | Reviewer interpretation | E2, E4 | DDN evaluates exact label matching without environment execution; CEFITO likewise reports sequence-label metrics. | High |
| C4 | CEFITO is limited by classifier errors, exponentially growing search, and low-data failure. | Author-disclosed limitation | E2 | Directly supported by oracle, runtime, and NIV results. | High |
| C5 | DDN's forward and conjugate dynamics jointly improve latent procedure planning over its ablations and contemporaneous baselines. | Author claim / benchmark result | E3, E4 | Table 1 strongly supports the within-paper ablation claim, though absolute exact-sequence success remains low. | High |
| C6 | The most useful next test is a matched, independently implemented comparison that varies task-vocabulary noise, horizon, and data density. | Reviewer recommendation | E2, E4 | Directly targets the failure surfaces exposed by both papers. | Medium-high |

## Methodology

- `Research objective`: Extend the prior DEP-E review by inspecting one randomly selected, previously unreviewed supporting source and using it to assess the lineage, mechanism, evidence, and limits of constrained procedure planning.
- `Sources inspected`: All three selected-DEP Markdown files; the prior source report, output log, DEP-E README, and manuscript; CEFITO arXiv v1 full HTML; the complete official ECVA DDN paper text, methods, tables, results, qualitative failure, and conclusion; canonical arXiv, DOI, ECVA, and author publication records.
- `Discovery strategy`: Repository-first inventory and prior-marker review, extraction of the three unreviewed DOI items in the prior Related Research and Reading section, a cryptographic random draw over that stable pool, DOI/title resolution, citation chasing from CEFITO, and primary-source inspection.
- `Inclusion criteria`: Primary or near-primary sources directly tied to the selected DEP, prior artifact, or randomly selected expansion thread; tables and sections necessary to evaluate central mechanisms and boundary conditions.
- `Exclusion criteria`: Secondary summaries as claim evidence, papers merely cited but not inspected, inaccessible project content, and any implementation or availability claim not verified from a source surface.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product research, safety/ethics, and replication analysis.
- `Evidence handling`: Major claims are mapped to evidence IDs; author claims, benchmark results, reviewer interpretation, and negative evidence are distinguished explicitly.
- `Uncertainty handling`: No result is treated as reproduced; unavailable code, uncollected datasets, project-page access failure, version uncertainty, and the difference between label matching and physical executability remain visible.
- `Extraction process`: Repository Markdown was read directly. Web evidence was read from arXiv HTML and ECVA's parsed official PDF. Visual screenshot retrieval for selected PDF pages was attempted and failed with a cache miss, so figure-level claims were limited to captions and extracted text.
- `Version control`: CEFITO was inspected as arXiv v1 dated 2026-08-17; DDN was inspected as the ECCV 2020 paper tied to DOI `10.1007/978-3-030-58621-8_20` and arXiv `1907.01172`.
- `Reviewer stance`: Comparative manuscript review, iterative literature expansion, DEP-ready preservation, and bounded product/replication translation.

## Scope, Constraints, and Assumptions

- `Scope`: Two substantive papers—CEFITO and the randomly selected DDN baseline—plus the selected DEP and prior review lineage.
- `Temporal boundary`: Sources accessed on 2026-08-22; later CEFITO revisions, releases, or venue versions may differ.
- `Evidence limits`: No repository implementation for CEFITO was verified, no code or dataset was downloaded, and no experiment, statistical calculation, model inference, or robot/environment execution was performed.
- `Assumptions`: The official arXiv and ECVA surfaces accurately represent the cited versions; parsed table values reflect the source documents.
- `Constraints`: Public-source access, redistribution restrictions, compute limits, privacy, safe-use boundaries, and public-output sanitization.
- `Out of scope`: Physical task execution, autonomous control, safety certification, production deployment, exhaustive literature review, dataset-license audit, and conclusions about human cognitive planning.
- `Intended use`: DEP deposition, research triage, evaluation design, benchmark interpretation, and human-supervised implementation planning.
- `Audience`: Computer-vision, planning, evaluation, and product-assurance researchers.
- `Reproducibility boundary`: Source identity and table transcription are reviewable from public links; performance and runtime claims are not independently reproduced.
- `Operational boundary`: Concepts may inform synthetic or offline planning tools, but this artifact does not authorize autonomous actuation or safety-critical decisions.
- `Data sensitivity`: Public paper and repository metadata only.

## Observations

- `Observed pattern`: The field moved from learning applicable-action dynamics (DDN) to learning a sequence-level energy plus explicit task restriction (CEFITO), while keeping the same fixed-horizon, predefined-action benchmark core.
- `Technical implication`: Task constraints reduce combinatorial waste, but their errors become planner errors. Constraint recall should therefore be measured alongside plan accuracy.
- `Observed pattern`: CEFITO's large improvement over its regression ablation is much bigger than its improvement over the strongest modern baseline, suggesting the objective is important but not alone sufficient to explain state-of-the-art performance.
- `Contradiction or tension`: CEFITO markets inference-time optimization as flexible reasoning, yet its exhaustive discrete search becomes dramatically slower beyond horizon 4.
- `Observed negative evidence`: NIV reverses the headline ranking; low per-task data may undermine the contrastive energy's separation.
- `Reviewer hypothesis`: A hybrid planner that uses learned constraints for pruning but preserves a recoverable fallback outside the predicted task subset could trade a small runtime increase for greater robustness to classifier error. This is an inference, not a tested result.

## Considerations

- Evaluate constraint precision and recall, not only final sequence accuracy. An omitted valid action can make the true plan unreachable.
- Separate exact label matching from semantic acceptability and physical executability. Multiple valid procedures may exist even when a benchmark supplies one sequence.
- Report performance as a function of horizon, task count, videos per task, action-vocabulary size, and classifier confidence.
- Benchmark approximate search against exhaustive search with identical predictors, hardware, and stopping criteria.
- Audit CrossTask/COIN licenses, splits, feature provenance, annotation assumptions, and leakage risks before reproduction or redistribution.
- Keep autonomous or safety-critical actuation out of the MVP. Human review and offline/synthetic evaluation are necessary because instructional videos do not expose full physical state, hazards, or object affordances.
- Monitor model revisions and project releases. The inspected CEFITO version is recent v1 preprint evidence and may change.

## Strengths

- CEFITO exposes a clear energy-minimization formulation and reports five-seed means with 90% confidence intervals.
- Its ablations connect the major gain to contrastive sequence training, then quantify smaller contributions from adaptive margins and auxiliary reconstruction.
- It publishes meaningful negative evidence: classifier-induced failures, long-horizon runtime escalation, and a failed low-data benchmark.
- DDN supplies an explicit model of state/action conjugacy and strong component ablations for the original benchmark setting.
- The paired review clarifies technical lineage and prevents the latest benchmark result from erasing the original task assumptions.

## Weaknesses

- Neither inspected paper validates plans by executing them in an underlying environment; sequence-label metrics are proxies.
- Both assume a known horizon and a predefined action vocabulary, limiting open-world transfer.
- CEFITO's strict-success improvements over the strongest reported baselines are small on CrossTask and COIN.
- CEFITO's exhaustive search scales poorly; approximate search is proposed but not established in the inspected evidence.
- CEFITO depends on task classification, and the paper reports that classifier errors explain about 20% of COIN validation failures.
- DDN requires full temporal/action supervision, uses a single CrossTask split and older feature pipeline, and reports low absolute exact-sequence success.
- No CEFITO code repository, dataset snapshot, dependency lock, or release hash was verified in this pass.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add constraint-recall recovery | Robustness | A wrong task prediction removes valid actions. | Reduces catastrophic false pruning. | Larger search and possible irrelevant actions. | Inject task-label noise and measure recovery/latency curves. |
| Compare exact and approximate search | Efficiency | Exhaustive search grows exponentially with horizon. | Establishes a usable accuracy-latency frontier. | Beam heuristics may miss the optimum. | Matched predictor, hardware, seeds, and horizons 3-8. |
| Vary examples per task | Data efficiency | NIV suggests contrastive collapse in low-data regimes. | Identifies minimum useful task density. | Requires controlled resampling. | Learning curves with fixed vocabulary and repeated seeds. |
| Add multi-valid-plan evaluation | Metric validity | Exact matching penalizes valid alternatives. | Better alignment with procedural utility. | Requires new annotations or simulators. | Human adjudication plus environment/symbolic feasibility checks. |
| Publish a pinned reproduction bundle | Reproducibility | Current public evidence does not verify executable code or artifacts. | Enables independent benchmark replay. | Licensing, storage, and maintenance burden. | Clean-environment reproduction with hashes and expected outputs. |
| Test open-action and unseen-task settings | Generalization | Both methods assume closed task/action sets. | Measures transfer beyond benchmark memorization. | Harder evaluation and ambiguous labels. | Base/novel task splits with explicit constraint-recall metrics. |

## Potential Implementations

1. `Offline procedure-plan auditor`: User - benchmark maintainers and research engineers. Goal - diagnose why a predicted sequence failed. Core mechanism - score candidate sequences, visualize excluded actions, and trace task-classifier confidence. Required inputs - public benchmark labels, model scores, and synthetic or authorized videos. Outputs - constraint audit, ranked alternatives, and failure taxonomy. Risk controls - no autonomous actuation, no raw private-video logging, visible confidence, and human review. Evaluation - reproduce known classifier, ordering, and horizon failures.
2. `Matched search benchmark`: User - planning researchers. Goal - compare exhaustive, beam, and fallback search fairly. Core mechanism - freeze one predictor and vary only the search policy. Required inputs - pinned model outputs and public/synthetic action graphs. Outputs - success, recall, latency, forward-pass counts, and failure traces. Risk controls - resource caps, deterministic seeds, and no production-control interface. Evaluation - horizon and vocabulary sweeps with identical hardware.
3. `Human-supervised instructional assistant`: User - a trained operator reviewing a public or explicitly authorized procedure. Goal - propose high-level next-step alternatives with evidence. Core mechanism - retrieve a task vocabulary, generate a short candidate plan, and require confirmation at every step. Required inputs - approved procedure library and non-sensitive observations. Outputs - suggestions and uncertainty warnings. Risk controls - read-only recommendations, stop conditions, hazard filters, and no medical, industrial, or robotic autonomy. Evaluation - expert review of plan validity and false-omission rates.

## Three Ways to Exercise This Research

1. `Constraint-noise audit`: Objective - test whether a planner can recover when the predicted task subset omits the correct action. Inputs - a toy action vocabulary, synthetic start/goal pairs, and controlled task-label noise. Method - compare strict pruning with a confidence-triggered fallback. Output - constraint-recall and plan-success curves. Success criterion - recovery improves without unbounded search. Safety boundary and stop condition - use synthetic data only and stop if runtime exceeds the preset cap.
2. `Horizon scaling replay`: Objective - measure the accuracy-latency tradeoff from horizon 3 through 8. Inputs - frozen synthetic energy scores and identical action subsets. Method - run exhaustive search, fixed-width beam search, and a bounded hybrid under one resource budget. Output - forward-pass, latency, and optimum-recovery tables. Success criterion - identify a policy that preserves most optimum plans under the cap. Safety boundary and stop condition - no autonomous environment; stop at the fixed compute budget.
3. `Metric validity review`: Objective - distinguish exact-match failure from semantically valid alternative procedures. Inputs - a small public procedure set with two or more expert-approved sequences per task. Method - score exact match, step accuracy, set overlap, ordering constraints, and expert feasibility separately. Output - an annotated disagreement matrix. Success criterion - every metric failure is attributable to order, omission, substitution, or invalidity. Safety boundary and stop condition - human-reviewed offline analysis only; stop before real-world execution.

## Example MVP Product

- `Product name`: Procedure Constraint Auditor
- `Target user`: Computer-vision and planning research teams evaluating procedure models.
- `Problem`: Aggregate plan scores hide whether failure came from task classification, action pruning, ordering, horizon assumptions, or the evaluation metric.
- `Core workflow`: Import a public/synthetic benchmark case; register the task vocabulary and predictor scores; display included and excluded actions; compare exact, beam, and fallback searches; export a source-linked audit report.
- `Data requirements`: Public or explicitly authorized benchmark labels, synthetic state/action records, model score tables, and versioned configuration. Raw personal video is excluded from the MVP.
- `Architecture`: Local-first CLI plus static web report; immutable JSON case bundle; deterministic search runners; metric module; provenance and schema validator.
- `Success metrics`: 100% traceability from reported failures to an input case; reproducible search outputs; constraint recall reported with plan accuracy; zero sensitive-data or local-system leaks; bounded runtime.
- `Risk controls`: No actuator interface, no automatic operational approval, local-only processing, explicit uncertainty, allowlisted inputs, resource caps, and human sign-off.
- `Limitations`: The MVP audits supplied scores and labels; it does not prove physical executability, recover missing state, or validate a paper's training pipeline.
- `MVP boundary`: Offline analysis of public or synthetic fixed-horizon procedures only.
- `Deployment model`: Local CLI and static Markdown/HTML bundle.
- `Evaluation plan`: Golden toy cases for omission/order failures, regression tests for search policies, reviewer agreement checks, and a leak-pattern sanitization gate.
- `Failure modes`: Incorrect task vocabulary, stale model scores, hidden multi-valid-plan ambiguity, metric misuse, and false confidence from a clean visualization.
- `Maintenance plan`: Version benchmark schemas, pin dependencies, retain correction history, and require review when metrics or search policies change.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Contrastive Energy Fields for Inference-Time Procedure Planning in Instructional Videos | Primary research thread | Primary work selected from the source DEP; full arXiv v1 HTML was inspected in this pass. | https://arxiv.org/abs/2608.16457 |
| Official CEFITO full-text representation | Primary source format | Provides the method, benchmark tables, ablations, runtime limits, failed NIV experiment, and conclusion. | https://arxiv.org/html/2608.16457 |
| **New in this pass: Procedure Planning in Instructional Videos** | Direct baseline and task-origin paper | Randomly selected prior related-reading item; the complete official ECCV paper was inspected to recover DDN's mechanism, benchmark setup, results, and limitations. | https://doi.org/10.1007/978-3-030-58621-8_20 |
| Official DDN conference paper | Primary full text | Official ECVA PDF for the newly expanded source. | https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123560324.pdf |
| Selected source DEP | Provenance record | Preserves the deposited finding and the prior Report-Mark used to route this iterative pass. | https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260819-Research%20Data%202234%20D0396 |
| Prior Contrastive Energy DEP-E | Prior review | Supplies the earlier evidence ledger, open questions, and three-item expansion pool. | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260820-Contrastive-Energy-D0EE |
| Model Predictive Control | Uninspected related locator retained from the prior manuscript | Connects constrained optimization and receding-horizon control; not independently inspected in this pass. | https://doi.org/10.1007/978-0-85729-398-5 |
| Planning as Inference | Uninspected related locator retained from the prior manuscript | Conceptual planning-as-inference context; not independently inspected in this pass. | https://doi.org/10.1016/j.tics.2012.08.006 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2608.16457 | CEFITO title, authors, arXiv identifier, date, abstract, and v1 status | 2026-08-22 | Primary record inspected |
| R2 | https://arxiv.org/html/2608.16457 | CEFITO method, equations, datasets, Tables 1-7, ablations, limitations, references, and conclusion | 2026-08-22 | Complete HTML inspected |
| R3 | https://export.arxiv.org/api/query?id_list=2608.16457 | Canonical Atom metadata retained from the prior pass | 2026-08-20 | Prior official metadata source; not needed for new claims |
| R4 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260819-Research%20Data%202234%20D0396/dep0396_research_findings_2026-08-19_2234.md | Selected finding and primary locator | 2026-08-22 | Repository file inspected; not collected |
| R5 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/Series/AA/AA/00/00/AA-AA00-0000/DEP-20260819-Research%20Data%202234%20D0396/README.md | Source inventory, attribution, and collection boundary | 2026-08-22 | Repository file inspected; not collected |
| R6 | https://doi.org/10.1007/978-3-030-58621-8_20 | Canonical DOI for the newly expanded DDN paper | 2026-08-22 | DOI resolution was unreliable in the web surface; identity was cross-checked through CEFITO, ECVA, arXiv, and author records |
| R7 | https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/1340_ECCV_2020_paper.php | DDN title, authors, venue, abstract, and official PDF link | 2026-08-22 | Official ECCV/ECVA landing page inspected |
| R8 | https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123560324.pdf | DDN full method, CrossTask setup, Tables 1-2, qualitative failure, limitations, and conclusion | 2026-08-22 | Complete 16-page official paper text inspected; no file collected |
| R9 | https://arxiv.org/abs/1907.01172 | DDN canonical preprint identity and abstract | 2026-08-22 | Primary record inspected |
| R10 | https://www.niebles.net/publications/ | DDN author, ECCV 2020 venue, and DOI cross-check | 2026-08-22 | Author publication record inspected |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.logs/20260820-DEP-20260819-Research%20Data%202234%20D0396-LOG.md | Prior questions, challenges, and expansion history | 2026-08-22 | Process provenance only |
| R12 | https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260820-Contrastive-Energy-D0EE | Prior manuscript and related-reading pool | 2026-08-22 | Generated review; not independent scientific evidence |

## Appendix

### Selection and iterative expansion provenance

- Automation: `Black-Lake Data Processing & Review 0900`.
- Canonical family marker: `automation_family_id=black-lake-data-processing-review-v1`.
- Selection run: 5,522 canonical candidates; 2 excluded by source/output markers within the preceding 24 hours; 5,520 metadata-eligible; 1 additional identity held by another active family reservation.
- Eligibility cutoff (UTC): `2026-08-21T00:07:23Z`.
- Reserved source: `Black-Lake-Data/.lake-data/DEP-20260819-Research Data 2234 D0396`.
- Source selection method: system-cryptographic random choice from the atomically locked available set; the helper exposed no raw random word, so none is fabricated here.
- Iterative status: prior source report, output log, DEP-E artifact, and Report-Mark001 were found and were older than 24 hours.
- Supporting pool: three unreviewed DOI items preserved by Report-Mark001.
- Supporting-source draw: Python `secrets.randbelow`, selected zero-based index `1` of `3`; pool SHA-256 `c773860e5bfa1d08bd992d427415fd7ee92cf9cfa809d238c6bac70c3bc50312`.
- Newly expanded thread: `https://doi.org/10.1007/978-3-030-58621-8_20`.

### Source inventory and validation boundary

- Inspected repository files: the selected DEP's `README.md`, generated finding, Report-Mark001, matching 2026-08-20 source report, prior Black-Lake log, prior DEP-E README, and prior manuscript.
- Inspected external sources: complete CEFITO arXiv v1 HTML; complete DDN official ECVA paper text; canonical arXiv, ECVA, DOI, and author publication records.
- Source files collected: none.
- Not executed: code, model, dataset, benchmark pipeline, statistical recomputation, simulator, robot, or real-world procedure.
- Remaining gaps: CEFITO code/release availability, dataset and feature licenses, independent five-seed replay, matched hardware runtime, approximate-search validation, multi-valid-plan annotations, and open-world/embodied transfer.
