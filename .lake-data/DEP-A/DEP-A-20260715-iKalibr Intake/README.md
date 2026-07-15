# DEP-A-20260715-iKalibr Intake

#robotics #sensor-calibration #multi-sensor-fusion #continuous-time #autonomous-systems #observability #whitepaper-review #archival-intake

Public-safe archival intake generated on 2026-07-15 by reviewing `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration` at source commit `398f692812550135476e8d560be1d2a01fa2982e`.

## Contents

- `README.md` - inventory, context, provenance pair, associated records, and final attribution.
- `ikalibr-intake-review.md` - whitepaper-grade reconstruction and audit of the complete iKalibr DEP-E bundle.

## Summary of Items

The review covers continuous-time state, adaptive splines, dynamic initialization, sensor-specific residuals, progressive optimization, Tables I-IX, Figures 1-9, appendices, repeatability-versus-accuracy, runtime, official code, and a calibration-evidence-gate re-conceptualization.

## Insights and Relevance

Calibration is an upstream evidence claim, not an anonymous transform file. Downstream work should preserve frame, clock, excitation, source data, solver version, residuals, uncertainty, ground-truth quality, and calibration identity; favorable repeatability does not exclude stable bias.

## Provenance Pair

- Paired task indicator: `BL-DEPPAIR-20260715-4FAD29AE`
- Direction: `DEP-E -> DEP-A`
- Source action: review-only.
- Source DEP modified: no.
- Files moved: no.
- Existing files copied into DEP-A: no.
- New derived data generated: yes.
- DEP-A intake status: complete after validation and repository submission.
- DEP-A deposition status: complete after validation and repository submission.

## Associated DEP Records

- `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration` - reviewed source record.
- `.lake-data/DEP-E/DEP-E-20260712-HERMES World Model` - related world-model calibration dependency.
- `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action` - related camera-motion dependency.
- `.lake-data/DEP-E/DEP-E-20260710-Self Learned IDC` - related downstream control dependency.

## Attribution Block

- Source URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration
  - Applies to: `ikalibr-intake-review.md`
  - Notes: Complete source DEP-E reviewed in place at the source commit; no source file was modified, moved, or copied.
- Source URL: https://arxiv.org/abs/2407.11420
  - Applies to: `ikalibr-intake-review.md`
  - Notes: Canonical v2 identity and source locators.
- Source URL: https://arxiv.org/html/2407.11420
  - Applies to: `ikalibr-intake-review.md`
  - Notes: Complete authorized paper rendering inspected; source document not uploaded.
- Source URL: https://doi.org/10.1109/TRO.2025.3532506
  - Applies to: `ikalibr-intake-review.md`
  - Notes: Published journal locator.
- Source URL: https://github.com/Unsigned-Long/iKalibr
  - Applies to: `ikalibr-intake-review.md`
  - Notes: Official code surface inspected without build or execution.
- Generated artifact: `ikalibr-intake-review.md`
  - Applies to: this DEP-A.
  - Notes: New derived public-safe review; not a copy. Repository data was reviewed in place and source documents were not uploaded.
