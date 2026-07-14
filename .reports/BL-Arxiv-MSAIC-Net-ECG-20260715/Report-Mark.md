# Report-Mark: MSAIC-Net ECG Review

Public run date: 2026-07-15

## Source Metadata

| Field | Value |
|---|---|
| Full title | *MSAIC-Net: A Multi-Scale Attention and Imbalance-Aware Contrastive Network for ECG-Based Myocardial Substrate Abnormality Detection* |
| Authors | Canyu Lei; Fenglin Zhang; Derek Bivona; Cristiane Singulane; Jonathan Pan; Kenneth Bilchick; Amit R. Patel; Jianxin Xie |
| Identifier | arXiv:2606.06718v1 |
| DOI | https://doi.org/10.48550/arXiv.2606.06718 |
| Submitted | 2026-06-04 |
| Subjects | Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Systems and Control (eess.SY) |
| Primary public record | https://arxiv.org/abs/2606.06718 |
| Full-paper public HTML | https://arxiv.org/html/2606.06718 |
| Public PDF | https://arxiv.org/pdf/2606.06718 |
| Public source endpoint | https://arxiv.org/e-print/2606.06718 |
| Source state | Verified complete local PDF and full-paper HTML; metadata and source package also preserved locally; all source files withheld from the repository |
| Review status | Full paper inspected; results transcribed but not independently reproduced |

## Concise Research Notes

### Problem

The paper targets low-cost screening for myocardial substrate abnormalities from multi-lead electrocardiograms. Scar and myocardial-infarction signatures can be subtle, appear at different temporal scales, vary by lead, and occur in imbalanced clinical datasets. The authors position ECG as a broadly available complement to late-gadolinium-enhancement cardiac MRI, not as direct tissue imaging.

### Method

MSAIC-Net is a binary multi-lead time-series classifier with four linked components:

1. Parallel atrous 1D-convolution branches capture local waveform morphology and longer-range conduction patterns at different dilation rates.
2. Channel attention applies pooled cross-channel weights inside the convolution blocks, then branch outputs are concatenated, projected, globally pooled, and classified.
3. Focal binary cross-entropy emphasizes difficult classification examples, while focal supervised contrastive learning downweights already well-aligned positive pairs and emphasizes hard same-class pairs in the embedding space.
4. Lead-wise perturbation importance measures sample-level prediction change and cohort-level AUROC/AUPRC degradation after disrupting one ECG lead.

### Evidence and Results

The institutional UVA cohort uses LGE-CMR-derived scar labels and segmentation-based augmentation. The paper reports 7,056 segments, including 5,632 training and 1,424 test segments, with patient-level partitioning. The training segments are 70.5% scar-positive. The public PTB-XL subset contains 12,428 ECGs: 2,950 MI-positive and 9,478 negative, with a patient-level 80/20 split and a 23.8% positive training rate.

On UVA, the baseline CNN plus focal BCE reports AUPRC 0.8935, AUROC 0.7853, and F1 0.8593. Full MSAIC-Net reports 0.9757, 0.9366, and 0.9169. Multi-scale convolution supplies the largest first step; channel attention and contrastive regularization add smaller gains, with focal contrastive learning producing the strongest reported row.

On PTB-XL, baseline CNN plus focal BCE reports AUPRC 0.9042, AUROC 0.9531, and F1 0.8209. Full MSAIC-Net reports 0.9343, 0.9678, and 0.8576. The gains are materially narrower than on UVA. Standard supervised contrastive learning reports a slightly higher AUROC of 0.9700, while focal supervised contrastive learning has higher AUPRC and F1.

Against named architecture baselines, the paper reports MSAIC-Net at AUROC/AUPRC/F1 of 0.9366/0.9757/0.9169 on UVA and 0.9678/0.9343/0.8576 on PTB-XL. On PTB-XL, the AUROC difference from CNN-LSTM is only 0.0001, so the practical distinction rests more on AUPRC and F1 than on AUROC.

The lead analysis ranks V2 highest on both datasets. V1 and I are also prominent on UVA; V3, II, and V4 are prominent on PTB-XL. The authors interpret V2 as a plausible septal-anterior signal, while correctly warning that cohort-level lead importance is not direct anatomical localization.

### Limitations

