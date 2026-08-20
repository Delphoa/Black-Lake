---
title: "RawBMamba Review - DEP-E"
generated_at: "2026-08-01"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of a raw-waveform bidirectional state-space model for audio deepfake detection."
source_status: "mixed"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-01"
temporal_cutoff: "2026-08-01"
primary_url: "https://arxiv.org/abs/2406.06086"
stable_identifier: "arXiv:2406.06086v2; DOI:10.21437/Interspeech.2024-698"
confidence_summary: "Medium-high for the reported architecture and tables; medium for reproducibility and deployment implications because no code or benchmark was executed."
safety_scope: "Defensive, educational, and authorized evaluation only"
distribution_notes: "Source files were inspected locally and withheld; this artifact contains derived Markdown and public source locators only."
---

# RawBMamba Review - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Status | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | RawBMamba primary paper | Primary artifact | PDF | arXiv:2406.06086v2 | https://arxiv.org/pdf/2406.06086; private copy inspected and withheld | Public source locator; no PDF redistributed | 2026-08-01 | Inspected |
| S2 | RawBMamba primary paper | Primary artifact | Full-paper HTML | arXiv:2406.06086v2 | https://arxiv.org/html/2406.06086; private copy inspected and withheld | Public source locator; no HTML redistributed | 2026-08-01 | Verified and inspected |
| S3 | arXiv record | Primary metadata | Abstract HTML | arXiv:2406.06086v2 | https://arxiv.org/abs/2406.06086 | Metadata page is not treated as full paper | 2026-08-01 | Inspected |
| S4 | Interspeech record | Official venue context | Publisher HTML | Interspeech 2024 | https://www.isca-archive.org/interspeech_2024/chen24k_interspeech.html | Venue metadata and DOI locator | 2026-08-01 | Inspected |
| S5 | Author-linked implementation | Official implementation | Git repository | main branch observed | https://github.com/cyjie429/RawBMamba | Repository was inspected, not executed or redistributed | 2026-08-01 | Inspected |
| S6 | Zenodo RawBMamba archive | Attributed artifact context | Archive record | DOI:10.5281/zenodo.12743966 | https://zenodo.org/records/12743966 | CC BY 4.0 context; not deposited or executed | 2026-08-01 | Inspected |
| S7 | AV Emotion Fusion DEP | Related research | Black Lake Markdown | DEP-E-20260713 | Public repository path in Source References | Derived public artifact; no claims transferred | 2026-08-01 | Inspected |
| S8 | Lattice Spoken LM DEP | Related research | Black Lake Markdown | DEP-E-20260731 | Public repository path in Source References | Derived public artifact; no claims transferred | 2026-08-01 | Inspected |
| S9 | APB2Face Safety DEP | Related research | Black Lake Markdown | DEP-E-20260720 | Public repository path in Source References | Derived public artifact; no claims transferred | 2026-08-01 | Inspected |

