# DEP-E-20260722-FAVLA Fast-Slow

#robotics #vision-language-action #contact-rich-manipulation #force-feedback #fast-slow-control #adaptive-inference #research-review

Public-safe deposition context: Source-first review of *FAVLA: A Force-Adaptive Fast-Slow VLA model for Contact-Rich Robotic Manipulation* (arXiv:2602.23648v1). The private archive unit passed complete-PDF and full-paper-HTML integrity checks after one bounded repair preserved its valid PDF and collected missing companion sources. Original source files and private execution records were withheld; this DEP contains derived Markdown only.

## Contents

- `README.md` - DEP inventory, context, source policy, relevance, and attribution.
- `favla_fast_slow_manuscript.md` - Schema-complete manuscript review with evidence ledger, mechanism and result analysis, limitations, implementation paths, exactly three related DEP bridges, replication guidance, and source-integrity appendix.

## Summary of Items

### `README.md`

Defines the DEP-E scope and confirms that no PDF, HTML, source archive, extracted text, cache, render, local verification record, or `.source/` directory is part of the public deposit.

### `favla_fast_slow_manuscript.md`

Reviews FAVLA's slow semantic backbone, force-injected action expert, future-force-variance predictor, adaptive execution schedule, fixed-noise reuse, and temporal ensemble. It records the reported 80.8% unweighted mean success, per-task baselines, two-task force measurements, component and frequency ablations, dataset/training details, and explicit failure cases. It also qualifies the three-way Box Flipping tie, distinguishes task-balanced from pooled-trial averaging, and identifies the under-specified relationship between 200 Hz recorded force, 30 Hz training data, and actual action-update timing.

## Insights and Relevance

The durable insight is that contact-rich VLA benefits from an explicit separation between slow semantic context and faster force-conditioned action revision. The paper turns that separation into a concrete cached-context and conditional-compute design. For follow-on engineering, the deposit is most useful as a benchmark and instrumentation specification rather than a safety claim: a credible reproduction needs native-rate timing traces, calibration lineage, sensor-age checks, matched-compute scheduler controls, repeated trials, force distributions and impulses, independent constraints, and deterministic fallback. The exactly three related DEP entries make those dependencies explicit through semantic action routing, spatiotemporal calibration, and CBF-based admissibility.

## Attribution Block

- Source URL: https://arxiv.org/abs/2602.23648
  - Applies to: paper identity, authors, version, submission date, arXiv DOI, license, and public source links.
  - Notes: Metadata page only; the manuscript synthesis used verified complete source documents.
- Source URL: https://arxiv.org/pdf/2602.23648
  - Applies to: `favla_fast_slow_manuscript.md`
  - Notes: Complete 16-page primary paper inspected locally and withheld.
- Source URL: https://arxiv.org/html/2602.23648
  - Applies to: `favla_fast_slow_manuscript.md`
  - Notes: Official full-paper rendering inspected after integrity validation and withheld.
- Source URL: https://arxiv.org/e-print/2602.23648
  - Applies to: `favla_fast_slow_manuscript.md`
  - Notes: TeX/source package used to cross-check equations, tables, captions, training details, appendix, and failures; withheld.
- Source URL: https://doi.org/10.48550/arXiv.2602.23648
  - Applies to: persistent paper identification.
  - Notes: arXiv-issued DOI.
- Source URL: https://creativecommons.org/licenses/by/4.0/
  - Applies to: license identified by the canonical arXiv record.
  - Notes: The task's source-locality policy still requires withholding original source files.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-Semantic%20Skill%20MoE/semantic_skill_moe_manuscript.md
  - Applies to: semantic routing and chunk-consistency synthesis.
  - Notes: Related processed research only; it does not validate FAVLA results.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Applies to: multi-sensor timing, calibration, observability, and drift synthesis.
  - Notes: Related processed research only; it does not validate FAVLA results.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260711-RRT-CBF%20Motion/rrt_cbf_motion_manuscript.md
  - Applies to: constraint, tracking, state/solver validity, and fallback synthesis.
  - Notes: Related processed research only; it does not validate FAVLA results.
- Source files: Withheld locally; none were uploaded, staged, copied, or attached, and no `.source/` directory was created.