- The paper does not report a complete reproducible training configuration: branch counts and dilation values, optimizer schedule, batch size, epoch/step budget, loss weights, focusing parameters, dropout values, seeds, and model-selection rules are not all specified.
- Main text reports augmented segment counts but not a stable, authoritative unaugmented patient-count table. Draft comments in the public source package contain conflicting cohort counts, so they are not used as evidence.
- No external-site validation, repeated patient-level folds, confidence intervals, statistical tests, calibration, decision-curve analysis, subgroup analysis, or prospective clinical study is reported.
- PTB-XL and UVA represent different targets—MI and MRI-defined scar—so cross-dataset performance is supportive transfer evidence, not replication of one label definition.
- The method defines lead disruption as Gaussian-noise replacement, while the result section describes random shuffling across the test set. These operators preserve different statistics and can produce different rankings.
- The paper does not expose an official implementation, split manifest, checkpoint, or independently executable reproduction package in the inspected sources.
- Permutation importance measures model reliance, not causal physiology. Correlated leads can redistribute importance, and perturbations may create out-of-distribution waveforms.

### Implementation Relevance

The most transferable contribution is a layered representation pattern: multi-scale temporal features, adaptive channel weighting, and hard-pair-aware contrastive regularization. In a research system, this can be paired with patient-level lineage checks, calibration intervals, shift detection, and human fallback. The architecture may also support compact ECG encoders, but no latency, memory, energy, or device benchmark establishes edge readiness.

### Reviewer Interpretation

The paper provides credible source-reported evidence that multi-scale temporal modeling improves both tasks and that hard-pair-aware contrastive regularization can improve imbalance-sensitive metrics. The evidence is strongest for ablation direction and weakest for clinical transfer, interpretability, and deployment. The UVA improvement is promising but especially vulnerable to uncertainty from limited patient count, segmentation multiplication, and a single patient split. The PTB-XL result suggests the architecture remains competitive at scale, while also showing that some claimed gains become small when the dataset is larger.

## Evidence and Attribution

| ID | Evidence | Supports | Reviewer confidence | Boundary |
|---|---|---|---|---|
| E1 | Official arXiv metadata and v1 record | Identity, authors, date, categories, DOI, abstract | High | Metadata alone cannot validate results |
| E2 | Verified full PDF and official full-paper HTML | Method, datasets, tables, conclusions, limitations | High for transcription | Experiments were not rerun |
| E3 | Official source package | Formula/source cross-check and archive integrity | Medium-high | Commented draft text is not treated as published evidence |
| E4 | UVA and PTB-XL ablation tables | Component-level metric changes | High for source reporting | No intervals, seeds, or independent reproduction |
| E5 | Comparative tables | Architecture comparisons | High for transcription | Baseline tuning parity is not independently audited |
| E6 | Lead-importance method/results | Model-reliance claims and clinical interpretation | Medium | Perturbation operator conflicts across sections |
| E7 | Hypercomplex MRI DEP | Clinical-model efficiency and case-level safety boundary | Medium | Conceptual bridge, not validation of MSAIC-Net |
| E8 | AV Emotion Fusion DEP | Physiological-signal fusion, grouped splits, and imbalance evaluation | Medium | Different labels, modalities, and task |
| E9 | PAC Confidence DEP | Finite-sample calibration, abstention, and distribution boundary | Medium | Not applied to the paper's logits or cohorts |

All numeric results above are author-reported values from the inspected paper. Reviewer synthesis is labeled separately and does not imply independent clinical efficacy.

## Related DEP Entries

Exactly three related entries were selected:

1. [Hypercomplex MRI - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md)
   - Repository path: `.lake-data/DEP-E/DEP-E-20260713-Hypercomplex MRI/hypercomplex_mri_manuscript.md`
   - Relevance: It reviews a clinical imaging model that trades model size against source-reported quality and explicitly separates parameter count from latency, memory, calibration, pathology preservation, and clinical readiness.
   - Source basis: the DEP manuscript and its primary reviewed paper, arXiv:2503.05063.
2. [AV Emotion Fusion - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md)
   - Repository path: `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md`
   - Relevance: It reviews multimodal physiological-signal learning under class imbalance and shows why group-disjoint splits, representation-value tests, calibration, and missing-stream stress tests are required before trusting fusion.
   - Source basis: the DEP manuscript and its primary reviewed paper, arXiv:2006.08129.
