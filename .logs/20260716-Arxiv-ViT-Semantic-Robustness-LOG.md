# Arxiv DEP Job Log: ViT Semantic Robustness

## Public-Safe Run Summary

- Deposit date: 2026-07-16
- Selected paper: arXiv:2507.01788v2, *Are Vision Transformer Representations Semantically Meaningful? A Case Study in Medical Imaging*
- Selection: accepted on the first uniform draw
- Source integrity: initial `partial`, repaired to verified `complete`
- Source policy: PDF, full-paper HTML, metadata HTML, cache, and extracted text remain local; none are deposited
- Extraction cache: initial miss; final `cached`

## Random Selection

- Enumeration: `rg --files -g "*.pdf"`
- PDFs / unique parent units: 75,777 / 75,776
- Sampling: PowerShell `Get-Random` over the sorted unique unit list
- Zero-based index: 30,086
- Exclusions: 0
- Reselections: 0

## Dedup Validation

No matching arXiv ID, DOI, normalized title, slug, Arxiv DEP log, Report-Mark, DEP-E manuscript, dedup pointer, automation-memory entry, or 24-hour same-paper marker was found. Companion-repository results were unrelated metadata rows returned by broad title terms; none represented this paper.

## Source Integrity and Cache

- PDF: 2,364,756 bytes with `%PDF-` header and trailing `%%EOF`
- Initial full-paper HTML: missing; official arXiv HTML returned 404
- Repair: approved ar5iv full-paper fallback plus official arXiv metadata, each fetched once
- Full HTML: 100,911 bytes; 26,427 body characters; one document marker; 31 heading/section markers; five structure terms
- Metadata: 42,666 bytes; metadata only
- Source package: not collected; partial files: 0
- Cache: 0.512-second missing-only backfill via `pypdf` and `html-regex`
- Cache text: PDF 36,652 bytes; HTML 30,928 bytes; source absent

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md` - anatomy- and disease-aware structure, longitudinal grounding, and clinically meaningful robustness criteria.
2. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` - subtle image manipulation, semantic versus low-level evidence, calibration, and fixed-denominator failure accounting.
3. `.lake-data/DEP-E/DEP-E-20260715-AFIDAF Vision Filters/afidaf_vision_filters_manuscript.md` - ViT representation design, attention alternatives, efficiency claims, and corruption/robustness audit requirements.

## Output Paths

- `.logs/20260716-Arxiv-ViT-Semantic-Robustness-LOG.md`
- `.logs/20260716-Arxiv-ViT-Semantic-Robustness-PHASE-LOG.md`
- `.reports/BL-Arxiv-ViT-Semantic-Robustness-20260716/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/README.md`
- `.lake-data/DEP-E/DEP-E-20260716-ViT Semantic Robustness/vit_semantic_robustness_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Next-Review Questions

1. Do PRM vulnerabilities persist under black-box transfer, realistic acquisition variation, held-out institutions/devices, and clinically reviewed imperceptibility constraints?
2. Which training objectives or architectural controls improve representation stability and class distinctiveness without degrading diagnostic utility or subgroup performance?
3. Can representation-sensitivity monitoring provide calibrated abstention and evidence for clinicians rather than a brittle binary manipulation alarm?

## Challenges

1. “Semantically meaningful” is operationalized through perturbation stability and target-class distinctiveness, not direct alignment with clinician-defined concepts.
2. Model- and dataset-agnostic language is stronger than evidence from two architecture families and four retinal/MedMNIST datasets.
3. The proposed Gaussian-noise detector is described qualitatively without a full detection table, calibration curve, adaptive evaluation, or clinical workflow study.

## Known Shortfalls

- PRM code, exact run configurations, checkpoints, seeds, and optimized images were not released through the inspected record.
- The cited MIL-VT baseline repository has legacy dependencies and no visible license; it was inspected but not executed.
- No clinician reader study, external-site validation, subgroup analysis, black-box attack, natural-corruption comparison, or prospective safety study was found.
- Local archive record updates encountered a permission-review delay; the validated source files were preserved and review remained closed until all records passed.

## Submission Record

- Primary artifact commit: https://github.com/Delphoa/Black-Lake/commit/43e3cc45702635c4511732a70727cc6610c4be66
- Slack notification: https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1784211765419799
- Source-upload gate: passed with exactly seven public-safe Markdown/JSON files and zero source or medical-image artifacts
- Submission status: direct default-branch push succeeded; Slack notice delivered
