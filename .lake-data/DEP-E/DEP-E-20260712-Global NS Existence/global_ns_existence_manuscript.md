---
title: "Global NS Existence - DEP-E"
generated_at: "2026-07-12 (date-only public marker; exact local timestamp and timezone withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of global strong and weak solutions for a two-dimensional compressible Navier-Stokes system with density-dependent bulk viscosity, Navier-slip boundaries, large data, and vacuum."
source_status: "public URLs and private extraction cache; no source files deposited"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-12"
temporal_cutoff: "arXiv v2 revised 2021-02-23; version of record published 2022-05-13; sources inspected through the date-only run marker"
primary_url: "https://arxiv.org/abs/2102.09229"
stable_identifier: "arXiv:2102.09229v2; DOI 10.1007/s00205-022-01790-4"
confidence_summary: "High for source identity and reporting the stated theorems; medium for proof-mechanism synthesis; low for independent correctness because the proof was not formally verified."
safety_scope: "non-sensitive pure and applied mathematics review"
distribution_notes: "Public URLs and repository-relative paths only; private archive and cache locations withheld."
---

# Global NS Existence - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | URL / Public Reference | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv abstract page | Primary metadata | HTML | arXiv:2102.09229v2 | https://arxiv.org/abs/2102.09229 | Public arXiv record; source file not redistributed. | 2026-07-12 | Inspected |
| S2 | Local archive PDF through extraction cache | Primary paper | PDF-derived text | arXiv:2102.09229v2 | https://arxiv.org/pdf/2102.09229 | Private local extraction; no source file or private path deposited. | 2026-07-12 | Complete text inspected with encoding caveats |
| S3 | Springer article page | Version-of-record metadata | HTML | DOI 10.1007/s00205-022-01790-4 | https://link.springer.com/article/10.1007/s00205-022-01790-4 | Publisher page; subscription content not collected. | 2026-07-12 | Metadata, abstract, references, and publication record inspected |
| S4 | arXiv DOI | Persistent identifier | DOI | 10.48550/arXiv.2102.09229 | https://doi.org/10.48550/arXiv.2102.09229 | arXiv-issued DOI. | 2026-07-12 | Recorded |
| S5 | Black Lake README | Repository authority | Markdown | origin/main | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Public deposition standard. | 2026-07-12 | Fetched and read |
| S6 | Black-Lake-Data README | Related repository authority | Markdown | main | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Public related-repository standard. | 2026-07-12 | Fetched and read |
| S7 | Fermat Difference - DEP-E | Related DEP | Markdown | DEP-E-20260709-Fermat Difference | `.lake-data/DEP-E/DEP-E-20260709-Fermat Difference/fermat-difference-manuscript.md` | Processed Black Lake artifact. | 2026-07-12 | Inspected |
| S8 | Physical Data AI - DEP-E | Related DEP | Markdown | DEP-E-20260710-Physical Data AI | `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` | Processed Black Lake artifact. | 2026-07-12 | Inspected |
| S9 | RRT-CBF Motion - DEP-E | Related DEP | Markdown | DEP-E-20260711-RRT-CBF Motion | `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` | Processed Black Lake artifact. | 2026-07-12 | Inspected |

