# Report-Mark: Integrals and Rigidity

## Source Metadata

- **Paper:** *Integrals and Rigidity on Manifolds with Nonnegative Ricci Curvature*
- **Authors:** Zixuan Chen; Guoyi Xu; Shuai Zhang
- **Canonical record:** https://arxiv.org/abs/2602.10393
- **Full paper:** https://arxiv.org/pdf/2602.10393 and https://arxiv.org/html/2602.10393
- **Source companion:** https://arxiv.org/e-print/2602.10393
- **Stable identifier:** arXiv:2602.10393v1; https://doi.org/10.48550/arXiv.2602.10393
- **Submission date:** 2026-02-11
- **Subject / MSC:** Differential Geometry (`math.DG`); `35K15`, `53C20`
- **License:** CC BY 4.0, linked from the canonical arXiv record
- **Source integrity:** initially `partial`; bounded repair completed; final state `complete`
- **Distribution:** generated Markdown and public URLs only; all source documents and local locators withheld

## Concise Research Notes

The paper proves a sharp boundary mean value inequality for nonzero nonnegative superharmonic functions on complete manifolds with nonnegative Ricci curvature:

`f(x) ≥ [n ω_n r^(n-1)]^(-1) ∫_(∂B_x(r)) f dσ`, for every `r > 0`.

The novelty is the removal of the classical radius-below-injectivity restriction. A generalized divergence theorem on geodesic balls handles cut-locus geometry after pulling the function back through the exponential map. A scale quantity `F(t)` is shown to be nonincreasing using difference estimates and a nested-interval contradiction. Equality makes the monotonicity and volume-comparison defects vanish, and Bishop-Gromov rigidity identifies the ball with its Euclidean counterpart.

For a complete noncompact three-manifold with nonnegative Ricci curvature and maximal volume growth, the paper also proves

`lim_(r→∞) r^(-1) ∫_(b≤r) R |∇b| = 8π(1 - V_M)`,

where `b` is the radius derived from the minimal positive Green function and `V_M` is the asymptotic volume ratio. Weighted-volume identities, Bochner and coarea formulas, topology of Green-function level sets, Gauss-Bonnet, and the Gauss equation produce the exact coefficient. Under `Ric ≥ ε R g ≥ 0`, the formula forces `V_M = 1`, so the maximal-volume-growth three-manifold is Euclidean.

The work is theorem-driven. No empirical benchmark, dataset, or official code repository was identified. The proof was source-reviewed but not independently certified.

## Evidence and Attribution

| Evidence ID | Inspected evidence | Supports | Assessment |
|---|---|---|---|
| E1 | Canonical arXiv record | Identity, authors, date, subject, DOI, license link, and artifact URLs | High-confidence metadata |
| E2 | Verified complete PDF and official full-paper HTML | Theorems 1.1, 4.3, 4.5 and the generalized divergence/monotonicity proof chain | High-confidence reporting; no formal certification |
| E3 | Verified complete PDF and official full-paper HTML | Theorems 1.5, 6.6, level-set topology, weighted-volume limits, and the `8π(1-V_M)` identity | High-confidence reporting within stated hypotheses |
| E4 | Verified complete PDF and official full-paper HTML | Corollaries 1.10 and 6.7 for Ricci pinching plus maximal volume growth | High-confidence reporting; not the unrestricted conjecture |
| E5 | Author discussion in the complete paper | Broader nonparabolic case without maximal volume growth remains open | Direct author boundary |
| E6 | Public-safe selection and integrity records | Uniform draw, zero reselections, initial partial state, bounded repair, complete-source gate | High-confidence process evidence |
| E7 | Three processed Black Lake artifacts | Cross-domain bridges for curvature, harmonic analysis, Green functions, and divergence methods | Context only; not evidence for the selected theorem |

The PDF has 32 pages and its metadata names the three authors, arXiv v1, the arXiv-issued DOI, and CC BY 4.0. The official HTML exposes the full six-section structure and the theorem statements. The local integrity verifier confirmed a valid PDF header and trailing EOF plus substantial, structured full-paper HTML before review began.

## Related DEP Entries

1. [Hyperbolic Catenaries - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Hyperbolic%20Catenaries/hyperbolic_catenaries_manuscript.md)
   - **Source basis:** inspected processed manuscript reviewing arXiv and journal evidence for hyperbolic catenaries and minimal surfaces of revolution.
   - **Relevance:** direct differential-geometric overlap through curvature equations, explicit manifold models, equality conditions, and geometric rigidity.
2. [Flag Hardy Operators - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md)
   - **Source basis:** inspected processed manuscript reviewing boundedness of singular integrals on flag Hardy spaces over the Heisenberg group.
   - **Relevance:** methodological overlap through geometry-adapted harmonic analysis, scale structure, cancellation, and sharp integral estimates.
