---
title: "EncoderMI Privacy - DEP-E"
generated_at: "2026-08-02 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of EncoderMI membership inference against contrastive image encoders."
source_status: "verified complete local PDF, full-paper HTML, and metadata inspected; sources withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-02"
temporal_cutoff: "2026-08-02 public-safe review boundary"
primary_url: "https://arxiv.org/abs/2108.11023"
stable_identifier: "arXiv:2108.11023; DOI:10.1145/3460120.3484749"
confidence_summary: "High for source identity, integrity, and transcription; medium for reported empirical interpretation; low for unreplicated deployment claims."
safety_scope: "Defensive privacy evaluation, offline research, and nonbinding audit planning only."
distribution_notes: "Source files, caches, extracted text, datasets, models, credentials, and local execution details are withheld."
selection_method: "Uniform random index over sorted unique PDF-parent units after rg PDF enumeration."
dedup_validation: "No prior Arxiv DEP artifact or same-paper marker; metadata-only inventory match did not count as a duplicate; zero reselections."
---

# EncoderMI Privacy - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Official arXiv record | Primary metadata | HTML | arXiv:2108.11023 | https://arxiv.org/abs/2108.11023 | Metadata page; source files withheld | 2026-08-02 | Inspected |
| S2 | Full paper | Primary artifact | HTML | arXiv full-paper rendering | https://arxiv.org/html/2108.11023 | Verified local copy; not redistributed | 2026-08-02 | Inspected in full |
| S3 | Full paper | Primary artifact | PDF | arXiv:2108.11023 | https://arxiv.org/pdf/2108.11023 | Verified local copy; not redistributed | 2026-08-02 | Integrity checked |
| S4 | Published record | Near-primary metadata | DOI/HTML | CCS 2021, pp. 2081–2095 | https://doi.org/10.1145/3460120.3484749 | Publication metadata | 2026-08-02 | Cross-checked |
| S5 | Publication metadata | Near-primary metadata | HTML | Penn State record | https://pure.psu.edu/en/publications/encodermi-membership-inference-against-pre-trained-encoders-in-co | Venue, pages, DOI | 2026-08-02 | Cross-checked |
| S6 | Related DEP | Related synthesis | Markdown | MRMMIA Memory Attack | `.lake-data/DEP-A/DEP-A-20260726-MRMMIA Memory Attack/2605.27825-whitepaper-review.md` | Repository synthesis only | 2026-08-02 | Inspected |
| S7 | Related DEP | Related synthesis | Markdown | 4DContrast Contrastive | `.lake-data/DEP-E/DEP-E-20260722-4DContrast Contrastive/4dcontrast_contrastive_manuscript.md` | Repository synthesis only | 2026-08-02 | Inspected |
| S8 | Related DEP | Related synthesis | Markdown | Equivariant Contrastive | `.lake-data/DEP-E/DEP-E-20260721-Equivariant Contrastive/equivariant_contrastive_manuscript.md` | Repository synthesis only | 2026-08-02 | Inspected |

Authors: Hongbin Liu, Jinyuan Jia, Wenjie Qu, and Neil Zhenqiang Gong. The arXiv record is dated 2021-08-25; the published CCS record is from 2021. The source unit was initially partial, then passed the complete PDF-plus-full-paper-HTML gate after one bounded local repair. The source package was unavailable through the approved redirect policy and was not needed for review.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Official metadata | Title, authors, arXiv ID, date, abstract, public locators | Source identity and high-level thesis | High | Abstract is not detailed result evidence |
| E2 | S2 | Primary full text | Threat model, shadow encoder, augmentation features, classifier variants, method flow | Method and assumptions | High | Full-paper rendering was reviewed locally and withheld |
| E3 | S2/S3 | Primary paper | CIFAR10, STL10, Tiny-ImageNet, CLIP tables and figures | Reported metrics and evaluation design | High for transcription | No independent rerun |
| E4 | S2/S3 | Primary paper | Early stopping, privacy-utility trade-off, differential privacy discussion, conclusion | Defense and limitation analysis | High for transcription | Differential privacy is future work in this paper |
| E5 | S4/S5 | Publication metadata | CCS venue, page range, DOI, publication cross-check | Bibliographic attribution | Medium-high | Metadata does not validate claims |
| E6 | S6 | Related DEP | Query aggregation, membership inference, false-positive operating points, privacy defenses | Direct conceptual bridge | Medium | Different target state and threat model |
| E7 | S7/S8 | Related DEP | Contrastive representations, augmentations, invariance, provenance-first evaluation | Methodological bridge | Medium | Different tasks and modalities |

