---
title: "Integrals and Rigidity - DEP-E"
generated_at: "2026-07-17 (date-only public marker)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of sharp mean value rigidity and an asymptotic weighted scalar-curvature formula on manifolds with nonnegative Ricci curvature."
source_status: "verified complete local PDF and full-paper HTML; metadata and TeX/source retained locally; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-17"
temporal_cutoff: "arXiv v1 and public records available through 2026-07-17"
primary_url: "https://arxiv.org/abs/2602.10393"
stable_identifier: "arXiv:2602.10393v1; DOI:10.48550/arXiv.2602.10393"
confidence_summary: "High for identity, theorem statements, assumptions, and reported proof architecture; medium for proof correctness because no formal or independent verification was performed."
safety_scope: "non-sensitive mathematical research, educational analysis, and bounded verification tooling"
distribution_notes: "Public URLs and generated Markdown only; source documents, local paths, exact execution times, machine details, and caches withheld."
---

# Integrals and Rigidity - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2602.10393v1 | https://arxiv.org/abs/2602.10393 | Public metadata; abstract not treated as the paper | 2026-07-17 | Inspected |
| S2 | *Integrals and Rigidity on Manifolds with Nonnegative Ricci Curvature* | Primary paper | PDF and full-paper HTML | arXiv:2602.10393v1; 32 PDF pages | https://arxiv.org/pdf/2602.10393; https://arxiv.org/html/2602.10393 | Verified complete local copies inspected; files withheld | 2026-07-17 | Complete paper inspected |
| S3 | arXiv TeX/source bundle | Primary source companion | Source archive | arXiv:2602.10393v1 | https://arxiv.org/e-print/2602.10393 | Collected locally for provenance; not deposited and not used as an independent proof check | 2026-07-17 | Downloaded and withheld |
| S4 | arXiv-issued DOI and license | Persistent identity and usage context | DOI / license deed | 10.48550/arXiv.2602.10393; CC BY 4.0 | https://doi.org/10.48550/arXiv.2602.10393; https://creativecommons.org/licenses/by/4.0/ | DOI verified from arXiv; license deed inspected | 2026-07-17 | Verified |
| S5 | Hyperbolic Catenaries - DEP-E | Related processed artifact 1 of 3 | Markdown | DEP-E-20260716-Hyperbolic Catenaries | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Hyperbolic%20Catenaries/hyperbolic_catenaries_manuscript.md | Contextual synthesis; not evidence for this paper's theorems | 2026-07-17 | Inspected |
| S6 | Flag Hardy Operators - DEP-E | Related processed artifact 2 of 3 | Markdown | DEP-E-20260716-Flag Hardy Operators | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md | Contextual synthesis; not evidence for this paper's theorems | 2026-07-17 | Inspected |
| S7 | Global NS Existence - DEP-E | Related processed artifact 3 of 3 | Markdown | DEP-E-20260712-Global NS Existence | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-Global%20NS%20Existence/global_ns_existence_manuscript.md | Contextual synthesis; not evidence for this paper's theorems | 2026-07-17 | Inspected |
| S8 | Black Lake repository authorities | Deposition and source-withholding rules | Markdown | Live default branch | https://github.com/Delphoa/Black-Lake/blob/main/README.md; https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | Process authority, not research evidence | 2026-07-17 | Fetched and read |
| S9 | Black-Lake-Data repository authority | Companion dedup context | Markdown | Live default branch | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Process authority and remote search context | 2026-07-17 | Fetched and read |
| S10 | Integrity, selection, and dedup records | Process evidence | Public-safe generated summaries | Complete-source gate | Public artifact summaries only | Local paths, exact timestamps, and private manifests withheld | 2026-07-17 | Validated |

The authors are Zixuan Chen, Guoyi Xu, and Shuai Zhang. The canonical arXiv record classifies the paper under Differential Geometry (`math.DG`), gives Mathematics Subject Classification codes `35K15` and `53C20`, and records submission of v1 on 2026-02-11. The PDF metadata identifies 32 pages, the arXiv-issued DOI, and CC BY 4.0.

