---
title: "AV Emotion Fusion - DEP-E"
generated_at: "2026-07-13"
artifact_type: "DEP research artifact"
primary_subject: "A source-first review of audio-video emotion classification with CNN, recurrent, contrastive, and 3D-convolutional pathways."
source_status: "URLs only; private local PDF inspected but not deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-13"
temporal_cutoff: "2026-07-13"
primary_url: "https://arxiv.org/abs/2006.08129"
stable_identifier: "arXiv:2006.08129v1"
confidence_summary: "High for source transcription, medium for mechanism interpretation, and low for generalization or independent reproducibility."
safety_scope: "Consent-based research and evaluation; no consequential emotion inference"
distribution_notes: "No source files are redistributed; the paper repository states that IEMOCAP must be requested from USC and cannot be shared by the authors."
---

# AV Emotion Fusion - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Reference | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Emotion Recognition in Audio and Video Using Deep Neural Networks | Primary paper record and full text | arXiv abstract and HTML | arXiv:2006.08129v1; submitted 2020-06-15 | https://arxiv.org/abs/2006.08129; https://arxiv.org/html/2006.08129 | Public research record; arXiv distribution terms apply | 2026-07-13 | Inspected |
| S2 | Emotion Recognition in Audio and Video Using Deep Neural Networks | Primary paper PDF | PDF | arXiv:2006.08129v1 | https://arxiv.org/pdf/2006.08129 | Public PDF locator; no PDF redistributed in this DEP | 2026-07-13 | Complete nine-page text privately extracted and inspected |
| S3 | CS231N-Project | Paper-declared implementation | GitHub repository | `julieeF/CS231N-Project`, default branch `master` | https://github.com/julieeF/CS231N-Project | MIT code license visible; IEMOCAP data excluded and separately governed | 2026-07-13 | README and repository inventory inspected; code not run |
| S4 | VLM Probing - DEP-E | Related processed artifact | Markdown | DEP-E-20260712-VLM Probing | `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Repository artifact; underlying primary basis arXiv:2005.07310 | 2026-07-13 | Inspected |
| S5 | HSD FTI-FDet - DEP-E | Related processed artifact | Markdown | DEP-E-20260712-HSD FTI-FDet | `.lake-data/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Repository artifact; underlying primary basis arXiv:2307.00701 | 2026-07-13 | Inspected |
| S6 | PAC Confidence - DEP-E | Related processed artifact | Markdown | DEP-E-20260713-PAC Confidence | `.lake-data/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Repository artifact; underlying primary basis arXiv:2011.00716v5 | 2026-07-13 | Inspected |
| S7 | Black Lake README | Target repository authority | Markdown | Live `main` branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Governs DEP class, naming, inventory, attribution, stability, and commit rules | 2026-07-13 | Fetched and read before writing |
| S8 | Black-Lake-Data README and code search | Related-repository authority and dedup evidence | Markdown / repository search | Live `main` branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Used only for layout authority and duplicate validation | 2026-07-13 | README inspected; ID/title/topic searches returned zero matches |
| S9 | Private archive paper unit and extraction summary | Selection and processing evidence | README, PDF, public-safe JSON summary | arXiv:2006.08129 | Location withheld; public equivalents are S1-S2 | Private evidence; no redistribution and no local path published | 2026-07-13 | Inspected; `pypdf` extraction succeeded |

Paper metadata:

- `Full title`: Emotion Recognition in Audio and Video Using Deep Neural Networks.
- `Authors`: Mandeep Singh and Yuan Fang.
- `Affiliations shown in paper`: SCPD, Stanford University; ICME, Stanford University.
- `Source platform and date`: arXiv v1, submitted 2020-06-15.
- `Venue status`: Not available from inspected primary sources beyond the arXiv record and the paper's CS231N project acknowledgements. This artifact does not imply peer review.
- `Primary dataset`: IEMOCAP audiovisual conversations. The paper describes 12 hours from 10 actors, five women and five men.
- `Task labels used`: happiness, sadness, anger, and neutral for four-class experiments; sadness, anger, and neutral for three-class experiments.
- `Code and data`: The paper-declared repository contains Jupyter notebooks and Python preprocessing scripts. Its README states that IEMOCAP must be requested from USC and cannot be shared by the authors. No dataset, checkpoint, or experiment was collected or executed for this DEP.
- `Private source note`: A private archive PDF and metadata README were inspected, but their locations are withheld and no source file is deposited.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1-S2 | Primary paper | Title, authors, date, abstract, introduction, dataset, method, experiments, Table 3, result analysis, conclusion | Identity, research question, architecture, preprocessing, metrics, results, and paper-disclosed limitations | High for source reporting | No independent reproduction or peer-review status verified |
| E2 | S2, Table 2 | Primary empirical evidence | Source class counts: happy 786, sad 1,752, anger 1,458, neutral 2,118 | Class imbalance and oversampling/reduction rationale | High for transcription | Exact train/validation lineage remains ambiguous |
| E3 | S1-S2, Table 3 | Primary empirical evidence | Four-class and three-class validation accuracies across CNN, CNN+LSTM, CNN+RNN, and CNN+RNN+3DCNN | Central architecture comparison and narrow fusion-gain claim | High for transcription | One reported validation setup; no seeds, intervals, or statistical tests |
| E4 | S1-S2, Sections 3.2 and 5.1-5.5 | Primary method and negative evidence | Segmentation, noise cleanup, augmentation, face cropping, hyperparameters, contrastive epochs, memory limits, confusion-matrix discussion | Preprocessing findings, failure analysis, and implementation boundary | High for reporting; medium for causal interpretation | Many explanations are author hypotheses rather than controlled ablations |
| E5 | S3 | Official implementation locator | Repository inventory, README, MIT license indicator, IEMOCAP access statement | Code availability and data-governance boundary | High | Code not executed; environment, split manifests, and checkpoints not verified |
| E6 | S4 | Related processed DEP | Fusion, modality importance, head/layer specialization, probe leakage, and causal-audit limits | Representation-audit synthesis | Medium | Different model family and datasets; analogy does not validate this paper |
| E7 | S5 | Related processed DEP | Heterogeneous pathways, task-specific feature preservation, compact inference, field-condition failure analysis | Architecture and deployment synthesis | Medium | Different task, domain, and labels |
| E8 | S6 | Related processed DEP | Finite-sample confidence intervals, thresholding, fallback, and distribution-match assumption | Calibration and abstention synthesis | Medium | Method not applied to this paper's data or logits |
| E9 | S7-S9 | Repository and processing evidence | Live submission rules, random selection record, extraction status, and cross-repository duplicate search | Artifact compliance and eligibility | High | Search quality depends on current repository contents and normalized query terms |

## Executive Summary

Singh and Fang study emotion classification from audio spectrograms and corresponding video frames. Their audio models compare CNN, CNN+LSTM, and CNN+RNN architectures. Their multimodal model combines a CNN+RNN audio pathway with a 3D-CNN video pathway, optionally preceded by contrastive training that pulls matching audio-video representations together and separates mismatched pairs. All reported classifiers use IEMOCAP and overall validation accuracy as the primary metric.

The central result is more conditional than the abstract's headline. For four emotions, the best audio-only CNN+RNN reaches 54.00%, while CNN+RNN+3DCNN reaches 51.94%. After removing happiness, audio-only reaches 70.25% and audio-video reaches 71.75%, a 1.50 percentage-point gain. The visual path therefore helps slightly in the reported three-class setting and hurts in the reported four-class setting. The authors connect this to scarce unique happiness examples, repeated oversampling, side-view faces, actor movement, and coarse static crops. They also report that spectrogram rotation/cropping and noise removal did not improve accuracy.

The evidence is useful as an engineering case study but insufficient for broad claims. The paper does not report speaker-disjoint repeated folds, confidence intervals, statistical tests, calibration, subgroup evaluation, or missing/conflicting-modality experiments. Its descriptions of class balancing and validation allocation do not fully determine a reproducible split. The public repository improves inspectability, but IEMOCAP is not distributed there, and the experiments were not rerun for this review.

The three related Black Lake entries convert those gaps into a stronger implementation agenda. VLM Probing supplies tests for modality fusion, dominance, and representation leakage. HSD FTI-FDet supplies heterogeneous-pathway and task-specific compression patterns under field constraints. PAC Confidence supplies finite-sample confidence intervals and abstention under an explicit distribution-match boundary. Reviewer synthesis: multimodal fusion should be treated as a claim to test per class and condition, followed by calibration and fallback, not as an automatic improvement. This interpretation is suitable for consent-based research and evaluation, not consequential emotion inference.

## Detailed Summary

### Problem Context

Emotion recognition from speech and facial behavior is difficult because the label is subjective, the signal is multimodal, and individual expression varies. The paper asks two practical questions: which deep neural architecture works best on spectrograms, and whether corresponding video frames add useful emotion evidence. It narrows IEMOCAP's wider label set to happiness, anger, sadness, and neutral so that its audio results can be compared with prior spectrogram work.

The problem is not simply image classification. Spectrograms encode time, frequency, and power; video clips encode facial pose and movement. These streams differ in sampling, noise, quality, and temporal support. A fusion system must align them and learn whether one stream is informative, redundant, missing, or contradictory for a given example.

### Data and Preprocessing

The paper describes IEMOCAP as 12 hours of audiovisual conversations from five female and five male actors. The reported source counts for the chosen labels are 786 happiness, 1,752 sadness, 1,458 anger, and 2,118 neutral examples. Happiness and anger are repeated to reach 1,600 examples, while sadness and neutral are reduced to 1,600. The paper separately says that 400 images per emotion are used for validation and later describes an 80/20 train/validation split. Those statements do not fully specify whether the 6,400 balanced images are all training inputs, the complete pool before validation, or a count after repetition. This ambiguity matters because duplicated descendants must not cross evaluation boundaries.

Audio files are described as recorded at 22 kHz, while spectrogram generation uses a 44 kHz sampling setting. Four data variants combine original-duration or three-second segments with noise cleanup on or off. Short three-second utterances are padded, and the denoising path uses a bandpass approach. The best reported results use original-duration inputs without noise cleanup. The authors suggest that denoising may suppress signal structure and that naturally present noise may regularize the model.

Spectrogram images use a consistent power scale and are cropped to remove regions above the observed useful frequency range. Rotation and top cropping expand the training images from 6,400 to 19,200 in the augmented condition, but these transforms do not improve validation accuracy. The paper reasonably avoids horizontal flips because reversing the time axis has no valid speech interpretation. Reviewer interpretation: rotations are also semantically risky because they couple changes in time and frequency rather than simulating a clean acoustic perturbation.

For video, the authors extract 20 frames per three-second segment, crop to the active speaker, and crop again around the face/head, producing 60-by-100 frames. The source videos often show actors from the side, and the actors move within the frame. The paper identifies this as a visual-evidence limitation and proposes automatic face/head detection for future work.

### Audio Models

The CNN contains three two-dimensional convolutional/max-pooling stages followed by two fully connected layers. CNN+LSTM and CNN+RNN add a recurrent layer after convolutional feature extraction. Cross-entropy trains all audio classifiers. The recurrent path is intended to capture temporal structure that a fixed convolutional stack may not represent.

The four-class table reports 52.23% for CNN, 39.77% for CNN+LSTM, and 54.00% for CNN+RNN without augmentation. Augmented CNN and CNN+LSTM are slightly worse at 51.90% and 39.65%. These results show that added architectural complexity is not sufficient: the LSTM path underperforms substantially under the reported tuning, while the simpler RNN path is best.

### Audio-Video Model and Contrastive Training

The multimodal architecture removes the audio classifier's final output layer and uses its higher-level representation. A separate video network contains four 3D-convolutional layers, three 3D max-pooling layers, and two fully connected layers. Audio and video representations are concatenated, and a final output layer predicts emotion.

The contrastive stage defines three pair types: matching audio/video from the same clip; hard negatives from different clips with different emotions; and super-hard negatives from different clips with the same emotion. The contrastive objective encourages matching representations to be close and mismatched representations to be separated by a margin. Supervised cross-entropy fine-tuning then performs classification. The paper also trains the fused network directly without pretraining. Five pretraining epochs yield classification accuracy 0.5 points above ten epochs in the reported comparison, which the authors attribute to overfitting.

### Training and Hyperparameters

The selected optimizer is Adam with learning rate `1e-4` and weight decay `0.01`; the paper says the weight decay improves accuracy by one point. Dropout probabilities are reported as 0.2 for the last fully connected layer and 0.1 for the RNN layer. A batch size of 64 is used, and the paper describes 80%/20% training and validation allocation. Image normalization with common RGB means and standard deviations improves accuracy by 0.37 points.

Doubling or quadrupling audio-layer dimensions reportedly improves accuracy by one to two points but increases memory use. The authors could not extend this experiment to the video path under a 12 GB memory limit. The result is an engineering observation, not evidence that unbounded model scale would solve the task.

### Results

| Architecture | Accuracy | Augmentation | Labels |
|---|---:|---|---|
| CNN | 52.23% | No | Happy, sad, angry, neutral |
| CNN | 51.90% | Yes | Happy, sad, angry, neutral |
| CNN+LSTM | 39.77% | No | Happy, sad, angry, neutral |
| CNN+LSTM | 39.65% | Yes | Happy, sad, angry, neutral |
| CNN+RNN | 54.00% | No | Happy, sad, angry, neutral |
| CNN+RNN | 70.25% | No | Sad, angry, neutral |
| CNN+RNN+3DCNN | 51.94% | No | Happy, sad, angry, neutral |
| CNN+RNN+3DCNN | 71.75% | No | Sad, angry, neutral |

For four classes, audio-video fusion is 2.06 points below audio-only CNN+RNN. For three classes, fusion is 1.50 points above audio-only. The paper calls the latter the best result but also says the improvement is not significant relative to CNN+RNN. Happiness is the main weak class in the confusion-matrix discussion. Removing it changes both task difficulty and label coverage, so the three-class result should not be treated as a repaired four-class model.

The paper reports that its three-class overall accuracy is 2.95 points above the comparison in prior work while its class accuracy lags by 5.4 points. Because this artifact did not independently inspect or reproduce that baseline, the comparison remains an author-reported contextual claim rather than a validated ranking.

### Negative Evidence and Boundary Conditions

Several negative results are particularly useful:

- Noise cleanup performs worse than retaining the original signal in the selected setup.
- Rotation/cropping spectrogram augmentation does not improve accuracy.
- CNN+LSTM is much weaker than CNN+RNN under the reported tuning.
- Four-class audio-video fusion underperforms audio alone.
- More contrastive pretraining is not better in the five-versus-ten-epoch comparison.
- Increasing dimensions has a memory cost and was not tested fully in the video pathway.

The paper does not show that these findings generalize across speakers, seeds, datasets, or acquisition conditions. They identify hypotheses and failure modes that a follow-up should test directly.

### Conclusion and Practical Boundary

The authors conclude that audio and video can complement each other and propose better noise handling, multi-speaker tests, automatic face cropping, acoustic augmentation, larger models, latency measurement, CNN+LSTM tuning, transfer learning, and broader emotion coverage. A careful reading supports a narrower conclusion: the explored multimodal design produces a small three-class validation gain but does not solve the four-class problem. The result is best used to design a stronger evaluation pipeline, not to justify real-world emotion inference.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The work compares CNN, CNN+LSTM, CNN+RNN, and CNN+RNN+3DCNN models on IEMOCAP emotion labels. | Author method claim | E1, E3 | Directly supported by the method and result table. | High |
| C2 | CNN+RNN is the best reported four-class model at 54.00%. | Author empirical claim | E3 | Table 3 supports the value; no repeated-run uncertainty is reported. | High for transcription; low for independent validity |
| C3 | CNN+RNN+3DCNN is the best reported three-class model at 71.75%. | Author empirical claim | E3 | Table 3 supports the value; the gain over audio-only is only 1.50 points and untested statistically. | High for transcription; low-medium for comparative interpretation |
| C4 | Video improves emotion prediction. | Author implication | E3-E4 | Partially supported only in the three-class setup; contradicted by the four-class comparison. | Low-medium |
| C5 | Happiness performance is limited by scarce data and weak facial evidence. | Author explanation | E2-E4 | Plausible and consistent with counts/confusion discussion, but not isolated causally. | Medium-low |
| C6 | Noise cleanup and the chosen image augmentation do not help in the reported setup. | Author empirical claim | E4 | Supported by reported comparisons and discussion; exact runs are not reproduced. | Medium-high |
| C7 | The public repository makes the experiments independently reproducible. | Possible inference | E5 | Not established: code is visible, but data access, environment pins, split lineage, checkpoints, and reruns are missing. | Low |
| C8 | Probe-guided fusion, task-specific pathway design, and interval-backed abstention form a stronger implementation pattern. | Reviewer synthesis | E6-E8 | Conceptually aligned across the three related DEPs; no joint experiment exists. | Medium |
| C9 | The paper was eligible for this automation run and had no prior same-paper marker. | Process claim | E9 | Target and related repositories, staging index, memory, ID, title, and topic were checked. | High |

## Methodology

- `Research objective`: Preserve a source-grounded review of arXiv:2006.08129, distinguish its reported findings from reviewer inference, and synthesize it with exactly three related Black Lake DEPs into bounded implementation directions.
- `Sources inspected`: Private archive PDF and README; public arXiv abstract, HTML full text, and PDF locator; the paper-declared GitHub repository; the live Black Lake README; the live Black-Lake-Data README and repository search; VLM Probing, HSD FTI-FDet, and PAC Confidence manuscripts.
- `Discovery strategy`: Enumerate archive PDFs with `rg --files -g "*.pdf"`; treat unique parent directories as paper units; draw one uniform random zero-based index with `Get-Random`; inspect paper metadata and full text; verify public primary sources; search target and related repositories for duplicates; search repository manuscripts for conceptual overlap.
- `Inclusion criteria`: Primary paper sections supporting identity, method, data, results, limitations, and code availability; repository evidence directly linked by the paper; related DEP entries with concrete overlap in multimodal representation auditing, heterogeneous/compact pathways, or confidence-based decision gates.
- `Exclusion criteria`: Secondary summaries as evidence for technical claims; unverified performance claims; local paths; exact local run details; non-redistributable source files; related entries with only keyword-level overlap.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, product research, and replication analysis.
- `Evidence handling`: Major claims map to evidence IDs. Paper metrics remain author-reported unless independently verified. Reviewer interpretations and implementation proposals are labeled. Negative evidence and ambiguity are preserved.
- `Uncertainty handling`: Missing repetitions, unclear split lineage, unavailable data, unexecuted code, and distribution-transfer gaps are stated rather than inferred away.
- `Extraction process`: The local PDF was extracted with `pypdf` after a source-processing preflight found no `pdftotext` or local HTML/source package. The complete nine-page text and public arXiv HTML table were inspected. No OCR or source-package reconstruction was needed.
- `Version control`: The reviewed paper is pinned to arXiv:2006.08129v1. Related artifacts are pinned by repository-relative DEP paths. The target repository README was fetched from live `origin/main` before writing.
- `Claim selection`: Priority went to the main architecture comparison, exact Table 3 values, class counts, preprocessing findings, paper-disclosed failures, reproducibility boundaries, and decision implications.
- `Cross-checking`: Table 3, paper metadata, result discussion, and code-repository identity were cross-checked between private extraction, public arXiv full text, and GitHub. Experiments were not rerun.
- `Safety handling`: Emotion inference is treated as sensitive. Implementations are limited to consent-based research, local/private processing, uncertainty display, abstention, and explicit non-use for consequential decisions.
- `Reviewer stance`: Mixed paper report, critique, DEP-ready preservation, replication planning, and bounded product translation.

Random-selection and validation pass:

- PDF candidates: 75,761.
- Unique parent-directory paper units: 75,761.
- Selection method: uniform random index over the unique units.
- Zero-based selected index: 19,382.
- Selected identifier: arXiv:2006.08129v1.
- Dedup locations: Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data.
- Dedup keys: arXiv ID, exact normalized title, and normalized topic/slug terms.
- Exclusions: 0.
- Reselections: 0.
- Same-paper 24-hour marker: none; cutoff date 2026-07-12.

## Scope, Constraints, and Assumptions

- `Scope`: Review the selected paper's data processing, audio and audio-video architectures, reported validation evidence, limitations, code/data boundary, and synthesis with three existing Black Lake DEPs.
- `Temporal boundary`: Sources were accessed through 2026-07-13; the paper version is arXiv v1 dated 2020-06-15.
- `Evidence limits`: Experiments, notebooks, dataset, checkpoints, and figures were not executed or reconstructed. No repeated seeds, uncertainty intervals, or independent dataset audit were available. The precise balanced split lineage is ambiguous.
- `Assumptions`: Table values and textual descriptions are transcribed faithfully. Repository-visible files correspond to the paper-declared project. The selected paper unit's PDF represents arXiv v1.
- `Constraints`: Local path and execution details are withheld; source redistribution is avoided; IEMOCAP access is separately governed; compute was not allocated for reproduction; privacy and consent limit product translation.
- `Out of scope`: Diagnosing an individual's emotion, validating use in healthcare or employment, surveillance, deception detection, clinical inference, legal assessment, production deployment, or claims about universal emotional expression.
- `Intended use`: Research review, replication planning, multimodal-evaluation design, DEP deposition, and bounded prototype ideation.
- `Audience`: Researchers and engineers evaluating multimodal classifiers, evidence gates, compact pathways, and calibrated abstention.
- `Depth target`: Full manuscript report with source provenance and implementation implications.
- `Reproducibility boundary`: Code inventory is inspectable, but independent reproduction requires authorized IEMOCAP access, deterministic split manifests, environment reconstruction, and repeated runs.
- `Operational boundary`: The artifact may discuss evaluation and consent-based prototypes, but it does not authorize consequential emotion inference.
- `Data sensitivity`: The reviewed research uses human audiovisual recordings and inferred affect labels; any implementation must treat raw media and labels as sensitive personal data.

## Observations

- `Observed pattern`: The fusion pathway is not uniformly beneficial. It loses 2.06 points on four classes and gains 1.50 points on three classes.
- `Observed pattern`: Increasing nominal sample balance by repeating happiness examples does not supply new speakers, poses, sentences, or recording conditions.
- `Technical implication`: Modality value should be measured per class, speaker, quality slice, and missing/conflicting-modality condition before fusion is released.
- `Technical implication`: Speaker and augmentation lineage should be group-split before balancing to avoid correlated descendants crossing evaluation boundaries.
- `Contradiction or tension`: The abstract foregrounds 54.0% and 71.75% for the multimodal direction, while Table 3 assigns the 54.00% four-class result to audio-only CNN+RNN and 51.94% to the fused model.
- `Contradiction or tension`: The data section's counts and validation description do not map cleanly to the later 80/20 split statement.
- `Evidence-quality implication`: Overall accuracy cannot show whether a small fusion gain improves the weakest class or merely benefits already strong classes.
- `Cross-source pattern`: VLM Probing, HSD FTI-FDet, and PAC Confidence each make an intermediate evidence object visible—representations, task-specific pathways, or calibration intervals—before a final decision is trusted.
- `Open question`: Would tracked frontal face regions help, or would video remain redundant once speaker-disjoint audio evaluation and stronger acoustic representations are used?
- `Reviewer hypothesis`: A quality-gated mixture of unimodal experts will outperform unconditional concatenation under occlusion, audio corruption, and class imbalance.

## Considerations

### Evaluation and Statistics

Repeated speaker-disjoint folds are necessary because random utterance splits can allow speaker identity and recording context to appear on both sides of evaluation. Report per-class precision, recall, macro-F1, calibration error, interval width, abstention rate, and failure slices. A 1.50-point difference should not be treated as meaningful without uncertainty across seeds and folds.

### Data and Label Governance

Emotion labels are interpretive and culturally situated. IEMOCAP uses acted dyadic conversations and does not represent every population, language, disability, or natural setting. Access permission for a research corpus does not automatically authorize a downstream commercial or consequential use. Split manifests, consent terms, retention, and deletion processes should be reviewed independently.

### Modality Quality and Failure

Video can be missing, side-facing, occluded, delayed, or misaligned; audio can be noisy, clipped, reverberant, or dominated by another speaker. A robust system should expose modality-quality signals and test contradictory cases. It should not silently convert an unavailable stream into zeros unless that masking operation was part of training and evaluation.

### Calibration and Shift

Point softmax scores are not decision guarantees. Calibration needs a held-out set separated by speaker and acquisition context. PAC-style intervals can make finite-sample support visible, but their coverage remains conditional on a matching deployment distribution. Shift detection and abstention are separate controls.

### Privacy, Ethics, and Misuse

Raw voice and face video are biometric-like personal signals. Emotion inference can be invasive, stigmatizing, or falsely authoritative. Do not deploy it for hiring, discipline, policing, insurance, medical triage, classroom surveillance, or credibility assessment. Bounded research tools should use explicit consent, local processing when feasible, minimal retention, uncertainty display, and human control.

### Operations and Maintenance

Version the preprocessing pipeline, model, split manifest, calibration set, label taxonomy, and modality-quality thresholds together. Monitor class support, drift, abstention, latency tails, and fallback health. Revalidation is required after changes to cameras, microphones, compression, sampling rate, face tracking, population, or label policy.

## Strengths

- The paper reports exact architecture comparisons and preserves negative results rather than showing only its preferred configuration.
- It compares audio-only and audio-video pathways under one project, making the marginal value of video inspectable.
- The contrastive pair taxonomy distinguishes matching, different-emotion, and same-emotion mismatches, which is a useful starting point for cross-modal alignment tests.
- Table 3 makes the four-class versus three-class boundary visible and prevents a simple claim that fusion always helps.
- The result analysis connects errors to class scarcity, side-view faces, crop quality, and augmentation semantics.
- The public repository exposes notebooks and preprocessing scripts and clearly states the IEMOCAP redistribution boundary.
- The discussion identifies practical follow-ups including face detection, latency, multi-speaker inputs, transfer learning, and broader emotion coverage.

## Weaknesses

- The empirical setup lacks repeated seeds, confidence intervals, statistical significance tests, and speaker-disjoint cross-validation evidence.
- Exact split lineage is ambiguous across the balance, validation-count, and 80/20 descriptions.
- Repeated oversampling can create count balance without representation diversity and can increase leakage risk if performed before splitting.
- Overall accuracy obscures per-class and subgroup harm; calibration and abstention are absent.
- The four-class fused model is worse than audio-only, which limits the paper's general multimodal conclusion.
- Static video crops and side views are weak visual inputs, and no video-only baseline is reported in Table 3.
- Missing, asynchronous, corrupted, and contradictory modality tests are absent.
- The 22 kHz source versus 44 kHz spectrogram rationale is unclear; resampling does not recover information above the original Nyquist limit.
- The repository does not establish a turnkey reproduction because data, environment pins, split manifests, checkpoints, and expected-run outputs were not verified.
- Ethical, privacy, demographic, cultural, and misuse boundaries are not evaluated.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Speaker-disjoint repeated folds | Evaluation | Prevent identity/context leakage and quantify uncertainty | More credible generalization estimate | More training runs and wider intervals | Grouped cross-validation, repeated seeds, preregistered metrics |
| Immutable sample lineage | Data pipeline | Clarify original, repeated, reduced, augmented, train, calibration, and test examples | Reproducibility and leak prevention | Engineering overhead | Hash-based manifest audit and split invariant tests |
| Track faces rather than static crops | Video preprocessing | Side views and movement weaken visual evidence | Better, more consistent facial region input | Detector bias and tracking errors | Compare static, tracked, missing-face, and oracle crops |
| Add video-only and modality-ablation baselines | Fusion evidence | Quantify unique and redundant evidence | Detect unhelpful or dominant modalities | Additional model runs | Audio-only, video-only, fused, shuffled-pair, and masked-stream evaluation |
| Use acoustically valid augmentation | Audio preprocessing | Rotating spectrograms changes time-frequency semantics | Better robustness without invalid transformations | Augmentation mismatch | Noise/reverb/pitch/time perturbation ablations with held-out conditions |
| Probe representations and run causal ablations | Interpretability | Attention or concatenation alone does not show useful fusion | Localize modality value and leakage | Probe overfitting | Linear controls, random weights, counterfactual masking, intervention tests |
| Calibrate and abstain | Decision layer | Overall accuracy does not express finite-sample trust | Safer handling of sparse or shifted cases | Coverage-utility tradeoff | Held-out intervals, abstention curves, distribution-shift stress tests |
| Publish environment and checkpoints | Reproducibility | Code visibility is not equivalent to executable evidence | Lower replication barrier | Maintenance and licensing work | Clean-room setup, expected hashes, smoke tests, documented failures |
| Add consent and non-use constraints | Governance | Emotion labels and audiovisual data are sensitive | Reduce misuse and false authority | Narrows product scope | Privacy review, data protection impact assessment, user studies |

## Potential Implementations

### 1. Multimodal Fusion Evidence Gate

- `User`: Research team deciding whether to add video to an audio classifier.
- `Goal`: Require measurable, repeatable evidence that fusion improves outcomes without masking class regressions.
- `Core mechanism`: Train aligned audio-only, video-only, and fused models on the same speaker-disjoint folds; compute per-class deltas, calibration, missing-modality performance, and probe results.
- `Required inputs`: Versioned audiovisual samples, consent metadata, speaker groups, immutable split manifests, model outputs, modality-quality scores.
- `Outputs`: Evidence card with fold distributions, per-class deltas, calibration support, probe results, and release decision.
- `Risk controls`: No raw-media export, explicit non-use for consequential decisions, minimum subgroup support, automatic rejection on leakage or missing consent.
- `Evaluation`: Repeated folds, permutation controls, corrupted-stream tests, counterfactual pairing, and blinded review.

### 2. Quality-Gated Compact Fusion Student

- `User`: Engineer building a local research prototype for constrained hardware.
- `Goal`: Preserve useful modality-specific features while avoiding unconditional fusion when one stream is weak.
- `Core mechanism`: Separate audio and tracked-face teachers produce representations and quality signals; a compact student learns task features and a gate chooses audio, video, fusion, or abstention.
- `Required inputs`: Authorized audiovisual data, modality-quality labels or synthetic corruptions, teacher outputs, hardware target profile.
- `Outputs`: Compact model, quality gate, latency/memory profile, and failure-slice report.
- `Risk controls`: Local-only inference, bounded label set, raw-media deletion, missing-stream support, human override, no covert capture.
- `Evaluation`: Accuracy/calibration Pareto curves, latency tails, energy, quality-gate error, unseen-speaker and device shifts.

### 3. Interval-Supported Research Annotation Tool

- `User`: Consent-based HCI or affective-computing researcher reviewing recordings.
- `Goal`: Prioritize clips for manual annotation without presenting machine labels as ground truth.
- `Core mechanism`: Display audio-only, video-only, and fused predictions alongside calibration support, modality disagreement, and an abstain state.
- `Required inputs`: Authorized research clips, model outputs, held-out calibration bins, provenance and retention policy.
- `Outputs`: Review queue, interval-supported suggestion, disagreement flag, and annotator decision.
- `Risk controls`: Suggestions hidden when support is sparse; no automated action; no identity inference; audit trail records model version and human override without retaining unnecessary media.
- `Evaluation`: Annotation time, disagreement resolution, abstention quality, calibration coverage, annotator trust calibration, privacy review.

## Three Ways to Exercise This Research

1. **Reproduce the architecture table:** Objective—test whether the ranking in Table 3 survives speaker-disjoint evaluation. Inputs—authorized IEMOCAP access, paper repository, immutable speaker-group splits, and environment pins. Steps—reconstruct preprocessing, run audio-only and fused models across repeated folds, record class metrics and uncertainty. Output—a reproduction matrix with deviations from reported values. Success criterion—the full pipeline and split lineage are independently auditable. Stop condition—data authorization, split integrity, or environment reconstruction cannot be established.
2. **Run a modality-value stress test:** Objective—measure when video helps, hurts, or is ignored. Inputs—a trained research model and held-out clips with consent. Steps—evaluate audio-only, video-only, fused, shuffled audio-video, masked streams, lighting degradation, occlusion, audio corruption, and temporal offsets. Output—condition-by-class fusion delta and modality-conflict report. Success criterion—the system identifies failure regimes without relying on one aggregate score. Stop condition—perturbations change labels in ways that cannot be validated or sensitive media cannot be handled safely.
3. **Build a calibration-and-abstention study:** Objective—attach finite-sample support to model suggestions. Inputs—speaker-disjoint calibration and test sets, fixed score bins, desired confidence level, and a human-review fallback. Steps—construct simultaneous bin intervals, choose abstention thresholds, test coverage and utility, then repeat under controlled shift. Output—coverage, interval width, abstention, and fallback-load curves. Success criterion—on-distribution coverage matches the stated procedure and shift failures are visible rather than hidden. Stop condition—calibration/test distribution identity or sample independence assumptions are violated.

## Example MVP Product

- `Product name`: Fusion Evidence Card.
- `Target user`: Multimodal ML researcher or model-risk reviewer.
- `Problem`: Teams often add modalities because aggregate validation accuracy appears higher, without proving that fusion is repeatable, class-safe, calibrated, or useful under degraded inputs.
- `Core workflow`: Import only de-identified metrics and immutable sample IDs; verify group splits and augmentation lineage; compare audio-only, video-only, and fused outputs; calculate per-class deltas and calibration support; run missing/conflicting-modality tests; generate a signed research evidence card; require human approval for any next experiment.
- `Data requirements`: Prediction tables, labels, speaker/group identifiers represented by non-reversible study IDs, modality-quality flags, calibration membership, model/version hashes, and consent status. Raw audiovisual media is out of the default MVP path.
- `Architecture`: Local CLI or notebook; schema validator; split-lineage checker; metric engine; interval calculator; shift-test module; static Markdown/JSON report generator. No remote upload is required.
- `Success metrics`: Zero split-lineage violations; reproducible metric hashes; fold-level uncertainty present; per-class fusion deltas reported; calibration-bin support visible; missing/conflicting-modality tests completed; reviewer decision recorded.
- `Risk controls`: Local-only operation, no raw-media logging, minimum support thresholds, explicit `research-only` label, no individual emotion dashboard, no consequential-use export, deletion and retention controls.
- `Limitations`: The MVP audits evidence supplied to it; it cannot prove labels are culturally valid, consent is adequate, a dataset is representative, or deployment is ethical. Statistical intervals remain conditional on their assumptions.
- `MVP boundary`: No model training, biometric identification, workplace monitoring, clinical assessment, or automated action.
- `Deployment model`: Local CLI/notebook producing repository-ready Markdown and JSON.
- `Evaluation plan`: Unit tests for split invariants and metrics; synthetic leakage fixtures; golden report snapshots; repeated-fold smoke test; privacy review; user test with research reviewers.
- `Failure modes`: Incorrect group IDs, hidden augmentation descendants, sparse classes, adaptive threshold leakage, mislabeled modality quality, distribution shift, and misleadingly narrow aggregate summaries.
- `Maintenance plan`: Version schemas and metrics; pin statistical dependencies; record report hashes; revalidate after label, model, preprocessing, device, or population changes.

Minimal illustrative interface:

```python
def build_evidence_card(audio_rows, video_rows, fused_rows, split_manifest):
    assert split_manifest.has_disjoint_groups()
    assert split_manifest.has_no_augmented_descendant_leakage()
    return {
        "audio": evaluate(audio_rows),
        "video": evaluate(video_rows),
        "fused": evaluate(fused_rows),
        "fusion_deltas": compare(fused_rows, audio_rows, by="class"),
        "release_status": "human-review-required",
    }