## Executive Summary

EncoderMI proposes a black-box membership-inference method for image encoders trained with contrastive learning. Its central observation is that contrastive training makes augmented views similar, while overfitting can make the similarity pattern of member examples differ from non-members. The method trains a shadow encoder on a split shadow dataset, extracts pairwise similarity features from multiple augmented views, and learns an inference classifier.

The inspected paper reports strong source-level results across CIFAR10, STL10, and Tiny-ImageNet. With all three background-knowledge dimensions available, its main table reports 91.4% accuracy, 90.1% precision, and 93.5% recall for EncoderMI-V on CIFAR10; the corresponding Tiny-ImageNet EncoderMI-V row reports 96.5% accuracy, 96.6% precision, and 97.0% recall. The paper also reports 0.66–0.75 accuracy across shadow datasets for a CLIP evaluation, but its potential members are not verified ground-truth members. Confidence is high for identity and transcription, medium for empirical interpretation, and low for deployment or generalization claims not independently reproduced.

The main practical implication is not that a similarity threshold proves training membership. It is that repeated-view representation behavior can expose a privacy signal that should be measured with consent, calibrated false-positive rates, query budgets, duplicate controls, and explicit abstention. The proposed early-stopping countermeasure reduces membership-inference accuracy at a cost to downstream utility, illustrating a privacy-utility frontier rather than a free defense.

## Detailed Summary

### Problem and context

Contrastive learning pre-trains image encoders from unlabeled images or image-text pairs and makes them reusable as feature extractors for downstream tasks. Encoder providers may publish or serve an encoder while keeping its pre-training data private. EncoderMI studies whether an input image was in that pre-training dataset when an inferrer can query only the encoder's feature output.

### Threat model and background knowledge

The inferrer has black-box access to the target encoder and may query feature vectors for original or augmented inputs. The paper varies three background-knowledge dimensions: pre-training-data distribution, encoder architecture, and training algorithm. Each may be known or unknown, giving eight combinations. The inferrer uses a shadow dataset; when the target distribution is unknown, the shadow distribution is allowed to differ. When architecture or training algorithm is unknown, the inferrer assumes one.

### Method

The shadow dataset is split into shadow members and shadow non-members. A shadow encoder is trained on the member split, so the labels are known for both groups. For each input, the method creates `n` augmented views, encodes them, and computes `n(n-1)/2` pairwise similarity scores. In the CLIP experiment, `n=10`, yielding 45 cosine-similarity features per input.

EncoderMI-V ranks the similarity scores and trains a vector-based binary classifier. EncoderMI-S treats the scores as a set. EncoderMI-T uses a threshold-based classifier, and the paper reports that average pairwise cosine similarity alone contains useful membership signal. The output is a member/non-member prediction, but the method is an inference estimate with error—not a proof of data provenance.

### Evaluation design and results

The paper pre-trains target encoders on CIFAR10, STL10, and Tiny-ImageNet, compares the three variants across all eight background-knowledge settings, reports accuracy/precision/recall and five-trial standard deviations, and studies the number of augmented views, similarity metrics, dataset sizes, and augmentation overlap. It reports that more background knowledge generally helps, training-algorithm knowledge is especially informative on STL10 and Tiny-ImageNet, and cosine similarity performs best when it matches the contrastive objective.

The reported Tiny-ImageNet EncoderMI-V accuracy ranges from 88.7% without the three dimensions of background knowledge to 96.5% with all three. On CIFAR10, the all-known EncoderMI-V row is 91.4% accuracy, 90.1% precision, and 93.5% recall. Results are author-reported and were not reproduced in this run.

### CLIP case study

