---
title: "Shuffled Autoregression - DEP-E"
generated_at: "2026-07-24 (date only; exact execution time withheld)"
artifact_type: "DEP research artifact and paper report"
primary_subject: "Source-grounded review of dependency-ordered autoregression for human-motion interpolation."
source_status: "complete verified local source bundle; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-24"
temporal_cutoff: "Paper v1 and public context inspected through 2026-07-24"
primary_url: "https://arxiv.org/abs/2306.06367v1"
stable_identifier: "arXiv:2306.06367v1; DOI:10.48550/arXiv.2306.06367; IEEE DOI:10.1109/ICASSP49357.2023.10095312"
confidence_summary: "High for identity, mechanism, and transcribed table values; medium for causal attribution and transfer because experiments were not reproduced."
safety_scope: "research review, synthetic evaluation, and non-consequential implementation planning"
distribution_notes: "Generated Markdown only; PDF, HTML, source package, renders, caches, extraction text, and verification records remain local."
---

# Shuffled Autoregression - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract record | Canonical metadata | HTML | 2306.06367v1 | https://arxiv.org/abs/2306.06367v1 | Metadata only; not used as full-paper evidence | 2026-07-24 | Inspected |
| S2 | arXiv paper | Primary artifact | PDF | 2306.06367v1; 2,310,025 bytes; five pages | https://arxiv.org/pdf/2306.06367 | arXiv distribution record visible; redistribution not assumed | 2026-07-24 | Complete, rendered, and inspected |
| S3 | ar5iv full-paper conversion | Searchable primary representation | HTML | 189,178 bytes; approved fallback | https://ar5iv.labs.arxiv.org/html/2306.06367 | Converted public representation; verified beyond abstract-only content | 2026-07-24 | Complete and inspected |
| S4 | arXiv source package | Primary source structure | TeX/source archive | 2,641,656 bytes | https://arxiv.org/e-print/2306.06367 | Withheld locally; no redistribution | 2026-07-24 | Collected and inventoried |
| S5 | arXiv DOI | Persistent metadata | DOI | 10.48550/arXiv.2306.06367 | https://doi.org/10.48550/arXiv.2306.06367 | Persistent locator | 2026-07-24 | Inspected |
| S6 | IEEE ICASSP record | Publisher context | DOI | 10.1109/ICASSP49357.2023.10095312 | https://doi.org/10.1109/ICASSP49357.2023.10095312 | Publisher locator | 2026-07-24 | Resolved by identifier |
| S7 | ICASSP 2023 program | Venue context | HTML | ICASSP 2023 | https://icassp23-static-program.pages.dev/ | Official conference program | 2026-07-24 | Inspected |
| S8 | Tsinghua HCSI publication page | Author context | HTML | ICASSP 2023 listing | https://hcsi.cs.tsinghua.edu.cn/ | Author-maintained publication listing | 2026-07-24 | Inspected |
| S9 | AR-Drag Motion Control | Related DEP | Markdown | DEP-E-20260720 | `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` | Repository-relative synthesis | 2026-07-24 | Inspected |
| S10 | Structured Thoughts | Related DEP | Markdown | DEP-A-20260715 | `.lake-data/DEP-A/DEP-A-20260715-Structured Thoughts/2607.10386-whitepaper-review.md` | Repository-relative synthesis | 2026-07-24 | Inspected |
| S11 | InterDance Reactive 3D Dance | Related DEP | Markdown | DEP-E-20260723 | `.lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md` | Repository-relative synthesis | 2026-07-24 | Inspected |

