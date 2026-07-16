# Hyperbolic Catenaries as Symmetry-Weighted Geodesic Variational Problems

## A whitepaper-grade archival intake review and independent re-conceptualization of the complete Hyperbolic Catenaries DEP-E record

**Artifact prepared:** 2026-07-16

**Source DEP-E:** `.lake-data/DEP-E/DEP-E-20260716-Hyperbolic Catenaries`

**Source commit:** `b5ad2459a6ee3d649feb8209d9390d86d475502c`

**Paired task indicator:** `BL-DEPPAIR-20260716-BE15A671`

**Direction:** `DEP-E -> DEP-A`

**Source provenance:** review-only; source DEP modified: no; files moved: no; existing files copied into DEP-A: no; new derived data generated: yes

**Review scope:** complete two-file DEP-E repository record, canonical arXiv identity and abstract, variational and geometric reconstruction, claim vetting, numerical audit, independent re-conceptualization, and falsification agenda

**Reproduction boundary:** the current intake did not independently re-read the external full paper, verify every proof, integrate the ODEs, or reproduce the publisher’s numerical figure. Detailed theorem and equation content is attributed to the DEP-E report, which records complete arXiv and publisher-source inspection.

---

## Executive assessment

The source record reviews Luiz C. B. da Silva and Rafael López’s construction of extrinsic catenaries in the hyperbolic plane and their relation to minimal surfaces of revolution in hyperbolic three-space.[^paper] The classical Euclidean catenary minimizes potential energy when height and arc length define a weighted-length functional. Hyperbolic space has no unique global “vertical” direction of the same kind. The paper resolves this by working in the hyperboloid model embedded in Lorentz–Minkowski space and measuring extrinsic distance to a chosen plane through the ambient origin.

The reference plane’s Lorentzian normal can be timelike, spacelike, or lightlike. These causal types produce elliptic, hyperbolic, and parabolic catenary families. The DEP-E reconstructs a common variational equation: for a positive weight `f` induced by the relevant ambient coordinate or distance, a critical curve satisfies a prescribed geodesic-curvature relation of the form `kappa = -<n, grad f>/f`. The corresponding first integral arises from a Killing symmetry. Rotating the curve about the geodesic or ideal structure selected by the same plane yields a surface whose area reduces to the same weighted-length functional; minimality is therefore equivalent to the generator being the appropriate extrinsic catenary.

This is a theorem-driven contribution. The numerical curves shown in the publisher version illustrate solutions but are not the evidentiary basis of the main equivalence. The DEP-E notes that the publisher record fixes curvature normalization at `-1/r^2`, strengthens the presentation of the “if and only if” statement, and adds a numerical figure. It also identifies a likely typographical expression, `cosh(u/u)`, that appears dimensionally or algebraically suspicious and persists across versions as reported.

Reviewer judgment: the record supports a coherent geometric mechanism. The causal classification is not three arbitrary cases; it is the conjugacy classification of symmetry types inherited from the ambient Lorentzian model. The strongest independent re-conceptualization is a symmetry–orbit-weight principle: the same Killing field that generates a surface of revolution determines the orbit-size factor in the reduced area, and that factor becomes the catenary’s weight. The source does not establish global existence, uniqueness, stability, embeddedness, or global minimization for every initial condition, and the intake preserves those limits.

## 1. Problem framing and research question

In Euclidean space, a catenary can be defined variationally by minimizing a weighted length where the weight is height above a reference plane. Revolving the curve about an axis produces a catenoid, and the weighted-length functional corresponds to surface area after symmetry reduction. In hyperbolic space, “height” depends on the model and the selected reference. Intrinsic distance to a geodesic is one option, but it does not exhaust the symmetry types available in the hyperboloid model.

The paper asks how to define a catenary using an extrinsic ambient notion that remains geometrically meaningful and how such curves characterize rotational minimal surfaces. The ambient space is Lorentzian. Hyperbolic space appears as a sheet of a quadratic hyperboloid, and planes through the origin intersect it according to the causal type of their normal. These intersections and their stabilizer groups distinguish elliptic rotations around a geodesic, hyperbolic rotations around a spacelike structure, and parabolic rotations fixing an ideal point.

