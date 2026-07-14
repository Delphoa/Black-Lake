---
title: "MSAIC ECG - DEP-E"
generated_at: "2026-07-15"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of MSAIC-Net for imbalanced multi-lead ECG classification and research-only clinical evidence design."
source_status: "mixed: verified local sources and public URLs; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-15"
temporal_cutoff: "2026-07-15"
primary_url: "https://arxiv.org/abs/2606.06718"
stable_identifier: "arXiv:2606.06718v1; DOI 10.48550/arXiv.2606.06718"
confidence_summary: "High for source transcription; medium for comparative interpretation; low for clinical deployment readiness."
safety_scope: "clinical research evaluation only; no diagnosis or automated care decision"
distribution_notes: "No source document is redistributed; public artifacts contain URLs and derived review text only."
---

# MSAIC ECG - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public-Safe Location | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | MSAIC-Net arXiv record | Primary metadata | HTML | arXiv:2606.06718v1; submitted 2026-06-04 | https://arxiv.org/abs/2606.06718 | arXiv non-exclusive distribution license shown; metadata used for attribution | 2026-07-15 | Inspected |
| S2 | MSAIC-Net full paper | Primary manuscript | PDF | arXiv:2606.06718v1; 4,053,909-byte verified local file | https://arxiv.org/pdf/2606.06718; local path withheld | Source used as evidence only; file not redistributed | 2026-07-15 | Verified and inspected |
| S3 | MSAIC-Net full-paper HTML | Primary manuscript | HTML | official arXiv full-paper rendering; 320,177 bytes | https://arxiv.org/html/2606.06718; local path withheld | Complete paper, not abstract metadata; file not redistributed | 2026-07-15 | Verified and inspected |
| S4 | MSAIC-Net source package | Primary source package | TeX/archive | official arXiv source endpoint | https://arxiv.org/e-print/2606.06718; local path withheld | Used for archive and formula/source cross-check; file not redistributed | 2026-07-15 | Archive listing inspected |
| S5 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2606.06718 | https://doi.org/10.48550/arXiv.2606.06718 | Metadata reference | 2026-07-15 | Inspected |
| S6 | Hypercomplex MRI - DEP-E | Related processed artifact 1 of 3 | Markdown | DEP-E-20260713-Hypercomplex MRI | `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md` | Repository evidence; primary basis arXiv:2503.05063 | 2026-07-15 | Inspected |
| S7 | AV Emotion Fusion - DEP-E | Related processed artifact 2 of 3 | Markdown | DEP-E-20260713-AV Emotion Fusion | `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md` | Repository evidence; primary basis arXiv:2006.08129 | 2026-07-15 | Inspected |
| S8 | PAC Confidence - DEP-E | Related processed artifact 3 of 3 | Markdown | DEP-E-20260713-PAC Confidence | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Repository evidence; primary basis arXiv:2011.00716v5 | 2026-07-15 | Inspected |
| S9 | Black Lake README and DEP filing rules | Deposition authority | Markdown | live fetched `main` revision | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Governs class, naming, inventory, attribution, source withholding, stability, and commit format | 2026-07-15 | Fetched and inspected |
| S10 | Black-Lake-Data README | Related repository authority | Markdown | live fetched `main` revision | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Governs related DEP layout and provenance used during dedup/context review | 2026-07-15 | Fetched and inspected |

Paper metadata:

- `Full title`: MSAIC-Net: A Multi-Scale Attention and Imbalance-Aware Contrastive Network for ECG-Based Myocardial Substrate Abnormality Detection.
- `Authors`: Canyu Lei, Fenglin Zhang, Derek Bivona, Cristiane Singulane, Jonathan Pan, Kenneth Bilchick, Amit R. Patel, and Jianxin Xie.
- `Source platform`: arXiv.
- `Submission/version date`: v1 submitted 2026-06-04.
- `Subjects`: Machine Learning (cs.LG), Artificial Intelligence (cs.AI), and Systems and Control (eess.SY).
- `Venue or peer-review status`: Not available from inspected sources. This artifact does not imply peer review or acceptance.
- `Primary tasks`: MRI-defined myocardial scar classification on an institutional UVA cohort and myocardial infarction classification on a public PTB-XL subset.
- `Code availability`: No paper-declared official implementation was found in the inspected paper or canonical arXiv record.
- `Local source paths`: Withheld by public-output policy. The verified PDF, full-paper HTML, metadata HTML, source package, and local verification records remain outside the repository.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5 | Primary/official metadata | Title, authors, date, categories, version, DOI, abstract | Bibliographic identity and high-level contribution | High | Metadata alone does not validate method or results |
| E2 | S2-S4 | Primary full text/source | Complete method, equations, datasets, ablations, comparative tables, conclusions, source cross-check | Architecture, loss design, evaluation, limitations, and numeric transcription | High for source reporting | No experiment, proof, or code path independently reproduced |
| E3 | S2-S3, Table 1 | Primary empirical evidence | UVA ablation: baseline and component rows for AUPRC, AUROC, F1 | Component contribution on the source-reported UVA split | High for transcription | One split; no seeds, confidence intervals, patient-level uncertainty, or external cohort |
| E4 | S2-S3, Table 2 | Primary empirical evidence | PTB-XL ablation across multi-scale convolution, channel attention, SCL, and FSCL | Component contribution on the public-dataset task | High for transcription | No rerun; focal SCL is not best on every metric |
| E5 | S2-S3, Tables 3-4 | Primary comparative evidence | Transformer, ResNet, LSTM, CNN-LSTM, and MSAIC-Net comparisons | Source-reported baseline position | High for values; medium for fairness | Baseline tuning parity and statistical uncertainty are not exposed |
| E6 | S2-S4, Sections 3.4 and 4.4 | Primary method/result evidence | Lead perturbation definitions, performance drops, lead rankings, clinical interpretation | Model reliance and interpretability claim | Medium | Gaussian replacement and cross-sample shuffling conflict; correlated-lead and OOD effects remain |
| E7 | S6 | Related DEP evidence | Clinical model-efficiency review, limited-data critique, resource and pathology-preservation boundaries | Systems and clinical-transfer synthesis | Medium | Different modality and reconstruction task |
| E8 | S7 | Related DEP evidence | Physiological-signal fusion, group-disjoint split lineage, imbalance, corruption, and calibration review | Representation and evaluation synthesis | Medium | Different task, labels, and modalities |
| E9 | S8 | Related DEP evidence | Finite-sample interval confidence, thresholding, abstention, and on-distribution limitation | Decision-layer and shift-boundary synthesis | Medium | Not applied to MSAIC-Net predictions or cohorts |
| E10 | S9-S10 and public-safe process record | Repository/process evidence | Live rules, random draw, dedup scans, source-integrity repair, allowlist policy | Eligibility and artifact compliance | High | Private local paths and exact execution times are intentionally omitted |