3. [PAC Confidence - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md)
   - Repository path: `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
   - Relevance: It supplies finite-sample confidence intervals, threshold selection, abstention logic, and the explicit requirement that calibration and deployment distributions match.
   - Source basis: the DEP manuscript and its primary reviewed paper, arXiv:2011.00716v5.

## Synthesis Note

### Concept Bridge

MSAIC-Net supplies a representation layer for subtle, imbalanced multi-lead signals: temporal scales are separated, informative channels are reweighted, and difficult same-class pairs receive extra optimization pressure. AV Emotion Fusion supplies the evaluation lesson that combining signal pathways is not automatically beneficial; the value of each pathway must be measured under group-disjoint lineage, corruption, missingness, and class-level metrics. Hypercomplex MRI supplies the clinical-systems lesson that parameter or architecture improvements do not establish operational efficiency or safe clinical transfer. PAC Confidence supplies the decision layer: predictions should be paired with finite-sample support, a shift boundary, and an abstain/fallback state.

Together, the four artifacts motivate an evidence-gated clinical research stack: patient-level split integrity before training; multi-scale and channel-aware representation learning; per-pathway and per-lead intervention tests; calibration intervals and distribution checks; resource/latency measurement; and human review rather than automatic diagnosis. This is a reviewer synthesis, not a jointly tested system.

### Potential Implementations

1. **Calibration-gated ECG research triage:** Run MSAIC-style predictions only inside a versioned patient/site envelope, attach class- and slice-aware confidence intervals, and route unsupported or shifted cases to human review.
2. **Multimodal cardiac evidence gate:** Compare ECG-only, imaging-only, metadata-only, and fused research models on the same patient-disjoint folds; accept fusion only when it improves prespecified sensitivity, calibration, and failure slices without leakage.
3. **Compact multi-scale audit harness:** Measure whether compressed or factorized multi-scale ECG encoders preserve AUPRC, calibration, lead-reliance stability, peak memory, latency tails, and abstention utility on target hardware.

### Deeper Relationship Observations

1. Focal supervised contrastive learning and PAC intervals solve different scarcity problems: the former reallocates training emphasis among hard pairs, while the latter exposes whether finite calibration evidence is sufficient for a downstream decision.
2. Channel attention and lead permutation importance operate at different semantic levels. Attention weights tune latent feature channels; perturbation importance tests input-lead reliance. Agreement is informative, but neither alone proves causal clinical relevance.
3. The largest MSAIC-Net gains appear in the smaller UVA setting, which is also where split variance, augmentation descendants, and calibration scarcity are most dangerous; the regime with the most apparent benefit needs the strongest evidence controls.

### Conceptual Similarities

1. MSAIC-Net, AV Emotion Fusion, and Hypercomplex MRI all encode structured relationships among channels or modalities rather than treating inputs as interchangeable flat features.
2. All four artifacts treat aggregate accuracy as incomplete: imbalance-sensitive metrics, per-condition evidence, calibration support, and failure boundaries are necessary for decision usefulness.
3. Each artifact separates a promising model-level mechanism from deployment validity; data lineage, shift, resource behavior, and fallback remain independent gates.

### MVP Implementations with Code Mock-Ups

1. **Hard-pair focal contrastive audit:** Verify that difficult positive pairs receive greater relative weight without processing patient identifiers.

```python
def focal_positive_weights(pair_probabilities, gamma=2.0):
    """Illustrative research audit; probabilities are synthetic."""
    weights = [(1.0 - p) ** gamma for p in pair_probabilities]
    total = sum(weights) or 1.0
    return [w / total for w in weights]

assert focal_positive_weights([0.2, 0.9])[0] > focal_positive_weights([0.2, 0.9])[1]
```

2. **Interval-and-shift evidence gate:** Release a model suggestion only when support, interval, shift, and fallback conditions all pass.

```python
def evidence_gate(lower_bound, threshold, support, shifted, fallback_ready):
    if shifted or support < 30 or not fallback_ready:
        return "review"
    return "supported" if lower_bound >= threshold else "review"

assert evidence_gate(0.92, 0.90, 80, False, True) == "supported"
assert evidence_gate(0.92, 0.90, 80, True, True) == "review"
```

3. **Lead-perturbation protocol checker:** Make the perturbation operator explicit so Gaussian replacement and cross-sample shuffling cannot be silently conflated.

```python
def perturb_lead(record, lead, mode, replacement):
    if mode not in {"gaussian", "cross_sample_shuffle"}:
        raise ValueError("pre-register one supported perturbation mode")
    changed = {name: list(values) for name, values in record.items()}
    changed[lead] = list(replacement)
    return changed, {"lead": lead, "mode": mode}

