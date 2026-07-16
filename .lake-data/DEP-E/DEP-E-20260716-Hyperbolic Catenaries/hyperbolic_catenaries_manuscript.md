---
title: "Hyperbolic Catenaries - DEP-E"
generated_at: "2026-07-16 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Version-aware review of a variational characterization of minimal surfaces of revolution in hyperbolic space."
source_status: "verified complete local PDF and full-paper HTML; metadata and TeX source inspected; public publisher HTML cross-checked; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-16"
temporal_cutoff: "arXiv v2 and publisher records available through 2026-07-16"
primary_url: "https://arxiv.org/abs/2211.15297v2"
stable_identifier: "arXiv:2211.15297v2; DOI:10.1017/prm.2024.56"
confidence_summary: "High for identity, theorem statements, version differences, and proof architecture; medium for proof correctness and numerical reproduction."
safety_scope: "non-sensitive mathematical research, educational visualization, and symbolic verification"
distribution_notes: "Date-only public provenance; local source files, paths, caches, extracted text, and machine details withheld."
---

# Hyperbolic Catenaries - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2211.15297v2 | https://arxiv.org/abs/2211.15297v2 | Public metadata; abstract is not treated as the paper | 2026-07-16 | Inspected |
| S2 | *Catenaries and minimal surfaces of revolution in hyperbolic space* | Primary paper | PDF and full-paper HTML | arXiv:2211.15297v2 | https://arxiv.org/pdf/2211.15297; https://arxiv.org/html/2211.15297 | Verified local copies inspected; no source file redistributed | 2026-07-16 | Complete paper inspected |
| S3 | arXiv e-print | Primary manuscript source | TeX/source archive | arXiv:2211.15297v2 | https://arxiv.org/e-print/2211.15297 | Formula-preserving source retained locally and extracted; not redistributed | 2026-07-16 | Archive validated and source inspected |
| S4 | arXiv-issued DOI | Persistent preprint identifier | DOI | 10.48550/arXiv.2211.15297 | https://doi.org/10.48550/arXiv.2211.15297 | Public DOI locator | 2026-07-16 | Verified from arXiv |
| S5 | Cambridge University Press version of record | Peer-reviewed publication | Publisher HTML | DOI 10.1017/prm.2024.56; volume 156, issue 1, pages 263-283 | https://doi.org/10.1017/prm.2024.56 | CC BY 4.0; inspected by URL and not downloaded | 2026-07-16 | Full open HTML and Figure 1 caption inspected |
| S6 | Black Lake repository authorities | Deposition rules | Markdown | live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Process authority, not research evidence | 2026-07-16 | Fetched and read |
| S7 | Black-Lake-Data README | Companion repository authority | Markdown | live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Read before dedup and related-context exploration | 2026-07-16 | Fetched and read |
| S8 | Flag Hardy Operators | Related processed artifact 1 of 3 | Markdown | DEP-E-20260716-Flag Hardy Operators | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md | Contextual synthesis; underlying sources separately attributed | 2026-07-16 | Inspected |
| S9 | iKalibr Calibration | Related processed artifact 2 of 3 | Markdown | DEP-E-20260714-iKalibr Calibration | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Contextual synthesis; underlying sources separately attributed | 2026-07-16 | Inspected |
| S10 | CoreMem Geometry | Related processed artifact 3 of 3 | Markdown | DEP-A-20260714-CoreMem Geometry | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-CoreMem%20Geometry/2606.18406-whitepaper-review.md | Contextual critique; underlying sources separately attributed | 2026-07-16 | Inspected |
| S11 | Integrity, cache, and dedup summaries | Process evidence | Public-safe generated records | source gate and cache schema 1.0 | Public artifact summaries only | Original source paths and private manifests withheld | 2026-07-16 | Validated |

The authors are Luiz C. B. da Silva and Rafael López. The arXiv record was submitted on 2022-11-28 and revised as v2 on 2023-06-11 under `math.DG`. The journal article was published online on 2024-05-10 and appears in the February 2026 issue of *Proceedings of the Royal Society of Edinburgh Section A: Mathematics*, volume 156, issue 1, pages 263-283. The publisher DOI is `10.1017/prm.2024.56`; the arXiv-issued DOI is `10.48550/arXiv.2211.15297`. The publisher version is open access under CC BY 4.0.