- **Paper title:** *Shuffled Autoregression For Motion Interpolation*
- **Authors:** Shuo Huang; Jia Jia; Zongxin Yang; Wei Wang; Haozhe Wu; Yi Yang; Junliang Xing
- **Venue and date:** IEEE ICASSP 2023; arXiv v1 submitted 2023-06-10
- **Subjects:** Computer Vision and Pattern Recognition; Artificial Intelligence
- **Public implementation status:** No official code repository was established by the inspected author page or an exact-name GitHub repository search. This is negative discovery evidence, not proof that no implementation exists.
- **Local source policy:** Complete PDF, full-paper HTML, metadata HTML, source archive, rendered pages, extraction caches, provenance, and verification records were inspected privately and withheld from publication.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5-S8 | Official and author metadata | Identity, author set, submission date, venue, subject classes, and DOI locators | Source identity and publication context | High | Publisher page text was not used for technical claims |
| E2 | S2-S4 | Complete primary paper | Problem formulation, SAR equations, DAG semantics, FDAM construction, three-stage pipeline, architecture, and training | Method description | High | Implementation was not executed |
| E3 | S2-S4 | Complete primary paper | AMASS/SMPL+H corpus construction, 166,696 windows, approximate 70/10/20 split, model dimensions, and keyframe indices | Experimental setup | High for transcription | Split granularity, subjects, seeds, and preprocessing manifest are incomplete |
| E4 | S2-S4 | Table 1 and results prose | Full-model MPJAE `0.0102`, MPJPE `0.0365`, Neighbor-L2 delta `-1.0368`, and NPSS `0.089` | Main quantitative result | High for table transcription | Results were not reproduced; Neighbor-L2 semantics are ambiguous |
| E5 | S2-S4 | Table 1 ablation and Section 4.4 | Original AR `0.1847/0.3461/89.395/6.594`; binary search `0.0152/0.0584/1.3489/0.107`; no smoothing `0.0121/0.0387/2.0001/0.096` | Topology and smoothing ablations | High for table transcription | One run/setting; no uncertainty or matched compute report |
| E6 | S2-S4 | Section 4.3 and Figure 3 | One representative sequence selected from 20 test samples; source-described qualitative defects | Qualitative evidence and boundary | High for source description | Not blinded, randomized, or a human preference study |
| E7 | S2-S4 | Table caption, metric definition, and row values | Neighbor-L2 is described as closeness to ground truth while signed deltas and “lower is better” language coexist | Metric ambiguity | High | No safe basis for a guessed correction |
| E8 | S2-S4 | Conclusion and contribution claims | Claimed extensibility to multiple keyframes and other interpolation domains | Transfer claim | High that the claim exists | No direct experiment supports the extension |
| E9 | S9 | Related DEP manuscript | AR-Drag uses inference-aligned generated history and studies autoregressive motion/video error | Cross-DEP mechanism bridge | Medium-high | Different model, modality, data, and evaluation |
| E10 | S10 | Related DEP review | Structured Thoughts compiles semantic state lifetimes into a custom attention visibility mask and runtime deletion | Cross-DEP mask/runtime bridge | Medium-high | Reasoning tokens rather than motion frames |
| E11 | S11 | Related DEP manuscript | InterDance studies reactive 3D dance generation with leader, music, and interaction constraints | Cross-DEP motion-domain bridge | Medium | No joint experiment or common benchmark |
| E12 | S1-S11 | Review process | Selection, dedup, source-integrity repair, visual verification, and public-source checks | Process validity | High | Does not reproduce scientific results |

## Executive Summary

*Shuffled Autoregression For Motion Interpolation* reframes autoregressive sequence generation as a graph-design problem. Instead of predicting every frame chronologically from all earlier predictions, Shuffled AutoRegression (SAR) chooses a topological generation order and a restricted set of predecessor frames for each target. The paper's motion-specific graph first generates sparse keyframes, then fills short local intervals, then smooths the complete sequence. A Flexible Dependency Attention Mask (FDAM) realizes those graph edges in a GPT-2-style temporal decoder. These mechanism claims are directly supported by the complete paper (E2).

The reported experiment uses 166,696 AMASS-derived windows and a spatial-temporal Transformer (E3). Table 1 reports MPJAE `0.0102`, MPJPE `0.0365`, and NPSS `0.089` for the full model (E4). The strongest causal evidence is internal ablation: chronological autoregression degrades to `0.1847`, `0.3461`, and `6.594` on the same three metrics, while binary-search ordering and removal of smoothing also underperform (E5). Within the paper's tested setup, these results support the claim that dependency topology and the smoothing stage matter.

The evidence does not establish a general solution to motion interpolation. Results come from one constructed dataset, the paper reports no seed uncertainty or user study, visually selects one representative sequence, leaves the Neighbor-L2 normalization ambiguous, and does not test the claimed extensions to multiple keyframes or other domains (E6-E8). No official code release was established. Confidence is therefore high in the transcribed mechanism and reported values, medium in component-level causal attribution, and low in broad transfer or deployment readiness.

The reusable research insight is that generation order is an explicit error-control surface. A safe implementation should compile one graph specification into the attention mask, inference schedule, and trace validator; reject cycles and stale-state reads; and measure dependency depth plus stage-specific error. This is reviewer interpretation derived from the mechanism and cross-DEP evidence (E9-E11), not an author-reported result.

## Detailed Summary

### Problem and Context

Motion interpolation generates the missing poses between a supplied start and end pose. The paper distinguishes this from in-betweening, infilling, and motion blending because endpoint interpolation has extremely sparse input. A deterministic left-to-right model repeatedly conditions on its own predictions and can drift or stop moving before reaching the required endpoint. A non-autoregressive model can instead average over plausible trajectories and over-smooth motion.

Classical interpolation weights frames according to temporal distance and can use information from either side of a target. The authors use this observation to argue that learned interpolation should not be constrained to past-only chronological dependencies. The problem is non-deterministic, yet the evaluation compares generated poses with one observed ground-truth sequence using joint-angle and joint-position losses.

### Shuffled AutoRegression

Standard autoregression uses the fixed order `[0, 1, ..., T-1]` and conditions target `i` on prior outputs. SAR replaces that schedule with a permutation `[t0, t1, ..., tT-1]` and a `choice` function that selects only declared predecessors. If frames are graph nodes and conditioning relationships are edges, the legal dependency structure is a directed acyclic graph; any topological sort consistent with that graph is a valid generation order. Nodes with the same resolved dependencies can potentially be generated together.