## Executive Summary

MSAIC-Net is a multi-lead ECG classifier designed for subtle, multi-scale, class-imbalanced myocardial substrate signals. Parallel dilated 1D-convolution branches learn short- and long-range temporal patterns; channel attention recalibrates feature channels; focal binary cross-entropy trains the output classifier; and a focal supervised contrastive loss emphasizes difficult same-class pairs. A separate perturbation analysis estimates which ECG leads most affect predictions.

The paper evaluates two related but distinct tasks. The UVA cohort uses late-gadolinium-enhancement cardiac MRI labels for myocardial scar and expands a limited patient cohort into 7,056 temporal segments. The PTB-XL subset contains 12,428 ECGs for MI-versus-negative classification. The authors state that splits are patient-level. On UVA, full MSAIC-Net reports AUPRC 0.9757, AUROC 0.9366, and F1 0.9169, compared with 0.8935, 0.7853, and 0.8593 for a CNN plus focal BCE. On PTB-XL, full MSAIC-Net reports 0.9343, 0.9678, and 0.8576, compared with 0.9042, 0.9531, and 0.8209. The smaller UVA setting shows the larger gain.

The evidence supports a narrow conclusion: multi-scale temporal modeling is the strongest source-reported architectural addition, and hard-pair-aware contrastive regularization can improve imbalance-sensitive metrics in the tested settings. It does not establish clinical readiness, prospective screening utility, external-site generalization, calibrated risk, causal lead localization, or hardware efficiency. Training details needed for exact reproduction are incomplete, no official implementation was found, statistical uncertainty is missing, and the lead-perturbation operator is inconsistent between method and results.

The three related DEP entries turn those gaps into an implementation boundary. AV Emotion Fusion emphasizes patient/group lineage, pathway-value tests, and corruption/missingness stress. Hypercomplex MRI separates model-size or architecture claims from latency, memory, pathology preservation, and clinical safety. PAC Confidence makes finite calibration support, distribution match, and abstention explicit. Reviewer confidence is high for transcription of the paper's method and tables, medium for causal/component interpretation, and low for deployment claims.

## Detailed Summary

### Problem and Clinical Context

Myocardial scar, fibrosis, and infarction-related injury alter cardiac electrical propagation and can increase risk of ventricular arrhythmia, heart failure, and sudden cardiac death. LGE-CMR provides tissue characterization but is expensive and less available than surface ECG. The paper asks whether multi-lead ECG can provide a lower-cost screening signal for myocardial substrate abnormalities.

The learning problem is difficult for four reasons. Relevant patterns can be local, such as QRS or ST-segment morphology, or longer-range, such as rhythm and conduction behavior. Different leads provide correlated projections of cardiac electrical activity. The label distributions are imbalanced. Finally, a clinical user needs evidence about model reliance and failure, not only a score.

The paper formulates binary classification over a `D x T` multi-lead time series. The output is the probability of the abnormal class. UVA and PTB-XL do not share an identical clinical label: the first targets MRI-defined scar and the second targets MI. The two tasks therefore test architectural transfer across related substrates rather than direct replication of the same endpoint.

### Multi-Scale Attention Architecture

MSAIC-Net contains `L` parallel branches with distinct dilation rates. Smaller dilation rates target fine-grained waveforms; larger rates target broader temporal dependencies. Each branch stacks `K` attention-enhanced atrous convolution blocks. A block performs dilated 1D convolution followed by channel attention. Batch normalization, ReLU, and dropout follow convolution.

Channel attention pools each channel across time, applies a one-dimensional convolution over the channel descriptor, passes it through a sigmoid, and multiplies the resulting weights into the feature channels. Branch outputs are concatenated, compressed by a projection convolution, globally averaged over time, and passed to a classifier.

This design embeds two distinct structures. Dilation models multiple temporal receptive fields. Channel recalibration models unequal utility among learned features and indirectly among lead-derived patterns. The paper does not publish all concrete architecture values needed to reconstruct the network, including the complete branch/dilation configuration and every training hyperparameter.

