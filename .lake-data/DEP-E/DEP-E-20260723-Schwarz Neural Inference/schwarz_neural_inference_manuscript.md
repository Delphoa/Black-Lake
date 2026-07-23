---
title: "Schwarz Neural Inference - DEP-E"
generated_at: "2026-07-23"
artifact_type: "DEP research artifact"
primary_subject: "Source-grounded review of local neural operators combined with additive Schwarz domain decomposition for geometry-general PDE solving."
source_status: "verified local PDF, full-paper HTML, and source package inspected; source files withheld"
reviewer: "Codex"
schema_version: "2026-07-07-expanded"
source_access_date: "2026-07-23"
temporal_cutoff: "arXiv v2 revised 2026-02-27; ICLR 2026 and official repository evidence inspected through 2026-07-23"
primary_url: "https://arxiv.org/abs/2504.00510"
stable_identifier: "arXiv:2504.00510v2; DOI 10.48550/arXiv.2504.00510"
confidence_summary: "High for source identity, method, tables, runtime, and code availability; medium for cross-format interpretation; low for independent convergence or empirical verification because neither proof nor experiments were reproduced."
safety_scope: "non-sensitive scientific-computing research and evaluation"
distribution_notes: "Public URLs and repository-relative paths only; paper files and processing infrastructure remain local."
---

# Schwarz Neural Inference - DEP-E

## Source Metadata

| ID | Source | Role | Type | Identifier / Version | Public Locator | License / Usage Notes | Access Date | Status |
|---|---|---|---|---|---|---|---|---|
| S1 | arXiv record | Primary metadata | HTML | arXiv:2504.00510v2 | https://arxiv.org/abs/2504.00510v2 | Record links CC BY 4.0; metadata and source endpoints inspected. | 2026-07-23 | Inspected |
| S2 | Complete paper | Primary research | PDF and full-paper HTML | arXiv:2504.00510v2 / ICLR 2026 | https://arxiv.org/pdf/2504.00510 ; https://arxiv.org/html/2504.00510 | Verified complete locally; files not redistributed. | 2026-07-23 | Inspected |
| S3 | TeX/source package | Primary research source | Source archive | arXiv:2504.00510v2 | https://arxiv.org/e-print/2504.00510 | Verified locally; files not redistributed. | 2026-07-23 | Inspected |
| S4 | ICLR 2026 poster page | Official venue record | HTML | ICLR 2026 Poster | https://iclr.cc/virtual/2026/poster/10010246 | Official public conference record. | 2026-07-23 | Inspected |
| S5 | SNI repository | Official implementation | GitHub repository | observed head 5fed406a0fefc67af3f9a670150acac0ffbefa5a | https://github.com/questionstorer/sni | Public code; no source copied into this DEP and no execution performed. | 2026-07-23 | README and selected code inspected |
| S6 | Physical Data AI | Related DEP | Markdown | DEP-E-20260710 | `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md` | Processed Black Lake artifact. | 2026-07-23 | Inspected |
| S7 | Global NS Existence | Related DEP | Markdown | DEP-E-20260712 | `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md` | Processed Black Lake artifact. | 2026-07-23 | Inspected |
| S8 | FGLE Midpoint Scheme | Related DEP | Markdown | DEP-E-20260716 | `.lake-data/DEP-E/DEP-E-20260716-FGLE Midpoint Scheme/fgle_midpoint_scheme_manuscript.md` | Processed Black Lake artifact. | 2026-07-23 | Inspected |

The authors are Jianing Huang, Kaixuan Zhang, Youjia Wu, and Ze Cheng. arXiv records initial submission on 2025-04-01 and revision on 2026-02-27. The official conference record lists the work as an ICLR 2026 Poster. The paper and official repository identify Corporate Research, Bosch (China) Investment Co., Ltd. as the authors' organization.

## Evidence Ledger

