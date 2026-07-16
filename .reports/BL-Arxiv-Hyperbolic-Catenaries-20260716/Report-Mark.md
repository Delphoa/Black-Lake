# Report-Mark: Hyperbolic Catenaries

## Source Metadata

| Field | Value |
|---|---|
| Selected work | *Catenaries and minimal surfaces of revolution in hyperbolic space* |
| Authors | Luiz C. B. da Silva; Rafael López |
| arXiv record | arXiv:2211.15297v2; submitted 2022-11-28; revised 2023-06-11 |
| arXiv DOI | https://doi.org/10.48550/arXiv.2211.15297 |
| Journal version | *Proceedings of the Royal Society of Edinburgh Section A: Mathematics*, volume 156, issue 1, February 2026, pages 263-283 |
| Journal DOI | https://doi.org/10.1017/prm.2024.56 |
| Subject | Differential Geometry (`math.DG`); MSC 53A04, 53A10, 53A35, 49J05 |
| License context | Publisher version is CC BY 4.0; source documents remain withheld by automation policy |
| Source-integrity state | Initial `partial`; repaired to verified `complete` before synthesis |
| Review basis | Complete arXiv v2 PDF, full-paper HTML, TeX/source extraction, metadata, and open publisher HTML |

## Concise Research Notes

The paper asks for a hyperbolic analogue of Euler's Euclidean fact that rotating a catenary produces a minimal catenoid. An intrinsic hyperbolic catenary does not directly generate a minimal surface after revolution, so the authors change the weight: instead of intrinsic distance to a geodesic, they use distance in the ambient Lorentz-Minkowski space from the curve to the fixed two-plane serving as the axis of revolution.

In the hyperboloid model, the causal type of that plane yields three regimes. A Lorentzian plane produces the elliptic family, a Riemannian plane the hyperbolic family, and a degenerate plane the parabolic family. In semi-geodesic coordinates, the corresponding weights are proportional to `sinh(u/r)`, `cosh(u/r) cosh(v/r)`, and `exp(-v/r) cosh(u/r)`.

The general weighted-length functional `∫ f(γ) ds` has critical curves satisfying `κ = -<n, grad f>/f`. For the three distance functions, the gradient is the tangential part of the ambient Killing field whose flow points toward the reference plane. This gives the coordinate-free law `κ = -<n, X>/dist(γ,P²)`.

The surface calculation classifies elliptic, hyperbolic, and parabolic rotations, computes their mean curvature, and rewrites the zero-mean-curvature condition as the same three curvature equations obtained from the variational problem. The journal theorem therefore states an equivalence: a surface of revolution is minimal exactly when its generating curve is the matching extrinsic catenary.

The elliptic family also admits an intrinsic description. Horo-geodesic coordinates make the horocycle distance `u exp(-v/r)` equal to the relevant ambient height, so every hyperbolic horocatenary is an elliptic extrinsic catenary. No analogous intrinsic characterization is supplied for the hyperbolic or parabolic families.

## Evidence and Attribution

| ID | Inspected evidence | Use | Confidence and limitation |
|---|---|---|---|
| E1 | arXiv metadata and version history | Identity, authors, dates, category, arXiv DOI | High; metadata does not establish proofs |
| E2 | Complete arXiv v2 PDF and extracted text | Full preprint argument, theorem statements, equations, conclusion | High for reporting; proof not independently certified |
| E3 | Official full-paper arXiv HTML and TeX/source | Formula and section cross-check, source-level typo detection | High for source transcription |
| E4 | Open Cambridge University Press version of record | Journal DOI, publication metadata, final theorem wording, corrected curvature scaling, Figure 1 numerical examples | High; numerical examples were not reproduced |
| E5 | Exactly three Black Lake records | Cross-domain conceptual synthesis | Medium; related records do not validate the selected theorem |
| E6 | Public-safe integrity and cache summaries | Complete-source gate and extraction status | High; raw paths and source files intentionally withheld |

## Version-Aware Findings