### Imbalance-Aware Objectives

The classification loss is focal binary cross-entropy. Its class-balance parameter `alpha` can change the relative weight of positive and negative examples, while the focusing exponent reduces the contribution of easy predictions.

The representation loss starts from supervised contrastive learning. Same-label samples form positive pairs; different-label samples form negative pairs. The proposed focal supervised contrastive loss multiplies each positive-pair log probability by `(1 - eta)^gamma_c`, so poorly aligned positive pairs receive more relative weight than already aligned pairs. The total loss is focal BCE plus `lambda` times focal supervised contrastive loss.

The term “imbalance-aware” should be read carefully. Focal BCE has an explicit class-balancing factor. Focal supervised contrastive learning explicitly emphasizes hard positive pairs, not class frequency by itself. Its minority-class behavior also depends on mini-batch composition, whether anchors have same-class positives, `gamma_c`, temperature, and the loss weight. These implementation details are not fully reported.

### Lead-Level Perturbation Importance

For one lead, the method section replaces its waveform with Gaussian noise whose mean and variance are estimated from that lead, then measures prediction change and the drop in cohort AUROC/AUPRC. The results section instead says that the lead is randomly shuffled across the test set. Gaussian replacement and cross-sample shuffling preserve different marginal and temporal properties, so the inconsistency is material.

The source reports V2 as most important for both UVA scar and PTB-XL MI. V1 and I are also prominent on UVA; V3, II, and V4 are prominent on PTB-XL. The authors relate V2 to septal-anterior electrical patterns but warn that surface lead importance is a cohort-level association, not direct anatomical localization.

Perturbation importance is a reliance test. It does not prove that a lead is causal or clinically sufficient. Correlated leads can share or mask information, and a replacement waveform can be out of distribution. A robust follow-up should compare multiple preregistered perturbations, conditional/correlation-aware controls, seed intervals, and clinical review.

### Data and Preprocessing

The UVA data use LGE-CMR-derived scar labels. Segmentation-based augmentation expands recordings into 7,056 samples, with 5,632 train and 1,424 test segments. The training segments contain 3,968 scar-positive and 1,664 normal examples, a 70.5% positive rate. The main paper does not expose a stable unaugmented patient-count table sufficient for independent split reconstruction.

The PTB-XL subset contains 12,428 ECG samples: 2,950 MI-positive and 9,478 negative. The 80/20 split yields 9,946 training and 2,482 test samples. The training set contains 2,366 positives and 7,580 negatives, a 23.8% positive rate.

Both datasets are noise filtered with BioSPPy and amplitude normalized. The authors state that splitting occurs at patient level so segments from one patient cannot cross partitions. That is an important control, but the paper does not provide the split manifest, repeated folds, calibration partition, or external-site test needed to independently verify lineage and estimate variance.

### Ablation Evidence

UVA ablation:

| Model | AUPRC | AUROC | F1 |
|---|---:|---:|---:|
| CNN + focal BCE | 0.8935 | 0.7853 | 0.8593 |
| Multi-scale CNN + focal BCE | 0.9475 | 0.8857 | 0.9095 |
| Multi-scale CNN + channel attention + focal BCE | 0.9558 | 0.8978 | 0.9008 |
| Above + standard supervised contrastive loss | 0.9634 | 0.9111 | 0.9016 |
| Full MSAIC-Net with focal supervised contrastive loss | 0.9757 | 0.9366 | 0.9169 |

Multi-scale convolution produces the largest first-step gain. Channel attention raises AUPRC and AUROC but lowers F1 relative to multi-scale convolution alone. Standard contrastive learning increases ranking metrics while F1 remains below the multi-scale-only row. Focal contrastive learning reports the best row across all three UVA metrics.

PTB-XL ablation:

| Model | AUPRC | AUROC | F1 |
|---|---:|---:|---:|
| CNN + focal BCE | 0.9042 | 0.9531 | 0.8209 |
| Multi-scale CNN + focal BCE | 0.9277 | 0.9653 | 0.8579 |
| Multi-scale CNN + channel attention + focal BCE | 0.9299 | 0.9653 | 0.8498 |
| Above + standard supervised contrastive loss | 0.9306 | 0.9700 | 0.8530 |
| Full MSAIC-Net with focal supervised contrastive loss | 0.9343 | 0.9678 | 0.8576 |

Here the tradeoff is more visible. Full MSAIC-Net has the best AUPRC and near-best F1, but standard supervised contrastive learning has the best AUROC. The multi-scale-only row has F1 0.8579, slightly above the full row's 0.8576. “Best” therefore depends on the prespecified metric and operating context.

### Comparative Evidence

On UVA, the paper reports MSAIC-Net above Transformer, ResNet, LSTM, and CNN-LSTM baselines, with AUROC/AUPRC/F1 of 0.9366/0.9757/0.9169. The nearest listed baseline is ResNet at 0.8778/0.9378/0.8839.

On PTB-XL, MSAIC-Net reports 0.9678/0.9343/0.8576. CNN-LSTM reports 0.9677/0.9326/0.8523. The AUROC difference is only 0.0001, while AUPRC and F1 differ by 0.0017 and 0.0053. Without repeated runs and confidence intervals, these small differences should not be presented as stable superiority.

### Evidence Boundary

