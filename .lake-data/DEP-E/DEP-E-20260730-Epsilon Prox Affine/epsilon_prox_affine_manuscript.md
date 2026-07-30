---
title: "Epsilon Prox-Affine - DEP-E"
generated_at: "2026-07-30 (public-safe date; exact execution time withheld)"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of Epsilon, a compiler and ADMM-based runtime for disciplined convex programs represented in prox-affine form."
source_status: "verified complete local PDF, full-paper HTML, metadata HTML, and TeX/source package inspected; all source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-30"
temporal_cutoff: "arXiv:1511.04815v1 and inspected public records through 2026-07-30"
primary_url: "https://arxiv.org/abs/1511.04815"
stable_identifier: "arXiv:1511.04815v1; DOI:10.48550/arXiv.1511.04815"
confidence_summary: "High for paper identity, architecture, equations, and source-reported benchmark transcription; medium for causal performance interpretation; low for current implementation and production performance because code was inaccessible and experiments were not reproduced."
safety_scope: "non-sensitive numerical optimization research and local-only prototype design"
distribution_notes: "No PDF, HTML, metadata page, TeX/source archive, extracted text, render, cache, verification record, or local path is redistributed."
---

# Epsilon Prox-Affine - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | Canonical arXiv record | Primary metadata | HTML | arXiv:1511.04815v1 | https://arxiv.org/abs/1511.04815 | Metadata and source locators; abstract alone was not used for detailed claims. | 2026-07-30 | Inspected |
| S2 | Paper PDF | Primary artifact | PDF | arXiv:1511.04815v1 | https://arxiv.org/pdf/1511.04815 | Complete paper inspected locally and visually; file withheld. | 2026-07-30 | Verified complete |
| S3 | Full-paper rendering | Primary artifact fallback | HTML | arXiv:1511.04815v1 | https://ar5iv.labs.arxiv.org/html/1511.04815 | Approved full-paper fallback after the official arXiv HTML endpoint was unavailable; local copy withheld. | 2026-07-30 | Verified complete |
| S4 | Paper source package | Primary source | TeX archive | arXiv:1511.04815v1 | https://arxiv.org/e-print/1511.04815 | Used to cross-check equations, table values, captions, and conclusion; archive withheld. | 2026-07-30 | Inspected |
| S5 | arXiv-issued DOI | Persistent identity | DOI | 10.48550/arXiv.1511.04815 | https://doi.org/10.48550/arXiv.1511.04815 | Persistent locator, not a separate peer-reviewed version. | 2026-07-30 | Resolved |
| S6 | arXiv license record | Usage context | HTML | Non-exclusive distribution 1.0 | https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html | Grants arXiv distribution rights; it was not treated as permission for this automation to upload source files. | 2026-07-30 | Inspected |
| S7 | Author publication record | Author context | HTML | 2015 preprint listing | https://zicokolter.com/publications/ | Confirms the preprint and links Epsilon software. | 2026-07-30 | Inspected |
| S8 | Paper-linked Epsilon repository | Implementation locator | GitHub repository | `mwytock/epsilon` | https://github.com/mwytock/epsilon | Linked by the paper; returned not found during this review. | 2026-07-30 | Inaccessible |
| S9 | Sparse SSN-PMM DEP | Related research | Markdown | DEP-E-20260719 | `.lake-data/DEP-E/DEP-E-20260719-Sparse SSN PMM/sparse_ssn_pmm_manuscript.md` | Related synthesis, not primary evidence for Epsilon. | 2026-07-30 | Inspected |
| S10 | CAP Rank Sparsity DEP | Related research | Markdown | DEP-E-20260719 | `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` | Related synthesis, not primary evidence for Epsilon. | 2026-07-30 | Inspected |
| S11 | GPMD Regularized RL DEP | Related research | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` | Related synthesis, not primary evidence for Epsilon. | 2026-07-30 | Inspected |
| S12 | Selection, dedup, repair, and validation records | Process evidence | Private records | Black Lake Arxiv DEP 0900 | Withheld local context | Supports only selection, integrity, and no-source-upload claims. | 2026-07-30 | Verified |

- **Paper title:** *Convex programming with fast proximal and linear operators*
- **Authors:** Matt Wytock, Po-Wei Wang, and J. Zico Kolter
- **Source platform:** arXiv, Mathematics - Optimization and Control (`math.OC`)
- **Submission:** 2015-11-16; the rendered paper is dated 2015-11-17
- **Version:** v1 only in the canonical record
- **Publication status:** Author record labels it a preprint; no separate peer-reviewed version of this exact paper was established
- **Local source paths:** Withheld by public-output policy
- **Source redistribution:** Prohibited for this automation; all original and extracted source material remains local

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S5-S7 | Canonical/author metadata | Title, authors, date, version, subject, DOI, preprint status, license context. | Source identity and distribution boundary. | High | Does not validate method or results. |
| E2 | S2-S4 | Complete paper | Introduction, DCP background, prox-affine definition, compiler passes, separation graph, ADMM update, operator library, examples, table, and conclusion. | Architecture and method transcription. | High | Equations and compiler rules were not independently proved or implemented. |
| E3 | S2-S4, Figure 1 and Sections 3-4 | Paper architecture | DCP AST to prox-affine IR, separable conversion, solver/operator interface, structured linear maps. | Mechanism-of-action claims. | High | Implementation fidelity could not be checked against code. |
| E4 | S2-S4, Figures 4-6 and Table 1 | Paper experiments | Lasso, multivariate lasso, total variation, and nineteen visible benchmark rows against CVXPY+SCS/ECOS. | Source-reported speed and objective comparisons. | High for transcription | Hardware, seeds, repetitions, dispersion, and raw timing data were not disclosed in the inspected paper. |
| E5 | S2-S4, Section 5 | Paper evaluation notes | Default tolerances; moderate-accuracy Epsilon/SCS versus high-accuracy ECOS; source statement that solvers reached relative accuracy about `1e-2`. | Accuracy/runtime interpretation boundary. | Medium-high | Stopping rules were not fully matched or independently audited; some objective values differ materially. |
| E6 | S7, S8 | Author/software context | Author listing and inaccessible paper-linked repository/project locator. | Current implementation-availability assessment. | High for observed accessibility | Repository history, license, code behavior, and reproducibility remain unknown. |
| E7 | S9-S11 | Related DEP evidence | Proximal/semismooth inner solves, ADMM thresholding atoms, and convex regularizer geometry. | Cross-DEP conceptual synthesis. | Medium | Conceptual overlap does not independently validate Epsilon. |
| E8 | S12 | Private process evidence | Uniform draw, global dedup, bounded repair, integrity metrics, public-output gate. | Selection eligibility and source completeness. | High | Local identities and paths are intentionally withheld. |

## Executive Summary

The paper introduces Epsilon, an optimization compiler/runtime intended to narrow the gap between expressive disciplined convex programming and fast special-purpose solvers. Instead of canonicalizing every valid problem to cone form, the compiler transforms a DCP abstract syntax tree into a **prox-affine** intermediate representation: a sum of prox-friendly functions composed with affine maps. Additional passes expose separability while trying to minimize unnecessary variable copies. An ADMM-based solver then invokes a typed library of proximal and linear operators, including structured maps such as Kronecker products that need not be materialized as generic sparse matrices.

The core design claim is well supported by the inspected source: retaining semantic structure through the intermediate representation enables operator-specific algebra that a lower-level cone representation may erase. The numerical evidence is promising within its source-era envelope. The paper reports roughly `10x` separation from SCS on a dense lasso scaling example, about `100x` on a multivariate lasso example, `27` seconds versus `2,192` seconds at approximately `13,500` variables for the latter, and `5.7` seconds versus `123` seconds for a `10,000`-variable total-variation example. In Table 1, Epsilon is faster than SCS and ECOS on all nineteen visible problem rows for which comparisons are present.

These results are not a current solver benchmark. The paper does not disclose hardware, random seeds, repetition counts, uncertainty intervals, or raw run manifests. Epsilon and SCS use source-described moderate-accuracy defaults while ECOS is high accuracy, and implementation availability could not be verified because the paper-linked repository was inaccessible. Code and experiments were not run. The strongest durable conclusion is therefore architectural: a typed, structure-preserving optimization IR can make general-purpose modeling compatible with specialized operators. Universal speed superiority, modern production readiness, and reproducibility are not established.

## Detailed Summary

### Problem Context

General convex modeling systems let users express broad problem families but typically reduce them to standardized cone programs. That abstraction creates solver interoperability and generality, yet it can erase useful computational structure. Special-purpose solvers exploit the lost structure but demand custom derivations and implementations for each formulation.

Epsilon treats this as a compiler problem. The user keeps a DCP modeling interface, while the system targets an intermediate form closer to the operators actually needed for an efficient iterative solver. The proposed bridge has two layers:

1. a compiler that validates/transforms the expression tree while preserving recognizable atoms and affine maps; and
2. a solver runtime with concrete proximal and linear operator implementations behind a common interface.

### Prox-Affine Intermediate Representation

The paper defines prox-affine form as

`minimize_x sum_i f_i(H_i(x))`,

where each `f_i` is prox-friendly and each `H_i` is affine. An atom is usable only when the runtime has a concrete generalized proximal implementation for the function/map combination. This compatibility condition matters: a proximal operator that is cheap under an identity or diagonal map may be difficult under a general dense map.

Cone programs remain representable because linear objectives, equality indicators, and cone indicators are themselves prox-friendly atoms. Prox-affine form is thus presented as a strict computational enrichment rather than a loss of DCP expressivity.

### Compiler Passes

The compiler starts from a DCP-valid AST. A first pass recognizes linear operations and maps them to runtime linear operators. A second pass tries to match nonlinear subtrees to available proximal rules; when no direct rule exists, it falls back to a conic transformation. The resulting tree can still contain coupled terms, so a separation pass introduces variable copies and linear equality constraints.

The separation problem is represented as a bipartite graph between prox-affine terms and variables. The compiler searches for a separable form while following a stated heuristic of minimizing the number of additional variables. This is analogous to an optimizing compiler choosing a lower-level program whose semantics are equivalent but whose execution cost depends on the target operator library.

### Solver

The separated problem has a sum of per-block objectives and a shared linear equality constraint. Epsilon applies a Gauss-Seidel-style ADMM variant. Each block update is a generalized proximal operation involving the block function, its affine map, and the equality-constraint operator. The compiler is responsible for ensuring that every emitted block maps to an efficient implementation.

The high-level iteration is intentionally agnostic to operator internals. This makes the runtime extensible: adding a new operator implementation plus matching compiler rules broadens the class of problems that can avoid generic cone expansion. The paper does not, in the inspected sections, provide a comprehensive convergence treatment for every multi-block transformation emitted by the compiler; the algorithmic endpoint should therefore be validated with residuals and problem-specific checks rather than assumed from DCP validity alone.

### Fast Atomic Operators

The linear-operator layer includes generic dense/sparse matrices and structured cases such as scalar, diagonal, Kronecker, and composed maps. The proximal layer includes common losses, norms, constraints, cone projections, total variation, and specialized procedures. Factorizations can be cached when a proximal update repeatedly solves the same normal equations.

The multivariate-lasso example illustrates why the distinction matters. A cone solver's sparse-matrix representation explicitly replicates the design matrix in a Kronecker structure, while Epsilon keeps a Kronecker operator and uses dense factorization without that replication. The total-variation example similarly retains a direct dynamic-programming proximal operator instead of expanding the penalty into auxiliary linear constraints.

### Numerical Evidence

The paper integrates with CVXPY and compares Epsilon with SCS and ECOS. The detailed examples are:

- **Dense lasso:** Epsilon's dense least-squares operator/factorization is reported roughly `10x` faster than SCS over the scaling range.
- **Multivariate lasso (`k = 10`):** a structured Kronecker operator widens the source-reported gap to about `100x`; the text gives `27` seconds for Epsilon versus `2,192` seconds for SCS at approximately `13,500` variables.
- **Fused lasso/total variation:** the direct total-variation proximal operator gives `5.7` seconds versus `123` seconds for SCS at `10,000` variables.

Table 1 shows nineteen visible problems. Epsilon is fastest in every row, with examples including `0.91` seconds versus `219.63` seconds for SCS and `1,752.97` seconds for ECOS on `mnist`, and `7.14` seconds versus `824.83` seconds for SCS on `mv_lasso`. Missing ECOS results are labeled as solver failure, unsupported problem, or a one-hour timeout.

Objective values are often close but not uniformly interchangeable. For `tv_1d`, the table reports `2.29e5` for Epsilon and `2.95e5` for SCS. For `qp`, the values are `4.30e3`, `4.28e3`, and `4.24e3` for Epsilon, SCS, and ECOS. These differences reinforce the need to compare achieved residuals and optimality gaps, not time alone.

### Evidence Boundary

The paper says examples use default tolerances and that Epsilon/SCS target moderate accuracy while ECOS targets high accuracy. It reports convergence to relative accuracy around `1e-2` for the statistical applications. The benchmark description does not expose hardware, seeds, repeated trials, variance, warmup policy, factorization reuse accounting, package versions, or raw traces. The currently linked implementation was not accessible, and no experiment was reproduced.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | General DCP problems can be lowered to prox-affine form while cone programs remain expressible as a special case. | Author method claim | E2, E3 | Directly supported by definitions and transformations in the paper; implementation completeness was not audited. | High for source report |
| C2 | Preserving prox-affine structure enables specialized proximal and linear operators that conic canonicalization may hide. | Author mechanism claim | E2-E4 | Strongly supported as an architectural mechanism and by worked examples. | High |
| C3 | Epsilon is faster than SCS and ECOS on the paper's tested examples. | Author empirical claim | E4, E5 | Supported for the displayed source-era suite and settings; not a modern or universal benchmark. | Medium-high |
| C4 | Epsilon's advantages are caused solely by the prox-affine IR. | Overbroad causal claim | E4, E5 | Not established because implementations, tolerances, factorization choices, language overhead, and hardware are not isolated. | High |
| C5 | Similar objective values establish matched solution quality. | Overbroad empirical claim | E4, E5 | Not established; objective values and tolerances differ on some rows, and residual/feasibility detail is limited. | High |
| C6 | The released implementation remains available and reproduces the paper. | Availability/reproduction claim | E6 | Not supported in this review; the paper-linked repository was inaccessible and no execution occurred. | High |
| C7 | The selected paper was globally non-duplicate and source-complete before synthesis. | Process claim | E8 | Exact ID/title/slug searches were negative; the initially partial unit was repaired and verified before review. | High |
| C8 | A modern optimizer can reuse the paper's compiler/runtime separation if it adds explicit validation receipts. | Reviewer interpretation | E2, E3, E7 | Plausible engineering transfer, not a source-tested result. | Medium |

## Methodology

- `Research objective`: Preserve the paper's architecture, method, evidence, limitations, and implementation implications in a public-safe DEP-E artifact.
- `Sources inspected`: Canonical arXiv metadata, complete PDF, approved full-paper HTML fallback, TeX/source package, rendered architecture/benchmark pages, arXiv DOI/license records, author publication record, paper-linked software locator, private integrity/process evidence, and exactly three related DEP manuscripts.
- `Discovery strategy`: Required local PDF enumeration and uniform selection; repository/memory dedup; bounded source repair; local full-text and TeX inspection; PDF rendering; canonical web-source checks; implementation-locator check; conceptual DEP search.
- `Inclusion criteria`: Sources had to identify the work, expose complete method/results/limitations, establish source integrity or software status, or provide a concrete operator/optimization bridge.
- `Exclusion criteria`: Abstract-only inference, unverified secondary summaries, inaccessible implementation behavior, background DEP mentions without concrete overlap, and prohibited local source publication.
- `Analytical approach`: Empirical, conceptual, comparative, implementation, safety/operational, product, and replication analysis.
- `Evidence handling`: Source metadata, author claims, displayed empirical values, reviewer interpretation, related-DEP synthesis, and private process claims are labeled separately.
- `Uncertainty handling`: Missing hardware, seeds, repetitions, raw traces, matched-accuracy detail, current code, and independent reproduction remain explicit limitations.
- `Extraction process`: TeX and verified HTML were searched for definitions, algorithms, equations, numerical values, and conclusion; PDF pages 5 and 18-22 were rendered for visual cross-checking.
- `Version control`: arXiv v1 is the reviewed paper version. No live implementation commit could be pinned.
- `Cross-checking`: The system diagram, three scaling figures, Table 1, numerical prose, source metadata, and source-integrity metrics were compared across formats.
- `Reviewer stance`: Source-first paper report, implementation translation, and reproduction-planning artifact.

### Random Selection and Deduplication

- Required enumeration: `rg --files -g "*.pdf"`.
- PDF candidates: `75,959`.
- Unique PDF-parent units: `75,956`.
- Used arXiv base IDs in the global index: `1,581`.
- Units excluded by used ID: `460`.
- Identifier-incomplete units withheld: `185`.
- Eligible units: `75,311`.
- Uniform method: PowerShell `Get-Random` over the eligible array.
- Selected zero-based eligible index: `47,711`.
- Accepted identity: arXiv `1511.04815v1`.
- Dedup scopes: Black Lake `.logs`, `.reports`, `.lake-data`, and `.staging`; automation memory; and fetched Black-Lake-Data `.lake-data`, `.logs`, `.reports`, and `.staging`.
- Exact keys checked: arXiv ID, arXiv DOI, canonical/normalized title, archive token, and planned slugs.
- Public-safe 24-hour cutoff date: `2026-07-29`.
- Duplicate rejections/reselections: `0`; the accepted first recorded draw had no match.

### Source Integrity

- Initial state: `partial`; a valid PDF was present but verified full-paper HTML was absent.
- Repair policy: review paused; the valid PDF was preserved; one bounded strategy attempted official HTML and then used the approved ar5iv fallback; metadata HTML and the source package were also fetched.
- PDF: `534,013` bytes, `%PDF-` header, trailing `%%EOF`, and SHA-256 identity with the preserved copy.
- Full-paper HTML: `1,077,004` bytes, `88,927` stripped body characters, document marker, `62` heading markers, and four paper-structure terms.
- Metadata HTML: `40,353` bytes.
- Source package: `231,386` bytes.
- Unexpected partials: `0`.
- Companion records: local README, attribution record, machine-readable summary, and verification report updated.
- Final state: `complete`.
- Public-source gate: no PDF, HTML, metadata, source archive, extracted text, cache, render, or verification record is included in this DEP.

## Scope, Constraints, and Assumptions

- `Scope`: Paper identity, DCP/prox-affine compiler architecture, solver method, operator library, benchmark evidence, limitations, related-DEP bridges, and bounded implementation ideas.
- `Temporal boundary`: arXiv v1 and public records inspected through 2026-07-30.
- `Evidence limits`: No code inspection, execution, theorem rederivation, benchmark rerun, raw-data audit, or modern baseline comparison.
- `Assumptions`: The paper's DCP validity, prox-rule coverage, affine-map compatibility, convexity, numerical precision, and stopping assumptions travel with its claims.
- `Constraints`: Source files remain local; public claims use source-reported values; no source redistribution or local-path disclosure; examples remain synthetic/local-only.
- `Out of scope`: Production solver certification, universal performance ranking, safety-critical control, current package compatibility, and independent proof of convergence for every emitted multi-block problem.
- `Intended use`: Research preservation, optimizer architecture review, compiler/runtime prototyping, and reproduction planning.
- `Audience`: Optimization researchers, scientific-computing engineers, compiler designers, and reproducibility reviewers.
- `Reproducibility boundary`: The complete source supports a detailed plan, but the implementation and original run environment were not available for reproduction.
- `Operational boundary`: DCP validity certifies convex syntax, not numerical convergence, conditioning, feasibility tolerance, or downstream decision safety.
- `Data sensitivity`: The paper's benchmark problems are non-sensitive; any future application data must remain governed separately.

## Observations

- `Observed pattern`: The largest reported gains occur when a semantic operator prevents materialization or poor factorization of a generic matrix representation.
- `Observed pattern`: Compiler quality and operator-library coverage are coupled; a rich IR has little value if rules cannot map it to verified kernels.
- `Technical implication`: A modern implementation should record which transformation rule and kernel handled every node, including conic fallbacks.
- `Evidence-quality implication`: Benchmark speed without matched residuals, hardware, repetition, and environment manifests is insufficient for a current solver ranking.
- `Contradiction or tension`: The paper frames Epsilon as a general solver, yet its advantage depends on specialized atoms and compatibility rules; generality is delivered by extensible specialization.
- `Open question`: How much of the reported gain survives against current CVXPY canonicalization, SCS, Clarabel, OSQP, commercial solvers, JIT compilation, and GPU-aware operator runtimes?
- `Reviewer hypothesis`: An explicit IR cost model that predicts memory traffic, factorization reuse, and fallback expansion would make compiler choices more reliable than minimizing variable copies alone.

## Considerations

**Numerical correctness.** A compiler must preserve objective, constraints, domains, and scaling. Every lowering pass needs equivalence tests and a reversible provenance map from solver residuals back to user expressions.

**Convergence.** Operator compatibility is not a complete convergence certificate. Multi-block ADMM variants, ill-conditioned maps, inexact proximal updates, and poor penalty selection can stall or diverge. A runtime should expose primal/dual residuals, objective history, feasibility, termination reason, and numerical warnings.

**Benchmark governance.** Timing must separate compile time, preprocessing, factorization, repeated solves, warm starts, kernel time, and synchronization. Comparisons require matched solution-quality gates and failure accounting. Unsupported/timeout cases should not disappear from denominators.

**Extensibility risk.** Adding a kernel and compiler rule can silently expand trusted code. Each atom needs domain checks, shape/type contracts, adjoint tests for linear maps, proximal optimality tests, overflow handling, and differential comparison against a slow reference.

**Maintenance.** A structure-preserving IR becomes an interface contract. Versioned schemas, migration rules, serialized receipts, deterministic planning, and operator deprecation policies are required for durable artifacts.

**Application risk.** Optimization success does not validate the model, data, causal assumptions, or downstream decision. Safety-critical uses need domain-specific verification beyond solver receipts.

## Strengths

- Reframes general-versus-specialized optimization as a compiler intermediate-representation problem.
- Preserves user-facing DCP expressivity while exposing operator-level structure.
- Provides concrete AST conversion, fallback, separation, and solver interfaces rather than an abstract slogan.
- Treats structured linear maps as first-class operators and demonstrates why materialization can be costly.
- Connects a reusable ADMM loop to an extensible proximal/linear kernel library.
- Includes detailed lasso, multivariate-lasso, and total-variation case studies.
- Reports a broad table with time and objective values, including failures/timeouts.
- Releases source-era benchmark specifications through the stated software distribution, even though current accessibility was not established.

## Weaknesses

- No disclosed hardware, random seeds, repetition counts, variance, or raw timing traces in the inspected paper.
- Accuracy matching is described coarsely; default tolerances differ by solver.
- The source-reported suite is dated and lacks current solver/compiler baselines.
- Some table objective values differ materially, complicating direct speed comparisons.
- Compiler transformation correctness and operator kernel correctness are not independently tested here.
- The paper-linked repository and project site were inaccessible during review.
- The inspected paper does not provide a comprehensive convergence boundary for every multi-block form the compiler may emit.
- Memory consumption, compilation overhead, numerical stability, and factorization reuse are discussed unevenly.
- No independent reproduction was performed.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Add transformation certificates | Compiler correctness | Every rewrite should preserve domains and semantics. | Auditable lowering and simpler debugging. | Larger artifacts and validator complexity. | Property-based equivalence tests and reference-solver comparisons. |
| Introduce a typed operator-compatibility lattice | IR and dispatch | Function/map combinations have different valid proximal implementations. | Fewer unsafe fallbacks and clearer extension contracts. | More type/rule maintenance. | Static rule checks plus generated counterexamples. |
| Use a calibrated cost model | Optimization passes | Minimizing variable copies alone misses memory traffic and factorization reuse. | Better plan selection across hardware and shapes. | Calibration drift. | Predict-versus-measure error on held-out problems. |
| Match accuracy before timing | Benchmarking | Speed claims need common residual/feasibility/duality gates. | Fairer comparisons. | More runs and possible timeouts. | Predeclared quality thresholds and complete failure ledger. |
| Publish deterministic run manifests | Reproducibility | Hardware, versions, seeds, and warmup are missing. | Repeatable evidence and regression tracking. | Operational overhead. | Clean-machine replay and hash-checked outputs. |
| Add solver-health telemetry | Runtime | DCP validity does not ensure numerical success. | Safer deployment and easier failure triage. | Telemetry/storage burden. | Fault injection, ill-conditioning suites, and residual audits. |
| Differentially test every atom | Operator library | Specialized kernels are trusted numerical code. | Detects adjoint, shape, and proximal errors. | Reference implementations may be slow. | Randomized adjoint tests and optimality-condition checks. |
| Rebenchmark against modern solvers | Comparative evidence | Source-era baselines no longer answer current adoption questions. | Current decision usefulness. | Significant engineering effort. | Containerized multi-solver benchmark with matched gates. |

## Potential Implementations

1. **Typed prox-affine compiler.** `User`: scientific-computing engineer. `Goal`: lower a safe convex DSL to a typed operator graph. `Core mechanism`: validate DCP, apply versioned rewrite rules, retain affine-map structure, emit separability constraints, and attach rule receipts. `Required inputs`: expression AST, shape/domain metadata, operator registry, solver target. `Outputs`: typed IR, transformation receipt, fallback report, and reference problem. `Risk controls`: pure transformations, no arbitrary code execution, exact domain checks, and reference-solver differential tests. `Evaluation`: semantic-equivalence rate, fallback rate, compile time, peak memory, and residual agreement.
2. **Operator compatibility and audit registry.** `User`: numerical-runtime maintainer. `Goal`: govern function/map/kernel combinations. `Core mechanism`: register capabilities, adjoints, proximal contracts, cached factorizations, numerical limits, and test receipts for each atom. `Required inputs`: kernel implementation metadata and synthetic test generators. `Outputs`: compatibility matrix, certification status, performance envelope, and blocked combinations. `Risk controls`: quarantined experimental kernels, precision bounds, determinism checks, and mandatory slow references. `Evaluation`: randomized property-test pass rate, worst residual, regression rate, and dispatch accuracy.
3. **Matched-accuracy optimizer benchmark.** `User`: research reviewer. `Goal`: compare structure-preserving and conic lowering fairly. `Core mechanism`: generate public synthetic DCPs, run multiple solvers to common residual/feasibility thresholds, and separate compile, setup, factorization, iteration, and total time. `Required inputs`: versioned benchmark specs, containers, solver adapters, and hardware manifest. `Outputs`: complete run ledger, Pareto curves, failures, and reproducibility bundle. `Risk controls`: no private data, predeclared exclusions, timeout accounting, and no ranking when quality gates differ. `Evaluation`: replay success, variance, quality-gate agreement, time/memory, and failure coverage.

## Three Ways to Exercise This Research

1. **AST equivalence exercise.** `Objective`: test one lowering rule without building a solver. `Inputs`: three tiny synthetic DCP expressions and a slow trusted evaluator. `Method`: lower each expression to a typed prox-affine graph, sample feasible points, compare objective/domain behavior, and record the rule trace. `Output`: equivalence report with counterexamples. `Success criterion`: exact domain agreement and numerical objective agreement within a declared tolerance. `Stop condition`: any shape, domain, or value mismatch. `Safety boundary`: synthetic data and pure local evaluation only.
2. **Structured-map memory exercise.** `Objective`: quantify when a Kronecker operator beats materialization. `Inputs`: synthetic matrices over a bounded shape grid. `Method`: implement forward/adjoint calls for the symbolic map, compare against an explicitly materialized reference, and measure bytes/time under a fixed environment. `Output`: correctness and cost envelope. `Success criterion`: adjoint/reference tests pass and the symbolic representation shows a reproducible benefit in at least one predeclared regime. `Stop condition`: memory ceiling, mismatch, or unstable timing. `Safety boundary`: bounded allocation and no external data.
3. **Matched-residual solver exercise.** `Objective`: reproduce one qualitative claim without recreating the full suite. `Inputs`: a seeded synthetic lasso problem and two locally available solvers. `Method`: predeclare feasibility and objective-gap thresholds, run both solvers across repeated seeds, report setup/solve time separately, and retain every failure. `Output`: a small evidence card. `Success criterion`: both solvers pass identical quality gates and results replay from a clean manifest. `Stop condition`: quality mismatch or missing environment metadata. `Safety boundary`: no production ranking and no unbounded matrix sizes.

## Example MVP Product

- `Product name`: ProxIR Audit.
- `Target user`: Optimization compiler engineer or numerical-method reviewer.
- `Problem`: Structure-preserving rewrites and specialized kernels are difficult to trust when only the final solver result is visible.
- `Core workflow`: Import a bounded synthetic DCP expression; validate its grammar; lower it to a typed prox-affine graph; display every rule, introduced variable, equality, and conic fallback; run static compatibility checks; optionally compare objective/constraint behavior with a slow reference; export a public-safe receipt.
- `Data requirements`: Synthetic expressions, public benchmark definitions, operator metadata, and user-approved solver outputs; no sensitive data required.
- `Architecture`: Local CLI or notebook with a pure AST frontend, versioned rule engine, typed operator registry, receipt store, reference evaluator, and validator.
- `Success metrics`: Transformation equivalence pass rate, unsupported-rule clarity, dispatch correctness, receipt completeness, peak memory, and reproducible replay.
- `Risk controls`: No arbitrary expression evaluation, bounded shapes, allowlisted atoms, no network requirement, deterministic seeds, no raw private inputs in receipts, and explicit "not a convergence certificate" labeling.
- `Limitations`: Does not prove global numerical convergence, kernel stability on all hardware, model validity, or modern performance superiority.
- `MVP boundary`: One convex DSL subset, one local reference evaluator, and a small operator library; no production solver orchestration.
- `Deployment model`: Local-only CLI/notebook.
- `Evaluation plan`: Unit tests for every rule; randomized equivalence and adjoint tests; malformed-AST tests; one matched-residual lasso smoke test; receipt-schema validation.
- `Failure modes`: Incorrect domain propagation, false compatibility, floating-point mismatch, fallback explosion, hidden memory materialization, or misleading pass labels.
- `Maintenance plan`: Version rules and schemas; pin operator tests; require migration notes and fresh receipts after kernel or compiler changes.

## Related Research and Reading

| Item | Type | Relevance | Public Locator |
|---|---|---|---|
| *Epigraph projections for fast general convex programming* | Follow-up primary paper | Same authors extend structure-preserving DCP solving with epigraph projections and report order-of-magnitude gains. | https://proceedings.mlr.press/v48/wangh16.html |
| *Distributed Optimization and Statistical Learning via ADMM* | Primary methodological reference | Defines the operator-splitting foundation used by Epsilon and many compared problems. | https://web.stanford.edu/~boyd/papers/admm_distr_stats.html |
| *Proximal Algorithms* | Primary methodological reference | Provides the proximal-operator theory underlying the atomic runtime. | https://web.stanford.edu/~boyd/papers/prox_algs.html |
| *Block Splitting for Distributed Optimization* | Primary neighboring architecture | Uses graph form plus operator splitting to preserve separable structure around a linear map. | https://web.stanford.edu/~boyd/papers/block_splitting.html |
| *A Semismooth Newton Method for Fast, Generic Convex Programming* | Follow-up primary paper | Applies nonsmooth Newton acceleration to ADMM fixed-point residuals for generic conic optimization. | https://arxiv.org/abs/1705.00772 |
| Sparse SSN-PMM DEP | Related Black Lake research | Shows a different compiler-like decomposition: outer majorization plus prox-structured semismooth Newton inner solve. | `.lake-data/DEP-E/DEP-E-20260719-Sparse SSN PMM/sparse_ssn_pmm_manuscript.md` |
| CAP Rank Sparsity DEP | Related Black Lake research | Maps convex robust-PCA decomposition to singular-value and elementwise thresholding under ADMM. | `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` |
| GPMD Regularized RL DEP | Related Black Lake research | Uses a convex regularizer to generate generalized Bregman update geometry. | `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` |

## Source References

| ID | Reference | Supports | Access Date | Notes |
|---|---|---|---|---|
| R1 | https://arxiv.org/abs/1511.04815 | Identity, authors, date, version, abstract context, subjects, source locators. | 2026-07-30 | Metadata only. |
| R2 | https://arxiv.org/pdf/1511.04815 | Full method, equations, figures, table, conclusion. | 2026-07-30 | Verified local PDF withheld. |
| R3 | https://ar5iv.labs.arxiv.org/html/1511.04815 | Full-paper searchable rendering. | 2026-07-30 | Approved fallback; verified local HTML withheld. |
| R4 | https://arxiv.org/e-print/1511.04815 | TeX source for exact equations, table values, captions, and conclusion. | 2026-07-30 | Local source package withheld. |
| R5 | https://doi.org/10.48550/arXiv.1511.04815 | Persistent identity. | 2026-07-30 | arXiv-issued DOI. |
| R6 | https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html | Visible arXiv distribution-license context. | 2026-07-30 | Not treated as source-upload authorization. |
| R7 | https://zicokolter.com/publications/ | Author publication status and Epsilon software link. | 2026-07-30 | Author-maintained record. |
| R8 | https://github.com/mwytock/epsilon | Paper-linked implementation locator. | 2026-07-30 | Inaccessible; no code evidence derived. |
| R9 | https://proceedings.mlr.press/v48/wangh16.html | Author follow-up on epigraph projections. | 2026-07-30 | Primary proceedings record. |
| R10 | https://web.stanford.edu/~boyd/papers/admm_distr_stats.html | ADMM methodological context. | 2026-07-30 | Primary author-hosted record. |
| R11 | https://web.stanford.edu/~boyd/papers/prox_algs.html | Proximal-method context. | 2026-07-30 | Primary author-hosted record. |
| R12 | https://web.stanford.edu/~boyd/papers/block_splitting.html | Graph-form/operator-splitting neighbor. | 2026-07-30 | Primary author-hosted record. |
| R13 | https://arxiv.org/abs/1705.00772 | Semismooth Newton follow-up context. | 2026-07-30 | Primary arXiv record. |
| R14 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-Sparse%20SSN%20PMM/sparse_ssn_pmm_manuscript.md | Related proximal/semismooth solver synthesis. | 2026-07-30 | Related DEP only. |
| R15 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260719-CAP%20Rank%20Sparsity/cap_rank_sparsity_manuscript.md | Related ADMM/thresholding synthesis. | 2026-07-30 | Related DEP only. |
| R16 | https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-GPMD%20Regularized%20RL/gpmd_regularized_rl_manuscript.md | Related regularizer-geometry synthesis. | 2026-07-30 | Related DEP only. |

## Appendix

### A. Reproduction Checklist

- [ ] Recover or reimplement a version-pinned Epsilon-compatible runtime.
- [ ] Record OS, CPU/GPU, BLAS/LAPACK, compiler, Python, CVXPY, solver versions, threading, and precision.
- [ ] Reconstruct the nineteen displayed benchmark rows plus detailed scaling cases from immutable specifications.
- [ ] Pin random seeds and publish generated-data hashes.
- [ ] Separate parse, canonicalization, compile, setup, factorization, iteration, and total time.
- [ ] Predeclare primal/dual residual, feasibility, objective-gap, and timeout gates.
- [ ] Run repeated trials and report dispersion, not minimum time only.
- [ ] Measure peak memory and any matrix materialization.
- [ ] Compare against current structure-aware and conic solvers.
- [ ] Preserve unsupported, timeout, numerical-error, and quality-gate failures.
- [ ] Differentially validate emitted problems against a trusted reference.
- [ ] Publish a manifest and source-safe derived results only.

### B. Decision Boundary

This artifact supports investigating typed structure-preserving optimization compilers. It does not support selecting Epsilon for current production use, claiming universal performance superiority, or treating successful DCP parsing as a numerical certificate.

### C. Source Locality

The complete PDF, full-paper HTML, metadata HTML, TeX/source package, extracted material, validation records, and rendered pages remain in the private local archive. No `.source/` directory was created and no original source file is included in this repository deposit.
