# Report-Mark: ADReFT Adaptive Decision

- Deployment job ID: `BLAD-2200-20260803-11C1283E`
- Deployment item ID: `BLAD-2200-20260803-11C1283E-P10`
- Review date: 2026-08-03

## Source Metadata

| Field | Value |
|---|---|
| Paper | *ADReFT: Adaptive Decision Repair for Safe Autonomous Driving via Reinforcement Fine-Tuning* |
| Authors | Cheng, Mingfei; Xie, Xiaofei; Wang, Renzhi; Zhou, Yuan; Hu, Ming |
| Identifier | arXiv:2506.23960; DOI:10.48550/arXiv.2506.23960 |
| Submitted / source date | 2025/06/30 |
| Record | https://arxiv.org/abs/2506.23960 |
| Full paper | https://arxiv.org/html/2506.23960 |
| PDF | https://arxiv.org/pdf/2506.23960 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260803-11C1283E`; `BLAD-2200-20260803-11C1283E-P10` |

## Concise Research Notes

The paper addresses adaptive, adreft, autonomous. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “To address this issue, we propose Adaptive Decision Repair ( ADReFT ), a novel and effective repair method …”. A short evaluation anchor is: “Autonomous Driving Systems (ADSs) continue to face safety-critical risks due to the inherent limitations in their design and …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Autonomous Driving Systems (ADSs) continue to face safety-critical risks due to the inherent limitations in their design and …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection/stealth_memory_trust_manuscript.md` - Stealth Memory Trust - DEP-E; overlap: reinforcement, fine-tuning, adaptive, decision.
2. `.lake-data/DEP-E/DEP-E-20260729-Decoupled Training with/decoupled_training_with_manuscript.md` - Decoupled Training with - DEP-E; overlap: reinforcement, fine-tuning, autonomous, decision, safe.
3. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` - LA-Pose Latent Action - DEP-E; overlap: driving, fine-tuning, decision, safe.

## Synthesis Note

### Concept Bridge

The selected paper contributes a adaptive, adreft, autonomous perspective. The three related DEPs overlap concretely through adaptive, autonomous, decision, driving, fine-tuning. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for adaptive that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's adreft mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Stealth Memory Trust - DEP-E overlaps through reinforcement, fine-tuning, adaptive, decision, clarifying a neighboring representation or evidence choice.
2. Decoupled Training with - DEP-E overlaps through reinforcement, fine-tuning, autonomous, decision, safe, exposing a complementary evaluation or operating boundary.
3. LA-Pose Latent Action - DEP-E overlaps through driving, fine-tuning, decision, safe, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 40,072 of 75,957 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2506.23960 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2506.23960 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2506.23960 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2506.23960 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260721-Stealth%20Memory%20Injection - related DEP: Stealth Memory Trust - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection/stealth_memory_trust_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260729-Decoupled%20Training%20with - related DEP: Decoupled Training with - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260729-Decoupled Training with/decoupled_training_with_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-LA-Pose%20Latent%20Action - related DEP: LA-Pose Latent Action - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