No result was independently reproduced. No official code, checkpoint, environment pin, split manifest, or expected-run output was found. The paper does not report external-site validation, prospective workflow testing, calibration, decision curves, per-patient uncertainty, subgroup/fairness analysis, or clinical-reader assessment. The manuscript supports research follow-up, not diagnosis or deployment.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Parallel dilated convolution and channel attention capture multi-scale, channel-dependent ECG features. | Author method claim | E2 | The architecture directly implements this mechanism; whether every branch adds unique information is not isolated. | High for description; medium for benefit |
| C2 | Focal supervised contrastive learning emphasizes hard positive pairs. | Author method claim | E2 | The focal weight supports this interpretation; class-imbalance benefit also depends on class/batch composition and loss settings. | High for mechanism; medium for imbalance claim |
| C3 | Multi-scale convolution is the largest architectural contributor in both ablations. | Reviewer interpretation of author tables | E3-E4 | The first-step metric gains are larger than later additions in the displayed rows. | High for table reading |
| C4 | Full MSAIC-Net achieves 0.9757 AUPRC, 0.9366 AUROC, and 0.9169 F1 on UVA. | Author empirical claim | E3 | Direct table transcription; no independent rerun or uncertainty. | High for transcription; low for external validity |
| C5 | Full MSAIC-Net achieves 0.9343 AUPRC, 0.9678 AUROC, and 0.8576 F1 on PTB-XL. | Author empirical claim | E4 | Direct table transcription; it is not best on every displayed metric. | High for transcription; medium for ranking interpretation |
| C6 | MSAIC-Net outperforms listed architectures on both datasets. | Author comparative claim | E5 | Displayed point estimates support the row ranking, but PTB-XL differences are small and baseline parity is unverified. | Medium |
| C7 | V2 carries the strongest lead-level importance on both tasks. | Author empirical claim | E6 | Reported figures/text support it; operator inconsistency and correlation prevent causal interpretation. | Medium |
| C8 | The framework is suitable for screening and clinical decision support. | Author implication | E2-E6 | Plausible research direction, not established by retrospective point metrics. | Low |
| C9 | Patient lineage, interval calibration, shift checks, resource telemetry, and fallback should gate any implementation. | Reviewer synthesis | E7-E9 | Strong cross-DEP conceptual support; no joint experiment exists. | Medium |
| C10 | The selected archive unit is complete and eligible for a new DEP-E review. | Process claim | E10 | Random draw, cross-repository dedup, PDF/HTML integrity, and no-source-upload gates passed. | High |

## Methodology

- `Research objective`: Randomly select one eligible locally archived arXiv paper, verify that its complete PDF and full-paper HTML are available, review it source-first, bridge it with exactly three concrete DEP entries, and create a schema-complete public-safe DEP-E manuscript.
- `Sources inspected`: Verified local PDF, official arXiv full-paper HTML, official metadata HTML, official source package, local README/provenance/verification records, canonical arXiv and DOI URLs, live Black Lake and Black-Lake-Data READMEs, repository dedup markers, automation memory, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, normalized each PDF parent as one paper unit, sorted unique units, selected a uniform zero-based index with PowerShell `Get-Random`, then derived the arXiv ID/title from the unit metadata.
- `Inclusion criteria`: Direct primary evidence for identity, mechanism, datasets, metrics, limitations, source integrity, repository authority, duplicate status, or a concrete bridge to clinical-model evaluation, physiological-signal fusion, or finite-sample confidence.
- `Exclusion criteria`: Abstract-only evidence, unverified code claims, secondary commentary, unrelated DEP entries, source-package draft comments as authoritative results, and any local source file for public deposition.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication review.
- `Evidence handling`: Author claims, source-reported values, reviewer interpretation, negative evidence, and process evidence use separate labels and ledger IDs. No metric is described as independently reproduced.
- `Uncertainty handling`: Missing hyperparameters, patient counts, repeated seeds, statistical intervals, external validation, calibration, code, and the perturbation conflict remain explicit rather than being inferred away.
- `Extraction process`: Full-paper HTML was inspected directly; PDF and source package were used for independent document/source cross-checks. The metadata HTML was used only for identity/provenance and did not satisfy the paper gate.
- `Version control`: Review is pinned to arXiv:2606.06718v1. Public sources were accessed on 2026-07-15. No later revision or venue record was inferred.
- `Claim selection`: Prioritized the architecture, focal contrastive mechanism, patient-level split claim, complete numeric tables, lead perturbation, missing evidence, and implementation boundaries.
- `Cross-checking`: Numeric tables and method text were compared across the PDF/full HTML; source-package text was searched for omitted settings; canonical metadata was checked against the arXiv record.
- `Safety handling`: Clinical ideas are framed as offline research/evaluation with human review, abstention, public or governance-approved data, and no automated diagnosis.
- `Reviewer stance`: Skeptical paper report, DEP-ready preservation, replication triage, and bounded clinical-AI product translation.
- `Random selection`: 75,776 PDF candidates and 75,776 unique parent-directory paper units were enumerated. Uniform zero-based index 65,580 selected arXiv:2606.06718. Randomness was generated by the command and was not manually substituted.
- `Deduplication and reselection validation`: Scanned Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data `.logs`, `.reports`, and `.lake-data` context for base/versioned ID, DOI, exact title, `MSAIC-Net`, and `MSAIC ECG`. The selected draw had no duplicate or 24-hour marker; exclusions 0, reselections 0; public cutoff date 2026-07-14.
- `Source-integrity repair`: The selected unit was initially partial because full-paper HTML was absent. The valid PDF was preserved. Official full HTML, metadata HTML, and source package were fetched with a bounded local-only repair. Local README, provenance, summary, and verification records were updated before review.
- `Source-integrity verification`: The 4,053,909-byte PDF begins with `%PDF-` and contains a trailing `%%EOF`. The 320,177-byte full HTML contains 101,684 post-strip body characters, a document marker, 58 heading/section markers, and six paper-structure terms. Zero `.part` files remained.

