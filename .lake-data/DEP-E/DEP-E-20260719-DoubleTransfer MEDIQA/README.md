# DEP-E-20260719-DoubleTransfer MEDIQA

#medical-nlp #transfer-learning #multi-task-learning #ensembles #question-answering #domain-adaptation

This DEP-E preserves a source-grounded review of *DoubleTransfer at MEDIQA 2019: Multi-Source Transfer Learning for Natural Language Understanding in the Medical Domain*. It reconstructs the bounded external-task sampling, multi-task fine-tuning, task-specific adaptation, and heterogeneous ensemble strategy; checks the reported leaderboard and ensemble arithmetic; and translates the evidence into modern medical-NLU evaluation requirements. The public artifact uses canonical URLs and repository-relative references only. All source documents and inspection material were withheld locally.

## Contents

- `README.md` - deposition inventory, item summary, relevance notes, and final source attribution.
- `doubletransfer_mediqa_manuscript.md` - schema-complete manuscript review with evidence ledger, quantitative critique, exactly three exercise paths, implementation guidance, and replication appendix.

No `.source/` directory is present. PDFs, full-paper HTML, metadata HTML, source archives, extracted text, caches, verification records, and rendered pages remain local and were not uploaded.

## Summary of Items

`doubletransfer_mediqa_manuscript.md` reviews the 2019 BioNLP system paper at full-paper depth. It preserves the MEDIQA task framing, mixture-ratio algorithm, datasets, objectives, task-specific preprocessing, hyperparameters, ensemble decision rules, leaderboard results, and component-code context. It distinguishes source claims from reviewer interpretation, records a table/prose inconsistency in the multi-source ensemble claim, documents the repaired source-integrity gate and random-selection/dedup method, and connects the paper to exactly three related Black Lake entries.

## Insights and Relevance

The durable contribution is a transfer contract: combine sources only when each has a stated role, constrain how external supervision enters training, and test whether heterogeneity adds incremental value at matched ensemble size and compute. The related DEPs sharpen that contract. AV Emotion Fusion shows that another modality can help one task slice and harm another; Pixel-Point Transfer makes the adapter and transfer channel inspectable; Medical Diff VQA adds medical-data lineage, leakage, calibration, and non-diagnostic boundaries. A modern implementation should therefore publish source/split manifests, matched ablations, seed-level uncertainty, calibration, worst-slice results, latency, and abstention behavior before claiming useful medical-domain transfer.

## Attribution Block

- Source URL: https://arxiv.org/abs/1906.04382v1
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Canonical arXiv metadata and version record.
- Source URL: https://arxiv.org/pdf/1906.04382
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Primary 7-page v1 paper inspected locally; no PDF redistributed.
- Source URL: https://ar5iv.labs.arxiv.org/html/1906.04382
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Approved full-paper HTML fallback used after official arXiv HTML returned 404; no HTML redistributed.
- Source URL: https://arxiv.org/e-print/1906.04382
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: TeX/source package inspected locally; no source archive redistributed.
- Source URL: https://doi.org/10.48550/arXiv.1906.04382
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: arXiv-issued persistent identifier.
- Source URL: https://aclanthology.org/W19-5042/
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Official ACL publication record and DOI 10.18653/v1/W19-5042.
- Source URL: https://doi.org/10.18653/v1/W19-5042
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Persistent ACL publication identifier.
- Source URL: https://aclanthology.org/W19-5039/
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Official MEDIQA 2019 shared-task context.
- Source URL: https://aclanthology.org/D18-1187/
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Official MedNLI publication record and clinical-domain transfer background.
- Source URL: https://github.com/namisan/mt-dnn
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Public component repository for MT-DNN; not a paper-specific DoubleTransfer package.
- Source URL: https://github.com/allenai/scibert
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Public component repository for SciBERT; not a paper-specific DoubleTransfer package.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-AV%20Emotion%20Fusion/av_emotion_fusion_manuscript.md
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Related DEP on heterogeneous fusion and negative evidence.
- Source URL: https://arxiv.org/abs/2006.08129
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Primary source basis recorded by the AV Emotion Fusion DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Related DEP on representation transfer, adapters, and domain shift.
- Source URL: https://arxiv.org/abs/2104.04687v3
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Primary source basis recorded by the Pixel-Point Transfer DEP.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA/medical_diff_vqa_manuscript.md
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Related DEP on medical QA evidence, governance, leakage, and abstention.
- Source URL: https://arxiv.org/abs/2307.11986v2
  - Applies to: `doubletransfer_mediqa_manuscript.md`
  - Notes: Primary source basis recorded by the Medical Diff VQA DEP.
