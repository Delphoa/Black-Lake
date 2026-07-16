# Noisy Poisson Inference

Tags: #arxiv #statistics #poisson-regression #measurement-error #high-dimensional-inference #nonconvex-optimization #hypothesis-testing #neuroimaging #DEP-E

This DEP-E preserves a public-safe, source-grounded review of arXiv:2301.00139v1. The source PDF, local full-paper rendering, metadata HTML, TeX/source package, extraction cache, and extracted text were inspected locally and deliberately withheld. The deposit contains derived Markdown only and does not claim independent reproduction, clinical validation, or production readiness.

## Contents

- `README.md` - deposit inventory, research context, and attribution.
- `noisy_poisson_inference_manuscript.md` - schema-complete manuscript covering evidence, theory, experiments, limitations, implementation boundaries, and related research.

No `.source/` directory was created. No PDF, HTML, TeX/source archive, cache, extracted source text, or other original source file is included.

## Summary of Items

The manuscript explains a noise-corrected high-dimensional Poisson loss, amenable nonconvex regularization, constrained and unconstrained estimators, and asymptotic Wald and score tests for linear hypotheses. It separates author theorems, source-reported simulations, ADNI observations, reviewer interpretations, and process evidence. It also records that the paper-declared GitHub repository was inspected at a pinned commit but appears to contain county COVID/weather analysis rather than the reported ADNI workflow.

## Insights and Relevance

Measurement error is not a preprocessing nuisance here: it changes the exponential mean term, the optimizer, the covariance estimate, and the null distribution used for inference. The paper's corrected tests substantially reduce the severe Type-I-error inflation shown for naive procedures, but that success is conditional on a credible error covariance, sparse structure, local curvature, tuning, and an appropriate local solution. PAC Confidence supplies a finite-sample and distribution-envelope contrast; Acoustic Phase Retrieval highlights observability and conditioning under noisy measurements; Joint Sensing MEC reinforces the difference between monotone iterative progress and global optimality in mixed nonconvex systems.

For clinical or scientific use, the artifact recommends a staged verifier: validate the count model and error covariance, check optimizer conditions and stability, preserve selection/inference boundaries, model dependent multiplicity, and require external replication. The ADNI findings remain observational associations and must not be treated as causal, diagnostic, or therapeutic conclusions.

## Attribution Block

- Source URL: https://arxiv.org/abs/2301.00139v1
  - Applies to: `noisy_poisson_inference_manuscript.md`
  - Notes: Canonical arXiv metadata, title, authors, abstract, version, and submission date.
- Source URL: https://arxiv.org/pdf/2301.00139
  - Applies to: `noisy_poisson_inference_manuscript.md`
  - Notes: Primary full-paper PDF inspected locally; file withheld and not redistributed.
- Source URL: https://arxiv.org/e-print/2301.00139
  - Applies to: `noisy_poisson_inference_manuscript.md`
  - Notes: Primary TeX/source package inspected locally; file withheld and not redistributed.
- Source URL: https://doi.org/10.48550/arXiv.2301.00139
  - Applies to: `noisy_poisson_inference_manuscript.md`
  - Notes: Canonical arXiv DOI locator.
- Source URL: https://github.com/feigroup/high-dimenisional-inference-for-count-data-with-errors/tree/41ca0fb990022015812e0ff53ab01627ddb6d21e
  - Applies to: `noisy_poisson_inference_manuscript.md`
  - Notes: Paper-declared implementation inspected as evidence only; no code collected, executed, or deposited.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence/pac_confidence_manuscript.md
  - Applies to: `noisy_poisson_inference_manuscript.md`
  - Notes: Related DEP used for finite-sample uncertainty and distribution-envelope synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Acoustic%20Phase%20Retrieval/acoustic_phase_retrieval_manuscript.md
  - Applies to: `noisy_poisson_inference_manuscript.md`
  - Notes: Related DEP used for measurement-noise, observability, and conditioning synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260715-Joint%20Sensing%20MEC/joint_sensing_mec_manuscript.md
  - Applies to: `noisy_poisson_inference_manuscript.md`
  - Notes: Related DEP used for nonconvex optimization and convergence-boundary synthesis.