The local archive unit was initially partial: a valid PDF existed, but metadata HTML and full-paper HTML were absent. One bounded brokered repair preserved the PDF and collected the missing metadata and full-paper HTML. Final validation found a 986,266-byte PDF with the required header and trailer, a 266,444-byte full-paper HTML file with 48,345 extracted body characters, 39 heading markers, a document marker, and 6 paper-structure term classes. No partial files remained. The optional source package was unavailable through the approved redirect policy. All original source files and repair records remain local and are not part of this deposit.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary paper PDF | Paper identity, architecture, training setup, result tables, conclusion | C1-C5; detailed summary | High | Source file is private and not redistributed |
| E2 | S2 | Primary full-paper HTML | Searchable sections, equations, ablations, tables, and result text | C1-C6 | High | HTML rendering may omit some visual fidelity from the PDF |
| E3 | S3 | Primary metadata record | Authors, v1/v2 dates, abstract, subjects, acceptance comment, arXiv DOI | Source metadata and C1 | High | Abstract is incomplete evidence for detailed empirical claims |
| E4 | S4 | Official venue record | Interspeech publication, pages, DOI, code locator, headline result | Source metadata and C1/C5 | High for metadata; medium for detailed metrics | Venue page repeats the paper abstract rather than full tables |
| E5 | S5 | Official repository README | Training/evaluation entry points, claimed result row, pre-trained-model availability, variance warning | C5 and reproducibility assessment | Medium | Repository was not executed; default branch state can change |
| E6 | S6 | Attributed artifact record | Code archive availability, DOI, file size, CC BY 4.0 record | Reproducibility context | Medium | Archive contents were not executed or independently diffed |
| E7 | S7 | Related Black Lake manuscript | Audio classification, modality/fusion ablations, negative-result discipline | Observations and related synthesis | Medium | Related paper is a different task and dataset |
| E8 | S8 | Related Black Lake manuscript | Speech representation, uncertainty preservation, and information-loss framing | Observations and related synthesis | Medium | Historical ASR/SLU setting differs from spoof detection |
| E9 | S9 | Related Black Lake manuscript | Audio-linked synthetic media, consent, provenance, and defensive evaluation | Considerations and safety synthesis | Medium | Generative face reenactment is not a detector |

## Executive Summary

RawBMamba is an end-to-end audio deepfake detector that operates on raw waveforms and separates short-range from long-range evidence. Its sinc and convolutional front end learns local acoustic features; two direction-specific Mamba paths scan the resulting sequence; a bidirectional fusion module joins the representations for classification. The paper evaluates ASVspoof2019 LA, ASVspoof2021 LA, and ASVspoof2021 DF using EER and minimum t-DCF.

The strongest displayed 12-layer bidirectional configuration reports 1.19% EER / 0.0360 t-DCF on 19LA, 3.28% / 0.2709 on 21LA, and 15.85% EER on 21DF. The paper reports a 34.1% improvement over Rawformer on 21LA, although the detailed table names SE-Rawformer, so the baseline mapping requires explicit reproduction. The public implementation provides evaluation entry points and a README result row close to the paper, but no execution was performed here.

Reviewer assessment: the paper provides a coherent and practically relevant architecture hypothesis with multi-condition evidence, but it does not establish deployment readiness. Fixed four-second windows, one training configuration, missing uncertainty estimates, benchmark-era limits, and unclear headline arithmetic leave meaningful replication work. Confidence is high for the mechanism and displayed tables, medium for generalization, and low-to-medium for operational performance.

## Detailed Summary

### Problem

Text-to-speech and voice-conversion systems can produce speech that is difficult to distinguish from bona fide speech. The paper frames detection as a need to identify artifacts that occur at both short and long temporal scales. Short-range evidence may include local spectral or phonetic irregularities; longer-range evidence may include prosody, rhythm, or context inconsistencies. The target is an end-to-end detector that learns from raw audio rather than relying on a separate hand-crafted feature pipeline.

### Background and Vocabulary

- Raw waveform: the sampled audio signal presented directly to a neural front end.
- Sinc layer: a parameterized band-pass filter bank whose cutoff frequencies are learned.
- State-space model: a sequence model that propagates a hidden state through learned transition and input/output maps.
- Mamba: a selective state-space architecture designed for efficient long-sequence processing.
- Bidirectional scan: two state-space passes, one over the forward sequence and one over the reversed sequence, followed by fusion.
- EER: equal error rate, where false-accept and false-reject rates meet; lower is better.
- Minimum t-DCF: a tandem detection cost used in spoofing evaluations; lower is better.

### Method

RawBMamba uses a RawNet2-inspired front end. A 70-filter sinc layer produces low-level feature maps, and four convolutional sub-blocks with squeeze-and-excitation operations produce high-level short-range maps. The time-frequency-like representation is flattened into a sequence. Two structurally identical Mamba networks process forward and reversed versions of the sequence. Each direction is passed through a linear self-attention operation, the results are concatenated, and a multilayer perceptron produces the fused representation for authenticity discrimination.