The authors are Xinyu Fan, Jiaxu Li, and Jing Li. arXiv records submission on 2021-02-18 and revision on 2021-02-23. Springer records publication in *Archive for Rational Mechanics and Analysis*, volume 245, pages 239-278, on 2022-05-13. The publisher page identifies the article DOI as 10.1007/s00205-022-01790-4.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S3, S4 | Primary metadata and publisher record | Title, authors, subject, versions, dates, venue, DOI, abstract, and publication history. | Source identity and high-level contribution. | High | Abstract and metadata do not validate proof correctness. |
| E2 | S2, introduction and Theorems 1.1-1.2 | Primary paper text | PDE system, viscosity law, pressure law, domain and boundary assumptions, strong/weak solution statements, and vacuum/large-data scope. | Main theorem report. | High for source reporting | Mathematical symbols contain extraction noise; theorem correctness not independently checked. |
| E3 | S2, Sections 2-3 | Primary paper text | Div-curl and BKM estimates, Riemann mapping, pull-back Green's function, effective viscous flux, commutator representation, and density upper-bound closure. | Core proof mechanism. | Medium-high | Proof reviewed structurally, not line by line or formally. |
| E4 | S2, Sections 4-5 | Primary paper text | Material-derivative estimates, higher regularity, lower-density statement, approximation, compactness, and uniqueness references. | Extension from a priori estimates to global strong and weak solutions. | Medium | Compactness and uniqueness arguments are sketched and defer to prior work. |
| E5 | S2, Remarks 1.1-1.4 and publisher references | Primary paper and publication context | Claimed novelty, threshold `beta > 4/3`, open regime `1 < beta <= 4/3`, and boundary-specific difficulty. | Limitations and research backlog. | Medium-high | Novelty was not exhaustively checked against the full literature. |
| E6 | Private cache public summary | Process evidence | Fresh `missing-only` cache, `pypdf` fallback, 72,259 bytes of PDF text, partial final status. | Extraction method and cache provenance. | High | Private cache location and exact local timestamps withheld. |
| E7 | S5-S6 and repository scans | Process evidence | Repository policy, uniform selection, dedup index, artifact scans, memory checks, and related-repository searches. | Eligibility and artifact compliance. | High | Process evidence does not support the mathematics. |
| E8 | S7-S9 | Related DEP artifacts | Theorem-regime review, PDE/domain-fit translation, and invariance/boundary-constrained dynamics. | Cross-DEP synthesis and implementation framing. | Medium | These entries do not validate the selected paper's theorems. |

## Executive Summary

The paper studies a barotropic compressible Navier-Stokes system on a general two-dimensional bounded simply connected domain. Pressure is `P = a rho^gamma` with `gamma > 1`; shear viscosity is a positive constant; and bulk viscosity scales as `lambda(rho) = b rho^beta`. Under Navier-slip conditions, `beta > 4/3`, and initial data that may include vacuum and need not be small, the authors state global existence and uniqueness of a strong solution. With weaker initial-density regularity, they state global existence of at least one weak solution.

The central obstacle is boundary geometry. In the full space or on a torus, inverse-Laplacian derivatives can be reorganized into classical Calderon-type commutators that help bound the density. That interchange is unavailable in a general bounded domain. The paper instead maps the domain conformally to the unit disk, pulls back a Neumann Green's function, uses angle preservation plus the slip condition to expose cancellation at the boundary, and derives a commutator-like pointwise representation for the effective viscous flux. This representation feeds the decisive uniform upper bound on density.

The source then combines lower- and higher-order a priori estimates, a Beale-Kato-Majda-type inequality, approximation by smooth positive-density data, compactness, and prior uniqueness machinery. The reviewer's confidence is high that this is what the paper states and medium that the summarized proof architecture is faithful. This deposit does not independently prove the estimates. The most explicit open boundary is the viscosity exponent: the paper requires `beta > 4/3` while identifying `1 < beta <= 4/3` as future work.

## Detailed Summary

### Problem Context

Compressible Navier-Stokes equations couple conservation of mass with momentum transport, pressure, and viscous dissipation. Vacuum makes the system degenerate because density can vanish, and large initial data remove the perturbative smallness used by many classical global-existence results. A bounded domain adds boundary terms and blocks Fourier-space manipulations available on the whole space or torus.

The unknowns are density `rho(x,t)` and velocity `u(x,t)`. The paper considers

- continuity: `rho_t + div(rho u) = 0`;
- momentum: `(rho u)_t + div(rho u tensor u) + grad P = mu Delta u + grad((mu + lambda) div u)`;
- pressure: `P = a rho^gamma`, `gamma > 1`;
- viscosities: constant `mu > 0` and `lambda(rho) = b rho^beta`;
- boundary conditions: `u dot n = 0` and `curl u = 0` on the boundary.

