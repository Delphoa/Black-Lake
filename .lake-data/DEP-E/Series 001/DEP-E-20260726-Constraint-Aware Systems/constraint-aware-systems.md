---
schema_version: "2026-07-07-expanded"
title: "Constraint-Aware Systems - DEP-E"
generated_at: "2026-07-26T00:03:06Z"
artifact_type: "DEP research artifact"
primary_subject: "Constraint-aware system design and evaluation"
source_status: "mixed: repository Markdown, canonical records, full papers, and official project surfaces inspected; no external source files deposited"
reviewer: "Codex"
source_repository: "Delphoa-Labs/Black-Lake-Data"
source_dep: "DEP-20260709-Tech Intel 1305"
source_snapshot: "3e2fc891c66520f82f4e1376b6b4180d47080040"
source_access_date: "2026-07-26"
---

# Constraint-Aware Systems - DEP-E

## Source Metadata

- **Selected source DEP:** `Black-Lake-Data/.lake-data/DEP-20260709-Tech Intel 1305`
- **Fixed source snapshot:** `3e2fc891c66520f82f4e1376b6b4180d47080040`
- **Source files inspected:** `README.md` and `daily_research_findings_2026-07-09_1305.md`
- **Primary research set:** ten arXiv papers identified by the source DEP, spanning database bypass, recursive self-improvement, reinforcement-learning post-training, autonomous cybersecurity research, feature unlearning, USSD workflow reliability, spin-lattice relaxation, quantum convolution, time-series imputation, and adaptive neural depth.
- **Supporting surfaces inspected:** the public Jailbreak repository and the public DiRLU repository README; the repository URL supplied by the recursive-self-improvement survey was unavailable at review time; ALER-TI's anonymous code surface was reachable but did not expose durable author or repository identity.
- **Full-text coverage:** full arXiv HTML or PDF was inspected for all ten papers. Five temporary PDFs were rendered for visual review of methods, tables, figures, and limitations. No PDF, source archive, dataset, code repository, or model artifact is included in this DEP.
- **Evidence boundary:** paper and repository statements are reported as source claims. Cross-paper conclusions, risk analysis, and product proposals are reviewer interpretations unless explicitly labeled as inference.
- **Prior-pass status:** no associated source report, Report-Mark, output log, or DEP Class artifact was found. This is an initial synthesis, so no secondary expansion draw applied.

## Evidence Ledger

| ID | Evidence item | Role | Availability | Material used |
|---|---|---|---|---|
| E01 | Selected DEP `README.md` | Source inventory and synthesis | Inspected at fixed repository snapshot | DEP scope, ten-paper inventory, tags, attribution |
| E02 | Selected DEP `daily_research_findings_2026-07-09_1305.md` | Original research notes | Inspected at fixed repository snapshot | Paper summaries, claimed metrics, source URLs |
| E03 | Giannakouris and Trummer, *Breaking Database Lock-in* | Primary paper | Full arXiv HTML inspected | Agent pipeline, storage readers, TPC-H correctness and speed, operational limits |
| E04 | Chen, Wang, and Qu, *Recursive Self-Improvement in AI* | Primary survey | Full arXiv HTML inspected | 1,250-paper corpus, taxonomy, loop-closure analysis, sampling limitations |
| E05 | Abdulsalam, Patel, and Saxe, *RL Post-Training Builds Compositional Reasoning Strategies* | Primary paper | Full arXiv HTML inspected | Synthetic rewrite environment, GRPO/RFT comparison, out-of-distribution composition |
| E06 | Li et al., *Hephaestus* | Primary position paper | Full arXiv HTML inspected | Cybersecurity AI Scientist architecture, containment, governance, stated open boundaries |
| E07 | Hasan and Alam, *Unlearning to Protect* | Primary paper | Full PDF and selected rendered pages inspected | A2C/KD design, Bot-IoT setup, feature removal/restoration, tables, class imbalance |
| E08 | Mamo et al., *Modeling Failure Dynamics in Mobile Interaction* | Primary paper | Full PDF and selected rendered pages inspected | 50,000-run simulation, latency regimes, blocking delay, success cliff |
| E09 | Adhikary and Upadhyaya, *Acoustic-phonon-driven spin-lattice relaxation* | Primary paper | Full PDF and selected rendered pages inspected | First-principles model, ZA phonons, field/temperature behavior, experimental mismatch |
| E10 | Falabella and Sazonov, *QCNN with Rough Path Signature Kernels* | Primary paper | Full PDF and selected rendered pages inspected | MNIST setup, signature construction, VQLS bottleneck, statevector classification |
| E11 | Truong et al., *ALER-TI* | Primary paper | Full arXiv HTML inspected | Latent retrieval, six datasets, ten backbones, overhead and shift tests |
| E12 | Krishnanunni, Scott, and Bui-Thanh, *Optimal control approach for neural network architecture adaptation* | Primary paper | Full PDF and selected rendered pages inspected | A posteriori estimator, layer insertion, synthetic and Navier-Stokes results |
| E13 | `gsvic/Jailbreak` | Official implementation surface | Public repository inspected; HEAD verified on 2026-07-26 | Build/runtime requirements, benchmark reports, MIT repository license |
| E14 | `bamboodrift/recursive_self_improvement` | Survey-linked supporting surface | Unavailable on 2026-07-26 | Availability failure recorded; no repository claims used |
| E15 | `Nahidhasan07/Botnet-Traffic-Detection` | Official implementation surface | Public README inspected; HEAD verified on 2026-07-26 | Project claim summary only; code not executed |
| E16 | ALER-TI anonymous code link | Anonymous supporting surface | Landing surface reachable on 2026-07-26 | Availability and impermanent identity noted; code not inspected or executed |