## Scope, Constraints, and Assumptions

- `Scope`: MSAIC-Net architecture, losses, UVA/PTB-XL data, ablation/comparative evidence, lead importance, reproducibility limits, clinical research implications, and exactly three related DEP bridges.
- `Temporal boundary`: Primary paper pinned to 2026-06-04 v1; public/repository evidence inspected through 2026-07-15.
- `Evidence limits`: No code, checkpoint, dataset, split manifest, protected health information, experiment, statistical analysis, or clinical workflow was independently obtained or executed.
- `Assumptions`: The verified local PDF/full HTML correspond to arXiv v1; the displayed tables accurately represent the authors' completed experiments; repository manuscripts accurately preserve their cited reviews.
- `Constraints`: No source file, extracted text, cache, local path, machine context, or patient data may be published. High-stakes medical conclusions require external evidence and human oversight.
- `Out of scope`: Diagnosis, prospective validation, regulatory approval, treatment selection, patient-specific interpretation, source-code audit, dataset-license audit, and production deployment.
- `Intended use`: DEP preservation, research triage, replication planning, clinical-AI evaluation design, and bounded MVP ideation.
- `Audience`: ECG/clinical ML researchers, biomedical engineers, model-risk reviewers, and Black Lake maintainers.
- `Depth target`: Full schema-complete manuscript review.
- `Reproducibility boundary`: Public paper artifacts support a future attempt, but the missing implementation/configuration prevents exact reproduction from this artifact.
- `Operational boundary`: Output may guide offline evaluation and human review; it cannot authorize clinical action or imply that confidence equals safety.
- `Data sensitivity`: Public scholarly metadata and derived review text only. Institutional patient data and local source artifacts remain outside the DEP.

## Observations

- `Observed pattern`: Multi-scale convolution supplies the largest and most consistent ablation gain on both datasets. Later modules improve some metrics while trading others.
- `Metric tension`: On PTB-XL, standard supervised contrastive learning has the highest AUROC, while focal supervised contrastive learning has the highest AUPRC and near-highest F1. Component superiority is metric-dependent.
- `Regime tension`: The strongest reported improvement occurs in the lower-data UVA setting, where single-split variance, augmentation lineage, and calibration scarcity are most consequential.
- `Mechanistic observation`: Focal supervised contrastive learning is explicitly hard-pair-aware; it is only indirectly class-imbalance-aware unless batch construction and class weighting ensure minority support.
- `Interpretability tension`: Input-lead perturbation and latent channel attention answer different questions. Neither should be presented as direct anatomical localization.
- `Source inconsistency`: The perturbation method specifies Gaussian replacement while the results describe random shuffling. This is a reproducibility blocker, not a cosmetic wording difference.
- `Cross-source pattern`: The selected paper and all three related DEPs make model structure visible but leave deployment validity to separate evidence about lineage, shift, resources, calibration, and fallback.
- `Reviewer hypothesis`: A patient-disjoint, calibration-gated multi-scale encoder will be more decision-useful than a higher-AUROC model whose support, shift state, and lead-reliance stability are hidden.

## Considerations

### Clinical Validity

Retrospective discrimination is not clinical utility. A screening system needs external sites, prevalence shifts, subgroup and rhythm slices, calibration, sensitivity at prespecified false-positive budgets, decision-curve analysis, prospective workflow impact, and a defined confirmatory pathway. LGE-CMR and MI labels are related but not interchangeable clinical endpoints.

### Split and Augmentation Lineage

Patient-level splitting is necessary but should be independently auditable. Every original ECG, repeat recording, temporal segment, augmentation descendant, calibration example, and test sample should belong to one immutable patient group and one partition. Report patient counts and patient-level intervals rather than treating correlated segments as independent evidence.

### Calibration, Shift, and Abstention

Softmax outputs do not express finite-sample support. PAC-style intervals can expose support for a score range, but only inside a matching calibration/deployment distribution. Site, device, waveform quality, rhythm, prevalence, and label changes should trigger a fail-closed review or recalibration path. Abstention utility must include human-review capacity and delay.

### Interpretation

Lead perturbation can help detect reliance on implausible inputs, but replacement distributions must be prespecified and clinically audited. Correlated leads, derived limb leads, preprocessing, and out-of-distribution artifacts complicate rankings. Use repeated perturbations, conditional controls, bootstrapped patient intervals, and clinician review. Do not convert cohort reliance into patient-specific localization.

### Resource and Operations

No edge-efficiency claim is supported without checkpoint size, peak memory, preprocessing cost, p50/p95/p99 latency, energy, throughput, and fallback measurements on target hardware. Model and calibration versions, input-quality checks, drift alarms, and review outcomes require joint lifecycle governance.

### Ethics and Governance

Clinical ECGs are sensitive health data. A research implementation should minimize data, use de-identified study IDs, restrict access, avoid raw-signal logging, preserve consent and retention boundaries, and support correction/deletion. Outputs must be presented as research suggestions, not diagnoses.

## Strengths