The training setup uses 64,000 sample inputs, approximately four seconds, Adam with learning rate 1e-5, batch size 32, 32 epochs, A-Softmax loss, and ASVspoof2019 LA training and development data on one RTX 3090. The design is not a causal streaming detector because the backward path uses future context relative to each position.

### Experiments and Results

The paper evaluates 19LA, 21LA, and 21DF. The 12-layer bidirectional configuration reports:

| Configuration | 19LA EER | 19LA t-DCF | 21LA EER | 21LA t-DCF | 21DF EER |
|---|---:|---:|---:|---:|---:|
| 12-layer unidirectional | 1.47 | 0.0467 | 2.84 | 0.2517 | 22.48 |
| 12-layer bidirectional | 1.19 | 0.0360 | 3.28 | 0.2709 | 15.85 |

The fusion ablation reports concatenation at 1.19% / 0.0360 on 19LA, 3.28% / 0.2709 on 21LA, and 15.85% on 21DF. Summation reports 1.27% / 0.0400, 4.13% / 0.2924, and 16.58%; attention reports 1.19% / 0.0369, 3.19% / 0.2620, and 18.42%.

The comparison table lists RawBMamba at 1.19% / 0.0360 on 19LA, 3.28% / 0.2709 on 21LA, and 15.85% on 21DF. SE-Rawformer is listed at 1.05% / 0.0344, 4.98% / 0.3186, and no 21DF result. A second SE-Rawformer row reports 1.15% / 0.0314, 4.31% / 0.2851, and 20.26%. RawMamba, the unidirectional counterpart, reports 1.47% / 0.0467, 2.84% / 0.2517, and 22.48%.

### Reproducibility and Availability

The author-linked GitHub repository contains model, data-feeder, training, feature-extraction, and evaluation files, and describes pre-trained-model evaluation scripts. Its README reports 1.19% EER on 19LA, 3.39% EER on 21LA, and 15.85% EER on 21DF, and explicitly notes training variance. A Zenodo record exposes a RawBMamba-main.zip archive with a DOI and CC BY 4.0 record. This evidence establishes public availability, not successful reproduction: code, dependencies, checkpoints, and benchmark access were not executed or independently verified in this review.

### Conclusion

The source concludes that bidirectional Mamba can combine short- and long-range audio evidence and can generalize across the selected ASVspoof conditions. The evidence supports a promising detector architecture and a useful ablation axis. It does not by itself support a universal detector claim, causal streaming deployment, speaker-level attribution, or legal/identity decisions.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | RawBMamba combines a learned short-range raw-audio front end with bidirectional long-range Mamba modeling. | Author claim supported by method | E1, E2, E3, E4 | Directly supported by the architecture description and equations. | High |
| C2 | The 12-layer bidirectional configuration improves 21DF EER over the displayed 12-layer unidirectional configuration from 22.48% to 15.85%. | Derived table comparison | E1, E2 | Arithmetic is directly recoverable from the source table; it is not an isolated causal ablation of every component. | High |
| C3 | Concatenation is the strongest displayed fusion method across the three reported aggregate conditions. | Author claim / table interpretation | E1, E2 | Supported by the displayed fusion rows, with attention slightly lower on 21LA EER but worse on 21DF. | High |
| C4 | RawBMamba achieves a 34.1% improvement over Rawformer on 21LA. | Author claim | E3, E4; detailed comparison in E1/E2 | The headline is plausible from the table but the Rawformer versus SE-Rawformer naming needs a precise arithmetic mapping. | Medium |
| C5 | The public implementation enables training and evaluation of RawBMamba. | Implementation observation | E5, E6 | Availability is supported; reproducibility is not established because no execution occurred. | Medium |
| C6 | The architecture is ready for operational authenticity decisions. | Reviewer assessment | E1-E9 | Not supported. The evidence lacks deployment calibration, uncertainty, shift coverage, privacy governance, and human-review validation. | High |