The domain is bounded, simply connected, and has `C^{2,1}` boundary. Constants `a` and `b` are normalized to one in the analysis.

### Main Strong-Solution Statement

Theorem 1.1 assumes `beta > 4/3`, `gamma > 1`, nonnegative initial density in `W^{1,q}` for some `q > 2`, and initial velocity in `H^1` satisfying the slip condition. It states that the problem has a unique global strong solution. The listed regularity controls density continuously in `W^{1,q}`, velocity in `L-infinity_t H^1_x` and integrable `W^{2,q}`, time-weighted `H^2` and time-derivative norms, momentum continuity in `L^2`, and a square-root-density-weighted velocity time derivative.

The theorem allows vacuum and does not impose smallness on the initial data. The authors describe this as the first such strong-solution result for the stated system in general two-dimensional bounded domains, but this review did not conduct a complete novelty audit.

### Main Weak-Solution Statement

Theorem 1.2 replaces the initial `W^{1,q}` density assumption with `L-infinity` density and states existence of at least one global weak solution. Its regularity includes bounded density, `H^1` velocity, positive-time velocity derivatives and gradient controls, and space-time control of vorticity and effective viscous flux.

The theorem also states a finite-time lower-density estimate proportional to the minimum initial density. Thus, if the initial density is strictly positive, the constructed weak solution does not develop vacuum during a finite time interval. The paper explicitly contrasts this with an open question for the broader Lions-Feireisl weak-solution class.

### Effective Viscous Flux and Density Control

The decisive quantity is the effective viscous flux

`F = (2 mu + lambda(rho)) div u - P`.

For `theta(rho) = 2 mu log rho + rho^beta / beta`, the continuity equation gives a material-path relation of the form

`D theta(rho) / Dt + P = -F`.

Controlling `F` therefore controls the growth of density. The flux solves a Neumann problem with source `div(rho dot-u)` and normal data `rho dot-u dot n`, where `dot-u` is the material derivative.

### Boundary Geometry and Pull-Back Green's Function

In a disk, the Neumann Green's function has an explicit reflected-logarithm form. For a general simply connected planar domain, the authors use the Riemann mapping theorem to obtain a conformal map to the disk and pull the disk Green's function back to the original domain.

Angle preservation is essential. The Navier-slip condition makes velocity tangential on the boundary, and conformal mapping preserves the orthogonality between tangent and normal directions. The paper uses this geometry to turn otherwise uncontrolled boundary singularities into differences such as `u(x) - u(y)` or `u(x') - u(y)`. Those differences cancel one degree of singularity when the velocity has sufficient spatial regularity.

Proposition 3.2 bounds the key integral by one order-one singular term and two commutator-type terms, including a boundary-point term. Proposition 3.3 controls the time integral of the commutator contribution. Proposition 3.4 closes an inequality for the maximum density. The exponent comparison closes only for `beta > 4/3`, yielding the uniform density upper bound and lower-order energy controls.

### Higher-Order Estimates and Global Continuation

Section 4 controls the material derivative, flux, vorticity, velocity gradients, and density gradients. Boundary traces created by integration by parts are handled using the slip condition and a tangential-divergence identity. A Beale-Kato-Majda-type logarithmic inequality converts `div u`, `curl u`, and second derivatives into control of `grad u` in `L-infinity`. Gronwall arguments then close the `W^{1,q}` density and `W^{2,q}` velocity estimates.

For smooth strictly positive approximate data, local theory plus the uniform a priori estimates yields global strong solutions. The authors approximate vacuum-allowing data by smooth positive-density data satisfying the slip condition, then pass to a limit using compactness. For the weak solution, another approximation and Aubin-Lions compactness give strong density convergence and passage to the nonlinear terms. Uniqueness of the strong solution is attributed to an argument similar to Germain's weak-strong uniqueness method.

