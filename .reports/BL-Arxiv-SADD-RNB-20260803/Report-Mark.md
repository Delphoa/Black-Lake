# Report-Mark: SADD RNB

## Source Metadata

| Field | Value |
|---|---|
| Paper | A Semi-Supervised Adaptive Discriminative Discretization Method Improving Discrimination Power of Regularized Naive Bayes |
| Authors | Shihe Wang; Jianfeng Ren; Ruibin Bai |
| arXiv | 2111.10983v3 |
| arXiv DOI | 10.48550/arXiv.2111.10983 |
| Journal DOI | 10.1016/j.eswa.2023.120094 |
| Venue | Expert Systems with Applications |
| Public version | Submitted 2021-11-22; revised 2023-04-05; publisher record dated 2023-09-01 |
| Review date | 2026-08-03 |
| Source integrity | Complete after one bounded repair; PDF and full-paper HTML verified |
| Distribution | Source files withheld locally; only derived public-safe Markdown is deposited |

## Research Notes

The paper targets a specific failure mode in tabular Naive Bayes: discretization can improve likelihood estimation and generalization, but aggressive early stopping can erase class-discriminative structure. SADD combines k-nearest-neighbor pseudo-labeling with an adaptive version of the MDLP split threshold. The threshold is scaled by a sigmoid of sample count with N0 = 2000, lowering the split barrier on smaller sets while retaining a floor against over-fragmentation. RNB+ applies the resulting discretization inside regularized Naive Bayes and its attribute-weighting design.

The reported evaluation covers 31 UCI datasets with mixed numeric and categorical features, missing-value imputation, stratified 10-fold cross-validation, and one-tailed t-tests at p = 0.05. SADD averages 82.07 accuracy against 78.96 for MDLP in the main comparison and 80.83 against 77.28 in the paper’s 40%-labeled semi-supervised setting. The results are source-reported, not independently reproduced. The most important review qualification is protocol scope: the framework description derives a discretization scheme using unlabeled testing covariates, so the main claim should be separated into transductive and strict-inductive variants.

## Evidence and Attribution

| ID | Evidence | Supports | Assessment |
|---|---|---|---|
| E1 | arXiv record: title, authors, v1/v3 dates, DOI, abstract, related journal DOI | Identity and publication context | High |
| E2 | Complete local PDF and approved full-paper HTML, sections 1-3 | SADD mechanism, pseudo-labeling, adaptive threshold, RNB+ integration, complexity | High for transcription |
| E3 | Full-paper HTML, sections 4.1-4.5 and Tables 3-10 | Datasets, cross-validation, averages, gains, significance counts, semi-supervised setting | High for transcription; no independent reproduction |
| E4 | Publisher record for Expert Systems with Applications | Journal title, date, DOI, highlights, 31-dataset summary | High for metadata and abstract-level corroboration |
| E5 | Creative Commons license deed linked from arXiv | License signal and redistribution caution | Medium; legal terms require the license text |
| E6 | Live related DEP manuscripts | Cross-paper synthesis on unlabeled data, soft labels, and disagreement governance | Medium; related artifacts are not validation of SADD |
| E7 | Live Black Lake README and .lake-data README | Filing, attribution, public-source, and index requirements | High for repository process |

## Related DEP Entries

1. [DEP-E-20260720-Decentralized SSL](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-Decentralized%20SSL/decentralized_ssl_manuscript.md) — concrete overlap through unlabeled-data utilization and the need to audit derived representations before claiming privacy or generalization.
2. [DEP-E-20260716-Adversarial Label Noise](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md) — concrete overlap through label-distribution uncertainty, soft targets, calibration, and the distinction between a useful target and ground truth.
3. [DEP-E-20260719-DUET Setwise CTR](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260719-DUET%20Setwise%20CTR/duet_setwise_ctr_manuscript.md) — concrete overlap through peer-generated pseudo-labels, correlated errors, disagreement telemetry, and promotion gates.

## Synthesis Note

### Concept Bridge

SADD supplies a compact bridge from source-aware preprocessing to deployment governance. Its central design choice is to use extra unlabeled covariates to recover a richer partition of feature space, then let regularized Naive Bayes estimate class likelihoods over those intervals. The bridge is useful only when the information source is explicit: a transductive batch may use unlabeled test covariates, while an inductive service must freeze boundaries from training data and treat new observations as assignments to existing intervals. The related DEPs extend this same contract from preprocessing to supervision and operations: unlabeled information can improve utility, but its uncertainty, provenance, and leakage surface must be observable.