The sampled archive unit initially contained a valid PDF but no full-paper HTML and was therefore classified `partial`. Review stopped until a bounded repair collected official full-paper HTML, metadata HTML, and a TeX/source companion. The final source state is `complete`. Source files and all machine-specific records remain local; this DEP contains generated Markdown and public URLs only.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Primary metadata | Title, authors, arXiv version, date, subject, abstract, DOI, license link, and canonical artifact URLs | Source identity and chronology | High | Abstract does not establish the theorem details |
| E2 | S2 | Complete primary paper | Theorem 1.1 / Theorems 4.3 and 4.5, generalized divergence theorem, monotone quantity, and Bishop-Gromov equality argument | Radius-free sharp mean value inequality and Euclidean-ball rigidity | High for reporting | Proof not formally certified |
| E3 | S2 | Complete primary paper | Green-function definition of `b`, weighted-volume identities, Bochner/coarea analysis, and asymptotic estimates | Analytical mechanism connecting Green functions and curvature | High for reporting | Dense notation and imported lemmas were not independently reproved |
| E4 | S2 | Complete primary paper | Theorem 1.5 / Theorem 6.6, level-set topology, Gauss-Bonnet, Gauss equation, and asymptotic volume ratio | Exact three-dimensional weighted scalar-curvature limit | High for reporting | Restricted to the stated nonparabolic/maximal-volume-growth setting |
| E5 | S2 | Complete primary paper | Corollary 1.10 / Corollary 6.7 | Ricci-pinched maximal-volume-growth three-manifold is Euclidean | High for reporting | Does not prove the unrestricted Hamilton pinching conjecture |
| E6 | S2 | Author discussion | Conjecture 1.7 and statement that the broader nonparabolic case without maximal volume growth remains open | Research boundary and extension target | High | Open rather than established |
| E7 | S5-S7 | Related processed artifacts | Curvature/rigidity, geometry-adapted integral analysis, and Green-function/divergence proof patterns | Cross-DEP synthesis only | Medium | These records do not validate the selected paper |
| E8 | S10 | Process evidence | Uniform draw, zero-reselection dedup result, initial source failure, bounded repair, and independent integrity checks | Eligibility and review preconditions | High | Private local locators intentionally withheld |
| E9 | S1-S3 | Availability evidence | Canonical links, full paper, and source bundle; focused code search | Preprint/source availability and absence of identified official code | Medium-high | Search cannot prove that no code exists anywhere |

## Executive Summary

Chen, Xu, and Zhang connect two forms of rigidity on complete Riemannian manifolds with nonnegative Ricci curvature. The first is local-to-global and analytic. For a nonzero smooth function `f ≥ 0` with `Δf ≤ 0`, they prove for every center `x` and every radius `r > 0`

`f(x) ≥ [n ω_n r^(n-1)]^(-1) ∫_(∂B_x(r)) f dσ`.

This is the sharp Schoen-Yau boundary mean value inequality without the earlier restriction that `r` lie below the injectivity radius. If equality holds at one center and radius, the entire geodesic ball is isometric to the Euclidean ball. The proof handles the cut locus by pulling the function back through the exponential map, establishing a generalized divergence theorem for geodesic balls, and proving a scale quantity `F(t)` is nonincreasing. Equality removes the analytic and volume-comparison defects, allowing Bishop-Gromov rigidity to finish the argument.

The second result is asymptotic and three-dimensional. Let `b = G(q,·)^(1/(2-n))` be the Green-function radius and `V_M` the asymptotic volume ratio. On a complete noncompact three-manifold with nonnegative Ricci curvature and maximal volume growth, the authors prove

`lim_(r→∞) [1/r] ∫_(b≤r) R |∇b| = 8π(1 - V_M)`.

The exact coefficient arises from the topology and curvature of Green-function level sets: asymptotically, the problematic higher-genus levels have zero density, while connected spherical levels contribute through Gauss-Bonnet. Under `Ric ≥ ε R g ≥ 0`, a separate vanishing directional-Ricci limit combines with the formula to force `V_M = 1`; Bishop-Gromov rigidity then yields Euclidean three-space.