### Boundary Conditions and Open Regime

The proof is tuned to two dimensions, simple connectivity, regular bounded domains, the stated slip condition, constant shear viscosity, and density-dependent bulk viscosity. The authors say `beta > 4/3` is technical and suggest `beta > 1` may be the extremal regime. The interval `1 < beta <= 4/3` is left open.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Global unique strong solutions exist under the stated 2D domain, slip, regularity, `gamma > 1`, and `beta > 4/3` assumptions without small initial data and with vacuum allowed. | Author theorem claim | E2 | Theorem 1.1 states this directly; not independently proven here. | High for reporting, low for independent verification |
| C2 | Global weak solutions exist for bounded initial density, with a lower-density estimate preserving positivity over finite time when the initial density is positive. | Author theorem claim | E2, E4 | Theorem 1.2 and Lemma 4.3 support the statement. | High for reporting |
| C3 | Pulling back the disk Neumann Green's function through a conformal map creates a usable pointwise representation of effective viscous flux in a general simply connected domain. | Author method claim | E3 | Lemmas 3.6-3.7 and the surrounding construction directly support the mechanism. | Medium-high |
| C4 | Slip-boundary orthogonality turns the dangerous boundary contribution into a commutator-like difference with cancellable singularity. | Author method claim | E3 | Proposition 3.2 and Remarks 3.1-3.3 support the claim. | Medium-high |
| C5 | The density upper-bound argument closes for `beta > 4/3`. | Author proof claim | E3 | Proposition 3.4 states the resulting bound and displays the exponent comparison. | Medium |
| C6 | The open regime `1 < beta <= 4/3` is not settled by this method. | Source-disclosed limitation | E5 | Remark 1.3 identifies it as future work. | High |
| C7 | A reusable review pattern is to preserve theorem assumptions, proof dependencies, and unverified transitions as structured evidence. | Reviewer interpretation | E2-E8 | Strongly motivated by this and related DEP artifacts, but not a paper theorem. | Medium-high |

## Methodology

- `Research objective`: Uniformly select one eligible local arXiv paper, process it through the extraction cache, review it source-first, relate it to exactly three existing deposits, and produce a schema-complete public-safe DEP-E manuscript.
- `Sources inspected`: Adjacent archive metadata; complete PDF-derived text; arXiv metadata; Springer version-of-record metadata, abstract, publication history, and references; live README files for both repositories; and exactly three related Black Lake manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, collapsed them by unique parent directory, drew a uniform zero-based `Get-Random` index, derived the arXiv ID from the filename and nearby README, and searched both repositories plus memory for duplicate identifiers.
- `Inclusion criteria`: Sources had to establish identity, theorem assumptions, proof mechanism, limitations, repository rules, extraction provenance, or concrete related-entry overlap.
- `Exclusion criteria`: Secondary summaries, recommender widgets, uninspected citations, and broad keyword-only DEP matches were excluded. No source file was redistributed.
- `Analytical approach`: Conceptual, comparative, implementation, product-research, replication/proof-review, and provenance analysis.
- `Evidence handling`: Theorem statements are reported as author claims; proof mechanisms are mapped to cited sections and evidence IDs; reviewer interpretations and related-entry synthesis are labeled separately.
- `Uncertainty handling`: Encoding corruption, absence of formal proof checking, deferred compactness details, unverified novelty, and lack of a direct related mathematical neighbor are explicit.
- `Extraction process`: Preflight found `pypdf` but not `pdftotext`, PyMuPDF, PyPDF2, or pdfminer. `extract-arxiv` ran in `missing-only` mode against the selected paper unit and central private cache. The fresh cache is partial: PDF text present at 72,259 bytes, HTML and source text absent.
- `Version control`: Paper review is pinned to arXiv:2102.09229v2; publication metadata is pinned to DOI 10.1007/s00205-022-01790-4.
- `Cross-checking`: Title, authors, abstract, dates, and DOI were checked across arXiv and Springer. Theorems, remarks, propositions, and final proof sections were checked within the complete PDF text.
- `Random selection`: Uniform zero-based index 17,885 over 75,761 PDF-parent paper units; the first draw was accepted.
- `Cache methodology`: Local-first `missing-only` extraction; no paper-body network backfill; public metadata consulted after local extraction.
- `Deduplication and reselection validation`: No match for arXiv ID, DOI, normalized title, or slug in the public index, Black Lake logs/reports/deposits, automation memory, Black-Lake-Data searches, or the preceding 24-hour window. Exclusions and reselections were zero.
- `Reviewer stance`: Skeptical paper report, theorem/proof dependency preservation, implementation translation, and future formalization planning.