| ID | Source | Source Type | Evidence Used | Supports | Confidence | Limitations |
|---|---|---|---|---|---|---|
| E1 | S1, S4 | Official metadata | Title, authors, dates, DOI, subjects, venue, license link, and public endpoints. | Source identity and publication status. | High | Metadata does not validate method or results. |
| E2 | S2, Sections 1-4 | Primary paper | Problem framing, random-polygon training data, GNOT local operator, METIS overlap, normalization, SNI update, equations, and Algorithm 1. | Method reconstruction. | High | No implementation execution. |
| E3 | S2, Table 1 and Figures 2-4 | Primary paper | Main relative-error results, three test domains, training-data curves, partition/depth/step behavior, and data-augmentation ablation. | Geometry-transfer and ablation claims. | High for source reporting | Three designed domains and source-generated datasets limit external validity. |
| E4 | S2, theorem and proof appendix | Primary paper | Contractive classical map, uniform local error, overlap factor, tracking bound, and claimed convergence. | Theory report and reviewer proof analysis. | High for transcription | Proof was not formally checked; reviewer identifies a non-vanishing Cauchy bound. |
| E5 | S2, runtime appendix Tables 4-5 | Primary paper | SNI time-to-convergence, FEM and GNOT reference times, initialization improvement, and non-parallelized implementation note. | Cost and deployment interpretation. | High for source reporting | Single-sample timings, limited hardware context, and unmatched implementations. |
| E6 | S2, appendices H-I | Primary paper | Dataset sizes, hyperparameters, one V100, evaluation formula, extra domains, architecture comparison, discussion, and broader impacts. | Reproducibility and limitation review. | High | No independent rerun or data audit. |
| E7 | S5 | Official code | Two-environment setup, data generation, training, inference, meshes, metrics, stopping logic, and dataset download instructions. | Code availability and implementation surface. | Medium-high | Observed head postdates paper; no tagged paper release or execution inspected. |
| E8 | Public-safe cache summary | Process evidence | Cache miss to cached; `pypdf`, HTML, and source extraction; text sizes and fallback reason. | Extraction provenance. | High | Private paths and exact local timestamps withheld. |
| E9 | Selection and dedup checks | Process evidence | Uniform draw, identifier/title/slug searches, memory, recent branches, and companion inventory classification. | Eligibility. | High | Process evidence does not validate research claims. |
| E10 | S6-S8 | Related DEP artifacts | PDE-prior fit, theorem/boundary assumptions, numerical convergence, solver realization, reference error, and runtime. | Cross-DEP synthesis. | Medium | Related artifacts do not validate this paper. |

## Executive Summary

The paper proposes a local-to-global route for geometry-general neural PDE solving. A neural operator is trained on random simple polygons rather than on every target geometry. At inference, an unseen domain is partitioned into overlapping subdomains, the local operator predicts each subproblem, and Schwarz Neural Inference iteratively patches the predictions into a global solution.

The empirical result is substantial on the paper's constructed tasks. Across 15 cells covering five PDE settings and three domains, SNI reports lower relative `l2` error than direct GNOT. Laplace2d-Dirichlet falls from `22-28%` to roughly `2.1-2.2%`; Darcy domain C falls from `167+/-8%` to `5.4+/-0.6%`. This supports the narrower claim that the domain-decomposition wrapper improves the tested local operator's transfer to those geometries.

The paper does not show speed advantage at the tested scale. Its appendix reports zero-initialized SNI time-to-convergence of 26-714 seconds for nine stationary cases. On one Laplace reference, FEM is reported at `6.15e-4` seconds, direct GNOT at `1.26e-2` seconds, and SNI at 100 seconds; GNOT initialization reduces SNI to 28 seconds. The authors appropriately describe larger and more complex domains as a future regime where advantage may emerge.

The theory is also narrower than the headline. The assumptions yield a useful uniform bound between learned and classical iterates. The displayed proof of learned-iterate convergence is incomplete because a fixed `2c'` term remains in its Cauchy estimate. The reviewer therefore treats convergence as an author claim requiring repair, not as established by the inspected argument.

## Detailed Summary

### Problem

Neural operators learn mappings between input functions and PDE solutions. Existing geometry-aware designs can accept irregular meshes, yet a model trained on one geometry distribution can still fail on topologically or geometrically different domains. Generating full solutions for every new target geometry reproduces the expense that learned solvers are meant to avoid.