## Executive Summary

The selected DEP presents ten technically unrelated papers. Read together, they expose one reusable engineering principle: a result is only as reliable as the operational boundary it makes explicit. Storage layout, evaluator quality, rewrite rules, permission scopes, class balance, interaction timeout, phonon spectrum, circuit size, retrieval distribution, and discretization error are not peripheral details. They determine whether a reported system works, what its metric means, and where it will fail.

The strongest empirical papers specify those boundaries and test them directly. Jailbreak reports large speedups but only for direct, readable database files under snapshot-like conditions. The USSD simulation isolates a blocking-delay interaction that produces a sharp completion cliff. ALER-TI separates frozen forecasting backbones from a lightweight retrieval adapter and reports both gains and overhead. The optimal-control work uses a computable error estimator to choose where new neural layers should be inserted. In each case, the mechanism is legible enough to audit.

The main caution is that high headline performance can coexist with weak external validity. DiRLU's 99% metrics sit on an extremely attack-heavy Bot-IoT sample and its feature-zeroing operation does not demonstrate deletion of personal training records. The QCNN study is simulated and its proposed quantum signature calculation becomes impractical at realistic sequence lengths, so the classification experiments use a classical signature library. Hephaestus is an architectural position paper rather than an evaluated autonomous cyber scientist. The recursive-self-improvement survey is broad but explicitly recency-biased and is not a census.

Reviewer interpretation: the most useful cross-domain artifact is not a single model. It is a constraint registry that binds each claim to the state assumptions, evaluator, resource budget, intervention, and failure boundary under which the claim was observed. Such a registry would make comparisons harder to game and would help future agents distinguish a paper's demonstrated capability from an attractive extrapolation.

## Detailed Summary

### Direct database storage readers

Jailbreak uses an agentic pipeline to generate C++17 readers that parse PostgreSQL heap files and MySQL InnoDB pages directly and expose data through the Arrow C Data Interface. The paper describes Dataset Generator, Architect, Coder, and QA agents, then evaluates the resulting readers on TPC-H scale factor 1. It reports correctness for all 22 TPC-H queries and speedups up to 5.1 times over PostgreSQL access and roughly 27 times over MySQL access in the evaluated pipeline.

Those results depend on privileged, low-level access to database files and on a stable snapshot. Direct page interpretation bypasses the server mechanisms that normally arbitrate transaction visibility, access control, recovery, and storage-version compatibility. The repository documents PostgreSQL 12-16 and MySQL 8.0 requirements, readable storage files, fixed platform details, benchmark scripts, and result reports. This makes the implementation unusually inspectable, but it also makes the operational constraint unusually consequential.

Reviewer interpretation: database bypass is best treated as a controlled offline-export or co-located analytics technique, not as a drop-in transactional read path. Numeric conversion, transaction visibility, storage upgrades, integrity checks, and file permissions need explicit conformance tests before the claimed performance can be transferred to a production setting.

### Recursive self-improvement as bounded loops

The recursive-self-improvement survey organizes 1,250 papers into deployment-time improvement, training-time improvement, evaluation and verification, autonomous research, and foundations. Its corpus combines 871 seed papers with 379 targeted additions. The authors argue that bounded self-refinement loops dominate the literature while open-ended recursive self-improvement remains sparse.

The survey's strongest contribution is structural rather than predictive. It distinguishes what is improved from how fully the feedback loop closes, and it treats evaluator and verifier quality as a load-bearing dependency. The reported category counts are 393 deployment, 340 training, 318 evaluation, 139 autonomous research, and 60 foundations. The authors also note that 74% of the corpus is from 2026, so the sample is heavily shaped by recency and query design.

Reviewer interpretation: “self-improvement” should never be accepted as a unitary capability claim. A deployable description needs at least the changed object, the evaluator, the acceptance threshold, the rollback path, the resource envelope, and the maximum loop depth. The paper's linked repository was unavailable during this review, so its dataset and categorization could not be independently inspected.

