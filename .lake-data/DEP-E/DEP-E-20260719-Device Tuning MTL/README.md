# DEP-E-20260719-Device Tuning MTL

#computer-vision #vision-transformer #edge-cloud #on-device-ai #multi-task-learning #token-compression #efficient-inference #research-review

- DEP class: DEP-E.
- Deposition date: 2026-07-19.
- Subject title: Device Tuning for Multi-Task Large Model.
- Public-safe context: Source-first review of arXiv:2302.10820v1, the official DAI 2023 accepted-paper record, focused implementation availability, successor-publication context, and exactly three related Black Lake DEPs. The verified PDF, full-paper and metadata HTML, TeX/source, extracted text, cache, and integrity records remain local and withheld; temporary review renderings were removed after inspection.
- Source policy: No `.source/` directory was created. No original source file is included or authorized for upload.

## Contents

- `README.md`
  - DEP inventory, public-safe context, source policy, item summaries, research relevance, and complete attribution.
- `device_tuning_mtl_manuscript.md`
  - Schema-complete review of the device-encoder/cloud-decoder architecture, token pooling, ImageNet evidence, missing multi-task/system measurements, implementation paths, and reproducibility boundary.

## Summary of Items

`device_tuning_mtl_manuscript.md` reconstructs a device/cloud transformer sketch in which a device encoder pools a token sequence, continues attention and feed-forward processing on the shorter representation, and passes the result to a cloud decoder. The introduction also claims shared cloud parameters, task-specific device parameters, and gradient-normalized multi-task training, but those components are not defined or evaluated in the method section.

The empirical evidence is limited to two ImageNet-1k top-1/parameter tables. The strongest clean comparison is the proposed 2.2M-parameter model at 70.6% top-1 versus MobileNetV2 at 2.6M and 69.8%. The paper supplies no task inventory, multi-task results, training recipe, pooling/split ablation, FLOPs, latency, memory, energy, bandwidth, serialized payload, or official implementation. The manuscript therefore treats the work as a promising compact-classifier/split-architecture hypothesis rather than a demonstrated multi-task or systems-efficiency result.

## Insights and Relevance

The durable idea is not simply to “halve tokens,” but to treat the device/cloud boundary as an auditable information contract. Edge Cloud Split shows the need for device-profile, bandwidth, latency, and privacy evidence; K-Token Merging shows that reduced sequence length must be evaluated as a quality/resource frontier; DMNN Conditional Paths shows why parameter/FLOP savings must not be mistaken for device runtime gains. A credible successor to Device Tuning would unite those lessons with explicit multi-task interference measurements, fixed-denominator failures, and an end-to-end cost ledger.

No source file was uploaded. Public arXiv, workshop, successor, and repository URLs below provide traceability while all source documents and derivatives remain withheld locally.

## Attribution Block

- Source URL: https://arxiv.org/abs/2302.10820
  - Applies to: `device_tuning_mtl_manuscript.md`.
  - Notes: Primary title, authors, submission/version, subject, license, abstract, venue note, and arXiv DOI; abstract alone was not used for detailed claims.
- Source URL: https://arxiv.org/pdf/2302.10820
  - Applies to: `device_tuning_mtl_manuscript.md`.
  - Notes: Complete paper, figures, equations, tables, and references; downloaded file remained local.
- Source URL: https://ar5iv.labs.arxiv.org/html/2302.10820
  - Applies to: `device_tuning_mtl_manuscript.md`.
  - Notes: Approved full-paper HTML fallback used after official arXiv HTML was unavailable; downloaded file remained local.
- Source URL: https://arxiv.org/e-print/2302.10820
  - Applies to: `device_tuning_mtl_manuscript.md`.
  - Notes: TeX/source used to verify equations, table values, and omitted method details; archive remained local.
- Source URL: https://doi.org/10.48550/arXiv.2302.10820
  - Applies to: `device_tuning_mtl_manuscript.md`.
  - Notes: arXiv-issued DOI identity.
- Source URL: https://sites.google.com/view/dai-2023/accepted-papers
  - Applies to: `device_tuning_mtl_manuscript.md`.
  - Notes: Official DAI 2023 accepted-paper list.
- Source URL: https://openaccess.thecvf.com/content/CVPR2023W/MobileAI/html/Jiang_High-Efficiency_Device-Cloud_Collaborative_Transformer_Model_CVPRW_2023_paper.html
  - Applies to: `device_tuning_mtl_manuscript.md` related reading.
  - Notes: Later device/cloud transformer paper by overlapping authors; treated as successor context, not selected-paper evidence.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md` and `device_tuning_mtl_manuscript.md`.
  - Notes: Live repository filing, attribution, source-locality, and submission authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md` and `device_tuning_mtl_manuscript.md`.
  - Notes: Live DEP-E container and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `device_tuning_mtl_manuscript.md`.
  - Notes: Related-repository authority inspected for dedup validation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260719-Edge%20Cloud%20Split/2607.13093-whitepaper-review.md
  - Applies to: `device_tuning_mtl_manuscript.md`.
  - Notes: Related DEP source for edge/cloud split, latency, bandwidth, and privacy boundaries.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260716-K%20Token%20Merging/2604.15153-whitepaper-review.md
  - Applies to: `device_tuning_mtl_manuscript.md`.
  - Notes: Related DEP source for sequence compression and quality/resource frontiers.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-DMNN%20Conditional%20Paths/dmnn_conditional_paths_manuscript.md
  - Applies to: `device_tuning_mtl_manuscript.md`.
  - Notes: Related DEP source for compact vision, conditional compute, and runtime-evidence boundaries.
- Source URL: https://arxiv.org/abs/1711.02257
  - Applies to: `device_tuning_mtl_manuscript.md` related reading.
  - Notes: GradNorm primary paper for an explicit gradient-normalization baseline absent from the selected work's method specification.
