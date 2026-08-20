# Arxiv DEP Log: SADD RNB

- Public-safe run date: 2026-08-03
- Selected paper: A Semi-Supervised Adaptive Discriminative Discretization Method Improving Discrimination Power of Regularized Naive Bayes
- Authors: Shihe Wang, Jianfeng Ren, and Ruibin Bai
- arXiv: 2111.10983v3
- DOI: 10.1016/j.eswa.2023.120094
- Source URL: https://arxiv.org/abs/2111.10983
- Source state: complete after repair; valid PDF and verified full-paper HTML; source files withheld locally

## Selection and Deduplication

- Enumeration method: rg --files -g "*.pdf" against the local arXiv archive root.
- PDF candidates: 75,960.
- Unique PDF-parent paper units: 75,957.
- Selection method: uniform zero-based PowerShell Get-Random index over sorted unique paper units.
- Selected index: 54,225.
- Duplicate exclusions: 0.
- Other identity or artifact exclusions: 0.
- Reselections: 0.
- Same-paper markers within the 24-hour exclusion window: 0.
- Dedup keys checked: base/versioned arXiv ID, DOI, normalized title, paper slug, prior Arxiv DEP paths, recent markers, automation memory, and relevant companion-repository entries.
- Acceptance note: the first draw was identity-eligible. The source gate required one bounded repair because full-paper HTML was initially absent.

## Source-Integrity Gate

- Initial classification: partial. The PDF was present and valid, but the unit had no full-paper HTML.
- Repair: one broker-mediated bounded acquisition preserved the PDF and added metadata HTML plus an approved ar5iv full-paper HTML fallback after official arXiv HTML routes returned 404.
- Final PDF checks: 782,656 bytes, %PDF- header, trailing %%EOF.
- Final full-paper HTML checks: 703,223 bytes, 82,918 body characters after script/style removal, article/main/LaTeXML markers, 53 heading markers, and 7 paper-structure term classes.
- Partial-transfer files: none.
- Source package: unavailable through the broker redirect policy; nonblocking because PDF and full-paper HTML passed.
- Local records updated: archive README, machine-readable summary, provenance record, verification report, and immutable acquisition receipt.
- Public-source rule: the abstract page was used for metadata only; the full-paper HTML was the review document.
- Source upload gate: passed. No PDF, HTML, abstract page, source archive, cache, extracted text, verification record, or local archive reference is included in public output.

## Review and Synthesis

- Reviewed problem, SADD method, pseudo-labeling, adaptive threshold, RNB+ integration, experimental protocol, tables, significance tests, semi-supervised setting, limitations, publisher record, and license metadata.
- Core evidence: 31 UCI datasets; stratified 10-fold cross-validation; reported average SADD accuracy 82.07 versus 78.96 for MDLP; reported semi-supervised average 80.83 versus 77.28 for MDLP; source-reported gains are not independently reproduced.
- Key caution: the paper describes deriving discretization from unlabeled testing data in its main framework, which is transductive and must be separated from strict inductive evaluation.
- Official code: no public implementation was established in the inspected sources; the paper describes MATLAB and KEEL components.

## Related DEP Entries

1. [Decentralized SSL](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-Decentralized%20SSL/decentralized_ssl_manuscript.md) — unlabeled-data utilization, pseudo-label-adjacent representation exchange, and privacy limits.
2. [Adversarial Label Noise](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md) — soft targets, label-distribution mismatch, and calibration boundaries.
3. [DUET Setwise CTR](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-DUET%20Setwise%20CTR/duet_setwise_ctr_manuscript.md) — peer-generated labels, disagreement monitoring, and deployment gating.

## Public Outputs

- .logs/20260803-Arxiv-SADD-RNB-LOG.md
- .reports/BL-Arxiv-SADD-RNB-20260803/Report-Mark.md
- .lake-data/DEP-E/DEP-E-20260803-SADD RNB/README.md
- .lake-data/DEP-E/DEP-E-20260803-SADD RNB/sadd_rnb_manuscript.md
- .lake-data/DEP-E/.index/pubs-index.md

## Exactly Three Next-Review Questions

1. Does a strict inductive protocol that learns all cut points from training data alone preserve the reported SADD advantage?
2. How do pseudo-label confidence filtering and abstention change accuracy, calibration, and interval stability across class-imbalanced tables?
3. Which modern tabular benchmarks and drifted data slices retain the method’s gains after leakage, multiple-testing, and compute costs are measured?

## Exactly Three Challenges

1. Reconstructing the MATLAB/KEEL pipeline, preprocessing, folds, k grid, seeds, and missing-value handling without silent protocol drift.
2. Separating transductive gains from inductive gains when unlabeled test covariates are used to set discretization boundaries.
3. Measuring whether finer discretization improves real deployment quality after calibration, memory, latency, and maintenance costs are included.

## Validation

- Required source-first workflow completed.
- Exactly three next-review questions and exactly three challenges are present.
- Public-safe allowlist is limited to generated Markdown artifacts plus the required publication-index Markdown update.
- No .source directory is created.

## Attribution Block

- Source URL: https://arxiv.org/abs/2111.10983
  - Applies to: selection metadata, authors, version history, abstract, and public citation.
  - Notes: Public arXiv record; source files withheld locally.
- Source URL: https://arxiv.org/pdf/2111.10983
  - Applies to: PDF integrity gate and primary-paper review.
  - Notes: Local PDF inspected; not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/2111.10983
  - Applies to: full-paper HTML review, methods, results, tables, and limitations.
  - Notes: Approved fallback rendering retained locally; not uploaded.
- Source URL: https://doi.org/10.1016/j.eswa.2023.120094
  - Applies to: publisher metadata and publication context.
  - Notes: Publisher DOI locator.