```

The example is intentionally non-operational: `evaluate` and `compare` require validated project-specific implementations, and no production or individual-level claim follows from the output.

## Related Research and Reading

Exactly three Black Lake DEP entries were selected for synthesis:

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| VLM Probing - DEP-E | Related Black Lake DEP | Supplies probes for modality fusion, dominance, specialized representations, leakage controls, and the gap between recoverable information and causal use | `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`; primary basis https://arxiv.org/abs/2005.07310 |
| HSD FTI-FDet - DEP-E | Related Black Lake DEP | Supplies heterogeneous task pathways, compact feature preservation, in-the-wild failure analysis, and a deployment Pareto perspective | `.lake-data/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`; primary basis https://arxiv.org/abs/2307.00701 |
| PAC Confidence - DEP-E | Related Black Lake DEP | Supplies finite-sample confidence intervals, threshold selection, fallback logic, and an explicit on-distribution coverage boundary | `.lake-data/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`; primary basis https://arxiv.org/abs/2011.00716 |

Primary and near-primary material:

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| Emotion Recognition in Audio and Video Using Deep Neural Networks | Primary paper | Reviewed work and central empirical evidence | https://arxiv.org/abs/2006.08129 |
| CS231N-Project | Paper-declared repository | Notebooks, preprocessing scripts, code license, and IEMOCAP access boundary | https://github.com/julieeF/CS231N-Project |

Synthesis: the reviewed paper supplies a concrete failure of unconditional multimodal optimism; VLM Probing supplies internal evidence tests; HSD FTI-FDet supplies pathway specialization and compactness; PAC Confidence supplies a bounded decision gate. This is reviewer synthesis, not a jointly validated system.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2006.08129 | Title, authors, submission date, abstract, version identity, and source navigation | 2026-07-13 | Primary arXiv record |
| R2 | https://arxiv.org/html/2006.08129 | Full method, dataset, tables, equations, results, limitations, and conclusion | 2026-07-13 | Primary public full text |
| R3 | https://arxiv.org/pdf/2006.08129 | Public counterpart of the privately inspected PDF | 2026-07-13 | No PDF copied into this DEP |
| R4 | https://github.com/julieeF/CS231N-Project | Repository inventory, README, code-license visibility, data access boundary | 2026-07-13 | Code not executed |
| R5 | `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Related multimodal representation and probe synthesis | 2026-07-13 | Existing Black Lake artifact; primary basis https://arxiv.org/abs/2005.07310 |
| R6 | `.lake-data/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Related heterogeneous pathway, compact inference, and field robustness synthesis | 2026-07-13 | Existing Black Lake artifact; primary basis https://arxiv.org/abs/2307.00701 |
| R7 | `.lake-data/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Related interval confidence, threshold, and abstention synthesis | 2026-07-13 | Existing Black Lake artifact; primary basis https://arxiv.org/abs/2011.00716 |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Target repository DEP and submission rules | 2026-07-13 | Live default-branch authority fetched before writing |
| R9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository layout and dedup context | 2026-07-13 | Live default-branch README inspected |
| R10 | Private archive paper unit and public-safe extraction summary; location withheld | Random selection identity, local full-text availability, and extraction status | 2026-07-13 | Private evidence only; public equivalents are R1-R3 |

