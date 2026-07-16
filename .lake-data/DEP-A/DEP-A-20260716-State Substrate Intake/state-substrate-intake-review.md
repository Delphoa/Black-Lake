# Governed State Meets Physical Substrate: A Cross-Domain Assurance Ledger

## A whitepaper-grade archival intake review and independent re-conceptualization of the complete State and Substrate DEP-E record

**Artifact prepared:** 2026-07-16

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260716-State and Substrate`

**Source commit:** `b5ad2459a6ee3d649feb8209d9390d86d475502c`

**Paired task indicator:** `BL-DEPPAIR-20260716-0095B1FD`

**Direction:** `DEP-E -> DEP-A`

**Source provenance:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes

**Review scope:** complete two-file composite DEP-E repository record, inventory and integrity audit of its ten-study reconstruction, claim vetting across heterogeneous evidence regimes, independent re-conceptualization, implications, failure modes, and falsification agenda

**Reproduction boundary:** the current intake did not independently re-open the ten external full papers, execute code, access datasets, run models, repeat attacks, fabricate devices, solve physical systems, or reproduce any result. Detailed study-level content is attributed to the DEP-E report, which states that its authoring run inspected all ten complete primary papers.

---

## Executive assessment

The source record is a composite scholarly DEP rather than a review of one paper. It rechecks a technology-intelligence digest against ten complete primary preprints and organizes them around a reviewer-created theme: governed state and physical substrate.[^dep] The software-facing studies cover repository-aware agent control, long-lived memory, privacy leakage across released models, continual survival learning, and low-resource code completion. The physical-facing studies cover perovskite passivation modeling, Rydberg quantum hashing, telecom-band photonic cluster states, path-superposition gate teleportation, and CMOS electrostatic-to-spin modeling.

The bundle’s unifying claim is deliberately modest. In every domain, a state influences the next action or inference: repository state authorizes an agent operation; memory state shapes later reasoning; released-model state leaks dataset lineage; clinical model state must adapt without catastrophic forgetting; atomic, photonic, electrostatic, and language-model states constrain observed performance. The source argues that reliability improves when authority, boundary, evidence, and validity regime are explicit before that state is trusted.

This is a useful cross-domain assurance heuristic, not a unified scientific law. The ten studies use incomparable evidence. MRMS reports 98.8% success on 800 deterministic synthetic tasks with a 98.0–99.4 interval. A privacy study reports a best AUC movement from .793 to .925 in one UTKFace comparison. MergeSurv reports, among other values, a VEA C-index of .6773 and forgetting of .0138, while another method leads one IPCW metric. A photonic experiment reports process fidelity `.71 ± .01`, negativity `.27 ± .02`, and indistinguishability at least `.83`. A CMOS reduced model reports 1.134 mV RMSE against much larger comparison errors in a matched two-dimensional case. A Pharo study reports average syntax-error reduction of 33%. These metrics cannot be ranked on one scale.

The DEP-E is strong because it preserves negative evidence. None of the benchmarks was independently reproduced. The clinical work does not establish prospective utility. The privacy work does not prove cryptographic security. Several quantum contributions are simulated, conceptual, or small-scale. The materials and CMOS results depend on modeled systems and parameter regimes. The code result is language- and resource-specific.

Reviewer judgment: the composite merits archival intake because it turns heterogeneous discovery into a disciplined evidence ledger. Its durable contribution is a state-admission question: before a state may control an action, what provenance, authority, validity, uncertainty, reversibility, and monitoring evidence must be attached? The main danger is analogy overreach. Similar governance vocabulary does not imply shared mechanisms, transferable effect sizes, or equivalent maturity.

## 1. Problem framing and research question

Technical systems increasingly combine persistent software state with specialized physical computation. An agent reads a repository and decides whether to mutate it. A memory system carries prior content into future tasks. A trained model encodes information about its data lineage. A clinical learner adapts across cohorts. A quantum or electronic device realizes computation only within a physical model and measurement regime. In every case, downstream behavior depends on what state is accepted as valid.

The source record asks whether a mixed set of new studies can be synthesized without erasing their evidence boundaries. Its answer is a ledger: record the state, how it was produced, what it is authorized to influence, what evidence supports it, where it is valid, and what failures remain.

The ten-study bundle can be grouped into three questions.

1. **Governance:** How do systems control repository mutation, memory, privacy lineage, and continual adaptation?
2. **Representation:** How do physical or learned representations preserve, transmit, compare, or compress relevant state?
3. **Validity:** Which result type—synthetic benchmark, retrospective cohort, simulation, analytical model, laboratory measurement, or code evaluation—supports which conclusion?

The source does not claim that “state” has one formal definition across all studies. In an agent it may be a repository snapshot and control policy. In privacy it may be model parameters that retain training-family signatures. In materials it may be an atomic configuration. In quantum experiments it is a density operator or encoded optical state. The synthesis operates at the assurance level: all require provenance and validity checks before downstream use.

## 2. Formal and technical reconstruction

### 2.1 HCRC: repository state as an authority boundary

The HCRC study, as represented by the DEP-E, proposes a hierarchical controller for repository-aware agent behavior. The system observes repository and task state, constrains available operations, and evaluates actions against thresholds. Its evidence is a deterministic synthetic task set rather than uncontrolled production repositories. The reported mechanism is useful because it treats mutation authority as an explicit control variable, not an emergent property of a language model’s confidence.

The key assurance object is a state transition `(repository_before, action, repository_after)` with policy and evidence. A high benchmark score can show consistency on covered cases but cannot demonstrate safety under novel tools, malicious instructions, ambiguous ownership, or race conditions.

### 2.2 MRMS: memory as governed carryover

MRMS manages memory across long-running agent interactions. The DEP-E reports invariants, a prototype, ablations, and 98.8% success on 800 deterministic synthetic tasks. Memory is not merely retrieval. It requires admission, consolidation, update, conflict handling, and expiration. A false or unauthorized memory can contaminate many later actions.

The source’s central assurance insight is that memory entries should carry origin, scope, confidence, and lifecycle. Synthetic tasks can test invariant enforcement, but they may not capture semantic ambiguity, adversarial memory poisoning, or long-horizon drift.

### 2.3 PRIME and ODMM: released models as lineage state

The privacy paper studies whether an adversary can infer relationships among datasets by observing models trained on them. The DEP-E describes an ODMM formulation and PRIME attack, evaluates datasets and defenses, and records a best single-comparison AUC increase from .793 to .925 on UTKFace. This shows that model release can expose information about dataset composition or relationship beyond ordinary membership of one example.

The evidence is attack performance under specified access, models, and datasets. It is not a cryptographic proof of leakage for all settings. AUC measures ranking discrimination, not operational harm by itself. Defenses must be evaluated against adaptive attacks and utility loss.

### 2.4 MergeSurv: clinical learning state across cohorts

MergeSurv addresses continual survival learning, where models adapt across clinical cohorts while seeking to preserve prior capability. The DEP-E reports four-cohort retrospective experiments and multiple metrics. VEA reaches a C-index of .6773 and forgetting of .0138 in one reported comparison, while EWC leads one IPCW measure. This mixed result warns against declaring one universal winner.

Continual clinical state includes parameters, replay or regularization mechanisms, cohort order, censoring, calibration, and historical performance. Retrospective predictive metrics do not establish prospective clinical benefit, treatment effect, fairness, or safety.

### 2.5 Perovskite passivation: atomic configuration as modeled state

The materials study compares modeled passivation strategies, including a hyP-26/D2 pipeline, and evaluates structural or electronic consequences through computation. The DEP-E tracks fitting comparisons, simulations, and supplemental errors. The important boundary is that calculated configurations and energies depend on functional choices, parameterization, finite cells, defect assumptions, and convergence.

The state-admission question is whether a computed structure is sufficiently converged and experimentally plausible to guide synthesis. Simulation can prioritize candidates but does not by itself establish device stability or manufacturing yield.

### 2.6 Rydberg hashing: encoded many-body state

The Rydberg study proposes quantum hashing through atomic encoding, simulated collision behavior, decoding, tamper analysis, and privacy discussion. The DEP-E labels the evidence as simulated and does not promote it to cryptographic security. A useful hash requires precise security definitions: collision resistance, preimage resistance, adversary access, noise, reproducibility, and verification cost.

Physical distinctness of quantum states is not automatically a cryptographic guarantee. Simulation under a chosen noise model is evidence about that model, not all implementations or adversaries.

### 2.7 Telecom cluster states: measured photonic substrate

The photonic study reports a telecom-band cluster-state experiment. The DEP-E preserves process fidelity `.71 ± .01`, negativity `.27 ± .02`, and indistinguishability at least `.83`. These are laboratory measurements with uncertainty, unlike the preceding simulations. They establish realized nonclassical performance within the device and protocol, not fault-tolerant scalable computation.

Loss, source brightness, mode matching, detector efficiency, multiphoton contamination, and reconstruction assumptions determine how the measured state can be used. The substrate is inseparable from the claimed computation.

### 2.8 Path-superposition gates: conceptual photonic control

The path-superposition paper develops gate-teleportation protocols, including CNOT/CZ constructions and a photonic realization outline. The DEP-E correctly labels the evidence as conceptual rather than a completed device demonstration. Circuit identities can be correct while resource overhead, loss tolerance, feed-forward timing, and fabrication remain unresolved.

The relevant state is distributed across path modes and entanglement resources. Operational validity requires both mathematical protocol correctness and a substrate capable of preserving coherence and measurement control.

### 2.9 CMOS PK-GF: reduced electrostatics linked to spin models

The CMOS paper couples a Poisson-kernel Green-function electrostatic approximation with finite-volume comparisons and quantum calculations. The DEP-E reports a matched two-dimensional RMSE of 1.134 mV for PK-GF versus 239.453 and 46.017 mV for comparison approximations. The gain is striking within that case, but scope matters: geometry, boundary conditions, dimensional reduction, and coupling to UHF/CASCI calculations define validity.

A reduced solver is valuable when its error is measured against a trusted reference and its domain is explicit. It should not be assumed accurate for arbitrary three-dimensional device layouts or charge regimes.

### 2.10 Pharo completion: code-model state under scarcity

The Pharo study evaluates code completion in a low-resource language and reports an average 33% reduction in syntax errors under its method. The DEP-E tracks the data pipeline, benchmarks, latency, and validity threats. The result indicates that language-specific training or constraints can improve syntactic validity, not that semantic correctness or maintainability is solved.

Training-data provenance is part of the model state. Duplication, project leakage, temporal splits, and licensing can change interpretation. Syntax-error reduction should be paired with exact match, compilation, tests, developer usefulness, and latency.

## 3. Evaluation design and evidence reconstructed

The source DEP-E performs a full-text evidence check for all ten papers and records a reference table with access boundaries.[^dep] It distinguishes synthetic agent evaluation, model-inference privacy experiments, retrospective clinical cohorts, computational materials modeling, quantum simulation, measured photonics, conceptual protocols, reduced-order device validation, and code benchmarks. This evidence-regime labeling is the composite’s primary methodological strength.

The current intake read both tracked files end to end. It did not independently re-open the ten primary papers, and therefore every detailed study claim remains DEP-E-reported. The primary object is the complete repository bundle: its inventory, cross-study synthesis, quantitative extracts, limitations, implementation ideas, exercises, minimum viable program, related reading, and appendix.

Cross-study evaluation cannot use a pooled effect size. The outcomes have different units, baselines, sample structures, and uncertainty. Instead, this review evaluates each result on five axes: evidence type, comparison target, uncertainty, external validity, and downstream claim. A synthetic 98.8% score can be precise but narrow. A laboratory fidelity with error bars can be directly measured but device-specific. A retrospective C-index can be clinically situated but not prospective utility.

The bundle’s evidence ledger is therefore more important than its thematic narrative. The narrative helps discovery; the ledger prevents a reader from upgrading simulation to experiment or benchmark performance to deployment readiness.

## 4. Results and quantitative audit

The reported values should be read within their own regimes.

- **MRMS:** 98.8% on 800 deterministic synthetic tasks, with a reported 98.0–99.4 interval. This indicates high covered-task success. Determinism and synthetic construction limit environmental generalization.
- **PRIME:** best single UTKFace AUC comparison rises from .793 to .925. The absolute increase is .132. AUC does not specify a deployment threshold, prevalence, or attack cost.
- **MergeSurv:** VEA C-index .6773 and forgetting .0138 in reported comparisons; EWC leads one IPCW measure. The multi-metric result does not identify a universal winner.
- **Photonic cluster state:** fidelity `.71 ± .01`, negativity `.27 ± .02`, indistinguishability `>= .83`. These measured quantities support nonclassical state quality within reported definitions and reconstruction.
- **CMOS PK-GF:** RMSE 1.134 mV versus 239.453 and 46.017 mV in a matched 2D comparison. Ratios are large, but extrapolation beyond that geometry is not justified.
- **Pharo:** average syntax-error reduction 33%. Baseline, task distribution, and semantic correctness determine practical importance.

The remaining studies are represented more by architectural or simulation outcomes than one headline number in the DEP-E synthesis. Absence of a number in this intake is not evidence of no evaluation; it reflects the bundle-level emphasis and current evidence boundary.

No cross-source confidence interval is meaningful. Nor should the ten papers be ranked by numerical magnitude. AUC, C-index, fidelity, RMSE, and syntax-error reduction answer different questions. The appropriate quantitative output is a typed ledger, not an average.

## 5. Ablations and missing discriminators

Each study has different missing controls.

- HCRC and MRMS need adversarial, ambiguous, concurrent, and real-repository/task tests beyond deterministic synthetic suites.
- PRIME needs adaptive attacks, additional model families, dataset shifts, calibrated operating points, and defense utility curves.
- MergeSurv needs cohort-order sensitivity, external sites, prospective validation, calibration, subgroup results, and clinical-decision analysis.
- Perovskite modeling needs method sensitivity, convergence, experimental synthesis, defect diversity, and device-level stability.
- Rydberg hashing needs formal security games, hardware noise, adversary models, scale analysis, and experimental implementation.
- Telecom photonics needs loss budgets, rate/scalability analysis, independent state characterization, and system integration.
- Path-superposition gates need resource accounting, fault/error models, feed-forward timing, and device demonstration.
- CMOS PK-GF needs broader three-dimensional geometries, boundary conditions, charge regimes, and end-to-end quantum-property error.
- Pharo completion needs project-disjoint temporal splits, compilation/tests, semantic metrics, human evaluation, and licensing audit.

The composite itself needs an analogy ablation: remove the shared “state and substrate” framing and ask whether the evidence ledger remains useful. If the synthesis adds only rhetoric, study-specific conclusions should be unchanged. If it adds value, it should produce concrete, testable governance requirements across multiple domains.

## 6. Claim-by-claim vetting

| Claim | Evidence | Assessment |
|---|---|---|
| Explicit state governance recurs across the ten studies. | DEP-E reviewer synthesis of complete primary-paper reviews. | Supported as a cross-domain organizing interpretation, not a shared formal theorem. |
| HCRC and MRMS demonstrate high reliability. | Synthetic-task results, including MRMS 98.8% on 800 tasks. | Supported only for covered deterministic tasks; production safety unproven. |
| Released models can leak dataset relationships. | PRIME attack results, including reported AUC improvement. | Supported under specified experiments; not universal or cryptographic proof. |
| MergeSurv solves continual clinical survival learning. | Retrospective four-cohort metrics with mixed method leadership. | Overstated; it contributes methods and evidence, not clinical resolution. |
| Physical substrate constraints materially determine quantum and CMOS performance. | Simulated, analytical, and measured study results. | Strong general principle; each quantitative claim remains system-specific. |
| Photonic metrics demonstrate scalable fault-tolerant computation. | Small-scale process fidelity, negativity, and indistinguishability. | Unsupported. |
| PK-GF is universally more accurate than alternatives. | Large RMSE advantage in one matched 2D comparison. | Unsupported beyond evaluated regimes. |
| Pharo syntax improvement establishes semantic code quality. | 33% average syntax-error reduction. | Unsupported without tests and semantic evaluation. |
| The ten-paper synthesis is a unified theory. | No common formal model or pooled experiment. | Rejected; it is an assurance heuristic and evidence ledger. |

## 7. External primary-source context

The source record identifies ten canonical arXiv records: HCRC `2607.04562`, MRMS `2607.04617`, PRIME `2607.05111`, MergeSurv `2607.04747`, perovskite passivation `2607.05321`, Rydberg hashing `2607.04991`, telecom cluster states `2607.04896`, path-superposition gates `2607.04672`, CMOS modeling `2607.04876`, and Pharo completion `2607.04939`.[^hcrc][^mrms][^prime][^merge][^physical]

The DEP-E appendix states that all ten complete papers were inspected and that major quoted metrics were checked against primary tables, captions, or results text. It also records that temporary PDFs were withheld and no payload was deposited. The present intake preserves that provenance but does not claim to repeat it.

All ten are v1 preprints in the source’s narrow collection window. Version status is material. Later revisions may alter methods, numbers, authorship, limitations, or conclusions. A correction intake should use a new source commit and pair indicator if the DEP-E source state materially changes.

The composite context is strongest when it routes readers back to individual primary sources. It is weakest if the thematic synthesis becomes a substitute for them. Accordingly, this DEP-A does not add publication-index rows: it did not independently re-review the ten complete external papers in the current intake.

## 8. Research notes, caveats, and code/reproducibility status

No study was independently reproduced in this run. No code repository, dataset, patient data, materials model, quantum circuit, device data, solver, or language model was accessed or executed. The source DEP-E reports full-paper inspection, not executable verification.

The studies differ in maturity. HCRC and MRMS are synthetic prototypes. PRIME is an offensive privacy evaluation that must be handled defensively and within authorized data/model access. MergeSurv is retrospective medical research. The materials and CMOS studies rely on modeling choices. One quantum study is simulated, one is a measured experiment, and one is a conceptual protocol. Pharo evaluation is a bounded software benchmark.

Cross-domain language can conceal this maturity gradient. “State,” “memory,” “fidelity,” “validity,” and “error” have domain-specific definitions. Every reuse should carry units, metric definitions, baseline, version, and threat or operating model.

The source’s minimum viable program is useful as planning, not evidence. Implementation ideas and exercises are explicitly proposals. They should not be misreported as systems built or tested by the paper authors.

## 9. Independent re-conceptualization

The ten-study synthesis can be made operational through a **state-admission gate**. Before any state influences a consequential action, record seven fields:

1. **Identity:** what state object is being admitted, at which version and granularity?
2. **Provenance:** which observations, data, model, process, or device produced it?
3. **Authority:** which actions or inferences may it influence, and who granted that scope?
4. **Validity regime:** under which environment, geometry, cohort, threat model, or hardware conditions is it supported?
5. **Uncertainty:** what error, confidence, calibration, or unresolved ambiguity accompanies it?
6. **Reversibility:** can the resulting action be rolled back, corrected, or isolated?
7. **Monitoring:** what signal detects drift, leakage, decoherence, model mismatch, or invalidation?

This gate applies differently by domain. Repository state needs clean-worktree and permission checks. Memory needs conflict and expiration rules. Privacy evaluation needs authorized access and threat models. Clinical state needs cohort, calibration, and governance. Simulated physical state needs model and convergence evidence. Measured quantum state needs calibration and uncertainty. Code-model state needs data lineage and executable tests.

The gate does not make results comparable; it makes their admissibility conditions comparable. That is the core reviewer inference. A typed state ledger can then prevent an action from relying on evidence outside its regime. For example, a simulated Rydberg collision rate cannot authorize a production cryptographic claim, and a retrospective C-index cannot authorize autonomous clinical treatment.

## 10. Implications and failure modes

For agent systems, the synthesis argues for explicit authority and provenance at every state transition. For research intelligence, it argues for evidence-type labels and versioned primary links. For physical computing, it argues that algorithmic claims must include substrate assumptions. For governance, it provides a common review checklist without pretending that one test fits all domains.

Failure modes include:

1. **Analogy laundering:** a shared word such as “state” implies evidence transfer across domains.
2. **Metric flattening:** incomparable values are ranked or averaged.
3. **Simulation promotion:** modeled performance is described as experimental realization.
4. **Benchmark promotion:** synthetic success is described as production safety.
5. **Clinical promotion:** retrospective discrimination is described as utility or benefit.
6. **Security promotion:** attack AUC or quantum distinctness is described as cryptographic proof.
7. **Version drift:** v1 claims persist after material paper revisions.
8. **Authority omission:** a state is technically available and therefore treated as authorized.
9. **Substrate omission:** geometry, noise, loss, device, or solver assumptions disappear from summaries.
10. **Irreversible action:** uncertain state triggers mutation without rollback or review.

Mitigation is a typed ledger with explicit claim ceilings. Each row states the strongest conclusion the evidence can support and the next test required to raise that ceiling.

## 11. Replication, falsification, and hypothesis agenda

The following are reviewer proposals.

**H1 — State-admission metadata reduces unsafe agent transitions.** Agents required to verify identity, provenance, authority, uncertainty, and reversibility before mutation will cause fewer unauthorized or invalid changes than agents given untyped context. Falsification: no improvement on adversarial real-repository tasks at equal completion rates.

**H2 — Typed evidence ledgers reduce claim inflation.** Reviewers using evidence-regime and claim-ceiling fields will make fewer simulation-to-deployment and benchmark-to-utility errors than reviewers using narrative summaries alone. Falsification: no difference in blinded claim-classification studies.

**H3 — Memory provenance improves long-horizon correction.** Memory systems with source, scope, conflict, and expiration fields will recover from injected false memories faster than vector retrieval without governance. Falsification: no improvement across realistic multi-session tasks.

**H4 — Substrate residuals predict transfer failure.** Physical-computing results with larger model-to-device residuals will show larger degradation when moved from simulation or reduced models to hardware. Falsification: residual magnitude does not predict transfer across preregistered systems.

**H5 — Claim ceilings improve interdisciplinary synthesis.** Explicit maximum supported claims will preserve more accurate downstream summaries without reducing useful cross-domain insight. Falsification: readers gain no accuracy or lose substantial comprehension.

Replication must remain study-specific. Reproduce HCRC/MRMS on real and adversarial tasks; rerun PRIME under authorized, adaptive threat models; validate MergeSurv across sites and prospectively; test materials predictions experimentally; formalize and implement quantum protocols at increasing scale; reproduce photonic tomography and loss budgets; benchmark CMOS approximations across geometries; and rerun Pharo evaluation with project-disjoint data and executable tests.

For the composite, create a preregistered extraction protocol. Two reviewers independently label evidence type, claim ceiling, metric, uncertainty, and external-validity boundary. Resolve disagreements and measure whether the final state-admission fields predict which results replicate or transfer.

## 12. Durable restatement

The complete DEP-E record supports a disciplined synthesis of ten distinct studies. Their shared lesson is not that software and physical systems obey one theory. It is that consequential state must carry evidence about where it came from, what it may control, where it remains valid, and how failure will be detected.

The quantitative results remain local: synthetic agent success, privacy AUC, retrospective clinical metrics, modeled material and CMOS performance, simulated or conceptual quantum behavior, measured photonic properties, and code-benchmark improvement. None can be upgraded beyond its evidence regime, and none was reproduced here.

The reviewer’s durable contribution is the state-admission gate: identity, provenance, authority, validity regime, uncertainty, reversibility, and monitoring. Used as a typed ledger, it preserves cross-domain insight while blocking analogy and maturity inflation.

## 13. Source and evidence notes

### Complete inventory and source integrity

| Item | Inspection | Role | Integrity assessment |
|---|---|---|---|
| Source `README.md` | Read end to end | Identity, source DEP lineage, inventory, summary, ten primary links, attribution | Complete public boundary and routing. |
| `state-and-substrate.md` | Read end to end | Ten-study reconstruction, metrics, limitations, proposals, evidence ledger, appendix | Complete composite DEP report; reports full-paper inspection for all ten sources. |
| Ten canonical primary records | Not independently reopened | Original studies listed by the DEP-E | Detailed claims remain DEP-E-reported. |
| Generated review | New derived artifact | Intake, evidence-regime audit, state-admission reconceptualization | Original prose; no source copied. |

### Coverage ledger

| Source dimension | Coverage in this review | Boundary |
|---|---|---|
| HCRC and MRMS | Technical reconstruction, metrics, controls | Synthetic evidence preserved. |
| PRIME privacy | Technical reconstruction, metrics, claims | Defensive review; no attack executed. |
| MergeSurv | Technical reconstruction, metrics, limitations | Retrospective clinical boundary preserved. |
| Perovskite modeling | Technical reconstruction and controls | Computational evidence, no experiment. |
| Rydberg hashing | Technical reconstruction and claims | Simulated; no cryptographic proof. |
| Telecom cluster state | Technical reconstruction and metrics | Measured small-scale evidence. |
| Path-superposition gates | Technical reconstruction and controls | Conceptual protocol, no device demonstration. |
| CMOS PK-GF | Technical reconstruction and metrics | Matched 2D scope explicit. |
| Pharo completion | Technical reconstruction and metrics | Syntax result not semantic certification. |
| Cross-study observations | Executive, reconceptualization, implications | Reviewer synthesis, not common theorem. |
| Proposals, exercises, MVP | Research notes and replication | Preserved as proposals only. |
| References and appendix | External context, footnotes, README attribution | No paper, data, code, or cache uploaded. |

### Evidence boundary

The complete DEP-E report is the source for all ten paper-level reconstructions, metrics, tables, figures, and limitations. The current intake directly inspected the repository bundle, not the ten external full papers. Reviewer inference includes the state-admission gate, claim-ceiling proposal, cross-domain hypotheses, and failure taxonomy. No benchmark, attack, clinical analysis, simulation, device, solver, or code model was independently reproduced.

Each paper reports study-specific results through the complete inspection boundary documented by the DEP-E.[^boundary] The one-way paired record preserves review-only provenance and confirms that no source file was transferred.[^provenance]

## 14. Footnotes

[^dep]: Complete source record, https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-State%20and%20Substrate, inspected at commit `b5ad2459a6ee3d649feb8209d9390d86d475502c`.
[^hcrc]: HCRC primary record, https://arxiv.org/abs/2607.04562.
[^mrms]: MRMS primary record, https://arxiv.org/abs/2607.04617.
[^prime]: PRIME privacy-composition primary record, https://arxiv.org/abs/2607.05111.
[^merge]: MergeSurv primary record, https://arxiv.org/abs/2607.04747.
[^physical]: Primary physical/computing records: https://arxiv.org/abs/2607.05321, https://arxiv.org/abs/2607.04991, https://arxiv.org/abs/2607.04896, https://arxiv.org/abs/2607.04672, https://arxiv.org/abs/2607.04876, and https://arxiv.org/abs/2607.04939.
[^boundary]: The DEP-E appendix states that complete full text was inspected for all ten papers and quoted metrics were checked against primary displays or results. This intake did not repeat that work.
[^provenance]: Paired task `BL-DEPPAIR-20260716-0095B1FD` records review-only derivation; no DEP-E file was modified, moved, or copied.
