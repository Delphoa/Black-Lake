# Report-Mark: E-CMANet Audio-Visual Parsing

Run date: 2026-08-20

## Source Metadata

| Field | Value |
|---|---|
| Paper | Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing |
| Identifier | arXiv:2509.14097v1 |
| Authors | Yaru Chen; Ruohao Guo; Liting Gao; Yang Xiang; Qingyu Luo; Zhenbo Li; Wenwu Wang |
| Public source | [arXiv metadata](https://arxiv.org/abs/2509.14097), [full HTML](https://arxiv.org/html/2509.14097), [PDF](https://arxiv.org/pdf/2509.14097) |
| Date | arXiv record dated 2025-09-17 |
| Source state | Initially partial; repaired to verified PDF/full-paper HTML/metadata locally. Source package unavailable. |
| Public distribution | Derived Markdown and public URLs only; original source files, extracted text, and caches withheld locally. |
| Review confidence | High for identity, method, and table transcription; medium for interpretation; low for independent reproduction. |

## Concise Research Notes

The paper addresses weakly-supervised audio-visual video parsing (AVVP), where training uses video-level event labels but evaluation requires segment-level audio-only, visual-only, and audio-visual event localization. The authors identify two failure pressures: coarse labels do not provide stable temporal supervision, and global audio-visual alignment can force unrelated or asynchronous events together.

The proposed E-CMA framework, labeled E-CMANet in the result tables, builds on a CoLeaF-style pipeline with CLAP and CLIP features, hierarchical attention, and multimodal multiple-instance pooling. An exponential-moving-average teacher produces segment-level pseudo masks using class-adaptive thresholds or top-k selection. A masked binary cross-entropy term applies supervision only at selected segment-class positions. The class-aware cross-modal agreement (CMA) term aligns audio and visual embeddings only when both modalities are confident for a labeled event class at the same segment; its loss is a cosine-distance average over those valid pairs.

The paper evaluates LLP (11,849 ten-second videos and 25 event categories) and UnAV-100 (10,790 videos and more than 30,000 event instances across 100 classes). It reports F1 scores at segment and event levels with IoU greater than 0.5. On LLP, E-CMANet reports segment-level A/V/AV scores of 66.1/69.9/61.7, Type@AV 65.9, and Event@AV 65.4; event-level A/V/AV scores are 54.5/66.6/53.5, with Type@AV 58.2 and Event@AV 54.3. On UnAV-100 it reports AV (Seg) 41.8 versus CoLeaF 41.5 and AV (Event) 47.4 versus the best listed baseline 47.8. These are source-reported results, not independent measurements.

The authors' ablation discussion attributes complementary value to EMA and CMA, while the conclusion acknowledges that the fixed pseudo-label strategies may not adapt to varying event distributions. Reviewer interpretation adds further limits: teacher confidence can reinforce systematic errors, thresholds and top-k choices may be distribution-sensitive, the baseline comparison is restricted by feature-fusion choices, and no independent seeds, calibration analysis, or code execution was available in this run. Implementation relevance is strongest for confidence-gated multimodal systems that preserve modality-specific evidence and abstain when alignment is uncertain.

## Evidence and Attribution

- **E1 — primary metadata:** The official arXiv record establishes title, authors, date, abstract, index terms, and identifier.
- **E2 — primary method:** The official full-paper HTML describes the AVVP problem, CoLeaF-based framework, EMA teacher update, adaptive/top-k pseudo masks, masked loss, and class-aware CMA conditions and loss.
- **E3 — primary experiments:** The official full-paper HTML reports LLP and UnAV-100 setup, metrics, Tables 1–3, ablations, and conclusion-level limitations.
- **E4 — local integrity evidence:** The private archive unit was repaired through the pinned broker; the valid PDF and full-paper HTML passed the required checks. Local paths and source bytes are withheld from this public report.
- **E5 — related processed evidence:** The AV Emotion Fusion DEP records audio-video fusion, contrastive pairing, modality-specific failure conditions, and the need for per-class and missing-modality evaluation.
- **E6 — related processed evidence:** The CorrKD Missing Modal DEP records complete-modality teacher to incomplete-modality student distillation and relational objectives for missing streams.
- **E7 — related processed evidence:** The Cued Speech MLLM Intake records modality accountability around confidence, availability, alignment, provenance, and privacy-sensitive multimodal cues.

## Related DEP Entries

1. **[AV Emotion Fusion](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md)** — selected because it directly examines audio-only, video-only, fused, and contrastively aligned audiovisual representations, including cases where fusion helps or hurts. Basis: E5 and its cited primary paper [arXiv:2006.08129](https://arxiv.org/abs/2006.08129).
2. **[CorrKD Missing Modal](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-CorrKD%20Missing%20Modal/corrkd_missing_modal_manuscript.md)** — selected because its complete-modality teacher/incomplete-modality student design supplies a robustness lens for E-CMA's confidence-gated alignment and for missing or unreliable streams. Basis: E6 and its cited primary paper [arXiv:2404.16456](https://arxiv.org/abs/2404.16456).
3. **[Cued Speech MLLM Intake](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260721-Cued%20Speech%20MLLM%20Intake/cued-speech-mllm-intake-review.md)** — selected because it reframes multimodal fusion as an accountable pipeline in which confidence, availability, alignment, and provenance travel with each cue. Basis: E7 and its cited primary paper [arXiv:2503.21785](https://arxiv.org/abs/2503.21785).

## Synthesis Note

### Concept Bridge

E-CMA turns weak video-level supervision into selective segment-level supervision and aligns modalities only when a class, time position, and confidence gate agree. AV Emotion Fusion supplies the empirical caution that multimodal fusion is conditional: a fused model can help on one label set and underperform audio alone on another. CorrKD supplies a teacher/student response to incomplete modalities, suggesting that the stable knowledge path should be separated from the inference path. Cued Speech MLLM Intake supplies the governance and observability layer: modality availability, confidence, temporal alignment, and provenance should be explicit outputs rather than hidden assumptions. The bridge is therefore **selective supervision -> conditional fusion -> graceful missingness -> accountable evidence**.

### Potential Implementations

1. **Confidence-gated AV event parser.** Add the EMA teacher and CMA pair selector to a weakly-supervised AVVP baseline, emit per-segment class masks, and abstain when only one modality is confident. Evaluate per-class segment/event F1, calibration, modality disagreement, and shuffled-pair controls.
2. **Missing-modality distillation adapter.** Train a complete-stream teacher and a student that sees masked or corrupted audio/video, transferring only confidence-qualified relational targets. Evaluate complete, single-stream, naturally missing, and synthetic-corruption conditions without exposing raw media in public artifacts.
3. **Modality accountability evidence card.** Wrap a multimodal parser with a signed record of input availability, alignment status, teacher confidence, selected pairs, disagreement, output, and abstention. Use the card to gate downstream automation and to make unsupported cross-modal matches reviewable.

### Deeper Relationship Observations

1. **Alignment is a decision, not a default.** E-CMA and AV Emotion Fusion both imply that cross-modal similarity should be conditioned on event identity and evidence quality; unconditional fusion can convert correlation into false agreement.
2. **Teacher privilege must be measured.** CorrKD makes the information asymmetry explicit because the teacher sees complete inputs. E-CMA's EMA teacher instead stabilizes a shared backbone; both designs need controls that separate teacher advantage from the student objective.
3. **Provenance is part of model quality.** The Cued Speech review's accountability framing generalizes to AVVP: a high score without the selected segments, modality state, and confidence path cannot explain whether the system localized an event for the right reason.

### Conceptual Similarities

1. **Selective evidence transfer:** all four records prefer transferring or using evidence at qualified positions rather than treating every modality token as equally reliable.
2. **Temporal or relational structure:** E-CMA uses segment-class pairs, AV Emotion Fusion uses synchronized clip relationships, CorrKD transfers representation geometry, and Cued Speech tracks cue alignment.
3. **Conditional deployment value:** each record warns, directly or by reviewer inference, that aggregate benchmark performance does not guarantee robustness under missing, conflicting, shifted, or privacy-constrained inputs.

### MVP Implementations with Code Mock-Ups

1. **Synthetic class-aware pair selector.**

```python
import numpy as np

def cma_pairs(audio, visual, pa, pv, video_labels, threshold=0.7):
    # Synthetic arrays only: [time, class, dim] and [time, class].
    valid = (pa >= threshold) & (pv >= threshold) & (video_labels[None, :] == 1)
    a = audio[valid]
    v = visual[valid]
    if len(a) == 0:
        return 0.0, valid
    cosine = (a * v).sum(1) / (np.linalg.norm(a, axis=1) * np.linalg.norm(v, axis=1) + 1e-8)
    return float(np.mean(1.0 - cosine)), valid
```

2. **EMA teacher and pseudo-mask update.**

```python
def ema_update(teacher, student, alpha=0.99):
    return {k: alpha * teacher[k] + (1.0 - alpha) * student[k]
            for k in teacher}

def adaptive_mask(scores, scale=1.0):
    # scores: synthetic [time, class] teacher probabilities.
    threshold = scale * scores.mean(axis=0, keepdims=True)
    return (scores >= threshold).astype("int8")
```

3. **Quality-aware fusion with abstention.**

```python
def fuse_or_abstain(audio_score, visual_score, audio_quality, visual_quality,
                    min_quality=0.6, max_disagreement=0.35):
    if min(audio_quality, visual_quality) < min_quality:
        return {"decision": "abstain", "reason": "low_modality_quality"}
    disagreement = abs(audio_score - visual_score)
    if disagreement > max_disagreement:
        return {"decision": "abstain", "reason": "cross_modal_conflict"}
    return {"decision": "fused", "score": (audio_score + visual_score) / 2.0}
```

### Developer Challenges

1. Build a confidence and provenance schema that preserves segment, class, modality, teacher version, threshold policy, and abstention reason without logging sensitive media.
2. Design matched-budget ablations that distinguish EMA stabilization, pseudo-mask selection, CMA alignment, and extra computation.
3. Stress-test asynchronous, missing, and contradictory modalities while keeping evaluation data authorized, privacy-preserving, and reproducible.

### Author Challenges

1. Replace fixed threshold/top-k choices with a distribution-aware policy and report calibration, uncertainty, and failure-regime behavior.
2. Publish enough configuration, seeds, and code or executable traces for independent reconstruction of the LLP and UnAV-100 tables.
3. Test whether the selective alignment mechanism transfers across domains, event-frequency shifts, natural missingness, and modality conflict rather than only benchmark-correlated settings.

## Validation Notes

- The source unit was classified `partial` before repair and `complete` after one bounded repair. PDF and full-paper HTML checks passed; source package was unavailable.
- The review used the public arXiv metadata and full-paper HTML plus private local source evidence. No experiment, code, dataset, or source file was independently executed or redistributed.
- The public artifact was checked for local paths, drive-letter paths, home-directory names, usernames, machine names, local timezone labels, and exact local execution timestamps before staging.
- The DEP inventory contains only its README and manuscript; no `.source/` directory was created.

## Attribution Block

- Source URL: https://arxiv.org/abs/2509.14097
  - Applies to: source identity, authors, date, abstract, and index terms.
- Source URL: https://arxiv.org/html/2509.14097
  - Applies to: method, equations, experiments, tables, ablations, and limitations.
- Source URL: https://arxiv.org/pdf/2509.14097
  - Applies to: public PDF locator; the local PDF was inspected but withheld.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: repository layout, DEP classes, source-withholding policy, and attribution rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: DEP-E filing and publication-index maintenance.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.logs/README.md
  - Applies to: public-safe log conventions.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.reports/README.md
  - Applies to: Report-Mark placement.
- Repository file: `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md`
  - Applies to: related audio-video fusion evidence and synthesis.
- Repository file: `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md`
  - Applies to: related teacher/student and missing-modality evidence.
- Repository file: `.lake-data/DEP-A/DEP-A-20260721-Cued Speech MLLM Intake/cued-speech-mllm-intake-review.md`
  - Applies to: related modality-accountability synthesis.
- Source URL: https://arxiv.org/abs/2006.08129
  - Applies to: the primary paper cited by the AV Emotion Fusion DEP.
- Source URL: https://arxiv.org/abs/2404.16456
  - Applies to: the primary paper cited by the CorrKD Missing Modal DEP.
- Source URL: https://arxiv.org/abs/2503.21785
  - Applies to: the primary paper cited by the Cued Speech MLLM Intake.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: inspected related raw-data repository policy; no raw source was used or copied.