The selected archive unit initially contained a valid PDF but no full-paper HTML. Review stopped while official full-paper HTML, metadata HTML, and a TeX/source archive were collected and verified. The final source state was `complete`, with zero partial files. These source documents and all extracted text remain local; this DEP contains generated Markdown and public URLs only.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Primary metadata | Title, authors, arXiv version, submission history, category, comments, arXiv DOI, and canonical URLs | Identity and preprint chronology | High | Abstract-level evidence does not establish theorems |
| E2 | S2 | Complete primary paper | Introduction, variational setup, curvature lemmas, Killing-field characterization, three revolution types, mean-curvature derivation, main theorem, horocatenaries, and conclusion | Full arXiv v2 technical reconstruction | High for reporting | Proofs were not independently certified |
| E3 | S3 | Primary source package | TeX equations, theorem wording, comments, bibliography, and absence of figures/tables in v2 | Formula and version audit | High | Source contains dormant/commented material not part of rendered paper |
| E4 | S5 | Version of record | Journal metadata, CC license, corrected curvature scaling, explicit if-and-only-if Theorem 5.3, Figure 1 numerical examples, final conclusion | Authoritative publication context and version differences | High | Numerical curves were not reproduced; a likely equation typo remains |
| E5 | S2, S3, S5 | Cross-version primary evidence | Comparison of `-1/r` versus `-1/r²`, theorem direction, figure addition, elliptic/spherical language, and `cosh(u/u)` | Version-aware critique | High | No automated full-text semantic diff was performed |
| E6 | S8 | Related DEP | Heisenberg dilation, flag geometry, scale-compatible proof mechanism | Symmetry-adapted analysis bridge | Medium | Contextual only; no support for this paper's theorem |
| E7 | S9 | Related DEP | Continuous-time `SO(3)` curves, gauge selection, geometric residuals, observability | Lie-group and coordinate-gauge bridge | Medium | Engineering context differs from minimal-surface theory |
| E8 | S10 | Related DEP | Audit showing global covariance reweighting is not demonstrated Fisher-Rao geometry | Negative comparison for geometric-claim rigor | Medium-high | Contextual critique, not primary evidence for this paper |
| E9 | S11 | Process evidence | Uniform random draw, dedup scans, source repair metrics, extractor preflight, cache outputs, and source-upload policy | Selection eligibility and review preconditions | High | Private manifests and local paths intentionally omitted |

## Executive Summary

Da Silva and López construct a hyperbolic counterpart of the Euclidean catenary-catenoid relationship. In Euclidean space, a hanging chain is a critical point of gravitational potential and its revolution is a minimal catenoid. A catenary defined only through intrinsic distance in the hyperbolic plane does not preserve that link. The paper restores it by defining an **extrinsic catenary**: a curve in the hyperbolic plane that is critical for a weighted-length functional whose weight is ambient Lorentz-Minkowski distance to the two-plane fixed by a rotation group.

The hyperboloid model makes three cases unavoidable. A Lorentzian, Riemannian, or degenerate fixed plane produces elliptic, hyperbolic, or parabolic rotations. Each case has a different distance weight and therefore a different curvature equation. The paper first derives these equations from Euler-Lagrange analysis, then derives an independent set of curvature conditions by setting the mean curvature of the matching surface of revolution to zero. The expressions coincide. The journal version states the central result cleanly: a surface of revolution in hyperbolic three-space is minimal if and only if its generating curve is an extrinsic catenary of the corresponding type.

The work also separates coordinate machinery from invariant meaning. For a general weight `f`, a critical curve satisfies `κ = -<n,∇f>/f`. When `f` is distance to the reference plane, its gradient is the tangential part of an ambient Killing field. This turns the Euler-Lagrange equation into a compact geometric law relating curvature, normal direction, and the symmetry that defines the weight.

Only the elliptic family receives an intrinsic reformulation. In horo-geodesic coordinates, distance measured along horocycles orthogonal to a reference geodesic equals the relevant ambient height, so horocatenaries coincide with elliptic extrinsic catenaries. Whether hyperbolic and parabolic families admit comparable model-independent formulations remains open.

Confidence is high that this artifact accurately reports the source identity, equations, theorem structure, journal metadata, and explicit open questions because complete arXiv v2 PDF/HTML/TeX and the open publisher HTML were inspected. Confidence is medium for proof correctness and numerical behavior: the argument was not formalized, Figure 1 was not reproduced, and no official solver code or initial conditions were identified. The version-of-record fixes one preprint scaling error but still appears to contain `cosh(u/u)` where the surrounding derivation requires `cosh(u/r)`.

## Detailed Summary

### Problem Context

The classical catenary minimizes gravitational potential among chains of fixed length with fixed endpoints. Its revolution about the reference line is a surface with zero mean curvature. This equivalence makes a one-dimensional variational problem and a two-dimensional geometric PDE different views of the same object.

Hyperbolic geometry complicates the analogy. An intrinsic catenary can be defined by weighting arc length with intrinsic distance to a geodesic, but revolving that curve does not generally yield a minimal surface in hyperbolic three-space. The authors therefore ask which curve functional produces the correct generators for hyperbolic minimal surfaces of revolution.

### Hyperboloid Model and Causal Types

The paper represents hyperbolic `n`-space of radius `r` as the upper sheet

`H^n(r) = {X in E_1^(n+1) : <X,X>_1 = -r², X_0 > 0}`,

with the metric induced by the Lorentz-Minkowski bilinear form. The journal version correctly states constant sectional curvature `-1/r²`.