### Reinforcement learning and compositional rewrite strategies

Abdulsalam, Patel, and Saxe train Transformers from scratch in a fully observable synthetic rewrite grammar. The environment provides primitive rewrite operations and evaluates solutions with a binary outcome-only reward. The paper compares group relative policy optimization with rejection fine-tuning under controlled pretraining mixtures and a 256-token solution budget.

The reported evidence supports a specific claim: reinforcement learning can discover compositions of already represented primitives rather than merely increase their marginal use. The RL policy combines sequential macro contractions and parallel contractions on harder tasks, while rejection fine-tuning produces many invalid shortcut-like rewrites. The organization of pretraining chains matters more than mere exposure to primitives.

The environment is intentionally narrow. It does not establish general compositional reasoning in natural language, tool use, or long-horizon open worlds. Reviewer interpretation: the result is valuable as a mechanistic test bed because its state, action, reward, and validity constraints are explicit; transferring the conclusion requires a comparably inspectable task grammar and evaluator.

### A bounded cybersecurity AI scientist

Hephaestus proposes a modular Cybersecurity AI Scientist whose roles cover hypothesis formation, experiment design, controlled execution, evidence aggregation, and governance. It emphasizes cyber ranges, digital twins, bounded permissions, containment, audit trails, and release boundaries. Its “four zeros” aspiration covers risk, trust, incident, and energy.

The paper is a position and architecture paper, not an empirical demonstration of an autonomous system. No benchmark establishes safe operation, discovery quality, or governance performance. Its most important evidence is therefore the explicit identification of safety constraints: experimental isolation, traceable evidence, least privilege, staged release, and human or institutional oversight.

Reviewer interpretation: these constraints should be implemented as independently enforced infrastructure rather than natural-language obligations inside an agent prompt. The paper leaves institutional placement and liability unresolved, which is a central deployment boundary rather than a minor future-work item.

### Distilled RL, feature suppression, and IoT security

DiRLU combines actor-critic learning, knowledge distillation, parameter hard weight masking, and LIME on a 25% Bot-IoT sample. The inspected paper reports 15,000,000 rows, of which 14,992,430 are attacks and 7,570 are benign, then uses a random 70/10/20 split and SMOTE on the training set. Table VII reports the 25% A2C student at 99.602% accuracy and 99.800% F1 before feature removal, 99.354% and 99.676% after removal, and 99.603% and 99.801% after restoration. The paper also reports 3,014 parameters and 2,370 FLOPS for the student.

The masking procedure zeros first-layer connections for the selected feature and can restore saved weights. That is evidence of reversible feature-influence suppression inside a trained model. It is not evidence that personal examples were deleted from training data, that all information about the feature was removed from correlated representations, or that a legal right-to-erasure request was satisfied. LIME is shown for one randomly selected test instance, which does not establish stable global explanation quality.

The class distribution makes aggregate accuracy and F1 difficult to interpret for benign behavior, and the paper does not document group-aware splitting that would rule out related-flow leakage. Table VII also contains a large degradation for the 30% A2C student, while the surrounding prose presents broad robustness. Reviewer interpretation: privacy, unlearning, and detection claims require separate tests with class-specific metrics, membership or influence attacks, group-disjoint splits, and explicit erasure semantics.

### The USSD success cliff

Mamo et al. simulate 50,000 USSD workflow runs under a 120-second session timeout. Network round-trip times follow low, medium, and high gamma regimes with means of 1, 2.5, and 5 seconds. A blocking SMS one-time-password action adds a uniformly distributed 5-30 second delay. Four workflow-complexity levels represent increasing interaction steps.

Without the blocking action, completion declines gradually as complexity rises. With blocking, the paper reports a cliff between levels 3 and 4 across network regimes: medium-latency completion is roughly 89%, while high-latency completion is roughly 75% at the highest complexity. The effect persists across the tested error regimes and latency-parameter combinations.

This is simulation evidence, not field telemetry. Results depend on the timeout, key-level timing assumptions, error model, and latency distribution. Reviewer interpretation: the contribution is the interaction effect, not a universal threshold. A production team should validate the cliff location with country, carrier, handset, retry, accessibility, and real-user timing data.

### Acoustic phonons and spin relaxation in hBN

Adhikary and Upadhyaya calculate the spin-lattice relaxation of the negatively charged boron vacancy in monolayer hexagonal boron nitride using first-principles electronic structure, spin-phonon coupling, and finite-momentum acoustic phonons. The model attributes low-temperature relaxation mainly to the flexural ZA branch, whose quadratic dispersion creates a finite low-energy density of states. The calculated field and temperature dependence reproduces the nonmonotonic trend reported in experiments.

The calculation uses a pristine monolayer model, whereas the motivating experiment uses a thicker supported flake. The authors identify possible cross-relaxation and other paramagnetic defects, an unresolved field region near an anticrossing due to momentum-grid resolution, and higher-temperature Raman processes outside the low-energy treatment.