### Training Data Generation

The framework defines a space of local building blocks. In the two-dimensional implementation these are simple polygons with 3-12 vertices, bounded by a compact region. FEniCSx generates local solutions with random boundary conditions, coefficient fields, source terms, or initial conditions. PDE symmetries provide rotation, translation, scaling, and value transforms where valid.

The main local model is GNOT with one expert and three layers of width 128. Training uses Adam, a cyclic learning-rate strategy with maximum `0.001`, and equation-specific epochs. The goal is not to invent a new neural-operator architecture but to learn accurate local solution operators over the building-block family.

### Schwarz Neural Inference

Given a target triangulation, METIS creates `K` connected partitions. Each partition is expanded by an overlap depth `d`. On every iteration, SNI:

1. forms local boundary and input functions from global data and the previous iterate;
2. maps geometry and function values into the training range with PDE-specific symmetries;
3. evaluates the frozen local neural operator;
4. inverts the transforms and restricts/extends local predictions;
5. updates the global solution with relaxation step `tau`.

The main algorithm resembles additive Schwarz Richardson iteration with the exact local solver replaced by a learned, pre/post-processed operator.

### Theoretical Claim and Gap

The theorem assumes:

- the exact classical iteration map is contractive with `0 < rho < 1`;
- each learned local solver differs uniformly from the exact local solver by at most `c`;
- each degree of freedom belongs to at most `t` subdomains.

It derives the recurrence

`||e^(n+1)|| <= rho ||e^n|| + tau*t*c`

and therefore the uniform bound

`||e^n|| <= tau*t*c/(1-rho) = c'`.

That tracking bound is useful. The subsequent convergence step is not. The proof bounds the distance between two learned iterates by the distance between two classical iterates plus `2c'`. As the classical term vanishes, the bound tends to `2c'`, not zero. This does not prove the learned sequence is Cauchy. Convergence might follow from stronger assumptions on the learned map, a decaying local error, or a different perturbation argument, but those are not supplied in the displayed proof.

### Experimental Design

The main evaluation uses three global domains:

- A: a simply connected disk-rectangle union;
- B: a square with two holes;
- C: a disk-like region with a complex interior cutout.

The five PDE settings are Laplace2d-Dirichlet, Laplace2d-Mixed, Darcy2d, Heat2d, and NonlinearLaplace2d. Most test sets contain 100 random conditions; Heat2d uses 10. The metric is mean relative `l2` error. Source-generated FEniCSx solutions provide ground truth.

### Main Results

| PDE | Domain | Direct GNOT | SNI |
|---|---|---:|---:|
| Laplace2d-Dirichlet | A / B / C | `22+/-2`, `22+/-2`, `28+/-3` | `2.2+/-0.6`, `2.1+/-0.4`, `2.1+/-0.9` |
| Laplace2d-Mixed | A / B / C | `10.7+/-0.8`, `10.7+/-0.8`, `38+/-6` | `6+/-4`, `7+/-1`, `6+/-1` |
| Darcy2d | A / B / C | `16+/-1`, `63+/-3`, `167+/-8` | `8+/-2`, `8+/-2`, `5.4+/-0.6` |
| Heat2d | A / B / C | `11.5+/-0.6`, `30+/-10`, `20+/-10` | `5.3+/-0.2`, `11+/-2`, `5.8+/-0.3` |
| NonlinearLaplace2d | A / B / C | `22+/-2`, `26+/-2`, `28+/-2` | `2.0+/-0.4`, `2.2+/-0.4`, `2.2+/-0.5` |

The result is consistently favorable to SNI within this table. The most dramatic direct-GNOT failures occur on geometries furthest from the simple-polygon training distribution. The paper also reports a dolphin-shaped domain at `4.5+/-0.9%` versus `2.1+/-0.5%` on a disk, showing some degradation on a harder shape.

### Ablations and Runtime

Increasing partitions can reduce final error but slows convergence. Overlap depths 1, 2, 4, and 8 produce nearly identical curves in the displayed Laplace case. Larger `tau` accelerates convergence up to the paper's stated stability limit. Rotation augmentation is consistently useful; scaling can help or hurt depending on its range and domain.

