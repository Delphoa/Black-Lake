# DEP-E-20260804-DRMOT Tracking

#rgbd #referring-tracking #multi-object-tracking #spatial-grounding #computer-vision #research-review

DEP-E research deposit for *DRMOT: A Dataset and Framework for RGBD Referring Multi-Object Tracking* (arXiv:2602.04692v2). The selected paper passed the complete-source gate after one bounded local archive repair. The PDF, full-paper HTML, metadata HTML, and archive verification records remain local and are not included here.

## Contents

- `README.md`
  - Public-safe DEP context, inventory, item summary, relevance, and attribution.
- `drmot_tracking_manuscript.md`
  - Schema-complete manuscript covering source metadata, evidence ledger, DRSet, DRTrack, results, limitations, implementation paths, MVP framing, related reading, and source-locality validation.

No `.source/` directory exists. No PDF, HTML, metadata page, source archive, cache, extracted source text, dataset, model, or credential is deposited.

## Summary of Items

`drmot_tracking_manuscript.md` records the source-grounded review of the DRMOT task, DRSet dataset, and DRTrack framework. It distinguishes author-reported results from reviewer interpretation, preserves the 187-scene/240-description/56-depth-related dataset counts, records the depth and GRPO ablations, and defines bounded research-to-implementation paths.

## Insights and Relevance

The deposit's main reusable idea is that depth can resolve language-defined spatial ambiguity and stabilize identity association when RGB appearance is insufficient. FEMOT Tracking contributes multimodal association and governance-aware evaluation, Language-to-Space contributes language-to-3D grounding, and Pixel-Point Transfer contributes calibrated RGB-D correspondence and projection-integrity checks. The combined bridge is useful for offline, auditable RGBD perception research; it does not establish production or safety-critical readiness.

## Attribution Block

- Source URL: https://arxiv.org/abs/2602.04692
  - Applies to: `drmot_tracking_manuscript.md`.
  - Notes: Canonical metadata, authors, revision, abstract, and public locators.
- Source URL: https://arxiv.org/html/2602.04692
  - Applies to: `drmot_tracking_manuscript.md`.
  - Notes: Full-paper technical, dataset, method, and results evidence.
- Source URL: https://arxiv.org/pdf/2602.04692
  - Applies to: `drmot_tracking_manuscript.md`.
  - Notes: Primary PDF inspected locally and withheld from this repository.
- Source URL: https://doi.org/10.48550/arXiv.2602.04692
  - Applies to: `drmot_tracking_manuscript.md`.
  - Notes: arXiv-issued DOI identity.
- Source URL: https://github.com/chen-si-jia/DRMOT
  - Applies to: `drmot_tracking_manuscript.md`.
  - Notes: Official repository availability, release statement, and license context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260720-FEMOT%20Tracking/femot_tracking_manuscript.md
  - Applies to: `drmot_tracking_manuscript.md`.
  - Notes: Related DEP for multimodal tracking and sensor-fusion evaluation.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260727-Language-to-Space/language_to_space_manuscript.md
  - Applies to: `drmot_tracking_manuscript.md`.
  - Notes: Related DEP for language-to-3D grounding.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260718-Pixel%20Point%20Transfer/pixel_point_transfer_manuscript.md
  - Applies to: `drmot_tracking_manuscript.md`.
  - Notes: Related DEP for calibrated RGB-D correspondence and geometry audits.
- Source files: withheld locally.
  - Applies to: this DEP entry.
  - Notes: No source file, cache, extracted text, or local archive record was uploaded, staged, committed, or attached; no `.source/` directory was created.