### Potential Implementations

#### Potential implementation 1: Leakage-aware SADD benchmark

- User: tabular-ML researchers and benchmark maintainers.
- Goal: compare transductive and strict-inductive SADD under identical folds.
- Core mechanism: fit pseudo-labeler, cut points, and RNB weights inside each training fold; add a separately labeled transductive arm.
- Inputs: public tabular datasets, fixed folds, seeds, and a versioned preprocessing manifest.
- Outputs: accuracy, log loss, calibration, cut-point counts, and leakage-class label.
- Risk controls: no test labels during fitting; no cross-fold cache reuse; synthetic/public data only.
- Evaluation: reproduce Tables 4, 7, and 9 trends before testing drifted and imbalanced slices.

#### Potential implementation 2: Confidence-gated discretization service

- User: teams operating compact tabular classifiers.
- Goal: accept only pseudo-label evidence strong enough to influence cut-point selection.
- Core mechanism: kNN confidence, class-balance checks, and abstention feed a weighted or hard-exclusion partition builder.
- Inputs: training rows, unlabeled rows, schema, and a confidence policy.
- Outputs: frozen interval map, confidence report, and abstention counts.
- Risk controls: schema validation, minimum-bin support, calibration checks, and human review for high-impact domains.
- Evaluation: compare accuracy, expected calibration error, minority-class recall, and interval stability.

#### Potential implementation 3: Drift and retraining audit ledger

- User: ML platform and model-risk reviewers.
- Goal: detect when feature distributions make the learned discretization stale.
- Core mechanism: record cut-point versions, bin occupancy, missingness, pseudo-label disagreement, and retraining triggers.
- Inputs: versioned schema, batch summaries, interval assignments, and approved thresholds.
- Outputs: drift dashboard, retraining recommendation, and rollback-ready artifact manifest.
- Risk controls: aggregate telemetry, retention limits, privacy review, and no raw-row logging.
- Evaluation: replay public drift scenarios and verify alert precision, recovery time, and calibration after refresh.

### Deeper Relationship Observations

#### Deeper relationship observation 1

Unlabeled information is not one concept. SADD uses it to shape a feature partition, Decentralized SSL uses it to align representations across clients, and DUET uses it to create peer targets. In all three cases, the benefit comes from importing structure that labels alone do not expose; the failure mode is that the imported structure can be biased, correlated, or difficult to audit.

#### Deeper relationship observation 2

The paper’s adaptive threshold and DUET’s symmetric consistency term are both control knobs on an uncertainty frontier. Lowering a split threshold preserves more discriminative detail; lowering a consistency penalty preserves more peer diversity. Neither knob is intrinsically better at an extreme, so evaluation should report a curve over utility, calibration, and operational cost rather than a single selected point.

#### Deeper relationship observation 3

The source paper treats accuracy as the main endpoint, while the related DEP entries make supervision quality and privacy part of the system contract. A durable implementation should therefore log not only predictions but also interval provenance, pseudo-label confidence, disagreement, calibration, and cohort-level failure cases.

### Conceptual Similarities

#### Conceptual similarity 1

All four artifacts treat a compact intermediate representation as an information bottleneck: SADD bins continuous attributes, Decentralized SSL exchanges representations, Adversarial Label Noise reshapes target distributions, and DUET compresses peer agreement into soft labels.

#### Conceptual similarity 2

All four distinguish a useful signal from ground truth. SADD’s pseudo-labels, DUET’s peer targets, and soft targets in the label-noise work are supervisory evidence; Decentralized SSL’s features are utility-bearing signals, not proof of privacy.

#### Conceptual similarity 3

All four benefit from explicit validation boundaries. Fold isolation, confidence checks, calibration, privacy audits, disagreement logging, and rollback manifests are more transferable than any one reported accuracy gain.

### MVP Implementations with Code Mock-ups

#### MVP implementation 1: Adaptive threshold calculator

Purpose: reproduce the bounded threshold transformation on synthetic values without fitting a model.

~~~python
import math

def adaptive_threshold(base_threshold, sample_count, n0=2000):
    scale = 1.0 / (1.0 + math.exp(-(sample_count / n0)))
    return scale * base_threshold