A surface of revolution is generated by a one-parameter subgroup of ambient Lorentz transformations that fixes a two-dimensional plane `P²` pointwise. The restricted metric on `P²` can be:

- Lorentzian, producing elliptic rotations and ellipse-like orbits;
- Riemannian, producing hyperbolic rotations and hyperbola-like orbits; or
- degenerate, producing parabolic rotations and parabola-like orbits.

This classification determines both the surface family and the curve's potential weight.

### Semi-Geodesic Coordinates and the Weighted Functional

The authors choose semi-geodesic coordinates `ψ(u,v)` on `H²(r)`, with metric

`ds² = du² + cosh²(u/r) dv²`.

For canonical representatives of the three plane types, ambient distance is proportional to:

| Type | Weight `f(u,v)` |
|---|---|
| Elliptic | `sinh(u/r)` |
| Hyperbolic | `cosh(u/r) cosh(v/r)` |
| Parabolic | `exp(-v/r) cosh(u/r)` |

The functional is

`W[γ] = ∫ f(u,v) sqrt(u_dot² + cosh²(u/r) v_dot²) dt`.

The source assumes the curve remains on one side of the plane so the weight is positive. A later remark notes that fixing the chain length introduces a Lagrange multiplier; geometrically, adding the multiplier corresponds to translating the reference plane.

### Curvature Characterization

The technical bridge is a general lemma for weighted length. If `γ` is a regular curve with unit normal `n`, then criticality of `∫ f ds` is equivalent to

`κ = -<n, grad f>/f`.

Substituting the three weights yields explicit elliptic, hyperbolic, and parabolic curvature laws. These are second-order ODE constraints once the semi-geodesic curvature expression is expanded.

The coordinate-free theorem identifies `grad f` with the tangential part of the ambient Killing field whose integral curves connect the point to the fixed plane. Therefore:

`κ(t) = -<n(t), X(t)> / dist(γ(t),P²)`.

This formulation explains the physics analogy. The Killing field gives the direction of the effective “gravity,” the denominator gives the height-like weight, and the curve bends in proportion to the normal component of that direction.

### Surfaces of Revolution and Mean Curvature

The paper writes explicit Lorentz-transformation matrices for the elliptic, hyperbolic, and parabolic one-parameter groups. Acting on a generating curve in a totally geodesic copy of `H²(r)` produces three surface parametrizations.

For each surface, the authors compute first and second fundamental forms and derive mean-curvature formulas. They then express the curvature of a general curve in the hyperbolic plane using a Lorentzian vector product and substitute that expression into the zero-mean-curvature equations.

The result is a three-case proposition: minimality is equivalent to a type-specific curvature law for the generating curve. When the generating curve is rewritten in semi-geodesic coordinates, these laws match the earlier Euler-Lagrange equations.

### Main Equivalence

Journal Theorem 5.3 states the result in its strongest form:

> A surface of revolution in `H³(r)` is minimal of elliptic, hyperbolic, or parabolic type if and only if its generating curve is an extrinsic catenary of the same type.

The proof is an identity comparison, not an existence theorem. It assumes a regular generating curve away from the fixed plane, computes both conditions, and observes equality of the curvature expressions. It does not prove that arbitrary endpoints admit a solution, that a solution is unique, that critical curves globally minimize the potential, or that the resulting surface is complete, embedded, or stable.

### Horocatenary Reformulation

The final geometric construction replaces distance along geodesics with length along horocycles orthogonal to a reference geodesic. A lightlike rotation generates horocycles and supplies coordinates with metric

`g = exp(-2v/r) du² + dv²`.

The horocycle distance from `φ(u,v)` to the reference geodesic is

`d_h = u exp(-v/r)`.

This quantity is also the relevant ambient height, so the horocatenary functional agrees with the elliptic extrinsic-catenary functional after the coordinate change. The paper concludes that every hyperbolic horocatenary is an elliptic extrinsic catenary and therefore generates an elliptic minimal surface of revolution.

### Conservation and Open Problems

The elliptic Lagrangian does not depend on `v`, so its conjugate momentum is conserved. The authors express this as a Clairaut-like relation:

`0.5 sinh(2u/r) cos(θ) = constant`.

No obvious first integral is given for the hyperbolic or parabolic cases. The paper asks whether this absence is intrinsic or an artifact of coordinates. It also asks whether the remaining two families admit intrinsic, model-independent characterizations and whether similar ideas extend to minimal surfaces of revolution in the three-sphere.

### Publisher-Version Evidence

The peer-reviewed version improves the preprint in several ways:

- it states the central theorem as a true equivalence;
- it corrects the constant-curvature factor from `-1/r` to `-1/r²`;
- it adds a motivating minimality section before the variational construction; and
- it adds Figure 1 with numerical examples of all three surface types in the Poincaré ball.