Reviewer interpretation: the useful constraint is model-to-specimen equivalence. Agreement in a curve's shape does not isolate a mechanism when substrate, thickness, defects, and cross-relaxation differ. The paper nevertheless provides a physically explicit hypothesis that can be falsified by thickness-, substrate-, isotope-, and field-resolution studies.

### Rough-path signatures in a QCNN

Falabella and Sazonov combine rough-path signature features with a quantum convolutional neural network for binary MNIST classification of digits 0 and 1. The dataset contains 12,665 training images and 2,115 test images. Images are represented as paths; signature features are encoded into quantum states and fused with raw-image features through an auxiliary-qubit design.

The paper also formulates a quantum computation of the signature kernel using a variational linear-system solver. Its own resource analysis shows that realistic 20-50-step paths produce linear systems of at least 800 by 800 and require at least ten fully connected qubits. The proposed VQLS route becomes unreliable already at five or six steps, so the classification experiments use the classical `sigkernel` library, downsample to 16 path points, and run noiseless statevector simulation.

Some circuit architectures benefit from the auxiliary signature representation, but exact performance values are primarily figure-based and not presented as a complete numeric table. Reviewer interpretation: the study supports signature-assisted simulated QCNN classification, not a practical quantum advantage or a hardware-realized quantum signature kernel.

### Retrieval augmentation for time-series imputation

ALER-TI adds retrieval to frozen time-series imputation backbones. It encodes historical candidate segments without a missingness mask, applies post-hoc masking in latent space, forms a candidate-guided query, retrieves cached embeddings, and uses a lightweight adapter around the frozen backbone. Evaluation covers six datasets, ten backbones, four missing rates, four sequence lengths, and three seeds.

The paper reports consistent MSE and MAE gains, with random retrieval sometimes harming performance and more expensive oracle-style matching providing a comparison point. It also reports operational cost. On Weather, database construction takes 921.7 seconds; the adapter has 0.0022 million parameters; and inference latency rises, for example, from 6.1 to 7.3 milliseconds for ModernTCN and from 1.3 to 2.1 milliseconds for DLinear. Early-window distribution-shift tests generally preserve gains, with a tie on Weather in one setting.

The anonymous code surface does not provide durable identity, and the study focuses on its selected missingness patterns. Reviewer interpretation: retrieval quality is part of the model boundary. A deployment needs database versioning, contamination controls, privacy policy, drift monitoring, fallback behavior for poor matches, and evaluation under block missingness and sensor failures.

### Error-guided neural depth adaptation

Krishnanunni, Scott, and Bui-Thanh formulate neural-network training as a continuous-time optimal-control problem. Piecewise-linear weights and biases are discretized with finite elements. A dual-weighted residual estimator assigns local error contributions, and layers are inserted where the estimated contribution is largest.

The method is evaluated on synthetic regression and an inverse Navier-Stokes problem. For the inverse problem, a 64 by 64 field, ten observations at time 0.5, 50 Karhunen-Loève coefficients, viscosity \(10^{-3}\), and 1% Gaussian noise are used with 700/100/300 train/validation/test samples. The final adaptive model reports relative error 0.161 in nine minutes, versus 0.166 for the three-minute baseline and 0.170-0.172 for several other insertion strategies. In synthetic regression, the final adaptive result reports MSE \(9\times10^{-6}\) in 46 minutes versus \(3.82\times10^{-5}\) in nine minutes for the baseline.

The manuscript retains publisher-template placeholders, so it should be treated as a preprint rather than a finalized journal record. Gains come with added estimator and retraining cost and are shown in small-width regimes. Reviewer interpretation: the estimator is most compelling as an auditable decision signal for architecture change; broader value depends on scaling tests, compute-normalized comparisons, and extension beyond depth.

## Key Claims and Evidence