## Methodology

- Research objective: preserve a source-grounded review of one randomly selected arXiv paper, test the integrity of its local source unit, reconstruct its mechanism and evidence, and translate it into safe follow-on research.
- Sources inspected: the repaired local PDF and full-paper HTML, arXiv metadata, the official Interspeech record, the author-linked GitHub README, the Zenodo record, and three existing Black Lake related manuscripts and READMEs.
- Discovery strategy: enumerate local PDF files with rg --files -g "*.pdf"; reduce parent directories to unique paper units; inspect the selected unit's nearby README; use public arXiv, venue, code, and archive pages for identity and context; inspect related Black Lake artifacts by repository search.
- Random selection: sort 75,957 unique PDF-parent units and use a uniform PowerShell Get-Random draw. The accepted draw was zero-based index 5,736 from 75,957 units.
- Deduplication: check arXiv ID, arXiv DOI, publisher DOI, normalized title, slug, prior logs, reports, DEP-E entries, staging markers, automation memory, and relevant Black-Lake-Data search results. The first draw had 0 exclusions and 0 reselections, including no same-paper marker in the preceding 24 hours.
- Source-integrity gate: classify the selected unit before review. The initial unit was partial because the PDF existed without full-paper HTML. One bounded brokered repair collected the missing metadata and full-paper HTML while preserving the valid PDF. The final PDF and HTML validators passed and no partial files remained.
- Inclusion criteria: primary full-paper evidence for method, experiments, results, limitations, and conclusion; official metadata for identity and dates; official code or venue pages for availability and publication context; related DEP artifacts with concrete conceptual overlap.
- Exclusion criteria: abstract-only evidence for detailed claims; unverified secondary summaries; private source files and caches from public outputs; unsupported claims about real-world accuracy, legal status, or deployment readiness.
- Analytical approach: empirical, conceptual, comparative, implementation, replication, product research, and safety/ethics.
- Evidence handling: assign evidence IDs, map claims to ledger entries, distinguish author claims from derived comparisons and reviewer interpretation, preserve exact table values, and state missing evidence.
- Uncertainty handling: mark the baseline naming issue, lack of repeated-seed intervals, unexecuted code, fixed-window boundary, source-package failure, and dataset/licensing limits instead of smoothing them away.
- Extraction process: inspect the PDF and full-paper HTML sections, equations, tables, and conclusion; cross-check numeric rows across the primary formats; inspect repository README and archive metadata without executing code.
- Version control: review arXiv v2 and the dated venue/code records accessed on 2026-08-01; code is referenced at its public default branch without claiming a frozen commit.
- Safety handling: keep examples synthetic and defensive, prohibit speaker identification or operational accusation, and require authorized data, privacy controls, provenance, calibration, abstention, and human review.
- Reviewer stance: DEP-ready paper report combining summary, critique, reproduction planning, implementation translation, product research, and safety review.

## Scope, Constraints, and Assumptions

- Scope: RawBMamba's problem framing, architecture, training setup, ASVspoof experiments, implementation availability, limitations, related DEP synthesis, and safe downstream research paths.
- Temporal boundary: sources and public repository pages inspected through 2026-08-01; paper version is arXiv v2 and venue record is Interspeech 2024.
- Evidence limits: no benchmark execution, no code execution, no independent checkpoint inspection, no repeated-seed experiment, no dataset audit, no full runtime profile, and no source package because the approved redirect policy rejected it.
- Assumptions: the displayed tables are transcribed faithfully from the inspected primary paper; the author-linked repository is intended to implement the paper because its README links to the paper and names the same system.
- Constraints: public-output allowlist permits only generated Markdown in logs, reports, and lake-data; local source files, caches, extracted text, audio, checkpoints, and private archive records must remain local.
- Out of scope: speaker identification, biometric enrollment, autonomous accusation, production access control, evasion design, model-weight redistribution, and claims about current state of the art.
- Intended use: research review, reproduction planning, safety-aware implementation design, and durable Black Lake knowledge deposition.
- Audience: speech and audio ML researchers, forensic-evaluation engineers, data-governance reviewers, and product teams considering authorized media-integrity workflows.
- Reproducibility boundary: a reader can inspect the public paper, venue record, and implementation entry points, but cannot infer exact reproducibility without licensed benchmark access, dependency pinning, checkpoints, and an executed manifest.
- Operational boundary: discussion is limited to defensive analysis and authorized research queues; no procedure here determines whether a real person is deceptive or whether an audio file should trigger legal or account action.
- Data sensitivity: speech may be biometric or personally identifying; benchmark licenses, consent, retention, and access terms must be reviewed before use.