This is a theorem-driven preprint, not an empirical study. Confidence is high that the artifact reports the assumptions, theorem statements, and proof architecture faithfully because the complete PDF and formula-preserving full-paper HTML were inspected. Confidence is medium for independent correctness: the long chain of geometric-measure, elliptic, topological, and comparison arguments was not formally verified, and no official proof code was identified.

## Detailed Summary

### Problem Context

Mean value identities translate differential equations into integral constraints. In Euclidean space a harmonic function equals suitable sphere or ball averages. On curved spaces, curvature and cut-locus geometry disturb that exact identity. Under nonnegative Ricci curvature, comparison geometry still yields sharp inequalities, but extending them past the injectivity radius requires a way to integrate across the nonsmooth structure of geodesic spheres.

The curvature half of the paper addresses a second question: whether a scale-invariant integral of scalar curvature can quantify deviation from Euclidean volume growth. In dimension two, Gauss-Bonnet and Cohn-Vossen connect total curvature and topology. The authors seek a three-dimensional analogue built from level surfaces of a Green-function-derived radius.

### Green-Function Radius and Mean Value Formulas

On a nonparabolic manifold the minimal positive Green function `G(q,x)` defines

`b(x) = G(q,x)^(1/(2-n))`.

Near the pole, `b` behaves like a normalized distance. Weighted integrals over `b`-sublevel and level sets therefore act as analytic replacements for Euclidean radius averages. Section 2 differentiates these weighted quantities using Green's identity and coarea, obtaining characterizations of harmonicity and subharmonicity through mean value behavior.

### Divergence Across the Cut Locus

The exponential map is smooth before the cut time but geodesic spheres can lose smoothness at the cut locus. Section 3 works in the tangent space, records the radial Jacobian, and uses finite-perimeter and measure-theoretic boundary machinery to establish a generalized divergence theorem for geodesic balls. This lets the proof compare radial integrals without requiring `r < inj(x)`.

### Monotonicity and Equality Rigidity

For a nonnegative superharmonic function the paper defines a scale quantity `F(t)` that agrees with the classical Schoen-Yau expression below the injectivity radius. Rather than rely only on a pointwise derivative, the authors estimate `F(t)-F(t-s)` and use a nested-interval contradiction together with the generalized divergence theorem to show that `F` is nonincreasing for all `t > 0`.

The small-radius limit of `F` is `n ω_n f(q)`. Comparing the boundary integral with `F(t)` yields the sharp inequality for arbitrary radii. If equality occurs, the strong maximum principle gives positivity, the monotonicity defects vanish, and the radial Jacobian reaches the Euclidean comparison value. Bishop-Gromov equality then identifies the ball with `B^n(r)`.

### Weighted Volume and Curvature Defects

Part II studies weighted volume and the geometry of regular level sets of `b`. Bochner's formula, coarea, divergence, and the second fundamental form turn derivatives of weighted volume into nonnegative curvature and Hessian defect terms. Their integrals control the asymptotic behavior of the level-set mean curvature and the radial component of Ricci curvature.

The proof is not merely a cone-limit heuristic. It develops intrinsic integral estimates that survive possible nonuniqueness or singularity of tangent cones. Maximal volume growth supplies the asymptotic normalization needed for exact limits.

### Level-Set Topology and the Exact Formula

In dimension three, the source uses structural results for complete noncompact manifolds with nonnegative Ricci curvature to show that the relevant nonparabolic manifold is diffeomorphic to `R^3` and that smooth Green-function levels are connected. The authors partition regular levels according to topology. Levels of genus at least one may occur, but under maximal volume growth their parameter set has zero asymptotic density.

On the dominant spherical levels, Gauss-Bonnet supplies a fixed intrinsic-curvature contribution. The Gauss equation connects that intrinsic curvature to ambient scalar curvature, Ricci curvature, mean curvature, and the second fundamental form. Combining the topological density statement with the weighted-volume limits yields

`lim_(r→∞) r^(-1) ∫_(b≤r) R |∇b| = 8π(1 - V_M)`.

The right-hand side is zero exactly at Euclidean asymptotic volume ratio. It increases as the asymptotic volume ratio drops, so the formula measures large-scale geometric deficit through a weighted scalar-curvature average.

### Pinching Application