Runtime is the clearest operational limitation. The current implementation is iterative and not fully parallelized. It can require thousands of steps and tens to hundreds of seconds on the paper's small domains. Better initialization helps materially but does not establish an advantage over classical solvers. Any product claim should therefore separate geometry-transfer accuracy from speed.

### Official Implementation

The official repository provides:

- separate FEM-data and neural-PDE conda environments;
- scripts for training and evaluation data generation;
- GNOT and Geo-FNO local operators;
- mesh/domain-decomposition utilities;
- training and inference entry points;
- Hugging Face dataset instructions;
- fixed-point and metric logging in the observed inference implementation.

The observed default-branch head is dated after the paper revision. Without a tagged paper release and executed reproduction, the repository is availability evidence, not proof that the reviewed commit regenerates the printed results.

## Key Claims and Evidence

| Claim ID | Claim | Claim Type | Evidence | Reviewer Assessment | Confidence |
|---|---|---|---|---|---|
| C1 | Training on local basic shapes plus SNI enables geometry transfer without generating target-domain training solutions. | Author method claim | E2 | Mechanism is clearly specified and implemented in the released project. | High |
| C2 | SNI lowers relative error against direct GNOT across all 15 main-table cells. | Author empirical claim | E3 | Supported by Table 1; not independently reproduced. | High for source report |
| C3 | The method is data efficient. | Author empirical claim | E3, E6 | Training-size curves favor SNI, but evidence is limited to source-generated tasks and a single local-operator family. | Medium |
| C4 | SNI converges under the theorem assumptions. | Author theorem claim | E4 | The inspected proof does not establish the learned iterates are Cauchy because its bound retains `2c'`. | Low for independent validity |
| C5 | The theorem supplies a uniform learned-versus-classical error bound. | Author theorem claim | E4 | The displayed recurrence supports the bound if its assumptions and norm inequalities hold. | Medium-high |
| C6 | SNI may become faster than classical solvers on large complicated domains. | Author future hypothesis | E5 | Not demonstrated; tested cases strongly favor FEM and direct GNOT in runtime. | Low |
| C7 | The official repository enables immediate reproducibility. | Availability implication | E7 | It materially improves inspectability, but an untagged post-paper head is not an immutable reproduction package. | Medium-low |
| C8 | Learned PDE solvers need joint physical-fit, theorem-scope, numerical-residual, and matched-cost evidence. | Reviewer synthesis | E4-E10 | Strongly motivated across the selected and related artifacts. | Medium-high |

## Methodology

- `Research objective`: Select one eligible local arXiv unit uniformly, enforce complete-source integrity, extract it through the central cache, review it source-first, connect it to exactly three related deposits, and create a schema-complete public DEP-E artifact.
- `Sources inspected`: Verified complete paper PDF, official full-paper HTML, TeX/source package, arXiv metadata, ICLR venue record, official implementation repository, live Black Lake and Black-Lake-Data repository rules, and exactly three related DEP manuscripts.
- `Discovery strategy`: Enumerated PDFs with `rg --files -g "*.pdf"`, collapsed paths to parent paper units, drew a uniform PowerShell `Get-Random` index, derived the arXiv ID from nearby metadata, and searched required dedup surfaces before acceptance.
- `Inclusion criteria`: Primary material supporting identity, method, theorem, result, runtime, limitation, code, repository policy, extraction provenance, or concrete related-entry overlap.
- `Exclusion criteria`: Abstract-only synthesis, generic topical matches, uninspected recommender links, and local-only source paths. Source files were never placed in the public DEP.
- `Analytical approach`: Empirical, conceptual, comparative, numerical-analysis, implementation, product-research, replication, and provenance review.
- `Evidence handling`: Author claims, printed evidence, reviewer arithmetic, proof analysis, code observations, and cross-DEP inference are labeled separately.
- `Uncertainty handling`: Unreproduced experiments, unverified proof transitions, code-version drift, limited geometry coverage, and runtime comparability remain explicit.
- `Extraction process`: Extractor preflight found `pypdf` but not `pdftotext`. `extract-arxiv` ran in `missing-only` mode against the verified local unit and produced PDF, HTML, and source text with no network access during extraction.
- `Version control`: Primary paper pinned to arXiv v2; implementation observations pinned to observed default-branch head `5fed406a0fefc67af3f9a670150acac0ffbefa5a`.
- `Claim selection`: Priority went to the local-to-global mechanism, main table, theorem assumptions, proof transition, runtime appendix, geometry scope, and reproducibility.
- `Cross-checking`: Identity and dates were checked across arXiv and ICLR; method and results across PDF, HTML, and TeX; selected tables and figures visually rendered; code claims checked against repository README and selected files.
- `Safety handling`: Implementation examples are monitoring and evaluation oriented; no harmful or sensitive operation is involved.
- `Reviewer stance`: Skeptical paper report, proof audit, numerical evidence review, implementation translation, and DEP-ready preservation.
- `Random selection methodology`: 75,780 PDFs collapsed to 75,777 unique parent units; uniform zero-based draw 57,700; first draw accepted; exclusions and reselections zero.
- `Cache methodology`: Initial cache miss; verified local sources populated a cached record in 0.860 seconds with `pypdf`, HTML regex, and `tarfile`.
- `Deduplication and reselection validation`: No arXiv ID, DOI, normalized-title, slug, prior-artifact, memory, recent-branch, or 24-hour collision. A companion inventory row was metadata only.