The research question has three parts. First, what weighted functional defines the curve for each reference-plane type? Second, what local differential equation and first integral characterize its critical points? Third, does revolution under the matching one-parameter isometry group produce a minimal surface exactly when the profile is such a critical curve?

The source further asks whether any extrinsic family has an intrinsic reformulation. The DEP-E reports that the elliptic horocatenary case can be interpreted through intrinsic lengths of horocycles orthogonal to a reference geodesic, providing a bridge between ambient-coordinate weighting and intrinsic hyperbolic geometry.

## 2. Formal and technical reconstruction

### 2.1 Hyperboloid model and causal planes

Let hyperbolic space of radius `r` be represented by vectors `x` in Lorentz–Minkowski space satisfying `<x,x>_L = -r^2` with a chosen time orientation. A plane through the origin can be represented by a normal vector `a`, and the scalar `<x,a>_L` supplies an ambient coordinate. The sign of `<a,a>_L` classifies `a` as timelike, spacelike, or lightlike. Under Lorentz isometries, each class can be normalized to a standard representative, which is why three canonical variational problems suffice.

The intersection of the reference plane or its associated orthogonal structure with the hyperboloid determines the axis or limiting object for revolution. Elliptic rotations have compact circular orbits around a geodesic. Hyperbolic and parabolic subgroups have different orbit geometry. The terminology refers to isometry type, not to the causal character of the catenary curve itself; the curves lie in a Riemannian hyperbolic plane.

### 2.2 Weighted-length functional

For a regular curve `gamma`, parameterized by hyperbolic arc length `s`, the functional has the generic form

`E[gamma] = integral f(gamma(s)) ds`,

where `f` is a positive weight derived from extrinsic distance or an ambient coordinate relative to the chosen plane. Varying the curve normally produces the Euler–Lagrange condition

`kappa = - <n, grad f> / f`,

up to the source’s sign conventions for the unit normal and geodesic curvature. Equivalently, `kappa = -<n, grad log f>`. This reveals that a weighted geodesic bends according to the normal component of the logarithmic weight gradient.

The equation is local. It characterizes critical points, not necessarily global minimizers. Boundary conditions, positivity of the weight, completeness, and admissible curve class remain decisive for existence and optimization questions.

### 2.3 Symmetry and first integrals

If the weight is invariant under a one-parameter isometry group generated by a Killing field `K`, Noether’s principle yields a conserved quantity along a critical curve. The precise expression depends on parameterization and normalization, but it combines the tangent direction with the symmetry field and weight. The DEP-E uses these invariants to reconstruct each family and to connect differential equations with orbit geometry.

First integrals reduce the second-order curvature equation to a first-order relation and help generate numerical curves. They do not by themselves guarantee that solutions are complete, embedded, or unique. Singular behavior can occur where the weight approaches zero or the reduced denominator vanishes.

### 2.4 From curve energy to surface area

Let the matching isometry subgroup act on a profile curve. The generated surface has one tangent direction along the profile and another along the group orbit. The norm of the orbit-generating Killing field determines the infinitesimal orbit length. After integrating over the group parameter, the surface-area functional becomes a constant multiple of

`integral ||K(gamma(s))|| ds`.

Thus the natural weight is `f = ||K||`. This is the core structural identity. A profile is critical for the weighted-length functional exactly when the invariant surface is critical for area under compatible variations; the paper proves the minimal-surface equivalence for the corresponding families.

This formulation makes the three cases economical. Instead of memorizing separate “gravity” formulas, identify the symmetry subgroup, compute its Killing field norm on a transverse plane, and use that orbit-size function as the catenary weight.

### 2.5 Intrinsic horocycle interpretation

