# DEP-E-20260719-Kernel Equivalence

#statistics #equivalence-testing #kernel-methods #mmd #ksd #bootstrap #model-validation

Public-safe context: `Black Lake Arxiv DEP 2200 x10` job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P04`, uniformly selected and source-first reviewed arXiv:2603.10886v2. A partial archive was repaired to verified complete before synthesis. Local paths, exact execution times, and source files are withheld.

## Contents

- `README.md` - context, contents, summary, insights, source policy, attribution.
- `kernel_equivalence_manuscript.md` - schema-complete review of four KSD/MMD equivalence tests, theory, experiments, limitations, implementation paths, selection/dedup, integrity, and related synthesis.

No `.source/` exists. PDF, full-paper HTML, metadata HTML, source package, extracted text, and cache remain local.

## Summary of Items

The manuscript explains why failing to reject distributional difference is not evidence of equivalence. It reviews one-sample KSD and two-sample MMD equivalence tests with normal and bootstrap critical values, pointwise asymptotic validity, a power-based margin option, and Gaussian, RBM, and MNIST experiments. Normal tests are reported as more powerful but poorly calibrated near small margins in some regimes; bootstrap tests are more conservative and better calibrated.

The deposit records a first-draw uniform selection, zero duplicates/reselections, bounded repair, complete integrity and cache receipts, exactly three related entries, and zero source uploads.

## Insights and Relevance

Equivalence is always relative to a kernel, representation, margin, sample design, and error budget. A power-selected margin expresses detectability, not necessarily scientific interchangeability. Production gates should require domain margin approval, representation and shift checks, method/margin sensitivity, and a complete decision receipt.

## Source and Distribution Policy

- Source state: verified complete after one bounded official-source repair.
- Sources: withheld locally; `.source/` not created; source uploads zero.
- Public deposit: generated Markdown and required indexes only.
- Deployment job ID: `BLAD-2200-20260719-7D93E819`.
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P04`.

## Attribution Block

- https://arxiv.org/abs/2603.10886 - canonical metadata and abstract.
- https://arxiv.org/html/2603.10886 - verified full-paper evidence; file withheld.
- https://arxiv.org/pdf/2603.10886 - verified cross-format evidence; file withheld.
- https://arxiv.org/e-print/2603.10886 - theorem/proof/figure cross-checks; archive withheld.
- https://doi.org/10.48550/arXiv.2603.10886 - persistent identity.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260713-PAC%20Confidence - related finite-sample confidence analysis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Noisy%20Poisson%20Inference - related test-calibration analysis.
- https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260718-Transport%20Convexity - related distribution-geometry analysis.
- Source files: PDF, HTML, metadata, source package, extracted text, cache. All withheld locally; zero source documents uploaded. Job `BLAD-2200-20260719-7D93E819`, item `BLAD-2200-20260719-7D93E819-P04`.