## Observations

- Observed pattern: bidirectionality produces its clearest displayed advantage on 21DF, where the 12-layer bidirectional model reduces EER from 22.48% to 15.85% relative to the 12-layer unidirectional model. This supports a context hypothesis but not a universal causal attribution.
- Observed pattern: fusion choice is consequential. Concatenation and attention are similar on 19LA and 21LA EER, but concatenation is much better on 21DF EER in the displayed ablation.
- Technical implication: a fixed four-second raw-waveform window makes the detector's effective evidence boundary explicit. Long utterances, very short clips, streaming constraints, and artifacts outside the crop require separate evaluation.
- Contradiction or tension: the abstract and venue page state a 34.1% improvement over Rawformer, while the detailed comparison table uses SE-Rawformer labels. The arithmetic should be bound to a named baseline row in a reproduction.
- Open question: whether the bidirectional gain is robust to speaker-disjoint, codec-shifted, noisy, multilingual, and post-processed audio remains unresolved by the inspected evidence.
- Reviewer hypothesis: local/global score decomposition could make model failures more diagnosable than a single fused score, but this is an implementation proposal rather than a source claim.
- Reviewer hypothesis: the official README's training-variance warning implies that point estimates may be unstable enough to change ranking; repeated seeds and interval estimates should be a release requirement.

## Considerations

### Evaluation and Adoption

Adoption should begin with public or explicitly licensed benchmarks and a local-only evaluation harness. Report EER, t-DCF, calibration, abstention, latency, memory, and slice-level outcomes by codec, duration, channel, noise, language, and speaker-disjoint split. A score should be treated as evidence for a human review queue, not as proof of identity, intent, or legal status.

### Privacy and Governance

Speech can expose identity, health, emotion, language, location, and social relationships. Data collection requires purpose limitation, documented consent or lawful authorization, retention limits, deletion procedures, access controls, and a prohibition on repurposing a detector for speaker surveillance. Public artifacts should not include raw audio, speaker identifiers, or embeddings.

### Security and Dual Use

Audio deepfake detection is dual-use. A defensive evaluation harness can also reveal benchmark weaknesses or encourage adversarial optimization. Keep tests authorized, rate-limited, and aggregate where possible. Do not publish evasion recipes, speaker-targeting instructions, or automated enforcement logic. Track provenance of checkpoints and benchmark manifests.

### Operational Risks

Distribution shift can convert a high benchmark score into a misleading field result. The system should expose shift indicators, reject out-of-envelope inputs, maintain a human appeal path, and log only privacy-minimized derived telemetry. Models, thresholds, dependencies, and benchmark versions need explicit lifecycle ownership.

## Strengths

- Clear mechanism-to-problem alignment: the short-range front end and bidirectional long-range paths directly address the paper's local/global artifact hypothesis.
- Useful ablations: directionality, layer count, and fusion method are separated in displayed tables rather than only compared as a single final system.
- Multi-condition evaluation: 19LA, 21LA, and 21DF provide more than one spoof and channel condition.
- Practical public trail: the author-linked repository provides training/evaluation entry points and reports a result row, while the venue page gives a stable publication DOI.
- Public-safety transfer value: the architecture naturally supports an evidence ledger that can preserve local/global score channels and abstention reasons.

