# Report-Mark: AV Emotion Fusion

Public-safe run date: 2026-07-13

## Source Metadata

| Field | Value |
|---|---|
| Reviewed work | *Emotion Recognition in Audio and Video Using Deep Neural Networks* |
| Authors | Mandeep Singh; Yuan Fang |
| Stable identifier | arXiv:2006.08129v1 |
| Source platform | arXiv; submitted 2020-06-15 |
| Research object | Audio-only and audio-video emotion classification using CNN, recurrent, and 3D-convolutional pathways |
| Primary data | IEMOCAP audiovisual conversations; the paper describes 12 hours from 10 actors |
| Public sources inspected | arXiv abstract/full text/PDF locator; paper-declared GitHub repository |
| Private source handling | A private archive PDF and local README were inspected. Their locations are withheld and no source file is redistributed. |
| Code/data boundary | The public repository exposes notebooks and preprocessing scripts under an MIT code license. Its README states that IEMOCAP must be requested from USC and cannot be shared by the authors. Code and data were not executed or independently reproduced. |
| Review confidence | High for source transcription; medium for the mechanism interpretation; low for generalization or reproducibility beyond the reported validation setup |

## Concise Research Notes

### Problem

The paper asks whether audio spectrograms and corresponding video frames can improve categorical emotion recognition over audio alone. It focuses on happiness, sadness, anger, and neutral speech from IEMOCAP, a setting where emotion labels are subjective, the class counts are uneven, and facial evidence is often captured from the side rather than frontally.

### Method

The audio path compares a three-layer CNN, CNN+LSTM, and CNN+RNN over spectrogram images. The multimodal path joins the best audio path, CNN+RNN, with a four-layer 3D CNN over 20 video frames per three-second segment. The final audio and video representations are concatenated for classification. A contrastive pretraining stage aligns audio and video from the same clip while separating mismatched clips; positive, hard-negative, and same-emotion/super-hard-negative pairs are described. Supervised cross-entropy training then predicts the emotion class.

The authors also vary utterance segmentation, noise cleanup, rotation/cropping augmentation, optimizer settings, regularization, channel dimensions, and normalization. Their reported best input uses the original utterance duration without noise removal. The paper balances the four classes by repetition or reduction, but its statements about 1,600 examples per class, 400 validation images per class, and a later 80/20 split do not fully specify one reproducible split construction.

### Evidence and Results

The main validation table reports:

| Architecture | Emotions | Accuracy | Interpretation |
|---|---:|---:|---|
| CNN | 4 | 52.23% | Audio-only baseline |
| CNN+LSTM | 4 | 39.77% | Lowest reported non-augmented result |
| CNN+RNN | 4 | 54.00% | Best four-class result |
| CNN+RNN+3DCNN | 4 | 51.94% | Multimodal model underperforms audio-only by 2.06 points |
| CNN+RNN | 3 | 70.25% | Happiness removed |
| CNN+RNN+3DCNN | 3 | 71.75% | Multimodal model improves by 1.50 points |

The reported evidence therefore supports a modest three-class fusion gain, not a general claim that adding video improves emotion recognition. The four-class result moves in the opposite direction. The authors attribute the weakness to limited unique happiness examples, side-view facial evidence, coarse face/head cropping, and movement within the crop. They also report that rotation/cropping augmentation and noise removal did not help, that five epochs of contrastive pretraining performed 0.5 points better than ten, and that larger audio-layer dimensions improved accuracy by 1-2 points but increased memory pressure.

### Limitations

- The paper reports a single validation setup without repeated seeds, confidence intervals, speaker-disjoint cross-validation, or statistical tests.
- The four-class class-balancing and validation description is not precise enough to reconstruct the exact sample lineage from the paper alone.
- Happiness has only 786 source examples before repetition, so repeated samples improve balance counts without adding subject, wording, pose, or recording diversity.
- Static side-view face/head crops can supply weak or misleading visual evidence. Missing-modality and conflicting-modality tests are not reported.
- Overall accuracy hides class-specific risk. The confusion-matrix discussion identifies happiness as weak, but per-class precision, recall, calibration, and uncertainty are not tabulated.
- The source audio is described as 22 kHz while spectrogram generation uses 44 kHz. Reviewer interpretation: resampling cannot restore frequency content absent from the original recording, so the Nyquist rationale needs correction or clearer documentation.
- The repository makes code visible, but IEMOCAP is not redistributed and the experiments were not rerun. Environment pins, deterministic split files, checkpoints, and repeated-run evidence were not verified.
- Emotion inference has privacy, consent, cultural, disability, and misuse risks. The paper does not establish suitability for consequential assessment, surveillance, employment, healthcare, or safety decisions.

