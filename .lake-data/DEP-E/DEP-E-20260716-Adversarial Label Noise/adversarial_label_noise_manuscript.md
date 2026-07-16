---
title: "Adversarial Label Noise - DEP-E"
generated_at: "2026-07-16"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of label distribution mismatch and robust overfitting in adversarial training."
source_status: "verified complete v4 PDF and official arXiv full-paper HTML inspected; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv:2110.03135v4, NeurIPS proceedings, and focused public code search inspected through 2026-07-16"
primary_url: "https://arxiv.org/abs/2110.03135v4"
stable_identifier: "arXiv:2110.03135v4; DOI 10.48550/arXiv.2110.03135"
confidence_summary: "High for method and table transcription; medium for causal interpretation; low for per-example true-label recovery."
safety_scope: "research analysis only; no production-robustness authorization"
distribution_notes: "Paper files, metadata HTML, caches, and extracted text were not redistributed."
---

# Adversarial Label Noise - DEP-E

## Source Metadata

| ID | Source | Role | Identifier / Version | Public Locator | Status |
|---|---|---|---|---|---|
| S1 | Label Noise in Adversarial Training | Primary metadata/PDF/HTML | arXiv:2110.03135v4 | https://arxiv.org/abs/2110.03135v4 | Full paper inspected |
| S2 | NeurIPS proceedings | Official publication record | NeurIPS 2022 Oral | https://proceedings.neurips.cc/paper_files/paper/2022/hash/6fe6a2ba2594521d15af3b1f2162d79c-Abstract-Conference.html | Inspected |
| S3 | arXiv DOI | Stable identifier | 10.48550/arXiv.2110.03135 | https://doi.org/10.48550/arXiv.2110.03135 | Resolved |
| S4 | ViT Semantic Robustness | Related DEP | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md` | Inspected |
| S5 | PAC Confidence | Related DEP | DEP-E-20260713 | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Inspected |
| S6 | AFIDAF Vision Filters | Related DEP | DEP-E-20260715 | `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` | Inspected |
| S7 | Black Lake README | Repository authority | live default branch | https://github.com/Delphoa/Black-Lake | Inspected before writing |

Authors: Chengyu Dong, Liyuan Liu, and Jingbo Shang. Submitted 2021-10-07; revised 2022-10-19, 2023-03-14, and 2023-10-13. The work appeared as a NeurIPS 2022 oral. Version 1 used the title *Double Descent in Adversarial Training: An Implicit Label Noise Perspective*. No official code repository was identified in the inspected paper, proceedings record, or focused search.

## Evidence Ledger

| ID | Source basis | Evidence class | Supports | Confidence | Limitation |
|---|---|---|---|---|---|
| E1 | S1, Sections 3-4 | Primary analysis | epoch-wise double descent and implicit label-noise hypothesis | High for observation | causal interpretation indirect |
| E2 | S1, Section 5 | Primary method | KD-AT-Auto teacher, temperature, and interpolation | High | teacher quality required |
| E3 | S1, Theorems 5.1-5.2 | Primary theory | existence of rectification improving total-variation mismatch | High for statement | unknown true distribution prevents direct use |
| E4 | S1, Table 1 | Primary empirical | multi-dataset robust-overfitting gaps | High for transcription | author results; no uncertainty |
| E5 | S1, Tables 2-5 | Primary empirical | architecture/method/attack/SVHN extensions | High for transcription | no independent reproduction |
| E6 | S1, limitations | Primary boundary | calibration, teacher, per-example, cost limitations | High | incomplete real-world semantics |
| E7 | Focused public search | Availability | no official code identified | Medium | search may miss unlinked code |
| E8 | S4-S6 | Related processed research | semantics, calibration, architecture audits | Medium | adjacent evidence only |
| E9 | Selection, source, cache, dedup records | Process evidence | eligibility and provenance | High | local identifiers omitted publicly |

## Executive Summary

The paper argues that adversarial perturbations may change the appropriate label distribution even when training keeps the clean sample's one-hot label. This mismatch behaves as implicit label noise and is proposed as a cause of robust overfitting. Extending training to 1,000 epochs reveals robust overfitting as the early phase of an epoch-wise double-descent curve in the studied setup.

KD-AT-Auto uses a separately robust-trained model as a self-teacher. Correctly classified adversarial examples receive a temperature-scaled predictive distribution; misclassified examples interpolate that distribution with the inherited one-hot target. Global temperature and interpolation values are selected through adversarial validation likelihood. Reported robust best-to-last gaps shrink from 5.93 to 0.25 points on CIFAR-10, 5.04 to 0.12 on CIFAR-100, and 1.80 to -0.10 on Tiny-ImageNet. These results support rectified soft targets as a mitigation within the tested threat models, not direct recovery of true per-example semantics.

## Detailed Summary

### Problem and Hypothesis

Standard adversarial training generates a bounded perturbation but retains the clean sample's assigned label. The authors model the perturbed example as having an unknown true label distribution that can differ from the inherited one-hot target. Training against the latter can therefore inject distribution mismatch. Longer fixed-learning-rate runs reveal an error curve the authors interpret as epoch-wise double descent, placing conventional robust overfitting before a later recovery.

### KD-AT-Auto

A robust self-teacher supplies predictive probabilities for adversarial examples. When the teacher predicts the inherited class correctly, temperature scaling softens or sharpens the distribution. When it predicts another class, the method interpolates the temperature-scaled distribution with the inherited one-hot target. The chosen rectified distribution becomes the training target in the outer adversarial objective.

Theorem 5.1 states that for a correctly classified adversarial example there exists a temperature whose scaled teacher distribution is no farther in total variation from the unknown true distribution. Theorem 5.2 states, under a maximum true-class probability of at least one half, that an interpolation weight exists for a misclassified example that improves the mismatch. These are existence statements; the operational method estimates global parameters using negative log-likelihood on an adversarial validation set.

### Experiments

The main setup uses preactivation ResNet-18 with PGD adversarial training, perturbation radius 8/255, ten attack steps, and step size 2/255. CIFAR-10, CIFAR-100, Tiny-ImageNet, and later SVHN are tested. AutoAttack is the main evaluation; extensions include TRADES, FGSM training, VGG-19, WideResNets, PGD-1000, Square, and RayS attacks.

For CIFAR-10, ordinary adversarial training reports robust best/last accuracy 47.35/41.42, a 5.93-point gap; fixed KD reports 48.76/46.33 and 2.43; KD-AT-Auto reports 49.05/48.80 and 0.25. CIFAR-100 gaps are 5.04, 2.19, and 0.12, respectively. Tiny-ImageNet gaps are 1.80, 0.68, and -0.10. Architecture, method, and attack tables similarly reduce gaps, including VGG-19 3.09 to 0.03, TRADES 2.97 to 0.36, PGD-1000 7.64 to 0.34, and Square 4.57 to 0.06.

## Key Claims and Evidence

| Claim | Type | Evidence | Assessment | Confidence |
|---|---|---|---|---|
| Adversarial perturbations create implicit label-distribution mismatch. | Mechanistic hypothesis | E1/E3 | Coherent formalization; true labels unobserved. | Medium |
| Robust overfitting is an early phase of epoch-wise double descent. | Empirical interpretation | E1 | Observed in long-run studied settings; not universalized. | Medium-high |
| Rectification can reduce total-variation mismatch. | Theory | E3 | Existence results under stated cases/assumptions. | High for theorem |
| KD-AT-Auto nearly removes best-to-last gaps. | Empirical | E4/E5 | Numerically supported across tested variants. | High for report |
| Learned labels recover true adversarial semantics. | Implication | E3/E6 | Not established sample-wise. | Low |
| The method adds no meaningful tuning/cost. | Operational claim | E2/E6 | No manual user tuning, but validation and an extra teacher remain. | Medium-low |
| First random draw was eligible. | Process | E9 | All dedup keys and 24-hour markers were clear. | High |

## Methodology

- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, treated unique PDF parent directories as paper units, and chose a uniform zero-based index with PowerShell `Get-Random`.
- `Source integrity`: Classified the unit before review. The valid PDF lacked full-paper HTML, so official arXiv HTML and metadata were fetched with bounded retries and validated for bytes, body text, document markers, headings, and structure terms.
- `Cache methodology`: Ran `document_source_processing.py extract-arxiv` in `missing-only` mode with the central archive cache. The miss became `cached`; `pypdf` emitted one image XForm decode warning but text extraction completed. No source package was collected.
- `Deduplication`: Scanned logs, reports, DEP-E paths, staging index, automation memory, relevant Black-Lake-Data entries, both known titles, arXiv ID, DOI, slug, and 24-hour markers. No match occurred; no reselection was needed.
- `Review`: Inspected the complete paper, equations, main and extension tables, limitations, NeurIPS record, and focused code search. No result was reproduced.
- `Related synthesis`: Selected exactly three inspected deposits for concrete overlap in perturbation semantics, calibration validity, and architecture-level robustness evaluation.
- `Distribution`: Only original review Markdown and derived index/status JSON are public. Source documents and extraction products remain local.

## Scope, Constraints, and Assumptions

- Reported results are author results, not reproduced findings.
- The true per-example label distribution is latent, so the central mismatch is not directly measured.
- Bounded image perturbations can preserve, weaken, or change semantic evidence; the answer may depend on task and annotator.
- Temperature and interpolation parameters use adversarial validation data and a threat-model-specific teacher.
- Robust accuracy against selected attacks does not prove open-world or semantic robustness.
- No official code was found; implementation and exact pipeline behavior were not audited.

## Observations

- Gap reduction is consistent across the paper's datasets, architectures, training methods, and attacks.
- KD-AT-Auto improves last-epoch robustness more consistently than it improves peak robustness, matching its stated overfitting objective.
- Negative gaps on Tiny-ImageNet and the CIFAR-10 SWA combination mean last-epoch results slightly exceed the recorded best checkpoint under the table convention.
- The theory motivates correction direction but does not identify the unknown true distribution.
- A self-teacher can transfer its own attack- and dataset-specific errors into the corrected labels.

## Considerations

Evaluation should separate calibration quality, semantic correctness, and attack robustness. Add human or task-specific semantic-equivalence studies, per-example uncertainty, multiple teachers, repeated seeds, confidence intervals, and validation-set sensitivity. Test transfer across attack families, perturbation radii, corruptions, natural distribution shift, and adaptive attacks aware of the rectification pipeline.

Operationally, account for the extra robust teacher, adversarial validation generation, tuning, storage, and training energy. A deployment should treat rectified labels as experimental targets with provenance, not ground truth.

## Strengths

- Offers a concrete distributional lens on robust overfitting.
- Connects a long-run double-descent observation to a practical mitigation.
- Provides formal existence results for both correct and incorrect teacher predictions.
- Tests multiple datasets, architectures, training methods, and attacks.
- Reports best, last, and gap values that directly measure the target failure mode.

## Weaknesses

- The unknown true label distribution makes the causal explanation empirically indirect.
- The theorems are existential and do not guarantee global validation parameters are sample-wise optimal.
- Teacher quality and calibration can limit or bias rectification.
- Repeated-seed uncertainty and statistical testing are not prominent.
- Extra robust-teacher training and adversarial validation increase cost.
- No official implementation was identified for independent verification.

## Potential Improvements

1. Release code, checkpoints, split definitions, seeds, and all teacher/validation settings.
2. Report repeated-seed intervals and sensitivity to validation size, threat model, temperature, and interpolation.
3. Collect per-example semantic and ambiguity labels for a subset to test the latent-distribution account directly.
4. Compare multiple teachers, ensembles, calibration methods, and teacher-free regularizers under equal compute.
5. Evaluate adaptive attacks, cross-attack transfer, corruptions, distribution shift, and compute/energy costs.

## Potential Implementations

| Implementation | Purpose | Required evidence | Main risk | Acceptance signal |
|---|---|---|---|---|
| Adversarial label auditor | Compare inherited and teacher distributions | predictions, perturbations, validation labels | teacher bias | stable gap reduction across attacks/seeds |
| Calibration sandbox | Tune without contaminating test evidence | held-out adversarial validation | threat-model overfit | transfer to unseen attacks |
| Semantic review queue | Escalate ambiguous perturbations | images, annotator protocol, uncertainty | subjective labels | inter-rater agreement and calibrated abstention |

## Three Ways to Exercise This Research

### 1. Reproduce the Gap Tables

- Recreate CIFAR-10/100 PGD-AT and all label variants with pinned splits and three or more seeds.
- Report best/last AutoAttack accuracy, gap, clean accuracy, and confidence intervals.
- Match teacher and student compute when comparing alternatives.

### 2. Test Calibration Transfer

- Learn parameters on one held-out attack and evaluate unseen white-box and black-box attacks.
- Sweep validation size, perturbation radius, teacher checkpoint, and calibration family.
- Record NLL, ECE, robust accuracy, and per-example target stability.

### 3. Audit Semantic Assumptions

- Sample adversarial pairs across confidence and disagreement strata.
- Ask multiple annotators whether the original class remains uniquely supported.
- Compare annotations with inherited, teacher, and rectified distributions, allowing abstention.

## Example MVP Product

### Robust Target Audit Bench

- `Purpose`: test whether adversarial soft-target correction generalizes beyond the calibration threat model.
- `Inputs`: student/teacher checkpoints, attacks, clean and adversarial validation/test sets, semantic annotations, compute budget.
- `Core mechanism`: generate adversarial examples, log inherited/teacher/rectified distributions, calibrate on a held-out slice, then test unseen attacks and shifts.
- `Outputs`: best-last gaps, robust and clean accuracy, NLL/ECE, target divergence, annotation agreement, compute/energy ledger, and failure samples.
- `Evaluation`: repeated-seed intervals, cross-attack transfer, validation sensitivity, semantic agreement, and cost-adjusted improvement.
- `Safety boundary`: research benchmarking only; rectified predictions are not verified labels or safety guarantees.

## Related Research and Reading

1. [ViT Semantic Robustness](../../DEP-E-20260716-ViT%20Semantic%20Robustness/vit_semantic_robustness_manuscript.md) - tests representation movement under bounded perturbations and highlights the missing human semantic-equivalence check.
2. [PAC Confidence](../../DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md) - supplies finite-sample calibration discipline and warns that adversarial shift can invalidate on-distribution guarantees.
3. [AFIDAF Vision Filters](../../DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md) - motivates matched architecture, corruption, resolution, and hardware audits rather than isolated accuracy claims.

## Source References

1. Dong, C., Liu, L., and Shang, J. *Label Noise in Adversarial Training: A Novel Perspective to Study Robust Overfitting*. arXiv:2110.03135v4. https://arxiv.org/abs/2110.03135v4
2. Full-paper PDF. https://arxiv.org/pdf/2110.03135
3. Full-paper HTML. https://arxiv.org/html/2110.03135
4. NeurIPS 2022 proceedings record. https://proceedings.neurips.cc/paper_files/paper/2022/hash/6fe6a2ba2594521d15af3b1f2162d79c-Abstract-Conference.html
5. arXiv DOI. https://doi.org/10.48550/arXiv.2110.03135
6. ViT Semantic Robustness DEP-E. `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md`
7. PAC Confidence DEP-E. `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
8. AFIDAF Vision Filters DEP-E. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md`

## Appendix

### Selected Quantitative Record

| Dataset / method | Robust best | Robust last | Gap | Reviewer note |
|---|---:|---:|---:|---|
| CIFAR-10 AT | 47.35 | 41.42 | 5.93 | reference |
| CIFAR-10 KD-AT-Auto | 49.05 | 48.80 | 0.25 | learned rectification |
| CIFAR-100 AT | 24.79 | 19.75 | 5.04 | reference |
| CIFAR-100 KD-AT-Auto | 26.36 | 26.24 | 0.12 | learned rectification |
| Tiny-ImageNet AT | 17.20 | 15.40 | 1.80 | reference |
| Tiny-ImageNet KD-AT-Auto | 18.29 | 18.39 | -0.10 | last slightly exceeds best column |

### Provenance and Distribution

- Random draw: uniform zero-based index 27,298 among 75,776 unique paper units; first draw accepted.
- Source gate: valid PDF plus repaired and verified official full-paper HTML; metadata HTML never counted as paper content.
- Cache: missing-only extraction changed miss to cached in about 1.6 seconds; a PDF image decode warning did not prevent text extraction; source package absent.
- Dedup: exact/base ID, DOI, both titles, normalized title, slug, artifact, memory, companion-repository, and 24-hour scans clear.
- Distribution: no PDF, HTML, metadata, source archive, cache, extracted text, or local archive reference is included in the repository.
