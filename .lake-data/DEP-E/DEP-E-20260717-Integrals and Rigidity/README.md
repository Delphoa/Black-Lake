# DEP-E-20260717-Integrals and Rigidity

#arxiv #differential-geometry #geometric-analysis #ricci-curvature #rigidity #harmonic-functions #scalar-curvature #green-functions #research-review

Public-safe context: one paper unit was selected uniformly from 75,776 unique PDF-parent units and accepted on the first draw after repository, memory, companion-repository, identifier, normalized-title, slug, and 24-hour dedup checks. The unit was initially partial because it had a valid PDF but no full-paper HTML. Review paused while a bounded repair collected and verified the missing full-paper companion artifacts. All source documents remain local and withheld.

## Contents

- `README.md`
  - DEP inventory, public-safe context, item summaries, insights, and source attribution.
- `integrals_and_rigidity_manuscript.md`
  - Schema-complete manuscript review of the sharp mean value inequality, equality rigidity, weighted scalar-curvature limit, proof architecture, limitations, implementation translations, and validation history.

No `.source/` directory exists. The PDF, full-paper HTML, metadata HTML, TeX/source archive, verification records, and extracted source material were not uploaded.

## Summary of Items

The manuscript reconstructs two connected results from Zixuan Chen, Guoyi Xu, and Shuai Zhang. First, it reports a sharp boundary mean value inequality for nonnegative superharmonic functions on complete manifolds with nonnegative Ricci curvature, valid at every radius, together with Euclidean-ball rigidity at equality. Second, it reports an exact asymptotic formula on complete noncompact three-manifolds with nonnegative Ricci curvature and maximal volume growth:

`lim_(r→∞) r^(-1) ∫_{b≤r} R |∇b| = 8π(1 - V_M)`.

The paper combines a generalized divergence theorem across geodesic cut loci, monotonicity, Green-function level sets, coarea and Bochner formulas, topology of three-manifolds, Gauss-Bonnet, and Bishop-Gromov rigidity. Under the added pinching condition `Ric ≥ ε R g ≥ 0`, the formula forces asymptotic volume ratio one and hence Euclidean space.

The record also preserves the random-selection method, zero-reselection dedup result, initial partial source state, bounded repair, complete-source verification, and exactly three related Black Lake entries. It does not claim independent proof certification.

## Insights and Relevance

The reusable pattern is an **analytic-to-geometric certificate**. A monotone integral quantity first converts a local differential inequality into a scale-global bound; equality then removes every nonnegative defect term and triggers a geometric comparison theorem. In the curvature half, Green-function level sets convert asymptotic geometry into surface topology and a scalar-curvature integral that Gauss-Bonnet can evaluate. The three related DEP entries reinforce different pieces of that pattern: Hyperbolic Catenaries supplies direct curvature and rigidity context, Flag Hardy Operators shows why integral estimates must respect ambient geometry and scaling, and Global NS Existence shows how Green functions and divergence identities become geometry-sensitive proof machinery.

## Attribution Block

- Source URL: https://arxiv.org/abs/2602.10393
  - Applies to: `integrals_and_rigidity_manuscript.md`; `README.md`
  - Notes: Canonical title, authors, submission history, subject classification, abstract, license link, and artifact URLs.
- Source URL: https://arxiv.org/pdf/2602.10393
  - Applies to: `integrals_and_rigidity_manuscript.md`
  - Notes: Complete primary paper used for theorem, proof-architecture, limitation, and reference review; verified local copy withheld.
- Source URL: https://arxiv.org/html/2602.10393
  - Applies to: `integrals_and_rigidity_manuscript.md`
  - Notes: Official full-paper HTML used for structural and formula-aware inspection; verified local copy withheld.
- Source URL: https://arxiv.org/e-print/2602.10393
  - Applies to: `integrals_and_rigidity_manuscript.md`
  - Notes: TeX/source archive collected locally for provenance and withheld; not deposited.
- Source URL: https://doi.org/10.48550/arXiv.2602.10393
  - Applies to: `integrals_and_rigidity_manuscript.md`; `README.md`
  - Notes: Persistent arXiv-issued DOI.
- Source URL: https://creativecommons.org/licenses/by/4.0/
  - Applies to: `integrals_and_rigidity_manuscript.md`
  - Notes: License deed reached from the canonical arXiv record.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Hyperbolic%20Catenaries/hyperbolic_catenaries_manuscript.md
  - Applies to: `integrals_and_rigidity_manuscript.md`
  - Notes: Related processed artifact for differential geometry, curvature equations, and rigidity; contextual only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md
  - Applies to: `integrals_and_rigidity_manuscript.md`
  - Notes: Related processed artifact for geometry-adapted harmonic analysis and scale-aware integral estimates; contextual only.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-Global%20NS%20Existence/global_ns_existence_manuscript.md
  - Applies to: `integrals_and_rigidity_manuscript.md`
  - Notes: Related processed artifact for Green functions, divergence methods, and geometry-sensitive estimates; contextual only.
- Source-file policy: original source files were withheld locally.
  - Applies to: the entire DEP entry.
  - Notes: No PDF, HTML, TeX/source archive, cache, extracted source text, or local archive locator was uploaded.