for n in (50, 200, 2000, 20000):
    print(n, round(adaptive_threshold(0.25, n), 4))
~~~

#### MVP implementation 2: Confidence-gated pseudo-label summary

Purpose: show how an authorized offline harness can retain only high-confidence pseudo-label counts while exposing abstentions.

~~~python
from collections import Counter

def summarize_pseudo_labels(predictions, confidences, minimum=0.8):
    kept = [label for label, score in zip(predictions, confidences)
            if score >= minimum]
    rejected = len(predictions) - len(kept)
    return {"counts": dict(Counter(kept)), "abstained": rejected}

print(summarize_pseudo_labels(["a", "a", "b"], [0.95, 0.62, 0.88]))
~~~

#### MVP implementation 3: Fold-isolated metric delta

Purpose: keep a strict-inductive comparison auditable by pairing fold-level scores rather than averaging predictions across folds.

~~~python
def paired_delta(candidate_scores, baseline_scores):
    if len(candidate_scores) != len(baseline_scores):
        raise ValueError("fold counts must match")
    deltas = [a - b for a, b in zip(candidate_scores, baseline_scores)]
    return {"fold_deltas": deltas, "mean_delta": sum(deltas) / len(deltas)}

print(paired_delta([0.81, 0.79, 0.83], [0.78, 0.78, 0.80]))
~~~

### Developer Challenges

1. Implementing fold-isolated pseudo-labeling and cut-point fitting without accidental access to held-out labels or cached transformations.
2. Preserving numerical stability, bin-support constraints, and predictable latency when the number of attributes and cut points grows.
3. Building calibration, drift, privacy, and rollback telemetry that remains useful without retaining raw rows.

### Author Challenges

1. Clarifying the transductive versus inductive scope of the main framework and reporting both protocols under matched folds.
2. Publishing complete preprocessing, fold, seed, k-search, implementation, and statistical-test artifacts so the 31-dataset tables can be independently reconstructed.
3. Extending evidence beyond UCI accuracy averages to calibration, class imbalance, drift, modern tabular benchmarks, and resource cost.

## Validation Notes

- Source gate: passed only after one bounded repair; PDF and full-paper HTML met every required integrity threshold.
- Manuscript contract: separate artifact contains all required full-report headings, YAML front matter, matching title/H1, evidence ledger, methodology, scope, exactly three research exercises, and an appendix.
- Synthesis contract: this note contains exactly 3 potential implementations, 3 deeper relationship observations, 3 conceptual similarities, 3 MVP implementations with Python mock-ups, 3 developer challenges, and 3 author challenges.
- Public safety: no local absolute paths, usernames, Windows drive paths, machine names, local timezone labels, exact local execution timestamps, source files, caches, extracted text, or verification records appear.
- Staged allowlist equivalent: the API submission will contain only the generated .logs, .reports, .lake-data Markdown paths, and the required publication-index Markdown update.

## Attribution Block

- Source URL: https://arxiv.org/abs/2111.10983
  - Applies to: source identity, version dates, authors, abstract, and citation.
  - Notes: Metadata page; source files withheld locally.
- Source URL: https://arxiv.org/pdf/2111.10983
  - Applies to: PDF integrity and primary-paper review.
  - Notes: Local source inspected; not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/2111.10983
  - Applies to: methods, tables, experiments, limitations, and full-paper review.
  - Notes: Approved fallback rendering; local copy withheld.
- Source URL: https://www.sciencedirect.com/science/article/pii/S0957417423005961
  - Applies to: publisher metadata, abstract, highlights, and journal context.
  - Notes: Public publisher record.
- Source URL: https://creativecommons.org/licenses/by-nc-nd/4.0/
  - Applies to: license and distribution caution.
  - Notes: Linked from the arXiv record; license terms should be reviewed before redistribution.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-Decentralized%20SSL/decentralized_ssl_manuscript.md
  - Applies to: related-entry synthesis.
  - Notes: Live Black Lake manuscript inspected.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md
  - Applies to: related-entry synthesis.
  - Notes: Live Black Lake manuscript inspected.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260719-DUET%20Setwise%20CTR/duet_setwise_ctr_manuscript.md
  - Applies to: related-entry synthesis.
  - Notes: Live Black Lake manuscript inspected.
