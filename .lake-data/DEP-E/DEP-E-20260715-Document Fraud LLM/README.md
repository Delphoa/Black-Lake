# DEP-E-20260715-Document Fraud LLM

#document-forensics #multimodal-llm #vision-language #fraud-detection #calibration #uncertainty #evaluation #human-review

Public-safe deposition context: on 2026-07-15, the recurring Arxiv DEP workflow uniformly selected and source-first reviewed arXiv:2508.11021v1, *Can Multi-modal (reasoning) LLMs detect document manipulation?* The source archive was repaired from partial to verified complete before synthesis. Exact local execution details and all private source locations are withheld.

Original PDFs, full-paper HTML, metadata HTML, TeX/source archives, extracted text, caches, and integrity records remain local. None was copied, staged, committed, attached, or uploaded. No `.source/` directory exists in this DEP.

## Contents

- `README.md` — DEP inventory, public-safe context, item summaries, relevance, and final source attribution.
- `document_fraud_llm_manuscript.md` — schema-complete manuscript covering the selected paper's method, evidence, limitations, implementation paths, random selection, deduplication, source-integrity validation, and exactly three related DEP bridges.

## Summary of Items

- `document_fraud_llm_manuscript.md` reconstructs the receipt-forgery benchmark across multimodal LLMs, SVM, and JPEG-forensic CNN baselines. It preserves the reported AUC table, reasoning comparison, GPT-O1 error/calibration analysis, omitted-output caveat, dataset-identity ambiguity, and arXiv text-overlap notice. It separates source claims from reviewer interpretation and proposes bounded, human-reviewed evaluation and product paths.
- `README.md` makes the deposit auditable by listing every package item, stating the no-source-upload policy, and mapping public URLs and related Black Lake artifacts to the generated manuscript.

## Insights and Relevance

The durable result is not that a general multimodal model solves document fraud. Most tested systems perform near chance, and the best reported AUC is 0.71. The useful design pattern is a layered evidence gate: specialized visual forensics detect compression or local-edit artifacts; multimodal reasoning checks arithmetic, merchant, temporal, and layout consistency; calibrated uncertainty and support telemetry determine whether a case can be accepted or must be reviewed. VLM Probing adds internal diagnostic tests, PAC Confidence adds finite-sample decision bounds, and RLMF Uncertainty prevents stated confidence from being mistaken for factual reliability. Together they turn a one-shot classifier comparison into a falsifiable, review-first evaluation architecture.

## Attribution Block

- Source URL: https://arxiv.org/abs/2508.11021
  - Applies to: `document_fraud_llm_manuscript.md`
  - Notes: Official title, author list, submission record, subjects, DOI, license locator, and administrator text-overlap notice; metadata only, not treated as the full paper.
- Source URL: https://arxiv.org/html/2508.11021
  - Applies to: `document_fraud_llm_manuscript.md`
  - Notes: Official full-paper HTML used for method, tables, results, conclusion, and appendix review; source file remains local.
- Source URL: https://arxiv.org/pdf/2508.11021
  - Applies to: `document_fraud_llm_manuscript.md`
  - Notes: Public locator for the verified PDF inspected locally; file not redistributed.
- Source URL: https://arxiv.org/e-print/2508.11021
  - Applies to: `document_fraud_llm_manuscript.md`
  - Notes: Public locator for the TeX/source package inspected locally; archive not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2508.11021
  - Applies to: `document_fraud_llm_manuscript.md`
  - Notes: Persistent arXiv-issued DOI.
- Source URL: https://creativecommons.org/licenses/by-nc-nd/4.0/
  - Applies to: `README.md`; `document_fraud_llm_manuscript.md`
  - Notes: License linked by the full-paper HTML. Original source files were withheld.
- Source URL: https://arxiv.org/abs/2503.20084
  - Applies to: `document_fraud_llm_manuscript.md`
  - Notes: Related earlier paper named by the selected arXiv record's administrator text-overlap note; used only for lineage context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-VLM%20Probing/vlm_probing_manuscript.md
  - Applies to: `document_fraud_llm_manuscript.md`
  - Notes: Related DEP on architecture-aware probing of vision-language models; primary basis arXiv:2005.07310v2.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md
  - Applies to: `document_fraud_llm_manuscript.md`
  - Notes: Related DEP on simultaneous finite-sample confidence coverage and distribution-envelope constraints; primary basis arXiv:2011.00716v5.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-RLMF%20Uncertainty/rlmf_uncertainty_manuscript.md
  - Applies to: `document_fraud_llm_manuscript.md`
  - Notes: Related DEP on factual, faithful, and expressed uncertainty; primary basis arXiv:2606.32032v1.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`; `document_fraud_llm_manuscript.md`
  - Notes: Live repository authority for DEP naming, source locality, contents, attribution, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`; `document_fraud_llm_manuscript.md`
  - Notes: Live class filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `document_fraud_llm_manuscript.md`
  - Notes: Live companion-repository context used for deduplication and provenance policy.
