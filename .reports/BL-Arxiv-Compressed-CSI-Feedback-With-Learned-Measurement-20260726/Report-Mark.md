# Report-Mark: Compressed CSI Feedback

- Deployment job ID: `BLAD-2200-20260726-1DBD5211`
- Deployment item ID: `BLAD-2200-20260726-1DBD5211-P01`
- Review date: 2026-07-26

## Source Metadata

| Field | Value |
|---|---|
| Paper | *Compressed CSI Feedback With Learned Measurement Matrix for mmWave Massive MIMO* |
| Authors | Wu, Pengxia; Liu, Zichuan; Cheng, Julian |
| Identifier | arXiv:1903.02127; DOI:10.48550/arXiv.1903.02127 |
| Submitted / source date | 2019/03/06 |
| Record | https://arxiv.org/abs/1903.02127 |
| Full paper | https://ar5iv.labs.arxiv.org/html/1903.02127 |
| PDF | https://arxiv.org/pdf/1903.02127 |
| Source state | Verified complete after one bounded local archive repair; source files withheld locally. |
| Deployment IDs | `BLAD-2200-20260726-1DBD5211`; `BLAD-2200-20260726-1DBD5211-P01` |

## Concise Research Notes

The paper addresses measurement, matrix, csi. The inspected full paper contains explicit method, evaluation, limitation, conclusion, and reference structure beyond the abstract. A short method evidence anchor is: “A major challenge to implement the compressed sensing method for channel state information (CSI) acquisition lies in the …”. A short evaluation anchor is: “Unfortunately, the widely adopted randomized measurement matrices drawn from Gaussian or Bernoulli distribution are not optimal for all …”. These anchors preserve traceability; they do not constitute independent reproduction.

The source positions its named approach as a response to the problem encoded by its title and abstract. A limitation-oriented anchor is: “A major challenge to implement the compressed sensing method for channel state information (CSI) acquisition lies in the …”. The reviewer interpretation is bounded: transfer requires versioned inputs, baseline parity, leakage checks, uncertainty handling, and failure-condition testing.

## Evidence and Attribution

| Evidence | Supports | Limits |
|---|---|---|
| Official metadata and abstract | Identity, authors, dates, DOI, and problem framing | Abstract is metadata-level evidence |
| Verified full-paper HTML and PDF integrity | Method, evaluation, limitations, conclusion, and section structure | Implementation and experiments were not rerun |
| Author-reported evaluation material | Evidence claimed in the source setting | No independent reproduction or target-domain validation |
| Source-integrity record | Complete PDF and structured full-paper HTML | Document integrity does not prove research claims |

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - Acoustic Phase Retrieval - DEP-E; overlap: recovery, problem.
2. `.lake-data/DEP-E/DEP-E-20260713-SMES Expert Sparsity/smes_expert_sparsity_manuscript.md` - SMES Expert Sparsity - DEP-E; overlap: sparsity, sparse.
3. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: compression, sparse.

## Synthesis Note

### Concept Bridge

The selected paper contributes a measurement, matrix, csi perspective. The three related DEPs overlap concretely through compression, problem, recovery, sparse, sparsity. Together they support a provenance-first workflow separating primary-source claims, reviewer interpretation, experimental validation, and deployment decisions.

### Potential Implementations

1. Build an offline evidence extractor for measurement that maps each output to a source section, configuration, and uncertainty record.
2. Create a frozen comparison harness for the paper's matrix mechanism against simple baselines and negative controls.
3. Add an abstaining review gate that blocks downstream use when provenance, calibration, privacy, or shift checks fail.

### Deeper Relationship Observations

1. Acoustic Phase Retrieval - DEP-E overlaps through recovery, problem, clarifying a neighboring representation or evidence choice.
2. SMES Expert Sparsity - DEP-E overlaps through sparsity, sparse, exposing a complementary evaluation or operating boundary.
3. CAP Compression - DEP-E overlaps through compression, sparse, showing how implementation assumptions affect practical transfer.

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

- Uniform draw index 18,733 of 75,778 units; duplicate exclusions 0; reselections 0.
- Complete-source gate passed with a verified PDF and full-paper HTML after one bounded local archive repair.
- Source claims and reviewer interpretation are separated; implementation concepts remain offline and nonbinding.
- Exactly three related entries and exactly three items in every required synthesis subsection.
- Public allowlist is Markdown/JSON only; source files are withheld with zero source uploads.

## Attribution Block

- https://arxiv.org/abs/1903.02127 - metadata, authors, abstract, dates, DOI, and public locators.
- https://ar5iv.labs.arxiv.org/html/1903.02127 - verified full-paper evidence; local copy withheld.
- https://arxiv.org/pdf/1903.02127 - verified primary PDF; local copy withheld.
- https://doi.org/10.48550/arXiv.1903.02127 - publisher identifier.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Acoustic%20Phase%20Retrieval - related DEP: Acoustic Phase Retrieval - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-SMES%20Expert%20Sparsity - related DEP: SMES Expert Sparsity - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260713-SMES Expert Sparsity/smes_expert_sparsity_manuscript.md`.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260719-CAP%20Rank%20Sparsity - related DEP: CAP Compression - DEP-E; source basis `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md`.
- Source files: verified PDF, full-paper HTML, metadata HTML, archive source when available, and integrity records; all withheld locally.