## Scope, Constraints, and Assumptions

- `Scope`: The selected paper's PDE setting, theorem statements, proof architecture, evidence limitations, and exactly three related-deposit bridges.
- `Temporal boundary`: arXiv v2 and the 2022 version of record, with public sources inspected through 2026-07-12.
- `Evidence limits`: No formal proof assistant, symbolic checker, independent referee, or exhaustive literature review was used. Extraction altered some mathematical glyphs.
- `Assumptions`: The archived PDF is arXiv v2; theorem and equation numbering survived extraction; publisher metadata refers to the same core work.
- `Constraints`: Public artifacts exclude private locations, usernames, machine data, timezone labels, exact local execution timestamps, and uncollected source files.
- `Out of scope`: Proving the theorems, resolving `1 < beta <= 4/3`, extending to multiply connected or three-dimensional domains, or implementing a numerical Navier-Stokes solver.
- `Intended use`: DEP deposition, mathematical review, proof-formalization planning, research backlog creation, and safe educational tooling.
- `Audience`: PDE researchers, mathematical reviewers, proof engineers, scientific-computing developers, and Black Lake maintainers.
- `Depth target`: Full schema-complete manuscript with theorem, proof-mechanism, limitation, and provenance coverage.
- `Reproducibility boundary`: A reviewer can retrieve and inspect the public paper, but this deposit alone cannot reproduce or certify the proof.
- `Operational boundary`: Implementation examples analyze theorem structure and synthetic metadata; they are not numerical solvers or scientific validation.
- `Data sensitivity`: Public scholarly and repository records only; private source locations are withheld.

## Observations

- `Observed pattern`: The proof's novelty is an interface between geometry and analysis: the conformal map is useful because it preserves the boundary orthogonality needed for singularity cancellation.
- `Technical implication`: Global existence depends on a chain of estimates whose assumptions should be recorded as dependencies, not compressed into an abstract-level claim.
- `Boundary implication`: The boundary is not a minor perturbation of the periodic case; it changes the available commutator calculus and forces a new Green-function representation.
- `Parameter implication`: `beta > 4/3` is both a theorem condition and a closure condition for the density exponent inequality, making it a natural target for future estimate refinement.
- `Evidence-quality implication`: The strongest evidence is theorem/proof text, but source inspection is not equivalent to proof verification.
- `Open question`: Can the commutator estimate be reformulated in a way that applies to multiply connected domains or weaker boundary regularity?
- `Reviewer hypothesis`: A machine-readable proof-dependency graph would expose exactly where simple connectivity, angle preservation, and the viscosity threshold enter.

## Considerations

Mathematical deployment claims require more than readable prose. A formalization project would need exact function spaces, trace theorems, elliptic regularity assumptions, constants, approximation topology, compactness modes, and the imported uniqueness theorem. Encoding-normalized LaTeX or source is preferable to PDF text for that task.

The paper's strong and weak results should not be conflated. The strong theorem includes uniqueness and higher regularity under `W^{1,q}` density; the weak theorem relaxes density regularity and states existence, not general uniqueness. The finite-time lower-density estimate applies to the constructed weak solution and depends on positive initial minimum.

