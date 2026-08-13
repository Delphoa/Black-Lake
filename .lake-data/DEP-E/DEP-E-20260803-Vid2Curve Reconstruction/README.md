# DEP-E-20260803-Vid2Curve Reconstruction

#computer-vision #3D-reconstruction #camera-pose #curve-reconstruction #thin-structures #geometry #source-review

- DEP class: DEP-E
- Deposit date: 2026-08-03
- Subject title: Vid2Curve: Simultaneous Camera Motion Estimation and Thin Structure Reconstruction from an RGB Video
- Primary identity: arXiv:2005.03372v3
- Context: Source-grounded paper, implementation, and related-DEP review. Original source files were verified and withheld locally.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, insights, source-locality statement, and complete attribution.
- `vid2curve_reconstruction_manuscript.md`
  - Schema-complete manuscript covering source metadata, evidence ledger, method, experiments, limitations, implementation inspection, three related DEP entries, product translation, and replication planning.

No `.source/` directory is present. The PDF, full-paper HTML, metadata HTML, TeX/source archive, code clone, rendered pages, extraction material, acquisition receipt, and verification records remain local and were not uploaded.

## Summary of Items

### `README.md`

Defines the DEP-E research boundary, inventories every deposited file, records why the deposit matters, and maps every public source URL to the generated manuscript. It also preserves the mandatory no-source-upload boundary.

### `vid2curve_reconstruction_manuscript.md`

Reviews Vid2Curve from complete primary evidence. The manuscript explains its curve-graph representation, connectivity-aware matching, alternating camera/curve optimization, self-occlusion rejection, sweep-surface reconstruction, synthetic metrics, baseline comparisons, runtime profile, and declared limitations. It separately inspects the author-linked GPL-3.0 C++ implementation at a pinned commit and distinguishes repository availability from reproduced results.

The manuscript also records the uniform random draw and dedup validation, the local repair from a partial to a complete source unit, exactly three concrete related DEP entries, and safe implementation/MVP paths. All source claims remain labeled as source claims; reviewer interpretations and proposals are explicit.

## Insights and Relevance

Vid2Curve is a strong example of representation-aligned reconstruction: a line-like object is modeled as a connected curve graph, and correspondence uses curve adjacency rather than generic nearest points. That design makes topology and self-occlusion explicit, which is valuable beyond the 2020 implementation.

The review's main synthesis is that calibration, correspondence, frame coverage, and topology form one evidence chain. APAP Correspondence supplies a match-repair perspective, iKalibr exposes calibration and observability as upstream integrity, and PaceVGGT reframes frame retention as a geometric coverage decision. A modern system should log all four layers and abstain when the evidence cannot support an auditable reconstruction.

The practical boundary is equally important. The method assumes known intrinsics, clean or pre-segmented backgrounds, favorable initialization, undistorted frames, static tubular objects, circular cross-sections, and offline compute. Reported results were not independently reproduced. The artifact is therefore appropriate for research, replication planning, and audit-tool design, not as proof of production readiness.

## Attribution Block

- Source URL: https://arxiv.org/abs/2005.03372
  - Applies to: `vid2curve_reconstruction_manuscript.md` and this README.
  - Notes: Canonical paper identity, authors, dates, subjects, version history, and artifact links; abstract treated as metadata only.
- Source URL: https://arxiv.org/pdf/2005.03372
  - Applies to: `vid2curve_reconstruction_manuscript.md`.
  - Notes: Complete paper used for methods, figures, tables, experiments, runtime, and limitations; verified source file withheld locally.
- Source URL: https://ar5iv.labs.arxiv.org/html/2005.03372
  - Applies to: `vid2curve_reconstruction_manuscript.md`.
  - Notes: Approved full-paper HTML fallback used for searchable cross-check; source file withheld locally.
- Source URL: https://arxiv.org/e-print/2005.03372
  - Applies to: `vid2curve_reconstruction_manuscript.md`.
  - Notes: TeX/source-package provenance and cross-check; source archive withheld locally.
- Source URL: https://doi.org/10.48550/arXiv.2005.03372
  - Applies to: `vid2curve_reconstruction_manuscript.md` and this README.
  - Notes: Persistent arXiv DOI.
- Source URL: https://doi.org/10.1145/3386569.3392476
  - Applies to: `vid2curve_reconstruction_manuscript.md` and this README.
  - Notes: Published ACM Transactions on Graphics article identity and venue metadata; ACM terms apply.
- Source URL: https://totoro97.github.io/projects/vid2curve/
  - Applies to: `vid2curve_reconstruction_manuscript.md`.
  - Notes: Author-linked project page used for method context, qualitative results, and implementation pointer.
- Source URL: https://github.com/Totoro97/Vid2Curve
  - Applies to: `vid2curve_reconstruction_manuscript.md`.
  - Notes: Official GPL-3.0 implementation inspected at commit `47c379dec5cca2e2de123a392e0b1f93ceb1048a`; code was not built or executed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260729-Correspondence%20Insert/apap_correspondence_manuscript.md
  - Applies to: `vid2curve_reconstruction_manuscript.md`.
  - Notes: Related correspondence-repair DEP; underlying sources are attributed in that artifact and its claims do not validate Vid2Curve.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Applies to: `vid2curve_reconstruction_manuscript.md`.
  - Notes: Related calibration and observability DEP; underlying sources are attributed in that artifact and its claims do not validate Vid2Curve.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-PaceVGGT%20Frame%20Pruning/2605.08371-whitepaper-review.md
  - Applies to: `vid2curve_reconstruction_manuscript.md`.
  - Notes: Related frame-selection and visual-geometry DEP; underlying sources are attributed in that artifact and its claims do not validate Vid2Curve.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: this README and deposition process notes in `vid2curve_reconstruction_manuscript.md`.
  - Notes: Live root repository authority for filing, naming, attribution, source locality, and commit rules.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: this README and deposition process notes in `vid2curve_reconstruction_manuscript.md`.
  - Notes: Live DEP class, container, publication-index, and filing authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: dedup context in `vid2curve_reconstruction_manuscript.md`.
  - Notes: Companion-repository authority fetched and read before relying on its layout.