The important mechanism is not arbitrary shuffling. The paper argues that error propagates along dependency edges, so topology should select relatively reliable and relevant predecessors while keeping error paths short. A poor graph can still fail: the binary-search ablation lacks enough local dependency and produces incoherent motion.

### Three-Stage Motion Graph

1. **Keyframe interpolation:** Generate sparse internal anchors recursively so later subproblems span shorter intervals. Early anchors are intended to remain close to ground truth and dilute long chronological error paths.
2. **Frame-by-frame generation:** Fill each short interval chronologically so adjacent frames preserve local continuity.
3. **Smoothing:** Regenerate the sequence in parallel while conditioning on the first-pass predictions, reducing discontinuities across subproblem boundaries.

This pipeline combines global anchors, local adjacency, and final whole-sequence correction. The ablations indicate that removing or replacing any one control changes the failure mode rather than merely changing one score.

### Architecture and Mask Semantics

Each pose is a set of joint rotations. A four-block spatial Transformer encoder attends across joints and produces a 1,248-dimensional pose embedding. Sinusoidal position embeddings are added before a six-block GPT-2-style temporal decoder. The temporal decoder's multi-head attention uses FDAM to determine which input frames are visible for each target embedding. The paper describes FDAM as a shuffled transpose of the dependency graph's adjacency matrix. A spatial MLP decoder maps temporal embeddings back to poses.

At inference, the model identifies the next target from the dependency schedule, activates the declared predecessors, generates one valid pose, writes that pose back into the sequence, and repeats. This makes the graph, mask, and state-update loop jointly normative. A row/column convention error or leakage from an unavailable frame would implement a different method.

### Training

Training has two phases. First, teacher forcing optimizes MSE between predictions and ground truth. Second, gradients are blocked while the trained model produces the keyframe and local-fill stages from the start and end frames. The resulting trajectory is fed through the smoothing stage, and MSE is optimized again. Inference follows the second-phase procedure.

The two-phase design narrows train-inference mismatch for the smoothing pass but does not fully expose all stages to an explicit self-rollout objective. The paper does not report schedule sensitivity, graph randomization, curriculum details, or independent loss weights beyond the described MSE objective.

### Dataset and Evaluation

The dataset is built from AMASS using an SMPL+H skeleton. Long motions are sliced into sequence-length-31 windows. For higher-frame-rate source sequences, the authors use both 31- and 62-frame windows and downsample the longer window. The result is 166,696 sequences with approximate 70%, 10%, and 20% training, validation, and test splits. The paper does not specify whether split assignment occurs before or after windowing at subject/session level, so leakage risk cannot be independently assessed.

Metrics are Mean Per Joint Angle Error (MPJAE), Mean Per Joint Position Error (MPJPE), Neighbor L2 Distance as a motion-speed/smoothness proxy, and Normalized Power Spectrum Similarity (NPSS). The source says closeness to ground-truth Neighbor-L2 is desirable, but Table 1 reports signed offsets and also says lower is better. The signed direction and ablation normalization need clarification.

### Results and Ablations

Against BERT, CAE, QuaterNet, and SLERP baselines, the full model has the best displayed MPJAE (`0.0102`), MPJPE (`0.0365`), and NPSS (`0.089`). SLERP is close on reconstruction metrics but the authors argue its averaged trajectory is visually weak. The displayed SAR Neighbor-L2 delta is `-1.0368`, closer to zero than BERT, CAE, or SLERP, but the table's exact transformation remains ambiguous.

Original chronological autoregression performs much worse, with MPJAE `0.1847`, MPJPE `0.3461`, a Neighbor-L2 value/delta of `89.395`, and NPSS `6.594`. Binary-search topology improves substantially over original AR but remains worse than the full model. Removing smoothing also degrades all displayed metrics. These results support the specific three-stage graph under the tested configuration; they do not prove that it is the optimal graph.

