# Biometric Identity Gaps

Tags: #arxiv #computer-vision #biometrics #face-recognition #synthetic-identities #identity-governance #deepfake-detection #fairness #safety #DEP-E

This DEP-E preserves a public-safe, source-grounded review of arXiv:2605.18238v1. The source PDF, official full-paper HTML, metadata HTML, TeX/source package, extraction cache, and extracted text were inspected locally and deliberately withheld. The deposit contains derived Markdown only and does not provide face-generation code, embeddings, biometric galleries, model weights, or operational provisioning instructions.

## Contents

- `README.md` - deposit inventory, research context, safety boundary, and attribution.
- `biometric_identity_gaps_manuscript.md` - schema-complete manuscript covering the BIP geometry, allocation, GapGen realization, capacity model, experiments, limitations, misuse risks, and related research.

No `.source/` directory was created. No PDF, HTML, TeX/source archive, biometric embedding, gallery, face image, cache, extracted source text, code, model, or dataset is included.

## Summary of Items

The manuscript reconstructs Biometric Identity Provisioning as a gallery-relative packing problem in an ArcFace embedding space. It explains the repulsion-plus-PCA proposal, exact hard checks, GapGen curriculum, threshold choice, approximate capacity analysis, open-world test, v-LFW protocols, and IAPCT detector. Author-reported results, reviewer interpretations, process evidence, and safety claims are separated.

The central audit result is that embedding allocation and face realization are not interchangeable. At the primary threshold, the displayed hard-checked 10M embedding result is 100.00% non-collision and 99.98% inter-class separation, while the realized 1M image result is 98.07% and 78.36%. The artifact also records a main-text/table-caption rounding inconsistency and the absence of an official public code, project, or dataset link in the inspected author-lab metadata.

## Insights and Relevance

The paper provides a useful identity-allocation formulation and an unusually explicit gallery-update remark: new enrollments can force revocation. That converts “persistent identity” into a lifecycle obligation involving threshold versioning, exact nearest-neighbor recall, re-encoding, periodic reassessment, and human-governed reassignment. Document Fraud LLM contributes fixed-denominator forensics and calibration cautions; BA-LoRA Bias contributes representation-diversity and minority-group governance; Mosaic Safety contributes independent monitoring, fallback/revocation, and falsification.

This deposit does not endorse operational biometric identity provisioning. A face is not required for a digital entity, and visual identity can increase anthropomorphic deception, surveillance, Sybil, KYC, consent, and resemblance risks. Any further work should remain synthetic/offline until independent governance establishes purpose limitation, non-biometric alternatives, data rights, demographic evaluation, attack testing, revocation policy, and human accountability.

## Attribution Block

- Source URL: https://arxiv.org/abs/2605.18238v1
  - Applies to: `biometric_identity_gaps_manuscript.md`
  - Notes: Canonical title, authors, abstract, subject, version, and submission date.
- Source URL: https://arxiv.org/pdf/2605.18238
  - Applies to: `biometric_identity_gaps_manuscript.md`
  - Notes: Primary full-paper PDF inspected locally; file withheld and not redistributed.
- Source URL: https://arxiv.org/html/2605.18238
  - Applies to: `biometric_identity_gaps_manuscript.md`
  - Notes: Official full-paper HTML inspected locally; file withheld and not redistributed.
- Source URL: https://arxiv.org/e-print/2605.18238
  - Applies to: `biometric_identity_gaps_manuscript.md`
  - Notes: Primary TeX/source package inspected locally; file withheld and not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2605.18238
  - Applies to: `biometric_identity_gaps_manuscript.md`
  - Notes: Canonical arXiv DOI locator.
- Source URL: https://github.com/VILab-Drexel/VILab.github.io/blob/271cb74f57f5e26e74f0bd62398742a0b4d46487/info.json
  - Applies to: `biometric_identity_gaps_manuscript.md`
  - Notes: Authors' lab publication metadata inspected for code/project availability; both fields were empty for this paper.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Document%20Fraud%20LLM/document_fraud_llm_manuscript.md
  - Applies to: `biometric_identity_gaps_manuscript.md`
  - Notes: Related DEP used for forensic evaluation and calibration synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-BA-LoRA%20Bias/ba-lora-bias-manuscript.md
  - Applies to: `biometric_identity_gaps_manuscript.md`
  - Notes: Related DEP used for bias, representation-diversity, and monitoring synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260709-Mosaic%20Safety/mosaic_safety_manuscript.md
  - Applies to: `biometric_identity_gaps_manuscript.md`
  - Notes: Related DEP used for monitoring, fallback, and falsification synthesis.