The CLIP case study treats a ViT-B/32 image encoder as the target and builds two proxy evaluation sets: 1,000 potential members plus 1,000 constructed non-members from Google image search, and the same counts from Flickr. The paper acknowledges that potential members may not actually be in CLIP's pre-training set. Its 0.66–0.75 accuracy range therefore supports distinguishability under a proxy-label protocol, not a verified membership rate for individual images.

### Countermeasure and conclusion

Early stopping is evaluated as an overfitting-reduction defense. Longer pre-training increases member/non-member separation in average pairwise similarity; stopping earlier lowers membership-inference accuracy but also lowers downstream classification utility. Differential privacy and adversarial learning are discussed as future directions. The paper concludes with white-box extension, image-text-pair membership, stronger countermeasures, and other encoder privacy risks as future work.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | EncoderMI is a membership-inference method for contrastively pre-trained image encoders. | Author claim, source-supported mechanism | E1, E2 | Directly supported by the threat model and method sections. | High |
| C2 | Augmented-view similarity features carry more membership signal than a single encoder feature vector in the paper's setup. | Reviewer interpretation of author evidence | E2, E3 | Supported by the method rationale and baseline comparisons; depends on the tested data and training conditions. | Medium-high |
| C3 | EncoderMI-V reaches 91.4% CIFAR10 accuracy and 96.5% Tiny-ImageNet accuracy when all three background-knowledge dimensions are available. | Author-reported quantitative result | E3 | Exact table transcription; not independently reproduced. | High for transcription, medium for validity |
| C4 | The CLIP experiment demonstrates that the method can identify ground-truth CLIP members. | Overclaim rejected | E3 | The paper uses potential members and acknowledges that they are not verified members. | High rejection confidence |
| C5 | More background knowledge generally improves inference accuracy. | Author-reported empirical pattern | E3 | Supported across the reported grid, with dataset/method-specific exceptions possible. | Medium-high |
| C6 | Early stopping reduces membership signal while reducing downstream utility. | Author-reported defense trade-off | E4 | Supported qualitatively by Figure 5 and discussion; no single universal operating point is established. | Medium-high |
| C7 | EncoderMI is suitable as a formal proof of unauthorized training-data use. | Unsupported implication | E1–E4 | Rejected: proxy labels, errors, data overlap, and distributional assumptions prevent proof-level interpretation. | High rejection confidence |
| C8 | A safe implementation should report membership-like scores with calibration, provenance, query budgets, and abstention. | Reviewer implementation inference | E2–E8 | Reasonable transfer principle; requires evaluation in an authorized setting. | Medium |

## Methodology

- `Research objective`: Preserve the selected paper's mechanism, reported evidence, limitations, public provenance, and safe implementation implications.
- `Sources inspected`: The official arXiv record; verified local PDF, metadata HTML, and full-paper HTML; DOI and Penn State publication metadata; and exactly three related Black Lake DEP records.
- `Discovery strategy`: Enumerated local PDFs with `rg --files -g "*.pdf"`, reduced to sorted unique parent units, selected one uniform `Get-Random` index, scanned local and remote artifact inventories for deduplication, repaired the missing full-paper companions through the pinned broker, and inspected the full text by section, table, and figure caption.
- `Selection validation`: 75,960 PDF candidates produced 75,957 unique parent units; index 15,397 was accepted on the first draw. No prior Arxiv DEP artifact, DOI/title/slug duplicate, or same-paper-within-24-hours marker was found. A metadata-only author inventory row was retained as an inventory match, not treated as a processed artifact.
- `Source-integrity validation`: The initial unit was partial because full-paper HTML and metadata were missing. One bounded repair preserved the valid PDF and added metadata and full-paper HTML. Final checks passed the PDF minimum size, `%PDF-` header, trailing `%%EOF`, HTML minimum size/body/marker/heading/structure tests, and no-partial-file check. The source package was unavailable and was not required.
- `Inclusion criteria`: Primary-paper problem, threat model, method, experimental setup, reported tables and figures, countermeasure, limitations, conclusion, public bibliographic metadata, and concrete conceptual neighbors.
- `Exclusion criteria`: Abstract-only reasoning, independent claims not supported by inspected evidence, source-file redistribution, unverified membership conclusions, unsafe attack operationalization, and unrelated repository inventory rows.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product, and replication analysis.
- `Evidence handling`: Source claims, direct table transcriptions, reviewer interpretations, and rejected overclaims are labeled separately and linked to evidence IDs.
- `Uncertainty handling`: Proxy CLIP labels, unreplicated metrics, missing official implementation, dataset overlap risk, and deployment transfer limits remain explicit.
- `Safety handling`: Implementation ideas are offline, synthetic or consented, calibrated, and nonbinding; they do not target private models or unauthorized data.