If `Ric ≥ ε R g ≥ 0`, integrating the pinching inequality in the radial direction compares the weighted scalar-curvature integral with a directional-Ricci quantity whose normalized limit is zero. The exact formula then forces `1 - V_M = 0`. Bishop-Gromov rigidity implies the manifold is isometric to `R^3`.

This is explicitly a maximal-volume-growth, three-dimensional case of Hamilton's pinching conjecture. The manuscript does not support removing those qualifications.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | The sharp boundary mean value inequality holds for every radius on a complete manifold with nonnegative Ricci curvature. | Author theorem | E2; Theorem 1.1 / 4.3 | Statement is explicit and the proof architecture addresses the cut-locus obstruction; correctness not independently certified. | High for reporting |
| C2 | Equality at one center and radius forces the geodesic ball to be Euclidean. | Author theorem | E2; Theorem 1.1 / 4.5 | The equality case is tied to positivity, vanishing defects, volume comparison, and Bishop-Gromov rigidity. | High for reporting |
| C3 | In the stated three-dimensional maximal-volume-growth setting, the weighted scalar-curvature limit equals `8π(1-V_M)`. | Author theorem | E3-E4; Theorem 1.5 / 6.6 | Full theorem and proof chain inspected; the boundary conditions are substantial and must remain visible. | High for reporting |
| C4 | Ricci pinching plus maximal volume growth forces Euclidean `R^3`. | Author corollary | E5; Corollary 1.10 / 6.7 | Supported as a corollary of the exact limit and Bishop-Gromov rigidity, not as the unrestricted conjecture. | High for reporting |
| C5 | The proof pattern can be engineered as an auditable analytic-to-geometric certificate. | Reviewer interpretation | E2-E7 | Monotonicity, explicit defect terms, topology checks, and a terminal rigidity theorem form a reusable verification pattern. | Medium |

## Methodology

- `Research objective`: Preserve a source-grounded DEP-E review of the paper's main inequalities, rigidity mechanisms, curvature formula, assumptions, limitations, and implementation relevance.
- `Sources inspected`: Canonical arXiv metadata, verified complete PDF, verified full-paper HTML, arXiv DOI and license link, live Black Lake authorities, live Black-Lake-Data authority, and exactly three related processed Black Lake artifacts.
- `Discovery strategy`: Enumerate local PDFs with `rg --files -g "*.pdf"`, collapse them by parent directory into paper units, select by a uniform `Get-Random` array index, inspect local companions, and cross-check canonical public sources.
- `Selection result`: 75,777 PDFs produced 75,776 unique paper units. Zero-based index 67,845 selected arXiv:2602.10393. The first draw was accepted.
- `Dedup and reselection`: ID, DOI, normalized title, and slug searches across `.logs`, `.reports`, `.lake-data`, public staging, automation memory, the active worktree, and relevant Black-Lake-Data results found no prior Arxiv DEP artifact or 24-hour marker. Exclusions and reselections were both zero.
- `Source gate`: The unit was initially `partial` because full-paper HTML was missing. Review paused; one bounded repair produced official HTML and companion provenance. Independent checks verified the PDF header/EOF and substantive full-paper structure before synthesis.
- `Inclusion criteria`: Primary theorem statements, proof dependencies, exact assumptions, author-stated open boundaries, and related records with concrete conceptual overlap.
- `Exclusion criteria`: Abstract-only claims, secondary summaries, unverified code claims, local paths, exact local timestamps, machine details, and source-file redistribution.
- `Analytical approach`: Conceptual, comparative, implementation, replication, and evidence-audit analysis of a theorem-driven mathematical paper.
- `Extraction process`: Formula-aware inspection of the verified HTML, PDF metadata/page checks, and targeted theorem/proof-structure reconstruction. The TeX/source bundle was retained for provenance but was not represented as independently inspected proof evidence.
- `Evidence handling`: Major claims map to ledger IDs and public source locators. Related DEP entries are contextual only.
- `Uncertainty handling`: The artifact separates author theorem, reviewer interpretation, process evidence, and unverified proof correctness. Missing publisher and code records remain visible.

## Scope, Constraints, and Assumptions

