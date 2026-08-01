# Report-Mark: RawBMamba

## Source Metadata

| Field | Value |
|---|---|
| Work | *RawBMamba: End-to-End Bidirectional State Space Model for Audio Deepfake Detection* |
| Authors | Yujie Chen; Jiangyan Yi; Jun Xue; Chenglong Wang; Xiaohui Zhang; Shunbo Dong; Siding Zeng; Jianhua Tao; Lv Zhao; Cunhang Fan |
| arXiv | 2406.06086v2; submitted 2024-06-10; revised 2024-06-18 |
| Venue | Interspeech 2024, pp. 2720-2724 |
| DOI | 10.21437/Interspeech.2024-698; arXiv DOI 10.48550/arXiv.2406.06086 |
| Primary URLs | https://arxiv.org/abs/2406.06086; https://arxiv.org/html/2406.06086; https://www.isca-archive.org/interspeech_2024/chen24k_interspeech.html |
| Source state | Initially partial; repaired to verified complete PDF plus full-paper HTML. Private source files were inspected locally and withheld. |
| Source package | Not available through the approved broker redirect policy. |
| Review date | 2026-08-01 |

## Research Notes

### Problem and Contribution

RawBMamba addresses audio deepfake detection from raw waveforms. The paper argues that spoof artifacts can appear at short time scales, such as local spectral or phonetic irregularities, and at longer scales, such as rhythm, prosody, and contextual inconsistencies. Its proposed path combines a parametrizable sinc front end and convolutional blocks for short-range features with two direction-specific Mamba paths for long-range context. A bidirectional feature-fusion module applies attention to each direction and concatenates the resulting embeddings before authenticity classification.

The main design contribution is therefore a representation split and recombination: learn local acoustic evidence without hand-crafted features, then expose the resulting sequence to forward and backward state-space scans. This is an architectural hypothesis, not proof that every spoof cue requires bidirectional modeling.

### Method and Evaluation

The inspected paper uses 64,000-sample inputs, approximately four seconds, a 70-filter sinc layer, four RawNet2-style convolutional sub-blocks, Adam with learning rate 1e-5, batch size 32, 32 epochs, A-Softmax loss, and ASVspoof 2019 LA training and development data on one RTX 3090. Evaluation uses ASVspoof2019 LA, ASVspoof2021 LA, and ASVspoof2021 DF with EER and minimum t-DCF.

The bidirectional model is evaluated at 4, 8, and 12 total Mamba layers. In the comparison table, the 12-layer bidirectional configuration reports 1.19% EER / 0.0360 t-DCF on 19LA, 3.28% / 0.2709 on 21LA, and 15.85% EER on 21DF. Concatenation is the strongest of the three displayed fusion choices on the aggregate table. The paper reports a 34.1% improvement over Rawformer on 21LA; the inspected table compares against SE-Rawformer rows, so the baseline naming and arithmetic should be made explicit in a reproduction.

The author-linked implementation is publicly available at https://github.com/cyjie429/RawBMamba. Its README provides training and evaluation entry points, pre-trained-model evaluation scripts, and one README result row: 1.19% EER on 19LA, 3.39% EER on 21LA, and 15.85% EER on 21DF. The README also warns that training variance can produce outcomes better than the paper. The repository was inspected but not executed for this review.

### Evidence and Attribution

The arXiv abstract and official Interspeech record support the paper identity, authorship, venue, DOI, acceptance context, high-level method, and headline result. The locally inspected full-paper PDF and full-paper HTML support the detailed architecture, training configuration, tables, ablations, and conclusion. The official code README supports implementation availability and the distinction between paper-reported and README-reported values. A Zenodo record exposes an attributed RawBMamba code archive with DOI 10.5281/zenodo.12743966; that archive was used as availability context, not as executed evidence.

## Related DEP Entries

| Entry | Concrete overlap | Source basis |
|---|---|---|
| .lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md | Audio representation, temporal modeling, fusion ablations, and the need to test whether added pathways improve a fixed task. | Inspected related manuscript and README; its four-class result shows that more modalities do not automatically improve a classifier. |
| .lake-data/DEP-E/DEP-E-20260731-Lattice Spoken LM/lattice_spoken_lm_manuscript.md | Speech representation design and the information lost when a downstream model receives only one compressed view of a speech signal. | Inspected related manuscript and README; its uncertainty-preserving lattice framing provides a contrast to RawBMamba's raw-waveform end-to-end path. |
| .lake-data/DEP-E/DEP-E-20260720-APB2Face Safety/apb2face_safety_manuscript.md | Audio-conditioned synthetic media, deepfake risk, provenance, consent, and defensive evaluation boundaries. | Inspected related manuscript and README; its safety analysis establishes a concrete governance frame for audio-linked manipulation systems. |