## Appendix

### A. Random Selection and Eligibility Record

| Field | Value |
|---|---|
| Enumeration command | `rg --files -g "*.pdf"` |
| Paper-unit rule | Unique parent directory for each PDF candidate |
| PDF candidate count | 75,761 |
| Unique paper-unit count | 75,761 |
| Random method | Uniform `Get-Random` zero-based index |
| Selected index | 19,382 |
| Selected identifier | arXiv:2006.08129v1 |
| Duplicate keys | arXiv ID, exact title, normalized topic/slug |
| Target scan | `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory |
| Related-repository scan | Black-Lake-Data README and authenticated repository code search |
| Exclusions | 0 |
| Reselections | 0 |
| 24-hour cutoff | 2026-07-12 |
| Same-paper recent marker | None found |

### B. Result Table Audit

The values below were cross-checked between the privately extracted PDF and public arXiv HTML Table 3:

| Model | Four-class | Three-class |
|---|---:|---:|
| CNN | 52.23% | Not reported |
| CNN with augmentation | 51.90% | Not reported |
| CNN+LSTM | 39.77% | Not reported |
| CNN+LSTM with augmentation | 39.65% | Not reported |
| CNN+RNN | 54.00% | 70.25% |
| CNN+RNN+3DCNN | 51.94% | 71.75% |

Derived differences are reviewer calculations:

- Four-class fusion delta: `51.94 - 54.00 = -2.06` percentage points.
- Three-class fusion delta: `71.75 - 70.25 = +1.50` percentage points.

### C. Replication Checklist

- [ ] Obtain IEMOCAP through an authorized channel and record license/consent constraints.
- [ ] Pin the paper repository commit and reconstruct an isolated environment.
- [ ] Create immutable original-sample, speaker, utterance, clip, and augmentation IDs.
- [ ] Split by speaker before balancing or augmentation.
- [ ] Reconcile the paper's 1,600-per-class, 400-validation-per-class, and 80/20 statements.
- [ ] Reproduce unaugmented and augmented audio baselines.
- [ ] Reproduce audio-only and audio-video three-class/four-class comparisons.
- [ ] Run repeated seeds and grouped folds with per-class metrics and uncertainty.
- [ ] Add video-only, shuffled-pair, masked-stream, temporal-offset, and corruption controls.
- [ ] Fit calibration intervals only on a held-out calibration partition.
- [ ] Audit subgroup support, privacy, consent, retention, and prohibited uses.
- [ ] Report compute, peak memory, latency distribution, and failure cases.

### D. Source Inventory

- No `.source/` directory was created.
- No PDF, dataset, notebook, checkpoint, or repository snapshot is redistributed.
- Public arXiv and GitHub URLs preserve source provenance.
- Private source locations and exact local execution details are withheld.