### Implementation Relevance

The most reusable implementation pattern is not the reported classifier itself. It is an evidence-oriented multimodal pipeline: preserve separate modality paths, measure the incremental value of fusion per class and condition, inspect intermediate representations, calibrate the final decision, and abstain when evidence is sparse or modalities conflict. That pattern can support consent-based research tools, media indexing, or human-computer interaction prototypes, but it needs demographic and speaker-disjoint evaluation before any real-world claim.

### Reviewer Interpretation

The paper is valuable as an inspectable project record showing several negative findings: denoising can suppress useful structure, naive spectrogram transforms can alter semantics, more complex recurrence can underperform, and multimodal fusion can hurt when one modality is poorly framed. The three-class 1.50-point gain is hypothesis-generating rather than deployment evidence. A stronger follow-up would treat fusion as a gated decision problem and make class diversity, modality quality, calibration support, and abstention visible release criteria.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Status and caveat |
|---|---|---|---|
| E1 | arXiv v1 full text, including Sections 3-6, Tables 1-3, and Figures 5-9 descriptions | Identity, dataset description, architectures, preprocessing, metrics, limitations, and future work | Primary evidence; results not independently reproduced |
| E2 | Table 3 values in the arXiv full-text rendering and extracted PDF | Exact four-class and three-class accuracy comparisons | High transcription confidence; no uncertainty estimates |
| E3 | Paper-declared GitHub repository and README | Code/notebook availability, MIT license visibility, and IEMOCAP access boundary | Repository inspected; notebooks not executed and dataset unavailable in the repository |
| E4 | `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` | Probe design for modality fusion, layer/head specialization, leakage controls, and causal-audit limitations | Processed related artifact; conceptual bridge, not validation of the emotion model |
| E5 | `.lake-data/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md` | Heterogeneous pathways, task-specific spatial information, compact inference, field-condition failures | Processed related artifact; different domain and task |
| E6 | `.lake-data/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md` | Finite-sample confidence intervals, threshold decisions, abstention, and distribution-match boundary | Processed related artifact; method not applied to this paper's outputs |
| E7 | Current Black Lake and Black-Lake-Data READMEs plus repository searches | Naming, attribution, deduplication, and deposition compliance | Process evidence only |

Source claims are labeled as author-reported unless independently visible in repository metadata. Statements about fusion gates, calibration, privacy, and product design are reviewer synthesis or implementation proposals, not claims made by the paper.

## Related DEP Entries

Exactly three related entries were selected from `Delphoa/Black-Lake`:

1. `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
   - Relevance: supplies a disciplined way to test where multimodal fusion occurs, which modality dominates, and whether probe results reflect usable representations or label leakage.
   - Source/reference basis: the inspected DEP evidence ledger, anchored to *Behind the Scene: Revealing the Secrets of Pre-trained Vision-and-Language Models* (arXiv:2005.07310; ECCV 2020).
2. `.lake-data/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`
   - Relevance: shows how heterogeneous pathways, spatial attention, localization-aware learning, and compact deployment can preserve task-specific evidence under field constraints.
   - Source/reference basis: the inspected DEP evidence ledger, anchored to *Efficient Visual Fault Detection for Freight Train Braking System via Heterogeneous Self Distillation in the Wild* (arXiv:2307.00701; *Advanced Engineering Informatics* 57, 102091).
3. `.lake-data/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
   - Relevance: converts point confidence into finite-sample intervals that can support abstention or fallback decisions when the calibration and use distributions match.
   - Source/reference basis: the inspected DEP evidence ledger, anchored to *PAC Confidence Predictions for Deep Neural Network Classifiers* (arXiv:2011.00716v5; ICLR 2021).

## Synthesis Note

### Concept Bridge

