# DEP-E-20260716-Hyperbolic Catenaries

#arxiv #differential-geometry #hyperbolic-geometry #minimal-surfaces #catenaries #calculus-of-variations #lorentzian-geometry #surfaces-of-revolution #research-review

This DEP-E entry preserves a source-grounded, version-aware review of *Catenaries and minimal surfaces of revolution in hyperbolic space* by Luiz C. B. da Silva and Rafael López (arXiv:2211.15297v2; journal DOI `10.1017/prm.2024.56`). The sampled archive unit was repaired and integrity-verified before review. Original PDF, full-paper HTML, metadata HTML, TeX/source, extracted text, and caches remain local and were not uploaded.

## Contents

- `README.md` - DEP inventory, public-safe context, item summaries, relevance, and attribution.
- `hyperbolic_catenaries_manuscript.md` - schema-complete manuscript review with evidence ledger, geometric reconstruction, version comparison, limitations, implementation translations, and replication checklist.

## Summary of Items

The manuscript reconstructs the paper's variational definition of an extrinsic catenary in the hyperboloid model, the elliptic/hyperbolic/parabolic classification induced by the causal character of a fixed plane, the Euler-Lagrange curvature laws, the coordinate-free Killing-field characterization, and the equivalence between minimal surfaces of revolution and their extrinsic-catenary generating curves. It also explains why horocycle distance yields an intrinsic characterization for the elliptic family.

The artifact distinguishes arXiv v2 from the later open-access journal version. The journal version states the main result as an explicit if-and-only-if theorem, corrects the constant-curvature scaling to `-1/r²`, and adds numerical examples of the three surface types. Both inspected versions retain a likely `cosh(u/u)` typographical defect in the hyperbolic calculation, and no official numerical code or initial-condition manifest was identified.

The record also preserves the uniform random draw, dedup checks, initial partial source state, bounded repair, complete-source verification, cache miss-to-cached transition, and exactly three related Black Lake entries. The proofs and numerical examples were not independently reproduced.

## Insights and Relevance

The durable conceptual bridge is that a two-dimensional weighted-length variational problem can encode a three-dimensional zero-mean-curvature condition when the weight is chosen from the ambient symmetry geometry. The three causal types are not cosmetic labels: Lorentzian, Riemannian, and degenerate axes produce distinct distance weights, orbit families, and curvature equations. The related Flag Hardy Operators entry reinforces the value of respecting non-Euclidean symmetry rather than flattening it; iKalibr shows the same need for group-aware curves and gauge choices in an engineering setting; CoreMem Geometry supplies a counterexample where geometric terminology outruns the actual metric construction.

## Attribution Block

- Source URL: https://arxiv.org/abs/2211.15297v2
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: Primary metadata, title, authors, submission history, abstract, subject, arXiv DOI, and source links.
- Source URL: https://arxiv.org/pdf/2211.15297
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: Complete arXiv v2 paper used for theorem, proof, and conclusion review; verified local copy withheld.
- Source URL: https://arxiv.org/html/2211.15297
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: Official full-paper HTML used for structural and formula cross-checking; verified local copy withheld.
- Source URL: https://arxiv.org/e-print/2211.15297
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: TeX/source package used through the local extraction cache; source archive withheld.
- Source URL: https://doi.org/10.48550/arXiv.2211.15297
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: Persistent arXiv-issued DOI.
- Source URL: https://doi.org/10.1017/prm.2024.56
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: Open-access Cambridge University Press version of record, publication metadata, final theorem wording, corrected curvature scaling, and numerical examples.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: `README.md`; `hyperbolic_catenaries_manuscript.md`
  - Notes: Live repository deposition, source-withholding, and commit authority.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: `README.md`; `hyperbolic_catenaries_manuscript.md`
  - Notes: DEP-E filing and publication-index authority.
- Source URL: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: Companion-repository authority read before dedup and related-context exploration.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: Related processed artifact for symmetry-adapted analysis on a non-Euclidean homogeneous space; it does not validate the selected paper.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: Related processed artifact for Lie-group curves, coordinate gauges, and geometric constraints; it does not validate the selected paper.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-CoreMem%20Geometry/2606.18406-whitepaper-review.md
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: Related processed artifact used as a negative comparison for unsupported geometric branding; it does not validate the selected paper.
- Source URL: https://doi.org/10.1007/s40863-023-00399-z
  - Applies to: `hyperbolic_catenaries_manuscript.md`
  - Notes: Near-primary related work on catenaries in Riemannian surfaces.
- Source-file policy: Original source files were withheld locally.
  - Applies to: the entire DEP entry.
  - Notes: No `.source/` directory was created and no PDF, HTML, source archive, cache, or extracted source text was uploaded.
