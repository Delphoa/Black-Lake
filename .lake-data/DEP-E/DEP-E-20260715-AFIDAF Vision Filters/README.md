# DEP-E-20260715-AFIDAF Vision Filters

#computer-vision #fourier-filters #lightweight-models #attention-alternatives #image-classification #object-detection #semantic-segmentation #model-compression #research-review

Deposition context: date-only 2026-07-15 recurring Arxiv DEP review; exact local execution details withheld.

This DEP-E contains a public-safe, source-grounded review of *AFIDAF: Alternating Fourier and Image Domain Adaptive Filters as an Efficient Alternative to Attention in ViTs*, arXiv:2407.12217v2. The paper proposes alternating decomposed large-kernel image filtering with adaptive Fourier-domain channel mixing, then applies the same principle to a compressed Swin-shaped hierarchy. The deposit separates source-reported evidence from reviewer interpretation and connects the work to exactly three existing Black Lake research entries.

The selected archive unit was repaired from `partial` to verified `complete` before review. The PDF, full-paper HTML, metadata HTML, source archive, extracted text, and integrity records remain local and were not copied, staged, uploaded, attached, or committed. No `.source/` directory exists in this DEP.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, relevance, and final attribution.
- `afidaf_vision_filters_manuscript.md`
  - Schema-complete DEP-E manuscript covering source metadata, evidence ledger, method, six result tables, limitations, implementation paths, exactly three exercises, an MVP, related DEP synthesis, and source references.

## Summary of Items

`afidaf_vision_filters_manuscript.md` reconstructs AFIDAF's image-domain large-kernel path, Fourier-domain channel mask, and hierarchical HAFIDAF variant. It records the paper's ImageNet-1K, COCO, and PASCAL VOC results; distinguishes parameter savings from actual FLOPs, latency, memory, and energy; documents the missing official code release; and preserves the random-selection, dedup, repair, and no-source-upload evidence.

`README.md` is the package-level map. It states the public-source policy, inventories every file in the DEP, and attributes every public URL used by the generated manuscript.

## Insights and Relevance

AFIDAF is most useful as evidence for role-separated feature mixing: spatial convolution is assigned local/high-frequency detail while Fourier filtering supplies global/non-local interaction. The reported gains over AFFNet are consistent across classification, object detection, and segmentation, but they arrive with modest parameter increases in AFIDAF itself. HAFIDAF offers stronger parameter compression, yet its ImageNet FLOPs remain close to Swin-T and its classification accuracy is lower. The practical lesson is that “attention-free” and “parameter-efficient” are hypotheses requiring device-level resource evidence, controlled ablations, and failure analysis.

The three related Black Lake entries deepen that conclusion. SSP Detection shows how explicit spatial priors can recover missing geometry; HSD FTI-FDet adds model-size, latency, memory, and field-failure evidence for compact vision; Physical Data AI shows that structured representations are only efficient when their domain assumptions hold. Together they motivate a matched Pareto benchmark rather than a parameter-count leaderboard.

## Attribution Block

- Source URL: https://arxiv.org/abs/2407.12217
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Official metadata page for title, authors, versions, subject, abstract, DOI, and license visibility; not treated as the paper document.
- Source URL: https://arxiv.org/pdf/2407.12217
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Complete PDF used locally for method, equations, figures, tables, results, and conclusion; source file withheld.
- Source URL: https://arxiv.org/html/2407.12217
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Official complete full-paper HTML used locally and withheld.
- Source URL: https://arxiv.org/e-print/2407.12217
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Official source package used locally for inventory and cross-checking; source archive withheld.
- Source URL: https://doi.org/10.48550/arXiv.2407.12217
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Persistent arXiv identifier.
- Source URL: https://link.springer.com/chapter/10.1007/978-3-031-77392-1_2
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Official publisher record for ISVC/LNCS publication metadata, pages, authors, and DOI.
- Source URL: https://doi.org/10.1007/978-3-031-77392-1_2
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Persistent DOI for the published ISVC chapter.
- Source URL: https://zsivine.github.io/research/
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Author-side publication context and code-availability check.
- Source URL: https://doi.org/10.1007/s41095-023-0364-2
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Visual Attention Network and large-kernel image-domain method context.
- Source URL: https://arxiv.org/abs/2103.14030
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Swin Transformer hierarchy used as the HAFIDAF compression baseline.
- Source URL: https://doi.org/10.1109/TPAMI.2023.3240462
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: GFNet frequency-domain visual-recognition context.
- Source URL: https://arxiv.org/abs/2307.09283
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: RepViT compact-convolution comparator context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-SSP%20Oriented%20Detection/ssp_oriented_detection_manuscript.md
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Related spatial-prior and object-detection DEP-E manuscript.
- Source URL: https://arxiv.org/abs/2506.10601
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Primary paper basis recorded for the related SSP Detection manuscript.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-HSD%20FTI-FDet/hsd_fti_fdet_manuscript.md
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Related compact visual deployment and resource-evidence DEP-E manuscript.
- Source URL: https://arxiv.org/abs/2307.00701
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Primary paper basis recorded for the related HSD FTI-FDet manuscript.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260710-Physical%20Data%20AI/physical_data_ai_manuscript.md
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Related structured-representation and parameter-efficiency DEP-E manuscript.
- Source URL: https://arxiv.org/abs/2407.14504
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Primary paper basis recorded for the related Physical Data AI manuscript.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`, `afidaf_vision_filters_manuscript.md`
  - Notes: Live target-repository deposition, attribution, naming, source-locality, and commit authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`, `afidaf_vision_filters_manuscript.md`
  - Notes: Live DEP-class filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `afidaf_vision_filters_manuscript.md`
  - Notes: Live companion-repository layout and dedup context.