- The architecture directly targets multi-scale temporal morphology and unequal feature-channel utility in multi-lead ECG.
- The paper reports ablations that separate multi-scale convolution, channel attention, standard supervised contrastive learning, and focal supervised contrastive learning.
- AUPRC is emphasized alongside AUROC and F1, which is appropriate for imbalanced tasks.
- Evaluation spans a limited institutional scar cohort and a larger public MI dataset with different class directions.
- Patient-level splitting is explicitly stated to reduce leakage across augmented segments.
- Lead-level perturbation attempts to expose reliance rather than presenting the classifier as opaque.
- The paper preserves metric tradeoffs: focal contrastive learning is not silently presented as best on every PTB-XL metric.

## Weaknesses

- Training and architecture configuration is incomplete, and no official implementation or checkpoint was found.
- Unaugmented patient counts and an auditable split manifest are missing from the published main text.
- One patient-level split per dataset cannot quantify variance; repeated folds, seeds, intervals, and statistical tests are absent.
- Comparative baseline tuning and compute parity are not established.
- External-site, prospective, subgroup, prevalence-shift, and calibration evidence is absent.
- The UVA and PTB-XL tasks use different targets, limiting direct cross-dataset interpretation.
- The perturbation operator conflicts between method and results, and correlated-lead/OOD controls are missing.
- Lead importance is a model-reliance measure but is discussed near clinical anatomy, which can invite overinterpretation.
- No latency, memory, energy, or deployment evidence supports large-scale screening or clinical decision-support claims.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Release code, configs, checkpoints, and environment pins | Reproducibility | Current text cannot recreate the network/training procedure | Independent verification and faster correction | Maintenance and data-path abstraction | Clean-room run reproduces every table within declared tolerances |
| Publish patient and segment lineage manifests | Data integrity | Augmented counts obscure independent sample support | Auditable leakage prevention and patient-level uncertainty | Governance and de-identification work | Hash-based group invariants and zero cross-partition descendants |
| Run repeated patient-disjoint and external-site studies | Generalization | One split and one institutional site cannot establish transfer | Stable effect estimates and boundary conditions | Compute, approvals, and data access | Repeated folds, site holdouts, bootstrap CIs, preregistered metrics |
| Prespecify and reconcile lead perturbations | Interpretability | Gaussian replacement and shuffling are different interventions | Reproducible rankings and honest uncertainty | Additional evaluation and clinician review | Multiple operators, conditional controls, rank stability, patient bootstrap |
| Add calibration, shift, and abstention evaluation | Decision safety | Point scores do not expose support or deployment mismatch | Safer research routing and visible uncertainty | More labeled data and review load | Interval coverage, ECE/Brier, risk-coverage, shift drills, fallback load |
| Report patient-level and subgroup metrics | Clinical evidence | Segment-level aggregates can hide clustered error and harm | More decision-relevant evidence | Sparse slices and multiplicity | Sensitivity/specificity/AUPRC/CIs by patient, site, rhythm, demographic slice |
| Measure operational resources | Systems | Architecture complexity is not deployment efficiency | Honest edge/clinical workflow assessment | Hardware instrumentation | Checkpoint, peak memory, latency tails, energy, throughput, preprocessing cost |
| Compare matched imbalance and representation baselines | Causal ablation | Gains may come from capacity, tuning, batch composition, or focal weighting | Isolate the new loss and architecture value | Larger experiment grid | Matched BCE/SCL/class-balanced samplers, equal parameter/compute budgets |

## Potential Implementations

1. `Patient-Lineage ECG Evidence Gate`
   - `User`: Clinical-ML research team evaluating an ECG classifier.
   - `Goal`: Prevent leakage and unsupported metric claims before model comparison.
   - `Core mechanism`: Validate patient/recording/segment ancestry, compute patient-level metrics and intervals, and reject any run with cross-partition descendants.
   - `Required inputs`: De-identified study IDs, patient groups, segment lineage, labels, predictions, model/config hashes.
   - `Outputs`: Split certificate, patient-level metric card, unsupported-slice list, and reviewer decision.
   - `Risk controls`: Local-only processing, no raw-signal export, minimum slice support, human approval, research-only labeling.
   - `Evaluation`: Synthetic leakage fixtures, deterministic metric hashes, repeated-fold intervals, and privacy review.

2. `Shift-Aware ECG Review Queue`
   - `User`: Offline clinical research reviewer.
   - `Goal`: Route predictions to review only when calibration support and input-envelope checks are visible.
   - `Core mechanism`: Join score-bin intervals, ECG quality, site/device/rhythm shift indicators, and a fallback state.
   - `Required inputs`: Held-out calibration predictions, adjudicated labels, de-identified slice metadata, quality signals, review capacity.
   - `Outputs`: Supported/review/unsupported state with interval, support count, shift flag, and model/calibration versions.
   - `Risk controls`: No automatic diagnosis, fail closed on shift or sparse support, no raw ECG logging, human override.
   - `Evaluation`: Coverage, interval width, sensitivity, abstention, shift detection, review load, and delay.

3. `Multi-Scale Encoder Pareto Lab`
   - `User`: Biomedical ML and edge-systems engineer.
   - `Goal`: Test whether multi-scale/attention/contrastive gains survive matched resource and calibration constraints.
   - `Core mechanism`: Compare baseline, MSAIC-style, compact/factorized, and class-balanced models on identical patient folds and hardware.
   - `Required inputs`: Governance-approved ECG data, immutable folds, reproducible configs, hardware measurement harness.
   - `Outputs`: Quality-calibration-resource Pareto report and lead-reliance stability matrix.
   - `Risk controls`: Offline study only, prespecified metrics, no patient identifiers, no deployment claim.
   - `Evaluation`: AUPRC, sensitivity/specificity, calibration, shift slices, p95 latency, peak memory, energy, and perturbation stability.

