# DEP-E-20260822-HSRNet Aliasing

#super-resolution #image-restoration #aliasing #self-similarity #iterative-reconstruction #attention

Public-safe research deposit for *Hierarchical Similarity Learning for Aliasing Suppression Image Super-Resolution* (arXiv:2206.03361v1). Source files were withheld locally; this entry contains generated Markdown only.

## Contents

- `README.md` - public-safe inventory, context, relevance, and attribution.
- `hsrnet_aliasing_manuscript.md` - schema-complete source-grounded manuscript.

## Summary of Items

- `hsrnet_aliasing_manuscript.md` records HSRNet's hierarchical similarity learning, half-quadratic-splitting-inspired iterations, hierarchical exploration block, multi-scale attention, reported super-resolution results, limitations, and bounded implementation paths.
- The manuscript preserves the public arXiv and publication locators and separates author-reported measurements from reviewer interpretation.
- The PDF, full-paper HTML, metadata HTML, source package, extracted text, caches, and verification receipts remain local and were not deposited.

## Insights and Relevance

HSRNet treats aliasing suppression as a structured inverse problem: an iterative solver-like update is paired with a learned denoiser whose receptive field and attention pattern are shaped by image self-similarity. The design is relevant to image restoration systems that need to expose degradation assumptions, preserve repeated structures, and compare accuracy against parameter and compute budgets. Its reported evidence is based on synthetic bicubic degradation and author-run benchmarks, so independent reproduction, real-world degradation tests, and runtime profiling remain necessary.

## Attribution Block

- Source URL: https://arxiv.org/abs/2206.03361
  - Applies to: `README.md` and `hsrnet_aliasing_manuscript.md`.
  - Notes: Official metadata, authors, abstract, version, and source locators.
- Source URL: https://arxiv.org/html/2206.03361
  - Applies to: `hsrnet_aliasing_manuscript.md`.
  - Notes: Full-paper method, evaluation, limitations, and conclusion; verified local copy withheld.
- Source URL: https://arxiv.org/pdf/2206.03361
  - Applies to: `hsrnet_aliasing_manuscript.md`.
  - Notes: Primary-paper integrity cross-check; PDF withheld locally.
- Source URL: https://doi.org/10.1109/TNNLS.2022.3191674
  - Applies to: `README.md` and `hsrnet_aliasing_manuscript.md`.
  - Notes: IEEE TNNLS publication identifier.
- Related artifact URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20002/DEP-E-20260819-LFMamba%20Light%20Field%20Image/lfmamba_light_field_image_manuscript.md
  - Applies to: `hsrnet_aliasing_manuscript.md`.
  - Notes: Image super-resolution and multi-scale restoration bridge; no source files copied.
- Related artifact URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260720-WKGM%20MRI%20Reconstruction/wkgm_mri_reconstruction_manuscript.md
  - Applies to: `hsrnet_aliasing_manuscript.md`.
  - Notes: Iterative inverse reconstruction and learned data-consistency bridge; no source files copied.
- Related artifact URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/Series%20001/DEP-E-20260819-EnsIR%20An%20Ensemble/ensir_an_ensemble_manuscript.md
  - Applies to: `hsrnet_aliasing_manuscript.md`.
  - Notes: Image-restoration ensemble and uncertainty bridge; no source files copied.