The caption says the generating curves were found by numerically equating the generic curvature formula with the extrinsic-catenary equation. The inspected page does not supply an initial-condition table, solver tolerance, code link, or data-availability statement, so the numerical examples remain illustrative rather than reproducible in this review.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Ambient distance to the fixed plane produces three weighted curve functionals indexed by causal type. | Author derivation | E2, E3 | The explicit plane representatives and distance formulas support the classification. | High |
| C2 | Critical curves of `∫ f ds` satisfy `κ = -<n,∇f>/f`. | Author theorem | E2, E3 | The coordinate derivation is compact and consistent with the first variation of weighted length. | High for reporting |
| C3 | Extrinsic catenaries admit a Killing-field curvature characterization. | Author theorem | E2, E3 | The proof identifies each distance gradient with the tangential projection of the corresponding ambient field. | High for reporting |
| C4 | Minimal surfaces of revolution are equivalent to matching extrinsic-catenary generators. | Author theorem | E2-E5 | Journal Theorem 5.3 states if and only if; the proof matches independent curvature formulas. | High for source reporting; medium for independent correctness |
| C5 | Elliptic extrinsic catenaries admit an intrinsic horocycle-distance characterization. | Author theorem | E2-E4 | The equality between horocycle length and ambient height supports the equivalence. | High for reporting |
| C6 | The elliptic family has a Clairaut-like conserved quantity. | Author observation | E2-E4 | Independence of the `v` coordinate gives a standard Noether/first-integral mechanism. | High |
| C7 | Similar first integrals and intrinsic characterizations for the other two families remain unresolved. | Source-disclosed open problem | E2, E4 | Explicitly posed in both conclusions. | High |
| C8 | The journal version materially supersedes arXiv v2 for wording and exposition. | Reviewer comparison | E5 | Supported by corrected scaling, explicit equivalence, and added numerical figures. | High |
| C9 | `cosh(u/u)` is likely a typographical defect. | Reviewer inference | E3-E5 | It is dimensionally inconsistent and conflicts with adjacent factors, but no erratum was found. | Medium-high |
| C10 | The transferable engineering idea is to derive weights and constraints from actual symmetry, not geometric branding. | Reviewer synthesis | E6-E8 | Strong conceptual bridge across the three related records; not a paper theorem. | Medium-high |

## Methodology

- `Research objective`: preserve a source-grounded, version-aware account of how extrinsic catenaries characterize minimal hyperbolic surfaces of revolution, while identifying proof, notation, numerical, and implementation boundaries.
- `Sources inspected`: complete arXiv v2 PDF, official full-paper HTML, TeX/source archive through a local extraction cache, arXiv metadata, arXiv DOI, open Cambridge publisher HTML, live repository authorities, and exactly three related Black Lake artifacts.
- `Discovery strategy`: enumerate PDF-backed archive units with `rg`, sample uniformly with `Get-Random`, deduplicate by stable identifiers and artifacts, verify/repair local source integrity, run extractor preflight and missing-only caching, inspect section/theorem/equation structure, search exact-title publisher and code surfaces, then compare the preprint with the version of record.
- `Inclusion criteria`: primary and near-primary sources directly identifying the paper, its full argument, publication status, source version, figures, or related geometric mechanism; related DEP records required a concrete conceptual bridge.
- `Exclusion criteria`: abstract-only evidence for technical claims, unverified source files, generic geometry records without a specific relationship, and secondary summaries not needed for source discovery.
- `Analytical approach`: conceptual, comparative, implementation, replication, and proof-structure analysis.
- `Evidence handling`: major claims were assigned evidence IDs; author theorems, reviewer inferences, version differences, and implementation translations are labeled separately.
- `Uncertainty handling`: unreproduced proofs and numerics are marked; likely typos are not silently corrected; missing code and intrinsic characterizations remain visible.
- `Extraction process`: extractor preflight found `pypdf` but not `pdftotext`; missing-only extraction used `pypdf`, `html-regex`, and `tarfile`, producing PDF, HTML, and source text in a private central cache.
- `Version control`: arXiv v2 is the complete locally archived source; the 2024 online/2026 issue publisher version is authoritative for final theorem wording and publication metadata.
- `Reviewer stance`: DEP-ready preservation, mathematical reconstruction, version critique, and bounded research-to-tool translation.

### Random Selection, Cache, and Dedup Methodology

The archive contained 75,777 PDF paths grouped into 75,776 unique parent-directory paper units. A uniform zero-based index was drawn from the complete array; index 43,368 selected this paper. The first draw passed dedup, so exclusions and reselections were both zero.

Dedup checked arXiv ID, arXiv DOI, journal DOI, normalized title, and slug across the public dedup index, Black Lake logs/reports/deposits, automation memory, Black-Lake-Data search results, and active worktrees. The only companion-repository hit was a metadata-only author inventory row, not a deposition.