## Scope, Constraints, and Assumptions

- `Scope`: The paper's two-dimensional local-to-global operator-learning framework, heat space-time extension, main empirical evidence, theorem, proof, runtime, official code, and three cross-DEP bridges.
- `Temporal boundary`: arXiv v2, ICLR 2026 record, and implementation evidence visible through 2026-07-23.
- `Evidence limits`: No proof assistant, expert referee, data regeneration, training, inference, metric recomputation, or matched solver benchmark.
- `Assumptions`: The verified local paper corresponds to arXiv v2 and the official implementation repository is author-controlled.
- `Constraints`: Public artifacts omit local paths, usernames, machine identifiers, exact local timestamps, timezone labels, source files, and extracted text.
- `Out of scope`: Certifying the theorem, reproducing tables, validating industrial-scale advantage, or extending SNI to Navier-Stokes, three-dimensional production meshes, or non-overlapping DDMs.
- `Intended use`: Research deposition, replication planning, proof review, benchmark design, and guarded implementation prototyping.
- `Audience`: Scientific-ML researchers, numerical analysts, PDE engineers, benchmark maintainers, and product teams evaluating learned solvers.
- `Reproducibility boundary`: Public sources and code enable a reproduction attempt, but this artifact does not certify results or paper-code parity.
- `Operational boundary`: The manuscript discusses evaluation and monitoring, not safety-critical simulation deployment.
- `Data sensitivity`: Public scholarly sources, public code, and synthetic PDE data descriptions.

## Observations

1. The largest error gains occur where direct GNOT is most out of distribution, supporting decomposition as a geometry-transfer mechanism.
2. SNI's iterative correction trades much higher inference cost for lower error in the tested cases.
3. Better initialization is both a speed improvement and an extra dependency on the direct model being useful.
4. The theorem's uniform tracking bound is meaningful even though its convergence step is incomplete.
5. The empirical nonlinear and space-time extensions sit outside the theorem's stated self-adjoint coercive elliptic scope.
6. Three designed domains do not characterize a geometry-general operating envelope.
7. A current public repository improves auditability but version drift weakens direct paper reproducibility.

## Considerations

A deployment should define a validated equation/domain envelope before accepting results. Inputs need mesh-quality checks, boundary-condition validation, subdomain-shape shift scores, coefficient-range checks, and symmetry-transform provenance. The iteration needs interface residuals, update norms, fixed-point residuals, stagnation detection, divergence detection, and a deterministic fallback.

Evaluation must be matched on accuracy, not only wall time. Classical FEM, optimized Schwarz, direct neural operators, and hybrid methods should use the same meshes, tolerances, hardware, parallel budget, and setup accounting. Training-data generation and amortization should be reported separately from per-query inference.

