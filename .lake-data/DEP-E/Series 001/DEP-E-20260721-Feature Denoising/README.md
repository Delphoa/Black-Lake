# DEP-E-20260721-Feature Denoising

#adversarial-robustness #computer-vision #feature-denoising #adversarial-training #non-local-networks #imagenet #research-review

Public deposition context: Source-first review of *Feature Denoising for Improving Adversarial Robustness* (arXiv:1812.03411v2; CVPR 2019). The private archive unit passed complete-PDF and full-paper-HTML integrity checks before review. Original source files and private execution records were withheld; this DEP contains derived public-safe Markdown only.

## Contents

- `README.md` - DEP inventory, deposition context, source policy, relevance, and attribution.
- `feature_denoising_manuscript.md` - Schema-complete manuscript review with source metadata, evidence ledger, method/results critique, implementation paths, related DEP synthesis, replication boundaries, and appendix.

## Summary of Items

### `README.md`

Defines the DEP-E scope and confirms that no PDF, HTML, source archive, cache, extracted text, render, or `.source/` directory is part of the public deposit.

### `feature_denoising_manuscript.md`

Reviews the paper's residual feature-denoising block, large-scale targeted-PGD training, matched ImageNet ablations, five-attacker black-box study, CAAD 2018 result, clean-robust trade-off, and archived official implementation. It distinguishes the denoising contribution - roughly three points over the authors' matched ResNet-152 baseline in key white-box settings - from the larger system-level headline comparison to ALP. It also connects the work to exactly three Black Lake deposits on adversarial label noise, representation robustness, and feature-filter architectures.

## Insights and Relevance

The durable insight is a design pattern: a corrective feature transform should be paired with a learned reintegration path and evaluated against parameter-matched null and capacity controls. The paper's projection-plus-residual ablation makes that pattern unusually concrete. For current work, the deposit is most useful as a benchmark specification seed rather than a robustness certificate: modern follow-up should add repeated seeds, untargeted and adaptive multi-attack suites, quantitative representation-noise metrics, calibration, corruption/shift testing, and hardware costs. The official code/models improve provenance, but their archived legacy stack, high distributed-compute requirement, secret CAAD evaluation, and non-commercial license constrain direct deployment.

## Attribution Block

- Source URL: https://arxiv.org/abs/1812.03411
  - Applies to: paper identity, authors, revision history, arXiv DOI, and public source links.
  - Notes: Metadata page only; the manuscript synthesis used verified complete source documents.
- Source URL: https://arxiv.org/pdf/1812.03411
  - Applies to: `feature_denoising_manuscript.md`
  - Notes: Complete primary paper inspected locally; source file withheld.
- Source URL: https://ar5iv.labs.arxiv.org/html/1812.03411
  - Applies to: `feature_denoising_manuscript.md`
  - Notes: Approved full-paper rendering inspected locally after validation; source file withheld.
- Source URL: https://arxiv.org/e-print/1812.03411
  - Applies to: `feature_denoising_manuscript.md`
  - Notes: TeX/source package used to cross-check equations, captions, settings, and tables; source archive withheld.
- Source URL: https://doi.org/10.48550/arXiv.1812.03411
  - Applies to: persistent paper identification.
  - Notes: arXiv-issued DOI.
- Source URL: https://openaccess.thecvf.com/content_CVPR_2019/html/Xie_Feature_Denoising_for_Improving_Adversarial_Robustness_CVPR_2019_paper.html
  - Applies to: CVPR 2019 venue, pages, author, and accepted-version attribution.
  - Notes: Official Computer Vision Foundation record.
- Source URL: https://github.com/facebookresearch/ImageNet-Adversarial-Training
  - Applies to: code, model, license, dependency, runtime, and archived-repository assessment.
  - Notes: Official public repository; code and checkpoints were not copied into this DEP.
- Source files: Withheld locally; none were uploaded and no `.source/` directory was created.