toy = {"I": [0.0, 0.1], "V2": [0.2, 0.3]}
_, audit = perturb_lead(toy, "V2", "gaussian", [0.0, 0.0])
assert audit["mode"] == "gaussian"
```

### Developer Challenges

1. Build a patient-lineage validator that proves segments, repeat ECGs, and calibration examples cannot cross training, validation, test, or external-site boundaries.
2. Implement both published lead-perturbation interpretations, quantify their ranking disagreement across seeds and cohorts, and refuse to label either as causal localization.
3. Produce a quality-calibration-resource Pareto report with AUPRC, sensitivity, interval width, abstention, shift alarms, p95 latency, peak memory, and human-review load.

### Author Challenges

1. Release the complete training configuration, code, split manifest, patient counts, seeds, checkpoints, and per-patient evaluation outputs needed to reproduce every table without disclosing protected health information.
2. Resolve the Gaussian-noise versus cross-sample-shuffle inconsistency and report confidence intervals, seed stability, correlated-lead controls, and clinically reviewed interpretation for lead importance.
3. Test external sites and prospective workflows with calibration, subgroup and prevalence shifts, decision-curve utility, human fallback, and prespecified non-inferiority or superiority criteria.

## Validation Notes

- Random selection was an actual uniform zero-based `Get-Random` draw over 75,776 unique PDF parent units; selected index 65,580; zero exclusions and zero reselections.
- Deduplication covered the selected arXiv ID, DOI, title, and slugs across Black Lake, Black-Lake-Data, and automation memory. No same-paper or 24-hour marker was found; cutoff date 2026-07-14.
- The local source state changed from partial to complete. The existing PDF passed minimum-size, `%PDF-`, and trailing `%%EOF` checks. Official full-paper HTML passed minimum-size, body-character, document-marker, heading, and structure-term checks.
- The metadata page was treated as metadata only; it never satisfied the full-paper gate.
- The manuscript source package was archive-list verified locally. Source documents and extracted material were not copied into `.logs`, `.reports`, `.lake-data`, Git staging, or Slack.
- Paper claims, reviewer interpretations, and cross-DEP synthesis are explicitly separated. No experiment, clinical claim, or code path was independently reproduced.
- Required Report-Mark counts are exact: three related DEP entries, three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP code mock-ups, three developer challenges, and three author challenges.
- Public-output sanitization requires zero local absolute paths, usernames, machine names, local timezone labels, or precise local execution timestamps before submission.

## Attribution Block

- Source URL: https://arxiv.org/abs/2606.06718
  - Applies to: paper identity, authors, date, categories, DOI, abstract, and version metadata.
  - Notes: Official arXiv metadata record.
- Source URL: https://arxiv.org/html/2606.06718
  - Applies to: method, datasets, results, limitations, tables, equations, and lead-importance review.
  - Notes: Official full-paper HTML; verified as a complete paper, not an abstract page.
- Source URL: https://arxiv.org/pdf/2606.06718
  - Applies to: complete-paper cross-check and source-first review.
  - Notes: Public locator for the verified local PDF; the file is withheld and not deposited.
- Source URL: https://arxiv.org/e-print/2606.06718
  - Applies to: public source-package provenance and formula/source cross-check.
  - Notes: The local package is withheld and not deposited.
- Source URL: https://doi.org/10.48550/arXiv.2606.06718
  - Applies to: persistent paper identity.
  - Notes: arXiv-issued DOI.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-Hypercomplex%20MRI/hypercomplex_mri_manuscript.md
  - Applies to: related DEP 1 and clinical-efficiency/safety synthesis.
  - Notes: Existing processed Black Lake artifact; primary basis https://arxiv.org/abs/2503.05063.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md
  - Applies to: related DEP 2 and signal-fusion/split-lineage synthesis.
  - Notes: Existing processed Black Lake artifact; primary basis https://arxiv.org/abs/2006.08129.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md
  - Applies to: related DEP 3 and calibration/abstention synthesis.
  - Notes: Existing processed Black Lake artifact; primary basis https://arxiv.org/abs/2011.00716.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: Black Lake filing, naming, attribution, source-withholding, stability, and commit rules.
  - Notes: Live default-branch repository authority read before writing.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related-repository layout and deduplication context.
  - Notes: Live default-branch repository authority read before related-context use.
- Source file: verified local arXiv archive unit, path withheld
  - Applies to: PDF/full-HTML integrity, metadata, source-package listing, and source-first review.
  - Notes: Source files remain local only; none are deposited, staged, uploaded, or attached.