Related DEP artifacts are interpretive neighbors only. Fermat Difference contributes theorem-regime and formal-verification patterns; Physical Data AI contributes PDE/domain-fit product translation; RRT-CBF contributes invariance and boundary-assumption telemetry. None is mathematical evidence for the Navier-Stokes theorems.

## Strengths

- The paper states explicit domain, boundary, pressure, viscosity, regularity, and exponent assumptions.
- The proof targets the genuinely boundary-specific failure of the periodic commutator argument.
- The conformal-map and pull-back Green-function mechanism is concrete and geometrically motivated.
- Strong and weak solution statements are separated, with distinct initial-density requirements.
- The authors identify a clear unresolved exponent regime instead of implying full sharpness.
- The version of record and public arXiv source provide stable provenance.

## Weaknesses

- This review did not independently verify every estimate or imported compactness/uniqueness result.
- The arXiv PDF extraction corrupts some symbols and spacing, limiting formula-perfect traceability.
- The proof is restricted to two-dimensional simply connected bounded domains with a specific slip boundary condition and viscosity law.
- The critical range `1 < beta <= 4/3` remains open in the paper's framework.
- Final approximation arguments are comparatively brief and rely on earlier literature.
- No official formalization or executable verification artifact was identified from the inspected primary records.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Publish formula-preserving source map | Reproducibility | PDF text is lossy for proof review. | Stable equation, lemma, and dependency references. | Source-maintenance effort. | Compare every mapped theorem and equation against the version of record. |
| Build a proof dependency graph | Verification | The global result depends on many estimates and imported results. | Exposes assumption flow and unresolved steps. | Risk of oversimplifying functional-analytic details. | Human PDE review of every dependency edge. |
| Isolate the `beta > 4/3` bottleneck | Analysis | The paper identifies a likely non-sharp technical threshold. | Focuses future work on the exact closure inequality. | New estimates may fail at the boundary. | Re-derive the density exponent comparison under candidate bounds. |
| Test broader domain topology | Geometry | Simple connectivity enables the disk conformal map. | Clarifies transfer to multiply connected domains. | Green-function and harmonic-field complications. | Prove or disprove analogous commutator representations on annular test domains. |
| Expand boundary-condition comparison | PDE scope | Slip orthogonality drives cancellation. | Shows whether the mechanism is robust or highly specific. | Boundary traces may become uncontrollable. | Compare Navier-slip, no-slip, and mixed conditions in a lemma-level matrix. |
| Formalize approximation steps | Weak/strong limit | Compactness and uniqueness are sketched. | Improves auditability of vacuum and weak-solution passage. | Significant proof-engineering effort. | Machine-check or expert-review the topology and nonlinear-limit steps. |

## Potential Implementations

1. `PDE Theorem Assumption Ledger`
   - `User`: Mathematical reviewer or proof engineer.
   - `Goal`: Convert theorem statements into a machine-readable list of domain, coefficient, regularity, boundary, and exponent assumptions.
   - `Core mechanism`: Parse curated theorem text into versioned YAML, attach evidence IDs, and require reviewer confirmation.
   - `Required inputs`: Formula-preserving theorem text, source version, reviewer annotations.
   - `Outputs`: Assumption matrix, conclusion matrix, unresolved-field report.
   - `Risk controls`: Never label extracted statements as verified; preserve source links and confidence.
   - `Evaluation`: Two independent reviewers reproduce the same assumption set.

2. `Proof Bottleneck Mapper`
   - `User`: PDE research group.
   - `Goal`: Identify which estimate introduces each domain and exponent restriction.
   - `Core mechanism`: Represent lemmas and propositions as a directed graph with assumption and conclusion tags.
   - `Required inputs`: Lemma statements, proof citations, equation references, imported results.
   - `Outputs`: Dependency graph, threshold-origin report, missing-proof alerts.
   - `Risk controls`: Human review required before any correctness claim.
   - `Evaluation`: Every main-theorem hypothesis traces to at least one reviewed dependency edge.