The DEP-E reports an intrinsic characterization for one extrinsic family. Horocycles are curves orthogonal to a family of geodesics approaching a common ideal point. Their intrinsic length relative to a reference geodesic can reproduce the relevant weight. This is conceptually important because it shows that at least one ambient definition is not merely an artifact of the hyperboloid embedding.

The result should not be generalized to all three causal types without proof. Each orbit family has different intrinsic geometry, and an analogous length interpretation may require a different reference foliation or may fail globally.

## 3. Evaluation design and evidence reconstructed

The source paper’s evaluation is deductive and geometric. It defines the three weights, computes Euler–Lagrange equations, derives curvature characterizations and first integrals, parameterizes the rotational surfaces, computes or relates mean curvature, and proves equivalence between zero mean curvature and the matching profile equation. The publisher version also includes numerical curves as illustration.

The DEP-E authoring run reports inspection of the complete arXiv PDF, HTML, TeX source, and open publisher HTML. It compares versions and explicitly accounts for the publisher curvature convention and added figure.[^dep] The current intake read both DEP-E files end to end and directly checked the canonical arXiv record. That record confirms the title, authors, v2 status, 20-page length, differential-geometry classification, and abstract-level claims about extrinsic distance, curvature characterization, minimal surfaces of revolution, and an intrinsic characterization for one family.[^arxiv]

The current run did not independently inspect the full external proofs. Detailed formulas and version differences therefore remain DEP-E-reported. This evidence boundary is especially important for sign conventions: curvature formulas can change sign when the chosen unit normal reverses. The durable content is the invariant relation between weighted variation and mean curvature, not a sign copied without its conventions.

No laboratory or observational experiment is relevant. Numerical integration can check example trajectories and detect typographical or sign errors, but it cannot establish the general theorems.

## 4. Results and quantitative audit

The main result is a three-family classification rather than a statistical measurement. The causal type of the reference plane induces three canonical weights and symmetry groups. Each weighted critical curve satisfies the reported prescribed-curvature equation. Revolving a curve under its matching group produces a minimal surface if and only if the profile is the corresponding extrinsic catenary.

The curvature normalization in the publisher record is reported as `-1/r^2`. Dimensional consistency matters: scaling the hyperboloid radius changes curvature and rescales ambient coordinates, arc length, and Killing-field norms. Any numerical example that silently sets `r=1` should not be compared to an arbitrary-radius formula without restoring scale.

The DEP-E reports no official solver code, initial-condition table, step-size policy, tolerance, or convergence study for the numerical figure. Therefore, the figure demonstrates qualitative plausibility only. It cannot support claims about the complete solution family, stability, bifurcations, or singularity avoidance.

The likely `cosh(u/u)` defect warrants targeted checking. Since `u/u=1` wherever defined, the expression would collapse to a constant and is unlikely to encode the intended variable dependence. The correction cannot be inferred safely from appearance alone; it should be checked against preceding definitions, source TeX, dimensional consistency, and the differential equation. The DEP-E appropriately labels it as likely rather than silently repairing it.

There are no reported sample sizes, error bars, or hypothesis tests except values associated with plotted numerical examples as represented by the source. A quantitative audit should focus on invariance, normalization, and residuals, not statistical significance.

## 5. Ablations and missing discriminators

Experimental ablations are not materially applicable, but geometric ablations clarify necessity.

- Replace the orbit-size weight with an arbitrary positive function: the curve remains a weighted geodesic, but the surface-area equivalence generally disappears.
- Pair a catenary weight with the wrong revolution subgroup: the orbit factor and curve functional no longer match.
- Ignore causal type: elliptic, hyperbolic, and parabolic orbits are conflated, losing global geometry.
- Reverse the curve normal without changing sign conventions: the curvature equation appears inconsistent even though the geometry is unchanged.
- Treat criticality as minimization: unstable or saddle critical curves are misclassified.
- Infer global existence from a local ODE: singular weights or denominators can obstruct extension.

Missing discriminators include a complete phase portrait for each first integral, conditions for complete embedded profiles, classification up to ambient isometry, stability through second variation, and numerical continuation across parameter values. The paper’s theorem does not require all of these, but they determine how the families behave beyond local criticality.