## Weaknesses

- The headline 34.1% comparison is not fully transparent because the abstract says Rawformer while the detailed table labels SE-Rawformer.
- Results are point estimates without repeated-seed intervals, significance tests, or a complete uncertainty analysis in the inspected evidence.
- The fixed approximately four-second input window limits conclusions about full utterances, streaming, very short clips, and artifact timing.
- Training is described with one GPU and one main configuration; compute, runtime, memory, checkpoint provenance, and dependency versions are not fully quantified in the paper.
- The benchmark family is valuable but historical and bounded; cross-language, cross-domain, codec, noise, and modern generator coverage are not established.
- Public code availability improves the reproduction path but does not guarantee paper-matched data, dependencies, checkpoints, or successful execution.
- The paper's t-SNE visualization is useful for qualitative intuition but does not substitute for calibrated, slice-level external validation.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Bind every headline gain to a named baseline row and formula | Reporting | Removes Rawformer/SE-Rawformer ambiguity | Auditable claims | Low; may expose a smaller gain | Recompute from published table values |
| Add repeated seeds and confidence intervals | Statistical validity | README already notes training variance | Stable rankings and uncertainty | Moderate compute | Pre-register seeds and report paired intervals |
| Sweep window length and streaming mode | Boundary conditions | Four seconds may omit relevant evidence | Better duration and latency understanding | Moderate engineering | Evaluate 1, 2, 4, 8 second windows and causal fallback |
| Add codec, noise, language, and generator-shift slices | External validity | 21DF alone is not field coverage | Failure map and safer abstention | Dataset/licensing burden | Hold out conditions and report calibration |
| Release a pinned environment and machine-readable manifest | Reproducibility | README commands do not pin the full run | Lower replication friction | Maintenance burden | Clean environment replay with expected checksums |
| Add privacy and provenance controls | Safety | Speech is sensitive and model output is dual-use | Reduced misuse and clearer accountability | Governance effort | Red-team, consent, retention, and human-review audit |

## Potential Implementations

1. **Authorized research benchmark harness**: User is an audio ML researcher. Goal is to compare local/global detector variants. Inputs are licensed audio, labels, and fixed splits. Mechanism is a versioned RawBMamba-like model with per-channel score logging. Outputs are metrics, calibration, and abstention reports. Risk controls are local processing, no raw-audio logs, and no production decisions. Evaluation uses repeated seeds and speaker-disjoint slices.
2. **Human-in-the-loop media triage**: User is an authorized media-integrity analyst. Goal is to prioritize clips for review. Inputs are consented clips, quality telemetry, and calibrated thresholds. Mechanism combines local/global evidence with shift gating. Outputs are a research queue and an evidence summary. Risk controls include human approval, appeal, retention limits, provenance disclosure, and no speaker identification. Evaluation measures false-positive cost, calibration, latency, and abstention.
3. **Reproduction card generator**: User is a paper maintainer or independent reviewer. Goal is to compare paper tables with public code. Inputs are a pinned repository, benchmark access, checkpoint provenance, and an execution manifest. Mechanism replays evaluation scripts and explains mismatches. Outputs are a versioned pass/fail card. Risk controls exclude dataset redistribution and uncontrolled scraping. Evaluation requires exact metric agreement or a documented cause for each difference.

## Three Ways to Exercise This Research