1. The arXiv v2 preprint writes the sectional curvature of the radius-`r` hyperboloid as `-1/r`; the journal version correctly uses `-1/r²`.
2. The preprint's headline theorem reads primarily in the minimal-surface-to-catenary direction, while journal Theorem 5.3 states the full if-and-only-if equivalence.
3. The journal version adds Figure 1 with numerical elliptic, parabolic, and hyperbolic examples in the Poincaré ball, whereas the inspected arXiv v2 source has no figures or tables.
4. Both inspected versions appear to retain `cosh(u/u)` in the hyperbolic identity that should dimensionally and contextually be `cosh(u/r)`.
5. The introductory phrase “spherical, hyperbolic, and parabolic” is later normalized by the formal theorem to “elliptic, hyperbolic, and parabolic,” reflecting a terminology inconsistency rather than a separate fourth class.

## Related DEP Entries

1. [Flag Hardy Operators](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md)
   - Relevance: both works let non-Euclidean symmetry determine the correct analytic object. Flag Hardy analysis preserves anisotropic Heisenberg scales; extrinsic catenaries preserve the orbit and causal structure of the hyperboloid model.
   - Source basis: the related manuscript's source metadata, executive summary, group dilation, flag-geometry discussion, and proof-mechanism analysis were inspected.
2. [iKalibr Calibration](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md)
   - Relevance: both works represent continuous curves on non-Euclidean spaces, distinguish coordinate choices from invariant content, and use group actions or Lie algebra machinery to preserve geometry.
   - Source basis: the related manuscript's source metadata, continuous-time `SO(3)` spline representation, gauge choice, and geometric-observability notes were inspected.
3. [CoreMem Geometry](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-CoreMem%20Geometry/2606.18406-whitepaper-review.md)
   - Relevance: this is a deliberate negative bridge. CoreMem's review shows how “Riemannian” can collapse to global covariance reweighting; the selected paper instead supplies an explicit manifold, induced metric, ambient bilinear form, isometry group, and curvature law.
   - Source basis: the related review's executive assessment, covariance construction, dimensional audit, and criticism of unsupported Fisher-Rao terminology were inspected.

## Synthesis Note

### Concept Bridge

The paper's reusable pattern is “symmetry-selected weighting.” Start with a curve in a manifold, identify the group action that generates the desired higher-dimensional object, and choose a scalar weight whose gradient encodes the corresponding orbit geometry. The Euler-Lagrange equation for the weighted curve then becomes the mean-curvature equation for the generated surface. This is stronger than a coordinate analogy: it maps a variational problem, a Killing field, and a geometric PDE onto the same invariant relation.

### Potential Implementations

1. **Symbolic equivalence auditor** - encode the semi-geodesic metric, three weights, surface parametrizations, and mean-curvature formulas; simplify both sides to verify the theorem and flag dimensional inconsistencies.
2. **Hyperbolic surface explorer** - numerically integrate the three curvature ODEs under explicit initial conditions, revolve the curves in the hyperboloid model, and visualize them after projection into the Poincaré ball.
3. **Geometry-claim evidence checker** - require every “Riemannian,” “hyperbolic,” or “invariant” software claim to identify a manifold, metric, group action, coordinate transformation, and testable invariant.

### Deeper Relationship Observations

1. Flag Hardy Operators and hyperbolic catenaries both show that flattening a non-Euclidean problem too early destroys the structure that makes the theorem work: scale relations matter in one case, causal orbit types in the other.
2. iKalibr and the selected paper both separate gauge-dependent coordinates from geometric content. A coordinate chart or reference sensor makes computation possible, but the meaningful statement is expressed through group-compatible residuals or curvature.
3. CoreMem's failed geometric branding clarifies why the selected construction is convincing: the latter derives its metric and gradients from an explicit ambient model and matches them to an independent mean-curvature calculation.

### Conceptual Similarities

1. **Invariant decomposition:** all three related records divide the problem according to geometry—flag scale regimes, sensor/state manifolds, or causal axis types—before aggregation.
2. **Compatibility certificate:** almost-orthogonality, calibrated residual geometry, and the equality of curvature laws each certify that two representations respect the same structure.
3. **Auditability through equations:** each record becomes most useful when names are replaced by dimensioned formulas, explicit transformations, and checkable boundary conditions.

### MVP Implementations with Code Mock-ups

1. **Causal-type classifier**

~~~python
import numpy as np

def causal_type(basis, minkowski_metric):
    gram = basis.T @ minkowski_metric @ basis
    eigenvalues = np.linalg.eigvalsh(gram)
    if np.any(np.isclose(eigenvalues, 0.0, atol=1e-10)):
        return "parabolic"
    if np.all(eigenvalues > 0):
        return "hyperbolic"
    return "elliptic"
