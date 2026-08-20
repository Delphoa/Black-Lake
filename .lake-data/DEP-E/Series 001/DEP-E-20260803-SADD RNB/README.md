# DEP-E-20260803-SADD RNB

#machine-learning
#naive-bayes
#semi-supervised-learning
#data-discretization
#tabular-ml

Public-safe research deposit for a source-grounded review of SADD and RNB+ for semi-supervised adaptive discretization in Naive Bayes. The original PDF, full-paper HTML, metadata HTML, source package status, caches, extracted text, and verification records remain in the local archive. No .source directory is included.

## Contents

- README.md — public-safe inventory, context, and attribution for this DEP-E.
- sadd_rnb_manuscript.md — schema-complete manuscript research artifact covering the paper, evidence ledger, methods, results, limitations, implementation paths, and related research.

## Summary of Items

The manuscript preserves the paper identity, source status, SADD/RNB+ mechanism, reported 31-dataset evaluation, transductive-versus-inductive caveat, evidence mapping, limitations, and safe implementation ideas. It is intended for downstream research review and reproducibility planning; it does not redistribute the paper or any local source file.

## Insights and Relevance

The deposit treats discretization as an information-allocation decision rather than a neutral preprocessing step. SADD’s use of pseudo-labeled unlabeled covariates can preserve discriminative structure, but the resulting gain must be classified by protocol: a transductive workflow may use unlabeled test covariates, while a strict-inductive service must learn interval boundaries from training data only. The related Black Lake entries connect this mechanism to broader governance of soft labels, representation exchange, disagreement, calibration, and deployment gates.

## Attribution Block

- Source URL: https://arxiv.org/abs/2111.10983
  - Applies to: sadd_rnb_manuscript.md and this README.
  - Notes: Public metadata, authors, version history, and abstract; source files withheld locally.
- Source URL: https://arxiv.org/pdf/2111.10983
  - Applies to: sadd_rnb_manuscript.md.
  - Notes: Local PDF inspected for integrity and review; not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/2111.10983
  - Applies to: sadd_rnb_manuscript.md.
  - Notes: Local full-paper HTML fallback inspected; not uploaded.
- Source URL: https://www.sciencedirect.com/science/article/pii/S0957417423005961
  - Applies to: publication metadata and corroborating abstract context.
  - Notes: Publisher record.
- Source URL: https://doi.org/10.1016/j.eswa.2023.120094
  - Applies to: stable journal identity.
  - Notes: Journal DOI.
- Source URL: https://creativecommons.org/licenses/by-nc-nd/4.0/
  - Applies to: source-distribution caution.
  - Notes: License deed linked from the arXiv record; original source is not redistributed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-Decentralized%20SSL/decentralized_ssl_manuscript.md
  - Applies to: related-entry synthesis in the manuscript.
  - Notes: Live related DEP inspected.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260716-Adversarial%20Label%20Noise/adversarial_label_noise_manuscript.md
  - Applies to: related-entry synthesis in the manuscript.
  - Notes: Live related DEP inspected.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260719-DUET%20Setwise%20CTR/duet_setwise_ctr_manuscript.md
  - Applies to: related-entry synthesis in the manuscript.
  - Notes: Live related DEP inspected.