## Scope, Constraints, and Assumptions

- `Scope`: The selected paper's source identity, threat model, method, evidence, countermeasure, limitations, and bounded research translation.
- `Temporal boundary`: Public-safe review boundary 2026-08-02; exact local execution time withheld.
- `Evidence limits`: The paper's experiments were not rerun; no official EncoderMI implementation was located; CLIP potential members are proxy labels; private training data and model internals were unavailable.
- `Assumptions`: The arXiv record and DOI identify the same work; the reported table values were transcribed correctly from the verified full paper; repository related entries are public-safe syntheses.
- `Constraints`: Privacy, consent, license, source locality, dual-use, and public-output restrictions apply. No source file is redistributed.
- `Out of scope`: Operational membership attacks against third-party models, individual privacy determinations, formal legal conclusions, production deployment, and claims of independent reproduction.
- `Intended use`: DEP preservation, defensive privacy evaluation, research planning, and evidence-grounded implementation review.
- `Audience`: Privacy researchers, ML security engineers, dataset stewards, and reviewers of model-training provenance.
- `Reproducibility boundary`: Source text and public locators are preserved; reproduction requires governed datasets, exact augmentation/model configurations, five-trial evaluation, and authorized model access.
- `Operational boundary`: Discussed as an audit concept only; not an instruction set for probing private or unauthorized services.
- `Data sensitivity`: Public paper metadata and local source documents withheld from publication; any derivative audit data must be consented or synthetic.

## Observations

- `Observed pattern`: The method turns the contrastive objective's augmented-view alignment into an observable membership signal.
- `Technical implication`: Privacy evaluation must measure representation behavior across transformations, not only output dimensionality or one feature vector.
- `Observed pattern`: Accuracy rises with background knowledge in the reported grid, while training-algorithm knowledge is especially informative on two datasets.
- `Contradiction or tension`: The same invariance that helps downstream transfer can make training-set-specific behavior easier to detect.
- `Reviewer hypothesis`: Dataset scale, augmentation overlap, and model overfitting may matter more than the choice among the three inference classifiers in some deployment regimes.
- `Open question`: Whether the signal persists under modern, heavily regularized encoders and strict query budgets is not established by this paper.

## Considerations

Membership inference is dual-use. A data owner may use it to investigate public-data reuse, while an attacker may use it to probe sensitive training data. Any implementation should require an authorization record, consented or synthetic calibration data, fixed false-positive targets, duplicate control, rate limits, version pinning, and human review. A result should be reported as membership-like evidence with confidence and scope, never as proof about an individual unless an independent provenance process confirms it.

Operational considerations include model and dataset drift, augmentation mismatch, shadow-model compute, inference query cost, calibration maintenance, and privacy leakage from audit logs. A safe workflow stores hashes or consented identifiers instead of raw images where possible, minimizes retention, and separates the audit signal from any consequential action.

## Strengths

- Defines a concrete black-box threat model and varies three meaningful background-knowledge dimensions.
- Provides a mechanism tied to the contrastive training objective instead of applying classifier membership attacks unchanged.
- Compares vector, set, and threshold representations and studies augmentations, similarity metrics, data sizes, and knowledge settings.
- Includes a defense experiment rather than only an attack result.
- Makes proxy-label limitations visible in the CLIP case study.

## Weaknesses