3. `Boundary Commutator Toy Lab`
   - `User`: Analysis student or scientific-computing researcher.
   - `Goal`: Visualize how velocity differences reduce a kernel singularity in disk-like toy geometry.
   - `Core mechanism`: Use synthetic smooth vector fields on a disk and compare raw singular kernels with difference-form kernels under controlled discretization.
   - `Required inputs`: Synthetic fields, grid, kernel regularization, boundary samples.
   - `Outputs`: Convergence plots and explanatory notebook.
   - `Risk controls`: Educational toy only; no claim of PDE proof or numerical-solver validity.
   - `Evaluation`: Refinement study shows stable qualitative cancellation without hidden divergence.

## Three Ways to Exercise This Research

1. `Assumption extraction review`: Objective—reconstruct Theorems 1.1 and 1.2 as an assumption/conclusion table; inputs—the public paper and this evidence ledger; method—two reviewers independently tag domain, coefficients, regularity, boundary, and result type; output—a reconciled table; success—no untraced field remains; stop—halt if formula corruption prevents unambiguous transcription.
2. `Dependency-path walkthrough`: Objective—trace density control from the continuity equation to Proposition 3.4; inputs—Sections 1-3 and a graph template; method—map `theta`, effective viscous flux, Neumann representation, commutator estimate, and exponent closure; output—a reviewed dependency graph; success—each edge cites a lemma, proposition, or equation; stop—do not mark the graph as proof verification.
3. `Synthetic cancellation demonstration`: Objective—illustrate why `u(x)-u(y)` softens a singular kernel; inputs—smooth synthetic fields on a disk; method—compare regularized raw and difference kernels under grid refinement; output—plots and caveat notes; success—qualitative cancellation persists across refinements; stop—do not generalize the numerical toy to the theorem.

## Example MVP Product

- `Product name`: PDE Proof Boundary Map.
- `Target user`: PDE reviewer, graduate seminar, or proof-formalization engineer.
- `Problem`: Long analytic papers make it difficult to see where domain topology, boundary conditions, coefficient laws, and exponent thresholds enter the final theorem.
- `Core workflow`: Import curated theorem and lemma excerpts; attach source anchors; tag assumptions and conclusions; draw dependency edges; run completeness checks; export a Markdown/YAML review bundle.
- `Data requirements`: Public source text, stable identifiers, theorem and equation anchors, reviewer annotations; no private or personal data.
- `Architecture`: Local-only parser and schema validator, graph store, reviewer UI, and public-safe Markdown exporter.
- `Success metrics`: Percentage of theorem assumptions traced to dependencies, reviewer agreement, unresolved-edge count, and source-link completeness.
- `Risk controls`: Prominent `reviewed, not proved` status; no automatic correctness claims; immutable source anchors; human approval for every dependency edge.
- `Limitations`: Formula parsing is brittle; a complete graph may still encode an incorrect proof; imported literature remains a separate verification burden.
- `MVP boundary`: One paper, manually curated excerpts, no general LaTeX theorem parser, and no proof-assistant integration.
- `Deployment model`: Local CLI plus static HTML/Markdown report.
- `Evaluation plan`: Reconstruct Theorems 1.1-1.2 and the Proposition 3.4 path, then compare two independent reviewer graphs.
- `Failure modes`: Symbol corruption, omitted hypotheses, false edge confidence, version drift, and treating a dependency map as formal verification.
- `Maintenance plan`: Pin paper versions, retain evidence IDs, and require re-review after source or schema changes.

Illustrative schema check:

```python
REQUIRED = {"domain", "boundary", "pressure", "viscosity", "initial_data", "conclusion"}

def missing_fields(theorem_record):
    """Review aid only; this does not verify a theorem."""
    return sorted(REQUIRED - set(theorem_record))
```