| Claim | Evidence | Assessment |
|---|---|---|
| Direct file readers can materially outperform server-mediated export in the evaluated TPC-H setup. | E03 and E13 report correctness checks, platform details, and large read/ETL speedups. | Supported for the stated database versions, accessible files, schema coverage, hardware, and snapshot-like conditions; not a transactional guarantee. |
| Recursive self-improvement research is dominated by bounded loops. | E04 categorizes 1,250 papers and reports sparse open-ended loop closure. | Supported within a recency-heavy, query-constructed survey corpus; not a census of all research. |
| RL can assemble represented rewrite primitives into harder strategies. | E05 contrasts GRPO and rejection fine-tuning in a controlled grammar. | Supported in the synthetic environment; natural-language and open-world transfer remain untested. |
| A Cybersecurity AI Scientist should be capability-bounded and evidence-native. | E06 specifies modular roles, ranges, permissions, containment, and auditability. | A well-motivated design claim, not an empirically validated system claim. |
| DiRLU preserves headline performance after suppressing one feature. | E07 Table VII reports small metric changes for the 25% A2C student. | Supported for that evaluation; it does not establish training-record erasure, general privacy compliance, or benign-class reliability. |
| Blocking delay and workflow length jointly create a USSD completion cliff. | E08 reports the interaction across simulated latency and error regimes. | Supported by simulation; cliff position requires field validation. |
| Finite-momentum acoustic phonons can explain the observed low-temperature relaxation trend in hBN vacancies. | E09 supplies a first-principles mechanism and comparison with experiment. | Plausible and source-supported, with specimen and unresolved-regime caveats. |
| Rough-path signatures can improve some simulated QCNN configurations. | E10 reports architecture-dependent gains in statevector experiments. | Supported narrowly; the quantum-kernel construction itself is not practical in the reported regime. |
| Latent retrieval improves multiple frozen time-series imputation backbones. | E11 covers six datasets, ten backbones, missing rates, lengths, seeds, and overhead. | Broad within the benchmark design; database shift, privacy, and non-random failures need stronger tests. |
| A posteriori error estimates can guide neural layer insertion. | E12 reports targeted insertion and lower errors than comparison strategies. | Supported in two proof settings; compute cost, small margins, and scale limit generalization. |
| Explicit constraints are a transferable source of scientific and engineering reliability. | E03-E12 each expose a decisive state, resource, evaluator, or modeling boundary. | Reviewer synthesis. It is a design heuristic, not a directly tested cross-domain causal law. |

## Methodology

The review began from the fixed source DEP snapshot and inspected every deposited file. Each listed paper was then checked against its canonical arXiv record. Full HTML was used where available; PDFs were used where necessary and selected pages were rendered to verify visual tables, figures, equations, or layout-dependent limitations.

For each work, the review extracted five elements: the object being changed, the operational state assumed, the evaluator or measurement, the reported result, and the failure or transfer boundary. Numerical claims were retained only when they were visible in the inspected source. Apparent inconsistencies were recorded rather than reconciled by invention.

Official project surfaces were inspected only when linked by a primary paper. Their presence was used to assess availability and implementation scope, not to treat README claims as independent replication. No code, data, or models were executed. Cross-paper synthesis was performed only after the individual evidence records were established.

## Scope, Constraints, and Assumptions

- This is a review of the ten works selected by the source DEP, not a systematic review of each field.
- All ten papers were July 2026 preprints at inspection time. Publication status may change.
- Reported measurements are author results unless explicitly identified as reviewer analysis.
- Five PDFs were temporarily downloaded for inspection; none are deposited. ArXiv HTML or canonical records supplied the remaining full-text evidence.
- No benchmark was rerun, no result was statistically recomputed, and no code dependency was installed.
- Repository availability was checked on 2026-07-26. Availability does not imply correctness, maintenance, reproducibility, or a particular license for paper content.
- The Jailbreak repository was publicly reachable and displayed an MIT repository license. That does not override the paper's separate terms.
- The recursive-self-improvement repository link was unavailable. The survey's corpus and counts were therefore not independently audited.
- The ALER-TI code surface was anonymous and impermanent by design; it was not treated as durable provenance.
- Legal claims about privacy, erasure, security, or compliance are not endorsed. They require domain-specific review and empirical evidence beyond the papers inspected here.

## Observations

1. **The hidden state is often the real experimental variable.** Database tuple visibility, related traffic flows, pretraining-chain organization, historical retrieval candidates, and physical specimen differences can all change the meaning of an otherwise stable metric.
2. **A verifier defines the ceiling of an improvement loop.** This is explicit in the self-improvement survey and visible elsewhere: query equivalence tests constrain Jailbreak, grammar validity constrains RL, timeout completion constrains USSD, and an error estimator constrains depth adaptation.
3. **Aggregate metrics can conceal the protected failure.** DiRLU's attack-heavy sample, ALER-TI's averaged datasets, and figure-only QCNN results all show why class-, regime-, and cost-specific reporting matters.
4. **Resource accounting changes capability claims.** Direct storage access, quantum-system size, database construction time, estimator overhead, and simulation fidelity are part of the method, not deployment footnotes.
5. **Mechanistic specificity improves auditability.** Acoustic-phonon branches, page layouts, rewrite primitives, blocking delays, and local residual errors give reviewers something falsifiable.
6. **Governance claims need enforcement surfaces.** Hephaestus's safety boundaries and the self-improvement survey's verifier hierarchy become credible only when permissions, isolation, audit logs, rollback, and release policy exist outside the model's discretion.

## Considerations

