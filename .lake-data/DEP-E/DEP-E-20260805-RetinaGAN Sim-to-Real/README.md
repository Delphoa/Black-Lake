# DEP-E-20260805-RetinaGAN Sim-to-Real

#robotics #sim-to-real #domain-adaptation #generative-models #object-detection #reinforcement-learning #imitation-learning #safety

Public-safe DEP-E research deposit for *RetinaGAN: An Object-aware Approach to Sim-to-Real Transfer* by Daniel Ho, Kanishka Rao, Zhuo Xu, Eric Jang, Mohi Khansari, and Yunfei Bai. The deposit reviews the complete paper, separates author-reported robot results from reviewer interpretation, and translates its detector-consistency mechanism into bounded evaluation and implementation ideas.

Original source documents and local verification material were withheld. No `.source/` directory was created, and no PDF, HTML, metadata page, TeX/source archive, receipt, cache, rendering, or extracted source text is included.

## Contents

- `README.md` - DEP inventory, public-safe context, summary, insights, source-locality statement, and source attribution.
- `retinagan_sim_to_real_manuscript.md` - schema-complete manuscript review with evidence ledger, claim map, methodology, limitations, implementation paths, exercise plans, MVP concept, related DEP synthesis, references, and validation appendix.

## Summary of Items

### `README.md`

Defines the DEP scope and source-handling boundary. It inventories every file in this DEP and annotates every public source URL used by the generated manuscript.

### `retinagan_sim_to_real_manuscript.md`

Reviews RetinaGAN's CycleGAN base, frozen EfficientDet-D1 constraint, box and class consistency losses, grasping/pushing/door-opening evaluations, and appendix settings. It preserves the reported results while exposing small trial counts, seen-environment evaluation, model-selection notes, detector blind spots, ambiguous printed notation, and the absence of an author-released end-to-end implementation.

## Insights and Relevance

The reusable idea is to treat perception as a transfer invariant. RetinaGAN constrains a pixel translator with a frozen detector so object boxes and class probabilities remain stable across original, translated, and cycled images. The three related DEPs broaden the evidence boundary: Habitat Synthetic Scenes shows that source-asset semantics and a measured reality gap matter before translation; Spiking Pose Tracking shows that mixed synthetic/real perception and domain adaptation still leave a residual transfer gap; ManipulationNet shows that physical robot evidence needs standardized setup, calibration, operator, and safety records. Together they motivate a synthetic-to-physical evidence ledger rather than a single success percentage.

## Attribution Block

- Source URL: https://arxiv.org/abs/2011.03148
  - Applies to: `retinagan_sim_to_real_manuscript.md` and `README.md`.
  - Notes: Canonical title, authors, dates, version history, subject, venue comment, abstract, and source locators. Abstract metadata was not treated as the complete paper.
- Source URL: https://arxiv.org/pdf/2011.03148
  - Applies to: `retinagan_sim_to_real_manuscript.md`.
  - Notes: Complete method, experiments, tables, figures, appendix, and visual checks. The verified PDF remained local.
- Source URL: https://ar5iv.labs.arxiv.org/html/2011.03148
  - Applies to: `retinagan_sim_to_real_manuscript.md`.
  - Notes: Approved full-paper HTML fallback used for searchable cross-checking. The file remained local.
- Source URL: https://arxiv.org/e-print/2011.03148
  - Applies to: `retinagan_sim_to_real_manuscript.md` source and equation inspection.
  - Notes: The TeX/source package remained local.
- Source URL: https://doi.org/10.48550/arXiv.2011.03148
  - Applies to: `retinagan_sim_to_real_manuscript.md` and `README.md`.
  - Notes: Persistent arXiv identity.
- Source URL: https://doi.org/10.1109/ICRA48506.2021.9561157
  - Applies to: `retinagan_sim_to_real_manuscript.md` and `README.md`.
  - Notes: Published ICRA 2021 identity.
- Source URL: https://retinagan.github.io/
  - Applies to: `retinagan_sim_to_real_manuscript.md` project context.
  - Notes: Official author project page with qualitative examples, videos, and public component links; no complete RetinaGAN implementation was exposed.
- Source URL: https://github.com/google-research/tensor2robot/blob/master/preprocessors/image_transformations.py
  - Applies to: `retinagan_sim_to_real_manuscript.md` implementation-boundary discussion.
  - Notes: Project-linked upstream preprocessing component, not an end-to-end RetinaGAN release.
- Source URL: https://github.com/google-research/tensor2robot/blob/master/layers/film_resnet_model.py
  - Applies to: `retinagan_sim_to_real_manuscript.md` implementation-boundary discussion.
  - Notes: Project-linked upstream ResNet-FiLM component, not an end-to-end RetinaGAN release.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260726-Habitat%20Synthetic%20Intake/whitepaper-intake-review.md
  - Applies to: `retinagan_sim_to_real_manuscript.md` related-DEP analysis.
  - Notes: Synthetic-scene, controllability, realism, and reality-gap relationship; processed research artifact only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260724-Spiking%20Pose%20Tracking/spiking_pose_tracking_manuscript.md
  - Applies to: `retinagan_sim_to_real_manuscript.md` related-DEP analysis.
  - Notes: Mixed synthetic/real perception and domain-adaptation relationship; processed research artifact only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260727-ManipulationNet%20An%20Intake/whitepaper-intake-review.md
  - Applies to: `retinagan_sim_to_real_manuscript.md` related-DEP analysis.
  - Notes: Physical robot benchmark, calibration, safety, and evaluation-governance relationship; processed research artifact only.