Proof claims should be versioned like code. The exact theorem assumptions, norm, local error definition, overlap factor, relaxation range, and repaired convergence argument should be linked to tests that falsify violations. Empirical success beyond theorem scope should be labeled empirical rather than implied by the theorem.

## Strengths

1. The local-to-global mechanism is conceptually clear and grounded in established domain-decomposition practice.
2. The main result table shows a consistent and sometimes dramatic accuracy advantage over direct GNOT.
3. The paper tests multiple PDE types, boundary conditions, a time-dependent extension, data size, augmentation, architecture, and partition hyperparameters.
4. Appendix hyperparameters and runtime evidence materially improve interpretability.
5. The authors explicitly acknowledge that tested classical solvers are faster and frame large-domain advantage as future work.
6. Public code and data instructions make the work substantially more inspectable than a paper-only release.

## Weaknesses

1. The convergence proof's Cauchy step is invalid as written because its upper bound retains a non-vanishing constant.
2. Geometry generalization is evaluated on a small designed set rather than a distribution with topology, scale, mesh, and boundary variation.
3. Runtime is orders of magnitude worse than the reported FEM and direct-GNOT references on the highlighted small case.
4. The theorem does not cover all empirical PDE settings.
5. Hyperparameter choice and initialization remain problem- and domain-dependent.
6. The official code head postdates the paper, and no inspected tagged release binds code, data, checkpoints, and tables.
7. The review found no independent reproduction, uncertainty calibration beyond reported standard deviations, or industrial-scale benchmark.

## Potential Improvements

| Improvement | Target Area | Rationale | Expected Benefit | Cost / Risk | Validation Approach |
|---|---|---|---|---|---|
| Repair the convergence theorem | Theory | Uniform tracking is not convergence | Correct scope and stronger trust | May require stronger assumptions | Independent proof review and counterexample search |
| Build a geometry-distribution benchmark | External validity | Three domains cannot define broad generalization | Measurable operating envelope | Large data-generation cost | Predefined topology/scale/mesh/boundary splits |
| Add optimized classical DDM baselines | Comparative evidence | Direct GNOT is not the only relevant baseline | Fairer attribution to learned local solves | Engineering burden | Matched-error, matched-parallelism benchmark |
| Parallelize and profile every phase | Systems | Current runtime hides partition, normalization, communication, and local inference | Actionable performance model | Hardware-specific complexity | Per-phase traces and scaling curves |
| Release an immutable reproduction bundle | Reproducibility | Moving main branch weakens paper parity | Repeatable tables and code audit | Maintenance and storage | Tagged release, hashes, CI, and table regression |
| Add online reliability diagnostics | Deployment | Ground truth is absent in real use | Safe fallback and auditable solves | Proxy residuals may miscalibrate | Held-out failure injection and coverage tests |

## Potential Implementations

1. **Geometry-transfer evaluation service**
   - `User`: Scientific-ML benchmark maintainer.
   - `Goal`: Compare learned and classical PDE solvers across unseen geometry families.
   - `Core mechanism`: Versioned meshes, boundary conditions, matched-error budgets, solver adapters, and evidence reports.
   - `Required inputs`: PDE definitions, geometry split, truth solver, method configs, hardware record, and seeds.
   - `Outputs`: Error, runtime, memory, convergence, residual, and failure-boundary tables.
   - `Risk controls`: No production claim from synthetic-only results; immutable configurations and independent review.
   - `Evaluation`: Regression fixtures plus held-out geometry/topology suites.

2. **Learned-Schwarz reliability monitor**
   - `User`: PDE platform engineer.
   - `Goal`: Detect stagnation, divergence, or subdomain distribution shift during inference.
   - `Core mechanism`: Interface residuals, fixed-point residuals, update norms, partition telemetry, and fallback routing.
   - `Required inputs`: Iterates, local predictions, mesh partitions, training-envelope statistics, and tolerances.
   - `Outputs`: Solve status, evidence ledger, alerts, and classical-solver fallback request.
   - `Risk controls`: Conservative no-result state; no silent acceptance after stagnation.
   - `Evaluation`: Inject bad meshes, out-of-range boundaries, poor initialization, and unstable relaxation.