- A performance comparison should publish the operational state that each method receives. Giving one method direct files and another a network path may be useful, but the state asymmetry must be part of the claim.
- A privacy or unlearning evaluation should state the erasure object: feature influence, parameter contribution, example membership, retained data, or downstream behavior. These are not interchangeable.
- Retrieval systems need provenance at both document and embedding levels. Candidate creation date, mask policy, data ownership, and contamination status should travel with retrieved evidence.
- Self-improving systems need stopping conditions and negative-result retention. Otherwise the loop can optimize an incomplete verifier and erase evidence of regression.
- Simulation studies should identify which distributions are calibrated from field data and which are hypothetical. Sensitivity tests do not substitute for population validity.
- Scientific ML claims should separate classical preprocessing, simulation, and quantum execution so the location of any quantum contribution is visible.
- Adaptive architectures should compare not only final error but total tuning cost, variance across seeds, and equal-compute baselines.

## Strengths

- The source DEP is compact, attributable, and internally consistent enough to seed a full source-first review.
- The ten papers expose unusually varied constraint types, enabling a useful cross-domain comparison without forcing a false common task.
- Jailbreak, the USSD study, ALER-TI, and the depth-adaptation paper report operational details and costs that allow bounded interpretation.
- The RL paper's synthetic grammar is narrow but mechanistically clear.
- The hBN paper connects a specific microscopic mechanism to an observed macroscopic trend and lists concrete mismatch sources.
- Several works publish implementation or data surfaces, making future replication or static audit possible.

## Weaknesses

- The source DEP's original summaries are high-level and do not carry a claim-by-claim evidence ledger.
- All ten primary works are preprints from a short time window, increasing the risk of revision and selection bias.
- Code and data were not executed, so reproducibility remains untested.
- DiRLU's extreme class imbalance, uncertain group separation, metric inconsistencies, and narrow explanation example weaken broad security and privacy claims.
- The QCNN paper's practical quantum path is blocked by its own resource analysis.
- Hephaestus lacks empirical validation.
- The self-improvement corpus could not be independently inspected because its linked repository was unavailable.
- Several studies test synthetic or controlled settings whose deployment populations are not established.

## Potential Improvements

- Publish a machine-readable constraint card beside every experiment with state assumptions, permissions, data split unit, evaluator, resource budget, stopping rule, and known invalid regimes.
- For Jailbreak, add versioned binary fixtures, transaction-visibility conformance, numeric round-trip tests, corruption handling, and online/offline safety modes.
- For recursive self-improvement, release a pinned corpus manifest with query provenance, deduplication logic, category annotations, and uncertainty estimates.
- For RL composition, add held-out grammars, partial observability, noisy feedback, tool side effects, and evaluator adversarial tests.
- For Hephaestus, implement a minimal cyber-range prototype whose permissions and evidence capture are enforced by the range controller.
- For DiRLU, use group-disjoint splits, class-specific precision/recall, calibration, membership and influence tests, multiple explanation samples, and a precise erasure contract.
- For USSD, calibrate distributions with field traces and stratify by carrier, region, handset, accessibility need, retry behavior, and session policy.
- For hBN, test thickness, substrate, isotope, defect concentration, and the unresolved anticrossing field window.
- For QCNN, report complete numeric tables, finite-shot and noise results, equal-parameter classical baselines, and a feasible hardware resource estimate.
- For ALER-TI, pin the code/data manifest and test block missingness, sensor outages, privacy constraints, database poisoning, drift, and stale retrieval.
- For adaptive depth, add seed variance, equal-compute baselines, larger widths, convolutional/recurrent settings, and compute-aware insertion criteria.

## Potential Implementations

### Claim Constraint Card

A repository-side YAML object can accompany each research claim:

```yaml
claim_id: C-001
source_evidence: [E03]
object_changed: storage_reader
state_assumptions:
  - stable_database_snapshot
  - readable_storage_files
evaluator:
  type: query_equivalence
  coverage: tpch_22_queries
resource_boundary:
  platform: disclosed_by_source
failure_boundaries:
  - concurrent_transaction_visibility
  - unsupported_storage_version
status: source_supported_not_independently_replicated
```

### Evaluator-Gated Improvement Loop

An improvement service can require every candidate change to declare its affected object, expected benefit, verifier, resource cost, rollback artifact, and maximum loop count. It should retain rejected trials, run permission checks before execution, and prohibit promotion when the verifier does not cover a declared failure boundary.

### Constraint-Aware Evidence Graph

A semantic graph can connect claims to sources, conditions, metrics, risks, and later replications. Edges should distinguish “reported by source,” “observed by reviewer,” “reviewer interpretation,” and “contradicted or unresolved.” This would let later DEP passes expand a single weak edge without rewriting the original provenance.

## Three Ways to Exercise This Research