- `Scope`: arXiv v1 identity, main theorems, core proof architecture, exact hypotheses, limitations, related processed context, and bounded research-to-tool translations.
- `Temporal boundary`: Sources and repository state inspected through the date-only marker 2026-07-17.
- `Evidence limits`: No journal version, referee report, independent replication, formal proof, or official code repository was identified. Dense imported results were not reproved.
- `Assumptions`: Standard notation is interpreted as in the paper: `Ric` is Ricci curvature, `R` scalar curvature, `ω_n` unit-ball volume, `G` the minimal positive Green function, `b = G^(1/(2-n))`, and `V_M` asymptotic volume ratio.
- `Constraints`: Public artifacts must omit local locators and source files. Mathematical implementation examples remain educational and do not claim proof certification.
- `Out of scope`: Proving the full Hamilton pinching conjecture, extending the theorem beyond maximal volume growth, certifying every cited lemma, or redistributing source documents.
- `Intended use`: DEP deposition, mathematical review, proof-audit planning, theorem dependency mapping, and safe MVP ideation.
- `Audience`: Geometric analysts, PDE researchers, formalization engineers, and research-tool developers.
- `Reproducibility boundary`: Source identity and theorem statements are reproducible from public arXiv artifacts; independent proof correctness is not established by this review.
- `Data sensitivity`: Public mathematical research; local source-document locality remains mandatory.

## Observations

- `Observed pattern`: Both headline results use monotonicity to turn nonnegative geometric defects into rigidity. In Part I the terminal equality is a Euclidean ball; in Part II the terminal asymptotic-volume equality is Euclidean space.
- `Technical implication`: The generalized divergence theorem is enabling infrastructure, not an incidental lemma. It removes the injectivity-radius ceiling by making cut-locus integration auditable.
- `Observed pattern`: Green-function level sets act as synthetic coordinate spheres whose weighted geometry is better aligned with noncompact analysis than raw geodesic spheres.
- `Technical implication`: The coefficient `8π` is topological as well as analytic; it enters through Gauss-Bonnet on the asymptotically dominant spherical levels.
- `Contradiction or tension`: The abstract's phrase “Hamilton's pinching conjecture in this case” is accurate only if “this case” retains dimension three and maximal volume growth. Any shortened retelling should surface those assumptions.
- `Open question`: The authors expect the exact integral identity to extend beyond maximal volume growth to a wider nonparabolic setting, but that extension is not proved here.
- `Reviewer hypothesis`: A quantitative version of the defect bookkeeping may support almost-rigidity estimates, but no rate converting small mean-value deficit to metric closeness is supplied.

## Considerations

- The paper is a v1 preprint. Citation should distinguish established source statements from independent mathematical acceptance.
- Formalization would need libraries for cut loci, finite-perimeter sets, coarea, Green functions on noncompact manifolds, Bishop-Gromov comparison, and three-manifold topology; the dependency surface is much larger than the compact headline statements suggest.
- Numerical experiments are not the natural validation mode. Better checks include symbolic normalization, dependency tracing, special-case recovery on Euclidean space, and theorem-assumption linting.
- A product should not infer a theorem from matching keywords. It must track dimension, completeness, nonparabolicity, Ricci sign, maximal volume growth, function sign, Laplacian sign, and equality versus near-equality.
- The proof's use of exceptional level sets suggests that “almost every scale” and “all scales” must be represented separately in any machine-readable theorem graph.
- Source documents are openly licensed, but this automation's locality policy still withholds them from the repository and Slack.

## Strengths

- **Sharp scope extension:** The mean value inequality removes the radius-below-injectivity restriction while retaining the Euclidean sharp constant.
- **Equality mechanism:** The paper does not stop at an inequality; it traces equality to Euclidean geometry through explicit monotonicity and comparison defects.
- **Independent-use lemma:** The generalized divergence theorem for geodesic balls addresses a recurring nonsmooth-boundary obstacle.
- **Exact asymptotic identity:** The scalar-curvature result is an equality, not only a limsup bound, under maximal volume growth.
- **Topology-analysis bridge:** Green-function level topology and Gauss-Bonnet are integrated with Bochner, coarea, and volume comparison in a coherent proof chain.
- **Concrete application:** The pinching corollary makes the asymptotic identity operational within a clearly stated geometric regime.