The local source state was initially `partial` because a valid PDF existed without full-paper HTML. After bounded repair and verification, the source state became `complete`. Cache lookup was a miss. A `missing-only` run used only the repaired local bundle and finished as `cached` with PDF, HTML, and source text present. No source file or cache output was copied into the public repository.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv v2, the open version of record, the variational and mean-curvature mechanism, source-disclosed open questions, version differences, and bounded implementation translations.
- `Temporal boundary`: sources inspected through 2026-07-16.
- `Evidence limits`: no formal proof assistant, independent referee report, official solver repository, initial-condition manifest, or numerical reproduction.
- `Assumptions`: the publisher's formal Theorem 5.3 is the authoritative statement; `cosh(u/u)` is treated as a probable typo rather than a new mathematical term; conventional Lorentzian sign choices match the source.
- `Constraints`: source files and caches must remain local; public records use date-only provenance and omit private paths, machine data, exact execution timestamps, and local timezone labels.
- `Out of scope`: proving new existence or stability theorems, solving the boundary-value problem, reproducing Figure 1, classifying all hyperbolic minimal surfaces, or deploying a production geometry solver.
- `Intended use`: durable research deposition, proof-review backlog, educational tooling, and version-aware mathematical QA.
- `Audience`: differential geometers, mathematical software developers, formalization researchers, and engineers using manifold or Lie-group language.
- `Reproducibility boundary`: source-level statements and formulas are reproducible from public paper URLs; proof correctness and numerical surfaces are not independently certified here.
- `Data sensitivity`: public mathematical research; no personal, regulated, or proprietary dataset is involved.

## Observations

- `Observed pattern`: the same curvature law emerges from two independent constructions—first variation of weighted length and zero mean curvature of a revolved surface.
- `Technical implication`: the ambient model is not merely a convenient coordinate system; it supplies the distance weight, causal classification, and Killing field needed for the equivalence.
- `Version observation`: peer review improved theorem wording and corrected a dimensional curvature factor, but at least one likely formula typo survived into the version of record.
- `Boundary observation`: “critical point” is weaker than “minimizer.” The paper establishes stationary equations, not global energy optimality under arbitrary endpoint constraints.
- `Open question`: the missing intrinsic descriptions for hyperbolic and parabolic types mark the exact point where the result remains model-dependent.
- `Reviewer hypothesis`: the right route to additional first integrals is likely to search for hidden one-parameter symmetries or alternative coordinates before attempting brute-force integration.
- `Cross-DEP pattern`: Flag Hardy Operators, iKalibr, and this paper all succeed when they retain the symmetry of the underlying space; CoreMem's audit shows what happens when geometric language is not matched by geometric structure.

## Considerations

Theoretical users should separate four claims that can easily be conflated: existence of stationary curves, global minimality of the weighted functional, zero mean curvature of a generated surface, and global stability of that surface. The paper directly establishes the equivalence between stationarity and zero mean curvature for regular generators of the defined revolution types. It does not establish all four.

Implementers must treat Lorentzian distance carefully. The ambient bilinear form is indefinite, and a degenerate fixed plane cannot be handled by a generic positive-definite norm. Numerical code needs explicit signature checks, constraint preservation on the hyperboloid, chart transitions or stable global parameterizations, and tests near axes where denominators vanish.

Version control is a mathematical requirement here. A system that ingests only arXiv v2 will preserve a curvature scaling error and miss the journal's explicit equivalence and numerical figure. A system that reads only the journal will still need to flag `cosh(u/u)`. Equation-level provenance should therefore include version, section, and formula identity.

Educational visualization is the safest first implementation. It can expose orbit types, weights, generating curves, and mean-curvature residuals without claiming new theorems. A production symbolic verifier or numerical solver would require mathematician review, convergence evidence, golden cases, and rigorous treatment of singular regimes.

## Strengths

- The central problem is precise and historically motivated by the catenary-catenoid relationship.
- The causal classification of fixed planes gives a principled three-way decomposition rather than an arbitrary taxonomy.
- The paper derives the curve condition and the surface condition independently before matching them.
- The general formula `κ = -<n,∇f>/f` is compact, reusable, and geometrically interpretable.
- The Killing-field formulation clarifies how ambient symmetry determines the effective force direction.
- The paper is self-contained enough to reconstruct the three revolution matrices and mean-curvature calculations.
- The horocatenary section isolates a genuine intrinsic result and clearly identifies what remains model-dependent.
- The publisher version is open access, peer reviewed, more explicit about equivalence, and includes numerical examples.
- The conclusion names concrete research gaps rather than presenting the framework as complete.

## Weaknesses

