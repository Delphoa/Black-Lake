# DEP-E-20260713-AV Emotion Fusion

#multimodal-learning #emotion-recognition #audio-classification #video-classification #contrastive-learning #representation-probing #calibration #abstention #responsible-ai #arxiv

Public-safe deposition context: On 2026-07-13, `Black Lake Arxiv DEP` randomly selected and reviewed arXiv:2006.08129v1, then synthesized it with exactly three related Black Lake DEP entries. Private source locations and exact execution details are withheld. No original source file is redistributed.

## Contents

- `README.md` — DEP inventory, deposition context, item summaries, relationship notes, and source attribution.
- `av_emotion_fusion_manuscript.md` — Schema-complete manuscript reviewing the selected paper, its evidence, limitations, replication boundary, exactly three related DEP entries, and bounded implementation paths.

## Summary of Items

- `README.md` makes the DEP auditable by enumerating every item and mapping the generated manuscript to the public sources and repository artifacts that support it.
- `av_emotion_fusion_manuscript.md` reviews *Emotion Recognition in Audio and Video Using Deep Neural Networks*. It preserves the paper's architecture and preprocessing comparisons, reports the four-class and three-class results, separates source claims from reviewer interpretation, documents random selection and deduplication, and connects the work to representation probes, heterogeneous compact pathways, and finite-sample confidence gates.
- No `.source/` directory is included. A private archive PDF was inspected but not redistributed; stable public arXiv URLs provide the public counterpart. The paper-declared repository states that IEMOCAP must be requested from USC and cannot be shared by the authors.

## Insights and Relevance

The paper is most useful as evidence against assuming that additional modalities automatically improve a classifier. Its audio-video model underperforms audio-only CNN+RNN on four emotions and improves by only 1.50 percentage points after happiness is removed. The manuscript bridges that boundary with three related DEPs: VLM Probing supplies fusion and representation diagnostics; HSD FTI-FDet supplies heterogeneous, task-specific pathways and field-condition evaluation; PAC Confidence supplies interval-backed thresholding and abstention. The downstream value is an evidence gate that requires repeatable per-class fusion benefit, speaker-disjoint evaluation, calibration support, shift monitoring, and a safe fallback before a multimodal path is trusted.

The manuscript is the durable research record. `.logs/20260713-Arxiv-AV-Emotion-Fusion-LOG.md` preserves the operational selection and validation trace, while `.reports/BL-Arxiv-AV-Emotion-Fusion-20260713/Report-Mark.md` preserves the detailed synthesis note, code mock-ups, and reviewer challenges.

## Attribution Block

- Source URL: https://arxiv.org/abs/2006.08129
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Primary paper metadata, abstract, authors, submission date, and version record.
- Source URL: https://arxiv.org/html/2006.08129
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Primary public full text used for methods, data, tables, results, limitations, and conclusions.
- Source URL: https://arxiv.org/pdf/2006.08129
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Public PDF corresponding to the privately inspected archive copy; no PDF is redistributed.
- Source URL: https://github.com/julieeF/CS231N-Project
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Paper-declared code repository used to verify notebook/script availability, code-license visibility, and the IEMOCAP access boundary; code was not executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`; `av_emotion_fusion_manuscript.md`.
  - Notes: Live target-repository authority for DEP class, naming, inventory, attribution, stability, and commit rules.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Live related-repository authority used before the cross-repository duplicate search.
- Source URL: https://arxiv.org/abs/2005.07310
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Primary research basis recorded by the related VLM Probing DEP.
- Source URL: https://arxiv.org/abs/2307.00701
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Primary research basis recorded by the related HSD FTI-FDet DEP.
- Source URL: https://arxiv.org/abs/2011.00716
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Primary research basis recorded by the related PAC Confidence DEP.
- Repository source: `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Related Black Lake manuscript on multimodal representation probing, fusion, and leakage-aware evaluation.
- Repository source: `.lake-data/DEP-E/DEP-E-20260712-HSD FTI-FDet/hsd_fti_fdet_manuscript.md`
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Related Black Lake manuscript on heterogeneous self-distillation, task-specific pathways, compact inference, and field failures.
- Repository source: `.lake-data/DEP-E/DEP-E-20260713-PAC Confidence/pac_confidence_manuscript.md`
  - Applies to: `av_emotion_fusion_manuscript.md`.
  - Notes: Related Black Lake manuscript on finite-sample confidence intervals, threshold decisions, abstention, and distribution assumptions.