## Weaknesses

- **Narrow exact-formula regime:** The scalar-curvature equality is three-dimensional and assumes maximal volume growth; the wider nonparabolic case remains open.
- **No quantitative stability:** Equality rigidity is exact, with no explicit estimate for near-equality or noisy geometric data.
- **Heavy imported machinery:** Several key steps rely on established comparison, topology, regularity, and geometric-measure results; this review did not independently certify those dependencies.
- **Preprint-only evidence:** No publisher version, independent referee report, or formal verification was identified.
- **Limited reproducibility artifacts:** No official code, proof assistant development, diagram set, or machine-readable theorem dependency graph was found.
- **Notation accessibility:** Formula-dense exposition and HTML text extraction can hide symbols, increasing the risk of incorrect secondary summaries.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Prove an almost-rigidity estimate | Mean value equality case | Exact equality is brittle for applications | Quantitative geometric closeness from a measurable deficit | Likely substantial new comparison analysis | Test on warped products and model cones with known deficits |
| Remove or weaken maximal volume growth | Scalar-curvature formula | Authors identify the broader nonparabolic case as open | Wider applicability and closer relation to the proposed conjecture | Topology and asymptotic normalization may fail | Establish substitute density and level-set controls |
| Publish a theorem dependency graph | Reproducibility | The argument crosses several mathematical subfields | Faster audit and formalization planning | Maintenance burden | Link every theorem to local lemmas and external citations |
| Add explicit model checks | Exposition | Long formulas are difficult to sanity-check | Immediate validation on Euclidean and rotationally symmetric examples | Does not prove the general case | Compute `b`, `V_M`, and both sides on documented models |
| Separate assumption summaries | Communication | The pinching corollary is easy to overgeneralize | Reduced citation drift | Minor editorial cost | Add boxed hypothesis tables before each headline theorem |

## Potential Implementations

1. **Theorem-assumption linter**
   - `User`: Research reviewer or technical writer.
   - `Goal`: Detect retellings that omit dimension, completeness, Ricci sign, maximal volume growth, or equality conditions.
   - `Core mechanism`: Parse a theorem summary into normalized hypotheses and compare it with a curated theorem card.
   - `Required inputs`: Public theorem text and a human-reviewed schema.
   - `Outputs`: Missing-hypothesis warnings and citation-ready theorem cards.
   - `Risk controls`: Never labels a proof correct; preserves source/version and reviewer approval.
   - `Evaluation`: Seed summaries with controlled omissions and measure detection precision/recall.

2. **Rigidity proof dependency explorer**
   - `User`: Geometric analyst or formalization engineer.
   - `Goal`: Trace how divergence, monotonicity, topology, and comparison results feed the final conclusions.
   - `Core mechanism`: Represent lemmas, assumptions, defect terms, and terminal rigidity steps as a directed graph.
   - `Required inputs`: Human-curated theorem and citation nodes.
   - `Outputs`: Dependency graph, unresolved imports, and suggested formalization order.
   - `Risk controls`: Every edge requires a source location; inferred edges are visibly labeled.
   - `Evaluation`: Audit graph coverage against the paper's section-level proof structure.

3. **Model-manifold identity sandbox**
   - `User`: Graduate student or researcher.
   - `Goal`: Exercise the mean value and curvature formulas on synthetic, known metrics.
   - `Core mechanism`: Compute symbolic or numerical radial Jacobians, Green-function radii, volume ratios, and normalized curvature integrals for selected model manifolds.
   - `Required inputs`: Explicit smooth radial metric functions with domain and regularity declarations.
   - `Outputs`: Plots, convergence tables, and theorem-hypothesis checks.
   - `Risk controls`: Educational models only; no claim of general proof or production numerical reliability.
   - `Evaluation`: Recover Euclidean equality and known comparison behavior under controlled perturbations.

## Three Ways to Exercise This Research