The qualitative comparison uses one sequence chosen as representative from 20 random test samples. The paper describes foot penetration for SLERP, upper-body trembling for CAE, over-smoothed motion for BERT, and stronger/coherent motion for SAR. This is useful visual evidence but not an independently rated study.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Sequence-generation dependencies can be represented as a DAG and realized through a topological order plus selective visibility. | Author conceptual and mechanism claim | E2 | Directly supported by the method; implementation correctness was not audited in code. | High |
| C2 | The paper's three-stage graph reduces error accumulation relative to chronological autoregression. | Author empirical and causal claim | E4, E5 | The very large original-AR ablation gap supports the claim in the tested setup; seed and compute controls are absent. | Medium-high |
| C3 | FDAM enables a Transformer decoder to implement the declared dependency graph. | Author mechanism claim | E2 | The paper provides a construction and diagram; no executable mask tests or code were inspected. | Medium-high |
| C4 | Smoothing contributes to final motion quality. | Author empirical claim | E5 | The no-smoothing row degrades all displayed metrics; contribution size lacks uncertainty. | Medium-high |
| C5 | SAR outperforms the selected deep-learning baselines on the main reconstruction and NPSS metrics. | Author empirical claim | E4 | Table values support the tested comparison; baseline parity and statistical significance are not established. | High for transcription; medium for generalization |
| C6 | The Neighbor-L2 evidence is unambiguous. | Implied measurement claim | E7 | Rejected. The caption, signed values, and “closer to ground truth” narrative need clarification. | High rejection confidence |
| C7 | The method transfers readily to multiple keyframes and other interpolation domains. | Author extension claim | E8 | Architecturally plausible but empirically unsupported in the inspected paper. | Low |
| C8 | The paper establishes physically valid, diverse, or human-preferred motion. | Possible broad inference | E6 | Not established; no physical-contact suite, diversity analysis, or blinded user study is reported. | Low |
| C9 | Dependency topology is a reusable error-control and audit surface. | Reviewer interpretation | E2, E5, E9-E11 | Strong mechanistic synthesis; requires new experiments in every target domain. | Medium-high |
| C10 | The reported results are independently reproducible from this deposit. | Reviewer assessment | E1-E12 | Rejected. Sources are inspectable, but code, seeds, data manifests, and runs were not reproduced. | High |

## Methodology

- `Research objective`: Preserve the paper's mechanism, reported evidence, ambiguity, limitations, and safe implementation implications in a schema-complete DEP-E research artifact.
- `Sources inspected`: Canonical arXiv metadata; complete PDF; verified ar5iv full-paper HTML fallback; arXiv source structure; IEEE DOI; official ICASSP program; author publication page; and exactly three related repository artifacts.
- `Discovery strategy`: Enumerated the private archive with `rg --files -g "*.pdf"`, grouped by PDF parent unit, built a cross-repository used-paper index, selected uniformly with PowerShell `Get-Random`, verified source integrity, repaired missing full-paper HTML, extracted structured HTML, rendered all five PDF pages, and searched public author/repository surfaces for publication and implementation context.
- `Inclusion criteria`: Primary-paper method, data, architecture, training, table, figure, ablation, conclusion, source-integrity, publication, and direct conceptual-overlap evidence.
- `Exclusion criteria`: Abstract-only empirical claims, unverified code locators, secondary technical summaries, source-file redistribution, unrelated graph uses, and deployment claims not supported by the inspected evidence.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, product-research, and replication analysis.
- `Evidence handling`: Source claims, reported metrics, negative evidence, reviewer interpretations, and unsupported implications are labeled separately and mapped to evidence IDs.
- `Uncertainty handling`: No metric correction was guessed; missing seed, split, code, compute, physical-validity, and transfer evidence remains explicit.
- `Extraction process`: Searchable full-paper HTML supplied section text and table values; the PDF was rendered at readable resolution and all five pages were inspected, with particular attention to Figure 2, Figure 3, and Table 1.
- `Version control`: Review is pinned to arXiv:2306.06367v1 and public sources as accessed on the date-only marker.
- `Cross-checking`: Title, authors, date, and venue were cross-checked across arXiv, the ICASSP program, and the author page. Table values were cross-checked between extracted HTML and the rendered PDF.
- `Random selection`: 75,780 PDFs mapped to 75,777 units. A used index of 1,204 arXiv IDs excluded 297 units; 185 identifier-incomplete units were withheld. Uniform zero-based eligible index 30,096 was drawn from 75,295 units.
- `Deduplication and reselection validation`: Black-Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and corresponding Black-Lake-Data surfaces were checked. No match existed for arXiv ID, arXiv DOI, IEEE DOI, canonical/normalized title, archive token, or slug. The 24-hour cutoff was 2026-07-23. Duplicate rejections/reselections: 0.
- `Reviewer stance`: Source-grounded paper report, critique, DEP preservation record, implementation brief, and replication plan.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's endpoint motion-interpolation formulation, SAR dependency graph, FDAM mechanism, reported AMASS experiment, ablations, limitations, related-DEP synthesis, and bounded implementation ideas.
- `Temporal boundary`: Paper v1 and public context inspected through 2026-07-24.
- `Evidence limits`: No training, inference, source-code audit, benchmark reproduction, human evaluation, source-data inspection, or independent statistics were performed.
- `Assumptions`: The canonical arXiv record identifies the reviewed PDF/source package, and the validated ar5iv document is a faithful searchable conversion of the same paper.
- `Constraints`: Local source documents must remain private. Public outputs omit local paths, usernames, machine identifiers, timezone labels, and exact execution timestamps. Motion examples use synthetic identifiers rather than human motion data.
- `Out of scope`: Production animation tooling, real-person motion capture collection, safety certification, broad cross-domain transfer claims, and correction of ambiguous source metrics.
- `Intended use`: Research review, DEP deposition, graph/mask verification planning, and reproducibility backlog.
- `Audience`: Motion-generation researchers, sequence-model engineers, evaluation designers, and Black Lake reviewers.
- `Depth target`: Full manuscript review with evidence ledger, critique, implementation paths, and replication notes.
- `Reproducibility boundary`: The algorithm is conceptually reconstructable; the reported results are not independently reproducible without exact code, environment, data/split manifests, seeds, checkpoints, and expected outputs.
- `Operational boundary`: The artifact may propose offline synthetic validators but does not authorize biometric tracking, real-person reenactment, or consequential motion decisions.
- `Data sensitivity`: Public scholarly metadata plus private local scholarly source copies; no human-motion source data was collected or published by this run.