1. **Synthetic local/global gate**: Objective is to test score fusion and abstention logic without audio or model weights. Inputs are synthetic scalar local/global scores and quality values. Method is to run the bounded mock-up from the Report-Mark, vary quality and score combinations, and record routes. Output is a small decision table. Success criterion is deterministic abstention below the quality floor. Stop condition is any attempt to treat the output as a real detector or identity decision.
2. **Public-benchmark reproduction review**: Objective is to check whether the official repository can reproduce its README result row. Inputs are the public repository, a licensed benchmark, pinned dependencies, and a fixed manifest. Method is to run only authorized evaluation scripts, compare displayed EER/t-DCF values, and report variance. Output is a reproducibility card. Success criterion is a traceable match or a quantified explanation of mismatch. Stop condition is missing rights, unclear provenance, or uncontrolled data access.
3. **Shift and calibration study**: Objective is to measure how performance changes under authorized duration, codec, noise, and channel shifts. Inputs are a licensed benchmark plus declared perturbation slices. Method is to keep the model and thresholds fixed, report EER, t-DCF, calibration, abstention, and latency, and retain no raw audio in logs. Output is a slice-level failure map. Success criterion is an explicit safe operating envelope. Stop condition is privacy, consent, or license uncertainty.

## Example MVP Product

- Product name: Audio Integrity Evidence Queue
- Target user: Authorized media-integrity researcher or review analyst.
- Problem: Benchmark detectors produce a score but often hide which evidence path was used, whether the input is out of distribution, and when a human should abstain.
- Core workflow: ingest an authorized clip locally; validate duration, sample rate, and provenance; compute bounded local/global evidence; calibrate against a versioned reference set; route uncertain or shifted clips to human review; export an aggregate evidence card.
- Data requirements: Public or explicitly licensed audio, labels, speaker-disjoint splits, provenance metadata, calibration examples, and a retention/deletion policy.
- Architecture: local audio validator; raw-waveform feature extractor; forward and backward state-space encoders; explicit fusion and quality gate; calibration and shift monitor; human review queue; redacted aggregate report.
- Success metrics: reproducible EER and t-DCF, expected calibration error, abstention quality, false-positive cost, per-slice robustness, median and tail latency, and zero raw-audio leakage into logs.
- Risk controls: local-only processing by default, consent and license checks, no speaker identification, no automated enforcement, human review, appeal, provenance disclosure, access control, retention limits, and red-team testing.
- Limitations: the MVP cannot prove authenticity, generalize beyond its evaluated envelope, replace expert review, or safely process unconsented speech.
- MVP boundary: no hosted public upload endpoint, no speaker search, no legal or employment decision, and no evasion testing against third-party systems.
- Deployment model: local CLI or controlled research notebook.
- Evaluation plan: synthetic smoke tests, benchmark replay, repeated seeds, calibration review, shift slices, privacy audit, and human factors review.
- Failure modes: out-of-distribution audio, label noise, data leakage, calibration drift, incorrect provenance, non-causal latency, and reviewer over-trust.
- Maintenance plan: version model, thresholds, dependencies, benchmark manifests, provenance rules, and review policy; rerun the gate after each model or dataset change.