1. `Euclidean recovery`: Objective—verify the equality cases. Inputs—Euclidean metric, constant positive harmonic/superharmonic functions, and the standard Green function. Method—compute the sphere average, radial Jacobian, `V_M`, and weighted curvature integral. Output—a zero-defect certificate. Success criterion—both equality statements reduce correctly. Stop condition—any normalization mismatch remains unresolved.
2. `Assumption-removal stress test`: Objective—measure which conclusions fail when one hypothesis is removed. Inputs—documented model manifolds with negative Ricci regions, nonmaximal volume growth, or parabolic behavior. Method—evaluate whether Green functions, normalized volumes, topology statements, and limits still exist. Output—a hypothesis/failure matrix. Success criterion—each failure is tied to an explicit proof dependency. Stop condition—model regularity or completeness cannot be established.
3. `Proof-graph reconstruction`: Objective—build an auditable dependency map from Theorem 1.1 and Theorem 1.5 back to lemmas and cited results. Inputs—public paper and curated theorem cards. Method—record nodes, assumptions, equations, and external imports; then run orphan and cycle checks. Output—a reviewable graph and formalization backlog. Success criterion—every terminal claim has a complete source trace. Stop condition—an edge cannot be justified from inspected text.

## Example MVP Product

- `Product name`: Rigidity Trace
- `Target user`: Mathematical reviewers, journal editors, and proof-formalization teams.
- `Problem`: Compact theorem summaries often drop the assumptions and intermediate defects that make rigidity statements valid.
- `Core workflow`: Import a public paper; select a theorem; enter or review its normalized assumptions; connect proof lemmas and external results; generate an assumption-complete theorem card, dependency graph, and unresolved-evidence list.
- `Data requirements`: Public paper text, human-reviewed equation snippets, bibliographic identifiers, and a small ontology for geometric assumptions.
- `Architecture`: Local-first Markdown/JSON store, parser-assisted extraction, graph database or typed adjacency list, deterministic validators, and a static report renderer.
- `Success metrics`: 100% retention of headline hypotheses in curated test cases; zero unlabeled inferred edges; reviewer agreement on dependency coverage; successful Euclidean normalization checks.
- `Risk controls`: No autonomous proof-correctness verdict; source/version pinning; reviewer sign-off; inference labels; no upload of local source files or private paths.
- `Limitations`: Mathematical notation parsing is brittle; graph completeness does not imply proof correctness; imported literature remains a separate verification burden.
- `MVP boundary`: The first release handles this paper's two headline chains and three model checks only.
- `Deployment model`: Local CLI plus static HTML/Markdown report.
- `Evaluation plan`: Golden theorem cards, mutation tests that delete assumptions, graph orphan checks, and expert review.
- `Failure modes`: Symbol loss, mistaken quantifier scope, conflated theorem versions, or treating a contextual citation as a proof dependency.
- `Maintenance plan`: Versioned theorem schemas and reviewer-approved updates when the paper is revised or published.

## Related Research and Reading

### Exactly Three Related Black Lake Entries

| Item | Type | Concrete overlap | Public locator |
|---|---|---|---|
| Hyperbolic Catenaries - DEP-E | Processed differential-geometry review | Curvature equations, manifold models, variational structure, and geometric rigidity provide the closest domain bridge. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Hyperbolic%20Catenaries/hyperbolic_catenaries_manuscript.md |
| Flag Hardy Operators - DEP-E | Processed harmonic-analysis review | Shows that sharp integral estimates and operator bounds must preserve the anisotropic geometry and scaling of the ambient space. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md |
| Global NS Existence - DEP-E | Processed PDE review | Uses Green functions, divergence identities, and geometry-sensitive cancellation to overcome a domain-geometry obstruction. | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-Global%20NS%20Existence/global_ns_existence_manuscript.md |