## Observations

- `Observed pattern`: Chronological autoregression is the weakest displayed variant by a large margin, while binary-search ordering recovers much of the performance but loses local coherence. Graph shape matters beyond path length alone.
- `Observed pattern`: The final smoothing pass improves every displayed ablation metric, suggesting that local interval filling does not by itself reconcile boundaries.
- `Technical implication`: FDAM is both a modeling object and a correctness boundary. The graph, topological order, attention tensor, active-frame state, and write-back loop must agree exactly.
- `Metric tension`: SLERP's strong reconstruction metrics coexist with source-described poor visual motion, while Neighbor-L2 semantics are unclear. The evaluation suite is not fully aligned with perceived or physical quality.
- `Generalization boundary`: The paper's DAG abstraction is broad, but all empirical evidence comes from one motion-interpolation construction. Abstraction breadth is not transfer evidence.
- `Open question`: Would a learned or adaptive dependency graph outperform the fixed `[1, 9, 19, 29]` keyframe pattern without leaking future information or sacrificing interpretability?
- `Reviewer hypothesis`: Maximum dependency depth, endpoint distance, local fan-in, and stage boundary count may predict error growth and could become topology-aware evaluation variables.

## Considerations

- **Evaluation:** Add subject-disjoint splits, repeated seeds, confidence intervals, matched implementation budgets, foot-contact and collision metrics, endpoint guarantees, diversity measures, and blinded human ratings.
- **Metric definition:** Publish raw Neighbor-L2 values, the exact reference value, sign convention, absolute/signed transformation, and optimization direction. Do not compare transformed values without the formula.
- **Graph safety:** Enforce acyclicity, known-node edges, topological consistency, no future-state leakage, and deterministic graph-to-mask compilation.
- **Train-inference parity:** Trace which frames are ground truth, generated, active, or masked in every phase. A mask that is correct under teacher forcing can still misrepresent rollout-time state.
- **Data governance:** AMASS aggregates multiple motion datasets. A derivative must honor dataset-specific licenses, subject consent, retention rules, and redistribution limits.
- **Physical validity:** Joint reconstruction error does not guarantee foot contact, collision avoidance, momentum plausibility, or animator utility.
- **Operations:** Measure latency, peak memory, number of sequential graph levels, parallelizable node groups, and failure fallback. A graph with strong metrics but deep serial levels may be impractical.
- **Human representation:** Avoid treating one skeletal parameterization or benchmark distribution as universally representative of bodies, movement styles, accessibility needs, or cultural motion.

## Strengths

- Makes generation order and selective dependencies explicit rather than burying them inside a fixed causal mask.
- Provides a simple graph interpretation that connects topology to error propagation and potential parallelism.
- Uses a three-stage design whose components correspond to recognizable global-anchor, local-continuity, and smoothing roles.
- Includes direct ablations of chronological order, a different DAG topology, and smoothing.
- Cross-checkable equations, diagrams, table values, and source files make the mechanism inspectable.
- Addresses a sparse-input problem where standard sequence assumptions are visibly strained.

## Weaknesses

- The five-page paper leaves many replication details under-specified, and no official code repository was established.
- One constructed AMASS dataset is the sole empirical domain; split isolation and preprocessing manifests are incomplete.
- Results lack multiple seeds, confidence intervals, statistical tests, compute/latency accounting, and parameter count.
- Table 1's Neighbor-L2 transformation and optimization direction are ambiguous.
- The qualitative study shows one author-selected representative example from 20 samples without blinded raters.
- The objective rewards agreement with one ground-truth path even though endpoint interpolation is non-deterministic.
- Physical plausibility, diversity, long-horizon behavior, endpoint robustness, and animator utility are not comprehensively measured.
- Multi-keyframe and cross-domain extensibility are asserted as possibilities rather than demonstrated.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release graph compiler, code, checkpoints, and environment | Reproducibility | FDAM/runtime agreement cannot be audited from prose alone | Independent replication and mask correctness testing | Engineering and license review | Reproduce Table 1 from a frozen manifest |
| Publish subject/session-disjoint split manifests | Data validity | Window-level splitting could leak neighboring motion | More credible generalization evidence | Reduced sample count or lower scores | Hash source sequences and verify no cross-split lineage |
| Clarify and expand motion metrics | Measurement | Current metrics disagree with visual claims and Neighbor-L2 is ambiguous | Better physical and perceptual validity | More annotation and implementation | Add raw/signed formulas, foot contact, penetration, acceleration, diversity, and human preference |
| Multi-seed matched ablations | Causal attribution | Single point estimates can hide training variance | Stronger topology and smoothing conclusions | Repeated training cost | At least three seeds with paired intervals |
| Learn or search graph topologies under constraints | Method | One hand-designed graph may not be optimal | Better tradeoff between depth, continuity, and error | Search instability and leakage risk | Compare fixed, learned, and oracle graphs on held-out subjects |
| Test multi-keyframe and longer sequences | External validity | Claimed extensibility is untested | Defines framework scope | Greater compute and new failure modes | Length/keyframe sweeps with stage-wise error and latency |
| Add rollout-state and mask conformance tests | Correctness | Silent visibility bugs implement a different method | Safer implementation and debugging | Test-maintenance burden | Synthetic golden graphs and trace equality checks |