1. **Paper audit:** Select one headline metric from each paper and produce a constraint card that identifies the state, evaluator, comparison baseline, resource budget, and unsupported transfer claim. Success means a second reviewer can reproduce the interpretation from the cited evidence.
2. **Bounded prototype:** Implement a toy improvement loop over a synthetic rewrite task. Enforce a fixed action grammar, immutable verifier, ten-iteration maximum, compute budget, retained rejection log, and one-click rollback. Test whether the system refuses changes outside verifier coverage.
3. **Cross-domain stress test:** Build three minimal cases—a snapshot database reader, an imputation retriever under drift, and a feature-suppression classifier under group-disjoint evaluation—and report both performance and constraint violations in the same schema.

## Example MVP Product

- **Product name:** Boundary Ledger
- **Problem:** Research and agent artifacts report results without a portable record of the conditions under which those results are valid.
- **Target user:** Research reviewers, model-risk teams, agent-platform engineers, and DEP maintainers.
- **Core workflow:** Import a paper or DEP; extract candidate claims; require a human-reviewed constraint card; link each field to evidence; run schema checks; publish a provenance graph and comparison view.
- **Inputs:** Primary sources, repository snapshots, reported metrics, experimental conditions, evaluator definitions, cost records, and reviewer annotations.
- **Outputs:** Versioned claim cards, evidence ledger, unresolved-boundary queue, cross-paper comparison, and machine-readable provenance.
- **MVP boundary:** Markdown and YAML artifacts only; no autonomous code execution, legal compliance decision, source redistribution, or factual promotion without reviewer approval.
- **Safety and governance:** Immutable source locators, explicit claim-status labels, role-based approval, reversible revisions, no secret ingestion, and automatic rejection of uncited numeric claims.
- **Success metrics:** At least 95% of published claims have a source locator and evaluator; zero claims are promoted with missing state assumptions; two independent reviewers agree on claim status for at least 85% of a 100-claim pilot; unresolved boundaries remain visible after revision.
- **Validation plan:** Seed the system with the ten papers in this DEP, conduct double review, deliberately insert state and metric omissions, verify detection, and compare review time and disagreement against plain Markdown review.
- **Primary risk:** Structured cards can create false confidence if reviewers fill them mechanically. Mitigation requires evidence links, disagreement capture, and random audit.

## Related Research and Reading

This initial pass substantively reviewed every primary item listed by the selected DEP. No prior DEP Class artifact existed, so there is no older related-reading thread to expand. The items below are the provenance-preserving reading frontier established in this pass.

| Item | Relationship to this manuscript | Inspection status |
|---|---|---|
| *Breaking Database Lock-in: Agentic Regeneration of High Performance Storage Readers for Database Bypass* | Shows how storage-state access and conformance testing bound a large performance claim. | Full paper and official repository inspected. |
| *Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops* | Supplies the improvement-object and loop-closure taxonomy and makes verifier quality central. | Full paper inspected; linked repository unavailable. |
| *RL Post-Training Builds Compositional Reasoning Strategies* | Offers a controlled setting where actions, validity, reward, and transfer difficulty are explicit. | Full paper inspected. |
| *Hephaestus: Toward a Cybersecurity AI Scientist* | Frames permissions, containment, evidence, and governance as native system boundaries. | Full paper inspected; no empirical system reported. |
| *Unlearning to Protect: A Distilled Reinforcement Learning Framework with Privacy-Preserving Feature Unlearning and XAI for IoT Security* | Exposes the need to separate feature suppression, privacy, detection, and explanation claims. | Full paper and official repository README inspected. |
| *Modeling Failure Dynamics in Mobile Interaction: Identifying the Success Cliff in USSD Workflows* | Demonstrates an interaction between blocking delay, latency, complexity, and timeout. | Full paper inspected. |
| *Acoustic-phonon-driven spin-lattice relaxation of the negatively charged boron vacancy center in hexagonal boron nitride* | Shows how specimen and model boundaries qualify a mechanistic explanation. | Full paper inspected. |
| *Quantum Convolutional Neural Network with Rough Path Signature Kernels* | Separates a classical signature-assisted simulation from a resource-limited quantum kernel proposal. | Full paper inspected. |
| *ALER-TI: Aligned Latent Embedding Retrieval for Time Series Imputation* | Treats retrieval state and adapter overhead as part of frozen-backbone imputation. | Full paper inspected; anonymous code surface reachable. |
| *An optimal control approach for neural network architecture adaptation with a posteriori error estimation* | Uses local error estimates to make architecture growth auditable. | Full paper inspected. |
| Jailbreak implementation repository | Supports future static audit and replay of direct-reader claims under pinned database versions. | Public surface inspected; no execution performed. |
| DiRLU implementation repository | Supports future audit of split construction, masking semantics, and class-specific evaluation. | Public README inspected; no execution performed. |

## Source References

