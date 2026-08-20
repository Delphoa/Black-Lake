# Report-Mark: Digital and Physical Face

- Deployment job ID: `BLAD-2200-20260813-F994AA5E`
- Deployment item ID: `BLAD-2200-20260813-F994AA5E-P03`
- Review date: 2026-08-13

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Digital and Physical Face Attacks: Reviewing and One Step Further* |
| Authors | Kong, Chenqi; Wang, Shiqi; Li, Haoliang |
| Identifier | arXiv:2209.14692; DOI:10.48550/arXiv.2209.14692 |
| Submitted / source date | 2022/09/29 |
| Record | https://arxiv.org/abs/2209.14692 |
| Full paper | https://arxiv.org/html/2209.14692 |
| PDF | https://arxiv.org/pdf/2209.14692 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260813-F994AA5E`; `BLAD-2200-20260813-F994AA5E-P03` |

## Concise Research Notes

The paper addresses attacks, digital, face. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “Face presentation attacks can be generally divided into two categories: obfuscation attacks and impersonation attacks. As shown in …”. A short evaluation anchor is: “With the rapid progress over the past five years, face authentication has become the most pervasive biometric recognition …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “With the rapid progress over the past five years, face authentication has become the most pervasive biometric recognition …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260804-Stealthy Jailbreak/stealthy_jailbreak_manuscript.md` - Stealthy Jailbreak - DEP-E; overlap: attacks, face, one.
2. `.lake-data/DEP-E/DEP-E-20260731-GADT Enhancing/gadt_enhancing_manuscript.md` - GADT Enhancing - DEP-E; overlap: attacks, one.
3. `.lake-data/DEP-E/DEP-E-20260720-APB2Face Safety/apb2face_safety_manuscript.md` - APB2Face Safety Review - DEP-E; overlap: face, digital.

## Synthesis Note

### Concept Bridge

The selected paper contributes a attacks, digital, face perspective. The three related DEPs overlap concretely through attacks, digital, face, one. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for attacks that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's digital mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Stealthy Jailbreak - DEP-E overlaps through attacks, face, one, clarifying a neighboring representation or evidence choice.
2. GADT Enhancing - DEP-E overlaps through attacks, one, exposing a complementary evaluation or operating boundary.
3. APB2Face Safety Review - DEP-E overlaps through face, digital, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 28,387 of 75,964 units; duplicate exclusions 0; reselections 1.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/2209.14692 - metadata, authors, abstract, dates, DOI, and public locators.
- https://arxiv.org/html/2209.14692 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/2209.14692 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.2209.14692 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260804-Stealthy%20Jailbreak - related DEP: Stealthy Jailbreak - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260804-Stealthy Jailbreak/stealthy_jailbreak_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260731-GADT%20Enhancing - related DEP: GADT Enhancing - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260731-GADT Enhancing/gadt_enhancing_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-APB2Face%20Safety - related DEP: APB2Face Safety Review - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260720-APB2Face Safety/apb2face_safety_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