## Potential Implementations

1. **Graph-to-FDAM compiler**
   - `User`: Sequence-model engineer.
   - `Goal`: Generate one consistent schedule, attention mask, and runtime contract from a versioned DAG.
   - `Core mechanism`: Validate nodes/edges, topologically sort, compute dependency closure and depth, emit tensor fixtures, and compare runtime traces.
   - `Required inputs`: Node schema, directed edges, frame roles, padding policy, and expected active-state transitions.
   - `Outputs`: Mask tensor, schedule, parallel levels, validation report, and golden tests.
   - `Risk controls`: Synthetic IDs, cycle rejection, no future-state reads, deterministic serialization, and no private motion logging.
   - `Evaluation`: Property tests on random DAGs plus hand-checked SAR fixtures.

2. **Motion Topology Audit Bench**
   - `User`: Motion-generation researcher.
   - `Goal`: Compare chronological, binary-search, SAR, and learned graphs under matched conditions.
   - `Core mechanism`: Hold architecture, data, training budget, metrics, and seeds fixed while changing only graph topology.
   - `Required inputs`: Authorized motion benchmark, frozen splits, graph definitions, model/environment manifest, and evaluation protocol.
   - `Outputs`: Reconstruction, physical, perceptual, dependency-depth, latency, and memory results with uncertainty.
   - `Risk controls`: Dataset-license checks, aggregate reporting, no subject identification, and pre-registered comparisons.
   - `Evaluation`: Subject-disjoint repeated-seed study with paired bootstrap intervals.

3. **Stage-Aware Interpolation Inspector**
   - `User`: Animator or research evaluator.
   - `Goal`: Diagnose whether failures arise in keyframe anchors, local filling, or smoothing.
   - `Core mechanism`: Visualize stage outputs and overlay endpoint error, velocity continuity, foot contact, and graph dependencies.
   - `Required inputs`: Consented or synthetic skeleton sequence, endpoint/keyframe poses, stage traces, and metric definitions.
   - `Outputs`: Nonbinding diagnostic report and trace visualization.
   - `Risk controls`: Local-only media, no identity inference, provenance, deletion controls, and explicit uncertainty.
   - `Evaluation`: Synthetic known-fault tests and a consented, blinded animator study.

## Three Ways to Exercise This Research

1. **Synthetic graph conformance:** Objective—verify graph/mask/runtime equality; inputs—a toy 12-frame sequence and four legal/illegal DAGs; method—compile each graph, simulate state activation, and compare permitted reads against the mask; output—a conformance report; success criterion—every injected cycle, future read, and direction error is detected; stop condition—no real motion or personal data is needed.
2. **Table and metric audit:** Objective—reconstruct the paper's claims without model execution; inputs—Table 1, metric definitions, and a clean calculation sheet; method—re-enter every value, recompute baseline deltas, and document Neighbor-L2 ambiguities; output—a signed evidence ledger; success criterion—every headline claim traces to a source cell and no unsupported correction is introduced; stop condition—halt any inference whose formula cannot be established.
3. **Matched topology experiment:** Objective—test whether graph topology drives the ablation gap; inputs—an authorized subject-disjoint motion subset, fixed code/configuration, chronological, binary, and SAR graphs, and at least three seeds; method—train under identical budgets and measure stage-wise/physical/perceptual outcomes; output—a reproducible comparison bundle; success criterion—interval estimates distinguish topology effects; stop condition—stop if split lineage, licensing, or compute parity cannot be verified.

## Example MVP Product