1. Delphoa-Labs, [selected source DEP at fixed snapshot](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/3e2fc891c66520f82f4e1376b6b4180d47080040/.lake-data/DEP-20260709-Tech%20Intel%201305), including its [README](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/3e2fc891c66520f82f4e1376b6b4180d47080040/.lake-data/DEP-20260709-Tech%20Intel%201305/README.md) and [research findings](https://github.com/Delphoa-Labs/Black-Lake-Data/blob/3e2fc891c66520f82f4e1376b6b4180d47080040/.lake-data/DEP-20260709-Tech%20Intel%201305/daily_research_findings_2026-07-09_1305.md), accessed 2026-07-26.
2. Victor Giannakouris and Immanuel Trummer, [*Breaking Database Lock-in: Agentic Regeneration of High Performance Storage Readers for Database Bypass*](https://arxiv.org/abs/2607.07696), arXiv:2607.07696v1, 2026.
3. Mingguang Chen, Licheng Wang, and Bo Qu, [*Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops*](https://arxiv.org/abs/2607.07663), arXiv:2607.07663v1, 2026.
4. Azwar Abdulsalam, Nishil Patel, and Andrew Saxe, [*RL Post-Training Builds Compositional Reasoning Strategies*](https://arxiv.org/abs/2607.07646), arXiv:2607.07646v1, 2026.
5. Jiaqi Li, Yang Zhao, Wen Lu, Lvyang Zhang, and Lidong Zhai, [*Hephaestus: Toward a Cybersecurity AI Scientist*](https://arxiv.org/abs/2606.29981), arXiv:2606.29981v1, 2026.
6. Md. Nahid Hasan and Md. Golam Rabiul Alam, [*Unlearning to Protect: A Distilled Reinforcement Learning Framework with Privacy-Preserving Feature Unlearning and XAI for IoT Security*](https://arxiv.org/abs/2607.07635), arXiv:2607.07635v2, 2026.
7. Aklile Seyoum Mamo, Amanuel Kebede, Anny Christelle Irakoze, and Jema Ndibwile, [*Modeling Failure Dynamics in Mobile Interaction: Identifying the Success Cliff in USSD Workflows*](https://arxiv.org/abs/2607.07650), arXiv:2607.07650v1, 2026.
8. Priyo Adhikary and Pramey Upadhyaya, [*Acoustic-phonon-driven spin-lattice relaxation of the negatively charged boron vacancy center in hexagonal boron nitride*](https://arxiv.org/abs/2607.07642), arXiv:2607.07642v1, 2026.
9. Leonardo Nogueira Falabella and Vasily Sazonov, [*Quantum Convolutional Neural Network with Rough Path Signature Kernels*](https://arxiv.org/abs/2607.07634), arXiv:2607.07634v1, 2026.
10. Xuan-Thong Truong, Trung-Kien Le, Tung Kieu, Thi-Thu Nguyen, and Nhat-Hai Nguyen, [*ALER-TI: Aligned Latent Embedding Retrieval for Time Series Imputation*](https://arxiv.org/abs/2607.07640), arXiv:2607.07640v1, 2026.
11. C. G. Krishnanunni, Thomas Scott, and Tan Bui-Thanh, [*An optimal control approach for neural network architecture adaptation with a posteriori error estimation*](https://arxiv.org/abs/2607.07637), arXiv:2607.07637v1, 2026.
12. Victor Giannakouris, [Jailbreak implementation repository](https://github.com/gsvic/Jailbreak), public HEAD `26eb4ba82128f74fab102f119931bce5800e1220` verified 2026-07-26.
13. Chen, Wang, and Qu, [recursive-self-improvement supporting repository](https://github.com/bamboodrift/recursive_self_improvement), unavailable during the 2026-07-26 review.
14. Hasan and Alam, [DiRLU implementation repository](https://github.com/Nahidhasan07/Botnet-Traffic-Detection), public HEAD `b2ff6477e4e4b1b955a781202a03367136c1e382` verified 2026-07-26.
15. Truong et al., [ALER-TI anonymous code surface](https://anonymous.4open.science/r/Time-series-0142/), reached 2026-07-26; durable identity and archival persistence not established.

## Appendix

### Selection and eligibility provenance

- Automation family: `Black-Lake Data Processing & Review` and `Black-Lake Data Processing & Review 0900`
- Eligibility cutoff: `2026-07-25T00:03:06Z`
- Canonical candidates: 83
- Excluded within 24 hours: 2
- Eligible candidates: 81
- Selection method: operating-system cryptographic random UInt32 with rejection sampling over the sorted eligible list
- Accepted UInt32: `1490031564`
- Successful zero-based index: 33
- Eligible-list SHA-256: `3d9508627db266978dc9666cd4acff28b3306d5b1bf95d2add1c22c2d79ca80d`
- Selected DEP: `DEP-20260709-Tech Intel 1305`

### Validation gaps

No code execution, dependency installation, dataset download, model run, benchmark replay, statistical recomputation, hardware experiment, database fixture, field USSD trace, privacy attack, or independent replication was performed. Repository HEAD checks establish availability only. The manuscript should be revised if primary papers or official artifacts change.
