# Report-Mark: Group-based control of

- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P57`
- Review date: 2026-08-19

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Group-based control of large-scale micro-robot swarms with on-board Physical Finite-State Machines* |
| Authors | Li, Siyu; Zefran, Milos; Paprotny, Igor |
| Identifier | arXiv:2208.08614; DOI:10.48550/arXiv.2208.08614 |
| Submitted / source date | 2022/08/18 |
| Record | https://arxiv.org/abs/2208.08614 |
| Full paper | https://arxiv.org/html/2208.08614 |
| PDF | https://arxiv.org/pdf/2208.08614 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Research focus | ML memory, stateful systems, and algorithmic research; matched stateful systems; evidence terms: finite state. |
| Deployment IDs | `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P57` |

## Concise Research Notes

The paper addresses control, finite-state, group-based. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “In [ 15 ] , Global Control Selective Response (GCSR) approach was proposed that relies on the separation …”. A short evaluation anchor is: “An important problem in microrobotics is how to control a large group of microrobots with a global control …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “MicroStressBot control has been successfully implemented in [ 15 ] . It has been shown that if the …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md` - Group-Control Swarms - DEP-E; overlap: swarms, finite-state, machines, physical, control.
2. `.lake-data/DEP-E/DEP-E-20260819-Listwise Policy/listwise_policy_manuscript.md` - Listwise Policy - DEP-E; overlap: group-based, control.
3. `.lake-data/DEP-E/DEP-E-20260819-LLM-FSM Scaling Large/llm_fsm_scaling_large_manuscript.md` - LLM-FSM Scaling Large - DEP-E; overlap: finite-state, large-scale, control.

## Synthesis Note

### Concept Bridge

The selected paper contributes a control, finite-state, group-based perspective. The three related DEPs overlap concretely through control, finite-state, group-based, large-scale, machines. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for control that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's finite-state mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Group-Control Swarms - DEP-E overlaps through swarms, finite-state, machines, physical, control, clarifying a neighboring representation or evidence choice.
2. Listwise Policy - DEP-E overlaps through group-based, control, exposing a complementary evaluation or operating boundary.
3. LLM-FSM Scaling Large - DEP-E overlaps through finite-state, large-scale, control, showing how implementation assumptions affect practical transfer.

### Conceptual Similarities

1. All four artifacts transform raw inputs into intermediate evidence rather than direct truth claims.
2. Each depends on explicit assumptions about data, representation, evaluation, and scope.
3. Each benefits from auditable versioning, negative controls, uncertainty, and failure-aware interpretation.

### MVP Implementations with Code Mock-Ups

1. Evidence map: `record = evaluate(input, config); require(record.provenance)`.
2. Frozen comparison: `scores = compare(baselines, candidate, split_manifest)`.
3. Abstention gate: `decision = review if drift or low_confidence else nonbinding_output`.

### Developer Challenges

1. Reproducing preprocessing, baselines, and metrics without leakage or silent version drift.
2. Preserving evidence lineage while keeping evaluation maintainable and privacy-aware.
3. Designing stable explanations and stop conditions outside the tested envelope.

### Author Challenges

1. Publishing enough configuration, data, and ablation detail for independent replication.
2. Separating benchmark improvement from claims of generalization or deployment readiness.
3. Reporting negative results, sensitivity, uncertainty, and failure cases alongside headline metrics.

## Validation Notes

- Deployment IDs validated: `BLAD-2200-20260819-8DFEF0DE`; `BLAD-2200-20260819-8DFEF0DE-P57`.
- Uniform draw index 33,160 of 75,964 units; duplicate exclusions 2; focus exclusions 27; reselections 29.
- One-time research-focus gate passed for ML memory, stateful systems, and algorithmic research; matched categories: stateful systems; terms: finite state.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2208.08614 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2208.08614 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2208.08614 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2208.08614 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260729-Group%20Control%20Swarms - related DEP: Group-Control Swarms - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260729-Group Control Swarms/group_control_swarms_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260819-Listwise%20Policy - related DEP: Listwise Policy - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-Listwise Policy/listwise_policy_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20002/DEP-E-20260819-LLM-FSM%20Scaling%20Large - related DEP: LLM-FSM Scaling Large - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260819-LLM-FSM Scaling Large/llm_fsm_scaling_large_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