### Primary and Near-Primary Reading Named by the Paper

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Schoen and Yau, *Lectures on Differential Geometry* | Classical source | Earlier sharp mean value inequality with an injectivity-radius restriction, as characterized by the paper. | ISBN 9781571460125 |
| Cheeger and Colding, lower Ricci curvature work | Foundational comparison research | Tangent-cone and maximal-volume-growth context used in the paper's asymptotic motivation and imports. | Referenced in the primary paper |
| Colding-Minicozzi monotonicity work | Foundational geometric analysis | Green-function and weighted-volume monotonicity framework extended or reorganized by the paper. | Referenced in the primary paper |
| Liu, three-manifold structure theorem | Foundational topology/geometry | Supplies the structural alternative used before proving the relevant manifold is diffeomorphic to `R^3`. | Referenced in the primary paper |
| Xu, integral scalar-curvature work | Direct predecessor | Provides a prior limsup inequality and pinching application under additional assumptions. | Referenced in the primary paper |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/2602.10393 | Metadata, abstract, version, authors, DOI, license link, public artifact URLs | 2026-07-17 | Canonical primary record |
| R2 | https://arxiv.org/pdf/2602.10393 | Complete theorem and proof review | 2026-07-17 | Verified local copy inspected and withheld |
| R3 | https://arxiv.org/html/2602.10393 | Formula-aware structural inspection | 2026-07-17 | Verified full-paper HTML inspected and withheld |
| R4 | https://arxiv.org/e-print/2602.10393 | Source companion provenance | 2026-07-17 | Collected locally and withheld; not claimed as independently analyzed |
| R5 | https://doi.org/10.48550/arXiv.2602.10393 | Persistent identifier | 2026-07-17 | arXiv-issued DOI |
| R6 | https://creativecommons.org/licenses/by/4.0/ | License context | 2026-07-17 | Reached from arXiv record |
| R7 | https://github.com/Delphoa/Black-Lake/blob/main/README.md | Repository authority | 2026-07-17 | Process source only |
| R8 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md | DEP-E filing and publication-index authority | 2026-07-17 | Process source only |
| R9 | https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md | Companion repository authority and dedup context | 2026-07-17 | Process source only |
| R10 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Hyperbolic%20Catenaries/hyperbolic_catenaries_manuscript.md | Related differential-geometry context | 2026-07-17 | Contextual, not claim evidence |
| R11 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Flag%20Hardy%20Operators/flag_hardy_operators_manuscript.md | Related harmonic-analysis context | 2026-07-17 | Contextual, not claim evidence |
| R12 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260712-Global%20NS%20Existence/global_ns_existence_manuscript.md | Related Green-function/divergence context | 2026-07-17 | Contextual, not claim evidence |

## Appendix

### Selection and Dedup Audit

| Field | Result |
|---|---|
| Enumeration | `rg --files -g "*.pdf"` |
| PDF candidates | 75,777 |
| Unique parent-directory paper units | 75,776 |
| Random method | Uniform `Get-Random` array index |
| Selected index | 67,845 zero-based / 67,846 one-based |
| Selected identifier | arXiv:2602.10393 |
| Exclusions | 0 |
| Reselections | 0 |
| Same-paper 24-hour markers | 0 |
| Dedup keys | arXiv ID, arXiv DOI, normalized title, slug |
| Dedup surfaces | Black Lake logs, reports, DEP data, public staging index, automation memory, active worktree, relevant Black-Lake-Data results |

### Source-Integrity Audit

| Check | Result |
|---|---|
| Initial state | `partial`: PDF present, full-paper HTML absent |
| Repair | One bounded direct-arXiv companion-bundle attempt; no retry or strategy switch |
| PDF | 308,002 bytes; `%PDF-`; trailing `%%EOF`; staged hash matched preserved copy |
| Full-paper HTML | 952,870 bytes; 137,716 body characters; document marker present; 63 heading markers; five structure terms |
| Metadata HTML | 39,280 bytes; metadata only |
| TeX/source archive | 27,139 bytes; retained locally |
| Partial files | 0 |
| Final state | `complete`; independent gate passed before review |
| Public source upload | None; `.source/` not created |

### Replication Checklist

- Verify the canonical v1 identity and theorem numbering.
- Reconstruct the generalized divergence theorem's finite-perimeter dependencies.
- Recover the small-radius limit of `F(t)` and its global monotonicity.
- Trace equality through every nonnegative defect to Bishop-Gromov rigidity.
- Define `b` and `V_M` with the paper's normalization.
- Reproduce the weighted-volume and radial-Ricci asymptotic limits.
- Verify the topology and density treatment of regular Green-function levels.
- Check the `8π` coefficient through Gauss-Bonnet and the Gauss equation.
- Confirm that the pinching corollary retains dimension three and maximal volume growth.
- Preserve “not independently verified” until a formal or expert proof audit is completed.
