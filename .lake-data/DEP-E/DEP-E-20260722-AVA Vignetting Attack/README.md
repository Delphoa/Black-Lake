# DEP-E-20260722-AVA Vignetting Attack

**Tags:** #adversarial-robustness #computer-vision #vignetting #photometric-perturbations #level-set-optimization #evidence-audit #research-review

This DEP-E package contains a public-safe, source-first review of *AVA: Adversarial Vignetting Attack against Visual Recognition*. It focuses on the method's physically inspired parameterization, the evidence supporting RA-AVA, the boundary between digital and physical claims, and defensive evaluation practices. A verified local PDF and full-paper HTML were inspected before synthesis. All original source files, extracted text, caches, and inspection renders were withheld locally and were not uploaded.

## Contents

- `README.md` — package inventory, context, synthesis summary, and attribution.
- `ava_vignetting_attack_manuscript.md` — schema-complete research manuscript with evidence ledger, critical review, defensive implementation directions, and source references.

No `.source/` directory is included because the original research files are not redistributed in this public deposit.

## Summary of Items

The manuscript records a uniform random selection from 75,777 paper units, a no-collision dedup check, a partial-to-complete source repair, and a cache miss-to-cached extraction. It reconstructs the paper's vignetting model, distinguishes RI-AVA from RA-AVA, checks the reported white-box and transfer tables, documents an unresolved prose/Table 2 discrepancy, and identifies evidence missing from claims of imperceptibility and physical realizability.

## Insights and Relevance

AVA is useful as evidence that structured photometric perturbations can expose robustness gaps not summarized by a conventional pixel-norm threat model. The strongest practical lesson is methodological: report structured attack coverage together with perceptual, semantic, calibration, restoration, and physical-acquisition evidence. The package deliberately frames implementation ideas as defensive audit and release-gating tools rather than as operational attack code.

The review connects AVA to exactly three existing DEP-E deposits: Feature Denoising as a representation-level defense counterpart, ViT Semantic Robustness as a perceptual/semantic validation bridge, and Adversarial Label Noise as a reminder that conclusions are conditional on threat and objective choices.

## Attribution Block

Primary research: Binyu Tian, Felix Juefei-Xu, Qing Guo, Xiaofei Xie, Xiaohong Li, and Yang Liu, *AVA: Adversarial Vignetting Attack against Visual Recognition*, IJCAI 2021, [arXiv:2105.05558](https://arxiv.org/abs/2105.05558), [DOI:10.24963/ijcai.2021/145](https://doi.org/10.24963/ijcai.2021/145). This DEP-E package is an independent research review and does not imply author endorsement. Source documents remain under their original terms, were retained locally, and were not uploaded or redistributed.