## Synthesis Note

### Concept Bridge

RawBMamba is best carried forward as a layered evidence gate rather than a universal authenticity oracle. Its short-range/long-range split gives engineers a useful diagnostic axis: when a detector changes, measure whether gains come from local artifact sensitivity, broader context, or a calibration side effect. The related DEP entries add three missing controls: compare modality and fusion paths under matched splits, preserve uncertainty rather than collapsing early, and bind deepfake research to consent, provenance, and abstention. Together they suggest a detector that reports evidence channels and shift state, not only a binary label.

### Potential Implementations

1. **Consent-bound offline authenticity review.** User: an authorized audio-forensics researcher. Goal: compare a RawBMamba-like local/global model against raw-waveform baselines on public or explicitly licensed benchmarks. Mechanism: run fixed windows, retain local/global score components, and require calibration plus speaker-disjoint evaluation before any conclusion. Inputs: licensed audio, labels, split manifest, model version, and evaluation policy. Outputs: per-slice EER/t-DCF, calibration plots, abstention counts, and an audit report. Risk controls: local processing, no speaker identification, no raw-audio logging, and no operational accusation workflow. Evaluation: repeated seeds, cross-dataset tests, and predeclared confidence bounds.

2. **Streaming quality-aware triage.** User: a media-integrity operations team with explicit authorization. Goal: prioritize clips for human review without making an automated identity or legal decision. Mechanism: combine short-range and bounded-context scores with audio-quality and shift indicators; abstain when the clip is outside the evaluated duration or channel envelope. Inputs: consented audio, quality telemetry, benchmark-calibrated thresholds, and a review queue. Outputs: triage priority, evidence summary, and reason for abstention. Risk controls: human review, appeal, retention limits, provenance disclosure, and rate limits. Evaluation: false-positive cost, slice calibration, latency, and shift-triggered abstention.

3. **Reproduction and regression harness.** User: an ML researcher or maintainer. Goal: establish whether the paper and public implementation can be reproduced. Mechanism: pin dependencies, replay public evaluation scripts, compare table rows, and record differences caused by seeds, checkpoints, windowing, or preprocessing. Inputs: public repository, released checkpoint if licensed, benchmark access, and a machine-readable manifest. Outputs: a versioned evidence ledger and pass/fail reproduction card. Risk controls: no dataset redistribution, no uncontrolled scraping, and synthetic smoke tests before restricted data. Evaluation: exact metric agreement where possible and a documented explanation for every mismatch.

### Deeper Relationship Observations

1. The paper's bidirectional context is an information-preservation choice: it delays the decision until both temporal directions have been scanned, while the lattice-related DEP preserves competing recognition hypotheses instead of forcing a single early path. Both raise the same engineering question: which evidence is removed before classification, and can the loss be measured?
2. The AV Emotion Fusion DEP shows that an extra pathway can hurt when evidence quality, labels, and splits are weak. RawBMamba's stronger table rows therefore need matched ablations and repeated evaluation before the architecture can be credited with generalization rather than favorable preprocessing or seed variance.
3. APB2Face Safety reframes audio-linked models as part of a synthetic-media ecosystem. A detector can reduce harm only when it is paired with provenance, consent, privacy, calibration, and human review; score improvement alone does not establish safe deployment.

### Conceptual Similarities

1. All four artifacts treat representation choice as a first-order determinant of downstream reliability: raw waveform, audio/video features, speech lattices, and audio-conditioned geometry each expose different evidence and failure modes.
2. All four require evaluation beyond one headline metric: RawBMamba uses multiple ASVspoof conditions; AV Emotion Fusion uses modality and class comparisons; Lattice Spoken LM tracks uncertainty and dataset boundaries; APB2Face Safety emphasizes consent, provenance, and misuse review.
3. All four benefit from reversible, auditable interfaces. A local/global score ledger, an explicit lattice, a modality-quality vector, or a consent/provenance record makes disagreement visible instead of hiding it inside a single prediction.

### MVP Implementations with Code Mock-ups

1. **Local/global score ledger**

~~~python
from dataclasses import dataclass

@dataclass(frozen=True)
class ScoreLedger:
    score: float
    abstain: bool
    reason: str

def combine_scores(local_score: float, global_score: float, quality: float) -> ScoreLedger:
    if not 0.0 <= quality <= 1.0:
        raise ValueError("quality must be normalized")
    if quality < 0.50:
        return ScoreLedger(0.0, True, "low_audio_quality")
    score = 0.45 * local_score + 0.55 * global_score
    return ScoreLedger(score, False, "calibrated_demo")
~~~

