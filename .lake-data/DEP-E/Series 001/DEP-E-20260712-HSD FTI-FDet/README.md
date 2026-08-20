# DEP-E-20260712-HSD FTI-FDet

#computer-vision #object-detection #fault-detection #knowledge-distillation #edge-ai #rail-safety #model-compression #ml-systems

Public-safe deposition context: On 2026-07-12, `Black Lake Arxiv DEP` randomly selected and reviewed arXiv:2307.00701, then synthesized it with exactly three related DEP entries. Private source locations and exact execution details are withheld. No original source file is redistributed.

## Contents

- `README.md` — DEP inventory, context, relationship summary, and source attribution.
- `hsd_fti_fdet_manuscript.md` — schema-complete, source-grounded research manuscript covering the paper, evidence, limitations, implementation paths, and cross-DEP synthesis.

## Summary of Items

- `README.md` makes the deposit auditable by enumerating every item and mapping the generated manuscript to the public sources that support it.
- `hsd_fti_fdet_manuscript.md` reviews heterogeneous self-distillation for compact freight-train braking-component detection. It preserves reported accuracy, latency, memory, model-size, dataset, ablation, and failure evidence; separates author claims from reviewer interpretation; and connects the paper to spatially structured detection, topology-aware distillation, and hardware-aware edge compression.

## Insights and Relevance

The paper's most reusable idea is that compact detection should preserve task-specific spatial and localization information rather than compress capacity indiscriminately. The related SSP DEP adds explicit spatial partitioning and boundary priors; the Tech Intel 1104 DEP adds teacher/student topology and throughput; and the Tech Intel 1311 DEP adds accelerator-aware quantization, compression, latency, and energy. The combined synthesis describes a lifecycle from information selection, through asymmetric training, to target-hardware validation. This manuscript is the durable research record; `.logs/20260712-Arxiv-HSD-FTI-FDet-LOG.md` preserves the operational selection/validation trace, and `.reports/BL-Arxiv-HSD-FTI-FDet-20260712/Report-Mark.md` preserves the detailed synthesis note and reviewer challenges.

Original source files were not collected into `.source/` because redistribution permission and downstream necessity were not established. The public arXiv, DOI, publisher, GitHub, and repository-relative references below preserve provenance.

## Attribution Block

- Source URL: https://arxiv.org/abs/2307.00701
  - Applies to: `hsd_fti_fdet_manuscript.md`
  - Notes: Primary paper metadata, abstract, authors, and submission record.
- Source URL: https://arxiv.org/html/2307.00701
  - Applies to: `hsd_fti_fdet_manuscript.md`
  - Notes: Primary full text used for methods, experiments, tables, results, and limitations.
- Source URL: https://arxiv.org/pdf/2307.00701
  - Applies to: `hsd_fti_fdet_manuscript.md`
  - Notes: Public PDF locator corresponding to the privately inspected archive copy; file not redistributed.
- Source URL: https://doi.org/10.1016/j.aei.2023.102091
  - Applies to: `hsd_fti_fdet_manuscript.md`
  - Notes: Publisher DOI and publication identity.
- Source URL: https://www.sciencedirect.com/science/article/pii/S1474034623002197
  - Applies to: `hsd_fti_fdet_manuscript.md`
  - Notes: Publisher abstract, highlights, volume, and article metadata.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`; `hsd_fti_fdet_manuscript.md`
  - Notes: Live repository authority for DEP naming, contents, attribution, and commit rules.
- Source file: `.lake-data/DEP-E/DEP-E-20260711-SSP Oriented Detection/ssp_oriented_detection_manuscript.md`
  - Applies to: `hsd_fti_fdet_manuscript.md`
  - Notes: Related processed DEP on spatially structured oriented object detection; primary basis https://arxiv.org/abs/2506.10601.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `README.md`; `hsd_fti_fdet_manuscript.md`
  - Notes: Live related-repository layout and provenance authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260629-Tech%20Intel%201104/daily_research_findings_2026-06-29_1104.md
  - Applies to: `hsd_fti_fdet_manuscript.md`
  - Notes: Related DEP finding on topology-aware knowledge distillation; primary basis https://arxiv.org/abs/2606.27797.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/.lake-data/DEP-20260711-Tech%20Intel%201311/daily_research_findings_2026-07-11_1311.md
  - Applies to: `hsd_fti_fdet_manuscript.md`
  - Notes: Related DEP findings on hardware-aware compression and edge deployment; primary bases https://arxiv.org/abs/2607.08015, https://arxiv.org/abs/2607.08029, and https://arxiv.org/abs/2607.08013.