## Three Ways to Exercise This Research

1. `Reproduce the loss on synthetic embeddings`: Objective—verify that focal supervised contrastive weights emphasize difficult positive pairs. Inputs—seeded synthetic embeddings and balanced/imbalanced batch layouts. Steps—implement SCL/FSCL, sweep temperature and focusing exponent, check gradients and anchors without positives. Output—weight, gradient, and failure-case report. Success criterion—the implementation matches the published formula and exposes class/batch sensitivity. Stop condition—formula ambiguity or numerical instability prevents a deterministic audit. Safety boundary—synthetic data only.
2. `Run a patient-lineage metric replay`: Objective—measure how segment multiplication changes apparent uncertainty. Inputs—governance-approved de-identified group IDs or a synthetic grouped dataset, predictions, and labels. Steps—compare naive segment intervals with patient-cluster bootstrap intervals and repeated group folds. Output—metric/interval gap and leakage audit. Success criterion—every reported estimate is tied to an independent patient unit. Stop condition—group identity or partition lineage cannot be verified. Safety boundary—no raw clinical signal is required.
3. `Compare lead-perturbation protocols`: Objective—test whether Gaussian replacement and cross-sample shuffling yield stable lead rankings. Inputs—synthetic multi-lead waveforms or approved held-out ECGs, fixed model outputs, preregistered perturbations. Steps—repeat both operators across seeds, add correlated-lead controls, bootstrap rankings by patient, and flag OOD perturbations. Output—operator agreement and uncertainty report. Success criterion—rank conclusions remain stable or the disagreement is explicitly documented. Stop condition—perturbations create clinically uninterpretable inputs or protected data cannot be handled safely.

## Example MVP Product

- `Product name`: ECG Evidence Card.
- `Target user`: Biomedical ML researcher or independent model-risk reviewer.
- `Problem`: A high AUPRC or AUROC can hide patient leakage, sparse calibration support, distribution shift, unstable lead explanations, and impractical review load.
- `Core workflow`: Import de-identified prediction tables and lineage manifests; verify patient-disjoint partitions; compute patient-level metrics and intervals; compare baseline and MSAIC-style ablations; attach calibration support; run shift and lead-perturbation stability checks; record resource telemetry; export a signed Markdown/JSON research evidence card.
- `Data requirements`: De-identified patient/study IDs, record/segment ancestry, labels, predictions, split membership, site/device/rhythm slices, calibration membership, model/config hashes, and aggregate resource measurements. Raw ECG is optional and excluded from the default metric-only path.
- `Architecture`: Local CLI/notebook, schema validator, lineage graph checker, clustered metric engine, interval/calibration module, shift adapter, perturbation protocol registry, resource importer, and static report generator.
- `Success metrics`: Zero lineage violations; deterministic report hash; patient-level intervals for all headline metrics; unsupported slices visible; calibration and shift states explicit; perturbation mode recorded; resource tails present; human decision logged.
- `Risk controls`: Local-only default, no raw-signal logging, allowlisted columns, minimum-support gates, fail-closed shift state, explicit research-only label, no diagnosis or automated action, human approval before any downstream experiment.
- `Limitations`: The MVP audits supplied evidence. It cannot prove label validity, causal physiology, representativeness, clinical utility, consent adequacy, or regulatory compliance. Calibration remains conditional on its data envelope.
- `MVP boundary`: No model training, patient recruitment, care recommendation, treatment selection, online monitoring, or automatic threshold deployment.
- `Deployment model`: Local CLI/notebook inside an approved research environment.
- `Evaluation plan`: Unit tests for grouped splits and metrics; synthetic leakage fixtures; known-bin coverage simulations; golden report snapshots; perturbation protocol tests; privacy/security review; blinded reviewer usability test.
- `Failure modes`: Missing patient groups, duplicated descendants, contaminated calibration data, sparse slices, adaptive threshold leakage, stale shift rules, mismatched perturbation operators, misleading segment-level precision, unavailable human fallback.
- `Maintenance plan`: Version schemas, metric definitions, interval methods, perturbation registry, slice taxonomy, model/calibration manifests, and evidence-card hashes; re-review after any data, model, device, preprocessing, or threshold change.

## Related Research and Reading

### Exactly Three Related DEP Entries