- The CLIP evaluation lacks verified ground-truth members, so it cannot establish per-image membership accuracy for CLIP's actual training data.
- Shadow-encoder training, augmentation choices, and background-knowledge assumptions may not transfer to modern encoders or service APIs.
- Metrics are reported on selected datasets and source configurations; independent code, checkpoint, and environment reproduction was not available in this review.
- Membership-like scores can be confounded by near-duplicates, web-source distribution, compression, or image quality rather than training membership.
- The early-stopping evaluation shows a trade-off but does not compare a broad modern defense suite under a common utility budget.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Verified membership benchmark | Ground truth | Remove proxy-label ambiguity | Calibrated per-image evaluation | Requires consent and governance | Hash-linked members/non-members with duplicate audit |
| Query-budget and calibration sweep | Threat model | Tie signal to realistic API access | Better operating-point interpretation | More evaluation runs | Report ROC/PR, TPR at fixed FPR, budget curves, and abstention |
| Modern encoder/defense matrix | Generalization | Test beyond the original setup | More durable privacy guidance | Compute and implementation burden | Match downstream utility across regularization, DP, augmentation, and release controls |
| Independent implementation release | Reproducibility | Make the shadow pipeline auditable | Easier replication and error finding | Maintenance and data-license review | Reproduce tables from frozen manifests and documented environments |

## Potential Implementations

1. **Consented encoder audit harness**: User: dataset steward. Goal: assess whether a released encoder exhibits membership-like signal for a consented test set. Core mechanism: shadow encoder, augmented-view features, calibrated inference, fixed FPR. Inputs: consent manifest, public/consented images, model API, shadow configuration. Outputs: auditable report with confidence, abstentions, and query cost. Risk controls: authorization, rate limits, minimization, no raw-image retention by default. Evaluation: five-trial synthetic validation plus ground-truth holdout.
2. **Privacy-utility regression gate**: User: model trainer. Goal: compare training defenses before release. Core mechanism: run EncoderMI-style audit and a fixed downstream task across matched model revisions. Inputs: versioned training configuration, consented dataset, utility benchmark, defense settings. Outputs: privacy-utility frontier and release recommendation. Risk controls: no automatic release decision, human sign-off, rollback, and audit logs. Evaluation: TPR/FPR at fixed utility bands and drift checks.
3. **Training-data provenance review**: User: data governance team. Goal: investigate possible public-data reuse without making unsupported individual claims. Core mechanism: combine consent records, near-duplicate controls, model-version metadata, and a bounded membership-like audit. Inputs: provenance ledger, model endpoint, synthetic calibration set, review policy. Outputs: evidence packet with scope and uncertainty. Risk controls: legal review, access control, no attacker-facing endpoint, retention limits. Evaluation: blinded seeded cases and reviewer agreement.

## Three Ways to Exercise This Research

1. **Synthetic shadow encoder**: Objective: verify the feature-construction logic. Inputs: synthetic vectors with labeled member/non-member groups. Method: create bounded augmented views, compute pairwise cosine features, fit a simple threshold, and inspect calibration. Output: reproducible toy report. Success criterion: known synthetic separation is recovered without leakage. Stop condition: any private data or untracked transformation enters the run.
2. **Consented public-encoder audit**: Objective: test proxy-label and source-distribution effects. Inputs: consented/public images, verified non-members, model API permission, fixed query budget. Method: compare EncoderMI variants and a random baseline under held-out calibration. Output: TPR/FPR, precision/recall, abstention, and query-cost report. Success criterion: results remain interpretable under fixed FPR and duplicate controls. Stop condition: membership ground truth or authorization becomes uncertain.
3. **Defense frontier study**: Objective: quantify privacy-utility trade-offs. Inputs: fixed downstream task, model checkpoints trained with early stopping and other approved defenses, consented audit set. Method: measure membership-like signal and downstream utility at matched compute and data versions. Output: frontier with confidence intervals and failure cases. Success criterion: a release decision can state the chosen utility and privacy operating point. Stop condition: utility or privacy metrics are not comparable across revisions.

## Example MVP Product