- `Product name`: DAG Motion Audit Kit.
- `Target user`: Sequence-model and motion-generation research teams.
- `Problem`: Custom dependency graphs and masks are easy to implement inconsistently, and final motion scores hide where error entered the pipeline.
- `Core workflow`: Import a versioned graph; validate and compile it; run synthetic conformance tests; ingest an authorized stage trace; compute topology, continuity, endpoint, and physical diagnostics; export a public-safe report.
- `Data requirements`: Graph JSON, synthetic fixtures, optional authorized skeleton traces, metric formulas, model/version metadata, and split manifest. Raw video is not required.
- `Architecture`: Local Python CLI; graph validator; topological scheduler; mask compiler; trace replayer; metric plugins; immutable provenance ledger; Markdown/JSON exporter.
- `Success metrics`: 100% detection of seeded cycle/direction/leakage faults; deterministic mask hashes; exact schedule-trace agreement; stage attribution on known synthetic failures; zero private path/source leakage.
- `Risk controls`: Local-only operation, synthetic fixtures by default, no identity inference, no source upload, dataset-license checks, access control, deletion receipts, and nonbinding output labels.
- `Limitations`: Does not train SAR, reproduce Table 1, judge animation aesthetics, or prove that a graph generalizes to a new domain.
- `MVP boundary`: Graph compilation, conformance, and offline diagnostics only; no motion generation or production animation integration.
- `Deployment model`: Local CLI or notebook in an authorized research environment.
- `Evaluation plan`: Unit tests for known DAGs, property tests on random DAGs, golden mask fixtures, malformed-input tests, synthetic motion faults, and reviewer sign-off on metric definitions.
- `Failure modes`: Reversed edge convention, off-by-one frame IDs, padding leakage, stale active-state writes, positional mismatch, ambiguous metric transformations, and overinterpretation of topology depth.
- `Maintenance plan`: Version graph schema, tensor convention, metric definitions, and fixtures together; require migration tests for every semantic change.

## Related Research and Reading

### Related DEP Entries

| Item | Type | Relevance | Repository-relative identifier |
|---|---|---|---|
| AR-Drag Motion Control | DEP-E manuscript | Compares teacher forcing, Self-Forcing, and Self-Rollout in autoregressive motion-controllable video; exposes generated-history and long-horizon error as training/runtime concerns | `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` |
| Structured Thoughts | DEP-A review | Uses a custom attention mask to encode semantic visibility and aligns the training information graph with inference-time state pruning | `.lake-data/DEP-A/DEP-A-20260715-Structured Thoughts/2607.10386-whitepaper-review.md` |
| InterDance Reactive 3D Dance | DEP-E manuscript | Neighboring 3D human-motion generation problem with music, leader motion, interaction, temporal coherence, and physical plausibility constraints | `.lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md` |

### Primary Context

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| AMASS | Dataset paper cited by the source | Underlying motion archive from which the paper constructs its evaluation windows | Paper reference [11]; use subject to AMASS component licenses |
| Robust Motion In-Betweening | Baseline/neighbor cited by the source | Sparse-keyframe motion generation and time-to-arrival conditioning | Paper reference [6] |
| Transformer / GPT-2 | Architecture foundations cited by the source | Spatial attention and temporal decoder backbone adapted through FDAM | Paper references [9], [10], and [12] |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2306.06367v1 | Canonical title, authors, date, abstract, subjects, version, and artifact locators | 2026-07-24 | Metadata only |
| R2 | https://arxiv.org/pdf/2306.06367 | Primary paper, equations, diagrams, Table 1, visual verification, and references | 2026-07-24 | Verified local copy withheld |
| R3 | https://ar5iv.labs.arxiv.org/html/2306.06367 | Searchable full-paper methods, experiment text, table extraction, and conclusion | 2026-07-24 | Approved fallback; verified local copy withheld |
| R4 | https://arxiv.org/e-print/2306.06367 | TeX/source structure | 2026-07-24 | Collected locally and withheld |
| R5 | https://doi.org/10.48550/arXiv.2306.06367 | Persistent arXiv identifier | 2026-07-24 | DataCite/arXiv DOI |
| R6 | https://doi.org/10.1109/ICASSP49357.2023.10095312 | Publisher/proceedings locator | 2026-07-24 | IEEE DOI |
| R7 | https://icassp23-static-program.pages.dev/ | Conference-program confirmation | 2026-07-24 | Official program context |
| R8 | https://hcsi.cs.tsinghua.edu.cn/ | Author-group venue/publication context | 2026-07-24 | Author-maintained page |
| R9 | `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` | Related synthesis: autoregressive motion and rollout history | 2026-07-24 | Repository-relative |
| R10 | `.lake-data/DEP-A/DEP-A-20260715-Structured Thoughts/2607.10386-whitepaper-review.md` | Related synthesis: visibility masks and runtime state | 2026-07-24 | Repository-relative |
| R11 | `.lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md` | Related synthesis: 3D human-motion generation | 2026-07-24 | Repository-relative |
| R12 | Local PDF, full-paper HTML, metadata HTML, source package, renders, extraction caches, attribution, summaries, and verification reports | Source integrity, visual review, and private provenance | 2026-07-24 | All files withheld locally; none uploaded |

## Appendix

### Random Selection and Dedup Record