3. **PDE method evidence card**
   - `User`: Research reviewer or release manager.
   - `Goal`: Keep theorem, experiment, code, and deployment claims aligned.
   - `Core mechanism`: Schema linking equation scope, assumptions, datasets, code hashes, checkpoints, metrics, costs, and unresolved gaps.
   - `Required inputs`: Manuscript claims, source tables, repository revision, environment, and benchmark outputs.
   - `Outputs`: Reviewable release card and blocking inconsistencies.
   - `Risk controls`: Author/reviewer role separation and explicit unsupported-claim status.
   - `Evaluation`: Seed with known theorem/code/table mismatches and require correct rejection.

## Three Ways to Exercise This Research

1. **Reproduce one complete Laplace case:** Objective - verify the full data-generation, training, direct-inference, and SNI chain; inputs - pinned Laplace2d data, mesh A, checkpoint, environment, and seeds; method - regenerate truth, run both models, log every residual and phase; output - Table 1 row plus runtime ledger; success criterion - printed values fall within a predeclared tolerance; stop condition - paper/code configuration cannot be reconciled.
2. **Run a geometry-shift ladder:** Objective - locate the generalization boundary; inputs - controlled changes in topology, scale, aspect ratio, holes, mesh density, boundary segmentation, and coefficient range; method - vary one dimension and selected interactions; output - error/residual/iteration surfaces; success criterion - a stable accepted envelope and reliable rejection outside it; stop condition - truth-solver or mesh-quality checks fail.
3. **Audit the convergence claim:** Objective - determine sufficient conditions for learned-iterate convergence; inputs - theorem source, synthetic contractive maps, bounded perturbations, and candidate counterexamples; method - formalize the recurrence, test non-vanishing perturbations, and prove a corrected statement; output - repaired theorem or counterexample; success criterion - every transition is independently checkable; stop condition - assumptions cannot be connected to the implemented operator.

## Example MVP Product

- `Product name`: SchwarzScope.
- `Target user`: Scientific-computing team evaluating a learned local solver in a non-safety-critical research environment.
- `Problem`: A learned PDE solver can appear accurate on selected geometries while hiding partition shift, iterative instability, unmatched cost, or theorem-scope violations.
- `Core workflow`: Register a PDE and evidence card; import a geometry split and truth-solver adapter; run direct, SNI, FEM, and classical-DDM baselines; collect residual and resource traces; gate results against equation, geometry, error, and stability criteria; export a public-safe report.
- `Data requirements`: Public or authorized meshes, boundary and coefficient functions, versioned truth solutions, training-envelope statistics, code/config hashes, hardware metadata, and seeds.
- `Architecture`: Local batch runner; solver adapters; geometry profiler; iteration telemetry collector; matched-error comparator; evidence-card store; review dashboard.
- `Success metrics`: Reproduces one printed case; detects seeded stagnation/divergence; rejects out-of-envelope geometries; reports matched-error cost without missing setup phases; preserves complete revision provenance.
- `Risk controls`: Research-only labeling, deterministic no-result state, classical fallback, no silent tolerance relaxation, immutable run bundles, and human review.
- `Limitations`: No guarantee of proof correctness, industrial-scale benefit, safety-critical validity, or transfer beyond tested PDEs.
- `MVP boundary`: Laplace2d-Dirichlet only, domains A-C plus a small held-out geometry ladder, one GNOT checkpoint, one FEM reference, and offline execution.
- `Deployment model`: Local CLI plus static review dashboard.
- `Evaluation plan`: Unit tests for residual math, synthetic fixed-point fixtures, one source reproduction, geometry-shift tests, and independent result review.
- `Failure modes`: Invalid mesh, boundary mismatch, checkpoint/config drift, stalled iteration, false residual confidence, unfair baseline settings, and missing ground truth.
- `Maintenance plan`: Pin solver dependencies, meshes, checkpoints, environments, schema version, and expected regression outputs.

## Related Research and Reading