## 6. Claim-by-claim vetting

| Claim | Evidence | Assessment |
|---|---|---|
| Extrinsic hyperbolic catenaries can be defined by ambient distance to reference planes. | DEP-E-reported definitions from complete paper inspection; abstract confirms the construction. | Supported within the hyperboloid model and chosen weights. |
| The causal type of the plane produces three families. | Lorentzian classification and source reconstruction. | Strongly grounded in ambient isometry geometry. |
| Critical curves satisfy `kappa = -<n,grad f>/f`. | Source-reported first-variation calculation. | Supported up to stated orientation conventions; not independently derived here. |
| Matching surfaces of revolution are minimal exactly for the corresponding catenaries. | Source-reported theorem and area/mean-curvature reduction; abstract confirms the direction. | Principal result; proof not independently certified here. |
| One family admits an intrinsic horocycle characterization. | Source-reported theorem and canonical abstract. | Supported for the specified family; no generalization to all families. |
| Numerical plots establish existence and uniqueness. | No such evidentiary design. | Unsupported. |
| Every critical catenary is a global minimizer. | First variation establishes criticality only. | Unsupported without second variation/global analysis. |
| The apparent formula typo has a known correction. | DEP-E identifies a suspicious expression but does not establish replacement text. | Defect plausible; correction remains unresolved. |

## 7. External primary-source context

The canonical arXiv record identifies the paper, authors, v2 revision date, 20-page length, subject, and abstract.[^arxiv] The abstract independently confirms the four major elements preserved by the DEP-E: extrinsic catenaries defined through ambient potential, curvature characterization, relation to minimal surfaces of revolution, and intrinsic characterization of one family. The record supplies the arXiv DOI and PDF/TeX locators.[^arxivdoi]

The DEP-E also records the publisher DOI `10.1017/prm.2024.56` and compares the open publisher presentation with arXiv. This provides version-aware provenance. The current intake did not directly re-open the publisher body and therefore attributes details such as Figure 1 and normalization edits to the DEP-E report.[^publisher]

The broader geometric context is the reduction of invariant variational problems. Minimal surfaces invariant under a one-parameter group are governed by a quotient-space curve functional whose density is orbit volume. The reviewed paper gives a concrete hyperbolic realization with all three Lorentzian symmetry types. The reviewer’s symmetry–orbit-weight terminology is a synthesis, not a claim of novelty over that broader theory.

## 8. Research notes, caveats, and code/reproducibility status

No official solver code is reported in the DEP-E. The numerical component is therefore not computationally reproducible from the public record alone without reconstructing the ODE, choosing normalization, initial conditions, integration domain, tolerances, and plotting conventions. A future reproduction should publish all of those plus residual checks against both the first integral and curvature equation.

Proof reproducibility requires attention to model conventions. Lorentzian signatures vary across texts; hyperboloid radius may be normalized; orientation choices change curvature signs; group parameters may be rescaled. A robust audit should rewrite each formula invariantly before comparing coordinate expressions.

The word “distance” also needs care. A signed ambient linear coordinate, absolute Lorentzian separation, and intrinsic hyperbolic distance are different objects. The source’s extrinsic construction deliberately uses ambient information. The horocycle result shows an intrinsic equivalence only in a specified setting.

The publisher figure cannot close theoretical gaps. A smooth curve drawn for one initial condition says nothing about other conserved quantities or global stability. Numerical solvers can also step across singular regions unless events are detected.

## 9. Independent re-conceptualization

The paper can be reorganized around an invariant recipe:

1. Choose a one-parameter isometry subgroup `G` of the ambient constant-curvature space.
2. Select a transverse profile plane and compute the generating Killing field `K`.
3. Define the orbit-size weight `f(x)=||K(x)||` on the profile domain.
4. Study critical curves of `integral f ds`.
5. Lift each curve through the `G` action; weighted criticality is the reduced form of minimality.