## Related Research and Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| RawBMamba | Primary paper | Short/long-range raw-waveform deepfake detection | https://arxiv.org/abs/2406.06086 |
| Interspeech 2024 record | Official venue | Published pages, DOI, and code locator | https://www.isca-archive.org/interspeech_2024/chen24k_interspeech.html |
| RawBMamba implementation | Official code | Training, evaluation, README results, and variance note | https://github.com/cyjie429/RawBMamba |
| Mamba: Linear-Time Sequence Modeling with Selective State Spaces | Methodological neighbor | State-space sequence modeling context cited by the repository | https://arxiv.org/abs/2312.00752 |
| AV Emotion Fusion DEP | Related Black Lake research | Audio features, fusion ablations, and negative-result discipline | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md |
| Lattice Spoken LM DEP | Related Black Lake research | Speech representation and uncertainty preservation | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260731-Lattice%20Spoken%20LM/lattice_spoken_lm_manuscript.md |
| APB2Face Safety DEP | Related Black Lake research | Audio-linked synthetic media, provenance, and consent | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-APB2Face%20Safety/apb2face_safety_manuscript.md |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2406.06086 | E3; identity, authors, dates, abstract, subjects, version | 2026-08-01 | Primary metadata; abstract-only evidence is not used for detailed method claims |
| R2 | https://arxiv.org/pdf/2406.06086 | E1; primary PDF methods, tables, and conclusion | 2026-08-01 | Private local copy inspected and withheld |
| R3 | https://arxiv.org/html/2406.06086 | E2; full-paper sections, equations, tables, and results | 2026-08-01 | Private local copy inspected and withheld |
| R4 | https://www.isca-archive.org/interspeech_2024/chen24k_interspeech.html | E4; venue, pages, DOI, acceptance context, code locator | 2026-08-01 | Official venue record |
| R5 | https://doi.org/10.21437/Interspeech.2024-698 | E4; publisher DOI | 2026-08-01 | Persistent venue identifier |
| R6 | https://github.com/cyjie429/RawBMamba | E5; official implementation README and result row | 2026-08-01 | Inspected, not executed |
| R7 | https://zenodo.org/records/12743966 | E6; attributed archive and license context | 2026-08-01 | Availability context, not executed or deposited |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md | E7; audio representation and fusion synthesis | 2026-08-01 | Related DEP; no claims transferred |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260731-Lattice%20Spoken%20LM/lattice_spoken_lm_manuscript.md | E8; speech representation and uncertainty synthesis | 2026-08-01 | Related DEP; no claims transferred |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-APB2Face%20Safety/apb2face_safety_manuscript.md | E9; synthetic-media safety and provenance synthesis | 2026-08-01 | Related DEP; no claims transferred |

## Appendix

### Selection and Integrity Checklist

- Candidate enumeration used the required local PDF search and found 75,960 files grouped into 75,957 unique parent units.
- Uniform draw selected index 5,736; first draw accepted with 0 duplicate exclusions, 0 other exclusions, and 0 reselections.
- Deduplication checked arXiv ID, DOI, normalized title, slug, existing public artifact areas, automation memory, and relevant Black-Lake-Data search results.
- Initial source state was partial and review was blocked until repair.
- Final PDF passed the 10 KB, header, and trailing EOF checks.
- Final full-paper HTML passed the 5 KB, body-character, document-marker, heading-marker, and paper-structure checks.
- No .part files remained; the source package was unavailable but nonblocking.
- No source file was uploaded, committed, staged, copied, or attached; no public .source directory was created.

### Replication Checklist

1. Pin the public repository and Mamba dependency versions.
2. Obtain benchmark data through the relevant license and access process.
3. Recreate the four-second windowing, sinc front end, optimizer, batch, epochs, loss, and split.
4. Replay the 4-, 8-, and 12-layer uni/bi configurations and fusion ablations.
5. Report EER, t-DCF, calibration, seed intervals, slice metrics, and resource use.
6. Explain any difference between the paper rows, README row, and reproduced results.
7. Keep raw speech local and produce only aggregate, public-safe evidence cards.

### Decision Usefulness

After reading this artifact, a reviewer can decide that RawBMamba is a plausible research baseline for local/global audio deepfake evidence and can plan a bounded reproduction. The reviewer still cannot decide that it is reliable for real-world attribution, legal enforcement, speaker identification, or production deployment without new evidence.

## Attribution Block

- Source URL: https://arxiv.org/abs/2406.06086
  - Applies to: this manuscript.
  - Notes: Canonical metadata and paper identity.
- Source URL: https://arxiv.org/html/2406.06086
  - Applies to: this manuscript.
  - Notes: Full-paper methods and results; private source withheld.
- Source URL: https://arxiv.org/pdf/2406.06086
  - Applies to: this manuscript.
  - Notes: Primary PDF; private source withheld.
- Source URL: https://www.isca-archive.org/interspeech_2024/chen24k_interspeech.html
  - Applies to: this manuscript.
  - Notes: Official venue record.
- Source URL: https://github.com/cyjie429/RawBMamba
  - Applies to: this manuscript.
  - Notes: Official implementation context; not executed.
- Source URL: https://zenodo.org/records/12743966
  - Applies to: this manuscript.
  - Notes: Attributed archive context; not deposited.