- Enumeration method: `rg --files -g "*.pdf"` over the private archive.
- Paper-unit definition: unique PDF parent directory.
- PDFs: 75,780.
- Candidate units: 75,777.
- Used base arXiv IDs: 1,204.
- Used-ID exclusions: 297.
- Identifier-incomplete withholds: 185.
- Eligible units: 75,295.
- Random method: PowerShell `Get-Random`, uniform zero-based index.
- Selected index: 30,096.
- Selected paper: arXiv:2306.06367, *Shuffled Autoregression For Motion Interpolation*.
- Dedup surfaces: Black-Lake `.logs`, `.reports`, `.lake-data`, `.staging`; automation memory; Black-Lake-Data `.logs`, `.reports`, `.lake-data`, `.staging`.
- Exact final keys: arXiv ID, arXiv DOI, IEEE DOI, canonical title, normalized title, archive token, and slug.
- 24-hour cutoff: 2026-07-23.
- Duplicate rejections/reselections: 0.

### Source Integrity Record

- Initial classification: partial; valid PDF present, verified full-paper HTML missing.
- Repair: preserved the valid PDF; collected metadata HTML, approved ar5iv full-paper HTML fallback, and arXiv source package through one bounded strategy.
- PDF: 2,310,025 bytes; `%PDF-` header; trailing `%%EOF`; five pages; unencrypted.
- Full-paper HTML: 189,178 bytes; 30,036 stripped body characters; document marker present; 43 headings; six structure terms.
- Metadata HTML: 41,910 bytes; metadata only.
- Source package: 2,641,656 bytes.
- Partial files: zero.
- Visual inspection: all five pages rendered; Figures 2 and 3 plus Table 1 inspected; non-fatal local font-substitution warnings did not prevent legibility.
- Source locality: all original and derived source evidence withheld locally; no `.source/` directory created; no source files uploaded.

### Replication Checklist

- [ ] Obtain and review authorized AMASS component licenses and source-sequence lineage.
- [ ] Freeze a subject/session-disjoint train/validation/test manifest before windowing.
- [ ] Publish exact skeleton preprocessing, coordinate conventions, window/downsampling logic, seeds, optimizer, schedule, and checkpoints.
- [ ] Compile graph, schedule, FDAM, and runtime state transitions from one versioned specification.
- [ ] Add synthetic cycle, direction, future-leakage, padding, and off-by-one tests.
- [ ] Reproduce chronological, binary-search, no-smoothing, and full-SAR variants with matched compute and multiple seeds.
- [ ] Define Neighbor-L2 raw value, reference, transform, sign, and optimization direction.
- [ ] Add physical, perceptual, diversity, endpoint, latency, memory, and parallel-depth evaluation.
- [ ] Test longer sequences, different keyframe sets, multi-keyframe inputs, and at least one held-out motion dataset.
- [ ] Preserve run manifests, graph hashes, mask hashes, code revisions, metric versions, and expected outputs.

## Attribution Block

| Source | Attribution | Use and boundary |
|---|---|---|
| [arXiv:2306.06367v1](https://arxiv.org/abs/2306.06367v1) | Shuo Huang, Jia Jia, Zongxin Yang, Wei Wang, Haozhe Wu, Yi Yang, and Junliang Xing | Canonical metadata, abstract, subject classes, version, and public locators; metadata is not full-paper evidence. |
| [arXiv PDF](https://arxiv.org/pdf/2306.06367) | Same authors | Complete primary paper, equations, figures, Table 1, and pagination; verified local copy withheld. |
| [Full-paper ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2306.06367) | Same authors; converted by ar5iv | Searchable full-paper representation; verified local copy withheld. |
| [arXiv source package](https://arxiv.org/e-print/2306.06367) | Same authors | Source-structure evidence; local source archive withheld and not redistributed. |
| [arXiv DOI](https://doi.org/10.48550/arXiv.2306.06367) | DataCite/arXiv | Persistent identifier. |
| [IEEE DOI](https://doi.org/10.1109/ICASSP49357.2023.10095312) | IEEE ICASSP 2023 | Publisher/proceedings locator. |
| [ICASSP 2023 program](https://icassp23-static-program.pages.dev/) | IEEE ICASSP 2023 organizers | Official program context and author listing. |
| [Tsinghua HCSI publication page](https://hcsi.cs.tsinghua.edu.cn/) | Jia Jia's HCSI group | Author-maintained publication context. |
| Local metadata HTML, PDF, full-paper HTML, source package, rendered pages, extraction caches, attribution, summaries, and verification reports | Original paper authors and locally generated verification metadata | Evidence only; all files withheld locally and none uploaded. |
| `.lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md` | Delphoa/Black-Lake DEP-E artifact | Related autoregressive motion-generation and rollout-history synthesis. |
| `.lake-data/DEP-A/DEP-A-20260715-Structured Thoughts/2607.10386-whitepaper-review.md` | Delphoa/Black-Lake DEP-A artifact | Related custom-attention-mask and runtime-state synthesis. |
| `.lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md` | Delphoa/Black-Lake DEP-E artifact | Related 3D human-motion generation and evaluation synthesis. |