- ArXiv v2 states `-1/r` instead of the correct sectional curvature `-1/r²`; the publisher fixes this.
- Both versions appear to retain `cosh(u/u)` in a central hyperbolic identity.
- Elliptic and spherical terminology is inconsistent in headline wording.
- The source often uses optimization language while proving criticality rather than global minimization.
- No endpoint existence, uniqueness, completeness, embeddedness, or stability theorem is supplied for the new variational formulation.
- Hyperbolic and parabolic types lack obvious first integrals and intrinsic characterizations.
- The journal numerical figure is not accompanied by inspected solver code, initial conditions, tolerances, or residual tables.
- The proof is algebraically dense and would benefit from symbolic regression tests for the three cases.
- The locally archived arXiv source predates the publisher's improved exposition and figures, increasing cross-version review cost.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish an erratum or corrected source | Equation quality | `cosh(u/u)` and elliptic/spherical wording remain confusing | Removes ambiguity from the main equivalence proof | Editorial overhead | Compare corrected formula with direct symbolic substitution |
| Release numerical scripts and manifests | Reproducibility | Figure 1 lacks inspected initial conditions and solver settings | Enables independent surface reconstruction | Code maintenance and dependency drift | Reproduce all three panels and report mean-curvature residuals |
| Prove boundary-value existence and uniqueness regimes | Variational theory | Critical equations do not guarantee a solution for arbitrary endpoints | Clarifies when the hanging-chain problem is well posed | Substantial analysis | Establish coercivity/compactness or shooting-map results under explicit domains |
| Analyze second variation and stability | Geometry | Zero mean curvature does not imply stability | Connects generators to physically and geometrically meaningful surfaces | Spectral analysis can be difficult | Derive Jacobi operator and compare with known rotational surfaces |
| Search for intrinsic weights for two remaining types | Model independence | Hyperbolic and parabolic cases depend on the hyperboloid embedding | Extends the strongest conceptual result | May face genuine obstructions | Characterize candidate foliations and prove equality or impossibility |
| Derive conserved quantities systematically | Integrability | Only elliptic cyclic symmetry is obvious | Improves solvability and qualitative phase portraits | Hidden symmetries may not exist | Apply Noether analysis across alternative charts |
| Add machine-checkable dimension/sign tests | Proof QA | Lorentzian signs and radius scaling are easy to mistype | Prevents silent algebra defects | Symbolic convention management | Golden tests at canonical curves and `r=1` |

## Potential Implementations

1. **Symbolic Extrinsic-Catenary Auditor**
   - `User`: differential geometers and journal reviewers.
   - `Goal`: verify the three Euler-Lagrange/mean-curvature identities and detect sign, radius, or variable-substitution errors.
   - `Core mechanism`: represent the hyperboloid constraint, semi-geodesic chart, weights, rotation matrices, fundamental forms, and simplification assumptions in a computer algebra system.
   - `Required inputs`: formula version, causal type, radius symbol, chart definitions, and regularity assumptions.
   - `Outputs`: normalized identities, dimensional warnings, proof traces, and version diffs.
   - `Risk controls`: never equate symbolic simplification with a full theorem proof; expose assumptions and denominators.
   - `Evaluation`: canonical-plane golden cases, random constraint-preserving substitutions, and regression tests for known typos.

2. **Hyperbolic Revolution Explorer**
   - `User`: students and geometry researchers.
   - `Goal`: visualize how the three weighted curve equations generate minimal surfaces.
   - `Core mechanism`: integrate a selected curvature ODE, embed the curve in the hyperboloid, apply the matching one-parameter group, project into the Poincaré ball, and compute a numerical mean-curvature residual.
   - `Required inputs`: type, radius, initial point/tangent, integration interval, solver tolerance, and projection choice.
   - `Outputs`: curve, surface mesh, orbit classification, residual plot, and reproducibility manifest.
   - `Risk controls`: enforce the hyperboloid constraint, stop near singular denominators, and label results numerical.
   - `Evaluation`: convergence under step refinement, constraint residual, mean-curvature residual, and comparison with publisher Figure 1.

3. **Geometry-Claim Review Gate**
   - `User`: research engineers reviewing software that invokes manifold geometry.
   - `Goal`: distinguish genuine geometric construction from renamed Euclidean scoring.
   - `Core mechanism`: require a claim card containing manifold, metric, group action, coordinates, invariant quantity, and empirical or symbolic verification.
   - `Required inputs`: manuscript equations, implementation pseudocode, dimensions, and claimed invariances.
   - `Outputs`: pass/warn/fail findings with missing-definition and dimension-mismatch traces.
   - `Risk controls`: advisory only; domain experts decide mathematical validity.
   - `Evaluation`: positive case from extrinsic catenaries, engineering case from iKalibr, and negative case from the CoreMem geometry audit.

## Three Ways to Exercise This Research

