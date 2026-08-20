# DEP-E-20260801-CrossNER Adapt

#named-entity-recognition #domain-adaptation #low-resource-learning #benchmark-design #dataset-provenance #evaluation-governance #source-grounded-research

Deposited 2026-08-01 as a DEP-E research artifact. This entry preserves a source-grounded review of arXiv:2012.04373v2, CrossNER: Evaluating Cross-Domain Named Entity Recognition. The local paper unit passed the complete-source gate before review: the PDF was valid and the full-paper HTML was verified after one bounded repair using an approved ar5iv fallback. Public output contains derived Markdown and public source locators only. Source files, caches, extracted text, repair receipts, and local filesystem details were withheld.

## Contents

- README.md
- crossner_domain_adaptation_manuscript.md

## Summary of Items

- README.md: This public-safe DEP inventory, classification, provenance summary, and attribution record. It tells later reviewers what is present and what was intentionally withheld.
- crossner_domain_adaptation_manuscript.md: The schema-complete manuscript generated with the manuscript-research-document contract. It records the paper’s source metadata, evidence ledger, method and results, limitations, implementation implications, three related DEP entries, and the selection/integrity validation record.

## Insights and Relevance

CrossNER contributes a practical benchmark pattern: specialized entity labels, small target-domain training sets, and domain-related unlabeled corpora make cross-domain transfer failures visible. The synthesis connects that pattern to DoubleTransfer’s multi-source transfer controls, Dataset Baselines’ benchmark and provenance discipline, and OMGEval’s multilingual slice and evaluator governance. The downstream value is a reusable review contract for domain adaptation: preserve data lineage and splits, compare corpus relevance against raw scale, report specialized-label failures, and abstain outside the tested domain and language envelope.

The manuscript is the canonical research artifact for this DEP. The operational selection and validation record belongs in .logs/20260801-Arxiv-CrossNER-LOG.md, while the detailed Report-Mark belongs in .reports/BL-Arxiv-CrossNER-20260801/Report-Mark.md. Those two artifacts provide complementary operational and synthesis views without duplicating source files.

## Attribution Block

- Source URL: https://arxiv.org/abs/2012.04373
  - Applies to: README.md and crossner_domain_adaptation_manuscript.md
  - Notes: Canonical metadata, authors, dates, abstract, DOI, venue status, and public code/data locator.
- Source URL: https://arxiv.org/pdf/2012.04373
  - Applies to: crossner_domain_adaptation_manuscript.md
  - Notes: Primary PDF inspected locally; source file withheld from this public DEP.
- Source URL: https://ar5iv.labs.arxiv.org/html/2012.04373
  - Applies to: crossner_domain_adaptation_manuscript.md
  - Notes: Approved full-paper HTML fallback used after the official HTML route returned 404; local copy withheld.
- Source URL: https://github.com/zliucr/CrossNER
  - Applies to: crossner_domain_adaptation_manuscript.md
  - Notes: Official code and dataset repository; README, dependency notes, sample commands, and license visibility inspected.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-DoubleTransfer%20MEDIQA/doubletransfer_mediqa_manuscript.md
  - Applies to: crossner_domain_adaptation_manuscript.md
  - Notes: Related DEP evidence for multi-source transfer and distribution-shift controls.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260721-Dataset%20Baselines/dataset_baselines_manuscript.md
  - Applies to: crossner_domain_adaptation_manuscript.md
  - Notes: Related DEP evidence for dataset, baseline, and provenance governance.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260717-OMGEval%20Benchmark/omgeval_benchmark_manuscript.md
  - Applies to: crossner_domain_adaptation_manuscript.md
  - Notes: Related DEP evidence for multilingual benchmark slices and evaluation controls.
- Source files: verified PDF, full-paper HTML, metadata HTML, local verification records, and any extracted local material
  - Applies to: none; all were withheld locally
  - Notes: The source package was unavailable. No source files or private paths were redistributed.