This **symmetry–orbit-weight duality** explains why the catenary and minimal-surface equations match. “Gravity” is not an extra physical field added after the fact. It is the local area contribution of the symmetry orbit. The Lorentzian causal classification identifies inequivalent orbit structures and therefore inequivalent weights.

The recipe also identifies extensions. In higher dimension, orbit volume replaces orbit length. For prescribed mean curvature, the reduced functional gains a volume term. In other ambient geometries, the same method applies if the isometry action and quotient metric are tractable. These are reviewer proposals and require separate proofs.

From a computational perspective, the invariant first integral should be used as an online error monitor. A numerical integrator that preserves the profile ODE but drifts in the conserved quantity is not trustworthy over long arcs. Coordinate charts should be switched before singularities, and reconstructed surfaces should be checked for induced-metric degeneracy and mean-curvature residual.

## 10. Implications and failure modes

The source illustrates a general research discipline: match a variational weight to a symmetry before interpreting a profile curve. For geometers, it organizes elliptic, hyperbolic, and parabolic rotations under one mechanism. For numerical work, it supplies two independent residuals—the Euler–Lagrange equation and first integral. For education, it connects Lorentzian causal classes to visibly different Riemannian surface families.

Failure modes include:

1. **Causal-label confusion:** treating a timelike plane normal as a causal curve classification.
2. **Weight mismatch:** revolving under one subgroup while using another subgroup’s orbit factor.
3. **Sign drift:** comparing curvature equations with opposite normal conventions.
4. **Scale loss:** setting `r=1` and failing to restore `-1/r^2` normalization.
5. **Critical/minimal conflation:** calling every stationary curve a global minimizer.
6. **Local/global conflation:** extending ODE solutions past singular weights without proof.
7. **Figure overreach:** using a numerical plot as evidence for classification or uniqueness.
8. **Typo propagation:** copying a suspicious formula without source and consistency checks.

The intake should be used to plan proof or numerical verification, not as a replacement for the source theorem.

## 11. Replication, falsification, and hypothesis agenda

The following are reviewer proposals.

**H1 — Orbit-weight residual equivalence.** For each of the three normalized symmetry groups, a numerically generated profile satisfying the weighted Euler–Lagrange equation will generate a surface whose computed mean-curvature residual converges to zero at the same order as discretization error. Falsification: persistent residual mismatch after convention and resolution checks.

**H2 — Conserved-quantity monitoring improves reliability.** Adaptive integration constrained by the first integral will extend accurate profiles farther than an unconstrained method at equal computational cost. Falsification: no reproducible improvement across initial conditions.

**H3 — Causal families have distinguishable global phase portraits.** Elliptic, hyperbolic, and parabolic weights yield topologically different classes of complete-profile trajectories under normalized parameters. Falsification: an isometry and parameter transformation identifies the proposed distinctions.

**H4 — The intrinsic characterization is exceptional.** Direct analogues of the reported horocycle-length formulation will fail for at least one other causal family without changing the intrinsic reference foliation. Falsification: an invariant construction yields equivalent intrinsic weights for all three.

A proof replication should normalize the Lorentzian signature and radius, reproduce the first variation, derive each Killing field and its norm, compute the induced metric of the surface, and verify the mean-curvature equivalence. Every sign should be checked under a stated orientation. The likely typo should be traced through arXiv TeX, publisher equation numbering, adjacent derivations, and dimensional behavior.

A numerical replication should publish initial data, parameter domains, event functions, absolute and relative tolerances, conserved-quantity drift, curvature residual, mean-curvature residual, mesh refinement, and code. Plots should distinguish complete curves from truncated integrations and flag intersections or coordinate singularities.

## 12. Durable restatement

The complete DEP-E record supports a precise durable statement. In the hyperboloid model, ambient reference planes fall into three Lorentzian causal types. Each type supplies a positive weight for a curve functional in the hyperbolic plane. Its critical curves obey a prescribed geodesic-curvature equation and admit symmetry-derived first integrals. When such a curve is revolved under the matching isometry subgroup, the surface-area functional reduces to the same weighted length, yielding the reported minimal-surface equivalence. One family also has an intrinsic horocycle interpretation.