| Entry | Type | Concrete Relevance | Source / Identifier |
|---|---|---|---|
| Hypercomplex MRI - DEP-E | Existing Black Lake manuscript | Supplies a clinical-model efficiency analogue and the boundary between parameter/architecture improvement and measured latency, memory, pathology preservation, calibration, and clinical readiness. | `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md`; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md; primary basis https://arxiv.org/abs/2503.05063 |
| AV Emotion Fusion - DEP-E | Existing Black Lake manuscript | Supplies physiological-signal fusion evidence, group-disjoint lineage, class-imbalance critique, pathway-value tests, corruption/missingness stress, and consent boundaries. | `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md`; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md; primary basis https://arxiv.org/abs/2006.08129 |
| PAC Confidence - DEP-E | Existing Black Lake manuscript | Supplies finite-sample confidence intervals, threshold selection, abstention, support counts, and the explicit on-distribution boundary required for high-stakes decisions. | `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md; primary basis https://arxiv.org/abs/2011.00716 |

### Primary and Near-Primary Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| MSAIC-Net | Primary reviewed paper | Architecture, losses, datasets, metrics, lead importance, and conclusions | https://arxiv.org/abs/2606.06718 |
| PTB-XL, a large publicly available electrocardiography dataset | Dataset paper cited by MSAIC-Net | Public ECG dataset context for the MI task | Scientific Data 7, 154 (2020), as cited in the reviewed paper |
| ECA-Net: Efficient Channel Attention for Deep Convolutional Neural Networks | Method cited by MSAIC-Net | Channel-attention basis for lightweight cross-channel interaction | CVPR 2020, as cited in the reviewed paper |

Synthesis: MSAIC-Net supplies a multi-scale hard-pair-aware ECG representation; AV Emotion Fusion supplies proof obligations for pathway value and group lineage; Hypercomplex MRI supplies clinical system/resource and pathology boundaries; PAC Confidence supplies finite-sample support and abstention. No inspected source jointly validates this architecture.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2606.06718 | Identity, authors, date, categories, abstract, DOI, source navigation | 2026-07-15 | Primary metadata |
| R2 | https://arxiv.org/html/2606.06718 | Full method, equations, datasets, tables, lead analysis, conclusion | 2026-07-15 | Verified complete full-paper HTML |
| R3 | https://arxiv.org/pdf/2606.06718 | Complete manuscript cross-check | 2026-07-15 | Public locator; local file withheld |
| R4 | https://arxiv.org/e-print/2606.06718 | Source-package provenance and source/formula cross-check | 2026-07-15 | Local package withheld |
| R5 | https://doi.org/10.48550/arXiv.2606.06718 | Persistent identity | 2026-07-15 | arXiv-issued DOI |
| R6 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md | Related clinical efficiency and safety synthesis | 2026-07-15 | Related DEP 1 of 3; primary basis https://arxiv.org/abs/2503.05063 |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md | Related signal-fusion and split-lineage synthesis | 2026-07-15 | Related DEP 2 of 3; primary basis https://arxiv.org/abs/2006.08129 |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md | Related interval-confidence and abstention synthesis | 2026-07-15 | Related DEP 3 of 3; primary basis https://arxiv.org/abs/2011.00716 |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Target repository deposition rules | 2026-07-15 | Live default-branch authority fetched before writing |
| R10 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related repository layout and dedup context | 2026-07-15 | Live default-branch authority fetched before use |
| R11 | Verified local paper unit, path withheld | Source-integrity repair, PDF/full-HTML review, metadata, source-package listing | 2026-07-15 | Source documents remain local and are not deposited |

## Appendix

### A. Random Selection and Eligibility Record

- Enumeration command class: `rg --files -g "*.pdf"` against the private archive root.
- PDF candidates: 75,776.
- Unique parent-directory paper units: 75,776.
- Selection method: PowerShell `Get-Random`, uniform zero-based index over sorted unique units.
- Selected index: 65,580.
- Selected identifier: arXiv:2606.06718v1.
- Duplicate scan: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`; automation memory; live Black-Lake-Data `.logs`, `.reports`, `.lake-data` context.
- Keys: base/versioned ID, DOI, exact title, `MSAIC-Net`, `MSAIC ECG`.
- Excluded draws: 0.
- Reselections: 0.
- 24-hour cutoff date: 2026-07-14.

### B. Source-Integrity Record

| Artifact | Validation | Result |
|---|---|---|
| PDF | at least 10 KB, `%PDF-` header, trailing `%%EOF` | Passed; 4,053,909 bytes |
| Full-paper HTML | at least 5 KB and 2,000 body characters | Passed; 320,177 bytes and 101,684 body characters |
| Full-paper structure | article/main/LaTeXML marker, at least two headings, at least two structure terms | Passed; document marker, 58 heading/section markers, six structure terms |
| Metadata HTML | non-empty official `/abs/` record; metadata only | Passed; not counted as the paper |
| Source package | official endpoint and readable archive listing | Passed; kept local |
| Partial files | zero `.part` files after repair | Passed |
| Public-source upload gate | no PDF, HTML, source archive, cache, extracted text, or `.source/` directory | Required and enforced before submission |

### C. Replication Checklist

- [ ] Obtain or reconstruct the complete architecture, branch/dilation, optimizer, scheduler, batch, dropout, loss, and seed configuration.
- [ ] Publish authoritative unaugmented patient counts and immutable patient/record/segment split manifests.
- [ ] Reproduce all ablation and comparison rows across repeated patient-disjoint folds.
- [ ] Report patient-cluster confidence intervals and prespecified primary metrics.
- [ ] Add calibration, Brier/ECE, risk-coverage, decision-curve, and prevalence-shift analysis.
- [ ] Reconcile Gaussian replacement versus cross-sample shuffling and rerun lead rankings with correlation-aware controls.
- [ ] Validate external sites/devices/rhythms and clinically relevant subgroups.
- [ ] Measure checkpoint size, peak memory, p50/p95/p99 latency, energy, preprocessing cost, and fallback load.
- [ ] Require clinical-reader review and a prospective workflow study before any care implication.

### D. Public Source Inventory

Public repository contents for this DEP are limited to this derived manuscript and its DEP README. The source PDF, full-paper HTML, metadata HTML, source package, extraction material, caches, and integrity records remain local. No `.source/` directory is created.