3. [Global NS Existence - DEP-E](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-Global%20NS%20Existence/global_ns_existence_manuscript.md)
   - **Source basis:** inspected processed manuscript reviewing global solutions for compressible Navier-Stokes flow on a bounded curved domain.
   - **Relevance:** analytic overlap through Green functions, divergence identities, geometry-sensitive estimates, and topology/boundary constraints.

## Synthesis Note

### Concept Bridge

The paper's reusable mechanism is an **analytic-to-geometric certificate**. First choose an integral quantity aligned with the manifold's geometry: a radial boundary functional for the mean value problem or a Green-level weighted volume for the curvature problem. Next prove monotonicity or an exact derivative identity whose error terms have controlled sign. Finally, use equality or an asymptotic zero defect to activate a terminal geometric theorem—Bishop-Gromov rigidity in both headline chains, with Gauss-Bonnet supplying the topological coefficient in dimension three.

This pattern makes proof translation auditable. A result is not merely “an inequality implies rigidity.” It is a sequence of typed obligations: hypotheses make the integral well-defined; divergence/coarea make scale changes legal; curvature controls the sign; topology fixes exceptional sets; and the terminal comparison theorem converts zero defect into Euclidean geometry.

### Potential Implementations

1. **Assumption-complete theorem cards** - encode every hypothesis, normalization, conclusion, equality condition, and source location; lint summaries that omit dimension, maximal volume growth, nonparabolicity, or the sign of `Δf`.
2. **Rigidity dependency graph** - map the generalized divergence theorem, monotonicity, level-set topology, Gauss-Bonnet, and Bishop-Gromov nodes into two reviewable proof chains with explicit imported results.
3. **Model-manifold verification lab** - exercise normalizations and defect terms on Euclidean space and synthetic radial metrics, reporting convergence and failed hypotheses without claiming a general proof.

### Deeper Relationship Observations

1. Hyperbolic Catenaries and the selected paper both make equality geometrically productive: one matches a weighted curve equation to zero mean curvature, while the other drives analytic or volume defects to zero and obtains Euclidean rigidity.
2. Flag Hardy Operators and the selected paper both succeed by respecting the ambient geometry in the integral quantity. Heisenberg dilations and flag scales play the same methodological role that radial Jacobians and Green-function levels play here.
3. Global NS Existence and the selected paper both use Green or divergence machinery to overcome a geometric obstruction that flat-domain reasoning cannot ignore: curved boundaries in one case and cut loci/noncompact level sets in the other.

### Conceptual Similarities

1. **Geometry-selected coordinates:** hyperbolic orbit types, Heisenberg flag scales, conformally transported Green kernels, and Green-function radii all replace naive Euclidean coordinates with structure-compatible ones.
2. **Signed defect accounting:** curvature, cancellation, commutator, Hessian, and Jacobian terms are useful because their sign or boundedness can be traced through the proof rather than hidden in a qualitative analogy.
3. **Terminal certificates:** minimality, operator boundedness, global solution control, and Euclidean rigidity each require a final condition that is stronger than intermediate numerical or symbolic similarity.

### MVP Implementations with Code Mock-ups

1. **Hypothesis linter**

~~~python
REQUIRED = {
    "mean_value": {"complete", "ricci_nonnegative", "f_nonnegative", "laplacian_nonpositive"},
    "curvature_limit": {"dimension_3", "complete", "noncompact", "ricci_nonnegative", "max_volume_growth"},
}

def missing_hypotheses(theorem, declared):
    return sorted(REQUIRED[theorem] - set(declared))

assert missing_hypotheses("curvature_limit", {
    "dimension_3", "complete", "noncompact", "ricci_nonnegative"
}) == ["max_volume_growth"]
~~~

This bounded checker detects omitted assumptions in a curated theorem card. It does not parse arbitrary mathematics or judge proof correctness.

2. **Monotonicity trace auditor**

~~~python
def audit_nonincreasing(samples, tolerance=1e-10):
    violations = []
    for left, right in zip(samples, samples[1:]):
        if right[1] > left[1] + tolerance:
            violations.append({"from": left, "to": right})
    return violations

toy_F = [(0.5, 3.0), (1.0, 2.6), (2.0, 2.6), (4.0, 2.1)]
assert audit_nonincreasing(toy_F) == []
~~~

This toy validates sampled data supplied by a model-manifold calculation. Sampling cannot establish continuum monotonicity; a production tool must keep that limitation visible.

3. **Asymptotic volume-deficit calculator**

~~~python
import math