1. **Equation identity check**: Objective: reproduce the elliptic equivalence algebraically. Inputs: the semi-geodesic parametrization, elliptic weight, and minimal-surface curvature formula. Method: differentiate symbolically, apply the hyperboloid constraint, and simplify both expressions. Output: a traceable equality report. Success criterion: both sides reduce to the same normalized expression with stated nonzero denominators. Stop condition: an assumption or symbol cannot be reconciled across versions.
2. **Bounded numerical curve**: Objective: recreate one publisher-style surface without claiming a theorem. Inputs: `r=1`, one causal type, explicit initial point/tangent, finite interval, and tolerances. Method: integrate the curvature ODE, revolve the curve, project to the Poincaré ball, and measure constraint and mean-curvature residuals. Output: mesh, manifest, and residual plots. Success criterion: residuals converge under refinement and the solver never crosses a singular axis. Stop condition: constraint drift or residual growth exceeds the declared tolerance.
3. **Geometry-language audit**: Objective: test whether a “Riemannian” software method supplies actual geometry. Inputs: a public method description and equations. Method: identify the manifold, metric, connection or distance, group action, coordinate dependence, and claimed invariant; compare dimensions and transformations. Output: an evidence card with unsupported claims. Success criterion: every geometric term has a checkable definition or is explicitly downgraded to analogy. Stop condition: primary equations or implementation dimensions are unavailable.

## Example MVP Product

- `Product name`: HyperCat Lab
- `Target user`: differential-geometry students, researchers, and symbolic-computation developers.
- `Problem`: the paper's central equivalence is algebraically dense, version-sensitive, and difficult to inspect or visualize from prose alone.
- `Core workflow`: choose elliptic, hyperbolic, or parabolic type; inspect the corresponding plane signature and weight; enter validated initial conditions; integrate the generator; revolve it; project it; compute constraint and mean-curvature residuals; export a versioned Markdown/JSON evidence report.
- `Data requirements`: public equations, explicit initial conditions, solver configuration, and optional reference meshes. No private or personal data.
- `Architecture`: local Python application; symbolic layer for formulas; numerical ODE layer; Lorentzian geometry primitives; deterministic renderer; report generator; golden-test suite.
- `Success metrics`: zero unsupported geometry labels; deterministic manifests; hyperboloid constraint below tolerance; decreasing mean-curvature residual under refinement; successful reproduction of at least one example per causal type; reviewer approval of conventions.
- `Risk controls`: local-only operation, bounded integration intervals, singularity stops, visible assumptions, no claim of formal proof, and explicit distinction between criticality, minimality, and stability.
- `Limitations`: does not prove existence, uniqueness, completeness, embeddedness, or stability; may fail near degenerate regimes; depends on sign and chart conventions.
- `MVP boundary`: one curve and one surface at a time; no global moduli-space search, theorem proving, or production CAD export.
- `Deployment model`: local notebook or desktop visualization tool.
- `Evaluation plan`: canonical plane signatures, `r=1` sanity checks, symbolic regression for theorem equations, convergence tests, malformed-input tests, and comparison with the publisher figure.
- `Failure modes`: Euclidean norm substitution, wrong Lorentzian sign, variable typo, axis crossing, stiff integration, projection blow-up, or a visually plausible surface with large mean-curvature residual.
- `Maintenance plan`: pin source versions, version mathematical conventions, preserve regression cases, and require expert sign-off before formula updates.

## Related Research and Reading

### Exactly Three Related DEP Entries

| Entry | Concrete overlap | Source basis |
|---|---|---|
| [Flag Hardy Operators](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md) | Non-Euclidean symmetry and anisotropic group structure determine the correct analytic decomposition, paralleling causal orbit types and Killing fields here. | Source metadata, executive summary, Heisenberg dilation, flag geometry, and proof-mechanism sections inspected |
| [iKalibr Calibration](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md) | Continuous-time curves on `SO(3)`, Lie algebra maps, coordinate gauges, and invariant geometric residuals provide an engineering analogue. | Source metadata, continuous-time state representation, gauge choice, observations, and implementation notes inspected |
| [CoreMem Geometry](https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-CoreMem%20Geometry/2606.18406-whitepaper-review.md) | Negative comparison showing that covariance whitening is not automatically Fisher-Rao/Riemannian geometry; the selected paper supplies an explicit manifold, metric, and symmetry group. | Executive assessment, covariance construction, dimension audit, and geometric-terminology critique inspected |

### Primary and Near-Primary Reading