| Item | Type | Relevance | URL / DOI / Identifier |
|---|---|---|---|
| Physical Data AI | Related Black Lake research artifact | PDE-informed representation and the domain-fit boundary for physical priors. | `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md`; https://arxiv.org/abs/2407.14504 |
| Global NS Existence | Related Black Lake research artifact | PDE geometry, boundary assumptions, theorem dependency, and a named out-of-scope equation family. | `.lake-data/DEP-E/DEP-E-20260712-Global NS Existence/global_ns_existence_manuscript.md`; https://arxiv.org/abs/2102.09229 |
| FGLE Midpoint Scheme | Related Black Lake research artifact | Numerical convergence, solver realization, independent reference error, and runtime discipline. | `.lake-data/DEP-E/DEP-E-20260716-FGLE Midpoint Scheme/fgle_midpoint_scheme_manuscript.md`; https://arxiv.org/abs/1601.02301 |
| GNOT | Primary methodological neighbor | Main local neural-operator architecture used by SNI. | https://arxiv.org/abs/2209.15571 |
| Domain Decomposition Methods | Foundational method | Classical additive Schwarz framework that motivates SNI. | https://doi.org/10.1007/978-3-540-27266-8 |
| Lie Point Symmetry Data Augmentation | Methodological neighbor | Symmetry-based augmentation and normalization used in local operator training/inference. | https://arxiv.org/abs/2203.03613 |

## Source References

1. Jianing Huang, Kaixuan Zhang, Youjia Wu, and Ze Cheng. *Operator Learning with Domain Decomposition for Geometry Generalization in PDE Solving*. ICLR 2026. [arXiv](https://arxiv.org/abs/2504.00510) - [PDF](https://arxiv.org/pdf/2504.00510) - [HTML](https://arxiv.org/html/2504.00510) - [source](https://arxiv.org/e-print/2504.00510) - [DOI](https://doi.org/10.48550/arXiv.2504.00510).
2. [Official ICLR 2026 poster record](https://iclr.cc/virtual/2026/poster/10010246), supporting venue, authors, and presentation status.
3. [Official SNI repository](https://github.com/questionstorer/sni) at observed head [`5fed406a0fefc67af3f9a670150acac0ffbefa5a`](https://github.com/questionstorer/sni/commit/5fed406a0fefc67af3f9a670150acac0ffbefa5a), supporting implementation availability and project structure.
4. Exactly three related Black Lake manuscripts listed above, used for contextual synthesis rather than validation of the selected paper.

## Appendix

### Source-Integrity and Processing Record

- Initial source classification: partial.
- Final source classification: complete.
- PDF: 3,294,807 bytes; header and EOF checks passed.
- Full-paper HTML: 497,212 bytes; 95,618 body characters; document marker, 79 headings, and eight structure terms.
- Source archive: 78 entries including `main.tex`.
- Cache: miss to cached; PDF, HTML, and source text all present.
- Selection: index 57,700 of 75,777 unique paper units; no reselection.
- Distribution: source documents, caches, and local provenance withheld; no `.source/` directory.

### Replication Checklist

- Pin the paper version and official code revision.
- Preserve environment files, dependency resolution, data manifests, meshes, and checkpoints.
- Recreate one training dataset and one held-out geometry with FEniCSx.
- Reproduce direct GNOT and SNI errors with the paper's seeds and tolerances.
- Log partitioning, normalization, initialization, per-iteration residuals, stop reason, runtime, memory, and hardware.
- Add optimized FEM and classical Schwarz baselines at matched error.
- Validate the corrected convergence claim separately from empirical success.

## Attribution Block

Primary research is attributed to Jianing Huang, Kaixuan Zhang, Youjia Wu, and Ze Cheng. Public locators are [arXiv:2504.00510](https://arxiv.org/abs/2504.00510), [DOI:10.48550/arXiv.2504.00510](https://doi.org/10.48550/arXiv.2504.00510), the [ICLR 2026 poster record](https://iclr.cc/virtual/2026/poster/10010246), and the [official implementation](https://github.com/questionstorer/sni). This manuscript is an independent review. Source files were retained locally under their original terms and were not uploaded or redistributed.