def predicted_weighted_curvature_limit(asymptotic_volume_ratio):
    v = float(asymptotic_volume_ratio)
    if not 0.0 <= v <= 1.0:
        raise ValueError("V_M must lie in [0, 1] under the stated setting")
    return 8.0 * math.pi * (1.0 - v)

assert predicted_weighted_curvature_limit(1.0) == 0.0
~~~

This calculator evaluates the theorem's right-hand side after a valid `V_M` is supplied. It does not estimate `V_M`, verify maximal volume growth, or certify that a manifold satisfies the theorem.

### Developer Challenges

1. Preserve mathematical quantifiers, signs, dimensions, and equality conditions when extracting theorem text from formula-rich HTML or PDF sources.
2. Represent proof dependencies across smooth geometry, geometric measure theory, elliptic PDE, topology, and comparison geometry without conflating cited imports with locally proved lemmas.
3. Build numerical model checks that respect completeness, cut-locus behavior, Green-function normalization, and volume growth while clearly separating finite-sample evidence from proof.

### Author Challenges

1. Extend the exact weighted scalar-curvature identity to the broader nonparabolic setting without maximal volume growth, or identify a sharp obstruction.
2. Develop a quantitative almost-rigidity theorem that bounds metric or measured closeness to Euclidean geometry from a small mean-value or volume-curvature defect.
3. Publish a dependency map, model calculations, or formalization notes that make the generalized divergence and level-set topology arguments easier to independently audit.

## Validation Notes

- **Random selection:** `rg --files -g "*.pdf"` found 75,777 PDFs and 75,776 unique parent-directory paper units. Uniform `Get-Random` index 67,845 selected this unit.
- **Dedup:** arXiv ID, DOI, normalized title, and slug produced no prior Arxiv DEP artifact in Black Lake, automation memory, public staging, relevant Black-Lake-Data results, or the preceding 24-hour window. Exclusions: 0. Reselections: 0.
- **Initial integrity:** `partial`; valid PDF present, full-paper HTML absent.
- **Repair:** one bounded direct-arXiv companion-bundle attempt in a fresh target; no credential use, retry, or strategy switch.
- **Final integrity:** PDF 308,002 bytes with `%PDF-` and trailing `%%EOF`; full-paper HTML 952,870 bytes with 137,716 body characters, a document marker, 63 headings/sections, and five structure terms; zero partial files.
- **Schema:** manuscript YAML title and H1 are identical and under 40 characters; all mandatory manuscript headings are present; the exercise section contains exactly three entries.
- **Report counts:** exactly three related DEP entries, three potential implementations, three deeper relationship observations, three conceptual similarities, three MVP code mock-ups, three developer challenges, and three author challenges.
- **Public-safety scan:** no local absolute path, username, drive path, machine name, local timezone label, exact local execution timestamp, source file, cache, or extracted source text is included.
- **Source-upload result:** no `.source/` directory was created and no original source file is eligible for staging.
- **Remaining gap:** mathematical correctness was not formally or independently certified.

## Attribution Block

- Source URL: https://arxiv.org/abs/2602.10393
  - Applies to: this Report-Mark.
  - Notes: Canonical metadata, abstract, version, subject, DOI, license link, and artifact URLs.
- Source URL: https://arxiv.org/pdf/2602.10393
  - Applies to: this Report-Mark.
  - Notes: Complete primary paper used for theorem and proof-architecture review; verified local copy withheld.
- Source URL: https://arxiv.org/html/2602.10393
  - Applies to: this Report-Mark.
  - Notes: Official full-paper HTML used for structure and formula-aware cross-checking; verified local copy withheld.
- Source URL: https://arxiv.org/e-print/2602.10393
  - Applies to: this Report-Mark.
  - Notes: Source companion collected locally for provenance and withheld.
- Source URL: https://doi.org/10.48550/arXiv.2602.10393
  - Applies to: this Report-Mark.
  - Notes: Persistent arXiv-issued DOI.
- Source URL: https://creativecommons.org/licenses/by/4.0/
  - Applies to: this Report-Mark.
  - Notes: License deed reached from the canonical arXiv record.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Hyperbolic%20Catenaries/hyperbolic_catenaries_manuscript.md
  - Applies to: Related DEP synthesis.
  - Notes: Context for differential geometry and rigidity; not theorem evidence.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md
  - Applies to: Related DEP synthesis.
  - Notes: Context for geometry-adapted harmonic analysis; not theorem evidence.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-Global%20NS%20Existence/global_ns_existence_manuscript.md
  - Applies to: Related DEP synthesis.
  - Notes: Context for Green functions and divergence methods; not theorem evidence.
- Source-file policy: original source files were withheld locally.
  - Applies to: the complete report.
  - Notes: No PDF, HTML, source archive, cache, extracted text, local path, or machine-specific record was uploaded.