| Item | Type | Relevance | URL / Identifier |
|---|---|---|---|
| Da Silva and López, *Catenaries in Riemannian Surfaces* | Direct related work | Extends catenary ideas across Riemannian surfaces and supplies the Clairaut-like context | https://doi.org/10.1007/s40863-023-00399-z |
| Mori, *Minimal surfaces of revolution in H³ and their global stability* | Foundational result | Prior elliptic rotational minimal surfaces and stability context | https://doi.org/10.1512/iumj.1981.30.30057 |
| do Carmo and Dajczer, *Rotation hypersurfaces in spaces of constant curvature* | Foundational classification | Source for rotation types and their relationship to helicoids | https://doi.org/10.1090/S0002-9947-1983-0694383-X |
| Izumiya, *Horospherical geometry in the hyperbolic space* | Geometric background | Horocycles and horospherical geometry used by the intrinsic reformulation | *Advanced Studies in Pure Mathematics* 55 (2009), 31–49 |
| Cambridge version of record | Primary published work | Final theorem wording, corrected curvature scaling, numerical examples, and publication status | https://doi.org/10.1017/prm.2024.56 |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2211.15297v2 | Identity, authors, dates, category, abstract, source links, arXiv DOI | 2026-07-16 | Primary metadata |
| R2 | https://arxiv.org/pdf/2211.15297 | Complete arXiv v2 theorem and proof review | 2026-07-16 | Verified local copy withheld |
| R3 | https://arxiv.org/html/2211.15297 | Full-paper structural and formula cross-check | 2026-07-16 | Verified local copy withheld |
| R4 | https://arxiv.org/e-print/2211.15297 | TeX-level formulas, comments, and bibliography | 2026-07-16 | Validated local archive withheld |
| R5 | https://doi.org/10.48550/arXiv.2211.15297 | Persistent arXiv identifier | 2026-07-16 | Metadata only |
| R6 | https://doi.org/10.1017/prm.2024.56 | Version-of-record metadata, final theorem, Figure 1, corrections, conclusion, and CC license | 2026-07-16 | Open publisher HTML inspected |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | DEP and source-withholding authority | 2026-07-16 | Live README fetched |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E container and publication-index authority | 2026-07-16 | Live filing README fetched |
| R9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository and dedup context | 2026-07-16 | Live README read |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md | Related non-Euclidean symmetry synthesis | 2026-07-16 | Context only |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-iKalibr%20Calibration/ikalibr_calibration_manuscript.md | Related Lie-group and gauge synthesis | 2026-07-16 | Context only |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260714-CoreMem%20Geometry/2606.18406-whitepaper-review.md | Negative geometry-claim comparison | 2026-07-16 | Context only |
| R13 | https://doi.org/10.1007/s40863-023-00399-z | Related catenary theory | 2026-07-16 | Near-primary reading |
| R14 | https://doi.org/10.1512/iumj.1981.30.30057 | Rotational minimal surfaces and stability background | 2026-07-16 | Foundational reading |
| R15 | https://doi.org/10.1090/S0002-9947-1983-0694383-X | Rotation hypersurface classification | 2026-07-16 | Foundational reading |

## Appendix

### Replication Checklist

- Pin arXiv:2211.15297v2 and DOI `10.1017/prm.2024.56` as separate source versions.
- Define the Lorentz-Minkowski sign convention and hyperboloid radius before symbolic work.
- Verify the corrected sectional curvature `-1/r²`.
- Encode the semi-geodesic parametrization and induced metric.
- Recompute distance weights for canonical Lorentzian, Riemannian, and degenerate planes.
- Derive the weighted-length Euler-Lagrange equation for a generic `f`.
- Confirm `κ = -<n,∇f>/f` under the stated normal convention.
- Verify each distance gradient against the tangential ambient Killing field.
- Recompute first and second fundamental forms for all three revolution matrices.
- Match zero mean curvature to the three extrinsic-catenary curvature equations.
- Replace or resolve the apparent `cosh(u/u)` defect explicitly; do not silently assume it.
- Publish numerical initial conditions, integration intervals, solver, tolerances, and stopping rules.
- Check hyperboloid constraint and mean-curvature residual under mesh/step refinement.
- Record whether curves approach the fixed plane or ideal boundary and how singularities are handled.
- Analyze second variation or state clearly that only stationarity is demonstrated.

### Process and Source Inventory

- Uniform selection: 75,776 paper units; first draw; zero-based index 43,368; zero exclusions; zero reselections.
- Dedup: no prior artifact marker; one metadata-only author-inventory row did not exclude the paper.
- Initial integrity: partial because full-paper HTML was absent.
- Final integrity: complete verified PDF and full-paper HTML, metadata HTML present, validated TeX/source archive, zero partial files.
- Cache: initial miss; `missing-only`; final `cached`; `pypdf`, `html-regex`, and `tarfile` succeeded.
- Public distribution: generated Markdown and derived index metadata only.
- Withheld: PDF, full-paper HTML, metadata HTML, TeX/source archive, extracted text, private manifests, caches, source paths, and machine-specific records.

### Version Difference Register

| Topic | arXiv v2 | Publisher version | Review treatment |
|---|---|---|---|
| Sectional curvature | `-1/r` | `-1/r²` | Publisher correction is authoritative |
| Main theorem | Headline wording emphasizes generators are catenaries | Formal Theorem 5.3 states if and only if | Use publisher theorem |
| Examples | No figures or tables in inspected source | Figure 1 shows three numerical surface types | Report as illustrative, not reproduced |
| Type wording | “spherical” appears in headline theorem | Formal theorem uses “elliptic” | Normalize to elliptic and note synonym inconsistency |
| Hyperbolic identity | Apparent `cosh(u/u)` | Apparent `cosh(u/u)` persists | Flag as unresolved probable typo |

### Source-Withholding Confirmation

No `.source/` directory exists in this DEP. No PDF, HTML, source archive, extracted source text, cache record, private manifest, or local archive path was staged, committed, pushed, or attached to Slack. Public arXiv and DOI URLs provide the source locators.