This is a synthetic, non-deployment mock-up. A real system would replace the scores with versioned model outputs and add calibration, shift detection, and human review.

2. **Shift and window audit**

~~~python
def audit_window(reference_seconds: float, observed_seconds: float,
                 reference_rate: float, observed_rate: float) -> dict:
    duration_ratio = observed_seconds / reference_seconds
    rate_ratio = observed_rate / reference_rate
    shifted = not (0.75 <= duration_ratio <= 1.25 and 0.95 <= rate_ratio <= 1.05)
    return {
        "duration_ratio": round(duration_ratio, 3),
        "sample_rate_ratio": round(rate_ratio, 3),
        "abstain": shifted,
        "reason": "outside_evaluated_envelope" if shifted else "in_envelope",
    }
~~~

This mock-up makes the four-second, fixed-rate evaluation boundary explicit without processing audio or identifying a speaker.

3. **Calibration-aware review queue**

~~~python
def route_for_review(score: float, threshold: float,
                     calibration_examples: int, shift_flag: bool) -> dict:
    if calibration_examples < 100 or shift_flag:
        return {"route": "human_review", "reason": "insufficient_calibration_or_shift"}
    label = "spoof_suspect" if score < threshold else "bonafide_candidate"
    return {"route": "research_queue", "label": label, "reason": "bounded_demo"}
~~~

This mock-up is intentionally not an accusation or access-control policy. It illustrates a stop condition before a score is used outside a research queue.

### Developer Challenges

1. Implementing bidirectional Mamba with stable dependencies, memory bounds, and a streaming fallback requires more than copying a research block; latency and causal/non-causal behavior must be specified.
2. Reproducing the benchmark tables requires a versioned data pipeline, exact four-second windowing, labels, splits, codecs, checkpoints, and deterministic evaluation while respecting dataset licenses.
3. A safe detector needs calibration, shift monitoring, abstention, retention controls, and human review interfaces in addition to a neural score.

### Author Challenges

1. Clarify the baseline naming behind the 34.1% headline and provide a reproducible arithmetic link from the cited row to the reported improvement.
2. Report repeated-seed uncertainty, confidence intervals or significance testing, and sensitivity to crop length, duration, channel, codec, and noise.
3. Expand reproducibility disclosure around exact preprocessing, checkpoint provenance, compute/runtime, code version, and benchmark access, while documenting privacy and consent boundaries.

## Validation Notes

- The primary local source unit passed the mandatory complete-paper gate after one bounded repair: PDF size/header/trailer checks passed; full-paper HTML passed body-size, document-marker, heading, and structure-term checks; no partial files remained.
- The source package was not collected because the approved broker rejected its redirect; the PDF and full-paper HTML remained sufficient for review.
- The title, authors, version, venue, and DOI were cross-checked against the arXiv record and official Interspeech page.
- Detailed method and result values were cross-checked against the locally inspected full-paper HTML tables. No code or benchmark was executed.
- Random selection used 75,957 unique paper units with a uniform draw at index 5,736. Deduplication found no match in current public artifact areas, automation memory, or relevant Black-Lake-Data search results; reselections: 0.
- Public allowlist boundary: generated Markdown under .logs, .reports, and .lake-data only. No PDF, HTML, source archive, cache, extracted text, local path, username, machine identifier, or exact local execution timestamp is included.

## Final Attribution Block

- Source URL: https://arxiv.org/abs/2406.06086
  - Applies to: identity, authors, abstract, dates, version, and arXiv DOI.
- Source URL: https://arxiv.org/html/2406.06086
  - Applies to: full-paper method, tables, results, ablations, and conclusion; a private local copy was inspected and withheld.
- Source URL: https://arxiv.org/pdf/2406.06086
  - Applies to: primary PDF verification and visual/source cross-check; the source file was withheld.
- Source URL: https://www.isca-archive.org/interspeech_2024/chen24k_interspeech.html
  - Applies to: official venue record, pages, DOI, acceptance context, and code locator.
- Source URL: https://doi.org/10.21437/Interspeech.2024-698
  - Applies to: publisher DOI.
- Source URL: https://github.com/cyjie429/RawBMamba
  - Applies to: official implementation, evaluation commands, README result row, and implementation availability.
- Source URL: https://zenodo.org/records/12743966
  - Applies to: attributed code-archive availability and license context; not executed for this review.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md
  - Applies to: related audio representation and fusion synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260731-Lattice%20Spoken%20LM/lattice_spoken_lm_manuscript.md
  - Applies to: related speech representation and uncertainty synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260720-APB2Face%20Safety/apb2face_safety_manuscript.md
  - Applies to: related synthetic-media safety and provenance synthesis.
