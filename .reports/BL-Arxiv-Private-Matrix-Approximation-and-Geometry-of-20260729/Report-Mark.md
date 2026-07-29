# Report-Mark: Private Matrix

- Deployment job ID: `BLAD-2200-20260729-5EE3EF9C`
- Deployment item ID: `BLAD-2200-20260729-5EE3EF9C-P02`
- Review date: 2026-07-29

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Private Matrix Approximation and Geometry of Unitary Orbits* |
| Authors | Mangoubi, Oren; Wu, Yikai; Kale, Satyen; Thakurta, Abhradeep Guha; Vishnoi, Nisheeth K. |
| Identifier | arXiv:2207.02794; DOI:10.48550/arXiv.2207.02794 |
| Submitted / source date | 2022/07/06 |
| Record | https://arxiv.org/abs/2207.02794 |
| Full paper | https://ar5iv.labs.arxiv.org/html/2207.02794 |
| PDF | https://arxiv.org/pdf/2207.02794 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260729-5EE3EF9C`; `BLAD-2200-20260729-5EE3EF9C-P02` |

## Concise Research Notes

The paper addresses approximation, matrix, private. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Since such matrix approximation problems are often applied to matrices arising from user data (i.e. each user contributes …”. A short evaluation anchor is: “Consider the following optimization problem: Given n × n 𝑛 𝑛 n\times n matrices A 𝐴 A and …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “All the algorithms mentioned above that come with pure differential privacy guarantees utilize the exponential mechanism [ 18 …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-Provably Faster Algorithm/provably_faster_algorithm_manuscript.md` - Provably Faster Algorithms for B - DEP-E; overlap: algorithms, optimization.
2. `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md` - Spiking Pose Tracking - DEP-E; overlap: human, pose.
3. `.lake-data/DEP-E/DEP-E-20260722-GenTune Traceable Prompts/gentune_traceable_prompts_manuscript.md` - GenTune Traceable Prompts Review - DEP-E; overlap: improve, image.

## Synthesis Note

### Concept Bridge

The selected paper contributes a approximation, matrix, private perspective. The three related DEPs overlap concretely through algorithms, human, image, improve, optimization. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for approximation that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's matrix mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Provably Faster Algorithms for B - DEP-E overlaps through algorithms, optimization, clarifying a neighboring representation or evidence choice.
2. Spiking Pose Tracking - DEP-E overlaps through human, pose, exposing a complementary evaluation or operating boundary.
3. GenTune Traceable Prompts Review - DEP-E overlaps through improve, image, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 22,919 of 75,778 units; duplicate exclusions 0; reselections 1.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2207.02794 - metadata, authors, abstract, dates, DOI, and public locators.
- https://ar5iv.labs.arxiv.org/html/2207.02794 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2207.02794 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2207.02794 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260723-Provably%20Faster%20Algorithm - related DEP: Provably Faster Algorithms for B - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260723-Provably Faster Algorithm/provably_faster_algorithm_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260724-Spiking%20Pose%20Tracking - related DEP: Spiking Pose Tracking - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260724-Spiking Pose Tracking/spiking_pose_tracking_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260722-GenTune%20Traceable%20Prompts - related DEP: GenTune Traceable Prompts Review - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260722-GenTune Traceable Prompts/gentune_traceable_prompts_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