- `Product name`: Consent-Aware Encoder Audit.
- `Target user`: Dataset steward, model trainer, or privacy reviewer.
- `Problem`: Encoder releases can expose training-data signals while proxy audits can be mistaken for proof.
- `Core workflow`: Import a consent/provenance manifest, validate duplicate-controlled calibration data, query an authorized encoder within a fixed budget, compute augmented-view signals, calibrate thresholds, emit an abstaining report, and route it to human review.
- `Data requirements`: Consent records, synthetic or consented images, verified non-members, model/version metadata, augmentation configuration, and downstream utility labels.
- `Architecture`: Local manifest validator, privacy-preserving image adapter, bounded feature-query client, calibration module, metric ledger, provenance store, report generator, and review UI.
- `Success metrics`: TPR at fixed FPR, calibration error, query cost, duplicate-control rate, reviewer agreement, downstream utility retention, and reproducibility of the evidence packet.
- `Risk controls`: Authorization gates, no secrets, no raw-image logging by default, minimum retention, rate limits, abstention, human review, access control, and no autonomous consequential decisions.
- `Limitations`: Shadow-model mismatch, proxy labels, distribution drift, and unknown model internals can produce misleading results; the MVP does not prove membership.
- `MVP boundary`: Offline or explicitly authorized evaluation only; no open probing service, no private-model targeting, and no automated legal or employment decision.

## Related Research and Reading

| Item | Type | Relevance | Repository Path / Public URL |
|---|---|---|---|
| MRMMIA Memory Attack | Related DEP | Direct membership-inference, repeated-query aggregation, false-positive, and privacy-defense context | `.lake-data/DEP-A/DEP-A-20260726-MRMMIA Memory Attack/2605.27825-whitepaper-review.md` |
| 4DContrast Contrastive | Related DEP | Contrastive representation, augmented correspondence, and evaluation-boundary context | `.lake-data/DEP-E/DEP-E-20260722-4DContrast Contrastive/4dcontrast_contrastive_manuscript.md` |
| Equivariant Contrastive | Related DEP | Augmentation-driven invariance and provenance-first representation evaluation | `.lake-data/DEP-E/DEP-E-20260721-Equivariant Contrastive/equivariant_contrastive_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2108.11023 | Identity, abstract, authors, date, and public locators | 2026-08-02 | Metadata page only |
| R2 | https://arxiv.org/html/2108.11023 | Full-paper method, tables, figures, and conclusion | 2026-08-02 | Verified local copy withheld; approved fallback used for the local full-paper file |
| R3 | https://arxiv.org/pdf/2108.11023 | Full-paper integrity and cross-check | 2026-08-02 | Verified local copy withheld |
| R4 | https://doi.org/10.1145/3460120.3484749 | CCS 2021 publication identity and DOI | 2026-08-02 | Published metadata |
| R5 | https://pure.psu.edu/en/publications/encodermi-membership-inference-against-pre-trained-encoders-in-co | Venue, page range, authors, and DOI cross-check | 2026-08-02 | Publication record |
| R6 | `.lake-data/DEP-A/DEP-A-20260726-MRMMIA Memory Attack/2605.27825-whitepaper-review.md` | Related membership-inference synthesis | 2026-08-02 | Public repository Markdown |
| R7 | `.lake-data/DEP-E/DEP-E-20260722-4DContrast Contrastive/4dcontrast_contrastive_manuscript.md` | Related contrastive representation synthesis | 2026-08-02 | Public repository Markdown |
| R8 | `.lake-data/DEP-E/DEP-E-20260721-Equivariant Contrastive/equivariant_contrastive_manuscript.md` | Related augmentation/invariance synthesis | 2026-08-02 | Public repository Markdown |

## Appendix

### Selection, Deduplication, and Source Verification Record

The source-first run enumerated 75,960 PDFs and 75,957 unique parent units, selected index 15,397 uniformly, and accepted the first draw. Local and remote artifact scans found no prior processed record for arXiv:2108.11023, DOI:10.1145/3460120.3484749, the normalized title, or the EncoderMI slug. The author inventory match was metadata-only and remained non-excluding. The paper unit began partial, then passed a bounded repair and the complete-source integrity gate. No public source directory was created and no source file was uploaded.

### Reproduction Checklist

- Freeze a consented or synthetic dataset and a duplicate-control manifest.
- Pin the encoder architecture, training algorithm, augmentations, model revision, and shadow split.
- Recreate the three inference variants and the eight background-knowledge settings.
- Report five-trial metrics, TPR/FPR curves, query budgets, calibration, abstention, and downstream utility.
- Compare early stopping and other authorized defenses under matched utility and versioned inputs.
- Retain only public-safe evidence, provenance references, and reviewer decisions.
