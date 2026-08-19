---
title: "AV Parsing CMA - DEP-E"
generated_at: "2026-08-20"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of teacher-guided pseudo supervision and class-aware cross-modal alignment for weakly-supervised audio-visual video parsing."
source_status: "URLs only"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-08-20"
temporal_cutoff: "arXiv v1 dated 2025-09-17; repository context accessed 2026-08-20"
primary_url: "https://arxiv.org/abs/2509.14097"
stable_identifier: "arXiv:2509.14097v1"
confidence_summary: "High for source-reported method and table transcription; medium for interpretation; low for independent reproduction."
safety_scope: "Research review; synthetic and authorized evaluation examples"
distribution_notes: "Public URLs and derived Markdown only; original PDF, HTML, metadata, source package, extracted text, and caches withheld locally."
---

# AV Parsing CMA - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Local Path | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2509.14097v1 | https://arxiv.org/abs/2509.14097 | Public research record; source files withheld | 2026-08-20 | Inspected |
| S2 | arXiv full paper | Primary artifact | HTML | arXiv:2509.14097v1 | https://arxiv.org/html/2509.14097 | Public full-paper locator; source files withheld | 2026-08-20 | Inspected |
| S3 | arXiv PDF | Primary artifact | PDF | arXiv:2509.14097v1 | https://arxiv.org/pdf/2509.14097 | Public PDF locator; local copy withheld | 2026-08-20 | Verified locally |
| S4 | Private archive unit | Source-integrity evidence | PDF, HTML, metadata, JSON | arXiv:2509.14097 | Private local source; exact path withheld | Original source files remain local and were not redistributed | 2026-08-20 | Complete after bounded repair; source package unavailable |
| S5 | AV Emotion Fusion DEP | Related processed artifact | Markdown | DEP-E-20260713 | `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md` | Derived repository record | 2026-08-20 | Inspected |
| S6 | CorrKD Missing Modal DEP | Related processed artifact | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` | Derived repository record | 2026-08-20 | Inspected |
| S7 | Cued Speech MLLM Intake | Related processed artifact | Markdown | DEP-A-20260721 | `.lake-data/DEP-A/DEP-A-20260721-Cued Speech MLLM Intake/cued-speech-mllm-intake-review.md` | Derived repository record | 2026-08-20 | Inspected |

The official arXiv record lists Yaru Chen, Ruohao Guo, Liting Gao, Yang Xiang, Qingyu Luo, Zhenbo Li, and Wenwu Wang and dates the record 2025-09-17. The source unit was initially partial because its full-paper and metadata HTML were absent. A bounded brokered repair produced verified full-paper HTML and updated local provenance and verification companions; the TeX/source package was unavailable. No local source path is published here.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1 | Primary metadata | Title, authors, date, abstract, index terms, identifier | Research-object identity and high-level thesis | High | Abstract-level claims are not sufficient for empirical validation |
| E2 | S2 | Primary full paper | Introduction, problem statement, framework, EMA teacher, pseudo-mask equations, CMA equations | Problem, mechanism, and loss construction | High | No code execution in this review |
| E3 | S2 | Primary full paper | Dataset, metrics, Tables 1–3, ablation discussion, conclusion | Evaluation context, reported results, and disclosed limitation | High for transcription | No independent seeds, intervals, or rerun |
| E4 | S4 | Private source-integrity record | PDF/header/EOF, HTML size/body/marker/heading/structure checks, metadata and source status | Source completeness and locality gate | High | Private evidence is summarized without local paths or bytes |
| E5 | S5 | Related processed DEP | Audio/video/fused models, contrastive pair types, modality-value and failure analysis | Conditional-fusion synthesis | Medium | Different task, data, and model family |
| E6 | S6 | Related processed DEP | Complete-modality teacher, incomplete-modality student, relational distillation | Missing-modality synthesis | Medium | Simulated missingness and different sentiment task |
| E7 | S7 | Related processed DEP | Cue confidence, availability, alignment, provenance, privacy, and falsification framing | Accountability synthesis | Medium | Intake is derived review, not new experiment |

## Executive Summary

The paper studies weakly-supervised audio-visual video parsing (AVVP), where video-level labels must support segment-level localization of audio-only, visual-only, and audio-visual events. It proposes an EMA teacher that generates class-wise segment pseudo masks and a class-aware cross-modal agreement loss that aligns audio and visual embeddings only at confident, label-consistent segment-class pairs. The primary evidence is a complete, locally verified paper source plus the official public full-paper HTML; the source package and independent reproduction were unavailable.

The authors report strong benchmark results for E-CMANet on LLP and competitive results on UnAV-100. The evidence supports a bounded claim: selective pseudo supervision and class-aware alignment improve the reported AVVP configuration under its named datasets and metrics. The reviewer's interpretation is narrower: the mechanism is promising for confidence-gated multimodal systems, but its robustness to asynchronous, missing, shifted, or systematically miscalibrated modalities remains unestablished.

## Detailed Summary

### Problem

AVVP must identify event class and modality at each temporal segment even though training often has only video-level event labels. The source argues that propagating a video label to every segment introduces noise and that global audio-visual alignment can match unrelated events or ignore different temporal occurrence patterns.

### Framework

The framework builds on a CoLeaF-style baseline. CLAP and CLIP provide audio and visual features; a hierarchical attention network models intra- and inter-modal dependencies; multimodal multiple-instance learning pooling produces video-level predictions. The paper refers to the proposed strategy as E-CMA and labels the evaluated model E-CMANet.

### EMA-Guided Pseudo Supervision

The student is optimized by gradient descent. The teacher shares the backbone but is updated by an exponential moving average:

`theta_teacher(k) = alpha * theta_teacher(k-1) + (1 - alpha) * theta_student(k)`.

Teacher audio and visual probabilities are averaged. For each class, the paper offers adaptive thresholding based on mean confidence or top-k segment selection. The resulting binary mask gates a masked binary cross-entropy term, so uncertain segment-class positions do not contribute to the pseudo-supervision loss.

### Class-Aware Cross-Modal Agreement

The CMA loss considers a time-class pair only when both modality probabilities exceed their confidence thresholds and the video-level label marks the class as present. For each valid pair it computes audio-visual cosine similarity and averages the corresponding cosine distance. The total objective combines the standard AVVP loss, pseudo loss, and CMA loss.

### Data and Evaluation

LLP contains 11,849 ten-second videos covering 25 event categories. UnAV-100 contains 10,790 videos and more than 30,000 event instances across 100 classes. The paper reports F1 scores for audio, visual, and audio-visual events at segment and event levels; IoU above 0.5 determines a correct event, and Type@AV and Event@AV aggregate performance.

### Reported Results

On LLP, Table 1 reports E-CMANet segment-level A/V/AV scores of 66.1/69.9/61.7, Type@AV 65.9, and Event@AV 65.4. Event-level A/V/AV scores are 54.5/66.6/53.5, Type@AV is 58.2, and Event@AV is 54.3. On UnAV-100, the paper reports AV (Seg) 41.8 versus CoLeaF 41.5 and AV (Event) 47.4 versus the best listed baseline 47.8. These figures are source-reported and were not independently recomputed.

Table 3 compares the full model with variants without CMA or EMA. The paper interprets the changes as evidence that CMA and EMA contribute complementary benefits. The table supports component sensitivity under one protocol; it does not by itself establish causal generality across seeds, data distributions, or matched compute budgets.

### Limitations

The conclusion states that fixed threshold/top-k pseudo-label policies may not adapt to varying event distributions. Additional reviewer-identified limits are the risk of teacher error reinforcement, unspecified sensitivity to threshold and top-k choices, no independent execution in this review, no reported calibration or uncertainty intervals, and no demonstrated behavior under naturally missing or contradictory streams.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | AVVP must infer segment-level modality and class events from weak video-level labels. | Author problem claim | E1, E2 | Directly supported by the problem statement and introduction. | High |
| C2 | EMA-guided pseudo masks provide selective temporal supervision. | Author method claim | E2 | Equations and method description support the mechanism; reliability is an empirical hypothesis. | High for mechanism; medium for benefit |
| C3 | CMA aligns only confident, label-consistent segment-class pairs. | Author method claim | E2 | Directly supported by the valid-pair conditions and cosine-distance loss. | High |
| C4 | E-CMANet reports the listed LLP and UnAV-100 results. | Author empirical claim | E3 | Tables support transcription; no independent reproduction was performed. | High for reporting; low for independent validity |
| C5 | Selective alignment is a better deployment default than unconditional fusion. | Reviewer interpretation | E3, E5, E6, E7 | Conceptually supported by cross-source failure patterns; not proven as a universal rule. | Medium |
| C6 | Modality state and provenance should accompany multimodal outputs. | Derived inference | E5-E7 | Useful implementation synthesis, not a direct claim of the paper. | Medium |

## Methodology

- `Research objective`: Preserve a source-grounded review of one randomly selected eligible arXiv paper, connect it to exactly three related DEP entries, and produce a stable DEP-E manuscript without redistributing source files.
- `Sources inspected`: Private local archive unit containing the repaired PDF, full-paper HTML, metadata HTML, README, provenance, verification, and acquisition receipt; official arXiv metadata and full-paper HTML; live Black Lake READMEs; live Black-Lake-Data README; and the three related Black Lake Markdown entries.
- `Discovery strategy`: `rg --files -g "*.pdf"` enumerated the local archive; parent directories were collapsed to paper units; uniform PowerShell `Get-Random` selected zero-based index 2,973; public arXiv pages verified identity and full text; repository search checked related artifacts and duplicate markers.
- `Inclusion criteria`: Primary source sections covering identity, problem, method, data, experiments, results, ablations, and limitations; related entries with concrete overlap in audiovisual fusion, teacher/student distillation, missing-modality behavior, or modality accountability.
- `Exclusion criteria`: Duplicate or recent-marker papers, abstract-only evidence, inaccessible or invalid full-paper source, unsupported code or DOI claims, local system details, raw source redistribution, and unrelated DEP entries.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/ethics, and replication-oriented review.
- `Evidence handling`: Evidence IDs separate metadata, method, results, source-integrity, related DEP, reviewer interpretation, and derived implementation ideas. Quantitative results are labeled source-reported.
- `Uncertainty handling`: Missing source package, absent independent execution, fixed pseudo-mask policies, unreported calibration/intervals, and cross-domain limits are retained as explicit gaps.
- `Extraction process`: The official full-paper HTML was inspected by heading, paragraph, equation, table, and conclusion structure; the local PDF and HTML integrity gates were checked independently. No source bytes or extracted text were copied into the public repository.
- `Version control`: Paper pinned to arXiv:2509.14097v1 as represented by the 2025-09-17 official record; repository context was read from live default-branch files.
- `Random selection and eligibility`: 75,967 PDF candidates, 75,964 unique parent units, selected zero-based index 2,973, duplicate exclusions 0, and reselections 0. The 2026-08-19 date-only 24-hour cutoff was applied. The first unit was partial and became complete after one bounded repair.

## Scope, Constraints, and Assumptions

- `Scope`: The selected paper's AVVP problem, EMA pseudo supervision, CMA alignment, reported benchmark evidence, limitations, implementation relevance, and synthesis with the three specified DEP entries.
- `Temporal boundary`: Official arXiv record dated 2025-09-17 and repository context accessed 2026-08-20.
- `Evidence limits`: No source package, code execution, dataset access, independent reproduction, seed replication, calibration study, or natural-missingness evaluation was available for this artifact.
- `Assumptions`: The official arXiv full-paper HTML and the repaired local source unit represent the same paper version; source-reported tables are transcribed accurately when they agree across inspected views.
- `Constraints`: Public output must not expose local paths, machine or user identifiers, exact local execution times, source bytes, private caches, or sensitive audiovisual data. Implementation examples use synthetic arrays only.
- `Out of scope`: Deployment approval, claims of production readiness, reimplementation of the benchmark, dataset redistribution, or statistical reanalysis beyond the paper's tables.
- `Intended use`: DEP-E research preservation, follow-on review, safe implementation planning, and hypothesis generation.
- `Audience`: Research engineers, multimodal-learning reviewers, repository maintainers, and future automation agents.
- `Reproducibility boundary`: A later reviewer can locate the public paper and reconstruct the conceptual method, but cannot reproduce the tables from this DEP alone.
- `Data sensitivity`: The research concerns audiovisual recordings; raw media, labels, and derived embeddings should be treated as potentially sensitive and remain outside the public DEP.

## Observations

- `Observed pattern`: The paper's main mechanism is a pair of gates—teacher-derived temporal confidence and class-aware cross-modal agreement—rather than unrestricted fusion.
- `Technical implication`: The valid-pair set is an implicit data-selection policy. Its size, class distribution, and temporal concentration should be monitored as first-class training telemetry.
- `Contradiction or tension`: CMA is intended to suppress false cross-modal matches, but an overconfident teacher can remove useful hard examples or reinforce a systematic mismatch.
- `Cross-source pattern`: AV Emotion Fusion shows that fusion value can change with label set and input quality; CorrKD shows that teacher privilege changes under missingness; Cued Speech emphasizes that modality state and provenance need to remain visible.
- `Open question`: Whether confidence-gated alignment transfers to natural asynchronous audio, occluded video, and event-frequency shifts is not established.

## Considerations

Multimodal systems should report modality-specific scores and disagreement rather than only a fused decision. A parser that sees audio from outside the camera field of view may be correct for audio-only events while being misleading for visual localization; CMA's same-time, same-class gate addresses part of this issue but does not remove sensor geometry or clock drift.

Operational use would require threshold calibration, teacher/student versioning, monitoring of the selected-pair rate, fallback behavior when a modality is missing, and an abstention path when modalities conflict. Privacy review is required for raw audiovisual inputs and any hosted feature extractor. Aggregate F1 cannot establish fairness, consent, or safe downstream action.

## Strengths

- The problem statement clearly identifies the mismatch between weak video labels and segment-level evaluation.
- The teacher update and pseudo-mask construction are explicit enough to explain the intended mechanism.
- CMA uses class and temporal confidence conditions, which makes the alignment target more inspectable than global similarity.
- Tables include both segment and event metrics plus ablations for EMA and CMA.
- The paper names a meaningful limitation: fixed pseudo-label selection may not adapt to event distributions.

## Weaknesses

- The source does not establish independent reproducibility, because code execution, dataset access, and seed-level reruns were outside this review.
- The fixed threshold/top-k choices may bias which segment-class pairs receive supervision, yet the evidence does not quantify pair-selection coverage or calibration.
- The teacher's confidence is treated as a reliability signal without a reported calibration or error-propagation analysis.
- The UnAV-100 event result is competitive rather than best among the listed baselines, so the SOTA framing should remain metric-specific.
- The method's behavior under missing, asynchronous, or adversarially contradictory modalities is not tested in the inspected evidence.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Report selected-pair coverage and calibration | Supervision quality | Mask density can vary by class and training stage | Detect silent class starvation or error reinforcement | Additional logging and calibration data | Reliability diagrams, per-class coverage, abstention curves |
| Add uncertainty-aware teacher gating | Pseudo labels | EMA stability does not guarantee correctness | Reduce confirmation bias | More estimators or held-out calibration | Compare fixed, adaptive, top-k, and uncertainty gates across seeds |
| Evaluate natural and synthetic missingness | Robustness | Benchmarks may not reflect sensor failure | Establish graceful degradation | Additional authorized data conditions | Stream masking, temporal offset, noise, and conflict tests |
| Match compute and tuning budgets | Comparative validity | Module gains may include extra optimization capacity | Make ablation claims more credible | More runs | Pre-registered budgets, repeated seeds, confidence intervals |

## Potential Implementations

1. `User`: AV event-detection researchers. `Goal`: improve segment localization under weak labels. `Core mechanism`: EMA teacher, class-wise pseudo masks, and CMA on qualified segment-class pairs. `Required inputs`: authorized synchronized feature sequences and video-level labels. `Outputs`: segment/event predictions, pair-selection telemetry, calibration report. `Risk controls`: synthetic corruption tests, privacy-preserving feature handling, abstention, and no raw-media logging. `Evaluation`: per-class segment/event F1, coverage, calibration, shuffled-pair controls, and repeated seeds.
2. `User`: Multimodal platform engineers. `Goal`: preserve useful predictions when audio or video is missing or degraded. `Core mechanism`: complete-stream teacher and incomplete-stream student with confidence-qualified relational transfer. `Required inputs`: authorized multimodal features, missingness masks, teacher outputs, and versioned policies. `Outputs`: single-stream/fused predictions and fallback reason. `Risk controls`: no silent zero-fill without training coverage, explicit modality state, and conservative abstention. `Evaluation`: complete, missing, asynchronous, and conflict conditions with matched budgets.
3. `User`: Research-ops and safety reviewers. `Goal`: make multimodal decisions auditable. `Core mechanism`: evidence card recording availability, alignment, confidence, selected pairs, disagreement, model version, and decision. `Required inputs`: de-identified prediction rows and immutable configuration identifiers. `Outputs`: signed review record and downstream gate. `Risk controls`: redact raw media and reversible identifiers; require human approval for high-impact actions. `Evaluation`: trace completeness, reproducibility of decisions, and reviewer agreement.

## Three Ways to Exercise This Research

1. **Synthetic pair-selection test**: Generate paired audio/visual score tensors with known class and time matches; compare global alignment with CMA-style qualified pairs; success is correct selection and stable loss under injected conflict; stop if the test requires real media.
2. **Authorized missing-modality stress test**: Run a local toy parser on public or synthetic features with masked streams, temporal offsets, and noise; success is a documented degradation curve and abstention behavior; stop when data authorization or split integrity is unclear.
3. **Reproduction-planning audit**: Build a checklist from the public paper for datasets, feature extractors, thresholds, seeds, metrics, and hardware; success is an auditable gap list rather than a claimed reproduction; stop before downloading restricted data or models.

## Example MVP Product

- `Product name`: AV Evidence Card
- `Target user`: Teams reviewing multimodal event-detection experiments.
- `Problem`: A fused event score does not show which modality, segment, class, or confidence gate supported it.
- `Core workflow`: Ingest de-identified prediction rows; validate configuration and time alignment; compute qualified-pair and disagreement fields; generate audio-only, visual-only, fused, and abstain outcomes; export a signed Markdown/JSON evidence card.
- `Data requirements`: Synthetic or authorized feature scores, video-level labels, modality-availability flags, alignment metadata, model/version hashes, threshold policy, and non-reversible study IDs.
- `Architecture`: Local-only validator and metrics layer, deterministic qualified-pair calculator, policy-controlled fusion gate, append-only evidence writer, and human-review surface.
- `Success metrics`: 100% required-field completeness on test fixtures; deterministic replay of decisions; per-class pair coverage; calibration error; conflict detection rate; and no raw media in outputs.
- `Risk controls`: local processing by default, schema validation, redaction, explicit abstention, version pinning, audit logs without secrets, and human approval for consequential actions.
- `Limitations`: It audits supplied evidence but cannot prove dataset consent, label validity, model fairness, causal correctness, or deployment safety.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| AV Emotion Fusion DEP | Related Black Lake artifact | Direct audiovisual fusion, contrastive pairing, modality-specific failure, and evaluation caveats | `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md`; [arXiv:2006.08129](https://arxiv.org/abs/2006.08129) |
| CorrKD Missing Modal DEP | Related Black Lake artifact | Teacher/student transfer under incomplete modalities and relational distillation | `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md`; [arXiv:2404.16456](https://arxiv.org/abs/2404.16456) |
| Cued Speech MLLM Intake | Related Black Lake artifact | Modality confidence, availability, alignment, provenance, privacy, and falsification framing | `.lake-data/DEP-A/DEP-A-20260721-Cued Speech MLLM Intake/cued-speech-mllm-intake-review.md`; [arXiv:2503.21785](https://arxiv.org/abs/2503.21785) |

The primary source remains [arXiv:2509.14097](https://arxiv.org/abs/2509.14097). The three related entries are conceptual neighbors, not independent validation of E-CMANet.

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2509.14097 | Identity, authors, date, abstract, index terms | 2026-08-20 | Primary metadata |
| R2 | https://arxiv.org/html/2509.14097 | Method, equations, data, metrics, tables, ablations, conclusion | 2026-08-20 | Primary full paper |
| R3 | https://arxiv.org/pdf/2509.14097 | Public PDF locator and source identity cross-check | 2026-08-20 | Local copy withheld |
| R4 | Private local source unit (path withheld) | PDF/full-paper HTML/metadata integrity and repair status | 2026-08-20 | Source files and caches withheld |
| R5 | `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md` | Fusion and modality-value synthesis | 2026-08-20 | Related processed DEP |
| R6 | `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` | Teacher/student and incomplete-modality synthesis | 2026-08-20 | Related processed DEP |
| R7 | `.lake-data/DEP-A/DEP-A-20260721-Cued Speech MLLM Intake/cued-speech-mllm-intake-review.md` | Modality accountability synthesis | 2026-08-20 | Related processed DEP |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository layout and source policy | 2026-08-20 | Live authority README |
| R9 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication index | 2026-08-20 | Live authority README |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.logs/README.md | Public-safe log convention | 2026-08-20 | Live authority README |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.reports/README.md | Report-Mark placement | 2026-08-20 | Live authority README |
| R12 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related raw-data repository policy | 2026-08-20 | Read for context; no raw source copied |

## Appendix

### Selection and Deduplication Record

- Candidate enumeration: `rg --files -g "*.pdf"`.
- Candidate PDFs: 75,967.
- Unique parent-directory units: 75,964.
- Selected zero-based index: 2,973.
- Selected identifier: arXiv:2509.14097.
- Dedup scan locations: repository `.logs`, `.reports`, `.lake-data`, automation memory, and relevant Black-Lake-Data search context.
- Duplicate exclusions: 0.
- Reselections: 0.
- Date-only 24-hour cutoff: 2026-08-19.

### Source-Integrity Gate

- Initial state: `partial` — valid PDF present; metadata HTML and full-paper HTML absent.
- Repair: one bounded brokered single-paper repair; valid PDF preserved.
- PDF gate: 6,861,613 bytes, `%PDF-1.7` header, trailing `%%EOF`.
- Full-paper HTML gate: 143,386 bytes, 31,911 body characters after local tag/script/style removal, article marker present, 33 heading markers, and six paper-structure terms detected.
- Metadata HTML: present and non-empty.
- Source package: unavailable; no source archive was uploaded.
- Partial files after repair: none.

### Public-Output Gate

Only generated Markdown artifacts and the required publication-index row are eligible for staging. Original PDF, HTML, metadata, source package, extracted text, caches, local paths, machine information, usernames, local timezone labels, and exact local execution timestamps are prohibited from the staged set.

## Attribution Block

- Source URL: https://arxiv.org/abs/2509.14097 — primary metadata and paper identity.
- Source URL: https://arxiv.org/html/2509.14097 — primary full-paper evidence.
- Source URL: https://arxiv.org/pdf/2509.14097 — primary PDF locator; source file withheld.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md — repository authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md — DEP-E filing and index authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.logs/README.md — log authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.reports/README.md — report authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md — related repository authority.
- Repository file: `.lake-data/DEP-E/DEP-E-20260713-AV Emotion Fusion/av_emotion_fusion_manuscript.md` — related fusion evidence.
- Repository file: `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` — related missing-modality evidence.
- Repository file: `.lake-data/DEP-A/DEP-A-20260721-Cued Speech MLLM Intake/cued-speech-mllm-intake-review.md` — related modality-accountability evidence.
- Source URL: https://arxiv.org/abs/2006.08129 — primary paper cited by AV Emotion Fusion.
- Source URL: https://arxiv.org/abs/2404.16456 — primary paper cited by CorrKD Missing Modal.
- Source URL: https://arxiv.org/abs/2503.21785 — primary paper cited by Cued Speech MLLM Intake.