Dependencies are Python 3 and a YAML/JSON parser if serialization is used. Production hardening would require a versioned schema, formula-preserving anchors, review signatures, and tests against intentionally incomplete records.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Huang and Li, 2016 | Direct predecessor | Global strong solutions for 2D barotropic compressible Navier-Stokes with vacuum and large data; a key method predecessor cited by the paper. | DOI and journal reference listed on the publisher page |
| Jiu, Wang, and Xin, 2014 | Direct predecessor | Global well-posedness for 2D compressible Navier-Stokes with large data and vacuum. | Journal of Mathematical Fluid Mechanics 16, 483-521 |
| Cai and Li, arXiv:2102.06348 | Boundary-method neighbor | Slip-boundary classical-solution estimates used as a lower-order boundary-control precedent. | https://arxiv.org/abs/2102.06348 |
| Germain, 2011 | Uniqueness neighbor | Weak-strong uniqueness machinery cited for the strong-solution uniqueness step. | Journal of Mathematical Fluid Mechanics 13, 137-146 |
| Fermat Difference - DEP-E | Related Black Lake artifact | Theorem-regime extraction and explicit limits of structural versus formal proof review. | `.lake-data/DEP-E/DEP-E-20260709-Fermat Difference/fermat-difference-manuscript.md` |
| Physical Data AI - DEP-E | Related Black Lake artifact | Translates PDE structure into domain-fit and implementation constraints without treating equations as universally transferable. | `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` |
| RRT-CBF Motion - DEP-E | Related Black Lake artifact | Connects invariance and boundary constraints to computational telemetry and explicit assumption/fallback review. | `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2102.09229 | Identity, authors, versions, abstract, subject, DOI links. | 2026-07-12 | Primary arXiv record. |
| R2 | https://arxiv.org/pdf/2102.09229 | Complete paper, theorems, proof structure, limitations, and references. | 2026-07-12 | Inspected through private extraction cache; not redistributed. |
| R3 | https://doi.org/10.48550/arXiv.2102.09229 | Persistent arXiv identifier. | 2026-07-12 | Metadata reference. |
| R4 | https://link.springer.com/article/10.1007/s00205-022-01790-4 | Version-of-record metadata, abstract, dates, venue, and bibliography. | 2026-07-12 | Publisher page; full subscription content not collected. |
| R5 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | DEP-E, path, README, attribution, stability, and commit rules. | 2026-07-12 | Repository authority. |
| R6 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Related-repository deposition and attribution context. | 2026-07-12 | Repository authority. |
| R7 | `.lake-data/DEP-E/DEP-E-20260709-Fermat Difference/fermat-difference-manuscript.md` | Theorem-regime and proof-review bridge. | 2026-07-12 | Contextual DEP evidence only. |
| R8 | `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` | PDE/domain-fit implementation bridge. | 2026-07-12 | Contextual DEP evidence only. |
| R9 | `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` | Invariance and boundary-constraint bridge. | 2026-07-12 | Contextual DEP evidence only. |

## Appendix

### Replication and Verification Checklist

- [x] Stable arXiv and publisher identifiers cross-checked.
- [x] Strong and weak theorem statements inspected.
- [x] Effective-flux, conformal-map, Green-function, commutator, and density-bound path inspected.
- [x] Higher-order estimates and approximation/compactness sections inspected.
- [x] Exactly three related DEP entries inspected.
- [x] Uniform selection and dedup validation recorded.
- [x] Cache status and extractor fallback recorded.
- [ ] Formula-perfect source transcription completed.
- [ ] Every estimate independently rederived.
- [ ] Imported compactness and uniqueness results independently verified.
- [ ] Proof assistant formalization completed.
- [ ] Open viscosity-exponent regime resolved.

### Related-Entry Bridge Notes

- `Fermat Difference`: overlap is theorem-regime classification, dependency preservation, and the distinction between source review and formal proof checking.
- `Physical Data AI`: overlap is PDE structure and the need to state when an equation family fits a target domain; it does not support the Navier-Stokes theorem.
- `RRT-CBF Motion`: overlap is invariance under explicit dynamical and boundary constraints, plus the gap between mathematical conditions and operational evidence.