~~~

This toy classifier turns a plane basis into the corresponding orbit family. A production version needs rank checks, tolerance policy, symbolic cases, and tests against canonical planes.

2. **Discrete weighted-length evaluator**

~~~python
import numpy as np

def weighted_length(points, weight):
    segments = points[1:] - points[:-1]
    midpoints = 0.5 * (points[1:] + points[:-1])
    lengths = np.linalg.norm(segments, axis=1)
    return float(np.sum(weight(midpoints) * lengths))
~~~

This is only a Euclidean discretization scaffold. A real hyperbolic implementation must use the induced metric, chart-aware distances, endpoint constraints, and convergence tests.

3. **Version-defect lint**

~~~python
def lint_geometry_text(text):
    findings = []
    if "K = -1/r" in text and "K = -1/r^2" not in text:
        findings.append("Check radius scaling: expected sectional curvature -1/r^2.")
    if "cosh(u/u)" in text:
        findings.append("Check likely typo: cosh(u/u) should be compared with cosh(u/r).")
    return findings
~~~

This bounded checker preserves known defects as review prompts; it does not prove that a manuscript is mathematically correct.

### Developer Challenges

1. Represent Lorentzian signatures, degenerate planes, and hyperbolic norms without silently applying Euclidean distance or positive-definite assumptions.
2. Integrate curvature ODEs near axes and ideal-boundary regions while maintaining constraints, stable parameterization, and reproducible stopping rules.
3. Distinguish harmless notation changes from theorem-altering version differences and generate traces that a mathematician can audit.

### Author Challenges

1. Provide intrinsic characterizations or rigorous obstructions for the hyperbolic and parabolic extrinsic families.
2. Publish complete numerical initial conditions, solver choices, tolerances, and code for the three surfaces shown in the journal figure.
3. Correct the surviving `cosh(u/u)` expression and harmonize elliptic/spherical terminology across headline and formal theorem statements.

## Validation Notes

- The local source gate passed before review: valid PDF, verified full-paper HTML, metadata HTML, validated TeX/source archive, and zero partial files.
- The extraction cache changed from miss to `cached` under `missing-only` mode; PDF, HTML, and source text were present.
- Major claims were cross-checked between arXiv v2 and the open publisher version.
- No local absolute path, username, machine name, exact execution timestamp, or local timezone label is included.
- The three Python mock-ups are intentionally bounded and will be syntax-checked before submission.
- The exactly-three requirements for implementations, relationship observations, similarities, MVP mock-ups, developer challenges, and author challenges are satisfied.
- No source file, extracted source text, cache, PDF, HTML, or source archive is included in this report directory.

## Attribution Block

- Source URL: https://arxiv.org/abs/2211.15297v2
  - Applies to: source identity, version history, abstract, category, and source links.
  - Notes: Primary arXiv metadata record.
- Source URL: https://arxiv.org/pdf/2211.15297
  - Applies to: full preprint review and formula cross-check.
  - Notes: Verified local PDF inspected; file withheld.
- Source URL: https://arxiv.org/html/2211.15297
  - Applies to: full-paper structure and text cross-check.
  - Notes: Verified local full-paper HTML inspected; file withheld.
- Source URL: https://arxiv.org/e-print/2211.15297
  - Applies to: TeX-level theorem and equation inspection.
  - Notes: Validated local source archive inspected; file withheld.
- Source URL: https://doi.org/10.1017/prm.2024.56
  - Applies to: version-of-record metadata, final theorem, figures, corrections, and open questions.
  - Notes: Open-access publisher HTML inspected by URL.
- Source URL: https://doi.org/10.48550/arXiv.2211.15297
  - Applies to: stable arXiv identifier.
  - Notes: arXiv-issued DOI.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md
  - Applies to: related symmetry-adapted non-Euclidean analysis.
  - Notes: Processed context only; not validation evidence.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md
  - Applies to: related Lie-group curve, gauge, and geometric-estimation analysis.
  - Notes: Processed context only; not validation evidence.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-CoreMem%20Geometry/2606.18406-whitepaper-review.md
  - Applies to: negative comparison for unsupported geometric terminology.
  - Notes: Processed context only; not validation evidence.
- Source-file policy: all original sources and extraction caches were withheld locally.
  - Applies to: the complete Report-Mark.
  - Notes: No source document was uploaded, staged, copied, or attached.
