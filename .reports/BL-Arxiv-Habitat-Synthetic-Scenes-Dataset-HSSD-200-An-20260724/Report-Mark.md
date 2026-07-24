# Report-Mark: Habitat Synthetic Scenes

- Deployment job ID: `BLAD-2200-20260724-CF53BCCB`
- Deployment item ID: `BLAD-2200-20260724-CF53BCCB-P03`
- Review date: 2026-07-24

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Habitat Synthetic Scenes Dataset (HSSD-200): An Analysis of 3D Scene Scale and Realism Tradeoffs for ObjectGoal Navigation* |
| Authors | Khanna, Mukul; Mao, Yongsen; Jiang, Hanxiao; Haresh, Sanjay; Shacklett, Brennan; Batra, Dhruv; Clegg, Alexander; Undersander, Eric; Chang, Angel X.; Savva, Manolis |
| Identifier | arXiv:2306.11290; DOI:10.48550/arXiv.2306.11290 |
| Submitted / source date | 2023/06/20 |
| Record | https://arxiv.org/abs/2306.11290 |
| Full paper | https://arxiv.org/html/2306.11290v1 |
| PDF | https://arxiv.org/pdf/2306.11290 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260724-CF53BCCB`; `BLAD-2200-20260724-CF53BCCB-P03` |

## Concise Research Notes

The paper addresses scenes, agents, scene. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Asset compression. After the above annotation was performed, all object assets were compressed to reduce GPU memory requirements …”. A short evaluation anchor is: “We contribute the Habitat Synthetic Scenes Dataset (HSSD-200), a dataset of 211 high-quality 3D scenes, and use it …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “Despite this, there has been limited work investigating the use of multi-room synthetic scenes for training ObjectNav agents. …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260710-BEAGLE Learner/beagle_learner_manuscript.md` - BEAGLE Learner - DEP-E; overlap: making, realism, fidelity, quickly, realistic.
2. `.lake-data/DEP-E/DEP-E-20260720-VG Navigable Space/vg_navigable_space_manuscript.md` - VG Navigable Space Review - DEP-E; overlap: navigation, environments, real-world, real, visual.
3. `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md` - SAGE-Nav Review - DEP-E; overlap: navigation, quickly, scene, zero-shot, real.

## Synthesis Note

### Concept Bridge

The selected paper contributes a scenes, agents, scene perspective. The three related DEPs overlap concretely through environments, fidelity, making, navigation, quickly. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for scenes that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's agents mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. BEAGLE Learner - DEP-E overlaps through making, realism, fidelity, quickly, realistic, clarifying a neighboring representation or evidence choice.
2. VG Navigable Space Review - DEP-E overlaps through navigation, environments, real-world, real, visual, exposing a complementary evaluation or operating boundary.
3. SAGE-Nav Review - DEP-E overlaps through navigation, quickly, scene, zero-shot, real, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 16,587 of 75,777 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2306.11290 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2306.11290v1 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2306.11290 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2306.11290 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260710-BEAGLE%20Learner - related DEP: BEAGLE Learner - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260710-BEAGLE Learner/beagle_learner_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260720-VG%20Navigable%20Space - related DEP: VG Navigable Space Review - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260720-VG Navigable Space/vg_navigable_space_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav%20Review - related DEP: SAGE-Nav Review - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
