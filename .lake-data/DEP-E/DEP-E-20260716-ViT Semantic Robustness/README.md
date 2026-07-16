# DEP-E-20260716-ViT Semantic Robustness

#vision-transformer #medical-imaging #representation-robustness #adversarial-evaluation #clinical-ai #interpretability

This public-safe DEP-E entry reviews Projected Representation Matching as a probe of medical ViT embedding stability and distinctiveness. Original paper documents, images, cache text, and archive records remain local and are not deposited.

## Contents

- `README.md` - deposit context, inventory, relevance, and attribution.
- `vit_semantic_robustness_manuscript.md` - schema-complete source-grounded research manuscript.

## Summary of Items

- The README defines public-safe scope and source withholding.
- The manuscript reconstructs PRM, reported accuracy/quality/embedding results, mitigation claims, limitations, and implementation-oriented safety implications.

## Insights and Relevance

The paper demonstrates that high clean accuracy does not establish a clinically meaningful internal geometry: bounded pixel changes can move embeddings toward another class and collapse downstream performance. Its evidence motivates representation-level robustness tests, but not a universal claim that ViTs lack semantics. Black Lake's related records add three missing dimensions: clinically structured grounding, manipulation-detection measurement, and architecture-level robustness accounting.

## Attribution Block

- Source URL: https://arxiv.org/abs/2507.01788v2
  - Applies to: `vit_semantic_robustness_manuscript.md`
  - Notes: Canonical metadata, authors, version, DOI, subjects, and license.
- Source URL: https://arxiv.org/pdf/2507.01788
  - Applies to: `vit_semantic_robustness_manuscript.md`
  - Notes: Complete PDF inspected locally and withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/2507.01788
  - Applies to: `vit_semantic_robustness_manuscript.md`
  - Notes: Approved full-paper HTML fallback after official arXiv HTML returned 404; local copy withheld.
- Source URL: https://doi.org/10.48550/arXiv.2507.01788
  - Applies to: `vit_semantic_robustness_manuscript.md`
  - Notes: arXiv-issued DOI.
- Source URL: https://github.com/greentreeys/MIL-VT
  - Applies to: `vit_semantic_robustness_manuscript.md`
  - Notes: Paper-linked baseline model repository; inspected but not executed; no visible license.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA/medical_diff_vqa_manuscript.md
  - Applies to: `vit_semantic_robustness_manuscript.md`
  - Notes: Related clinically structured representation and grounding evidence.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Document%20Fraud%20LLM/document_fraud_llm_manuscript.md
  - Applies to: `vit_semantic_robustness_manuscript.md`
  - Notes: Related subtle-manipulation detection and evaluation evidence.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-AFIDAF%20Vision%20Filters/afidaf_vision_filters_manuscript.md
  - Applies to: `vit_semantic_robustness_manuscript.md`
  - Notes: Related ViT architecture and robustness-audit evidence.
