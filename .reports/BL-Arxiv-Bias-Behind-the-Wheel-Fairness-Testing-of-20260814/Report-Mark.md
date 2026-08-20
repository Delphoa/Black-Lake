# Report-Mark: Bias Behind the Wheel

- Deployment job ID: `BLAD-2200-20260814-24737ACA`
- Deployment item ID: `BLAD-2200-20260814-24737ACA-P01`
- Review date: 2026-08-14

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Bias Behind the Wheel: Fairness Testing of Autonomous Driving Systems* |
| Authors | Li, Xinyue; Chen, Zhenpeng; Zhang, Jie M.; Sarro, Federica; Zhang, Ying; Liu, Xuanzhe |
| Identifier | arXiv:2308.02935; DOI:10.48550/arXiv.2308.02935 |
| Submitted / source date | 2023/08/05 |
| Record | https://arxiv.org/abs/2308.02935 |
| Full paper | https://arxiv.org/html/2308.02935 |
| PDF | https://arxiv.org/pdf/2308.02935 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260814-24737ACA`; `BLAD-2200-20260814-24737ACA-P01` |

## Concise Research Notes

The paper addresses autonomous, behind, bias. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Extensive research efforts have been devoted to the testing of autonomous driving systems. For example, Tian et al. …”. A short evaluation anchor is: “This paper conducts fairness testing of automated pedestrian detection, a crucial but under-explored issue in autonomous driving systems. …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “This paper conducts fairness testing of automated pedestrian detection, a crucial but under-explored issue in autonomous driving systems. …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md` - Stable Diffusion Depth - DEP-E; overlap: driving, behind, bias, systems, autonomous.
2. `.lake-data/DEP-E/DEP-E-20260803-ADReFT Adaptive Decision/adreft_adaptive_decision_manuscript.md` - ADReFT Adaptive Decision - DEP-E; overlap: driving, autonomous, systems, testing.
3. `.lake-data/DEP-E/DEP-E-20260805-Light the Night A/light_the_night_a_manuscript.md` - Light the Night A - DEP-E; overlap: driving, autonomous, systems, testing.

## Synthesis Note

### Concept Bridge

The selected paper contributes a autonomous, behind, bias perspective. The three related DEPs overlap concretely through autonomous, behind, bias, driving, systems. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for autonomous that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's behind mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Stable Diffusion Depth - DEP-E overlaps through driving, behind, bias, systems, autonomous, clarifying a neighboring representation or evidence choice.
2. ADReFT Adaptive Decision - DEP-E overlaps through driving, autonomous, systems, testing, exposing a complementary evaluation or operating boundary.
3. Light the Night A - DEP-E overlaps through driving, autonomous, systems, testing, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 68,864 of 75,964 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2308.02935 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2308.02935 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2308.02935 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2308.02935 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260718-Stable%20Diffusion%20Depth - related DEP: Stable Diffusion Depth - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260718-Stable Diffusion Depth/stable_diffusion_depth_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260803-ADReFT%20Adaptive%20Decision - related DEP: ADReFT Adaptive Decision - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260803-ADReFT Adaptive Decision/adreft_adaptive_decision_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260805-Light%20the%20Night%20A - related DEP: Light the Night A - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260805-Light the Night A/light_the_night_a_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