The selected paper exposes a multimodal evidence problem: adding a video branch does not reliably improve the classifier, because the visual stream can be low-quality, imbalanced, or redundant. VLM Probing turns that ambiguity into measurable questions about fusion, modality dominance, specialization, and leakage. HSD FTI-FDet contributes a design pattern for keeping heterogeneous pathways task-specific and compact rather than forcing uniform representations. PAC Confidence adds a decision boundary: even a well-designed fusion model should emit an interval-supported decision or abstain, and its guarantee should not be carried across untested distribution shift.

Together, the four artifacts suggest an evidence stack. First, preserve modality-specific encoders and audit what each contributes. Second, distill or compress only after identifying information worth preserving. Third, attach calibration support, shift status, and fallback behavior to the output. The selected paper's negative four-class fusion result becomes useful evidence for this stack: fusion should earn its place per class and condition rather than be assumed beneficial.

### Potential Implementations

1. **Fusion evidence gate:** Train audio-only, video-only, and fused models on identical speaker-disjoint folds; release the fused path only when it improves predeclared per-class metrics and calibration without unacceptable subgroup regressions.
2. **Compact multimodal edge monitor:** Use separate lightweight audio and tracked-face encoders, distill condition-specific features into a compact student, and preserve a modality-quality vector so poor lighting, occlusion, or audio corruption can trigger fallback.
3. **Consent-based affect research assistant:** Present interval-valued predictions and modality contributions to a human researcher, retain no raw media by default, and abstain on sparse calibration bins, distribution-shift alarms, or audio-video disagreement.

### Deeper Relationship Observations

1. Modality fusion and knowledge distillation are both information-selection problems: each succeeds only when the system knows which intermediate evidence must survive combination or compression.
2. The happiness failure links data diversity to uncertainty: repeated examples can balance counts while leaving representation coverage and confidence intervals weak in the regions that matter.
3. Representation probes and calibration answer different questions. Probes ask what the network encodes; calibration asks how much decision trust the observed sample supports. Neither substitutes for the other.

### Conceptual Similarities

1. All four artifacts separate a high-capacity training or analysis path from a constrained decision path.
2. All four rely on explicit intermediate structure—modality tokens, heterogeneous features, correctness bins, or contrastive embeddings—rather than only an end-to-end score.
3. All four reveal boundary conditions where an aggregate metric can mislead: leakage in probes, field shift in detection, distribution mismatch in PAC coverage, and class/modality imbalance in emotion recognition.

### MVP Implementations with Code Mock-Ups

1. **Per-fold fusion release gate**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class FoldResult:
    audio_accuracy: float
    fused_accuracy: float
    worst_class_delta: float

def fusion_is_supported(result: FoldResult, min_gain: float = 0.01) -> bool:
    return (
        result.fused_accuracy - result.audio_accuracy >= min_gain
        and result.worst_class_delta >= 0.0
    )
```

This toy gate makes the comparison explicit. A production version needs repeated speaker-disjoint folds, uncertainty intervals, calibration checks, and subgroup review.

2. **Modality contribution probe**

```python
def modality_deltas(predict, sample):
    full = predict(audio=sample["audio"], video=sample["video"])
    no_audio = predict(audio=None, video=sample["video"])
    no_video = predict(audio=sample["audio"], video=None)
    return {
        "audio_contribution": full - no_audio,
        "video_contribution": full - no_video,
        "conflict": (full.argmax() != no_audio.argmax()
                     and full.argmax() != no_video.argmax()),
    }
```

The mock-up treats missing-modality evaluation as a first-class test. Real use must define neutral masking, avoid interpreting logits as causal explanations, and validate against counterfactual controls.

3. **Interval-backed abstention**

```python
from scipy.stats import beta

def clopper_pearson_lower(successes: int, total: int, alpha: float) -> float:
    if total <= 0 or successes == 0:
        return 0.0
    return float(beta.ppf(alpha, successes, total - successes + 1))

def may_emit(successes: int, total: int, required_accuracy: float) -> bool:
    return clopper_pearson_lower(successes, total, alpha=0.025) >= required_accuracy