The record does not establish that every critical curve is a global minimizer, complete, unique, stable, or embedded. Numerical illustrations do not replace those results. The current intake does not independently verify the proofs or computations.

The reviewer’s reusable restatement is that orbit geometry determines variational weight: compute the norm of the symmetry-generating Killing field, and the invariant minimal-surface problem becomes a weighted geodesic problem on the profile space.

## 13. Source and evidence notes

### Complete inventory and source integrity

| Item | Inspection | Role | Integrity assessment |
|---|---|---|---|
| Source `README.md` | Read end to end | Identity, inventory, source boundary, summary, associations, attribution | Complete and version-aware. |
| `hyperbolic_catenaries_whitepaper.md` | Read end to end | Variational reconstruction, three cases, theorems, numerical notes, limitations, coverage | Complete DEP report; reports full source inspection. |
| Canonical arXiv record | Directly inspected | Title, authors, v2, abstract, identifiers, access links | Primary metadata; full body not re-read here. |
| Generated review | New derived artifact | Intake, audit, re-conceptualization, replication plan | Original prose; no source copied. |

### Coverage ledger

| Source dimension | Coverage in this review | Boundary |
|---|---|---|
| Hyperboloid and Lorentzian setup | Framing and technical reconstruction | DEP-E-reported formalism. |
| Three causal plane types | Technical reconstruction and claim table | All three represented conceptually. |
| Weighted functional and curvature | Technical reconstruction | Sign conventions retained as a caveat. |
| First integrals and Killing fields | Technical reconstruction and reconceptualization | Exact case formulas not independently checked. |
| Minimal-surface equivalence | Executive, technical reconstruction, claims, durable restatement | Source theorem; no proof certificate. |
| Intrinsic horocycle result | Framing, technical reconstruction, claims | Limited to reported family. |
| Publisher comparison and Figure 1 | Results and external context | DEP-E-reported; not re-opened here. |
| Numerical methods | Results, research notes, replication | No code/settings; no reproduction. |
| Limitations and failure modes | Research notes and implications | Source caveats plus labeled reviewer analysis. |
| References and attribution | External context, footnotes, README attribution | No PDF, TeX, HTML, or cache uploaded. |

### Evidence boundary

The complete DEP-E report is the source for theorem, equation, figure, and version-comparison detail. Directly inspected primary evidence in this run is limited to canonical arXiv metadata and abstract. Reviewer inference includes symmetry–orbit-weight terminology, extension paths, and numerical monitoring proposals. No proof, ODE integration, figure, or surface computation was independently reproduced.

The paper reports the detailed equivalences through the complete source inspection documented by the DEP-E.[^boundary] The one-way provenance pair preserves the distinction between reviewed source data and newly generated archival analysis.[^provenance]

## 14. Footnotes

[^paper]: Luiz C. B. da Silva and Rafael López, “Catenaries and minimal surfaces of revolution in hyperbolic space,” arXiv:2211.15297v2, https://arxiv.org/abs/2211.15297v2.
[^dep]: Complete source record, https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Hyperbolic%20Catenaries, inspected at commit `b5ad2459a6ee3d649feb8209d9390d86d475502c`.
[^arxiv]: Canonical arXiv metadata and abstract, https://arxiv.org/abs/2211.15297.
[^arxivdoi]: Persistent arXiv DOI, https://doi.org/10.48550/arXiv.2211.15297.
[^publisher]: Publisher DOI reported by the source record, https://doi.org/10.1017/prm.2024.56.
[^boundary]: The DEP-E records complete arXiv PDF, HTML, TeX, and open publisher HTML inspection. This intake did not repeat that external full-paper review.
[^provenance]: Paired task `BL-DEPPAIR-20260716-BE15A671` records review-only derivation; no DEP-E file was modified, moved, or copied.