```

This illustrates a lower-bound gate for a fixed calibration bin and requires SciPy. A production PAC construction must account for simultaneous bins, distribution matching, adaptive choices, and the cost of fallback.

### Developer Challenges

1. Build speaker-disjoint data lineage that prevents utterances, speakers, and augmented descendants from crossing train, calibration, and test boundaries.
2. Instrument each modality with quality, contribution, latency, and missingness telemetry without logging raw sensitive media.
3. Demonstrate that compression, fusion, calibration, and abstention remain valid together under noise, occlusion, lighting, class imbalance, and unseen speakers.

### Author Challenges

1. Publish deterministic split manifests, environment pins, repeated-seed results, and per-class uncertainty so the reported 1.50-point fusion gain can be tested rather than inferred from one run.
2. Compare static crops with tracked faces and add audio-only, video-only, missing-modality, asynchronous-modality, and conflicting-modality ablations.
3. Reframe the task around calibrated, consent-aware assistance, documenting subgroup performance, label ambiguity, privacy limits, and explicit non-use in consequential decisions.

## Validation Notes

- Random selection used `rg` over PDFs, unique parent-directory paper units, and a uniform zero-based index. Candidate count: 75,761; selected index: 19,382.
- Deduplication searched `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and Black-Lake-Data for arXiv ID, exact title, and normalized topic. Exclusions: 0; reselections: 0; 24-hour cutoff date: 2026-07-12.
- Private extraction status: PDF text succeeded with `pypdf`; no local HTML or source package was available. Public arXiv HTML and the paper-declared repository were inspected independently.
- Source files were not collected into the public deposit because the public URLs are stable, the private archive location must remain withheld, and the IEMOCAP dataset is not redistributable through the paper repository.
- Required exact counts are present in this Report-Mark: three related DEP entries, three potential implementations, three deeper observations, three conceptual similarities, three code mock-ups, three developer challenges, and three author challenges.
- Pre-commit validation confirmed manuscript schema, title length and equality, exact-three counts, syntax parsing for all four Python blocks, README inventory, five-file staged scope, URL attribution coverage, and zero public-safety leaks. SciPy is declared but was not installed, so the Clopper-Pearson mock-up's external import was not resolved.

## Attribution Block

- Source URL: https://arxiv.org/abs/2006.08129
  - Applies to: source identity, authors, date, abstract, and public paper navigation.
  - Notes: Primary arXiv record for the selected paper.
- Source URL: https://arxiv.org/html/2006.08129
  - Applies to: method, dataset, tables, metrics, figures, limitations, and conclusions.
  - Notes: Primary public full-text evidence.
- Source URL: https://arxiv.org/pdf/2006.08129
  - Applies to: the complete paper corresponding to the privately inspected PDF.
  - Notes: Public PDF locator; no source PDF is redistributed in this report.
- Source URL: https://github.com/julieeF/CS231N-Project
  - Applies to: code/notebook availability, project README, MIT code license visibility, and IEMOCAP access boundary.
  - Notes: Paper-declared repository; code was inspected but not executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: target repository naming, contents, attribution, stability, and commit rules.
  - Notes: Live default-branch repository authority fetched before writing.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: related-repository layout and cross-repository dedup scope.
  - Notes: Live default-branch README inspected before the related-repository search.
- Source URL: https://arxiv.org/abs/2005.07310
  - Applies to: primary research basis recorded by the VLM Probing DEP.
  - Notes: Used through the inspected processed DEP entry.
- Source URL: https://arxiv.org/abs/2307.00701
  - Applies to: primary research basis recorded by the HSD FTI-FDet DEP.
  - Notes: Used through the inspected processed DEP entry.
- Source URL: https://arxiv.org/abs/2011.00716
  - Applies to: primary research basis recorded by the PAC Confidence DEP.
  - Notes: Used through the inspected processed DEP entry.
- Repository source: `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
  - Applies to: representation-probe and multimodal-fusion synthesis.
  - Notes: Existing Black Lake manuscript inspected for evidence and limitations.
- Repository source: `.lake-data/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`
  - Applies to: heterogeneous-pathway, compact-inference, and field-robustness synthesis.
  - Notes: Existing Black Lake manuscript inspected for evidence and limitations.
- Repository source: `.lake-data/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
  - Applies to: confidence-interval, abstention, and distribution-boundary synthesis.
  - Notes: Existing Black Lake manuscript inspected for evidence and limitations.
